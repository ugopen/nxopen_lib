from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
class AngleFormat(Enum):
    """
    Members Include: 
     |FractionalDegrees|  Fractional degrees format, e.g. 30.55 degrees 
     |DegreesMinutes|  Degrees minutes format, e.g. 30 degrees 30" 
     |DegreesMinutesSeconds|  Degrees minutes seconds format, e.g. 30 degrees 30"30' 
     |WholeDegrees|  Whole degrees only, e.g. 30 degrees 

    """
    FractionalDegrees: int
    DegreesMinutes: int
    DegreesMinutesSeconds: int
    WholeDegrees: int
    @staticmethod
    def ValueOf(value: int) -> AngleFormat:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class AnnotationPreferences(NXOpen.Object): 
    """ Represents the global preferences for annotations """
    def GetAngularTolerances(self) -> AngularTolerance:
        """
         Returns the global angular tolerances for the part 
         Returns prefs ( AngularTolerance NXOpen.A):  .
        """
        pass
    def GetDimensionPreferences(self) -> DimensionPreferences:
        """
         Returns the global dimension preferences for the part 
         Returns prefs ( DimensionPreferences NXOpen.A):  .
        """
        pass
    def GetFrameBarPreferences(self) -> FrameBarPreferences:
        """
         Returns the global frame bar preferences for the part 
         Returns frame_bar_prefs ( FrameBarPreferences NXOpen.A):  .
        """
        pass
    def GetLetteringPreferences(self) -> LetteringPreferences:
        """
         Returns the global lettering preferences for the part 
         Returns lettering_prefs ( LetteringPreferences NXOpen.A):  .
        """
        pass
    def GetLineAndArrowPreferences(self) -> LineAndArrowPreferences:
        """
         Returns the global line and arrow preferences for the part 
         Returns prefs ( LineAndArrowPreferences NXOpen.A):  .
        """
        pass
    def GetLinearTolerances(self) -> LinearTolerance:
        """
         Returns the global linear tolerances for the part 
         Returns prefs ( LinearTolerance NXOpen.A):  .
        """
        pass
    def GetNxFontCharacterSpaceFactor(self) -> CharacterSpaceFactor:
        """
         Returns the NX font text space factor for each text type (dimension,general,appended,tolerance) for the part 
         Returns nx_font_character_space_factor ( CharacterSpaceFactor NXOpen.A):  .
        """
        pass
    def GetPmiPreferences(self) -> PmiPreferences:
        """
         Returns the global PMI preferences for the part 
         Returns pmi_prefs ( PmiPreferences NXOpen.A):  .
        """
        pass
    def GetStandardFontCharacterSpaceFactor(self) -> CharacterSpaceFactor:
        """
         Returns the standard font text space factor for each text type (dimension,general,appended,tolerance) for the part 
         Returns standard_font_character_space_factor ( CharacterSpaceFactor NXOpen.A):  .
        """
        pass
    def GetSymbolPreferences(self) -> SymbolPreferences:
        """
         Returns the global symbol preferences for the part 
         Returns prefs ( SymbolPreferences NXOpen.A):  .
        """
        pass
    def SetAngularTolerances(self, prefs: AngularTolerance) -> None:
        """
         Sets the global angular tolerances for the part 
        """
        pass
    def SetDimensionPreferences(self, prefs: DimensionPreferences) -> None:
        """
         Sets the global dimension preferences for the part 
        """
        pass
    def SetFrameBarPreferences(self, frame_bar_prefs: FrameBarPreferences) -> None:
        """
         Sets the global frame bar preferences for the part 
        """
        pass
    def SetLetteringPreferences(self, lettering_prefs: LetteringPreferences) -> None:
        """
         Sets the global lettering preferences for the part 
        """
        pass
    def SetLineAndArrowPreferences(self, prefs: LineAndArrowPreferences) -> None:
        """
         Sets the global line and arrow preferences for the part 
        """
        pass
    def SetLinearTolerances(self, prefs: LinearTolerance) -> None:
        """
         Sets the global linear tolerances for the part 
        """
        pass
    def SetNxFontCharacterSpaceFactor(self, nx_font_character_space_factor: CharacterSpaceFactor) -> None:
        """
         Sets the NX font text space factor for each text type (dimension,general,appended,tolerance) for the part 
        """
        pass
    def SetPmiPreferences(self, pmi_prefs: PmiPreferences) -> None:
        """
         Sets the global PMI preferences for the part 
        """
        pass
    def SetStandardFontCharacterSpaceFactor(self, standard_font_character_space_factor: CharacterSpaceFactor) -> None:
        """
         Sets the standard font text space factor for each text type (dimension,general,appended,tolerance) for the part 
        """
        pass
    def SetSymbolPreferences(self, prefs: SymbolPreferences) -> None:
        """
         Sets the global symbol preferences for the part 
        """
        pass
import NXOpen
class BaseViewPreferences(NXOpen.Object): 
    """ Represents set of Base View Preferences applicable to drafting views. 
        These settings apply to any newly created base view.
     """
    def SetFacetedRepresentation(self, is_faceted_representation: bool) -> None:
        """
         The status of faceted representation, if True the clipping bounds are inherited, else 
                    the imported model view is placed on the drawing with an Automatic Rectangular Boundary 
        """
        pass
    def SetInheritClippingBoundary(self, is_inherit_clipping_boundary: bool) -> None:
        """
         The status of inherit clipping boundary, if True the model view's 
                    clipping boundary are inherited when model view is imported onto the drawing, else 
                    the imported model view is placed on the drawing with an Automatic Rectangular Boundary.
                 
        """
        pass
    def SetTransferAnnotation(self, is_transfer_annotation: bool) -> None:
        """
         The status of transfer annotation controls whether or not annotations created in 
                    a model view are transferred to the drawing when a view is imported.
                 
        """
        pass
import NXOpen
class CoatingPreferences(NXOpen.Object): 
    """ Represents Coatings preferences that are applicable
        to the entire session. """
    @property
    def CreateNgc(self) -> bool:
        """
        Getter for property: (bool) CreateNgc
         Returns whether automatically creates non-geometric component for Coatings.  
              
         
        """
        pass
    @CreateNgc.setter
    def CreateNgc(self, create_ngc: bool):
        """
        Setter for property: (bool) CreateNgc
         Returns whether automatically creates non-geometric component for Coatings.  
              
         
        """
        pass
class DecimalPointCharacter(Enum):
    """
    Members Include: 
     |Period|  "." 
     |Comma|  "," 

    """
    Period: int
    Comma: int
    @staticmethod
    def ValueOf(value: int) -> DecimalPointCharacter:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class DetailBoundaryOption(Enum):
    """
    Members Include: 
     |Circular|  Circular boundary 
     |Rectangular|  Rectangular boundary 

    """
    Circular: int
    Rectangular: int
    @staticmethod
    def ValueOf(value: int) -> DetailBoundaryOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class DetailViewPreferences(NXOpen.Object): 
    """ Represents set of Detail View Preferences applicable to drafting views. """
    @property
    def CreateIndependent(self) -> int:
        """
        Getter for property: (int) CreateIndependent
         Returns the toogle create independent    
            
         
        """
        pass
    @CreateIndependent.setter
    def CreateIndependent(self, create_independent_toogle: int):
        """
        Setter for property: (int) CreateIndependent
         Returns the toogle create independent    
            
         
        """
        pass
    @property
    def ViewBoundaryColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) ViewBoundaryColor
         Returns the view boundary color option   
            
         
        """
        pass
    @ViewBoundaryColor.setter
    def ViewBoundaryColor(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) ViewBoundaryColor
         Returns the view boundary color option   
            
         
        """
        pass
    @property
    def ViewBoundaryFont(self) -> Font:
        """
        Getter for property: ( Font NXOpen.P) ViewBoundaryFont
         Returns the view boundary font option   
            
         
        """
        pass
    @ViewBoundaryFont.setter
    def ViewBoundaryFont(self, font: Font):
        """
        Setter for property: ( Font NXOpen.P) ViewBoundaryFont
         Returns the view boundary font option   
            
         
        """
        pass
    @property
    def ViewBoundaryWidth(self) -> Width:
        """
        Getter for property: ( Width NXOpen.P) ViewBoundaryWidth
         Returns the view boundary width option   
            
         
        """
        pass
    @ViewBoundaryWidth.setter
    def ViewBoundaryWidth(self, width: Width):
        """
        Setter for property: ( Width NXOpen.P) ViewBoundaryWidth
         Returns the view boundary width option   
            
         
        """
        pass
    def SetCircularBoundary(self, circular_boundary_option: bool) -> None:
        """
         Sets the circular boundary option. If True, circular boundary is displayed for detail 
                    view, else rectangular boundary is displayed.
                 
        """
        pass
import NXOpen
class DraftingPreferenceManager(NXOpen.Object): 
    """ Represents a collection of pmi preference builders."""
    def CreateLoadDraftingStandardBuilder(self) -> LoadDraftingStandardBuilder:
        """
         Creates the load drafting standard builder 
         Returns builder ( LoadDraftingStandardBuilder NXOpen.P):  the loaddraftingstandard Builder with this identifier .
        """
        pass
import NXOpen
class DrawShapeTaskPrefs(NXOpen.Object): 
    """ Represents the set of Draw Shape preferences applicable to entire session"""
    @property
    def CurveColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) CurveColor
         Returns the Curve color.  
             
         
        """
        pass
    @CurveColor.setter
    def CurveColor(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) CurveColor
         Returns the Curve color.  
             
         
        """
        pass
    @property
    def CurveThickness(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectWidth) CurveThickness
         Returns the Curve thickness.  
             
         
        """
        pass
    @CurveThickness.setter
    def CurveThickness(self, thickness: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectWidth) CurveThickness
         Returns the Curve thickness.  
             
         
        """
        pass
    @property
    def StrokeColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) StrokeColor
         Returns the Stroke color.  
             
         
        """
        pass
    @StrokeColor.setter
    def StrokeColor(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) StrokeColor
         Returns the Stroke color.  
             
         
        """
        pass
    @property
    def StrokeThickness(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectWidth) StrokeThickness
         Returns the Stroke thickness.  
             
         
        """
        pass
    @StrokeThickness.setter
    def StrokeThickness(self, thickness: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectWidth) StrokeThickness
         Returns the Stroke thickness.  
             
         
        """
        pass
    @property
    def SymmetryCurveFont(self) -> NXOpen.DisplayableObject.ObjectFont:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectFont) SymmetryCurveFont
         Returns the Mirror Curve font.  
             
         
        """
        pass
    @SymmetryCurveFont.setter
    def SymmetryCurveFont(self, font: NXOpen.DisplayableObject.ObjectFont):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectFont) SymmetryCurveFont
         Returns the Mirror Curve font.  
             
         
        """
        pass
    @property
    def TangentAtSymmetryPlane(self) -> bool:
        """
        Getter for property: (bool) TangentAtSymmetryPlane
         Returns the option to be tangent at symmetry plane.  
             
         
        """
        pass
    @TangentAtSymmetryPlane.setter
    def TangentAtSymmetryPlane(self, isTangentAtSymmetryPlane: bool):
        """
        Setter for property: (bool) TangentAtSymmetryPlane
         Returns the option to be tangent at symmetry plane.  
             
         
        """
        pass
    @property
    def TrimAtSymmetryPlane(self) -> bool:
        """
        Getter for property: (bool) TrimAtSymmetryPlane
         Returns the option to trim at symmetry plane.  
             
         
        """
        pass
    @TrimAtSymmetryPlane.setter
    def TrimAtSymmetryPlane(self, isTrimAtSymmetryPlane: bool):
        """
        Setter for property: (bool) TrimAtSymmetryPlane
         Returns the option to trim at symmetry plane.  
             
         
        """
        pass
import NXOpen
import NXOpen.SheetMetal
class FlatPatternViewPreferences(NXOpen.Object): 
    """ Provides access to object and callout properties for sheet-metal data in
    flat pattern views on drawings. """
    def Commit(self) -> None:
        """
         Commits and applies all the settings done with set_callout_type_display
                    and set_object_type_display. It must be called after a sequence of calls
                    to those methods to cause the view to update. 
        """
        pass
    def GetPropertiesObject(self) -> NXOpen.SheetMetal.FlatPatternSettings:
        """
         Returns the properties object for the part's flat pattern view preferences. 
         Returns properties_object ( NXOpen.SheetMetal.FlatPatternSettings):  Reference to the object on which to get and set the
                                preferences for flat pattern drawing member views. .
        """
        pass
class Font(Enum):
    """
    Members Include: 
     |Invisible|  Invisible 
     |Solid|  Solid 
     |Dashed|  Dashed 
     |Phantom|  Phantom 
     |Centerline|  Centerline 
     |Dotted|  Dotted
     |LongDashed|  Long Dashed 
     |DottedDashed|  Dotted Dashed 
     |Original|  Original 
     |Eight|  Long Dashed Double Dotted
     |Nine|  Long Dashed Dotted for OOTB fonts and Undulating for shipbuilding fonts 
     |Ten|  Long Dashed Triplicate Dotted for OOTB fonts and Zigzag for shipbuilding fonts 
     |Eleven|  Long Dashed Double Short Dashed for OOTB fonts and Railway for shipbuilding fonts 

    """
    Invisible: int
    Solid: int
    Dashed: int
    Phantom: int
    Centerline: int
    Dotted: int
    LongDashed: int
    DottedDashed: int
    Original: int
    Eight: int
    Nine: int
    Ten: int
    Eleven: int
    @staticmethod
    def ValueOf(value: int) -> Font:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.Features.SheetMetal
class FpcdPreferencesBuilder(NXOpen.Builder): 
    """ Represents a Preferences.FpcdPreferencesBuilder builder """
    class FlatPatternCalloutOrientationTypes(Enum):
        """
        Members Include: 
         |Leadered|  Leadered 
         |Aligned|  Aligned 

        """
        Leadered: int
        Aligned: int
        @staticmethod
        def ValueOf(value: int) -> FpcdPreferencesBuilder.FlatPatternCalloutOrientationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FlatPatternObjectTypes(Enum):
        """
        Members Include: 
         |BendUpCenterLine|  
         |BendDownCenterLine|  
         |BendTangentLine|  
         |OuterMoldLine|  
         |InnerMoldLine|  
         |ExteriorCurves|  
         |InteriorCutoutCurves|  
         |InteriorFeatureCurves|  
         |LighteningHoleCenter|  
         |JoggleLine|  
         |AddedTopGeometry|  
         |AddedBottomGeometry|  
         |ToolMarker|  
         |Hole|  
         |CenterMark|  

        """
        BendUpCenterLine: int
        BendDownCenterLine: int
        BendTangentLine: int
        OuterMoldLine: int
        InnerMoldLine: int
        ExteriorCurves: int
        InteriorCutoutCurves: int
        InteriorFeatureCurves: int
        LighteningHoleCenter: int
        JoggleLine: int
        AddedTopGeometry: int
        AddedBottomGeometry: int
        ToolMarker: int
        Hole: int
        CenterMark: int
        @staticmethod
        def ValueOf(value: int) -> FpcdPreferencesBuilder.FlatPatternObjectTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FlexibleCableContactFaceOptions(Enum):
        """
        Members Include: 
         |TopFace|  Top face. 
         |BottomFace|  Bottom face. 

        """
        TopFace: int
        BottomFace: int
        @staticmethod
        def ValueOf(value: int) -> FpcdPreferencesBuilder.FlexibleCableContactFaceOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ParameterEntryTypes(Enum):
        """
        Members Include: 
         |Value|  The manual Value entry method
         |MaterialTable|  The Material Table entry method

        """
        Value: int
        MaterialTable: int
        @staticmethod
        def ValueOf(value: int) -> FpcdPreferencesBuilder.ParameterEntryTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PlanarSegmentCurveTypes(Enum):
        """
        Members Include: 
         |BendCenterLine|  
         |BendTangentLine|  

        """
        BendCenterLine: int
        BendTangentLine: int
        @staticmethod
        def ValueOf(value: int) -> FpcdPreferencesBuilder.PlanarSegmentCurveTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FlatPatternCalloutTypeDisplay:
        """
         The members of the following structure are the display data for a
                    callout in a flat pattern drawing member view. 
         FpcdPreferencesBuilderFlatPatternCalloutTypeDisplay_Struct NXOpen.P is an alias for  FpcdPreferencesBuilder.FlatPatternCalloutTypeDisplay NXOpen.P.
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
        def IsEnabled(self) -> bool:
            """
            Getter for property IsEnabled
            Enabled status for the callout type.

            """
            pass
        @IsEnabled.setter
        def IsEnabled(self, value: bool):
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
         FpcdPreferencesBuilderFlatPatternObjectTypeDisplay_Struct NXOpen.P is an alias for  FpcdPreferencesBuilder.FlatPatternObjectTypeDisplay NXOpen.P.
        """
        @property
        def Type(self) -> FpcdPreferencesBuilder.FlatPatternObjectTypes:
            """
            Getter for property Type
            Object type

            """
            pass
        @Type.setter
        def Type(self, value: FpcdPreferencesBuilder.FlatPatternObjectTypes):
            """
            Getter for property Type
            Object type
            Setter for property Type
            Object type

            """
            pass
        @property
        def IsEnabled(self) -> bool:
            """
            Getter for property IsEnabled
            Enabled status for the object type

            """
            pass
        @IsEnabled.setter
        def IsEnabled(self, value: bool):
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
        def Layer(self) -> int:
            """
            Getter for property Layer
            Object Layer

            """
            pass
        @Layer.setter
        def Layer(self, value: int):
            """
            Getter for property Layer
            Object Layer
            Setter for property Layer
            Object Layer

            """
            pass
        @property
        def Font(self) -> NXOpen.DisplayableObject.ObjectFont:
            """
            Getter for property Font
            Object font

            """
            pass
        @Font.setter
        def Font(self, value: NXOpen.DisplayableObject.ObjectFont):
            """
            Getter for property Font
            Object font
            Setter for property Font
            Object font

            """
            pass
        @property
        def Width(self) -> NXOpen.DisplayableObject.ObjectWidth:
            """
            Getter for property Width
            Object width

            """
            pass
        @Width.setter
        def Width(self, value: NXOpen.DisplayableObject.ObjectWidth):
            """
            Getter for property Width
            Object width
            Setter for property Width
            Object width

            """
            pass
    class PlanarSegmentCurvesDisplayData:
        """
         The members of the following structure are the display data of a planar segment curve type. 
         FpcdPreferencesBuilderPlanarSegmentCurvesDisplayData_Struct NXOpen.P is an alias for  FpcdPreferencesBuilder.PlanarSegmentCurvesDisplayData NXOpen.P.
        """
        @property
        def Type(self) -> FpcdPreferencesBuilder.PlanarSegmentCurveTypes:
            """
            Getter for property Type
            Curve type

            """
            pass
        @Type.setter
        def Type(self, value: FpcdPreferencesBuilder.PlanarSegmentCurveTypes):
            """
            Getter for property Type
            Curve type
            Setter for property Type
            Curve type

            """
            pass
        @property
        def IsEnabled(self) -> int:
            """
            Getter for property IsEnabled
            Enabled status of the curve type

            """
            pass
        @IsEnabled.setter
        def IsEnabled(self, value: int):
            """
            Getter for property IsEnabled
            Enabled status of the curve type
            Setter for property IsEnabled
            Enabled status of the curve type

            """
            pass
        @property
        def Color(self) -> int:
            """
            Getter for property Color
            Curve color

            """
            pass
        @Color.setter
        def Color(self, value: int):
            """
            Getter for property Color
            Curve color
            Setter for property Color
            Curve color

            """
            pass
        @property
        def Font(self) -> NXOpen.DisplayableObject.ObjectFont:
            """
            Getter for property Font
            Curve font

            """
            pass
        @Font.setter
        def Font(self, value: NXOpen.DisplayableObject.ObjectFont):
            """
            Getter for property Font
            Curve font
            Setter for property Font
            Curve font

            """
            pass
        @property
        def Width(self) -> NXOpen.DisplayableObject.ObjectWidth:
            """
            Getter for property Width
            Curve width

            """
            pass
        @Width.setter
        def Width(self, value: NXOpen.DisplayableObject.ObjectWidth):
            """
            Getter for property Width
            Curve width
            Setter for property Width
            Curve width

            """
            pass
    @property
    def BendRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BendRadius
         Returns the bend radius   
            
         
        """
        pass
    @property
    def BendReliefDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BendReliefDepth
         Returns the bend relief depth   
            
         
        """
        pass
    @property
    def BendReliefWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BendReliefWidth
         Returns the bend relief width   
            
         
        """
        pass
    @property
    def BottomFaceColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) BottomFaceColor
         Returns the bottom face color.  
             
         
        """
        pass
    @BottomFaceColor.setter
    def BottomFaceColor(self, bottomFaceColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) BottomFaceColor
         Returns the bottom face color.  
             
         
        """
        pass
    @property
    def DeviationalTolerance(self) -> float:
        """
        Getter for property: (float) DeviationalTolerance
         Returns the flat pattern treatment deviational tolerance.  
           This is needed only when  SimplifyBSplines  is let to true.   
         
        """
        pass
    @DeviationalTolerance.setter
    def DeviationalTolerance(self, deviationalTolerance: float):
        """
        Setter for property: (float) DeviationalTolerance
         Returns the flat pattern treatment deviational tolerance.  
           This is needed only when  SimplifyBSplines  is let to true.   
         
        """
        pass
    @property
    def FlatPatternHoleTreatmentDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlatPatternHoleTreatmentDiameter
         Returns the flat pattern treatment hole diameter   
            
         
        """
        pass
    @property
    def FlatPatternInsideCornerTreatmentValue(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlatPatternInsideCornerTreatmentValue
         Returns the flat pattern treatment inside value   
            
         
        """
        pass
    @property
    def FlatPatternOutsideCornerTreatmentValue(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlatPatternOutsideCornerTreatmentValue
         Returns the flat pattern treatment outside value   
            
         
        """
        pass
    @property
    def FlatSolidColor(self) -> int:
        """
        Getter for property: (int) FlatSolidColor
         Returns the flat solid color   
            
         
        """
        pass
    @FlatSolidColor.setter
    def FlatSolidColor(self, flatSolidColor: int):
        """
        Setter for property: (int) FlatSolidColor
         Returns the flat solid color   
            
         
        """
        pass
    @property
    def FlatSolidLayer(self) -> int:
        """
        Getter for property: (int) FlatSolidLayer
         Returns the flat solid layer   
            
         
        """
        pass
    @FlatSolidLayer.setter
    def FlatSolidLayer(self, flatSolidLayer: int):
        """
        Setter for property: (int) FlatSolidLayer
         Returns the flat solid layer   
            
         
        """
        pass
    @property
    def FlexibleCableConductorSpacing(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlexibleCableConductorSpacing
         Returns the conductor spacing expression.  
             
         
        """
        pass
    @property
    def FlexibleCableConductorWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlexibleCableConductorWidth
         Returns the conductor width expression.  
             
         
        """
        pass
    @property
    def FlexibleCableContactFace(self) -> FpcdPreferencesBuilder.FlexibleCableContactFaceOptions:
        """
        Getter for property: ( FpcdPreferencesBuilder.FlexibleCableContactFaceOptions NXOpen.P) FlexibleCableContactFace
         Returns the contact face.  
             
         
        """
        pass
    @FlexibleCableContactFace.setter
    def FlexibleCableContactFace(self, faceOption: FpcdPreferencesBuilder.FlexibleCableContactFaceOptions):
        """
        Setter for property: ( FpcdPreferencesBuilder.FlexibleCableContactFaceOptions NXOpen.P) FlexibleCableContactFace
         Returns the contact face.  
             
         
        """
        pass
    @property
    def FlexibleCableStrippingLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlexibleCableStrippingLength
         Returns the stripping length expression   
            
         
        """
        pass
    @property
    def HoleTreatmentType(self) -> NXOpen.Features.SheetMetal.FeatureProperty:
        """
        Getter for property: ( NXOpen.Features.SheetMetal.FeatureProperty) HoleTreatmentType
         Returns the flat pattern hole treatment type   
            
         
        """
        pass
    @HoleTreatmentType.setter
    def HoleTreatmentType(self, holeTreatmentType: NXOpen.Features.SheetMetal.FeatureProperty):
        """
        Setter for property: ( NXOpen.Features.SheetMetal.FeatureProperty) HoleTreatmentType
         Returns the flat pattern hole treatment type   
            
         
        """
        pass
    @property
    def InsideCornerTreatmentType(self) -> NXOpen.Features.SheetMetal.FeatureProperty:
        """
        Getter for property: ( NXOpen.Features.SheetMetal.FeatureProperty) InsideCornerTreatmentType
         Returns the flat pattern inside treatment type   
            
         
        """
        pass
    @InsideCornerTreatmentType.setter
    def InsideCornerTreatmentType(self, insideCornerTreatmentType: NXOpen.Features.SheetMetal.FeatureProperty):
        """
        Setter for property: ( NXOpen.Features.SheetMetal.FeatureProperty) InsideCornerTreatmentType
         Returns the flat pattern inside treatment type   
            
         
        """
        pass
    @property
    def IntegratePhysicalMaterialLibrary(self) -> bool:
        """
        Getter for property: (bool) IntegratePhysicalMaterialLibrary
         Returns whether to integrate the physical material library   
            
         
        """
        pass
    @IntegratePhysicalMaterialLibrary.setter
    def IntegratePhysicalMaterialLibrary(self, integratePhysicalMaterialLibrary: bool):
        """
        Setter for property: (bool) IntegratePhysicalMaterialLibrary
         Returns whether to integrate the physical material library   
            
         
        """
        pass
    @property
    def MaintainCircularShapeForHoles(self) -> bool:
        """
        Getter for property: (bool) MaintainCircularShapeForHoles
         Returns whether the circular shape for holes in the flat pattern should be maintained.  
             
         
        """
        pass
    @MaintainCircularShapeForHoles.setter
    def MaintainCircularShapeForHoles(self, maintainCircularShapeForHoles: bool):
        """
        Setter for property: (bool) MaintainCircularShapeForHoles
         Returns whether the circular shape for holes in the flat pattern should be maintained.  
             
         
        """
        pass
    @property
    def MaterialThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaterialThickness
         Returns the material thickness   
            
         
        """
        pass
    @property
    def MinimumArcTolerance(self) -> float:
        """
        Getter for property: (float) MinimumArcTolerance
         Returns the flat pattern treatment minimum arc tolerance.  
           This is needed only when  SimplifyBSplines  is let to true.   
         
        """
        pass
    @MinimumArcTolerance.setter
    def MinimumArcTolerance(self, minimumArcTolerance: float):
        """
        Setter for property: (float) MinimumArcTolerance
         Returns the flat pattern treatment minimum arc tolerance.  
           This is needed only when  SimplifyBSplines  is let to true.   
         
        """
        pass
    @property
    def NeutralFactor(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NeutralFactor
         Returns the neutral factor   
            
         
        """
        pass
    @property
    def OutsideCornerTreatmentType(self) -> NXOpen.Features.SheetMetal.FeatureProperty:
        """
        Getter for property: ( NXOpen.Features.SheetMetal.FeatureProperty) OutsideCornerTreatmentType
         Returns the flat pattern outside treatment type   
            
         
        """
        pass
    @OutsideCornerTreatmentType.setter
    def OutsideCornerTreatmentType(self, outsideCornerTreatmentType: NXOpen.Features.SheetMetal.FeatureProperty):
        """
        Setter for property: ( NXOpen.Features.SheetMetal.FeatureProperty) OutsideCornerTreatmentType
         Returns the flat pattern outside treatment type   
            
         
        """
        pass
    @property
    def ParameterEntryType(self) -> FpcdPreferencesBuilder.ParameterEntryTypes:
        """
        Getter for property: ( FpcdPreferencesBuilder.ParameterEntryTypes NXOpen.P) ParameterEntryType
         Returns the parameter entry type   
            
         
        """
        pass
    @ParameterEntryType.setter
    def ParameterEntryType(self, parameterEntryType: FpcdPreferencesBuilder.ParameterEntryTypes):
        """
        Setter for property: ( FpcdPreferencesBuilder.ParameterEntryTypes NXOpen.P) ParameterEntryType
         Returns the parameter entry type   
            
         
        """
        pass
    @property
    def RemoveBendReliefs(self) -> bool:
        """
        Getter for property: (bool) RemoveBendReliefs
         Returns whether the bend reliefs in the flat pattern should be removed.  
             
         
        """
        pass
    @RemoveBendReliefs.setter
    def RemoveBendReliefs(self, removeBendReliefs: bool):
        """
        Setter for property: (bool) RemoveBendReliefs
         Returns whether the bend reliefs in the flat pattern should be removed.  
             
         
        """
        pass
    @property
    def SimplifyBSplines(self) -> bool:
        """
        Getter for property: (bool) SimplifyBSplines
         Returns whether the bspline curves in the flat pattern should be simplified.  
             
         
        """
        pass
    @SimplifyBSplines.setter
    def SimplifyBSplines(self, simplifyBSplinesFlag: bool):
        """
        Setter for property: (bool) SimplifyBSplines
         Returns whether the bspline curves in the flat pattern should be simplified.  
             
         
        """
        pass
    @property
    def TopFaceColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) TopFaceColor
         Returns the top face color.  
             
         
        """
        pass
    @TopFaceColor.setter
    def TopFaceColor(self, topFaceColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) TopFaceColor
         Returns the top face color.  
             
         
        """
        pass
    def GetFlatPatternAllCalloutTypeDisplay(self) -> List[FpcdPreferencesBuilder.FlatPatternCalloutTypeDisplay]:
        """
         Returns the dialog names, identifiers, and enabled status for all the available callout types. 
         Returns displayData ( FpcdPreferencesBuilder.FlatPatternCalloutTypeDisplay List[NXOpen):  Array of structures with the object type display data. .
        """
        pass
    def GetFlatPatternAllObjectTypeDisplay(self) -> List[FpcdPreferencesBuilder.FlatPatternObjectTypeDisplay]:
        """
         Returns the types, colors, fonts, widths, and enabled status for all the 
                available flat pattern display object types. 
         Returns displayData ( FpcdPreferencesBuilder.FlatPatternObjectTypeDisplay List[NXOpen):  Array of structures with the object type display data. .
        """
        pass
    def GetFlatPatternCalloutOrientationType(self) -> FpcdPreferencesBuilder.FlatPatternCalloutOrientationTypes:
        """
         Returns the orientation type for flat pattern callouts. 
         Returns orientation ( FpcdPreferencesBuilder.FlatPatternCalloutOrientationTypes NXOpen.P):  The orientation type for the flat pattern callouts. .
        """
        pass
    def GetFlatPatternCalloutTypeContents(self, calloutType: str) -> List[str]:
        """
         Returns the contents for a callout type. 
         Returns contents (List[str]):  The contents for the callout type. .
        """
        pass
    def GetFlatPatternCalloutTypeDisplay(self, calloutType: str) -> FpcdPreferencesBuilder.FlatPatternCalloutTypeDisplay:
        """
         Returns the display data for a callout type. The name member of the
                    NXOpen.Preferences.FpcdPreferencesBuilder.FlatPatternCalloutTypeDisplay
                    is separately allocated from the calloutType argument string.
                    In some cases the new string will contain an extended form of the callout_type passed in, 
                    and that form should be used for subsequent JA calls, without modification. 
         Returns displayData ( FpcdPreferencesBuilder.FlatPatternCalloutTypeDisplay NXOpen.P):  The display data for the callout type. .
        """
        pass
    def GetFlatPatternObjectTypeDisplay(self, objectType: FpcdPreferencesBuilder.FlatPatternObjectTypes) -> FpcdPreferencesBuilder.FlatPatternObjectTypeDisplay:
        """
         Returns display data for a given flat pattern object type 
         Returns displayData ( FpcdPreferencesBuilder.FlatPatternObjectTypeDisplay NXOpen.P):  The display data for the flat pattern object type. .
        """
        pass
    def GetMaterialName(self) -> str:
        """
         Returns the name of the material saved with the part 
         Returns materialName (str): .
        """
        pass
    def GetMaterialNames(self) -> List[str]:
        """
         Returns the material names defined in the material standards table 
         Returns materialNames (List[str]): .
        """
        pass
    def GetMaterialProperties(self, materialName: str) -> Tuple[List[str], List[str]]:
        """
         Returns the properties of the given material  
         Returns A tuple consisting of (propertyValues, propertyNames). 
         - propertyValues is: List[str].property Values .
         - propertyNames is: List[str].property Names .

        """
        pass
    def GetMultiThicknessLayerScheme(self) -> str:
        """
         Gets the layer scheme for multi thickness. 
         Returns multiHeightLayerScheme (str):  Name of layer scheme.
        """
        pass
    def GetPlanarSegmentCurveDisplayData(self, curveType: FpcdPreferencesBuilder.PlanarSegmentCurveTypes) -> FpcdPreferencesBuilder.PlanarSegmentCurvesDisplayData:
        """
         Returns display data for a given planar segment curve type. 
         Returns displayData ( FpcdPreferencesBuilder.PlanarSegmentCurvesDisplayData NXOpen.P):  The display data for the tab curve. .
        """
        pass
    def SetFlatPatternCalloutOrientationType(self, orientation: FpcdPreferencesBuilder.FlatPatternCalloutOrientationTypes) -> None:
        """
         Sets the orientation type for flat pattern callouts. 
        """
        pass
    def SetFlatPatternCalloutTypeContents(self, calloutType: str, contents: List[str]) -> None:
        """
         Sets the contents for a callout type. 
        """
        pass
    def SetFlatPatternCalloutTypeDisplay(self, calloutType: str, displayData: FpcdPreferencesBuilder.FlatPatternCalloutTypeDisplay) -> None:
        """
         Sets the display data for a callout type. 
        """
        pass
    def SetFlatPatternObjectTypeDisplay(self, objectType: FpcdPreferencesBuilder.FlatPatternObjectTypes, displayData: FpcdPreferencesBuilder.FlatPatternObjectTypeDisplay) -> None:
        """
         Sets display data for a given flat pattern object type 
        """
        pass
    def SetMaterial(self, materialName: str) -> None:
        """
         Sets the material to the part 
        """
        pass
    def SetMultiThicknessLayerScheme(self, multiHeightLayerScheme: str) -> None:
        """
         Sets the layer scheme for multi thickness. 
        """
        pass
    def SetPlanarSegmentCurveDisplayData(self, curveType: FpcdPreferencesBuilder.PlanarSegmentCurveTypes, displayData: FpcdPreferencesBuilder.PlanarSegmentCurvesDisplayData) -> None:
        """
         Sets display data for a given planar segment curve type. 
        """
        pass
import NXOpen
import NXOpen.Features.SheetMetal
class FpcdPreferencesManager(NXOpen.Object): 
    """ Represents a collection of fpcd preference builders."""
    def CreateFpcdPreferencesBuilder(self) -> FpcdPreferencesBuilder:
        """
         Creates a NXOpen.Preferences.FpcdPreferencesBuilder 
         Returns builder ( FpcdPreferencesBuilder NXOpen.P): .
        """
        pass
    def GetBendRadius(self) -> NXOpen.Expression:
        """
         Returns the bend radius expression tag. This API is only to get the expression from the preferences, 
                    to modify any of the values use Preferences.FpcdPreferencesBuilder.  
         Returns bendRadius ( NXOpen.Expression):  bend radius expression tag .
        """
        pass
    def GetBendReliefDepth(self) -> NXOpen.Expression:
        """
         Returns the bend relief depth expression tag.This API is only to get the expression from the preferences, 
                    to modify any of the values use Preferences.FpcdPreferencesBuilder. 
         Returns bendReliefDepth ( NXOpen.Expression):  bend relief depth expression tag .
        """
        pass
    def GetBendReliefWidth(self) -> NXOpen.Expression:
        """
         Returns the bend relief width expression tag. This API is only to get the expression from the preferences, 
                    to modify any of the values use Preferences.FpcdPreferencesBuilder. 
         Returns bendReliefWidth ( NXOpen.Expression):  bend relief width expression tag .
        """
        pass
    def GetBottomFaceColor(self) -> NXOpen.NXColor:
        """
         Returns bottom face color. 
         Returns bottomFaceColor ( NXOpen.NXColor): .
        """
        pass
    def GetDeviationalTolerance(self) -> float:
        """
         Returns the flat pattern deviational tolerance value 
         Returns deviationalTolerance (float):  flat pattern deviational tolerance value .
        """
        pass
    def GetFlatPatternAllCalloutTypeDisplay(self) -> List[FpcdPreferencesBuilder.FlatPatternCalloutTypeDisplay]:
        """
         Returns the dialog names, identifiers, and enabled status for all the available callout types. 
         Returns displayData ( FpcdPreferencesBuilder.FlatPatternCalloutTypeDisplay List[NXOpen):  Array of structures with the object type display data. .
        """
        pass
    def GetFlatPatternAllObjectTypeDisplay(self) -> List[FpcdPreferencesBuilder.FlatPatternObjectTypeDisplay]:
        """
         Returns the types, colors, fonts, widths, and enabled status for all the 
                available flat pattern display object types. 
         Returns displayData ( FpcdPreferencesBuilder.FlatPatternObjectTypeDisplay List[NXOpen):  Array of structures with the object type display data. .
        """
        pass
    def GetFlatPatternCalloutOrientationType(self) -> FpcdPreferencesBuilder.FlatPatternCalloutOrientationTypes:
        """
         Returns the orientation type for flat pattern callouts. 
         Returns orientation ( FpcdPreferencesBuilder.FlatPatternCalloutOrientationTypes NXOpen.P):  The orientation type for the flat pattern callouts. .
        """
        pass
    def GetFlatPatternCalloutTypeContents(self, calloutType: str) -> List[str]:
        """
         Returns the contents for a callout type. 
         Returns contents (List[str]):  The contents for the callout type. .
        """
        pass
    def GetFlatPatternCalloutTypeDisplay(self, calloutType: str) -> FpcdPreferencesBuilder.FlatPatternCalloutTypeDisplay:
        """
         Returns the display data for a callout type. The name member of the
                    NXOpen.Preferences.FpcdPreferencesBuilder.FlatPatternCalloutTypeDisplay
                    is separately allocated from the calloutType argument string.
                    In some cases the new string will contain an extended form of the callout_type passed in, 
                    and that form should be used for subsequent JA calls, without modification. 
         Returns displayData ( FpcdPreferencesBuilder.FlatPatternCalloutTypeDisplay NXOpen.P):  The display data for the callout type. .
        """
        pass
    def GetFlatPatternHoleTreatmentDiameterValue(self) -> NXOpen.Expression:
        """
         Returns the expression tag of flat pattern hole treatment diameter value. This API is only to get the expression from the preferences, 
                    to modify any of the values use Preferences.FpcdPreferencesBuilder. 
         Returns holeTreatmentValue ( NXOpen.Expression):  expression tag of flat pattern hole treatment value .
        """
        pass
    def GetFlatPatternInsideCornerTreatmentValue(self) -> NXOpen.Expression:
        """
         Returns expression tag of the flat pattern inside corner treatment value. This API is only to get the expression from the preferences, 
                    to modify any of the values use Preferences.FpcdPreferencesBuilder. 
         Returns insideCornerTreatmentValue ( NXOpen.Expression):  expression tag of flat pattern inside corner treatment value .
        """
        pass
    def GetFlatPatternObjectTypeDisplay(self, objectType: FpcdPreferencesBuilder.FlatPatternObjectTypes) -> FpcdPreferencesBuilder.FlatPatternObjectTypeDisplay:
        """
         Returns display data for a given flat pattern object type 
         Returns displayData ( FpcdPreferencesBuilder.FlatPatternObjectTypeDisplay NXOpen.P):  The display data for the flat pattern object type. .
        """
        pass
    def GetFlatPatternOutsideCornerTreatmentValue(self) -> NXOpen.Expression:
        """
         Retruns the expression tag of flat pattern outside corner treatment value. This API is only to get the expression from the preferences, 
                    to modify any of the values use Preferences.FpcdPreferencesBuilder. 
         Returns outsideCornerTreatmentValue ( NXOpen.Expression):  expression tag of flat pattern outside corner treatment value .
        """
        pass
    def GetFlatSolidColor(self) -> int:
        """
         Returns the flat solid color 
         Returns flatSolidColor (int): .
        """
        pass
    def GetFlatSolidLayer(self) -> int:
        """
         Returns the flat solid layer 
         Returns flatSolidLayer (int): .
        """
        pass
    def GetFlexibleCableConductorSpacing(self) -> NXOpen.Expression:
        """
         Returns the conductor spacing expression tag. This API is only to get the expression from the preferences, 
                    to modify any of the values use Preferences.FpcdPreferencesBuilder. 
         Returns conductorSpacing ( NXOpen.Expression):  conductor spacing expression tag .
        """
        pass
    def GetFlexibleCableConductorWidth(self) -> NXOpen.Expression:
        """
         Returns the conductor width expression tag. This API is only to get the expression from the preferences, 
                    to modify any of the values use Preferences.FpcdPreferencesBuilder. 
         Returns conductoWidth ( NXOpen.Expression):  conductor width expression tag .
        """
        pass
    def GetFlexibleCableStrippingLength(self) -> NXOpen.Expression:
        """
         Returns the conductor spacing expression tag. This API is only to get the expression from the preferences, 
                    to modify any of the values use Preferences.FpcdPreferencesBuilder. 
         Returns strippingLength ( NXOpen.Expression):  stripping length expression tag .
        """
        pass
    def GetHoleTreatmentType(self) -> NXOpen.Features.SheetMetal.FeatureProperty:
        """
         Returns the flat pattern hole treatment type 
         Returns holeTreatmentType ( NXOpen.Features.SheetMetal.FeatureProperty):  hole treatment type .
        """
        pass
    def GetInsideCornerTreatmentType(self) -> NXOpen.Features.SheetMetal.FeatureProperty:
        """
         Returns the flat pattern inside corner treatment type 
         Returns insideCornerTreatmentType ( NXOpen.Features.SheetMetal.FeatureProperty):  inside corner treatment type .
        """
        pass
    def GetIntegratePhysicalMaterialLibrary(self) -> bool:
        """
         Returns whether the physical material library is integrated or not. 
         Returns integratePhysicalMaterialLibrary (bool): .
        """
        pass
    def GetMaintainCircularShapeForHoles(self) -> bool:
        """
         Returns whether the circular shape for holes in the flat pattern is maintained or not. 
         Returns isCircularShapeForHolesMaintained (bool): .
        """
        pass
    def GetMaterialName(self) -> str:
        """
         Returns the name of the material saved with the part 
         Returns materialName (str): .
        """
        pass
    def GetMaterialNames(self) -> List[str]:
        """
         Returns the material names defined in the material standards table 
         Returns materialNames (List[str]): .
        """
        pass
    def GetMaterialProperties(self, materialName: str) -> Tuple[List[str], List[str]]:
        """
         Returns the properties of the given material  
         Returns A tuple consisting of (propertyValues, propertyNames). 
         - propertyValues is: List[str].property Values .
         - propertyNames is: List[str].property Names .

        """
        pass
    def GetMaterialThickness(self) -> NXOpen.Expression:
        """
         Returns the material thickness expression tag. This API is only to get the expression from the preferences, 
                    to modify any of the values use Preferences.FpcdPreferencesBuilder. 
         Returns thickness ( NXOpen.Expression):  material thickness expression tag.
        """
        pass
    def GetMinimumArcTolerance(self) -> float:
        """
         Returns the flat pattern minimum arc tolerance value 
         Returns minArcTolerance (float):  flat pattern minimum arc tolerance value .
        """
        pass
    def GetMultiThicknessLayerScheme(self) -> str:
        """
         Returns the layer scheme name for multi thickness. 
         Returns multiHeightLayerScheme (str):  Layer scheme name .
        """
        pass
    def GetNeutralFactor(self) -> NXOpen.Expression:
        """
         Returns neutral factor expression tag. This API is only to get the expression from the preferences, 
                    to modify any of the values use Preferences.FpcdPreferencesBuilder. 
         Returns neutralFactor ( NXOpen.Expression):  neutral factor expression tag .
        """
        pass
    def GetOutsideCornerTreatmentType(self) -> NXOpen.Features.SheetMetal.FeatureProperty:
        """
         Returns the flat pattern outside corner treatment type 
         Returns outsideCornerTreatmentType ( NXOpen.Features.SheetMetal.FeatureProperty):  outside corner treatment type .
        """
        pass
    def GetParameterEntryType(self) -> FpcdPreferencesBuilder.ParameterEntryTypes:
        """
         Returns parameter entry type 
         Returns parameterEntryType ( FpcdPreferencesBuilder.ParameterEntryTypes NXOpen.P): .
        """
        pass
    def GetPlanarSegmentCurveDisplayData(self, curveType: FpcdPreferencesBuilder.PlanarSegmentCurveTypes) -> FpcdPreferencesBuilder.PlanarSegmentCurvesDisplayData:
        """
         Returns display data for a given planar segment curve type. 
         Returns displayData ( FpcdPreferencesBuilder.PlanarSegmentCurvesDisplayData NXOpen.P):  The display data for the tab curve. .
        """
        pass
    def GetRemoveSysGenBendReliefs(self) -> bool:
        """
         Returns whether the bend reliefs in the flat pattern are removed or not. 
         Returns areBendReliefsRemoved (bool): .
        """
        pass
    def GetSimplifyBSplines(self) -> bool:
        """
         Returns whether the bspline curves in the flat pattern are simplified or not. 
         Returns areBSplinesSimplified (bool): .
        """
        pass
    def GetTopFaceColor(self) -> NXOpen.NXColor:
        """
         Returns top face color. 
         Returns topFaceColor ( NXOpen.NXColor): .
        """
        pass
import NXOpen
class FrameBarPreferences(NXOpen.Object): 
    """ Represents Frame Bar Preferencess applicable to drafting views. 
     """
    @property
    def Horizontal(self) -> bool:
        """
        Getter for property: (bool) Horizontal
         Returns the status of horizontal framebar.  
           If true it automatically creates 
                    horizontal framebar for views when ship axis matches with view axis
                    for horizontal framebar.
                   
         
        """
        pass
    @Horizontal.setter
    def Horizontal(self, horizontal: bool):
        """
        Setter for property: (bool) Horizontal
         Returns the status of horizontal framebar.  
           If true it automatically creates 
                    horizontal framebar for views when ship axis matches with view axis
                    for horizontal framebar.
                   
         
        """
        pass
    @property
    def HorizontalDistance(self) -> float:
        """
        Getter for property: (float) HorizontalDistance
         Returns the horizontal distance   
            
         
        """
        pass
    @HorizontalDistance.setter
    def HorizontalDistance(self, horizontalDistance: float):
        """
        Setter for property: (float) HorizontalDistance
         Returns the horizontal distance   
            
         
        """
        pass
    @property
    def HorizontalPosition(self) -> BaseFrameBarBuilder.HorizontalPositionType:
        """
        Getter for property: ( BaseFrameBarBuilder.HorizontalPositionType NXOpen.A) HorizontalPosition
         Returns the horizontal position   
            
         
        """
        pass
    @HorizontalPosition.setter
    def HorizontalPosition(self, horizontalPosition: BaseFrameBarBuilder.HorizontalPositionType):
        """
        Setter for property: ( BaseFrameBarBuilder.HorizontalPositionType NXOpen.A) HorizontalPosition
         Returns the horizontal position   
            
         
        """
        pass
    @property
    def Vertical(self) -> bool:
        """
        Getter for property: (bool) Vertical
         Returns the status of vertical framebar.  
           If true it automatically creates 
                    vertical framebar for views when ship axis matches with view axis
                    for vertical framebar.
                   
         
        """
        pass
    @Vertical.setter
    def Vertical(self, vertical: bool):
        """
        Setter for property: (bool) Vertical
         Returns the status of vertical framebar.  
           If true it automatically creates 
                    vertical framebar for views when ship axis matches with view axis
                    for vertical framebar.
                   
         
        """
        pass
    @property
    def VerticalDistance(self) -> float:
        """
        Getter for property: (float) VerticalDistance
         Returns the vertical distance   
            
         
        """
        pass
    @VerticalDistance.setter
    def VerticalDistance(self, verticalDistance: float):
        """
        Setter for property: (float) VerticalDistance
         Returns the vertical distance   
            
         
        """
        pass
    @property
    def VerticalPosition(self) -> BaseFrameBarBuilder.VerticalPositionType:
        """
        Getter for property: ( BaseFrameBarBuilder.VerticalPositionType NXOpen.A) VerticalPosition
         Returns the vertical position   
            
         
        """
        pass
    @VerticalPosition.setter
    def VerticalPosition(self, verticalPosition: BaseFrameBarBuilder.VerticalPositionType):
        """
        Setter for property: ( BaseFrameBarBuilder.VerticalPositionType NXOpen.A) VerticalPosition
         Returns the vertical position   
            
         
        """
        pass
class GdtOption(Enum):
    """
    Members Include: 
     |NotSet|  Does not inherit any GD and T display instances. 
     |InDrawingPlane|  inherit display instances of geometric tolerance features that are parallel to the drawing plane onto the drawing view. 
     |FromModelView|  inherit display instances of geometric tolerance features that exist in a particular modeling view (e.g. Top, Front, etc.). 

    """
    NotSet: int
    InDrawingPlane: int
    FromModelView: int
    @staticmethod
    def ValueOf(value: int) -> GdtOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class GeneralDisplayIdOption(Enum):
    """
    Members Include: 
     |NotSet|  None 
     |Orientation|  Orientation 
     |Name|  Name 

    """
    NotSet: int
    Orientation: int
    Name: int
    @staticmethod
    def ValueOf(value: int) -> GeneralDisplayIdOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class GeneralExtractedEdgesOption(Enum):
    """
    Members Include: 
     |NotSet|  None 
     |Associative|  Associative 
     |NonAssociative|  Non-Associative 

    """
    NotSet: int
    Associative: int
    NonAssociative: int
    @staticmethod
    def ValueOf(value: int) -> GeneralExtractedEdgesOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class GeneralToleranceOption(Enum):
    """
    Members Include: 
     |Coarse|  Coarse 
     |Medium|  Medium 
     |Standard|  Standard 
     |Fine|  Fine 
     |ExtraFine|  Extra Fine 
     |Customize|  Customize 

    """
    Coarse: int
    Medium: int
    Standard: int
    Fine: int
    ExtraFine: int
    Customize: int
    @staticmethod
    def ValueOf(value: int) -> GeneralToleranceOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class GeneralViewLockmethodOption(Enum):
    """
    Members Include: 
     |NotSet|  Normal 
     |Snapshot|  Snapshot 
     |Complete|  Locked 

    """
    NotSet: int
    Snapshot: int
    Complete: int
    @staticmethod
    def ValueOf(value: int) -> GeneralViewLockmethodOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class GeneralViewPreferences(NXOpen.Object): 
    """ Represents set of General View Preferencess applicable to drafting views. 
        These settings apply to any newly created base view.
     """
    @property
    def AngleDecimalPointFormat(self) -> DecimalPointCharacter:
        """
        Getter for property: ( DecimalPointCharacter NXOpen.P) AngleDecimalPointFormat
         Returns the decimal point character to use for view angle display.  
             
         
        """
        pass
    @AngleDecimalPointFormat.setter
    def AngleDecimalPointFormat(self, format: DecimalPointCharacter):
        """
        Setter for property: ( DecimalPointCharacter NXOpen.P) AngleDecimalPointFormat
         Returns the decimal point character to use for view angle display.  
             
         
        """
        pass
    @property
    def AngleFormat(self) -> AngleFormat:
        """
        Getter for property: ( AngleFormat NXOpen.P) AngleFormat
         Returns the format to use for view angle display.  
             
         
        """
        pass
    @AngleFormat.setter
    def AngleFormat(self, format: AngleFormat):
        """
        Setter for property: ( AngleFormat NXOpen.P) AngleFormat
         Returns the format to use for view angle display.  
             
         
        """
        pass
    @property
    def AnglePrecision(self) -> int:
        """
        Getter for property: (int) AnglePrecision
         Returns the precision to use for view angle display.  
             
         
        """
        pass
    @AnglePrecision.setter
    def AnglePrecision(self, precision: int):
        """
        Setter for property: (int) AnglePrecision
         Returns the precision to use for view angle display.  
             
         
        """
        pass
    @property
    def AutomaticAnchorPoint(self) -> bool:
        """
        Getter for property: (bool) AutomaticAnchorPoint
         Returns the status of Automatic anchor point   
            
         
        """
        pass
    @AutomaticAnchorPoint.setter
    def AutomaticAnchorPoint(self, automatic_anchor_point: bool):
        """
        Setter for property: (bool) AutomaticAnchorPoint
         Returns the status of Automatic anchor point   
            
         
        """
        pass
    @property
    def AutomaticUpdate(self) -> bool:
        """
        Getter for property: (bool) AutomaticUpdate
         Returns the status of Automatic Update.  
           if true, then position, 
                    hidden lines, silhouettes, view bounds, section views and 
                    section view details are updated after a model change else 
                    above items are not updated after a model change. 
                   
         
        """
        pass
    @AutomaticUpdate.setter
    def AutomaticUpdate(self, automatic_update: bool):
        """
        Setter for property: (bool) AutomaticUpdate
         Returns the status of Automatic Update.  
           if true, then position, 
                    hidden lines, silhouettes, view bounds, section views and 
                    section view details are updated after a model change else 
                    above items are not updated after a model change. 
                   
         
        """
        pass
    @property
    def BoundaryStatus(self) -> bool:
        """
        Getter for property: (bool) BoundaryStatus
         Returns the boundary status.  
           This option determines whether or not a view's out-of-date status 
                    includes its boundary. If True, the system checks the view boundary and marks it out of 
                    date if changes to non-solid geometry would cause the view's boundary to change when updated, 
                    else the system does not perform view boundary checks.
                   
         
        """
        pass
    @BoundaryStatus.setter
    def BoundaryStatus(self, boundary_status: bool):
        """
        Setter for property: (bool) BoundaryStatus
         Returns the boundary status.  
           This option determines whether or not a view's out-of-date status 
                    includes its boundary. If True, the system checks the view boundary and marks it out of 
                    date if changes to non-solid geometry would cause the view's boundary to change when updated, 
                    else the system does not perform view boundary checks.
                   
         
        """
        pass
    @property
    def Centerlines(self) -> bool:
        """
        Getter for property: (bool) Centerlines
         Returns the status of center line.  
           If true it automatically creates 
                    linear, cylindrical, and bolt circle centerlines (with a 
                    circular instance set) for views where the hole or pin axis
                    is perpendicular or parallel to the plane of the drawing view.
                   
         
        """
        pass
    @Centerlines.setter
    def Centerlines(self, centerlines: bool):
        """
        Setter for property: (bool) Centerlines
         Returns the status of center line.  
           If true it automatically creates 
                    linear, cylindrical, and bolt circle centerlines (with a 
                    circular instance set) for views where the hole or pin axis
                    is perpendicular or parallel to the plane of the drawing view.
                   
         
        """
        pass
    @property
    def DisplayId(self) -> GeneralDisplayIdOption:
        """
        Getter for property: ( GeneralDisplayIdOption NXOpen.P) DisplayId
         Returns the display identifier option for a member view.  
          
                   
         
        """
        pass
    @DisplayId.setter
    def DisplayId(self, option: GeneralDisplayIdOption):
        """
        Setter for property: ( GeneralDisplayIdOption NXOpen.P) DisplayId
         Returns the display identifier option for a member view.  
          
                   
         
        """
        pass
    @property
    def ExtractedEdges(self) -> GeneralExtractedEdgesOption:
        """
        Getter for property: ( GeneralExtractedEdgesOption NXOpen.P) ExtractedEdges
         Returns the extracted edge that provides an alternative way to display
                    model geometry in a drawing view.  
          
                   
         
        """
        pass
    @ExtractedEdges.setter
    def ExtractedEdges(self, edges_option: GeneralExtractedEdgesOption):
        """
        Setter for property: ( GeneralExtractedEdgesOption NXOpen.P) ExtractedEdges
         Returns the extracted edge that provides an alternative way to display
                    model geometry in a drawing view.  
          
                   
         
        """
        pass
    @property
    def FramebarHorizontal(self) -> bool:
        """
        Getter for property: (bool) FramebarHorizontal
         Returns the status of horizontal framebar.  
           If true it automatically creates 
                    horizontal framebar for views when ship axis matches with view axis
                    for horizontal framebar.
                   
         
        """
        pass
    @FramebarHorizontal.setter
    def FramebarHorizontal(self, horizontal: bool):
        """
        Setter for property: (bool) FramebarHorizontal
         Returns the status of horizontal framebar.  
           If true it automatically creates 
                    horizontal framebar for views when ship axis matches with view axis
                    for horizontal framebar.
                   
         
        """
        pass
    @property
    def FramebarVertical(self) -> bool:
        """
        Getter for property: (bool) FramebarVertical
         Returns the status of vertical framebar.  
           If true it automatically creates 
                    vertical framebar for views when ship axis matches with view axis
                    for vertical framebar.
                   
         
        """
        pass
    @FramebarVertical.setter
    def FramebarVertical(self, vertical: bool):
        """
        Setter for property: (bool) FramebarVertical
         Returns the status of vertical framebar.  
           If true it automatically creates 
                    vertical framebar for views when ship axis matches with view axis
                    for vertical framebar.
                   
         
        """
        pass
    @property
    def LegacyView(self) -> bool:
        """
        Getter for property: (bool) LegacyView
         Returns the leagcy view toggle on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @LegacyView.setter
    def LegacyView(self, legacyView: bool):
        """
        Setter for property: (bool) LegacyView
         Returns the leagcy view toggle on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def LightweightView(self) -> bool:
        """
        Getter for property: (bool) LightweightView
         Returns the view representation enum on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @LightweightView.setter
    def LightweightView(self, lightweightView: bool):
        """
        Setter for property: (bool) LightweightView
         Returns the view representation enum on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def LockmethodView(self) -> GeneralViewLockmethodOption:
        """
        Getter for property: ( GeneralViewLockmethodOption NXOpen.P) LockmethodView
         Returns the lock method setting on the Configuration tab of the View Style Dialog   
            
         
        """
        pass
    @LockmethodView.setter
    def LockmethodView(self, lockmethodView: GeneralViewLockmethodOption):
        """
        Setter for property: ( GeneralViewLockmethodOption NXOpen.P) LockmethodView
         Returns the lock method setting on the Configuration tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Reference(self) -> bool:
        """
        Getter for property: (bool) Reference
         Returns the status of reference.  
          A view can have a status of either Active or Reference. 
                    So if the status is True the view is considered a reference view else considered 
                    as an Active view.
                   
         
        """
        pass
    @Reference.setter
    def Reference(self, reference: bool):
        """
        Setter for property: (bool) Reference
         Returns the status of reference.  
          A view can have a status of either Active or Reference. 
                    So if the status is True the view is considered a reference view else considered 
                    as an Active view.
                   
         
        """
        pass
    @property
    def ShowAngleLeadingZeros(self) -> bool:
        """
        Getter for property: (bool) ShowAngleLeadingZeros
         Returns the status of leading zeros display in view angle.  
             
         
        """
        pass
    @ShowAngleLeadingZeros.setter
    def ShowAngleLeadingZeros(self, show: bool):
        """
        Setter for property: (bool) ShowAngleLeadingZeros
         Returns the status of leading zeros display in view angle.  
             
         
        """
        pass
    @property
    def ShowAngleTrailingZeros(self) -> bool:
        """
        Getter for property: (bool) ShowAngleTrailingZeros
         Returns the status of trailing zeros display in view angle.  
             
         
        """
        pass
    @ShowAngleTrailingZeros.setter
    def ShowAngleTrailingZeros(self, show: bool):
        """
        Setter for property: (bool) ShowAngleTrailingZeros
         Returns the status of trailing zeros display in view angle.  
             
         
        """
        pass
    @property
    def Silhouettes(self) -> bool:
        """
        Getter for property: (bool) Silhouettes
         Returns the status of silhouettes curves, if true silhouettes for 
                    selected drawing member views are added else silhouettes are removed 
                    from the selected member views.  
           
                   
         
        """
        pass
    @Silhouettes.setter
    def Silhouettes(self, silhouettes: bool):
        """
        Setter for property: (bool) Silhouettes
         Returns the status of silhouettes curves, if true silhouettes for 
                    selected drawing member views are added else silhouettes are removed 
                    from the selected member views.  
           
                   
         
        """
        pass
    @property
    def SnapshotView(self) -> bool:
        """
        Getter for property: (bool) SnapshotView
         Returns the snapshot toggle on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @SnapshotView.setter
    def SnapshotView(self, snapshotView: bool):
        """
        Setter for property: (bool) SnapshotView
         Returns the snapshot toggle on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Tolerance(self) -> float:
        """
        Getter for property: (float) Tolerance
         Returns the value of tolerance that specifies a chord height tolerance
                    value for silhouette and hidden line generation in a given 
                    drawing view.  
          
                   
         
        """
        pass
    @Tolerance.setter
    def Tolerance(self, tolerance: float):
        """
        Setter for property: (float) Tolerance
         Returns the value of tolerance that specifies a chord height tolerance
                    value for silhouette and hidden line generation in a given 
                    drawing view.  
          
                   
         
        """
        pass
    @property
    def UvGrid(self) -> bool:
        """
        Getter for property: (bool) UvGrid
         Returns the status of UV grid.  
           If true, grid curves for selected drawing
                    member views are added else the grid curves are removed from 
                    the selected member views.
                   
         
        """
        pass
    @UvGrid.setter
    def UvGrid(self, uv_grid: bool):
        """
        Setter for property: (bool) UvGrid
         Returns the status of UV grid.  
           If true, grid curves for selected drawing
                    member views are added else the grid curves are removed from 
                    the selected member views.
                   
         
        """
        pass
    @property
    def ViewQuality(self) -> GeneralViewQualityOption:
        """
        Getter for property: ( GeneralViewQualityOption NXOpen.P) ViewQuality
         Returns the view quality that provides alternative ways to display
                    geometry in a drawing member view.  
          
                   
         
        """
        pass
    @ViewQuality.setter
    def ViewQuality(self, view_quality_option: GeneralViewQualityOption):
        """
        Setter for property: ( GeneralViewQualityOption NXOpen.P) ViewQuality
         Returns the view quality that provides alternative ways to display
                    geometry in a drawing member view.  
          
                   
         
        """
        pass
    @property
    def ViewRepresentation(self) -> GeneralViewRepresentationOption:
        """
        Getter for property: ( GeneralViewRepresentationOption NXOpen.P) ViewRepresentation
         Returns the view representation enum on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @ViewRepresentation.setter
    def ViewRepresentation(self, viewRepresentation: GeneralViewRepresentationOption):
        """
        Setter for property: ( GeneralViewRepresentationOption NXOpen.P) ViewRepresentation
         Returns the view representation enum on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def WireframeColorSource(self) -> GeneralWireframeColorSourceOption:
        """
        Getter for property: ( GeneralWireframeColorSourceOption NXOpen.P) WireframeColorSource
         Returns the source of the wireframe color for a member view.  
          
                   
         
        """
        pass
    @WireframeColorSource.setter
    def WireframeColorSource(self, edges_option: GeneralWireframeColorSourceOption):
        """
        Setter for property: ( GeneralWireframeColorSourceOption NXOpen.P) WireframeColorSource
         Returns the source of the wireframe color for a member view.  
          
                   
         
        """
        pass
    @property
    def FrameBar() -> FrameBarPreferences:
        """
         Returns object for doing settings applicable to FrameBar 
        """
        pass
class GeneralViewQualityOption(Enum):
    """
    Members Include: 
     |Coarse|  Coarse 
     |Medium|  Medium 
     |Fine|  Fine 

    """
    Coarse: int
    Medium: int
    Fine: int
    @staticmethod
    def ValueOf(value: int) -> GeneralViewQualityOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class GeneralViewRepresentationOption(Enum):
    """
    Members Include: 
     |Exact|  Exact 
     |SmartLightweight|  Smart Lightweight 
     |Lightweight|  Lightweight 
     |PreNx85Exact|  Pre-NX 8.5 Exact 

    """
    Exact: int
    SmartLightweight: int
    Lightweight: int
    PreNx85Exact: int
    @staticmethod
    def ValueOf(value: int) -> GeneralViewRepresentationOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class GeneralWireframeColorSourceOption(Enum):
    """
    Members Include: 
     |FromBody|  From Body 
     |FromFace|  From Face 

    """
    FromBody: int
    FromFace: int
    @staticmethod
    def ValueOf(value: int) -> GeneralWireframeColorSourceOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class HiddenLineInterferingSolidsOption(Enum):
    """
    Members Include: 
     |NotSet|  None 
     |Yes|  Yes 
     |InterferenceCurves|  Interference Curves 

    """
    NotSet: int
    Yes: int
    InterferenceCurves: int
    @staticmethod
    def ValueOf(value: int) -> HiddenLineInterferingSolidsOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class HiddenLineSmallFeatureOption(Enum):
    """
    Members Include: 
     |ShowAll|  Show All 
     |Simplify|  Simplify 
     |Hide|  Hide 

    """
    ShowAll: int
    Simplify: int
    Hide: int
    @staticmethod
    def ValueOf(value: int) -> HiddenLineSmallFeatureOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class HiddenLinesViewPreferences(NXOpen.Object): 
    """ Represents set of Hidden Lines View Preferences applicable to drafting views. 
        Hidden Lines allows access to the hidden line display preferences for all 
        views added to the drawing.
     """
    @property
    def EdgesHiddenByEdges(self) -> bool:
        """
        Getter for property: (bool) EdgesHiddenByEdges
         Returns the staus of edges hidden by edges.  
           This allows to control the display of edges 
                    which are hidden by other overlapping edges.
                   
         
        """
        pass
    @EdgesHiddenByEdges.setter
    def EdgesHiddenByEdges(self, edges_hidden_by_edges: bool):
        """
        Setter for property: (bool) EdgesHiddenByEdges
         Returns the staus of edges hidden by edges.  
           This allows to control the display of edges 
                    which are hidden by other overlapping edges.
                   
         
        """
        pass
    @property
    def Hiddenline(self) -> bool:
        """
        Getter for property: (bool) Hiddenline
         Returns the status of hiddenline.  
           The status affects the appearance of lines in a member view.  
         
        """
        pass
    @Hiddenline.setter
    def Hiddenline(self, hiddenline: bool):
        """
        Setter for property: (bool) Hiddenline
         Returns the status of hiddenline.  
           The status affects the appearance of lines in a member view.  
         
        """
        pass
    @property
    def HiddenlineColor(self) -> int:
        """
        Getter for property: (int) HiddenlineColor
         Returns the color of hidden line.  
           The value should be between 1 and 216.   
         
        """
        pass
    @HiddenlineColor.setter
    def HiddenlineColor(self, color: int):
        """
        Setter for property: (int) HiddenlineColor
         Returns the color of hidden line.  
           The value should be between 1 and 216.   
         
        """
        pass
    @property
    def HiddenlineFont(self) -> Font:
        """
        Getter for property: ( Font NXOpen.P) HiddenlineFont
         Returns the font type of hidden line.  
            
         
        """
        pass
    @HiddenlineFont.setter
    def HiddenlineFont(self, font: Font):
        """
        Setter for property: ( Font NXOpen.P) HiddenlineFont
         Returns the font type of hidden line.  
            
         
        """
        pass
    @property
    def HiddenlineWidth(self) -> Width:
        """
        Getter for property: ( Width NXOpen.P) HiddenlineWidth
         Returns the width of hidden line or edges.  
             
         
        """
        pass
    @HiddenlineWidth.setter
    def HiddenlineWidth(self, width: Width):
        """
        Setter for property: ( Width NXOpen.P) HiddenlineWidth
         Returns the width of hidden line or edges.  
             
         
        """
        pass
    @property
    def IncludeModelCurves(self) -> bool:
        """
        Getter for property: (bool) IncludeModelCurves
         Returns the status of include model curves.  
           This allows the modeling curves 
                    in drawing views to participate in hidden line processing. Most useful where 
                    drawing are produced with wireframe curves or 2D sketch curves.
                   
         
        """
        pass
    @IncludeModelCurves.setter
    def IncludeModelCurves(self, include_model_curves: bool):
        """
        Setter for property: (bool) IncludeModelCurves
         Returns the status of include model curves.  
           This allows the modeling curves 
                    in drawing views to participate in hidden line processing. Most useful where 
                    drawing are produced with wireframe curves or 2D sketch curves.
                   
         
        """
        pass
    @property
    def InterferingSolids(self) -> bool:
        """
        Getter for property: (bool) InterferingSolids
         Returns the status of interfering solids.  
           This allows the correct rendering of hidden lines 
                    in a drawing member view with interfering solids.
                   
         
        """
        pass
    @InterferingSolids.setter
    def InterferingSolids(self, interfering_solids: bool):
        """
        Setter for property: (bool) InterferingSolids
         Returns the status of interfering solids.  
           This allows the correct rendering of hidden lines 
                    in a drawing member view with interfering solids.
                   
         
        """
        pass
    @property
    def InterferingSolidsOption(self) -> HiddenLineInterferingSolidsOption:
        """
        Getter for property: ( HiddenLineInterferingSolidsOption NXOpen.P) InterferingSolidsOption
         Returns the status of interfering solids.  
           This allows the correct rendering of hidden lines 
                    in a drawing member view with interfering solids.
                   
         
        """
        pass
    @InterferingSolidsOption.setter
    def InterferingSolidsOption(self, interfering_solids: HiddenLineInterferingSolidsOption):
        """
        Setter for property: ( HiddenLineInterferingSolidsOption NXOpen.P) InterferingSolidsOption
         Returns the status of interfering solids.  
           This allows the correct rendering of hidden lines 
                    in a drawing member view with interfering solids.
                   
         
        """
        pass
    @property
    def ReferenceEdgesOnly(self) -> bool:
        """
        Getter for property: (bool) ReferenceEdgesOnly
         Returns the status of reference edges only.  
          This controls the rendering of hidden edges with 
                    annotation. If True, only hidden edges referencing annotations are rendered.
                    Hidden edges not referenced by annotation are not rendered.
                   
         
        """
        pass
    @ReferenceEdgesOnly.setter
    def ReferenceEdgesOnly(self, reference_edges_only: bool):
        """
        Setter for property: (bool) ReferenceEdgesOnly
         Returns the status of reference edges only.  
          This controls the rendering of hidden edges with 
                    annotation. If True, only hidden edges referencing annotations are rendered.
                    Hidden edges not referenced by annotation are not rendered.
                   
         
        """
        pass
    @property
    def SelfHidden(self) -> bool:
        """
        Getter for property: (bool) SelfHidden
         Returns the status of self hidden.  
           This allows the rendering of edges hidden by 
                    their own solid in the selected hidden line color, font, and width settings. If False, 
                    the hidden line processing only processes the lines hidden by other solids.
                   
         
        """
        pass
    @SelfHidden.setter
    def SelfHidden(self, self_hidden: bool):
        """
        Setter for property: (bool) SelfHidden
         Returns the status of self hidden.  
           This allows the rendering of edges hidden by 
                    their own solid in the selected hidden line color, font, and width settings. If False, 
                    the hidden line processing only processes the lines hidden by other solids.
                   
         
        """
        pass
    @property
    def SmallFeature(self) -> HiddenLineSmallFeatureOption:
        """
        Getter for property: ( HiddenLineSmallFeatureOption NXOpen.P) SmallFeature
         Returns the small feature option.  
           This allows the simplification or removal of rendering of small features 
                    in large scale assembly drawings. Not all small features are considered for simplified rendering. 
                    Only if the boundary of a small feature lies completely within a face of the model is the small 
                    feature's display modified.
                   
         
        """
        pass
    @SmallFeature.setter
    def SmallFeature(self, small_feature: HiddenLineSmallFeatureOption):
        """
        Setter for property: ( HiddenLineSmallFeatureOption NXOpen.P) SmallFeature
         Returns the small feature option.  
           This allows the simplification or removal of rendering of small features 
                    in large scale assembly drawings. Not all small features are considered for simplified rendering. 
                    Only if the boundary of a small feature lies completely within a face of the model is the small 
                    feature's display modified.
                   
         
        """
        pass
    @property
    def SmallFeaturesTolerance(self) -> float:
        """
        Getter for property: (float) SmallFeaturesTolerance
         Returns the value of small features tolerance.  
            
         
        """
        pass
    @SmallFeaturesTolerance.setter
    def SmallFeaturesTolerance(self, small_features_tolerance: float):
        """
        Setter for property: (float) SmallFeaturesTolerance
         Returns the value of small features tolerance.  
            
         
        """
        pass
import NXOpen
class IBaseViewPreferences(NXOpen.Object): 
    """ Represents set of IBaseViewPreferences applicable to drafting views. """
    pass
import NXOpen
class IDetailViewPreferences(NXOpen.Object): 
    """ Represents set of Detail ViewPreferences applicable to drafting views. """
    pass
import NXOpen
class IGeneralViewPreferences(NXOpen.Object): 
    """ Represents set of General View Styles applicable to drafting views. """
    pass
import NXOpen
class IHiddenLinesViewPreferences(NXOpen.Object): 
    """ Represents set of HiddenLinesViewStyle applicable to drafting views. """
    pass
class IncludeModelCurvesOption(Enum):
    """
    Members Include: 
     |No|  Do not process model curves for hidden line processing 
     |Yes|  Process model curves for hidden line procesing 

    """
    No: int
    Yes: int
    @staticmethod
    def ValueOf(value: int) -> IncludeModelCurvesOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class InheritPmiPreferences(NXOpen.Object): 
    """ Represents set of InheritPmiPreferences applicable to drafting views. """
    @property
    def CrosshatchPmiLightweightSectionView(self) -> bool:
        """
        Getter for property: (bool) CrosshatchPmiLightweightSectionView
         Returns the cross-hatch setting for the current inherited PMI Lightweight Section View   
            
         
        """
        pass
    @CrosshatchPmiLightweightSectionView.setter
    def CrosshatchPmiLightweightSectionView(self, crosshatch: bool):
        """
        Setter for property: (bool) CrosshatchPmiLightweightSectionView
         Returns the cross-hatch setting for the current inherited PMI Lightweight Section View   
            
         
        """
        pass
    @property
    def InheritGdt(self) -> GdtOption:
        """
        Getter for property: ( GdtOption NXOpen.P) InheritGdt
         Returns the Inherit GD and T option   
            
         
        """
        pass
    @InheritGdt.setter
    def InheritGdt(self, gdt_option: GdtOption):
        """
        Setter for property: ( GdtOption NXOpen.P) InheritGdt
         Returns the Inherit GD and T option   
            
         
        """
        pass
    @property
    def InheritPmiMode(self) -> PmiOption:
        """
        Getter for property: ( PmiOption NXOpen.P) InheritPmiMode
         Returns the Status of inherit pmi mode.  
             
         
        """
        pass
    @InheritPmiMode.setter
    def InheritPmiMode(self, pmi_option: PmiOption):
        """
        Setter for property: ( PmiOption NXOpen.P) InheritPmiMode
         Returns the Status of inherit pmi mode.  
             
         
        """
        pass
    @property
    def InheritPmiToDrawing(self) -> bool:
        """
        Getter for property: (bool) InheritPmiToDrawing
         Returns the Status of pmi inherited to drawing.  
             
         
        """
        pass
    @InheritPmiToDrawing.setter
    def InheritPmiToDrawing(self, pmi_to_drawing: bool):
        """
        Setter for property: (bool) InheritPmiToDrawing
         Returns the Status of pmi inherited to drawing.  
             
         
        """
        pass
import NXOpen
class IOrientationViewPreferences(NXOpen.Object): 
    """ Represents set of IOrientationViewPreferences applicable to drafting views. """
    pass
import NXOpen
class IPerspectiveViewPreferences(NXOpen.Object): 
    """ Represents set of PerspectiveViewPreferences applicable to drafting views. """
    pass
import NXOpen
class IProjectedViewPreferences(NXOpen.Object): 
    """ Represents set of ProjectedViewPreferences applicable to drafting views. """
    pass
import NXOpen
class ISectionViewPreferences(NXOpen.Object): 
    """ Represents set of SectionViewPreferences applicable to drafting views. """
    pass
import NXOpen
class IShadingViewPreferences(NXOpen.Object): 
    """ Represents set of Shading ViewPreferences applicable to drafting views. """
    pass
import NXOpen
class ISmoothEdgesViewPreferences(NXOpen.Object): 
    """ Represents set of SmoothEdgesViewPreferences applicable to drafting views. """
    pass
import NXOpen
class IThreadsViewPreferences(NXOpen.Object): 
    """ Represents set of ThreadsViewPreferences applicable to drafting views. """
    pass
import NXOpen
class ITraceLinesViewPreferences(NXOpen.Object): 
    """ Represents interface for TraceLinesViewPreferences applicable to drafting views. """
    pass
import NXOpen
class IVirtualIntersectionsViewPreferences(NXOpen.Object): 
    """ Represents set of Virtual Intersections View Preferences applicable to drafting views. """
    pass
import NXOpen
class IVisibleLinesViewPreferences(NXOpen.Object): 
    """ Represents set of VisibleLinesViewPreferences applicable to drafting views. """
    pass
import NXOpen
class LoadDraftingStandardBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Preferences.LoadDraftingStandardBuilder
    """
    class LoadLevel(Enum):
        """
        Members Include: 
         |Shipped|  the shipped level 
         |Package|  the package level 
         |Site|  the site level    
         |Group|   the group level  
         |User|   the user level   

        """
        Shipped: int
        Package: int
        Site: int
        Group: int
        User: int
        @staticmethod
        def ValueOf(value: int) -> LoadDraftingStandardBuilder.LoadLevel:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Level(self) -> LoadDraftingStandardBuilder.LoadLevel:
        """
        Getter for property: ( LoadDraftingStandardBuilder.LoadLevel NXOpen.P) Level
         Returns the standard level   
            
         
        """
        pass
    @Level.setter
    def Level(self, level: LoadDraftingStandardBuilder.LoadLevel):
        """
        Setter for property: ( LoadDraftingStandardBuilder.LoadLevel NXOpen.P) Level
         Returns the standard level   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the standard name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the standard name   
            
         
        """
        pass
    @property
    def WelcomeMode(self) -> bool:
        """
        Getter for property: (bool) WelcomeMode
         Returns the welcome mode   
            
         
        """
        pass
    @WelcomeMode.setter
    def WelcomeMode(self, welcomeMode: bool):
        """
        Setter for property: (bool) WelcomeMode
         Returns the welcome mode   
            
         
        """
        pass
import NXOpen
class MidSurfacePreferencesBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Preferences.MidSurfacePreferencesBuilder """
    @property
    def DefiningOneColor(self) -> int:
        """
        Getter for property: (int) DefiningOneColor
         Returns the defining one color   
            
         
        """
        pass
    @DefiningOneColor.setter
    def DefiningOneColor(self, definingOneColor: int):
        """
        Setter for property: (int) DefiningOneColor
         Returns the defining one color   
            
         
        """
        pass
    @property
    def DefiningTwoColor(self) -> int:
        """
        Getter for property: (int) DefiningTwoColor
         Returns the defining two color   
            
         
        """
        pass
    @DefiningTwoColor.setter
    def DefiningTwoColor(self, definingTwoColor: int):
        """
        Setter for property: (int) DefiningTwoColor
         Returns the defining two color   
            
         
        """
        pass
    @property
    def InheritMidsurfaceColor(self) -> bool:
        """
        Getter for property: (bool) InheritMidsurfaceColor
         Returns the inherit midsurface color - Allow midsurface to inherit its color from the parent solid body   
            
         
        """
        pass
    @InheritMidsurfaceColor.setter
    def InheritMidsurfaceColor(self, inheritMidsurfaceColor: bool):
        """
        Setter for property: (bool) InheritMidsurfaceColor
         Returns the inherit midsurface color - Allow midsurface to inherit its color from the parent solid body   
            
         
        """
        pass
    @property
    def MidsurfaceColor(self) -> int:
        """
        Getter for property: (int) MidsurfaceColor
         Returns the midsurface color   
            
         
        """
        pass
    @MidsurfaceColor.setter
    def MidsurfaceColor(self, midsurfaceColor: int):
        """
        Setter for property: (int) MidsurfaceColor
         Returns the midsurface color   
            
         
        """
        pass
    @property
    def SideOneColor(self) -> int:
        """
        Getter for property: (int) SideOneColor
         Returns the color of side one   
            
         
        """
        pass
    @SideOneColor.setter
    def SideOneColor(self, sideOneColor: int):
        """
        Setter for property: (int) SideOneColor
         Returns the color of side one   
            
         
        """
        pass
    @property
    def SideTwoColor(self) -> int:
        """
        Getter for property: (int) SideTwoColor
         Returns the color of side two   
            
         
        """
        pass
    @SideTwoColor.setter
    def SideTwoColor(self, sideTwoColor: int):
        """
        Setter for property: (int) SideTwoColor
         Returns the color of side two   
            
         
        """
        pass
import NXOpen
class ModelingPreferencesBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Preferences.ModelingPreferencesBuilder """
    class ActionAfternterrupt(Enum):
        """
        Members Include: 
         |MakeLastSuccessfulFeatureCurrent| 
         |Undo| 

        """
        MakeLastSuccessfulFeatureCurrent: int
        Undo: int
        @staticmethod
        def ValueOf(value: int) -> ModelingPreferencesBuilder.ActionAfternterrupt:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class BodyType(Enum):
        """
        Members Include: 
         |Solid| 
         |Sheet| 

        """
        Solid: int
        Sheet: int
        @staticmethod
        def ValueOf(value: int) -> ModelingPreferencesBuilder.BodyType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class C0KnotLineColor(Enum):
        """
        Members Include: 
         |BodyColor| 
         |SpecificColor| 

        """
        BodyColor: int
        SpecificColor: int
        @staticmethod
        def ValueOf(value: int) -> ModelingPreferencesBuilder.C0KnotLineColor:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class C1KnotLineColor(Enum):
        """
        Members Include: 
         |BodyColor| 
         |SpecificColor| 

        """
        BodyColor: int
        SpecificColor: int
        @staticmethod
        def ValueOf(value: int) -> ModelingPreferencesBuilder.C1KnotLineColor:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class C2KnotLineColor(Enum):
        """
        Members Include: 
         |BodyColor| 
         |SpecificColor| 

        """
        BodyColor: int
        SpecificColor: int
        @staticmethod
        def ValueOf(value: int) -> ModelingPreferencesBuilder.C2KnotLineColor:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CurveFitMethod(Enum):
        """
        Members Include: 
         |Cubic| 
         |Quintic| 
         |Advanced| 

        """
        Cubic: int
        Quintic: int
        Advanced: int
        @staticmethod
        def ValueOf(value: int) -> ModelingPreferencesBuilder.CurveFitMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DeleteChildFeatures(Enum):
        """
        Members Include: 
         |Yes| 
         |No| 
         |Ask| 

        """
        Yes: int
        No: int
        Ask: int
        @staticmethod
        def ValueOf(value: int) -> ModelingPreferencesBuilder.DeleteChildFeatures:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DensityUnits(Enum):
        """
        Members Include: 
         |Lbmin3| 
         |Lbmft3| 
         |Gcm3| 
         |Kgm3| 

        """
        Lbmin3: int
        Lbmft3: int
        Gcm3: int
        Kgm3: int
        @staticmethod
        def ValueOf(value: int) -> ModelingPreferencesBuilder.DensityUnits:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DynamicUpdateMode(Enum):
        """
        Members Include: 
         |NotSet| 
         |Incremental| 
         |Continuous| 

        """
        NotSet: int
        Incremental: int
        Continuous: int
        @staticmethod
        def ValueOf(value: int) -> ModelingPreferencesBuilder.DynamicUpdateMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DynamicsUpdateLevel(Enum):
        """
        Members Include: 
         |First| 
         |All| 

        """
        First: int
        All: int
        @staticmethod
        def ValueOf(value: int) -> ModelingPreferencesBuilder.DynamicsUpdateLevel:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EditPoleColor(Enum):
        """
        Members Include: 
         |BodyColor| 
         |SpecificColor| 

        """
        BodyColor: int
        SpecificColor: int
        @staticmethod
        def ValueOf(value: int) -> ModelingPreferencesBuilder.EditPoleColor:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EditPoleStyle(Enum):
        """
        Members Include: 
         |ThreeDimensionSphere| 
         |OpenCircle| 
         |FilledCircle| 
         |PlusSign| 
         |Cross| 

        """
        ThreeDimensionSphere: int
        OpenCircle: int
        FilledCircle: int
        PlusSign: int
        Cross: int
        @staticmethod
        def ValueOf(value: int) -> ModelingPreferencesBuilder.EditPoleStyle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EditPolylineColor(Enum):
        """
        Members Include: 
         |BodyColor| 
         |SpecificColor| 

        """
        BodyColor: int
        SpecificColor: int
        @staticmethod
        def ValueOf(value: int) -> ModelingPreferencesBuilder.EditPolylineColor:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EndPointColor(Enum):
        """
        Members Include: 
         |CurveColor| 
         |SpecificColor| 

        """
        CurveColor: int
        SpecificColor: int
        @staticmethod
        def ValueOf(value: int) -> ModelingPreferencesBuilder.EndPointColor:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EndPointStyle(Enum):
        """
        Members Include: 
         |OpenCircle| 
         |FilledCircle| 
         |PlusSign| 
         |Cross| 
         |Point| 
         |Asterisk| 
         |PoundSign| 
         |FilledSquare| 
         |FilledTriangle| 
         |FilledDiamond| 
         |Centerline| 

        """
        OpenCircle: int
        FilledCircle: int
        PlusSign: int
        Cross: int
        Point: int
        Asterisk: int
        PoundSign: int
        FilledSquare: int
        FilledTriangle: int
        FilledDiamond: int
        Centerline: int
        @staticmethod
        def ValueOf(value: int) -> ModelingPreferencesBuilder.EndPointStyle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FaceModifiedByBoolean(Enum):
        """
        Members Include: 
         |InheritfromTargetBody| 
         |InheritfromToolBody| 

        """
        InheritfromTargetBody: int
        InheritfromToolBody: int
        @staticmethod
        def ValueOf(value: int) -> ModelingPreferencesBuilder.FaceModifiedByBoolean:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FeatureDoubleClickAction(Enum):
        """
        Members Include: 
         |EditParameter| 
         |EditwithRollback| 

        """
        EditParameter: int
        EditwithRollback: int
        @staticmethod
        def ValueOf(value: int) -> ModelingPreferencesBuilder.FeatureDoubleClickAction:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class GridLineColor(Enum):
        """
        Members Include: 
         |BodyColor| 
         |SpecificColor| 

        """
        BodyColor: int
        SpecificColor: int
        @staticmethod
        def ValueOf(value: int) -> ModelingPreferencesBuilder.GridLineColor:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LinkOrExtractGeometry(Enum):
        """
        Members Include: 
         |InheritfromParent| 
         |InheritObjectPreferences| 

        """
        InheritfromParent: int
        InheritObjectPreferences: int
        @staticmethod
        def ValueOf(value: int) -> ModelingPreferencesBuilder.LinkOrExtractGeometry:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ModelDelayAndUpdateGranularity(Enum):
        """
        Members Include: 
         |Group| 
         |Feature| 

        """
        Group: int
        Feature: int
        @staticmethod
        def ValueOf(value: int) -> ModelingPreferencesBuilder.ModelDelayAndUpdateGranularity:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ModelingMode(Enum):
        """
        Members Include: 
         |HistoryFree| 
         |History| 

        """
        HistoryFree: int
        History: int
        @staticmethod
        def ValueOf(value: int) -> ModelingPreferencesBuilder.ModelingMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class NewFaces(Enum):
        """
        Members Include: 
         |InheritfromParent| 
         |InheritObjectPreferences| 

        """
        InheritfromParent: int
        InheritObjectPreferences: int
        @staticmethod
        def ValueOf(value: int) -> ModelingPreferencesBuilder.NewFaces:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PlanarFaceType(Enum):
        """
        Members Include: 
         |Plane| 
         |Bsurface| 

        """
        Plane: int
        Bsurface: int
        @staticmethod
        def ValueOf(value: int) -> ModelingPreferencesBuilder.PlanarFaceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PoleColor(Enum):
        """
        Members Include: 
         |BodyColor| 
         |SpecificColor| 

        """
        BodyColor: int
        SpecificColor: int
        @staticmethod
        def ValueOf(value: int) -> ModelingPreferencesBuilder.PoleColor:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PoleStyle(Enum):
        """
        Members Include: 
         |ThreeDimensionSphere| 
         |OpenCircle| 
         |FilledCircle| 
         |PlusSign| 
         |Cross| 

        """
        ThreeDimensionSphere: int
        OpenCircle: int
        FilledCircle: int
        PlusSign: int
        Cross: int
        @staticmethod
        def ValueOf(value: int) -> ModelingPreferencesBuilder.PoleStyle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PolylineColor(Enum):
        """
        Members Include: 
         |BodyColor| 
         |SpecificColor| 

        """
        BodyColor: int
        SpecificColor: int
        @staticmethod
        def ValueOf(value: int) -> ModelingPreferencesBuilder.PolylineColor:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PreviewResolution(Enum):
        """
        Members Include: 
         |NotSet| 
         |Coarse| 
         |Standard| 
         |Fine| 
         |ExtraFine| 
         |SuperFine| 
         |UltraFine| 

        """
        NotSet: int
        Coarse: int
        Standard: int
        Fine: int
        ExtraFine: int
        SuperFine: int
        UltraFine: int
        @staticmethod
        def ValueOf(value: int) -> ModelingPreferencesBuilder.PreviewResolution:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SketchDoubleClickAction(Enum):
        """
        Members Include: 
         |EditwithRollback| 
         |DirectEdit| 

        """
        EditwithRollback: int
        DirectEdit: int
        @staticmethod
        def ValueOf(value: int) -> ModelingPreferencesBuilder.SketchDoubleClickAction:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SplineDefaultClickAction(Enum):
        """
        Members Include: 
         |StudioSpline| 
         |XForm| 

        """
        StudioSpline: int
        XForm: int
        @staticmethod
        def ValueOf(value: int) -> ModelingPreferencesBuilder.SplineDefaultClickAction:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SurfaceExtension(Enum):
        """
        Members Include: 
         |Linear| 
         |Soft| 

        """
        Linear: int
        Soft: int
        @staticmethod
        def ValueOf(value: int) -> ModelingPreferencesBuilder.SurfaceExtension:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ActionAfterInterruptValue(self) -> ModelingPreferencesBuilder.ActionAfternterrupt:
        """
        Getter for property: ( ModelingPreferencesBuilder.ActionAfternterrupt NXOpen.P) ActionAfterInterruptValue
         Returns the action after interrupt value   
            
         
        """
        pass
    @ActionAfterInterruptValue.setter
    def ActionAfterInterruptValue(self, actionAfterInterruptValue: ModelingPreferencesBuilder.ActionAfternterrupt):
        """
        Setter for property: ( ModelingPreferencesBuilder.ActionAfternterrupt NXOpen.P) ActionAfterInterruptValue
         Returns the action after interrupt value   
            
         
        """
        pass
    @property
    def ActivateTrimmedAnimation(self) -> bool:
        """
        Getter for property: (bool) ActivateTrimmedAnimation
         Returns the activate trimmed animation   
            
         
        """
        pass
    @ActivateTrimmedAnimation.setter
    def ActivateTrimmedAnimation(self, activateTrimmedAnimation: bool):
        """
        Setter for property: (bool) ActivateTrimmedAnimation
         Returns the activate trimmed animation   
            
         
        """
        pass
    @property
    def AngleTolerance(self) -> float:
        """
        Getter for property: (float) AngleTolerance
         Returns the angle tolerance   
            
         
        """
        pass
    @AngleTolerance.setter
    def AngleTolerance(self, angleTolerance: float):
        """
        Setter for property: (float) AngleTolerance
         Returns the angle tolerance   
            
         
        """
        pass
    @property
    def AssociativeFreeFormEdit(self) -> bool:
        """
        Getter for property: (bool) AssociativeFreeFormEdit
         Returns the associative free form edit   
            
         
        """
        pass
    @AssociativeFreeFormEdit.setter
    def AssociativeFreeFormEdit(self, associativeFreeFormEdit: bool):
        """
        Setter for property: (bool) AssociativeFreeFormEdit
         Returns the associative free form edit   
            
         
        """
        pass
    @property
    def BodyTypeValue(self) -> ModelingPreferencesBuilder.BodyType:
        """
        Getter for property: ( ModelingPreferencesBuilder.BodyType NXOpen.P) BodyTypeValue
         Returns the body type value   
            
         
        """
        pass
    @BodyTypeValue.setter
    def BodyTypeValue(self, bodyTypeValue: ModelingPreferencesBuilder.BodyType):
        """
        Setter for property: ( ModelingPreferencesBuilder.BodyType NXOpen.P) BodyTypeValue
         Returns the body type value   
            
         
        """
        pass
    @property
    def C0KnotLineColorValue(self) -> ModelingPreferencesBuilder.C0KnotLineColor:
        """
        Getter for property: ( ModelingPreferencesBuilder.C0KnotLineColor NXOpen.P) C0KnotLineColorValue
         Returns the c0 knot line color value   
            
         
        """
        pass
    @C0KnotLineColorValue.setter
    def C0KnotLineColorValue(self, c0KnotLineColorValue: ModelingPreferencesBuilder.C0KnotLineColor):
        """
        Setter for property: ( ModelingPreferencesBuilder.C0KnotLineColor NXOpen.P) C0KnotLineColorValue
         Returns the c0 knot line color value   
            
         
        """
        pass
    @property
    def C0KnotLineStyleValue(self) -> NXOpen.LineFontBuilder:
        """
        Getter for property: ( NXOpen.LineFontBuilder) C0KnotLineStyleValue
         Returns the c0 knot line style value   
            
         
        """
        pass
    @property
    def C1KnotLineColorValue(self) -> ModelingPreferencesBuilder.C1KnotLineColor:
        """
        Getter for property: ( ModelingPreferencesBuilder.C1KnotLineColor NXOpen.P) C1KnotLineColorValue
         Returns the c1 knot line color value   
            
         
        """
        pass
    @C1KnotLineColorValue.setter
    def C1KnotLineColorValue(self, c1KnotLineColorValue: ModelingPreferencesBuilder.C1KnotLineColor):
        """
        Setter for property: ( ModelingPreferencesBuilder.C1KnotLineColor NXOpen.P) C1KnotLineColorValue
         Returns the c1 knot line color value   
            
         
        """
        pass
    @property
    def C1KnotLineStyleValue(self) -> NXOpen.LineFontBuilder:
        """
        Getter for property: ( NXOpen.LineFontBuilder) C1KnotLineStyleValue
         Returns the c1 knot line style value   
            
         
        """
        pass
    @property
    def C2KnotLineColorValue(self) -> ModelingPreferencesBuilder.C2KnotLineColor:
        """
        Getter for property: ( ModelingPreferencesBuilder.C2KnotLineColor NXOpen.P) C2KnotLineColorValue
         Returns the c2 knot line color value   
            
         
        """
        pass
    @C2KnotLineColorValue.setter
    def C2KnotLineColorValue(self, c2KnotLineColorValue: ModelingPreferencesBuilder.C2KnotLineColor):
        """
        Setter for property: ( ModelingPreferencesBuilder.C2KnotLineColor NXOpen.P) C2KnotLineColorValue
         Returns the c2 knot line color value   
            
         
        """
        pass
    @property
    def C2KnotLineStyleValue(self) -> NXOpen.LineFontBuilder:
        """
        Getter for property: ( NXOpen.LineFontBuilder) C2KnotLineStyleValue
         Returns the c2 knot line style value   
            
         
        """
        pass
    @property
    def CopyAttributesOnSplit(self) -> bool:
        """
        Getter for property: (bool) CopyAttributesOnSplit
         Returns the copy attributes to faces and edges on split value   
            
         
        """
        pass
    @CopyAttributesOnSplit.setter
    def CopyAttributesOnSplit(self, copy_attributes_on_split: bool):
        """
        Setter for property: (bool) CopyAttributesOnSplit
         Returns the copy attributes to faces and edges on split value   
            
         
        """
        pass
    @property
    def CurveFitMethodValue(self) -> ModelingPreferencesBuilder.CurveFitMethod:
        """
        Getter for property: ( ModelingPreferencesBuilder.CurveFitMethod NXOpen.P) CurveFitMethodValue
         Returns the curve fit method value   
            
         
        """
        pass
    @CurveFitMethodValue.setter
    def CurveFitMethodValue(self, curveFitMethodValue: ModelingPreferencesBuilder.CurveFitMethod):
        """
        Setter for property: ( ModelingPreferencesBuilder.CurveFitMethod NXOpen.P) CurveFitMethodValue
         Returns the curve fit method value   
            
         
        """
        pass
    @property
    def DelayModelUpdate(self) -> bool:
        """
        Getter for property: (bool) DelayModelUpdate
         Returns the delay model update   
            
         
        """
        pass
    @DelayModelUpdate.setter
    def DelayModelUpdate(self, delayModelUpdate: bool):
        """
        Setter for property: (bool) DelayModelUpdate
         Returns the delay model update   
            
         
        """
        pass
    @property
    def DeleteChildFeaturesValue(self) -> ModelingPreferencesBuilder.DeleteChildFeatures:
        """
        Getter for property: ( ModelingPreferencesBuilder.DeleteChildFeatures NXOpen.P) DeleteChildFeaturesValue
         Returns the delete child features value   
            
         
        """
        pass
    @DeleteChildFeaturesValue.setter
    def DeleteChildFeaturesValue(self, deleteChildFeaturesValue: ModelingPreferencesBuilder.DeleteChildFeatures):
        """
        Setter for property: ( ModelingPreferencesBuilder.DeleteChildFeatures NXOpen.P) DeleteChildFeaturesValue
         Returns the delete child features value   
            
         
        """
        pass
    @property
    def DensityUnitsValue(self) -> ModelingPreferencesBuilder.DensityUnits:
        """
        Getter for property: ( ModelingPreferencesBuilder.DensityUnits NXOpen.P) DensityUnitsValue
         Returns the density units value   
            
         
        """
        pass
    @DensityUnitsValue.setter
    def DensityUnitsValue(self, densityUnitsValue: ModelingPreferencesBuilder.DensityUnits):
        """
        Setter for property: ( ModelingPreferencesBuilder.DensityUnits NXOpen.P) DensityUnitsValue
         Returns the density units value   
            
         
        """
        pass
    @property
    def DensityValue(self) -> float:
        """
        Getter for property: (float) DensityValue
         Returns the density value   
            
         
        """
        pass
    @DensityValue.setter
    def DensityValue(self, densityValue: float):
        """
        Setter for property: (float) DensityValue
         Returns the density value   
            
         
        """
        pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance   
            
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance   
            
         
        """
        pass
    @property
    def DynamicsUpdateLevelValue(self) -> ModelingPreferencesBuilder.DynamicsUpdateLevel:
        """
        Getter for property: ( ModelingPreferencesBuilder.DynamicsUpdateLevel NXOpen.P) DynamicsUpdateLevelValue
         Returns the dynamics update level value   
            
         
        """
        pass
    @DynamicsUpdateLevelValue.setter
    def DynamicsUpdateLevelValue(self, dynamicsUpdateLevelValue: ModelingPreferencesBuilder.DynamicsUpdateLevel):
        """
        Setter for property: ( ModelingPreferencesBuilder.DynamicsUpdateLevel NXOpen.P) DynamicsUpdateLevelValue
         Returns the dynamics update level value   
            
         
        """
        pass
    @property
    def DynamicsUpdateModeValue(self) -> ModelingPreferencesBuilder.DynamicUpdateMode:
        """
        Getter for property: ( ModelingPreferencesBuilder.DynamicUpdateMode NXOpen.P) DynamicsUpdateModeValue
         Returns the dynamics update mode value   
            
         
        """
        pass
    @DynamicsUpdateModeValue.setter
    def DynamicsUpdateModeValue(self, dynamicsUpdateModeValue: ModelingPreferencesBuilder.DynamicUpdateMode):
        """
        Setter for property: ( ModelingPreferencesBuilder.DynamicUpdateMode NXOpen.P) DynamicsUpdateModeValue
         Returns the dynamics update mode value   
            
         
        """
        pass
    @property
    def EditDuringUpdateDialogOnError(self) -> bool:
        """
        Getter for property: (bool) EditDuringUpdateDialogOnError
         Returns the update dialog on warning   
            
         
        """
        pass
    @EditDuringUpdateDialogOnError.setter
    def EditDuringUpdateDialogOnError(self, updateOnError: bool):
        """
        Setter for property: (bool) EditDuringUpdateDialogOnError
         Returns the update dialog on warning   
            
         
        """
        pass
    @property
    def EditDuringUpdateDialogOnWarning(self) -> bool:
        """
        Getter for property: (bool) EditDuringUpdateDialogOnWarning
         Returns the update dialog on warning   
            
         
        """
        pass
    @EditDuringUpdateDialogOnWarning.setter
    def EditDuringUpdateDialogOnWarning(self, updateOnWarning: bool):
        """
        Setter for property: (bool) EditDuringUpdateDialogOnWarning
         Returns the update dialog on warning   
            
         
        """
        pass
    @property
    def EditPoleColorValue(self) -> ModelingPreferencesBuilder.EditPoleColor:
        """
        Getter for property: ( ModelingPreferencesBuilder.EditPoleColor NXOpen.P) EditPoleColorValue
         Returns the edit pole color value   
            
         
        """
        pass
    @EditPoleColorValue.setter
    def EditPoleColorValue(self, editPoleColorValue: ModelingPreferencesBuilder.EditPoleColor):
        """
        Setter for property: ( ModelingPreferencesBuilder.EditPoleColor NXOpen.P) EditPoleColorValue
         Returns the edit pole color value   
            
         
        """
        pass
    @property
    def EditPoleStyleValue(self) -> ModelingPreferencesBuilder.EditPoleStyle:
        """
        Getter for property: ( ModelingPreferencesBuilder.EditPoleStyle NXOpen.P) EditPoleStyleValue
         Returns the edit pole style value   
            
         
        """
        pass
    @EditPoleStyleValue.setter
    def EditPoleStyleValue(self, editPoleStyleValue: ModelingPreferencesBuilder.EditPoleStyle):
        """
        Setter for property: ( ModelingPreferencesBuilder.EditPoleStyle NXOpen.P) EditPoleStyleValue
         Returns the edit pole style value   
            
         
        """
        pass
    @property
    def EditPolylineColorValue(self) -> ModelingPreferencesBuilder.EditPolylineColor:
        """
        Getter for property: ( ModelingPreferencesBuilder.EditPolylineColor NXOpen.P) EditPolylineColorValue
         Returns the edit polyline color value   
            
         
        """
        pass
    @EditPolylineColorValue.setter
    def EditPolylineColorValue(self, editPolylineColorValue: ModelingPreferencesBuilder.EditPolylineColor):
        """
        Setter for property: ( ModelingPreferencesBuilder.EditPolylineColor NXOpen.P) EditPolylineColorValue
         Returns the edit polyline color value   
            
         
        """
        pass
    @property
    def EditPolylineStyleValue(self) -> NXOpen.LineFontBuilder:
        """
        Getter for property: ( NXOpen.LineFontBuilder) EditPolylineStyleValue
         Returns the edit polyline style value   
            
         
        """
        pass
    @property
    def EditSpecifcPoleColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) EditSpecifcPoleColor
         Returns the edit specifc pole color   
            
         
        """
        pass
    @EditSpecifcPoleColor.setter
    def EditSpecifcPoleColor(self, editSpecifcPoleColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) EditSpecifcPoleColor
         Returns the edit specifc pole color   
            
         
        """
        pass
    @property
    def EditSpecificPolylineColorValue(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) EditSpecificPolylineColorValue
         Returns the edit specific polyline color value   
            
         
        """
        pass
    @EditSpecificPolylineColorValue.setter
    def EditSpecificPolylineColorValue(self, editSpecificPolylineColorValue: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) EditSpecificPolylineColorValue
         Returns the edit specific polyline color value   
            
         
        """
        pass
    @property
    def EndPointColorValue(self) -> ModelingPreferencesBuilder.EndPointColor:
        """
        Getter for property: ( ModelingPreferencesBuilder.EndPointColor NXOpen.P) EndPointColorValue
         Returns the end point color value   
            
         
        """
        pass
    @EndPointColorValue.setter
    def EndPointColorValue(self, endPointColorValue: ModelingPreferencesBuilder.EndPointColor):
        """
        Setter for property: ( ModelingPreferencesBuilder.EndPointColor NXOpen.P) EndPointColorValue
         Returns the end point color value   
            
         
        """
        pass
    @property
    def EndPointStyleValue(self) -> ModelingPreferencesBuilder.EndPointStyle:
        """
        Getter for property: ( ModelingPreferencesBuilder.EndPointStyle NXOpen.P) EndPointStyleValue
         Returns the end point style value   
            
         
        """
        pass
    @EndPointStyleValue.setter
    def EndPointStyleValue(self, endPointStyleValue: ModelingPreferencesBuilder.EndPointStyle):
        """
        Setter for property: ( ModelingPreferencesBuilder.EndPointStyle NXOpen.P) EndPointStyleValue
         Returns the end point style value   
            
         
        """
        pass
    @property
    def FacesModifiedByBooleanValue(self) -> ModelingPreferencesBuilder.FaceModifiedByBoolean:
        """
        Getter for property: ( ModelingPreferencesBuilder.FaceModifiedByBoolean NXOpen.P) FacesModifiedByBooleanValue
         Returns the faces modified by boolean value   
            
         
        """
        pass
    @FacesModifiedByBooleanValue.setter
    def FacesModifiedByBooleanValue(self, facesModifiedByBooleanValue: ModelingPreferencesBuilder.FaceModifiedByBoolean):
        """
        Setter for property: ( ModelingPreferencesBuilder.FaceModifiedByBoolean NXOpen.P) FacesModifiedByBooleanValue
         Returns the faces modified by boolean value   
            
         
        """
        pass
    @property
    def FacetAngleTolerance(self) -> float:
        """
        Getter for property: (float) FacetAngleTolerance
         Returns the facet angle tolerance   
            
         
        """
        pass
    @FacetAngleTolerance.setter
    def FacetAngleTolerance(self, facetAngleTolerance: float):
        """
        Setter for property: (float) FacetAngleTolerance
         Returns the facet angle tolerance   
            
         
        """
        pass
    @property
    def FacetDistanceTolerance(self) -> float:
        """
        Getter for property: (float) FacetDistanceTolerance
         Returns the facet distance tolerance   
            
         
        """
        pass
    @FacetDistanceTolerance.setter
    def FacetDistanceTolerance(self, facetDistanceTolerance: float):
        """
        Setter for property: (float) FacetDistanceTolerance
         Returns the facet distance tolerance   
            
         
        """
        pass
    @property
    def FeatureDoubleClickActionValue(self) -> ModelingPreferencesBuilder.FeatureDoubleClickAction:
        """
        Getter for property: ( ModelingPreferencesBuilder.FeatureDoubleClickAction NXOpen.P) FeatureDoubleClickActionValue
         Returns the feature double click action value   
            
         
        """
        pass
    @FeatureDoubleClickActionValue.setter
    def FeatureDoubleClickActionValue(self, featureDoubleClickActionValue: ModelingPreferencesBuilder.FeatureDoubleClickAction):
        """
        Setter for property: ( ModelingPreferencesBuilder.FeatureDoubleClickAction NXOpen.P) FeatureDoubleClickActionValue
         Returns the feature double click action value   
            
         
        """
        pass
    @property
    def GridLineColorValue(self) -> ModelingPreferencesBuilder.GridLineColor:
        """
        Getter for property: ( ModelingPreferencesBuilder.GridLineColor NXOpen.P) GridLineColorValue
         Returns the grid line color value   
            
         
        """
        pass
    @GridLineColorValue.setter
    def GridLineColorValue(self, gridLineColorValue: ModelingPreferencesBuilder.GridLineColor):
        """
        Setter for property: ( ModelingPreferencesBuilder.GridLineColor NXOpen.P) GridLineColorValue
         Returns the grid line color value   
            
         
        """
        pass
    @property
    def GridLineStyleValue(self) -> NXOpen.LineFontBuilder:
        """
        Getter for property: ( NXOpen.LineFontBuilder) GridLineStyleValue
         Returns the grid line style value   
            
         
        """
        pass
    @property
    def LimitChordLengthToMax(self) -> bool:
        """
        Getter for property: (bool) LimitChordLengthToMax
         Returns the limit chord length to max   
            
         
        """
        pass
    @LimitChordLengthToMax.setter
    def LimitChordLengthToMax(self, limitChordLengthToMax: bool):
        """
        Setter for property: (bool) LimitChordLengthToMax
         Returns the limit chord length to max   
            
         
        """
        pass
    @property
    def LimitFacetWidthToMaximum(self) -> bool:
        """
        Getter for property: (bool) LimitFacetWidthToMaximum
         Returns the limit facet width to maximum   
            
         
        """
        pass
    @LimitFacetWidthToMaximum.setter
    def LimitFacetWidthToMaximum(self, limitFacetWidthToMaximum: bool):
        """
        Setter for property: (bool) LimitFacetWidthToMaximum
         Returns the limit facet width to maximum   
            
         
        """
        pass
    @property
    def LinkOrExtractGeometryValue(self) -> ModelingPreferencesBuilder.LinkOrExtractGeometry:
        """
        Getter for property: ( ModelingPreferencesBuilder.LinkOrExtractGeometry NXOpen.P) LinkOrExtractGeometryValue
         Returns the link or extract geometry value   
            
         
        """
        pass
    @LinkOrExtractGeometryValue.setter
    def LinkOrExtractGeometryValue(self, linkOrExtractGeometryValue: ModelingPreferencesBuilder.LinkOrExtractGeometry):
        """
        Setter for property: ( ModelingPreferencesBuilder.LinkOrExtractGeometry NXOpen.P) LinkOrExtractGeometryValue
         Returns the link or extract geometry value   
            
         
        """
        pass
    @property
    def MakeCurrentFeatureOnError(self) -> bool:
        """
        Getter for property: (bool) MakeCurrentFeatureOnError
         Returns the make current feature on error   
            
         
        """
        pass
    @MakeCurrentFeatureOnError.setter
    def MakeCurrentFeatureOnError(self, makeCurrentFeatureOnError: bool):
        """
        Setter for property: (bool) MakeCurrentFeatureOnError
         Returns the make current feature on error   
            
         
        """
        pass
    @property
    def MakeSketchInternal(self) -> bool:
        """
        Getter for property: (bool) MakeSketchInternal
         Returns the make sketch internal   
            
         
        """
        pass
    @MakeSketchInternal.setter
    def MakeSketchInternal(self, makeSketchInternal: bool):
        """
        Setter for property: (bool) MakeSketchInternal
         Returns the make sketch internal   
            
         
        """
        pass
    @property
    def MaxChordLength(self) -> float:
        """
        Getter for property: (float) MaxChordLength
         Returns the max chord length   
            
         
        """
        pass
    @MaxChordLength.setter
    def MaxChordLength(self, maxChordLength: float):
        """
        Setter for property: (float) MaxChordLength
         Returns the max chord length   
            
         
        """
        pass
    @property
    def MaxFacetWidth(self) -> float:
        """
        Getter for property: (float) MaxFacetWidth
         Returns the max facet width   
            
         
        """
        pass
    @MaxFacetWidth.setter
    def MaxFacetWidth(self, maxFacetWidth: float):
        """
        Setter for property: (float) MaxFacetWidth
         Returns the max facet width   
            
         
        """
        pass
    @property
    def MaxRebuildDegree(self) -> int:
        """
        Getter for property: (int) MaxRebuildDegree
         Returns the max rebuild degree   
            
         
        """
        pass
    @MaxRebuildDegree.setter
    def MaxRebuildDegree(self, maxRebuildDegree: int):
        """
        Setter for property: (int) MaxRebuildDegree
         Returns the max rebuild degree   
            
         
        """
        pass
    @property
    def MaxRebuildSegments(self) -> int:
        """
        Getter for property: (int) MaxRebuildSegments
         Returns the max rebuild segments   
            
         
        """
        pass
    @MaxRebuildSegments.setter
    def MaxRebuildSegments(self, maxRebuildSegments: int):
        """
        Setter for property: (int) MaxRebuildSegments
         Returns the max rebuild segments   
            
         
        """
        pass
    @property
    def ModelDelayAndUpdateGranularityValue(self) -> ModelingPreferencesBuilder.ModelDelayAndUpdateGranularity:
        """
        Getter for property: ( ModelingPreferencesBuilder.ModelDelayAndUpdateGranularity NXOpen.P) ModelDelayAndUpdateGranularityValue
         Returns the model delay and update granularity value   
            
         
        """
        pass
    @ModelDelayAndUpdateGranularityValue.setter
    def ModelDelayAndUpdateGranularityValue(self, modelDelayAndUpdateGranularityValue: ModelingPreferencesBuilder.ModelDelayAndUpdateGranularity):
        """
        Setter for property: ( ModelingPreferencesBuilder.ModelDelayAndUpdateGranularity NXOpen.P) ModelDelayAndUpdateGranularityValue
         Returns the model delay and update granularity value   
            
         
        """
        pass
    @property
    def ModelingModeValue(self) -> ModelingPreferencesBuilder.ModelingMode:
        """
        Getter for property: ( ModelingPreferencesBuilder.ModelingMode NXOpen.P) ModelingModeValue
         Returns the modeling mode value   
            
         
        """
        pass
    @ModelingModeValue.setter
    def ModelingModeValue(self, modelingModeValue: ModelingPreferencesBuilder.ModelingMode):
        """
        Setter for property: ( ModelingPreferencesBuilder.ModelingMode NXOpen.P) ModelingModeValue
         Returns the modeling mode value   
            
         
        """
        pass
    @property
    def NewFacesValue(self) -> ModelingPreferencesBuilder.NewFaces:
        """
        Getter for property: ( ModelingPreferencesBuilder.NewFaces NXOpen.P) NewFacesValue
         Returns the new faces value   
            
         
        """
        pass
    @NewFacesValue.setter
    def NewFacesValue(self, newFacesValue: ModelingPreferencesBuilder.NewFaces):
        """
        Setter for property: ( ModelingPreferencesBuilder.NewFaces NXOpen.P) NewFacesValue
         Returns the new faces value   
            
         
        """
        pass
    @property
    def NotifyOnDelete(self) -> bool:
        """
        Getter for property: (bool) NotifyOnDelete
         Returns the notify on delete   
            
         
        """
        pass
    @NotifyOnDelete.setter
    def NotifyOnDelete(self, notifyOnDelete: bool):
        """
        Setter for property: (bool) NotifyOnDelete
         Returns the notify on delete   
            
         
        """
        pass
    @property
    def OptimizeCurve(self) -> bool:
        """
        Getter for property: (bool) OptimizeCurve
         Returns the optimize curve   
            
         
        """
        pass
    @OptimizeCurve.setter
    def OptimizeCurve(self, optimizeCurve: bool):
        """
        Setter for property: (bool) OptimizeCurve
         Returns the optimize curve   
            
         
        """
        pass
    @property
    def OptimizeCurveAngleTol(self) -> float:
        """
        Getter for property: (float) OptimizeCurveAngleTol
         Returns the optimize curve angle tol   
            
         
        """
        pass
    @OptimizeCurveAngleTol.setter
    def OptimizeCurveAngleTol(self, optimizeCurveAngleTol: float):
        """
        Setter for property: (float) OptimizeCurveAngleTol
         Returns the optimize curve angle tol   
            
         
        """
        pass
    @property
    def OptimizeCurveDitanceTol(self) -> float:
        """
        Getter for property: (float) OptimizeCurveDitanceTol
         Returns the optimize curve ditance tol   
            
         
        """
        pass
    @OptimizeCurveDitanceTol.setter
    def OptimizeCurveDitanceTol(self, optimizeCurveDitanceTol: float):
        """
        Setter for property: (float) OptimizeCurveDitanceTol
         Returns the optimize curve ditance tol   
            
         
        """
        pass
    @property
    def PlanarFaceTypeValue(self) -> ModelingPreferencesBuilder.PlanarFaceType:
        """
        Getter for property: ( ModelingPreferencesBuilder.PlanarFaceType NXOpen.P) PlanarFaceTypeValue
         Returns the planar face type value   
            
         
        """
        pass
    @PlanarFaceTypeValue.setter
    def PlanarFaceTypeValue(self, planarFaceTypeValue: ModelingPreferencesBuilder.PlanarFaceType):
        """
        Setter for property: ( ModelingPreferencesBuilder.PlanarFaceType NXOpen.P) PlanarFaceTypeValue
         Returns the planar face type value   
            
         
        """
        pass
    @property
    def PoleColorValue(self) -> ModelingPreferencesBuilder.PoleColor:
        """
        Getter for property: ( ModelingPreferencesBuilder.PoleColor NXOpen.P) PoleColorValue
         Returns the pole color value   
            
         
        """
        pass
    @PoleColorValue.setter
    def PoleColorValue(self, poleColorValue: ModelingPreferencesBuilder.PoleColor):
        """
        Setter for property: ( ModelingPreferencesBuilder.PoleColor NXOpen.P) PoleColorValue
         Returns the pole color value   
            
         
        """
        pass
    @property
    def PoleStyleValue(self) -> ModelingPreferencesBuilder.PoleStyle:
        """
        Getter for property: ( ModelingPreferencesBuilder.PoleStyle NXOpen.P) PoleStyleValue
         Returns the pole style value   
            
         
        """
        pass
    @PoleStyleValue.setter
    def PoleStyleValue(self, poleStyleValue: ModelingPreferencesBuilder.PoleStyle):
        """
        Setter for property: ( ModelingPreferencesBuilder.PoleStyle NXOpen.P) PoleStyleValue
         Returns the pole style value   
            
         
        """
        pass
    @property
    def PolylineColorValue(self) -> ModelingPreferencesBuilder.PolylineColor:
        """
        Getter for property: ( ModelingPreferencesBuilder.PolylineColor NXOpen.P) PolylineColorValue
         Returns the polyline color value   
            
         
        """
        pass
    @PolylineColorValue.setter
    def PolylineColorValue(self, polylineColorValue: ModelingPreferencesBuilder.PolylineColor):
        """
        Setter for property: ( ModelingPreferencesBuilder.PolylineColor NXOpen.P) PolylineColorValue
         Returns the polyline color value   
            
         
        """
        pass
    @property
    def PolylineStyleValue(self) -> NXOpen.LineFontBuilder:
        """
        Getter for property: ( NXOpen.LineFontBuilder) PolylineStyleValue
         Returns the polyline style value   
            
         
        """
        pass
    @property
    def PreviewResolutionValue(self) -> ModelingPreferencesBuilder.PreviewResolution:
        """
        Getter for property: ( ModelingPreferencesBuilder.PreviewResolution NXOpen.P) PreviewResolutionValue
         Returns the preview resolution value   
            
         
        """
        pass
    @PreviewResolutionValue.setter
    def PreviewResolutionValue(self, previewResolutionValue: ModelingPreferencesBuilder.PreviewResolution):
        """
        Setter for property: ( ModelingPreferencesBuilder.PreviewResolution NXOpen.P) PreviewResolutionValue
         Returns the preview resolution value   
            
         
        """
        pass
    @property
    def ReportWarningAfterUpdate(self) -> bool:
        """
        Getter for property: (bool) ReportWarningAfterUpdate
         Returns the report warning after update   
            
         
        """
        pass
    @ReportWarningAfterUpdate.setter
    def ReportWarningAfterUpdate(self, reportWarningAfterUpdate: bool):
        """
        Setter for property: (bool) ReportWarningAfterUpdate
         Returns the report warning after update   
            
         
        """
        pass
    @property
    def ShowParentSketchDim(self) -> bool:
        """
        Getter for property: (bool) ShowParentSketchDim
         Returns the show parent sketch dim   
            
         
        """
        pass
    @ShowParentSketchDim.setter
    def ShowParentSketchDim(self, showParentSketchDim: bool):
        """
        Setter for property: (bool) ShowParentSketchDim
         Returns the show parent sketch dim   
            
         
        """
        pass
    @property
    def ShowSimulation(self) -> bool:
        """
        Getter for property: (bool) ShowSimulation
         Returns the show simulation   
            
         
        """
        pass
    @ShowSimulation.setter
    def ShowSimulation(self, showSimulation: bool):
        """
        Setter for property: (bool) ShowSimulation
         Returns the show simulation   
            
         
        """
        pass
    @property
    def ShowSymbolicThreadDecalSticker(self) -> bool:
        """
        Getter for property: (bool) ShowSymbolicThreadDecalSticker
         Returns the symbolic thread decal sticker   
            
         
        """
        pass
    @ShowSymbolicThreadDecalSticker.setter
    def ShowSymbolicThreadDecalSticker(self, showSymbolicThreadDecalSticker: bool):
        """
        Setter for property: (bool) ShowSymbolicThreadDecalSticker
         Returns the symbolic thread decal sticker   
            
         
        """
        pass
    @property
    def SketchDoubleClickActionValue(self) -> ModelingPreferencesBuilder.SketchDoubleClickAction:
        """
        Getter for property: ( ModelingPreferencesBuilder.SketchDoubleClickAction NXOpen.P) SketchDoubleClickActionValue
         Returns the sketch double click action value   
            
         
        """
        pass
    @SketchDoubleClickActionValue.setter
    def SketchDoubleClickActionValue(self, sketchDoubleClickActionValue: ModelingPreferencesBuilder.SketchDoubleClickAction):
        """
        Setter for property: ( ModelingPreferencesBuilder.SketchDoubleClickAction NXOpen.P) SketchDoubleClickActionValue
         Returns the sketch double click action value   
            
         
        """
        pass
    @property
    def SpecificC0KnotLineColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) SpecificC0KnotLineColor
         Returns the specific c0 knot line color   
            
         
        """
        pass
    @SpecificC0KnotLineColor.setter
    def SpecificC0KnotLineColor(self, specificC0KnotLineColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) SpecificC0KnotLineColor
         Returns the specific c0 knot line color   
            
         
        """
        pass
    @property
    def SpecificC1KnotLineColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) SpecificC1KnotLineColor
         Returns the specific c1 knot line color   
            
         
        """
        pass
    @SpecificC1KnotLineColor.setter
    def SpecificC1KnotLineColor(self, specificC1KnotLineColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) SpecificC1KnotLineColor
         Returns the specific c1 knot line color   
            
         
        """
        pass
    @property
    def SpecificC2KnotLineColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) SpecificC2KnotLineColor
         Returns the specific c2 knot line color   
            
         
        """
        pass
    @SpecificC2KnotLineColor.setter
    def SpecificC2KnotLineColor(self, specificC2KnotLineColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) SpecificC2KnotLineColor
         Returns the specific c2 knot line color   
            
         
        """
        pass
    @property
    def SpecificEndPointColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) SpecificEndPointColor
         Returns the specific end point color   
            
         
        """
        pass
    @SpecificEndPointColor.setter
    def SpecificEndPointColor(self, specificEndPointColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) SpecificEndPointColor
         Returns the specific end point color   
            
         
        """
        pass
    @property
    def SpecificGridLineColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) SpecificGridLineColor
         Returns the specific grid line color   
            
         
        """
        pass
    @SpecificGridLineColor.setter
    def SpecificGridLineColor(self, specificGridLineColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) SpecificGridLineColor
         Returns the specific grid line color   
            
         
        """
        pass
    @property
    def SpecificPoleColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) SpecificPoleColor
         Returns the specific pole color   
            
         
        """
        pass
    @SpecificPoleColor.setter
    def SpecificPoleColor(self, specificPoleColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) SpecificPoleColor
         Returns the specific pole color   
            
         
        """
        pass
    @property
    def SpecificPolylineColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) SpecificPolylineColor
         Returns the specific polyline color   
            
         
        """
        pass
    @SpecificPolylineColor.setter
    def SpecificPolylineColor(self, specificPolylineColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) SpecificPolylineColor
         Returns the specific polyline color   
            
         
        """
        pass
    @property
    def SplineDoubleClickActionValue(self) -> ModelingPreferencesBuilder.SplineDefaultClickAction:
        """
        Getter for property: ( ModelingPreferencesBuilder.SplineDefaultClickAction NXOpen.P) SplineDoubleClickActionValue
         Returns the spline double click action value   
            
         
        """
        pass
    @SplineDoubleClickActionValue.setter
    def SplineDoubleClickActionValue(self, splineDoubleClickActionValue: ModelingPreferencesBuilder.SplineDefaultClickAction):
        """
        Setter for property: ( ModelingPreferencesBuilder.SplineDefaultClickAction NXOpen.P) SplineDoubleClickActionValue
         Returns the spline double click action value   
            
         
        """
        pass
    @property
    def SurfaceExtensionValue(self) -> ModelingPreferencesBuilder.SurfaceExtension:
        """
        Getter for property: ( ModelingPreferencesBuilder.SurfaceExtension NXOpen.P) SurfaceExtensionValue
         Returns the surface extension value   
            
         
        """
        pass
    @SurfaceExtensionValue.setter
    def SurfaceExtensionValue(self, surfaceExtensionValue: ModelingPreferencesBuilder.SurfaceExtension):
        """
        Setter for property: ( ModelingPreferencesBuilder.SurfaceExtension NXOpen.P) SurfaceExtensionValue
         Returns the surface extension value   
            
         
        """
        pass
    @property
    def TreatDegrre1SplineAsPolyline(self) -> bool:
        """
        Getter for property: (bool) TreatDegrre1SplineAsPolyline
         Returns the treat degrre1 spline as polyline   
            
         
        """
        pass
    @TreatDegrre1SplineAsPolyline.setter
    def TreatDegrre1SplineAsPolyline(self, treatDegrre1SplineAsPolyline: bool):
        """
        Setter for property: (bool) TreatDegrre1SplineAsPolyline
         Returns the treat degrre1 spline as polyline   
            
         
        """
        pass
    @property
    def UGridLines(self) -> int:
        """
        Getter for property: (int) UGridLines
         Returns the u grid lines   
            
         
        """
        pass
    @UGridLines.setter
    def UGridLines(self, uGridLines: int):
        """
        Setter for property: (int) UGridLines
         Returns the u grid lines   
            
         
        """
        pass
    @property
    def UseTriangularMesh(self) -> bool:
        """
        Getter for property: (bool) UseTriangularMesh
         Returns the use triangular mesh   
            
         
        """
        pass
    @UseTriangularMesh.setter
    def UseTriangularMesh(self, useTriangularMesh: bool):
        """
        Setter for property: (bool) UseTriangularMesh
         Returns the use triangular mesh   
            
         
        """
        pass
    @property
    def VGridLines(self) -> int:
        """
        Getter for property: (int) VGridLines
         Returns the v grid lines   
            
         
        """
        pass
    @VGridLines.setter
    def VGridLines(self, vGridLines: int):
        """
        Setter for property: (int) VGridLines
         Returns the v grid lines   
            
         
        """
        pass
    @property
    def WarnOnMissingReference(self) -> bool:
        """
        Getter for property: (bool) WarnOnMissingReference
         Returns the warn on missing reference   
            
         
        """
        pass
    @WarnOnMissingReference.setter
    def WarnOnMissingReference(self, warnOnMissingReference: bool):
        """
        Setter for property: (bool) WarnOnMissingReference
         Returns the warn on missing reference   
            
         
        """
        pass
import NXOpen
class MorphMeshPreferences(NXOpen.Object): 
    """ Represents the set of Morph Mesh preferences applicable to entire session"""
    class CagePolylineVertexSizes(Enum):
        """
        Members Include: 
         |Small| 
         |Medium| 
         |Large| 

        """
        Small: int
        Medium: int
        Large: int
        @staticmethod
        def ValueOf(value: int) -> MorphMeshPreferences.CagePolylineVertexSizes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CagePolylineVertexStyles(Enum):
        """
        Members Include: 
         |NotSet| 
         |Square| 
         |Triangle| 
         |Circle| 
         |Plus| 
         |Cross| 

        """
        NotSet: int
        Square: int
        Triangle: int
        Circle: int
        Plus: int
        Cross: int
        @staticmethod
        def ValueOf(value: int) -> MorphMeshPreferences.CagePolylineVertexStyles:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class VertexSizeTypes(Enum):
        """
        Members Include: 
         |Small| 
         |Medium| 
         |Large| 

        """
        Small: int
        Medium: int
        Large: int
        @staticmethod
        def ValueOf(value: int) -> MorphMeshPreferences.VertexSizeTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class VertexStyleTypes(Enum):
        """
        Members Include: 
         |Square| 
         |Triangle| 
         |Circle| 
         |Plus| 
         |Cross| 

        """
        Square: int
        Triangle: int
        Circle: int
        Plus: int
        Cross: int
        @staticmethod
        def ValueOf(value: int) -> MorphMeshPreferences.VertexStyleTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CagePolylineColor(self) -> int:
        """
        Getter for property: (int) CagePolylineColor
         Returns the cage polyline color.  
             
         
        """
        pass
    @CagePolylineColor.setter
    def CagePolylineColor(self, lineColor: int):
        """
        Setter for property: (int) CagePolylineColor
         Returns the cage polyline color.  
             
         
        """
        pass
    @property
    def CagePolylineStyle(self) -> int:
        """
        Getter for property: (int) CagePolylineStyle
         Returns the cage polyline style.  
             
         
        """
        pass
    @CagePolylineStyle.setter
    def CagePolylineStyle(self, lineStyle: int):
        """
        Setter for property: (int) CagePolylineStyle
         Returns the cage polyline style.  
             
         
        """
        pass
    @property
    def CagePolylineVertexColor(self) -> int:
        """
        Getter for property: (int) CagePolylineVertexColor
         Returns the cage polyline vertex color.  
             
         
        """
        pass
    @CagePolylineVertexColor.setter
    def CagePolylineVertexColor(self, vertexColor: int):
        """
        Setter for property: (int) CagePolylineVertexColor
         Returns the cage polyline vertex color.  
             
         
        """
        pass
    @property
    def CagePolylineVertexSize(self) -> MorphMeshPreferences.CagePolylineVertexSizes:
        """
        Getter for property: ( MorphMeshPreferences.CagePolylineVertexSizes NXOpen.P) CagePolylineVertexSize
         Returns the cage polyline vertex size.  
             
         
        """
        pass
    @CagePolylineVertexSize.setter
    def CagePolylineVertexSize(self, vertexSize: MorphMeshPreferences.CagePolylineVertexSizes):
        """
        Setter for property: ( MorphMeshPreferences.CagePolylineVertexSizes NXOpen.P) CagePolylineVertexSize
         Returns the cage polyline vertex size.  
             
         
        """
        pass
    @property
    def CagePolylineVertexStyle(self) -> MorphMeshPreferences.CagePolylineVertexStyles:
        """
        Getter for property: ( MorphMeshPreferences.CagePolylineVertexStyles NXOpen.P) CagePolylineVertexStyle
         Returns the cage polyline vertex style.  
             
         
        """
        pass
    @CagePolylineVertexStyle.setter
    def CagePolylineVertexStyle(self, vertexStyle: MorphMeshPreferences.CagePolylineVertexStyles):
        """
        Setter for property: ( MorphMeshPreferences.CagePolylineVertexStyles NXOpen.P) CagePolylineVertexStyle
         Returns the cage polyline vertex style.  
             
         
        """
        pass
    @property
    def CagePolylineWidth(self) -> int:
        """
        Getter for property: (int) CagePolylineWidth
         Returns the cage polyline width.  
             
         
        """
        pass
    @CagePolylineWidth.setter
    def CagePolylineWidth(self, lineWidth: int):
        """
        Setter for property: (int) CagePolylineWidth
         Returns the cage polyline width.  
             
         
        """
        pass
    @property
    def CanAllowBackSideSelection(self) -> bool:
        """
        Getter for property: (bool) CanAllowBackSideSelection
         Returns the flag indicating if the hidden topology selection is allowed or not.  
             
         
        """
        pass
    @CanAllowBackSideSelection.setter
    def CanAllowBackSideSelection(self, allow: bool):
        """
        Setter for property: (bool) CanAllowBackSideSelection
         Returns the flag indicating if the hidden topology selection is allowed or not.  
             
         
        """
        pass
    @property
    def CanRefineMesh(self) -> bool:
        """
        Getter for property: (bool) CanRefineMesh
         Returns the flag indicating if mesh refinement should be done before morphing   
            
         
        """
        pass
    @CanRefineMesh.setter
    def CanRefineMesh(self, canRefineMesh: bool):
        """
        Setter for property: (bool) CanRefineMesh
         Returns the flag indicating if mesh refinement should be done before morphing   
            
         
        """
        pass
    @property
    def ConstraintColor(self) -> int:
        """
        Getter for property: (int) ConstraintColor
         Returns the constrained entity color.  
             
         
        """
        pass
    @ConstraintColor.setter
    def ConstraintColor(self, color: int):
        """
        Setter for property: (int) ConstraintColor
         Returns the constrained entity color.  
             
         
        """
        pass
    @property
    def HighlightFaceTranslucency(self) -> int:
        """
        Getter for property: (int) HighlightFaceTranslucency
         Returns the percentage translucency of the highlighted face.  
             
         
        """
        pass
    @HighlightFaceTranslucency.setter
    def HighlightFaceTranslucency(self, highlightLineTranslucency: int):
        """
        Setter for property: (int) HighlightFaceTranslucency
         Returns the percentage translucency of the highlighted face.  
             
         
        """
        pass
    @property
    def IsXRayCage(self) -> bool:
        """
        Getter for property: (bool) IsXRayCage
         Returns the flag indicating if the hidden edge of the cage are visible or not.  
             
         
        """
        pass
    @IsXRayCage.setter
    def IsXRayCage(self, isXRayCage: bool):
        """
        Setter for property: (bool) IsXRayCage
         Returns the flag indicating if the hidden edge of the cage are visible or not.  
             
         
        """
        pass
    @property
    def LineColor(self) -> int:
        """
        Getter for property: (int) LineColor
         Returns the line color.  
             
         
        """
        pass
    @LineColor.setter
    def LineColor(self, lineColor: int):
        """
        Setter for property: (int) LineColor
         Returns the line color.  
             
         
        """
        pass
    @property
    def LineStyle(self) -> int:
        """
        Getter for property: (int) LineStyle
         Returns the line style.  
             
         
        """
        pass
    @LineStyle.setter
    def LineStyle(self, lineStyle: int):
        """
        Setter for property: (int) LineStyle
         Returns the line style.  
             
         
        """
        pass
    @property
    def LineWidth(self) -> int:
        """
        Getter for property: (int) LineWidth
         Returns the line width.  
             
         
        """
        pass
    @LineWidth.setter
    def LineWidth(self, lineWidth: int):
        """
        Setter for property: (int) LineWidth
         Returns the line width.  
             
         
        """
        pass
    @property
    def RefinementRatio(self) -> float:
        """
        Getter for property: (float) RefinementRatio
         Returns the refinement percentage   
            
         
        """
        pass
    @RefinementRatio.setter
    def RefinementRatio(self, refinementRatio: float):
        """
        Setter for property: (float) RefinementRatio
         Returns the refinement percentage   
            
         
        """
        pass
    @property
    def VertexColor(self) -> int:
        """
        Getter for property: (int) VertexColor
         Returns the vertex color.  
             
         
        """
        pass
    @VertexColor.setter
    def VertexColor(self, vertexColor: int):
        """
        Setter for property: (int) VertexColor
         Returns the vertex color.  
             
         
        """
        pass
    @property
    def VertexSize(self) -> MorphMeshPreferences.VertexSizeTypes:
        """
        Getter for property: ( MorphMeshPreferences.VertexSizeTypes NXOpen.P) VertexSize
         Returns the vertex size.  
             
         
        """
        pass
    @VertexSize.setter
    def VertexSize(self, vertexSize: MorphMeshPreferences.VertexSizeTypes):
        """
        Setter for property: ( MorphMeshPreferences.VertexSizeTypes NXOpen.P) VertexSize
         Returns the vertex size.  
             
         
        """
        pass
    @property
    def VertexStyle(self) -> MorphMeshPreferences.VertexStyleTypes:
        """
        Getter for property: ( MorphMeshPreferences.VertexStyleTypes NXOpen.P) VertexStyle
         Returns the vertex style.  
             
         
        """
        pass
    @VertexStyle.setter
    def VertexStyle(self, vertexStyle: MorphMeshPreferences.VertexStyleTypes):
        """
        Setter for property: ( MorphMeshPreferences.VertexStyleTypes NXOpen.P) VertexStyle
         Returns the vertex style.  
             
         
        """
        pass
import NXOpen
class ObjectPreferences(NXOpen.Object): 
    """ Captures the UI based calls required for Object Preferences """
    class Translucency(Enum):
        """
        Members Include: 
         |Disabled|   
         |Enabled|   
         |TemporarilyEnabled|   

        """
        Disabled: int
        Enabled: int
        TemporarilyEnabled: int
        @staticmethod
        def ValueOf(value: int) -> ObjectPreferences.Translucency:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def ResetSessionTranslucency(option: bool) -> ObjectPreferences.Translucency:
        """
         Resets the session translucency 
         Returns session_translucency ( ObjectPreferences.Translucency NXOpen.P):  Return Value .
        """
        pass
    def SetSessionTranslucency(option: ObjectPreferences.Translucency) -> ObjectPreferences.Translucency:
        """
         Sets the session translucency 
         Returns session_translucency ( ObjectPreferences.Translucency NXOpen.P):  Return Value .
        """
        pass
import NXOpen
class PartAeroSheetmetal(NXOpen.Object): 
    """ Represents the NX Sheetmetal preferences applicable to part """
    def GetJoggleDepthThreshold(self) -> NXOpen.Expression:
        """
         RETURNS the joggle depth threshold expression 
         Returns depth_threshold ( NXOpen.Expression):  expression object for joggle depth threshold .
        """
        pass
    def GetJoggleDistanceThreshold(self) -> NXOpen.Expression:
        """
         RETURNS the joggle distance threshold expression 
         Returns distance_threshold ( NXOpen.Expression):  expression object for joggle distance threshold .
        """
        pass
    def GetJoggleOffsetRadius(self) -> NXOpen.Expression:
        """
         RETURNS the joggle offset radius expression 
         Returns offset_radius ( NXOpen.Expression):  expression object for joggle offset radius .
        """
        pass
    def GetJoggleStationaryRadius(self) -> NXOpen.Expression:
        """
         RETURNS the joggle stationary radius expression 
         Returns stationary_radius ( NXOpen.Expression):  expression object for joggle stationary radius .
        """
        pass
    def SetJoggleDepthThreshold(self, update_model: bool, depth_threshold: str) -> None:
        """
         THE joggle depth threshold value 
        """
        pass
    def SetJoggleDistanceThreshold(self, update_model: bool, distance_threshold: str) -> None:
        """
         THE joggle distance threshold value 
        """
        pass
    def SetJoggleOffsetRadius(self, update_model: bool, offset_radius: str) -> None:
        """
         The joggle offset radius value 
        """
        pass
    def SetJoggleStationaryRadius(self, update_model: bool, stationary_radius: str) -> None:
        """
         THE joggle stationary radius value string 
        """
        pass
import NXOpen
class PartAppearanceMgrPreference(NXOpen.Object): 
    """
    Represents preferences for AppearanceManagement that are applicable
        to the entire part. """
    class DesignatorSourceType(Enum):
        """
        Members Include: 
         |ProductStructure|  from part file related .dlf 
         |File|  from an seperate .dlf file specified by user 

        """
        ProductStructure: int
        File: int
        @staticmethod
        def ValueOf(value: int) -> PartAppearanceMgrPreference.DesignatorSourceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DesignatorLibSource(self) -> PartAppearanceMgrPreference.DesignatorSourceType:
        """
        Getter for property: ( PartAppearanceMgrPreference.DesignatorSourceType NXOpen.P) DesignatorLibSource
         Returns the source of designator library   
            
         
        """
        pass
    @DesignatorLibSource.setter
    def DesignatorLibSource(self, designator_source_type: PartAppearanceMgrPreference.DesignatorSourceType):
        """
        Setter for property: ( PartAppearanceMgrPreference.DesignatorSourceType NXOpen.P) DesignatorLibSource
         Returns the source of designator library   
            
         
        """
        pass
    @property
    def PrefixAppearanceAreas(self) -> str:
        """
        Getter for property: (str) PrefixAppearanceAreas
         Returns the appearance areas name automatic generating  
            
         
        """
        pass
    @PrefixAppearanceAreas.setter
    def PrefixAppearanceAreas(self, designator_prefix: str):
        """
        Setter for property: (str) PrefixAppearanceAreas
         Returns the appearance areas name automatic generating  
            
         
        """
        pass
    @property
    def PrefixAppearanceDesignators(self) -> str:
        """
        Getter for property: (str) PrefixAppearanceDesignators
         Returns the appearance designators name automatic generating  
            
         
        """
        pass
    @PrefixAppearanceDesignators.setter
    def PrefixAppearanceDesignators(self, designator_prefix: str):
        """
        Setter for property: (str) PrefixAppearanceDesignators
         Returns the appearance designators name automatic generating  
            
         
        """
        pass
    @property
    def PrefixAppearanceSchemes(self) -> str:
        """
        Getter for property: (str) PrefixAppearanceSchemes
         Returns the appearance schemes automatic generating  
            
         
        """
        pass
    @PrefixAppearanceSchemes.setter
    def PrefixAppearanceSchemes(self, designator_prefix: str):
        """
        Setter for property: (str) PrefixAppearanceSchemes
         Returns the appearance schemes automatic generating  
            
         
        """
        pass
    def GetDesignatorLibraryFile(self) -> str:
        """
         Get the seperate .dlf file of designator library 
         Returns designator_file (str): .
        """
        pass
    def SetDesignatorLibraryFile(self, designator_file: str) -> None:
        """
         Set the seperate .dlf file of designator library 
        """
        pass
import NXOpen
class PartDrafting(NXOpen.Object): 
    """ Represents the set of drafting preferences applicable to part """
    class BreakLineStyle(Enum):
        """
        Members Include: 
         |Existing|  Existing Curve 
         |Simple|  Simple 
         |Straight|  Straight 
         |Sawtooth|  Sawtooth 
         |LongBreak|  LongBreak 
         |Tubular|  Tubular 
         |SolidTubular|  Solid Tubular 
         |SolidRod|  Solid Rod 
         |Jigsaw|  Jigsaw 
         |Wood|  Wood 

        """
        Existing: int
        Simple: int
        Straight: int
        Sawtooth: int
        LongBreak: int
        Tubular: int
        SolidTubular: int
        SolidRod: int
        Jigsaw: int
        Wood: int
        @staticmethod
        def ValueOf(value: int) -> PartDrafting.BreakLineStyle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FontType(Enum):
        """
        Members Include: 
         |Original|  Original  
         |Invisible|  Invisible 
         |Solid|  Solid 
         |Dashed|  Dashed 
         |Phantom|  Phantom 
         |Centerline|  CenterLine  
         |Dotted|  Dotted 
         |LongDashed|  Long Dashed 
         |DottedDashed|  Dotted Dashed 
         |Eight|  Long Dashed Double Dotted 
         |Nine|  Long Dashed Dotted for OOTB fonts and Undulating for shipbuilding fonts 
         |Ten|  Long Dashed Triplicate Dotted for OOTB fonts and Zigzag for shipbuilding fonts 
         |Eleven|  Long Dashed Double Short Dashed for OOTB fonts and Railway for shipbuilding fonts 

        """
        Original: int
        Invisible: int
        Solid: int
        Dashed: int
        Phantom: int
        Centerline: int
        Dotted: int
        LongDashed: int
        DottedDashed: int
        Eight: int
        Nine: int
        Ten: int
        Eleven: int
        @staticmethod
        def ValueOf(value: int) -> PartDrafting.FontType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class UpdateViewWithoutLwDataOption(Enum):
        """
        Members Include: 
         |Ignore|  Ignore 
         |Notify|  Notify 
         |DoNotNotify|  Do Not Notify 
         |Generate|  Generate 

        """
        Ignore: int
        Notify: int
        DoNotNotify: int
        Generate: int
        @staticmethod
        def ValueOf(value: int) -> PartDrafting.UpdateViewWithoutLwDataOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ViewStyleType(Enum):
        """
        Members Include: 
         |Border|  Border  
         |Wireframe|  Wireframe 
         |HiddenWireframe|  Hidden Wireframe 
         |Shaded|  Shaded  

        """
        Border: int
        Wireframe: int
        HiddenWireframe: int
        Shaded: int
        @staticmethod
        def ValueOf(value: int) -> PartDrafting.ViewStyleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class WidthType(Enum):
        """
        Members Include: 
         |Original|  Original  
         |Thin|  Thin 
         |Normal|  Normal 
         |Thick|  Thick 
         |ThicknessOne|  Width One 
         |ThicknessTwo|  Width Two 
         |ThicknessThree|  Width Three 
         |ThicknessFour|  Width Four 
         |ThicknessFive|  Width Five 
         |ThicknessSix|  Width Six 
         |ThicknessSeven|  Width Seven 
         |ThicknessEight|  Width Eight 
         |ThicknessNine|  Width Nine 

        """
        Original: int
        Thin: int
        Normal: int
        Thick: int
        ThicknessOne: int
        ThicknessTwo: int
        ThicknessThree: int
        ThicknessFour: int
        ThicknessFive: int
        ThicknessSix: int
        ThicknessSeven: int
        ThicknessEight: int
        ThicknessNine: int
        @staticmethod
        def ValueOf(value: int) -> PartDrafting.WidthType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ActiveViewColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) ActiveViewColor
         Returns the drafting active view color.  
             
         
        """
        pass
    @ActiveViewColor.setter
    def ActiveViewColor(self, border_color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) ActiveViewColor
         Returns the drafting active view color.  
             
         
        """
        pass
    @property
    def AssociativeAlignment(self) -> bool:
        """
        Getter for property: (bool) AssociativeAlignment
         Returns the flag indicating whether to associatively align the view when placing it   
            
         
        """
        pass
    @AssociativeAlignment.setter
    def AssociativeAlignment(self, associativeAlignment: bool):
        """
        Setter for property: (bool) AssociativeAlignment
         Returns the flag indicating whether to associatively align the view when placing it   
            
         
        """
        pass
    @property
    def BorderColor(self) -> int:
        """
        Getter for property: (int) BorderColor
         Returns the drafting view border color.  
           The value should be between 1 and 216.  
         
        """
        pass
    @BorderColor.setter
    def BorderColor(self, border_color: int):
        """
        Setter for property: (int) BorderColor
         Returns the drafting view border color.  
           The value should be between 1 and 216.  
         
        """
        pass
    @property
    def BreakLineAmplitude(self) -> float:
        """
        Getter for property: (float) BreakLineAmplitude
         Returns the break line amplitude.  
             
         
        """
        pass
    @BreakLineAmplitude.setter
    def BreakLineAmplitude(self, amplitude: float):
        """
        Setter for property: (float) BreakLineAmplitude
         Returns the break line amplitude.  
             
         
        """
        pass
    @property
    def BreakLineColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) BreakLineColor
         Returns the break line color.  
             
         
        """
        pass
    @BreakLineColor.setter
    def BreakLineColor(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) BreakLineColor
         Returns the break line color.  
             
         
        """
        pass
    @property
    def BreakLineExtension(self) -> float:
        """
        Getter for property: (float) BreakLineExtension
         Returns    
            
         
        """
        pass
    @BreakLineExtension.setter
    def BreakLineExtension(self, extension: float):
        """
        Setter for property: (float) BreakLineExtension
         Returns    
            
         
        """
        pass
    @property
    def BreakLineGap(self) -> float:
        """
        Getter for property: (float) BreakLineGap
         Returns the break line gap.  
             
         
        """
        pass
    @BreakLineGap.setter
    def BreakLineGap(self, gap: float):
        """
        Setter for property: (float) BreakLineGap
         Returns the break line gap.  
             
         
        """
        pass
    @property
    def BreakLineType(self) -> PartDrafting.BreakLineStyle:
        """
        Getter for property: ( PartDrafting.BreakLineStyle NXOpen.P) BreakLineType
         Returns the break line type.  
             
         
        """
        pass
    @BreakLineType.setter
    def BreakLineType(self, line_type: PartDrafting.BreakLineStyle):
        """
        Setter for property: ( PartDrafting.BreakLineStyle NXOpen.P) BreakLineType
         Returns the break line type.  
             
         
        """
        pass
    @property
    def BreakLineWidth(self) -> int:
        """
        Getter for property: (int) BreakLineWidth
         Returns the break line width.  
             
         
        """
        pass
    @BreakLineWidth.setter
    def BreakLineWidth(self, width: int):
        """
        Setter for property: (int) BreakLineWidth
         Returns the break line width.  
             
         
        """
        pass
    @property
    def BreakLinesVisibility(self) -> bool:
        """
        Getter for property: (bool) BreakLinesVisibility
         Returns the break lines visibility.  
             
         
        """
        pass
    @BreakLinesVisibility.setter
    def BreakLinesVisibility(self, isVisible: bool):
        """
        Setter for property: (bool) BreakLinesVisibility
         Returns the break lines visibility.  
             
         
        """
        pass
    @property
    def Color(self) -> int:
        """
        Getter for property: (int) Color
         Returns the color of the retained  NXOpen::Annotations::Annotation  objects.  
           
                The value should be between 1 and 216.   
         
        """
        pass
    @Color.setter
    def Color(self, color: int):
        """
        Setter for property: (int) Color
         Returns the color of the retained  NXOpen::Annotations::Annotation  objects.  
           
                The value should be between 1 and 216.   
         
        """
        pass
    @property
    def CustomSymbolSmashToSketch(self) -> bool:
        """
        Getter for property: (bool) CustomSymbolSmashToSketch
         Returns the custom symbol smash behavior.  
             
         
        """
        pass
    @CustomSymbolSmashToSketch.setter
    def CustomSymbolSmashToSketch(self, isSmashToSketch: bool):
        """
        Setter for property: (bool) CustomSymbolSmashToSketch
         Returns the custom symbol smash behavior.  
             
         
        """
        pass
    @property
    def DelayUpdateOnCreation(self) -> bool:
        """
        Getter for property: (bool) DelayUpdateOnCreation
         Returns the flag indicating whether the newly created views should update immediately even
                when the view update is delayed.  
             
         
        """
        pass
    @DelayUpdateOnCreation.setter
    def DelayUpdateOnCreation(self, isDelayUpdateOnCreationOn: bool):
        """
        Setter for property: (bool) DelayUpdateOnCreation
         Returns the flag indicating whether the newly created views should update immediately even
                when the view update is delayed.  
             
         
        """
        pass
    @property
    def DelayViewUpdate(self) -> bool:
        """
        Getter for property: (bool) DelayViewUpdate
         Returns the flag indicating whether to delay update of the drafting views during system 
                initiated drawing updates    
            
         
        """
        pass
    @DelayViewUpdate.setter
    def DelayViewUpdate(self, isDelayViewUpdateOn: bool):
        """
        Setter for property: (bool) DelayViewUpdate
         Returns the flag indicating whether to delay update of the drafting views during system 
                initiated drawing updates    
            
         
        """
        pass
    @property
    def Delimiter(self) -> str:
        """
        Getter for property: (str) Delimiter
         Returns the delimiter    
            
         
        """
        pass
    @Delimiter.setter
    def Delimiter(self, delimiter: str):
        """
        Setter for property: (str) Delimiter
         Returns the delimiter    
            
         
        """
        pass
    @property
    def DisplayBorders(self) -> bool:
        """
        Getter for property: (bool) DisplayBorders
         Returns the flag indicating whether to display borders around drafting views, when selected   
            
         
        """
        pass
    @DisplayBorders.setter
    def DisplayBorders(self, display_borders: bool):
        """
        Setter for property: (bool) DisplayBorders
         Returns the flag indicating whether to display borders around drafting views, when selected   
            
         
        """
        pass
    @property
    def EnableSmoothEdgesForLWView(self) -> bool:
        """
        Getter for property: (bool) EnableSmoothEdgesForLWView
         Returns the flat indicating whether the smart lightweight views should show the smooth edges 
                or render them as normal curves   
            
         
        """
        pass
    @EnableSmoothEdgesForLWView.setter
    def EnableSmoothEdgesForLWView(self, enableSmoothEdges: bool):
        """
        Setter for property: (bool) EnableSmoothEdgesForLWView
         Returns the flat indicating whether the smart lightweight views should show the smooth edges 
                or render them as normal curves   
            
         
        """
        pass
    @property
    def Font(self) -> PartDrafting.FontType:
        """
        Getter for property: ( PartDrafting.FontType NXOpen.P) Font
         Returns the line font of the retained  NXOpen::Annotations::Annotation  objects   
            
         
        """
        pass
    @Font.setter
    def Font(self, font: PartDrafting.FontType):
        """
        Setter for property: ( PartDrafting.FontType NXOpen.P) Font
         Returns the line font of the retained  NXOpen::Annotations::Annotation  objects   
            
         
        """
        pass
    @property
    def FrameBarPrecision(self) -> int:
        """
        Getter for property: (int) FrameBarPrecision
         Returns the frame bar precision.  
             
         
        """
        pass
    @FrameBarPrecision.setter
    def FrameBarPrecision(self, precision: int):
        """
        Setter for property: (int) FrameBarPrecision
         Returns the frame bar precision.  
             
         
        """
        pass
    @property
    def FrameBarTicDirection(self) -> int:
        """
        Getter for property: (int) FrameBarTicDirection
         Returns the frame bar tic direction.  
             
         
        """
        pass
    @FrameBarTicDirection.setter
    def FrameBarTicDirection(self, ticDirection: int):
        """
        Setter for property: (int) FrameBarTicDirection
         Returns the frame bar tic direction.  
             
         
        """
        pass
    @property
    def InitialSecondaryNumber(self) -> str:
        """
        Getter for property: (str) InitialSecondaryNumber
         Returns the initial secondary number   
            
         
        """
        pass
    @InitialSecondaryNumber.setter
    def InitialSecondaryNumber(self, initialSecondaryNumber: str):
        """
        Setter for property: (str) InitialSecondaryNumber
         Returns the initial secondary number   
            
         
        """
        pass
    @property
    def InitialSheetNumber(self) -> str:
        """
        Getter for property: (str) InitialSheetNumber
         Returns the initial sheet number   
            
         
        """
        pass
    @InitialSheetNumber.setter
    def InitialSheetNumber(self, initialSheetNumber: str):
        """
        Setter for property: (str) InitialSheetNumber
         Returns the initial sheet number   
            
         
        """
        pass
    @property
    def LineAntialiasing(self) -> bool:
        """
        Getter for property: (bool) LineAntialiasing
         Returns the flag indicating whether to display drawing using line antialiasing.  
              
         
        """
        pass
    @LineAntialiasing.setter
    def LineAntialiasing(self, line_antialiasing: bool):
        """
        Setter for property: (bool) LineAntialiasing
         Returns the flag indicating whether to display drawing using line antialiasing.  
              
         
        """
        pass
    @property
    def MinimumComponentsForLargeAssemblyOption(self) -> int:
        """
        Getter for property: (int) MinimumComponentsForLargeAssemblyOption
         Returns the minimum number of components for large assembly option to get enabled   
            
         
        """
        pass
    @MinimumComponentsForLargeAssemblyOption.setter
    def MinimumComponentsForLargeAssemblyOption(self, minComponents: int):
        """
        Setter for property: (int) MinimumComponentsForLargeAssemblyOption
         Returns the minimum number of components for large assembly option to get enabled   
            
         
        """
        pass
    @property
    def PropagateBreakLines(self) -> bool:
        """
        Getter for property: (bool) PropagateBreakLines
         Returns the propagation of view break.  
             
         
        """
        pass
    @PropagateBreakLines.setter
    def PropagateBreakLines(self, doesPropagate: bool):
        """
        Setter for property: (bool) PropagateBreakLines
         Returns the propagation of view break.  
             
         
        """
        pass
    @property
    def RetainAnnotations(self) -> bool:
        """
        Getter for property: (bool) RetainAnnotations
         Returns the flag indicating whether to retain  NXOpen::Annotations::Annotation  objects
                when the geometry they are attached to is deleted.  
           When false, the  NXOpen::Annotations::Annotation  
                objects get deleted with the geometry.   
         
        """
        pass
    @RetainAnnotations.setter
    def RetainAnnotations(self, retain_annotations: bool):
        """
        Setter for property: (bool) RetainAnnotations
         Returns the flag indicating whether to retain  NXOpen::Annotations::Annotation  objects
                when the geometry they are attached to is deleted.  
           When false, the  NXOpen::Annotations::Annotation  
                objects get deleted with the geometry.   
         
        """
        pass
    @property
    def ShowFacetEdges(self) -> bool:
        """
        Getter for property: (bool) ShowFacetEdges
         Returns the flag indicating whether to display facet edges in shaded member views.  
              
         
        """
        pass
    @ShowFacetEdges.setter
    def ShowFacetEdges(self, show_facet_edges: bool):
        """
        Setter for property: (bool) ShowFacetEdges
         Returns the flag indicating whether to display facet edges in shaded member views.  
              
         
        """
        pass
    @property
    def Translucency(self) -> bool:
        """
        Getter for property: (bool) Translucency
         Returns the flag indicating whether to display solids in shaded member views with translucency.  
              
         
        """
        pass
    @Translucency.setter
    def Translucency(self, translucency: bool):
        """
        Setter for property: (bool) Translucency
         Returns the flag indicating whether to display solids in shaded member views with translucency.  
              
         
        """
        pass
    @property
    def UpdateViewWithoutLwData(self) -> PartDrafting.UpdateViewWithoutLwDataOption:
        """
        Getter for property: ( PartDrafting.UpdateViewWithoutLwDataOption NXOpen.P) UpdateViewWithoutLwData
         Returns the option specifying the action when missing, incomplete or invalid lightweight 
                bodies are found during view create or update   
            
         
        """
        pass
    @UpdateViewWithoutLwData.setter
    def UpdateViewWithoutLwData(self, updateViewWithoutLwDataOption: PartDrafting.UpdateViewWithoutLwDataOption):
        """
        Setter for property: ( PartDrafting.UpdateViewWithoutLwDataOption NXOpen.P) UpdateViewWithoutLwData
         Returns the option specifying the action when missing, incomplete or invalid lightweight 
                bodies are found during view create or update   
            
         
        """
        pass
    @property
    def VersionObjects(self) -> bool:
        """
        Getter for property: (bool) VersionObjects
         Returns the drafting version objects setting when updating drafting objects and member views   
            
         
        """
        pass
    @VersionObjects.setter
    def VersionObjects(self, version_objects: bool):
        """
        Setter for property: (bool) VersionObjects
         Returns the drafting version objects setting when updating drafting objects and member views   
            
         
        """
        pass
    @property
    def ViewStyle(self) -> PartDrafting.ViewStyleType:
        """
        Getter for property: ( PartDrafting.ViewStyleType NXOpen.P) ViewStyle
         Returns the drafting view style type for preview when placing the view   
            
         
        """
        pass
    @ViewStyle.setter
    def ViewStyle(self, view_style: PartDrafting.ViewStyleType):
        """
        Setter for property: ( PartDrafting.ViewStyleType NXOpen.P) ViewStyle
         Returns the drafting view style type for preview when placing the view   
            
         
        """
        pass
    @property
    def ViewTracking(self) -> bool:
        """
        Getter for property: (bool) ViewTracking
         Returns the flag indicating whether to track a drafting view during preview
                when placing the view.  
           The cursor is tracked using XCYC coordinates.    
         
        """
        pass
    @ViewTracking.setter
    def ViewTracking(self, view_tracking: bool):
        """
        Setter for property: (bool) ViewTracking
         Returns the flag indicating whether to track a drafting view during preview
                when placing the view.  
           The cursor is tracked using XCYC coordinates.    
         
        """
        pass
    @property
    def Width(self) -> PartDrafting.WidthType:
        """
        Getter for property: ( PartDrafting.WidthType NXOpen.P) Width
         Returns the line width of the retained  NXOpen::Annotations::Annotation  objects   
            
         
        """
        pass
    @Width.setter
    def Width(self, width: PartDrafting.WidthType):
        """
        Setter for property: ( PartDrafting.WidthType NXOpen.P) Width
         Returns the line width of the retained  NXOpen::Annotations::Annotation  objects   
            
         
        """
        pass
import NXOpen
import NXOpen.Features.SheetMetal
class PartFlexiblePrintedCircuitDesign(NXOpen.Object): 
    """ Represents the Flexible Printed Circuit Design preferences applicable to part """
    class FlatPatternCalloutOrientationType(Enum):
        """
        Members Include: 
         |Leadered|  Leadered 
         |Aligned|  Aligned 

        """
        Leadered: int
        Aligned: int
        @staticmethod
        def ValueOf(value: int) -> PartFlexiblePrintedCircuitDesign.FlatPatternCalloutOrientationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
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
        def ValueOf(value: int) -> PartFlexiblePrintedCircuitDesign.FlatPatternObjectType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FlexibleCableContactFaceOptions(Enum):
        """
        Members Include: 
         |TopFace|  Top face. 
         |BottomFace|  Bottom face. 

        """
        TopFace: int
        BottomFace: int
        @staticmethod
        def ValueOf(value: int) -> PartFlexiblePrintedCircuitDesign.FlexibleCableContactFaceOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ParameterEntryType(Enum):
        """
        Members Include: 
         |Value|  The manual Value entry method
         |MaterialTable|  The Material Table entry method

        """
        Value: int
        MaterialTable: int
        @staticmethod
        def ValueOf(value: int) -> PartFlexiblePrintedCircuitDesign.ParameterEntryType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PlanarSegmentCurveType(Enum):
        """
        Members Include: 
         |BendCenterLine| 
         |BendTangentLine| 

        """
        BendCenterLine: int
        BendTangentLine: int
        @staticmethod
        def ValueOf(value: int) -> PartFlexiblePrintedCircuitDesign.PlanarSegmentCurveType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FlatPatternCalloutTypeDisplay:
        """
         The members of the following structure are the display data for a
                    callout in a flat pattern drawing member view. 
         PartFlexiblePrintedCircuitDesignFlatPatternCalloutTypeDisplay_Struct NXOpen.P is an alias for  PartFlexiblePrintedCircuitDesign.FlatPatternCalloutTypeDisplay NXOpen.P.
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
         PartFlexiblePrintedCircuitDesignFlatPatternObjectTypeDisplay_Struct NXOpen.P is an alias for  PartFlexiblePrintedCircuitDesign.FlatPatternObjectTypeDisplay NXOpen.P.
        """
        @property
        def Type(self) -> PartFlexiblePrintedCircuitDesign.FlatPatternObjectType:
            """
            Getter for property Type
            Object type

            """
            pass
        @Type.setter
        def Type(self, value: PartFlexiblePrintedCircuitDesign.FlatPatternObjectType):
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
        def Layer(self) -> int:
            """
            Getter for property Layer
            Object Layer

            """
            pass
        @Layer.setter
        def Layer(self, value: int):
            """
            Getter for property Layer
            Object Layer
            Setter for property Layer
            Object Layer

            """
            pass
        @property
        def Font(self) -> NXOpen.DisplayableObject.ObjectFont:
            """
            Getter for property Font
            Object font

            """
            pass
        @Font.setter
        def Font(self, value: NXOpen.DisplayableObject.ObjectFont):
            """
            Getter for property Font
            Object font
            Setter for property Font
            Object font

            """
            pass
        @property
        def Width(self) -> NXOpen.DisplayableObject.ObjectWidth:
            """
            Getter for property Width
            Object width

            """
            pass
        @Width.setter
        def Width(self, value: NXOpen.DisplayableObject.ObjectWidth):
            """
            Getter for property Width
            Object width
            Setter for property Width
            Object width

            """
            pass
    class PlanarSegmentCurveTypeDisplayData:
        """
         The members of the following structure are the display data. 
         PartFlexiblePrintedCircuitDesignPlanarSegmentCurveTypeDisplayData_Struct NXOpen.P is an alias for  PartFlexiblePrintedCircuitDesign.PlanarSegmentCurveTypeDisplayData NXOpen.P.
        """
        @property
        def Type(self) -> PartFlexiblePrintedCircuitDesign.PlanarSegmentCurveType:
            """
            Getter for property Type
            Curve type

            """
            pass
        @Type.setter
        def Type(self, value: PartFlexiblePrintedCircuitDesign.PlanarSegmentCurveType):
            """
            Getter for property Type
            Curve type
            Setter for property Type
            Curve type

            """
            pass
        @property
        def IsEnabled(self) -> int:
            """
            Getter for property IsEnabled
            Enabled status for the curve type

            """
            pass
        @IsEnabled.setter
        def IsEnabled(self, value: int):
            """
            Getter for property IsEnabled
            Enabled status for the curve type
            Setter for property IsEnabled
            Enabled status for the curve type

            """
            pass
        @property
        def Color(self) -> int:
            """
            Getter for property Color
            Curve color

            """
            pass
        @Color.setter
        def Color(self, value: int):
            """
            Getter for property Color
            Curve color
            Setter for property Color
            Curve color

            """
            pass
        @property
        def Font(self) -> NXOpen.DisplayableObject.ObjectFont:
            """
            Getter for property Font
            Curve font

            """
            pass
        @Font.setter
        def Font(self, value: NXOpen.DisplayableObject.ObjectFont):
            """
            Getter for property Font
            Curve font
            Setter for property Font
            Curve font

            """
            pass
        @property
        def Width(self) -> NXOpen.DisplayableObject.ObjectWidth:
            """
            Getter for property Width
            Curve width

            """
            pass
        @Width.setter
        def Width(self, value: NXOpen.DisplayableObject.ObjectWidth):
            """
            Getter for property Width
            Curve width
            Setter for property Width
            Curve width

            """
            pass
    def Commit(self) -> None:
        """
         Commits and applies all the settings done with set_callout_type_display
                    and set_object_type_display. It must be called after a sequence of calls
                    to those methods to cause the view to update. 
        """
        pass
    def GetBendRadius(self) -> NXOpen.Expression:
        """
         Returns the bend radius expression 
         Returns bend_radius ( NXOpen.Expression):  expression object for radius of bend faces.
        """
        pass
    def GetBendReliefDepth(self) -> NXOpen.Expression:
        """
         Returns the bend relief depth 
         Returns bend_relief_depth ( NXOpen.Expression):  expression object for depth of bend relief .
        """
        pass
    def GetBendReliefWidth(self) -> NXOpen.Expression:
        """
         Returns the bend relief width 
         Returns bend_relief_width ( NXOpen.Expression):  expression object for width of bend relief .
        """
        pass
    def GetDeviationalToleranceInFlatSolid(self) -> float:
        """
         Returns the deviational tolerance during Flat Solid simplification 
         Returns deviational_tolerance_in_flat_solid (float):  flag  .
        """
        pass
    def GetFlatPatternAllCalloutTypeDisplay(self) -> List[PartFlexiblePrintedCircuitDesign.FlatPatternCalloutTypeDisplay]:
        """
         Returns the dialog names, identifiers, and enabled status for all the
                    available callout types. 
         Returns displayData ( PartFlexiblePrintedCircuitDesign.FlatPatternCalloutTypeDisplay List[NXOpen):  Array of structures with the callout type display data. .
        """
        pass
    def GetFlatPatternAllObjectTypeDisplay(self) -> List[PartFlexiblePrintedCircuitDesign.FlatPatternObjectTypeDisplay]:
        """
         Returns the types, colors, fonts, widths, and enabled status for all the
                    the available object types. 
         Returns displayData ( PartFlexiblePrintedCircuitDesign.FlatPatternObjectTypeDisplay List[NXOpen):  Array of structures with the object type display data. .
        """
        pass
    def GetFlatPatternCalloutOrientationType(self) -> PartFlexiblePrintedCircuitDesign.FlatPatternCalloutOrientationType:
        """
         Returns the orientation type for flat pattern callouts. 
         Returns orientation ( PartFlexiblePrintedCircuitDesign.FlatPatternCalloutOrientationType NXOpen.P):  The orientation type for the flat pattern callouts. .
        """
        pass
    def GetFlatPatternCalloutTypeContents(self, calloutType: str) -> List[str]:
        """
         Returns the contents for a callout type. 
         Returns contents (List[str]):  The contents for the callout type. .
        """
        pass
    def GetFlatPatternCalloutTypeDisplay(self, calloutType: str) -> PartFlexiblePrintedCircuitDesign.FlatPatternCalloutTypeDisplay:
        """
         Returns the display data for a callout type. The name member of the
                    NXOpen.Preferences.PartFlexiblePrintedCircuitDesign.FlatPatternCalloutTypeDisplay
                    is separately allocated from the callout_type argument string.
                    In some cases the new string will contain an
                    extended form of the callout_type passed in, and that form should
                    be used for subsequent JA calls, without modification. 
         Returns displayData ( PartFlexiblePrintedCircuitDesign.FlatPatternCalloutTypeDisplay NXOpen.P):  The display data for the callout type. .
        """
        pass
    def GetFlatPatternObjectTypeDisplay(self, objectType: PartFlexiblePrintedCircuitDesign.FlatPatternObjectType) -> PartFlexiblePrintedCircuitDesign.FlatPatternObjectTypeDisplay:
        """
         Returns the display data for a flat pattern object type.  
         Returns displayData ( PartFlexiblePrintedCircuitDesign.FlatPatternObjectTypeDisplay NXOpen.P):  The display data for the flat pattern object type. .
        """
        pass
    def GetFlatSolidColor(self) -> int:
        """
        Gets the color of Flat Solid body.
         Returns flatSolidColor (int): .
        """
        pass
    def GetFlatSolidLayer(self) -> int:
        """
        Gets the layer of the Flat Solid body.
         Returns flatSolidLayer (int): .
        """
        pass
    def GetFlexibleCableBottomFaceColor(self) -> NXOpen.NXColor:
        """
         Returns the bottom face color. 
         Returns bottomFaceColor ( NXOpen.NXColor): .
        """
        pass
    def GetFlexibleCableConductorSpacing(self) -> NXOpen.Expression:
        """
         Returns the conductor spacing expression. 
         Returns conductorSpacing ( NXOpen.Expression):  expression object for flexible cable conductor width. .
        """
        pass
    def GetFlexibleCableConductorWidth(self) -> NXOpen.Expression:
        """
         Returns the conductor width expression. 
         Returns conductorWidth ( NXOpen.Expression):  expression object for flexible cable conductor width. .
        """
        pass
    def GetFlexibleCableContactFace(self) -> PartFlexiblePrintedCircuitDesign.FlexibleCableContactFaceOptions:
        """
         Returns the contact face. 
         Returns faceOption ( PartFlexiblePrintedCircuitDesign.FlexibleCableContactFaceOptions NXOpen.P): .
        """
        pass
    def GetFlexibleCableStrippingLength(self) -> NXOpen.Expression:
        """
         Returns the stripping length expression. 
         Returns strippingLength ( NXOpen.Expression):  expression object for flexible cable conductor width. .
        """
        pass
    def GetFlexibleCableTopFaceColor(self) -> NXOpen.NXColor:
        """
         Returns the top face color. 
         Returns topFaceColor ( NXOpen.NXColor): .
        """
        pass
    def GetHoleTreatmentDiameter(self) -> NXOpen.Expression:
        """
         RETURNS the hole treatment diameter value in Flat Pattern operation 
         Returns diameter ( NXOpen.Expression):  expression object for hole diameter value .
        """
        pass
    def GetHoleTreatmentType(self) -> NXOpen.Features.SheetMetal.FeatureProperty:
        """
         RETURNS the hole treatment type in Flat Pattern operation 
         Returns hole_treatment_type ( NXOpen.Features.SheetMetal.FeatureProperty):  hole treatment type .
        """
        pass
    def GetInnerCornerTreatmentType(self) -> NXOpen.Features.SheetMetal.FeatureProperty:
        """
         Returns the inner corner treatment type in Flat as Solid operation 
         Returns inner_corner_treatment_type ( NXOpen.Features.SheetMetal.FeatureProperty):  outer corner treatment type .
        """
        pass
    def GetInnerCornerTreatmentValue(self) -> NXOpen.Expression:
        """
         Returns the inner corner treatment value for Flat as Solid operations 
         Returns inner_corner_treatment ( NXOpen.Expression):  expression object for inner corner treatment value .
        """
        pass
    def GetIsBsplineSimplifiedInFlatSolid(self) -> bool:
        """
         Returns the flag indicating whether B-Splines are simplified as part of the Flat Solid creation
         Returns is_bspline_simplified_in_flat_solid (bool):  flag  .
        """
        pass
    def GetIsSystemGeneratedBendReliefRemovedInFlatSolid(self) -> bool:
        """
         Returns the flag indicating whether or not system generated bend releifs are removed as part of the Flat Solid creation
         Returns is_system_generated_bend_relief_removed (bool):  flag  .
        """
        pass
    def GetMaintainCircularShapeForHolesInFlatSolid(self) -> bool:
        """
         Returns the flag indicating whether or not maintain circular shape for holes as part of the Flat Solid creation.
         Returns isMaintainCircularShapeForHoles (bool):  flag  .
        """
        pass
    def GetMaterial(self) -> str:
        """
         Returns the material name saved with the part 
         Returns materialName (str):  The name of the material saved with the part.
        """
        pass
    def GetMaterialNames(self) -> List[str]:
        """
         Returns the material names defined in the material standards table 
         Returns materialNames (List[str]): .
        """
        pass
    def GetMaterialProperties(self, materialName: str) -> Tuple[List[str], List[str]]:
        """
         Returns the material name saved with the part 
         Returns A tuple consisting of (propertyValues, propertyNames). 
         - propertyValues is: List[str]. property Values .
         - propertyNames is: List[str]. properties .

        """
        pass
    def GetMinimumArcToleranceInFlatSolid(self) -> float:
        """
         Returns the minimum arc tolerance during Flat Solid simplification 
         Returns minimum_arc_tolerance_in_flat_solid (float):  flag  .
        """
        pass
    def GetMultiThicknessLayerScheme(self) -> str:
        """
         Gets the layer scheme for multi thickness. 
         Returns multiHeightLayerScheme (str):  Name of layer scheme .
        """
        pass
    def GetNeutralFactor(self) -> NXOpen.Expression:
        """
         Returns the neutral factor 
         Returns neutral_factor ( NXOpen.Expression):  expression object for neutral factor of bend areas .
        """
        pass
    def GetOuterCornerTreatmentType(self) -> NXOpen.Features.SheetMetal.FeatureProperty:
        """
         Returns the outer corner treatment type in Flat as Solid operation 
         Returns outer_corner_treatment_type ( NXOpen.Features.SheetMetal.FeatureProperty):  outer corner treatment type .
        """
        pass
    def GetOuterCornerTreatmentValue(self) -> NXOpen.Expression:
        """
         Returns the out corner treatment value for Flat as Solid operations 
         Returns outer_corner_treatment ( NXOpen.Expression):  expression object for out corner treatment value .
        """
        pass
    def GetParameterEntryType(self) -> PartFlexiblePrintedCircuitDesign.ParameterEntryType:
        """
         Returns the current parameter entry type 
         Returns parameter_entry_type ( PartFlexiblePrintedCircuitDesign.ParameterEntryType NXOpen.P):  parameter entry type .
        """
        pass
    def GetPhysicalMaterialIntegrationFlag(self) -> bool:
        """
         Returns the physical material library integration flag.
         Returns isPhysicalMaterialIntegrationFlagSet (bool): .
        """
        pass
    def GetPlanarSegmentCurveTypeDisplayData(self, curveType: PartFlexiblePrintedCircuitDesign.PlanarSegmentCurveType) -> PartFlexiblePrintedCircuitDesign.PlanarSegmentCurveTypeDisplayData:
        """
         Returns the display data of a given planar segment curve type for the Flexible Printed Circuit Design application.  
         Returns displayData ( PartFlexiblePrintedCircuitDesign.PlanarSegmentCurveTypeDisplayData NXOpen.P):  The display data for the planar segment curve type. .
        """
        pass
    def GetThickness(self) -> NXOpen.Expression:
        """
         Returns the thickness expression 
         Returns thickness ( NXOpen.Expression):  expression object for sheet thickness .
        """
        pass
    def SetBendRadius(self, update_model: bool, bend_radius: str) -> None:
        """
         Sets the bend radius value 
        """
        pass
    def SetBendReliefDepth(self, update_model: bool, bend_relief_depth: str) -> None:
        """
         Sets the bend relief depth value 
        """
        pass
    def SetBendReliefWidth(self, update_model: bool, bend_relief_width: str) -> None:
        """
         Sets the bend relief depth value 
        """
        pass
    def SetDeviationalToleranceInFlatSolid(self, update_model: bool, deviational_tolerance_in_flat_solid: float) -> None:
        """
         Sets the deviational tolerance during Flat Solid simplification 
        """
        pass
    def SetFlatPatternCalloutOrientationType(self, orientation: PartFlexiblePrintedCircuitDesign.FlatPatternCalloutOrientationType) -> None:
        """
         Sets the orientation type for flat pattern callouts. 
        """
        pass
    def SetFlatPatternCalloutTypeContents(self, calloutType: str, contents: List[str]) -> None:
        """
         Sets the contents for a callout type. 
        """
        pass
    def SetFlatPatternCalloutTypeDisplay(self, calloutType: str, displayData: PartFlexiblePrintedCircuitDesign.FlatPatternCalloutTypeDisplay) -> None:
        """
         Sets the display data for a callout type. 
        """
        pass
    def SetFlatPatternObjectTypeDisplay(self, updateModel: bool, objectType: PartFlexiblePrintedCircuitDesign.FlatPatternObjectType, displayData: PartFlexiblePrintedCircuitDesign.FlatPatternObjectTypeDisplay) -> None:
        """
         Sets the display data for a flat pattern object type. 
        """
        pass
    def SetFlatSolidColor(self, updateModel: bool, flatSolidColor: int) -> None:
        """
        Sets the color of the Flat Solid body.
        """
        pass
    def SetFlatSolidLayer(self, updateModel: bool, flatSolidLayer: int) -> None:
        """
        Sets the layer of the Flat Solid body.
        """
        pass
    def SetFlexibleCableBottomFaceColor(self, bottomFaceColor: NXOpen.NXColor) -> None:
        """
         Sets the bottom face color. 
        """
        pass
    def SetFlexibleCableConductorSpacing(self, conductorSpacing: str) -> None:
        """
         Sets the conductor spacing value string. 
        """
        pass
    def SetFlexibleCableConductorWidth(self, conductorWidth: str) -> None:
        """
         Sets the conductor width value string. 
        """
        pass
    def SetFlexibleCableContactFace(self, faceOption: PartFlexiblePrintedCircuitDesign.FlexibleCableContactFaceOptions) -> None:
        """
         Sets the contact face. 
        """
        pass
    def SetFlexibleCableStrippingLength(self, strippingLength: str) -> None:
        """
         Sets the stripping length value string. 
        """
        pass
    def SetFlexibleCableTopFaceColor(self, topFaceColor: NXOpen.NXColor) -> None:
        """
         Sets the top face color. 
        """
        pass
    def SetHoleTreatmentDiameter(self, update_model: bool, diameter: str) -> None:
        """
         SETS the hole treatment diameter value in Flat Pattern operation 
        """
        pass
    def SetHoleTreatmentType(self, update_model: bool, hole_treatment_type: NXOpen.Features.SheetMetal.FeatureProperty) -> None:
        """
         SETS the hole treatment type in Flat Pattern operation 
        """
        pass
    def SetInnerCornerTreatmentType(self, update_model: bool, inner_corner_treatment_type: NXOpen.Features.SheetMetal.FeatureProperty) -> None:
        """
         Sets the inner corner treatment type in Flat as Solid operation 
        """
        pass
    def SetInnerCornerTreatmentValue(self, update_model: bool, inner_corner_treatment: str) -> None:
        """
         Sets the the inner corner treatment value for Flat as Solid operations 
        """
        pass
    def SetIsBsplineSimplifiedInFlatSolid(self, update_model: bool, is_bspline_simplified_in_flat_solid: bool) -> None:
        """
         Sets the flag indicating whether or not B-Splines are simplified as part of the Flat Solid creation
        """
        pass
    def SetIsSystemGeneratedBendReliefRemovedInFlatSolid(self, update_model: bool, is_system_generated_bend_relief_removed: bool) -> None:
        """
         Sets the flag indicating whether or not system generated bend releifs are removed as part of the Flat Solid creation
        """
        pass
    def SetMaintainCircularShapeForHolesInFlatSolid(self, updateModel: bool, isMaintainCircularShapeForHoles: bool) -> None:
        """
         Sets the flag indicating whether or not maintain circular shape for holes as part of the Flat Solid creation.
        """
        pass
    def SetMaterial(self, update_model: bool, standardName: str) -> None:
        """
         Sets the material standard 
        """
        pass
    def SetMinimumArcToleranceInFlatSolid(self, update_model: bool, minimum_arc_tolerance_in_flat_solid: float) -> None:
        """
         Sets the minimum arc tolerance during Flat Solid simplification 
        """
        pass
    def SetMultiThicknessLayerScheme(self, update_model: bool, multiHeightLayerScheme: str) -> None:
        """
         Sets the layer scheme for multi thickness. 
        """
        pass
    def SetNeutralFactor(self, update_model: bool, neutral_factor: str) -> None:
        """
         Sets the neutral factor value 
        """
        pass
    def SetOuterCornerTreatmentType(self, update_model: bool, outer_corner_treatment_type: NXOpen.Features.SheetMetal.FeatureProperty) -> None:
        """
         Sets the the outer corner treatment type in Flat as Solid operation 
        """
        pass
    def SetOuterCornerTreatmentValue(self, update_model: bool, outer_corner_treatment: str) -> None:
        """
         Sets the outer corner treatment value for Flat as Solid operations 
        """
        pass
    def SetParameterEntryType(self, update_model: bool, parameter_entry_type: PartFlexiblePrintedCircuitDesign.ParameterEntryType) -> None:
        """
         Sets the parameter entry type 
        """
        pass
    def SetPhysicalMaterialIntegrationFlag(self, setPhysicalMaterialIntegrationFlag: bool) -> None:
        """
         Sets physical material library integration flag.
        """
        pass
    def SetPlanarSegmentCurveTypeDisplayData(self, updateModel: bool, curveType: PartFlexiblePrintedCircuitDesign.PlanarSegmentCurveType, displayData: PartFlexiblePrintedCircuitDesign.PlanarSegmentCurveTypeDisplayData) -> None:
        """
         Sets the display data of a given planar segment curve type for the Flexible Printed Circuit Design application. 
        """
        pass
    def SetThickness(self, update_model: bool, thickness: str) -> None:
        """
         Sets the thickness value string 
        """
        pass
import NXOpen
class PartModeling(NXOpen.Object): 
    """ Represents the set of Modeling preferences applicable to part """
    class CurveCurvatureDisplayType(Enum):
        """
        Members Include: 
         |Comb|  Curve curvature display is Curvature Comb 
         |RadiusOfComb|  Curve curvature display is radius of Curvature Comb 

        """
        Comb: int
        RadiusOfComb: int
        @staticmethod
        def ValueOf(value: int) -> PartModeling.CurveCurvatureDisplayType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DensityUnitType(Enum):
        """
        Members Include: 
         |LbPerCuInch|  Unit is pound per cubic inch  
         |LbPerCuFeet|  Unit is pound per cubic feet 
         |GmPerCuCm|  Unit is gram per cubic centimeter 
         |KgPerCuMeter|  Unit is kg per cubic meter 

        """
        LbPerCuInch: int
        LbPerCuFeet: int
        GmPerCuCm: int
        KgPerCuMeter: int
        @staticmethod
        def ValueOf(value: int) -> PartModeling.DensityUnitType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class GridKnotLineFontType(Enum):
        """
        Members Include: 
         |Solid|  
         |Dashed|  
         |Phantom|  
         |Centerline|  
         |Dotted|  
         |LongDashed|  
         |DottedDashed|  
         |Eight|  Long Dashed Double Dotted 
         |Nine|  Long Dashed Dotted for OOTB fonts and Undulating for shipbuilding fonts 
         |Ten|  Long Dashed Triplicate Dotted for OOTB fonts and Zigzag for shipbuilding fonts 
         |Eleven|  Long Dashed Double Short Dashed for OOTB fonts and Railway for shipbuilding fonts 

        """
        Solid: int
        Dashed: int
        Phantom: int
        Centerline: int
        Dotted: int
        LongDashed: int
        DottedDashed: int
        Eight: int
        Nine: int
        Ten: int
        Eleven: int
        @staticmethod
        def ValueOf(value: int) -> PartModeling.GridKnotLineFontType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class GridResolutionType(Enum):
        """
        Members Include: 
         |NotSet|  No specific selection for grid resolution 
         |Coarse|  Coarse grid resolution 
         |Standard|  Standard grid resolution 
         |Fine|  Fine grid resolution 
         |ExtraFine|  Extra Fine grid resolution 
         |UltraFine|  Ultra Fine grid resolution 

        """
        NotSet: int
        Coarse: int
        Standard: int
        Fine: int
        ExtraFine: int
        UltraFine: int
        @staticmethod
        def ValueOf(value: int) -> PartModeling.GridResolutionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngleToleranceData(self) -> float:
        """
        Getter for property: (float) AngleToleranceData
         Returns the angle tolerance data.  
           Angle tolerance is the maximum allowable angle between the surface normals at 
            corresponding points, or the maximum allowable angle between curve tangent vectors at corresponding points. 
            This value can be read from any part but can only be set when the part owning these preferences is the work part.   
         
        """
        pass
    @AngleToleranceData.setter
    def AngleToleranceData(self, angle_tol_data: float):
        """
        Setter for property: (float) AngleToleranceData
         Returns the angle tolerance data.  
           Angle tolerance is the maximum allowable angle between the surface normals at 
            corresponding points, or the maximum allowable angle between curve tangent vectors at corresponding points. 
            This value can be read from any part but can only be set when the part owning these preferences is the work part.   
         
        """
        pass
    @property
    def C0KnotLineColor(self) -> int:
        """
        Getter for property: (int) C0KnotLineColor
         Returns the C0 knot line color   
            
         
        """
        pass
    @C0KnotLineColor.setter
    def C0KnotLineColor(self, knot_line_color: int):
        """
        Setter for property: (int) C0KnotLineColor
         Returns the C0 knot line color   
            
         
        """
        pass
    @property
    def C0KnotLineFont(self) -> PartModeling.GridKnotLineFontType:
        """
        Getter for property: ( PartModeling.GridKnotLineFontType NXOpen.P) C0KnotLineFont
         Returns the C0 knot line font   
            
         
        """
        pass
    @C0KnotLineFont.setter
    def C0KnotLineFont(self, knot_line_font: PartModeling.GridKnotLineFontType):
        """
        Setter for property: ( PartModeling.GridKnotLineFontType NXOpen.P) C0KnotLineFont
         Returns the C0 knot line font   
            
         
        """
        pass
    @property
    def C0KnotUseBodyColor(self) -> bool:
        """
        Getter for property: (bool) C0KnotUseBodyColor
         Returns whether c0 knot line use body color  
            
         
        """
        pass
    @C0KnotUseBodyColor.setter
    def C0KnotUseBodyColor(self, use_body_color: bool):
        """
        Setter for property: (bool) C0KnotUseBodyColor
         Returns whether c0 knot line use body color  
            
         
        """
        pass
    @property
    def C0KnotUseBodyFont(self) -> bool:
        """
        Getter for property: (bool) C0KnotUseBodyFont
         Returns whether C0_knot use body font  
            
         
        """
        pass
    @C0KnotUseBodyFont.setter
    def C0KnotUseBodyFont(self, use_body_font: bool):
        """
        Setter for property: (bool) C0KnotUseBodyFont
         Returns whether C0_knot use body font  
            
         
        """
        pass
    @property
    def C1KnotLineColor(self) -> int:
        """
        Getter for property: (int) C1KnotLineColor
         Returns the C1 knot line color   
            
         
        """
        pass
    @C1KnotLineColor.setter
    def C1KnotLineColor(self, knot_line_color: int):
        """
        Setter for property: (int) C1KnotLineColor
         Returns the C1 knot line color   
            
         
        """
        pass
    @property
    def C1KnotLineFont(self) -> PartModeling.GridKnotLineFontType:
        """
        Getter for property: ( PartModeling.GridKnotLineFontType NXOpen.P) C1KnotLineFont
         Returns the C1 knot line font   
            
         
        """
        pass
    @C1KnotLineFont.setter
    def C1KnotLineFont(self, knot_line_font: PartModeling.GridKnotLineFontType):
        """
        Setter for property: ( PartModeling.GridKnotLineFontType NXOpen.P) C1KnotLineFont
         Returns the C1 knot line font   
            
         
        """
        pass
    @property
    def C1KnotUseBodyColor(self) -> bool:
        """
        Getter for property: (bool) C1KnotUseBodyColor
         Returns whether c1 knot line use body color  
            
         
        """
        pass
    @C1KnotUseBodyColor.setter
    def C1KnotUseBodyColor(self, use_body_color: bool):
        """
        Setter for property: (bool) C1KnotUseBodyColor
         Returns whether c1 knot line use body color  
            
         
        """
        pass
    @property
    def C1KnotUseBodyFont(self) -> bool:
        """
        Getter for property: (bool) C1KnotUseBodyFont
         Returns whether C1_knot use body font  
            
         
        """
        pass
    @C1KnotUseBodyFont.setter
    def C1KnotUseBodyFont(self, use_body_font: bool):
        """
        Setter for property: (bool) C1KnotUseBodyFont
         Returns whether C1_knot use body font  
            
         
        """
        pass
    @property
    def C2KnotLineColor(self) -> int:
        """
        Getter for property: (int) C2KnotLineColor
         Returns the C2 knot line color   
            
         
        """
        pass
    @C2KnotLineColor.setter
    def C2KnotLineColor(self, knot_line_color: int):
        """
        Setter for property: (int) C2KnotLineColor
         Returns the C2 knot line color   
            
         
        """
        pass
    @property
    def C2KnotLineFont(self) -> PartModeling.GridKnotLineFontType:
        """
        Getter for property: ( PartModeling.GridKnotLineFontType NXOpen.P) C2KnotLineFont
         Returns the C2 knot line font   
            
         
        """
        pass
    @C2KnotLineFont.setter
    def C2KnotLineFont(self, knot_line_font: PartModeling.GridKnotLineFontType):
        """
        Setter for property: ( PartModeling.GridKnotLineFontType NXOpen.P) C2KnotLineFont
         Returns the C2 knot line font   
            
         
        """
        pass
    @property
    def C2KnotUseBodyColor(self) -> bool:
        """
        Getter for property: (bool) C2KnotUseBodyColor
         Returns whether c2 knot line use body color  
            
         
        """
        pass
    @C2KnotUseBodyColor.setter
    def C2KnotUseBodyColor(self, use_body_color: bool):
        """
        Setter for property: (bool) C2KnotUseBodyColor
         Returns whether c2 knot line use body color  
            
         
        """
        pass
    @property
    def C2KnotUseBodyFont(self) -> bool:
        """
        Getter for property: (bool) C2KnotUseBodyFont
         Returns whether C2_knot use body font  
            
         
        """
        pass
    @C2KnotUseBodyFont.setter
    def C2KnotUseBodyFont(self, use_body_font: bool):
        """
        Setter for property: (bool) C2KnotUseBodyFont
         Returns whether C2_knot use body font  
            
         
        """
        pass
    @property
    def ConvertAnalyticToConvergentAngularTolerance(self) -> float:
        """
        Getter for property: (float) ConvertAnalyticToConvergentAngularTolerance
         Returns the angular tolerance for converting analytic body to Convergent body   
            
         
        """
        pass
    @ConvertAnalyticToConvergentAngularTolerance.setter
    def ConvertAnalyticToConvergentAngularTolerance(self, dAnalyticToConvergentAngTol: float):
        """
        Setter for property: (float) ConvertAnalyticToConvergentAngularTolerance
         Returns the angular tolerance for converting analytic body to Convergent body   
            
         
        """
        pass
    @property
    def ConvertAnalyticToConvergentDistanceTolerance(self) -> float:
        """
        Getter for property: (float) ConvertAnalyticToConvergentDistanceTolerance
         Returns the distance tolerance for converting analytic body to Convergent body   
            
         
        """
        pass
    @ConvertAnalyticToConvergentDistanceTolerance.setter
    def ConvertAnalyticToConvergentDistanceTolerance(self, dAnalyticToConvergentDistTol: float):
        """
        Setter for property: (float) ConvertAnalyticToConvergentDistanceTolerance
         Returns the distance tolerance for converting analytic body to Convergent body   
            
         
        """
        pass
    @property
    def ConvertAnalyticToConvergentMaximumChordLength(self) -> float:
        """
        Getter for property: (float) ConvertAnalyticToConvergentMaximumChordLength
         Returns the maximum chord length for converting analytic body to convergent body   
            
         
        """
        pass
    @ConvertAnalyticToConvergentMaximumChordLength.setter
    def ConvertAnalyticToConvergentMaximumChordLength(self, dAnalyticToConvergentMaxChordLength: float):
        """
        Setter for property: (float) ConvertAnalyticToConvergentMaximumChordLength
         Returns the maximum chord length for converting analytic body to convergent body   
            
         
        """
        pass
    @property
    def ConvertAnalyticToConvergentMaximumFacetWidth(self) -> float:
        """
        Getter for property: (float) ConvertAnalyticToConvergentMaximumFacetWidth
         Returns the maximum facet width for converting analytic body to convergent body   
            
         
        """
        pass
    @ConvertAnalyticToConvergentMaximumFacetWidth.setter
    def ConvertAnalyticToConvergentMaximumFacetWidth(self, dAnalyticToConvergentMaxFacetWidth: float):
        """
        Setter for property: (float) ConvertAnalyticToConvergentMaximumFacetWidth
         Returns the maximum facet width for converting analytic body to convergent body   
            
         
        """
        pass
    @property
    def CurveCurvatureDisplay(self) -> PartModeling.CurveCurvatureDisplayType:
        """
        Getter for property: ( PartModeling.CurveCurvatureDisplayType NXOpen.P) CurveCurvatureDisplay
         Returns the curve curvature display.  
             
         
        """
        pass
    @CurveCurvatureDisplay.setter
    def CurveCurvatureDisplay(self, curve_curvature_display: PartModeling.CurveCurvatureDisplayType):
        """
        Setter for property: ( PartModeling.CurveCurvatureDisplayType NXOpen.P) CurveCurvatureDisplay
         Returns the curve curvature display.  
             
         
        """
        pass
    @property
    def CurveCurvatureShowCap(self) -> bool:
        """
        Getter for property: (bool) CurveCurvatureShowCap
         Returns the curve curvature display show cap line   
            
         
        """
        pass
    @CurveCurvatureShowCap.setter
    def CurveCurvatureShowCap(self, show_cap: bool):
        """
        Setter for property: (bool) CurveCurvatureShowCap
         Returns the curve curvature display show cap line   
            
         
        """
        pass
    @property
    def CurveCurvatureStyle(self) -> int:
        """
        Getter for property: (int) CurveCurvatureStyle
         Returns the curve curvature display style   
            
         
        """
        pass
    @CurveCurvatureStyle.setter
    def CurveCurvatureStyle(self, style: int):
        """
        Setter for property: (int) CurveCurvatureStyle
         Returns the curve curvature display style   
            
         
        """
        pass
    @property
    def CutViewUpdateDelayed(self) -> bool:
        """
        Getter for property: (bool) CutViewUpdateDelayed
         Returns the state of the cut view delay update flag.  
              
         
        """
        pass
    @CutViewUpdateDelayed.setter
    def CutViewUpdateDelayed(self, is_delayed: bool):
        """
        Setter for property: (bool) CutViewUpdateDelayed
         Returns the state of the cut view delay update flag.  
              
         
        """
        pass
    @property
    def Density(self) -> float:
        """
        Getter for property: (float) Density
         Returns the density.  
           The value used to set this property must be in
                the units of the density units preference
                (that is, the value of  NXOpen::Preferences::PartModeling::DensityUnit ).
                Likewise, the density returned by this property is in the units
                of the density units preference.   
         
        """
        pass
    @Density.setter
    def Density(self, density: float):
        """
        Setter for property: (float) Density
         Returns the density.  
           The value used to set this property must be in
                the units of the density units preference
                (that is, the value of  NXOpen::Preferences::PartModeling::DensityUnit ).
                Likewise, the density returned by this property is in the units
                of the density units preference.   
         
        """
        pass
    @property
    def DensityUnit(self) -> PartModeling.DensityUnitType:
        """
        Getter for property: ( PartModeling.DensityUnitType NXOpen.P) DensityUnit
         Returns the density unit   
            
         
        """
        pass
    @DensityUnit.setter
    def DensityUnit(self, density_unit: PartModeling.DensityUnitType):
        """
        Setter for property: ( PartModeling.DensityUnitType NXOpen.P) DensityUnit
         Returns the density unit   
            
         
        """
        pass
    @property
    def DisplayCurveCurvatureOutside(self) -> bool:
        """
        Getter for property: (bool) DisplayCurveCurvatureOutside
         Returns the curve curvature display style to show it on the insideoutside of the curve   
            
         
        """
        pass
    @DisplayCurveCurvatureOutside.setter
    def DisplayCurveCurvatureOutside(self, display_outside: bool):
        """
        Setter for property: (bool) DisplayCurveCurvatureOutside
         Returns the curve curvature display style to show it on the insideoutside of the curve   
            
         
        """
        pass
    @property
    def DistanceToleranceData(self) -> float:
        """
        Getter for property: (float) DistanceToleranceData
         Returns the modeling distance tolerance data.  
           This tolerance value is used throughout the Modeling application, 
            such as for creating swept and revolved solid bodies and sectioning solid bodies. For example, when creating 
            sheet bodies, the distance tolerance specifies the maximum allowable distance between corresponding points on 
            the original surface and the resulting B-surface. This value can be read from any part but can only be set
            when the part owning these preferences is the work part.    
         
        """
        pass
    @DistanceToleranceData.setter
    def DistanceToleranceData(self, dist_tol_data: float):
        """
        Setter for property: (float) DistanceToleranceData
         Returns the modeling distance tolerance data.  
           This tolerance value is used throughout the Modeling application, 
            such as for creating swept and revolved solid bodies and sectioning solid bodies. For example, when creating 
            sheet bodies, the distance tolerance specifies the maximum allowable distance between corresponding points on 
            the original surface and the resulting B-surface. This value can be read from any part but can only be set
            when the part owning these preferences is the work part.    
         
        """
        pass
    @property
    def GridLineColor(self) -> int:
        """
        Getter for property: (int) GridLineColor
         Returns the grid line color   
            
         
        """
        pass
    @GridLineColor.setter
    def GridLineColor(self, grid_line_color: int):
        """
        Setter for property: (int) GridLineColor
         Returns the grid line color   
            
         
        """
        pass
    @property
    def GridLineFont(self) -> PartModeling.GridKnotLineFontType:
        """
        Getter for property: ( PartModeling.GridKnotLineFontType NXOpen.P) GridLineFont
         Returns the grid line font   
            
         
        """
        pass
    @GridLineFont.setter
    def GridLineFont(self, grid_line_font: PartModeling.GridKnotLineFontType):
        """
        Setter for property: ( PartModeling.GridKnotLineFontType NXOpen.P) GridLineFont
         Returns the grid line font   
            
         
        """
        pass
    @property
    def GridLinesUCount(self) -> int:
        """
        Getter for property: (int) GridLinesUCount
         Returns the U count for grid lines.  
           It is the number of grid curves in the U direction of the faces of the body   
         
        """
        pass
    @GridLinesUCount.setter
    def GridLinesUCount(self, grid_line_u_count: int):
        """
        Setter for property: (int) GridLinesUCount
         Returns the U count for grid lines.  
           It is the number of grid curves in the U direction of the faces of the body   
         
        """
        pass
    @property
    def GridLinesVCount(self) -> int:
        """
        Getter for property: (int) GridLinesVCount
         Returns the V count for grid lines.  
           It is the number of grid curves in the V direction of the faces of the body    
         
        """
        pass
    @GridLinesVCount.setter
    def GridLinesVCount(self, grid_line_v_count: int):
        """
        Setter for property: (int) GridLinesVCount
         Returns the V count for grid lines.  
           It is the number of grid curves in the V direction of the faces of the body    
         
        """
        pass
    @property
    def GridResolution(self) -> PartModeling.GridResolutionType:
        """
        Getter for property: ( PartModeling.GridResolutionType NXOpen.P) GridResolution
         Returns the grid resolution.  
           The six options, None, Coarse, Standard, Fine, Extra Fine and Ultra Fine, produce a grid that 
            is respectively more detailed. The None option shows no grid at all in wireframe mode.   
         
        """
        pass
    @GridResolution.setter
    def GridResolution(self, grid_resolution: PartModeling.GridResolutionType):
        """
        Setter for property: ( PartModeling.GridResolutionType NXOpen.P) GridResolution
         Returns the grid resolution.  
           The six options, None, Coarse, Standard, Fine, Extra Fine and Ultra Fine, produce a grid that 
            is respectively more detailed. The None option shows no grid at all in wireframe mode.   
         
        """
        pass
    @property
    def GridUseBodyColor(self) -> bool:
        """
        Getter for property: (bool) GridUseBodyColor
         Returns whether grid line use body color  
            
         
        """
        pass
    @GridUseBodyColor.setter
    def GridUseBodyColor(self, use_body_color: bool):
        """
        Setter for property: (bool) GridUseBodyColor
         Returns whether grid line use body color  
            
         
        """
        pass
    @property
    def GridUseBodyFont(self) -> bool:
        """
        Getter for property: (bool) GridUseBodyFont
         Returns whether grid use body font  
            
         
        """
        pass
    @GridUseBodyFont.setter
    def GridUseBodyFont(self, use_body_font: bool):
        """
        Setter for property: (bool) GridUseBodyFont
         Returns whether grid use body font  
            
         
        """
        pass
    @property
    def MaxChordLengthOption(self) -> bool:
        """
        Getter for property: (bool) MaxChordLengthOption
         Returns the maximum chord length option for converting analytic body to convergent body   
            
         
        """
        pass
    @MaxChordLengthOption.setter
    def MaxChordLengthOption(self, maxChordLength: bool):
        """
        Setter for property: (bool) MaxChordLengthOption
         Returns the maximum chord length option for converting analytic body to convergent body   
            
         
        """
        pass
    @property
    def MaxFacetWidthOption(self) -> bool:
        """
        Getter for property: (bool) MaxFacetWidthOption
         Returns the maximum facet width option for converting analytic body to convergent body   
            
         
        """
        pass
    @MaxFacetWidthOption.setter
    def MaxFacetWidthOption(self, maxFacetWidth: bool):
        """
        Setter for property: (bool) MaxFacetWidthOption
         Returns the maximum facet width option for converting analytic body to convergent body   
            
         
        """
        pass
    @property
    def OptimizeCurve(self) -> bool:
        """
        Getter for property: (bool) OptimizeCurve
         Returns the optimize curve flag   
            
         
        """
        pass
    @OptimizeCurve.setter
    def OptimizeCurve(self, optimizeCurve: bool):
        """
        Setter for property: (bool) OptimizeCurve
         Returns the optimize curve flag   
            
         
        """
        pass
    @property
    def OptimizeCurveAngleToleranceFactor(self) -> float:
        """
        Getter for property: (float) OptimizeCurveAngleToleranceFactor
         Returns the optimize curve angle tolerance factor   
            
         
        """
        pass
    @OptimizeCurveAngleToleranceFactor.setter
    def OptimizeCurveAngleToleranceFactor(self, optimieCurveAngleFactor: float):
        """
        Setter for property: (float) OptimizeCurveAngleToleranceFactor
         Returns the optimize curve angle tolerance factor   
            
         
        """
        pass
    @property
    def OptimizeCurveDistanceToleranceFactor(self) -> float:
        """
        Getter for property: (float) OptimizeCurveDistanceToleranceFactor
         Returns the optimize curve distance tolerance factor   
            
         
        """
        pass
    @OptimizeCurveDistanceToleranceFactor.setter
    def OptimizeCurveDistanceToleranceFactor(self, optimieCurveDistanceFactor: float):
        """
        Setter for property: (float) OptimizeCurveDistanceToleranceFactor
         Returns the optimize curve distance tolerance factor   
            
         
        """
        pass
    @property
    def OptimizeCurveToleranceFactor(self) -> float:
        """
        Getter for property: (float) OptimizeCurveToleranceFactor
         Returns the optimize curve tolerance factor   
            
         
        """
        pass
    @OptimizeCurveToleranceFactor.setter
    def OptimizeCurveToleranceFactor(self, optimieCurveFactor: float):
        """
        Setter for property: (float) OptimizeCurveToleranceFactor
         Returns the optimize curve tolerance factor   
            
         
        """
        pass
    @property
    def TreatOneDegreeBsplineAsPolyline(self) -> bool:
        """
        Getter for property: (bool) TreatOneDegreeBsplineAsPolyline
         Returns the option to treat degree one bspline as polyline   
            
         
        """
        pass
    @TreatOneDegreeBsplineAsPolyline.setter
    def TreatOneDegreeBsplineAsPolyline(self, treatOneDegreeBsplineAsPolyline: bool):
        """
        Setter for property: (bool) TreatOneDegreeBsplineAsPolyline
         Returns the option to treat degree one bspline as polyline   
            
         
        """
        pass
    def GetHistoryMode(self) -> bool:
        """
         Returns whether the part is in History or History-Free mode.
                Return true for History mode or false for History-Free mode.  
         Returns history (bool):   .
        """
        pass
    def GetIsSavedByWebApp(self) -> bool:
        """
         Get the flag to indicate if it is saved by web application 
         Returns isSavedByWebApp (bool):   .
        """
        pass
    def GetKeepLocalFeatures(self) -> bool:
        """
         Returns whether keep NX6-era local feature in the part 
         Returns keepLocalFeatures (bool):   .
        """
        pass
    def SetHistoryFreeMode(self) -> None:
        """
         Changes the modeling mode to History-Free Modeling. This will remove parameters from features in the model. Feature edit will not be available and the model will not update.
        """
        pass
    def SetHistoryMode(self) -> None:
        """
         Changes the modeling mode to History Modeling. This will remove Local feature from the model.
        """
        pass
    def SetIsSavedByWebApp(self, isSavedByWebApp: bool) -> None:
        """
         Set the flag to indicate if it is saved by web application 
        """
        pass
    def SetKeepLocalFeatures(self, keepLocalFeatures: bool) -> None:
        """
         This will keep NX6-era Local feature when changing to History-free mode.
        """
        pass
import NXOpen
class PartObject(NXOpen.Object): 
    """ Represents the set of object preferences applicable to entire part. All the preferences available at 
    UG GUI for object can be set by using this class except work layer. Work Layer should be set by using 
    NXOpen.Layer.LayerManager class which holds a work layer property. """
    class ColorSelection(Enum):
        """
        Members Include: 
         |NoChange|  No Change 
         |DefaultColor|  Default Color 
         |Color|  User Defined Color 

        """
        NoChange: int
        DefaultColor: int
        Color: int
        @staticmethod
        def ValueOf(value: int) -> PartObject.ColorSelection:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LineFontType(Enum):
        """
        Members Include: 
         |PartDefault|  Default Value from Part
         |Solid|  Solid 
         |Dashed|  Dashed 
         |Phantom|  Phantom 
         |Centerline|  Centerline 
         |Dotted|  Dotted 
         |LongDashed|  Long Dashed 
         |DottedDashed|  Dotted Dashed 
         |Eight|  Long Dashed Double Dotted 
         |Nine|  Long Dashed Dotted for OOTB fonts and Undulating for shipbuilding fonts 
         |Ten|  Long Dashed Triplicate Dotted for OOTB fonts and Zigzag for shipbuilding fonts 
         |Eleven|  Long Dashed Double Short Dashed for OOTB fonts and Railway for shipbuilding fonts 

        """
        PartDefault: int
        Solid: int
        Dashed: int
        Phantom: int
        Centerline: int
        Dotted: int
        LongDashed: int
        DottedDashed: int
        Eight: int
        Nine: int
        Ten: int
        Eleven: int
        @staticmethod
        def ValueOf(value: int) -> PartObject.LineFontType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ObjectType(Enum):
        """
        Members Include: 
         |General|  Default Type Value 
         |Line|  Line 
         |Arc|  Arc 
         |Conic|  Conic 
         |Spline|  Spline 
         |Solidbody|  Solid Body 
         |Sheetbody|  Sheet Body 
         |Datum|  Datum 
         |Point|  Point 
         |CoordinateSystem|  Coordinate System 
         |AllButDefault|  All But Default 
         |DatumCsys|  Datum CSYS Feature 
         |Traceline|  Traceline 
         |InfiniteLine|  Infinite Line 
         |PointCloud|  Point Cloud 

        """
        General: int
        Line: int
        Arc: int
        Conic: int
        Spline: int
        Solidbody: int
        Sheetbody: int
        Datum: int
        Point: int
        CoordinateSystem: int
        AllButDefault: int
        DatumCsys: int
        Traceline: int
        InfiniteLine: int
        PointCloud: int
        @staticmethod
        def ValueOf(value: int) -> PartObject.ObjectType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class WidthType(Enum):
        """
        Members Include: 
         |PartDefault|  Default Value from Part 
         |ThinWidth|  Thin Width 
         |NormalWidth|  Normal Width 
         |ThickWidth|  Thick Width 
         |WidthOne| 
         |WidthTwo| 
         |WidthThree| 
         |WidthFour| 
         |WidthFive| 
         |WidthSix| 
         |WidthSeven| 
         |WidthEight| 
         |WidthNine| 

        """
        PartDefault: int
        ThinWidth: int
        NormalWidth: int
        ThickWidth: int
        WidthOne: int
        WidthTwo: int
        WidthThree: int
        WidthFour: int
        WidthFive: int
        WidthSix: int
        WidthSeven: int
        WidthEight: int
        WidthNine: int
        @staticmethod
        def ValueOf(value: int) -> PartObject.WidthType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FaceAnalysis(self) -> bool:
        """
        Getter for property: (bool) FaceAnalysis
         Returns the face analysis flag for Solid and Sheets   
            
         
        """
        pass
    @FaceAnalysis.setter
    def FaceAnalysis(self, face_analysis: bool):
        """
        Setter for property: (bool) FaceAnalysis
         Returns the face analysis flag for Solid and Sheets   
            
         
        """
        pass
    @property
    def PartiallyShaded(self) -> bool:
        """
        Getter for property: (bool) PartiallyShaded
         Returns the partially shaded flag for Solid and Sheets   
            
         
        """
        pass
    @PartiallyShaded.setter
    def PartiallyShaded(self, partially_shaded: bool):
        """
        Setter for property: (bool) PartiallyShaded
         Returns the partially shaded flag for Solid and Sheets   
            
         
        """
        pass
    @property
    def PointSymbol(self) -> int:
        """
        Getter for property: (int) PointSymbol
         Returns the point symbol for Point   
            
         
        """
        pass
    @PointSymbol.setter
    def PointSymbol(self, pointSymbol: int):
        """
        Setter for property: (int) PointSymbol
         Returns the point symbol for Point   
            
         
        """
        pass
    @property
    def Translucency(self) -> int:
        """
        Getter for property: (int) Translucency
         Returns the translucency value   
            
         
        """
        pass
    @Translucency.setter
    def Translucency(self, translucency: int):
        """
        Setter for property: (int) Translucency
         Returns the translucency value   
            
         
        """
        pass
    def ConvertColorNumberToRGBValue(self, color_number: int) -> ViewVisualizationSpecialEffects.ColorRGB:
        """
         Converts color number to RGB constituents. The color number passed should be between 1 to 216 
         Returns fog_color_rgb_value ( ViewVisualizationSpecialEffects.ColorRGB NXOpen.P):  Equivalent RGB constituents .
        """
        pass
    def ConvertRGBValueToColorNumber(self, fog_color_rgb_value: ViewVisualizationSpecialEffects.ColorRGB) -> int:
        """
         Converts RGB color constituents to color number. The Red, Green and Blue color constituents
                should be between 0 to 255. 
         Returns color_number (int):  Equivalent color value .
        """
        pass
    def GetColor(self, type: PartObject.ObjectType) -> int:
        """
         Returns the current color value for specified type. 
                The equivalent RGB values can be found by calling 
                ConvertColorNumberToRGBValue
                Red Component is ((((216 - color_number) % 36)6) 51)
                Green component is (((216 - color_number)36)  51)
                Blue is (((216 - color_number) % 6) 51). 
                So for example if returned color value is 47 then 
                Red is ((((216 - 47) % 36)6) 51) = (((169 % 36)6) 51) = ((256) 51) = 451 = 204
                Green is (((216 - 47)36)  51) = ((16936)  51) = 451 = 204
                Blue is (((216 - 47) % 6) 51) = ((169 % 6) 51) = 151 = 51
                
         Returns color (int):   .
        """
        pass
    def GetLegacyLineWidthMap(self) -> List[PartObject.WidthType]:
        """
         Gets line width map that is used to convert legacy line widths to
                    new line widths.
                    Following widths are considered as legacy line widths.
                    Preferences.PartObject.WidthType.ThinWidth
                    Preferences.PartObject.WidthType.NormalWidth
                    Preferences.PartObject.WidthType.ThickWidth
                    New line widths contain corresponding line widths for above three
                    legacy line widths respectively. New line widths start at
                    Preferences.PartObject.WidthType.WidthOne.
                  
         Returns newLineWidths ( PartObject.WidthType List[NXOpen):  
                        Array of 3 new widths each corresponding to a legacy width.
                        First element corresponds to Thin width
                        Second element corresponds to Normal width
                        Third element corresponds to Thick width. .
        """
        pass
    def GetLineFont(self, type: PartObject.ObjectType) -> PartObject.LineFontType:
        """
         Returns the current line font for specified object type 
         Returns line_font ( PartObject.LineFontType NXOpen.P):   .
        """
        pass
    def GetObjectColor(self, type: PartObject.ObjectType) -> Tuple[int, PartObject.ColorSelection]:
        """
         Returns the current color value for specified type. 
                The equivalent RGB values can be found by calling 
                ConvertColorNumberToRGBValue
                Red Component is ((((216 - color_number) % 36)6) 51)
                Green component is (((216 - color_number)36)  51)
                Blue is (((216 - color_number) % 6) 51). 
                So for example if returned color value is 47 then 
                Red is ((((216 - 47) % 36)6) 51) = (((169 % 36)6) 51) = ((256) 51) = 451 = 204
                Green is (((216 - 47)36)  51) = ((16936)  51) = 451 = 204
                Blue is (((216 - 47) % 6) 51) = ((169 % 6) 51) = 151 = 51
                
         Returns A tuple consisting of (color, colorSelection). 
         - color is: int.  .
         - colorSelection is:  PartObject.ColorSelection NXOpen.P.  .

        """
        pass
    def GetWidth(self, type: PartObject.ObjectType) -> PartObject.WidthType:
        """
         Returns the current width for specified object type 
         Returns width ( PartObject.WidthType NXOpen.P):   .
        """
        pass
    def MigrateLegacyLineWidths(self) -> bool:
        """
         Migrates line width attributes stored in the part file to 
                    corresponding new line widths. The migration is performed
                    based on the legacy line width map stored in the part file.
                    See Preferences.PartObject.GetLegacyLineWidthMap 
                    
                    Line widths of various displayable objects such as solids,
                    wireframe, drawing views etc. will be updated to new line widths.
                    Display is regenerated if necessary to reflect the changes.
                    A displayable object, that already has new line width assigned to
                    it, is not affected.
                  
         Returns migrated (bool):  At least one legacy line width 
                                                     attribute has been migrated. .
        """
        pass
    def SetColor(self, type: PartObject.ObjectType, color: int) -> None:
        """
         Sets the color. For Default color pass -2 as color value and for no change pass -1. 
                For other color calculate the color in RGB format.  
                If you pass R value of Red component G value of Green and B value of Blue the color will be:
                color = (((255-R)51)6 + ((255-G)51)36 + ((255-B)51)1) + 1 ;
                Where R G and B values are between 0 and 255 . So for Green (0,255,0)we will pass
                color = (((255-0)51)6 + ((255-255)51)36 + ((255-0)51)1) + 1 = 30+0+5+1 = 36
                The equivalent color number value can be found by calling 
                ConvertRGBValueToColorNumber
                
        """
        pass
    def SetLegacyLineWidthMap(self, newLineWidths: List[PartObject.WidthType]) -> None:
        """
         Sets line width map that is used to convert legacy line widths to
                    new line widths.
                    See Preferences.PartObject.GetLegacyLineWidthMap 
                    
                    The new line widths used to map legacy line width are in logical order; 
                    i.e.; Preferences.PartObject.WidthType.ThinWidth
                    maps to a smaller width value compared to 
                    Preferences.PartObject.WidthType.NormalWidth and
                    so on. Otherwise, the legacy line width map will be rejected.
                  
        """
        pass
    def SetLineFont(self, type: PartObject.ObjectType, line_font: PartObject.LineFontType) -> None:
        """
         Sets line font for specified object type 
        """
        pass
    def SetObjectColor(self, type: PartObject.ObjectType, colorSelection: PartObject.ColorSelection, color: int) -> None:
        """
         Sets the color. 
                For default color use NXOpen.Preferences.PartObject.ColorSelection.DefaultColor
                For no change use NXOpen.Preferences.PartObject.ColorSelection.NoChange
                For other color, use NXOpen.Preferences.PartObject.ColorSelection.Color and calculate the color in RGB format.
                If you pass R value of Red component G value of Green and B value of Blue the color will be:
                color = (((255-R)51)6 + ((255-G)51)36 + ((255-B)51)1) + 1 ;
                Where R G and B values are between 0 and 255 . So for Green (0,255,0)we will pass
                color = (((255-0)51)6 + ((255-255)51)36 + ((255-0)51)1) + 1 = 30+0+5+1 = 36
                The equivalent color number value can be found by calling 
                ConvertRGBValueToColorNumber
                
        """
        pass
    def SetWidth(self, type: PartObject.ObjectType, width: PartObject.WidthType) -> None:
        """
         Sets width for specified object type  
        """
        pass
import NXOpen
class PartPreferences(NXOpen.Object): 
    """ Represents set of preferences applicable to displayed part. """
    @property
    def Workplane(self) -> WorkPlane:
        """
        Getter for property: ( WorkPlane NXOpen.P) Workplane
         Returns the workplane preferences.  
             
         
        """
        pass
    @property
    def Modeling() -> PartModeling:
        """
         Returns object for doing Modeling preferences settings applicable to displayed part 
        """
        pass
    @property
    def Drafting() -> PartDrafting:
        """
         Returns object for doing Drafting preferences settings applicable to displayed part 
        """
        pass
    @property
    def ObjectPreferences() -> PartObject:
        """
         Returns object for doing object preferences settings applicable to displayed part 
        """
        pass
    @property
    def UserInterface() -> PartUserInterface:
        """
         Returns object for doing User Interface preferences settings applicable to displayed part 
        """
        pass
    @property
    def VisualVisualization() -> PartVisualizationVisual:
        """
         Returns object for doing Visualization preferences settings for Visual tab applicable to displayed part 
        """
        pass
    @property
    def LineVisualization() -> PartVisualizationLine:
        """
         Returns object for doing Visualization preferences settings for Line tab applicable to displayed part 
        """
        pass
    @property
    def NamesBorderVisualization() -> PartVisualizationNamesBorders:
        """
         Returns object for doing Visualization preferences settings for NamesBorder tab applicable to displayed part 
        """
        pass
    @property
    def ColorSettingVisualization() -> PartVisualizationColorSetting:
        """
         Returns object for doing Visualization preferences settings for color setting tab applicable to displayed part 
        """
        pass
    @property
    def ShadeVisualization() -> PartVisualizationShade:
        """
         Returns object for doing Visualization preferences settings for shade tab applicable to displayed part 
        """
        pass
    @property
    def PartSheetmetal() -> PartSheetmetal:
        """
         Returns object to modify the Preference settings for NX Sheetmetal application 
        """
        pass
    @property
    def PartFlexiblePrintedCircuitDesign() -> PartFlexiblePrintedCircuitDesign:
        """
         Returns object to modify the Preference settings for Flexible Printed Circuit Design application 
        """
        pass
    @property
    def PartAeroSheetmetal() -> PartAeroSheetmetal:
        """
         Returns object to modify the Preference settings for Aerospace Sheetmetal application 
        """
        pass
    @property
    def PartSketch() -> PartSketch:
        """
         Returns object to modify the Preference settings for Sketcher application 
        """
        pass
    @property
    def DraftingPreference() -> DraftingPreferenceManager:
        """
         Returns object to modify the Preference settings for PMIdrafting application 
        """
        pass
    @property
    def EmphasisVisualization() -> PartVisualizationEmphasis:
        """
         Returns object for doing Visualization preferences settings for emphasis tab applicable to displayed part 
        """
        pass
    @property
    def PerformanceVisualization() -> PartVisualizationPerformance:
        """
         Returns object for doing Visualization performance preference 
                    settings for displayed part.
                
        """
        pass
    @property
    def ScreenVisualization() -> PartVisualizationScreen:
        """
         Returns object for doing Visualization preferences settings for screen tab applicable to displayed part 
        """
        pass
    @property
    def AppearanceMgmtPreference() -> PartAppearanceMgrPreference:
        """
         This is an internal API and can be changed at any time 
        """
        pass
    @property
    def SheetMetalPreferences() -> SheetMetalPreferencesManager:
        """
         Returns object to modify the Preferences settings for NX Sheetmetal application 
        """
        pass
    @property
    def FpcdPreferences() -> FpcdPreferencesManager:
        """
         Returns object to modify the Preferences settings for NX Flexbile printed circuit design application 
        """
        pass
import NXOpen
import NXOpen.Features.SheetMetal
class PartSheetmetal(NXOpen.Object): 
    """ Represents the NX Sheetmetal preferences applicable to part """
    class BendDefinitionMethodOptions(Enum):
        """
        Members Include: 
         |NeutralFactorValue|  The neutral factor value method
         |BendTable|  The bend table method
         |BendAllowanceFormula|  The bend allowance formula method
         |MaterialTable|  The material table method
         |ToolTable|  The tool table method
         |BendAllowanceTable|  The bend allowance table method
         |BendDeductionTable|  The bend deduction table method
         |BendDeductionFormula|  The bend deduction formula method
         |Din6935Formula|  The DIN6935 formula method

        """
        NeutralFactorValue: int
        BendTable: int
        BendAllowanceFormula: int
        MaterialTable: int
        ToolTable: int
        BendAllowanceTable: int
        BendDeductionTable: int
        BendDeductionFormula: int
        Din6935Formula: int
        @staticmethod
        def ValueOf(value: int) -> PartSheetmetal.BendDefinitionMethodOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FlatPatternCalloutOrientationType(Enum):
        """
        Members Include: 
         |Leadered|  Leadered 
         |Aligned|  Aligned 

        """
        Leadered: int
        Aligned: int
        @staticmethod
        def ValueOf(value: int) -> PartSheetmetal.FlatPatternCalloutOrientationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
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
         |StrikePoint|  
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
        StrikePoint: int
        LighteningHoleCenter: int
        JoggleLine: int
        AddedTopGeometry: int
        AddedBottomGeometry: int
        ToolMarker: int
        Hole: int
        Centermark: int
        @staticmethod
        def ValueOf(value: int) -> PartSheetmetal.FlatPatternObjectType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ParameterEntryType(Enum):
        """
        Members Include: 
         |Value|  The manual Value entry method
         |MaterialTable|  The Material Table entry method
         |ToolIdTable|  The Tool ID Table entry method

        """
        Value: int
        MaterialTable: int
        ToolIdTable: int
        @staticmethod
        def ValueOf(value: int) -> PartSheetmetal.ParameterEntryType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TabCurveType(Enum):
        """
        Members Include: 
         |BendCenterLine|  
         |BendTangentLine|  

        """
        BendCenterLine: int
        BendTangentLine: int
        @staticmethod
        def ValueOf(value: int) -> PartSheetmetal.TabCurveType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FlatPatternCalloutTypeDisplay:
        """
         The members of the following structure are the display data for a
                    callout in a flat pattern drawing member view. 
         PartSheetmetalFlatPatternCalloutTypeDisplay_Struct NXOpen.P is an alias for  PartSheetmetal.FlatPatternCalloutTypeDisplay NXOpen.P.
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
         PartSheetmetalFlatPatternObjectTypeDisplay_Struct NXOpen.P is an alias for  PartSheetmetal.FlatPatternObjectTypeDisplay NXOpen.P.
        """
        @property
        def Type(self) -> PartSheetmetal.FlatPatternObjectType:
            """
            Getter for property Type
            Object type

            """
            pass
        @Type.setter
        def Type(self, value: PartSheetmetal.FlatPatternObjectType):
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
        def Layer(self) -> int:
            """
            Getter for property Layer
            Object Layer

            """
            pass
        @Layer.setter
        def Layer(self, value: int):
            """
            Getter for property Layer
            Object Layer
            Setter for property Layer
            Object Layer

            """
            pass
        @property
        def Font(self) -> NXOpen.DisplayableObject.ObjectFont:
            """
            Getter for property Font
            Object font

            """
            pass
        @Font.setter
        def Font(self, value: NXOpen.DisplayableObject.ObjectFont):
            """
            Getter for property Font
            Object font
            Setter for property Font
            Object font

            """
            pass
        @property
        def Width(self) -> NXOpen.DisplayableObject.ObjectWidth:
            """
            Getter for property Width
            Object width

            """
            pass
        @Width.setter
        def Width(self, value: NXOpen.DisplayableObject.ObjectWidth):
            """
            Getter for property Width
            Object width
            Setter for property Width
            Object width

            """
            pass
    class TabCurveTypeDisplayData:
        """
         The members of the following structure are the display data of a tab curve type
         PartSheetmetalTabCurveTypeDisplayData_Struct NXOpen.P is an alias for  PartSheetmetal.TabCurveTypeDisplayData NXOpen.P.
        """
        @property
        def Type(self) -> PartSheetmetal.TabCurveType:
            """
            Getter for property Type
            Curve type

            """
            pass
        @Type.setter
        def Type(self, value: PartSheetmetal.TabCurveType):
            """
            Getter for property Type
            Curve type
            Setter for property Type
            Curve type

            """
            pass
        @property
        def IsEnabled(self) -> int:
            """
            Getter for property IsEnabled
            Enabled status of the curve type

            """
            pass
        @IsEnabled.setter
        def IsEnabled(self, value: int):
            """
            Getter for property IsEnabled
            Enabled status of the curve type
            Setter for property IsEnabled
            Enabled status of the curve type

            """
            pass
        @property
        def Color(self) -> int:
            """
            Getter for property Color
            Curve color

            """
            pass
        @Color.setter
        def Color(self, value: int):
            """
            Getter for property Color
            Curve color
            Setter for property Color
            Curve color

            """
            pass
        @property
        def Font(self) -> NXOpen.DisplayableObject.ObjectFont:
            """
            Getter for property Font
            Curve font

            """
            pass
        @Font.setter
        def Font(self, value: NXOpen.DisplayableObject.ObjectFont):
            """
            Getter for property Font
            Curve font
            Setter for property Font
            Curve font

            """
            pass
        @property
        def Width(self) -> NXOpen.DisplayableObject.ObjectWidth:
            """
            Getter for property Width
            Curve width

            """
            pass
        @Width.setter
        def Width(self, value: NXOpen.DisplayableObject.ObjectWidth):
            """
            Getter for property Width
            Curve width
            Setter for property Width
            Curve width

            """
            pass
    def Commit(self) -> None:
        """
         Commits and applies all the settings done with set_callout_type_display
                    and set_object_type_display. It must be called after a sequence of calls
                    to those methods to cause the view to update. 
        """
        pass
    def GetBendAllowanceFormula(self) -> str:
        """
         RETURNS the bend allowance formula 
         Returns bend_allowance_formula (str):  bend allowance formula.
        """
        pass
    def GetBendDeductionFormula(self) -> str:
        """
         Returns the bend deduction formula
         Returns bend_deduction_formula (str):  bend deduction formula.
        """
        pass
    def GetBendDefinitionMethodOption(self) -> PartSheetmetal.BendDefinitionMethodOptions:
        """
         RETURNS the bend definition method 
         Returns bend_definition_method ( PartSheetmetal.BendDefinitionMethodOptions NXOpen.P):  bend definition method option .
        """
        pass
    def GetBendTable(self) -> str:
        """
         RETURNS the bend table name 
         Returns bend_table (str):  bend table name.
        """
        pass
    def GetDepthThreshold(self) -> NXOpen.Expression:
        """
         RETURNS the depth threshold 
         Returns depth_threshold ( NXOpen.Expression):  expression object for depth threshold of joggle .
        """
        pass
    def GetDeviationalToleranceInFlatSolid(self) -> float:
        """
         RETURNS the deviational tolerance during Flat Solid simplification 
         Returns deviational_tolerance_in_flat_solid (float):  flag  .
        """
        pass
    def GetDistanceThreshold(self) -> NXOpen.Expression:
        """
         RETURNS the distance threshold 
         Returns distance_threshold ( NXOpen.Expression):  expression object for distance threshold of joggle .
        """
        pass
    def GetFlatPatternAllCalloutTypeDisplay(self) -> List[PartSheetmetal.FlatPatternCalloutTypeDisplay]:
        """
         Returns the dialog names, identifiers, and enabled status for all the
                    available callout types. 
         Returns displayData ( PartSheetmetal.FlatPatternCalloutTypeDisplay List[NXOpen):  Array of structures with the callout type display data. .
        """
        pass
    def GetFlatPatternAllObjectTypeDisplay(self) -> List[PartSheetmetal.FlatPatternObjectTypeDisplay]:
        """
         Returns the types, colors, fonts, widths, and enabled status for all the
                    the available object types. 
         Returns displayData ( PartSheetmetal.FlatPatternObjectTypeDisplay List[NXOpen):  Array of structures with the object type display data. .
        """
        pass
    def GetFlatPatternCalloutOrientationType(self) -> PartSheetmetal.FlatPatternCalloutOrientationType:
        """
         Returns the orientation type for flat pattern callouts. 
         Returns orientation ( PartSheetmetal.FlatPatternCalloutOrientationType NXOpen.P):  The orientation type for the flat pattern callouts. .
        """
        pass
    def GetFlatPatternCalloutTypeContents(self, calloutType: str) -> List[str]:
        """
         Returns the contents for a callout type. 
         Returns contents (List[str]):  The contents for the callout type. .
        """
        pass
    def GetFlatPatternCalloutTypeDisplay(self, calloutType: str) -> PartSheetmetal.FlatPatternCalloutTypeDisplay:
        """
         Returns the display data for a callout type. The name member of the
                    NXOpen.Preferences.PartFlexiblePrintedCircuitDesign.FlatPatternCalloutTypeDisplay
                    is separately allocated from the callout_type argument string.
                    In some cases the new string will contain an
                    extended form of the callout_type passed in, and that form should
                    be used for subsequent JA calls, without modification. 
         Returns displayData ( PartSheetmetal.FlatPatternCalloutTypeDisplay NXOpen.P):  The display data for the callout type. .
        """
        pass
    def GetFlatPatternObjectTypeDisplay(self, objectType: PartSheetmetal.FlatPatternObjectType) -> PartSheetmetal.FlatPatternObjectTypeDisplay:
        """
         Returns the display data for a flat pattern object type.  
         Returns displayData ( PartSheetmetal.FlatPatternObjectTypeDisplay NXOpen.P):  The display data for the flat pattern object type. .
        """
        pass
    def GetFlatSolidColor(self) -> int:
        """
        Gets the color of Flat Solid body.
         Returns flatSolidColor (int): .
        """
        pass
    def GetFlatSolidLayer(self) -> int:
        """
        Gets the layer of Flat Solid body.
         Returns flatSolidLayer (int): .
        """
        pass
    def GetFlexibleCableBottomFaceColor(self) -> NXOpen.NXColor:
        """
         RETURNS the bottom face color. 
         Returns bottomFaceColor ( NXOpen.NXColor): .
        """
        pass
    def GetFlexibleCableTopFaceColor(self) -> NXOpen.NXColor:
        """
         RETURNS the top face color. 
         Returns topFaceColor ( NXOpen.NXColor): .
        """
        pass
    def GetHoleTreatmentDiameter(self) -> NXOpen.Expression:
        """
         RETURNS the hole treatment diameter value in Flat Pattern operation 
         Returns diameter ( NXOpen.Expression):  expression object for hole diameter value .
        """
        pass
    def GetHoleTreatmentType(self) -> NXOpen.Features.SheetMetal.FeatureProperty:
        """
         RETURNS the hole treatment type in Flat Pattern operation 
         Returns hole_treatment_type ( NXOpen.Features.SheetMetal.FeatureProperty):  hole treatment type .
        """
        pass
    def GetInnerCornerTreatmentType(self) -> NXOpen.Features.SheetMetal.FeatureProperty:
        """
         RETURNS the inner corner treatment type in Flat as Solid operation 
         Returns inner_corner_treatment_type ( NXOpen.Features.SheetMetal.FeatureProperty):  outer corner treatment type .
        """
        pass
    def GetInnerCornerTreatmentValue(self) -> NXOpen.Expression:
        """
         RETURNS the inner corner treatment value for Flat as Solid operations 
         Returns inner_corner_treatment ( NXOpen.Expression):  expression object for inner corner treatment value .
        """
        pass
    def GetIsBsplineSimplifiedInFlatSolid(self) -> bool:
        """
         RETURNS the flag indicating whether B-Splines are simplified as part of the Flat Solid creation
         Returns is_bspline_simplified_in_flat_solid (bool):  flag  .
        """
        pass
    def GetIsSystemGeneratedBendReliefRemovedInFlatSolid(self) -> bool:
        """
         RETURNS the flag indicating whether or not system generated bend releifs are removed as part of the Flat Solid creation
         Returns is_system_generated_bend_relief_removed (bool):  flag  .
        """
        pass
    def GetLouverCutoutCurvesAsInteriorCutout(self) -> bool:
        """
         Louver cutout curves should display as interior cutout curves or not in flat pattern output
         Returns isLouverCutoutCurvesDisplayAsInteriorCutout (bool):  flag  .
        """
        pass
    def GetMaintainCircularShapeForHolesInFlatSolid(self) -> bool:
        """
         Returns the flag indicating whether or not maintain circular shape for holes as part of the Flat Solid creation
         Returns is_maintain_circular_shape_for_holes (bool):  flag  .
        """
        pass
    def GetMaterial(self) -> str:
        """
         RETURNS the material name saved with the part 
         Returns materialName (str):  The name of the material saved with the part.
        """
        pass
    def GetMaterialNames(self) -> List[str]:
        """
         RETURNS the material names defined in the material standards table 
         Returns materialNames (List[str]): .
        """
        pass
    def GetMaterialProperties(self, materialName: str) -> Tuple[List[str], List[str]]:
        """
         RETURNS the material name saved with the part 
         Returns A tuple consisting of (propertyValues, propertyNames). 
         - propertyValues is: List[str].property Values .
         - propertyNames is: List[str].property Names .

        """
        pass
    def GetMinimumArcToleranceInFlatSolid(self) -> float:
        """
         RETURNS the minimum arc tolerance during Flat Solid simplification 
         Returns minimum_arc_tolerance_in_flat_solid (float):  flag  .
        """
        pass
    def GetMinimumToolClearance(self) -> NXOpen.Expression:
        """
         Returns the minimum tool clearance expression 
         Returns minToolClearance ( NXOpen.Expression):  expression object for punch tool clearance .
        """
        pass
    def GetMinimumWebLength(self) -> NXOpen.Expression:
        """
         Returns the minimum Web Length expression 
         Returns minWebLength ( NXOpen.Expression):  expression object for Web Length  .
        """
        pass
    def GetOffsetRadius(self) -> NXOpen.Expression:
        """
         RETURNS the offset radius 
         Returns offset_radius ( NXOpen.Expression):  expression object for offset radius of joggle .
        """
        pass
    def GetOuterCornerTreatmentType(self) -> NXOpen.Features.SheetMetal.FeatureProperty:
        """
         RETURNS the outer corner treatment type in Flat as Solid operation 
         Returns outer_corner_treatment_type ( NXOpen.Features.SheetMetal.FeatureProperty):  outer corner treatment type .
        """
        pass
    def GetOuterCornerTreatmentValue(self) -> NXOpen.Expression:
        """
         RETURNS the out corner treatment value for Flat as Solid operations 
         Returns outer_corner_treatment ( NXOpen.Expression):  expression object for out corner treatment value .
        """
        pass
    def GetParameterEntryType(self) -> PartSheetmetal.ParameterEntryType:
        """
         Returns the current parameter entry type 
         Returns parameter_entry_type ( PartSheetmetal.ParameterEntryType NXOpen.P):  parameter entry type .
        """
        pass
    def GetPhysicalMaterialIntegrationFlag(self) -> bool:
        """
         Returns the physical material library integration flag.
         Returns isPhysicalMaterialIntegrationFlagSet (bool): .
        """
        pass
    def GetSecondaryToolName(self) -> str:
        """
         Returns the secondaryToolName refered from Material Table 
         Returns secondaryToolName (str):  secondaryToolName.
        """
        pass
    def GetStationaryRadius(self) -> NXOpen.Expression:
        """
         RETURNS the stationary radius 
         Returns stationary_radius ( NXOpen.Expression):  expression object for stationary radius of joggle .
        """
        pass
    def GetTabCurveTypeDisplayData(self, curveType: PartSheetmetal.TabCurveType) -> PartSheetmetal.TabCurveTypeDisplayData:
        """
         Returns the display data for a given tab curve type.  
         Returns displayData ( PartSheetmetal.TabCurveTypeDisplayData NXOpen.P):  The display data for the tab curves object type. .
        """
        pass
    def GetTool(self) -> str:
        """
         Returns the tool name saved with the part 
         Returns toolName (str):  The name of the tool saved with the part.
        """
        pass
    def GetToolNames(self) -> List[str]:
        """
         Returns the tool names defined in the material standards table 
         Returns toolNames (List[str]): .
        """
        pass
    def GetToolProperties(self, toolName: str) -> Tuple[List[str], List[str]]:
        """
         Returns the tool properties saved with the part 
         Returns A tuple consisting of (propertyValues, propertyNames). 
         - propertyValues is: List[str].property Values .
         - propertyNames is: List[str].property Names .

        """
        pass
    def SetBendAllowanceFormula(self, update_model: bool, bend_allowance_formula: str) -> None:
        """
         SETS the bend allowance formula 
        """
        pass
    def SetBendDeductionFormula(self, update_model: bool, bend_deduction_formula: str) -> None:
        """
         
        """
        pass
    def SetBendDefinitionMethodOption(self, update_model: bool, bend_definition_method: PartSheetmetal.BendDefinitionMethodOptions) -> None:
        """
         SETS the bend definition method 
        """
        pass
    def SetBendTable(self, update_model: bool, bend_table: str) -> None:
        """
         SETS the bend table name 
        """
        pass
    def SetDepthThreshold(self, update_model: bool, depth_threshold: str) -> None:
        """
         THE depth threshold 
        """
        pass
    def SetDeviationalToleranceInFlatSolid(self, update_model: bool, deviational_tolerance_in_flat_solid: float) -> None:
        """
         SETS the deviational tolerance during Flat Solid simplification 
        """
        pass
    def SetDistanceThreshold(self, update_model: bool, distance_threshold: str) -> None:
        """
         THE distance threshold 
        """
        pass
    def SetFlatPatternCalloutOrientationType(self, orientation: PartSheetmetal.FlatPatternCalloutOrientationType) -> None:
        """
         Sets the orientation type for flat pattern callouts. 
        """
        pass
    def SetFlatPatternCalloutTypeContents(self, calloutType: str, contents: List[str]) -> None:
        """
         Sets the contents for a callout type. 
        """
        pass
    def SetFlatPatternCalloutTypeDisplay(self, calloutType: str, displayData: PartSheetmetal.FlatPatternCalloutTypeDisplay) -> None:
        """
         Sets the display data for a callout type. 
        """
        pass
    def SetFlatPatternObjectTypeDisplay(self, updateModel: bool, objectType: PartSheetmetal.FlatPatternObjectType, displayData: PartSheetmetal.FlatPatternObjectTypeDisplay) -> None:
        """
         Sets the display data for a flat pattern object type. 
        """
        pass
    def SetFlatSolidColor(self, updateModel: bool, flatSolidColor: int) -> None:
        """
        Sets the color of Flat Solid body.
        """
        pass
    def SetFlatSolidLayer(self, updateModel: bool, flatSolidLayer: int) -> None:
        """
        Sets the layer of Flat Solid Body.
        """
        pass
    def SetFlexibleCableBottomFaceColor(self, bottomFaceColor: NXOpen.NXColor) -> None:
        """
         THE bottom face color. 
        """
        pass
    def SetFlexibleCableTopFaceColor(self, topFaceColor: NXOpen.NXColor) -> None:
        """
         THE top face color. 
        """
        pass
    def SetHoleTreatmentDiameter(self, update_model: bool, diameter: str) -> None:
        """
         SETS the hole treatment diameter value in Flat Pattern operation 
        """
        pass
    def SetHoleTreatmentType(self, update_model: bool, hole_treatment_type: NXOpen.Features.SheetMetal.FeatureProperty) -> None:
        """
         SETS the hole treatment type in Flat Pattern operation 
        """
        pass
    def SetInnerCornerTreatmentType(self, update_model: bool, inner_corner_treatment_type: NXOpen.Features.SheetMetal.FeatureProperty) -> None:
        """
         SETS the inner corner treatment type in Flat as Solid operation 
        """
        pass
    def SetInnerCornerTreatmentValue(self, update_model: bool, inner_corner_treatment: str) -> None:
        """
         SETS the inner corner treatment value for Flat as Solid operations 
        """
        pass
    def SetIsBsplineSimplifiedInFlatSolid(self, update_model: bool, is_bspline_simplified_in_flat_solid: bool) -> None:
        """
         SETS the flag indicating whether or not B-Splines are simplified as part of the Flat Solid creation
        """
        pass
    def SetIsSystemGeneratedBendReliefRemovedInFlatSolid(self, update_model: bool, is_system_generated_bend_relief_removed: bool) -> None:
        """
         SETS the flag indicating whether or not system generated bend releifs are removed as part of the Flat Solid creation
        """
        pass
    def SetLouverCutoutCurvesAsInteriorCutout(self, update_model: bool, isLouverCurvesDisplayAsCutout: bool) -> None:
        """
          
        """
        pass
    def SetMaintainCircularShapeForHolesInFlatSolid(self, update_model: bool, is_maintain_circular_shape_for_holes: bool) -> None:
        """
         Sets the flag indicating whether or not maintain circular shape for holes as part of the Flat Solid creation
        """
        pass
    def SetMaterial(self, update_model: bool, standardName: str) -> None:
        """
         The material standard 
        """
        pass
    def SetMinimumArcToleranceInFlatSolid(self, update_model: bool, minimum_arc_tolerance_in_flat_solid: float) -> None:
        """
         SETS the minimum arc tolerance during Flat Solid simplification 
        """
        pass
    def SetMinimumToolClearance(self, updateModel: bool, minToolClearance: str) -> None:
        """
        Sets minimum tool clearance expression 
        """
        pass
    def SetMinimumWebLength(self, updateModel: bool, minWebLength: str) -> None:
        """
        Sets minimum Web Length expression 
        """
        pass
    def SetOffsetRadius(self, update_model: bool, offset_radius: str) -> None:
        """
         THE offset radius 
        """
        pass
    def SetOuterCornerTreatmentType(self, update_model: bool, outer_corner_treatment_type: NXOpen.Features.SheetMetal.FeatureProperty) -> None:
        """
         SETS the outer corner treatment type in Flat as Solid operation 
        """
        pass
    def SetOuterCornerTreatmentValue(self, update_model: bool, outer_corner_treatment: str) -> None:
        """
         THE outer corner treatment value for Flat as Solid operations 
        """
        pass
    def SetParameterEntryType(self, update_model: bool, parameter_entry_type: PartSheetmetal.ParameterEntryType) -> None:
        """
         Sets the parameter entry type 
        """
        pass
    def SetPhysicalMaterialIntegrationFlag(self, setPhysicalMaterialIntegrationFlag: bool) -> None:
        """
         Sets physical material library integration flag.
        """
        pass
    def SetSecondaryToolName(self, update_model: bool, secondaryToolName: str) -> None:
        """
         
        """
        pass
    def SetStationaryRadius(self, update_model: bool, stationary_radius: str) -> None:
        """
         THE stationary radius 
        """
        pass
    def SetTabCurveTypeDisplayData(self, updateModel: bool, curveType: PartSheetmetal.TabCurveType, displayData: PartSheetmetal.TabCurveTypeDisplayData) -> None:
        """
         Sets the display data for a given tab curve type. 
        """
        pass
    def SetTool(self, update_model: bool, standardName: str) -> None:
        """
         The tool standard 
        """
        pass
import NXOpen
class PartSketch(NXOpen.Object): 
    """ Represents the set of Sketcher preferences applicable to entire part. Other Sketch preference 
settings are available with NXOpen.Preferences.SessionSketch for settings applicable to session
and with NXOpen.Preferences.SketchPreferences for Sketch specific Preferences """
    @property
    def AutomaticDimensionColor(self) -> int:
        """
        Getter for property: (int) AutomaticDimensionColor
         Returns the sketch automatic dimension color   
            
         
        """
        pass
    @AutomaticDimensionColor.setter
    def AutomaticDimensionColor(self, sketch_automatic_dimension_color: int):
        """
        Setter for property: (int) AutomaticDimensionColor
         Returns the sketch automatic dimension color   
            
         
        """
        pass
    @property
    def ConflictingColor(self) -> int:
        """
        Getter for property: (int) ConflictingColor
         Returns the sketch conflicting color   
            
         
        """
        pass
    @ConflictingColor.setter
    def ConflictingColor(self, sketch_conflicting_color: int):
        """
        Setter for property: (int) ConflictingColor
         Returns the sketch conflicting color   
            
         
        """
        pass
    @property
    def ConstantDimensionColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) ConstantDimensionColor
         Returns the sketch constant dimension color   
            
         
        """
        pass
    @ConstantDimensionColor.setter
    def ConstantDimensionColor(self, sketchConstantDimensionColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) ConstantDimensionColor
         Returns the sketch constant dimension color   
            
         
        """
        pass
    @property
    def CurveColor(self) -> int:
        """
        Getter for property: (int) CurveColor
         Returns the sketch curve color   
            
         
        """
        pass
    @CurveColor.setter
    def CurveColor(self, sketch_curve_color: int):
        """
        Setter for property: (int) CurveColor
         Returns the sketch curve color   
            
         
        """
        pass
    @property
    def DOFColor(self) -> int:
        """
        Getter for property: (int) DOFColor
         Returns the sketch degree of freedom arrow color   
            
         
        """
        pass
    @DOFColor.setter
    def DOFColor(self, sketch_d_o_f_color: int):
        """
        Setter for property: (int) DOFColor
         Returns the sketch degree of freedom arrow color   
            
         
        """
        pass
    @property
    def DimensionColor(self) -> int:
        """
        Getter for property: (int) DimensionColor
         Returns the sketch dimension color   
            
         
        """
        pass
    @DimensionColor.setter
    def DimensionColor(self, sketch_dimension_color: int):
        """
        Setter for property: (int) DimensionColor
         Returns the sketch dimension color   
            
         
        """
        pass
    @property
    def FullyDefinedColor(self) -> int:
        """
        Getter for property: (int) FullyDefinedColor
         Returns the sketch fully defined constraint color   
            
         
        """
        pass
    @FullyDefinedColor.setter
    def FullyDefinedColor(self, sketch_fully_color: int):
        """
        Setter for property: (int) FullyDefinedColor
         Returns the sketch fully defined constraint color   
            
         
        """
        pass
    @property
    def GeometricConstraintColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) GeometricConstraintColor
         Returns the sketch geometric constraint color   
            
         
        """
        pass
    @GeometricConstraintColor.setter
    def GeometricConstraintColor(self, sketchGeometricConstraintColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) GeometricConstraintColor
         Returns the sketch geometric constraint color   
            
         
        """
        pass
    @property
    def InactiveSketchColor(self) -> int:
        """
        Getter for property: (int) InactiveSketchColor
         Returns the inactive sketch color   
            
         
        """
        pass
    @InactiveSketchColor.setter
    def InactiveSketchColor(self, sketch_inactive_color: int):
        """
        Setter for property: (int) InactiveSketchColor
         Returns the inactive sketch color   
            
         
        """
        pass
    @property
    def LockedObjectColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) LockedObjectColor
         Returns the sketch unlocked object color   
            
         
        """
        pass
    @LockedObjectColor.setter
    def LockedObjectColor(self, sketchLockedObjectColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) LockedObjectColor
         Returns the sketch unlocked object color   
            
         
        """
        pass
    @property
    def MovableCurveColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) MovableCurveColor
         Returns the sketch movable curve color   
            
         
        """
        pass
    @MovableCurveColor.setter
    def MovableCurveColor(self, sketchMovableCurveColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) MovableCurveColor
         Returns the sketch movable curve color   
            
         
        """
        pass
    @property
    def NonWorkRegionColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) NonWorkRegionColor
         Returns the sketch non-work region color   
            
         
        """
        pass
    @NonWorkRegionColor.setter
    def NonWorkRegionColor(self, sketchNonWorkRegionColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) NonWorkRegionColor
         Returns the sketch non-work region color   
            
         
        """
        pass
    @property
    def OutOfDateColor(self) -> int:
        """
        Getter for property: (int) OutOfDateColor
         Returns the sketch out of date curve color   
            
         
        """
        pass
    @OutOfDateColor.setter
    def OutOfDateColor(self, sketch_out_of_date_color: int):
        """
        Setter for property: (int) OutOfDateColor
         Returns the sketch out of date curve color   
            
         
        """
        pass
    @property
    def OverconstrainedColor(self) -> int:
        """
        Getter for property: (int) OverconstrainedColor
         Returns the sketch overconstrained color   
            
         
        """
        pass
    @OverconstrainedColor.setter
    def OverconstrainedColor(self, sketch_overconstrained_color: int):
        """
        Setter for property: (int) OverconstrainedColor
         Returns the sketch overconstrained color   
            
         
        """
        pass
    @property
    def PartiallyDefinedColor(self) -> int:
        """
        Getter for property: (int) PartiallyDefinedColor
         Returns the sketch partially defined constraint color   
            
         
        """
        pass
    @PartiallyDefinedColor.setter
    def PartiallyDefinedColor(self, sketch_partial_color: int):
        """
        Setter for property: (int) PartiallyDefinedColor
         Returns the sketch partially defined constraint color   
            
         
        """
        pass
    @property
    def ParticipatingDatumColor(self) -> int:
        """
        Getter for property: (int) ParticipatingDatumColor
         Returns the sketch participating datum curve color   
            
         
        """
        pass
    @ParticipatingDatumColor.setter
    def ParticipatingDatumColor(self, sketch_participating_datum_color: int):
        """
        Setter for property: (int) ParticipatingDatumColor
         Returns the sketch participating datum curve color   
            
         
        """
        pass
    @property
    def PersistentRelationColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) PersistentRelationColor
         Returns the sketch persistent relation color   
            
         
        """
        pass
    @PersistentRelationColor.setter
    def PersistentRelationColor(self, sketchPersistentRelationColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) PersistentRelationColor
         Returns the sketch persistent relation color   
            
         
        """
        pass
    @property
    def PreviewDimensionColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) PreviewDimensionColor
         Returns the sketch preview dimension color   
            
         
        """
        pass
    @PreviewDimensionColor.setter
    def PreviewDimensionColor(self, sketchPreviewDimensionColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) PreviewDimensionColor
         Returns the sketch preview dimension color   
            
         
        """
        pass
    @property
    def ReferenceCurveColor(self) -> int:
        """
        Getter for property: (int) ReferenceCurveColor
         Returns the sketch reference curve color   
            
         
        """
        pass
    @ReferenceCurveColor.setter
    def ReferenceCurveColor(self, sketch_reference_curve_color: int):
        """
        Setter for property: (int) ReferenceCurveColor
         Returns the sketch reference curve color   
            
         
        """
        pass
    @property
    def ReferenceDimensionColor(self) -> int:
        """
        Getter for property: (int) ReferenceDimensionColor
         Returns the sketch reference dimension color   
            
         
        """
        pass
    @ReferenceDimensionColor.setter
    def ReferenceDimensionColor(self, sketch_reference_dimension_color: int):
        """
        Setter for property: (int) ReferenceDimensionColor
         Returns the sketch reference dimension color   
            
         
        """
        pass
    @property
    def RelationColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) RelationColor
         Returns the sketch relation color   
            
         
        """
        pass
    @RelationColor.setter
    def RelationColor(self, sketchRelationColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) RelationColor
         Returns the sketch relation color   
            
         
        """
        pass
    @property
    def ShadedRegionColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) ShadedRegionColor
         Returns the sketch shaded region color   
            
         
        """
        pass
    @ShadedRegionColor.setter
    def ShadedRegionColor(self, sketchShadedRegionColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) ShadedRegionColor
         Returns the sketch shaded region color   
            
         
        """
        pass
    @property
    def UnsolvedCurvesColor(self) -> int:
        """
        Getter for property: (int) UnsolvedCurvesColor
         Returns the sketch unsolved curves color   
            
         
        """
        pass
    @UnsolvedCurvesColor.setter
    def UnsolvedCurvesColor(self, sketch_unsolved_curves_color: int):
        """
        Setter for property: (int) UnsolvedCurvesColor
         Returns the sketch unsolved curves color   
            
         
        """
        pass
    @property
    def WorkRegionBoundaryColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) WorkRegionBoundaryColor
         Returns the sketch work region boundary color   
            
         
        """
        pass
    @WorkRegionBoundaryColor.setter
    def WorkRegionBoundaryColor(self, sketchWorkRegionBoundaryColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) WorkRegionBoundaryColor
         Returns the sketch work region boundary color   
            
         
        """
        pass
import NXOpen
class PartUserInterface(NXOpen.Object): 
    """ Represents the set of User Interface preferences applicable to entire part. Other User Interface 
settings are available with NXOpen.Preferences.SessionUserInterface for settings applicable to session
and with SessionUserInterfaceUI class for UI based User Interface Preferences """
    @property
    def DialogBoxDecimalPlaces(self) -> int:
        """
        Getter for property: (int) DialogBoxDecimalPlaces
         Returns the dialog box decimal places   
            
         
        """
        pass
    @DialogBoxDecimalPlaces.setter
    def DialogBoxDecimalPlaces(self, dialog_box_decimal_places: int):
        """
        Setter for property: (int) DialogBoxDecimalPlaces
         Returns the dialog box decimal places   
            
         
        """
        pass
import NXOpen
class PartVisualizationColorSetting(NXOpen.Object): 
    """ Represents the set of visualization preferences under color setting tab applicable to part """
    class RandomColorDisplayFor(Enum):
        """
        Members Include: 
         |Faces|  For Faces 
         |Bodies|  For Bodies 

        """
        Faces: int
        Bodies: int
        @staticmethod
        def ValueOf(value: int) -> PartVisualizationColorSetting.RandomColorDisplayFor:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AttentionColor(self) -> int:
        """
        Getter for property: (int) AttentionColor
         Returns the color that an HD3D objects associated objects are highlighted with when the HD3D object is selected.  
          
            The color must be in the range of 1 to 216 inclusive.   
         
        """
        pass
    @AttentionColor.setter
    def AttentionColor(self, attention_color: int):
        """
        Setter for property: (int) AttentionColor
         Returns the color that an HD3D objects associated objects are highlighted with when the HD3D object is selected.  
          
            The color must be in the range of 1 to 216 inclusive.   
         
        """
        pass
    @property
    def HandleActiveColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) HandleActiveColor
         Returns the color of active handles.  
             
         
        """
        pass
    @HandleActiveColor.setter
    def HandleActiveColor(self, handle_active_color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) HandleActiveColor
         Returns the color of active handles.  
             
         
        """
        pass
    @property
    def HandleColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) HandleColor
         Returns the color of handles.  
             
         
        """
        pass
    @HandleColor.setter
    def HandleColor(self, handle_color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) HandleColor
         Returns the color of handles.  
             
         
        """
        pass
    @property
    def HandleOrientxpressColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) HandleOrientxpressColor
         Returns the color of the OrientXpress handle.  
             
         
        """
        pass
    @HandleOrientxpressColor.setter
    def HandleOrientxpressColor(self, handle_orientxpress_color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) HandleOrientxpressColor
         Returns the color of the OrientXpress handle.  
             
         
        """
        pass
    @property
    def HandlePreselectionColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) HandlePreselectionColor
         Returns the preselection color of handles.  
             
         
        """
        pass
    @HandlePreselectionColor.setter
    def HandlePreselectionColor(self, handle_preselection_color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) HandlePreselectionColor
         Returns the preselection color of handles.  
             
         
        """
        pass
    @property
    def HandleSelectionColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) HandleSelectionColor
         Returns the selection color of handles.  
             
         
        """
        pass
    @HandleSelectionColor.setter
    def HandleSelectionColor(self, handle_selection_color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) HandleSelectionColor
         Returns the selection color of handles.  
             
         
        """
        pass
    @property
    def HiddenGeometryColor(self) -> int:
        """
        Getter for property: (int) HiddenGeometryColor
         Returns the color of hidden geometry.  
             
         
        """
        pass
    @HiddenGeometryColor.setter
    def HiddenGeometryColor(self, hidden_geometry_color: int):
        """
        Setter for property: (int) HiddenGeometryColor
         Returns the color of hidden geometry.  
             
         
        """
        pass
    @property
    def MonochromeBackgroundColor(self) -> int:
        """
        Getter for property: (int) MonochromeBackgroundColor
         Returns the monochrome background color   
            
         
        """
        pass
    @MonochromeBackgroundColor.setter
    def MonochromeBackgroundColor(self, monochrome_background_color: int):
        """
        Setter for property: (int) MonochromeBackgroundColor
         Returns the monochrome background color   
            
         
        """
        pass
    @property
    def MonochromeDisplay(self) -> bool:
        """
        Getter for property: (bool) MonochromeDisplay
         Returns the monochrome display flag.  
           If true it turns on the monochrome display options. 
        Monochrome display also applies to Expanded drawing views.   
         
        """
        pass
    @MonochromeDisplay.setter
    def MonochromeDisplay(self, monochrome_display: bool):
        """
        Setter for property: (bool) MonochromeDisplay
         Returns the monochrome display flag.  
           If true it turns on the monochrome display options. 
        Monochrome display also applies to Expanded drawing views.   
         
        """
        pass
    @property
    def MonochromeForegroundColor(self) -> int:
        """
        Getter for property: (int) MonochromeForegroundColor
         Returns the monochrome foreground color.  
           Monochrome color for all displayable 
        objects, view borders, and view names.   
         
        """
        pass
    @MonochromeForegroundColor.setter
    def MonochromeForegroundColor(self, monochrome_foreground_color: int):
        """
        Setter for property: (int) MonochromeForegroundColor
         Returns the monochrome foreground color.  
           Monochrome color for all displayable 
        objects, view borders, and view names.   
         
        """
        pass
    @property
    def MonochromePreselectionColor(self) -> int:
        """
        Getter for property: (int) MonochromePreselectionColor
         Returns the monochrome color for preselected objects    
            
         
        """
        pass
    @MonochromePreselectionColor.setter
    def MonochromePreselectionColor(self, monochrome_preselection_color: int):
        """
        Setter for property: (int) MonochromePreselectionColor
         Returns the monochrome color for preselected objects    
            
         
        """
        pass
    @property
    def MonochromeSelectionColor(self) -> int:
        """
        Getter for property: (int) MonochromeSelectionColor
         Returns the monochrome selection_color.  
           Displays all selectedhighlighted objects, 
        temporary display objects (such as coneheads, temporary text), and drawing borders 
        in this color.   
         
        """
        pass
    @MonochromeSelectionColor.setter
    def MonochromeSelectionColor(self, monochrome_selection_color: int):
        """
        Setter for property: (int) MonochromeSelectionColor
         Returns the monochrome selection_color.  
           Displays all selectedhighlighted objects, 
        temporary display objects (such as coneheads, temporary text), and drawing borders 
        in this color.   
         
        """
        pass
    @property
    def PreselectionColor(self) -> int:
        """
        Getter for property: (int) PreselectionColor
         Returns the preselection color.  
           Represents color of selectable objects for the current operation.   
         
        """
        pass
    @PreselectionColor.setter
    def PreselectionColor(self, preselection_color: int):
        """
        Setter for property: (int) PreselectionColor
         Returns the preselection color.  
           Represents color of selectable objects for the current operation.   
         
        """
        pass
    @property
    def RandomColorDisplay(self) -> PartVisualizationColorSetting.RandomColorDisplayFor:
        """
        Getter for property: ( PartVisualizationColorSetting.RandomColorDisplayFor NXOpen.P) RandomColorDisplay
         Returns the random color display selection.  
            
         
        """
        pass
    @RandomColorDisplay.setter
    def RandomColorDisplay(self, random_color_display: PartVisualizationColorSetting.RandomColorDisplayFor):
        """
        Setter for property: ( PartVisualizationColorSetting.RandomColorDisplayFor NXOpen.P) RandomColorDisplay
         Returns the random color display selection.  
            
         
        """
        pass
    @property
    def RandomColorDisplayOption(self) -> bool:
        """
        Getter for property: (bool) RandomColorDisplayOption
         Returns the random color display flag.  
           If true it provides a temporary display of unique colors 
        per solid object.   
         
        """
        pass
    @RandomColorDisplayOption.setter
    def RandomColorDisplayOption(self, random_color_display_option: bool):
        """
        Setter for property: (bool) RandomColorDisplayOption
         Returns the random color display flag.  
           If true it provides a temporary display of unique colors 
        per solid object.   
         
        """
        pass
    @property
    def SelectionColor(self) -> int:
        """
        Getter for property: (int) SelectionColor
         Returns the selection color.  
           Represents color of selected objects, the grid, view names and borders, 
        and temporary points and conehead vectors.   
         
        """
        pass
    @SelectionColor.setter
    def SelectionColor(self, selection_color: int):
        """
        Setter for property: (int) SelectionColor
         Returns the selection color.  
           Represents color of selected objects, the grid, view names and borders, 
        and temporary points and conehead vectors.   
         
        """
        pass
    @property
    def ShowWidths(self) -> bool:
        """
        Getter for property: (bool) ShowWidths
         Returns the show widths flag.  
           If true, the object width attribute determines the displayed width 
        of lines or curves used to represent an object.   
         
        """
        pass
    @ShowWidths.setter
    def ShowWidths(self, show_widths: bool):
        """
        Setter for property: (bool) ShowWidths
         Returns the show widths flag.  
           If true, the object width attribute determines the displayed width 
        of lines or curves used to represent an object.   
         
        """
        pass
    def ShuffleRandomColor(self) -> None:
        """
         Allows user to shuffle the Random color 
        """
        pass
import NXOpen
class PartVisualizationEmphasis(NXOpen.Object): 
    """ Represents visualization preferences for emphasis that are applicable
        to the entire part. """
    class EdgesType(Enum):
        """
        Members Include: 
         |Off| 
                        Displays no edges for de-emphasized shaded geometry. 
         |Normal| 
                        Displays edges for de-emphasized shaded geometry if 
                        edges are normally displayed for shaded geometry. 

        """
        Off: int
        Normal: int
        @staticmethod
        def ValueOf(value: int) -> PartVisualizationEmphasis.EdgesType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SeeThruStyleType(Enum):
        """
        Members Include: 
         |Shell| 
                        Displays de-emphasized shaded geometry as a translucent
                        shell with a single color. 
         |OriginalColorShell| 
                        Displays de-emphasized shaded geometry as a translucent
                        shell, preserving original colors. 
         |Layers| 
                        Displays de-emphasized shaded geometry as translucent
                        layers with a single color. 

        """
        Shell: int
        OriginalColorShell: int
        Layers: int
        @staticmethod
        def ValueOf(value: int) -> PartVisualizationEmphasis.SeeThruStyleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LayersOptions:
        """
         Specifies options that control the appearance of de-emphasized
                    shaded geometry when the See-Thru style is set to Layers. 
         PartVisualizationEmphasisLayersOptions_Struct NXOpen.P is an alias for  PartVisualizationEmphasis.LayersOptions NXOpen.P.
        """
        @property
        def Rgb(self) -> NXOpen.NXColor.Rgb:
            """
            Getter for property Rgb
            the color of de-emphasized shaded geometry when the                See-Thru style is set to Layers.

            """
            pass
        @Rgb.setter
        def Rgb(self, value: NXOpen.NXColor.Rgb):
            """
            Getter for property Rgb
            the color of de-emphasized shaded geometry when the                See-Thru style is set to Layers.
            Setter for property Rgb
            the color of de-emphasized shaded geometry when the                See-Thru style is set to Layers.

            """
            pass
        @property
        def Edges(self) -> PartVisualizationEmphasis.EdgesType:
            """
            Getter for property Edges
            whether or not edges are displayed for de-emphasized                shaded geometry when the See-Thru style is set to Layers.

            """
            pass
        @Edges.setter
        def Edges(self, value: PartVisualizationEmphasis.EdgesType):
            """
            Getter for property Edges
            whether or not edges are displayed for de-emphasized                shaded geometry when the See-Thru style is set to Layers.
            Setter for property Edges
            whether or not edges are displayed for de-emphasized                shaded geometry when the See-Thru style is set to Layers.

            """
            pass
        @property
        def EdgesRgb(self) -> NXOpen.NXColor.Rgb:
            """
            Getter for property EdgesRgb
            the color of edges displayed for de-emphasized shaded                geometry when the See-Thru style is set to Layers.

            """
            pass
        @EdgesRgb.setter
        def EdgesRgb(self, value: NXOpen.NXColor.Rgb):
            """
            Getter for property EdgesRgb
            the color of edges displayed for de-emphasized shaded                geometry when the See-Thru style is set to Layers.
            Setter for property EdgesRgb
            the color of edges displayed for de-emphasized shaded                geometry when the See-Thru style is set to Layers.

            """
            pass
        @property
        def Translucency(self) -> int:
            """
            Getter for property Translucency
            the translucency of de-emphasized shaded geometry when                the See-Thru style is set to Layers.

            """
            pass
        @Translucency.setter
        def Translucency(self, value: int):
            """
            Getter for property Translucency
            the translucency of de-emphasized shaded geometry when                the See-Thru style is set to Layers.
            Setter for property Translucency
            the translucency of de-emphasized shaded geometry when                the See-Thru style is set to Layers.

            """
            pass
    class OriginalColorShellOptions:
        """
         Specifies options that control the appearance of de-emphasized
                    shaded geometry when the See-Thru style is set to Original Color
                    Shell. 
         PartVisualizationEmphasisOriginalColorShellOptions_Struct NXOpen.P is an alias for  PartVisualizationEmphasis.OriginalColorShellOptions NXOpen.P.
        """
        @property
        def Edges(self) -> PartVisualizationEmphasis.EdgesType:
            """
            Getter for property Edges
            whether or not edges are displayed for de-emphasized shaded                geometry when the See-Thru style is set to Original Color                Shell.

            """
            pass
        @Edges.setter
        def Edges(self, value: PartVisualizationEmphasis.EdgesType):
            """
            Getter for property Edges
            whether or not edges are displayed for de-emphasized shaded                geometry when the See-Thru style is set to Original Color                Shell.
            Setter for property Edges
            whether or not edges are displayed for de-emphasized shaded                geometry when the See-Thru style is set to Original Color                Shell.

            """
            pass
        @property
        def EdgesRgb(self) -> NXOpen.NXColor.Rgb:
            """
            Getter for property EdgesRgb
            the color of edges displayed for de-emphasized shaded                geometry when the See-Thru style is set to Original Color                Shell.

            """
            pass
        @EdgesRgb.setter
        def EdgesRgb(self, value: NXOpen.NXColor.Rgb):
            """
            Getter for property EdgesRgb
            the color of edges displayed for de-emphasized shaded                geometry when the See-Thru style is set to Original Color                Shell.
            Setter for property EdgesRgb
            the color of edges displayed for de-emphasized shaded                geometry when the See-Thru style is set to Original Color                Shell.

            """
            pass
        @property
        def Translucency(self) -> int:
            """
            Getter for property Translucency
            the translucency of de-emphasized shaded geometry when                the See-Thru style is set to Original Color Shell.

            """
            pass
        @Translucency.setter
        def Translucency(self, value: int):
            """
            Getter for property Translucency
            the translucency of de-emphasized shaded geometry when                the See-Thru style is set to Original Color Shell.
            Setter for property Translucency
            the translucency of de-emphasized shaded geometry when                the See-Thru style is set to Original Color Shell.

            """
            pass
    class ShellOptions:
        """
         Specifies options that control the appearance of de-emphasized
                    shaded geometry when the See-Thru style is set to Shell. 
         PartVisualizationEmphasisShellOptions_Struct NXOpen.P is an alias for  PartVisualizationEmphasis.ShellOptions NXOpen.P.
        """
        @property
        def Rgb(self) -> NXOpen.NXColor.Rgb:
            """
            Getter for property Rgb
            the color of de-emphasized shaded geometry when the                See-Thru style is set to Shell.

            """
            pass
        @Rgb.setter
        def Rgb(self, value: NXOpen.NXColor.Rgb):
            """
            Getter for property Rgb
            the color of de-emphasized shaded geometry when the                See-Thru style is set to Shell.
            Setter for property Rgb
            the color of de-emphasized shaded geometry when the                See-Thru style is set to Shell.

            """
            pass
        @property
        def Edges(self) -> PartVisualizationEmphasis.EdgesType:
            """
            Getter for property Edges
            whether or not edges are displayed for de-emphasized                shaded geometry when the See-Thru style is set to Shell.

            """
            pass
        @Edges.setter
        def Edges(self, value: PartVisualizationEmphasis.EdgesType):
            """
            Getter for property Edges
            whether or not edges are displayed for de-emphasized                shaded geometry when the See-Thru style is set to Shell.
            Setter for property Edges
            whether or not edges are displayed for de-emphasized                shaded geometry when the See-Thru style is set to Shell.

            """
            pass
        @property
        def EdgesRgb(self) -> NXOpen.NXColor.Rgb:
            """
            Getter for property EdgesRgb
            the color of edges displayed for de-emphasized shaded                geometry when the See-Thru style is set to Shell.

            """
            pass
        @EdgesRgb.setter
        def EdgesRgb(self, value: NXOpen.NXColor.Rgb):
            """
            Getter for property EdgesRgb
            the color of edges displayed for de-emphasized shaded                geometry when the See-Thru style is set to Shell.
            Setter for property EdgesRgb
            the color of edges displayed for de-emphasized shaded                geometry when the See-Thru style is set to Shell.

            """
            pass
        @property
        def Translucency(self) -> int:
            """
            Getter for property Translucency
            the translucency of de-emphasized shaded geometry when                the See-Thru style is set to Shell.

            """
            pass
        @Translucency.setter
        def Translucency(self, value: int):
            """
            Getter for property Translucency
            the translucency of de-emphasized shaded geometry when                the See-Thru style is set to Shell.
            Setter for property Translucency
            the translucency of de-emphasized shaded geometry when                the See-Thru style is set to Shell.

            """
            pass
    class WireframeBlendOptions:
        """
         Specifies options that control the color-blending effect used to
                    de-emphasize wireframe geometry. 
         PartVisualizationEmphasisWireframeBlendOptions_Struct NXOpen.P is an alias for  PartVisualizationEmphasis.WireframeBlendOptions NXOpen.P.
        """
        @property
        def BlendColor(self) -> int:
            """
            Getter for property BlendColor
            the de-emphasis color that is blended with object colors                to de-emphasize wireframe geometry.

            """
            pass
        @BlendColor.setter
        def BlendColor(self, value: int):
            """
            Getter for property BlendColor
            the de-emphasis color that is blended with object colors                to de-emphasize wireframe geometry.
            Setter for property BlendColor
            the de-emphasis color that is blended with object colors                to de-emphasize wireframe geometry.

            """
            pass
        @property
        def BlendPercentage(self) -> int:
            """
            Getter for property BlendPercentage
            the percentage of the de-emphasis color that is blended                with object colors to de-emphasize wireframe geometry                It is a value between 10 and 100.

            """
            pass
        @BlendPercentage.setter
        def BlendPercentage(self, value: int):
            """
            Getter for property BlendPercentage
            the percentage of the de-emphasis color that is blended                with object colors to de-emphasize wireframe geometry                It is a value between 10 and 100.
            Setter for property BlendPercentage
            the percentage of the de-emphasis color that is blended                with object colors to de-emphasize wireframe geometry                It is a value between 10 and 100.

            """
            pass
    @property
    def SeeThruStyle(self) -> PartVisualizationEmphasis.SeeThruStyleType:
        """
        Getter for property: ( PartVisualizationEmphasis.SeeThruStyleType NXOpen.P) SeeThruStyle
         Returns the See-Thru style that determines how translucency and color
                    are used to de-emphasize shaded geometry.  
             
         
        """
        pass
    @SeeThruStyle.setter
    def SeeThruStyle(self, seeThruStyle: PartVisualizationEmphasis.SeeThruStyleType):
        """
        Setter for property: ( PartVisualizationEmphasis.SeeThruStyleType NXOpen.P) SeeThruStyle
         Returns the See-Thru style that determines how translucency and color
                    are used to de-emphasize shaded geometry.  
             
         
        """
        pass
    def GetLayersOptions(self) -> PartVisualizationEmphasis.LayersOptions:
        """
         Returns options that control the appearance of de-emphasized
                    shaded geometry when the See-Thru style is set to Layers. 
         Returns layersOptions ( PartVisualizationEmphasis.LayersOptions NXOpen.P): 
                        options that control the appearance of de-emphasized
                        shaded geometry when the See-Thru style is set to Layers. .
        """
        pass
    def GetOriginalColorShellOptions(self) -> PartVisualizationEmphasis.OriginalColorShellOptions:
        """
         Returns options that control the appearance of de-emphasized
                    shaded geometry when the See-Thru style is set to Original Color
                    Shell. 
         Returns originalColorShellOptions ( PartVisualizationEmphasis.OriginalColorShellOptions NXOpen.P): 
                        options that control the appearance of de-emphasized
                        shaded geometry when the See-Thru style is set to
                        Original Color Shell. .
        """
        pass
    def GetShellOptions(self) -> PartVisualizationEmphasis.ShellOptions:
        """
         Returns options that control the appearance of de-emphasized
                    shaded geometry when the See-Thru style is set to Shell. 
         Returns shellOptions ( PartVisualizationEmphasis.ShellOptions NXOpen.P): 
                        options that control the appearance of de-emphasized
                        shaded geometry when the See-Thru style is set to Shell. .
        """
        pass
    def GetWireframeBlendOptions(self) -> PartVisualizationEmphasis.WireframeBlendOptions:
        """
         Returns options that control the color-blending effect used to
                    de-emphasize wireframe geometry. 
         Returns wireframeBlendOptions ( PartVisualizationEmphasis.WireframeBlendOptions NXOpen.P): 
                        options that control the color-blending effect used to
                        de-emphasize wireframe geometry. .
        """
        pass
    def SetLayersOptions(self, layersOptions: PartVisualizationEmphasis.LayersOptions) -> None:
        """
         Modifies options that control the appearance of de-emphasized
                    shaded geometry when the See-Thru style is set to Layers. 
        """
        pass
    def SetOriginalColorShellOptions(self, originalColorShellOptions: PartVisualizationEmphasis.OriginalColorShellOptions) -> None:
        """
         Modifies options that control the appearance of de-emphasized
                    shaded geometry when the See-Thru style is set to Original Color
                    Shell. 
        """
        pass
    def SetShellOptions(self, shellOptions: PartVisualizationEmphasis.ShellOptions) -> None:
        """
         Modifies options that control the appearance of de-emphasized
                    shaded geometry when the See-Thru style is set to Shell. 
        """
        pass
    def SetWireframeBlendOptions(self, wireframeBlendOptions: PartVisualizationEmphasis.WireframeBlendOptions) -> None:
        """
         Modifies options that control the color-blending effect used to
                    de-emphasize wireframe geometry. 
        """
        pass
import NXOpen
class PartVisualizationLine(NXOpen.Object): 
    """ Represents the set of visualization preferences under Line tab applicable to part """
    class LineFontDisplayType(Enum):
        """
        Members Include: 
         |Software|   
         |Hardware|   

        """
        Software: int
        Hardware: int
        @staticmethod
        def ValueOf(value: int) -> PartVisualizationLine.LineFontDisplayType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CurveTolerance(self) -> float:
        """
        Getter for property: (float) CurveTolerance
         Returns the curve tolerance.  
           Specifies the level of detail for the current Display Mode.   
         
        """
        pass
    @CurveTolerance.setter
    def CurveTolerance(self, line_curve_tolerance: float):
        """
        Setter for property: (float) CurveTolerance
         Returns the curve tolerance.  
           Specifies the level of detail for the current Display Mode.   
         
        """
        pass
    @property
    def DashSize(self) -> float:
        """
        Getter for property: (float) DashSize
         Returns the dash size.  
           Sets the length of a segment of a dashed curve.   
         
        """
        pass
    @DashSize.setter
    def DashSize(self, line_dash_size: float):
        """
        Setter for property: (float) DashSize
         Returns the dash size.  
           Sets the length of a segment of a dashed curve.   
         
        """
        pass
    @property
    def LineFontDisplay(self) -> PartVisualizationLine.LineFontDisplayType:
        """
        Getter for property: ( PartVisualizationLine.LineFontDisplayType NXOpen.P) LineFontDisplay
         Returns the line font display.  
           Controls the line font. The Hardware option uses the system graphics library to generate the 
        seven standard line fonts. Selecting hardware line fonts can improve drawing performance and reduce memory consumption. 
        The Software option generates non-solid curves with the values entered for the Dash, Space, and Symbol size.   
         
        """
        pass
    @LineFontDisplay.setter
    def LineFontDisplay(self, line_font_display: PartVisualizationLine.LineFontDisplayType):
        """
        Setter for property: ( PartVisualizationLine.LineFontDisplayType NXOpen.P) LineFontDisplay
         Returns the line font display.  
           Controls the line font. The Hardware option uses the system graphics library to generate the 
        seven standard line fonts. Selecting hardware line fonts can improve drawing performance and reduce memory consumption. 
        The Software option generates non-solid curves with the values entered for the Dash, Space, and Symbol size.   
         
        """
        pass
    @property
    def ShowWidths(self) -> bool:
        """
        Getter for property: (bool) ShowWidths
         Returns the show widths option.  
           If true, the object width attribute determines the displayed width of lines or curves used 
        to represent an object.If false, all curves are drawn thin, regardless of object width settings.   
         
        """
        pass
    @ShowWidths.setter
    def ShowWidths(self, isShowWidthOn: bool):
        """
        Setter for property: (bool) ShowWidths
         Returns the show widths option.  
           If true, the object width attribute determines the displayed width of lines or curves used 
        to represent an object.If false, all curves are drawn thin, regardless of object width settings.   
         
        """
        pass
    @property
    def SpaceSize(self) -> float:
        """
        Getter for property: (float) SpaceSize
         Returns the space size.  
           Sets the distance between two segments of a dashed curve.   
         
        """
        pass
    @SpaceSize.setter
    def SpaceSize(self, line_space_size: float):
        """
        Setter for property: (float) SpaceSize
         Returns the space size.  
           Sets the distance between two segments of a dashed curve.   
         
        """
        pass
    @property
    def SymbolSize(self) -> float:
        """
        Getter for property: (float) SymbolSize
         Returns the symbol size.  
           Controls the displayed size of symbols used in software line fonts.   
         
        """
        pass
    @SymbolSize.setter
    def SymbolSize(self, line_symbol_size: float):
        """
        Setter for property: (float) SymbolSize
         Returns the symbol size.  
           Controls the displayed size of symbols used in software line fonts.   
         
        """
        pass
    @property
    def WidthScale(self) -> float:
        """
        Getter for property: (float) WidthScale
         Returns the width scale option.  
           Controls scaling of the width of lines and curves displayed in the graphics window. If set to 0.0 (the minimum value), 
            widths range from 1 to 3 pixels. If set to 1.0 (the maximum value), widths range from 1 to the maximum supported pixel width.   
         
        """
        pass
    @WidthScale.setter
    def WidthScale(self, width_scale: float):
        """
        Setter for property: (float) WidthScale
         Returns the width scale option.  
           Controls scaling of the width of lines and curves displayed in the graphics window. If set to 0.0 (the minimum value), 
            widths range from 1 to 3 pixels. If set to 1.0 (the maximum value), widths range from 1 to the maximum supported pixel width.   
         
        """
        pass
    def GetPixelWidthOptions(self) -> Tuple[bool, float, List[int]]:
        """
         Returns pixel widths used in the graphics window. 
         Returns A tuple consisting of (useWidthScale, widthScale, pixelWidths). 
         - useWidthScale is: bool.
                     If true, width appearance in the graphics window is controlled
                     by width scale. If false, width appearance is controlled by
                     pixel widths. .
         - widthScale is: float.
                     the width scale option, which controls scaling of widths in the
                     graphics window when useWidthScale is true. If set to 0.0 (the
                     minimum value), widths range from 1 to 3 pixels. If set to 1.0
                     (the maximum value), widths range from 1 to 9 pixels. .
         - pixelWidths is: List[int].
                     Array of 9 pixel widths, one for each of the 9 width settings,
                     that defines the appearance of widths in the graphics window
                     when useWidthScale is false. Valid pixel widths range from
                     1 to 9. .

        """
        pass
    def GetPixelWidths(self) -> List[int]:
        """
         Returns options that control width appearance in the graphics window. 
         Returns pixelWidths (List[int]): 
                  Array of 9 pixel widths, one for each of the 9 width settings,
                  that defines the appearance of widths in the graphics window.
                  Valid pixel widths range from 1 to 9. .
        """
        pass
    def GetWidthOptions(self) -> Tuple[bool, float]:
        """
         Returns the show widths and width scale options. 
         Returns A tuple consisting of (show_widths, width_scale). 
         - show_widths is: bool. 
                     the show widths option, which controls whether or not the 
                     object width attribute determines the displayed width of 
                     lines and curves. .
         - width_scale is: float.  
                     the width scale option, which controls scaling of the width 
                     of lines and curves displayed in the graphics window.  .

        """
        pass
    def RegenerateFromToleranceChange(self, updateModeChanged: bool, studio: bool) -> None:
        """
         Regenerates after changing tolerance. 
        """
        pass
    def ResetPixelWidthOptions(self) -> None:
        """
         Resets all pixel width options to settings specified by customer
            defaults. 
        """
        pass
    def SetPixelWidthOptions(self, useWidthScale: bool, widthScale: float, pixelWidths: List[int]) -> None:
        """
         Modifies options that control width appearance in the graphics window. 
        """
        pass
    def SetPixelWidths(self, pixelWidths: List[int]) -> None:
        """
         Modifies pixel widths used in the graphics window. 
        """
        pass
    def SetWidthOptions(self, show_widths: bool, width_scale: float) -> None:
        """
         Modifies the show widths and width scale options. 
        """
        pass
    def UpdateLineFontObjects(self, softwareUpdate: bool) -> None:
        """
         Regenerates after changing line-font settings. 
        """
        pass
import NXOpen
class PartVisualizationNamesBorders(NXOpen.Object): 
    """ Represents the set of visualization preferences of entire Working Part coming under Namesborders Tab"""
    class NameDisplay(Enum):
        """
        Members Include: 
         |Off|  Display is Off 
         |ViewOfDefinition|  View of Definition places 
                                                                                          each name in the work view 
                                                                                          current at the time of name 
                                                                                          creation 
         |WorkView|  Work View places all names 
                                                                                          in the current work view, even 
                                                                                          if the existing names had been 
                                                                                          defined in different views 
         |AllViews|  All Views places all names 
                                                                                          in the all views except the 
                                                                                        drawing member views
         |ObjectDisplaySpecific|  Object Display Specific places all names
                                                                                            in all views except drawing member views,
                                                                                            but only for objects which 'Display Object Name'
                                                                                            has been enabled

        """
        Off: int
        ViewOfDefinition: int
        WorkView: int
        AllViews: int
        ObjectDisplaySpecific: int
        @staticmethod
        def ValueOf(value: int) -> PartVisualizationNamesBorders.NameDisplay:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CharacterSize(self) -> float:
        """
        Getter for property: (float) CharacterSize
         Returns the character size.  
           Allows to define the size of the text in the object names   
         
        """
        pass
    @CharacterSize.setter
    def CharacterSize(self, character_size: float):
        """
        Setter for property: (float) CharacterSize
         Returns the character size.  
           Allows to define the size of the text in the object names   
         
        """
        pass
    @property
    def ObjectNameDisplay(self) -> PartVisualizationNamesBorders.NameDisplay:
        """
        Getter for property: ( PartVisualizationNamesBorders.NameDisplay NXOpen.P) ObjectNameDisplay
         Returns the object name display   
            
         
        """
        pass
    @ObjectNameDisplay.setter
    def ObjectNameDisplay(self, object_name_display: PartVisualizationNamesBorders.NameDisplay):
        """
        Setter for property: ( PartVisualizationNamesBorders.NameDisplay NXOpen.P) ObjectNameDisplay
         Returns the object name display   
            
         
        """
        pass
    @property
    def ShowModelViewBorders(self) -> bool:
        """
        Getter for property: (bool) ShowModelViewBorders
         Returns the show model view border flag.  
           allows to turn on and off the display of view borders.   
         
        """
        pass
    @ShowModelViewBorders.setter
    def ShowModelViewBorders(self, show_model_view_borders: bool):
        """
        Setter for property: (bool) ShowModelViewBorders
         Returns the show model view border flag.  
           allows to turn on and off the display of view borders.   
         
        """
        pass
    @property
    def ShowModelViewNames(self) -> bool:
        """
        Getter for property: (bool) ShowModelViewNames
         Returns  the show model view names flag.  
           Allows to turn on and off the display of view names.    
         
        """
        pass
    @ShowModelViewNames.setter
    def ShowModelViewNames(self, show_model_view_names: bool):
        """
        Setter for property: (bool) ShowModelViewNames
         Returns  the show model view names flag.  
           Allows to turn on and off the display of view names.    
         
        """
        pass
import NXOpen
class PartVisualizationPerformance(NXOpen.Object): 
    """ Represents the set of visualization performance preferences 
        applicable to entire part.
    """
    @property
    def SaveAdvancedDisplayFacets(self) -> bool:
        """
        Getter for property: (bool) SaveAdvancedDisplayFacets
         Returns the save advanced facets.  
          
                      
                    Enable saving of advanced display facets in the part file.
                      
                  
         
        """
        pass
    @SaveAdvancedDisplayFacets.setter
    def SaveAdvancedDisplayFacets(self, saveAdvancedDisplayFacets: bool):
        """
        Setter for property: (bool) SaveAdvancedDisplayFacets
         Returns the save advanced facets.  
          
                      
                    Enable saving of advanced display facets in the part file.
                      
                  
         
        """
        pass
import NXOpen
class PartVisualizationScreen(NXOpen.Object): 
    """ Represents the set of visualization preferences under screen tab applicable to part """
    class ViewTriadLocation(Enum):
        """
        Members Include: 
         |BottomLeft|  View triad display on the bottom left of the view 
         |BottomRight|  View triad display on the bottom right of the view 

        """
        BottomLeft: int
        BottomRight: int
        @staticmethod
        def ValueOf(value: int) -> PartVisualizationScreen.ViewTriadLocation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CsysFixedSizeOnScreen(self) -> bool:
        """
        Getter for property: (bool) CsysFixedSizeOnScreen
         Returns  whether the CSYS display in fixed size on screen.  
             
         
        """
        pass
    @CsysFixedSizeOnScreen.setter
    def CsysFixedSizeOnScreen(self, fixedSizeOnScreen: bool):
        """
        Setter for property: (bool) CsysFixedSizeOnScreen
         Returns  whether the CSYS display in fixed size on screen.  
             
         
        """
        pass
    @property
    def CsysShowThrough(self) -> bool:
        """
        Getter for property: (bool) CsysShowThrough
         Returns  whether the CSYS display in show through mode   
            
         
        """
        pass
    @CsysShowThrough.setter
    def CsysShowThrough(self, showThrough: bool):
        """
        Setter for property: (bool) CsysShowThrough
         Returns  whether the CSYS display in show through mode   
            
         
        """
        pass
    @property
    def CurveShowThrough(self) -> bool:
        """
        Getter for property: (bool) CurveShowThrough
         Returns  whether the Curve display in show through mode   
            
         
        """
        pass
    @CurveShowThrough.setter
    def CurveShowThrough(self, showThrough: bool):
        """
        Setter for property: (bool) CurveShowThrough
         Returns  whether the Curve display in show through mode   
            
         
        """
        pass
    @property
    def PointShowThrough(self) -> bool:
        """
        Getter for property: (bool) PointShowThrough
         Returns  whether the Point display in show through mode   
            
         
        """
        pass
    @PointShowThrough.setter
    def PointShowThrough(self, showThrough: bool):
        """
        Setter for property: (bool) PointShowThrough
         Returns  whether the Point display in show through mode   
            
         
        """
        pass
    @property
    def TriadLocation(self) -> PartVisualizationScreen.ViewTriadLocation:
        """
        Getter for property: ( PartVisualizationScreen.ViewTriadLocation NXOpen.P) TriadLocation
         Returns the view triad location   
            
         
        """
        pass
    @TriadLocation.setter
    def TriadLocation(self, triadLocation: PartVisualizationScreen.ViewTriadLocation):
        """
        Setter for property: ( PartVisualizationScreen.ViewTriadLocation NXOpen.P) TriadLocation
         Returns the view triad location   
            
         
        """
        pass
    @property
    def TriadVisibility(self) -> bool:
        """
        Getter for property: (bool) TriadVisibility
         Returns the show view triad flag.  
           Allows to turn on and off the display of view triad.   
         
        """
        pass
    @TriadVisibility.setter
    def TriadVisibility(self, triadVisibility: bool):
        """
        Setter for property: (bool) TriadVisibility
         Returns the show view triad flag.  
           Allows to turn on and off the display of view triad.   
         
        """
        pass
import NXOpen
class PartVisualizationShade(NXOpen.Object): 
    """ Represents the set of shade visualization preferences applicable to entire part"""
    class AdvViewToleranceType(Enum):
        """
        Members Include: 
         |Coarse|  Coarse  
         |Standard|  Standard
         |Fine|  Fine  
         |Extrafine|  Extrafine 
         |Superfine|  Superfine 
         |Ultrafine|  Ultrafine  
         |Customize|  Customize. User can specify the Edge Tolerance,
                                                                                    Face Tolerance and Angle Tolerance, Width Tolerance
                                                                                    specifically.  

        """
        Coarse: int
        Standard: int
        Fine: int
        Extrafine: int
        Superfine: int
        Ultrafine: int
        Customize: int
        @staticmethod
        def ValueOf(value: int) -> PartVisualizationShade.AdvViewToleranceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class HiddenShadedFaceEdges(Enum):
        """
        Members Include: 
         |Invisible|  If selected, shaded face edges that are 
                                                                                   hidden are not displayed  
         |Dashed|  If selected, hidden shaded face edges are 
                                                                                   displayed in the body color with a dashed line 
                                                                                   font. 
         |HiddenColor|  If any color is selected, hidden shaded face 
                                                                                    edges are displayed in that color.

        """
        Invisible: int
        Dashed: int
        HiddenColor: int
        @staticmethod
        def ValueOf(value: int) -> PartVisualizationShade.HiddenShadedFaceEdges:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ShadedFaceEdge(Enum):
        """
        Members Include: 
         |Off|  Option is off 
         |BodyColor|  Body Color  
         |SpecifyColor|  Specified Color 

        """
        Off: int
        BodyColor: int
        SpecifyColor: int
        @staticmethod
        def ValueOf(value: int) -> PartVisualizationShade.ShadedFaceEdge:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ShadedViewToleranceType(Enum):
        """
        Members Include: 
         |Coarse|  For Coarse: Facet Edge Tolerance is 0.01, Facet 
                                                                                    Chord Tolerance is 0.01, and Angular Tolerance is 0.0  
         |Standard|  For Standard: Facet Edge Tolerance is 0.005, Facet 
                                                                                    Chord Tolerance is 0.005 , and Angular Tolerance is 15 
         |Fine|  For Fine: Facet Edge Tolerance is 0.0005, Facet 
                                                                                    Chord Tolerance is 0.0025, and Angular Tolerance is 6 
         |Extrafine|  For Extrafine: Facet Edge Tolerance is 0.005, Facet 
                                                                                    Chord Tolerance is 0.001, and Angular Tolerance is 6 
         |Ultrafine|  For Ultrafine: Facet Edge Tolerance is 0.0005, Facet 
                                                                                    Chord Tolerance is 0.0005, and Angular Tolerance is 3 
         |Customize|  Customize. User can specify the Edge Tolerance,
                                                                                    Face Tolerance and Angle Tolerance specifically. 

        """
        Coarse: int
        Standard: int
        Fine: int
        Extrafine: int
        Ultrafine: int
        Customize: int
        @staticmethod
        def ValueOf(value: int) -> PartVisualizationShade.ShadedViewToleranceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ViewUpdateModeType(Enum):
        """
        Members Include: 
         |VisibleObject|  Applicable only to visible object. 
                                                                                                Changed update mode name from 'Visible Objects' to 'Visible Faces and Curves'.  
         |VisibleFacesAndCurves|  Applicable only to visible faces and curves 
         |AllObject|  Applicable to all object 
         |NotSet|  No object. 
                                                                                                Deprecated in NX1872. 
                                                                                                To get the same effect as 'None' update mode, please set facet scale 
                                                                                                to 'FIXED' via JA_DISPLAY_FACET_SETTINGS_BUILDER_set_ShadedFacetScale. 
         |VisibleBodiesAndCurves|  Applicable only to visible bodies and curves - Default Value

        """
        VisibleObject: int
        VisibleFacesAndCurves: int
        AllObject: int
        NotSet: int
        VisibleBodiesAndCurves: int
        @staticmethod
        def ValueOf(value: int) -> PartVisualizationShade.ViewUpdateModeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AdvancedVisViewTolerance(self) -> PartVisualizationShade.AdvViewToleranceType:
        """
        Getter for property: ( PartVisualizationShade.AdvViewToleranceType NXOpen.P) AdvancedVisViewTolerance
         Returns the tolerance for advanced visualization views.  
             
         
        """
        pass
    @AdvancedVisViewTolerance.setter
    def AdvancedVisViewTolerance(self, advanced_vis_view_tolerance: PartVisualizationShade.AdvViewToleranceType):
        """
        Setter for property: ( PartVisualizationShade.AdvViewToleranceType NXOpen.P) AdvancedVisViewTolerance
         Returns the tolerance for advanced visualization views.  
             
         
        """
        pass
    @property
    def AdvancedVisViewUpdateMode(self) -> PartVisualizationShade.ViewUpdateModeType:
        """
        Getter for property: ( PartVisualizationShade.ViewUpdateModeType NXOpen.P) AdvancedVisViewUpdateMode
         Returns the update mode for advanced visualization views.  
             
         
        """
        pass
    @AdvancedVisViewUpdateMode.setter
    def AdvancedVisViewUpdateMode(self, advanced_vis_view_update_mode: PartVisualizationShade.ViewUpdateModeType):
        """
        Setter for property: ( PartVisualizationShade.ViewUpdateModeType NXOpen.P) AdvancedVisViewUpdateMode
         Returns the update mode for advanced visualization views.  
             
         
        """
        pass
    @property
    def AlignAdvVisViewFacetsAlongEdges(self) -> bool:
        """
        Getter for property: (bool) AlignAdvVisViewFacetsAlongEdges
         Returns the state of whether facets should be aligned along common edges for Advanced Visualization Views   
            
         
        """
        pass
    @AlignAdvVisViewFacetsAlongEdges.setter
    def AlignAdvVisViewFacetsAlongEdges(self, align_adv_vis_view_facets_along_edges: bool):
        """
        Setter for property: (bool) AlignAdvVisViewFacetsAlongEdges
         Returns the state of whether facets should be aligned along common edges for Advanced Visualization Views   
            
         
        """
        pass
    @property
    def AlignShadedViewFacetsAlongEdges(self) -> bool:
        """
        Getter for property: (bool) AlignShadedViewFacetsAlongEdges
         Returns the state of whether facets should be aligned along common edges for Shaded Views   
            
         
        """
        pass
    @AlignShadedViewFacetsAlongEdges.setter
    def AlignShadedViewFacetsAlongEdges(self, align_shaded_view_facets_along_edges: bool):
        """
        Setter for property: (bool) AlignShadedViewFacetsAlongEdges
         Returns the state of whether facets should be aligned along common edges for Shaded Views   
            
         
        """
        pass
    @property
    def HiddenGeometryColor(self) -> int:
        """
        Getter for property: (int) HiddenGeometryColor
         Returns the shade hidden geometry color.  
              
         
        """
        pass
    @HiddenGeometryColor.setter
    def HiddenGeometryColor(self, hidden_geom_color: int):
        """
        Setter for property: (int) HiddenGeometryColor
         Returns the shade hidden geometry color.  
              
         
        """
        pass
    @property
    def ShadedViewTolerance(self) -> PartVisualizationShade.ShadedViewToleranceType:
        """
        Getter for property: ( PartVisualizationShade.ShadedViewToleranceType NXOpen.P) ShadedViewTolerance
         Returns the tolerance for shaded views.  
             
         
        """
        pass
    @ShadedViewTolerance.setter
    def ShadedViewTolerance(self, shaded_view_tolerance: PartVisualizationShade.ShadedViewToleranceType):
        """
        Setter for property: ( PartVisualizationShade.ShadedViewToleranceType NXOpen.P) ShadedViewTolerance
         Returns the tolerance for shaded views.  
             
         
        """
        pass
    @property
    def ShadedViewUpdateMode(self) -> PartVisualizationShade.ViewUpdateModeType:
        """
        Getter for property: ( PartVisualizationShade.ViewUpdateModeType NXOpen.P) ShadedViewUpdateMode
         Returns the update mode for shaded views.  
             
         
        """
        pass
    @ShadedViewUpdateMode.setter
    def ShadedViewUpdateMode(self, shaded_view_update_mode: PartVisualizationShade.ViewUpdateModeType):
        """
        Setter for property: ( PartVisualizationShade.ViewUpdateModeType NXOpen.P) ShadedViewUpdateMode
         Returns the update mode for shaded views.  
             
         
        """
        pass
    def GetAdvVisViewFacetTolerances(self, adv_vis_view_tolerance_set: PartVisualizationShade.AdvViewToleranceType) -> Tuple[float, float, float, float]:
        """
         Returns the edge, face, angle and width tolerances to be used with the specified
            tolerance set for Advanced Visualization views. 
         Returns A tuple consisting of (edge_tolerance, face_tolerance, angle_tolerance, width_tolerance). 
         - edge_tolerance is: float.  .
         - face_tolerance is: float.  .
         - angle_tolerance is: float.  .
         - width_tolerance is: float.  .

        """
        pass
    def GetShadedViewFacetTolerances(self, shaded_view_tolerance_set: PartVisualizationShade.ShadedViewToleranceType) -> Tuple[float, float, float]:
        """
         Returns the edge, face and angle tolerances to be used with the specified
            tolerance set for shaded views. 
         Returns A tuple consisting of (edge_tolerance, face_tolerance, angle_tolerance). 
         - edge_tolerance is: float.  .
         - face_tolerance is: float.  .
         - angle_tolerance is: float.  .

        """
        pass
    def RegenerateShadedViewsFromToleranceChange(self) -> None:
        """
         Regenerates Shaded Views. Updates all objects based on their surfacing tolerance. 
        """
        pass
    def RegenerateStudioAnalysisViewsFromToleranceChange(self, updateEnvCube: bool) -> None:
        """
         Regenerates Studio Analysis Views. Updates all objects based on their surfacing tolerance. 
        """
        pass
    def SetAdvVisViewFacetTolerances(self, adv_vis_view_tolerance_set: PartVisualizationShade.AdvViewToleranceType, edge_tolerance: float, face_tolerance: float, angle_tolerance: float, width_tolerance: float) -> None:
        """
         Sets the edge, face, angle and width tolerances to be used with the specified
            tolerance set for Advanced Visualization views. 
        """
        pass
    def SetShadedViewFacetTolerances(self, shaded_view_tolerance_set: PartVisualizationShade.ShadedViewToleranceType, edge_tolerance: float, face_tolerance: float, angle_tolerance: float) -> None:
        """
         Sets the edge, face and angle tolerances to be used with the specified
            tolerance set for shaded views. 
        """
        pass
import NXOpen
class PartVisualizationVisual(NXOpen.Object): 
    """ Represents the set of visualization preferences applicable to entire session"""
    @property
    def UpdateHiddenEdge(self) -> bool:
        """
        Getter for property: (bool) UpdateHiddenEdge
         Returns the update hidden edges flag for working part.  
           Controls whether or not hidden edges are updated 
        whenever a solid body is edited.   
         
        """
        pass
    @UpdateHiddenEdge.setter
    def UpdateHiddenEdge(self, update_hidden_edge: bool):
        """
        Setter for property: (bool) UpdateHiddenEdge
         Returns the update hidden edges flag for working part.  
           Controls whether or not hidden edges are updated 
        whenever a solid body is edited.   
         
        """
        pass
class PmiOption(Enum):
    """
    Members Include: 
     |NotSet|  Does not inherit PMI. 
     |FromModelView|  Inherit PMI from the parent model view. 
     |InDrawingPlaneFromView|  Inherit PMI that are parallel to the drawing plane from the model view. 
     |InDrawingPlaneFromPart|  Inherit PMI that are parallel to the drawing plane from the entire part. 

    """
    NotSet: int
    FromModelView: int
    InDrawingPlaneFromView: int
    InDrawingPlaneFromPart: int
    @staticmethod
    def ValueOf(value: int) -> PmiOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class PostProcessing(NXOpen.Object): 
    """ CAE Post Processing preferences  """
    @property
    def NoModelDisplayOnPostviewCreation(self) -> bool:
        """
        Getter for property: (bool) NoModelDisplayOnPostviewCreation
         Returns the flag which indicates that no finite element model data will displayed when postviews are created  
            
         
        """
        pass
    @NoModelDisplayOnPostviewCreation.setter
    def NoModelDisplayOnPostviewCreation(self, emptyview: bool):
        """
        Setter for property: (bool) NoModelDisplayOnPostviewCreation
         Returns the flag which indicates that no finite element model data will displayed when postviews are created  
            
         
        """
        pass
import NXOpen
class ProjectedViewPreferences(NXOpen.Object): 
    """ Represents set of Projected View Preferences applicable to drafting views. 
        It applies to any newly created projected view."""
    pass
class ReferenceSetBehavior(Enum):
    """
    Members Include: 
     |NotSet|  No PMI will be inherited if any of the PMI objects has a reference to an object which is not in the active reference set.  
     |Partial|  Inherit only PMI for which all of the referenced objects are in the active reference set. 
     |All|  Inherit all PMI regardless of whether the referenced objects are in the active reference set. Inherited PMI with references to objects outside of the active reference set will be retained. 

    """
    NotSet: int
    Partial: int
    All: int
    @staticmethod
    def ValueOf(value: int) -> ReferenceSetBehavior:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.Routing
class RoutingApplicationView(NXOpen.Object): 
    """
        The RoutingApplicationView class contains all of the various preferences and options
        available from the Routing Application View file.  In order to call any of the
        methods of this class (or it's contained objects), first call
        Preferences.RoutingApplicationView.LoadAppView to load defaults
        from the application view file.
        """
    class AppType(Enum):
        """
        Members Include: 
         |NotSet|  Not currently in any of the routing applications. 
         |Mechanical|  In routing mechanical application. 
         |Electrical|  In routing electrical application. 
         |Logical|  In routing logical application. 
         |RsdMechanical| In RSD Mechanical  
         |RsdElectrical| In RSd Electrical  

        """
        NotSet: int
        Mechanical: int
        Electrical: int
        Logical: int
        RsdMechanical: int
        RsdElectrical: int
        @staticmethod
        def ValueOf(value: int) -> RoutingApplicationView.AppType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ApplicationType(self) -> RoutingApplicationView.AppType:
        """
        Getter for property: ( RoutingApplicationView.AppType NXOpen.P) ApplicationType
         Returns the given routing application type.  
           This is only used in the context of routing to execute design rules.
                Application type should be set to Preferences::RoutingApplicationView::AppTypeNone 
                before exiting from the routing applications.   
         
        """
        pass
    @ApplicationType.setter
    def ApplicationType(self, app_type: RoutingApplicationView.AppType):
        """
        Setter for property: ( RoutingApplicationView.AppType NXOpen.P) ApplicationType
         Returns the given routing application type.  
           This is only used in the context of routing to execute design rules.
                Application type should be set to Preferences::RoutingApplicationView::AppTypeNone 
                before exiting from the routing applications.   
         
        """
        pass
    @property
    def CurrentDiscipline(self) -> str:
        """
        Getter for property: (str) CurrentDiscipline
         Returns the current discipline.  
           A discipline value of "" (the empty string)
                 indicates no current discipline.    
         
        """
        pass
    @CurrentDiscipline.setter
    def CurrentDiscipline(self, current_discipline: str):
        """
        Setter for property: (str) CurrentDiscipline
         Returns the current discipline.  
           A discipline value of "" (the empty string)
                 indicates no current discipline.    
         
        """
        pass
    @property
    def CurrentSpecification(self) -> str:
        """
        Getter for property: (str) CurrentSpecification
         Returns the current specification for the current discipline.  
           A specification
                 value of "" (the empty string) indicates no current specification.   
         
        """
        pass
    @CurrentSpecification.setter
    def CurrentSpecification(self, current_spec: str):
        """
        Setter for property: (str) CurrentSpecification
         Returns the current specification for the current discipline.  
           A specification
                 value of "" (the empty string) indicates no current specification.   
         
        """
        pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the application view description.  
             
         
        """
        pass
    @property
    def Filename(self) -> str:
        """
        Getter for property: (str) Filename
         Returns the filename of the current application view.  
             
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the application view name.  
             
         
        """
        pass
    @property
    def PartPreferences() -> RoutingPart:
        """
         Routing preferences related to parts. 
        """
        pass
    @property
    def CharacteristicPreferences() -> RoutingCharacteristics:
        """
         Preferences related to optionrequired characteristics. 
        """
        pass
    @property
    def RoutingStock() -> RoutingStock:
        """
         Stock preferences structure 
        """
        pass
    @property
    def RoutingPath() -> RoutingPath:
        """
         Path preferences structure 
        """
        pass
    @property
    def RoutingMechanical() -> RoutingMechanical:
        """
         Routing mechanical preferences 
        """
        pass
    @property
    def RoutingLogical() -> RoutingLogical:
        """
         Routing logical preferences 
        """
        pass
    @property
    def RoutingElectrical() -> RoutingElectrical:
        """
         Routing electrical preferences structure 
        """
        pass
    @property
    def RoutingUserPreferences() -> RoutingUserPreferences:
        """
         Routing user preferences 
        """
        pass
    def GetDisciplines() -> List[str]:
        """
         Returns all of the disciplines available in the current application view. 
         Returns discipline_names (List[str]):  .
        """
        pass
    def GetFabricationCharacteristics() -> List[NXOpen.Routing.CharacteristicList.CharacteristicInformation]:
        """
         Returns fabrication characteristics. These characteristics
                    must be set for any fabrication created out of a Routing assembly. 
         Returns fabricationCharacteristics ( NXOpen.Routing.CharacteristicList.CharacteristicInformation Li):  .
        """
        pass
    def GetOptionalCharacteristics() -> List[NXOpen.Routing.CharacteristicList.CharacteristicInformation]:
        """
         Returns the intersection of the optional stock characteristics and optional
                    part characteristics for the current discipline of the application view. 
         Returns optionalCharacteristics ( NXOpen.Routing.CharacteristicList.CharacteristicInformation Li):  .
        """
        pass
    def GetRequiredCharacteristics() -> List[NXOpen.Routing.CharacteristicList.CharacteristicInformation]:
        """
         Returns the intersection of the required stock characteristics and required
                    part characteristics for the current discipline of the application view. 
         Returns requiredCharacteristics ( NXOpen.Routing.CharacteristicList.CharacteristicInformation Li):  .
        """
        pass
    def GetSpecifications() -> List[str]:
        """
         Returns the specifications available in the current discipline. 
         Returns spec_names (List[str]):  .
        """
        pass
    def LoadAppView(file_name: str) -> None:
        """
          Loads the preferences from an application view file.  This file may be either
                 a legacy application view file (with a .apv extension) or a new XML style application
                 view file (with a .xml extension).  See the Routing Administrator documentation for the
                 format of these files.  Once an application view file is loaded, it cannot be
                 unloaded.  After loading the file the first time in a session, subsequent loads do not pick
                 up changes made to the application view file, but it does set the preferences to
                 the cached values loaded from that file.
                 Here is some example code, after the second call to
                 Preferences.RoutingApplicationView.LoadAppView the current defaults
                 are defaults initially read from the mechanical application view.
                 
                    Session.GetSession().Preferences.RoutingApplicationView.LoadAppView ( "ugroute_mech_in.xml" );
                    
                    Session.GetSession().Preferences.RoutingApplicationView.LoadAppView ( "ugroute_elec_in.xml" );
                    
                    Session.GetSession().Preferences.RoutingApplicationView.LoadAppView ( "ugroute_mech_in.xml" );
                    
                 
                 
        """
        pass
import NXOpen
import NXOpen.Routing
class RoutingCharacteristics(NXOpen.Object): 
    """ Contains all of the various preferences for option and required characteristics. Optional and
       Required characteristics are specified in the Discipline section of the application view file.
       Changing the current discipline modifies the set of optional and required characteristics.
       """
    def GetComponentCharacteristicValues() -> NXOpen.Routing.CharacteristicList:
        """
         Get the latest stored component characterstics values specified in the Specify Item dialog or
                  in Edit Characteristics.  
         Returns values ( NXOpen.Routing.CharacteristicList):  .
        """
        pass
    def GetComponentOptionalCharacteristics() -> List[NXOpen.Routing.CharacteristicList.CharacteristicInformation]:
        """
         Get the set of optional characteristics to apply to NXOpen.Assemblies.Component objects
                   when placing parts.  
         Returns optional ( NXOpen.Routing.CharacteristicList.CharacteristicInformation Li):  .
        """
        pass
    def GetComponentRequiredCharacteristics() -> List[NXOpen.Routing.CharacteristicList.CharacteristicInformation]:
        """
         Get the set of required characteristics to apply to NXOpen.Assemblies.Component objects
                   when placing parts.  
         Returns required ( NXOpen.Routing.CharacteristicList.CharacteristicInformation Li):  .
        """
        pass
    def GetDefaultElbowCharacteristicValues() -> NXOpen.Routing.CharacteristicList:
        """
         Get the latest stored characterstics values specified for default elbows in the 
                 Specify Item dialog.  
         Returns values ( NXOpen.Routing.CharacteristicList):  .
        """
        pass
    def GetDestintationCharacteristics() -> List[NXOpen.Routing.CharacteristicList.CharacteristicInformation]:
        """
         Get the set of characteristics read from objects during placement object selection in the 
                    Specify Item dialog.  Destination characteristics are discipline specific. 
         Returns destination ( NXOpen.Routing.CharacteristicList.CharacteristicInformation Li):  .
        """
        pass
    def GetStockCharacteristicValues() -> NXOpen.Routing.CharacteristicList:
        """
         Get the latest stored stock characterstics values specified in the Specify Item dialog or
                  in Edit Characteristics.  
         Returns values ( NXOpen.Routing.CharacteristicList):  .
        """
        pass
    def GetStockOptionalCharacteristics() -> List[NXOpen.Routing.CharacteristicList.CharacteristicInformation]:
        """
         Get the set of optional characteristics to apply to NXOpen.Routing.Stock objects
                   when assinging stock.  
         Returns optional ( NXOpen.Routing.CharacteristicList.CharacteristicInformation Li):  .
        """
        pass
    def GetStockRequiredCharacteristics() -> List[NXOpen.Routing.CharacteristicList.CharacteristicInformation]:
        """
         Get the set of required characteristics to apply to NXOpen.Routing.Stock objects
                   when assinging stock.  
         Returns required ( NXOpen.Routing.CharacteristicList.CharacteristicInformation Li):  .
        """
        pass
    def UpdateComponentCharacteristicValues(values: NXOpen.Routing.CharacteristicList) -> None:
        """
         Replaces any stored component characteristics with the input values, adds any new
                 values in the input list.  Doesn't delete any stored component characteristics. 
        """
        pass
    def UpdateDefaultElbowCharacteristicValues(values: NXOpen.Routing.CharacteristicList) -> None:
        """
         Replaces any stored default elbow characteristics with the input values, adds any new
                 values in the input list.  Doesn't delete any stored default elbow characteristics. 
        """
        pass
    def UpdateStockCharacteristicValues(values: NXOpen.Routing.CharacteristicList) -> None:
        """
         Replaces any stored stock characteristics with the input values, adds any new
                 values in the input list.  Doesn't delete any stored stock characteristics. 
        """
        pass
import NXOpen
import NXOpen.Routing
class RoutingElectrical(NXOpen.Object): 
    """ The RoutingElectrical object stores a set of route electrical
        preferences.  A valid application view file is necessary to get
        values other than defaults for the electrical preferences. """
    class ComponentMatchType(Enum):
        """
        Members Include: 
         |FileName|  Match file name during component assignment. 
         |ComponentName|  Match component name during component assignment. 
         |AttributeName|  Match attribute name during component assignment. 

        """
        FileName: int
        ComponentName: int
        AttributeName: int
        @staticmethod
        def ValueOf(value: int) -> RoutingElectrical.ComponentMatchType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CreateTerminalsType(Enum):
        """
        Members Include: 
         |All|  Create terminals to all terminals 
         |Listed|  Create terminals to listed terminals 
         |Routed|  Create terminals to routed terminals 

        """
        All: int
        Listed: int
        Routed: int
        @staticmethod
        def ValueOf(value: int) -> RoutingElectrical.CreateTerminalsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AutoRouteStockStyle(self) -> NXOpen.Routing.StockStyle:
        """
        Getter for property: ( NXOpen.Routing.StockStyle) AutoRouteStockStyle
         Returnsthe option to Auto Route using centerline stock style (i.  
          e. none) or simple stock style.  
         
        """
        pass
    @AutoRouteStockStyle.setter
    def AutoRouteStockStyle(self, stock_style: NXOpen.Routing.StockStyle):
        """
        Setter for property: ( NXOpen.Routing.StockStyle) AutoRouteStockStyle
         Returnsthe option to Auto Route using centerline stock style (i.  
          e. none) or simple stock style.  
         
        """
        pass
    @property
    def AutomaticRouteLevel(self) -> bool:
        """
        Getter for property: (bool) AutomaticRouteLevel
         Returns the level at which to automatically route a path.  
             
         
        """
        pass
    @AutomaticRouteLevel.setter
    def AutomaticRouteLevel(self, is_pin_level_route: bool):
        """
        Setter for property: (bool) AutomaticRouteLevel
         Returns the level at which to automatically route a path.  
             
         
        """
        pass
    @property
    def BundleColor(self) -> int:
        """
        Getter for property: (int) BundleColor
         Returns the default bundle color.  
             
         
        """
        pass
    @BundleColor.setter
    def BundleColor(self, bundle_color: int):
        """
        Setter for property: (int) BundleColor
         Returns the default bundle color.  
             
         
        """
        pass
    @property
    def ComponentMatchMethod(self) -> RoutingElectrical.ComponentMatchType:
        """
        Getter for property: ( RoutingElectrical.ComponentMatchType NXOpen.P) ComponentMatchMethod
         Returns the component match option for automaticmanual component assignment.  
             
         
        """
        pass
    @ComponentMatchMethod.setter
    def ComponentMatchMethod(self, component_match_method: RoutingElectrical.ComponentMatchType):
        """
        Setter for property: ( RoutingElectrical.ComponentMatchType NXOpen.P) ComponentMatchMethod
         Returns the component match option for automaticmanual component assignment.  
             
         
        """
        pass
    @property
    def CreateTerminalsOption(self) -> RoutingElectrical.CreateTerminalsType:
        """
        Getter for property: ( RoutingElectrical.CreateTerminalsType NXOpen.P) CreateTerminalsOption
         Returns the create terminals option.  
              
         
        """
        pass
    @CreateTerminalsOption.setter
    def CreateTerminalsOption(self, create_terminals_option: RoutingElectrical.CreateTerminalsType):
        """
        Setter for property: ( RoutingElectrical.CreateTerminalsType NXOpen.P) CreateTerminalsOption
         Returns the create terminals option.  
              
         
        """
        pass
    @property
    def DefaultJumperLength(self) -> str:
        """
        Getter for property: (str) DefaultJumperLength
         Returns the default length of a jumper wire.  
             
         
        """
        pass
    @DefaultJumperLength.setter
    def DefaultJumperLength(self, default_jumper_length: str):
        """
        Setter for property: (str) DefaultJumperLength
         Returns the default length of a jumper wire.  
             
         
        """
        pass
    @property
    def ExportFormatInLegacyFile(self) -> bool:
        """
        Getter for property: (bool) ExportFormatInLegacyFile
         Returns the option to export the format at the top of a legacy routelist file.  
             
         
        """
        pass
    @ExportFormatInLegacyFile.setter
    def ExportFormatInLegacyFile(self, export_format: bool):
        """
        Setter for property: (bool) ExportFormatInLegacyFile
         Returns the option to export the format at the top of a legacy routelist file.  
             
         
        """
        pass
    @property
    def FormboardSynchronizationLengthTolerance(self) -> float:
        """
        Getter for property: (float) FormboardSynchronizationLengthTolerance
         Returns the default segment length tolerance to use for Formboard Synchronization.  
             
         
        """
        pass
    @FormboardSynchronizationLengthTolerance.setter
    def FormboardSynchronizationLengthTolerance(self, segment_length_tolerance: float):
        """
        Setter for property: (float) FormboardSynchronizationLengthTolerance
         Returns the default segment length tolerance to use for Formboard Synchronization.  
             
         
        """
        pass
    @property
    def HighlightWire(self) -> bool:
        """
        Getter for property: (bool) HighlightWire
         Returns the option to highlight a wire in the connection list navigator.  
             
         
        """
        pass
    @HighlightWire.setter
    def HighlightWire(self, highlight_wire: bool):
        """
        Setter for property: (bool) HighlightWire
         Returns the option to highlight a wire in the connection list navigator.  
             
         
        """
        pass
    @property
    def RecordNetlistHistory(self) -> bool:
        """
        Getter for property: (bool) RecordNetlistHistory
         Returnsthe option to record import and export activity in the Connection and Component Lists.  
             
         
        """
        pass
    @RecordNetlistHistory.setter
    def RecordNetlistHistory(self, record_netlist_history: bool):
        """
        Setter for property: (bool) RecordNetlistHistory
         Returnsthe option to record import and export activity in the Connection and Component Lists.  
             
         
        """
        pass
    @property
    def ReportRouteErrors(self) -> bool:
        """
        Getter for property: (bool) ReportRouteErrors
         Returns the option to report automanual route errors to the listing window.  
             
         
        """
        pass
    @ReportRouteErrors.setter
    def ReportRouteErrors(self, report_route_errors: bool):
        """
        Setter for property: (bool) ReportRouteErrors
         Returns the option to report automanual route errors to the listing window.  
             
         
        """
        pass
    @property
    def TerminalSegmentSolidDisplay(self) -> bool:
        """
        Getter for property: (bool) TerminalSegmentSolidDisplay
         Returns the terminal segment solid display option   
            
         
        """
        pass
    @TerminalSegmentSolidDisplay.setter
    def TerminalSegmentSolidDisplay(self, terminal_segment_solid: bool):
        """
        Setter for property: (bool) TerminalSegmentSolidDisplay
         Returns the terminal segment solid display option   
            
         
        """
        pass
    def GetComponentMatchColumnHeading() -> str:
        """
         Gets the column name of the component list used for component matching
                   if the method is attribute matching. 
         Returns column_heading (str):  .
        """
        pass
    def GetComponentMatchComponentAttributeTitle() -> str:
        """
         Gets the component attribute name used for component matching
                   if the method is attribute matching. 
         Returns component_attribute_title (str):  .
        """
        pass
    def GetDefaultHarnessName() -> str:
        """
         Gets the default harness name.  The default harness name replaces
                    the Harness field value of any records in an imported
                    connectioncomponent list that are empty.  A blank string in the
                    Default_Harness_Name element below replaces blank Harness fields
                    with the leaf name of the work part.  
         Returns default_harness_name (str):  .
        """
        pass
    def GetFilterBlankingAttribute() -> str:
        """
         Gets the Rlist_Filter_Blanking_Attribute. 
         Returns attribute_name (str):  .
        """
        pass
    def GetFormboardFrameSizes() -> List[str]:
        """
         Gets the formboard frame sizes currently specified within the
                    Routing Electrical application.  Formboard frame sizes are character
                    strings are of the form Height x Length (units).
                    Units can be "in" or "mm" (case insensitive).
                    The Height, Length and units fields of the string are separated
                    by one of the following separator characters:
                           "x", "X",  any whitespace, ":" (colon), or a "," (comma)
                  
         Returns frames (List[str]):  .
        """
        pass
    def SetComponentMatchColumnHeading(column_heading: str) -> None:
        """
         Sets the column name of the component list used for component matching
                   if the method is attribute matching. 
        """
        pass
    def SetComponentMatchComponentAttributeTitle(component_attribute_title: str) -> None:
        """
         Sets the component attribute name used for component matching
                   if the method is attribute matching. 
        """
        pass
    def SetDefaultHarnessName(default_harness_name: str) -> None:
        """
         Sets the default harness name 
        """
        pass
    def SetFilterBlankingAttribute(attribute_name: str) -> None:
        """
         Sets the Rlist_Filter_Blanking_Attribute. 
        """
        pass
    def SetFormboardFrameSizes(frame_sizes: List[str]) -> None:
        """
         Sets a formboard frame size. 
        """
        pass
import NXOpen
class RoutingLogical(NXOpen.Object): 
    """ The RoutingLogical object stores a set of route logical preferences. """
    class FlowArrowEnumType(Enum):
        """
        Members Include: 
         |Open|  Open arrow head on flow arrow. 
         |Closed|  Closed arrow head on flow arrow. 
         |Filled|  Filled arrow head on flow arrow. 

        """
        Open: int
        Closed: int
        Filled: int
        @staticmethod
        def ValueOf(value: int) -> RoutingLogical.FlowArrowEnumType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FlowArrowParameterA(self) -> float:
        """
        Getter for property: (float) FlowArrowParameterA
         Returns the application view flow arrow parameter A   
            
         
        """
        pass
    @FlowArrowParameterA.setter
    def FlowArrowParameterA(self, flow_arrow_parameter_a: float):
        """
        Setter for property: (float) FlowArrowParameterA
         Returns the application view flow arrow parameter A   
            
         
        """
        pass
    @property
    def FlowArrowParameterB(self) -> float:
        """
        Getter for property: (float) FlowArrowParameterB
         Returns the application view flow arrow parameter B   
            
         
        """
        pass
    @FlowArrowParameterB.setter
    def FlowArrowParameterB(self, flow_arrow_parameter_b: float):
        """
        Setter for property: (float) FlowArrowParameterB
         Returns the application view flow arrow parameter B   
            
         
        """
        pass
    @property
    def FlowArrowType(self) -> RoutingLogical.FlowArrowEnumType:
        """
        Getter for property: ( RoutingLogical.FlowArrowEnumType NXOpen.P) FlowArrowType
         Returns the application view flow arrow type   
            
         
        """
        pass
    @FlowArrowType.setter
    def FlowArrowType(self, flow_arrow_type: RoutingLogical.FlowArrowEnumType):
        """
        Setter for property: ( RoutingLogical.FlowArrowEnumType NXOpen.P) FlowArrowType
         Returns the application view flow arrow type   
            
         
        """
        pass
import NXOpen
class RoutingMechanical(NXOpen.Object): 
    """ The RoutingMechanical object stores a set of route mechanical preferences. """
    class LineColorType(Enum):
        """
        Members Include: 
         |Unknown|  
         |Name|  
         |Index|  
         |Rgb|  
         |Hex|  
         |Max|  

        """
        Unknown: int
        Name: int
        Index: int
        Rgb: int
        Hex: int
        Max: int
        @staticmethod
        def ValueOf(value: int) -> RoutingMechanical.LineColorType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetIsInitialized() -> bool:
        """
         Returns the information of whether the mechanical preferences section
                    exists in the application view file. 
         Returns is_initialized (bool):  .
        """
        pass
    def GetLineColorTypes() -> List[RoutingMechanical.LineColorType]:
        """
         Returns types of string in line_color field.  Valid values are
                    specified by the NXOpen.Preferences.RoutingMechanical.LineColorType . 
         Returns line_color_types ( RoutingMechanical.LineColorType List[NXOpen):  .
        """
        pass
    def GetLineColors() -> List[str]:
        """
         Returns the name, index or rgb strings (hex or , separated) of line color 
         Returns line_colors (List[str]):  .
        """
        pass
    def GetLineFontIndices() -> List[int]:
        """
         Returns the line font indices: line font to apply to segments in the run
                    (currently 1-7 supported), 0 indicates unknown line font 
         Returns line_font_indices (List[int]):  .
        """
        pass
    def GetLineFonts() -> List[str]:
        """
         Returns the names of line font to apply to segments, only used if
                    line_font_index is 0 
         Returns line_fonts (List[str]):  .
        """
        pass
    def GetLineWidths() -> List[int]:
        """
         Returns the thicknesses of segments (currently 0-2 supported) 
         Returns line_widths (List[int]):  .
        """
        pass
    def GetRunTypeNames() -> List[str]:
        """
         Returns the names of run type displays
         Returns run_type_name (List[str]):  .
        """
        pass
import NXOpen
import NXOpen.Routing
class RoutingPartLibrary(NXOpen.Object): 
    """Represents a Routing Part library.  """
    class ColumnStatus(Enum):
        """
        Members Include: 
         |NotHidden|  Column is displayed in Specify Item. 
         |Hidden|  Column is not displayed in Specify Item. 

        """
        NotHidden: int
        Hidden: int
        @staticmethod
        def ValueOf(value: int) -> RoutingPartLibrary.ColumnStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ColumnType(Enum):
        """
        Members Include: 
         |Integer|  Integer values. 
         |Real|  Floating-point values. 
         |String|  String values. 

        """
        Integer: int
        Real: int
        String: int
        @staticmethod
        def ValueOf(value: int) -> RoutingPartLibrary.ColumnType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class NodeType(Enum):
        """
        Members Include: 
         |Normal|  Normal node, may contain part table children.  
                                                        Doesn't have any part table information.  
         |Table|  Part table node.  Contains columnsrows that
                                                        specify parts. 
         |Part|  Part node, contains information necessary
                                                        for loadingusing a routing part. 

        """
        Normal: int
        Table: int
        Part: int
        @staticmethod
        def ValueOf(value: int) -> RoutingPartLibrary.NodeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RootType(Enum):
        """
        Members Include: 
         |Top|  Top of entire part table. 
         |Stock|  Top node for selecting stocks.
         |Wire|  Top node for selecting wires. 
         |Part|  Top node for selecting parts. 

        """
        Top: int
        Stock: int
        Wire: int
        Part: int
        @staticmethod
        def ValueOf(value: int) -> RoutingPartLibrary.RootType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Column:
        """
         Part table column type. 
         RoutingPartLibraryColumn_Struct NXOpen.P is an alias for  RoutingPartLibrary.Column NXOpen.P.
        """
        @property
        def Name(self) -> str:
            """
            Getter for property Name
            Column name.

            """
            pass
        @Name.setter
        def Name(self, value: str):
            """
            Getter for property Name
            Column name.
            Setter for property Name
            Column name.

            """
            pass
        @property
        def Hidden(self) -> RoutingPartLibrary.ColumnStatus:
            """
            Getter for property Hidden
            Whether or not the column is used for selection                                                    in the specify item dialog.

            """
            pass
        @Hidden.setter
        def Hidden(self, value: RoutingPartLibrary.ColumnStatus):
            """
            Getter for property Hidden
            Whether or not the column is used for selection                                                    in the specify item dialog.
            Setter for property Hidden
            Whether or not the column is used for selection                                                    in the specify item dialog.

            """
            pass
        @property
        def Type(self) -> RoutingPartLibrary.ColumnType:
            """
            Getter for property Type
            The value type the column stores.

            """
            pass
        @Type.setter
        def Type(self, value: RoutingPartLibrary.ColumnType):
            """
            Getter for property Type
            The value type the column stores.
            Setter for property Type
            The value type the column stores.

            """
            pass
    def CreateCriteria() -> NXOpen.Routing.CharacteristicList:
        """
         Creates a new empty NXOpen.Routing.CharacteristicList object that can be used
                 as input to Preferences.RoutingPartLibrary.MatchCriteria and
                 Preferences.RoutingPartLibrary.MatchCriteriaWithFilter.  
         Returns criteria ( NXOpen.Routing.CharacteristicList):  .
        """
        pass
    def FilterOnCurrentSpecifications(match: NXOpen.Routing.CharacteristicList, part_classes: List[str]) -> bool:
        """
         Does a characteristic list match the current discipline and specifications? 
         Returns is_valid (bool):  Is the characteristic list valid under the current discipline and specifications? .
        """
        pass
    def GetChildrenNodes(parent: str) -> List[str]:
        """
         Returns the children nodes of the input node. Do not call it on Part type nodes. 
         Returns children (List[str]):  .
        """
        pass
    def GetFilteredRoot(root_type: RoutingPartLibrary.RootType) -> str:
        """
         Returns the root node of the part library using the current active
                   discipline.  Returns  if there is no root node.  
         Returns root (str):  .
        """
        pass
    def GetNodeType(node: str) -> RoutingPartLibrary.NodeType:
        """
         Returns the node type. 
         Returns type ( RoutingPartLibrary.NodeType NXOpen.P):  .
        """
        pass
    def GetPartDefinition(node: str) -> NXOpen.Routing.CharacteristicList:
        """
         Returns the part information for a given 
                    NXOpen.Preferences.RoutingPartLibrary.NodeType.Part node.  
         Returns part_def ( NXOpen.Routing.CharacteristicList):  .
        """
        pass
    def GetRoot() -> str:
        """
         Returns the root node of the part library. Returns  if there
                   is no root node. 
         Returns root (str):  .
        """
        pass
    def GetTableDefinition(node: str) -> List[RoutingPartLibrary.Column]:
        """
         Returns the table information for a given 
                    NXOpen.Preferences.RoutingPartLibrary.NodeType.Table node.  
         Returns columns ( RoutingPartLibrary.Column List[NXOpen):  .
        """
        pass
    def MatchCriteria(start_node: str, criteria: NXOpen.Routing.CharacteristicList) -> List[NXOpen.Routing.CharacteristicList]:
        """
         Search for entries in the part library table nodes that match the given set of 
                  criteria.  Returns an array of NXOpen.Routing.CharacteristicList objects that
                  can be used for assigning stock or placing parts. Searches all nodes at or below
                  the input node for matches.
                   
                    Performs matches on the namevalue pairs in the input critiera, to the column name
                    column values in the part tables below the input node.  Ignores names in the input 
                    critiera that don't have a corresonding column in the part for matching.
                   
                  
         Returns matches ( NXOpen.Routing.CharacteristicList Li):  .
        """
        pass
    def MatchCriteriaWithFilter(start_node: str, criteria: NXOpen.Routing.CharacteristicList) -> List[NXOpen.Routing.CharacteristicList]:
        """
         Similar to Preferences.RoutingPartLibrary.MatchCriteria, however it also
                 filters out any parts that don't match the critiera specified by the current specification.  
         Returns matches ( NXOpen.Routing.CharacteristicList Li):  .
        """
        pass
import NXOpen
class RoutingPart(NXOpen.Object): 
    """  Contains the preferences related to placingfindingadding parts and generating
        the Routing bill of materials.  """
    class DetailLevel(Enum):
        """
        Members Include: 
         |Summary|  
         |Itemized|  

        """
        Summary: int
        Itemized: int
        @staticmethod
        def ValueOf(value: int) -> RoutingPart.DetailLevel:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FabricationNumbering(Enum):
        """
        Members Include: 
         |Sequence|  Sequential numbering of fabrications in the parts list. 
         |Original|  Use the fabrication number in the parts list. 

        """
        Sequence: int
        Original: int
        @staticmethod
        def ValueOf(value: int) -> RoutingPart.FabricationNumbering:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PreferredPortMethod(Enum):
        """
        Members Include: 
         |Attribute|  Examine an attribute applied to the
                                                                        port, and match it's value to a desired
                                                                        value. 
         |Name|  Compare the ports name with a desired value. 

        """
        Attribute: int
        Name: int
        @staticmethod
        def ValueOf(value: int) -> RoutingPart.PreferredPortMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StockLengthDisplay(Enum):
        """
        Members Include: 
         |Sum|  Display single sum for each type of stock. 
         |Item|  Display length of each stock individually. 

        """
        Sum: int
        Item: int
        @staticmethod
        def ValueOf(value: int) -> RoutingPart.StockLengthDisplay:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class UsePreferredPort(Enum):
        """
        Members Include: 
         |FalseValue|  
         |TrueValue|  

        """
        FalseValue: int
        TrueValue: int
        @staticmethod
        def ValueOf(value: int) -> RoutingPart.UsePreferredPort:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BomDetailLevelFlag(self) -> RoutingPart.DetailLevel:
        """
        Getter for property: ( RoutingPart.DetailLevel NXOpen.P) BomDetailLevelFlag
         Returns the detail level for the Routing bill of material.  
             
         
        """
        pass
    @BomDetailLevelFlag.setter
    def BomDetailLevelFlag(self, detail: RoutingPart.DetailLevel):
        """
        Setter for property: ( RoutingPart.DetailLevel NXOpen.P) BomDetailLevelFlag
         Returns the detail level for the Routing bill of material.  
             
         
        """
        pass
    @property
    def BomFormatPart(self) -> str:
        """
        Getter for property: (str) BomFormatPart
         Returns the name of the template Routing bill of material part file.  
             
         
        """
        pass
    @BomFormatPart.setter
    def BomFormatPart(self, bom_part: str):
        """
        Setter for property: (str) BomFormatPart
         Returns the name of the template Routing bill of material part file.  
             
         
        """
        pass
    @property
    def DefaultElbowNode(self) -> str:
        """
        Getter for property: (str) DefaultElbowNode
         Returns the node in the part library to use for searching for the default
                    elbow to place during create path.  
            The part library node must 
                    have a type of  NXOpen::Preferences::RoutingPartLibrary::NodeTypeTable . A
                    NULL node indicates no default elbow part table.   
         
        """
        pass
    @DefaultElbowNode.setter
    def DefaultElbowNode(self, elbow_node: str):
        """
        Setter for property: (str) DefaultElbowNode
         Returns the node in the part library to use for searching for the default
                    elbow to place during create path.  
            The part library node must 
                    have a type of  NXOpen::Preferences::RoutingPartLibrary::NodeTypeTable . A
                    NULL node indicates no default elbow part table.   
         
        """
        pass
    @property
    def FabricationNumberingFlag(self) -> RoutingPart.FabricationNumbering:
        """
        Getter for property: ( RoutingPart.FabricationNumbering NXOpen.P) FabricationNumberingFlag
         Returns the fabrication numbering for the Routing bill of material.  
             
         
        """
        pass
    @FabricationNumberingFlag.setter
    def FabricationNumberingFlag(self, numbering: RoutingPart.FabricationNumbering):
        """
        Setter for property: ( RoutingPart.FabricationNumbering NXOpen.P) FabricationNumberingFlag
         Returns the fabrication numbering for the Routing bill of material.  
             
         
        """
        pass
    @property
    def InvalidSequenceCharacters(self) -> str:
        """
        Getter for property: (str) InvalidSequenceCharacters
         Returns the list of characters that cannot be used when generating sequences
                    of terminals in qualify part.  
             
         
        """
        pass
    @InvalidSequenceCharacters.setter
    def InvalidSequenceCharacters(self, invalid_chars: str):
        """
        Setter for property: (str) InvalidSequenceCharacters
         Returns the list of characters that cannot be used when generating sequences
                    of terminals in qualify part.  
             
         
        """
        pass
    @property
    def Layer(self) -> int:
        """
        Getter for property: (int) Layer
         Returns the layer to apply to new components.  
             
         
        """
        pass
    @Layer.setter
    def Layer(self, layer: int):
        """
        Setter for property: (int) Layer
         Returns the layer to apply to new components.  
             
         
        """
        pass
    @property
    def MaximumSolutions(self) -> int:
        """
        Getter for property: (int) MaximumSolutions
         Returns the maximum number of placement solutions to generate when determining
                    placement solutions for a component.  
             
         
        """
        pass
    @MaximumSolutions.setter
    def MaximumSolutions(self, max_sols: int):
        """
        Setter for property: (int) MaximumSolutions
         Returns the maximum number of placement solutions to generate when determining
                    placement solutions for a component.  
             
         
        """
        pass
    @property
    def PreferredPortMethodFlag(self) -> RoutingPart.PreferredPortMethod:
        """
        Getter for property: ( RoutingPart.PreferredPortMethod NXOpen.P) PreferredPortMethodFlag
         Returns the current method for determining the preferred placement port.  
             
         
        """
        pass
    @property
    def StockLengthDisplayFlag(self) -> RoutingPart.StockLengthDisplay:
        """
        Getter for property: ( RoutingPart.StockLengthDisplay NXOpen.P) StockLengthDisplayFlag
         Returns the stock length display for the Routing bill of material.  
             
         
        """
        pass
    @StockLengthDisplayFlag.setter
    def StockLengthDisplayFlag(self, display: RoutingPart.StockLengthDisplay):
        """
        Setter for property: ( RoutingPart.StockLengthDisplay NXOpen.P) StockLengthDisplayFlag
         Returns the stock length display for the Routing bill of material.  
             
         
        """
        pass
    @property
    def UsePreferredPortFlag(self) -> RoutingPart.UsePreferredPort:
        """
        Getter for property: ( RoutingPart.UsePreferredPort NXOpen.P) UsePreferredPortFlag
         Returns whether or not to use the preffered placement port during
                    calcluation of placement solutions during place part.  
              
         
        """
        pass
    @UsePreferredPortFlag.setter
    def UsePreferredPortFlag(self, use_flag: RoutingPart.UsePreferredPort):
        """
        Setter for property: ( RoutingPart.UsePreferredPort NXOpen.P) UsePreferredPortFlag
         Returns whether or not to use the preffered placement port during
                    calcluation of placement solutions during place part.  
              
         
        """
        pass
    @property
    def PartLibrary() -> RoutingPartLibrary:
        """
         The Routing part library. 
        """
        pass
    def GetPreferredPortAttribute() -> Tuple[str, str]:
        """
         Gets the attribute and it's value for determining the preferred port for method type 
                    NXOpen.Preferences.RoutingPart.PreferredPortMethod.Attribute 
         Returns A tuple consisting of (attribute_name, attribute_value). 
         - attribute_name is: str.  if method is not 
                                NXOpen.Preferences.RoutingPart.PreferredPortMethod.Attribute .
         - attribute_value is: str.  if method is not
                                NXOpen.Preferences.RoutingPart.PreferredPortMethod.Attribute .

        """
        pass
    def GetPreferredPortName() -> str:
        """
         Gets the desired port name for method type
                    NXOpen.Preferences.RoutingPart.PreferredPortMethod.Name 
         Returns desired_port (str):   if method is not
                            NXOpen.Preferences.RoutingPart.PreferredPortMethod.Name .
        """
        pass
    def SetPreferredPortAttribute(attribute_name: str, attribute_value: str) -> None:
        """
         Sets the method for determining the preferred port to 
                    NXOpen.Preferences.RoutingPart.PreferredPortMethod.Attribute and
                    sets the desired port attribute and it's value. 
        """
        pass
    def SetPreferredPortName(desired_port: str) -> None:
        """
         Sets the method for determining the preferred port to 
                    NXOpen.Preferences.RoutingPart.PreferredPortMethod.Name and
                    sets the desired port name. 
        """
        pass
import NXOpen
import NXOpen.Routing
class RoutingPath(NXOpen.Object): 
    """ The RoutingPath object stores a set of path preferences. """
    class AddPointsToSpline(Enum):
        """
        Members Include: 
         |FalseValue|  Do not merge duplicate RCPs. 
         |TrueValue|  Merge duplicate RCPs. 

        """
        FalseValue: int
        TrueValue: int
        @staticmethod
        def ValueOf(value: int) -> RoutingPath.AddPointsToSpline:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class AllowedCornerType(Enum):
        """
        Members Include: 
         |NotSet|  UF_ROUTE_AV_CORNERS_NONE 
         |Bend|  UF_ROUTE_AV_CORNERS_BEND 
         |Cope|  UF_ROUTE_AV_CORNERS_COPE 
         |Miter|  UF_ROUTE_AV_CORNERS_MITER 
         |Sbend|  UF_ROUTE_AV_CORNERS_SBEND 

        """
        NotSet: int
        Bend: int
        Cope: int
        Miter: int
        Sbend: int
        @staticmethod
        def ValueOf(value: int) -> RoutingPath.AllowedCornerType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ConfirmBranchSel(Enum):
        """
        Members Include: 
         |FalseValue|  Do not confirm branch selection. 
         |TrueValue|  Confirm branch selection. 

        """
        FalseValue: int
        TrueValue: int
        @staticmethod
        def ValueOf(value: int) -> RoutingPath.ConfirmBranchSel:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ContinueUpdOnError(Enum):
        """
        Members Include: 
         |FalseValue|  
         |TrueValue|  

        """
        FalseValue: int
        TrueValue: int
        @staticmethod
        def ValueOf(value: int) -> RoutingPath.ContinueUpdOnError:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CreateSlopeConstraints(Enum):
        """
        Members Include: 
         |FalseValue|  
         |TrueValue|  

        """
        FalseValue: int
        TrueValue: int
        @staticmethod
        def ValueOf(value: int) -> RoutingPath.CreateSlopeConstraints:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CreateSmartRcps(Enum):
        """
        Members Include: 
         |FalseValue|  Do not create smart RCPs. 
         |TrueValue|  Create smart RCPs. 

        """
        FalseValue: int
        TrueValue: int
        @staticmethod
        def ValueOf(value: int) -> RoutingPath.CreateSmartRcps:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CreateTangency(Enum):
        """
        Members Include: 
         |FalseValue|  Do not merge duplicate RCPs. 
         |TrueValue|  Merge duplicate RCPs. 

        """
        FalseValue: int
        TrueValue: int
        @staticmethod
        def ValueOf(value: int) -> RoutingPath.CreateTangency:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CurveType(Enum):
        """
        Members Include: 
         |Line|  UF_ROUTE_AV_CURVES_LINES 
         |Arc|  UF_ROUTE_AV_CURVES_ARCS 
         |Spline|  UF_ROUTE_AV_CURVES_SPLINES 

        """
        Line: int
        Arc: int
        Spline: int
        @staticmethod
        def ValueOf(value: int) -> RoutingPath.CurveType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DefaultCornerType(Enum):
        """
        Members Include: 
         |NotSet|  No Corner
         |Bend|  Bend Corner
         |Miter|  Miter Corner 
         |BendTable|  Not really a corner type.
                                                                          Used to indicate use of bend table in
                                                                          conjunction with a Bend corner 

        """
        NotSet: int
        Bend: int
        Miter: int
        BendTable: int
        @staticmethod
        def ValueOf(value: int) -> RoutingPath.DefaultCornerType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DisplayObject(Enum):
        """
        Members Include: 
         |FalseValue|  
         |TrueValue|  

        """
        FalseValue: int
        TrueValue: int
        @staticmethod
        def ValueOf(value: int) -> RoutingPath.DisplayObject:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MergeDupRcps(Enum):
        """
        Members Include: 
         |FalseValue|  Do not merge duplicate RCPs. 
         |TrueValue|  Merge duplicate RCPs. 

        """
        FalseValue: int
        TrueValue: int
        @staticmethod
        def ValueOf(value: int) -> RoutingPath.MergeDupRcps:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RadiusMethod(Enum):
        """
        Members Include: 
         |Radius|  Use specified radius 
         |Ratio|  Use ratio to stock diameter to determine radius 
         |Table|  Use radius obtained from a bend table lookup 
         |InnerRadius|  Use inner radius 
         |RatioToAttribute|  Use ratio to stock attribute to determine radius 

        """
        Radius: int
        Ratio: int
        Table: int
        InnerRadius: int
        RatioToAttribute: int
        @staticmethod
        def ValueOf(value: int) -> RoutingPath.RadiusMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RadiusUnits(Enum):
        """
        Members Include: 
         |NotSet|  Unspecified. Use units of part file. 
         |Inches|  Use inch units 
         |Millimeters|  Use metric (mm) units 

        """
        NotSet: int
        Inches: int
        Millimeters: int
        @staticmethod
        def ValueOf(value: int) -> RoutingPath.RadiusUnits:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetAllowedCorners() -> List[RoutingPath.AllowedCornerType]:
        """
         Query the types of corners allowed in an application view 
         Returns allowed_corners ( RoutingPath.AllowedCornerType List[NXOpen):  .
        """
        pass
    def GetAllowedCurves() -> List[RoutingPath.CurveType]:
        """
         Query the types of curves allowed in an application view 
         Returns allowed_curves ( RoutingPath.CurveType List[NXOpen):  .
        """
        pass
    def GetBendAttributeName() -> str:
        """
         Bret Leupen 14-Oct-2019
         Returns bend_attribute_name (str):  .
        """
        pass
    def GetBendRadius() -> float:
        """
         Needs a work part and a loaded applicaiton view.
                    Radius units are converted to work part units automatically.
                    Returns -1 and quits if input requirements are not met. 
         Returns bend_radius (float):  .
        """
        pass
    def GetBendRadiusMethod() -> RoutingPath.RadiusMethod:
        """
         Query wether the default corner should use bend ratio. 
         Returns radius_method ( RoutingPath.RadiusMethod NXOpen.P):  .
        """
        pass
    def GetBendRadiusTable() -> str:
        """
         Returns the bend radius table spreadsheet name. Used when default corner uses bend table method 
         Returns bend_table_spreadsheet (str):  .
        """
        pass
    def GetBendRadiusTableDataForStock(stock_part_number: str) -> List[NXOpen.Routing.CharacteristicList]:
        """
         Returns the rows of data from the bend radius table for the given stock part number. 
         Returns stock_rows ( NXOpen.Routing.CharacteristicList Li):  .
        """
        pass
    def GetBendRadiusUnits() -> RoutingPath.RadiusUnits:
        """
         Query bend radius units stored in path preferences 
         Returns radius_units ( RoutingPath.RadiusUnits NXOpen.P):  .
        """
        pass
    def GetBendRatio() -> float:
        """
         Query default bend ratio. Used when default corner uses bend ratio method 
         Returns bend_ratio (float):  .
        """
        pass
    def GetBendRatioToAttribute() -> float:
        """
         Bret Leupen 14-Oct-2019
         Returns bend_ratio_to_attribute (float):  .
        """
        pass
    def GetConfirmBranchSelection() -> RoutingPath.ConfirmBranchSel:
        """
         Confirm branch selection during Path selection? 
         Returns confirm_branch_sel ( RoutingPath.ConfirmBranchSel NXOpen.P):  .
        """
        pass
    def GetContinueUpdateOnError() -> RoutingPath.ContinueUpdOnError:
        """
         Query default down direction for fixed length splines 
         Returns update ( RoutingPath.ContinueUpdOnError NXOpen.P):  .
        """
        pass
    def GetCreateNewPointsOnSubdivide() -> RoutingPath.AddPointsToSpline:
        """
         Add points to subdivided splines to maintain shape? 
         Returns add_points ( RoutingPath.AddPointsToSpline NXOpen.P):  .
        """
        pass
    def GetCreateSlopeConstraints() -> RoutingPath.CreateSlopeConstraints:
        """
         Create slope constraints during line path creation to and from fitting ports? 
         Returns create_slope_constraints ( RoutingPath.CreateSlopeConstraints NXOpen.P):  .
        """
        pass
    def GetCreateSmartRcps() -> RoutingPath.CreateSmartRcps:
        """
         Create smart RCPs during path creation? 
         Returns create_smart ( RoutingPath.CreateSmartRcps NXOpen.P):  .
        """
        pass
    def GetCreateSplineTangency() -> RoutingPath.CreateTangency:
        """
         Create tangency between splines? 
         Returns apply_tangency ( RoutingPath.CreateTangency NXOpen.P):  .
        """
        pass
    def GetDefaultCorner() -> RoutingPath.DefaultCornerType:
        """
         Query the default corner type in an application view 
         Returns default_corner ( RoutingPath.DefaultCornerType NXOpen.P):  .
        """
        pass
    def GetDisplayAnchors() -> RoutingPath.DisplayObject:
        """
         Display anchors? 
         Returns display_anchors ( RoutingPath.DisplayObject NXOpen.P):  .
        """
        pass
    def GetDisplayConnectedPorts() -> RoutingPath.DisplayObject:
        """
         Display connected ports? 
         Returns display_connected_ports ( RoutingPath.DisplayObject NXOpen.P):  .
        """
        pass
    def GetDisplayPortLength() -> float:
        """
         Displayed port length 
         Returns display_port_length (float):  .
        """
        pass
    def GetDisplayPorts() -> RoutingPath.DisplayObject:
        """
         Display ports? 
         Returns display_ports ( RoutingPath.DisplayObject NXOpen.P):  .
        """
        pass
    def GetDisplayRcps() -> RoutingPath.DisplayObject:
        """
         Display RCPs? 
         Returns display_rcps ( RoutingPath.DisplayObject NXOpen.P):  .
        """
        pass
    def GetDisplaySegmentConstraints() -> RoutingPath.DisplayObject:
        """
         Display segment constraints? 
         Returns display_constraints ( RoutingPath.DisplayObject NXOpen.P):  .
        """
        pass
    def GetHealPathCurveType() -> RoutingPath.CurveType:
        """
         Heal Path curve type. 
         Returns heal_path_curve_type ( RoutingPath.CurveType NXOpen.P):  .
        """
        pass
    def GetMergeDuplicateRcps() -> RoutingPath.MergeDupRcps:
        """
         Merge duplicate RCPs after a Transform [Move or Copy] operation? 
         Returns merge_duplicates ( RoutingPath.MergeDupRcps NXOpen.P):  .
        """
        pass
    def GetStockOffsetExpression() -> str:
        """
         Query default stock offset expression used by Create Path and Create Stock Offset Port [via Qualify Part] 
         Returns stock_offset_exp (str):  .
        """
        pass
    def SetAllowedCorners(allowed_corners: List[RoutingPath.AllowedCornerType]) -> None:
        """
         
        """
        pass
    def SetAllowedCurves(allowed_curves: List[RoutingPath.CurveType]) -> None:
        """
         
        """
        pass
    def SetBendAttributeName(bend_attribute_name: str) -> None:
        """
         Bret Leupen 14-Oct-2019
        """
        pass
    def SetBendRadius(bend_radius: float) -> None:
        """
         Needs a work part and a loaded applicaiton view.
                    Radius units are assumed to be work part units and are set automatically.
                    Returns -1 and quits if input requirements are not met. 
        """
        pass
    def SetBendRadiusMethod(radius_method: RoutingPath.RadiusMethod) -> None:
        """
         Set whether the default corner should use bend ratio. 
        """
        pass
    def SetBendRadiusTable(bend_table_spreadsheet: str) -> None:
        """
         Sets the bend radius table spreadsheet name. Used when default corner uses bend table method 
        """
        pass
    def SetBendRadiusUnits(radius_units: RoutingPath.RadiusUnits) -> None:
        """
         
        """
        pass
    def SetBendRatio(bend_ratio: float) -> None:
        """
         
        """
        pass
    def SetBendRatioToAttribute(bend_ratio_to_attribute: float) -> None:
        """
         Bret Leupen 14-Oct-2019
        """
        pass
    def SetConfirmBranchSelection(confirm_branch_sel: RoutingPath.ConfirmBranchSel) -> None:
        """
         
        """
        pass
    def SetContinueUpdateOnError(update: RoutingPath.ContinueUpdOnError) -> None:
        """
         
        """
        pass
    def SetCreateNewPointsOnSubdivide(add_points: RoutingPath.AddPointsToSpline) -> None:
        """
          
        """
        pass
    def SetCreateSlopeConstraints(create_slope_constraints: RoutingPath.CreateSlopeConstraints) -> None:
        """
         
        """
        pass
    def SetCreateSmartRcps(create_smart: RoutingPath.CreateSmartRcps) -> None:
        """
         
        """
        pass
    def SetCreateSplineTangency(apply_tangency: RoutingPath.CreateTangency) -> None:
        """
          
        """
        pass
    def SetDefaultCorner(default_corner: RoutingPath.DefaultCornerType) -> None:
        """
         
        """
        pass
    def SetDisplayAnchors(display_anchors: RoutingPath.DisplayObject) -> None:
        """
         
        """
        pass
    def SetDisplayConnectedPorts(display_connected_ports: RoutingPath.DisplayObject) -> None:
        """
         Display connected ports in the model 
        """
        pass
    def SetDisplayPortLength(display_port_length: float) -> None:
        """
         
        """
        pass
    def SetDisplayPorts(display_ports: RoutingPath.DisplayObject) -> None:
        """
         Display ports in the model? 
        """
        pass
    def SetDisplayRcps(display_rcps: RoutingPath.DisplayObject) -> None:
        """
         
        """
        pass
    def SetDisplaySegmentConstraints(display_constraints: RoutingPath.DisplayObject) -> None:
        """
         
        """
        pass
    def SetHealPathCurveType(heal_path_curve_type: RoutingPath.CurveType) -> None:
        """
         
        """
        pass
    def SetMergeDuplicateRcps(merge_duplicates: RoutingPath.MergeDupRcps) -> None:
        """
         
        """
        pass
    def SetStockOffsetExpression(stock_offset_exp: str) -> None:
        """
         
        """
        pass
import NXOpen
class RoutingPreferences(NXOpen.Object): 
    """ Represents the set of navigation preferences applicable to entire session. """
    @property
    def ApplyElectricalTopologyPathStyle(self) -> bool:
        """
        Getter for property: (bool) ApplyElectricalTopologyPathStyle
         Returns the routed system designer determines whether or not to show cableway electrical topology paths in the specified color, style, and width   
            
         
        """
        pass
    @ApplyElectricalTopologyPathStyle.setter
    def ApplyElectricalTopologyPathStyle(self, applyElectricalTopologyPathStyle: bool):
        """
        Setter for property: (bool) ApplyElectricalTopologyPathStyle
         Returns the routed system designer determines whether or not to show cableway electrical topology paths in the specified color, style, and width   
            
         
        """
        pass
    @property
    def ApplyJumpPathStyle(self) -> bool:
        """
        Getter for property: (bool) ApplyJumpPathStyle
         Returns the routed system designer determines whether or not to show cableway jump paths in the specified color, style, and width   
            
         
        """
        pass
    @ApplyJumpPathStyle.setter
    def ApplyJumpPathStyle(self, applyJumpPathStyle: bool):
        """
        Setter for property: (bool) ApplyJumpPathStyle
         Returns the routed system designer determines whether or not to show cableway jump paths in the specified color, style, and width   
            
         
        """
        pass
    @property
    def ApplyTranslucencyToExistingObjects(self) -> bool:
        """
        Getter for property: (bool) ApplyTranslucencyToExistingObjects
         Returns the preference for applying temporary translucency to existing routing objects in session.  
            
         
        """
        pass
    @ApplyTranslucencyToExistingObjects.setter
    def ApplyTranslucencyToExistingObjects(self, applyToExisting: bool):
        """
        Setter for property: (bool) ApplyTranslucencyToExistingObjects
         Returns the preference for applying temporary translucency to existing routing objects in session.  
            
         
        """
        pass
    @property
    def CurrentDiscipline(self) -> str:
        """
        Getter for property: (str) CurrentDiscipline
         Returns the current discipline.  
           A discipline value of "" (the empty string)
                indicates no current discipline.    
         
        """
        pass
    @CurrentDiscipline.setter
    def CurrentDiscipline(self, currentDiscipline: str):
        """
        Setter for property: (str) CurrentDiscipline
         Returns the current discipline.  
           A discipline value of "" (the empty string)
                indicates no current discipline.    
         
        """
        pass
    @property
    def DisciplineIndex(self) -> int:
        """
        Getter for property: (int) DisciplineIndex
         Returns the next generation routing discipline preference   
            
         
        """
        pass
    @DisciplineIndex.setter
    def DisciplineIndex(self, disciplineIndex: int):
        """
        Setter for property: (int) DisciplineIndex
         Returns the next generation routing discipline preference   
            
         
        """
        pass
    @property
    def DisplayConnectedPorts(self) -> bool:
        """
        Getter for property: (bool) DisplayConnectedPorts
         Returns the next generation routing display connected ports preference   
            
         
        """
        pass
    @DisplayConnectedPorts.setter
    def DisplayConnectedPorts(self, displayConnectedPorts: bool):
        """
        Setter for property: (bool) DisplayConnectedPorts
         Returns the next generation routing display connected ports preference   
            
         
        """
        pass
    @property
    def ElectricalTopologyPathColor(self) -> int:
        """
        Getter for property: (int) ElectricalTopologyPathColor
         Returns the routed system designer specifies the color of cableway electrical topology paths   
            
         
        """
        pass
    @ElectricalTopologyPathColor.setter
    def ElectricalTopologyPathColor(self, electricalTopologyPathColor: int):
        """
        Setter for property: (int) ElectricalTopologyPathColor
         Returns the routed system designer specifies the color of cableway electrical topology paths   
            
         
        """
        pass
    @property
    def ElectricalTopologyPathStyle(self) -> int:
        """
        Getter for property: (int) ElectricalTopologyPathStyle
         Returns the routed system designer specifies the line style for cableway electrical topology paths   
            
         
        """
        pass
    @ElectricalTopologyPathStyle.setter
    def ElectricalTopologyPathStyle(self, electricalTopologyPathStyle: int):
        """
        Setter for property: (int) ElectricalTopologyPathStyle
         Returns the routed system designer specifies the line style for cableway electrical topology paths   
            
         
        """
        pass
    @property
    def ElectricalTopologyPathWidth(self) -> int:
        """
        Getter for property: (int) ElectricalTopologyPathWidth
         Returns the routed system designer specifies the line width for cableway electrical topology paths   
            
         
        """
        pass
    @ElectricalTopologyPathWidth.setter
    def ElectricalTopologyPathWidth(self, electricalTopologyPathWidth: int):
        """
        Setter for property: (int) ElectricalTopologyPathWidth
         Returns the routed system designer specifies the line width for cableway electrical topology paths   
            
         
        """
        pass
    @property
    def InsulationTranslucency(self) -> int:
        """
        Getter for property: (int) InsulationTranslucency
         Returns the next generation insulation translucency preference   
            
         
        """
        pass
    @InsulationTranslucency.setter
    def InsulationTranslucency(self, insulationTranslucency: int):
        """
        Setter for property: (int) InsulationTranslucency
         Returns the next generation insulation translucency preference   
            
         
        """
        pass
    @property
    def JumpPathColor(self) -> int:
        """
        Getter for property: (int) JumpPathColor
         Returns the routed system designer specifies the color of cableway jump paths   
            
         
        """
        pass
    @JumpPathColor.setter
    def JumpPathColor(self, jumpPathColor: int):
        """
        Setter for property: (int) JumpPathColor
         Returns the routed system designer specifies the color of cableway jump paths   
            
         
        """
        pass
    @property
    def JumpPathStyle(self) -> int:
        """
        Getter for property: (int) JumpPathStyle
         Returns the routed system designer specifies the line style for cableway jump paths   
            
         
        """
        pass
    @JumpPathStyle.setter
    def JumpPathStyle(self, jumpPathStyle: int):
        """
        Setter for property: (int) JumpPathStyle
         Returns the routed system designer specifies the line style for cableway jump paths   
            
         
        """
        pass
    @property
    def JumpPathWidth(self) -> int:
        """
        Getter for property: (int) JumpPathWidth
         Returns the routed system designer specifies the line width for cableway jump paths   
            
         
        """
        pass
    @JumpPathWidth.setter
    def JumpPathWidth(self, jumpPathWidth: int):
        """
        Setter for property: (int) JumpPathWidth
         Returns the routed system designer specifies the line width for cableway jump paths   
            
         
        """
        pass
    @property
    def OffsetExpressionString(self) -> str:
        """
        Getter for property: (str) OffsetExpressionString
         Returns the next generation routing offset expression string preference   
            
         
        """
        pass
    @OffsetExpressionString.setter
    def OffsetExpressionString(self, offsetExpressionString: str):
        """
        Setter for property: (str) OffsetExpressionString
         Returns the next generation routing offset expression string preference   
            
         
        """
        pass
    @property
    def PortLength(self) -> float:
        """
        Getter for property: (float) PortLength
         Returns the next generation routing port length preference in part units   
            
         
        """
        pass
    @PortLength.setter
    def PortLength(self, portLength: float):
        """
        Setter for property: (float) PortLength
         Returns the next generation routing port length preference in part units   
            
         
        """
        pass
    @property
    def SpaceReservationTranslucency(self) -> int:
        """
        Getter for property: (int) SpaceReservationTranslucency
         Returns the next generation space reservation translucency preference   
            
         
        """
        pass
    @SpaceReservationTranslucency.setter
    def SpaceReservationTranslucency(self, spaceReservationTranslucency: int):
        """
        Setter for property: (int) SpaceReservationTranslucency
         Returns the next generation space reservation translucency preference   
            
         
        """
        pass
    @property
    def StockComponentFolder(self) -> str:
        """
        Getter for property: (str) StockComponentFolder
         Returns the routed system designer stock component folder preference   
            
         
        """
        pass
    @StockComponentFolder.setter
    def StockComponentFolder(self, stockComponentFolder: str):
        """
        Setter for property: (str) StockComponentFolder
         Returns the routed system designer stock component folder preference   
            
         
        """
        pass
    @property
    def StockTranslucency(self) -> int:
        """
        Getter for property: (int) StockTranslucency
         Returns the next generation routing stock translucency preference   
            
         
        """
        pass
    @StockTranslucency.setter
    def StockTranslucency(self, stockTranslucency: int):
        """
        Setter for property: (int) StockTranslucency
         Returns the next generation routing stock translucency preference   
            
         
        """
        pass
    @property
    def SubdivideSegmentForFixturePartPlacement(self) -> bool:
        """
        Getter for property: (bool) SubdivideSegmentForFixturePartPlacement
         Returns the routed system designer subdivide segment for fixture part placement preference.  
            
         
        """
        pass
    @SubdivideSegmentForFixturePartPlacement.setter
    def SubdivideSegmentForFixturePartPlacement(self, prefSubdivideSegment: bool):
        """
        Setter for property: (bool) SubdivideSegmentForFixturePartPlacement
         Returns the routed system designer subdivide segment for fixture part placement preference.  
            
         
        """
        pass
    @property
    def UsePreferredPortPlacement(self) -> bool:
        """
        Getter for property: (bool) UsePreferredPortPlacement
         Returns the routed system designer use preferred port placement preference   
            
         
        """
        pass
    @UsePreferredPortPlacement.setter
    def UsePreferredPortPlacement(self, usePreferredPortPlacement: bool):
        """
        Setter for property: (bool) UsePreferredPortPlacement
         Returns the routed system designer use preferred port placement preference   
            
         
        """
        pass
    def GetAllAvailableDisciplines() -> List[str]:
        """
         Returns All disciplines available in the current application view. 
         Returns disciplines (List[str]): .
        """
        pass
import NXOpen
import NXOpen.Routing
class RoutingStock(NXOpen.Object): 
    """ The Preferences for Routing Stock objects.  These correspond to
        the values represented on the Preferences-Routing dialog, Stock
        property page. """
    class SpaceReservationModeFlag(Enum):
        """
        Members Include: 
         |LegacySpaceReservation|  solid body in the work part, no component 
         |SpaceReservationAsComponent|  component created with solid body in the component 

        """
        LegacySpaceReservation: int
        SpaceReservationAsComponent: int
        @staticmethod
        def ValueOf(value: int) -> RoutingStock.SpaceReservationModeFlag:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StockModeFlag(Enum):
        """
        Members Include: 
         |LegacyStock|  solid body in the work part, no component 
         |StockAsComponent|  component created with solid body in the component 

        """
        LegacyStock: int
        StockAsComponent: int
        @staticmethod
        def ValueOf(value: int) -> RoutingStock.StockModeFlag:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CurrentTile(self) -> str:
        """
        Getter for property: (str) CurrentTile
         Returns the current routing leveltile   
            
         
        """
        pass
    @CurrentTile.setter
    def CurrentTile(self, tile: str):
        """
        Setter for property: (str) CurrentTile
         Returns the current routing leveltile   
            
         
        """
        pass
    @property
    def DefaultStockStyle(self) -> NXOpen.Routing.StockStyle:
        """
        Getter for property: ( NXOpen.Routing.StockStyle) DefaultStockStyle
         Returns the default stock style   
            
         
        """
        pass
    @DefaultStockStyle.setter
    def DefaultStockStyle(self, default_stock_style: NXOpen.Routing.StockStyle):
        """
        Setter for property: ( NXOpen.Routing.StockStyle) DefaultStockStyle
         Returns the default stock style   
            
         
        """
        pass
    @property
    def DeleteOverstock(self) -> bool:
        """
        Getter for property: (bool) DeleteOverstock
         Returns the delete overstock flag during deletion of last stock covered by
                    the overstock   
            
         
        """
        pass
    @DeleteOverstock.setter
    def DeleteOverstock(self, delete_overstock: bool):
        """
        Setter for property: (bool) DeleteOverstock
         Returns the delete overstock flag during deletion of last stock covered by
                    the overstock   
            
         
        """
        pass
    @property
    def SpaceReservationMode(self) -> RoutingStock.SpaceReservationModeFlag:
        """
        Getter for property: ( RoutingStock.SpaceReservationModeFlag NXOpen.P) SpaceReservationMode
         Returns the space reservation creation mode   
            
         
        """
        pass
    @SpaceReservationMode.setter
    def SpaceReservationMode(self, spaceReservationMode: RoutingStock.SpaceReservationModeFlag):
        """
        Setter for property: ( RoutingStock.SpaceReservationModeFlag NXOpen.P) SpaceReservationMode
         Returns the space reservation creation mode   
            
         
        """
        pass
    @property
    def SpaceReservationTranslucency(self) -> int:
        """
        Getter for property: (int) SpaceReservationTranslucency
         Returns the desired translucnecy of the newly created Space Reservation Stock   
            
         
        """
        pass
    @SpaceReservationTranslucency.setter
    def SpaceReservationTranslucency(self, spaceReservationTranslucency: int):
        """
        Setter for property: (int) SpaceReservationTranslucency
         Returns the desired translucnecy of the newly created Space Reservation Stock   
            
         
        """
        pass
    @property
    def StockAnchor(self) -> str:
        """
        Getter for property: (str) StockAnchor
         Returns the  NXOpen::Routing::Anchor  name associated with the stock preferences.  
             
         
        """
        pass
    @StockAnchor.setter
    def StockAnchor(self, anchor_name: str):
        """
        Setter for property: (str) StockAnchor
         Returns the  NXOpen::Routing::Anchor  name associated with the stock preferences.  
             
         
        """
        pass
    @property
    def StockFolder(self) -> str:
        """
        Getter for property: (str) StockFolder
         Returns the default folder for stock components   
            
         
        """
        pass
    @StockFolder.setter
    def StockFolder(self, stock_folder: str):
        """
        Setter for property: (str) StockFolder
         Returns the default folder for stock components   
            
         
        """
        pass
    @property
    def StockMode(self) -> RoutingStock.StockModeFlag:
        """
        Getter for property: ( RoutingStock.StockModeFlag NXOpen.P) StockMode
         Returns the stock creation mode   
            
         
        """
        pass
    @StockMode.setter
    def StockMode(self, stock_mode: RoutingStock.StockModeFlag):
        """
        Setter for property: ( RoutingStock.StockModeFlag NXOpen.P) StockMode
         Returns the stock creation mode   
            
         
        """
        pass
    def GetDefaultStock() -> Tuple[NXOpen.Routing.CharacteristicList, NXOpen.Routing.CharacteristicList]:
        """
         Returns the current default stock to assign when creating paths.  
         Returns A tuple consisting of (stock_part, data_charx). 
         - stock_part is:  NXOpen.Routing.CharacteristicList. Characteristic list used to find the appropriate 
                      NXOpen.Routing.StockData for building the stock.  
                      See Routing.StockDataCollection.CreateStockData. .
         - data_charx is:  NXOpen.Routing.CharacteristicList. The list of optional and required characteristics to apply to the new stock. .

        """
        pass
    def GetPreferredFillerStock() -> Tuple[NXOpen.Routing.CharacteristicList, NXOpen.Routing.CharacteristicList]:
        """
         Returns the preferred for creating filler stock.  
         Returns A tuple consisting of (stock_part, data_charx). 
         - stock_part is:  NXOpen.Routing.CharacteristicList. Characteristic list used to find the appropriate 
                      NXOpen.Routing.StockData for building the stock.  
                      See Routing.StockDataCollection.CreateStockData. .
         - data_charx is:  NXOpen.Routing.CharacteristicList. The list of optional and required characteristics to apply to the new stock. .

        """
        pass
    def GetPreferredOverstock() -> Tuple[NXOpen.Routing.CharacteristicList, NXOpen.Routing.CharacteristicList]:
        """
         Returns the preferred stock for creating overstock.  
         Returns A tuple consisting of (stock_part, data_charx). 
         - stock_part is:  NXOpen.Routing.CharacteristicList. Characteristic list used to find the appropriate 
                      NXOpen.Routing.StockData for building the stock.  
                      See Routing.StockDataCollection.CreateStockData. .
         - data_charx is:  NXOpen.Routing.CharacteristicList. The list of optional and required characteristics to apply to the new stock. .

        """
        pass
    def GetPreferredSpaceReservation() -> Tuple[NXOpen.Routing.CharacteristicList, NXOpen.Routing.CharacteristicList]:
        """
         Returns the preferred stock for creating space reservation  
         Returns A tuple consisting of (stock_part, data_charx). 
         - stock_part is:  NXOpen.Routing.CharacteristicList. Characteristic list used to find the appropriate 
                      NXOpen.Routing.StockData for building the stock.  
                      See Routing.StockDataCollection.CreateStockData. .
         - data_charx is:  NXOpen.Routing.CharacteristicList. The list of optional and required characteristics to apply to the new stock. .

        """
        pass
    def SetDefaultStock(stock_part: NXOpen.Routing.CharacteristicList, data_charx: NXOpen.Routing.CharacteristicList) -> None:
        """
         Sets the current default stock to assign when creating paths. 
        """
        pass
    def SetPreferredFillerStock(stock_part: NXOpen.Routing.CharacteristicList, data_charx: NXOpen.Routing.CharacteristicList) -> None:
        """
         Sets the preferred stock for creating filler stock 
        """
        pass
    def SetPreferredOverstock(stock_part: NXOpen.Routing.CharacteristicList, data_charx: NXOpen.Routing.CharacteristicList) -> None:
        """
         Sets the preferred stock for creating overstock 
        """
        pass
    def SetPreferredSpaceReservation(stock_part: NXOpen.Routing.CharacteristicList, data_charx: NXOpen.Routing.CharacteristicList) -> None:
        """
         Sets the preferred stock for creating space Reservation 
        """
        pass
import NXOpen
class RoutingUserPreferences(NXOpen.Object): 
    """ Allows access to the User Preferences section of the Routing Application View file. """
    def GetDoubleArrayPreference(name: str) -> Tuple[bool, List[float]]:
        """
         Returns the values of the named double array user preference from the Application View file. 
         Returns A tuple consisting of (isFound, values). 
         - isFound is: bool. Was the preference found in the Application View file? .
         - values is: List[float]. The values of the preference, if found.  .

        """
        pass
    def GetDoublePreference(name: str) -> Tuple[bool, float]:
        """
         Returns the value of the named double user preference from the Application View file. 
         Returns A tuple consisting of (isFound, value). 
         - isFound is: bool. Was the preference found in the Application View file? .
         - value is: float. The value of the preference, if found. .

        """
        pass
    def GetIntegerArrayPreference(name: str) -> Tuple[bool, List[int]]:
        """
         Returns the values of the named integer array user preference from the Application View file. 
         Returns A tuple consisting of (isFound, values). 
         - isFound is: bool. Was the preference found in the Application View file? .
         - values is: List[int]. The values of the preference, if found.  .

        """
        pass
    def GetIntegerPreference(name: str) -> Tuple[bool, int]:
        """
         Returns the value of the named integer user preference from the Application View file. 
         Returns A tuple consisting of (isFound, value). 
         - isFound is: bool. Was the preference found in the Application View file? .
         - value is: int. The value of the preference, if found. .

        """
        pass
    def GetStringArrayPreference(name: str) -> Tuple[bool, List[str]]:
        """
         Returns the values of the named string array user preference from the Application View file. 
         Returns A tuple consisting of (isFound, values). 
         - isFound is: bool. Was the preference found in the Application View file? .
         - values is: List[str]. The values of the preference, if found.  .

        """
        pass
    def GetStringPreference(name: str) -> Tuple[bool, str]:
        """
         Returns the value of the named string user preference from the Application View file. 
         Returns A tuple consisting of (isFound, value). 
         - isFound is: bool. Was the preference found in the Application View file? .
         - value is: str. The value of the preference, if found. .

        """
        pass
    def SetDoubleArrayPreference(name: str, values: List[float]) -> None:
        """
         Sets the values of the named double array user preference in the current NX session. 
        """
        pass
    def SetDoublePreference(name: str, value: float) -> None:
        """
         Sets the value of the named double user preference in the current NX session. 
        """
        pass
    def SetIntegerArrayPreference(name: str, values: List[int]) -> None:
        """
         Sets the values of the named integer array user preference in the current NX session. 
        """
        pass
    def SetIntegerPreference(name: str, value: int) -> None:
        """
         Sets the value of the named integer user preference in the current NX session. 
        """
        pass
    def SetStringArrayPreference(name: str, values: List[str]) -> None:
        """
         Sets the values of the named string array user preference in the current NX session. 
        """
        pass
    def SetStringPreference(name: str, value: str) -> None:
        """
         Sets the value of the named string user preference in the current NX session. 
        """
        pass
import NXOpen
class RulePreferences(NXOpen.Object): 
    """ Provides methods for manipulating the Knowledge Fusion preferences in a session. """
    class AbsoluteTemperatureConversionDefinition:
        """
         Math Function definition for converting base part temperature from relative to absolute. 
         RulePreferencesAbsoluteTemperatureConversionDefinition_Struct NXOpen.P is an alias for  RulePreferences.AbsoluteTemperatureConversionDefinition NXOpen.P.
        """
        @property
        def MathFunctionName(self) -> str:
            """
            Getter for property MathFunctionName
            """
            pass
        @MathFunctionName.setter
        def MathFunctionName(self, value: str):
            """
            Getter for property MathFunctionNameSetter for property MathFunctionName
            """
            pass
        @property
        def CanReturnUnits(self) -> bool:
            """
            Getter for property CanReturnUnits
            This may be optional, but the conversion needs to know up front if it is possible.

            """
            pass
        @CanReturnUnits.setter
        def CanReturnUnits(self, value: bool):
            """
            Getter for property CanReturnUnits
            This may be optional, but the conversion needs to know up front if it is possible.
            Setter for property CanReturnUnits
            This may be optional, but the conversion needs to know up front if it is possible.

            """
            pass
        @property
        def CanHaveOptionalBaseParameter(self) -> bool:
            """
            Getter for property CanHaveOptionalBaseParameter
            Is one of the parameter inputs the optional base parameter.

            """
            pass
        @CanHaveOptionalBaseParameter.setter
        def CanHaveOptionalBaseParameter(self, value: bool):
            """
            Getter for property CanHaveOptionalBaseParameter
            Is one of the parameter inputs the optional base parameter.
            Setter for property CanHaveOptionalBaseParameter
            Is one of the parameter inputs the optional base parameter.

            """
            pass
        @property
        def CanHaveOptionalUseUnitsParameter(self) -> bool:
            """
            Getter for property CanHaveOptionalUseUnitsParameter
            Is one of the parameter inputs the optional useUnits parameter, such as abs or mod?

            """
            pass
        @CanHaveOptionalUseUnitsParameter.setter
        def CanHaveOptionalUseUnitsParameter(self, value: bool):
            """
            Getter for property CanHaveOptionalUseUnitsParameter
            Is one of the parameter inputs the optional useUnits parameter, such as abs or mod?
            Setter for property CanHaveOptionalUseUnitsParameter
            Is one of the parameter inputs the optional useUnits parameter, such as abs or mod?

            """
            pass
        @property
        def OptionLocation(self) -> int:
            """
            Getter for property OptionLocation
            This is the actual location where the value (truefalse, 10) may be found to identify if units are impacted.

            """
            pass
        @OptionLocation.setter
        def OptionLocation(self, value: int):
            """
            Getter for property OptionLocation
            This is the actual location where the value (truefalse, 10) may be found to identify if units are impacted.
            Setter for property OptionLocation
            This is the actual location where the value (truefalse, 10) may be found to identify if units are impacted.

            """
            pass
        @property
        def IsDependentOnOptionalParameter(self) -> bool:
            """
            Getter for property IsDependentOnOptionalParameter
            The math function may return units, but that may be dependent on the parameters whether it actually does.

            """
            pass
        @IsDependentOnOptionalParameter.setter
        def IsDependentOnOptionalParameter(self, value: bool):
            """
            Getter for property IsDependentOnOptionalParameter
            The math function may return units, but that may be dependent on the parameters whether it actually does.
            Setter for property IsDependentOnOptionalParameter
            The math function may return units, but that may be dependent on the parameters whether it actually does.

            """
            pass
        @property
        def NotConvertingParameterWithNoOption(self) -> bool:
            """
            Getter for property NotConvertingParameterWithNoOption
            This identifies the function so that the parameters will not be converted if the optional input is missing.

            """
            pass
        @NotConvertingParameterWithNoOption.setter
        def NotConvertingParameterWithNoOption(self, value: bool):
            """
            Getter for property NotConvertingParameterWithNoOption
            This identifies the function so that the parameters will not be converted if the optional input is missing.
            Setter for property NotConvertingParameterWithNoOption
            This identifies the function so that the parameters will not be converted if the optional input is missing.

            """
            pass
        @property
        def NotConvertingParameterIfOptionIsOff(self) -> bool:
            """
            Getter for property NotConvertingParameterIfOptionIsOff
            This identifies the function so that if the optional parameter is present, but if false0, then the parameters will not be converted.

            """
            pass
        @NotConvertingParameterIfOptionIsOff.setter
        def NotConvertingParameterIfOptionIsOff(self, value: bool):
            """
            Getter for property NotConvertingParameterIfOptionIsOff
            This identifies the function so that if the optional parameter is present, but if false0, then the parameters will not be converted.
            Setter for property NotConvertingParameterIfOptionIsOff
            This identifies the function so that if the optional parameter is present, but if false0, then the parameters will not be converted.

            """
            pass
        @property
        def IsFinalAdjustmentNotNeccessaryIfUnitless(self) -> bool:
            """
            Getter for property IsFinalAdjustmentNotNeccessaryIfUnitless
            This function does not need to be finally adjusted if the expression is unitless.

            """
            pass
        @IsFinalAdjustmentNotNeccessaryIfUnitless.setter
        def IsFinalAdjustmentNotNeccessaryIfUnitless(self, value: bool):
            """
            Getter for property IsFinalAdjustmentNotNeccessaryIfUnitless
            This function does not need to be finally adjusted if the expression is unitless.
            Setter for property IsFinalAdjustmentNotNeccessaryIfUnitless
            This function does not need to be finally adjusted if the expression is unitless.

            """
            pass
        @property
        def DontConvertParameterLastResort(self) -> bool:
            """
            Getter for property DontConvertParameterLastResort
            Once all the other checks have been performed, if none of them are applicable, then check                                                    this setting.

            """
            pass
        @DontConvertParameterLastResort.setter
        def DontConvertParameterLastResort(self, value: bool):
            """
            Getter for property DontConvertParameterLastResort
            Once all the other checks have been performed, if none of them are applicable, then check                                                    this setting.
            Setter for property DontConvertParameterLastResort
            Once all the other checks have been performed, if none of them are applicable, then check                                                    this setting.

            """
            pass
        @property
        def AddCelsiusToMissingParameters(self) -> bool:
            """
            Getter for property AddCelsiusToMissingParameters
            For some functions, if the parameter is missing the temperature dimension, then add Celsius.

            """
            pass
        @AddCelsiusToMissingParameters.setter
        def AddCelsiusToMissingParameters(self, value: bool):
            """
            Getter for property AddCelsiusToMissingParameters
            For some functions, if the parameter is missing the temperature dimension, then add Celsius.
            Setter for property AddCelsiusToMissingParameters
            For some functions, if the parameter is missing the temperature dimension, then add Celsius.

            """
            pass
    def AddDisplayToAbsoluteTemperatureFunction(definition: RulePreferences.AbsoluteTemperatureConversionDefinition) -> None:
        """
         Add a math function definition to control how the relative to obsolute temperature conversion is done. Must be done before opening the part. 
        """
        pass
    def GetSearchLibraries() -> List[str]:
        """
         Get the search libraries for user classes. 
         Returns user_libraries (List[str]):  search libraries .
        """
        pass
    def InitializeDisplayToAbsoluteTemperatureFunctionDefinition(definition: RulePreferences.AbsoluteTemperatureConversionDefinition) -> None:
        """
         Initialize definition to defaults. 
        """
        pass
    def SetSearchLibraries(user_libraries: List[str]) -> None:
        """
         Set the search libraries for user classes. 
        """
        pass
import NXOpen
class SectionViewPreferences(NXOpen.Object): 
    """ Represents set of Section View Preferences applicable to drafting views. """
    @property
    def AssemblyCrossHatching(self) -> bool:
        """
        Getter for property: (bool) AssemblyCrossHatching
         Returns the status of assembly cross hatching.  
           Controls the crosshatching angle
                    of adjacent solids in an assembly section view.  
                    Works when  Preferences::SectionViewPreferences::CrossHatch  is True.  
                   
         
        """
        pass
    @AssemblyCrossHatching.setter
    def AssemblyCrossHatching(self, assembly_cross_hatching: bool):
        """
        Setter for property: (bool) AssemblyCrossHatching
         Returns the status of assembly cross hatching.  
           Controls the crosshatching angle
                    of adjacent solids in an assembly section view.  
                    Works when  Preferences::SectionViewPreferences::CrossHatch  is True.  
                   
         
        """
        pass
    @property
    def Background(self) -> bool:
        """
        Getter for property: (bool) Background
         Returns the status of background.  
           Suppress or display the background curves for a section view. If True,
                    not only the curves and crosshatching generated by cutting the solid are displayed, 
                    but the curves behind the cutting plane are displayed as well. If False, only the curves and 
                    crosshatching generated by cutting the solid are displayed in the view.
                   
         
        """
        pass
    @Background.setter
    def Background(self, background: bool):
        """
        Setter for property: (bool) Background
         Returns the status of background.  
           Suppress or display the background curves for a section view. If True,
                    not only the curves and crosshatching generated by cutting the solid are displayed, 
                    but the curves behind the cutting plane are displayed as well. If False, only the curves and 
                    crosshatching generated by cutting the solid are displayed in the view.
                   
         
        """
        pass
    @property
    def Bendlines(self) -> bool:
        """
        Getter for property: (bool) Bendlines
         Returns the status of bendlines   
            
         
        """
        pass
    @Bendlines.setter
    def Bendlines(self, bendlines: bool):
        """
        Setter for property: (bool) Bendlines
         Returns the status of bendlines   
            
         
        """
        pass
    @property
    def CrossHatch(self) -> bool:
        """
        Getter for property: (bool) CrossHatch
         Returns the status of cross hatch.  
           Allows to control whether or not crosshatching is generated in 
                    a given section view. If True, crosshatching is displayed for a section view on the drawing, 
                    else crosshatching is not generated for a section view on the drawing, and a performance 
                    increase is gained.
                   
         
        """
        pass
    @CrossHatch.setter
    def CrossHatch(self, cross_hatch: bool):
        """
        Setter for property: (bool) CrossHatch
         Returns the status of cross hatch.  
           Allows to control whether or not crosshatching is generated in 
                    a given section view. If True, crosshatching is displayed for a section view on the drawing, 
                    else crosshatching is not generated for a section view on the drawing, and a performance 
                    increase is gained.
                   
         
        """
        pass
    @property
    def CrosshatchAdjacencyTolarance(self) -> float:
        """
        Getter for property: (float) CrosshatchAdjacencyTolarance
         Returns the value of crosshatch adjacency tolarance.  
           Controls the crosshatching angle of adjacent 
                    solids in an assembly section view.  
                    Works when  Preferences::SectionViewPreferences::AssemblyCrossHatching  is True.   
                   
         
        """
        pass
    @CrosshatchAdjacencyTolarance.setter
    def CrosshatchAdjacencyTolarance(self, crosshatch_adjacency_tolarance: float):
        """
        Setter for property: (float) CrosshatchAdjacencyTolarance
         Returns the value of crosshatch adjacency tolarance.  
           Controls the crosshatching angle of adjacent 
                    solids in an assembly section view.  
                    Works when  Preferences::SectionViewPreferences::AssemblyCrossHatching  is True.   
                   
         
        """
        pass
    @property
    def Foreground(self) -> bool:
        """
        Getter for property: (bool) Foreground
         Returns the status of foreground   
            
         
        """
        pass
    @Foreground.setter
    def Foreground(self, foreground: bool):
        """
        Setter for property: (bool) Foreground
         Returns the status of foreground   
            
         
        """
        pass
    @property
    def HiddenLineHatching(self) -> bool:
        """
        Getter for property: (bool) HiddenLineHatching
         Returns the status of hidden line hatching.  
           Controls whether hatching for a Break-Out
                    or Pictorial Section view participates in hidden line processing. When it is True for a break-out section view, 
                    the only hatch style available is iron (equally spaced solid lines).  
                    Works when  Preferences::SectionViewPreferences::CrossHatch  is True.  
                   
         
        """
        pass
    @HiddenLineHatching.setter
    def HiddenLineHatching(self, hidden_line_hatching: bool):
        """
        Setter for property: (bool) HiddenLineHatching
         Returns the status of hidden line hatching.  
           Controls whether hatching for a Break-Out
                    or Pictorial Section view participates in hidden line processing. When it is True for a break-out section view, 
                    the only hatch style available is iron (equally spaced solid lines).  
                    Works when  Preferences::SectionViewPreferences::CrossHatch  is True.  
                   
         
        """
        pass
    @property
    def RestrictCrosshatchAngle(self) -> bool:
        """
        Getter for property: (bool) RestrictCrosshatchAngle
         Returns the status of restrict crosshatch angle.  
           Restricts the crosshatch angle
                    of adjacent solids in an assembly section view.  
                    Works when  Preferences::SectionViewPreferences::AssemblyCrossHatching  is True.   
                   
         
        """
        pass
    @RestrictCrosshatchAngle.setter
    def RestrictCrosshatchAngle(self, restrict_crosshatch_angle: bool):
        """
        Setter for property: (bool) RestrictCrosshatchAngle
         Returns the status of restrict crosshatch angle.  
           Restricts the crosshatch angle
                    of adjacent solids in an assembly section view.  
                    Works when  Preferences::SectionViewPreferences::AssemblyCrossHatching  is True.   
                   
         
        """
        pass
    @property
    def SectionSheetBodies(self) -> bool:
        """
        Getter for property: (bool) SectionSheetBodies
         Returns the status of section sheet bodies.  
           Allows sectioning of sheet bodies in a Section view.   
         
        """
        pass
    @SectionSheetBodies.setter
    def SectionSheetBodies(self, section_sheet_bodies: bool):
        """
        Setter for property: (bool) SectionSheetBodies
         Returns the status of section sheet bodies.  
           Allows sectioning of sheet bodies in a Section view.   
         
        """
        pass
import NXOpen
class SessionAppearanceMgrPreference(NXOpen.Object): 
    """  Represents preferences for AppearanceManagement that are applicable
        to the session.  """
    @property
    def DispSceneLabels(self) -> bool:
        """
        Getter for property: (bool) DispSceneLabels
         Returns the objects in the scene assigned with appearance designators display with scene labels when the Appearance Designator dialog is up   
            
         
        """
        pass
    @DispSceneLabels.setter
    def DispSceneLabels(self, show_scene_lable: bool):
        """
        Setter for property: (bool) DispSceneLabels
         Returns the objects in the scene assigned with appearance designators display with scene labels when the Appearance Designator dialog is up   
            
         
        """
        pass
    @property
    def DispSeeThru(self) -> bool:
        """
        Getter for property: (bool) DispSeeThru
         Returns the objects in the scene assigned with appearance designators disply in see-thru when the Appearance Designator dialog is up   
            
         
        """
        pass
    @DispSeeThru.setter
    def DispSeeThru(self, show_see_through: bool):
        """
        Setter for property: (bool) DispSeeThru
         Returns the objects in the scene assigned with appearance designators disply in see-thru when the Appearance Designator dialog is up   
            
         
        """
        pass
    @property
    def ExcludeFromSelection(self) -> bool:
        """
        Getter for property: (bool) ExcludeFromSelection
         Returns the objects in the scene assigned with appearance designators display with scene labels when the Appearance Designator dialog is up   
            
         
        """
        pass
    @ExcludeFromSelection.setter
    def ExcludeFromSelection(self, exclude_from_selection: bool):
        """
        Setter for property: (bool) ExcludeFromSelection
         Returns the objects in the scene assigned with appearance designators display with scene labels when the Appearance Designator dialog is up   
            
         
        """
        pass
    def GetDirectoryOfStudioMaterial() -> str:
        """
         Get the directory of studio material 
         Returns studio_material_directory (str): .
        """
        pass
    def GetDirectoryOfTexture() -> str:
        """
         Get the directory of texture 
         Returns texture_dir (str): .
        """
        pass
    def SetDirectoryOfStudioMaterial(studio_material_directory: str) -> None:
        """
         Set the directory of studio material 
        """
        pass
    def SetDirectoryOfTexture(texture_dir: str) -> None:
        """
         Set the directory of texture 
        """
        pass
import NXOpen
class SessionAssemblies(NXOpen.Object): 
    """ Represents the set of Assemblies Preferences applicable to entire session """
    class DragHandlePositionOption(Enum):
        """
        Members Include: 
         |CenterOfBoundingBox|  
         |OriginOfComponent|  

        """
        CenterOfBoundingBox: int
        OriginOfComponent: int
        @staticmethod
        def ValueOf(value: int) -> SessionAssemblies.DragHandlePositionOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PartNameOption(Enum):
        """
        Members Include: 
         |FileName|  
         |Description|  
         |SpecifiedAttributes|  

        """
        FileName: int
        Description: int
        SpecifiedAttributes: int
        @staticmethod
        def ValueOf(value: int) -> SessionAssemblies.PartNameOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PositioningArrangementTargetOption(Enum):
        """
        Members Include: 
         |AllArrangements| 
         |ActiveArrangement| 

        """
        AllArrangements: int
        ActiveArrangement: int
        @staticmethod
        def ValueOf(value: int) -> SessionAssemblies.PositioningArrangementTargetOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PositioningTaskCollectionOptionForDesignElements(Enum):
        """
        Members Include: 
         |Work|  
         |Context|  

        """
        Work: int
        Context: int
        @staticmethod
        def ValueOf(value: int) -> SessionAssemblies.PositioningTaskCollectionOptionForDesignElements:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TemplateTypeOptionForNewAssemblyTemplate(Enum):
        """
        Members Include: 
         |Gateway| Use Gateway application type to identify a default template 
         |Assemblies| Use Assemblies application type to identify a default template 
         |SelectFromFileNew| Select template from File New dialog 

        """
        Gateway: int
        Assemblies: int
        SelectFromFileNew: int
        @staticmethod
        def ValueOf(value: int) -> SessionAssemblies.TemplateTypeOptionForNewAssemblyTemplate:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TemplateTypeOptionForNewComponentTemplate(Enum):
        """
        Members Include: 
         |Modeling| 
         |Gateway| Use Gateway application type to identify a default template 
         |Assemblies| Use Assemblies application type to identify a default template 
         |SelectFromFileNew| Select template from File New dialog 

        """
        Modeling: int
        Gateway: int
        Assemblies: int
        SelectFromFileNew: int
        @staticmethod
        def ValueOf(value: int) -> SessionAssemblies.TemplateTypeOptionForNewComponentTemplate:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TemplateTypeOptionForNewParentTemplate(Enum):
        """
        Members Include: 
         |Gateway|  Use Gateway application type to identify a default template 
         |Assemblies| Use Assemblies application type to identify a default template
         |SelectFromFile| Select template from File New dialog 

        """
        Gateway: int
        Assemblies: int
        SelectFromFile: int
        @staticmethod
        def ValueOf(value: int) -> SessionAssemblies.TemplateTypeOptionForNewParentTemplate:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CheckNewerRevisionsOfTemplatePart(self) -> bool:
        """
        Getter for property: (bool) CheckNewerRevisionsOfTemplatePart
         Returns the check for newer revisions of template part option   
            
         
        """
        pass
    @CheckNewerRevisionsOfTemplatePart.setter
    def CheckNewerRevisionsOfTemplatePart(self, check_newer_revisions_of_template_part: bool):
        """
        Setter for property: (bool) CheckNewerRevisionsOfTemplatePart
         Returns the check for newer revisions of template part option   
            
         
        """
        pass
    @property
    def ComponentMemberSelect(self) -> bool:
        """
        Getter for property: (bool) ComponentMemberSelect
         Returns the component member select option   
            
         
        """
        pass
    @ComponentMemberSelect.setter
    def ComponentMemberSelect(self, component_member_select: bool):
        """
        Setter for property: (bool) ComponentMemberSelect
         Returns the component member select option   
            
         
        """
        pass
    @property
    def CreatePersistentConstraints(self) -> bool:
        """
        Getter for property: (bool) CreatePersistentConstraints
         Returns the option that determines if assembly constraints are created persistent or not   
            
         
        """
        pass
    @CreatePersistentConstraints.setter
    def CreatePersistentConstraints(self, shouldCreatePersistentConstraints: bool):
        """
        Setter for property: (bool) CreatePersistentConstraints
         Returns the option that determines if assembly constraints are created persistent or not   
            
         
        """
        pass
    @property
    def DisplayUpdateReport(self) -> bool:
        """
        Getter for property: (bool) DisplayUpdateReport
         Returns the display update report option   
            
         
        """
        pass
    @DisplayUpdateReport.setter
    def DisplayUpdateReport(self, display_update_report: bool):
        """
        Setter for property: (bool) DisplayUpdateReport
         Returns the display update report option   
            
         
        """
        pass
    @property
    def DragHandlePositionPreference(self) -> SessionAssemblies.DragHandlePositionOption:
        """
        Getter for property: ( SessionAssemblies.DragHandlePositionOption NXOpen.P) DragHandlePositionPreference
         Returns the drag handle position preference   
            
         
        """
        pass
    @DragHandlePositionPreference.setter
    def DragHandlePositionPreference(self, dragHandlePosition: SessionAssemblies.DragHandlePositionOption):
        """
        Setter for property: ( SessionAssemblies.DragHandlePositionOption NXOpen.P) DragHandlePositionPreference
         Returns the drag handle position preference   
            
         
        """
        pass
    @property
    def InterpartPositioning(self) -> bool:
        """
        Getter for property: (bool) InterpartPositioning
         Returns the option to allow interpart geometry selection in the assembly constraints dialog   
            
         
        """
        pass
    @InterpartPositioning.setter
    def InterpartPositioning(self, allow_interpart_positioning: bool):
        """
        Setter for property: (bool) InterpartPositioning
         Returns the option to allow interpart geometry selection in the assembly constraints dialog   
            
         
        """
        pass
    @property
    def PartNameAttribute(self) -> str:
        """
        Getter for property: (str) PartNameAttribute
         Returns the part name attribute   
            
         
        """
        pass
    @PartNameAttribute.setter
    def PartNameAttribute(self, part_name_attribute: str):
        """
        Setter for property: (str) PartNameAttribute
         Returns the part name attribute   
            
         
        """
        pass
    @property
    def PartNameStyle(self) -> SessionAssemblies.PartNameOption:
        """
        Getter for property: ( SessionAssemblies.PartNameOption NXOpen.P) PartNameStyle
         Returns the part name style   
            
         
        """
        pass
    @PartNameStyle.setter
    def PartNameStyle(self, part_name_style: SessionAssemblies.PartNameOption):
        """
        Setter for property: ( SessionAssemblies.PartNameOption NXOpen.P) PartNameStyle
         Returns the part name style   
            
         
        """
        pass
    @property
    def PositioningArrangementTargetPreference(self) -> SessionAssemblies.PositioningArrangementTargetOption:
        """
        Getter for property: ( SessionAssemblies.PositioningArrangementTargetOption NXOpen.P) PositioningArrangementTargetPreference
         Returns the option that determines the arrangement target when creating new assembly constraints   
            
         
        """
        pass
    @PositioningArrangementTargetPreference.setter
    def PositioningArrangementTargetPreference(self, arrangementTarget: SessionAssemblies.PositioningArrangementTargetOption):
        """
        Setter for property: ( SessionAssemblies.PositioningArrangementTargetOption NXOpen.P) PositioningArrangementTargetPreference
         Returns the option that determines the arrangement target when creating new assembly constraints   
            
         
        """
        pass
    @property
    def PositioningTaskCollectionForDesignElements(self) -> SessionAssemblies.PositioningTaskCollectionOptionForDesignElements:
        """
        Getter for property: ( SessionAssemblies.PositioningTaskCollectionOptionForDesignElements NXOpen.P) PositioningTaskCollectionForDesignElements
         Returns the option to specify where to add Design Elements selected whilst working in the Assembly Constraints Dialog.  
          
                    The Design Elements will either be added to the Work or the Context collection of the Positioning Task.   
         
        """
        pass
    @PositioningTaskCollectionForDesignElements.setter
    def PositioningTaskCollectionForDesignElements(self, collection: SessionAssemblies.PositioningTaskCollectionOptionForDesignElements):
        """
        Setter for property: ( SessionAssemblies.PositioningTaskCollectionOptionForDesignElements NXOpen.P) PositioningTaskCollectionForDesignElements
         Returns the option to specify where to add Design Elements selected whilst working in the Assembly Constraints Dialog.  
          
                    The Design Elements will either be added to the Work or the Context collection of the Positioning Task.   
         
        """
        pass
    @property
    def PreviewComponentOnAdd(self) -> bool:
        """
        Getter for property: (bool) PreviewComponentOnAdd
         Returns the preview component on add option   
            
         
        """
        pass
    @PreviewComponentOnAdd.setter
    def PreviewComponentOnAdd(self, preview_component_on_add: bool):
        """
        Setter for property: (bool) PreviewComponentOnAdd
         Returns the preview component on add option   
            
         
        """
        pass
    @property
    def ProductInterfaceEmphasize(self) -> bool:
        """
        Getter for property: (bool) ProductInterfaceEmphasize
         Returns the product interface display emphasis setting   
            
         
        """
        pass
    @ProductInterfaceEmphasize.setter
    def ProductInterfaceEmphasize(self, product_interface_emphasize: bool):
        """
        Setter for property: (bool) ProductInterfaceEmphasize
         Returns the product interface display emphasis setting   
            
         
        """
        pass
    @property
    def SimplifyPrepopulate(self) -> bool:
        """
        Getter for property: (bool) SimplifyPrepopulate
         Returns the option to populate the Assembly Simplify dialog with visible solids on entry   
            
         
        """
        pass
    @SimplifyPrepopulate.setter
    def SimplifyPrepopulate(self, prepopulate: bool):
        """
        Setter for property: (bool) SimplifyPrepopulate
         Returns the option to populate the Assembly Simplify dialog with visible solids on entry   
            
         
        """
        pass
    @property
    def TemplateOptionForNewAssembly(self) -> SessionAssemblies.TemplateTypeOptionForNewAssemblyTemplate:
        """
        Getter for property: ( SessionAssemblies.TemplateTypeOptionForNewAssemblyTemplate NXOpen.P) TemplateOptionForNewAssembly
         Returns the option that determines template to be used for New Assembly  
            
         
        """
        pass
    @TemplateOptionForNewAssembly.setter
    def TemplateOptionForNewAssembly(self, templateOptionForNewAssembly: SessionAssemblies.TemplateTypeOptionForNewAssemblyTemplate):
        """
        Setter for property: ( SessionAssemblies.TemplateTypeOptionForNewAssemblyTemplate NXOpen.P) TemplateOptionForNewAssembly
         Returns the option that determines template to be used for New Assembly  
            
         
        """
        pass
    @property
    def TemplateOptionForNewComponent(self) -> SessionAssemblies.TemplateTypeOptionForNewComponentTemplate:
        """
        Getter for property: ( SessionAssemblies.TemplateTypeOptionForNewComponentTemplate NXOpen.P) TemplateOptionForNewComponent
         Returns the option that determines template to be used for New Component  
            
         
        """
        pass
    @TemplateOptionForNewComponent.setter
    def TemplateOptionForNewComponent(self, templateOptionForNewComponent: SessionAssemblies.TemplateTypeOptionForNewComponentTemplate):
        """
        Setter for property: ( SessionAssemblies.TemplateTypeOptionForNewComponentTemplate NXOpen.P) TemplateOptionForNewComponent
         Returns the option that determines template to be used for New Component  
            
         
        """
        pass
    @property
    def TemplateOptionForNewParent(self) -> SessionAssemblies.TemplateTypeOptionForNewParentTemplate:
        """
        Getter for property: ( SessionAssemblies.TemplateTypeOptionForNewParentTemplate NXOpen.P) TemplateOptionForNewParent
         Returns the option that determines template to be used for New Parent  
            
         
        """
        pass
    @TemplateOptionForNewParent.setter
    def TemplateOptionForNewParent(self, templateOptionForNewParent: SessionAssemblies.TemplateTypeOptionForNewParentTemplate):
        """
        Setter for property: ( SessionAssemblies.TemplateTypeOptionForNewParentTemplate NXOpen.P) TemplateOptionForNewParent
         Returns the option that determines template to be used for New Parent  
            
         
        """
        pass
    @property
    def TolerantPositioning(self) -> bool:
        """
        Getter for property: (bool) TolerantPositioning
         Returns the option to allow tolerant (imprecise) geometry selection for assembly positioning   
            
         
        """
        pass
    @TolerantPositioning.setter
    def TolerantPositioning(self, allow_tolerant_positioning: bool):
        """
        Setter for property: (bool) TolerantPositioning
         Returns the option to allow tolerant (imprecise) geometry selection for assembly positioning   
            
         
        """
        pass
    @property
    def TrueShapeFiltering(self) -> bool:
        """
        Getter for property: (bool) TrueShapeFiltering
         Returns the true shape filtering option   
            
         
        """
        pass
    @TrueShapeFiltering.setter
    def TrueShapeFiltering(self, true_shape_filtering: bool):
        """
        Setter for property: (bool) TrueShapeFiltering
         Returns the true shape filtering option   
            
         
        """
        pass
    @property
    def UpdateDesignElementPositionOnLoad(self) -> bool:
        """
        Getter for property: (bool) UpdateDesignElementPositionOnLoad
         Returns the option that enables automatic local positioning update of design elements  
            
         
        """
        pass
    @UpdateDesignElementPositionOnLoad.setter
    def UpdateDesignElementPositionOnLoad(self, update_design_element_position_on_load: bool):
        """
        Setter for property: (bool) UpdateDesignElementPositionOnLoad
         Returns the option that enables automatic local positioning update of design elements  
            
         
        """
        pass
    @property
    def UpdateStructureOnExpand(self) -> bool:
        """
        Getter for property: (bool) UpdateStructureOnExpand
         Returns the update structure on assembly tree expand option   
            
         
        """
        pass
    @UpdateStructureOnExpand.setter
    def UpdateStructureOnExpand(self, update_structure: bool):
        """
        Setter for property: (bool) UpdateStructureOnExpand
         Returns the update structure on assembly tree expand option   
            
         
        """
        pass
    @property
    def WarnOnDelete(self) -> bool:
        """
        Getter for property: (bool) WarnOnDelete
         Returns the warn on delete option   
            
         
        """
        pass
    @WarnOnDelete.setter
    def WarnOnDelete(self, work_on_delete: bool):
        """
        Setter for property: (bool) WarnOnDelete
         Returns the warn on delete option   
            
         
        """
        pass
    @property
    def WarnOnDragDrop(self) -> bool:
        """
        Getter for property: (bool) WarnOnDragDrop
         Returns the warn on drag and drop   
            
         
        """
        pass
    @WarnOnDragDrop.setter
    def WarnOnDragDrop(self, warn_on_drag_drop: bool):
        """
        Setter for property: (bool) WarnOnDragDrop
         Returns the warn on drag and drop   
            
         
        """
        pass
    @property
    def WorkPartDisplayAsEntirePart(self) -> bool:
        """
        Getter for property: (bool) WorkPartDisplayAsEntirePart
         Returns the work part display as entire part option   
            
         
        """
        pass
    @WorkPartDisplayAsEntirePart.setter
    def WorkPartDisplayAsEntirePart(self, work_part_display_as_entire_part: bool):
        """
        Setter for property: (bool) WorkPartDisplayAsEntirePart
         Returns the work part display as entire part option   
            
         
        """
        pass
    @property
    def WorkPartEmphasize(self) -> bool:
        """
        Getter for property: (bool) WorkPartEmphasize
         Returns the emphasize for work part    
            
         
        """
        pass
    @WorkPartEmphasize.setter
    def WorkPartEmphasize(self, work_part_emphasize: bool):
        """
        Setter for property: (bool) WorkPartEmphasize
         Returns the emphasize for work part    
            
         
        """
        pass
    @property
    def WorkPartMaintain(self) -> bool:
        """
        Getter for property: (bool) WorkPartMaintain
         Returns the work part maintain option   
            
         
        """
        pass
    @WorkPartMaintain.setter
    def WorkPartMaintain(self, work_part_maintain: bool):
        """
        Setter for property: (bool) WorkPartMaintain
         Returns the work part maintain option   
            
         
        """
        pass
    @property
    def WorkPartWarnOnAutomaticChange(self) -> bool:
        """
        Getter for property: (bool) WorkPartWarnOnAutomaticChange
         Returns the warn on automatic change for work part option   
            
         
        """
        pass
    @WorkPartWarnOnAutomaticChange.setter
    def WorkPartWarnOnAutomaticChange(self, work_part_warn_on_automatic_change: bool):
        """
        Setter for property: (bool) WorkPartWarnOnAutomaticChange
         Returns the warn on automatic change for work part option   
            
         
        """
        pass
import NXOpen
class SessionDrafting(NXOpen.Object): 
    """ Represents the set of Drafting preferences applicable to entire session"""
    class AnnotationStyleType(Enum):
        """
        Members Include: 
         |TextboxAndLeaders|   
         |Detailed|   

        """
        TextboxAndLeaders: int
        Detailed: int
        @staticmethod
        def ValueOf(value: int) -> SessionDrafting.AnnotationStyleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EdgeFaceDisplayType(Enum):
        """
        Members Include: 
         |DisplayAndEmphasize|   
         |CurvesOnly|   

        """
        DisplayAndEmphasize: int
        CurvesOnly: int
        @staticmethod
        def ValueOf(value: int) -> SessionDrafting.EdgeFaceDisplayType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class GridObjectType(Enum):
        """
        Members Include: 
         |Drafting|  Drafting Grid  
         |Sketch|  Sketch Grid 
         |Sheetzone|  Sheet Zone Grid 

        """
        Drafting: int
        Sketch: int
        Sheetzone: int
        @staticmethod
        def ValueOf(value: int) -> SessionDrafting.GridObjectType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AutomaticCustomSymbolUpdate(self) -> bool:
        """
        Getter for property: (bool) AutomaticCustomSymbolUpdate
         Returns the automatic update drafting preferences for custom symbol   
            
         
        """
        pass
    @AutomaticCustomSymbolUpdate.setter
    def AutomaticCustomSymbolUpdate(self, automaticUpdateOption: bool):
        """
        Setter for property: (bool) AutomaticCustomSymbolUpdate
         Returns the automatic update drafting preferences for custom symbol   
            
         
        """
        pass
    @property
    def DynamicAlignment(self) -> bool:
        """
        Getter for property: (bool) DynamicAlignment
         Returns the dynamic alignment flag.  
             
         
        """
        pass
    @DynamicAlignment.setter
    def DynamicAlignment(self, dynamic_alignment: bool):
        """
        Setter for property: (bool) DynamicAlignment
         Returns the dynamic alignment flag.  
             
         
        """
        pass
    @property
    def ExtractedEdgeFaceDisplay(self) -> SessionDrafting.EdgeFaceDisplayType:
        """
        Getter for property: ( SessionDrafting.EdgeFaceDisplayType NXOpen.P) ExtractedEdgeFaceDisplay
         Returns the extracted edge face display   
            
         
        """
        pass
    @ExtractedEdgeFaceDisplay.setter
    def ExtractedEdgeFaceDisplay(self, extracted_edge_face_display: SessionDrafting.EdgeFaceDisplayType):
        """
        Setter for property: ( SessionDrafting.EdgeFaceDisplayType NXOpen.P) ExtractedEdgeFaceDisplay
         Returns the extracted edge face display   
            
         
        """
        pass
    @property
    def ForcedWelcomeMode(self) -> int:
        """
        Getter for property: (int) ForcedWelcomeMode
         Returns the Drafting Welcome mode, for autotests only   
            
         
        """
        pass
    @ForcedWelcomeMode.setter
    def ForcedWelcomeMode(self, enter_welcome_mode: int):
        """
        Setter for property: (int) ForcedWelcomeMode
         Returns the Drafting Welcome mode, for autotests only   
            
         
        """
        pass
    @property
    def GridObject(self) -> SessionDrafting.GridObjectType:
        """
        Getter for property: ( SessionDrafting.GridObjectType NXOpen.P) GridObject
         Returns the drafting grid object.  
             
         
        """
        pass
    @GridObject.setter
    def GridObject(self, drawing_grid_object: SessionDrafting.GridObjectType):
        """
        Setter for property: ( SessionDrafting.GridObjectType NXOpen.P) GridObject
         Returns the drafting grid object.  
             
         
        """
        pass
    @property
    def LoadComponentOnFacetedViewSelection(self) -> bool:
        """
        Getter for property: (bool) LoadComponentOnFacetedViewSelection
         Returns the load on selection flag   
            
         
        """
        pass
    @LoadComponentOnFacetedViewSelection.setter
    def LoadComponentOnFacetedViewSelection(self, load_component_on_faceted_view_selection: bool):
        """
        Setter for property: (bool) LoadComponentOnFacetedViewSelection
         Returns the load on selection flag   
            
         
        """
        pass
    @property
    def LoadComponentOnFacetedViewUpdate(self) -> bool:
        """
        Getter for property: (bool) LoadComponentOnFacetedViewUpdate
         Returns the load on update flag   
            
         
        """
        pass
    @LoadComponentOnFacetedViewUpdate.setter
    def LoadComponentOnFacetedViewUpdate(self, load_component_on_faceted_view_update: bool):
        """
        Setter for property: (bool) LoadComponentOnFacetedViewUpdate
         Returns the load on update flag   
            
         
        """
        pass
    @property
    def SmartlightweightViewsLoadComponentOnDemand(self) -> bool:
        """
        Getter for property: (bool) SmartlightweightViewsLoadComponentOnDemand
         Returns the load on demand flag   
            
         
        """
        pass
    @SmartlightweightViewsLoadComponentOnDemand.setter
    def SmartlightweightViewsLoadComponentOnDemand(self, load_component_on_demand: bool):
        """
        Setter for property: (bool) SmartlightweightViewsLoadComponentOnDemand
         Returns the load on demand flag   
            
         
        """
        pass
import NXOpen
class SessionMeasureRequirements(NXOpen.Object): 
    """ Represents the two options available on the Measure Requirements toolbar and applicable to the entire session """
    class ActionOnViolation(Enum):
        """
        Members Include: 
         |HightlightMeasure|  Highlight (color) measure for requirements violations 
         |StopPlayback|  Suspend playback and wait for acknowledgement for requirements violations 

        """
        HightlightMeasure: int
        StopPlayback: int
        @staticmethod
        def ValueOf(value: int) -> SessionMeasureRequirements.ActionOnViolation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def UpdateFrameRate(self) -> int:
        """
        Getter for property: (int) UpdateFrameRate
         Returns the frame rate.  
            The frame rate specifies how frequently a displayed measure annotation is updated in Assembly Sequencing.
        So a rate of 1 specifies that the annotation will update every frame during playback.
        A rate of 5 specifies that the annotation will update every fifth frame during playback.   
         
        """
        pass
    @UpdateFrameRate.setter
    def UpdateFrameRate(self, frame_rate: int):
        """
        Setter for property: (int) UpdateFrameRate
         Returns the frame rate.  
            The frame rate specifies how frequently a displayed measure annotation is updated in Assembly Sequencing.
        So a rate of 1 specifies that the annotation will update every frame during playback.
        A rate of 5 specifies that the annotation will update every fifth frame during playback.   
         
        """
        pass
    @property
    def ViolationAction(self) -> SessionMeasureRequirements.ActionOnViolation:
        """
        Getter for property: ( SessionMeasureRequirements.ActionOnViolation NXOpen.P) ViolationAction
         Returns the violation action.  
            The violation action is one of the enumerated type values.   
         
        """
        pass
    @ViolationAction.setter
    def ViolationAction(self, violation_action: SessionMeasureRequirements.ActionOnViolation):
        """
        Setter for property: ( SessionMeasureRequirements.ActionOnViolation NXOpen.P) ViolationAction
         Returns the violation action.  
            The violation action is one of the enumerated type values.   
         
        """
        pass
import NXOpen
class SessionModeling(NXOpen.Object): 
    """ Represents the set of Modeling preferences applicable to entire session"""
    class BodyTypeOption(Enum):
        """
        Members Include: 
         |Solid|  Indicates Body Type is solid  
         |Sheet|  Indicates Body Type is solid 

        """
        Solid: int
        Sheet: int
        @staticmethod
        def ValueOf(value: int) -> SessionModeling.BodyTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class BooleanFacePropertiesInheritance(Enum):
        """
        Members Include: 
         |TargetBody|  Indicates that display of boolean face properties inherits from target body 
         |ToolBody|  Indicates that display of boolean face properties inherits from tool body 

        """
        TargetBody: int
        ToolBody: int
        @staticmethod
        def ValueOf(value: int) -> SessionModeling.BooleanFacePropertiesInheritance:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CurveFitMethodType(Enum):
        """
        Members Include: 
         |Cubic|  Indicates the Curve Fit Method type is cubic 
         |Quintic|  Indicates the Curve Fit Method type is quintic 
         |Advanced|  Indicates the Curve Fit Method type is advanced 

        """
        Cubic: int
        Quintic: int
        Advanced: int
        @staticmethod
        def ValueOf(value: int) -> SessionModeling.CurveFitMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DeleteChildFeaturesOptionType(Enum):
        """
        Members Include: 
         |Yes|  Delete child features including recipe curves, of a feature being deleted 
         |No|  Do not delete child features of feature being deleted 
         |Ask|  Ask user "Do you want to delete child features?" 

        """
        Yes: int
        No: int
        Ask: int
        @staticmethod
        def ValueOf(value: int) -> SessionModeling.DeleteChildFeaturesOptionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DynamicUpdateType(Enum):
        """
        Members Include: 
         |NotSet|  Indicates that Dynamic Update type is not selected, this option is deprecated from NX12.0 
         |Incremental|  Indicates that Dynamic Update type is incremental
         |Continuous|  Indicates that Dynamic Update type is continuous 

        """
        NotSet: int
        Incremental: int
        Continuous: int
        @staticmethod
        def ValueOf(value: int) -> SessionModeling.DynamicUpdateType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EndpointDisplayStyleType(Enum):
        """
        Members Include: 
         |OpenCircle|  
         |FilledCircle|  
         |PlusSign|  
         |Cross|  
         |Point|  
         |Asterisk|  
         |PoundSign|  
         |FilledSquare|  
         |FilledTriangle|  
         |FilledDiamond|  
         |Centerline|  

        """
        OpenCircle: int
        FilledCircle: int
        PlusSign: int
        Cross: int
        Point: int
        Asterisk: int
        PoundSign: int
        FilledSquare: int
        FilledTriangle: int
        FilledDiamond: int
        Centerline: int
        @staticmethod
        def ValueOf(value: int) -> SessionModeling.EndpointDisplayStyleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FreeFormConstructionResultType(Enum):
        """
        Members Include: 
         |Plane|  Indicates the construction result option is plane  
         |BSurface|  Indicates the construction result option is B Surface  

        """
        Plane: int
        BSurface: int
        @staticmethod
        def ValueOf(value: int) -> SessionModeling.FreeFormConstructionResultType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ImmediateChildrenType(Enum):
        """
        Members Include: 
         |FirstLevel|  Indicates that Immediate Children type is at first level 
         |All|  Indicates that Immediate Children type is at all level  

        """
        FirstLevel: int
        All: int
        @staticmethod
        def ValueOf(value: int) -> SessionModeling.ImmediateChildrenType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LinkedAndExtractedGeometryPropertiesInheritance(Enum):
        """
        Members Include: 
         |ParentObject|  Indicates that display of linked and extracted geometry properties inherits from parent object  
         |PartDefault|  Indicates that display of linked and extracted geometry properties inherits from part default 

        """
        ParentObject: int
        PartDefault: int
        @staticmethod
        def ValueOf(value: int) -> SessionModeling.LinkedAndExtractedGeometryPropertiesInheritance:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ModelDelayUpdateGranilarityType(Enum):
        """
        Members Include: 
         |Group|  Delay dependents from other group, group includes design group and part modules 
         |Feature|  Delay immediate dependents 

        """
        Group: int
        Feature: int
        @staticmethod
        def ValueOf(value: int) -> SessionModeling.ModelDelayUpdateGranilarityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class NewFacePropertiesInheritance(Enum):
        """
        Members Include: 
         |Body|  Indicates that display of new face properties inherits from body  
         |PartDefault|  Indicates that display of new face properties inherits from part default 

        """
        Body: int
        PartDefault: int
        @staticmethod
        def ValueOf(value: int) -> SessionModeling.NewFacePropertiesInheritance:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PoleDisplayStyleType(Enum):
        """
        Members Include: 
         |NotSet|  
         |OpenCircle|  
         |FilledCircle|  
         |PlusSign|  
         |Cross|  

        """
        NotSet: int
        OpenCircle: int
        FilledCircle: int
        PlusSign: int
        Cross: int
        @staticmethod
        def ValueOf(value: int) -> SessionModeling.PoleDisplayStyleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PoleEditStyleType(Enum):
        """
        Members Include: 
         |Sphere3d|  
         |OpenCircle|  
         |FilledCircle|  
         |PlusSign|  
         |Cross|  

        """
        Sphere3d: int
        OpenCircle: int
        FilledCircle: int
        PlusSign: int
        Cross: int
        @staticmethod
        def ValueOf(value: int) -> SessionModeling.PoleEditStyleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PolylineStyleType(Enum):
        """
        Members Include: 
         |Solid|  
         |Dashed|  
         |Phantom|  
         |Centerline|  
         |Dotted|  
         |Longdashed|  
         |Dotteddashed|  
         |Eight|  Long Dashed Double Dotted 
         |Nine|  Long Dashed Dotted for OOTB fonts and Undulating for shipbuilding fonts 
         |Ten|  Long Dashed Triplicate Dotted for OOTB fonts and Zigzag for shipbuilding fonts 
         |Eleven|  Long Dashed Double Short Dashed for OOTB fonts and Railway for shipbuilding fonts 

        """
        Solid: int
        Dashed: int
        Phantom: int
        Centerline: int
        Dotted: int
        Longdashed: int
        Dotteddashed: int
        Eight: int
        Nine: int
        Ten: int
        Eleven: int
        @staticmethod
        def ValueOf(value: int) -> SessionModeling.PolylineStyleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PreviewResolutionType(Enum):
        """
        Members Include: 
         |NotSet|  
         |Coarse|  
         |Standard|  
         |Fine|  
         |ExtraFine|  
         |SuperFine|  
         |UltraFine|  

        """
        NotSet: int
        Coarse: int
        Standard: int
        Fine: int
        ExtraFine: int
        SuperFine: int
        UltraFine: int
        @staticmethod
        def ValueOf(value: int) -> SessionModeling.PreviewResolutionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SaveDataForFeatureEditOption(Enum):
        """
        Members Include: 
         |NotSet|  Indicates the no additional data is saved 
         |FastRollback|  Indicates the additional parasolid data is saved for faster rollback 
         |FastRollbackAndPreviousStateOfFailedFeature|  Indicates the additional parasolid data is saved for faster rollback and to show the previous state of failed feature 

        """
        NotSet: int
        FastRollback: int
        FastRollbackAndPreviousStateOfFailedFeature: int
        @staticmethod
        def ValueOf(value: int) -> SessionModeling.SaveDataForFeatureEditOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ShareGeometriesOnSaveType(Enum):
        """
        Members Include: 
         |DontShare| 
         |Share| 

        """
        DontShare: int
        Share: int
        @staticmethod
        def ValueOf(value: int) -> SessionModeling.ShareGeometriesOnSaveType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SketchDefaultActionType(Enum):
        """
        Members Include: 
         |EditWithRollback|  Edit sketch with rollback on double click 
         |Edit|  Edit sketch without rollback on double click 

        """
        EditWithRollback: int
        Edit: int
        @staticmethod
        def ValueOf(value: int) -> SessionModeling.SketchDefaultActionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SketchEditType(Enum):
        """
        Members Include: 
         |InTaskEnvironment|  Edit sketch in task environment 
         |Direct|  Edit sketch without entering task environment 

        """
        InTaskEnvironment: int
        Direct: int
        @staticmethod
        def ValueOf(value: int) -> SessionModeling.SketchEditType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SplineDefaultActionTypes(Enum):
        """
        Members Include: 
         |StudioSpline|  Specifies Studio Spline for editing a spline 
         |Xform|  Specifies X-form for editing a spline 

        """
        StudioSpline: int
        Xform: int
        @staticmethod
        def ValueOf(value: int) -> SessionModeling.SplineDefaultActionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SurfaceExtensionOption(Enum):
        """
        Members Include: 
         |Linear|  
         |Soft|  
         |Reflective|  
         |Natural|  
         |Arc|  

        """
        Linear: int
        Soft: int
        Reflective: int
        Natural: int
        Arc: int
        @staticmethod
        def ValueOf(value: int) -> SessionModeling.SurfaceExtensionOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AccelerationColor(self) -> int:
        """
        Getter for property: (int) AccelerationColor
         Returns the acceleration color   
            
         
        """
        pass
    @AccelerationColor.setter
    def AccelerationColor(self, acceleration_color: int):
        """
        Setter for property: (int) AccelerationColor
         Returns the acceleration color   
            
         
        """
        pass
    @property
    def ActivateFeatureGroupWithRollback(self) -> bool:
        """
        Getter for property: (bool) ActivateFeatureGroupWithRollback
         Returns the flag to activate the feature group with rollback or not, if the flag is true, the highest member feature will be made as current feature  
            
         
        """
        pass
    @ActivateFeatureGroupWithRollback.setter
    def ActivateFeatureGroupWithRollback(self, activateFeatureGroupWithRollback: bool):
        """
        Setter for property: (bool) ActivateFeatureGroupWithRollback
         Returns the flag to activate the feature group with rollback or not, if the flag is true, the highest member feature will be made as current feature  
            
         
        """
        pass
    @property
    def AllowEditingOfDimensionOfInternalSketch(self) -> bool:
        """
        Getter for property: (bool) AllowEditingOfDimensionOfInternalSketch
         Returns the option "allow_editing_of_dimension_of_internal_sketch" gives choice, 
             whether or not the sketch dimensions will display and be possible to select and edit directly, 
             without entering the Sketch task environment when a dialog (e.  
          g. Extrude, Revolve, Hole etc.) is active 
             which allows editing on an internal sketch.  
         
        """
        pass
    @AllowEditingOfDimensionOfInternalSketch.setter
    def AllowEditingOfDimensionOfInternalSketch(self, allow_editing_of_dimension_of_internal_sketch: bool):
        """
        Setter for property: (bool) AllowEditingOfDimensionOfInternalSketch
         Returns the option "allow_editing_of_dimension_of_internal_sketch" gives choice, 
             whether or not the sketch dimensions will display and be possible to select and edit directly, 
             without entering the Sketch task environment when a dialog (e.  
          g. Extrude, Revolve, Hole etc.) is active 
             which allows editing on an internal sketch.  
         
        """
        pass
    @property
    def AssociativeEditFreeForm(self) -> bool:
        """
        Getter for property: (bool) AssociativeEditFreeForm
         Returns the associative edit free form option.  
           Specify whether the output of editing certain free form features remain 
            as free form features or as unparameterized features.   
         
        """
        pass
    @AssociativeEditFreeForm.setter
    def AssociativeEditFreeForm(self, associative_edit_free_form: bool):
        """
        Setter for property: (bool) AssociativeEditFreeForm
         Returns the associative edit free form option.  
           Specify whether the output of editing certain free form features remain 
            as free form features or as unparameterized features.   
         
        """
        pass
    @property
    def BodyType(self) -> SessionModeling.BodyTypeOption:
        """
        Getter for property: ( SessionModeling.BodyTypeOption NXOpen.P) BodyType
         Returns the body type.  
           Toggles between Solid and Sheet. When creating bodies through curves, the Body Type option provides
             control to the type of body (for example, solid body vs. sheet body) that is created.   
         
        """
        pass
    @BodyType.setter
    def BodyType(self, body_type: SessionModeling.BodyTypeOption):
        """
        Setter for property: ( SessionModeling.BodyTypeOption NXOpen.P) BodyType
         Returns the body type.  
           Toggles between Solid and Sheet. When creating bodies through curves, the Body Type option provides
             control to the type of body (for example, solid body vs. sheet body) that is created.   
         
        """
        pass
    @property
    def BooleanFaceProperties(self) -> SessionModeling.BooleanFacePropertiesInheritance:
        """
        Getter for property: ( SessionModeling.BooleanFacePropertiesInheritance NXOpen.P) BooleanFaceProperties
         Returns the boolean face properties inheritance.  
           Specifies whether the boolean face properties inherit from target body or tool body   
         
        """
        pass
    @BooleanFaceProperties.setter
    def BooleanFaceProperties(self, boolean_face_properties: SessionModeling.BooleanFacePropertiesInheritance):
        """
        Setter for property: ( SessionModeling.BooleanFacePropertiesInheritance NXOpen.P) BooleanFaceProperties
         Returns the boolean face properties inheritance.  
           Specifies whether the boolean face properties inherit from target body or tool body   
         
        """
        pass
    @property
    def ConvertAnalyticToConvergentAngularTolerance(self) -> float:
        """
        Getter for property: (float) ConvertAnalyticToConvergentAngularTolerance
         Returns the angular tolerance for converting analytic body to Convergent body   
            
         
        """
        pass
    @ConvertAnalyticToConvergentAngularTolerance.setter
    def ConvertAnalyticToConvergentAngularTolerance(self, dAnalyticToConvergentAngTol: float):
        """
        Setter for property: (float) ConvertAnalyticToConvergentAngularTolerance
         Returns the angular tolerance for converting analytic body to Convergent body   
            
         
        """
        pass
    @property
    def ConvertAnalyticToConvergentDistanceTolerance(self) -> float:
        """
        Getter for property: (float) ConvertAnalyticToConvergentDistanceTolerance
         Returns the distance tolerance for converting analytic body to Convergent body   
            
         
        """
        pass
    @ConvertAnalyticToConvergentDistanceTolerance.setter
    def ConvertAnalyticToConvergentDistanceTolerance(self, dAnalyticToConvergentDistTol: float):
        """
        Setter for property: (float) ConvertAnalyticToConvergentDistanceTolerance
         Returns the distance tolerance for converting analytic body to Convergent body   
            
         
        """
        pass
    @property
    def CurvatureColor(self) -> int:
        """
        Getter for property: (int) CurvatureColor
         Returns the curvature color   
            
         
        """
        pass
    @CurvatureColor.setter
    def CurvatureColor(self, curvature_color: int):
        """
        Setter for property: (int) CurvatureColor
         Returns the curvature color   
            
         
        """
        pass
    @property
    def CurveFitMethod(self) -> SessionModeling.CurveFitMethodType:
        """
        Getter for property: ( SessionModeling.CurveFitMethodType NXOpen.P) CurveFitMethod
         Returns the curve fit method.  
           Controls the fitting method used when curves must be approximated by splines.   
         
        """
        pass
    @CurveFitMethod.setter
    def CurveFitMethod(self, body_type: SessionModeling.CurveFitMethodType):
        """
        Setter for property: ( SessionModeling.CurveFitMethodType NXOpen.P) CurveFitMethod
         Returns the curve fit method.  
           Controls the fitting method used when curves must be approximated by splines.   
         
        """
        pass
    @property
    def DelayModelUpdates(self) -> bool:
        """
        Getter for property: (bool) DelayModelUpdates
         Returns the delay model updates option.  
            
         
        """
        pass
    @property
    def DeleteChildFeaturesOption(self) -> SessionModeling.DeleteChildFeaturesOptionType:
        """
        Getter for property: ( SessionModeling.DeleteChildFeaturesOptionType NXOpen.P) DeleteChildFeaturesOption
         Returns the delete child features options     
            
         
        """
        pass
    @DeleteChildFeaturesOption.setter
    def DeleteChildFeaturesOption(self, deleteChildFeatureOption: SessionModeling.DeleteChildFeaturesOptionType):
        """
        Setter for property: ( SessionModeling.DeleteChildFeaturesOptionType NXOpen.P) DeleteChildFeaturesOption
         Returns the delete child features options     
            
         
        """
        pass
    @property
    def DisplayLegacyFeatureName(self) -> bool:
        """
        Getter for property: (bool) DisplayLegacyFeatureName
         Returns the toggle "Display Legacy Feature names" gives choice, how user wants feature name in "Name" Coulmn in Partnav
             checked toggled(True) will show old feature names in "Name" column in Partnav, while
             unchecked toggled(False) will show new translatable feature names in "Name" column in Partnav  
            
         
        """
        pass
    @DisplayLegacyFeatureName.setter
    def DisplayLegacyFeatureName(self, display_legacy_feature_name: bool):
        """
        Setter for property: (bool) DisplayLegacyFeatureName
         Returns the toggle "Display Legacy Feature names" gives choice, how user wants feature name in "Name" Coulmn in Partnav
             checked toggled(True) will show old feature names in "Name" column in Partnav, while
             unchecked toggled(False) will show new translatable feature names in "Name" column in Partnav  
            
         
        """
        pass
    @property
    def DynamicUpdate(self) -> SessionModeling.DynamicUpdateType:
        """
        Getter for property: ( SessionModeling.DynamicUpdateType NXOpen.P) DynamicUpdate
         Returns the dynamic update.  
           Specifies that the system dynamically displays in real time with each 
            updation of parent curves, splines, bridge curves, lines or arcs   
         
        """
        pass
    @DynamicUpdate.setter
    def DynamicUpdate(self, dynamic_update: SessionModeling.DynamicUpdateType):
        """
        Setter for property: ( SessionModeling.DynamicUpdateType NXOpen.P) DynamicUpdate
         Returns the dynamic update.  
           Specifies that the system dynamically displays in real time with each 
            updation of parent curves, splines, bridge curves, lines or arcs   
         
        """
        pass
    @property
    def EditWithRollbackUponDoubleClick(self) -> bool:
        """
        Getter for property: (bool) EditWithRollbackUponDoubleClick
         Returns the option "Edit with Rollback upon Double-Click" gives choice of what action to 
            be taken on feature upon Double clicking, either in partnavigator or in Graphics widow.  
          
            if the option is true then edit with rollback will be happen upon Double-click.
            if the option is false then the previous default action will be executed   
         
        """
        pass
    @EditWithRollbackUponDoubleClick.setter
    def EditWithRollbackUponDoubleClick(self, default_edit_option: bool):
        """
        Setter for property: (bool) EditWithRollbackUponDoubleClick
         Returns the option "Edit with Rollback upon Double-Click" gives choice of what action to 
            be taken on feature upon Double clicking, either in partnavigator or in Graphics widow.  
          
            if the option is true then edit with rollback will be happen upon Double-click.
            if the option is false then the previous default action will be executed   
         
        """
        pass
    @property
    def EnableTrimmedAnimation(self) -> bool:
        """
        Getter for property: (bool) EnableTrimmedAnimation
         Returns the enable trimmed animation setting.  
             
         
        """
        pass
    @EnableTrimmedAnimation.setter
    def EnableTrimmedAnimation(self, enable: bool):
        """
        Setter for property: (bool) EnableTrimmedAnimation
         Returns the enable trimmed animation setting.  
             
         
        """
        pass
    @property
    def EndpointDisplayColor(self) -> int:
        """
        Getter for property: (int) EndpointDisplayColor
         Returns the color for display endpoints for curves.  
             
         
        """
        pass
    @EndpointDisplayColor.setter
    def EndpointDisplayColor(self, endpoint_display_color: int):
        """
        Setter for property: (int) EndpointDisplayColor
         Returns the color for display endpoints for curves.  
             
         
        """
        pass
    @property
    def EndpointDisplayInheritColor(self) -> bool:
        """
        Getter for property: (bool) EndpointDisplayInheritColor
         Returns the endpoint color inherit option, for display with curves.  
             
         
        """
        pass
    @EndpointDisplayInheritColor.setter
    def EndpointDisplayInheritColor(self, endpoint_display_inherit_color: bool):
        """
        Setter for property: (bool) EndpointDisplayInheritColor
         Returns the endpoint color inherit option, for display with curves.  
             
         
        """
        pass
    @property
    def EndpointDisplayStyle(self) -> SessionModeling.EndpointDisplayStyleType:
        """
        Getter for property: ( SessionModeling.EndpointDisplayStyleType NXOpen.P) EndpointDisplayStyle
         Returns the style (2D disk, mark, etc.  
          ) of the endpoints for display of curves.   
         
        """
        pass
    @EndpointDisplayStyle.setter
    def EndpointDisplayStyle(self, endpoint_display_style: SessionModeling.EndpointDisplayStyleType):
        """
        Setter for property: ( SessionModeling.EndpointDisplayStyleType NXOpen.P) EndpointDisplayStyle
         Returns the style (2D disk, mark, etc.  
          ) of the endpoints for display of curves.   
         
        """
        pass
    @property
    def FreeFormConstructionResult(self) -> SessionModeling.FreeFormConstructionResultType:
        """
        Getter for property: ( SessionModeling.FreeFormConstructionResultType NXOpen.P) FreeFormConstructionResult
         Returns the free form construction result.  
           Controls free form feature creation when using the Through Curves, Through 
            Curve Mesh, Swept, and Ruled options.   
         
        """
        pass
    @FreeFormConstructionResult.setter
    def FreeFormConstructionResult(self, free_form_constr_result: SessionModeling.FreeFormConstructionResultType):
        """
        Setter for property: ( SessionModeling.FreeFormConstructionResultType NXOpen.P) FreeFormConstructionResult
         Returns the free form construction result.  
           Controls free form feature creation when using the Through Curves, Through 
            Curve Mesh, Swept, and Ruled options.   
         
        """
        pass
    @property
    def ImmediateChildren(self) -> SessionModeling.ImmediateChildrenType:
        """
        Getter for property: ( SessionModeling.ImmediateChildrenType NXOpen.P) ImmediateChildren
         Returns the immediate children.  
           Specifies to which level the dynamic updation is applicable.   
         
        """
        pass
    @ImmediateChildren.setter
    def ImmediateChildren(self, immediate_children: SessionModeling.ImmediateChildrenType):
        """
        Setter for property: ( SessionModeling.ImmediateChildrenType NXOpen.P) ImmediateChildren
         Returns the immediate children.  
           Specifies to which level the dynamic updation is applicable.   
         
        """
        pass
    @property
    def InterruptUpdateOnError(self) -> bool:
        """
        Getter for property: (bool) InterruptUpdateOnError
         Returns the option "Interrupt Update on Error" gives choice, whether the user 
             wants the "Edit During Update" dialog to appear when features contain 
             errors during feature updateplayback.  
          
             if the option is true then the dialog will appear.
             if the option is false then dialog will not appear during feature update.  
         
        """
        pass
    @InterruptUpdateOnError.setter
    def InterruptUpdateOnError(self, interrupt_on_error: bool):
        """
        Setter for property: (bool) InterruptUpdateOnError
         Returns the option "Interrupt Update on Error" gives choice, whether the user 
             wants the "Edit During Update" dialog to appear when features contain 
             errors during feature updateplayback.  
          
             if the option is true then the dialog will appear.
             if the option is false then dialog will not appear during feature update.  
         
        """
        pass
    @property
    def InterruptUpdateOnMissingReferences(self) -> bool:
        """
        Getter for property: (bool) InterruptUpdateOnMissingReferences
         Returns the option "Interrupt Update on Missing References" gives choice, whether the
             user wants the "Edit During Update" dialog to appear when features contain 
             missing references during feature updateplayback.  
          
             if the option is true then the dialog will appear.
             if the option is false then dialog will not appear during feature update.  
         
        """
        pass
    @InterruptUpdateOnMissingReferences.setter
    def InterruptUpdateOnMissingReferences(self, interrupt_on_missing_references: bool):
        """
        Setter for property: (bool) InterruptUpdateOnMissingReferences
         Returns the option "Interrupt Update on Missing References" gives choice, whether the
             user wants the "Edit During Update" dialog to appear when features contain 
             missing references during feature updateplayback.  
          
             if the option is true then the dialog will appear.
             if the option is false then dialog will not appear during feature update.  
         
        """
        pass
    @property
    def InterruptUpdateOnWarning(self) -> bool:
        """
        Getter for property: (bool) InterruptUpdateOnWarning
         Returns the option "Interrupt Update on Warning" gives choice, whether the
             user wants the "Edit During Update" dialog to appear when features contain 
             warnings during feature updateplayback.  
          
             if the option is true then the dialog will appear.
             if the option is false then dialog will not appear during feature update.  
         
        """
        pass
    @InterruptUpdateOnWarning.setter
    def InterruptUpdateOnWarning(self, interrupt_on_warning: bool):
        """
        Setter for property: (bool) InterruptUpdateOnWarning
         Returns the option "Interrupt Update on Warning" gives choice, whether the
             user wants the "Edit During Update" dialog to appear when features contain 
             warnings during feature updateplayback.  
          
             if the option is true then the dialog will appear.
             if the option is false then dialog will not appear during feature update.  
         
        """
        pass
    @property
    def LinkedAndExtractedGeometryProperties(self) -> SessionModeling.LinkedAndExtractedGeometryPropertiesInheritance:
        """
        Getter for property: ( SessionModeling.LinkedAndExtractedGeometryPropertiesInheritance NXOpen.P) LinkedAndExtractedGeometryProperties
         Returns the linked and extracted geometry properties inheritance.  
           Specifies whether linked and extracted geometry properties inherits from parent object or part default   
         
        """
        pass
    @LinkedAndExtractedGeometryProperties.setter
    def LinkedAndExtractedGeometryProperties(self, linked_and_extracted_geometry_properties: SessionModeling.LinkedAndExtractedGeometryPropertiesInheritance):
        """
        Setter for property: ( SessionModeling.LinkedAndExtractedGeometryPropertiesInheritance NXOpen.P) LinkedAndExtractedGeometryProperties
         Returns the linked and extracted geometry properties inheritance.  
           Specifies whether linked and extracted geometry properties inherits from parent object or part default   
         
        """
        pass
    @property
    def MakeCurrentOnError(self) -> bool:
        """
        Getter for property: (bool) MakeCurrentOnError
         Returns the option "Make Current on Error" gives choice, whether the user 
             wants to make error feature current when features contain 
             errors during feature updateplayback.  
          
             If the option is true then the error feature will be made
             current.
             If the option is false then the error feature will not be made current feature
              during feature update.  
         
        """
        pass
    @MakeCurrentOnError.setter
    def MakeCurrentOnError(self, current_on_error: bool):
        """
        Setter for property: (bool) MakeCurrentOnError
         Returns the option "Make Current on Error" gives choice, whether the user 
             wants to make error feature current when features contain 
             errors during feature updateplayback.  
          
             If the option is true then the error feature will be made
             current.
             If the option is false then the error feature will not be made current feature
              during feature update.  
         
        """
        pass
    @property
    def MakeDatumsInternal(self) -> bool:
        """
        Getter for property: (bool) MakeDatumsInternal
         Returns the option specifying whether to automatically make the datums internal during  
             the sketch creation.  
           If the option is true then datums are automatically made internal to child sketches, else
             datums are not automatically made internal to child sketches.   
         
        """
        pass
    @MakeDatumsInternal.setter
    def MakeDatumsInternal(self, makeDatumsInternal: bool):
        """
        Setter for property: (bool) MakeDatumsInternal
         Returns the option specifying whether to automatically make the datums internal during  
             the sketch creation.  
           If the option is true then datums are automatically made internal to child sketches, else
             datums are not automatically made internal to child sketches.   
         
        """
        pass
    @property
    def MakeSketchesInternal(self) -> bool:
        """
        Getter for property: (bool) MakeSketchesInternal
         Returns the option specifying whether to automatically make sketch internal during  
             feature creation.  
           If the option is true then external sketches are automatically made internal to child features, else
             external sketches are not automatically made internal to child features.   
         
        """
        pass
    @MakeSketchesInternal.setter
    def MakeSketchesInternal(self, makeSketchesInternal: bool):
        """
        Setter for property: (bool) MakeSketchesInternal
         Returns the option specifying whether to automatically make sketch internal during  
             feature creation.  
           If the option is true then external sketches are automatically made internal to child features, else
             external sketches are not automatically made internal to child features.   
         
        """
        pass
    @property
    def ModelDelayUpdateGranilarity(self) -> SessionModeling.ModelDelayUpdateGranilarityType:
        """
        Getter for property: ( SessionModeling.ModelDelayUpdateGranilarityType NXOpen.P) ModelDelayUpdateGranilarity
         Returns the option that determines granularity if model delay   
            
         
        """
        pass
    @property
    def NewFaceProperties(self) -> SessionModeling.NewFacePropertiesInheritance:
        """
        Getter for property: ( SessionModeling.NewFacePropertiesInheritance NXOpen.P) NewFaceProperties
         Returns the new face properties inheritance.  
           Specifies whether new face properties inherits from body or part default   
         
        """
        pass
    @NewFaceProperties.setter
    def NewFaceProperties(self, new_face_properties: SessionModeling.NewFacePropertiesInheritance):
        """
        Setter for property: ( SessionModeling.NewFacePropertiesInheritance NXOpen.P) NewFaceProperties
         Returns the new face properties inheritance.  
           Specifies whether new face properties inherits from body or part default   
         
        """
        pass
    @property
    def NotifyOnDelete(self) -> bool:
        """
        Getter for property: (bool) NotifyOnDelete
         Returns the option " Notify on Delete " gives choice, whether the user wants a 
             notification message when a feature is being deleted will effect other features.  
          
             if the option is true then it popup a notification message.
             if the option is false then it will not popup any notification message   
         
        """
        pass
    @NotifyOnDelete.setter
    def NotifyOnDelete(self, notify_on_delete: bool):
        """
        Setter for property: (bool) NotifyOnDelete
         Returns the option " Notify on Delete " gives choice, whether the user wants a 
             notification message when a feature is being deleted will effect other features.  
          
             if the option is true then it popup a notification message.
             if the option is false then it will not popup any notification message   
         
        """
        pass
    @property
    def PoleDisplayColor(self) -> int:
        """
        Getter for property: (int) PoleDisplayColor
         Returns the color for display poles for B curves.  
             
         
        """
        pass
    @PoleDisplayColor.setter
    def PoleDisplayColor(self, pole_display_color: int):
        """
        Setter for property: (int) PoleDisplayColor
         Returns the color for display poles for B curves.  
             
         
        """
        pass
    @property
    def PoleDisplayInheritColor(self) -> bool:
        """
        Getter for property: (bool) PoleDisplayInheritColor
         Returns the pole color inherit option, for display with B curves.  
             
         
        """
        pass
    @PoleDisplayInheritColor.setter
    def PoleDisplayInheritColor(self, pole_display_inherit_color: bool):
        """
        Setter for property: (bool) PoleDisplayInheritColor
         Returns the pole color inherit option, for display with B curves.  
             
         
        """
        pass
    @property
    def PoleDisplayStyle(self) -> SessionModeling.PoleDisplayStyleType:
        """
        Getter for property: ( SessionModeling.PoleDisplayStyleType NXOpen.P) PoleDisplayStyle
         Returns the style (3D ball, 2D disk, mark, etc.  
          ) of the poles for display of B curves.   
         
        """
        pass
    @PoleDisplayStyle.setter
    def PoleDisplayStyle(self, pole_display_style: SessionModeling.PoleDisplayStyleType):
        """
        Setter for property: ( SessionModeling.PoleDisplayStyleType NXOpen.P) PoleDisplayStyle
         Returns the style (3D ball, 2D disk, mark, etc.  
          ) of the poles for display of B curves.   
         
        """
        pass
    @property
    def PoleEditColor(self) -> int:
        """
        Getter for property: (int) PoleEditColor
         Returns the color for editing poles for B curves and B surfaces.  
             
         
        """
        pass
    @PoleEditColor.setter
    def PoleEditColor(self, pole_edit_color: int):
        """
        Setter for property: (int) PoleEditColor
         Returns the color for editing poles for B curves and B surfaces.  
             
         
        """
        pass
    @property
    def PoleEditInheritColor(self) -> bool:
        """
        Getter for property: (bool) PoleEditInheritColor
         Returns the pole color inherit option, for editing B curves and B surfaces.  
             
         
        """
        pass
    @PoleEditInheritColor.setter
    def PoleEditInheritColor(self, pole_edit_inherit_color: bool):
        """
        Setter for property: (bool) PoleEditInheritColor
         Returns the pole color inherit option, for editing B curves and B surfaces.  
             
         
        """
        pass
    @property
    def PoleEditStyle(self) -> SessionModeling.PoleEditStyleType:
        """
        Getter for property: ( SessionModeling.PoleEditStyleType NXOpen.P) PoleEditStyle
         Returns the style (3D ball, 2D disk, mark, etc.  
          ) of the poles for editing B curves and B surfaces.   
         
        """
        pass
    @PoleEditStyle.setter
    def PoleEditStyle(self, pole_edit_style: SessionModeling.PoleEditStyleType):
        """
        Setter for property: ( SessionModeling.PoleEditStyleType NXOpen.P) PoleEditStyle
         Returns the style (3D ball, 2D disk, mark, etc.  
          ) of the poles for editing B curves and B surfaces.   
         
        """
        pass
    @property
    def PolylineDisplayColor(self) -> int:
        """
        Getter for property: (int) PolylineDisplayColor
         Returns the color for display polylines for B curves and B surfaces   
            
         
        """
        pass
    @PolylineDisplayColor.setter
    def PolylineDisplayColor(self, polyline_display_color: int):
        """
        Setter for property: (int) PolylineDisplayColor
         Returns the color for display polylines for B curves and B surfaces   
            
         
        """
        pass
    @property
    def PolylineDisplayInheritColor(self) -> bool:
        """
        Getter for property: (bool) PolylineDisplayInheritColor
         Returns the polyline color inherit option, for display with B curves and B surfaces.  
             
         
        """
        pass
    @PolylineDisplayInheritColor.setter
    def PolylineDisplayInheritColor(self, polyline_display_inherit_color: bool):
        """
        Setter for property: (bool) PolylineDisplayInheritColor
         Returns the polyline color inherit option, for display with B curves and B surfaces.  
             
         
        """
        pass
    @property
    def PolylineDisplayStyle(self) -> SessionModeling.PolylineStyleType:
        """
        Getter for property: ( SessionModeling.PolylineStyleType NXOpen.P) PolylineDisplayStyle
         Returns the style (solid, dashed, etc.  
          ) of the polylines display for B curves and B surfaces.   
         
        """
        pass
    @PolylineDisplayStyle.setter
    def PolylineDisplayStyle(self, polyline_display_style: SessionModeling.PolylineStyleType):
        """
        Setter for property: ( SessionModeling.PolylineStyleType NXOpen.P) PolylineDisplayStyle
         Returns the style (solid, dashed, etc.  
          ) of the polylines display for B curves and B surfaces.   
         
        """
        pass
    @property
    def PolylineEditColor(self) -> int:
        """
        Getter for property: (int) PolylineEditColor
         Returns the color for editing polylines for B curves and B surfaces.  
             
         
        """
        pass
    @PolylineEditColor.setter
    def PolylineEditColor(self, polyline_edit_color: int):
        """
        Setter for property: (int) PolylineEditColor
         Returns the color for editing polylines for B curves and B surfaces.  
             
         
        """
        pass
    @property
    def PolylineEditInheritColor(self) -> bool:
        """
        Getter for property: (bool) PolylineEditInheritColor
         Returns the polyline color inherit option, for editing B curves and B surfaces.  
             
         
        """
        pass
    @PolylineEditInheritColor.setter
    def PolylineEditInheritColor(self, polyline_edit_inherit_color: bool):
        """
        Setter for property: (bool) PolylineEditInheritColor
         Returns the polyline color inherit option, for editing B curves and B surfaces.  
             
         
        """
        pass
    @property
    def PolylineEditStyle(self) -> SessionModeling.PolylineStyleType:
        """
        Getter for property: ( SessionModeling.PolylineStyleType NXOpen.P) PolylineEditStyle
         Returns the style (solid, dashed, etc.  
          ) of the polylines for editing B curves and B surfaces.   
         
        """
        pass
    @PolylineEditStyle.setter
    def PolylineEditStyle(self, polyline_edit_style: SessionModeling.PolylineStyleType):
        """
        Setter for property: ( SessionModeling.PolylineStyleType NXOpen.P) PolylineEditStyle
         Returns the style (solid, dashed, etc.  
          ) of the polylines for editing B curves and B surfaces.   
         
        """
        pass
    @property
    def PositionColor(self) -> int:
        """
        Getter for property: (int) PositionColor
         Returns the position color   
            
         
        """
        pass
    @PositionColor.setter
    def PositionColor(self, position_color: int):
        """
        Setter for property: (int) PositionColor
         Returns the position color   
            
         
        """
        pass
    @property
    def PreviewResolution(self) -> SessionModeling.PreviewResolutionType:
        """
        Getter for property: ( SessionModeling.PreviewResolutionType NXOpen.P) PreviewResolution
         Returns the preview resolution setting.  
             
         
        """
        pass
    @PreviewResolution.setter
    def PreviewResolution(self, resolution: SessionModeling.PreviewResolutionType):
        """
        Setter for property: ( SessionModeling.PreviewResolutionType NXOpen.P) PreviewResolution
         Returns the preview resolution setting.  
             
         
        """
        pass
    @property
    def SaveDataForFeatureEdit(self) -> SessionModeling.SaveDataForFeatureEditOption:
        """
        Getter for property: ( SessionModeling.SaveDataForFeatureEditOption NXOpen.P) SaveDataForFeatureEdit
         Returns the option "Save Data for Feature Edit" specifies what additional data will 
                 be saved in the part to enhance feature edit.  
           Rollback data improves feature 
                 edit performance. Previous state data is a copy of a face or body input to a 
                 feature for visual reference while editing a failed feature.   
         
        """
        pass
    @SaveDataForFeatureEdit.setter
    def SaveDataForFeatureEdit(self, save_data_for_feature_edit: SessionModeling.SaveDataForFeatureEditOption):
        """
        Setter for property: ( SessionModeling.SaveDataForFeatureEditOption NXOpen.P) SaveDataForFeatureEdit
         Returns the option "Save Data for Feature Edit" specifies what additional data will 
                 be saved in the part to enhance feature edit.  
           Rollback data improves feature 
                 edit performance. Previous state data is a copy of a face or body input to a 
                 feature for visual reference while editing a failed feature.   
         
        """
        pass
    @property
    def ShareGeometriesOption(self) -> SessionModeling.ShareGeometriesOnSaveType:
        """
        Getter for property: ( SessionModeling.ShareGeometriesOnSaveType NXOpen.P) ShareGeometriesOption
         Returns the option " Share Geometry on Save " gives choice of whether to share geometries among Parasolid solid entities on save or not   
            
         
        """
        pass
    @ShareGeometriesOption.setter
    def ShareGeometriesOption(self, share_geometry_on_save: SessionModeling.ShareGeometriesOnSaveType):
        """
        Setter for property: ( SessionModeling.ShareGeometriesOnSaveType NXOpen.P) ShareGeometriesOption
         Returns the option " Share Geometry on Save " gives choice of whether to share geometries among Parasolid solid entities on save or not   
            
         
        """
        pass
    @property
    def ShowSimuationUiInModeling(self) -> bool:
        """
        Getter for property: (bool) ShowSimuationUiInModeling
         Returns the option to specify whether simulation specific UI should show up in modeling   
            
         
        """
        pass
    @ShowSimuationUiInModeling.setter
    def ShowSimuationUiInModeling(self, show_simuation_ui_in_modeling: bool):
        """
        Setter for property: (bool) ShowSimuationUiInModeling
         Returns the option to specify whether simulation specific UI should show up in modeling   
            
         
        """
        pass
    @property
    def SketchDefaultAction(self) -> SessionModeling.SketchDefaultActionType:
        """
        Getter for property: ( SessionModeling.SketchDefaultActionType NXOpen.P) SketchDefaultAction
         Returns the sketch default action   
            
         
        """
        pass
    @SketchDefaultAction.setter
    def SketchDefaultAction(self, sketchAction: SessionModeling.SketchDefaultActionType):
        """
        Setter for property: ( SessionModeling.SketchDefaultActionType NXOpen.P) SketchDefaultAction
         Returns the sketch default action   
            
         
        """
        pass
    @property
    def SketchEditOption(self) -> SessionModeling.SketchEditType:
        """
        Getter for property: ( SessionModeling.SketchEditType NXOpen.P) SketchEditOption
         Returns the option that determines whether or not task environment is used to edit the sketch   
            
         
        """
        pass
    @SketchEditOption.setter
    def SketchEditOption(self, sketchEditOption: SessionModeling.SketchEditType):
        """
        Setter for property: ( SessionModeling.SketchEditType NXOpen.P) SketchEditOption
         Returns the option that determines whether or not task environment is used to edit the sketch   
            
         
        """
        pass
    @property
    def SplineDefaultActionType(self) -> SessionModeling.SplineDefaultActionTypes:
        """
        Getter for property: ( SessionModeling.SplineDefaultActionTypes NXOpen.P) SplineDefaultActionType
         Returns the value indicating the default action for a spline.  
             
         
        """
        pass
    @SplineDefaultActionType.setter
    def SplineDefaultActionType(self, action: SessionModeling.SplineDefaultActionTypes):
        """
        Setter for property: ( SessionModeling.SplineDefaultActionTypes NXOpen.P) SplineDefaultActionType
         Returns the value indicating the default action for a spline.  
             
         
        """
        pass
    @property
    def SurfaceExtension(self) -> SessionModeling.SurfaceExtensionOption:
        """
        Getter for property: ( SessionModeling.SurfaceExtensionOption NXOpen.P) SurfaceExtension
         Returns the surface extension option.  
           Controls how surfaces will be extended while moving geometry   
         
        """
        pass
    @SurfaceExtension.setter
    def SurfaceExtension(self, surfaceExtensionOption: SessionModeling.SurfaceExtensionOption):
        """
        Setter for property: ( SessionModeling.SurfaceExtensionOption NXOpen.P) SurfaceExtension
         Returns the surface extension option.  
           Controls how surfaces will be extended while moving geometry   
         
        """
        pass
    @property
    def TangentColor(self) -> int:
        """
        Getter for property: (int) TangentColor
         Returns the tangent color   
            
         
        """
        pass
    @TangentColor.setter
    def TangentColor(self, tangent_color: int):
        """
        Setter for property: (int) TangentColor
         Returns the tangent color   
            
         
        """
        pass
    @property
    def TreatOneDegreeBsplineAsPolyline(self) -> bool:
        """
        Getter for property: (bool) TreatOneDegreeBsplineAsPolyline
         Returns the option to treat single degree bspline as polyline   
            
         
        """
        pass
    @TreatOneDegreeBsplineAsPolyline.setter
    def TreatOneDegreeBsplineAsPolyline(self, preference: bool):
        """
        Setter for property: (bool) TreatOneDegreeBsplineAsPolyline
         Returns the option to treat single degree bspline as polyline   
            
         
        """
        pass
    @property
    def UpdateDelayed(self) -> bool:
        """
        Getter for property: (bool) UpdateDelayed
         Returns the update delayed option.  
            If the option is true, then an edited
            feature does not update until  NXOpen::Update::DoUpdate  is
            explicitly called.  If the option is false, then the edited feature
            updates immediately.  The default is false.   
         
        """
        pass
    @UpdateDelayed.setter
    def UpdateDelayed(self, option: bool):
        """
        Setter for property: (bool) UpdateDelayed
         Returns the update delayed option.  
            If the option is true, then an edited
            feature does not update until  NXOpen::Update::DoUpdate  is
            explicitly called.  If the option is false, then the edited feature
            updates immediately.  The default is false.   
         
        """
        pass
    @property
    def UpdateFailureReportPreference(self) -> bool:
        """
        Getter for property: (bool) UpdateFailureReportPreference
         Returns the option "Update Failure Report" gives choice, whether the
             user wants the update failure report to be generated for the features that 
             failed during current update cycle.  
          
             If the option is true then the update failure report will be launched at the end
             of every update cycle. It will list only those features that failed in that update 
             cycle. If the option is false then no such report will be launched.  
         
        """
        pass
    @UpdateFailureReportPreference.setter
    def UpdateFailureReportPreference(self, update_failure_report: bool):
        """
        Setter for property: (bool) UpdateFailureReportPreference
         Returns the option "Update Failure Report" gives choice, whether the
             user wants the update failure report to be generated for the features that 
             failed during current update cycle.  
          
             If the option is true then the update failure report will be launched at the end
             of every update cycle. It will list only those features that failed in that update 
             cycle. If the option is false then no such report will be launched.  
         
        """
        pass
    @property
    def UpdatePending(self) -> bool:
        """
        Getter for property: (bool) UpdatePending
         Returns the update pending option.  
           This option only works when the NXOpen::Preferences::SessionModeling::UpdateDelayed option is true.
            If the option is true, there is an edited feature to be updated till  NXOpen::Update::DoUpdate  is explicitly called.  
            If the option is false, there is not an edited feature to be updated. The default is false.   
         
        """
        pass
    @UpdatePending.setter
    def UpdatePending(self, option: bool):
        """
        Setter for property: (bool) UpdatePending
         Returns the update pending option.  
           This option only works when the NXOpen::Preferences::SessionModeling::UpdateDelayed option is true.
            If the option is true, there is an edited feature to be updated till  NXOpen::Update::DoUpdate  is explicitly called.  
            If the option is false, there is not an edited feature to be updated. The default is false.   
         
        """
        pass
    @property
    def UseTriangularMesh(self) -> bool:
        """
        Getter for property: (bool) UseTriangularMesh
         Returns the use triangular mesh setting setting.  
             
         
        """
        pass
    @UseTriangularMesh.setter
    def UseTriangularMesh(self, use: bool):
        """
        Setter for property: (bool) UseTriangularMesh
         Returns the use triangular mesh setting setting.  
             
         
        """
        pass
    def GetShowSymbolicThreadDecalSticker() -> bool:
        """
         Get the flag to show symbolic thread decal sticker 
         Returns showSymbolicThreadDecalSticker (bool):   .
        """
        pass
    def SetDelayModelUpdatesAndGranularity(delay_model_updates: bool, modelDelayUpdateGranularityOption: SessionModeling.ModelDelayUpdateGranilarityType, undoMarkId: int) -> None:
        """
         
        """
        pass
    def SetShowSymbolicThreadDecalSticker(showSymbolicThreadDecalSticker: bool) -> None:
        """
         Set the flag to show symbolic thread decal sticker 
        """
        pass
import NXOpen
class SessionNavigation(NXOpen.Object): 
    """ Represents the set of navigation preferences applicable to entire session.
      """
    class PerspectiveStatusOnExit(Enum):
        """
        Members Include: 
         |Retain|  Retains the perspective view when exiting fly-through 
         |RevertToPreviousState|  Reverts the perspective view to the state it had before entering fly-through 

        """
        Retain: int
        RevertToPreviousState: int
        @staticmethod
        def ValueOf(value: int) -> SessionNavigation.PerspectiveStatusOnExit:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AdaptiveSpeed(self) -> bool:
        """
        Getter for property: (bool) AdaptiveSpeed
         Returns the adaptive speed.  
           If adaptive speed is toggled on, gradually slows down the navigation 
                    speed when approaching a reference location and gradually speeds up the navigation speed 
                    when moving away from a reference location. A reference location is a point coordinate 
                    derived from setting the persistent Rotation Reference (e.g., snapping to a point on face).    
         
        """
        pass
    @AdaptiveSpeed.setter
    def AdaptiveSpeed(self, adaptiveSpeed: bool):
        """
        Setter for property: (bool) AdaptiveSpeed
         Returns the adaptive speed.  
           If adaptive speed is toggled on, gradually slows down the navigation 
                    speed when approaching a reference location and gradually speeds up the navigation speed 
                    when moving away from a reference location. A reference location is a point coordinate 
                    derived from setting the persistent Rotation Reference (e.g., snapping to a point on face).    
         
        """
        pass
    @property
    def NavigationSpeed(self) -> float:
        """
        Getter for property: (float) NavigationSpeed
         Returns the navigation speed.  
           The higher the value, the faster the speed of the navigation.   
         
        """
        pass
    @NavigationSpeed.setter
    def NavigationSpeed(self, navigationSpeed: float):
        """
        Setter for property: (float) NavigationSpeed
         Returns the navigation speed.  
           The higher the value, the faster the speed of the navigation.   
         
        """
        pass
    @property
    def PerspectiveOnFlyThoughExit(self) -> SessionNavigation.PerspectiveStatusOnExit:
        """
        Getter for property: ( SessionNavigation.PerspectiveStatusOnExit NXOpen.P) PerspectiveOnFlyThoughExit
         Returns the perspective on exit.  
           These states mean: Retains the perspective view when exiting fly-through, or
                   reverts the perspective view to the state it had before entering fly-through.  
         
        """
        pass
    @PerspectiveOnFlyThoughExit.setter
    def PerspectiveOnFlyThoughExit(self, perspectiveOnExit: SessionNavigation.PerspectiveStatusOnExit):
        """
        Setter for property: ( SessionNavigation.PerspectiveStatusOnExit NXOpen.P) PerspectiveOnFlyThoughExit
         Returns the perspective on exit.  
           These states mean: Retains the perspective view when exiting fly-through, or
                   reverts the perspective view to the state it had before entering fly-through.  
         
        """
        pass
import NXOpen
class SessionNXGateway(NXOpen.Object): 
    """ Represents the set of NXGateway Preferences applicable to entire session """
    @property
    def AngularTolerance(self) -> float:
        """
        Getter for property: (float) AngularTolerance
         Returns the angular tolerance.  
           One of the heal geometry option for I-DEAS import   
         
        """
        pass
    @AngularTolerance.setter
    def AngularTolerance(self, angular_tolerance: float):
        """
        Setter for property: (float) AngularTolerance
         Returns the angular tolerance.  
           One of the heal geometry option for I-DEAS import   
         
        """
        pass
    @property
    def AttachFidelityCheckData(self) -> bool:
        """
        Getter for property: (bool) AttachFidelityCheckData
         Returns the attach FC data flag for I-DEAS gateway   
            
         
        """
        pass
    @AttachFidelityCheckData.setter
    def AttachFidelityCheckData(self, attach_fidelity_check_data: bool):
        """
        Setter for property: (bool) AttachFidelityCheckData
         Returns the attach FC data flag for I-DEAS gateway   
            
         
        """
        pass
    @property
    def AutomaticallyCheckItemRevisions(self) -> bool:
        """
        Getter for property: (bool) AutomaticallyCheckItemRevisions
         Returns the automatically checking of items revision flag for I-DEAS import   
            
         
        """
        pass
    @AutomaticallyCheckItemRevisions.setter
    def AutomaticallyCheckItemRevisions(self, automatically_check_item_revisions: bool):
        """
        Setter for property: (bool) AutomaticallyCheckItemRevisions
         Returns the automatically checking of items revision flag for I-DEAS import   
            
         
        """
        pass
    @property
    def HealGeometryOnImport(self) -> bool:
        """
        Getter for property: (bool) HealGeometryOnImport
         Returns the heal geometry on import flag for I-DEAS import   
            
         
        """
        pass
    @HealGeometryOnImport.setter
    def HealGeometryOnImport(self, heal_geometry_on_import: bool):
        """
        Setter for property: (bool) HealGeometryOnImport
         Returns the heal geometry on import flag for I-DEAS import   
            
         
        """
        pass
    @property
    def IgnoreUpdateOfIdenticalVersions(self) -> bool:
        """
        Getter for property: (bool) IgnoreUpdateOfIdenticalVersions
         Returns the ignore update of identical versions flag for I-DEAS   
            
         
        """
        pass
    @IgnoreUpdateOfIdenticalVersions.setter
    def IgnoreUpdateOfIdenticalVersions(self, ignore_update_of_identical_versions: bool):
        """
        Setter for property: (bool) IgnoreUpdateOfIdenticalVersions
         Returns the ignore update of identical versions flag for I-DEAS   
            
         
        """
        pass
    @property
    def LoadConstructionGeometry(self) -> bool:
        """
        Getter for property: (bool) LoadConstructionGeometry
         Returns the load construction geometry flag for I-DEAS   
            
         
        """
        pass
    @LoadConstructionGeometry.setter
    def LoadConstructionGeometry(self, load_construction_geometry: bool):
        """
        Setter for property: (bool) LoadConstructionGeometry
         Returns the load construction geometry flag for I-DEAS   
            
         
        """
        pass
    @property
    def LoadProductManufacturingInformation(self) -> bool:
        """
        Getter for property: (bool) LoadProductManufacturingInformation
         Returns the load product manufacturing information flag for I-DEAS   
            
         
        """
        pass
    @LoadProductManufacturingInformation.setter
    def LoadProductManufacturingInformation(self, load_product_manufacturing_information: bool):
        """
        Setter for property: (bool) LoadProductManufacturingInformation
         Returns the load product manufacturing information flag for I-DEAS   
            
         
        """
        pass
    @property
    def LoadSolidEdgeAssemblyFeatures(self) -> bool:
        """
        Getter for property: (bool) LoadSolidEdgeAssemblyFeatures
         Returns the Assembly-level features flag for Solid Edge   
            
         
        """
        pass
    @LoadSolidEdgeAssemblyFeatures.setter
    def LoadSolidEdgeAssemblyFeatures(self, load_assembly_features: bool):
        """
        Setter for property: (bool) LoadSolidEdgeAssemblyFeatures
         Returns the Assembly-level features flag for Solid Edge   
            
         
        """
        pass
    @property
    def LoadSolidEdgeConstructionGeometry(self) -> bool:
        """
        Getter for property: (bool) LoadSolidEdgeConstructionGeometry
         Returns the load construction geometry flag for Solid Edge   
            
         
        """
        pass
    @LoadSolidEdgeConstructionGeometry.setter
    def LoadSolidEdgeConstructionGeometry(self, load_construction_geometry: bool):
        """
        Setter for property: (bool) LoadSolidEdgeConstructionGeometry
         Returns the load construction geometry flag for Solid Edge   
            
         
        """
        pass
    @property
    def LoadSolidEdgeProductManufacturingInformation(self) -> bool:
        """
        Getter for property: (bool) LoadSolidEdgeProductManufacturingInformation
         Returns the load product manufacturing information flag for Solid Edge   
            
         
        """
        pass
    @LoadSolidEdgeProductManufacturingInformation.setter
    def LoadSolidEdgeProductManufacturingInformation(self, load_product_manufacturing_information: bool):
        """
        Setter for property: (bool) LoadSolidEdgeProductManufacturingInformation
         Returns the load product manufacturing information flag for Solid Edge   
            
         
        """
        pass
    @property
    def MinimumSmallEdgeLength(self) -> float:
        """
        Getter for property: (float) MinimumSmallEdgeLength
         Returns the minimum small edge length.  
           One of the heal geometry option for I-DEAS import   
         
        """
        pass
    @MinimumSmallEdgeLength.setter
    def MinimumSmallEdgeLength(self, minimum_small_edge_length: float):
        """
        Setter for property: (float) MinimumSmallEdgeLength
         Returns the minimum small edge length.  
           One of the heal geometry option for I-DEAS import   
         
        """
        pass
    @property
    def OnlyImportDesignParts(self) -> bool:
        """
        Getter for property: (bool) OnlyImportDesignParts
         Returns the only import design parts flag for Solid Edge.  
           It is under Solid Edge Gateway preferences   
         
        """
        pass
    @OnlyImportDesignParts.setter
    def OnlyImportDesignParts(self, only_import_design_parts: bool):
        """
        Setter for property: (bool) OnlyImportDesignParts
         Returns the only import design parts flag for Solid Edge.  
           It is under Solid Edge Gateway preferences   
         
        """
        pass
    @property
    def PerformFidelityCheckOnImport(self) -> bool:
        """
        Getter for property: (bool) PerformFidelityCheckOnImport
         Returns the perform fidelity check on import flag for I-DEAS   
            
         
        """
        pass
    @PerformFidelityCheckOnImport.setter
    def PerformFidelityCheckOnImport(self, perform_fidelity_check_on_import: bool):
        """
        Setter for property: (bool) PerformFidelityCheckOnImport
         Returns the perform fidelity check on import flag for I-DEAS   
            
         
        """
        pass
    @property
    def PreserveNominalGeometry(self) -> bool:
        """
        Getter for property: (bool) PreserveNominalGeometry
         Returns the preserve nominal geometry flag.  
           One of the heal geometry option for I-DEAS import   
         
        """
        pass
    @PreserveNominalGeometry.setter
    def PreserveNominalGeometry(self, preserve_nominal_geometry: bool):
        """
        Setter for property: (bool) PreserveNominalGeometry
         Returns the preserve nominal geometry flag.  
           One of the heal geometry option for I-DEAS import   
         
        """
        pass
    @property
    def ReferenceGeometryImportColor(self) -> int:
        """
        Getter for property: (int) ReferenceGeometryImportColor
         Returns the reference geometry import color for I-DEAS   
            
         
        """
        pass
    @ReferenceGeometryImportColor.setter
    def ReferenceGeometryImportColor(self, reference_geometry_import_color: int):
        """
        Setter for property: (int) ReferenceGeometryImportColor
         Returns the reference geometry import color for I-DEAS   
            
         
        """
        pass
    @property
    def ReferenceGeometryImportLayer(self) -> int:
        """
        Getter for property: (int) ReferenceGeometryImportLayer
         Returns the reference geometry import layer for I-DEAS    
            
         
        """
        pass
    @ReferenceGeometryImportLayer.setter
    def ReferenceGeometryImportLayer(self, reference_geometry_import_layer: int):
        """
        Setter for property: (int) ReferenceGeometryImportLayer
         Returns the reference geometry import layer for I-DEAS    
            
         
        """
        pass
    @property
    def RemoveDiscontinuity(self) -> bool:
        """
        Getter for property: (bool) RemoveDiscontinuity
         Returns the remove discontinuity flag.  
           One of the heal geometry option for I-DEAS import   
         
        """
        pass
    @RemoveDiscontinuity.setter
    def RemoveDiscontinuity(self, remove_discontinuity: bool):
        """
        Setter for property: (bool) RemoveDiscontinuity
         Returns the remove discontinuity flag.  
           One of the heal geometry option for I-DEAS import   
         
        """
        pass
    @property
    def RemoveSelfIntersections(self) -> bool:
        """
        Getter for property: (bool) RemoveSelfIntersections
         Returns the remove self intersection flag.  
           One of the heal geometry option for I-DEAS import    
         
        """
        pass
    @RemoveSelfIntersections.setter
    def RemoveSelfIntersections(self, remove_self_intersections: bool):
        """
        Setter for property: (bool) RemoveSelfIntersections
         Returns the remove self intersection flag.  
           One of the heal geometry option for I-DEAS import    
         
        """
        pass
    @property
    def RemoveSmallEdges(self) -> bool:
        """
        Getter for property: (bool) RemoveSmallEdges
         Returns the remove small edges flag.  
           One of the heal geometry option for I-DEAS import   
         
        """
        pass
    @RemoveSmallEdges.setter
    def RemoveSmallEdges(self, remove_small_edges: bool):
        """
        Setter for property: (bool) RemoveSmallEdges
         Returns the remove small edges flag.  
           One of the heal geometry option for I-DEAS import   
         
        """
        pass
    @property
    def RepairTolerance(self) -> float:
        """
        Getter for property: (float) RepairTolerance
         Returns the repair tolerance.  
           One of the heal geometry option for I-DEAS import    
         
        """
        pass
    @RepairTolerance.setter
    def RepairTolerance(self, repair_tolerance: float):
        """
        Setter for property: (float) RepairTolerance
         Returns the repair tolerance.  
           One of the heal geometry option for I-DEAS import    
         
        """
        pass
    @property
    def RetainFidelityCheckingInformation(self) -> bool:
        """
        Getter for property: (bool) RetainFidelityCheckingInformation
         Returns the retain fidelity checking information flag for I-DEAS   
            
         
        """
        pass
    @RetainFidelityCheckingInformation.setter
    def RetainFidelityCheckingInformation(self, retain_fidelity_checking_information: bool):
        """
        Setter for property: (bool) RetainFidelityCheckingInformation
         Returns the retain fidelity checking information flag for I-DEAS   
            
         
        """
        pass
    @property
    def SaveComponentPartFilesDuringLoad(self) -> bool:
        """
        Getter for property: (bool) SaveComponentPartFilesDuringLoad
         Returns the save component part files flag during load for I-DEAS   
            
         
        """
        pass
    @SaveComponentPartFilesDuringLoad.setter
    def SaveComponentPartFilesDuringLoad(self, save_component_part_files_during_load: bool):
        """
        Setter for property: (bool) SaveComponentPartFilesDuringLoad
         Returns the save component part files flag during load for I-DEAS   
            
         
        """
        pass
    @property
    def SuppressSurfaceModification(self) -> bool:
        """
        Getter for property: (bool) SuppressSurfaceModification
         Returns the suppress surface modification flag.  
           One of the heal geometry option for I-DEAS import   
         
        """
        pass
    @SuppressSurfaceModification.setter
    def SuppressSurfaceModification(self, suppress_surface_modification: bool):
        """
        Setter for property: (bool) SuppressSurfaceModification
         Returns the suppress surface modification flag.  
           One of the heal geometry option for I-DEAS import   
         
        """
        pass
    @property
    def Tolerance(self) -> float:
        """
        Getter for property: (float) Tolerance
         Returns the tolerance.  
           One of the heal geometry option for I-DEAS import    
         
        """
        pass
    @Tolerance.setter
    def Tolerance(self, tolerance: float):
        """
        Setter for property: (float) Tolerance
         Returns the tolerance.  
           One of the heal geometry option for I-DEAS import    
         
        """
        pass
    @property
    def UseRepairTolerance(self) -> bool:
        """
        Getter for property: (bool) UseRepairTolerance
         Returns the use repair tolerance flag.  
           One of the heal geometry option for I-DEAS import    
         
        """
        pass
    @UseRepairTolerance.setter
    def UseRepairTolerance(self, use_repair_tolerance: bool):
        """
        Setter for property: (bool) UseRepairTolerance
         Returns the use repair tolerance flag.  
           One of the heal geometry option for I-DEAS import    
         
        """
        pass
    @property
    def WireframeGeometryImportColor(self) -> int:
        """
        Getter for property: (int) WireframeGeometryImportColor
         Returns the wireframe geometry import color for I-DEAS    
            
         
        """
        pass
    @WireframeGeometryImportColor.setter
    def WireframeGeometryImportColor(self, wireframe_geometry_import_color: int):
        """
        Setter for property: (int) WireframeGeometryImportColor
         Returns the wireframe geometry import color for I-DEAS    
            
         
        """
        pass
    @property
    def WireframeGeometryImportLayer(self) -> int:
        """
        Getter for property: (int) WireframeGeometryImportLayer
         Returns the wireframe geometry import layer for I-DEAS    
            
         
        """
        pass
    @WireframeGeometryImportLayer.setter
    def WireframeGeometryImportLayer(self, wireframe_geometry_import_layer: int):
        """
        Setter for property: (int) WireframeGeometryImportLayer
         Returns the wireframe geometry import layer for I-DEAS    
            
         
        """
        pass
import NXOpen
class SessionPdm(NXOpen.Object): 
    """ Represents the NX Manager preferences for the entire session """
    class JtUpdateFromSourceType(Enum):
        """
        Members Include: 
         |Complete|  
         |NotSet|  

        """
        Complete: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> SessionPdm.JtUpdateFromSourceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LockingPolicyType(Enum):
        """
        Members Include: 
         |AutocheckinSave|  Automatic Check-out on Modify or Save; Check-in on Save or Close 
         |AutocheckinClose|  Automatic Check-out on Modify or Save; Check-in on Close 
         |Manual|  Automatic Check-out on Save; Check-in on Save 
         |Manualplusplus|  Manul Check-out required for Save, Manual Check-in 
         |Supermanualplusplus|  Manul Check-out required for Save, Check-in on Close 

        """
        AutocheckinSave: int
        AutocheckinClose: int
        Manual: int
        Manualplusplus: int
        Supermanualplusplus: int
        @staticmethod
        def ValueOf(value: int) -> SessionPdm.LockingPolicyType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MessagesInconsistentRevisionsType(Enum):
        """
        Members Include: 
         |NotSet|  
         |Warning|  
         |Error| 

        """
        NotSet: int
        Warning: int
        Error: int
        @staticmethod
        def ValueOf(value: int) -> SessionPdm.MessagesInconsistentRevisionsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SynchroniseOnLoadType(Enum):
        """
        Members Include: 
         |Complete|  
         |AddWithTransforms|  
         |NotSet|  

        """
        Complete: int
        AddWithTransforms: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> SessionPdm.SynchroniseOnLoadType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SynchroniseOnSaveType(Enum):
        """
        Members Include: 
         |Complete|  
         |NotSet|  

        """
        Complete: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> SessionPdm.SynchroniseOnSaveType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class UnpopulatedBehaviourType(Enum):
        """
        Members Include: 
         |OnSave| 
         |ModifiedPrompt| 
         |ModifiedNoPrompt| 
         |Never| 
         |PreNx4| 

        """
        OnSave: int
        ModifiedPrompt: int
        ModifiedNoPrompt: int
        Never: int
        PreNx4: int
        @staticmethod
        def ValueOf(value: int) -> SessionPdm.UnpopulatedBehaviourType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def JtUpdateFromSource(self) -> SessionPdm.JtUpdateFromSourceType:
        """
        Getter for property: ( SessionPdm.JtUpdateFromSourceType NXOpen.P) JtUpdateFromSource
         Returns the kind of JT update performed when a part is loaded   
            
         
        """
        pass
    @JtUpdateFromSource.setter
    def JtUpdateFromSource(self, update: SessionPdm.JtUpdateFromSourceType):
        """
        Setter for property: ( SessionPdm.JtUpdateFromSourceType NXOpen.P) JtUpdateFromSource
         Returns the kind of JT update performed when a part is loaded   
            
         
        """
        pass
    @property
    def LockingPolicy(self) -> SessionPdm.LockingPolicyType:
        """
        Getter for property: ( SessionPdm.LockingPolicyType NXOpen.P) LockingPolicy
         Returns the Teamncemter Integration Preferences : Check-Out\Check-In Policy.  
             
         
        """
        pass
    @LockingPolicy.setter
    def LockingPolicy(self, lock: SessionPdm.LockingPolicyType):
        """
        Setter for property: ( SessionPdm.LockingPolicyType NXOpen.P) LockingPolicy
         Returns the Teamncemter Integration Preferences : Check-Out\Check-In Policy.  
             
         
        """
        pass
    @property
    def MessagesInconsistentRevisions(self) -> SessionPdm.MessagesInconsistentRevisionsType:
        """
        Getter for property: ( SessionPdm.MessagesInconsistentRevisionsType NXOpen.P) MessagesInconsistentRevisions
         Returns the kind of messages about inconsistent revisions when a part is loaded   
            
         
        """
        pass
    @MessagesInconsistentRevisions.setter
    def MessagesInconsistentRevisions(self, message: SessionPdm.MessagesInconsistentRevisionsType):
        """
        Setter for property: ( SessionPdm.MessagesInconsistentRevisionsType NXOpen.P) MessagesInconsistentRevisions
         Returns the kind of messages about inconsistent revisions when a part is loaded   
            
         
        """
        pass
    @property
    def SynchroniseOnLoad(self) -> SessionPdm.SynchroniseOnLoadType:
        """
        Getter for property: ( SessionPdm.SynchroniseOnLoadType NXOpen.P) SynchroniseOnLoad
         Returns the kind of synchronisation performed when a part is loaded   
            
         
        """
        pass
    @SynchroniseOnLoad.setter
    def SynchroniseOnLoad(self, sync: SessionPdm.SynchroniseOnLoadType):
        """
        Setter for property: ( SessionPdm.SynchroniseOnLoadType NXOpen.P) SynchroniseOnLoad
         Returns the kind of synchronisation performed when a part is loaded   
            
         
        """
        pass
    @property
    def SynchroniseOnSave(self) -> SessionPdm.SynchroniseOnSaveType:
        """
        Getter for property: ( SessionPdm.SynchroniseOnSaveType NXOpen.P) SynchroniseOnSave
         Returns the kind of synchronisation performed when a part is saved   
            
         
        """
        pass
    @SynchroniseOnSave.setter
    def SynchroniseOnSave(self, sync: SessionPdm.SynchroniseOnSaveType):
        """
        Setter for property: ( SessionPdm.SynchroniseOnSaveType NXOpen.P) SynchroniseOnSave
         Returns the kind of synchronisation performed when a part is saved   
            
         
        """
        pass
    @property
    def UnpopulatedBehaviour(self) -> SessionPdm.UnpopulatedBehaviourType:
        """
        Getter for property: ( SessionPdm.UnpopulatedBehaviourType NXOpen.P) UnpopulatedBehaviour
         Returns the behaviour when an unpopulated part is loaded   
            
         
        """
        pass
    @UnpopulatedBehaviour.setter
    def UnpopulatedBehaviour(self, behaviour: SessionPdm.UnpopulatedBehaviourType):
        """
        Setter for property: ( SessionPdm.UnpopulatedBehaviourType NXOpen.P) UnpopulatedBehaviour
         Returns the behaviour when an unpopulated part is loaded   
            
         
        """
        pass
    @property
    def UnpopulatedWithJtBehaviour(self) -> SessionPdm.UnpopulatedBehaviourType:
        """
        Getter for property: ( SessionPdm.UnpopulatedBehaviourType NXOpen.P) UnpopulatedWithJtBehaviour
         Returns the behaviour when part having JT dataset and no NX dataset is loaded   
            
         
        """
        pass
    @UnpopulatedWithJtBehaviour.setter
    def UnpopulatedWithJtBehaviour(self, behaviour: SessionPdm.UnpopulatedBehaviourType):
        """
        Setter for property: ( SessionPdm.UnpopulatedBehaviourType NXOpen.P) UnpopulatedWithJtBehaviour
         Returns the behaviour when part having JT dataset and no NX dataset is loaded   
            
         
        """
        pass
    def SetDefaultSeed(seed_name: str) -> None:
        """
         Sets the default seed part that NX uses for parts without datasets  
        """
        pass
import NXOpen
class SessionPmi(NXOpen.Object): 
    """ Represents the set of PMI preferences applicable to entire session"""
    @property
    def AssocHighlightColor(self) -> int:
        """
        Getter for property: (int) AssocHighlightColor
         Returns the associated highlight color   
            
         
        """
        pass
    @AssocHighlightColor.setter
    def AssocHighlightColor(self, assoc_highlight_color: int):
        """
        Setter for property: (int) AssocHighlightColor
         Returns the associated highlight color   
            
         
        """
        pass
    @property
    def ReadingDirection(self) -> bool:
        """
        Getter for property: (bool) ReadingDirection
         Returns the reading direction preference   
            
         
        """
        pass
    @ReadingDirection.setter
    def ReadingDirection(self, reading_direction: bool):
        """
        Setter for property: (bool) ReadingDirection
         Returns the reading direction preference   
            
         
        """
        pass
    def UpdateTrackingPropertiesFromXml() -> None:
        """
         Update tracking properties
        """
        pass
import NXOpen
class SessionPreferences(NXOpen.Object): 
    """ Represents a collection of session based preferences. """
    @property
    def Sketch() -> SessionSketch:
        """
         Returns object for doing sketch preferences settings applicable to entire session 
        """
        pass
    @property
    def NXGateway() -> SessionNXGateway:
        """
         Returns object for doing NXGateway preferences settings applicable to entire session 
        """
        pass
    @property
    def Assemblies() -> SessionAssemblies:
        """
         Returns object for doing Asseblies preferences settings applicable to entire session 
        """
        pass
    @property
    def WorkPlane() -> SessionWorkPlane:
        """
         Returns object for doing WorkPlane preferences settings applicable to entire session 
        """
        pass
    @property
    def Modeling() -> SessionModeling:
        """
         Returns object for doing Modeling preferences settings applicable to entire session 
        """
        pass
    @property
    def Drafting() -> SessionDrafting:
        """
         Returns object for doing Drafting preferences settings  applicable to entire session 
        """
        pass
    @property
    def Pmi() -> SessionPmi:
        """
         Returns object for doing Pmi preferences settings  applicable to entire session 
        """
        pass
    @property
    def UserInterface() -> SessionUserInterface:
        """
         Returns object for doing Selection preferences settings applicable to entire session 
        """
        pass
    @property
    def PerformanceVisualization() -> SessionVisualizationPerformance:
        """
         Returns object for doing Visualization Performance preferences settings applicable to entire session 
        """
        pass
    @property
    def ScreenVisualization() -> SessionVisualizationScreen:
        """
         Returns object for doing Visualization Screen preferences settings applicable to entire session 
        """
        pass
    @property
    def ColorSettingVisualization() -> SessionVisualizationColorSetting:
        """
         Returns object for doing Visualization preferences settings applicable to entire session 
        """
        pass
    @property
    def HighQualityImageVisualization() -> SessionVisualizationHighQualityImage:
        """
         Returns object for doing Visualization High Quality Image preferences settings applicable to entire session 
        """
        pass
    @property
    def SpecialEffectsVisualization() -> SessionVisualizationSpecialEffects:
        """
         Returns object for doing Visualization Special Effects preferences settings applicable to entire session 
        """
        pass
    @property
    def RoutingApplicationView() -> RoutingApplicationView:
        """
         Returns the Routing Application View preferences. 
        """
        pass
    @property
    def KnowledgeFusion() -> RulePreferences:
        """
         Returns object for doing Rule preferences settings applicable to entire session 
        """
        pass
    @property
    def Pdm() -> SessionPdm:
        """
         Returns object for doing Pdm preference settings applicable to entire session 
        """
        pass
    @property
    def SessionMeasureReq() -> SessionMeasureRequirements:
        """
         Returns object for doing Measure Requirements in Assembly Sequencing applicable to the entire session 
        """
        pass
    @property
    def VisualizationHandles() -> VisualizationHandles:
        """
         Returns the Visualization Handles preferences 
        """
        pass
    @property
    def SubdivisionModeling() -> SubdivisionModelingPreferences:
        """
         Returns object for doing Subdivision Modeling preferences settings applicable to entire session 
        """
        pass
    @property
    def MorphMesh() -> MorphMeshPreferences:
        """
         Returns object for doing Morph Mesh preferences settings applicable to entire session 
        """
        pass
    @property
    def VisualizationFonts() -> VisualizationFonts:
        """
         Returns the Visualization Fonts preferences 
        """
        pass
    @property
    def EmphasisVisualization() -> SessionVisualizationEmphasis:
        """
         Returns object for doing Visualization Emphasis preferences settings applicable to entire session 
        """
        pass
    @property
    def PostProcessing() -> PostProcessing:
        """
         Returns the CAE Post Processing preferences 
        """
        pass
    @property
    def HighEndRenderingVisualization() -> SessionVisualizationHighEndRendering:
        """
         Returns object for doing Visualization Performance preferences settings applicable to entire session 
        """
        pass
    @property
    def SessionNavigation() -> SessionNavigation:
        """
         Returns object for navigation preferences settings applicable to entire session 
        """
        pass
    @property
    def TextureModeling() -> TextureModelingPreferences:
        """
         Returns object for doing Texture Modeling preferences settings applicable to entire session 
        """
        pass
    @property
    def RoutingPreferences() -> RoutingPreferences:
        """
         Returns object for NextGen Routing preferences applicable to entire session 
        """
        pass
    @property
    def ViewVisualization() -> SessionVisualizationView:
        """
         Returns object for doing Visualization view preferences settings applicable to entire session 
        """
        pass
    @property
    def DrawShape() -> DrawShapeTaskPrefs:
        """
         Returns object for doing Draw Shape preferences settings applicable to entire session 
        """
        pass
    @property
    def AppearanceManagementPref() -> SessionAppearanceMgrPreference:
        """
         This is an internal API and can be changed at any time 
        """
        pass
    @property
    def WiringPreferences() -> WiringPreferences:
        """
         This is an internal API and can be changed at any time 
        """
        pass
    @property
    def CoatingPreferences() -> CoatingPreferences:
        """
         Returns object for Coating preferences applicable to entire session 
        """
        pass
    @property
    def VisualizationVisualPreferences() -> SessionVisualizationVisual:
        """
         Returns object for doing Visualization visual preferences settings applicable to entire session 
        """
        pass
    @property
    def VisualizationLinePreferences() -> VisualizationLine:
        """
         Returns object for doing Visualization line preferences settings applicable to entire session 
        """
        pass
    @property
    def VisualizationShadingPreferences() -> SessionVisualizationShade:
        """
         Returns object for doing Visualization shading preferences settings applicable to entire session 
        """
        pass
    @property
    def FacetBodyVisualization() -> SessionVisualizationFacetBody:
        """
         Returns object for doing Visualization Facet Body preferences settings applicable to entire session 
        """
        pass
    def CreateMeasurePrefsBuilder() -> NXOpen.MeasurePrefsBuilder:
        """
         Create a NXOpen.MeasurePrefsBuilder object 
         Returns builder ( NXOpen.MeasurePrefsBuilder): .
        """
        pass
    def CreateMidSurfacePreferencesBuilder() -> MidSurfacePreferencesBuilder:
        """
         Create a NXOpen.Preferences.MidSurfacePreferencesBuilder object 
         Returns builder ( MidSurfacePreferencesBuilder NXOpen.P): .
        """
        pass
    def CreateModelingPreferencesBuilder() -> ModelingPreferencesBuilder:
        """
         Create a NXOpen.Preferences.ModelingPreferencesBuilder object 
         Returns builder ( ModelingPreferencesBuilder NXOpen.P): .
        """
        pass
    def CreateViewSectionPreference() -> ViewSection:
        """
         Create a NXOpen.Preferences.ViewSection object 
         Returns builder ( ViewSection NXOpen.P): .
        """
        pass
import NXOpen
class SessionSketch(NXOpen.Object): 
    """ Represents the set of sketch preferences applicable to entire session """
    class BackgroundType(Enum):
        """
        Members Include: 
         |Inherit|  Sketch background color is inherited from the parent application 
         |Plain|  Sketch background color is forced to the plain background color 

        """
        Inherit: int
        Plain: int
        @staticmethod
        def ValueOf(value: int) -> SessionSketch.BackgroundType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class GroupConstraintType(Enum):
        """
        Members Include: 
         |PreventConflict|  Preserves external constraints and prevents new conflicts 
         |PreserveAll|  Preserves all external constraints                        

        """
        PreventConflict: int
        PreserveAll: int
        @staticmethod
        def ValueOf(value: int) -> SessionSketch.GroupConstraintType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LineOutputType(Enum):
        """
        Members Include: 
         |Segment|  Sketch line output type is the line segment 
         |AddInfiniteLine|  Sketch line output type is the line segment and a collinear infinite line 
         |InfiniteLine|  Sketch line output type is the infinite line 

        """
        Segment: int
        AddInfiniteLine: int
        InfiniteLine: int
        @staticmethod
        def ValueOf(value: int) -> SessionSketch.LineOutputType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OriginType(Enum):
        """
        Members Include: 
         |InferFromPlaneSelection|  Sketch origin is inferred from placement face 
         |ProjectWorkPartOrigin|  Sketch origin is the projection of the work part origin 

        """
        InferFromPlaneSelection: int
        ProjectWorkPartOrigin: int
        @staticmethod
        def ValueOf(value: int) -> SessionSketch.OriginType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RigidSetConstraintType(Enum):
        """
        Members Include: 
         |PreventConflict|  Preserves external constraints and prevents new conflicts 
         |PreserveAll|  Preserves all external constraints                        

        """
        PreventConflict: int
        PreserveAll: int
        @staticmethod
        def ValueOf(value: int) -> SessionSketch.RigidSetConstraintType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AddRemoteFindingAfterSnap(self) -> bool:
        """
        Getter for property: (bool) AddRemoteFindingAfterSnap
         Returns the setting that controls whether or not remote finding is applied to curves after curve creation or dragging.  
             
         
        """
        pass
    @AddRemoteFindingAfterSnap.setter
    def AddRemoteFindingAfterSnap(self, addFinding: bool):
        """
        Setter for property: (bool) AddRemoteFindingAfterSnap
         Returns the setting that controls whether or not remote finding is applied to curves after curve creation or dragging.  
             
         
        """
        pass
    @property
    def AutoDimensionsToArcCenter(self) -> bool:
        """
        Getter for property: (bool) AutoDimensionsToArcCenter
         Returns the setting that controls whether or not auto-dimensions are created to arc centers.  
             
         
        """
        pass
    @AutoDimensionsToArcCenter.setter
    def AutoDimensionsToArcCenter(self, toArcCenter: bool):
        """
        Setter for property: (bool) AutoDimensionsToArcCenter
         Returns the setting that controls whether or not auto-dimensions are created to arc centers.  
             
         
        """
        pass
    @property
    def AutoReverse(self) -> bool:
        """
        Getter for property: (bool) AutoReverse
         Returns the setting that controls whether to turn on the automatic reverse option for the section view of the active sketch.  
             
         
        """
        pass
    @AutoReverse.setter
    def AutoReverse(self, autoReverse: bool):
        """
        Setter for property: (bool) AutoReverse
         Returns the setting that controls whether to turn on the automatic reverse option for the section view of the active sketch.  
             
         
        """
        pass
    @property
    def BackgroundOption(self) -> SessionSketch.BackgroundType:
        """
        Getter for property: ( SessionSketch.BackgroundType NXOpen.P) BackgroundOption
         Returns the background option   
            
         
        """
        pass
    @BackgroundOption.setter
    def BackgroundOption(self, background_type: SessionSketch.BackgroundType):
        """
        Setter for property: ( SessionSketch.BackgroundType NXOpen.P) BackgroundOption
         Returns the background option   
            
         
        """
        pass
    @property
    def ChangeViewOrientation(self) -> bool:
        """
        Getter for property: (bool) ChangeViewOrientation
         Returns the setting that controls whether the view orientation will be changed to align with the sketch when the sketch is activated.  
             
         
        """
        pass
    @ChangeViewOrientation.setter
    def ChangeViewOrientation(self, change_view_orientation: bool):
        """
        Setter for property: (bool) ChangeViewOrientation
         Returns the setting that controls whether the view orientation will be changed to align with the sketch when the sketch is activated.  
             
         
        """
        pass
    @property
    def ConstraintSymbolSize(self) -> float:
        """
        Getter for property: (float) ConstraintSymbolSize
         Returns the constraint symbol size.  
             
         
        """
        pass
    @ConstraintSymbolSize.setter
    def ConstraintSymbolSize(self, constraint_symbol_size: float):
        """
        Setter for property: (float) ConstraintSymbolSize
         Returns the constraint symbol size.  
             
         
        """
        pass
    @property
    def ContinuousAutoDimensioning(self) -> bool:
        """
        Getter for property: (bool) ContinuousAutoDimensioning
         Returns the setting that controls whether or not to continuously create auto dimensions in a sketch.  
             
         
        """
        pass
    @ContinuousAutoDimensioning.setter
    def ContinuousAutoDimensioning(self, contin_auto_dim: bool):
        """
        Setter for property: (bool) ContinuousAutoDimensioning
         Returns the setting that controls whether or not to continuously create auto dimensions in a sketch.  
             
         
        """
        pass
    @property
    def CreateDimensionForTypedValues(self) -> bool:
        """
        Getter for property: (bool) CreateDimensionForTypedValues
         Returns the setting that controls whether or not driving dimensions are created when values are typed in
                while creating curves.  
             
         
        """
        pass
    @CreateDimensionForTypedValues.setter
    def CreateDimensionForTypedValues(self, createDimension: bool):
        """
        Setter for property: (bool) CreateDimensionForTypedValues
         Returns the setting that controls whether or not driving dimensions are created when values are typed in
                while creating curves.  
             
         
        """
        pass
    @property
    def CreateInferredConstraints(self) -> bool:
        """
        Getter for property: (bool) CreateInferredConstraints
         Returns the setting that controls whether or not to create inferred constraints   
            
         
        """
        pass
    @CreateInferredConstraints.setter
    def CreateInferredConstraints(self, create_inferred_constraints: bool):
        """
        Setter for property: (bool) CreateInferredConstraints
         Returns the setting that controls whether or not to create inferred constraints   
            
         
        """
        pass
    @property
    def CreatePersistentRelations(self) -> bool:
        """
        Getter for property: (bool) CreatePersistentRelations
         Returns the setting that controls whether or not persistent relations are created on geometry.  
             
         
        """
        pass
    @CreatePersistentRelations.setter
    def CreatePersistentRelations(self, createRelations: bool):
        """
        Setter for property: (bool) CreatePersistentRelations
         Returns the setting that controls whether or not persistent relations are created on geometry.  
             
         
        """
        pass
    @property
    def CreateReferenceGeometry(self) -> bool:
        """
        Getter for property: (bool) CreateReferenceGeometry
         Returns the setting that controls whether or not curves are created as reference geometry.  
             
         
        """
        pass
    @CreateReferenceGeometry.setter
    def CreateReferenceGeometry(self, createReferenceGeometry: bool):
        """
        Setter for property: (bool) CreateReferenceGeometry
         Returns the setting that controls whether or not curves are created as reference geometry.  
             
         
        """
        pass
    @property
    def DefaultArcNamePrefix(self) -> str:
        """
        Getter for property: (str) DefaultArcNamePrefix
         Returns the default arc name prefix   
            
         
        """
        pass
    @DefaultArcNamePrefix.setter
    def DefaultArcNamePrefix(self, default_arc_name_prefix: str):
        """
        Setter for property: (str) DefaultArcNamePrefix
         Returns the default arc name prefix   
            
         
        """
        pass
    @property
    def DefaultConicNamePrefix(self) -> str:
        """
        Getter for property: (str) DefaultConicNamePrefix
         Returns the default conic name prefix   
            
         
        """
        pass
    @DefaultConicNamePrefix.setter
    def DefaultConicNamePrefix(self, default_conic_name_prefix: str):
        """
        Setter for property: (str) DefaultConicNamePrefix
         Returns the default conic name prefix   
            
         
        """
        pass
    @property
    def DefaultLineNamePrefix(self) -> str:
        """
        Getter for property: (str) DefaultLineNamePrefix
         Returns the default line name prefix   
            
         
        """
        pass
    @DefaultLineNamePrefix.setter
    def DefaultLineNamePrefix(self, default_line_name_prefix: str):
        """
        Setter for property: (str) DefaultLineNamePrefix
         Returns the default line name prefix   
            
         
        """
        pass
    @property
    def DefaultSketchNamePrefix(self) -> str:
        """
        Getter for property: (str) DefaultSketchNamePrefix
         Returns the default sketch name prefix    
            
         
        """
        pass
    @DefaultSketchNamePrefix.setter
    def DefaultSketchNamePrefix(self, default_sketch_name_prefix: str):
        """
        Setter for property: (str) DefaultSketchNamePrefix
         Returns the default sketch name prefix    
            
         
        """
        pass
    @property
    def DefaultSplineNamePrefix(self) -> str:
        """
        Getter for property: (str) DefaultSplineNamePrefix
         Returns the default spline name prefix   
            
         
        """
        pass
    @DefaultSplineNamePrefix.setter
    def DefaultSplineNamePrefix(self, default_spline_name_prefix: str):
        """
        Setter for property: (str) DefaultSplineNamePrefix
         Returns the default spline name prefix   
            
         
        """
        pass
    @property
    def DefaultVertexNamePrefix(self) -> str:
        """
        Getter for property: (str) DefaultVertexNamePrefix
         Returns the default vertex name prefix   
            
         
        """
        pass
    @DefaultVertexNamePrefix.setter
    def DefaultVertexNamePrefix(self, default_vertex_name_prefix: str):
        """
        Setter for property: (str) DefaultVertexNamePrefix
         Returns the default vertex name prefix   
            
         
        """
        pass
    @property
    def DelayEvaluation(self) -> bool:
        """
        Getter for property: (bool) DelayEvaluation
         Returns the setting that controls whether or not the sketch should be evaluated when a constraint is
            added to the sketch.  
             
         
        """
        pass
    @DelayEvaluation.setter
    def DelayEvaluation(self, delay_evaluation: bool):
        """
        Setter for property: (bool) DelayEvaluation
         Returns the setting that controls whether or not the sketch should be evaluated when a constraint is
            added to the sketch.  
             
         
        """
        pass
    @property
    def DimensionLabel(self) -> SketchPreferences.DimensionLabelType:
        """
        Getter for property: ( SketchPreferences.DimensionLabelType NXOpen.P) DimensionLabel
         Returns the dimension label   
            
         
        """
        pass
    @DimensionLabel.setter
    def DimensionLabel(self, dimension_label: SketchPreferences.DimensionLabelType):
        """
        Setter for property: ( SketchPreferences.DimensionLabelType NXOpen.P) DimensionLabel
         Returns the dimension label   
            
         
        """
        pass
    @property
    def DisplayAutoDimensions(self) -> bool:
        """
        Getter for property: (bool) DisplayAutoDimensions
         Returns the setting that controls whether or not to display auto dimensions   
            
         
        """
        pass
    @DisplayAutoDimensions.setter
    def DisplayAutoDimensions(self, display_auto_dimensions: bool):
        """
        Setter for property: (bool) DisplayAutoDimensions
         Returns the setting that controls whether or not to display auto dimensions   
            
         
        """
        pass
    @property
    def DisplayConstraintSymbols(self) -> bool:
        """
        Getter for property: (bool) DisplayConstraintSymbols
         Returns the setting that controls whether or not to display constraint symbols   
            
         
        """
        pass
    @DisplayConstraintSymbols.setter
    def DisplayConstraintSymbols(self, display_constraint_symbols: bool):
        """
        Setter for property: (bool) DisplayConstraintSymbols
         Returns the setting that controls whether or not to display constraint symbols   
            
         
        """
        pass
    @property
    def DisplayDOFArrows(self) -> bool:
        """
        Getter for property: (bool) DisplayDOFArrows
         Returns the setting that controls whether or not the degree of freedom arrows are displayed.  
             
         
        """
        pass
    @DisplayDOFArrows.setter
    def DisplayDOFArrows(self, display_d_o_f_arrows: bool):
        """
        Setter for property: (bool) DisplayDOFArrows
         Returns the setting that controls whether or not the degree of freedom arrows are displayed.  
             
         
        """
        pass
    @property
    def DisplayObjectColor(self) -> bool:
        """
        Getter for property: (bool) DisplayObjectColor
         Returns the setting that controls whether or not sketch objects should be displayed in their true color   
            
         
        """
        pass
    @DisplayObjectColor.setter
    def DisplayObjectColor(self, display_obj_color: bool):
        """
        Setter for property: (bool) DisplayObjectColor
         Returns the setting that controls whether or not sketch objects should be displayed in their true color   
            
         
        """
        pass
    @property
    def DisplayObjectName(self) -> bool:
        """
        Getter for property: (bool) DisplayObjectName
         Returns the setting that controls whether or not objects are displayed with their names in sketch.  
             
         
        """
        pass
    @DisplayObjectName.setter
    def DisplayObjectName(self, displayObjectName: bool):
        """
        Setter for property: (bool) DisplayObjectName
         Returns the setting that controls whether or not objects are displayed with their names in sketch.  
             
         
        """
        pass
    @property
    def DisplayParenthesesOnReferenceDimensions(self) -> bool:
        """
        Getter for property: (bool) DisplayParenthesesOnReferenceDimensions
         Returns the setting that controls whether or not to display parentheses on reference dimensions   
            
         
        """
        pass
    @DisplayParenthesesOnReferenceDimensions.setter
    def DisplayParenthesesOnReferenceDimensions(self, displayParentheses: bool):
        """
        Setter for property: (bool) DisplayParenthesesOnReferenceDimensions
         Returns the setting that controls whether or not to display parentheses on reference dimensions   
            
         
        """
        pass
    @property
    def DisplayReferenceGeometry(self) -> bool:
        """
        Getter for property: (bool) DisplayReferenceGeometry
         Returns the setting that controls whether or not the reference geometry are displayed on inactive sketches.  
             
         
        """
        pass
    @DisplayReferenceGeometry.setter
    def DisplayReferenceGeometry(self, displayReferenceGeometry: bool):
        """
        Setter for property: (bool) DisplayReferenceGeometry
         Returns the setting that controls whether or not the reference geometry are displayed on inactive sketches.  
             
         
        """
        pass
    @property
    def DisplaySectionMappingWarning(self) -> bool:
        """
        Getter for property: (bool) DisplaySectionMappingWarning
         Returns the display section mapping warning flag.  
           If this is true, when user exits
            sketcher, would get a warning that some dependent feature section may require mapping   
         
        """
        pass
    @DisplaySectionMappingWarning.setter
    def DisplaySectionMappingWarning(self, displaySectionMappingWarning: bool):
        """
        Setter for property: (bool) DisplaySectionMappingWarning
         Returns the display section mapping warning flag.  
           If this is true, when user exits
            sketcher, would get a warning that some dependent feature section may require mapping   
         
        """
        pass
    @property
    def DisplayShadedRegions(self) -> bool:
        """
        Getter for property: (bool) DisplayShadedRegions
         Returns the setting that specifies whether or not closed curve regions are displayed as shaded regions in an active sketch.  
             
         
        """
        pass
    @DisplayShadedRegions.setter
    def DisplayShadedRegions(self, displayShadedRegions: bool):
        """
        Setter for property: (bool) DisplayShadedRegions
         Returns the setting that specifies whether or not closed curve regions are displayed as shaded regions in an active sketch.  
             
         
        """
        pass
    @property
    def DisplayVertices(self) -> bool:
        """
        Getter for property: (bool) DisplayVertices
         Returns the setting that controls whether or not to display sketch vertices.  
             
         
        """
        pass
    @DisplayVertices.setter
    def DisplayVertices(self, displayVertices: bool):
        """
        Setter for property: (bool) DisplayVertices
         Returns the setting that controls whether or not to display sketch vertices.  
             
         
        """
        pass
    @property
    def DynamicConstraintDisplay(self) -> bool:
        """
        Getter for property: (bool) DynamicConstraintDisplay
         Returns the setting that controls whether or not constraint symbols are displayed if the associated geometry is very small.  
             
         
        """
        pass
    @DynamicConstraintDisplay.setter
    def DynamicConstraintDisplay(self, dynamic_constraint_display: bool):
        """
        Setter for property: (bool) DynamicConstraintDisplay
         Returns the setting that controls whether or not constraint symbols are displayed if the associated geometry is very small.  
             
         
        """
        pass
    @property
    def EditDimensionOnCreation(self) -> bool:
        """
        Getter for property: (bool) EditDimensionOnCreation
         Returns the setting that controls whether or not parentheses are displayed on reference dimensions.  
             
         
        """
        pass
    @EditDimensionOnCreation.setter
    def EditDimensionOnCreation(self, editDimOnCreation: bool):
        """
        Setter for property: (bool) EditDimensionOnCreation
         Returns the setting that controls whether or not parentheses are displayed on reference dimensions.  
             
         
        """
        pass
    @property
    def FindMovableObjects(self) -> bool:
        """
        Getter for property: (bool) FindMovableObjects
         Returns the setting that controls whether or not to show results of find movable objects in the active sketch.  
             
         
        """
        pass
    @FindMovableObjects.setter
    def FindMovableObjects(self, findMovableObjects: bool):
        """
        Setter for property: (bool) FindMovableObjects
         Returns the setting that controls whether or not to show results of find movable objects in the active sketch.  
             
         
        """
        pass
    @property
    def FixedTextSize(self) -> float:
        """
        Getter for property: (float) FixedTextSize
         Returns the dimension text size when the text size fixed flag is set.  
             
         
        """
        pass
    @FixedTextSize.setter
    def FixedTextSize(self, fixed_text_size: float):
        """
        Setter for property: (float) FixedTextSize
         Returns the dimension text size when the text size fixed flag is set.  
             
         
        """
        pass
    @property
    def GroupConstraintOption(self) -> SessionSketch.GroupConstraintType:
        """
        Getter for property: ( SessionSketch.GroupConstraintType NXOpen.P) GroupConstraintOption
         Returns the sketch group external constraint management option   
            
         
        """
        pass
    @GroupConstraintOption.setter
    def GroupConstraintOption(self, constraintType: SessionSketch.GroupConstraintType):
        """
        Setter for property: ( SessionSketch.GroupConstraintType NXOpen.P) GroupConstraintOption
         Returns the sketch group external constraint management option   
            
         
        """
        pass
    @property
    def LayoutDimensionTextMode(self) -> SketchPreferences.DimensionTextSizeMode:
        """
        Getter for property: ( SketchPreferences.DimensionTextSizeMode NXOpen.P) LayoutDimensionTextMode
         Returns the setting that controls dimension text size mode in Layout application.  
             
         
        """
        pass
    @LayoutDimensionTextMode.setter
    def LayoutDimensionTextMode(self, mode: SketchPreferences.DimensionTextSizeMode):
        """
        Setter for property: ( SketchPreferences.DimensionTextSizeMode NXOpen.P) LayoutDimensionTextMode
         Returns the setting that controls dimension text size mode in Layout application.  
             
         
        """
        pass
    @property
    def MaintainBlankStatus(self) -> bool:
        """
        Getter for property: (bool) MaintainBlankStatus
         Returns the setting that controls whether or not previously blanked objects will be visible when a sketch is activated   
            
         
        """
        pass
    @MaintainBlankStatus.setter
    def MaintainBlankStatus(self, keep_blank: bool):
        """
        Setter for property: (bool) MaintainBlankStatus
         Returns the setting that controls whether or not previously blanked objects will be visible when a sketch is activated   
            
         
        """
        pass
    @property
    def MaintainLayerStatus(self) -> bool:
        """
        Getter for property: (bool) MaintainLayerStatus
         Returns the setting that controls whether or not the work layer remains the same or returns to its previous 
            value when a sketch is deactivated.  
             
         
        """
        pass
    @MaintainLayerStatus.setter
    def MaintainLayerStatus(self, maintain_layer_status: bool):
        """
        Setter for property: (bool) MaintainLayerStatus
         Returns the setting that controls whether or not the work layer remains the same or returns to its previous 
            value when a sketch is deactivated.  
             
         
        """
        pass
    @property
    def OriginOption(self) -> SessionSketch.OriginType:
        """
        Getter for property: ( SessionSketch.OriginType NXOpen.P) OriginOption
         Returns the origin option   
            
         
        """
        pass
    @OriginOption.setter
    def OriginOption(self, origin_type: SessionSketch.OriginType):
        """
        Setter for property: ( SessionSketch.OriginType NXOpen.P) OriginOption
         Returns the origin option   
            
         
        """
        pass
    @property
    def OverrideConstraints(self) -> bool:
        """
        Getter for property: (bool) OverrideConstraints
         Returns the setting that specifies whether or not constraints will be overridden in sketch operations.  
             
         
        """
        pass
    @OverrideConstraints.setter
    def OverrideConstraints(self, overrideConstraints: bool):
        """
        Setter for property: (bool) OverrideConstraints
         Returns the setting that specifies whether or not constraints will be overridden in sketch operations.  
             
         
        """
        pass
    @property
    def RelaxDimensions(self) -> bool:
        """
        Getter for property: (bool) RelaxDimensions
         Returns the setting that controls whether or not dimensions will be relaxed in sketch operations.  
             
         
        """
        pass
    @RelaxDimensions.setter
    def RelaxDimensions(self, relaxDimensions: bool):
        """
        Setter for property: (bool) RelaxDimensions
         Returns the setting that controls whether or not dimensions will be relaxed in sketch operations.  
             
         
        """
        pass
    @property
    def RetainDimensions(self) -> bool:
        """
        Getter for property: (bool) RetainDimensions
         Returns the retain dimensions flag.  
           If it is True, sketch dimensions continue to display after a sketch is deactivated.    
         
        """
        pass
    @RetainDimensions.setter
    def RetainDimensions(self, retain_dimensions: bool):
        """
        Setter for property: (bool) RetainDimensions
         Returns the retain dimensions flag.  
           If it is True, sketch dimensions continue to display after a sketch is deactivated.    
         
        """
        pass
    @property
    def RigidSetConstraintOption(self) -> SessionSketch.RigidSetConstraintType:
        """
        Getter for property: ( SessionSketch.RigidSetConstraintType NXOpen.P) RigidSetConstraintOption
         Returns the rigid set external constraint management option   
            
         
        """
        pass
    @RigidSetConstraintOption.setter
    def RigidSetConstraintOption(self, constraintType: SessionSketch.RigidSetConstraintType):
        """
        Setter for property: ( SessionSketch.RigidSetConstraintType NXOpen.P) RigidSetConstraintOption
         Returns the rigid set external constraint management option   
            
         
        """
        pass
    @property
    def ScaleOnFirstDrivingDimension(self) -> bool:
        """
        Getter for property: (bool) ScaleOnFirstDrivingDimension
         Returns the setting that controls whether or not the entire active sketch is scaled
            about the sketch origin when the first non-angular driving dimension is applied.  
             
         
        """
        pass
    @ScaleOnFirstDrivingDimension.setter
    def ScaleOnFirstDrivingDimension(self, scaleOnFirstDrivingDimension: bool):
        """
        Setter for property: (bool) ScaleOnFirstDrivingDimension
         Returns the setting that controls whether or not the entire active sketch is scaled
            about the sketch origin when the first non-angular driving dimension is applied.  
             
         
        """
        pass
    @property
    def SectionView(self) -> bool:
        """
        Getter for property: (bool) SectionView
         Returns the setting that controls whether to turn on section view when the sketch is activated.  
             
         
        """
        pass
    @SectionView.setter
    def SectionView(self, section_view: bool):
        """
        Setter for property: (bool) SectionView
         Returns the setting that controls whether to turn on section view when the sketch is activated.  
             
         
        """
        pass
    @property
    def SketchChecking(self) -> bool:
        """
        Getter for property: (bool) SketchChecking
         Returns the setting that controls whether or not checking results will be found after each modification to the sketch.  
             
         
        """
        pass
    @SketchChecking.setter
    def SketchChecking(self, sketchChecking: bool):
        """
        Setter for property: (bool) SketchChecking
         Returns the setting that controls whether or not checking results will be found after each modification to the sketch.  
             
         
        """
        pass
    @property
    def SliceOption(self) -> bool:
        """
        Getter for property: (bool) SliceOption
         Returns the setting that controls whether to turn on the slice option for the section view of the active sketch.  
             
         
        """
        pass
    @SliceOption.setter
    def SliceOption(self, slice_option: bool):
        """
        Setter for property: (bool) SliceOption
         Returns the setting that controls whether to turn on the slice option for the section view of the active sketch.  
             
         
        """
        pass
    @property
    def SnapAngle(self) -> float:
        """
        Getter for property: (float) SnapAngle
         Returns the snap angle.  
            This is snap angle tolerance for vertical, horizontal, parallel, and perpendicular 
            lines.The default value is 3 and maximum value is 20   
         
        """
        pass
    @SnapAngle.setter
    def SnapAngle(self, snap_angle: float):
        """
        Setter for property: (float) SnapAngle
         Returns the snap angle.  
            This is snap angle tolerance for vertical, horizontal, parallel, and perpendicular 
            lines.The default value is 3 and maximum value is 20   
         
        """
        pass
    @property
    def SolvingTolerance(self) -> float:
        """
        Getter for property: (float) SolvingTolerance
         Returns the sketch solving tolerance.  
           This specifies the maximum allowable distance when solving the sketch
                constraints. The tolerance value must be greater than 1e-08.   
         
        """
        pass
    @SolvingTolerance.setter
    def SolvingTolerance(self, tolerance: float):
        """
        Setter for property: (float) SolvingTolerance
         Returns the sketch solving tolerance.  
           This specifies the maximum allowable distance when solving the sketch
                constraints. The tolerance value must be greater than 1e-08.   
         
        """
        pass
    @property
    def TextSizeFixed(self) -> bool:
        """
        Getter for property: (bool) TextSizeFixed
         Returns the setting that controls whether or not dimension text size is fixed.  
           If it is True, text size adjusts opposite of zoom scale so that dimensions appear a constant size.   
         
        """
        pass
    @TextSizeFixed.setter
    def TextSizeFixed(self, text_size_fixed: bool):
        """
        Setter for property: (bool) TextSizeFixed
         Returns the setting that controls whether or not dimension text size is fixed.  
           If it is True, text size adjusts opposite of zoom scale so that dimensions appear a constant size.   
         
        """
        pass
    @property
    def UpdateSketchOnly(self) -> bool:
        """
        Getter for property: (bool) UpdateSketchOnly
         Returns the setting that controls whether or not to update only the sketch while sketching using Direct Sketch.  
           When 
            this preference is set to false, an update will propagate through the whole model   
         
        """
        pass
    @UpdateSketchOnly.setter
    def UpdateSketchOnly(self, delay_model_update: bool):
        """
        Setter for property: (bool) UpdateSketchOnly
         Returns the setting that controls whether or not to update only the sketch while sketching using Direct Sketch.  
           When 
            this preference is set to false, an update will propagate through the whole model   
         
        """
        pass
    @property
    def UseSolvingTolerance(self) -> bool:
        """
        Getter for property: (bool) UseSolvingTolerance
         Returns the setting that controls whether or not to use user input for sketch solving tolerance.  
             
         
        """
        pass
    @UseSolvingTolerance.setter
    def UseSolvingTolerance(self, useTolerance: bool):
        """
        Setter for property: (bool) UseSolvingTolerance
         Returns the setting that controls whether or not to use user input for sketch solving tolerance.  
             
         
        """
        pass
import NXOpen
class SessionUserInterfaceUI(NXOpen.Object): 
    """ Represents all UI based session user interface preferences. Other User Interface settings are 
available with NXOpen.Preferences.SessionUserInterface for settings applicable to session and 
with NXOpen.Preferences.PartUserInterface for User Interface Preferences applicable
to part """
    class DisplayResourceBar(Enum):
        """
        Members Include: 
         |Left|   
         |Right|   

        """
        Left: int
        Right: int
        @staticmethod
        def ValueOf(value: int) -> SessionUserInterfaceUI.DisplayResourceBar:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class NxThemeTypes(Enum):
        """
        Members Include: 
         |Light|   
         |LightGray|   
         |Dark|   
         |Classic|   

        """
        Light: int
        LightGray: int
        Dark: int
        Classic: int
        @staticmethod
        def ValueOf(value: int) -> SessionUserInterfaceUI.NxThemeTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SpeechMode(Enum):
        """
        Members Include: 
         |Single|   
         |Continuous|   

        """
        Single: int
        Continuous: int
        @staticmethod
        def ValueOf(value: int) -> SessionUserInterfaceUI.SpeechMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ConfirmUndo(self) -> bool:
        """
        Getter for property: (bool) ConfirmUndo
         Returns the confirm undo flag   
            
         
        """
        pass
    @ConfirmUndo.setter
    def ConfirmUndo(self, confirm_undo: bool):
        """
        Setter for property: (bool) ConfirmUndo
         Returns the confirm undo flag   
            
         
        """
        pass
    @property
    def DialogBarDecimalPlaces(self) -> int:
        """
        Getter for property: (int) DialogBarDecimalPlaces
         Returns the dialog box decimal places   
            
         
        """
        pass
    @DialogBarDecimalPlaces.setter
    def DialogBarDecimalPlaces(self, dialog_bar_decimal_places: int):
        """
        Setter for property: (int) DialogBarDecimalPlaces
         Returns the dialog box decimal places   
            
         
        """
        pass
    @property
    def DialogBarTracking(self) -> bool:
        """
        Getter for property: (bool) DialogBarTracking
         Returns the dialog bar tracking flag   
            
         
        """
        pass
    @DialogBarTracking.setter
    def DialogBarTracking(self, dialog_bar_tracking_flag: bool):
        """
        Setter for property: (bool) DialogBarTracking
         Returns the dialog bar tracking flag   
            
         
        """
        pass
    @property
    def DisplayAlertsOnInformation(self) -> bool:
        """
        Getter for property: (bool) DisplayAlertsOnInformation
         Returns the option "Display Alerts on Information" gives choice, whether the
             user wants the Diagnostic alerts appear when 
             features contain information messages during feature 
             creation, edit, and update.  
          
             if the option is true then the diagnostic alerts will appear.
             if the option is false then diagnostic alerts will not appear.
             Use  DisplayAlertsOnWarnings  for display of
             alerts on warnings. Alerts are
             always displayed for errors and display of alerts on errors can not be
             changed.   
         
        """
        pass
    @DisplayAlertsOnInformation.setter
    def DisplayAlertsOnInformation(self, display_alerts_on_information: bool):
        """
        Setter for property: (bool) DisplayAlertsOnInformation
         Returns the option "Display Alerts on Information" gives choice, whether the
             user wants the Diagnostic alerts appear when 
             features contain information messages during feature 
             creation, edit, and update.  
          
             if the option is true then the diagnostic alerts will appear.
             if the option is false then diagnostic alerts will not appear.
             Use  DisplayAlertsOnWarnings  for display of
             alerts on warnings. Alerts are
             always displayed for errors and display of alerts on errors can not be
             changed.   
         
        """
        pass
    @property
    def DisplayAlertsOnWarnings(self) -> bool:
        """
        Getter for property: (bool) DisplayAlertsOnWarnings
         Returns the option "Display Alerts on Warnings" gives choice, whether the
             user wants the Diagnostic alerts appear when 
             features contain warnings during feature 
             creation, edit, and update.  
          
             if the option is true then the diagnostic alerts will appear.
             if the option is false then diagnostic alerts will not appear.
             Use  DisplayAlertsOnInformation  for display of
             alerts on information messages. Alerts are
             always displayed for errors and display of alerts on errors can not be
             changed.   
         
        """
        pass
    @DisplayAlertsOnWarnings.setter
    def DisplayAlertsOnWarnings(self, display_alerts_on_warnings: bool):
        """
        Setter for property: (bool) DisplayAlertsOnWarnings
         Returns the option "Display Alerts on Warnings" gives choice, whether the
             user wants the Diagnostic alerts appear when 
             features contain warnings during feature 
             creation, edit, and update.  
          
             if the option is true then the diagnostic alerts will appear.
             if the option is false then diagnostic alerts will not appear.
             Use  DisplayAlertsOnInformation  for display of
             alerts on information messages. Alerts are
             always displayed for errors and display of alerts on errors can not be
             changed.   
         
        """
        pass
    @property
    def DisplayDialogsInPlayback(self) -> bool:
        """
        Getter for property: (bool) DisplayDialogsInPlayback
         Returns the display dialogs in playback flag   
            
         
        """
        pass
    @DisplayDialogsInPlayback.setter
    def DisplayDialogsInPlayback(self, display_dialog_in_playback_flag: bool):
        """
        Setter for property: (bool) DisplayDialogsInPlayback
         Returns the display dialogs in playback flag   
            
         
        """
        pass
    @property
    def DisplayResourceBarOption(self) -> SessionUserInterfaceUI.DisplayResourceBar:
        """
        Getter for property: ( SessionUserInterfaceUI.DisplayResourceBar NXOpen.P) DisplayResourceBarOption
         Returns the display resource bar option   
            
         
        """
        pass
    @DisplayResourceBarOption.setter
    def DisplayResourceBarOption(self, display_resource_bar: SessionUserInterfaceUI.DisplayResourceBar):
        """
        Setter for property: ( SessionUserInterfaceUI.DisplayResourceBar NXOpen.P) DisplayResourceBarOption
         Returns the display resource bar option   
            
         
        """
        pass
    @property
    def HomePageURL(self) -> str:
        """
        Getter for property: (str) HomePageURL
         Returns the home page URL   
            
         
        """
        pass
    @HomePageURL.setter
    def HomePageURL(self, home_page_url: str):
        """
        Setter for property: (str) HomePageURL
         Returns the home page URL   
            
         
        """
        pass
    @property
    def InitialDialogDisplay(self) -> bool:
        """
        Getter for property: (bool) InitialDialogDisplay
         Returns the initial dialog display flag   
            
         
        """
        pass
    @InitialDialogDisplay.setter
    def InitialDialogDisplay(self, initial_dialog_display: bool):
        """
        Setter for property: (bool) InitialDialogDisplay
         Returns the initial dialog display flag   
            
         
        """
        pass
    @property
    def ListingDecimalPlaces(self) -> int:
        """
        Getter for property: (int) ListingDecimalPlaces
         Returns the listing decimal places  
            
         
        """
        pass
    @ListingDecimalPlaces.setter
    def ListingDecimalPlaces(self, listing_decimal_places: int):
        """
        Setter for property: (int) ListingDecimalPlaces
         Returns the listing decimal places  
            
         
        """
        pass
    @property
    def NxTheme(self) -> SessionUserInterfaceUI.NxThemeTypes:
        """
        Getter for property: ( SessionUserInterfaceUI.NxThemeTypes NXOpen.P) NxTheme
         Returns the nx theme option   
            
         
        """
        pass
    @property
    def PagesAutomaticallyFlyOut(self) -> bool:
        """
        Getter for property: (bool) PagesAutomaticallyFlyOut
         Returns the pages automatically fly outflag   
            
         
        """
        pass
    @PagesAutomaticallyFlyOut.setter
    def PagesAutomaticallyFlyOut(self, pages_automatically_fly_out: bool):
        """
        Setter for property: (bool) PagesAutomaticallyFlyOut
         Returns the pages automatically fly outflag   
            
         
        """
        pass
    @property
    def PauseDuration(self) -> int:
        """
        Getter for property: (int) PauseDuration
         Returns the pause duration   
            
         
        """
        pass
    @PauseDuration.setter
    def PauseDuration(self, pause_duration: int):
        """
        Setter for property: (int) PauseDuration
         Returns the pause duration   
            
         
        """
        pass
    @property
    def RecordAllTransform(self) -> bool:
        """
        Getter for property: (bool) RecordAllTransform
         Returns the record all transform flag   
            
         
        """
        pass
    @RecordAllTransform.setter
    def RecordAllTransform(self, record_all_transform_flag: bool):
        """
        Setter for property: (bool) RecordAllTransform
         Returns the record all transform flag   
            
         
        """
        pass
    @property
    def SaveLayoutAtExit(self) -> bool:
        """
        Getter for property: (bool) SaveLayoutAtExit
         Returns the save layout at exit flag.  
             
         
        """
        pass
    @SaveLayoutAtExit.setter
    def SaveLayoutAtExit(self, save_layout_flag: bool):
        """
        Setter for property: (bool) SaveLayoutAtExit
         Returns the save layout at exit flag.  
             
         
        """
        pass
    @property
    def SpeechRecognitionMode(self) -> SessionUserInterfaceUI.SpeechMode:
        """
        Getter for property: ( SessionUserInterfaceUI.SpeechMode NXOpen.P) SpeechRecognitionMode
         Returns the speech recognition mode   
            
         
        """
        pass
    @SpeechRecognitionMode.setter
    def SpeechRecognitionMode(self, listening_mode_single: SessionUserInterfaceUI.SpeechMode):
        """
        Setter for property: ( SessionUserInterfaceUI.SpeechMode NXOpen.P) SpeechRecognitionMode
         Returns the speech recognition mode   
            
         
        """
        pass
    @property
    def UseSystemPrecision(self) -> bool:
        """
        Getter for property: (bool) UseSystemPrecision
         Returns the use system precision flag.  
           True uses the system precision   
         
        """
        pass
    @UseSystemPrecision.setter
    def UseSystemPrecision(self, use_system_precision: bool):
        """
        Setter for property: (bool) UseSystemPrecision
         Returns the use system precision flag.  
           True uses the system precision   
         
        """
        pass
    def ResetDialogBoxSettings() -> None:
        """
         Resets all dialog box settings 
        """
        pass
import NXOpen
class SessionUserInterface(NXOpen.Object): 
    """ Represents the set of User Interface preferences applicable to entire session. Other User Interface 
    settings are available with NXOpen.Preferences.PartUserInterface for settings applicable to 
    part and with the SessionUserInterfaceUI class for UI based User Interface Preferences """
    class JournalFileFormatType(Enum):
        """
        Members Include: 
         |Ascii|  Ascii 
         |Unicode|  Unicode  
         |UnicodeBigEndian|  Unicode Big Endian 
         |Utf8|  UTF 8 

        """
        Ascii: int
        Unicode: int
        UnicodeBigEndian: int
        Utf8: int
        @staticmethod
        def ValueOf(value: int) -> SessionUserInterface.JournalFileFormatType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class JournalLanguageType(Enum):
        """
        Members Include: 
         |VisualBasic|  
         |CPlusPlus|  C++ restricts the file format to Ascii  
         |Java|  
         |Cs|  
         |Python|  

        """
        VisualBasic: int
        CPlusPlus: int
        Java: int
        Cs: int
        Python: int
        @staticmethod
        def ValueOf(value: int) -> SessionUserInterface.JournalLanguageType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def InsetMenuDialogComments(self) -> bool:
        """
        Getter for property: (bool) InsetMenuDialogComments
         Returns the insert menudialog comments flag   
            
         
        """
        pass
    @InsetMenuDialogComments.setter
    def InsetMenuDialogComments(self, inset_menu_dialog_comments: bool):
        """
        Setter for property: (bool) InsetMenuDialogComments
         Returns the insert menudialog comments flag   
            
         
        """
        pass
    @property
    def JournalFileFormat(self) -> SessionUserInterface.JournalFileFormatType:
        """
        Getter for property: ( SessionUserInterface.JournalFileFormatType NXOpen.P) JournalFileFormat
         Returns the journal file format   
            
         
        """
        pass
    @JournalFileFormat.setter
    def JournalFileFormat(self, journal_file_format: SessionUserInterface.JournalFileFormatType):
        """
        Setter for property: ( SessionUserInterface.JournalFileFormatType NXOpen.P) JournalFileFormat
         Returns the journal file format   
            
         
        """
        pass
    @property
    def JournalLanguage(self) -> SessionUserInterface.JournalLanguageType:
        """
        Getter for property: ( SessionUserInterface.JournalLanguageType NXOpen.P) JournalLanguage
         Returns the journal language.  
            Setting the journal language to C++ restricts the 
                file format to Ascii.   
         
        """
        pass
    @JournalLanguage.setter
    def JournalLanguage(self, language: SessionUserInterface.JournalLanguageType):
        """
        Setter for property: ( SessionUserInterface.JournalLanguageType NXOpen.P) JournalLanguage
         Returns the journal language.  
            Setting the journal language to C++ restricts the 
                file format to Ascii.   
         
        """
        pass
import NXOpen
class SessionVisualizationColorSetting(NXOpen.Object): 
    """ Represents the set of visualization preferences applicable to entire session"""
    @property
    def HandlesColor(self) -> int:
        """
        Getter for property: (int) HandlesColor
         Returns the handles color.  
           Sets the handle color. Unigraphics NX displays all handles using a "handle" color. 
        A session attribute determines the color of handles and applies to all parts in a session.  
          This property is deprecated. Use NXOpen.Preferences.PartVisualizationColorSetting.HandleColor instead.
             
         
        """
        pass
    @HandlesColor.setter
    def HandlesColor(self, handles_color: int):
        """
        Setter for property: (int) HandlesColor
         Returns the handles color.  
           Sets the handle color. Unigraphics NX displays all handles using a "handle" color. 
        A session attribute determines the color of handles and applies to all parts in a session.  
          This property is deprecated. Use NXOpen.Preferences.PartVisualizationColorSetting.HandleColor instead.
             
         
        """
        pass
import NXOpen
class SessionVisualizationEmphasis(NXOpen.Object): 
    """ Represents visualization preferences for emphasis that are applicable
        to the entire session. """
    @property
    def ObjectsOffSketchWorkPlaneNonSelectable(self) -> bool:
        """
        Getter for property: (bool) ObjectsOffSketchWorkPlaneNonSelectable
         Returns the setting that controls whether or not objects off the work
                    plane are non-selectable in the Sketch Task Environment.  
           This setting will work if either
                     Preferences::SessionVisualizationEmphasis::SetSketchWorkPlaneEmphasis  or
                     Preferences::SessionVisualizationEmphasis::SetSketchPlaneEmphasis  is set.   
         
        """
        pass
    @ObjectsOffSketchWorkPlaneNonSelectable.setter
    def ObjectsOffSketchWorkPlaneNonSelectable(self, objectsOffSketchWorkPlaneNonSelectable: bool):
        """
        Setter for property: (bool) ObjectsOffSketchWorkPlaneNonSelectable
         Returns the setting that controls whether or not objects off the work
                    plane are non-selectable in the Sketch Task Environment.  
           This setting will work if either
                     Preferences::SessionVisualizationEmphasis::SetSketchWorkPlaneEmphasis  or
                     Preferences::SessionVisualizationEmphasis::SetSketchPlaneEmphasis  is set.   
         
        """
        pass
    @property
    def ObjectsOffWcsWorkPlaneNonSelectable(self) -> bool:
        """
        Getter for property: (bool) ObjectsOffWcsWorkPlaneNonSelectable
         Returns the setting that controls whether or not objects off the WCS work
                    plane are non-selectable.  
             
         
        """
        pass
    @ObjectsOffWcsWorkPlaneNonSelectable.setter
    def ObjectsOffWcsWorkPlaneNonSelectable(self, objectsOffWcsWorkPlaneNonSelectable: bool):
        """
        Setter for property: (bool) ObjectsOffWcsWorkPlaneNonSelectable
         Returns the setting that controls whether or not objects off the WCS work
                    plane are non-selectable.  
             
         
        """
        pass
    @property
    def ProductInterfaceEmphasis(self) -> bool:
        """
        Getter for property: (bool) ProductInterfaceEmphasis
         Returns the setting that controls whether or not Product Interface objects
                    are emphasized.  
             
         
        """
        pass
    @ProductInterfaceEmphasis.setter
    def ProductInterfaceEmphasis(self, productInterfaceEmphasis: bool):
        """
        Setter for property: (bool) ProductInterfaceEmphasis
         Returns the setting that controls whether or not Product Interface objects
                    are emphasized.  
             
         
        """
        pass
    @property
    def SeeThruAll(self) -> bool:
        """
        Getter for property: (bool) SeeThruAll
         Returns the setting that controls whether or not all less important
                    objects are de-emphasized.  
             
         
        """
        pass
    @SeeThruAll.setter
    def SeeThruAll(self, seeThruAll: bool):
        """
        Setter for property: (bool) SeeThruAll
         Returns the setting that controls whether or not all less important
                    objects are de-emphasized.  
             
         
        """
        pass
    @property
    def SeeThruDeEmphasizedObjects(self) -> bool:
        """
        Getter for property: (bool) SeeThruDeEmphasizedObjects
         Returns the setting that controls whether or not See-Thru is applied 
                    to de-emphasized objects.  
             
         
        """
        pass
    @SeeThruDeEmphasizedObjects.setter
    def SeeThruDeEmphasizedObjects(self, seeThruDeEmphasizedObjects: bool):
        """
        Setter for property: (bool) SeeThruDeEmphasizedObjects
         Returns the setting that controls whether or not See-Thru is applied 
                    to de-emphasized objects.  
             
         
        """
        pass
    @property
    def SeeThruPreview(self) -> bool:
        """
        Getter for property: (bool) SeeThruPreview
         Returns the setting that controls whether or not all less important
                    objects are de-emphasized related to the Model Preview.  
             
         
        """
        pass
    @SeeThruPreview.setter
    def SeeThruPreview(self, seeThruPreview: bool):
        """
        Setter for property: (bool) SeeThruPreview
         Returns the setting that controls whether or not all less important
                    objects are de-emphasized related to the Model Preview.  
             
         
        """
        pass
    @property
    def SeeThruSection(self) -> bool:
        """
        Getter for property: (bool) SeeThruSection
         Returns the setting that controls whether or not geometry on the section
                    plane is emphasized.  
             
         
        """
        pass
    @SeeThruSection.setter
    def SeeThruSection(self, seeThruSection: bool):
        """
        Setter for property: (bool) SeeThruSection
         Returns the setting that controls whether or not geometry on the section
                    plane is emphasized.  
             
         
        """
        pass
    @property
    def SketchPlaneEmphasis(self) -> bool:
        """
        Getter for property: (bool) SketchPlaneEmphasis
         Returns the setting that controls if objects not part of the sketch are de-emphasized in the Sketch task environment.  
          
                     If  Preferences::SessionVisualizationEmphasis::SetSketchWorkPlaneEmphasis  and 
                     Preferences::SessionVisualizationEmphasis::SetSketchPlaneEmphasis  are both set, then the behavior of
                     Preferences::SessionVisualizationEmphasis::SetSketchPlaneEmphasis 
                    will override the behavior of  Preferences::SessionVisualizationEmphasis::SetSketchWorkPlaneEmphasis .   
         
        """
        pass
    @SketchPlaneEmphasis.setter
    def SketchPlaneEmphasis(self, sketchPlaneEmphasis: bool):
        """
        Setter for property: (bool) SketchPlaneEmphasis
         Returns the setting that controls if objects not part of the sketch are de-emphasized in the Sketch task environment.  
          
                     If  Preferences::SessionVisualizationEmphasis::SetSketchWorkPlaneEmphasis  and 
                     Preferences::SessionVisualizationEmphasis::SetSketchPlaneEmphasis  are both set, then the behavior of
                     Preferences::SessionVisualizationEmphasis::SetSketchPlaneEmphasis 
                    will override the behavior of  Preferences::SessionVisualizationEmphasis::SetSketchWorkPlaneEmphasis .   
         
        """
        pass
    @property
    def SketchWorkPlaneEmphasis(self) -> bool:
        """
        Getter for property: (bool) SketchWorkPlaneEmphasis
         Returns the setting that controls whether or not objects on the work
                    plane are emphasized in the Sketch Task Environment.  
           If  Preferences::SessionVisualizationEmphasis::SetSketchWorkPlaneEmphasis  and 
                     Preferences::SessionVisualizationEmphasis::SetSketchPlaneEmphasis  are both set, then the behavior of
                     Preferences::SessionVisualizationEmphasis::SetSketchPlaneEmphasis 
                    will override the behavior of  Preferences::SessionVisualizationEmphasis::SetSketchWorkPlaneEmphasis .   
         
        """
        pass
    @SketchWorkPlaneEmphasis.setter
    def SketchWorkPlaneEmphasis(self, sketchWorkPlaneEmphasis: bool):
        """
        Setter for property: (bool) SketchWorkPlaneEmphasis
         Returns the setting that controls whether or not objects on the work
                    plane are emphasized in the Sketch Task Environment.  
           If  Preferences::SessionVisualizationEmphasis::SetSketchWorkPlaneEmphasis  and 
                     Preferences::SessionVisualizationEmphasis::SetSketchPlaneEmphasis  are both set, then the behavior of
                     Preferences::SessionVisualizationEmphasis::SetSketchPlaneEmphasis 
                    will override the behavior of  Preferences::SessionVisualizationEmphasis::SetSketchWorkPlaneEmphasis .   
         
        """
        pass
    @property
    def WcsWorkPlaneEmphasis(self) -> bool:
        """
        Getter for property: (bool) WcsWorkPlaneEmphasis
         Returns the setting that controls whether or not objects on the WCS work
                    plane are emphasized.  
             
         
        """
        pass
    @WcsWorkPlaneEmphasis.setter
    def WcsWorkPlaneEmphasis(self, wcsWorkPlaneEmphasis: bool):
        """
        Setter for property: (bool) WcsWorkPlaneEmphasis
         Returns the setting that controls whether or not objects on the WCS work
                    plane are emphasized.  
             
         
        """
        pass
    @property
    def WorkPartEmphasis(self) -> bool:
        """
        Getter for property: (bool) WorkPartEmphasis
         Returns the setting that controls whether or not the work part is
                    emphasized.  
             
         
        """
        pass
    @WorkPartEmphasis.setter
    def WorkPartEmphasis(self, workPartEmphasis: bool):
        """
        Setter for property: (bool) WorkPartEmphasis
         Returns the setting that controls whether or not the work part is
                    emphasized.  
             
         
        """
        pass
import NXOpen
class SessionVisualizationFacetBody(NXOpen.Object): 
    """ Represents the set of visualization facet body preferences applicable to entire session.
    Set facet body preferences.
    """
    @property
    def EnableMeshEffects(self) -> bool:
        """
        Getter for property: (bool) EnableMeshEffects
         Returns the flag to distinguish display of mesh geometry such as a convergent face.  
           Mesh geometry 
                    is displayed using dimmed facet edges.   
         
        """
        pass
    @EnableMeshEffects.setter
    def EnableMeshEffects(self, enableMeshEffects: bool):
        """
        Setter for property: (bool) EnableMeshEffects
         Returns the flag to distinguish display of mesh geometry such as a convergent face.  
           Mesh geometry 
                    is displayed using dimmed facet edges.   
         
        """
        pass
import NXOpen
class SessionVisualizationHighEndRendering(NXOpen.Object): 
    """ Represents the set of visualization preferences under High End Rendering tab applicable to entire session"""
    class MaterialEditorEditingMode(Enum):
        """
        Members Include: 
         |Basic|  Studio Material Editor in Basic properties mode 
         |Intermediate|  Studio Material Editor in Intermediate properties mode 
         |Full|  Studio Material Editor in Full properties mode 

        """
        Basic: int
        Intermediate: int
        Full: int
        @staticmethod
        def ValueOf(value: int) -> SessionVisualizationHighEndRendering.MaterialEditorEditingMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AllowApplyingMaterialsToAllBodiesOfComponents(self) -> bool:
        """
        Getter for property: (bool) AllowApplyingMaterialsToAllBodiesOfComponents
         Returns  the option which allows an assembly component to be
                     selected (via the Assembly Navigator, graphics window selection, or QuickPick) when
                     applying a Studio material.  
            Applying a material to a selected component will apply it to all bodies of the 
                     component.
                     If false, a component will not be selectable when applying a Studio material.
                  
         
        """
        pass
    @AllowApplyingMaterialsToAllBodiesOfComponents.setter
    def AllowApplyingMaterialsToAllBodiesOfComponents(self, applyToAllBodies: bool):
        """
        Setter for property: (bool) AllowApplyingMaterialsToAllBodiesOfComponents
         Returns  the option which allows an assembly component to be
                     selected (via the Assembly Navigator, graphics window selection, or QuickPick) when
                     applying a Studio material.  
            Applying a material to a selected component will apply it to all bodies of the 
                     component.
                     If false, a component will not be selectable when applying a Studio material.
                  
         
        """
        pass
    @property
    def StudioMaterialEditorEditingMode(self) -> SessionVisualizationHighEndRendering.MaterialEditorEditingMode:
        """
        Getter for property: ( SessionVisualizationHighEndRendering.MaterialEditorEditingMode NXOpen.P) StudioMaterialEditorEditingMode
         Returns  the Studio Material Editor editing mode   
            
         
        """
        pass
    @StudioMaterialEditorEditingMode.setter
    def StudioMaterialEditorEditingMode(self, current_mode: SessionVisualizationHighEndRendering.MaterialEditorEditingMode):
        """
        Setter for property: ( SessionVisualizationHighEndRendering.MaterialEditorEditingMode NXOpen.P) StudioMaterialEditorEditingMode
         Returns  the Studio Material Editor editing mode   
            
         
        """
        pass
    def GetCustomTextureAssetPaths() -> List[str]:
        """
         The custom texture asset paths used for Visual Materials in high end rendering applications like
                Advanced Studio and Ray Traced Studio. These asset paths are parsed through for texture assets to render textured Visual Materials.
                Texture assets are image files used to represent various parameters of textured Visual Materials. 
         Returns customTexturePaths (List[str]): .
        """
        pass
    def SetCustomTextureAssetPaths(customTexturePaths: List[str]) -> None:
        """
         The custom texture asset paths used for Visual Materials. Asset path priority will be considered 
                based on the order in which they are specified, with the highest priority path first and the lowest priority path last.
                If the default texture asset locations are not included within the customTexturePaths array, the paths will be 
                prioritized ahead of the default locations. It is encouraged to query the existing asset paths
                via NXOpen.Preferences.SessionVisualizationHighEndRendering.GetCustomTextureAssetPaths to obtain the default paths.
        """
        pass
import NXOpen
class SessionVisualizationHighQualityImage(NXOpen.Object): 
    """ Represents the High Quality Image preferences for the entire session """
    class ImageSizeType(Enum):
        """
        Members Include: 
         |FillView|  
         |AnsiA|  
         |AnsiB|  
         |AnsiC|  
         |AnsiD|  
         |AnsiE|  
         |IsoA4|  
         |IsoA3|  
         |IsoA2|  
         |IsoA1|  
         |IsoA0|  
         |UserDefined|  
         |TrueSize|  

        """
        FillView: int
        AnsiA: int
        AnsiB: int
        AnsiC: int
        AnsiD: int
        AnsiE: int
        IsoA4: int
        IsoA3: int
        IsoA2: int
        IsoA1: int
        IsoA0: int
        UserDefined: int
        TrueSize: int
        @staticmethod
        def ValueOf(value: int) -> SessionVisualizationHighQualityImage.ImageSizeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OrientationType(Enum):
        """
        Members Include: 
         |Landscape|  
         |Portrait|  

        """
        Landscape: int
        Portrait: int
        @staticmethod
        def ValueOf(value: int) -> SessionVisualizationHighQualityImage.OrientationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PlotQualityType(Enum):
        """
        Members Include: 
         |Fine|  
         |Medium|  
         |Rough|  
         |Coarse|  

        """
        Fine: int
        Medium: int
        Rough: int
        Coarse: int
        @staticmethod
        def ValueOf(value: int) -> SessionVisualizationHighQualityImage.PlotQualityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ResolutionType(Enum):
        """
        Members Include: 
         |Draft|  
         |Low|  
         |Medium|  
         |High|  
         |UserDefined|  

        """
        Draft: int
        Low: int
        Medium: int
        High: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> SessionVisualizationHighQualityImage.ResolutionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Orientation(self) -> SessionVisualizationHighQualityImage.OrientationType:
        """
        Getter for property: ( SessionVisualizationHighQualityImage.OrientationType NXOpen.P) Orientation
         Returns the orientation for the High Quality Image (portrait or landscape).  
          
                orientation is not used if image_size is fill_view or user_defined.   
         
        """
        pass
    @Orientation.setter
    def Orientation(self, orientation: SessionVisualizationHighQualityImage.OrientationType):
        """
        Setter for property: ( SessionVisualizationHighQualityImage.OrientationType NXOpen.P) Orientation
         Returns the orientation for the High Quality Image (portrait or landscape).  
          
                orientation is not used if image_size is fill_view or user_defined.   
         
        """
        pass
    @property
    def PlotQuality(self) -> SessionVisualizationHighQualityImage.PlotQualityType:
        """
        Getter for property: ( SessionVisualizationHighQualityImage.PlotQualityType NXOpen.P) PlotQuality
         Returns the quality of the plot of the High Quality Image.  
           
                plot_quality is not used if image_size is fill_view   
         
        """
        pass
    @PlotQuality.setter
    def PlotQuality(self, plot_quality: SessionVisualizationHighQualityImage.PlotQualityType):
        """
        Setter for property: ( SessionVisualizationHighQualityImage.PlotQualityType NXOpen.P) PlotQuality
         Returns the quality of the plot of the High Quality Image.  
           
                plot_quality is not used if image_size is fill_view   
         
        """
        pass
    @property
    def SubRegion(self) -> bool:
        """
        Getter for property: (bool) SubRegion
         Returns the setting for whether the High Quality Image is generated from a sub-region.  
          
                sub_region is only used when image_size is fill_view   
         
        """
        pass
    @SubRegion.setter
    def SubRegion(self, use_sub_region: bool):
        """
        Setter for property: (bool) SubRegion
         Returns the setting for whether the High Quality Image is generated from a sub-region.  
          
                sub_region is only used when image_size is fill_view   
         
        """
        pass
    def GetImageSize() -> Tuple[SessionVisualizationHighQualityImage.ImageSizeType, int, int]:
        """
         Returns the image size to use for the generation of the High Quality Image.
                x_size and y_size vary only for User Defined image size type.
                For other image size types, the values returned in them are the x and y
                sizes fixed for the image size type. 
         Returns A tuple consisting of (image_size, x_size, y_size). 
         - image_size is:  SessionVisualizationHighQualityImage.ImageSizeType NXOpen.P. .
         - x_size is: int. X Pixel size. See note above. .
         - y_size is: int. Y Pixel size. See note above .

        """
        pass
    def GetResolution() -> Tuple[SessionVisualizationHighQualityImage.ResolutionType, int]:
        """
         Returns the resolution to use when generating a High Quality Image.
                The resolution is not used if the image_size is fill_view.
                dots_per_inch is variable only for User Defined resolution type. For other
                resolution types, the returned dots_per_inch is the number of dots
                per inch which is fixed for the given resolution type. 
         Returns A tuple consisting of (resolution, dots_per_inch). 
         - resolution is:  SessionVisualizationHighQualityImage.ResolutionType NXOpen.P. .
         - dots_per_inch is: int. Dots per inch.  See note above. .

        """
        pass
    def SetImageSize(image_size: SessionVisualizationHighQualityImage.ImageSizeType, x_size: int, y_size: int) -> None:
        """
         Specifies the image size to use for the generation of the High Quality Image.
                x_size and y_size only apply for User Defined image size type.
                For other image size types, they are ignored. 
        """
        pass
    def SetResolution(resolution: SessionVisualizationHighQualityImage.ResolutionType, dots_per_inch: int) -> None:
        """
         Specifies the resolution to use when generating a High Quality Image.
                The given resolution is not used if the image_size is fill_view.
                dots_per_inch is used only for User Defined resolution.  For other
                resolutions types, the input dots_per_inch is ignored. 
        """
        pass
import NXOpen
class SessionVisualizationPerformance(NXOpen.Object): 
    """ Represents visualization performance preferences that are applicable
        to the entire session. """
    @property
    def RenderSolidsUsingStoredFacets(self) -> bool:
        """
        Getter for property: (bool) RenderSolidsUsingStoredFacets
         Returns the rendering of solids using stored facets during interactive mode.  
          
                      When a solid is rendered in non-lightweight mode, this
                   preference can be enabled to use facets stored in the part if 
                   valid facets exist for the solid, even if those facets do not meet
                   the current rendering parameters. This improves performance of 
                   certain shaded displays by avoiding need to tessellate the solid, 
                   though the visual quality may be impacted. E.g. when this preference 
                   is enabled, smooth edge settings (e.g. see use of 
                    NXOpen::Preferences::ViewVisualizationVisual::SmoothEdgeWidth )
                   are implicitly ignored to improve the performance.
                     
                     
                   This setting is ignored by  NXOpen::ViewCollection::UpdateDisplay .
                     
                     
                   The display is not immediately regenerated when this setting is changed.
                   Use  NXOpen::ViewCollection::Regenerate  to update display.
                     
                  
         
        """
        pass
    @RenderSolidsUsingStoredFacets.setter
    def RenderSolidsUsingStoredFacets(self, useStoredFacets: bool):
        """
        Setter for property: (bool) RenderSolidsUsingStoredFacets
         Returns the rendering of solids using stored facets during interactive mode.  
          
                      When a solid is rendered in non-lightweight mode, this
                   preference can be enabled to use facets stored in the part if 
                   valid facets exist for the solid, even if those facets do not meet
                   the current rendering parameters. This improves performance of 
                   certain shaded displays by avoiding need to tessellate the solid, 
                   though the visual quality may be impacted. E.g. when this preference 
                   is enabled, smooth edge settings (e.g. see use of 
                    NXOpen::Preferences::ViewVisualizationVisual::SmoothEdgeWidth )
                   are implicitly ignored to improve the performance.
                     
                     
                   This setting is ignored by  NXOpen::ViewCollection::UpdateDisplay .
                     
                     
                   The display is not immediately regenerated when this setting is changed.
                   Use  NXOpen::ViewCollection::Regenerate  to update display.
                     
                  
         
        """
        pass
import NXOpen
class SessionVisualizationScreen(NXOpen.Object): 
    """ Represents the set of visualization preferences under screen tab applicable to entire session"""
    class ViewTriadLocation(Enum):
        """
        Members Include: 
         |BottomLeft|  View triad display on the bottom left of the view 
         |BottomRight|  View triad display on the bottom right of the view 

        """
        BottomLeft: int
        BottomRight: int
        @staticmethod
        def ValueOf(value: int) -> SessionVisualizationScreen.ViewTriadLocation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CsysFixedSizeOnScreen(self) -> bool:
        """
        Getter for property: (bool) CsysFixedSizeOnScreen
         Returns  whether the CSYS display in fixed size on screen.  
             
         
        """
        pass
    @CsysFixedSizeOnScreen.setter
    def CsysFixedSizeOnScreen(self, fixed_size_on_screen: bool):
        """
        Setter for property: (bool) CsysFixedSizeOnScreen
         Returns  whether the CSYS display in fixed size on screen.  
             
         
        """
        pass
    @property
    def CsysShowThrough(self) -> bool:
        """
        Getter for property: (bool) CsysShowThrough
         Returns  whether the CSYS display in show through mode   
            
         
        """
        pass
    @CsysShowThrough.setter
    def CsysShowThrough(self, show_through: bool):
        """
        Setter for property: (bool) CsysShowThrough
         Returns  whether the CSYS display in show through mode   
            
         
        """
        pass
    @property
    def DisplayCenterOfRotation(self) -> bool:
        """
        Getter for property: (bool) DisplayCenterOfRotation
         Returns whether a graphic representing the center of rotation is displayed 
            during interactive view rotation.  
             
         
        """
        pass
    @DisplayCenterOfRotation.setter
    def DisplayCenterOfRotation(self, display_center_of_rotation: bool):
        """
        Setter for property: (bool) DisplayCenterOfRotation
         Returns whether a graphic representing the center of rotation is displayed 
            during interactive view rotation.  
             
         
        """
        pass
    @property
    def DoFitOnHideOrShow(self) -> bool:
        """
        Getter for property: (bool) DoFitOnHideOrShow
         Returns the option to specify whether a Fit should be done when a Hide or Show is performed.  
             
         
        """
        pass
    @DoFitOnHideOrShow.setter
    def DoFitOnHideOrShow(self, is_do_fit_on_hide_or_show: bool):
        """
        Setter for property: (bool) DoFitOnHideOrShow
         Returns the option to specify whether a Fit should be done when a Hide or Show is performed.  
             
         
        """
        pass
    @property
    def ExcludeDatumsFromFit(self) -> bool:
        """
        Getter for property: (bool) ExcludeDatumsFromFit
         Returns the option to specify whether datum objects and planar ship grids should not be examined
            when a Fit is done.  
             
         
        """
        pass
    @ExcludeDatumsFromFit.setter
    def ExcludeDatumsFromFit(self, is_exclude_datums_from_fit: bool):
        """
        Setter for property: (bool) ExcludeDatumsFromFit
         Returns the option to specify whether datum objects and planar ship grids should not be examined
            when a Fit is done.  
             
         
        """
        pass
    @property
    def FitPercentage(self) -> int:
        """
        Getter for property: (int) FitPercentage
         Returns the fit percentage.  
           Specifies the area of the graphics display to be occupied by the model after a fit operation 
        is performed. For example, a fit percentage of 100% scales the model so that it occupies 100% of the graphics display. 
        Similarly, a fit percentage of 80% fits the model within 80% of the graphics display area.   
         
        """
        pass
    @FitPercentage.setter
    def FitPercentage(self, fit_percentage: int):
        """
        Setter for property: (int) FitPercentage
         Returns the fit percentage.  
           Specifies the area of the graphics display to be occupied by the model after a fit operation 
        is performed. For example, a fit percentage of 100% scales the model so that it occupies 100% of the graphics display. 
        Similarly, a fit percentage of 80% fits the model within 80% of the graphics display area.   
         
        """
        pass
    @property
    def FitToSectionClipPlanes(self) -> bool:
        """
        Getter for property: (bool) FitToSectionClipPlanes
         Returns the option to specify whether, when sectioning is enabled for a view, the bounds computed
            by a Fit operation should be limited by the sectioning clipping planes.  
             
         
        """
        pass
    @FitToSectionClipPlanes.setter
    def FitToSectionClipPlanes(self, is_fit_to_section_clip_planes: bool):
        """
        Setter for property: (bool) FitToSectionClipPlanes
         Returns the option to specify whether, when sectioning is enabled for a view, the bounds computed
            by a Fit operation should be limited by the sectioning clipping planes.  
             
         
        """
        pass
    @property
    def HighPrecisionPanning(self) -> bool:
        """
        Getter for property: (bool) HighPrecisionPanning
         Returns whether mouse-driven panning is to be done using a higher precision
            than normal, which means that a given mouse motion will result in
            a smaller panning.  
             
         
        """
        pass
    @HighPrecisionPanning.setter
    def HighPrecisionPanning(self, is_high_precision_panning: bool):
        """
        Setter for property: (bool) HighPrecisionPanning
         Returns whether mouse-driven panning is to be done using a higher precision
            than normal, which means that a given mouse motion will result in
            a smaller panning.  
             
         
        """
        pass
    @property
    def HighPrecisionRotation(self) -> bool:
        """
        Getter for property: (bool) HighPrecisionRotation
         Returns whether mouse-driven rotation is to be done using a higher precision
            than normal, which means that a given mouse motion will result in
            a smaller rotation.  
             
         
        """
        pass
    @HighPrecisionRotation.setter
    def HighPrecisionRotation(self, is_high_precision_rotation: bool):
        """
        Setter for property: (bool) HighPrecisionRotation
         Returns whether mouse-driven rotation is to be done using a higher precision
            than normal, which means that a given mouse motion will result in
            a smaller rotation.  
             
         
        """
        pass
    @property
    def IgnoreLockVerticalAxis(self) -> bool:
        """
        Getter for property: (bool) IgnoreLockVerticalAxis
         Returns whether the locked vertical axis should be ignored when model is tilted
            during interactive view rotation.  
             
         
        """
        pass
    @IgnoreLockVerticalAxis.setter
    def IgnoreLockVerticalAxis(self, ignore_lock_vertical_axis: bool):
        """
        Setter for property: (bool) IgnoreLockVerticalAxis
         Returns whether the locked vertical axis should be ignored when model is tilted
            during interactive view rotation.  
             
         
        """
        pass
    @property
    def InferEdgeOutput(self) -> bool:
        """
        Getter for property: (bool) InferEdgeOutput
         Returns whether plotted edges reflect onscreen edge appearance.  
           This option 
        affects the appearance of edges in output produced by Plot, Print, CGM 
        Export and similar functions. It affects edge appearance for modeling 
        views only, not for views on a drawing sheet. When this option is disabled, 
        the appearance of plotted edges is controlled by edge display options 
        (Hidden Edges, Silhouettes, Smooth Edges) used for Static Wireframe 
        rendering style. When this option is enabled, the appearance of plotted 
        edges is inferred from onscreen edge appearance.   
         
        """
        pass
    @InferEdgeOutput.setter
    def InferEdgeOutput(self, infer_edge_output: bool):
        """
        Setter for property: (bool) InferEdgeOutput
         Returns whether plotted edges reflect onscreen edge appearance.  
           This option 
        affects the appearance of edges in output produced by Plot, Print, CGM 
        Export and similar functions. It affects edge appearance for modeling 
        views only, not for views on a drawing sheet. When this option is disabled, 
        the appearance of plotted edges is controlled by edge display options 
        (Hidden Edges, Silhouettes, Smooth Edges) used for Static Wireframe 
        rendering style. When this option is enabled, the appearance of plotted 
        edges is inferred from onscreen edge appearance.   
         
        """
        pass
    @property
    def LockVerticalAxis(self) -> bool:
        """
        Getter for property: (bool) LockVerticalAxis
         Returns whether the vertical axis of the model should be locked 
            during interactive view rotation.  
             
         
        """
        pass
    @LockVerticalAxis.setter
    def LockVerticalAxis(self, lock_vertical_axis: bool):
        """
        Setter for property: (bool) LockVerticalAxis
         Returns whether the vertical axis of the model should be locked 
            during interactive view rotation.  
             
         
        """
        pass
    @property
    def PreserveFieldOfViewAngleForFit(self) -> bool:
        """
        Getter for property: (bool) PreserveFieldOfViewAngleForFit
         Returns whether for a perspective view the Fit operation should not change the
            field of view angle from the camera position to the view bounds   
            
         
        """
        pass
    @PreserveFieldOfViewAngleForFit.setter
    def PreserveFieldOfViewAngleForFit(self, is_preserve_field_of_view_angle_for_fit: bool):
        """
        Setter for property: (bool) PreserveFieldOfViewAngleForFit
         Returns whether for a perspective view the Fit operation should not change the
            field of view angle from the camera position to the view bounds   
            
         
        """
        pass
    @property
    def RotationPointDelay(self) -> int:
        """
        Getter for property: (int) RotationPointDelay
         Returns    
            
         
        """
        pass
    @RotationPointDelay.setter
    def RotationPointDelay(self, rotation_point_delay: int):
        """
        Setter for property: (int) RotationPointDelay
         Returns    
            
         
        """
        pass
    @property
    def TiltSnapAngle(self) -> float:
        """
        Getter for property: (float) TiltSnapAngle
         Returns the angle when the model should automatically orient to align it's vertical axis 
            during interactive view rotation.  
             
         
        """
        pass
    @TiltSnapAngle.setter
    def TiltSnapAngle(self, tilt_snap_angle: float):
        """
        Setter for property: (float) TiltSnapAngle
         Returns the angle when the model should automatically orient to align it's vertical axis 
            during interactive view rotation.  
             
         
        """
        pass
    @property
    def TriadLocation(self) -> SessionVisualizationScreen.ViewTriadLocation:
        """
        Getter for property: ( SessionVisualizationScreen.ViewTriadLocation NXOpen.P) TriadLocation
         Returns the view triad location   
            
         
        """
        pass
    @TriadLocation.setter
    def TriadLocation(self, triad_location: SessionVisualizationScreen.ViewTriadLocation):
        """
        Setter for property: ( SessionVisualizationScreen.ViewTriadLocation NXOpen.P) TriadLocation
         Returns the view triad location   
            
         
        """
        pass
    @property
    def TriadVisibility(self) -> int:
        """
        Getter for property: (int) TriadVisibility
         Returns    
            
         
        """
        pass
    @TriadVisibility.setter
    def TriadVisibility(self, triad_visibility: int):
        """
        Setter for property: (int) TriadVisibility
         Returns    
            
         
        """
        pass
import NXOpen
class SessionVisualizationShade(NXOpen.Object): 
    """ Represents the UI related Visualization Shade preferences. These preferences are maintained at
UI level and applicable to entire session """
    @property
    def EdgesEmphasis(self) -> bool:
        """
        Getter for property: (bool) EdgesEmphasis
         Returns the edge emphasis flag.  
          Alters how edges are displayed when Shaded Face Edges is flag is true.   
         
        """
        pass
    @EdgesEmphasis.setter
    def EdgesEmphasis(self, edges_emphasis: bool):
        """
        Setter for property: (bool) EdgesEmphasis
         Returns the edge emphasis flag.  
          Alters how edges are displayed when Shaded Face Edges is flag is true.   
         
        """
        pass
    @property
    def LwrtStudioDisplay(self) -> bool:
        """
        Getter for property: (bool) LwrtStudioDisplay
         Returns the lwrt studio display flag.  
          Alters how studio are displayed.   
         
        """
        pass
    @LwrtStudioDisplay.setter
    def LwrtStudioDisplay(self, lwrt_studio_display: bool):
        """
        Setter for property: (bool) LwrtStudioDisplay
         Returns the lwrt studio display flag.  
          Alters how studio are displayed.   
         
        """
        pass
    @property
    def ShowFacetEdges(self) -> bool:
        """
        Getter for property: (bool) ShowFacetEdges
         Returns the show facet edge flag.  
           Toggles the display of facet edges. If this flag is true it can help 
            when trying to evaluate or interpret faceted edges.   
         
        """
        pass
    @ShowFacetEdges.setter
    def ShowFacetEdges(self, facet_edges: bool):
        """
        Setter for property: (bool) ShowFacetEdges
         Returns the show facet edge flag.  
           Toggles the display of facet edges. If this flag is true it can help 
            when trying to evaluate or interpret faceted edges.   
         
        """
        pass
    def RegenerateShadedViewsFromToleranceChange() -> None:
        """
         Regenerates Shaded Views. Updates all objects based on their surfacing tolerance. 
        """
        pass
    def RegenerateStudioAnalysisViewsFromTolChange(update_env_option: bool) -> None:
        """
         Regenerates Studio Analysis Views. Updates all objects based on their surfacing tolerance. 
        """
        pass
import NXOpen
class SessionVisualizationSpecialEffects(NXOpen.Object): 
    """ Represents the set of visualization special effect preferences applicable to entire session.
    Set stereo preferences.
    """
    @property
    def EnableStereo(self) -> bool:
        """
        Getter for property: (bool) EnableStereo
         Returns the enable stereo flag.  
           Toggles the display of stereo. To see correct stereo display, you need a supported graphics card,
                a 3D Stereo Display or Projector, and 3D glasses (and possibly a hub). The hardware vendor control panel Stereo option must
                also be turned on.   
         
        """
        pass
    @EnableStereo.setter
    def EnableStereo(self, enableStereo: bool):
        """
        Setter for property: (bool) EnableStereo
         Returns the enable stereo flag.  
           Toggles the display of stereo. To see correct stereo display, you need a supported graphics card,
                a 3D Stereo Display or Projector, and 3D glasses (and possibly a hub). The hardware vendor control panel Stereo option must
                also be turned on.   
         
        """
        pass
    @property
    def ParallaxFactor(self) -> int:
        """
        Getter for property: (int) ParallaxFactor
         Returns the parallax factor.  
           Defines the amount of 'Stereo effect'. A larger setting produces stronger 3D effect but may cause visual discomfort. 
                The minimum setting is 0 (no 3D effect) and the maximum setting is 20 (strong 3D effect).   
         
        """
        pass
    @ParallaxFactor.setter
    def ParallaxFactor(self, parallaxFactor: int):
        """
        Setter for property: (int) ParallaxFactor
         Returns the parallax factor.  
           Defines the amount of 'Stereo effect'. A larger setting produces stronger 3D effect but may cause visual discomfort. 
                The minimum setting is 0 (no 3D effect) and the maximum setting is 20 (strong 3D effect).   
         
        """
        pass
    @property
    def SupportStereo(self) -> bool:
        """
        Getter for property: (bool) SupportStereo
         Returns the support stereo flag.  
           Queries whether your system supports stereo display (A supported graphics card is installed and
                the Stereo option in hardware vendor control panel is turned on). To see correct stereo display, you also need a 3D Stereo 
                Display or Projector, and 3D glasses (and possibly a hub).  
         
        """
        pass
import NXOpen
class SessionVisualizationView(NXOpen.Object): 
    """ Represents visualization view preferences that are applicable
        to the entire session. """
    @property
    def MaintainViewOriginWhenZooming(self) -> bool:
        """
        Getter for property: (bool) MaintainViewOriginWhenZooming
         Returns whether the view origin is maintained at the current location when zooming.  
              
         
        """
        pass
    @MaintainViewOriginWhenZooming.setter
    def MaintainViewOriginWhenZooming(self, maintain_view_origin: bool):
        """
        Setter for property: (bool) MaintainViewOriginWhenZooming
         Returns whether the view origin is maintained at the current location when zooming.  
              
         
        """
        pass
    @property
    def SetViewOriginWhenRotationReferenceIsSet(self) -> bool:
        """
        Getter for property: (bool) SetViewOriginWhenRotationReferenceIsSet
         Returns whether automatically sets the view origin when the rotation reference is set.  
              
         
        """
        pass
    @SetViewOriginWhenRotationReferenceIsSet.setter
    def SetViewOriginWhenRotationReferenceIsSet(self, set_view_origin: bool):
        """
        Setter for property: (bool) SetViewOriginWhenRotationReferenceIsSet
         Returns whether automatically sets the view origin when the rotation reference is set.  
              
         
        """
        pass
import NXOpen
class SessionVisualizationVisual(NXOpen.Object): 
    """ Represents all UI based session Visualization visual preferences """
    class FinishEffect(Enum):
        """
        Members Include: 
         |GlobalFinish|  Material based finish effect 
         |PartShininess|  Shininess based finish effect 

        """
        GlobalFinish: int
        PartShininess: int
        @staticmethod
        def ValueOf(value: int) -> SessionVisualizationVisual.FinishEffect:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class GlobalFinishType(Enum):
        """
        Members Include: 
         |Flat|  Flat global finish effect 
         |Glossy|  Glossy global finish effect 
         |Matte|  Matte global finish effect 
         |Satin|  Satin global finish effect 

        """
        Flat: int
        Glossy: int
        Matte: int
        Satin: int
        @staticmethod
        def ValueOf(value: int) -> SessionVisualizationVisual.GlobalFinishType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DecalStickersInShadedDisplay(self) -> bool:
        """
        Getter for property: (bool) DecalStickersInShadedDisplay
         Returns the decal stickers in shaded display flag.  
             
         
        """
        pass
    @DecalStickersInShadedDisplay.setter
    def DecalStickersInShadedDisplay(self, decalStickersInShadedDisplay: bool):
        """
        Setter for property: (bool) DecalStickersInShadedDisplay
         Returns the decal stickers in shaded display flag.  
             
         
        """
        pass
    @property
    def EnableFlatShading(self) -> bool:
        """
        Getter for property: (bool) EnableFlatShading
         Returns    
            
         
        """
        pass
    @EnableFlatShading.setter
    def EnableFlatShading(self, enableFlatShading: bool):
        """
        Setter for property: (bool) EnableFlatShading
         Returns    
            
         
        """
        pass
    @property
    def EnableMaterialsInShadedMode(self) -> bool:
        """
        Getter for property: (bool) EnableMaterialsInShadedMode
         Returns the materials in shaded mode flag.  
             
         
        """
        pass
    @EnableMaterialsInShadedMode.setter
    def EnableMaterialsInShadedMode(self, materialsInShadedMode: bool):
        """
        Setter for property: (bool) EnableMaterialsInShadedMode
         Returns the materials in shaded mode flag.  
             
         
        """
        pass
    @property
    def FinishEffectInShadedMode(self) -> SessionVisualizationVisual.FinishEffect:
        """
        Getter for property: ( SessionVisualizationVisual.FinishEffect NXOpen.P) FinishEffectInShadedMode
         Returns the finished effects in shaded mode flag.  
          
            This settings applies all shaded views of all parts in a session.  This is a transient setting.
              
         
        """
        pass
    @FinishEffectInShadedMode.setter
    def FinishEffectInShadedMode(self, finishEffectInShadedMode: SessionVisualizationVisual.FinishEffect):
        """
        Setter for property: ( SessionVisualizationVisual.FinishEffect NXOpen.P) FinishEffectInShadedMode
         Returns the finished effects in shaded mode flag.  
          
            This settings applies all shaded views of all parts in a session.  This is a transient setting.
              
         
        """
        pass
    @property
    def FullSceneAntialiasing(self) -> bool:
        """
        Getter for property: (bool) FullSceneAntialiasing
         Returns the scene antialiasing flag.  
             
         
        """
        pass
    @FullSceneAntialiasing.setter
    def FullSceneAntialiasing(self, full_scene_antialiasing: bool):
        """
        Setter for property: (bool) FullSceneAntialiasing
         Returns the scene antialiasing flag.  
             
         
        """
        pass
    @property
    def GlobalFinish(self) -> SessionVisualizationVisual.GlobalFinishType:
        """
        Getter for property: ( SessionVisualizationVisual.GlobalFinishType NXOpen.P) GlobalFinish
         Returns the global finished type.  
           
                Global finish type is applied to all shaded views of all parts in a session.
                  
                See  NXOpen::Preferences::SessionVisualizationVisual::FinishEffectInShadedMode  regarding when this setting is used.
                  
              
         
        """
        pass
    @GlobalFinish.setter
    def GlobalFinish(self, globalFinishType: SessionVisualizationVisual.GlobalFinishType):
        """
        Setter for property: ( SessionVisualizationVisual.GlobalFinishType NXOpen.P) GlobalFinish
         Returns the global finished type.  
           
                Global finish type is applied to all shaded views of all parts in a session.
                  
                See  NXOpen::Preferences::SessionVisualizationVisual::FinishEffectInShadedMode  regarding when this setting is used.
                  
              
         
        """
        pass
    @property
    def LineAntialiasing(self) -> bool:
        """
        Getter for property: (bool) LineAntialiasing
         Returns the line antialiasing flag.  
           True value specifies that lines, curves, and edges are drawn more smoothly   
         
        """
        pass
    @LineAntialiasing.setter
    def LineAntialiasing(self, line_antialiasing: bool):
        """
        Setter for property: (bool) LineAntialiasing
         Returns the line antialiasing flag.  
           True value specifies that lines, curves, and edges are drawn more smoothly   
         
        """
        pass
    @property
    def ReduceEdgeBleedThrough(self) -> bool:
        """
        Getter for property: (bool) ReduceEdgeBleedThrough
         Returns the reduce edge bleed-through flag.  
          
                True indicates that Show Line Widths, Edge Emphasis, and Line Antialising settings
                are overriden so as to minimize the effects of edges bleeding through surfaces.   
         
        """
        pass
    @ReduceEdgeBleedThrough.setter
    def ReduceEdgeBleedThrough(self, reduce_edge_bleed_through: bool):
        """
        Setter for property: (bool) ReduceEdgeBleedThrough
         Returns the reduce edge bleed-through flag.  
          
                True indicates that Show Line Widths, Edge Emphasis, and Line Antialising settings
                are overriden so as to minimize the effects of edges bleeding through surfaces.   
         
        """
        pass
    @property
    def Translucency(self) -> bool:
        """
        Getter for property: (bool) Translucency
         Returns the translucency flag.  
           True value specifies that each shaded object is drawn with the translucency setting 
            specified with Edit-\Object Display. False value specify that all objects in Fully Shaded or Partially Shaded 
            views appear opaque, regardless of their individual translucency settings.    
         
        """
        pass
    @Translucency.setter
    def Translucency(self, translucency: bool):
        """
        Setter for property: (bool) Translucency
         Returns the translucency flag.  
           True value specifies that each shaded object is drawn with the translucency setting 
            specified with Edit-\Object Display. False value specify that all objects in Fully Shaded or Partially Shaded 
            views appear opaque, regardless of their individual translucency settings.    
         
        """
        pass
import NXOpen
class SessionWorkPlane(NXOpen.Object): 
    """ Represents the set of WorkPlane preferences applicable to session """
    class ObjectDisplay(Enum):
        """
        Members Include: 
         |Normal|  Normal Display 
         |DimAndSelectable|  Dim and Selectable 
         |DimAndNonSelectable|  Dim and Non Selectable 

        """
        Normal: int
        DimAndSelectable: int
        DimAndNonSelectable: int
        @staticmethod
        def ValueOf(value: int) -> SessionWorkPlane.ObjectDisplay:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ObjectOffWorkPlane(self) -> SessionWorkPlane.ObjectDisplay:
        """
        Getter for property: ( SessionWorkPlane.ObjectDisplay NXOpen.P) ObjectOffWorkPlane
         Returns the object off work plane.  
           Comes under Display tab. This preference is to de-emphasize or "dim" all objects in the 
            work plane.   
         
        """
        pass
    @ObjectOffWorkPlane.setter
    def ObjectOffWorkPlane(self, object_off_work_plane: SessionWorkPlane.ObjectDisplay):
        """
        Setter for property: ( SessionWorkPlane.ObjectDisplay NXOpen.P) ObjectOffWorkPlane
         Returns the object off work plane.  
           Comes under Display tab. This preference is to de-emphasize or "dim" all objects in the 
            work plane.   
         
        """
        pass
class ShadingRenderingStyleOption(Enum):
    """
    Members Include: 
     |FullyShaded|  Fully shaded 
     |PartiallyShaded|  Partially Shaded 
     |Wireframe|  Wireframe 

    """
    FullyShaded: int
    PartiallyShaded: int
    Wireframe: int
    @staticmethod
    def ValueOf(value: int) -> ShadingRenderingStyleOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class ShadingToleranceOption(Enum):
    """
    Members Include: 
     |Coarse|  Coarse 
     |Standard|  Standard 
     |Fine|  Fine 
     |ExtraFine|  Extra Fine 
     |UltraFine|  Ultra Fine 
     |Customize|  Customize 

    """
    Coarse: int
    Standard: int
    Fine: int
    ExtraFine: int
    UltraFine: int
    Customize: int
    @staticmethod
    def ValueOf(value: int) -> ShadingToleranceOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class ShadingViewPreferences(NXOpen.Object): 
    """ Represents set of Shading View Preferences applicable to drafting views. """
    @property
    def CustomAngleTolerance(self) -> float:
        """
        Getter for property: (float) CustomAngleTolerance
         Returns the custom angle tolerance.  
            
         
        """
        pass
    @CustomAngleTolerance.setter
    def CustomAngleTolerance(self, custom_angle_tolerance: float):
        """
        Setter for property: (float) CustomAngleTolerance
         Returns the custom angle tolerance.  
            
         
        """
        pass
    @property
    def CustomEdgeTolerance(self) -> float:
        """
        Getter for property: (float) CustomEdgeTolerance
         Returns the custom edge tolerance.  
            
         
        """
        pass
    @CustomEdgeTolerance.setter
    def CustomEdgeTolerance(self, custom_edge_tolerance: float):
        """
        Setter for property: (float) CustomEdgeTolerance
         Returns the custom edge tolerance.  
            
         
        """
        pass
    @property
    def CustomFaceTolerance(self) -> float:
        """
        Getter for property: (float) CustomFaceTolerance
         Returns the custom face tolerance.  
            
         
        """
        pass
    @CustomFaceTolerance.setter
    def CustomFaceTolerance(self, custom_face_tolerance: float):
        """
        Setter for property: (float) CustomFaceTolerance
         Returns the custom face tolerance.  
            
         
        """
        pass
    @property
    def OverrideHiddenWireframeColor(self) -> int:
        """
        Getter for property: (int) OverrideHiddenWireframeColor
         Returns the hidden wireframe override color.  
           The value should be between 1 and 216.  
         
        """
        pass
    @OverrideHiddenWireframeColor.setter
    def OverrideHiddenWireframeColor(self, overrideHiddenWireframeColor: int):
        """
        Setter for property: (int) OverrideHiddenWireframeColor
         Returns the hidden wireframe override color.  
           The value should be between 1 and 216.  
         
        """
        pass
    @property
    def OverrideVisibleWireframeColor(self) -> int:
        """
        Getter for property: (int) OverrideVisibleWireframeColor
         Returns the visible wireframe override color.  
           The value should be between 1 and 216.  
         
        """
        pass
    @OverrideVisibleWireframeColor.setter
    def OverrideVisibleWireframeColor(self, overrideVisibleWireframeColor: int):
        """
        Setter for property: (int) OverrideVisibleWireframeColor
         Returns the visible wireframe override color.  
           The value should be between 1 and 216.  
         
        """
        pass
    @property
    def RenderingStyle(self) -> ShadingRenderingStyleOption:
        """
        Getter for property: ( ShadingRenderingStyleOption NXOpen.P) RenderingStyle
         Returns the rendering style.  
            
         
        """
        pass
    @RenderingStyle.setter
    def RenderingStyle(self, rendering_style_option: ShadingRenderingStyleOption):
        """
        Setter for property: ( ShadingRenderingStyleOption NXOpen.P) RenderingStyle
         Returns the rendering style.  
            
         
        """
        pass
    @property
    def ShadedCutFaceColor(self) -> int:
        """
        Getter for property: (int) ShadedCutFaceColor
         Returns the shaded cut face color.  
           The value should be between 1 and 216.   
         
        """
        pass
    @ShadedCutFaceColor.setter
    def ShadedCutFaceColor(self, shaded_cut_face_color: int):
        """
        Setter for property: (int) ShadedCutFaceColor
         Returns the shaded cut face color.  
           The value should be between 1 and 216.   
         
        """
        pass
    @property
    def ShadingTolerance(self) -> ShadingToleranceOption:
        """
        Getter for property: ( ShadingToleranceOption NXOpen.P) ShadingTolerance
         Returns the shading tolerance.  
            
         
        """
        pass
    @ShadingTolerance.setter
    def ShadingTolerance(self, shading_tolerance: ShadingToleranceOption):
        """
        Setter for property: ( ShadingToleranceOption NXOpen.P) ShadingTolerance
         Returns the shading tolerance.  
            
         
        """
        pass
    @property
    def Shininess(self) -> float:
        """
        Getter for property: (float) Shininess
         Returns the shininess tolerance.  
            
         
        """
        pass
    @Shininess.setter
    def Shininess(self, shininess_tolerance: float):
        """
        Setter for property: (float) Shininess
         Returns the shininess tolerance.  
            
         
        """
        pass
    @property
    def TwoSidedLight(self) -> bool:
        """
        Getter for property: (bool) TwoSidedLight
         Returns the two sided light toggle data.  
            
         
        """
        pass
    @TwoSidedLight.setter
    def TwoSidedLight(self, two_sided_light: bool):
        """
        Setter for property: (bool) TwoSidedLight
         Returns the two sided light toggle data.  
            
         
        """
        pass
import NXOpen
import NXOpen.Features.SheetMetal
class SheetMetalPreferencesBuilder(NXOpen.Builder): 
    """ Represents a Preferences.SheetMetalPreferencesBuilder builder """
    class BendDefinitionMethodOptions(Enum):
        """
        Members Include: 
         |NeutralFactorValue|  The neutral factor value method
         |BendTable|  The bend table method
         |BendAllowanceFormula|  The bend allowance formula method
         |MaterialTable|  The material table method
         |ToolTable|  The tool table method
         |BendAllowanceTable|  The bend allowance table method
         |BendDeductionTable|  The bend deduction table method
         |BendDeductionFormula|  The bend deduction formula method
         |Din6935Formula|  The DIN6935 formula method

        """
        NeutralFactorValue: int
        BendTable: int
        BendAllowanceFormula: int
        MaterialTable: int
        ToolTable: int
        BendAllowanceTable: int
        BendDeductionTable: int
        BendDeductionFormula: int
        Din6935Formula: int
        @staticmethod
        def ValueOf(value: int) -> SheetMetalPreferencesBuilder.BendDefinitionMethodOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FlatPatternCalloutOrientationTypes(Enum):
        """
        Members Include: 
         |Leadered|  Leadered 
         |Aligned|  Aligned 

        """
        Leadered: int
        Aligned: int
        @staticmethod
        def ValueOf(value: int) -> SheetMetalPreferencesBuilder.FlatPatternCalloutOrientationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FlatPatternObjectTypes(Enum):
        """
        Members Include: 
         |BendUpCenterLine|  
         |BendDownCenterLine|  
         |BendTangentLine|  
         |OuterMoldLine|  
         |InnerMoldLine|  
         |ExteriorCurves|  
         |InteriorCutoutCurves|  
         |InteriorFeatureCurves|  
         |StrikePoint|  
         |LighteningHoleCenter|  
         |JoggleLine|  
         |AddedTopGeometry|  
         |AddedBottomGeometry|  
         |ToolMarker|  
         |Hole|  
         |CenterMark|  

        """
        BendUpCenterLine: int
        BendDownCenterLine: int
        BendTangentLine: int
        OuterMoldLine: int
        InnerMoldLine: int
        ExteriorCurves: int
        InteriorCutoutCurves: int
        InteriorFeatureCurves: int
        StrikePoint: int
        LighteningHoleCenter: int
        JoggleLine: int
        AddedTopGeometry: int
        AddedBottomGeometry: int
        ToolMarker: int
        Hole: int
        CenterMark: int
        @staticmethod
        def ValueOf(value: int) -> SheetMetalPreferencesBuilder.FlatPatternObjectTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ParameterEntryTypes(Enum):
        """
        Members Include: 
         |Value|  The manual Value entry method
         |MaterialTable|  The Material Table entry method
         |ToolIdTable|  The Tool ID Table entry method

        """
        Value: int
        MaterialTable: int
        ToolIdTable: int
        @staticmethod
        def ValueOf(value: int) -> SheetMetalPreferencesBuilder.ParameterEntryTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TabCurveTypes(Enum):
        """
        Members Include: 
         |BendCenterLine|  
         |BendTangentLine|  

        """
        BendCenterLine: int
        BendTangentLine: int
        @staticmethod
        def ValueOf(value: int) -> SheetMetalPreferencesBuilder.TabCurveTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FlatPatternCalloutTypeDisplay:
        """
         The members of the following structure are the display data for a
                    callout in a flat pattern drawing member view. 
         SheetMetalPreferencesBuilderFlatPatternCalloutTypeDisplay_Struct NXOpen.P is an alias for  SheetMetalPreferencesBuilder.FlatPatternCalloutTypeDisplay NXOpen.P.
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
        def IsEnabled(self) -> bool:
            """
            Getter for property IsEnabled
            Enabled status for the callout type.

            """
            pass
        @IsEnabled.setter
        def IsEnabled(self, value: bool):
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
         SheetMetalPreferencesBuilderFlatPatternObjectTypeDisplay_Struct NXOpen.P is an alias for  SheetMetalPreferencesBuilder.FlatPatternObjectTypeDisplay NXOpen.P.
        """
        @property
        def Type(self) -> SheetMetalPreferencesBuilder.FlatPatternObjectTypes:
            """
            Getter for property Type
            Object type

            """
            pass
        @Type.setter
        def Type(self, value: SheetMetalPreferencesBuilder.FlatPatternObjectTypes):
            """
            Getter for property Type
            Object type
            Setter for property Type
            Object type

            """
            pass
        @property
        def IsEnabled(self) -> bool:
            """
            Getter for property IsEnabled
            Enabled status for the object type

            """
            pass
        @IsEnabled.setter
        def IsEnabled(self, value: bool):
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
        def Layer(self) -> int:
            """
            Getter for property Layer
            Object Layer

            """
            pass
        @Layer.setter
        def Layer(self, value: int):
            """
            Getter for property Layer
            Object Layer
            Setter for property Layer
            Object Layer

            """
            pass
        @property
        def Font(self) -> NXOpen.DisplayableObject.ObjectFont:
            """
            Getter for property Font
            Object font

            """
            pass
        @Font.setter
        def Font(self, value: NXOpen.DisplayableObject.ObjectFont):
            """
            Getter for property Font
            Object font
            Setter for property Font
            Object font

            """
            pass
        @property
        def Width(self) -> NXOpen.DisplayableObject.ObjectWidth:
            """
            Getter for property Width
            Object width

            """
            pass
        @Width.setter
        def Width(self, value: NXOpen.DisplayableObject.ObjectWidth):
            """
            Getter for property Width
            Object width
            Setter for property Width
            Object width

            """
            pass
    class TabCurvesDisplayData:
        """
         The members of the following structure are the display data of a tab curve type. 
         SheetMetalPreferencesBuilderTabCurvesDisplayData_Struct NXOpen.P is an alias for  SheetMetalPreferencesBuilder.TabCurvesDisplayData NXOpen.P.
        """
        @property
        def Type(self) -> SheetMetalPreferencesBuilder.TabCurveTypes:
            """
            Getter for property Type
            Curve type

            """
            pass
        @Type.setter
        def Type(self, value: SheetMetalPreferencesBuilder.TabCurveTypes):
            """
            Getter for property Type
            Curve type
            Setter for property Type
            Curve type

            """
            pass
        @property
        def IsEnabled(self) -> int:
            """
            Getter for property IsEnabled
            Enabled status of the curve type

            """
            pass
        @IsEnabled.setter
        def IsEnabled(self, value: int):
            """
            Getter for property IsEnabled
            Enabled status of the curve type
            Setter for property IsEnabled
            Enabled status of the curve type

            """
            pass
        @property
        def Color(self) -> int:
            """
            Getter for property Color
            Curve color

            """
            pass
        @Color.setter
        def Color(self, value: int):
            """
            Getter for property Color
            Curve color
            Setter for property Color
            Curve color

            """
            pass
        @property
        def Font(self) -> NXOpen.DisplayableObject.ObjectFont:
            """
            Getter for property Font
            Curve font

            """
            pass
        @Font.setter
        def Font(self, value: NXOpen.DisplayableObject.ObjectFont):
            """
            Getter for property Font
            Curve font
            Setter for property Font
            Curve font

            """
            pass
        @property
        def Width(self) -> NXOpen.DisplayableObject.ObjectWidth:
            """
            Getter for property Width
            Curve width

            """
            pass
        @Width.setter
        def Width(self, value: NXOpen.DisplayableObject.ObjectWidth):
            """
            Getter for property Width
            Curve width
            Setter for property Width
            Curve width

            """
            pass
    @property
    def BendAllowanceFormula(self) -> str:
        """
        Getter for property: (str) BendAllowanceFormula
         Returns the bend allowance formula   
            
         
        """
        pass
    @BendAllowanceFormula.setter
    def BendAllowanceFormula(self, bendAllowanceFormula: str):
        """
        Setter for property: (str) BendAllowanceFormula
         Returns the bend allowance formula   
            
         
        """
        pass
    @property
    def BendDeductionFormula(self) -> str:
        """
        Getter for property: (str) BendDeductionFormula
         Returns the bend deduction formula   
            
         
        """
        pass
    @BendDeductionFormula.setter
    def BendDeductionFormula(self, bendDeductionFormula: str):
        """
        Setter for property: (str) BendDeductionFormula
         Returns the bend deduction formula   
            
         
        """
        pass
    @property
    def BendRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BendRadius
         Returns the bend radius   
            
         
        """
        pass
    @property
    def BendReliefDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BendReliefDepth
         Returns the bend relief depth   
            
         
        """
        pass
    @property
    def BendReliefWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BendReliefWidth
         Returns the bend relief width   
            
         
        """
        pass
    @property
    def DeviationalTolerance(self) -> float:
        """
        Getter for property: (float) DeviationalTolerance
         Returns the flat pattern treatment deviational tolerance.  
           This is needed only when  SimplifyBSplines  is let to true.   
         
        """
        pass
    @DeviationalTolerance.setter
    def DeviationalTolerance(self, deviationalTolerance: float):
        """
        Setter for property: (float) DeviationalTolerance
         Returns the flat pattern treatment deviational tolerance.  
           This is needed only when  SimplifyBSplines  is let to true.   
         
        """
        pass
    @property
    def FlatPatternHoleTreatmentDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlatPatternHoleTreatmentDiameter
         Returns the flat pattern treatment hole diameter   
            
         
        """
        pass
    @property
    def FlatPatternInsideCornerTreatmentValue(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlatPatternInsideCornerTreatmentValue
         Returns the flat pattern treatment inside value   
            
         
        """
        pass
    @property
    def FlatPatternOutsideCornerTreatmentValue(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlatPatternOutsideCornerTreatmentValue
         Returns the flat pattern treatment outside value   
            
         
        """
        pass
    @property
    def FlatSolidColor(self) -> int:
        """
        Getter for property: (int) FlatSolidColor
         Returns the flat solid color   
            
         
        """
        pass
    @FlatSolidColor.setter
    def FlatSolidColor(self, flatSolidColor: int):
        """
        Setter for property: (int) FlatSolidColor
         Returns the flat solid color   
            
         
        """
        pass
    @property
    def FlatSolidLayer(self) -> int:
        """
        Getter for property: (int) FlatSolidLayer
         Returns the flat solid layer   
            
         
        """
        pass
    @FlatSolidLayer.setter
    def FlatSolidLayer(self, flatSolidLayer: int):
        """
        Setter for property: (int) FlatSolidLayer
         Returns the flat solid layer   
            
         
        """
        pass
    @property
    def HoleTreatmentType(self) -> NXOpen.Features.SheetMetal.FeatureProperty:
        """
        Getter for property: ( NXOpen.Features.SheetMetal.FeatureProperty) HoleTreatmentType
         Returns the flat pattern hole treatment type   
            
         
        """
        pass
    @HoleTreatmentType.setter
    def HoleTreatmentType(self, holeTreatmentType: NXOpen.Features.SheetMetal.FeatureProperty):
        """
        Setter for property: ( NXOpen.Features.SheetMetal.FeatureProperty) HoleTreatmentType
         Returns the flat pattern hole treatment type   
            
         
        """
        pass
    @property
    def InsideCornerTreatmentType(self) -> NXOpen.Features.SheetMetal.FeatureProperty:
        """
        Getter for property: ( NXOpen.Features.SheetMetal.FeatureProperty) InsideCornerTreatmentType
         Returns the flat pattern inside treatment type   
            
         
        """
        pass
    @InsideCornerTreatmentType.setter
    def InsideCornerTreatmentType(self, insideCornerTreatmentType: NXOpen.Features.SheetMetal.FeatureProperty):
        """
        Setter for property: ( NXOpen.Features.SheetMetal.FeatureProperty) InsideCornerTreatmentType
         Returns the flat pattern inside treatment type   
            
         
        """
        pass
    @property
    def IntegratePhysicalMaterialLibrary(self) -> bool:
        """
        Getter for property: (bool) IntegratePhysicalMaterialLibrary
         Returns whether to integrate the physical material library   
            
         
        """
        pass
    @IntegratePhysicalMaterialLibrary.setter
    def IntegratePhysicalMaterialLibrary(self, integratePhysicalMaterialLibrary: bool):
        """
        Setter for property: (bool) IntegratePhysicalMaterialLibrary
         Returns whether to integrate the physical material library   
            
         
        """
        pass
    @property
    def JoggleDepthThreshold(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) JoggleDepthThreshold
         Returns the joggle depth threshold   
            
         
        """
        pass
    @property
    def JoggleDistanceThreshold(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) JoggleDistanceThreshold
         Returns the joggle distance threshold   
            
         
        """
        pass
    @property
    def JoggleOffsetRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) JoggleOffsetRadius
         Returns the joggle offset radius   
            
         
        """
        pass
    @property
    def JoggleStationaryRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) JoggleStationaryRadius
         Returns the joggle stationary radius   
            
         
        """
        pass
    @property
    def MaintainCircularShapeForHoles(self) -> bool:
        """
        Getter for property: (bool) MaintainCircularShapeForHoles
         Returns whether the circular shape for holes in the flat pattern should be maintained.  
             
         
        """
        pass
    @MaintainCircularShapeForHoles.setter
    def MaintainCircularShapeForHoles(self, maintainCircularShapeForHoles: bool):
        """
        Setter for property: (bool) MaintainCircularShapeForHoles
         Returns whether the circular shape for holes in the flat pattern should be maintained.  
             
         
        """
        pass
    @property
    def MaterialThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaterialThickness
         Returns the material thickness   
            
         
        """
        pass
    @property
    def MinimumArc(self) -> float:
        """
        Getter for property: (float) MinimumArc
         Returns the flat pattern treatment minimum arc.  
           This is needed only when  SimplifyBSplines  is let to true.   
         
        """
        pass
    @MinimumArc.setter
    def MinimumArc(self, minimumArc: float):
        """
        Setter for property: (float) MinimumArc
         Returns the flat pattern treatment minimum arc.  
           This is needed only when  SimplifyBSplines  is let to true.   
         
        """
        pass
    @property
    def MinimumToolClearance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumToolClearance
         Returns the minimum tool clearance expression   
            
         
        """
        pass
    @property
    def MinimumWebLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumWebLength
         Returns the minimum web length expression   
            
         
        """
        pass
    @property
    def NeutralFactor(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NeutralFactor
         Returns the neutral factor   
            
         
        """
        pass
    @property
    def OutsideCornerTreatmentType(self) -> NXOpen.Features.SheetMetal.FeatureProperty:
        """
        Getter for property: ( NXOpen.Features.SheetMetal.FeatureProperty) OutsideCornerTreatmentType
         Returns the flat pattern outside treatment type   
            
         
        """
        pass
    @OutsideCornerTreatmentType.setter
    def OutsideCornerTreatmentType(self, outsideCornerTreatmentType: NXOpen.Features.SheetMetal.FeatureProperty):
        """
        Setter for property: ( NXOpen.Features.SheetMetal.FeatureProperty) OutsideCornerTreatmentType
         Returns the flat pattern outside treatment type   
            
         
        """
        pass
    @property
    def ParameterEntryType(self) -> SheetMetalPreferencesBuilder.ParameterEntryTypes:
        """
        Getter for property: ( SheetMetalPreferencesBuilder.ParameterEntryTypes NXOpen.P) ParameterEntryType
         Returns the parameter entry type   
            
         
        """
        pass
    @ParameterEntryType.setter
    def ParameterEntryType(self, parameterEntryType: SheetMetalPreferencesBuilder.ParameterEntryTypes):
        """
        Setter for property: ( SheetMetalPreferencesBuilder.ParameterEntryTypes NXOpen.P) ParameterEntryType
         Returns the parameter entry type   
            
         
        """
        pass
    @property
    def RemoveBendReliefs(self) -> bool:
        """
        Getter for property: (bool) RemoveBendReliefs
         Returns whether the bend reliefs in the flat pattern should be removed.  
             
         
        """
        pass
    @RemoveBendReliefs.setter
    def RemoveBendReliefs(self, removeBendReliefs: bool):
        """
        Setter for property: (bool) RemoveBendReliefs
         Returns whether the bend reliefs in the flat pattern should be removed.  
             
         
        """
        pass
    @property
    def ShowLouverCutoutCurvesAsInteriorCutout(self) -> bool:
        """
        Getter for property: (bool) ShowLouverCutoutCurvesAsInteriorCutout
         Returns whether louver cutout curves in flat pattern should be shown as interior cutout curves.  
             
         
        """
        pass
    @ShowLouverCutoutCurvesAsInteriorCutout.setter
    def ShowLouverCutoutCurvesAsInteriorCutout(self, showLouverCutoutCurvesAsInteriorCutout: bool):
        """
        Setter for property: (bool) ShowLouverCutoutCurvesAsInteriorCutout
         Returns whether louver cutout curves in flat pattern should be shown as interior cutout curves.  
             
         
        """
        pass
    @property
    def ShowSingleBendLineForAlignedBends(self) -> bool:
        """
        Getter for property: (bool) ShowSingleBendLineForAlignedBends
         Returns whether single continuous bend lines should get created in case of aligned cylindrical bends.  
             
         
        """
        pass
    @ShowSingleBendLineForAlignedBends.setter
    def ShowSingleBendLineForAlignedBends(self, showSingleBendLineForAlignedBends: bool):
        """
        Setter for property: (bool) ShowSingleBendLineForAlignedBends
         Returns whether single continuous bend lines should get created in case of aligned cylindrical bends.  
             
         
        """
        pass
    @property
    def SimplifyBSplines(self) -> bool:
        """
        Getter for property: (bool) SimplifyBSplines
         Returns whether the bspline curves in the flat pattern should be simplified.  
             
         
        """
        pass
    @SimplifyBSplines.setter
    def SimplifyBSplines(self, simplifyBSplinesFlag: bool):
        """
        Setter for property: (bool) SimplifyBSplines
         Returns whether the bspline curves in the flat pattern should be simplified.  
             
         
        """
        pass
    def GetBendDefinitionMethod(self) -> SheetMetalPreferencesBuilder.BendDefinitionMethodOptions:
        """
         Returns bend definition method 
         Returns bendDefinitionMethod ( SheetMetalPreferencesBuilder.BendDefinitionMethodOptions NXOpen.P): .
        """
        pass
    def GetBendTable(self) -> str:
        """
         Returns bend table 
         Returns bendTable (str): .
        """
        pass
    def GetFlatPatternAllCalloutTypeDisplay(self) -> List[SheetMetalPreferencesBuilder.FlatPatternCalloutTypeDisplay]:
        """
         Returns the dialog names, identifiers, and enabled status for all the available callout types. 
         Returns displayData ( SheetMetalPreferencesBuilder.FlatPatternCalloutTypeDisplay List[NXOpen):  Array of structures with the object type display data. .
        """
        pass
    def GetFlatPatternAllObjectTypeDisplay(self) -> List[SheetMetalPreferencesBuilder.FlatPatternObjectTypeDisplay]:
        """
         Returns the types, colors, fonts, widths, and enabled status for all the 
                available flat pattern display object types. 
         Returns displayData ( SheetMetalPreferencesBuilder.FlatPatternObjectTypeDisplay List[NXOpen):  Array of structures with the object type display data. .
        """
        pass
    def GetFlatPatternCalloutOrientationType(self) -> SheetMetalPreferencesBuilder.FlatPatternCalloutOrientationTypes:
        """
         Returns the orientation type for flat pattern callouts. 
         Returns orientation ( SheetMetalPreferencesBuilder.FlatPatternCalloutOrientationTypes NXOpen.P):  The orientation type for the flat pattern callouts. .
        """
        pass
    def GetFlatPatternCalloutTypeContents(self, calloutType: str) -> List[str]:
        """
         Returns the contents for a callout type. 
         Returns contents (List[str]):  The contents for the callout type. .
        """
        pass
    def GetFlatPatternCalloutTypeDisplay(self, calloutType: str) -> SheetMetalPreferencesBuilder.FlatPatternCalloutTypeDisplay:
        """
         Returns the display data for a callout type. The name member of the
                    NXOpen.Preferences.PartFlexiblePrintedCircuitDesign.FlatPatternCalloutTypeDisplay
                    is separately allocated from the calloutType argument string.
                    In some cases the new string will contain an extended form of the callout_type passed in, 
                    and that form should be used for subsequent JA calls, without modification. 
         Returns displayData ( SheetMetalPreferencesBuilder.FlatPatternCalloutTypeDisplay NXOpen.P):  The display data for the callout type. .
        """
        pass
    def GetFlatPatternObjectTypeDisplay(self, objectType: SheetMetalPreferencesBuilder.FlatPatternObjectTypes) -> SheetMetalPreferencesBuilder.FlatPatternObjectTypeDisplay:
        """
         Returns display data for a given flat pattern object type 
         Returns displayData ( SheetMetalPreferencesBuilder.FlatPatternObjectTypeDisplay NXOpen.P):  The display data for the flat pattern object type. .
        """
        pass
    def GetMaterialName(self) -> str:
        """
         Returns the name of the material saved with the part 
         Returns materialName (str): .
        """
        pass
    def GetMaterialNames(self) -> List[str]:
        """
         Returns the material names defined in the material standards table 
         Returns materialNames (List[str]): .
        """
        pass
    def GetMaterialProperties(self, materialName: str) -> Tuple[List[str], List[str]]:
        """
         Returns the properties of the given material  
         Returns A tuple consisting of (propertyValues, propertyNames). 
         - propertyValues is: List[str].property Values .
         - propertyNames is: List[str].property Names .

        """
        pass
    def GetSecondaryToolName(self) -> str:
        """
         Returns secondary tool name 
         Returns secondaryToolName (str): .
        """
        pass
    def GetTabCurveDisplayData(self, curveType: SheetMetalPreferencesBuilder.TabCurveTypes) -> SheetMetalPreferencesBuilder.TabCurvesDisplayData:
        """
         Returns display data for a given tab curve type. 
         Returns displayData ( SheetMetalPreferencesBuilder.TabCurvesDisplayData NXOpen.P):  The display data for the tab curve. .
        """
        pass
    def GetToolName(self) -> str:
        """
         Returns tool name 
         Returns toolName (str):  The name of the tool saved with the part .
        """
        pass
    def GetToolNames(self) -> List[str]:
        """
         Returns the tool names defined in the material standards table 
         Returns toolNames (List[str]): .
        """
        pass
    def GetToolProperties(self, toolName: str) -> Tuple[List[str], List[str]]:
        """
         Returns the tool properties saved with the part 
         Returns A tuple consisting of (propertyValues, propertyNames). 
         - propertyValues is: List[str].property Values .
         - propertyNames is: List[str].property Names .

        """
        pass
    def SetBendDefinitionMethod(self, bendDefinitionMethod: SheetMetalPreferencesBuilder.BendDefinitionMethodOptions) -> None:
        """
         Sets bend definition method 
        """
        pass
    def SetBendTable(self, bendTable: str) -> None:
        """
         Sets bend table 
        """
        pass
    def SetFlatPatternCalloutOrientationType(self, orientation: SheetMetalPreferencesBuilder.FlatPatternCalloutOrientationTypes) -> None:
        """
         Sets the orientation type for flat pattern callouts. 
        """
        pass
    def SetFlatPatternCalloutTypeContents(self, calloutType: str, contents: List[str]) -> None:
        """
         Sets the contents for a callout type. 
        """
        pass
    def SetFlatPatternCalloutTypeDisplay(self, calloutType: str, displayData: SheetMetalPreferencesBuilder.FlatPatternCalloutTypeDisplay) -> None:
        """
         Sets the display data for a callout type. 
        """
        pass
    def SetFlatPatternObjectTypeDisplay(self, objectType: SheetMetalPreferencesBuilder.FlatPatternObjectTypes, displayData: SheetMetalPreferencesBuilder.FlatPatternObjectTypeDisplay) -> None:
        """
         Sets display data for a given flat pattern object type 
        """
        pass
    def SetMaterial(self, materialName: str) -> None:
        """
         Sets the material to the part 
        """
        pass
    def SetSecondaryToolName(self, secondaryToolName: str) -> None:
        """
         Sets secondary tool name 
        """
        pass
    def SetTabCurveDisplayData(self, curveType: SheetMetalPreferencesBuilder.TabCurveTypes, displayData: SheetMetalPreferencesBuilder.TabCurvesDisplayData) -> None:
        """
         Sets display data for a given tab curve type. 
        """
        pass
    def SetToolName(self, toolName: str) -> None:
        """
         Sets tool name 
        """
        pass
import NXOpen
import NXOpen.Features.SheetMetal
class SheetMetalPreferencesManager(NXOpen.Object): 
    """ Represents a collection of sbsm preference builders."""
    def CreateSheetMetalPreferencesBuilder(self) -> SheetMetalPreferencesBuilder:
        """
         Creates a NXOpen.Preferences.SheetMetalPreferencesBuilder 
         Returns builder ( SheetMetalPreferencesBuilder NXOpen.P): .
        """
        pass
    def GetBendAllowanceFormula(self) -> str:
        """
         Returns the bend allowance formula 
         Returns bendAllowanceFormula (str):  bend allowance formula.
        """
        pass
    def GetBendDeductionFormula(self) -> str:
        """
         Returns the bend deduction formula 
         Returns bendDeductionFormula (str):  bend deduction formula.
        """
        pass
    def GetBendDefinitionMethod(self) -> SheetMetalPreferencesBuilder.BendDefinitionMethodOptions:
        """
         Returns bend definition method 
         Returns bendDefinitionMethod ( SheetMetalPreferencesBuilder.BendDefinitionMethodOptions NXOpen.P): .
        """
        pass
    def GetBendRadius(self) -> NXOpen.Expression:
        """
         Returns the bend radius expression tag. This API is only to get the expression from the preferences, 
                    to modify any of the values use Preferences.SheetMetalPreferencesBuilder. 
         Returns bendRadius ( NXOpen.Expression):  expression object tag for radius of bend faces.
        """
        pass
    def GetBendReliefDepth(self) -> NXOpen.Expression:
        """
         Returns the bend relief depth expression tag. This API is only to get the expression from the preferences, 
                    to modify any of the values use Preferences.SheetMetalPreferencesBuilder. 
         Returns bendReliefDepth ( NXOpen.Expression):  expression object tag for bend relief depth .
        """
        pass
    def GetBendReliefWidth(self) -> NXOpen.Expression:
        """
         Returns the bend relief width expression tag. This API is only to get the expression from the preferences, 
                    to modify any of the values use Preferences.SheetMetalPreferencesBuilder. 
         Returns bendReliefWidth ( NXOpen.Expression):  expression object tag for bend relief width .
        """
        pass
    def GetBendTable(self) -> str:
        """
         Returns bend table name 
         Returns bendTable (str): .
        """
        pass
    def GetDepthThreshold(self) -> NXOpen.Expression:
        """
         Returns the expression tag of joggle depth threshold value. This API is only to get the expression from the preferences, 
                    to modify any of the values use Preferences.SheetMetalPreferencesBuilder. 
         Returns depthThreshold ( NXOpen.Expression):  expression object tag for joggle depth threshold value .
        """
        pass
    def GetDeviationalTolerance(self) -> float:
        """
         Returns the flat pattern deviational tolerance value 
         Returns deviationalTolerance (float):  flat pattern deviational tolerance value .
        """
        pass
    def GetDistanceThreshold(self) -> NXOpen.Expression:
        """
         Returns the expression tag of joggle distance threshold value. This API is only to get the expression from the preferences, 
                    to modify any of the values use Preferences.SheetMetalPreferencesBuilder. 
         Returns distanceThreshold ( NXOpen.Expression):  expression object tag for joggle distance threshold value .
        """
        pass
    def GetFlatPatternAllCalloutTypeDisplay(self) -> List[SheetMetalPreferencesBuilder.FlatPatternCalloutTypeDisplay]:
        """
         Returns the dialog names, identifiers, and enabled status for all the available callout types. 
         Returns displayData ( SheetMetalPreferencesBuilder.FlatPatternCalloutTypeDisplay List[NXOpen):  Array of structures with the object type display data. .
        """
        pass
    def GetFlatPatternAllObjectTypeDisplay(self) -> List[SheetMetalPreferencesBuilder.FlatPatternObjectTypeDisplay]:
        """
         Returns the types, colors, fonts, widths, and enabled status for all the 
                available flat pattern display object types. 
         Returns displayData ( SheetMetalPreferencesBuilder.FlatPatternObjectTypeDisplay List[NXOpen):  Array of structures with the object type display data. .
        """
        pass
    def GetFlatPatternCalloutOrientationType(self) -> SheetMetalPreferencesBuilder.FlatPatternCalloutOrientationTypes:
        """
         Returns the orientation type for flat pattern callouts. 
         Returns orientation ( SheetMetalPreferencesBuilder.FlatPatternCalloutOrientationTypes NXOpen.P):  The orientation type for the flat pattern callouts. .
        """
        pass
    def GetFlatPatternCalloutTypeContents(self, calloutType: str) -> List[str]:
        """
         Returns the contents for a callout type. 
         Returns contents (List[str]):  The contents for the callout type. .
        """
        pass
    def GetFlatPatternCalloutTypeDisplay(self, calloutType: str) -> SheetMetalPreferencesBuilder.FlatPatternCalloutTypeDisplay:
        """
         Returns the display data for a callout type. The name member of the
                    NXOpen.Preferences.SheetMetalPreferencesBuilder.FlatPatternCalloutTypeDisplay
                    is separately allocated from the calloutType argument string.
                    In some cases the new string will contain an extended form of the callout_type passed in, 
                    and that form should be used for subsequent JA calls, without modification. 
         Returns displayData ( SheetMetalPreferencesBuilder.FlatPatternCalloutTypeDisplay NXOpen.P):  The display data for the callout type. .
        """
        pass
    def GetFlatPatternHoleTreatmentDiameterValue(self) -> NXOpen.Expression:
        """
         Returns the expression tag of flat pattern hole treatment diameter value. This API is only to get the expression from the preferences, 
                    to modify any of the values use Preferences.SheetMetalPreferencesBuilder. 
         Returns holeTreatmentValue ( NXOpen.Expression):  expression object tag for flat pattern hole treatment value .
        """
        pass
    def GetFlatPatternInsideCornerTreatmentValue(self) -> NXOpen.Expression:
        """
         Returns expression tag of the flat pattern inside corner treatment value. This API is only to get the expression from the preferences, 
                    to modify any of the values use Preferences.SheetMetalPreferencesBuilder. 
         Returns insideCornerTreatmentValue ( NXOpen.Expression):  expression object tag for flat pattern inside corner treatment value .
        """
        pass
    def GetFlatPatternObjectTypeDisplay(self, objectType: SheetMetalPreferencesBuilder.FlatPatternObjectTypes) -> SheetMetalPreferencesBuilder.FlatPatternObjectTypeDisplay:
        """
         Returns display data for a given flat pattern object type 
         Returns displayData ( SheetMetalPreferencesBuilder.FlatPatternObjectTypeDisplay NXOpen.P):  The display data for the flat pattern object type. .
        """
        pass
    def GetFlatPatternOutsideCornerTreatmentValue(self) -> NXOpen.Expression:
        """
         Retruns the expression tag of flat pattern outside corner treatment value. This API is only to get the expression from the preferences, 
                    to modify any of the values use Preferences.SheetMetalPreferencesBuilder. 
         Returns outsideCornerTreatmentValue ( NXOpen.Expression):  expression object tag for flat pattern outside corner treatment value .
        """
        pass
    def GetFlatSolidColor(self) -> int:
        """
         Returns the flat solid color 
         Returns flatSolidColor (int): .
        """
        pass
    def GetFlatSolidLayer(self) -> int:
        """
         Returns the flat solid layer 
         Returns flatSolidLayer (int): .
        """
        pass
    def GetHoleTreatmentType(self) -> NXOpen.Features.SheetMetal.FeatureProperty:
        """
         Returns the flat pattern hole treatment type 
         Returns holeTreatmentType ( NXOpen.Features.SheetMetal.FeatureProperty):  hole treatment type .
        """
        pass
    def GetInsideCornerTreatmentType(self) -> NXOpen.Features.SheetMetal.FeatureProperty:
        """
         Returns the flat pattern inside corner treatment type 
         Returns insideCornerTreatmentType ( NXOpen.Features.SheetMetal.FeatureProperty):  inside corner treatment type .
        """
        pass
    def GetIntegratePhysicalMaterialLibrary(self) -> bool:
        """
         Returns whether the physical material library is integrated or not. 
         Returns integratePhysicalMaterialLibrary (bool): .
        """
        pass
    def GetMaintainCircularShapeForHoles(self) -> bool:
        """
         Returns whether the circular shape for holes in the flat pattern is maintained or not. 
         Returns isCircularShapeForHolesMaintained (bool): .
        """
        pass
    def GetMaterialName(self) -> str:
        """
         Returns the name of the material saved with the part 
         Returns materialName (str): .
        """
        pass
    def GetMaterialNames(self) -> List[str]:
        """
         Returns the material names defined in the material standards table 
         Returns materialNames (List[str]): .
        """
        pass
    def GetMaterialProperties(self, materialName: str) -> Tuple[List[str], List[str]]:
        """
         Returns the properties of the given material  
         Returns A tuple consisting of (propertyValues, propertyNames). 
         - propertyValues is: List[str].property Values .
         - propertyNames is: List[str].property Names .

        """
        pass
    def GetMaterialThickness(self) -> NXOpen.Expression:
        """
         Returns the material thickness expression tag. This API is only to get the expression from the preferences, 
                    to modify any of the values use Preferences.SheetMetalPreferencesBuilder. 
         Returns thickness ( NXOpen.Expression):  expression object tag for sheet thickness .
        """
        pass
    def GetMinimumArcTolerance(self) -> float:
        """
         Returns the flat pattern minimum arc tolerance value 
         Returns minArcTolerance (float):  flat pattern minimum arc tolerance value .
        """
        pass
    def GetMinimumToolClearance(self) -> NXOpen.Expression:
        """
         Returns the expression of minimum tool clearance value. This API is only to get the expression from the preferences, 
                    to modify any of the values use Preferences.SheetMetalPreferencesBuilder. 
         Returns minToolClearance ( NXOpen.Expression):  expression object tag for minimum tool clearance value .
        """
        pass
    def GetMinimumWebLength(self) -> NXOpen.Expression:
        """
         Returns the expression of minimum web length value. This API is only to get the expression from the preferences, 
                    to modify any of the values use Preferences.SheetMetalPreferencesBuilder. 
         Returns minWebLength ( NXOpen.Expression):  expression object tag for minimum web length value .
        """
        pass
    def GetNeutralFactor(self) -> NXOpen.Expression:
        """
         Returns neutral factor expression tag. This API is only to get the expression from the preferences, 
                    to modify any of the values use Preferences.SheetMetalPreferencesBuilder. 
         Returns neutralFactor ( NXOpen.Expression):  expression object tag for neutral factor of bend areas .
        """
        pass
    def GetOffsetRadius(self) -> NXOpen.Expression:
        """
         Returns the expression tag of joggle offset radius value. This API is only to get the expression from the preferences, 
                    to modify any of the values use Preferences.SheetMetalPreferencesBuilder. 
         Returns offsetRadius ( NXOpen.Expression):  expression object tag for joggle offset radius value .
        """
        pass
    def GetOutsideCornerTreatmentType(self) -> NXOpen.Features.SheetMetal.FeatureProperty:
        """
         Returns the flat pattern outside corner treatment type 
         Returns outsideCornerTreatmentType ( NXOpen.Features.SheetMetal.FeatureProperty):  outside corner treatment type .
        """
        pass
    def GetParameterEntryType(self) -> SheetMetalPreferencesBuilder.ParameterEntryTypes:
        """
         Returns parameter entry type 
         Returns parameterEntryType ( SheetMetalPreferencesBuilder.ParameterEntryTypes NXOpen.P): .
        """
        pass
    def GetRemoveSysGenBendReliefs(self) -> bool:
        """
         Returns whether the bend reliefs in the flat pattern are removed or not. 
         Returns areBendReliefsRemoved (bool): .
        """
        pass
    def GetSecondaryToolName(self) -> str:
        """
         Returns secondary tool name 
         Returns secondaryToolName (str): .
        """
        pass
    def GetShowLouverCutoutCurvesAsInteriorCutout(self) -> bool:
        """
         Returns whether louver cutout curves in flat pattern are shown as interior cutout curves or not. 
         Returns isLouverCutoutCurvesShownAsInteriorCutout (bool): .
        """
        pass
    def GetShowSingleBendLineForAlignedBends(self) -> bool:
        """
         Returns whether single continuous bend lines are created in case of aligned cylindrical bends or not. 
         Returns isSingleBendLineShowForAlignedBends (bool): .
        """
        pass
    def GetSimplifyBSplines(self) -> bool:
        """
         Returns whether the bspline curves in the flat pattern are simplified or not. 
         Returns areBSplinesSimplified (bool): .
        """
        pass
    def GetStationaryRadius(self) -> NXOpen.Expression:
        """
         Returns the expression tag of joggle stationary radius value. This API is only to get the expression from the preferences, 
                    to modify any of the values use Preferences.SheetMetalPreferencesBuilder. 
         Returns stationaryRadius ( NXOpen.Expression):  expression object tag for joggle stationary radius value .
        """
        pass
    def GetTabCurveDisplayData(self, curveType: SheetMetalPreferencesBuilder.TabCurveTypes) -> SheetMetalPreferencesBuilder.TabCurvesDisplayData:
        """
         Returns display data for a given tab curve type. 
         Returns displayData ( SheetMetalPreferencesBuilder.TabCurvesDisplayData NXOpen.P):  The display data for the tab curve. .
        """
        pass
    def GetToolName(self) -> str:
        """
         Returns the name of the tool saved with the part 
         Returns toolName (str): .
        """
        pass
    def GetToolNames(self) -> List[str]:
        """
         Returns the tool names defined in the material standards table 
         Returns toolNames (List[str]): .
        """
        pass
    def GetToolProperties(self, toolName: str) -> Tuple[List[str], List[str]]:
        """
         Returns the tool properties saved with the part 
         Returns A tuple consisting of (propertyValues, propertyNames). 
         - propertyValues is: List[str].property Values .
         - propertyNames is: List[str].property Names .

        """
        pass
import NXOpen
class ShipbuildingLinesViewPreferences(NXOpen.Object): 
    """ Represents set of Shipbuilding Lines View Preferences applicable to drafting views. 
        Shipbuilding lines are used for a Profile or a Plate feature in Ship Design """
    class Lines(Enum):
        """
        Members Include: 
         |Hidden|  Hidden 
         |Visible|  Visible 

        """
        Hidden: int
        Visible: int
        @staticmethod
        def ValueOf(value: int) -> ShipbuildingLinesViewPreferences.Lines:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ShipbuildingLines(Enum):
        """
        Members Include: 
         |Profile|  Profile 
         |Plate|  Plate 

        """
        Profile: int
        Plate: int
        @staticmethod
        def ValueOf(value: int) -> ShipbuildingLinesViewPreferences.ShipbuildingLines:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetColor(self, feature_name: str, lines_type: ShipbuildingLinesViewPreferences.Lines) -> int:
        """
         Get line color 
         Returns color (int): .
        """
        pass
    def GetFont(self, feature_name: str, lines_type: ShipbuildingLinesViewPreferences.Lines) -> Font:
        """
         Get line font 
         Returns font ( Font NXOpen.P): .
        """
        pass
    def GetSingleLineRepresentation(self, feature_type: ShipbuildingLinesViewPreferences.ShipbuildingLines, feature_name: str) -> bool:
        """
         Get single line status 
         Returns single_line (bool):  status that determines SLR for the feature .
        """
        pass
    def GetWidth(self, feature_name: str, lines_type: ShipbuildingLinesViewPreferences.Lines) -> Width:
        """
         Get line width 
         Returns width ( Width NXOpen.P): .
        """
        pass
    def SetColor(self, feature_name: str, lines_type: ShipbuildingLinesViewPreferences.Lines, color: int) -> None:
        """
         The color of ship line. The value should be between UF_OBJ_MIN_COLOR and UF_OBJ_MAX_COLOR. 
        """
        pass
    def SetFont(self, feature_name: str, lines_type: ShipbuildingLinesViewPreferences.Lines, font: Font) -> None:
        """
         The font type of ship line.
        """
        pass
    def SetSingleLineRepresentation(self, feature_type: ShipbuildingLinesViewPreferences.ShipbuildingLines, feature_name: str, single_line: bool) -> None:
        """
         Note: The initial values are set based on the customer defaults depending on 
                whether the feature is a Profile or a Plate.
                The status determines the single line representation for the ship feature in a view.
        """
        pass
    def SetWidth(self, feature_name: str, lines_type: ShipbuildingLinesViewPreferences.Lines, width: Width) -> None:
        """
         The width of hidden line or edges. 
        """
        pass
import NXOpen
class ShipDraftingViewLinesViewPreferences(NXOpen.Object): 
    """ Represents set of Ship Drafting View Lines View Preferences applicable to drafting views. 
        Ship drafting view lines are used for the features in Ship Design """
    class Lines(Enum):
        """
        Members Include: 
         |HiddenNonsection|  Hidden, NonSection 
         |VisibleNonsection|  Visible, NonSection
         |HiddenSection|  Hidden, Section 
         |VisibleSection|  Visible, Section
         |SecondaryHiddenNonsection|  Secondary, Hidden, NonSection 
         |SecondaryVisibleNonsection|  Secondary, Visible, NonSection
         |SecondaryHiddenSection|  Secondary, Hidden, Section 
         |SecondaryVisibleSection|  Secondary, Visible, Section

        """
        HiddenNonsection: int
        VisibleNonsection: int
        HiddenSection: int
        VisibleSection: int
        SecondaryHiddenNonsection: int
        SecondaryVisibleNonsection: int
        SecondaryHiddenSection: int
        SecondaryVisibleSection: int
        @staticmethod
        def ValueOf(value: int) -> ShipDraftingViewLinesViewPreferences.Lines:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetColor(self, feature_name: str, lines_type: ShipDraftingViewLinesViewPreferences.Lines) -> int:
        """
         Get line color 
         Returns color (int): .
        """
        pass
    def GetFont(self, feature_name: str, lines_type: ShipDraftingViewLinesViewPreferences.Lines) -> Font:
        """
         Get line font 
         Returns font ( Font NXOpen.P): .
        """
        pass
    def GetShipDrawingObject(self, feature_name: str) -> bool:
        """
         Get single line status 
         Returns single_line (bool):  status that determines SLR for the feature .
        """
        pass
    def GetWidth(self, feature_name: str, lines_type: ShipDraftingViewLinesViewPreferences.Lines) -> Width:
        """
         Get line width 
         Returns width ( Width NXOpen.P): .
        """
        pass
    def SetColor(self, feature_name: str, lines_type: ShipDraftingViewLinesViewPreferences.Lines, color: int) -> None:
        """
         The color of ship line. The value should be between UF_OBJ_MIN_COLOR and UF_OBJ_MAX_COLOR. 
        """
        pass
    def SetFont(self, feature_name: str, lines_type: ShipDraftingViewLinesViewPreferences.Lines, font: Font) -> None:
        """
         The font type of ship line.
        """
        pass
    def SetShipDrawingObject(self, feature_name: str, single_line: bool) -> None:
        """
         Note: The initial values are set based on the file NX_ShipAttribute.xml
                The status determines the line settings for the ship feature in a view.
        """
        pass
    def SetWidth(self, feature_name: str, lines_type: ShipDraftingViewLinesViewPreferences.Lines, width: Width) -> None:
        """
         The width of hidden line or edges. 
        """
        pass
import NXOpen
class ShipGeneralArrangementViewLinesViewPreferences(NXOpen.Object): 
    """ Represents set of Ship GeneralArrangement View Lines View Preferences applicable to drafting views. 
        Ship GeneralArrangement view lines are used for the bodies in Ship General Arrangement application"""
    class Lines(Enum):
        """
        Members Include: 
         |Visible|  visible 
         |Hidden|  hidden

        """
        Visible: int
        Hidden: int
        @staticmethod
        def ValueOf(value: int) -> ShipGeneralArrangementViewLinesViewPreferences.Lines:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetAttributeName(self, viewPlan: str, displayName: str) -> str:
        """
         Get the attribute name of the line type in general arrangement view.
         Returns attributeName (str): .
        """
        pass
    def GetAttributeValue(self, viewPlan: str, displayName: str) -> str:
        """
         Get the attribute value of the line type in general arrangement view.
         Returns attributeValue (str): .
        """
        pass
    def GetColor(self, viewPlan: str, displayName: str, lines_type: ShipGeneralArrangementViewLinesViewPreferences.Lines) -> NXOpen.NXColor:
        """
         Gets line color. 
         Returns color ( NXOpen.NXColor): .
        """
        pass
    def GetFont(self, viewPlan: str, displayName: str, lines_type: ShipGeneralArrangementViewLinesViewPreferences.Lines) -> Font:
        """
         Gets line font. 
         Returns font ( Font NXOpen.P): .
        """
        pass
    def GetWidth(self, viewPlan: str, displayName: str, lines_type: ShipGeneralArrangementViewLinesViewPreferences.Lines) -> Width:
        """
         Gets line width 
         Returns width ( Width NXOpen.P): .
        """
        pass
    def SetAttributeName(self, viewPlan: str, displayName: str, attributeName: str) -> None:
        """
         Set the attribute name of the line type in general arrangement view.
        """
        pass
    def SetAttributeValue(self, viewPlan: str, displayName: str, attributeValue: str) -> None:
        """
         Set the attribute value of the line type in general arrangement view.
        """
        pass
    def SetColor(self, viewPlan: str, displayName: str, lines_type: ShipGeneralArrangementViewLinesViewPreferences.Lines, color: NXOpen.NXColor) -> None:
        """
         The color of ship general arrangement line. The value should be between UF_OBJ_MIN_COLOR and UF_OBJ_MAX_COLOR. 
        """
        pass
    def SetFont(self, viewPlan: str, displayName: str, lines_type: ShipGeneralArrangementViewLinesViewPreferences.Lines, font: Font) -> None:
        """
         The font type of ship line.
        """
        pass
    def SetWidth(self, viewPlan: str, displayName: str, lines_type: ShipGeneralArrangementViewLinesViewPreferences.Lines, width: Width) -> None:
        """
         The width of ship line. 
        """
        pass
import NXOpen
class SketchPreferences(NXOpen.Object): 
    """ Represents the set of sketch preferences applicable on NXOpen.Sketch object"""
    class DimensionLabelType(Enum):
        """
        Members Include: 
         |Expression|  Displays the entire expression such as P2=P34 
         |Name|  Displays only the name of the expression, such as P2 
         |Value|  Displays the numerical value of the expression 

        """
        Expression: int
        Name: int
        Value: int
        @staticmethod
        def ValueOf(value: int) -> SketchPreferences.DimensionLabelType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DimensionTextSizeMode(Enum):
        """
        Members Include: 
         |DraftingStandard|  The size is determined by the current Drafting Standard 
         |FixedOnScreen|  The size is adjusted opposite of zoom scale so that the size on screen remains fixed 
         |Variable|  The size is computed for the current zoom scale when first dimension is created in given sketch 

        """
        DraftingStandard: int
        FixedOnScreen: int
        Variable: int
        @staticmethod
        def ValueOf(value: int) -> SketchPreferences.DimensionTextSizeMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ConstraintSymbolSize(self) -> float:
        """
        Getter for property: (float) ConstraintSymbolSize
         Returns the constraint symbol size    
            
         
        """
        pass
    @ConstraintSymbolSize.setter
    def ConstraintSymbolSize(self, constraint_size: float):
        """
        Setter for property: (float) ConstraintSymbolSize
         Returns the constraint symbol size    
            
         
        """
        pass
    @property
    def ContinuousAutoDimensioningSetting(self) -> bool:
        """
        Getter for property: (bool) ContinuousAutoDimensioningSetting
         Returns the setting that controls whether or not to continuously create auto dimensions in a sketch.  
           If the option is true (On) then the auto dimensioner will be 
            automatically executed after an individual curve is created in a sketch.   
         
        """
        pass
    @ContinuousAutoDimensioningSetting.setter
    def ContinuousAutoDimensioningSetting(self, auto_dim: bool):
        """
        Setter for property: (bool) ContinuousAutoDimensioningSetting
         Returns the setting that controls whether or not to continuously create auto dimensions in a sketch.  
           If the option is true (On) then the auto dimensioner will be 
            automatically executed after an individual curve is created in a sketch.   
         
        """
        pass
    @property
    def CreateInferredConstraints(self) -> bool:
        """
        Getter for property: (bool) CreateInferredConstraints
         Returns the setting that controls whether or not inferred constraints are automatically created when curves and points are created in the sketch.  
             
         
        """
        pass
    @CreateInferredConstraints.setter
    def CreateInferredConstraints(self, create_inferred_constraints: bool):
        """
        Setter for property: (bool) CreateInferredConstraints
         Returns the setting that controls whether or not inferred constraints are automatically created when curves and points are created in the sketch.  
             
         
        """
        pass
    @property
    def DimensionLabel(self) -> SketchPreferences.DimensionLabelType:
        """
        Getter for property: ( SketchPreferences.DimensionLabelType NXOpen.P) DimensionLabel
         Returns the dimension label.  
           Controls how expressions in sketch dimensions are displayed   
         
        """
        pass
    @DimensionLabel.setter
    def DimensionLabel(self, dimension_label: SketchPreferences.DimensionLabelType):
        """
        Setter for property: ( SketchPreferences.DimensionLabelType NXOpen.P) DimensionLabel
         Returns the dimension label.  
           Controls how expressions in sketch dimensions are displayed   
         
        """
        pass
    @property
    def DimensionTextScale(self) -> float:
        """
        Getter for property: (float) DimensionTextScale
         Returns the scale of the dimension text.  
             
         
        """
        pass
    @DimensionTextScale.setter
    def DimensionTextScale(self, dimensionTextScale: float):
        """
        Setter for property: (float) DimensionTextScale
         Returns the scale of the dimension text.  
             
         
        """
        pass
    @property
    def DisplayObjectColor(self) -> bool:
        """
        Getter for property: (bool) DisplayObjectColor
         Returns the setting that controls whether or not objects are displayed in their actual color in sketch   
            
         
        """
        pass
    @DisplayObjectColor.setter
    def DisplayObjectColor(self, display_object_color: bool):
        """
        Setter for property: (bool) DisplayObjectColor
         Returns the setting that controls whether or not objects are displayed in their actual color in sketch   
            
         
        """
        pass
    @property
    def DisplayObjectName(self) -> bool:
        """
        Getter for property: (bool) DisplayObjectName
         Returns the setting that controls whether or not objects are displayed with their names in sketch.  
             
         
        """
        pass
    @DisplayObjectName.setter
    def DisplayObjectName(self, displayObjectName: bool):
        """
        Setter for property: (bool) DisplayObjectName
         Returns the setting that controls whether or not objects are displayed with their names in sketch.  
             
         
        """
        pass
    @property
    def DisplayParenthesesOnReferenceDimensions(self) -> bool:
        """
        Getter for property: (bool) DisplayParenthesesOnReferenceDimensions
         Returns the setting that controls whether or not parentheses are displayed on reference dimensions.  
             
         
        """
        pass
    @DisplayParenthesesOnReferenceDimensions.setter
    def DisplayParenthesesOnReferenceDimensions(self, displayParentheses: bool):
        """
        Setter for property: (bool) DisplayParenthesesOnReferenceDimensions
         Returns the setting that controls whether or not parentheses are displayed on reference dimensions.  
             
         
        """
        pass
    @property
    def DisplayReferenceGeometry(self) -> bool:
        """
        Getter for property: (bool) DisplayReferenceGeometry
         Returns the setting that controls whether or not the reference geometry are displayed on inactive sketches   
            
         
        """
        pass
    @DisplayReferenceGeometry.setter
    def DisplayReferenceGeometry(self, displayReferenceGeometry: bool):
        """
        Setter for property: (bool) DisplayReferenceGeometry
         Returns the setting that controls whether or not the reference geometry are displayed on inactive sketches   
            
         
        """
        pass
    @property
    def DisplayShadedRegions(self) -> bool:
        """
        Getter for property: (bool) DisplayShadedRegions
         Returns the setting that specifies whether or not closed curve regions are displayed as shaded regions in an active sketch.  
             
         
        """
        pass
    @DisplayShadedRegions.setter
    def DisplayShadedRegions(self, displayShadedRegions: bool):
        """
        Setter for property: (bool) DisplayShadedRegions
         Returns the setting that specifies whether or not closed curve regions are displayed as shaded regions in an active sketch.  
             
         
        """
        pass
    @property
    def DisplayVertices(self) -> bool:
        """
        Getter for property: (bool) DisplayVertices
         Returns the setting that controls whether or not vertices are displayed in an active sketch.  
             
         
        """
        pass
    @DisplayVertices.setter
    def DisplayVertices(self, displayVertices: bool):
        """
        Setter for property: (bool) DisplayVertices
         Returns the setting that controls whether or not vertices are displayed in an active sketch.  
             
         
        """
        pass
    @property
    def FixedTextSize(self) -> float:
        """
        Getter for property: (float) FixedTextSize
         Returns the fixed text size.  
            It is the visible dimension size when text size fixed is enabled.   
         
        """
        pass
    @FixedTextSize.setter
    def FixedTextSize(self, fixed_text_size: float):
        """
        Setter for property: (float) FixedTextSize
         Returns the fixed text size.  
            It is the visible dimension size when text size fixed is enabled.   
         
        """
        pass
    @property
    def SolvingTolerance(self) -> float:
        """
        Getter for property: (float) SolvingTolerance
         Returns the sketch solving tolerance.  
           This specifies the maximum allowable distance between two objects 
                when solving the sketch constraints for the given sketch. The tolerance value must be greater than 1e-08.   
         
        """
        pass
    @SolvingTolerance.setter
    def SolvingTolerance(self, tolerance: float):
        """
        Setter for property: (float) SolvingTolerance
         Returns the sketch solving tolerance.  
           This specifies the maximum allowable distance between two objects 
                when solving the sketch constraints for the given sketch. The tolerance value must be greater than 1e-08.   
         
        """
        pass
    @property
    def TextSizeFixed(self) -> bool:
        """
        Getter for property: (bool) TextSizeFixed
         Returns the setting that controls whether or not the dimension text size should be fixed.  
             
         
        """
        pass
    @TextSizeFixed.setter
    def TextSizeFixed(self, text_size_fixed: bool):
        """
        Setter for property: (bool) TextSizeFixed
         Returns the setting that controls whether or not the dimension text size should be fixed.  
             
         
        """
        pass
    @property
    def TextSizeMode(self) -> SketchPreferences.DimensionTextSizeMode:
        """
        Getter for property: ( SketchPreferences.DimensionTextSizeMode NXOpen.P) TextSizeMode
         Returns the setting that controls dimension text size mode.  
             
         
        """
        pass
    @TextSizeMode.setter
    def TextSizeMode(self, mode: SketchPreferences.DimensionTextSizeMode):
        """
        Setter for property: ( SketchPreferences.DimensionTextSizeMode NXOpen.P) TextSizeMode
         Returns the setting that controls dimension text size mode.  
             
         
        """
        pass
    @property
    def UseSolvingTolerance(self) -> bool:
        """
        Getter for property: (bool) UseSolvingTolerance
         Returns the setting that controls whether or not to use user input for sketch solving tolerance.  
             
         
        """
        pass
    @UseSolvingTolerance.setter
    def UseSolvingTolerance(self, useTolerance: bool):
        """
        Setter for property: (bool) UseSolvingTolerance
         Returns the setting that controls whether or not to use user input for sketch solving tolerance.  
             
         
        """
        pass
    def ApplySketchPreferences(self, dim_display_flag: int) -> None:
        """
         Applies sketch preferences set by user. The dimDisplayFlag is the API version of the UI setting of 
                Retain Dimensions which was last available for use in NX 6. The setting still exists in the UI for 
                legacy parts that have a sketch with Retain Dimensions enabled.  However, once the setting is turned off,
                it cannot be turned on again. This functionality is replaced by NXOpen.Annotations.AnnotationManager.MakePmi
                in an active sketch or NXOpen.Features.EditDimensionBuilder.DisplayAsPmi when not in an active sketch.
        """
        pass
import NXOpen
class SmoothEdgesViewPreferences(NXOpen.Object): 
    """ Represents set of Smooth Edges View Preferences applicable to drafting views.
        Allows to control the display of smooth edges. Smooth edges are those whose adjacent 
        faces have the same surface tangent at the edge where they meet.
     """
    @property
    def SmoothEdge(self) -> bool:
        """
        Getter for property: (bool) SmoothEdge
         Returns the status of smooth edge.  
           If True then it enables the smooth edge options.   
         
        """
        pass
    @SmoothEdge.setter
    def SmoothEdge(self, smooth_edge: bool):
        """
        Setter for property: (bool) SmoothEdge
         Returns the status of smooth edge.  
           If True then it enables the smooth edge options.   
         
        """
        pass
    @property
    def SmoothEdgeColor(self) -> int:
        """
        Getter for property: (int) SmoothEdgeColor
         Returns the color of smooth edge.  
           The value should be between 1 and 216.  
         
        """
        pass
    @SmoothEdgeColor.setter
    def SmoothEdgeColor(self, smooth_edge_color: int):
        """
        Setter for property: (int) SmoothEdgeColor
         Returns the color of smooth edge.  
           The value should be between 1 and 216.  
         
        """
        pass
    @property
    def SmoothEdgeEndGaps(self) -> bool:
        """
        Getter for property: (bool) SmoothEdgeEndGaps
         Returns the status of smooth edge end gaps.  
           If True, the visible ends are suppressed from the display.
                    The length of the suppressed end is in drawing units and is controlled by the value set in 
                    the End Gap field. If False, the visible ends are not suppressed from the display.
                   
         
        """
        pass
    @SmoothEdgeEndGaps.setter
    def SmoothEdgeEndGaps(self, smooth_edge_end_gaps: bool):
        """
        Setter for property: (bool) SmoothEdgeEndGaps
         Returns the status of smooth edge end gaps.  
           If True, the visible ends are suppressed from the display.
                    The length of the suppressed end is in drawing units and is controlled by the value set in 
                    the End Gap field. If False, the visible ends are not suppressed from the display.
                   
         
        """
        pass
    @property
    def SmoothEdgeEndGapsData(self) -> float:
        """
        Getter for property: (float) SmoothEdgeEndGapsData
         Returns the value of smooth edge end gaps.  
            
         
        """
        pass
    @SmoothEdgeEndGapsData.setter
    def SmoothEdgeEndGapsData(self, smooth_edge_end_gaps_data: float):
        """
        Setter for property: (float) SmoothEdgeEndGapsData
         Returns the value of smooth edge end gaps.  
            
         
        """
        pass
    @property
    def SmoothEdgeFont(self) -> Font:
        """
        Getter for property: ( Font NXOpen.P) SmoothEdgeFont
         Returns the font of smooth edge.  
            
         
        """
        pass
    @SmoothEdgeFont.setter
    def SmoothEdgeFont(self, smooth_edge_font: Font):
        """
        Setter for property: ( Font NXOpen.P) SmoothEdgeFont
         Returns the font of smooth edge.  
            
         
        """
        pass
    @property
    def SmoothEdgeTolerance(self) -> bool:
        """
        Getter for property: (bool) SmoothEdgeTolerance
         Returns the status of smooth edge angle tolerance.  
           If True,  the value set in 
                    the Tolerance Data field is used. If False, the system default angle tolerance is used.
                   
         
        """
        pass
    @SmoothEdgeTolerance.setter
    def SmoothEdgeTolerance(self, smooth_edge_tolerance: bool):
        """
        Setter for property: (bool) SmoothEdgeTolerance
         Returns the status of smooth edge angle tolerance.  
           If True,  the value set in 
                    the Tolerance Data field is used. If False, the system default angle tolerance is used.
                   
         
        """
        pass
    @property
    def SmoothEdgeToleranceData(self) -> float:
        """
        Getter for property: (float) SmoothEdgeToleranceData
         Returns the value of smooth edge angle tolerance in degrees.  
            
         
        """
        pass
    @SmoothEdgeToleranceData.setter
    def SmoothEdgeToleranceData(self, smooth_edge_tolerance_data: float):
        """
        Setter for property: (float) SmoothEdgeToleranceData
         Returns the value of smooth edge angle tolerance in degrees.  
            
         
        """
        pass
    @property
    def SmoothEdgeWidth(self) -> Width:
        """
        Getter for property: ( Width NXOpen.P) SmoothEdgeWidth
         Returns the width of smooth edge.  
            
         
        """
        pass
    @SmoothEdgeWidth.setter
    def SmoothEdgeWidth(self, smooth_edge_width: Width):
        """
        Setter for property: ( Width NXOpen.P) SmoothEdgeWidth
         Returns the width of smooth edge.  
            
         
        """
        pass
import NXOpen
class SubdivisionModelingPreferences(NXOpen.Object): 
    """ Represents the set of Modeling preferences applicable to entire session"""
    class CagePolylineVertexSizes(Enum):
        """
        Members Include: 
         |Small| 
         |Medium| 
         |Large| 

        """
        Small: int
        Medium: int
        Large: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionModelingPreferences.CagePolylineVertexSizes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CagePolylineVertexStyles(Enum):
        """
        Members Include: 
         |NotSet| 
         |Square| 
         |Triangle| 
         |Circle| 
         |Plus| 
         |Cross| 

        """
        NotSet: int
        Square: int
        Triangle: int
        Circle: int
        Plus: int
        Cross: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionModelingPreferences.CagePolylineVertexStyles:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DisplayModes(Enum):
        """
        Members Include: 
         |CageAndBody|  Display both cage and body 
         |CageOnly|  Display cage only 
         |BodyOnly|  Display body only 

        """
        CageAndBody: int
        CageOnly: int
        BodyOnly: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionModelingPreferences.DisplayModes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class VertexSizeTypes(Enum):
        """
        Members Include: 
         |Small| 
         |Medium| 
         |Large| 

        """
        Small: int
        Medium: int
        Large: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionModelingPreferences.VertexSizeTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class VertexStyleTypes(Enum):
        """
        Members Include: 
         |Square| 
         |Triangle| 
         |Circle| 
         |Plus| 
         |Cross| 

        """
        Square: int
        Triangle: int
        Circle: int
        Plus: int
        Cross: int
        @staticmethod
        def ValueOf(value: int) -> SubdivisionModelingPreferences.VertexStyleTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CagePolylineColor(self) -> int:
        """
        Getter for property: (int) CagePolylineColor
         Returns the cage polyline color.  
             
         
        """
        pass
    @CagePolylineColor.setter
    def CagePolylineColor(self, lineColor: int):
        """
        Setter for property: (int) CagePolylineColor
         Returns the cage polyline color.  
             
         
        """
        pass
    @property
    def CagePolylineFont(self) -> int:
        """
        Getter for property: (int) CagePolylineFont
         Returns the cage polyline font.  
             
         
        """
        pass
    @CagePolylineFont.setter
    def CagePolylineFont(self, lineFont: int):
        """
        Setter for property: (int) CagePolylineFont
         Returns the cage polyline font.  
             
         
        """
        pass
    @property
    def CagePolylineVertexColor(self) -> int:
        """
        Getter for property: (int) CagePolylineVertexColor
         Returns the cage polyline vertex color.  
             
         
        """
        pass
    @CagePolylineVertexColor.setter
    def CagePolylineVertexColor(self, vertexColor: int):
        """
        Setter for property: (int) CagePolylineVertexColor
         Returns the cage polyline vertex color.  
             
         
        """
        pass
    @property
    def CagePolylineVertexSize(self) -> SubdivisionModelingPreferences.CagePolylineVertexSizes:
        """
        Getter for property: ( SubdivisionModelingPreferences.CagePolylineVertexSizes NXOpen.P) CagePolylineVertexSize
         Returns the cage polyline vertex size.  
             
         
        """
        pass
    @CagePolylineVertexSize.setter
    def CagePolylineVertexSize(self, vertexSize: SubdivisionModelingPreferences.CagePolylineVertexSizes):
        """
        Setter for property: ( SubdivisionModelingPreferences.CagePolylineVertexSizes NXOpen.P) CagePolylineVertexSize
         Returns the cage polyline vertex size.  
             
         
        """
        pass
    @property
    def CagePolylineVertexStyle(self) -> SubdivisionModelingPreferences.CagePolylineVertexStyles:
        """
        Getter for property: ( SubdivisionModelingPreferences.CagePolylineVertexStyles NXOpen.P) CagePolylineVertexStyle
         Returns the cage polyline vertex style.  
             
         
        """
        pass
    @CagePolylineVertexStyle.setter
    def CagePolylineVertexStyle(self, vertexStyle: SubdivisionModelingPreferences.CagePolylineVertexStyles):
        """
        Setter for property: ( SubdivisionModelingPreferences.CagePolylineVertexStyles NXOpen.P) CagePolylineVertexStyle
         Returns the cage polyline vertex style.  
             
         
        """
        pass
    @property
    def CagePolylineWidth(self) -> int:
        """
        Getter for property: (int) CagePolylineWidth
         Returns the cage polyline width.  
             
         
        """
        pass
    @CagePolylineWidth.setter
    def CagePolylineWidth(self, lineWidth: int):
        """
        Setter for property: (int) CagePolylineWidth
         Returns the cage polyline width.  
             
         
        """
        pass
    @property
    def CanAllowBackSideSelection(self) -> bool:
        """
        Getter for property: (bool) CanAllowBackSideSelection
         Returns the flag indicating if the hidden topology selection is allowed or not.  
             
         
        """
        pass
    @CanAllowBackSideSelection.setter
    def CanAllowBackSideSelection(self, allow: bool):
        """
        Setter for property: (bool) CanAllowBackSideSelection
         Returns the flag indicating if the hidden topology selection is allowed or not.  
             
         
        """
        pass
    @property
    def CanShowWeight(self) -> bool:
        """
        Getter for property: (bool) CanShowWeight
         Returns the flag indicating if the edge weights are displayed or not.  
             
         
        """
        pass
    @CanShowWeight.setter
    def CanShowWeight(self, showWeight: bool):
        """
        Setter for property: (bool) CanShowWeight
         Returns the flag indicating if the edge weights are displayed or not.  
             
         
        """
        pass
    @property
    def ConstraintColor(self) -> int:
        """
        Getter for property: (int) ConstraintColor
         Returns the constrained entity color.  
             
         
        """
        pass
    @ConstraintColor.setter
    def ConstraintColor(self, color: int):
        """
        Setter for property: (int) ConstraintColor
         Returns the constrained entity color.  
             
         
        """
        pass
    @property
    def DisplayMode(self) -> SubdivisionModelingPreferences.DisplayModes:
        """
        Getter for property: ( SubdivisionModelingPreferences.DisplayModes NXOpen.P) DisplayMode
         Returns the mesh and solid body display option   
            
         
        """
        pass
    @DisplayMode.setter
    def DisplayMode(self, displayOption: SubdivisionModelingPreferences.DisplayModes):
        """
        Setter for property: ( SubdivisionModelingPreferences.DisplayModes NXOpen.P) DisplayMode
         Returns the mesh and solid body display option   
            
         
        """
        pass
    @property
    def HighlightFaceTranslucency(self) -> int:
        """
        Getter for property: (int) HighlightFaceTranslucency
         Returns the percentage translucency of the highlighted face.  
             
         
        """
        pass
    @HighlightFaceTranslucency.setter
    def HighlightFaceTranslucency(self, highlightLineTranslucency: int):
        """
        Setter for property: (int) HighlightFaceTranslucency
         Returns the percentage translucency of the highlighted face.  
             
         
        """
        pass
    @property
    def IsXRayCage(self) -> bool:
        """
        Getter for property: (bool) IsXRayCage
         Returns the flag indicating if the hidden edge of the cage are visible or not.  
             
         
        """
        pass
    @IsXRayCage.setter
    def IsXRayCage(self, isXRayCage: bool):
        """
        Setter for property: (bool) IsXRayCage
         Returns the flag indicating if the hidden edge of the cage are visible or not.  
             
         
        """
        pass
    @property
    def LineColor(self) -> int:
        """
        Getter for property: (int) LineColor
         Returns the line color.  
             
         
        """
        pass
    @LineColor.setter
    def LineColor(self, lineColor: int):
        """
        Setter for property: (int) LineColor
         Returns the line color.  
             
         
        """
        pass
    @property
    def LineFont(self) -> int:
        """
        Getter for property: (int) LineFont
         Returns the smooth edge line font.  
             
         
        """
        pass
    @LineFont.setter
    def LineFont(self, lineFont: int):
        """
        Setter for property: (int) LineFont
         Returns the smooth edge line font.  
             
         
        """
        pass
    @property
    def LineWidth(self) -> int:
        """
        Getter for property: (int) LineWidth
         Returns the line width.  
             
         
        """
        pass
    @LineWidth.setter
    def LineWidth(self, lineWidth: int):
        """
        Setter for property: (int) LineWidth
         Returns the line width.  
             
         
        """
        pass
    @property
    def MakeExternalFaceTranslucent(self) -> bool:
        """
        Getter for property: (bool) MakeExternalFaceTranslucent
         Returns the flag indicating if external faces will be made translucent in preview of some commands if vertices have been selected on these faces.  
            
         
        """
        pass
    @MakeExternalFaceTranslucent.setter
    def MakeExternalFaceTranslucent(self, makeTranslucent: bool):
        """
        Setter for property: (bool) MakeExternalFaceTranslucent
         Returns the flag indicating if external faces will be made translucent in preview of some commands if vertices have been selected on these faces.  
            
         
        """
        pass
    @property
    def MergeSubdivisionBodyFacesIfPossible(self) -> bool:
        """
        Getter for property: (bool) MergeSubdivisionBodyFacesIfPossible
         Returns the flag indicating if Subdivision Body faces should be merged.  
           When turned on, smoothly
                    connected face regions of Subdivision Body may be merged while maintaining an accurate representation
                    of the initial body.
                  
         
        """
        pass
    @MergeSubdivisionBodyFacesIfPossible.setter
    def MergeSubdivisionBodyFacesIfPossible(self, merge: bool):
        """
        Setter for property: (bool) MergeSubdivisionBodyFacesIfPossible
         Returns the flag indicating if Subdivision Body faces should be merged.  
           When turned on, smoothly
                    connected face regions of Subdivision Body may be merged while maintaining an accurate representation
                    of the initial body.
                  
         
        """
        pass
    @property
    def SharpEdgeLineColor(self) -> int:
        """
        Getter for property: (int) SharpEdgeLineColor
         Returns the sharp edge line color.  
             
         
        """
        pass
    @SharpEdgeLineColor.setter
    def SharpEdgeLineColor(self, lineColor: int):
        """
        Setter for property: (int) SharpEdgeLineColor
         Returns the sharp edge line color.  
             
         
        """
        pass
    @property
    def SharpEdgeLineFont(self) -> int:
        """
        Getter for property: (int) SharpEdgeLineFont
         Returns the sharp edge line font.  
             
         
        """
        pass
    @SharpEdgeLineFont.setter
    def SharpEdgeLineFont(self, lineFont: int):
        """
        Setter for property: (int) SharpEdgeLineFont
         Returns the sharp edge line font.  
             
         
        """
        pass
    @property
    def VertexColor(self) -> int:
        """
        Getter for property: (int) VertexColor
         Returns the vertex color.  
             
         
        """
        pass
    @VertexColor.setter
    def VertexColor(self, vertexColor: int):
        """
        Setter for property: (int) VertexColor
         Returns the vertex color.  
             
         
        """
        pass
    @property
    def VertexSize(self) -> SubdivisionModelingPreferences.VertexSizeTypes:
        """
        Getter for property: ( SubdivisionModelingPreferences.VertexSizeTypes NXOpen.P) VertexSize
         Returns the vertex size.  
             
         
        """
        pass
    @VertexSize.setter
    def VertexSize(self, vertexSize: SubdivisionModelingPreferences.VertexSizeTypes):
        """
        Setter for property: ( SubdivisionModelingPreferences.VertexSizeTypes NXOpen.P) VertexSize
         Returns the vertex size.  
             
         
        """
        pass
    @property
    def VertexStyle(self) -> SubdivisionModelingPreferences.VertexStyleTypes:
        """
        Getter for property: ( SubdivisionModelingPreferences.VertexStyleTypes NXOpen.P) VertexStyle
         Returns the vertex style.  
             
         
        """
        pass
    @VertexStyle.setter
    def VertexStyle(self, vertexStyle: SubdivisionModelingPreferences.VertexStyleTypes):
        """
        Setter for property: ( SubdivisionModelingPreferences.VertexStyleTypes NXOpen.P) VertexStyle
         Returns the vertex style.  
             
         
        """
        pass
import NXOpen
class TextureModelingPreferences(NXOpen.Object): 
    """ Represents the set of Texture Modeling preferences applicable to entire session"""
    @property
    def ReversedUVPatchColor(self) -> int:
        """
        Getter for property: (int) ReversedUVPatchColor
         Returns the reversed UV patch color.  
             
         
        """
        pass
    @ReversedUVPatchColor.setter
    def ReversedUVPatchColor(self, color: int):
        """
        Setter for property: (int) ReversedUVPatchColor
         Returns the reversed UV patch color.  
             
         
        """
        pass
    @property
    def RipEdgesColor(self) -> int:
        """
        Getter for property: (int) RipEdgesColor
         Returns the Rip Edges color.  
             
         
        """
        pass
    @RipEdgesColor.setter
    def RipEdgesColor(self, color: int):
        """
        Setter for property: (int) RipEdgesColor
         Returns the Rip Edges color.  
             
         
        """
        pass
    @property
    def RipEdgesFont(self) -> NXOpen.DisplayableObject.ObjectFont:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectFont) RipEdgesFont
         Returns the Rip Edges font.  
             
         
        """
        pass
    @RipEdgesFont.setter
    def RipEdgesFont(self, font: NXOpen.DisplayableObject.ObjectFont):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectFont) RipEdgesFont
         Returns the Rip Edges font.  
             
         
        """
        pass
    @property
    def RipEdgesWidth(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectWidth) RipEdgesWidth
         Returns the Rip Edges width.  
             
         
        """
        pass
    @RipEdgesWidth.setter
    def RipEdgesWidth(self, width: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectWidth) RipEdgesWidth
         Returns the Rip Edges width.  
             
         
        """
        pass
    @property
    def Show2DGrid(self) -> bool:
        """
        Getter for property: (bool) Show2DGrid
         Returns the Show 2D Grid.  
             
         
        """
        pass
    @Show2DGrid.setter
    def Show2DGrid(self, show: bool):
        """
        Setter for property: (bool) Show2DGrid
         Returns the Show 2D Grid.  
             
         
        """
        pass
    @property
    def Show3DGrid(self) -> bool:
        """
        Getter for property: (bool) Show3DGrid
         Returns the Show 3D Grid.  
             
         
        """
        pass
    @Show3DGrid.setter
    def Show3DGrid(self, show: bool):
        """
        Setter for property: (bool) Show3DGrid
         Returns the Show 3D Grid.  
             
         
        """
        pass
    @property
    def ULineColor(self) -> int:
        """
        Getter for property: (int) ULineColor
         Returns the U line color.  
             
         
        """
        pass
    @ULineColor.setter
    def ULineColor(self, color: int):
        """
        Setter for property: (int) ULineColor
         Returns the U line color.  
             
         
        """
        pass
    @property
    def ULineFont(self) -> NXOpen.DisplayableObject.ObjectFont:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectFont) ULineFont
         Returns the U line font.  
             
         
        """
        pass
    @ULineFont.setter
    def ULineFont(self, font: NXOpen.DisplayableObject.ObjectFont):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectFont) ULineFont
         Returns the U line font.  
             
         
        """
        pass
    @property
    def ULineWidth(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectWidth) ULineWidth
         Returns the U line width.  
             
         
        """
        pass
    @ULineWidth.setter
    def ULineWidth(self, width: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectWidth) ULineWidth
         Returns the U line width.  
             
         
        """
        pass
    @property
    def UVPatchColor(self) -> int:
        """
        Getter for property: (int) UVPatchColor
         Returns the UV patch color.  
             
         
        """
        pass
    @UVPatchColor.setter
    def UVPatchColor(self, color: int):
        """
        Setter for property: (int) UVPatchColor
         Returns the UV patch color.  
             
         
        """
        pass
    @property
    def VLineColor(self) -> int:
        """
        Getter for property: (int) VLineColor
         Returns the V line color.  
             
         
        """
        pass
    @VLineColor.setter
    def VLineColor(self, color: int):
        """
        Setter for property: (int) VLineColor
         Returns the V line color.  
             
         
        """
        pass
    @property
    def VLineFont(self) -> NXOpen.DisplayableObject.ObjectFont:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectFont) VLineFont
         Returns the V line font.  
             
         
        """
        pass
    @VLineFont.setter
    def VLineFont(self, font: NXOpen.DisplayableObject.ObjectFont):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectFont) VLineFont
         Returns the V line font.  
             
         
        """
        pass
    @property
    def VLineWidth(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectWidth) VLineWidth
         Returns the V line width.  
             
         
        """
        pass
    @VLineWidth.setter
    def VLineWidth(self, width: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectWidth) VLineWidth
         Returns the V line width.  
             
         
        """
        pass
    def DisplayDistortion(display: bool) -> None:
        """
         Displays distortion map. 
        """
        pass
import NXOpen
class ThreadsViewPreferences(NXOpen.Object): 
    """ Represents set of Threads View Preferences applicable to drafting views.
        Allows to create ANSI and ISO thread representations for both internal 
        and external threads in drawing member views.  """
    @property
    def MinimumPitchField(self) -> float:
        """
        Getter for property: (float) MinimumPitchField
         Returns the minimum pitch field.  
           Allows to control the minimum distance (in drawing coordinates) 
                    to which two points which represent crests of a thread are drawn. It is also used to control 
                    the minimum distance between a thread and it's defining geometry such as edges, silhouettes or 
                    section edges of the cylindrical face or chamfered face. This can be used to help prevent lines 
                    from running together, when threads with a small pitch are plotted at a small scale.
                   
         
        """
        pass
    @MinimumPitchField.setter
    def MinimumPitchField(self, minimum_pitch_field: float):
        """
        Setter for property: (float) MinimumPitchField
         Returns the minimum pitch field.  
           Allows to control the minimum distance (in drawing coordinates) 
                    to which two points which represent crests of a thread are drawn. It is also used to control 
                    the minimum distance between a thread and it's defining geometry such as edges, silhouettes or 
                    section edges of the cylindrical face or chamfered face. This can be used to help prevent lines 
                    from running together, when threads with a small pitch are plotted at a small scale.
                   
         
        """
        pass
    @property
    def OverrideVisibleThreadColor(self) -> int:
        """
        Getter for property: (int) OverrideVisibleThreadColor
         Returns the visible thread override color.  
           The value should be between 1 and 216.  
         
        """
        pass
    @OverrideVisibleThreadColor.setter
    def OverrideVisibleThreadColor(self, overrideVisibleThreadColor: int):
        """
        Setter for property: (int) OverrideVisibleThreadColor
         Returns the visible thread override color.  
           The value should be between 1 and 216.  
         
        """
        pass
    @property
    def RenderTrueHiddenLine(self) -> bool:
        """
        Getter for property: (bool) RenderTrueHiddenLine
         Returns the status of render true hidden line   
            
         
        """
        pass
    @RenderTrueHiddenLine.setter
    def RenderTrueHiddenLine(self, render_true_hidden_line: bool):
        """
        Setter for property: (bool) RenderTrueHiddenLine
         Returns the status of render true hidden line   
            
         
        """
        pass
    @property
    def ThreadsStandardOptionData(self) -> int:
        """
        Getter for property: (int) ThreadsStandardOptionData
         Returns the threads standard option.  
            
         
        """
        pass
    @ThreadsStandardOptionData.setter
    def ThreadsStandardOptionData(self, threads_standard_option_data: int):
        """
        Setter for property: (int) ThreadsStandardOptionData
         Returns the threads standard option.  
            
         
        """
        pass
import NXOpen
class TraceLinesViewPreferences(NXOpen.Object): 
    """ Represents set of Trace Lines View Preferences applicable to drafting views. """
    @property
    def CreateGapsStatus(self) -> bool:
        """
        Getter for property: (bool) CreateGapsStatus
         Returns the status of create gaps   
            
         
        """
        pass
    @CreateGapsStatus.setter
    def CreateGapsStatus(self, create_gaps: bool):
        """
        Setter for property: (bool) CreateGapsStatus
         Returns the status of create gaps   
            
         
        """
        pass
    @property
    def GapSize(self) -> float:
        """
        Getter for property: (float) GapSize
         Returns the gap size.  
             
         
        """
        pass
    @GapSize.setter
    def GapSize(self, gap_size: float):
        """
        Setter for property: (float) GapSize
         Returns the gap size.  
             
         
        """
        pass
    @property
    def HiddenColor(self) -> int:
        """
        Getter for property: (int) HiddenColor
         Returns the hidden color.  
           The value should be between 1 and 216.  
         
        """
        pass
    @HiddenColor.setter
    def HiddenColor(self, hidden_color: int):
        """
        Setter for property: (int) HiddenColor
         Returns the hidden color.  
           The value should be between 1 and 216.  
         
        """
        pass
    @property
    def HiddenFont(self) -> Font:
        """
        Getter for property: ( Font NXOpen.P) HiddenFont
         Returns the hidden font   
            
         
        """
        pass
    @HiddenFont.setter
    def HiddenFont(self, hidden_font: Font):
        """
        Setter for property: ( Font NXOpen.P) HiddenFont
         Returns the hidden font   
            
         
        """
        pass
    @property
    def HiddenWidth(self) -> Width:
        """
        Getter for property: ( Width NXOpen.P) HiddenWidth
         Returns the hidden width   
            
         
        """
        pass
    @HiddenWidth.setter
    def HiddenWidth(self, hidden_width: Width):
        """
        Setter for property: ( Width NXOpen.P) HiddenWidth
         Returns the hidden width   
            
         
        """
        pass
    @property
    def VisibleColor(self) -> int:
        """
        Getter for property: (int) VisibleColor
         Returns the visible color.  
           The value should be between 1 and 216.   
         
        """
        pass
    @VisibleColor.setter
    def VisibleColor(self, visible_color: int):
        """
        Setter for property: (int) VisibleColor
         Returns the visible color.  
           The value should be between 1 and 216.   
         
        """
        pass
    @property
    def VisibleFont(self) -> Font:
        """
        Getter for property: ( Font NXOpen.P) VisibleFont
         Returns the visible font   
            
         
        """
        pass
    @VisibleFont.setter
    def VisibleFont(self, visible_font: Font):
        """
        Setter for property: ( Font NXOpen.P) VisibleFont
         Returns the visible font   
            
         
        """
        pass
    @property
    def VisibleWidth(self) -> Width:
        """
        Getter for property: ( Width NXOpen.P) VisibleWidth
         Returns the visible width   
            
         
        """
        pass
    @VisibleWidth.setter
    def VisibleWidth(self, visible_width: Width):
        """
        Setter for property: ( Width NXOpen.P) VisibleWidth
         Returns the visible width   
            
         
        """
        pass
import NXOpen
class ViewPreferences(NXOpen.Object): 
    """ Represents set of style applicable to drafting views. """
    @property
    def General() -> GeneralViewPreferences:
        """
         Returns object for doing View style settings applicable to General 
        """
        pass
    @property
    def BaseView() -> BaseViewPreferences:
        """
         Returns object for doing View style settings applicable to BaseView 
        """
        pass
    @property
    def Projected() -> ProjectedViewPreferences:
        """
         Returns object for doing View Preferences settings applicable to Projected 
        """
        pass
    @property
    def InheritPmi() -> InheritPmiPreferences:
        """
         Returns object for doing View Preferences settings applicable to Inherit Pmi 
        """
        pass
    @property
    def Detail() -> DetailViewPreferences:
        """
         Returns object for doing View Preferences settings applicable to Detail 
        """
        pass
    @property
    def Section() -> SectionViewPreferences:
        """
         Returns object for doing View Preferences settings applicable to Section 
        """
        pass
    @property
    def VirtualIntersections() -> VirtualIntersectionsViewPreferences:
        """
         Returns object for doing View Preferences settings applicable to VirtualIntersections 
        """
        pass
    @property
    def SmoothEdges() -> SmoothEdgesViewPreferences:
        """
         Returns object for doing View Preferences settings applicable to SmoothEdges 
        """
        pass
    @property
    def VisibleLines() -> VisibleLinesViewPreferences:
        """
         Returns object for doing View Preferences settings applicable to VisibleLines 
        """
        pass
    @property
    def Threads() -> ThreadsViewPreferences:
        """
         Returns object for doing View Preferences settings applicable to Threads 
        """
        pass
    @property
    def TraceLines() -> TraceLinesViewPreferences:
        """
         Returns object for doing View Preferences settings applicable to TraceLines 
        """
        pass
    @property
    def HiddenLines() -> HiddenLinesViewPreferences:
        """
         Returns object for doing View Preferences settings applicable to HiddenLines 
        """
        pass
    @property
    def Shading() -> ShadingViewPreferences:
        """
         Returns object for doing View Preferences settings applicable to Shading 
        """
        pass
    @property
    def FlatPattern() -> FlatPatternViewPreferences:
        """
         Returns object for doing View Preferences settings applicable to Flat Patterns 
        """
        pass
    @property
    def ShipbuildingLines() -> ShipbuildingLinesViewPreferences:
        """
         Returns object for doing View Preferences settings applicable to Shipbuilding Lines 
        """
        pass
    @property
    def ShipDraftingViewLines() -> ShipDraftingViewLinesViewPreferences:
        """
         Returns object for doing View Preferences settings applicable to Ship Drafting View Lines 
        """
        pass
    @property
    def ShipGeneralArrangementViewLines() -> ShipGeneralArrangementViewLinesViewPreferences:
        """
         Returns object for doing View Preferences settings applicable to Ship General Arrangement View Lines 
        """
        pass
import NXOpen
class ViewSection(NXOpen.Builder): 
    """ Records  queries view section preferences. """
    @property
    def LoadExact(self) -> bool:
        """
        Getter for property: (bool) LoadExact
         Returns the load exact geometry on a save section curves operation
                    view section preference.  
             
         
        """
        pass
    @LoadExact.setter
    def LoadExact(self, loadExact: bool):
        """
        Setter for property: (bool) LoadExact
         Returns the load exact geometry on a save section curves operation
                    view section preference.  
             
         
        """
        pass
    @property
    def TranslucentPlanes(self) -> bool:
        """
        Getter for property: (bool) TranslucentPlanes
         Returns the translucent plane setting view section preference.  
             
         
        """
        pass
    @TranslucentPlanes.setter
    def TranslucentPlanes(self, translucentPlanes: bool):
        """
        Setter for property: (bool) TranslucentPlanes
         Returns the translucent plane setting view section preference.  
             
         
        """
        pass
    def SetDefaults(self) -> None:
        """
         Set current view section preferences to the default 
                    customer default values.
                 
        """
        pass
import NXOpen
class ViewVisualizationSpecialEffects(NXOpen.Object): 
    """ Represents the set of visualization special effect preferences applicable to entire session. 
Mainly sets fog preferences. Fog is the ability to display close objects in shades that are different 
than those of distant objects resulting in a display that shows which geometry is closest to the 
viewer and which is furthest.
"""
    class FogType(Enum):
        """
        Members Include: 
         |Linear|  Linear Fog  
         |Light|  Non linear Fog. Light fog produces a fog effect less pervasive than Heavy fog 
         |Heavy|  Non linear Fog 

        """
        Linear: int
        Light: int
        Heavy: int
        @staticmethod
        def ValueOf(value: int) -> ViewVisualizationSpecialEffects.FogType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ColorHLS:
        """
         Represents three constituents of a HLS color pattern 
         ViewVisualizationSpecialEffectsColorHLS_Struct NXOpen.P is an alias for  ViewVisualizationSpecialEffects.ColorHLS NXOpen.P.
        """
        @property
        def Hue(self) -> float:
            """
            Getter for property Hue
            Hue in HSV pattern is the color type (such as red, blue, or yellow) Ranges from 0-360

            """
            pass
        @Hue.setter
        def Hue(self, value: float):
            """
            Getter for property Hue
            Hue in HSV pattern is the color type (such as red, blue, or yellow) Ranges from 0-360
            Setter for property Hue
            Hue in HSV pattern is the color type (such as red, blue, or yellow) Ranges from 0-360

            """
            pass
        @property
        def Lightness(self) -> float:
            """
            Getter for property Lightness
            Lightness in HLS pattern Ranges from 0-255

            """
            pass
        @Lightness.setter
        def Lightness(self, value: float):
            """
            Getter for property Lightness
            Lightness in HLS pattern Ranges from 0-255
            Setter for property Lightness
            Lightness in HLS pattern Ranges from 0-255

            """
            pass
        @property
        def Saturation(self) -> float:
            """
            Getter for property Saturation
            Saturation in HSV pattern is the vibrancy of the color Ranges from 0-255

            """
            pass
        @Saturation.setter
        def Saturation(self, value: float):
            """
            Getter for property Saturation
            Saturation in HSV pattern is the vibrancy of the color Ranges from 0-255
            Setter for property Saturation
            Saturation in HSV pattern is the vibrancy of the color Ranges from 0-255

            """
            pass
    class ColorHSV:
        """
         Represents three constituents of a HSV color pattern 
         ViewVisualizationSpecialEffectsColorHSV_Struct NXOpen.P is an alias for  ViewVisualizationSpecialEffects.ColorHSV NXOpen.P.
        """
        @property
        def Hue(self) -> float:
            """
            Getter for property Hue
            Hue in HSV pattern is the color  type (such as red, blue, or yellow) Ranges from 0-360

            """
            pass
        @Hue.setter
        def Hue(self, value: float):
            """
            Getter for property Hue
            Hue in HSV pattern is the color  type (such as red, blue, or yellow) Ranges from 0-360
            Setter for property Hue
            Hue in HSV pattern is the color  type (such as red, blue, or yellow) Ranges from 0-360

            """
            pass
        @property
        def Saturation(self) -> float:
            """
            Getter for property Saturation
            Saturation in HSV pattern is the vibrancy of the color Ranges from 0-255

            """
            pass
        @Saturation.setter
        def Saturation(self, value: float):
            """
            Getter for property Saturation
            Saturation in HSV pattern is the vibrancy of the color Ranges from 0-255
            Setter for property Saturation
            Saturation in HSV pattern is the vibrancy of the color Ranges from 0-255

            """
            pass
        @property
        def Value(self) -> float:
            """
            Getter for property Value
            Value in HSV pattern is the brightness of the color Ranges from 0-255

            """
            pass
        @Value.setter
        def Value(self, value: float):
            """
            Getter for property Value
            Value in HSV pattern is the brightness of the color Ranges from 0-255
            Setter for property Value
            Value in HSV pattern is the brightness of the color Ranges from 0-255

            """
            pass
    class ColorRGB:
        """
         Represents three constituents of a RGB color pattern 
         ViewVisualizationSpecialEffectsColorRGB_Struct NXOpen.P is an alias for  ViewVisualizationSpecialEffects.ColorRGB NXOpen.P.
        """
        @property
        def RedColor(self) -> float:
            """
            Getter for property RedColor
            Red in RGB pattern

            """
            pass
        @RedColor.setter
        def RedColor(self, value: float):
            """
            Getter for property RedColor
            Red in RGB pattern
            Setter for property RedColor
            Red in RGB pattern

            """
            pass
        @property
        def GreenColor(self) -> float:
            """
            Getter for property GreenColor
            Green in RGB pattern

            """
            pass
        @GreenColor.setter
        def GreenColor(self, value: float):
            """
            Getter for property GreenColor
            Green in RGB pattern
            Setter for property GreenColor
            Green in RGB pattern

            """
            pass
        @property
        def BlueColor(self) -> float:
            """
            Getter for property BlueColor
            Blue in RGB pattern

            """
            pass
        @BlueColor.setter
        def BlueColor(self, value: float):
            """
            Getter for property BlueColor
            Blue in RGB pattern
            Setter for property BlueColor
            Blue in RGB pattern

            """
            pass
    class FogData:
        """
         Represents the constituents of fog data 
         ViewVisualizationSpecialEffectsFogData_Struct NXOpen.P is an alias for  ViewVisualizationSpecialEffects.FogData NXOpen.P.
        """
        @property
        def FogMode(self) -> int:
            """
            Getter for property FogMode
            Fog mode

            """
            pass
        @FogMode.setter
        def FogMode(self, value: int):
            """
            Getter for property FogMode
            Fog mode
            Setter for property FogMode
            Fog mode

            """
            pass
        @property
        def FogColorFlag(self) -> bool:
            """
            Getter for property FogColorFlag
            If true fog color is applied to the view

            """
            pass
        @FogColorFlag.setter
        def FogColorFlag(self, value: bool):
            """
            Getter for property FogColorFlag
            If true fog color is applied to the view
            Setter for property FogColorFlag
            If true fog color is applied to the view

            """
            pass
        @property
        def FogColor(self) -> ViewVisualizationSpecialEffects.ColorRGB:
            """
            Getter for property FogColor
            Fog Color

            """
            pass
        @FogColor.setter
        def FogColor(self, value: ViewVisualizationSpecialEffects.ColorRGB):
            """
            Getter for property FogColor
            Fog Color
            Setter for property FogColor
            Fog Color

            """
            pass
        @property
        def FogStart(self) -> float:
            """
            Getter for property FogStart
            Start of fog

            """
            pass
        @FogStart.setter
        def FogStart(self, value: float):
            """
            Getter for property FogStart
            Start of fog
            Setter for property FogStart
            Start of fog

            """
            pass
        @property
        def FogEnd(self) -> float:
            """
            Getter for property FogEnd
            End of fog

            """
            pass
        @FogEnd.setter
        def FogEnd(self, value: float):
            """
            Getter for property FogEnd
            End of fog
            Setter for property FogEnd
            End of fog

            """
            pass
        @property
        def FogDensity(self) -> float:
            """
            Getter for property FogDensity
            Density of fog

            """
            pass
        @FogDensity.setter
        def FogDensity(self, value: float):
            """
            Getter for property FogDensity
            Density of fog
            Setter for property FogDensity
            Density of fog

            """
            pass
    @property
    def FogBackValue(self) -> int:
        """
        Getter for property: (int) FogBackValue
         Returns the fog back scale value.  
           The Back scale defines the point at which fog reaches its maximum.   
         
        """
        pass
    @FogBackValue.setter
    def FogBackValue(self, fog_back_value: int):
        """
        Setter for property: (int) FogBackValue
         Returns the fog back scale value.  
           The Back scale defines the point at which fog reaches its maximum.   
         
        """
        pass
    @property
    def FogBackgroundColor(self) -> bool:
        """
        Getter for property: (bool) FogBackgroundColor
         Returns the use background color flag.  
           If true background color is used as fog color   
         
        """
        pass
    @FogBackgroundColor.setter
    def FogBackgroundColor(self, fog_background_color: bool):
        """
        Setter for property: (bool) FogBackgroundColor
         Returns the use background color flag.  
           If true background color is used as fog color   
         
        """
        pass
    @property
    def FogColorHLSValue(self) -> ViewVisualizationSpecialEffects.ColorHLS:
        """
        Getter for property: ( ViewVisualizationSpecialEffects.ColorHLS NXOpen.P) FogColorHLSValue
         Returns the value of HLS color pattern  
            
         
        """
        pass
    @FogColorHLSValue.setter
    def FogColorHLSValue(self, fog_color_hls_value: ViewVisualizationSpecialEffects.ColorHLS):
        """
        Setter for property: ( ViewVisualizationSpecialEffects.ColorHLS NXOpen.P) FogColorHLSValue
         Returns the value of HLS color pattern  
            
         
        """
        pass
    @property
    def FogColorHSVValue(self) -> ViewVisualizationSpecialEffects.ColorHSV:
        """
        Getter for property: ( ViewVisualizationSpecialEffects.ColorHSV NXOpen.P) FogColorHSVValue
         Returns the value of HSV color pattern  
            
         
        """
        pass
    @FogColorHSVValue.setter
    def FogColorHSVValue(self, fog_color_hsv_value: ViewVisualizationSpecialEffects.ColorHSV):
        """
        Setter for property: ( ViewVisualizationSpecialEffects.ColorHSV NXOpen.P) FogColorHSVValue
         Returns the value of HSV color pattern  
            
         
        """
        pass
    @property
    def FogColorRGBValue(self) -> ViewVisualizationSpecialEffects.ColorRGB:
        """
        Getter for property: ( ViewVisualizationSpecialEffects.ColorRGB NXOpen.P) FogColorRGBValue
         Returns the value of RGB color pattern  
            
         
        """
        pass
    @FogColorRGBValue.setter
    def FogColorRGBValue(self, fog_color_rgb_value: ViewVisualizationSpecialEffects.ColorRGB):
        """
        Setter for property: ( ViewVisualizationSpecialEffects.ColorRGB NXOpen.P) FogColorRGBValue
         Returns the value of RGB color pattern  
            
         
        """
        pass
    @property
    def FogFrontValue(self) -> int:
        """
        Getter for property: (int) FogFrontValue
         Returns the fog front scale value.  
           The front scale defines the beginning of fog.   
         
        """
        pass
    @FogFrontValue.setter
    def FogFrontValue(self, fog_front_value: int):
        """
        Setter for property: (int) FogFrontValue
         Returns the fog front scale value.  
           The front scale defines the beginning of fog.   
         
        """
        pass
    @property
    def FogRateValue(self) -> int:
        """
        Getter for property: (int) FogRateValue
         Returns the fog rate value.  
           Specifies the rate at which an object fades as the distance in the view increases.   
         
        """
        pass
    @FogRateValue.setter
    def FogRateValue(self, fog_rate_value: int):
        """
        Setter for property: (int) FogRateValue
         Returns the fog rate value.  
           Specifies the rate at which an object fades as the distance in the view increases.   
         
        """
        pass
    @property
    def FogSetting(self) -> ViewVisualizationSpecialEffects.FogType:
        """
        Getter for property: ( ViewVisualizationSpecialEffects.FogType NXOpen.P) FogSetting
         Returns the fog setting type   
            
         
        """
        pass
    @FogSetting.setter
    def FogSetting(self, fog_setting: ViewVisualizationSpecialEffects.FogType):
        """
        Setter for property: ( ViewVisualizationSpecialEffects.FogType NXOpen.P) FogSetting
         Returns the fog setting type   
            
         
        """
        pass
    @property
    def FogSettingOption(self) -> bool:
        """
        Getter for property: (bool) FogSettingOption
         Returns the fog option.  
           If true fog settings are available and applied to display   
         
        """
        pass
    @FogSettingOption.setter
    def FogSettingOption(self, fog_setting_option: bool):
        """
        Setter for property: (bool) FogSettingOption
         Returns the fog option.  
           If true fog settings are available and applied to display   
         
        """
        pass
    def UpdateFogDisplay(self, fog_data: ViewVisualizationSpecialEffects.FogData) -> None:
        """
         Applies current fog settings to display 
        """
        pass
import NXOpen
class ViewVisualizationVisual(NXOpen.Object): 
    """ Represents the set of View related Visualization visual preferences """
    class DisplayModeType(Enum):
        """
        Members Include: 
         |Wireframe|  View is displayed as a wireframe-model 
         |PartiallyShaded|  Shade only selected object 
         |FullyShaded|  Shading is applicable to all objects in view 
         |FaceAnalysis|  Display faces using the color analysis data  
         |Studio|  In Studio mode, objects are realistically 
                                                                                     rendered according to material and texture 
                                                                                     characteristics assigned to them 

        """
        Wireframe: int
        PartiallyShaded: int
        FullyShaded: int
        FaceAnalysis: int
        Studio: int
        @staticmethod
        def ValueOf(value: int) -> ViewVisualizationVisual.DisplayModeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class HiddenEdgeColorStyleType(Enum):
        """
        Members Include: 
         |ObjectColor|  Object Color 
         |HiddenGeometryColor|  Hidden Geometry Color 

        """
        ObjectColor: int
        HiddenGeometryColor: int
        @staticmethod
        def ValueOf(value: int) -> ViewVisualizationVisual.HiddenEdgeColorStyleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class HiddenEdgeStyleType(Enum):
        """
        Members Include: 
         |Invisible|   
         |HiddenGeometryColor|   
         |Dashed|   

        """
        Invisible: int
        HiddenGeometryColor: int
        Dashed: int
        @staticmethod
        def ValueOf(value: int) -> ViewVisualizationVisual.HiddenEdgeStyleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class HiddenEdges(Enum):
        """
        Members Include: 
         |Visible|   
         |Invisible|   
         |GrayThin|   
         |Dashed|   

        """
        Visible: int
        Invisible: int
        GrayThin: int
        Dashed: int
        @staticmethod
        def ValueOf(value: int) -> ViewVisualizationVisual.HiddenEdges:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class HiddenEdgesType(Enum):
        """
        Members Include: 
         |Visible|  All edges in a solid body that are hidden appear 
                                                                                 as solid lines  
         |Invisible|  grid line display of all existing and subsequently 
                                                                                 created solid bodies in the selected view, except 
                                                                                 that portions of geometry and text that appear 
                                                                                 behind solid bodies are erased 
         |Dashed|  grid line display of all existing and subsequently 
                                                                                 created solid bodies in the selected view, except 
                                                                                 that all portions of the geometry and text that 
                                                                                 appear behind solid bodies are displayed as dashed 
                                                                                 lines 
         |GrayThin|  All hidden edges in the color gray, with solid font
                                                                                 and thin width. 
         |HiddenSurface|  Faceted display of all existing and subsequently 
                                                                                 created bodies in the selected view 

        """
        Visible: int
        Invisible: int
        Dashed: int
        GrayThin: int
        HiddenSurface: int
        @staticmethod
        def ValueOf(value: int) -> ViewVisualizationVisual.HiddenEdgesType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class InterferingSolids(Enum):
        """
        Members Include: 
         |Off|  Do not process solid interferences when rendering. 
         |On|  Do process basic solid interferences when rendering. 
         |WithCurves|  Do process solid interferences and 
                                                                                         interference curves when rendering. 

        """
        Off: int
        On: int
        WithCurves: int
        @staticmethod
        def ValueOf(value: int) -> ViewVisualizationVisual.InterferingSolids:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RenderingStyle(Enum):
        """
        Members Include: 
         |Shaded|   
         |Wireframe|   
         |Studio|   
         |FaceAnalysis|   
         |PartiallyShaded|   
         |StaticWireframe|   

        """
        Shaded: int
        Wireframe: int
        Studio: int
        FaceAnalysis: int
        PartiallyShaded: int
        StaticWireframe: int
        @staticmethod
        def ValueOf(value: int) -> ViewVisualizationVisual.RenderingStyle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ShadedEdgeStyleType(Enum):
        """
        Members Include: 
         |ShadedEdgeColor|   
         |BodyColor|   
         |NotSet|   

        """
        ShadedEdgeColor: int
        BodyColor: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> ViewVisualizationVisual.ShadedEdgeStyleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SmoothEdgeFont(Enum):
        """
        Members Include: 
         |Original|   
         |Solid|   
         |Dashed|   
         |Phantom|   
         |CenterLine|   
         |Dotted|   
         |LongDashed|   
         |DottedDashed|   
         |Eight|  Long Dashed Double Dotted
         |Nine|  Long Dashed Dotted for OOTB fonts and Undulating for shipbuilding fonts 
         |Ten|  Long Dashed Triplicate Dotted for OOTB fonts and Zigzag for shipbuilding fonts 
         |Eleven|  Long Dashed Double Short Dashed for OOTB fonts and Railway for shipbuilding fonts 

        """
        Original: int
        Solid: int
        Dashed: int
        Phantom: int
        CenterLine: int
        Dotted: int
        LongDashed: int
        DottedDashed: int
        Eight: int
        Nine: int
        Ten: int
        Eleven: int
        @staticmethod
        def ValueOf(value: int) -> ViewVisualizationVisual.SmoothEdgeFont:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SmoothEdgeWidth(Enum):
        """
        Members Include: 
         |Original|   
         |Thin|   
         |Normal|   
         |Thick|   
         |One|   
         |Two|   
         |Three|   
         |Four|   
         |Five|   
         |Six|   
         |Seven|   
         |Eight|   
         |Nine|   

        """
        Original: int
        Thin: int
        Normal: int
        Thick: int
        One: int
        Two: int
        Three: int
        Four: int
        Five: int
        Six: int
        Seven: int
        Eight: int
        Nine: int
        @staticmethod
        def ValueOf(value: int) -> ViewVisualizationVisual.SmoothEdgeWidth:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DisplayAppearanceOptions:
        """
         Describes the rendering style and the appearance of edges and silhouettes in the view. 
         ViewVisualizationVisualDisplayAppearanceOptions_Struct NXOpen.P is an alias for  ViewVisualizationVisual.DisplayAppearanceOptions NXOpen.P.
        """
        @property
        def RenderingStyle(self) -> ViewVisualizationVisual.RenderingStyle:
            """
            Getter for property RenderingStyle
            Rendering style for geometry.

            """
            pass
        @RenderingStyle.setter
        def RenderingStyle(self, value: ViewVisualizationVisual.RenderingStyle):
            """
            Getter for property RenderingStyle
            Rendering style for geometry.
            Setter for property RenderingStyle
            Rendering style for geometry.

            """
            pass
        @property
        def HiddenEdges(self) -> ViewVisualizationVisual.HiddenEdges:
            """
            Getter for property HiddenEdges
            Appearance of hidden edges

            """
            pass
        @HiddenEdges.setter
        def HiddenEdges(self, value: ViewVisualizationVisual.HiddenEdges):
            """
            Getter for property HiddenEdges
            Appearance of hidden edges
            Setter for property HiddenEdges
            Appearance of hidden edges

            """
            pass
        @property
        def InterferingSolids(self) -> ViewVisualizationVisual.InterferingSolids:
            """
            Getter for property InterferingSolids
            Allows to control the level of processing                                                                            when solid interference occurs.

            """
            pass
        @InterferingSolids.setter
        def InterferingSolids(self, value: ViewVisualizationVisual.InterferingSolids):
            """
            Getter for property InterferingSolids
            Allows to control the level of processing                                                                            when solid interference occurs.
            Setter for property InterferingSolids
            Allows to control the level of processing                                                                            when solid interference occurs.

            """
            pass
        @property
        def Silhouettes(self) -> bool:
            """
            Getter for property Silhouettes
            Allows to control whether the silhouettes                                                                             (or outlines) on cones, cylinders, spheres,                                                                             and Tori solid bodies display.

            """
            pass
        @Silhouettes.setter
        def Silhouettes(self, value: bool):
            """
            Getter for property Silhouettes
            Allows to control whether the silhouettes                                                                             (or outlines) on cones, cylinders, spheres,                                                                             and Tori solid bodies display.
            Setter for property Silhouettes
            Allows to control whether the silhouettes                                                                             (or outlines) on cones, cylinders, spheres,                                                                             and Tori solid bodies display.

            """
            pass
        @property
        def SmoothEdges(self) -> bool:
            """
            Getter for property SmoothEdges
            Allows to control whether edges shared by                                                                             tangent faces display or not.

            """
            pass
        @SmoothEdges.setter
        def SmoothEdges(self, value: bool):
            """
            Getter for property SmoothEdges
            Allows to control whether edges shared by                                                                             tangent faces display or not.
            Setter for property SmoothEdges
            Allows to control whether edges shared by                                                                             tangent faces display or not.

            """
            pass
        @property
        def SmoothEdgeColor(self) -> int:
            """
            Getter for property SmoothEdgeColor
            Color attribute for visible smooth edges

            """
            pass
        @SmoothEdgeColor.setter
        def SmoothEdgeColor(self, value: int):
            """
            Getter for property SmoothEdgeColor
            Color attribute for visible smooth edges
            Setter for property SmoothEdgeColor
            Color attribute for visible smooth edges

            """
            pass
        @property
        def SmoothEdgeFont(self) -> ViewVisualizationVisual.SmoothEdgeFont:
            """
            Getter for property SmoothEdgeFont
            Font attribute for visible smooth edges

            """
            pass
        @SmoothEdgeFont.setter
        def SmoothEdgeFont(self, value: ViewVisualizationVisual.SmoothEdgeFont):
            """
            Getter for property SmoothEdgeFont
            Font attribute for visible smooth edges
            Setter for property SmoothEdgeFont
            Font attribute for visible smooth edges

            """
            pass
        @property
        def SmoothEdgeWidth(self) -> ViewVisualizationVisual.SmoothEdgeWidth:
            """
            Getter for property SmoothEdgeWidth
            Width attribute for visible smooth edges

            """
            pass
        @SmoothEdgeWidth.setter
        def SmoothEdgeWidth(self, value: ViewVisualizationVisual.SmoothEdgeWidth):
            """
            Getter for property SmoothEdgeWidth
            Width attribute for visible smooth edges
            Setter for property SmoothEdgeWidth
            Width attribute for visible smooth edges

            """
            pass
        @property
        def SmoothEdgeAngleTolerance(self) -> float:
            """
            Getter for property SmoothEdgeAngleTolerance
            Angle tolerance (in degrees)                                                                             attribute for visible smooth edges.

            """
            pass
        @SmoothEdgeAngleTolerance.setter
        def SmoothEdgeAngleTolerance(self, value: float):
            """
            Getter for property SmoothEdgeAngleTolerance
            Angle tolerance (in degrees)                                                                             attribute for visible smooth edges.
            Setter for property SmoothEdgeAngleTolerance
            Angle tolerance (in degrees)                                                                             attribute for visible smooth edges.

            """
            pass
    class SurfaceDisplayOptions:
        """
         Describes the appearance of edges and silhouettes in the view. 
         ViewVisualizationVisualSurfaceDisplayOptions_Struct NXOpen.P is an alias for  ViewVisualizationVisual.SurfaceDisplayOptions NXOpen.P.
        """
        @property
        def RenderingStyle(self) -> ViewVisualizationVisual.RenderingStyle:
            """
            Getter for property RenderingStyle
            Rendering style for geometry.

            """
            pass
        @RenderingStyle.setter
        def RenderingStyle(self, value: ViewVisualizationVisual.RenderingStyle):
            """
            Getter for property RenderingStyle
            Rendering style for geometry.
            Setter for property RenderingStyle
            Rendering style for geometry.

            """
            pass
        @property
        def HiddenEdges(self) -> ViewVisualizationVisual.HiddenEdges:
            """
            Getter for property HiddenEdges
            Appearance of hidden edges

            """
            pass
        @HiddenEdges.setter
        def HiddenEdges(self, value: ViewVisualizationVisual.HiddenEdges):
            """
            Getter for property HiddenEdges
            Appearance of hidden edges
            Setter for property HiddenEdges
            Appearance of hidden edges

            """
            pass
        @property
        def Silhouettes(self) -> bool:
            """
            Getter for property Silhouettes
            Allows to control whether the silhouettes                                                                           (or outlines) on cones, cylinders, spheres,                                                                           and Tori solid bodies display.

            """
            pass
        @Silhouettes.setter
        def Silhouettes(self, value: bool):
            """
            Getter for property Silhouettes
            Allows to control whether the silhouettes                                                                           (or outlines) on cones, cylinders, spheres,                                                                           and Tori solid bodies display.
            Setter for property Silhouettes
            Allows to control whether the silhouettes                                                                           (or outlines) on cones, cylinders, spheres,                                                                           and Tori solid bodies display.

            """
            pass
        @property
        def SmoothEdges(self) -> bool:
            """
            Getter for property SmoothEdges
            Allows to control whether edges shared by                                                                           tangent faces display or not.

            """
            pass
        @SmoothEdges.setter
        def SmoothEdges(self, value: bool):
            """
            Getter for property SmoothEdges
            Allows to control whether edges shared by                                                                           tangent faces display or not.
            Setter for property SmoothEdges
            Allows to control whether edges shared by                                                                           tangent faces display or not.

            """
            pass
        @property
        def SmoothEdgeColor(self) -> int:
            """
            Getter for property SmoothEdgeColor
            Color attribute for visible smooth edges

            """
            pass
        @SmoothEdgeColor.setter
        def SmoothEdgeColor(self, value: int):
            """
            Getter for property SmoothEdgeColor
            Color attribute for visible smooth edges
            Setter for property SmoothEdgeColor
            Color attribute for visible smooth edges

            """
            pass
        @property
        def SmoothEdgeFont(self) -> ViewVisualizationVisual.SmoothEdgeFont:
            """
            Getter for property SmoothEdgeFont
            Font attribute for visible smooth edges

            """
            pass
        @SmoothEdgeFont.setter
        def SmoothEdgeFont(self, value: ViewVisualizationVisual.SmoothEdgeFont):
            """
            Getter for property SmoothEdgeFont
            Font attribute for visible smooth edges
            Setter for property SmoothEdgeFont
            Font attribute for visible smooth edges

            """
            pass
        @property
        def SmoothEdgeWidth(self) -> ViewVisualizationVisual.SmoothEdgeWidth:
            """
            Getter for property SmoothEdgeWidth
            Width attribute for visible smooth edges

            """
            pass
        @SmoothEdgeWidth.setter
        def SmoothEdgeWidth(self, value: ViewVisualizationVisual.SmoothEdgeWidth):
            """
            Getter for property SmoothEdgeWidth
            Width attribute for visible smooth edges
            Setter for property SmoothEdgeWidth
            Width attribute for visible smooth edges

            """
            pass
    class TrueSurfaceDisplayPref:
        """
         Represents the various surface display parameters. 
         ViewVisualizationVisualTrueSurfaceDisplayPref_Struct NXOpen.P is an alias for  ViewVisualizationVisual.TrueSurfaceDisplayPref NXOpen.P.
        """
        @property
        def HiddenEdgesType(self) -> ViewVisualizationVisual.HiddenEdgesType:
            """
            Getter for property HiddenEdgesType
            Hidden Edge Type

            """
            pass
        @HiddenEdgesType.setter
        def HiddenEdgesType(self, value: ViewVisualizationVisual.HiddenEdgesType):
            """
            Getter for property HiddenEdgesType
            Hidden Edge Type
            Setter for property HiddenEdgesType
            Hidden Edge Type

            """
            pass
        @property
        def Silhouettes(self) -> bool:
            """
            Getter for property Silhouettes
            Allows to control whether the silhouettes                                                                             (or outlines) on cones, cylinders, spheres,                                                                             and Tori solid bodies display.

            """
            pass
        @Silhouettes.setter
        def Silhouettes(self, value: bool):
            """
            Getter for property Silhouettes
            Allows to control whether the silhouettes                                                                             (or outlines) on cones, cylinders, spheres,                                                                             and Tori solid bodies display.
            Setter for property Silhouettes
            Allows to control whether the silhouettes                                                                             (or outlines) on cones, cylinders, spheres,                                                                             and Tori solid bodies display.

            """
            pass
        @property
        def SmoothEdges(self) -> bool:
            """
            Getter for property SmoothEdges
            Allows to control whether edges shared by                                                                             tangent faces display or not.

            """
            pass
        @SmoothEdges.setter
        def SmoothEdges(self, value: bool):
            """
            Getter for property SmoothEdges
            Allows to control whether edges shared by                                                                             tangent faces display or not.
            Setter for property SmoothEdges
            Allows to control whether edges shared by                                                                             tangent faces display or not.

            """
            pass
        @property
        def SmoothEdgesColor(self) -> int:
            """
            Getter for property SmoothEdgesColor
            Color attribute for visible smooth edges

            """
            pass
        @SmoothEdgesColor.setter
        def SmoothEdgesColor(self, value: int):
            """
            Getter for property SmoothEdgesColor
            Color attribute for visible smooth edges
            Setter for property SmoothEdgesColor
            Color attribute for visible smooth edges

            """
            pass
        @property
        def SmoothEdgesFont(self) -> ViewVisualizationVisual.SmoothEdgeFont:
            """
            Getter for property SmoothEdgesFont
            Font attribute for visible smooth edges

            """
            pass
        @SmoothEdgesFont.setter
        def SmoothEdgesFont(self, value: ViewVisualizationVisual.SmoothEdgeFont):
            """
            Getter for property SmoothEdgesFont
            Font attribute for visible smooth edges
            Setter for property SmoothEdgesFont
            Font attribute for visible smooth edges

            """
            pass
        @property
        def SmoothEdgesWidth(self) -> ViewVisualizationVisual.SmoothEdgeWidth:
            """
            Getter for property SmoothEdgesWidth
            Width attribute for visible smooth edges

            """
            pass
        @SmoothEdgesWidth.setter
        def SmoothEdgesWidth(self, value: ViewVisualizationVisual.SmoothEdgeWidth):
            """
            Getter for property SmoothEdgesWidth
            Width attribute for visible smooth edges
            Setter for property SmoothEdgesWidth
            Width attribute for visible smooth edges

            """
            pass
        @property
        def DisplayMode(self) -> ViewVisualizationVisual.DisplayModeType:
            """
            Getter for property DisplayMode
            Display Mode

            """
            pass
        @DisplayMode.setter
        def DisplayMode(self, value: ViewVisualizationVisual.DisplayModeType):
            """
            Getter for property DisplayMode
            Display Mode
            Setter for property DisplayMode
            Display Mode

            """
            pass
    @property
    def DisplayAppearance(self) -> ViewVisualizationVisual.DisplayAppearanceOptions:
        """
        Getter for property: ( ViewVisualizationVisual.DisplayAppearanceOptions NXOpen.P) DisplayAppearance
         Returns the rendering style and the edge display options of the view.  
             
         
        """
        pass
    @DisplayAppearance.setter
    def DisplayAppearance(self, display_appearance_options: ViewVisualizationVisual.DisplayAppearanceOptions):
        """
        Setter for property: ( ViewVisualizationVisual.DisplayAppearanceOptions NXOpen.P) DisplayAppearance
         Returns the rendering style and the edge display options of the view.  
             
         
        """
        pass
    @property
    def HiddenEdgeColorStyle(self) -> ViewVisualizationVisual.HiddenEdgeColorStyleType:
        """
        Getter for property: ( ViewVisualizationVisual.HiddenEdgeColorStyleType NXOpen.P) HiddenEdgeColorStyle
         Returns the hidden edge color type for harware wireframe in the view.  
             
         
        """
        pass
    @HiddenEdgeColorStyle.setter
    def HiddenEdgeColorStyle(self, hiddenEdgeColorStyle: ViewVisualizationVisual.HiddenEdgeColorStyleType):
        """
        Setter for property: ( ViewVisualizationVisual.HiddenEdgeColorStyleType NXOpen.P) HiddenEdgeColorStyle
         Returns the hidden edge color type for harware wireframe in the view.  
             
         
        """
        pass
    @property
    def HiddenEdgeStyle(self) -> ViewVisualizationVisual.HiddenEdgeStyleType:
        """
        Getter for property: ( ViewVisualizationVisual.HiddenEdgeStyleType NXOpen.P) HiddenEdgeStyle
         Returns the hidden edge display style for shaded faces in the view.  
             
         
        """
        pass
    @HiddenEdgeStyle.setter
    def HiddenEdgeStyle(self, hidden_edge_style: ViewVisualizationVisual.HiddenEdgeStyleType):
        """
        Setter for property: ( ViewVisualizationVisual.HiddenEdgeStyleType NXOpen.P) HiddenEdgeStyle
         Returns the hidden edge display style for shaded faces in the view.  
             
         
        """
        pass
    @property
    def ShadedEdgeColor(self) -> int:
        """
        Getter for property: (int) ShadedEdgeColor
         Returns the edge color for shaded faces in the view.  
             
         
        """
        pass
    @ShadedEdgeColor.setter
    def ShadedEdgeColor(self, shaded_edge_color: int):
        """
        Setter for property: (int) ShadedEdgeColor
         Returns the edge color for shaded faces in the view.  
             
         
        """
        pass
    @property
    def ShadedEdgeStyle(self) -> ViewVisualizationVisual.ShadedEdgeStyleType:
        """
        Getter for property: ( ViewVisualizationVisual.ShadedEdgeStyleType NXOpen.P) ShadedEdgeStyle
         Returns the edge display style for shaded faces in the view.  
             
         
        """
        pass
    @ShadedEdgeStyle.setter
    def ShadedEdgeStyle(self, shaded_edge_style: ViewVisualizationVisual.ShadedEdgeStyleType):
        """
        Setter for property: ( ViewVisualizationVisual.ShadedEdgeStyleType NXOpen.P) ShadedEdgeStyle
         Returns the edge display style for shaded faces in the view.  
             
         
        """
        pass
    @property
    def ShininessData(self) -> float:
        """
        Getter for property: (float) ShininessData
         Returns the shininess value.  
           Specifies the intensity of the graphics driver addition of highlights to shaded surfaces, 
            making them appear shiny. The value 0.0 adds no shininess, and 1.0 adds the maximum amount of shininess.   
         
        """
        pass
    @ShininessData.setter
    def ShininessData(self, shininess_data: float):
        """
        Setter for property: (float) ShininessData
         Returns the shininess value.  
           Specifies the intensity of the graphics driver addition of highlights to shaded surfaces, 
            making them appear shiny. The value 0.0 adds no shininess, and 1.0 adds the maximum amount of shininess.   
         
        """
        pass
    @property
    def SurfaceDisplay(self) -> ViewVisualizationVisual.SurfaceDisplayOptions:
        """
        Getter for property: ( ViewVisualizationVisual.SurfaceDisplayOptions NXOpen.P) SurfaceDisplay
         Returns the rendering style and the edge display options of the view.  
             
         
        """
        pass
    @SurfaceDisplay.setter
    def SurfaceDisplay(self, surface_display: ViewVisualizationVisual.SurfaceDisplayOptions):
        """
        Setter for property: ( ViewVisualizationVisual.SurfaceDisplayOptions NXOpen.P) SurfaceDisplay
         Returns the rendering style and the edge display options of the view.  
             
         
        """
        pass
    @property
    def TrueSurfaceDisplay(self) -> ViewVisualizationVisual.TrueSurfaceDisplayPref:
        """
        Getter for property: ( ViewVisualizationVisual.TrueSurfaceDisplayPref NXOpen.P) TrueSurfaceDisplay
         Returns the true surface display parameters.  
             
         
        """
        pass
    @TrueSurfaceDisplay.setter
    def TrueSurfaceDisplay(self, true_surface_display: ViewVisualizationVisual.TrueSurfaceDisplayPref):
        """
        Setter for property: ( ViewVisualizationVisual.TrueSurfaceDisplayPref NXOpen.P) TrueSurfaceDisplay
         Returns the true surface display parameters.  
             
         
        """
        pass
    @property
    def TwoSidedLight(self) -> bool:
        """
        Getter for property: (bool) TwoSidedLight
         Returns the two sided light flag.  
           Specifies whether lighting should be applied to both the front and backsides of faces. 
            If it is true, then lighting from a light source is applied to the front or the back face, depending on which side is 
            exposed to the light source. If this is false, then lighting is not applied to the back of a face even if the back is 
            exposed to the light source.   
         
        """
        pass
    @TwoSidedLight.setter
    def TwoSidedLight(self, two_sided_light: bool):
        """
        Setter for property: (bool) TwoSidedLight
         Returns the two sided light flag.  
           Specifies whether lighting should be applied to both the front and backsides of faces. 
            If it is true, then lighting from a light source is applied to the front or the back face, depending on which side is 
            exposed to the light source. If this is false, then lighting is not applied to the back of a face even if the back is 
            exposed to the light source.   
         
        """
        pass
import NXOpen
class VirtualIntersectionsViewPreferences(NXOpen.Object): 
    """ Represents set of Virtual Intersections View Preferences applicable to drafting views. 
        Allows to display imaginary intersection curves.
     """
    @property
    def AdjacentBlends(self) -> bool:
        """
        Getter for property: (bool) AdjacentBlends
         Returns the status of adjacent blends.  
            
         
        """
        pass
    @AdjacentBlends.setter
    def AdjacentBlends(self, adjacent_blends: bool):
        """
        Setter for property: (bool) AdjacentBlends
         Returns the status of adjacent blends.  
            
         
        """
        pass
    @property
    def AdjacentBlendsColor(self) -> int:
        """
        Getter for property: (int) AdjacentBlendsColor
         Returns the color of adjacent blends.  
           The value should be between 1 and 216.  
         
        """
        pass
    @AdjacentBlendsColor.setter
    def AdjacentBlendsColor(self, adjacent_blends_color: int):
        """
        Setter for property: (int) AdjacentBlendsColor
         Returns the color of adjacent blends.  
           The value should be between 1 and 216.  
         
        """
        pass
    @property
    def AdjacentBlendsEndGaps(self) -> bool:
        """
        Getter for property: (bool) AdjacentBlendsEndGaps
         Returns the status of adjacent blends end gaps.  
           It controls the display of visible ends. If True, the 
                    visible ends are suppressed from the display. The length of the suppressed end is in drawing 
                    units and is controlled by the value set in the End Gap field. If False, the visible ends are 
                    not suppressed from the display.
                   
         
        """
        pass
    @AdjacentBlendsEndGaps.setter
    def AdjacentBlendsEndGaps(self, adjacent_blends_end_gaps: bool):
        """
        Setter for property: (bool) AdjacentBlendsEndGaps
         Returns the status of adjacent blends end gaps.  
           It controls the display of visible ends. If True, the 
                    visible ends are suppressed from the display. The length of the suppressed end is in drawing 
                    units and is controlled by the value set in the End Gap field. If False, the visible ends are 
                    not suppressed from the display.
                   
         
        """
        pass
    @property
    def AdjacentBlendsEndGapsData(self) -> float:
        """
        Getter for property: (float) AdjacentBlendsEndGapsData
         Returns the value of adjacent blends end gaps.  
            
         
        """
        pass
    @AdjacentBlendsEndGapsData.setter
    def AdjacentBlendsEndGapsData(self, adjacent_blends_end_gaps_data: float):
        """
        Setter for property: (float) AdjacentBlendsEndGapsData
         Returns the value of adjacent blends end gaps.  
            
         
        """
        pass
    @property
    def AdjacentBlendsFont(self) -> Font:
        """
        Getter for property: ( Font NXOpen.P) AdjacentBlendsFont
         Returns the font of adjacent blends.  
            
         
        """
        pass
    @AdjacentBlendsFont.setter
    def AdjacentBlendsFont(self, adjacent_blends_font: Font):
        """
        Setter for property: ( Font NXOpen.P) AdjacentBlendsFont
         Returns the font of adjacent blends.  
            
         
        """
        pass
    @property
    def AdjacentBlendsWidth(self) -> Width:
        """
        Getter for property: ( Width NXOpen.P) AdjacentBlendsWidth
         Returns the width of adjacent blends.  
            
         
        """
        pass
    @AdjacentBlendsWidth.setter
    def AdjacentBlendsWidth(self, adjacent_blends_width: Width):
        """
        Setter for property: ( Width NXOpen.P) AdjacentBlendsWidth
         Returns the width of adjacent blends.  
            
         
        """
        pass
    @property
    def VirtualIntersection(self) -> bool:
        """
        Getter for property: (bool) VirtualIntersection
         Returns the status of virtual intersection.  
            
         
        """
        pass
    @VirtualIntersection.setter
    def VirtualIntersection(self, virtual_intersection: bool):
        """
        Setter for property: (bool) VirtualIntersection
         Returns the status of virtual intersection.  
            
         
        """
        pass
import NXOpen
class VisibleLinesViewPreferences(NXOpen.Object): 
    """ Represents set of Visible Lines View Preferences applicable to drafting views. """
    @property
    def VisibleColor(self) -> int:
        """
        Getter for property: (int) VisibleColor
         Returns the visible color.  
           The value should be between 1 and 216.   
         
        """
        pass
    @VisibleColor.setter
    def VisibleColor(self, visible_color: int):
        """
        Setter for property: (int) VisibleColor
         Returns the visible color.  
           The value should be between 1 and 216.   
         
        """
        pass
    @property
    def VisibleFont(self) -> Font:
        """
        Getter for property: ( Font NXOpen.P) VisibleFont
         Returns the visible font.  
             
         
        """
        pass
    @VisibleFont.setter
    def VisibleFont(self, visible_font: Font):
        """
        Setter for property: ( Font NXOpen.P) VisibleFont
         Returns the visible font.  
             
         
        """
        pass
    @property
    def VisibleWidth(self) -> Width:
        """
        Getter for property: ( Width NXOpen.P) VisibleWidth
         Returns the visible width.  
             
         
        """
        pass
    @VisibleWidth.setter
    def VisibleWidth(self, visible_width: Width):
        """
        Setter for property: ( Width NXOpen.P) VisibleWidth
         Returns the visible width.  
             
         
        """
        pass
import NXOpen
class VisualizationFonts(NXOpen.Object): 
    """ Represents visualization preferences for standard text fonts 
        applicable to the entire session """
    class StyleType(Enum):
        """
        Members Include: 
         |Regular| 
                    Regular or normal font style 
         |Bold| 
                    Bold font style 
         |Italic| 
                    Italic or oblique font style 
         |BoldItalic| 
                    Bold-italic or bold-oblique font style 

        """
        Regular: int
        Bold: int
        Italic: int
        BoldItalic: int
        @staticmethod
        def ValueOf(value: int) -> VisualizationFonts.StyleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetDefaultStandardTextFont() -> Tuple[str, VisualizationFonts.StyleType, int]:
        """
         Returns settings for the default standard text font 
         Returns A tuple consisting of (fontFamily, fontStyle, fontSize). 
         - fontFamily is: str.
                    the name of the font family .
         - fontStyle is:  VisualizationFonts.StyleType NXOpen.P.
                    the font style .
         - fontSize is: int.
                    the font size in points (72 points per inch) .

        """
        pass
    def SetDefaultStandardTextFont(fontFamily: str, fontStyle: VisualizationFonts.StyleType, fontSize: int) -> None:
        """
         Modifies settings for the default standard text font 
        """
        pass
import NXOpen
class VisualizationHandles(NXOpen.Object): 
    """ Represents the set of visualization preferences under handles tab applicable to entire session"""
    class HandleSizeValue(Enum):
        """
        Members Include: 
         |Small|  Small Handle Size 
         |Medium|  Medium Handle Size 
         |Large|  Large Handle Size 

        """
        Small: int
        Medium: int
        Large: int
        @staticmethod
        def ValueOf(value: int) -> VisualizationHandles.HandleSizeValue:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def HandleSize(self) -> int:
        """
        Getter for property: (int) HandleSize
         Returns the default handle size   
            
         
        """
        pass
    @HandleSize.setter
    def HandleSize(self, handleSize: int):
        """
        Setter for property: (int) HandleSize
         Returns the default handle size   
            
         
        """
        pass
    @property
    def ShowHandleHints(self) -> bool:
        """
        Getter for property: (bool) ShowHandleHints
         Returns the show handle hints flag.  
           If true displays handle hint when handle is preselected    
         
        """
        pass
    @ShowHandleHints.setter
    def ShowHandleHints(self, showHandleHints: bool):
        """
        Setter for property: (bool) ShowHandleHints
         Returns the show handle hints flag.  
           If true displays handle hint when handle is preselected    
         
        """
        pass
import NXOpen
class VisualizationLine(NXOpen.Object): 
    """ This class is for UI related preferences changes """
    @property
    def DepthSortedWireframe(self) -> bool:
        """
        Getter for property: (bool) DepthSortedWireframe
         Returns the depth sorted wireframe.  
           Specifies whether the graphics driver should sort objects by depth in wireframe views.   
         
        """
        pass
    @DepthSortedWireframe.setter
    def DepthSortedWireframe(self, depth_sorted_wireframe: bool):
        """
        Setter for property: (bool) DepthSortedWireframe
         Returns the depth sorted wireframe.  
           Specifies whether the graphics driver should sort objects by depth in wireframe views.   
         
        """
        pass
    @property
    def WireframeContrast(self) -> bool:
        """
        Getter for property: (bool) WireframeContrast
         Returns whether colors applied to wireframe geometry are automatically adjusted as necessary to produce a minimum contrast relative to the view background.  
           
                The option affects onscreen displays only, so it affects interactive displays and raster images captured from interactive displays. It does not affect vector output produced by Plot, Print, CGM Export and similar functions.   
         
        """
        pass
    @WireframeContrast.setter
    def WireframeContrast(self, wireframe_contrast: bool):
        """
        Setter for property: (bool) WireframeContrast
         Returns whether colors applied to wireframe geometry are automatically adjusted as necessary to produce a minimum contrast relative to the view background.  
           
                The option affects onscreen displays only, so it affects interactive displays and raster images captured from interactive displays. It does not affect vector output produced by Plot, Print, CGM Export and similar functions.   
         
        """
        pass
    def RegenerateFromToleranceChange(update_mode_change: bool, studio: bool) -> None:
        """
         Regenerates after changing tolerance 
        """
        pass
    def UpdateLineFontObjects(do_software_update: bool) -> None:
        """
         Updates the UI after line font is changed 
        """
        pass
class Width(Enum):
    """
    Members Include: 
     |Original|  Original 
     |Thin|  Thin 
     |Normal|  Normal 
     |Thick|  Thick 
     |One|  Width One 
     |Two|  Width Two 
     |Three|  Width Three 
     |Four|  Width Four 
     |Five|  Width Five 
     |Six|  Width Six 
     |Seven|  Width Seven 
     |Eight|  Width Eight 
     |Nine|  Width Nine 

    """
    Original: int
    Thin: int
    Normal: int
    Thick: int
    One: int
    Two: int
    Three: int
    Four: int
    Five: int
    Six: int
    Seven: int
    Eight: int
    Nine: int
    @staticmethod
    def ValueOf(value: int) -> Width:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class WorkPlane(NXOpen.NXObject): 
    """ Represents the set of WorkPlanePreferences preferences applicable to part. Sets parameters for the 
Graphics Window grid and the Work Plane Emphasis mode. """
    class Grid(Enum):
        """
        Members Include: 
         |Polar|  Polar Grid 
         |Rectangular|  Rectangular Grid 

        """
        Polar: int
        Rectangular: int
        @staticmethod
        def ValueOf(value: int) -> WorkPlane.Grid:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class GridSize:
        """
         Grid size parameters 
         WorkPlaneGridSize_Struct NXOpen.P is an alias for  WorkPlane.GridSize NXOpen.P.
        """
        @property
        def MajorGridSpacing(self) -> float:
            """
            Getter for property MajorGridSpacing
            Distance between major grid lines

            """
            pass
        @MajorGridSpacing.setter
        def MajorGridSpacing(self, value: float):
            """
            Getter for property MajorGridSpacing
            Distance between major grid lines
            Setter for property MajorGridSpacing
            Distance between major grid lines

            """
            pass
        @property
        def MinorLinesPerMajor(self) -> int:
            """
            Getter for property MinorLinesPerMajor
            Number of minor lines between major grid lines

            """
            pass
        @MinorLinesPerMajor.setter
        def MinorLinesPerMajor(self, value: int):
            """
            Getter for property MinorLinesPerMajor
            Number of minor lines between major grid lines
            Setter for property MinorLinesPerMajor
            Number of minor lines between major grid lines

            """
            pass
        @property
        def SnapPointsPerMinor(self) -> int:
            """
            Getter for property SnapPointsPerMinor
            Number of snap points between minor grid lines

            """
            pass
        @SnapPointsPerMinor.setter
        def SnapPointsPerMinor(self, value: int):
            """
            Getter for property SnapPointsPerMinor
            Number of snap points between minor grid lines
            Setter for property SnapPointsPerMinor
            Number of snap points between minor grid lines

            """
            pass
    class NonuniformGridSize:
        """
         Nonuniform grid size parameters 
         WorkPlaneNonuniformGridSize_Struct NXOpen.P is an alias for  WorkPlane.NonuniformGridSize NXOpen.P.
        """
        @property
        def XcGridSize(self) -> WorkPlane.GridSize:
            """
            Getter for property XcGridSize
            XC axis grid parameters

            """
            pass
        @XcGridSize.setter
        def XcGridSize(self, value: WorkPlane.GridSize):
            """
            Getter for property XcGridSize
            XC axis grid parameters
            Setter for property XcGridSize
            XC axis grid parameters

            """
            pass
        @property
        def YcGridSize(self) -> WorkPlane.GridSize:
            """
            Getter for property YcGridSize
            YC axis grid parameters

            """
            pass
        @YcGridSize.setter
        def YcGridSize(self, value: WorkPlane.GridSize):
            """
            Getter for property YcGridSize
            YC axis grid parameters
            Setter for property YcGridSize
            YC axis grid parameters

            """
            pass
    class PolarGridSize:
        """
         Polar grid size parameters 
         WorkPlanePolarGridSize_Struct NXOpen.P is an alias for  WorkPlane.PolarGridSize NXOpen.P.
        """
        @property
        def RadialGridSize(self) -> WorkPlane.GridSize:
            """
            Getter for property RadialGridSize
            Radial grid circle parameters

            """
            pass
        @RadialGridSize.setter
        def RadialGridSize(self, value: WorkPlane.GridSize):
            """
            Getter for property RadialGridSize
            Radial grid circle parameters
            Setter for property RadialGridSize
            Radial grid circle parameters

            """
            pass
        @property
        def AngularGridSize(self) -> WorkPlane.GridSize:
            """
            Getter for property AngularGridSize
            Angular grid line parameters

            """
            pass
        @AngularGridSize.setter
        def AngularGridSize(self, value: WorkPlane.GridSize):
            """
            Getter for property AngularGridSize
            Angular grid line parameters
            Setter for property AngularGridSize
            Angular grid line parameters

            """
            pass
    @property
    def GridColor(self) -> int:
        """
        Getter for property: (int) GridColor
         Returns the grid color.  
           Specifies the color of grid.    
         
        """
        pass
    @GridColor.setter
    def GridColor(self, grid_color: int):
        """
        Setter for property: (int) GridColor
         Returns the grid color.  
           Specifies the color of grid.    
         
        """
        pass
    @property
    def GridIsNonUniform(self) -> bool:
        """
        Getter for property: (bool) GridIsNonUniform
         Returns the grid non uniform flag.  
           If true grid is non uniform. A uniform grid has the same spacing in X and Y. 
            A non-uniform grid allows for different spacing in X and Y.   
         
        """
        pass
    @GridIsNonUniform.setter
    def GridIsNonUniform(self, grid_is_non_uniform: bool):
        """
        Setter for property: (bool) GridIsNonUniform
         Returns the grid non uniform flag.  
           If true grid is non uniform. A uniform grid has the same spacing in X and Y. 
            A non-uniform grid allows for different spacing in X and Y.   
         
        """
        pass
    @property
    def GridOnTop(self) -> bool:
        """
        Getter for property: (bool) GridOnTop
         Returns the grid on top flag.  
           If true displays the grid on top of other graphics in the scene.    
         
        """
        pass
    @GridOnTop.setter
    def GridOnTop(self, grid_on_top: bool):
        """
        Setter for property: (bool) GridOnTop
         Returns the grid on top flag.  
           If true displays the grid on top of other graphics in the scene.    
         
        """
        pass
    @property
    def GridType(self) -> WorkPlane.Grid:
        """
        Getter for property: ( WorkPlane.Grid NXOpen.P) GridType
         Returns the grid type.  
           It may be polar or rectangular    
         
        """
        pass
    @GridType.setter
    def GridType(self, grid_type: WorkPlane.Grid):
        """
        Setter for property: ( WorkPlane.Grid NXOpen.P) GridType
         Returns the grid type.  
           It may be polar or rectangular    
         
        """
        pass
    @property
    def PolarShowMajorLines(self) -> bool:
        """
        Getter for property: (bool) PolarShowMajorLines
         Returns the show major lines flag for polar grid     
            
         
        """
        pass
    @PolarShowMajorLines.setter
    def PolarShowMajorLines(self, polar_show_major_lines: bool):
        """
        Setter for property: (bool) PolarShowMajorLines
         Returns the show major lines flag for polar grid     
            
         
        """
        pass
    @property
    def RectangularShowMajorLines(self) -> bool:
        """
        Getter for property: (bool) RectangularShowMajorLines
         Returns the show major lines flag for rectangular grid     
            
         
        """
        pass
    @RectangularShowMajorLines.setter
    def RectangularShowMajorLines(self, rectangular_show_major_lines: bool):
        """
        Setter for property: (bool) RectangularShowMajorLines
         Returns the show major lines flag for rectangular grid     
            
         
        """
        pass
    @property
    def ShowGrid(self) -> bool:
        """
        Getter for property: (bool) ShowGrid
         Returns the show and hide grid flag.  
           If true displays the grid pattern in the graphics window else hides    
         
        """
        pass
    @ShowGrid.setter
    def ShowGrid(self, show_grid: bool):
        """
        Setter for property: (bool) ShowGrid
         Returns the show and hide grid flag.  
           If true displays the grid pattern in the graphics window else hides    
         
        """
        pass
    @property
    def ShowLabels(self) -> bool:
        """
        Getter for property: (bool) ShowLabels
         Returns the show and hide grid labels flag.  
           If true displays the grid labels in the graphics window else hides    
         
        """
        pass
    @ShowLabels.setter
    def ShowLabels(self, show_labels: bool):
        """
        Setter for property: (bool) ShowLabels
         Returns the show and hide grid labels flag.  
           If true displays the grid labels in the graphics window else hides    
         
        """
        pass
    @property
    def SnapToGrid(self) -> bool:
        """
        Getter for property: (bool) SnapToGrid
         Returns the snap to grid flag.  
           If true enables snapping (moves an indicated screen position point to the nearest 
            grid point). Points snap to the grid even when Show Grid is off.   
         
        """
        pass
    @SnapToGrid.setter
    def SnapToGrid(self, snap_to_grid: bool):
        """
        Setter for property: (bool) SnapToGrid
         Returns the snap to grid flag.  
           If true enables snapping (moves an indicated screen position point to the nearest 
            grid point). Points snap to the grid even when Show Grid is off.   
         
        """
        pass
    def GetPolarGridSize(self) -> WorkPlane.PolarGridSize:
        """
         Query the polar grid size parameters. 
         Returns polar_grid_size ( WorkPlane.PolarGridSize NXOpen.P):  .
        """
        pass
    def GetRectangularNonuniformGridSize(self) -> WorkPlane.NonuniformGridSize:
        """
         Query the rectangular nonuniform grid size parameters.  
         Returns nonuniform_grid_size ( WorkPlane.NonuniformGridSize NXOpen.P):  .
        """
        pass
    def GetRectangularUniformGridSize(self) -> WorkPlane.GridSize:
        """
         Query the rectangular uniform grid size parameters.  
         Returns grid_size ( WorkPlane.GridSize NXOpen.P):  .
        """
        pass
    def SetPolarGridSize(self, polar_grid_size: WorkPlane.PolarGridSize) -> None:
        """
          Set the polar grid size parameters. 
        """
        pass
    def SetRectangularNonuniformGridSize(self, nonuniform_grid_size: WorkPlane.NonuniformGridSize) -> None:
        """
          Set the rectangular nonuniform grid size parameters. 
        """
        pass
    def SetRectangularUniformGridSize(self, grid_size: WorkPlane.GridSize) -> None:
        """
          Set the rectangular uniform grid size parameters. 
        """
        pass
