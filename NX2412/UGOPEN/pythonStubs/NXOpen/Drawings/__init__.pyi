from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class AddObjectsToRegionBuilder(NXOpen.Builder): 
    """ Creates the builder for associating the symbols from library to the region   """
    @property
    def SelectedRegion(self) -> SelectDrawingRegion:
        """
        Getter for property: ( SelectDrawingRegion NXOpen.) SelectedRegion
         Returns the get selected region   
            
         
        """
        pass
    def SetMasterSymbolFilePaths(self, symbolPath: List[str]) -> None:
        """
         Set the master symbol paths
        """
        pass
import NXOpen
class AddRemoveBoxViewBuilder(NXOpen.Builder): 
    """ This class is used to construct the add remove box view Builder """
    class ModeType(Enum):
        """
        Members Include: 
         |Add|  Add mode 
         |Remove|  Remove mode 

        """
        Add: int
        Remove: int
        @staticmethod
        def ValueOf(value: int) -> AddRemoveBoxViewBuilder.ModeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Mode(self) -> AddRemoveBoxViewBuilder.ModeType:
        """
        Getter for property: ( AddRemoveBoxViewBuilder.ModeType NXOpen.) Mode
         Returns the mode type   
            
         
        """
        pass
    @Mode.setter
    def Mode(self, mode: AddRemoveBoxViewBuilder.ModeType):
        """
        Setter for property: ( AddRemoveBoxViewBuilder.ModeType NXOpen.) Mode
         Returns the mode type   
            
         
        """
        pass
    @property
    def SelectedView(self) -> NXOpen.ModelingView:
        """
        Getter for property: ( NXOpen.ModelingView) SelectedView
         Returns the selected view   
            
         
        """
        pass
    @SelectedView.setter
    def SelectedView(self, selectedView: NXOpen.ModelingView):
        """
        Setter for property: ( NXOpen.ModelingView) SelectedView
         Returns the selected view   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class AnnotationSettingsBuilder(NXOpen.TaggedObject): 
    """
    Represents a Drawings.AnnotationSettingsBuilder.
    This class queries and sets settings specific to drawings data which will get converted to PMIs.
    """
    class AnnotationTypeEnum(Enum):
        """
        Members Include: 
         |Dimension| 
         |Note| 
         |FeatureControlFrame| 
         |DatumFeatureSymbol| 
         |DatumTarget| 
         |Balloon| 
         |SurfaceFinishSymbol| 
         |WeldSymbol| 
         |CustomSymbol| 
         |CenterLine| 
         |UserDefinedSymbol| 
         |EdgeConditionSymbol| 
         |MaxAnnotationYypes| 

        """
        Dimension: int
        Note: int
        FeatureControlFrame: int
        DatumFeatureSymbol: int
        DatumTarget: int
        Balloon: int
        SurfaceFinishSymbol: int
        WeldSymbol: int
        CustomSymbol: int
        CenterLine: int
        UserDefinedSymbol: int
        EdgeConditionSymbol: int
        MaxAnnotationYypes: int
        @staticmethod
        def ValueOf(value: int) -> AnnotationSettingsBuilder.AnnotationTypeEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class UnitsEnum(Enum):
        """
        Members Include: 
         |UseTargetPartUnits| 
         |UseDrawingUnits| 

        """
        UseTargetPartUnits: int
        UseDrawingUnits: int
        @staticmethod
        def ValueOf(value: int) -> AnnotationSettingsBuilder.UnitsEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ConvertToOriginalModelView(self) -> bool:
        """
        Getter for property: (bool) ConvertToOriginalModelView
         Returns the convert to original model view    
            
         
        """
        pass
    @ConvertToOriginalModelView.setter
    def ConvertToOriginalModelView(self, convertToOriginalModelView: bool):
        """
        Setter for property: (bool) ConvertToOriginalModelView
         Returns the convert to original model view    
            
         
        """
        pass
    @property
    def LinearDimensionTolerance(self) -> float:
        """
        Getter for property: (float) LinearDimensionTolerance
         Returns the linear dimension tolerance   
            
         
        """
        pass
    @LinearDimensionTolerance.setter
    def LinearDimensionTolerance(self, linearDimensionTolerance: float):
        """
        Setter for property: (float) LinearDimensionTolerance
         Returns the linear dimension tolerance   
            
         
        """
        pass
    @property
    def PreserveDraftingLayer(self) -> bool:
        """
        Getter for property: (bool) PreserveDraftingLayer
         Returns the preserve drafting layer    
            
         
        """
        pass
    @PreserveDraftingLayer.setter
    def PreserveDraftingLayer(self, preserveDraftingLayer: bool):
        """
        Setter for property: (bool) PreserveDraftingLayer
         Returns the preserve drafting layer    
            
         
        """
        pass
    @property
    def PreserveHiddenStatus(self) -> bool:
        """
        Getter for property: (bool) PreserveHiddenStatus
         Returns the preserve hidden status   
            
         
        """
        pass
    @PreserveHiddenStatus.setter
    def PreserveHiddenStatus(self, preserveHiddenStatus: bool):
        """
        Setter for property: (bool) PreserveHiddenStatus
         Returns the preserve hidden status   
            
         
        """
        pass
    @property
    def ProcessObjectsHidden(self) -> bool:
        """
        Getter for property: (bool) ProcessObjectsHidden
         Returns the process objects hidden    
            
         
        """
        pass
    @ProcessObjectsHidden.setter
    def ProcessObjectsHidden(self, processObjectsHidden: bool):
        """
        Setter for property: (bool) ProcessObjectsHidden
         Returns the process objects hidden    
            
         
        """
        pass
    @property
    def Units(self) -> AnnotationSettingsBuilder.UnitsEnum:
        """
        Getter for property: ( AnnotationSettingsBuilder.UnitsEnum NXOpen.) Units
         Returns the units   
            
         
        """
        pass
    @Units.setter
    def Units(self, units: AnnotationSettingsBuilder.UnitsEnum):
        """
        Setter for property: ( AnnotationSettingsBuilder.UnitsEnum NXOpen.) Units
         Returns the units   
            
         
        """
        pass
    def SaveAnnotationType(self, annType: AnnotationSettingsBuilder.AnnotationTypeEnum, annValue: bool) -> None:
        """
         API used to save settings data 
        """
        pass
class ArrowDirectionType(Enum):
    """
    Members Include: 
     |OutofSheet|  Out of Sheet 
     |IntoSheet| 

    """
    OutofSheet: int
    IntoSheet: int
    @staticmethod
    def ValueOf(value: int) -> ArrowDirectionType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class ArrowStyleType(Enum):
    """
    Members Include: 
     |Filled|  Filled 
     |Closed|  Closed 
     |ClosedSolid|  Close Solid 
     |Open| 

    """
    Filled: int
    Closed: int
    ClosedSolid: int
    Open: int
    @staticmethod
    def ValueOf(value: int) -> ArrowStyleType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class AssociativeAngleBuilder(NXOpen.TaggedObject): 
    """ This builder allows the user to create an associative or non-associative angle by measuring
        between a combination of two objects or vectors evaluated on a specified plane, or by an expression """
    class EvaluationPlaneType(Enum):
        """
        Members Include: 
         |DrawingSheet| 
         |TrueAngle| 
         |SpecifyPlane| 

        """
        DrawingSheet: int
        TrueAngle: int
        SpecifyPlane: int
        @staticmethod
        def ValueOf(value: int) -> AssociativeAngleBuilder.EvaluationPlaneType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ObjectType(Enum):
        """
        Members Include: 
         |Object|  indicates the selected type is an object 
         |Vector|  indicates the selected type is a vector 

        """
        Object: int
        Vector: int
        @staticmethod
        def ValueOf(value: int) -> AssociativeAngleBuilder.ObjectType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Angle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Angle
         Returns the angle   
            
         
        """
        pass
    @property
    def AngleValue(self) -> float:
        """
        Getter for property: (float) AngleValue
         Returns the angle value   
            
         
        """
        pass
    @AngleValue.setter
    def AngleValue(self, angleValue: float):
        """
        Setter for property: (float) AngleValue
         Returns the angle value   
            
         
        """
        pass
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns the associative flag   
            
         
        """
        pass
    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
         Returns the associative flag   
            
         
        """
        pass
    @property
    def EvaluationPlane(self) -> AssociativeAngleBuilder.EvaluationPlaneType:
        """
        Getter for property: ( AssociativeAngleBuilder.EvaluationPlaneType NXOpen.) EvaluationPlane
         Returns the evaluation plane type   
            
         
        """
        pass
    @EvaluationPlane.setter
    def EvaluationPlane(self, evaluationPlane: AssociativeAngleBuilder.EvaluationPlaneType):
        """
        Setter for property: ( AssociativeAngleBuilder.EvaluationPlaneType NXOpen.) EvaluationPlane
         Returns the evaluation plane type   
            
         
        """
        pass
    @property
    def FirstMapView(self) -> NXOpen.View:
        """
        Getter for property: ( NXOpen.View) FirstMapView
         Returns the first map view   
            
         
        """
        pass
    @FirstMapView.setter
    def FirstMapView(self, firstMapView: NXOpen.View):
        """
        Setter for property: ( NXOpen.View) FirstMapView
         Returns the first map view   
            
         
        """
        pass
    @property
    def FirstObject(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) FirstObject
         Returns the first object   
            
         
        """
        pass
    @property
    def FirstObjectType(self) -> AssociativeAngleBuilder.ObjectType:
        """
        Getter for property: ( AssociativeAngleBuilder.ObjectType NXOpen.) FirstObjectType
         Returns the first object type   
            
         
        """
        pass
    @FirstObjectType.setter
    def FirstObjectType(self, objtype: AssociativeAngleBuilder.ObjectType):
        """
        Setter for property: ( AssociativeAngleBuilder.ObjectType NXOpen.) FirstObjectType
         Returns the first object type   
            
         
        """
        pass
    @property
    def FirstVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) FirstVector
         Returns the first vector   
            
         
        """
        pass
    @FirstVector.setter
    def FirstVector(self, firstVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) FirstVector
         Returns the first vector   
            
         
        """
        pass
    @property
    def Plane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) Plane
         Returns the plane   
            
         
        """
        pass
    @Plane.setter
    def Plane(self, plane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) Plane
         Returns the plane   
            
         
        """
        pass
    @property
    def ScalarObject(self) -> NXOpen.Scalar:
        """
        Getter for property: ( NXOpen.Scalar) ScalarObject
         Returns the scalar object   
            
         
        """
        pass
    @ScalarObject.setter
    def ScalarObject(self, scalarObject: NXOpen.Scalar):
        """
        Setter for property: ( NXOpen.Scalar) ScalarObject
         Returns the scalar object   
            
         
        """
        pass
    @property
    def SecondMapView(self) -> NXOpen.View:
        """
        Getter for property: ( NXOpen.View) SecondMapView
         Returns the second map view   
            
         
        """
        pass
    @SecondMapView.setter
    def SecondMapView(self, secondMapView: NXOpen.View):
        """
        Setter for property: ( NXOpen.View) SecondMapView
         Returns the second map view   
            
         
        """
        pass
    @property
    def SecondObject(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) SecondObject
         Returns the second object   
            
         
        """
        pass
    @property
    def SecondObjectType(self) -> AssociativeAngleBuilder.ObjectType:
        """
        Getter for property: ( AssociativeAngleBuilder.ObjectType NXOpen.) SecondObjectType
         Returns the second object type   
            
         
        """
        pass
    @SecondObjectType.setter
    def SecondObjectType(self, objtype: AssociativeAngleBuilder.ObjectType):
        """
        Setter for property: ( AssociativeAngleBuilder.ObjectType NXOpen.) SecondObjectType
         Returns the second object type   
            
         
        """
        pass
    @property
    def SecondVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) SecondVector
         Returns the second vector   
            
         
        """
        pass
    @SecondVector.setter
    def SecondVector(self, secondVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) SecondVector
         Returns the second vector   
            
         
        """
        pass
    def AlternateAngle(self) -> None:
        """
         The alternate angle 
        """
        pass
    def CreateScalarObject(self) -> None:
        """
         Creates a scalar object for an associative angle 
        """
        pass
    def CreateScalarObjectFromData(self, scalarTag: NXOpen.Scalar, angleValue: float) -> None:
        """
          Creates scalar object for an associative angle using data from existing scalar object or angle value. 
        """
        pass
    def SetIsMeasure(self, isMeasure: bool) -> None:
        """
         Sets IsMeasure flag indicating angle is result of a measure 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class AutomationBookletBuilder(NXOpen.TaggedObject): 
    """ 
     Represents a NXOpen.Drawings.AutomationBookletBuilder
    """
    @property
    def HiddenLineColorFontWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) HiddenLineColorFontWidth
         Returns the hidden line color font width   
            
         
        """
        pass
    @property
    def VisibleLineColorFontWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) VisibleLineColorFontWidth
         Returns the visible line color font width   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class AutomationTemplateRegionBuilder(NXOpen.TaggedObject): 
    """ 
     Represents a NXOpen.Drawings.AutomationTemplateRegionBuilder
    """
    @property
    def DisplayRegionLabel(self) -> bool:
        """
        Getter for property: (bool) DisplayRegionLabel
         Returns the flag to indicate if the display region label should be displayed   
            
         
        """
        pass
    @DisplayRegionLabel.setter
    def DisplayRegionLabel(self, displayRegionLabel: bool):
        """
        Setter for property: (bool) DisplayRegionLabel
         Returns the flag to indicate if the display region label should be displayed   
            
         
        """
        pass
    @property
    def DisplayTemplatePart(self) -> bool:
        """
        Getter for property: (bool) DisplayTemplatePart
         Returns the value that determines whether or not regions should be displayed in a non-template part.  
            
         
        """
        pass
    @DisplayTemplatePart.setter
    def DisplayTemplatePart(self, displayTemplatePart: bool):
        """
        Setter for property: (bool) DisplayTemplatePart
         Returns the value that determines whether or not regions should be displayed in a non-template part.  
            
         
        """
        pass
    @property
    def LineColorFontWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) LineColorFontWidth
         Returns the value that specifies the color font width of region objectsline   
            
         
        """
        pass
class BaseHalfSectionLine(SectionLine): 
    """ Represents a Base Half Section Line."""
    pass
class BasePointToPointSectionLine(SectionLine): 
    """ Represents a Base Point to Point Section Line."""
    pass
class BaseSteppedSectionLine(SectionLine): 
    """ Represents a Base Stepped Section Line."""
    pass
import NXOpen
class BaseViewBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Drawings.BaseView builder """
    @property
    def HiddenObjects(self) -> HiddenObjectsBuilder:
        """
        Getter for property: ( HiddenObjectsBuilder NXOpen.) HiddenObjects
         Returns the list of objects to not show in the view   
            
         
        """
        pass
    @property
    def NonSectionedObjects(self) -> HiddenObjectsBuilder:
        """
        Getter for property: ( HiddenObjectsBuilder NXOpen.) NonSectionedObjects
         Returns the list of objects to not section in the view   
            
         
        """
        pass
    @property
    def Placement(self) -> ViewPlacementBuilder:
        """
        Getter for property: ( ViewPlacementBuilder NXOpen.) Placement
         Returns the view placement   
            
         
        """
        pass
    @property
    def Scale(self) -> ViewScaleBuilder:
        """
        Getter for property: ( ViewScaleBuilder NXOpen.) Scale
         Returns the view scale   
            
         
        """
        pass
    @property
    def SecondaryComponents(self) -> DraftingComponentSelectionBuilder:
        """
        Getter for property: ( DraftingComponentSelectionBuilder NXOpen.) SecondaryComponents
         Returns the list of secondary objects in the view   
            
         
        """
        pass
    @property
    def SelectModelView(self) -> SelectModelViewBuilder:
        """
        Getter for property: ( SelectModelViewBuilder NXOpen.) SelectModelView
         Returns the model view   
            
         
        """
        pass
    @property
    def Style(self) -> ViewStyleBuilder:
        """
        Getter for property: ( ViewStyleBuilder NXOpen.) Style
         Returns the view style   
            
         
        """
        pass
import NXOpen
import NXOpen.Preferences
class BaseViewStyle(NXOpen.Object): 
    """ Represents set of Base View Style Preferences applicable to drafting views. 
     """
    def LoadModelFromPart(self, load_part_name: str, load_part_toggle: bool) -> None:
        """
         To load the assemblies arrangement part file. If the logical argument is True, 
                    the part would be loaded.
                 
        """
        pass
    def SetAssemblyArrangement(self, config: str) -> None:
        """
         Sets the configuration for the arrangement in assembly after an 
                    arrangement part file is loaded.
                 
        """
        pass
    def SetFacetedRepresentation(self, is_faceted_representation: bool) -> None:
        """
         The status of faceted representation, if True the clipping bounds are inherited, else 
                    the imported model view is placed on the drawing with an Automatic Rectangular Boundary.
                 
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
class BaseView(DraftingView): 
    """ Represents a Base View. 
        A base view is a modeling view that you import onto a drawing.
        The base view can be a standalone view or a parent view
        for other drawings types such as a section view. """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class BorderAndZoneStyleBuilder(NXOpen.TaggedObject): 
    """ Represents the Border and Zone Style Builder which manages all the style attributes related
       to sheet borders, sheet margins and sheet zones.
    """
    @property
    def BorderAndZoneStandard(self) -> int:
        """
        Getter for property: (int) BorderAndZoneStandard
         Returns the borders and zones standard   
            
         
        """
        pass
    @BorderAndZoneStandard.setter
    def BorderAndZoneStandard(self, borderAndZoneStandard: int):
        """
        Setter for property: (int) BorderAndZoneStandard
         Returns the borders and zones standard   
            
         
        """
        pass
    @property
    def SheetBorderSettingsStyle(self) -> SheetBorderSettingsBuilder:
        """
        Getter for property: ( SheetBorderSettingsBuilder NXOpen.) SheetBorderSettingsStyle
         Returns the drawing sheet border settings builder   
            
         
        """
        pass
    @property
    def SheetMarginSettingsStyle(self) -> SheetMarginSettingsBuilder:
        """
        Getter for property: ( SheetMarginSettingsBuilder NXOpen.) SheetMarginSettingsStyle
         Returns the drawing sheet margin settings builder   
            
         
        """
        pass
    @property
    def SheetZoneSettingsStyle(self) -> SheetZoneSettingsBuilder:
        """
        Getter for property: ( SheetZoneSettingsBuilder NXOpen.) SheetZoneSettingsStyle
         Returns the drawing sheet zone settings builder   
            
         
        """
        pass
    def InheritSettingsFromCustomerDefault(self) -> None:
        """
         Inherit settings from customer default 
        """
        pass
    def InheritSettingsFromPreferences(self) -> None:
        """
         Inherit settings from preference 
        """
        pass
import NXOpen
class BordersAndZonesBuilder(NXOpen.Builder): 
    """ Builder for creating Borders and Zones. It creates and redefines borders and zones. """
    class FontEnum(Enum):
        """
        Members Include: 
         |Blockfont| 

        """
        Blockfont: int
        @staticmethod
        def ValueOf(value: int) -> BordersAndZonesBuilder.FontEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class HorizontalCenteringMarkType(Enum):
        """
        Members Include: 
         |NotSet|  None 
         |LeftArrow|  Left Arrow 
         |RightArrow|   Right Arrow 
         |LeftandRightArrow|  Left and Right Arrow 
         |LeftandRightLine| 

        """
        NotSet: int
        LeftArrow: int
        RightArrow: int
        LeftandRightArrow: int
        LeftandRightLine: int
        @staticmethod
        def ValueOf(value: int) -> BordersAndZonesBuilder.HorizontalCenteringMarkType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class VerticalCenteringMarkType(Enum):
        """
        Members Include: 
         |NotSet|  None 
         |BottomArrow|  Bottom Arrow 
         |TopArrow|  Top Arrow 
         |BottomandTopArrow|  Bottom and Top Arrow 
         |BottomandTopLine| 

        """
        NotSet: int
        BottomArrow: int
        TopArrow: int
        BottomandTopArrow: int
        BottomandTopLine: int
        @staticmethod
        def ValueOf(value: int) -> BordersAndZonesBuilder.VerticalCenteringMarkType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ZoneMethod(Enum):
        """
        Members Include: 
         |NotSet|  None 
         |Standard|  Standard 
         |Custom| 

        """
        NotSet: int
        Standard: int
        Custom: int
        @staticmethod
        def ValueOf(value: int) -> BordersAndZonesBuilder.ZoneMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ZoneOrigin(Enum):
        """
        Members Include: 
         |BottomRight|  Bottom Right 
         |TopLeft|  Top Left 
         |TopRight|  Top Right 
         |BottomLeft| 

        """
        BottomRight: int
        TopLeft: int
        TopRight: int
        BottomLeft: int
        @staticmethod
        def ValueOf(value: int) -> BordersAndZonesBuilder.ZoneOrigin:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BorderAndZoneStyle(self) -> BorderAndZoneStyleBuilder:
        """
        Getter for property: ( BorderAndZoneStyleBuilder NXOpen.) BorderAndZoneStyle
         Returns the border and zone style builder   
            
         
        """
        pass
    @property
    def BottomMargin(self) -> float:
        """
        Getter for property: (float) BottomMargin
         Returns the bottom margin   
            
         
        """
        pass
    @BottomMargin.setter
    def BottomMargin(self, bottomMargin: float):
        """
        Setter for property: (float) BottomMargin
         Returns the bottom margin   
            
         
        """
        pass
    @property
    def CenteringMarkExtension(self) -> float:
        """
        Getter for property: (float) CenteringMarkExtension
         Returns the centering mark extension   
            
         
        """
        pass
    @CenteringMarkExtension.setter
    def CenteringMarkExtension(self, centeringMarkExtension: float):
        """
        Setter for property: (float) CenteringMarkExtension
         Returns the centering mark extension   
            
         
        """
        pass
    @property
    def CreateBorders(self) -> bool:
        """
        Getter for property: (bool) CreateBorders
         Returns the create borders   
            
         
        """
        pass
    @CreateBorders.setter
    def CreateBorders(self, createBorders: bool):
        """
        Setter for property: (bool) CreateBorders
         Returns the create borders   
            
         
        """
        pass
    @property
    def CreateTrimmingMarks(self) -> bool:
        """
        Getter for property: (bool) CreateTrimmingMarks
         Returns the create trimming marks   
            
         
        """
        pass
    @CreateTrimmingMarks.setter
    def CreateTrimmingMarks(self, createTrimmingMarks: bool):
        """
        Setter for property: (bool) CreateTrimmingMarks
         Returns the create trimming marks   
            
         
        """
        pass
    @property
    def CreateZoneLabels(self) -> bool:
        """
        Getter for property: (bool) CreateZoneLabels
         Returns the create zone labels   
            
         
        """
        pass
    @CreateZoneLabels.setter
    def CreateZoneLabels(self, createZoneLabels: bool):
        """
        Setter for property: (bool) CreateZoneLabels
         Returns the create zone labels   
            
         
        """
        pass
    @property
    def CreateZoneMarking(self) -> bool:
        """
        Getter for property: (bool) CreateZoneMarking
         Returns the create zone marking   
            
         
        """
        pass
    @CreateZoneMarking.setter
    def CreateZoneMarking(self, createZoneMarking: bool):
        """
        Setter for property: (bool) CreateZoneMarking
         Returns the create zone marking   
            
         
        """
        pass
    @property
    def HorizontalCenteringMark(self) -> BordersAndZonesBuilder.HorizontalCenteringMarkType:
        """
        Getter for property: ( BordersAndZonesBuilder.HorizontalCenteringMarkType NXOpen.) HorizontalCenteringMark
         Returns the horizontal centering mark   
            
         
        """
        pass
    @HorizontalCenteringMark.setter
    def HorizontalCenteringMark(self, horizontalCenteringMark: BordersAndZonesBuilder.HorizontalCenteringMarkType):
        """
        Setter for property: ( BordersAndZonesBuilder.HorizontalCenteringMarkType NXOpen.) HorizontalCenteringMark
         Returns the horizontal centering mark   
            
         
        """
        pass
    @property
    def HorizontalSize(self) -> float:
        """
        Getter for property: (float) HorizontalSize
         Returns the horizontal size of the zones  
            
         
        """
        pass
    @HorizontalSize.setter
    def HorizontalSize(self, horizontalSize: float):
        """
        Setter for property: (float) HorizontalSize
         Returns the horizontal size of the zones  
            
         
        """
        pass
    @property
    def LabelFont(self) -> int:
        """
        Getter for property: (int) LabelFont
         Returns the label font   
            
         
        """
        pass
    @LabelFont.setter
    def LabelFont(self, labelFont: int):
        """
        Setter for property: (int) LabelFont
         Returns the label font   
            
         
        """
        pass
    @property
    def LabelHeight(self) -> float:
        """
        Getter for property: (float) LabelHeight
         Returns the label height   
            
         
        """
        pass
    @LabelHeight.setter
    def LabelHeight(self, labelHeight: float):
        """
        Setter for property: (float) LabelHeight
         Returns the label height   
            
         
        """
        pass
    @property
    def LeftMargin(self) -> float:
        """
        Getter for property: (float) LeftMargin
         Returns the left margin   
            
         
        """
        pass
    @LeftMargin.setter
    def LeftMargin(self, leftMargin: float):
        """
        Setter for property: (float) LeftMargin
         Returns the left margin   
            
         
        """
        pass
    @property
    def MarkingHeight(self) -> float:
        """
        Getter for property: (float) MarkingHeight
         Returns the marking height   
            
         
        """
        pass
    @MarkingHeight.setter
    def MarkingHeight(self, markingHeight: float):
        """
        Setter for property: (float) MarkingHeight
         Returns the marking height   
            
         
        """
        pass
    @property
    def Method(self) -> BordersAndZonesBuilder.ZoneMethod:
        """
        Getter for property: ( BordersAndZonesBuilder.ZoneMethod NXOpen.) Method
         Returns the method of creation of zones  
            
         
        """
        pass
    @Method.setter
    def Method(self, method: BordersAndZonesBuilder.ZoneMethod):
        """
        Setter for property: ( BordersAndZonesBuilder.ZoneMethod NXOpen.) Method
         Returns the method of creation of zones  
            
         
        """
        pass
    @property
    def Origin(self) -> BordersAndZonesBuilder.ZoneOrigin:
        """
        Getter for property: ( BordersAndZonesBuilder.ZoneOrigin NXOpen.) Origin
         Returns the zone origin type  
            
         
        """
        pass
    @Origin.setter
    def Origin(self, origin: BordersAndZonesBuilder.ZoneOrigin):
        """
        Setter for property: ( BordersAndZonesBuilder.ZoneOrigin NXOpen.) Origin
         Returns the zone origin type  
            
         
        """
        pass
    @property
    def RightMargin(self) -> float:
        """
        Getter for property: (float) RightMargin
         Returns the right margin   
            
         
        """
        pass
    @RightMargin.setter
    def RightMargin(self, rightMargin: float):
        """
        Setter for property: (float) RightMargin
         Returns the right margin   
            
         
        """
        pass
    @property
    def TopMargin(self) -> float:
        """
        Getter for property: (float) TopMargin
         Returns the top margin   
            
         
        """
        pass
    @TopMargin.setter
    def TopMargin(self, topMargin: float):
        """
        Setter for property: (float) TopMargin
         Returns the top margin   
            
         
        """
        pass
    @property
    def TrimmingMarkLength(self) -> float:
        """
        Getter for property: (float) TrimmingMarkLength
         Returns the trimming mark length   
            
         
        """
        pass
    @TrimmingMarkLength.setter
    def TrimmingMarkLength(self, trimmingMarkLength: float):
        """
        Setter for property: (float) TrimmingMarkLength
         Returns the trimming mark length   
            
         
        """
        pass
    @property
    def TrimmingMarkThickness(self) -> float:
        """
        Getter for property: (float) TrimmingMarkThickness
         Returns the trimming mark thickness   
            
         
        """
        pass
    @TrimmingMarkThickness.setter
    def TrimmingMarkThickness(self, trimmingMarkThickness: float):
        """
        Setter for property: (float) TrimmingMarkThickness
         Returns the trimming mark thickness   
            
         
        """
        pass
    @property
    def VerticalCenteringMark(self) -> BordersAndZonesBuilder.VerticalCenteringMarkType:
        """
        Getter for property: ( BordersAndZonesBuilder.VerticalCenteringMarkType NXOpen.) VerticalCenteringMark
         Returns the vertical centering mark   
            
         
        """
        pass
    @VerticalCenteringMark.setter
    def VerticalCenteringMark(self, verticalCenteringMark: BordersAndZonesBuilder.VerticalCenteringMarkType):
        """
        Setter for property: ( BordersAndZonesBuilder.VerticalCenteringMarkType NXOpen.) VerticalCenteringMark
         Returns the vertical centering mark   
            
         
        """
        pass
    @property
    def VerticalSize(self) -> float:
        """
        Getter for property: (float) VerticalSize
         Returns the vertical size of the zones  
            
         
        """
        pass
    @VerticalSize.setter
    def VerticalSize(self, verticalSize: float):
        """
        Setter for property: (float) VerticalSize
         Returns the vertical size of the zones  
            
         
        """
        pass
    @property
    def Width(self) -> float:
        """
        Getter for property: (float) Width
         Returns the width of the border  
            
         
        """
        pass
    @Width.setter
    def Width(self, width: float):
        """
        Setter for property: (float) Width
         Returns the width of the border  
            
         
        """
        pass
import NXOpen
class BordersAndZonesCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Drawings.BordersAndZones objects """
    def CreateBordersAndZonesBuilder(self, bordersAndZones: BordersAndZones) -> BordersAndZonesBuilder:
        """
         Creates a borders and zones builder 
         Returns builder ( BordersAndZonesBuilder NXOpen.):  BordersAndZonesBuilder object .
        """
        pass
    def FindObject(self, name: str) -> BordersAndZones:
        """
          Finds the  NXOpen.Drawings.BordersAndZones  with the given name. 
                     An exception will be thrown if no object can be found with the given name. 
         Returns object ( BordersAndZones NXOpen.):   Borders and zones object .
        """
        pass
import NXOpen
class BordersAndZones(NXOpen.NXObject): 
    """ Represents Borders and Zones"""
    pass
import NXOpen
import NXOpen.Annotations
class BrokenViewBuilder(NXOpen.Builder): 
    """ This class is used to construct the broken view Builder """
    class BreakLineStyle(Enum):
        """
        Members Include: 
         |Simple|  Simple 
         |Straight|  Straight 
         |Sawtooth|  Sawtooth 
         |LongBreak|  LongBreak 
         |Tubular|  Tubular 
         |SolidTubular|  Solid Tubular 
         |SolidRod|  Solid Rod 
         |Jigsaw|  Jigsaw 
         |Wood|  Wood 
         |CopyCurve|  Copy of the existing curve 
         |TemplateCurve|  Template, based on the existing curve 

        """
        Simple: int
        Straight: int
        Sawtooth: int
        LongBreak: int
        Tubular: int
        SolidTubular: int
        SolidRod: int
        Jigsaw: int
        Wood: int
        CopyCurve: int
        TemplateCurve: int
        @staticmethod
        def ValueOf(value: int) -> BrokenViewBuilder.BreakLineStyle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class HorizontalBreakSide(Enum):
        """
        Members Include: 
         |LeftEnd|  Hide Left side 
         |RightEnd|  Hide Right side 

        """
        LeftEnd: int
        RightEnd: int
        @staticmethod
        def ValueOf(value: int) -> BrokenViewBuilder.HorizontalBreakSide:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LineWidth(Enum):
        """
        Members Include: 
         |Thin|  Thin 
         |Medium|  Medium 
         |Thick|  Thick 
         |WidthOne|  Width One 
         |WidthTwo|  Width Two 
         |WidthThree|  Width Three 
         |WidthFour|  Width Four 
         |WidthFive|  Width Five 
         |WidthSix|  Width Six 
         |WidthSeven|  Width Seven 
         |WidthEight|  Width Eight 
         |WidthNine|  Width Nine 

        """
        Thin: int
        Medium: int
        Thick: int
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
        def ValueOf(value: int) -> BrokenViewBuilder.LineWidth:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TypeBreak(Enum):
        """
        Members Include: 
         |Regular|  Regular Break 
         |SingleSided|  SingleSiled Break 

        """
        Regular: int
        SingleSided: int
        @staticmethod
        def ValueOf(value: int) -> BrokenViewBuilder.TypeBreak:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TypeDirection(Enum):
        """
        Members Include: 
         |Parallel|  Parallel 
         |Perpendicular|  Perpendicular 
         |Vector|  Specified by Vector 

        """
        Parallel: int
        Perpendicular: int
        Vector: int
        @staticmethod
        def ValueOf(value: int) -> BrokenViewBuilder.TypeDirection:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class VerticalBreakSide(Enum):
        """
        Members Include: 
         |TopEnd|  Hide Top side 
         |BottomEnd|  Hide Bottom side 

        """
        TopEnd: int
        BottomEnd: int
        @staticmethod
        def ValueOf(value: int) -> BrokenViewBuilder.VerticalBreakSide:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Amplitude(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Amplitude
         Returns the break line amplitude   
            
         
        """
        pass
    @property
    def BreakLine1Anchor(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) BreakLine1Anchor
         Returns the object specifying the position of the first break line   
            
         
        """
        pass
    @BreakLine1Anchor.setter
    def BreakLine1Anchor(self, anchor1: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) BreakLine1Anchor
         Returns the object specifying the position of the first break line   
            
         
        """
        pass
    @property
    def BreakLine1ModelAnchor(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) BreakLine1ModelAnchor
         Returns the object specifying the position of the first break line   
            
         
        """
        pass
    @BreakLine1ModelAnchor.setter
    def BreakLine1ModelAnchor(self, anchor1: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) BreakLine1ModelAnchor
         Returns the object specifying the position of the first break line   
            
         
        """
        pass
    @property
    def BreakLine1Offset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BreakLine1Offset
         Returns the offset from the object locating the first break line   
            
         
        """
        pass
    @property
    def BreakLine2Anchor(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) BreakLine2Anchor
         Returns the object specifying the position of the second break line.  
           For  Drawings::BrokenViewBuilder::TypeBreakRegular  only   
         
        """
        pass
    @BreakLine2Anchor.setter
    def BreakLine2Anchor(self, anchor2: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) BreakLine2Anchor
         Returns the object specifying the position of the second break line.  
           For  Drawings::BrokenViewBuilder::TypeBreakRegular  only   
         
        """
        pass
    @property
    def BreakLine2ModelAnchor(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) BreakLine2ModelAnchor
         Returns the object specifying the position of the second break line.  
           For  Drawings::BrokenViewBuilder::TypeBreakRegular  only   
         
        """
        pass
    @BreakLine2ModelAnchor.setter
    def BreakLine2ModelAnchor(self, anchor2: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) BreakLine2ModelAnchor
         Returns the object specifying the position of the second break line.  
           For  Drawings::BrokenViewBuilder::TypeBreakRegular  only   
         
        """
        pass
    @property
    def BreakLine2Offset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BreakLine2Offset
         Returns the offset from the object locating the second break line.  
           For  Drawings::BrokenViewBuilder::TypeBreakRegular  only   
         
        """
        pass
    @property
    def BreakLineType(self) -> BrokenViewBuilder.BreakLineStyle:
        """
        Getter for property: ( BrokenViewBuilder.BreakLineStyle NXOpen.) BreakLineType
         Returns the break line type   
            
         
        """
        pass
    @BreakLineType.setter
    def BreakLineType(self, lineType: BrokenViewBuilder.BreakLineStyle):
        """
        Setter for property: ( BrokenViewBuilder.BreakLineStyle NXOpen.) BreakLineType
         Returns the break line type   
            
         
        """
        pass
    @property
    def BreakType(self) -> BrokenViewBuilder.TypeBreak:
        """
        Getter for property: ( BrokenViewBuilder.TypeBreak NXOpen.) BreakType
         Returns the break type   
            
         
        """
        pass
    @BreakType.setter
    def BreakType(self, breakType: BrokenViewBuilder.TypeBreak):
        """
        Setter for property: ( BrokenViewBuilder.TypeBreak NXOpen.) BreakType
         Returns the break type   
            
         
        """
        pass
    @property
    def BreakVisibility(self) -> bool:
        """
        Getter for property: (bool) BreakVisibility
         Returns the view break visibilitity   
            
         
        """
        pass
    @BreakVisibility.setter
    def BreakVisibility(self, visibilitity: bool):
        """
        Setter for property: (bool) BreakVisibility
         Returns the view break visibilitity   
            
         
        """
        pass
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) Color
         Returns the break line color   
            
         
        """
        pass
    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) Color
         Returns the break line color   
            
         
        """
        pass
    @property
    def CrossHatch(self) -> NXOpen.Annotations.HatchFillSettingsBuilder:
        """
        Getter for property: ( NXOpen.Annotations.HatchFillSettingsBuilder) CrossHatch
         Returns the HatchFillSetting   
            
         
        """
        pass
    @property
    def DirectionType(self) -> BrokenViewBuilder.TypeDirection:
        """
        Getter for property: ( BrokenViewBuilder.TypeDirection NXOpen.) DirectionType
         Returns the direction type   
            
         
        """
        pass
    @DirectionType.setter
    def DirectionType(self, directionType: BrokenViewBuilder.TypeDirection):
        """
        Setter for property: ( BrokenViewBuilder.TypeDirection NXOpen.) DirectionType
         Returns the direction type   
            
         
        """
        pass
    @property
    def DirectionVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) DirectionVector
         Returns the direction vector.  
           For  Drawings::BrokenViewBuilder::TypeDirectionVector .   
         
        """
        pass
    @DirectionVector.setter
    def DirectionVector(self, directionVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) DirectionVector
         Returns the direction vector.  
           For  Drawings::BrokenViewBuilder::TypeDirectionVector .   
         
        """
        pass
    @property
    def ExistingCurve(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) ExistingCurve
         Returns the curve to use as existing curve   
            
         
        """
        pass
    @property
    def Extension1(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Extension1
         Returns the break line extension (topright) beyond geometry   
            
         
        """
        pass
    @property
    def Extension2(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Extension2
         Returns the break line extension (bottomleft) beyond geometry   
            
         
        """
        pass
    @property
    def Gap(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Gap
         Returns the gap on the sheet between the two break lines   
            
         
        """
        pass
    @property
    def IsBreakLine1Associative(self) -> bool:
        """
        Getter for property: (bool) IsBreakLine1Associative
         Returns the associative positionning of the first break line   
            
         
        """
        pass
    @IsBreakLine1Associative.setter
    def IsBreakLine1Associative(self, isBreakLine1Associative: bool):
        """
        Setter for property: (bool) IsBreakLine1Associative
         Returns the associative positionning of the first break line   
            
         
        """
        pass
    @property
    def IsBreakLine2Associative(self) -> bool:
        """
        Getter for property: (bool) IsBreakLine2Associative
         Returns the associative positionning of the second break line.  
           For  
                 Drawings::BrokenViewBuilder::TypeBreakRegular  only   
         
        """
        pass
    @IsBreakLine2Associative.setter
    def IsBreakLine2Associative(self, isBreakLine2Associative: bool):
        """
        Setter for property: (bool) IsBreakLine2Associative
         Returns the associative positionning of the second break line.  
           For  
                 Drawings::BrokenViewBuilder::TypeBreakRegular  only   
         
        """
        pass
    @property
    def MasterView(self) -> SelectDraftingView:
        """
        Getter for property: ( SelectDraftingView NXOpen.) MasterView
         Returns the master view   
            
         
        """
        pass
    @property
    def Repetition(self) -> int:
        """
        Getter for property: (int) Repetition
         Returns the repetition of the break line pattern   
            
         
        """
        pass
    @Repetition.setter
    def Repetition(self, repetition: int):
        """
        Setter for property: (int) Repetition
         Returns the repetition of the break line pattern   
            
         
        """
        pass
    @property
    def Suppress(self) -> bool:
        """
        Getter for property: (bool) Suppress
         Returns the view break suppress status   
            
         
        """
        pass
    @Suppress.setter
    def Suppress(self, suppress: bool):
        """
        Setter for property: (bool) Suppress
         Returns the view break suppress status   
            
         
        """
        pass
    @property
    def Width(self) -> BrokenViewBuilder.LineWidth:
        """
        Getter for property: ( BrokenViewBuilder.LineWidth NXOpen.) Width
         Returns the curve width of the break line   
            
         
        """
        pass
    @Width.setter
    def Width(self, width: BrokenViewBuilder.LineWidth):
        """
        Setter for property: ( BrokenViewBuilder.LineWidth NXOpen.) Width
         Returns the curve width of the break line   
            
         
        """
        pass
import NXOpen
class CompareReportBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Drawings.CompareReportBuilder builder """
    @property
    def SummaryStatusLine(self) -> str:
        """
        Getter for property: (str) SummaryStatusLine
         Returns the report summary status line  
            
         
        """
        pass
    def GetChangesSummary(self) -> List[str]:
        """
         Returns the changes summary of report
         Returns changesSummary (List[str]): .
        """
        pass
    def GetDetailSummary(self) -> List[str]:
        """
         Returns the detail summary of report
         Returns detailSummary (List[str]): .
        """
        pass
    def GetSummary(self) -> List[str]:
        """
         Returns the summary 
         Returns summary (List[str]): .
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ConversionProcessSettingsBuilder(NXOpen.TaggedObject): 
    """
    Represents a Drawings.ConversionProcessSettingsBuilder.
    This class queries and sets settings specific to drafting data which will get converted to PMIs.
    """
    class ActionOnErrorEnum(Enum):
        """
        Members Include: 
         |SkipObjectAndContinue| 
         |StopProcessingAfterLimit| 
         |StopProcessing| 

        """
        SkipObjectAndContinue: int
        StopProcessingAfterLimit: int
        StopProcessing: int
        @staticmethod
        def ValueOf(value: int) -> ConversionProcessSettingsBuilder.ActionOnErrorEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ActionOnError(self) -> ConversionProcessSettingsBuilder.ActionOnErrorEnum:
        """
        Getter for property: ( ConversionProcessSettingsBuilder.ActionOnErrorEnum NXOpen.) ActionOnError
         Returns the action on error   
            
         
        """
        pass
    @ActionOnError.setter
    def ActionOnError(self, actionOnError: ConversionProcessSettingsBuilder.ActionOnErrorEnum):
        """
        Setter for property: ( ConversionProcessSettingsBuilder.ActionOnErrorEnum NXOpen.) ActionOnError
         Returns the action on error   
            
         
        """
        pass
    @property
    def ConfigurationFile(self) -> str:
        """
        Getter for property: (str) ConfigurationFile
         Returns the configuration file browser   
            
         
        """
        pass
    @ConfigurationFile.setter
    def ConfigurationFile(self, filename: str):
        """
        Setter for property: (str) ConfigurationFile
         Returns the configuration file browser   
            
         
        """
        pass
    @property
    def CreateInMasterModelPart(self) -> bool:
        """
        Getter for property: (bool) CreateInMasterModelPart
         Returns the create in master model part option   
            
         
        """
        pass
    @CreateInMasterModelPart.setter
    def CreateInMasterModelPart(self, createInMasterModelPart: bool):
        """
        Setter for property: (bool) CreateInMasterModelPart
         Returns the create in master model part option   
            
         
        """
        pass
    @property
    def ErrorLimit(self) -> int:
        """
        Getter for property: (int) ErrorLimit
         Returns the error limit integer   
            
         
        """
        pass
    @ErrorLimit.setter
    def ErrorLimit(self, errorLimit: int):
        """
        Setter for property: (int) ErrorLimit
         Returns the error limit integer   
            
         
        """
        pass
    @property
    def JTGeometryTolerance(self) -> float:
        """
        Getter for property: (float) JTGeometryTolerance
         Returns the geometry tolerance   
            
         
        """
        pass
    @JTGeometryTolerance.setter
    def JTGeometryTolerance(self, geometryTolerance: float):
        """
        Setter for property: (float) JTGeometryTolerance
         Returns the geometry tolerance   
            
         
        """
        pass
    @property
    def JTPartNameAttribute(self) -> str:
        """
        Getter for property: (str) JTPartNameAttribute
         Returns the JT part name   
            
         
        """
        pass
    @JTPartNameAttribute.setter
    def JTPartNameAttribute(self, partNameAttribute: str):
        """
        Setter for property: (str) JTPartNameAttribute
         Returns the JT part name   
            
         
        """
        pass
    @property
    def LogFileLocation(self) -> str:
        """
        Getter for property: (str) LogFileLocation
         Returns the log file location folder   
            
         
        """
        pass
    @LogFileLocation.setter
    def LogFileLocation(self, foldername: str):
        """
        Setter for property: (str) LogFileLocation
         Returns the log file location folder   
            
         
        """
        pass
    @property
    def MultiCADAssembly(self) -> bool:
        """
        Getter for property: (bool) MultiCADAssembly
         Returns the multi-CAD assembly   
            
         
        """
        pass
    @MultiCADAssembly.setter
    def MultiCADAssembly(self, multiCADAssembly: bool):
        """
        Setter for property: (bool) MultiCADAssembly
         Returns the multi-CAD assembly   
            
         
        """
        pass
    @property
    def SaveAsLocation(self) -> str:
        """
        Getter for property: (str) SaveAsLocation
         Returns the save as file browser   
            
         
        """
        pass
    @SaveAsLocation.setter
    def SaveAsLocation(self, filename: str):
        """
        Setter for property: (str) SaveAsLocation
         Returns the save as file browser   
            
         
        """
        pass
    @property
    def SourcePartNameAttribute(self) -> str:
        """
        Getter for property: (str) SourcePartNameAttribute
         Returns the Source part name   
            
         
        """
        pass
    @SourcePartNameAttribute.setter
    def SourcePartNameAttribute(self, partNameAttribute: str):
        """
        Setter for property: (str) SourcePartNameAttribute
         Returns the Source part name   
            
         
        """
        pass
    @property
    def StoreLogFileInTeamCenter(self) -> bool:
        """
        Getter for property: (bool) StoreLogFileInTeamCenter
         Returns the store log file in teamcenter   
            
         
        """
        pass
    @StoreLogFileInTeamCenter.setter
    def StoreLogFileInTeamCenter(self, storeLogFileInTeamCenter: bool):
        """
        Setter for property: (bool) StoreLogFileInTeamCenter
         Returns the store log file in teamcenter   
            
         
        """
        pass
import NXOpen
class ConvertDraftingContentsBuilder(NXOpen.Builder): 
    """
    Represents a Drawings.ConvertDraftingContentsBuilder.
    This class queries and sets settings specific to drafting data which will get converted to PMI.
    This class will always return NULL_TAG on commit and GetCommittedObjects function is not going to return objects commited by this builder.

    Refer to "Convert to PMI report" to know about the objects converted using this builder.
    """
    class SelectConversionEntityType(Enum):
        """
        Members Include: 
         |Drawing| 
         |Sheet| 
         |View| 
         |Annotation| 

        """
        Drawing: int
        Sheet: int
        View: int
        Annotation: int
        @staticmethod
        def ValueOf(value: int) -> ConvertDraftingContentsBuilder.SelectConversionEntityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ConfigurationFile(self) -> str:
        """
        Getter for property: (str) ConfigurationFile
         Returns the configuration file   
            
         
        """
        pass
    @ConfigurationFile.setter
    def ConfigurationFile(self, filename: str):
        """
        Setter for property: (str) ConfigurationFile
         Returns the configuration file   
            
         
        """
        pass
    @property
    def OpenConvertedPmiDestinationPart(self) -> bool:
        """
        Getter for property: (bool) OpenConvertedPmiDestinationPart
         Returns the option to open converted pmi destination part   
            
         
        """
        pass
    @OpenConvertedPmiDestinationPart.setter
    def OpenConvertedPmiDestinationPart(self, openConvertedPmiDestinationPart: bool):
        """
        Setter for property: (bool) OpenConvertedPmiDestinationPart
         Returns the option to open converted pmi destination part   
            
         
        """
        pass
    @property
    def SelectDraftingSheet(self) -> NXOpen.SelectViewList:
        """
        Getter for property: ( NXOpen.SelectViewList) SelectDraftingSheet
         Returns the select drafting sheet block.  
           
                Expect selection object of type DraftingSheet, validation is done at builder level   
         
        """
        pass
    @property
    def SelectDraftingView(self) -> SelectDraftingViewList:
        """
        Getter for property: ( SelectDraftingViewList NXOpen.) SelectDraftingView
         Returns the select drafting view block   
            
         
        """
        pass
    @property
    def SelectObjectsToConvert(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SelectObjectsToConvert
         Returns the select objects to convert   
            
         
        """
        pass
    @property
    def SelectionType(self) -> ConvertDraftingContentsBuilder.SelectConversionEntityType:
        """
        Getter for property: ( ConvertDraftingContentsBuilder.SelectConversionEntityType NXOpen.) SelectionType
         Returns the selection type   
            
         
        """
        pass
    @SelectionType.setter
    def SelectionType(self, selectionType: ConvertDraftingContentsBuilder.SelectConversionEntityType):
        """
        Setter for property: ( ConvertDraftingContentsBuilder.SelectConversionEntityType NXOpen.) SelectionType
         Returns the selection type   
            
         
        """
        pass
    @property
    def SettingsBuilder(self) -> SettingsBuilder:
        """
        Getter for property: ( SettingsBuilder NXOpen.) SettingsBuilder
         Returns the settings   
            
         
        """
        pass
    @property
    def UseContextAssembly(self) -> bool:
        """
        Getter for property: (bool) UseContextAssembly
         Returns the use context assembly   
            
         
        """
        pass
    @UseContextAssembly.setter
    def UseContextAssembly(self, useContextAssembly: bool):
        """
        Setter for property: (bool) UseContextAssembly
         Returns the use context assembly   
            
         
        """
        pass
    def SetContextAssembly(self, contextAssembly: str) -> None:
        """
         Context assembly part file path 
        """
        pass
import NXOpen
class ConvertToPMIBuilderManager(NXOpen.Object): 
    """
    Represents NXOpen.Drawings.ConvertToPMIBuilderManager
    """
    def CreateConvertDraftingContentsBuilder(self) -> ConvertDraftingContentsBuilder:
        """
         Creator for Drawing to PMI Builder 
         Returns builder ( ConvertDraftingContentsBuilder NXOpen.): .
        """
        pass
    def CreateReportBuilder(self) -> ReportBuilder:
        """
         Creator for Drawing to PMI Report Builder 
         Returns builder ( ReportBuilder NXOpen.): .
        """
        pass
    def DeleteConversionReport(self, reportIndex: int) -> None:
        """
         API used to delete drawing to PMI conversion report 
        """
        pass
    def DeleteConvertedData(self, reportIndex: int) -> None:
        """
         API used to delete drawing to PMI conversion data 
        """
        pass
    def GetConversionReportsCount(self) -> int:
        """
         API used to get count of drawing to PMI conversion reports 
         Returns reportIndex (int): .
        """
        pass
import NXOpen
class CustomViewSettingsBuilder(NXOpen.Builder): 
    """ this class represents the "this class represents Drawings.CustomViewSettingsBuilder.
        It consists of the settings which optimize the view creation for large assemblies and these
        settings are subset of the view style settings """
    class Features(Enum):
        """
        Members Include: 
         |ShowAll| 
         |Simplify| 
         |Hide| 

        """
        ShowAll: int
        Simplify: int
        Hide: int
        @staticmethod
        def ValueOf(value: int) -> CustomViewSettingsBuilder.Features:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Font(Enum):
        """
        Members Include: 
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
        def ValueOf(value: int) -> CustomViewSettingsBuilder.Font:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Interfering(Enum):
        """
        Members Include: 
         |NotSet| 
         |WithoutInterference| 
         |WithInterference| 

        """
        NotSet: int
        WithoutInterference: int
        WithInterference: int
        @staticmethod
        def ValueOf(value: int) -> CustomViewSettingsBuilder.Interfering:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ThreadStandards(Enum):
        """
        Members Include: 
         |NotSet| 
         |AnsiSimplified| 
         |AnsiSchematic| 
         |AnsiDetailed| 
         |IsoSimplified| 
         |IsoDetailed| 
         |EskdSimplified| 

        """
        NotSet: int
        AnsiSimplified: int
        AnsiSchematic: int
        AnsiDetailed: int
        IsoSimplified: int
        IsoDetailed: int
        EskdSimplified: int
        @staticmethod
        def ValueOf(value: int) -> CustomViewSettingsBuilder.ThreadStandards:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Width(Enum):
        """
        Members Include: 
         |Original|  Original 
         |One|  One      
         |Two|  Two      
         |Three|  Three    
         |Four|  Four     
         |Five|  Five     
         |Six|  Six      
         |Seven|  Seven    
         |Eight|  Eight    
         |Nine|  Nine     

        """
        Original: int
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
        def ValueOf(value: int) -> CustomViewSettingsBuilder.Width:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DelayUpdateOnCreation(self) -> bool:
        """
        Getter for property: (bool) DelayUpdateOnCreation
         Returns the delay update on creation   
            
         
        """
        pass
    @DelayUpdateOnCreation.setter
    def DelayUpdateOnCreation(self, delayUpdateOnCreation: bool):
        """
        Setter for property: (bool) DelayUpdateOnCreation
         Returns the delay update on creation   
            
         
        """
        pass
    @property
    def DelayViewUpdate(self) -> bool:
        """
        Getter for property: (bool) DelayViewUpdate
         Returns the delay view update   
            
         
        """
        pass
    @DelayViewUpdate.setter
    def DelayViewUpdate(self, delayViewUpdate: bool):
        """
        Setter for property: (bool) DelayViewUpdate
         Returns the delay view update   
            
         
        """
        pass
    @property
    def HiddenLinesColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) HiddenLinesColor
         Returns the hidden lines color   
            
         
        """
        pass
    @HiddenLinesColor.setter
    def HiddenLinesColor(self, hiddenLinesColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) HiddenLinesColor
         Returns the hidden lines color   
            
         
        """
        pass
    @property
    def HiddenLinesFont(self) -> CustomViewSettingsBuilder.Font:
        """
        Getter for property: ( CustomViewSettingsBuilder.Font NXOpen.) HiddenLinesFont
         Returns the hidden lines font   
            
         
        """
        pass
    @HiddenLinesFont.setter
    def HiddenLinesFont(self, hiddenLinesFont: CustomViewSettingsBuilder.Font):
        """
        Setter for property: ( CustomViewSettingsBuilder.Font NXOpen.) HiddenLinesFont
         Returns the hidden lines font   
            
         
        """
        pass
    @property
    def HiddenLinesWidth(self) -> CustomViewSettingsBuilder.Width:
        """
        Getter for property: ( CustomViewSettingsBuilder.Width NXOpen.) HiddenLinesWidth
         Returns the hidden line hidden font   
            
         
        """
        pass
    @HiddenLinesWidth.setter
    def HiddenLinesWidth(self, hiddenLinesWidth: CustomViewSettingsBuilder.Width):
        """
        Setter for property: ( CustomViewSettingsBuilder.Width NXOpen.) HiddenLinesWidth
         Returns the hidden line hidden font   
            
         
        """
        pass
    @property
    def InterferingSolids(self) -> CustomViewSettingsBuilder.Interfering:
        """
        Getter for property: ( CustomViewSettingsBuilder.Interfering NXOpen.) InterferingSolids
         Returns the interfering solids   
            
         
        """
        pass
    @InterferingSolids.setter
    def InterferingSolids(self, interferingSolids: CustomViewSettingsBuilder.Interfering):
        """
        Setter for property: ( CustomViewSettingsBuilder.Interfering NXOpen.) InterferingSolids
         Returns the interfering solids   
            
         
        """
        pass
    @property
    def MinimumPitch(self) -> float:
        """
        Getter for property: (float) MinimumPitch
         Returns the minimum pitch   
            
         
        """
        pass
    @MinimumPitch.setter
    def MinimumPitch(self, minimumPitch: float):
        """
        Setter for property: (float) MinimumPitch
         Returns the minimum pitch   
            
         
        """
        pass
    @property
    def RenderTrueHiddenLine(self) -> bool:
        """
        Getter for property: (bool) RenderTrueHiddenLine
         Returns the render true hidden line   
            
         
        """
        pass
    @RenderTrueHiddenLine.setter
    def RenderTrueHiddenLine(self, renderTrueHiddenLine: bool):
        """
        Setter for property: (bool) RenderTrueHiddenLine
         Returns the render true hidden line   
            
         
        """
        pass
    @property
    def ShowAdjacentBlends(self) -> bool:
        """
        Getter for property: (bool) ShowAdjacentBlends
         Returns the show adjacent blends   
            
         
        """
        pass
    @ShowAdjacentBlends.setter
    def ShowAdjacentBlends(self, showAdjacentBlends: bool):
        """
        Setter for property: (bool) ShowAdjacentBlends
         Returns the show adjacent blends   
            
         
        """
        pass
    @property
    def ShowCenterLines(self) -> bool:
        """
        Getter for property: (bool) ShowCenterLines
         Returns the show center lines   
            
         
        """
        pass
    @ShowCenterLines.setter
    def ShowCenterLines(self, showCenterLines: bool):
        """
        Setter for property: (bool) ShowCenterLines
         Returns the show center lines   
            
         
        """
        pass
    @property
    def ShowCheckBoundaryStatus(self) -> bool:
        """
        Getter for property: (bool) ShowCheckBoundaryStatus
         Returns the show check boundary status   
            
         
        """
        pass
    @ShowCheckBoundaryStatus.setter
    def ShowCheckBoundaryStatus(self, showCheckBoundaryStatus: bool):
        """
        Setter for property: (bool) ShowCheckBoundaryStatus
         Returns the show check boundary status   
            
         
        """
        pass
    @property
    def ShowEdgesHiddenByEdges(self) -> bool:
        """
        Getter for property: (bool) ShowEdgesHiddenByEdges
         Returns the show edges hidden by edges   
            
         
        """
        pass
    @ShowEdgesHiddenByEdges.setter
    def ShowEdgesHiddenByEdges(self, showEdgesHiddenByEdges: bool):
        """
        Setter for property: (bool) ShowEdgesHiddenByEdges
         Returns the show edges hidden by edges   
            
         
        """
        pass
    @property
    def ShowHiddenLines(self) -> bool:
        """
        Getter for property: (bool) ShowHiddenLines
         Returns the show hidden lines   
            
         
        """
        pass
    @ShowHiddenLines.setter
    def ShowHiddenLines(self, showHiddenLines: bool):
        """
        Setter for property: (bool) ShowHiddenLines
         Returns the show hidden lines   
            
         
        """
        pass
    @property
    def ShowSelfHiddenLines(self) -> bool:
        """
        Getter for property: (bool) ShowSelfHiddenLines
         Returns the show self hidden lines   
            
         
        """
        pass
    @ShowSelfHiddenLines.setter
    def ShowSelfHiddenLines(self, showSelfHiddenLines: bool):
        """
        Setter for property: (bool) ShowSelfHiddenLines
         Returns the show self hidden lines   
            
         
        """
        pass
    @property
    def ShowSmoothEdgeEndGapsLock(self) -> bool:
        """
        Getter for property: (bool) ShowSmoothEdgeEndGapsLock
         Returns the show end gaps lock   
            
         
        """
        pass
    @ShowSmoothEdgeEndGapsLock.setter
    def ShowSmoothEdgeEndGapsLock(self, showEndGapsLock: bool):
        """
        Setter for property: (bool) ShowSmoothEdgeEndGapsLock
         Returns the show end gaps lock   
            
         
        """
        pass
    @property
    def ShowSmoothEdgeEndGapsValue(self) -> float:
        """
        Getter for property: (float) ShowSmoothEdgeEndGapsValue
         Returns the show end gaps value   
            
         
        """
        pass
    @ShowSmoothEdgeEndGapsValue.setter
    def ShowSmoothEdgeEndGapsValue(self, showEndGapsValue: float):
        """
        Setter for property: (float) ShowSmoothEdgeEndGapsValue
         Returns the show end gaps value   
            
         
        """
        pass
    @property
    def ShowSmoothEdges(self) -> bool:
        """
        Getter for property: (bool) ShowSmoothEdges
         Returns the show smooth edges   
            
         
        """
        pass
    @ShowSmoothEdges.setter
    def ShowSmoothEdges(self, showSmoothEdges: bool):
        """
        Setter for property: (bool) ShowSmoothEdges
         Returns the show smooth edges   
            
         
        """
        pass
    @property
    def ShowTraceLines(self) -> bool:
        """
        Getter for property: (bool) ShowTraceLines
         Returns the show trace lines   
            
         
        """
        pass
    @ShowTraceLines.setter
    def ShowTraceLines(self, showTraceLines: bool):
        """
        Setter for property: (bool) ShowTraceLines
         Returns the show trace lines   
            
         
        """
        pass
    @property
    def ShowUVGrids(self) -> bool:
        """
        Getter for property: (bool) ShowUVGrids
         Returns the show uvgrids   
            
         
        """
        pass
    @ShowUVGrids.setter
    def ShowUVGrids(self, showUVGrids: bool):
        """
        Setter for property: (bool) ShowUVGrids
         Returns the show uvgrids   
            
         
        """
        pass
    @property
    def ShowVIEndGapsLock(self) -> bool:
        """
        Getter for property: (bool) ShowVIEndGapsLock
         Returns the show end gaps lock   
            
         
        """
        pass
    @ShowVIEndGapsLock.setter
    def ShowVIEndGapsLock(self, showEndGapsLock: bool):
        """
        Setter for property: (bool) ShowVIEndGapsLock
         Returns the show end gaps lock   
            
         
        """
        pass
    @property
    def ShowVIEndGapsValue(self) -> float:
        """
        Getter for property: (float) ShowVIEndGapsValue
         Returns the show end gaps value   
            
         
        """
        pass
    @ShowVIEndGapsValue.setter
    def ShowVIEndGapsValue(self, showEndGapsValue: float):
        """
        Setter for property: (float) ShowVIEndGapsValue
         Returns the show end gaps value   
            
         
        """
        pass
    @property
    def ShowVirtualIntersections(self) -> bool:
        """
        Getter for property: (bool) ShowVirtualIntersections
         Returns the show virtual intersections   
            
         
        """
        pass
    @ShowVirtualIntersections.setter
    def ShowVirtualIntersections(self, showVirtualIntersections: bool):
        """
        Setter for property: (bool) ShowVirtualIntersections
         Returns the show virtual intersections   
            
         
        """
        pass
    @property
    def SmallFeatures(self) -> CustomViewSettingsBuilder.Features:
        """
        Getter for property: ( CustomViewSettingsBuilder.Features NXOpen.) SmallFeatures
         Returns the small features   
            
         
        """
        pass
    @SmallFeatures.setter
    def SmallFeatures(self, smallFeatures: CustomViewSettingsBuilder.Features):
        """
        Setter for property: ( CustomViewSettingsBuilder.Features NXOpen.) SmallFeatures
         Returns the small features   
            
         
        """
        pass
    @property
    def SmoothEdgeColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) SmoothEdgeColor
         Returns the smooth edge color pick   
            
         
        """
        pass
    @SmoothEdgeColor.setter
    def SmoothEdgeColor(self, smoothEdgeColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) SmoothEdgeColor
         Returns the smooth edge color pick   
            
         
        """
        pass
    @property
    def SmoothEdgeFont(self) -> CustomViewSettingsBuilder.Font:
        """
        Getter for property: ( CustomViewSettingsBuilder.Font NXOpen.) SmoothEdgeFont
         Returns the smooth edge line font   
            
         
        """
        pass
    @SmoothEdgeFont.setter
    def SmoothEdgeFont(self, smoothEdgeLineFont: CustomViewSettingsBuilder.Font):
        """
        Setter for property: ( CustomViewSettingsBuilder.Font NXOpen.) SmoothEdgeFont
         Returns the smooth edge line font   
            
         
        """
        pass
    @property
    def SmoothEdgeWidth(self) -> CustomViewSettingsBuilder.Width:
        """
        Getter for property: ( CustomViewSettingsBuilder.Width NXOpen.) SmoothEdgeWidth
         Returns the smooth edges line hidden font   
            
         
        """
        pass
    @SmoothEdgeWidth.setter
    def SmoothEdgeWidth(self, smoothEdgeLineWidth: CustomViewSettingsBuilder.Width):
        """
        Setter for property: ( CustomViewSettingsBuilder.Width NXOpen.) SmoothEdgeWidth
         Returns the smooth edges line hidden font   
            
         
        """
        pass
    @property
    def ThreadStandard(self) -> CustomViewSettingsBuilder.ThreadStandards:
        """
        Getter for property: ( CustomViewSettingsBuilder.ThreadStandards NXOpen.) ThreadStandard
         Returns the thread standard   
            
         
        """
        pass
    @ThreadStandard.setter
    def ThreadStandard(self, threadStandard: CustomViewSettingsBuilder.ThreadStandards):
        """
        Setter for property: ( CustomViewSettingsBuilder.ThreadStandards NXOpen.) ThreadStandard
         Returns the thread standard   
            
         
        """
        pass
    @property
    def TraceLineCreateGapsLock(self) -> bool:
        """
        Getter for property: (bool) TraceLineCreateGapsLock
         Returns the trace line create gaps lock   
            
         
        """
        pass
    @TraceLineCreateGapsLock.setter
    def TraceLineCreateGapsLock(self, traceLineCreateGapsLock: bool):
        """
        Setter for property: (bool) TraceLineCreateGapsLock
         Returns the trace line create gaps lock   
            
         
        """
        pass
    @property
    def TraceLineCreateGapsValue(self) -> float:
        """
        Getter for property: (float) TraceLineCreateGapsValue
         Returns the trace line create gaps value   
            
         
        """
        pass
    @TraceLineCreateGapsValue.setter
    def TraceLineCreateGapsValue(self, traceLineCreateGapsValue: float):
        """
        Setter for property: (float) TraceLineCreateGapsValue
         Returns the trace line create gaps value   
            
         
        """
        pass
    @property
    def TraceLineHiddenColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) TraceLineHiddenColor
         Returns the trace line hidden color   
            
         
        """
        pass
    @TraceLineHiddenColor.setter
    def TraceLineHiddenColor(self, traceLineHiddenColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) TraceLineHiddenColor
         Returns the trace line hidden color   
            
         
        """
        pass
    @property
    def TraceLineHiddenFont(self) -> CustomViewSettingsBuilder.Font:
        """
        Getter for property: ( CustomViewSettingsBuilder.Font NXOpen.) TraceLineHiddenFont
         Returns the trace line hidden font   
            
         
        """
        pass
    @TraceLineHiddenFont.setter
    def TraceLineHiddenFont(self, traceLineHiddenFont: CustomViewSettingsBuilder.Font):
        """
        Setter for property: ( CustomViewSettingsBuilder.Font NXOpen.) TraceLineHiddenFont
         Returns the trace line hidden font   
            
         
        """
        pass
    @property
    def TraceLineHiddenWidth(self) -> CustomViewSettingsBuilder.Width:
        """
        Getter for property: ( CustomViewSettingsBuilder.Width NXOpen.) TraceLineHiddenWidth
         Returns the trace line hidden Width   
            
         
        """
        pass
    @TraceLineHiddenWidth.setter
    def TraceLineHiddenWidth(self, traceLineHiddenWidth: CustomViewSettingsBuilder.Width):
        """
        Setter for property: ( CustomViewSettingsBuilder.Width NXOpen.) TraceLineHiddenWidth
         Returns the trace line hidden Width   
            
         
        """
        pass
    @property
    def TraceLineVisibleColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) TraceLineVisibleColor
         Returns the trace line visible color   
            
         
        """
        pass
    @TraceLineVisibleColor.setter
    def TraceLineVisibleColor(self, traceLineVisibleColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) TraceLineVisibleColor
         Returns the trace line visible color   
            
         
        """
        pass
    @property
    def TraceLineVisibleFont(self) -> CustomViewSettingsBuilder.Font:
        """
        Getter for property: ( CustomViewSettingsBuilder.Font NXOpen.) TraceLineVisibleFont
         Returns the trace line visible font   
            
         
        """
        pass
    @TraceLineVisibleFont.setter
    def TraceLineVisibleFont(self, traceLineVisibleFont: CustomViewSettingsBuilder.Font):
        """
        Setter for property: ( CustomViewSettingsBuilder.Font NXOpen.) TraceLineVisibleFont
         Returns the trace line visible font   
            
         
        """
        pass
    @property
    def TraceLineVisibleWidth(self) -> CustomViewSettingsBuilder.Width:
        """
        Getter for property: ( CustomViewSettingsBuilder.Width NXOpen.) TraceLineVisibleWidth
         Returns the trace line visible font   
            
         
        """
        pass
    @TraceLineVisibleWidth.setter
    def TraceLineVisibleWidth(self, traceLineVisibleWidth: CustomViewSettingsBuilder.Width):
        """
        Setter for property: ( CustomViewSettingsBuilder.Width NXOpen.) TraceLineVisibleWidth
         Returns the trace line visible font   
            
         
        """
        pass
    @property
    def VirtualInterSectionColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) VirtualInterSectionColor
         Returns the virtual inter section color   
            
         
        """
        pass
    @VirtualInterSectionColor.setter
    def VirtualInterSectionColor(self, virtualInterSectionColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) VirtualInterSectionColor
         Returns the virtual inter section color   
            
         
        """
        pass
    @property
    def VirtualInterSectionFont(self) -> CustomViewSettingsBuilder.Font:
        """
        Getter for property: ( CustomViewSettingsBuilder.Font NXOpen.) VirtualInterSectionFont
         Returns the virtual inter section font   
            
         
        """
        pass
    @VirtualInterSectionFont.setter
    def VirtualInterSectionFont(self, virtualInterSectionFont: CustomViewSettingsBuilder.Font):
        """
        Setter for property: ( CustomViewSettingsBuilder.Font NXOpen.) VirtualInterSectionFont
         Returns the virtual inter section font   
            
         
        """
        pass
    @property
    def VirtualInterSectionWidth(self) -> CustomViewSettingsBuilder.Width:
        """
        Getter for property: ( CustomViewSettingsBuilder.Width NXOpen.) VirtualInterSectionWidth
         Returns the virtual inter section width   
            
         
        """
        pass
    @VirtualInterSectionWidth.setter
    def VirtualInterSectionWidth(self, virtualInterSectionWidth: CustomViewSettingsBuilder.Width):
        """
        Setter for property: ( CustomViewSettingsBuilder.Width NXOpen.) VirtualInterSectionWidth
         Returns the virtual inter section width   
            
         
        """
        pass
import NXOpen
class DetailViewBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Drawings.DetailView.  This class is
    used to create and edit Detail Views
    """
    class LabelOnParentType(Enum):
        """
        Members Include: 
         |NotSet|  No display 
         |Circle|  Circular 
         |Note|  Circular with a note 
         |Label|  Circular with a label 
         |Embedded|  Circular with a note embedded 
         |Boundary|  The shape is the same as the boundary 
         |LabelOnBoundary|  Boundary with a label 

        """
        NotSet: int
        Circle: int
        Note: int
        Label: int
        Embedded: int
        Boundary: int
        LabelOnBoundary: int
        @staticmethod
        def ValueOf(value: int) -> DetailViewBuilder.LabelOnParentType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |Undefined|  For initial values 
         |Circular|  Circular boundary 
         |RectangleByCorners|  Rectangular boundary defined by two corners 
         |RectangleByCenterAndCorner|  Rectangular boundary defined by the center and a corner 
         |Custom|  Custom boundary (this should not be used unless the detail view already has a custom boundary 

        """
        Undefined: int
        Circular: int
        RectangleByCorners: int
        RectangleByCenterAndCorner: int
        Custom: int
        @staticmethod
        def ValueOf(value: int) -> DetailViewBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns the associative toggle
                    If view is associative and set associative to false, the view will be converted
                    to independent detail view.  
           Otherwise, this setting will have no effect
                  
         
        """
        pass
    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
         Returns the associative toggle
                    If view is associative and set associative to false, the view will be converted
                    to independent detail view.  
           Otherwise, this setting will have no effect
                  
         
        """
        pass
    @property
    def BoundaryPoint1(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) BoundaryPoint1
         Returns
                the first boundary point.  
            This is the center of the boundary for these types:
                 NXOpen::Drawings::DetailViewBuilder::TypesCircular  and 
                 NXOpen::Drawings::DetailViewBuilder::TypesRectangleByCenterAndCorner .
                This boundary point will be NULL for the type: 
                 NXOpen::Drawings::DetailViewBuilder::TypesCustom 
                  
         
        """
        pass
    @BoundaryPoint1.setter
    def BoundaryPoint1(self, boundaryPoint1: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) BoundaryPoint1
         Returns
                the first boundary point.  
            This is the center of the boundary for these types:
                 NXOpen::Drawings::DetailViewBuilder::TypesCircular  and 
                 NXOpen::Drawings::DetailViewBuilder::TypesRectangleByCenterAndCorner .
                This boundary point will be NULL for the type: 
                 NXOpen::Drawings::DetailViewBuilder::TypesCustom 
                  
         
        """
        pass
    @property
    def BoundaryPoint2(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) BoundaryPoint2
         Returns
                the second boundary point.  
            This is the point on the circle for the 
                 NXOpen::Drawings::DetailViewBuilder::TypesCircular  and 
                the corner point for the  NXOpen::Drawings::DetailViewBuilder::TypesRectangleByCenterAndCorner .
                This boundary point will be NULL for the type:
                 NXOpen::Drawings::DetailViewBuilder::TypesCustom 
                  
         
        """
        pass
    @BoundaryPoint2.setter
    def BoundaryPoint2(self, boundaryPoint2: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) BoundaryPoint2
         Returns
                the second boundary point.  
            This is the point on the circle for the 
                 NXOpen::Drawings::DetailViewBuilder::TypesCircular  and 
                the corner point for the  NXOpen::Drawings::DetailViewBuilder::TypesRectangleByCenterAndCorner .
                This boundary point will be NULL for the type:
                 NXOpen::Drawings::DetailViewBuilder::TypesCustom 
                  
         
        """
        pass
    @property
    def HiddenObjects(self) -> HiddenObjectsBuilder:
        """
        Getter for property: ( HiddenObjectsBuilder NXOpen.) HiddenObjects
         Returns the list of objects to not show in the view   
            
         
        """
        pass
    @property
    def LabelOnParent(self) -> DetailViewBuilder.LabelOnParentType:
        """
        Getter for property: ( DetailViewBuilder.LabelOnParentType NXOpen.) LabelOnParent
         Returns the label on parent   
            
         
        """
        pass
    @LabelOnParent.setter
    def LabelOnParent(self, labelOnParent: DetailViewBuilder.LabelOnParentType):
        """
        Setter for property: ( DetailViewBuilder.LabelOnParentType NXOpen.) LabelOnParent
         Returns the label on parent   
            
         
        """
        pass
    @property
    def NonSectionedObjects(self) -> HiddenObjectsBuilder:
        """
        Getter for property: ( HiddenObjectsBuilder NXOpen.) NonSectionedObjects
         Returns the list of objects to not section in the view   
            
         
        """
        pass
    @property
    def Origin(self) -> ViewPlacementBuilder:
        """
        Getter for property: ( ViewPlacementBuilder NXOpen.) Origin
         Returns the origin   
            
         
        """
        pass
    @property
    def Parent(self) -> ParentViewBuilder:
        """
        Getter for property: ( ParentViewBuilder NXOpen.) Parent
         Returns the parent view   
            
         
        """
        pass
    @property
    def Scale(self) -> ViewScaleBuilder:
        """
        Getter for property: ( ViewScaleBuilder NXOpen.) Scale
         Returns the scale   
            
         
        """
        pass
    @property
    def SecondaryComponents(self) -> DraftingComponentSelectionBuilder:
        """
        Getter for property: ( DraftingComponentSelectionBuilder NXOpen.) SecondaryComponents
         Returns the list of secondary components in the view   
            
         
        """
        pass
    @property
    def Style(self) -> ViewStyleBuilder:
        """
        Getter for property: ( ViewStyleBuilder NXOpen.) Style
         Returns the style   
            
         
        """
        pass
    @property
    def Type(self) -> DetailViewBuilder.Types:
        """
        Getter for property: ( DetailViewBuilder.Types NXOpen.) Type
         Returns the type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: DetailViewBuilder.Types):
        """
        Setter for property: ( DetailViewBuilder.Types NXOpen.) Type
         Returns the type   
            
         
        """
        pass
class DetailView(DraftingView): 
    """ Represents a Detail View.
        A detail view is a view which contains an enlarged portion of an already
        existing drawing view. The enlarged detail view shows detail which is not
        apparent in the view from which the detail was made. """
    def LogUpdate(self, reason: int) -> None:
        """
         Notify detail view update. 
        """
        pass
import NXOpen
class DraftingBodyCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Drawings.DraftingBodys.   """
    def FindObject(self, journal_identifier: str) -> DraftingBody:
        """
         Finds the  NXOpen.Drawings.DraftingBody  with the given identifier as recorded in a journal.
                An object may not return the same value as its JournalIdentifier in different versions of
                the software. However newer versions of the software should find the same object when
                FindObject is passed older versions of its journal identifier. In general, this method
                should not be used in handwritten code and exists to support record and playback of journals.
                An exception will be thrown if no object can be found with the given journal identifier. 
         Returns found ( DraftingBody NXOpen.):  DraftingBody with this identifier .
        """
        pass
import NXOpen
class DraftingBody(NXOpen.DisplayableObject): 
    """ Represents a drafting body. """
    @property
    def DraftingCurves() -> DraftingCurveCollection:
        """
         Returns the DraftingCurveCollection 
        """
        pass
    @property
    def DraftingPoints() -> DraftingPointCollection:
        """
         Returns the DraftingPointCollection 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class DraftingComponentSelectionBuilder(NXOpen.TaggedObject): 
    """ This builder allows the user to select a view in which
        component objects can be designated as primary or secondary geometry """
    class Geometry(Enum):
        """
        Members Include: 
         |PrimaryGeometry|  indicates the component objects are to be rendered with Primary geometry colorfontwidth 
         |SecondaryGeometry|  indicates the component objects are to be rendered with Secondary geometry colorfontwidth 

        """
        PrimaryGeometry: int
        SecondaryGeometry: int
        @staticmethod
        def ValueOf(value: int) -> DraftingComponentSelectionBuilder.Geometry:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ObjectType(self) -> DraftingComponentSelectionBuilder.Geometry:
        """
        Getter for property: ( DraftingComponentSelectionBuilder.Geometry NXOpen.) ObjectType
         Returns the object type   
            
         
        """
        pass
    @ObjectType.setter
    def ObjectType(self, objectType: DraftingComponentSelectionBuilder.Geometry):
        """
        Setter for property: ( DraftingComponentSelectionBuilder.Geometry NXOpen.) ObjectType
         Returns the object type   
            
         
        """
        pass
    @property
    def Objects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Objects
         Returns the selected objects (part occurrences) based on current object type   
            
         
        """
        pass
    @property
    def Part(self) -> NXOpen.Part:
        """
        Getter for property: ( NXOpen.Part) Part
         Returns the part to use for populating the primary and secondary components object list   
            
         
        """
        pass
    @Part.setter
    def Part(self, part: NXOpen.Part):
        """
        Setter for property: ( NXOpen.Part) Part
         Returns the part to use for populating the primary and secondary components object list   
            
         
        """
        pass
    @property
    def PartForKF(self) -> NXOpen.Part:
        """
        Getter for property: ( NXOpen.Part) PartForKF
         Returns the part to use for populating the primary and secondary components object list   
            
         
        """
        pass
    def ClearSecondaryComponentList(self) -> None:
        """
         Clears the secondary component list. 
        """
        pass
    def InitializeListFromObject(self, inputObject: NXOpen.NXObject) -> None:
        """
         Initialize list of components from the input object's components list. 
        """
        pass
    def ResetListToGlobal(self) -> None:
        """
         Reset list of components to those specified by Properties-Drawings-Secondary Geometry 
        """
        pass
import NXOpen
class DraftingCurveCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Drawings.DraftingCurves.   """
    def FindObject(self, journal_identifier: str) -> DraftingCurve:
        """
         Finds the  NXOpen.Drawings.DraftingCurve  with the given identifier as recorded in a journal.
                An object may not return the same value as its JournalIdentifier in different versions of
                the software. However newer versions of the software should find the same object when
                FindObject is passed older versions of its journal identifier. In general, this method
                should not be used in handwritten code and exists to support record and playback of journals.
                An exception will be thrown if no object can be found with the given journal identifier. 
         Returns found ( DraftingCurve NXOpen.):  DraftingCurve with this identifier .
        """
        pass
import NXOpen
class DraftingCurveInfo(NXOpen.TransientObject): 
    """ Represents Drafting Curve Info """
    class DraftingCurveType(Enum):
        """
        Members Include: 
         |NonDraftingCurve|  Specifies Not a Drafting Curve 
         |ExtractedEdge|  Specifies Extracted Edge Curve 
         |ExtractedModelCurve|  Specifies Extracted Model Curve 
         |SilhouetteCurve|  Specifies Silhouette Curve 
         |ThreadSilhouetteCurve|  Specifies Thread Silhouette Curve 
         |SectionEdge|  Specifies Section Edge Curve 
         |ThreadSectionEdge|  Specifies Thread Section Edge Curve 
         |VICurve|  Specifies Virtual Intersection Curve 
         |UVHatchCurve|  Specifies UVHatch Curve 
         |TracelineCurve|  Specifies TraceLine Curve 
         |SimplifiedCurve|  Specifies Simplified Curve 
         |InterferenceCurve|  Specifies Interference Curve 
         |ExtractedPoint|  Specifies Extracted Model Point 

        """
        NonDraftingCurve: int
        ExtractedEdge: int
        ExtractedModelCurve: int
        SilhouetteCurve: int
        ThreadSilhouetteCurve: int
        SectionEdge: int
        ThreadSectionEdge: int
        VICurve: int
        UVHatchCurve: int
        TracelineCurve: int
        SimplifiedCurve: int
        InterferenceCurve: int
        ExtractedPoint: int
        @staticmethod
        def ValueOf(value: int) -> DraftingCurveInfo.DraftingCurveType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CurveType(self) -> DraftingCurveInfo.DraftingCurveType:
        """
        Getter for property: ( DraftingCurveInfo.DraftingCurveType NXOpen.) CurveType
         Returns the drafting curve type   
            
         
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory. After this method is called,
                it is illegal to use the object. In .NET, this method is automatically
                called when the object is deleted by the garbage collector. 
        """
        pass
    def GetParents(self) -> List[NXOpen.NXObject]:
        """
         Returns the parents for input drafting curve 
         Returns parents ( NXOpen.NXObject Li):  List of parents .
        """
        pass
import NXOpen
class DraftingCurve(NXOpen.DisplayableObject): 
    """ Represents a Drafting VD Curve. """
    pass
class DraftingDrawingSheetBuilder(DrawingSheetBuilder): 
    """ Represents a Builder for creating NXOpen.Drawings.DraftingDrawingSheets """
    pass
import NXOpen
class DraftingDrawingSheetCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Drawings.DraftingDrawingSheets. """
    @property
    def CurrentDrawingSheet(self) -> DraftingDrawingSheet:
        """
        Getter for property: ( DraftingDrawingSheet NXOpen.) CurrentDrawingSheet
         Returns the currently opened drafting drawing sheet.  
           This will return NULL if no drafting drawing sheet is opened.   
         
        """
        pass
    def CreateDraftingDrawingSheetBuilder(self, draftingDrawingSheet: DraftingDrawingSheet) -> DraftingDrawingSheetBuilder:
        """
         Creates a NXOpen.Drawings.DraftingDrawingSheetBuilder 
         Returns builder ( DraftingDrawingSheetBuilder NXOpen.):  the drafting drawing sheet builder .
        """
        pass
    def FindObject(self, journalIdentifier: str) -> DraftingDrawingSheet:
        """
         Finds the NXOpen.Drawings.DraftingDrawingSheet with the given identifier 
                as recorded in a journal.  An object may not return the same value as its JournalIdentifier in 
                different versions of  the software. However newer versions of the software should find the same 
                object when  FindObject is passed older versions of its journal identifier. In general, this method 
                should not be used in handwritten code and exists to support record and playback of journals.
                An exception will be thrown if no object can be found with the given journal identifier. 
         Returns draftingDrawingSheet ( DraftingDrawingSheet NXOpen.):  Drafting drawing sheet with this identifier .
        """
        pass
    @overload
    def InsertSheet(self, drawing_name: str, drawing_units: DrawingSheet.Unit, width: float, height: float, numerator: float, denominator: float, projection_angle: DrawingSheet.ProjectionAngleType) -> DraftingDrawingSheet:
        """
         Inserts a drafting drawing sheet into a part. 
         Returns drawing_sheet ( DraftingDrawingSheet NXOpen.):   .
        """
        pass
    @overload
    def InsertSheet(self, drawing_name: str, sheet_size: DrawingSheet.StandardSheetSize, numerator: float, denominator: float, projection_angle: DrawingSheet.ProjectionAngleType) -> DraftingDrawingSheet:
        """
         Inserts a sheet into a part. The drawings units will be inferred from the standard
                    size.
         Returns drawing_sheet ( DraftingDrawingSheet NXOpen.):   .
        """
        pass
class DraftingDrawingSheet(DrawingSheet): 
    """ Represents a drafting drawing sheet. """
    pass
import NXOpen
class DraftingPointCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Drawings.DraftingPoints.   """
    def FindObject(self, journal_identifier: str) -> DraftingPoint:
        """
         Finds the  NXOpen.Drawings.DraftingPoint  with the given identifier as recorded in a journal.
                An object may not return the same value as its JournalIdentifier in different versions of
                the software. However newer versions of the software should find the same object when
                FindObject is passed older versions of its journal identifier. In general, this method
                should not be used in handwritten code and exists to support record and playback of journals.
                An exception will be thrown if no object can be found with the given journal identifier. 
         Returns found ( DraftingPoint NXOpen.):  DraftingPoint with this identifier .
        """
        pass
import NXOpen
class DraftingPoint(NXOpen.Point): 
    """ Represents a Drafting VD Point. """
    def GetDraftingPointInfo(self) -> DraftingCurveInfo:
        """
         Creates new DraftingCurveInfo object 
         Returns draftingCurveInfo ( DraftingCurveInfo NXOpen.):  New DraftingCurveInfo object. Returns  if the input object
                                                                                                                           is not a drafting curvepoint .
        """
        pass
import NXOpen
class DraftingViewCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Drawings.DraftingViews.   """
    class ViewCopyAnnotOption(Enum):
        """
        Members Include: 
         |CopyAnnotation|  copy annotation
         |DontCopyAnnotation|  don't copy annotation

        """
        CopyAnnotation: int
        DontCopyAnnotation: int
        @staticmethod
        def ValueOf(value: int) -> DraftingViewCollection.ViewCopyAnnotOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ViewCopyDetailOption(Enum):
        """
        Members Include: 
         |DetailView|  detail view
         |DuplicateView|  duplicate view
         |ModelView|  model view

        """
        DetailView: int
        DuplicateView: int
        ModelView: int
        @staticmethod
        def ValueOf(value: int) -> DraftingViewCollection.ViewCopyDetailOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ViewUpdateOption(Enum):
        """
        Members Include: 
         |All|  Updates all views in scope (part or drawing sheet).
         |OutOfDate|  Updates all out of date views in scope (part or drawing sheet).
         |OutOfDateAutomatic|  Updates all out of date automatic views in scope (part or drawing sheet).

        """
        All: int
        OutOfDate: int
        OutOfDateAutomatic: int
        @staticmethod
        def ValueOf(value: int) -> DraftingViewCollection.ViewUpdateOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def ConvertLegacyViewsToLightweight(self, views: List[DraftingView]) -> None:
        """
         Converts legacy views to lightweight.  The views in list can be spread
                    amongst multiple sheets, but they must all belong to the same part.
                
        """
        pass
    def CreateAddRemoveBoxViewBuilder(self, activeView: DraftingView) -> AddRemoveBoxViewBuilder:
        """
         Creates a NXOpen.Drawings.AddRemoveBoxViewBuilder 
         Returns builder ( AddRemoveBoxViewBuilder NXOpen.): .
        """
        pass
    def CreateBaseViewBuilder(self, view: BaseView) -> BaseViewBuilder:
        """
         Creates the Base View Builder 
         Returns builder ( BaseViewBuilder NXOpen.): .
        """
        pass
    def CreateBrokenViewBuilder(self, viewbreak: ViewBreak) -> BrokenViewBuilder:
        """
         Creates a NXOpen.Drawings.BrokenViewBuilder 
         Returns builder ( BrokenViewBuilder NXOpen.): .
        """
        pass
    def CreateCopyTo3dBuilder(self) -> ViewCopyTo3dBuilder:
        """
         Creates a NXOpen.Drawings.ViewCopyTo3dBuilder 
         Returns builder ( ViewCopyTo3dBuilder NXOpen.): .
        """
        pass
    def CreateCustomViewSettingsBuilder(self) -> CustomViewSettingsBuilder:
        """
         Creates a NXOpen.Drawings.CustomViewSettingsBuilder 
         Returns builder ( CustomViewSettingsBuilder NXOpen.): .
        """
        pass
    def CreateDetailViewBuilder(self, view: DetailView) -> DetailViewBuilder:
        """
         Creates a NXOpen.Drawings.DetailViewBuilder 
         Returns builder ( DetailViewBuilder NXOpen.): .
        """
        pass
    def CreateDrawingViewBuilder(self, drawingview: DrawingView) -> DrawingViewBuilder:
        """
         Creates a DrawingViewBuilder 
         Returns builder ( DrawingViewBuilder NXOpen.): .
        """
        pass
    def CreateProjectedViewBuilder(self, view: ProjectedView) -> ProjectedViewBuilder:
        """
         Creates the Projected View Builder 
         Returns builder ( ProjectedViewBuilder NXOpen.): .
        """
        pass
    def CreateRefineDisplayBuilder(self) -> RefineDisplayBuilder:
        """
         Creates a NXOpen.Drawings.RefineDisplayBuilder 
         Returns builder ( RefineDisplayBuilder NXOpen.): .
        """
        pass
    def CreateSecondaryGeometryInViewsBuilder(self) -> SecondaryGeometryInViewsBuilder:
        """
         Creates a NXOpen.Drawings.SecondaryGeometryInViewsBuilder 
         Returns builder ( SecondaryGeometryInViewsBuilder NXOpen.):  Returns the Secondary Geometry In Views builder .
        """
        pass
    def CreateSectionInViewBuilder(self) -> SectionInViewBuilder:
        """
         Creates the Section In View Builder 
         Returns builder ( SectionInViewBuilder NXOpen.): .
        """
        pass
    def CreateSectionViewBuilder(self, sectionViewOrSectionLine: NXOpen.NXObject) -> SectionViewBuilder:
        """
         Creates the Section View Builder 
         Returns builder ( SectionViewBuilder NXOpen.): .
        """
        pass
    def CreateShipbuildingLineBuilder(self) -> ViewStyleShipbuildingLinesBuilder:
        """
         Creates a NXOpen.Drawings.ViewStyleShipbuildingLinesBuilder 
         Returns style ( ViewStyleShipbuildingLinesBuilder NXOpen.):  Returns the empty Shipbuilding Lines sub-builder on View Style .
        """
        pass
    def CreateStandardViewsBuilder(self) -> StandardViewsBuilder:
        """
         Creates a StandardViewsBuilder 
         Returns builder ( StandardViewsBuilder NXOpen.): .
        """
        pass
    def CreateUpdateViewsBuilder(self) -> UpdateViewsBuilder:
        """
         Creates the Update Views Builder 
         Returns builder ( UpdateViewsBuilder NXOpen.): .
        """
        pass
    def CreateViewCreationWizardBuilder(self) -> ViewCreationWizardBuilder:
        """
         Creates a NXOpen.Drawings.ViewCreationWizardBuilder 
         Returns builder ( ViewCreationWizardBuilder NXOpen.): .
        """
        pass
    def CreateViewProjectionBuilder(self) -> ViewProjectionBuilder:
        """
         Creates a NXOpen.Drawings.ViewProjectionBuilder 
         Returns builder ( ViewProjectionBuilder NXOpen.): .
        """
        pass
    def DeleteViewsInOriginalPart(self, views: List[DraftingView]) -> None:
        """
         Deletes views in original part
        """
        pass
    def FindObject(self, journal_identifier: str) -> DraftingView:
        """
         Finds the  NXOpen.Drawings.DraftingView  with the given identifier as recorded in a journal.
                An object may not return the same value as its JournalIdentifier in different versions of
                the software. However newer versions of the software should find the same object when
                FindObject is passed older versions of its journal identifier. In general, this method
                should not be used in handwritten code and exists to support record and playback of journals.
                An exception will be thrown if no object can be found with the given journal identifier. 
         Returns found ( DraftingView NXOpen.):  View with this identifier .
        """
        pass
    def GetParentOfView(self, view: NXOpen.View) -> NXOpen.ModelingView:
        """
         Find the parent cut (sectioned) model view of a drawing member view.
                    If the parent view is not a cut model view,  is returned. 
         Returns parentView ( NXOpen.ModelingView): .
        """
        pass
    def MoveViewsToDrawing(self, views: List[DraftingView], drawing: DrawingSheet) -> None:
        """
         Move views to drawing
        """
        pass
    def PasteViews(self, drawing: DrawingSheet, views: List[DraftingView], detail_option: DraftingViewCollection.ViewCopyDetailOption, annot_option: DraftingViewCollection.ViewCopyAnnotOption) -> List[DraftingView]:
        """
         Paste views 
         Returns newViews ( DraftingView List[NXOpe): new views .
        """
        pass
    def RestoreViewBreaks(self, view: DraftingView) -> None:
        """
         Restore all view breaks of the view suppressed by Drawings.DraftingViewCollection.SuppressViewBreaks 
        """
        pass
    def SuppressViewBreaks(self, view: DraftingView) -> None:
        """
         Suppress all view breaks of the view. It is neccessary if we want change the view contents
        """
        pass
    def UpdateSheetsAndViews(self, inputViews: List[NXOpen.NXObject]) -> None:
        """
         Updates the drawing sheets and drafting views. The views in list can be spread
                amongst multiple sheets, but they must all belong to the same part.
                
        """
        pass
    def UpdateViewBreaks(self, view: DraftingView) -> None:
        """
         Log all view breaks of the view for update 
        """
        pass
    @overload
    def UpdateViews(self, update_option: DraftingViewCollection.ViewUpdateOption) -> None:
        """
         Updates drafting views in the part determined by an update option.
                    For example, to update all out of date views in a part, pass in
                    Drawings.DraftingViewCollection.ViewUpdateOption.OutOfDate.
                
        """
        pass
    @overload
    def UpdateViews(self, update_option: DraftingViewCollection.ViewUpdateOption, drawing: DrawingSheet) -> None:
        """
         Updates drafting views in a sheet determined by an update option.
                    For example, to update all out of date views on the sheet, pass in
                    Drawings.DraftingViewCollection.ViewUpdateOption.OutOfDate.
                
        """
        pass
    @overload
    def UpdateViews(self, views: List[DraftingView]) -> None:
        """
         Updates the drafting views.  The views in list can be spread
                    amongst multiple sheets, but they must all belong to the same part.
                
        """
        pass
import NXOpen
class DraftingView(NXOpen.View): 
    """ Represents a drafting view. """
    @property
    def IsActiveForSketching(self) -> bool:
        """
        Getter for property: (bool) IsActiveForSketching
         Returns true if this view is the active sketch view.  
              
         
        """
        pass
    @property
    def IsBroken(self) -> bool:
        """
        Getter for property: (bool) IsBroken
         Returns the status on whether this  NXOpen::Drawings::DraftingView  is broken.  
             
         
        """
        pass
    @property
    def IsDecoration(self) -> bool:
        """
        Getter for property: (bool) IsDecoration
         Returns the status on whether this  NXOpen::Drawings::DraftingView  is decoration.  
             
         
        """
        pass
    @property
    def IsOutOfDate(self) -> bool:
        """
        Getter for property: (bool) IsOutOfDate
         Returns the status on whether this  NXOpen::Drawings::DraftingView  is out of date.  
             
         
        """
        pass
    @property
    def IsSlave(self) -> bool:
        """
        Getter for property: (bool) IsSlave
         Returns the status on whether this  NXOpen::Drawings::DraftingView  is slave.  
             
         
        """
        pass
    @property
    def Style() -> ViewStyle:
        """
         Returns object to View Style 
        """
        pass
    @property
    def ViewBreaks() -> ViewBreakCollection:
        """
         Returns the ViewBreakCollection instance belonging to this view 
        """
        pass
    @property
    def DraftingBodies() -> DraftingBodyCollection:
        """
         Returns the DraftingBodyCollection 
        """
        pass
    def ActivateForSketching(self) -> None:
        """
         Sets this drafting view as the active sketch view. 
        """
        pass
    def CalculateMinMaxBox(self) -> Tuple[NXOpen.Point3d, NXOpen.Point3d]:
        """
         Returns the absolute min-max box that contains all the entities in the view. 
         Returns A tuple consisting of (minimumPoint, maximumPoint). 
         - minimumPoint is:  NXOpen.Point3d.
         - maximumPoint is:  NXOpen.Point3d.

        """
        pass
    def CheckForInvalidParentModelView(self) -> None:
        """
         Checks the view's validity by looking at the parent model view 
        """
        pass
    def Commit(self) -> None:
        """
         Commits and applies all the settings like NXOpen.Drawings.ViewStyle to the View.This must be called on the view after creation or edit to reflect all the settings on it
        """
        pass
    def GetBrokenViewDecoration(self) -> DraftingView:
        """
         Return the decoration view of a slave or a master view. If the view is a decoration view, return this view. return NULL for other type of view. 
         Returns decoration_view ( DraftingView NXOpen.):  .
        """
        pass
    def GetBrokenViewInternalViews(self) -> List[DraftingView]:
        """
         Returns an array of views representing the internal views of broken view. Other views return zero objects. 
         Returns views ( DraftingView List[NXOpe): .
        """
        pass
    def GetBrokenViewMaster(self) -> DraftingView:
        """
         Return the master view of a slave or a decoration view. return NULL for other type of view. 
         Returns master_view ( DraftingView NXOpen.):  .
        """
        pass
    def GetDraftingSketches(self) -> List[NXOpen.Sketch]:
        """
         Returns all drafting  NXOpen.Sketch es of the view. 
         Returns sketches ( NXOpen.Sketch Li):  .
        """
        pass
    def GetDrawingReferencePoint(self) -> NXOpen.Point3d:
        """
         Returns the view origin(location).
         Returns drawing_reference_point ( NXOpen.Point3d):  View origin(location) .
        """
        pass
    def GetToolMarkers(self) -> List[FlatPatternObject]:
        """
         Returns an array of pointers to objects representing the tool markers in the
                    view. Pertains to flat pattern views. Other views return zero objects. 
         Returns markers ( FlatPatternObject List[NXOpe): .
        """
        pass
    def HideComponents(self, components: List[NXOpen.NXObject]) -> None:
        """
         Hides the specified components in the view.
        """
        pass
    def HideViewBorder(self) -> None:
        """
         Hide the view border of the broken view. 
        """
        pass
    def MoveView(self, drawing_reference_point: NXOpen.Point3d) -> None:
        """
         Sets the view origin at the provided location. This method is quite similar 
                    NXOpen.Drawings.DraftingView.SetDrawingReferencePoint and 
                    handles section views and broken views cases also.
                
        """
        pass
    def RestoreViewBorder(self) -> None:
        """
         Restores the view border from the dashed line to the normal line for cut operation
        """
        pass
    def SetDeleteSectionLine(self, deleteSectionLine: bool) -> None:
        """
         Set the section line delete option, If false section line will not be deleted with section view 
        """
        pass
    def SetDrawingReferencePoint(self, drawing_reference_point: NXOpen.Point3d) -> None:
        """
         Sets the view origin at the provided location.
        """
        pass
    def ShowComponents(self, components: List[NXOpen.NXObject]) -> None:
        """
         Shows the specified components in the view.
        """
        pass
    def ShowViewBorder(self) -> None:
        """
         Show the view border of the broken view. 
        """
        pass
    def Update(self) -> None:
        """
         Updates the drawing member view on a drawing. The view update
                    process includes updating the view bounds, resectioning section views,
                    updating silhouettes, and updating hidden line display when
                    applicable.
                
        """
        pass
    @overload
    def UpdateAutomaticViewBound(self) -> None:
        """
         Recalculates and updates the view boundary of a drawing member view
        """
        pass
    @overload
    def UpdateAutomaticViewBound(self, updateDependent: bool) -> None:
        """
         Recalculates and updates the view boundary of a drawing member view 
                    and update the boundary dependent objects 
        """
        pass
import NXOpen
class DrawingCompareSettingsBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Drawings.DrawingCompareSettingsBuilder builder """
    class ChangeSymbolType(Enum):
        """
        Members Include: 
         |Circle| 
         |TriangleUp| 
         |TriangleDown| 
         |Square| 
         |Hexagon| 

        """
        Circle: int
        TriangleUp: int
        TriangleDown: int
        Square: int
        Hexagon: int
        @staticmethod
        def ValueOf(value: int) -> DrawingCompareSettingsBuilder.ChangeSymbolType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ComparisonBaseline(Enum):
        """
        Members Include: 
         |Snapshot| 
         |TrackedChanges| 

        """
        Snapshot: int
        TrackedChanges: int
        @staticmethod
        def ValueOf(value: int) -> DrawingCompareSettingsBuilder.ComparisonBaseline:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FontType(Enum):
        """
        Members Include: 
         |Solid| 
         |Dashed| 
         |Phantom| 
         |Centerline| 
         |Dotted| 
         |LongDash| 
         |DottedDash| 
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
        LongDash: int
        DottedDash: int
        Eight: int
        Nine: int
        Ten: int
        Eleven: int
        @staticmethod
        def ValueOf(value: int) -> DrawingCompareSettingsBuilder.FontType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class WidthType(Enum):
        """
        Members Include: 
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
        def ValueOf(value: int) -> DrawingCompareSettingsBuilder.WidthType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BaselineForComparison(self) -> DrawingCompareSettingsBuilder.ComparisonBaseline:
        """
        Getter for property: ( DrawingCompareSettingsBuilder.ComparisonBaseline NXOpen.) BaselineForComparison
         Returns the baseline for comparison   
            
         
        """
        pass
    @BaselineForComparison.setter
    def BaselineForComparison(self, baselineForComparison: DrawingCompareSettingsBuilder.ComparisonBaseline):
        """
        Setter for property: ( DrawingCompareSettingsBuilder.ComparisonBaseline NXOpen.) BaselineForComparison
         Returns the baseline for comparison   
            
         
        """
        pass
    @property
    def CenterlineCompare(self) -> bool:
        """
        Getter for property: (bool) CenterlineCompare
         Returns the centerline compare   
            
         
        """
        pass
    @CenterlineCompare.setter
    def CenterlineCompare(self, centerlineCompare: bool):
        """
        Setter for property: (bool) CenterlineCompare
         Returns the centerline compare   
            
         
        """
        pass
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) Color
         Returns the color   
            
         
        """
        pass
    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) Color
         Returns the color   
            
         
        """
        pass
    @property
    def CompareTolerance(self) -> float:
        """
        Getter for property: (float) CompareTolerance
         Returns the compare tolerance   
            
         
        """
        pass
    @CompareTolerance.setter
    def CompareTolerance(self, compareTolerance: float):
        """
        Setter for property: (float) CompareTolerance
         Returns the compare tolerance   
            
         
        """
        pass
    @property
    def CrosshatchAreaFillsCompare(self) -> bool:
        """
        Getter for property: (bool) CrosshatchAreaFillsCompare
         Returns the crosshatch area fills compare   
            
         
        """
        pass
    @CrosshatchAreaFillsCompare.setter
    def CrosshatchAreaFillsCompare(self, crosshatchAreaFillsCompare: bool):
        """
        Setter for property: (bool) CrosshatchAreaFillsCompare
         Returns the crosshatch area fills compare   
            
         
        """
        pass
    @property
    def DatumFeatureSymbolCompare(self) -> bool:
        """
        Getter for property: (bool) DatumFeatureSymbolCompare
         Returns the datum feature symbol compare   
            
         
        """
        pass
    @DatumFeatureSymbolCompare.setter
    def DatumFeatureSymbolCompare(self, datumFeatureSymbolCompare: bool):
        """
        Setter for property: (bool) DatumFeatureSymbolCompare
         Returns the datum feature symbol compare   
            
         
        """
        pass
    @property
    def DatumFeatureSymbolLeaderTerminatorCompare(self) -> bool:
        """
        Getter for property: (bool) DatumFeatureSymbolLeaderTerminatorCompare
         Returns the datum feature symbol leader info compare   
            
         
        """
        pass
    @DatumFeatureSymbolLeaderTerminatorCompare.setter
    def DatumFeatureSymbolLeaderTerminatorCompare(self, datumFeatureSymbolLeaderTerminatorCompare: bool):
        """
        Setter for property: (bool) DatumFeatureSymbolLeaderTerminatorCompare
         Returns the datum feature symbol leader info compare   
            
         
        """
        pass
    @property
    def DatumFeatureSymbolOriginCompare(self) -> bool:
        """
        Getter for property: (bool) DatumFeatureSymbolOriginCompare
         Returns the datum feature symbol origin compare   
            
         
        """
        pass
    @DatumFeatureSymbolOriginCompare.setter
    def DatumFeatureSymbolOriginCompare(self, datumFeatureSymbolOriginCompare: bool):
        """
        Setter for property: (bool) DatumFeatureSymbolOriginCompare
         Returns the datum feature symbol origin compare   
            
         
        """
        pass
    @property
    def DatumFeatureSymbolRetainedStatusCompare(self) -> bool:
        """
        Getter for property: (bool) DatumFeatureSymbolRetainedStatusCompare
         Returns the datum feature symbol retained status compare   
            
         
        """
        pass
    @DatumFeatureSymbolRetainedStatusCompare.setter
    def DatumFeatureSymbolRetainedStatusCompare(self, datumFeatureSymbolRetainedStatusCompare: bool):
        """
        Setter for property: (bool) DatumFeatureSymbolRetainedStatusCompare
         Returns the datum feature symbol retained status compare   
            
         
        """
        pass
    @property
    def DatumFeatureSymbolTextCompare(self) -> bool:
        """
        Getter for property: (bool) DatumFeatureSymbolTextCompare
         Returns the datum feature symbol text compare   
            
         
        """
        pass
    @DatumFeatureSymbolTextCompare.setter
    def DatumFeatureSymbolTextCompare(self, datumFeatureSymbolTextCompare: bool):
        """
        Setter for property: (bool) DatumFeatureSymbolTextCompare
         Returns the datum feature symbol text compare   
            
         
        """
        pass
    @property
    def DatumTargetCompare(self) -> bool:
        """
        Getter for property: (bool) DatumTargetCompare
         Returns the datum target compare   
            
         
        """
        pass
    @DatumTargetCompare.setter
    def DatumTargetCompare(self, datumTargetCompare: bool):
        """
        Setter for property: (bool) DatumTargetCompare
         Returns the datum target compare   
            
         
        """
        pass
    @property
    def DatumTargetLeaderTerminatorCompare(self) -> bool:
        """
        Getter for property: (bool) DatumTargetLeaderTerminatorCompare
         Returns the datum target leader info compare   
            
         
        """
        pass
    @DatumTargetLeaderTerminatorCompare.setter
    def DatumTargetLeaderTerminatorCompare(self, datumTargetLeaderTerminatorCompare: bool):
        """
        Setter for property: (bool) DatumTargetLeaderTerminatorCompare
         Returns the datum target leader info compare   
            
         
        """
        pass
    @property
    def DatumTargetOriginCompare(self) -> bool:
        """
        Getter for property: (bool) DatumTargetOriginCompare
         Returns the datum target origin compare   
            
         
        """
        pass
    @DatumTargetOriginCompare.setter
    def DatumTargetOriginCompare(self, datumTargetOriginCompare: bool):
        """
        Setter for property: (bool) DatumTargetOriginCompare
         Returns the datum target origin compare   
            
         
        """
        pass
    @property
    def DatumTargetRetainedStatusCompare(self) -> bool:
        """
        Getter for property: (bool) DatumTargetRetainedStatusCompare
         Returns the datum target retained status compare   
            
         
        """
        pass
    @DatumTargetRetainedStatusCompare.setter
    def DatumTargetRetainedStatusCompare(self, datumTargetRetainedStatusCompare: bool):
        """
        Setter for property: (bool) DatumTargetRetainedStatusCompare
         Returns the datum target retained status compare   
            
         
        """
        pass
    @property
    def DatumTargetTextCompare(self) -> bool:
        """
        Getter for property: (bool) DatumTargetTextCompare
         Returns the datum target text compare   
            
         
        """
        pass
    @DatumTargetTextCompare.setter
    def DatumTargetTextCompare(self, datumTargetTextCompare: bool):
        """
        Setter for property: (bool) DatumTargetTextCompare
         Returns the datum target text compare   
            
         
        """
        pass
    @property
    def DimCompare(self) -> bool:
        """
        Getter for property: (bool) DimCompare
         Returns the dim compare   
            
         
        """
        pass
    @DimCompare.setter
    def DimCompare(self, dimCompare: bool):
        """
        Setter for property: (bool) DimCompare
         Returns the dim compare   
            
         
        """
        pass
    @property
    def DimOriginCompare(self) -> bool:
        """
        Getter for property: (bool) DimOriginCompare
         Returns the dim origin compare   
            
         
        """
        pass
    @DimOriginCompare.setter
    def DimOriginCompare(self, dimOriginCompare: bool):
        """
        Setter for property: (bool) DimOriginCompare
         Returns the dim origin compare   
            
         
        """
        pass
    @property
    def DimRetainedStatusCompare(self) -> bool:
        """
        Getter for property: (bool) DimRetainedStatusCompare
         Returns the dim retained status compare   
            
         
        """
        pass
    @DimRetainedStatusCompare.setter
    def DimRetainedStatusCompare(self, dimRetainedStatusCompare: bool):
        """
        Setter for property: (bool) DimRetainedStatusCompare
         Returns the dim retained status compare   
            
         
        """
        pass
    @property
    def DimSizeCompare(self) -> bool:
        """
        Getter for property: (bool) DimSizeCompare
         Returns the dim size compare   
            
         
        """
        pass
    @DimSizeCompare.setter
    def DimSizeCompare(self, dimSizeCompare: bool):
        """
        Setter for property: (bool) DimSizeCompare
         Returns the dim size compare   
            
         
        """
        pass
    @property
    def DisplayChangeSymbol(self) -> bool:
        """
        Getter for property: (bool) DisplayChangeSymbol
         Returns the display change symbol   
            
         
        """
        pass
    @DisplayChangeSymbol.setter
    def DisplayChangeSymbol(self, displayChangeSymbol: bool):
        """
        Setter for property: (bool) DisplayChangeSymbol
         Returns the display change symbol   
            
         
        """
        pass
    @property
    def FcfCompare(self) -> bool:
        """
        Getter for property: (bool) FcfCompare
         Returns the fcf compare   
            
         
        """
        pass
    @FcfCompare.setter
    def FcfCompare(self, fcfCompare: bool):
        """
        Setter for property: (bool) FcfCompare
         Returns the fcf compare   
            
         
        """
        pass
    @property
    def FcfLeaderTerminatorCompare(self) -> bool:
        """
        Getter for property: (bool) FcfLeaderTerminatorCompare
         Returns the fcf leader info compare   
            
         
        """
        pass
    @FcfLeaderTerminatorCompare.setter
    def FcfLeaderTerminatorCompare(self, fcfLeaderTerminatorCompare: bool):
        """
        Setter for property: (bool) FcfLeaderTerminatorCompare
         Returns the fcf leader info compare   
            
         
        """
        pass
    @property
    def FcfOriginCompare(self) -> bool:
        """
        Getter for property: (bool) FcfOriginCompare
         Returns the fcf origin compare   
            
         
        """
        pass
    @FcfOriginCompare.setter
    def FcfOriginCompare(self, fcfOriginCompare: bool):
        """
        Setter for property: (bool) FcfOriginCompare
         Returns the fcf origin compare   
            
         
        """
        pass
    @property
    def FcfRetainedStatusCompare(self) -> bool:
        """
        Getter for property: (bool) FcfRetainedStatusCompare
         Returns the fcf retained status compare   
            
         
        """
        pass
    @FcfRetainedStatusCompare.setter
    def FcfRetainedStatusCompare(self, fcfRetainedStatusCompare: bool):
        """
        Setter for property: (bool) FcfRetainedStatusCompare
         Returns the fcf retained status compare   
            
         
        """
        pass
    @property
    def FcfTextCompare(self) -> bool:
        """
        Getter for property: (bool) FcfTextCompare
         Returns the fcf text compare   
            
         
        """
        pass
    @FcfTextCompare.setter
    def FcfTextCompare(self, fcfTextCompare: bool):
        """
        Setter for property: (bool) FcfTextCompare
         Returns the fcf text compare   
            
         
        """
        pass
    @property
    def NoteCompare(self) -> bool:
        """
        Getter for property: (bool) NoteCompare
         Returns the note compare   
            
         
        """
        pass
    @NoteCompare.setter
    def NoteCompare(self, noteCompare: bool):
        """
        Setter for property: (bool) NoteCompare
         Returns the note compare   
            
         
        """
        pass
    @property
    def NoteLeaderTerminatorCompare(self) -> bool:
        """
        Getter for property: (bool) NoteLeaderTerminatorCompare
         Returns the note leader info compare   
            
         
        """
        pass
    @NoteLeaderTerminatorCompare.setter
    def NoteLeaderTerminatorCompare(self, noteLeaderTerminatorCompare: bool):
        """
        Setter for property: (bool) NoteLeaderTerminatorCompare
         Returns the note leader info compare   
            
         
        """
        pass
    @property
    def NoteOriginCompare(self) -> bool:
        """
        Getter for property: (bool) NoteOriginCompare
         Returns the note origin compare   
            
         
        """
        pass
    @NoteOriginCompare.setter
    def NoteOriginCompare(self, noteOriginCompare: bool):
        """
        Setter for property: (bool) NoteOriginCompare
         Returns the note origin compare   
            
         
        """
        pass
    @property
    def NoteRetainedStatusCompare(self) -> bool:
        """
        Getter for property: (bool) NoteRetainedStatusCompare
         Returns the note retained status compare   
            
         
        """
        pass
    @NoteRetainedStatusCompare.setter
    def NoteRetainedStatusCompare(self, noteRetainedStatusCompare: bool):
        """
        Setter for property: (bool) NoteRetainedStatusCompare
         Returns the note retained status compare   
            
         
        """
        pass
    @property
    def NoteTextCompare(self) -> bool:
        """
        Getter for property: (bool) NoteTextCompare
         Returns the note text compare   
            
         
        """
        pass
    @NoteTextCompare.setter
    def NoteTextCompare(self, noteTextCompare: bool):
        """
        Setter for property: (bool) NoteTextCompare
         Returns the note text compare   
            
         
        """
        pass
    @property
    def PartListCompare(self) -> bool:
        """
        Getter for property: (bool) PartListCompare
         Returns the part list compare   
            
         
        """
        pass
    @PartListCompare.setter
    def PartListCompare(self, partListCompare: bool):
        """
        Setter for property: (bool) PartListCompare
         Returns the part list compare   
            
         
        """
        pass
    @property
    def RestartNumbers(self) -> bool:
        """
        Getter for property: (bool) RestartNumbers
         Returns the restart numbers   
            
         
        """
        pass
    @RestartNumbers.setter
    def RestartNumbers(self, restartNumbers: bool):
        """
        Setter for property: (bool) RestartNumbers
         Returns the restart numbers   
            
         
        """
        pass
    @property
    def SheetCompare(self) -> bool:
        """
        Getter for property: (bool) SheetCompare
         Returns the sheet compare   
            
         
        """
        pass
    @SheetCompare.setter
    def SheetCompare(self, sheetCompare: bool):
        """
        Setter for property: (bool) SheetCompare
         Returns the sheet compare   
            
         
        """
        pass
    @property
    def SymbolCompare(self) -> bool:
        """
        Getter for property: (bool) SymbolCompare
         Returns the symbol compare   
            
         
        """
        pass
    @SymbolCompare.setter
    def SymbolCompare(self, symbolCompare: bool):
        """
        Setter for property: (bool) SymbolCompare
         Returns the symbol compare   
            
         
        """
        pass
    @property
    def SymbolFont(self) -> DrawingCompareSettingsBuilder.FontType:
        """
        Getter for property: ( DrawingCompareSettingsBuilder.FontType NXOpen.) SymbolFont
         Returns the symbol font   
            
         
        """
        pass
    @SymbolFont.setter
    def SymbolFont(self, symbolFont: DrawingCompareSettingsBuilder.FontType):
        """
        Setter for property: ( DrawingCompareSettingsBuilder.FontType NXOpen.) SymbolFont
         Returns the symbol font   
            
         
        """
        pass
    @property
    def SymbolLeaderTerminatorCompare(self) -> bool:
        """
        Getter for property: (bool) SymbolLeaderTerminatorCompare
         Returns the symbol leader info compare   
            
         
        """
        pass
    @SymbolLeaderTerminatorCompare.setter
    def SymbolLeaderTerminatorCompare(self, symbolLeaderTerminatorCompare: bool):
        """
        Setter for property: (bool) SymbolLeaderTerminatorCompare
         Returns the symbol leader info compare   
            
         
        """
        pass
    @property
    def SymbolOriginCompare(self) -> bool:
        """
        Getter for property: (bool) SymbolOriginCompare
         Returns the symbol origin compare   
            
         
        """
        pass
    @SymbolOriginCompare.setter
    def SymbolOriginCompare(self, symbolOriginCompare: bool):
        """
        Setter for property: (bool) SymbolOriginCompare
         Returns the symbol origin compare   
            
         
        """
        pass
    @property
    def SymbolRetainedStatusCompare(self) -> bool:
        """
        Getter for property: (bool) SymbolRetainedStatusCompare
         Returns the symbol retained status compare   
            
         
        """
        pass
    @SymbolRetainedStatusCompare.setter
    def SymbolRetainedStatusCompare(self, symbolRetainedStatusCompare: bool):
        """
        Setter for property: (bool) SymbolRetainedStatusCompare
         Returns the symbol retained status compare   
            
         
        """
        pass
    @property
    def SymbolSize(self) -> float:
        """
        Getter for property: (float) SymbolSize
         Returns the symbol size   
            
         
        """
        pass
    @SymbolSize.setter
    def SymbolSize(self, symbolSize: float):
        """
        Setter for property: (float) SymbolSize
         Returns the symbol size   
            
         
        """
        pass
    @property
    def SymbolTextCompare(self) -> bool:
        """
        Getter for property: (bool) SymbolTextCompare
         Returns the symbol text compare   
            
         
        """
        pass
    @SymbolTextCompare.setter
    def SymbolTextCompare(self, symbolTextCompare: bool):
        """
        Setter for property: (bool) SymbolTextCompare
         Returns the symbol text compare   
            
         
        """
        pass
    @property
    def SymbolType(self) -> DrawingCompareSettingsBuilder.ChangeSymbolType:
        """
        Getter for property: ( DrawingCompareSettingsBuilder.ChangeSymbolType NXOpen.) SymbolType
         Returns the symbol type   
            
         
        """
        pass
    @SymbolType.setter
    def SymbolType(self, symbolType: DrawingCompareSettingsBuilder.ChangeSymbolType):
        """
        Setter for property: ( DrawingCompareSettingsBuilder.ChangeSymbolType NXOpen.) SymbolType
         Returns the symbol type   
            
         
        """
        pass
    @property
    def SymbolWidth(self) -> DrawingCompareSettingsBuilder.WidthType:
        """
        Getter for property: ( DrawingCompareSettingsBuilder.WidthType NXOpen.) SymbolWidth
         Returns the symbol width   
            
         
        """
        pass
    @SymbolWidth.setter
    def SymbolWidth(self, symbolWidth: DrawingCompareSettingsBuilder.WidthType):
        """
        Setter for property: ( DrawingCompareSettingsBuilder.WidthType NXOpen.) SymbolWidth
         Returns the symbol width   
            
         
        """
        pass
    @property
    def TableCompare(self) -> bool:
        """
        Getter for property: (bool) TableCompare
         Returns the table compare   
            
         
        """
        pass
    @TableCompare.setter
    def TableCompare(self, tableCompare: bool):
        """
        Setter for property: (bool) TableCompare
         Returns the table compare   
            
         
        """
        pass
    @property
    def ViewCompare(self) -> bool:
        """
        Getter for property: (bool) ViewCompare
         Returns the view compare   
            
         
        """
        pass
    @ViewCompare.setter
    def ViewCompare(self, viewCompare: bool):
        """
        Setter for property: (bool) ViewCompare
         Returns the view compare   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class DrawingFormatSheetBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.Drawings.DrawingFormatSheetBuilder
    """
    @property
    def InitialSecondarySheetNumber(self) -> str:
        """
        Getter for property: (str) InitialSecondarySheetNumber
         Returns the initial secondary sheet number   
            
         
        """
        pass
    @InitialSecondarySheetNumber.setter
    def InitialSecondarySheetNumber(self, initialSecondarySheetNumber: str):
        """
        Setter for property: (str) InitialSecondarySheetNumber
         Returns the initial secondary sheet number   
            
         
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
    def SecondaryNumberDelimiter(self) -> str:
        """
        Getter for property: (str) SecondaryNumberDelimiter
         Returns the secondary number delimiter   
            
         
        """
        pass
    @SecondaryNumberDelimiter.setter
    def SecondaryNumberDelimiter(self, secondaryNumberDelimiter: str):
        """
        Setter for property: (str) SecondaryNumberDelimiter
         Returns the secondary number delimiter   
            
         
        """
        pass
import NXOpen
class DrawingRegionBuilder(NXOpen.Builder): 
    """ Represents a Drawing Region Builder """
    class ContentToMove(Enum):
        """
        Members Include: 
         |All| 
         |OnlyOverlapping| 

        """
        All: int
        OnlyOverlapping: int
        @staticmethod
        def ValueOf(value: int) -> DrawingRegionBuilder.ContentToMove:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RegionContinuation(Enum):
        """
        Members Include: 
         |NotSet| 
         |NewSheet| 
         |NextRegion| 
         |NewSheetRight| 
         |NewSheetLeft| 
         |NewSheetUp| 
         |NewSheetDown| 

        """
        NotSet: int
        NewSheet: int
        NextRegion: int
        NewSheetRight: int
        NewSheetLeft: int
        NewSheetUp: int
        NewSheetDown: int
        @staticmethod
        def ValueOf(value: int) -> DrawingRegionBuilder.RegionContinuation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RegionDraftingObjectType(Enum):
        """
        Members Include: 
         |View| 
         |Table| 
         |Annotation| 
         |Symbol| 
         |Blank| 
         |NotSet| 

        """
        View: int
        Table: int
        Annotation: int
        Symbol: int
        Blank: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> DrawingRegionBuilder.RegionDraftingObjectType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RegionGrowthDirection(Enum):
        """
        Members Include: 
         |RightfromTopLeft| 
         |RightfromBottomLeft| 
         |LeftfromTopRight| 
         |LeftfromBottomRight| 
         |DownfromTopLeft| 
         |DownfromTopRight| 
         |UpfromBottomLeft| 
         |UpfromBottomRight| 
         |NotSet| 

        """
        RightfromTopLeft: int
        RightfromBottomLeft: int
        LeftfromTopRight: int
        LeftfromBottomRight: int
        DownfromTopLeft: int
        DownfromTopRight: int
        UpfromBottomLeft: int
        UpfromBottomRight: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> DrawingRegionBuilder.RegionGrowthDirection:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RegionHorizontalGrowthDirection(Enum):
        """
        Members Include: 
         |Left| 
         |Right| 

        """
        Left: int
        Right: int
        @staticmethod
        def ValueOf(value: int) -> DrawingRegionBuilder.RegionHorizontalGrowthDirection:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RegionVerticalGrowthDirection(Enum):
        """
        Members Include: 
         |Up| 
         |Down| 

        """
        Up: int
        Down: int
        @staticmethod
        def ValueOf(value: int) -> DrawingRegionBuilder.RegionVerticalGrowthDirection:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DrawingRegionRulesBuilder(self) -> DrawingRegionRulesBuilder:
        """
        Getter for property: ( DrawingRegionRulesBuilder NXOpen.) DrawingRegionRulesBuilder
         Returns the DrawingRegionRules builder   
            
         
        """
        pass
    @property
    def Gap(self) -> float:
        """
        Getter for property: (float) Gap
         Returns the gap   
            
         
        """
        pass
    @Gap.setter
    def Gap(self, gap: float):
        """
        Setter for property: (float) Gap
         Returns the gap   
            
         
        """
        pass
    @property
    def GrowthDirection(self) -> DrawingRegionBuilder.RegionGrowthDirection:
        """
        Getter for property: ( DrawingRegionBuilder.RegionGrowthDirection NXOpen.) GrowthDirection
         Returns the  growth direction (this is for  NXOpen::Annotations::CustomSymbol  and  NXOpen::Annotations::Note )   
            
         
        """
        pass
    @GrowthDirection.setter
    def GrowthDirection(self, growthDirection: DrawingRegionBuilder.RegionGrowthDirection):
        """
        Setter for property: ( DrawingRegionBuilder.RegionGrowthDirection NXOpen.) GrowthDirection
         Returns the  growth direction (this is for  NXOpen::Annotations::CustomSymbol  and  NXOpen::Annotations::Note )   
            
         
        """
        pass
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Height
         Returns the height   
            
         
        """
        pass
    @property
    def HorizontalGrowthDirection(self) -> DrawingRegionBuilder.RegionHorizontalGrowthDirection:
        """
        Getter for property: ( DrawingRegionBuilder.RegionHorizontalGrowthDirection NXOpen.) HorizontalGrowthDirection
         Returns the horizantal growth direction   
            
         
        """
        pass
    @HorizontalGrowthDirection.setter
    def HorizontalGrowthDirection(self, horizontalGrowthDirection: DrawingRegionBuilder.RegionHorizontalGrowthDirection):
        """
        Setter for property: ( DrawingRegionBuilder.RegionHorizontalGrowthDirection NXOpen.) HorizontalGrowthDirection
         Returns the horizantal growth direction   
            
         
        """
        pass
    @property
    def Length(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Length
         Returns the length   
            
         
        """
        pass
    @property
    def MoveContent(self) -> DrawingRegionBuilder.ContentToMove:
        """
        Getter for property: ( DrawingRegionBuilder.ContentToMove NXOpen.) MoveContent
         Returns the move content   
            
         
        """
        pass
    @MoveContent.setter
    def MoveContent(self, moveContent: DrawingRegionBuilder.ContentToMove):
        """
        Setter for property: ( DrawingRegionBuilder.ContentToMove NXOpen.) MoveContent
         Returns the move content   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    @property
    def ObjectType(self) -> DrawingRegionBuilder.RegionDraftingObjectType:
        """
        Getter for property: ( DrawingRegionBuilder.RegionDraftingObjectType NXOpen.) ObjectType
         Returns the type   
            
         
        """
        pass
    @ObjectType.setter
    def ObjectType(self, type: DrawingRegionBuilder.RegionDraftingObjectType):
        """
        Setter for property: ( DrawingRegionBuilder.RegionDraftingObjectType NXOpen.) ObjectType
         Returns the type   
            
         
        """
        pass
    @property
    def Origin(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Origin
         Returns the origin   
            
         
        """
        pass
    @Origin.setter
    def Origin(self, origin: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Origin
         Returns the origin   
            
         
        """
        pass
    @property
    def Priority(self) -> int:
        """
        Getter for property: (int) Priority
         Returns the priority   
            
         
        """
        pass
    @Priority.setter
    def Priority(self, priority: int):
        """
        Setter for property: (int) Priority
         Returns the priority   
            
         
        """
        pass
    @property
    def SpecifyContinuation(self) -> DrawingRegionBuilder.RegionContinuation:
        """
        Getter for property: ( DrawingRegionBuilder.RegionContinuation NXOpen.) SpecifyContinuation
         Returns the continuation   
            
         
        """
        pass
    @SpecifyContinuation.setter
    def SpecifyContinuation(self, specifyContinuation: DrawingRegionBuilder.RegionContinuation):
        """
        Setter for property: ( DrawingRegionBuilder.RegionContinuation NXOpen.) SpecifyContinuation
         Returns the continuation   
            
         
        """
        pass
    @property
    def VerticalGrowthDirection(self) -> DrawingRegionBuilder.RegionVerticalGrowthDirection:
        """
        Getter for property: ( DrawingRegionBuilder.RegionVerticalGrowthDirection NXOpen.) VerticalGrowthDirection
         Returns  the  vertical growth direction   
            
         
        """
        pass
    @VerticalGrowthDirection.setter
    def VerticalGrowthDirection(self, verticalGrowthDirection: DrawingRegionBuilder.RegionVerticalGrowthDirection):
        """
        Setter for property: ( DrawingRegionBuilder.RegionVerticalGrowthDirection NXOpen.) VerticalGrowthDirection
         Returns  the  vertical growth direction   
            
         
        """
        pass
    def SetNextLinkedRegion(self, nextLinkedRegion: DrawingRegion) -> None:
        """
         Set the next linked regions 
        """
        pass
import NXOpen
class DrawingRegionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of drawing regions """
    def CreateAddObjectsToRegionBuilder(self) -> AddObjectsToRegionBuilder:
        """
         Creates add objects to region builder 
         Returns builder ( AddObjectsToRegionBuilder NXOpen.): .
        """
        pass
    def CreateDrawingRegionBuilder(self, objectValue: DrawingRegion) -> DrawingRegionBuilder:
        """
         Creates the DrawingRegion builder 
         Returns builder ( DrawingRegionBuilder NXOpen.): .
        """
        pass
    def CreateRemoveObjectsBuilder(self) -> RemoveObjectsBuilder:
        """
         Creates remove objects builder 
         Returns builder ( RemoveObjectsBuilder NXOpen.): .
        """
        pass
    def CreateSelectRegionBuilder(self) -> SelectRegionBuilder:
        """
         Creates select region builder 
         Returns builder ( SelectRegionBuilder NXOpen.): .
        """
        pass
    def FindObject(self, name: str) -> DrawingRegion:
        """
          Finds the  NXOpen.Drawings.DrawingRegion  with the given name. 
                An exception will be thrown if no object can be found with the given name. 
         Returns drawingRegion ( DrawingRegion NXOpen.):   Drawing Region object .
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class DrawingRegionRulesBuilder(NXOpen.TaggedObject): 
    """ Represents a Drawing region rules builder """
    def GetRules(self) -> List[str]:
        """
         Get Rules 
         Returns rule (List[str]): .
        """
        pass
    def RemoveRules(self, rules: List[str]) -> None:
        """
         Remove Rules 
        """
        pass
    def SetRules(self, rules: List[str]) -> None:
        """
         Set Rules 
        """
        pass
import NXOpen
class DrawingRegion(NXOpen.DisplayableObject): 
    """ Represents a Drawing Region """
    pass
import NXOpen
class DrawingSheetBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Drawings.DrawingSheetBuilder
    """
    class SheetBaseordrawingView(Enum):
        """
        Members Include: 
         |Base|  auto start base view 
         |Drawing|  auto start drawing view 

        """
        Base: int
        Drawing: int
        @staticmethod
        def ValueOf(value: int) -> DrawingSheetBuilder.SheetBaseordrawingView:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SheetMode(Enum):
        """
        Members Include: 
         |Create|  create mode 
         |Edit|  edit mode 

        """
        Create: int
        Edit: int
        @staticmethod
        def ValueOf(value: int) -> DrawingSheetBuilder.SheetMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SheetOption(Enum):
        """
        Members Include: 
         |UseTemplate|  a drawing sheet template 
         |StandardSize|  a standard size drawing sheet 
         |CustomSize|  a custom size drawing sheet 

        """
        UseTemplate: int
        StandardSize: int
        CustomSize: int
        @staticmethod
        def ValueOf(value: int) -> DrawingSheetBuilder.SheetOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SheetProjectionAngle(Enum):
        """
        Members Include: 
         |First|  first angle projection 
         |Third|  third angle projection 

        """
        First: int
        Third: int
        @staticmethod
        def ValueOf(value: int) -> DrawingSheetBuilder.SheetProjectionAngle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SheetStandardEnglishScale(Enum):
        """
        Members Include: 
         |S81|  a scale of 8:1 
         |S41|  a scale of 4:1 
         |S21|  a scale of 2:1 
         |S11|  a scale of 1:1 
         |S12|  a scale of 1:2 
         |S14|  a scale of 1:4 
         |S18|  a scale of 1:8 
         |Custom|  a custom scale 

        """
        S81: int
        S41: int
        S21: int
        S11: int
        S12: int
        S14: int
        S18: int
        Custom: int
        @staticmethod
        def ValueOf(value: int) -> DrawingSheetBuilder.SheetStandardEnglishScale:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SheetStandardMetricScale(Enum):
        """
        Members Include: 
         |S501|  a scale of 50:1 
         |S201|  a scale of 20:1 
         |S101|  a scale of 10:1 
         |S51|  a scale of 5:1 
         |S21|  a scale of 2:1 
         |S11|  a scale of 1:1 
         |S12|  a scale of 1:2 
         |S15|  a scale of 1:5 
         |S110|  a scale of 1:10 
         |S120|  a scale of 1:20 
         |S150|  a scale of 1:50 
         |S1100|  a scale of 1:100 
         |Custom|  a custom scale 

        """
        S501: int
        S201: int
        S101: int
        S51: int
        S21: int
        S11: int
        S12: int
        S15: int
        S110: int
        S120: int
        S150: int
        S1100: int
        Custom: int
        @staticmethod
        def ValueOf(value: int) -> DrawingSheetBuilder.SheetStandardMetricScale:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SheetUnits(Enum):
        """
        Members Include: 
         |Metric|  a Metric units drawing sheet 
         |English|  an English units drawing sheet 

        """
        Metric: int
        English: int
        @staticmethod
        def ValueOf(value: int) -> DrawingSheetBuilder.SheetUnits:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AutoStartBaseView(self) -> bool:
        """
        Getter for property: (bool) AutoStartBaseView
         Returns the setting that controls whether or not the Add Base View command is automatically 
                    started after inserting a sheet that has no views on it.  
          
                    This option does not appear for Edit Sheet. 
                    the toggle is changed to be auto start view creation in Nx7.0, obsolete.
                  
         
        """
        pass
    @AutoStartBaseView.setter
    def AutoStartBaseView(self, auto_start_base_view: bool):
        """
        Setter for property: (bool) AutoStartBaseView
         Returns the setting that controls whether or not the Add Base View command is automatically 
                    started after inserting a sheet that has no views on it.  
          
                    This option does not appear for Edit Sheet. 
                    the toggle is changed to be auto start view creation in Nx7.0, obsolete.
                  
         
        """
        pass
    @property
    def AutoStartViewCreation(self) -> bool:
        """
        Getter for property: (bool) AutoStartViewCreation
         Returns the setting that controls whether or not the Add View creation is automatically 
                    started after inserting a sheet that has no views on it.  
          
                    This option does not appear for Edit Sheet.             
                  
         
        """
        pass
    @AutoStartViewCreation.setter
    def AutoStartViewCreation(self, auto_start_view_creation: bool):
        """
        Setter for property: (bool) AutoStartViewCreation
         Returns the setting that controls whether or not the Add View creation is automatically 
                    started after inserting a sheet that has no views on it.  
          
                    This option does not appear for Edit Sheet.             
                  
         
        """
        pass
    @property
    def BaseordrawingView(self) -> DrawingSheetBuilder.SheetBaseordrawingView:
        """
        Getter for property: ( DrawingSheetBuilder.SheetBaseordrawingView NXOpen.) BaseordrawingView
         Returns the option of base view or drawing view   
            
         
        """
        pass
    @BaseordrawingView.setter
    def BaseordrawingView(self, option: DrawingSheetBuilder.SheetBaseordrawingView):
        """
        Setter for property: ( DrawingSheetBuilder.SheetBaseordrawingView NXOpen.) BaseordrawingView
         Returns the option of base view or drawing view   
            
         
        """
        pass
    @property
    def EnglishSheetTemplateLocation(self) -> str:
        """
        Getter for property: (str) EnglishSheetTemplateLocation
         Returns the location of the english drawing sheet template to be added to the part file   
            
         
        """
        pass
    @EnglishSheetTemplateLocation.setter
    def EnglishSheetTemplateLocation(self, englishSheetTemplatelocation: str):
        """
        Setter for property: (str) EnglishSheetTemplateLocation
         Returns the location of the english drawing sheet template to be added to the part file   
            
         
        """
        pass
    @property
    def Height(self) -> float:
        """
        Getter for property: (float) Height
         Returns the custom or standard height for the drawing sheet   
            
         
        """
        pass
    @Height.setter
    def Height(self, height: float):
        """
        Setter for property: (float) Height
         Returns the custom or standard height for the drawing sheet   
            
         
        """
        pass
    @property
    def Length(self) -> float:
        """
        Getter for property: (float) Length
         Returns the custom or standard length to be used for the drawing to be created or edited.  
             
         
        """
        pass
    @Length.setter
    def Length(self, custom_length: float):
        """
        Setter for property: (float) Length
         Returns the custom or standard length to be used for the drawing to be created or edited.  
             
         
        """
        pass
    @property
    def MetricSheetTemplateLocation(self) -> str:
        """
        Getter for property: (str) MetricSheetTemplateLocation
         Returns the location of the metric drawing sheet template to be added to the part file   
            
         
        """
        pass
    @MetricSheetTemplateLocation.setter
    def MetricSheetTemplateLocation(self, metricSheetTemplateLocation: str):
        """
        Setter for property: (str) MetricSheetTemplateLocation
         Returns the location of the metric drawing sheet template to be added to the part file   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of the drawing sheet to be created or edited   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name of the drawing sheet to be created or edited   
            
         
        """
        pass
    @property
    def Number(self) -> str:
        """
        Getter for property: (str) Number
         Returns the number of the drawing sheet to be created or edited   
            
         
        """
        pass
    @Number.setter
    def Number(self, number: str):
        """
        Setter for property: (str) Number
         Returns the number of the drawing sheet to be created or edited   
            
         
        """
        pass
    @property
    def Option(self) -> DrawingSheetBuilder.SheetOption:
        """
        Getter for property: ( DrawingSheetBuilder.SheetOption NXOpen.) Option
         Returns the option to be used to create the drawing sheet   
            
         
        """
        pass
    @Option.setter
    def Option(self, option: DrawingSheetBuilder.SheetOption):
        """
        Setter for property: ( DrawingSheetBuilder.SheetOption NXOpen.) Option
         Returns the option to be used to create the drawing sheet   
            
         
        """
        pass
    @property
    def ProjectionAngle(self) -> DrawingSheetBuilder.SheetProjectionAngle:
        """
        Getter for property: ( DrawingSheetBuilder.SheetProjectionAngle NXOpen.) ProjectionAngle
         Returns the projection_angle option   
            
         
        """
        pass
    @ProjectionAngle.setter
    def ProjectionAngle(self, projection_angle: DrawingSheetBuilder.SheetProjectionAngle):
        """
        Setter for property: ( DrawingSheetBuilder.SheetProjectionAngle NXOpen.) ProjectionAngle
         Returns the projection_angle option   
            
         
        """
        pass
    @property
    def Revision(self) -> str:
        """
        Getter for property: (str) Revision
         Returns the revision of the drawing sheet to be created or edited   
            
         
        """
        pass
    @Revision.setter
    def Revision(self, revision: str):
        """
        Setter for property: (str) Revision
         Returns the revision of the drawing sheet to be created or edited   
            
         
        """
        pass
    @property
    def ScaleDenominator(self) -> float:
        """
        Getter for property: (float) ScaleDenominator
         Returns the denominator of a custom scale   
            
         
        """
        pass
    @ScaleDenominator.setter
    def ScaleDenominator(self, scale_denominator: float):
        """
        Setter for property: (float) ScaleDenominator
         Returns the denominator of a custom scale   
            
         
        """
        pass
    @property
    def ScaleNumerator(self) -> float:
        """
        Getter for property: (float) ScaleNumerator
         Returns the numerator of a custom scale   
            
         
        """
        pass
    @ScaleNumerator.setter
    def ScaleNumerator(self, scale_numerator: float):
        """
        Setter for property: (float) ScaleNumerator
         Returns the numerator of a custom scale   
            
         
        """
        pass
    @property
    def SecondaryNumber(self) -> str:
        """
        Getter for property: (str) SecondaryNumber
         Returns the secondary number of the drawing sheet to be created or edited   
            
         
        """
        pass
    @SecondaryNumber.setter
    def SecondaryNumber(self, secondaryNumber: str):
        """
        Setter for property: (str) SecondaryNumber
         Returns the secondary number of the drawing sheet to be created or edited   
            
         
        """
        pass
    @property
    def StandardEnglishScale(self) -> DrawingSheetBuilder.SheetStandardEnglishScale:
        """
        Getter for property: ( DrawingSheetBuilder.SheetStandardEnglishScale NXOpen.) StandardEnglishScale
         Returns the standard English drawing scale   
            
         
        """
        pass
    @StandardEnglishScale.setter
    def StandardEnglishScale(self, english_scale: DrawingSheetBuilder.SheetStandardEnglishScale):
        """
        Setter for property: ( DrawingSheetBuilder.SheetStandardEnglishScale NXOpen.) StandardEnglishScale
         Returns the standard English drawing scale   
            
         
        """
        pass
    @property
    def StandardMetricScale(self) -> DrawingSheetBuilder.SheetStandardMetricScale:
        """
        Getter for property: ( DrawingSheetBuilder.SheetStandardMetricScale NXOpen.) StandardMetricScale
         Returns the standard Metric drawing scale   
            
         
        """
        pass
    @StandardMetricScale.setter
    def StandardMetricScale(self, metric_scale: DrawingSheetBuilder.SheetStandardMetricScale):
        """
        Setter for property: ( DrawingSheetBuilder.SheetStandardMetricScale NXOpen.) StandardMetricScale
         Returns the standard Metric drawing scale   
            
         
        """
        pass
    @property
    def Units(self) -> DrawingSheetBuilder.SheetUnits:
        """
        Getter for property: ( DrawingSheetBuilder.SheetUnits NXOpen.) Units
         Returns the units for the drawing sheet   
            
         
        """
        pass
    @Units.setter
    def Units(self, units: DrawingSheetBuilder.SheetUnits):
        """
        Setter for property: ( DrawingSheetBuilder.SheetUnits NXOpen.) Units
         Returns the units for the drawing sheet   
            
         
        """
        pass
import NXOpen
class DrawingSheetCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of drawing sheets."""
    @property
    def CurrentDrawingSheet(self) -> DrawingSheet:
        """
        Getter for property: ( DrawingSheet NXOpen.) CurrentDrawingSheet
         Returns the currently opened drawing sheet.  
            This will return NULL 
                if no drawing sheet is opened.   
         
        """
        pass
    @property
    def SheetTemplates() -> SheetTemplateManager:
        """
         Returns the Sheet Template Manager for part 
        """
        pass
    def DrawingSheetBuilder(self, sheet: DrawingSheet) -> DrawingSheetBuilder:
        """
         Create a drawing Sheet builder  
         Returns builder ( DrawingSheetBuilder NXOpen.):  the drawing sheet Builder with this identifier .
        """
        pass
    def FindObject(self, journal_identifier: str) -> DrawingSheet:
        """
         Finds the  NXOpen.Drawings.DrawingSheet  with the given identifier as recorded in a journal. 
                An object may not return the same value as its JournalIdentifier in different versions of 
                the software. However newer versions of the software should find the same object when 
                FindObject is passed older versions of its journal identifier. In general, this method 
                should not be used in handwritten code and exists to support record and playback of journals.
                An exception will be thrown if no object can be found with the given journal identifier. 
         Returns sketch ( DrawingSheet NXOpen.):  Drawing sheet with this identifier .
        """
        pass
    @overload
    def InsertSheet(self, drawing_name: str, drawing_units: DrawingSheet.Unit, width: float, height: float, numerator: float, denominator: float, projection_angle: DrawingSheet.ProjectionAngleType) -> DrawingSheet:
        """
         Inserts a sheet into a part. 
         Returns drawing_sheet ( DrawingSheet NXOpen.):   .
        """
        pass
    @overload
    def InsertSheet(self, drawing_name: str, sheet_size: DrawingSheet.StandardSheetSize, numerator: float, denominator: float, projection_angle: DrawingSheet.ProjectionAngleType) -> DrawingSheet:
        """
         Inserts a sheet into a part. The drawings units will be inferred from the standard
                    size.
         Returns drawing_sheet ( DrawingSheet NXOpen.):   .
        """
        pass
    def PasteDrawingSheets(self, dwgSheets: List[DrawingSheet]) -> List[DrawingSheet]:
        """
         Paste drawing sheets 
         Returns newPastedDwgSheets ( DrawingSheet List[NXOpe): new dwgs sheets.
        """
        pass
    def RefreshCurrentSheet(self) -> None:
        """
         Refresh the current Sheet  
        """
        pass
import NXOpen
class DrawingSheet(NXOpen.NXObject): 
    """ Represents a drawing sheet.
    When you create a sheet using Add Child Rule in KF with the use_template option, 
    you will need to set the option to either custom_size or standard_size afterwards.
    You also will need to set the scale, units, projection_angle, height, and length parameters, 
    as these are not required when creating a sheet with a template. """
    class ProjectionAngleType(Enum):
        """
        Members Include: 
         |FirstAngle|  
         |ThirdAngle|  

        """
        FirstAngle: int
        ThirdAngle: int
        @staticmethod
        def ValueOf(value: int) -> DrawingSheet.ProjectionAngleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StandardSheetSize(Enum):
        """
        Members Include: 
         |A|  8.5 x 11 inches 
         |B|  11 X 17 inches
         |C|  17 X 22 inches
         |D|  22 X 34 inches
         |E|  34 X 44 inches 
         |F|  28 X 40 inches 
         |H|  28 X 44 inches 
         |J|  34 X 55 inches 
         |A0|  841 x 1189 millimeters 
         |A1|  594 X 841 millimeters 
         |A2|  420 X 594 millimeters 
         |A3|  297 X 420 millimeters 
         |A4|  210 X 297 millimeters 

        """
        A: int
        B: int
        C: int
        D: int
        E: int
        F: int
        H: int
        J: int
        A0: int
        A1: int
        A2: int
        A3: int
        A4: int
        @staticmethod
        def ValueOf(value: int) -> DrawingSheet.StandardSheetSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Unit(Enum):
        """
        Members Include: 
         |Inches|  
         |Millimeters|  

        """
        Inches: int
        Millimeters: int
        @staticmethod
        def ValueOf(value: int) -> DrawingSheet.Unit:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BordersAndZones(self) -> BordersAndZones:
        """
        Getter for property: ( BordersAndZones NXOpen.) BordersAndZones
         Returns the borders and zones object if present   
            
         
        """
        pass
    @BordersAndZones.setter
    def BordersAndZones(self, bodersAndZones: BordersAndZones):
        """
        Setter for property: ( BordersAndZones NXOpen.) BordersAndZones
         Returns the borders and zones object if present   
            
         
        """
        pass
    @property
    def Height(self) -> float:
        """
        Getter for property: (float) Height
         Returns the height of the drawing sheet.  
             
         
        """
        pass
    @property
    def IsActiveForSketching(self) -> bool:
        """
        Getter for property: (bool) IsActiveForSketching
         Returns true if this drawing sheet's view is the active sketch view.  
             
         
        """
        pass
    @property
    def IsOutOfDate(self) -> bool:
        """
        Getter for property: (bool) IsOutOfDate
         Returns the status on whether this  NXOpen::Drawings::DrawingSheet  is out of date.  
             
         
        """
        pass
    @property
    def Length(self) -> float:
        """
        Getter for property: (float) Length
         Returns the length of the drawing sheet.  
             
         
        """
        pass
    @property
    def ProjectionAngle(self) -> DrawingSheet.ProjectionAngleType:
        """
        Getter for property: ( DrawingSheet.ProjectionAngleType NXOpen.) ProjectionAngle
         Returns the projection angle of the drawing sheet.  
             
         
        """
        pass
    @property
    def Units(self) -> DrawingSheet.Unit:
        """
        Getter for property: ( DrawingSheet.Unit NXOpen.) Units
         Returns the units of the drawing sheet.  
           To change the units of drawing sheet, use 
                     NXOpen::Drawings::DrawingSheet::SetParameters    
         
        """
        pass
    @property
    def View(self) -> NXOpen.View:
        """
        Getter for property: ( NXOpen.View) View
         Returns the  NXOpen::View  that represents this drawing sheet.  
             
         
        """
        pass
    @property
    def SheetDraftingViews() -> SheetDraftingViewCollection:
        """
         Returns the SheetDraftingViewCollection instance belonging to this drawing sheet 
        """
        pass
    @property
    def SheetSectionLines() -> SheetSectionLineCollection:
        """
         Returns the SheetSectionLineCollection instance belonging to this drawing sheet 
        """
        pass
    def ActivateForSketching(self) -> None:
        """
         Sets this drawingsheet's view as the active sketch view. 
                    Note: Can only activate a drawing sheet view for 
                          an active drawing sheet 
        """
        pass
    def GetDraftingSketches(self) -> List[NXOpen.Sketch]:
        """
         Returns all drafting  NXOpen.Sketch es on a sheet. 
         Returns sketches ( NXOpen.Sketch Li):  .
        """
        pass
    def GetDraftingViews(self) -> List[DraftingView]:
        """
         Returns the NXOpen.Drawings.DraftingViews on a sheet. 
         Returns views ( DraftingView List[NXOpe):  .
        """
        pass
    def GetScale(self) -> Tuple[float, float]:
        """
         Returns the scale of the drawing sheet. The scale of views that are
                defined by an expression, will not modified by this method.
         Returns A tuple consisting of (numerator, denominator). 
         - numerator is: float. .
         - denominator is: float. .

        """
        pass
    def GetSheetZoneReference(self, viewTag: DraftingView) -> str:
        """
         Returns the sheet and zone location or reference of the view if sheet zones are defined. 
         Returns sheetZoneReference (str): .
        """
        pass
    def GetZoneReference(self, viewTag: DraftingView) -> str:
        """
         Returns the zone location or reference of the view if sheet zones are defined. 
         Returns zoneReference (str): .
        """
        pass
    def Open(self) -> None:
        """
         Displays and activates the drawing sheet so that it can be edited. 
        """
        pass
    def ResetActiveForSketching(self) -> None:
        """
         Resets active for sketching view in given drawing. 
        """
        pass
    def SetParameters(self, height: float, length: float, numerator: float, denominator: float, units: DrawingSheet.Unit, projection_angle: DrawingSheet.ProjectionAngleType) -> List[DraftingView]:
        """
         Sets the parameters of the drawing sheet.  The scale of those NXOpen.Drawings.DraftingViews that are
                defined by an expression, will not modified by this method.  Currently this method only works for
                drawings that are opened.
         Returns associated_views ( DraftingView List[NXOpe):  List of  Drafting Views that did not have their scale modified
                                due to being defined by an expression. .
        """
        pass
import NXOpen
import NXOpen.Assemblies
class DrawingsPropertiesBuilder(NXOpen.Builder): 
    """
    Represents an NXOpen.Drawings.DrawingsPropertiesBuilder to be used for marking the
    component as secondary geometry.
    """
    class SecondaryComponentOptions(Enum):
        """
        Members Include: 
         |No|  Not marked as secondary geometry 
         |Yes|  Marked as secondary geometry 
         |Mixed|  Objects secondary geometry properties differ and will not change 

        """
        No: int
        Yes: int
        Mixed: int
        @staticmethod
        def ValueOf(value: int) -> DrawingsPropertiesBuilder.SecondaryComponentOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def SecondaryComponent(self) -> DrawingsPropertiesBuilder.SecondaryComponentOptions:
        """
        Getter for property: ( DrawingsPropertiesBuilder.SecondaryComponentOptions NXOpen.) SecondaryComponent
         Returns the secondary geometry state.  
          
                If true, the part occurrences are marked as secondary components. Otherwise, the part occurrences are considered as non-secondary components.   
         
        """
        pass
    @SecondaryComponent.setter
    def SecondaryComponent(self, secondaryComponent: DrawingsPropertiesBuilder.SecondaryComponentOptions):
        """
        Setter for property: ( DrawingsPropertiesBuilder.SecondaryComponentOptions NXOpen.) SecondaryComponent
         Returns the secondary geometry state.  
          
                If true, the part occurrences are marked as secondary components. Otherwise, the part occurrences are considered as non-secondary components.   
         
        """
        pass
    @property
    def SelectedObjects(self) -> NXOpen.Assemblies.SelectComponentList:
        """
        Getter for property: ( NXOpen.Assemblies.SelectComponentList) SelectedObjects
         Returns the selected object(s) list.  
           This is the active list of components that will be
                modified by any changes.   
         
        """
        pass
import NXOpen
class DrawingViewBuilder(NXOpen.Builder): 
    """ This builder allows the user to create a Drawing View """
    @property
    def CenterCoordinate(self) -> ViewCenterCoordinateBuilder:
        """
        Getter for property: ( ViewCenterCoordinateBuilder NXOpen.) CenterCoordinate
         Returns the center coordinate   
            
         
        """
        pass
    @property
    def MultipleViewPlacement(self) -> MultipleViewPlacementBuilder:
        """
        Getter for property: ( MultipleViewPlacementBuilder NXOpen.) MultipleViewPlacement
         Returns the multiple view placement   
            
         
        """
        pass
    @property
    def Scale(self) -> ViewScaleBuilder:
        """
        Getter for property: ( ViewScaleBuilder NXOpen.) Scale
         Returns the view scale   
            
         
        """
        pass
    @property
    def TwodOrientation(self) -> View2dOrientBuilder:
        """
        Getter for property: ( View2dOrientBuilder NXOpen.) TwodOrientation
         Returns the view orientation in 2D   
            
         
        """
        pass
    @property
    def ViewBoundary(self) -> ViewBoundaryBuilder:
        """
        Getter for property: ( ViewBoundaryBuilder NXOpen.) ViewBoundary
         Returns the view boundary.  
          
                    It is replace by  Drawings::DrawingViewBuilder::MultipleViewPlacement    
         
        """
        pass
    @property
    def ViewPlacement(self) -> ViewPlacementBuilder:
        """
        Getter for property: ( ViewPlacementBuilder NXOpen.) ViewPlacement
         Returns the view placement.  
          
                    It is replace by  Drawings::DrawingViewBuilder::MultipleViewPlacement    
         
        """
        pass
    @property
    def ViewStyle(self) -> ViewStyleBuilder:
        """
        Getter for property: ( ViewStyleBuilder NXOpen.) ViewStyle
         Returns the view style   
            
         
        """
        pass
class DrawingView(DraftingView): 
    """  Drawing View - an empty view created without any geometric objects.
         A drawing view can be used to create sketches in, or create view-dependent 
         geometry while in the expanded mode. """
    pass
class EditSectionLineSettingsBuilder(BaseEditSettingsBuilder): 
    """ Represents a NXOpen.Drawings.EditSectionLineSettingsBuilder builder.
        It provides an interface for editing section line style settings.
        This can be used to change one specific section line or all section lines. """
    @property
    def ViewCommonViewLabel(self) -> ViewCommonViewLabelBuilder:
        """
        Getter for property: ( ViewCommonViewLabelBuilder NXOpen.) ViewCommonViewLabel
         Returns the view common label builder   
            
         
        """
        pass
    @property
    def ViewSectionLine(self) -> ViewSectionLineBuilder:
        """
        Getter for property: ( ViewSectionLineBuilder NXOpen.) ViewSectionLine
         Returns the view section line builder   
            
         
        """
        pass
    def InheritSettingsFromCustomerDefault(self) -> None:
        """
         Inherit Settings From Customer Default 
        """
        pass
    def InheritSettingsFromPreferences(self) -> None:
        """
         Inherit Settings From Preference 
        """
        pass
    def InheritSettingsFromSelectedObjects(self, selectedObject: SectionLine) -> None:
        """
         Inherit Settings From Selected Objects 
        """
        pass
import NXOpen
import NXOpen.Annotations
class EditViewLabelSettingsBuilder(BaseEditSettingsBuilder): 
    """ Represents a NXOpen.Drawings.EditViewLabelSettingsBuilder builder.
        It provides an interface for editing view label style settings.
        This can be used to change one specific view label or all view labels. """
    @property
    def AnnotationStyle(self) -> NXOpen.Annotations.StyleBuilder:
        """
        Getter for property: ( NXOpen.Annotations.StyleBuilder) AnnotationStyle
         Returns the annotation style builder   
            
         
        """
        pass
    @property
    def ViewCommonViewLabel(self) -> ViewCommonViewLabelBuilder:
        """
        Getter for property: ( ViewCommonViewLabelBuilder NXOpen.) ViewCommonViewLabel
         Returns the view common view label builder   
            
         
        """
        pass
    @property
    def ViewDetailLabel(self) -> ViewDetailLabelBuilder:
        """
        Getter for property: ( ViewDetailLabelBuilder NXOpen.) ViewDetailLabel
         Returns the view detail label builder   
            
         
        """
        pass
    @property
    def ViewLabel(self) -> ViewLabelBuilder:
        """
        Getter for property: ( ViewLabelBuilder NXOpen.) ViewLabel
         Returns the view label builder   
            
         
        """
        pass
    @property
    def ViewProjectedLabel(self) -> ViewProjectedLabelBuilder:
        """
        Getter for property: ( ViewProjectedLabelBuilder NXOpen.) ViewProjectedLabel
         Returns the view projected label builder   
            
         
        """
        pass
    @property
    def ViewSectionLabel(self) -> ViewSectionLabelBuilder:
        """
        Getter for property: ( ViewSectionLabelBuilder NXOpen.) ViewSectionLabel
         Returns the view section label builder   
            
         
        """
        pass
    def InheritSettingsFromCustomerDefault(self) -> None:
        """
         Inherit Settings From Customer Default 
        """
        pass
    def InheritSettingsFromPreferences(self) -> None:
        """
         Inherit Settings From Preference 
        """
        pass
    def InheritSettingsFromSelectedObjects(self, selectedObject: NXOpen.NXObject) -> None:
        """
         Inherit Settings From Selected Objects 
        """
        pass
class EditViewSettingsBuilder(BaseEditSettingsBuilder): 
    """ Represents a NXOpen.Drawings.EditViewSettingsBuilder builder.
        It provides an interface for editing view style settings.
        This can be used to change one specific view or all views. """
    @property
    def ViewDetailLabel(self) -> ViewDetailLabelBuilder:
        """
        Getter for property: ( ViewDetailLabelBuilder NXOpen.) ViewDetailLabel
         Returns the view detail label builder   
            
         
        """
        pass
    @property
    def ViewLabel(self) -> ViewLabelBuilder:
        """
        Getter for property: ( ViewLabelBuilder NXOpen.) ViewLabel
         Returns the view label builder   
            
         
        """
        pass
    @property
    def ViewProjectedLabel(self) -> ViewProjectedLabelBuilder:
        """
        Getter for property: ( ViewProjectedLabelBuilder NXOpen.) ViewProjectedLabel
         Returns the view projected label builder   
            
         
        """
        pass
    @property
    def ViewSectionLabel(self) -> ViewSectionLabelBuilder:
        """
        Getter for property: ( ViewSectionLabelBuilder NXOpen.) ViewSectionLabel
         Returns the view section label builder   
            
         
        """
        pass
    @property
    def ViewStyle(self) -> ViewStyleBuilder:
        """
        Getter for property: ( ViewStyleBuilder NXOpen.) ViewStyle
         Returns the view style builder   
            
         
        """
        pass
    def InheritSettingsFromCustomerDefault(self) -> None:
        """
         Inherit Settings From Customer Default 
        """
        pass
    def InheritSettingsFromPreferences(self) -> None:
        """
         Inherit Settings From Preference 
        """
        pass
    def InheritSettingsFromSelectedObjects(self, selectedObject: DraftingView) -> None:
        """
         Inherit Settings From Selected Objects 
        """
        pass
import NXOpen
class FlatPatternObject(NXOpen.TransientObject): 
    """ Provides an interface to the data available for flat pattern objects on drawing
        views. """
    def Dispose(self) -> None:
        """
         Frees the memory of the underlying class 
        """
        pass
    def GetDirections(self) -> Tuple[NXOpen.Vector3d, NXOpen.Vector3d]:
        """
         Returns the X and Y direction vectors that correspond to the flattened
                    datum csys feature object. The vectors have been transformed to
                    drawing sheet coordinates. 
         Returns A tuple consisting of (xDirection, yDirection). 
         - xDirection is:  NXOpen.Vector3d. X direction of simulated CSYS .
         - yDirection is:  NXOpen.Vector3d. Y direction of simulated CSYS .

        """
        pass
    def GetFlatSolidObject(self) -> NXOpen.CartesianCoordinateSystem:
        """
         Returns the point object containing the attributes the user put on the
                    original datum CSYS feature. This is the prototype object. The 
                    recommended procedure is to use the point to obtain attribute values 
                    and to use GetOrigin and GetDirections to obtain the geometrical data 
                    because of mappings to occurrences and to the drawing sheet. 
         Returns csys ( NXOpen.CartesianCoordinateSystem): .
        """
        pass
    def GetOrigin(self) -> NXOpen.Point3d:
        """
         Returns the origin of the marker object (the point on the drawing). 
                    The point has been transformed to drawing sheet coordinates. 
         Returns origin ( NXOpen.Point3d): .
        """
        pass
import NXOpen
import NXOpen.SheetMetal
class FlatPatternViewStyle(NXOpen.Object): 
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
         Returns the properties object for the view's flat pattern style settings. 
         Returns properties_object ( NXOpen.SheetMetal.FlatPatternSettings):  Reference to the object on which to get and set the
                                style for flat pattern drawing member views. .
        """
        pass
class FontEnum(Enum):
    """
    Members Include: 
     |Blockfont| 

    """
    Blockfont: int
    @staticmethod
    def ValueOf(value: int) -> FontEnum:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.Preferences
class GeneralViewStyle(NXOpen.Object): 
    """ Represents set of General View Styles Preferences applicable to drafting views. """
    @property
    def Angle(self) -> float:
        """
        Getter for property: (float) Angle
         Returns the value of angle of a member view.  
            
         
        """
        pass
    @Angle.setter
    def Angle(self, angle: float):
        """
        Setter for property: (float) Angle
         Returns the value of angle of a member view.  
            
         
        """
        pass
    @property
    def AngleDecimalPointFormat(self) -> NXOpen.Preferences.DecimalPointCharacter:
        """
        Getter for property: ( NXOpen.Preferences.DecimalPointCharacter) AngleDecimalPointFormat
         Returns the decimal point character to use for view angle display.  
             
         
        """
        pass
    @AngleDecimalPointFormat.setter
    def AngleDecimalPointFormat(self, format: NXOpen.Preferences.DecimalPointCharacter):
        """
        Setter for property: ( NXOpen.Preferences.DecimalPointCharacter) AngleDecimalPointFormat
         Returns the decimal point character to use for view angle display.  
             
         
        """
        pass
    @property
    def AngleFormat(self) -> NXOpen.Preferences.AngleFormat:
        """
        Getter for property: ( NXOpen.Preferences.AngleFormat) AngleFormat
         Returns the format to use for view angle display.  
             
         
        """
        pass
    @AngleFormat.setter
    def AngleFormat(self, angleFormat: NXOpen.Preferences.AngleFormat):
        """
        Setter for property: ( NXOpen.Preferences.AngleFormat) AngleFormat
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
    def AnglePrecision(self, anglePrecision: int):
        """
        Setter for property: (int) AnglePrecision
         Returns the precision to use for view angle display.  
             
         
        """
        pass
    @property
    def AssociativeAngle(self) -> NXOpen.Scalar:
        """
        Getter for property: ( NXOpen.Scalar) AssociativeAngle
         Returns the value of angle of a member view.  
            
         
        """
        pass
    @AssociativeAngle.setter
    def AssociativeAngle(self, angle: NXOpen.Scalar):
        """
        Setter for property: ( NXOpen.Scalar) AssociativeAngle
         Returns the value of angle of a member view.  
            
         
        """
        pass
    @property
    def AutomaticAnchorPoint(self) -> bool:
        """
        Getter for property: (bool) AutomaticAnchorPoint
         Returns the status of Automatic Anchor Point.  
            
         
        """
        pass
    @AutomaticAnchorPoint.setter
    def AutomaticAnchorPoint(self, automatic_anchor_point: bool):
        """
        Setter for property: (bool) AutomaticAnchorPoint
         Returns the status of Automatic Anchor Point.  
            
         
        """
        pass
    @property
    def AutomaticUpdate(self) -> bool:
        """
        Getter for property: (bool) AutomaticUpdate
         Returns the status of Automatic update, if true then position, 
                    hidden lines, silhouettes, view bounds, section views, and 
                    section view details updated after a model change else 
                    the above items are not updated after a model change.  
           
                  
         
        """
        pass
    @AutomaticUpdate.setter
    def AutomaticUpdate(self, automatic_update: bool):
        """
        Setter for property: (bool) AutomaticUpdate
         Returns the status of Automatic update, if true then position, 
                    hidden lines, silhouettes, view bounds, section views, and 
                    section view details updated after a model change else 
                    the above items are not updated after a model change.  
           
                  
         
        """
        pass
    @property
    def BoundaryStatus(self) -> bool:
        """
        Getter for property: (bool) BoundaryStatus
         Returns the boundary status.  
            
         
        """
        pass
    @BoundaryStatus.setter
    def BoundaryStatus(self, boundary_status: bool):
        """
        Setter for property: (bool) BoundaryStatus
         Returns the boundary status.  
            
         
        """
        pass
    @property
    def DisplayId(self) -> NXOpen.Preferences.GeneralDisplayIdOption:
        """
        Getter for property: ( NXOpen.Preferences.GeneralDisplayIdOption) DisplayId
         Returns the display identifier option for a member view.  
          
                  
         
        """
        pass
    @DisplayId.setter
    def DisplayId(self, option: NXOpen.Preferences.GeneralDisplayIdOption):
        """
        Setter for property: ( NXOpen.Preferences.GeneralDisplayIdOption) DisplayId
         Returns the display identifier option for a member view.  
          
                  
         
        """
        pass
    @property
    def ExpressionForScale(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ExpressionForScale
         Returns the expression for scale   
            
         
        """
        pass
    @ExpressionForScale.setter
    def ExpressionForScale(self, expression_for_scale: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) ExpressionForScale
         Returns the expression for scale   
            
         
        """
        pass
    @property
    def ExtractedEdges(self) -> NXOpen.Preferences.GeneralExtractedEdgesOption:
        """
        Getter for property: ( NXOpen.Preferences.GeneralExtractedEdgesOption) ExtractedEdges
         Returns the extracted edge, that provides an alternative way to display
                    model geometry in a drawing view.  
          
                  
         
        """
        pass
    @ExtractedEdges.setter
    def ExtractedEdges(self, edges_option: NXOpen.Preferences.GeneralExtractedEdgesOption):
        """
        Setter for property: ( NXOpen.Preferences.GeneralExtractedEdgesOption) ExtractedEdges
         Returns the extracted edge, that provides an alternative way to display
                    model geometry in a drawing view.  
          
                  
         
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
    def LockmethodView(self) -> NXOpen.Preferences.GeneralViewLockmethodOption:
        """
        Getter for property: ( NXOpen.Preferences.GeneralViewLockmethodOption) LockmethodView
         Returns the lock method setting on the Configuration tab of the View Style Dialog   
            
         
        """
        pass
    @LockmethodView.setter
    def LockmethodView(self, lockmethodView: NXOpen.Preferences.GeneralViewLockmethodOption):
        """
        Setter for property: ( NXOpen.Preferences.GeneralViewLockmethodOption) LockmethodView
         Returns the lock method setting on the Configuration tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Reference(self) -> bool:
        """
        Getter for property: (bool) Reference
         Returns the status of reference, that toggles a view from active to reference.  
          
                    If true, the view is considered a reference view.
                   
         
        """
        pass
    @Reference.setter
    def Reference(self, reference: bool):
        """
        Setter for property: (bool) Reference
         Returns the status of reference, that toggles a view from active to reference.  
          
                    If true, the view is considered a reference view.
                   
         
        """
        pass
    @property
    def RenderCount(self) -> int:
        """
        Getter for property: (int) RenderCount
         Returns the render count.  
            
         
        """
        pass
    @RenderCount.setter
    def RenderCount(self, render_count: int):
        """
        Setter for property: (int) RenderCount
         Returns the render count.  
            
         
        """
        pass
    @property
    def Scale(self) -> float:
        """
        Getter for property: (float) Scale
         Returns the scale of a member view.  
            
         
        """
        pass
    @Scale.setter
    def Scale(self, scale: float):
        """
        Setter for property: (float) Scale
         Returns the scale of a member view.  
            
         
        """
        pass
    @property
    def ScaleLabel(self) -> bool:
        """
        Getter for property: (bool) ScaleLabel
         Returns the display of scale label.  
            
         
        """
        pass
    @ScaleLabel.setter
    def ScaleLabel(self, scale_label: bool):
        """
        Setter for property: (bool) ScaleLabel
         Returns the display of scale label.  
            
         
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
                    selected drawing member views added else silhouettes removed 
                    from the selected member views.  
           
                  
         
        """
        pass
    @Silhouettes.setter
    def Silhouettes(self, silhouettes: bool):
        """
        Setter for property: (bool) Silhouettes
         Returns the status of silhouettes curves, if true silhouettes for 
                    selected drawing member views added else silhouettes removed 
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
         Returns the value of tolerance, that specifies a chord height tolerance
                    value for silhouette and hidden line generation in a given 
                    drawing view.  
          
                  
         
        """
        pass
    @Tolerance.setter
    def Tolerance(self, tolerance: float):
        """
        Setter for property: (float) Tolerance
         Returns the value of tolerance, that specifies a chord height tolerance
                    value for silhouette and hidden line generation in a given 
                    drawing view.  
          
                  
         
        """
        pass
    @property
    def UvGrid(self) -> bool:
        """
        Getter for property: (bool) UvGrid
         Returns the status of UV grid, if true, grid curves for selected drawing
                    member views are added else the grid curves are removed from 
                    the selected member views.  
          
                   
         
        """
        pass
    @UvGrid.setter
    def UvGrid(self, uv_grid: bool):
        """
        Setter for property: (bool) UvGrid
         Returns the status of UV grid, if true, grid curves for selected drawing
                    member views are added else the grid curves are removed from 
                    the selected member views.  
          
                   
         
        """
        pass
    @property
    def ViewLabel(self) -> bool:
        """
        Getter for property: (bool) ViewLabel
         Returns the display of view label.  
            
         
        """
        pass
    @ViewLabel.setter
    def ViewLabel(self, view_label: bool):
        """
        Setter for property: (bool) ViewLabel
         Returns the display of view label.  
            
         
        """
        pass
    @property
    def ViewQuality(self) -> NXOpen.Preferences.GeneralViewQualityOption:
        """
        Getter for property: ( NXOpen.Preferences.GeneralViewQualityOption) ViewQuality
         Returns the view quality, that provides an alternative way to display
                    model geometry in a drawing view.  
          
                  
         
        """
        pass
    @ViewQuality.setter
    def ViewQuality(self, quality_option: NXOpen.Preferences.GeneralViewQualityOption):
        """
        Setter for property: ( NXOpen.Preferences.GeneralViewQualityOption) ViewQuality
         Returns the view quality, that provides an alternative way to display
                    model geometry in a drawing view.  
          
                  
         
        """
        pass
    @property
    def ViewRepresentation(self) -> NXOpen.Preferences.GeneralViewRepresentationOption:
        """
        Getter for property: ( NXOpen.Preferences.GeneralViewRepresentationOption) ViewRepresentation
         Returns the view representation enum on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @ViewRepresentation.setter
    def ViewRepresentation(self, viewRepresentation: NXOpen.Preferences.GeneralViewRepresentationOption):
        """
        Setter for property: ( NXOpen.Preferences.GeneralViewRepresentationOption) ViewRepresentation
         Returns the view representation enum on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def WireframeColorSource(self) -> NXOpen.Preferences.GeneralWireframeColorSourceOption:
        """
        Getter for property: ( NXOpen.Preferences.GeneralWireframeColorSourceOption) WireframeColorSource
         Returns the source of the wireframe color for a member view.  
          
                  
         
        """
        pass
    @WireframeColorSource.setter
    def WireframeColorSource(self, color_option: NXOpen.Preferences.GeneralWireframeColorSourceOption):
        """
        Setter for property: ( NXOpen.Preferences.GeneralWireframeColorSourceOption) WireframeColorSource
         Returns the source of the wireframe color for a member view.  
          
                  
         
        """
        pass
    def SetCenterlines(self, centerlines: bool) -> None:
        """
         The status of center line, if true automatically creates 
                    linear, cylindrical, and bolt circle centerlines (with a 
                    circular instance set) for views where the hole or pin axis
                    is perpendicular or parallel to the plane of the drawing view.
                
        """
        pass
    def SetFramebarHorizontal(self, framebarHorizontal: bool) -> None:
        """
         The status of framebar horizontal, if true automatically creates 
                    horizontal framebar for views where the view axis match with
                    ship axis.
                
        """
        pass
    def SetFramebarVertical(self, framebarVertical: bool) -> None:
        """
         The status of framebar vertical, if true automatically creates 
                    vertical framebar for views where the view axis match with
                    ship axis.
                
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class GeneralWorkFlowBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.Drawings.GeneralWorkFlowBuilder
    """
    class GridSettingsType(Enum):
        """
        Members Include: 
         |Drafting| 
         |Sketch| 
         |SheetZone| 

        """
        Drafting: int
        Sketch: int
        SheetZone: int
        @staticmethod
        def ValueOf(value: int) -> GeneralWorkFlowBuilder.GridSettingsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ModelBasedAlwaysStartType(Enum):
        """
        Members Include: 
         |ViewCreationWizard| 
         |BaseViewCommand| 
         |NoViewCommands| 

        """
        ViewCreationWizard: int
        BaseViewCommand: int
        NoViewCommands: int
        @staticmethod
        def ValueOf(value: int) -> GeneralWorkFlowBuilder.ModelBasedAlwaysStartType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SettingsOrientationType(Enum):
        """
        Members Include: 
         |DrawingTemplate| 
         |DrawingStandard| 

        """
        DrawingTemplate: int
        DrawingStandard: int
        @staticmethod
        def ValueOf(value: int) -> GeneralWorkFlowBuilder.SettingsOrientationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CreateDraftingComponent(self) -> bool:
        """
        Getter for property: (bool) CreateDraftingComponent
         Returns the flag indicating whether to creates a drafting component when creating a view of the master model part   
            
         
        """
        pass
    @CreateDraftingComponent.setter
    def CreateDraftingComponent(self, createDraftingComponent: bool):
        """
        Setter for property: (bool) CreateDraftingComponent
         Returns the flag indicating whether to creates a drafting component when creating a view of the master model part   
            
         
        """
        pass
    @property
    def GridSettings(self) -> GeneralWorkFlowBuilder.GridSettingsType:
        """
        Getter for property: ( GeneralWorkFlowBuilder.GridSettingsType NXOpen.) GridSettings
         Returns the option that indicates the grid settings   
            
         
        """
        pass
    @GridSettings.setter
    def GridSettings(self, gridSettings: GeneralWorkFlowBuilder.GridSettingsType):
        """
        Setter for property: ( GeneralWorkFlowBuilder.GridSettingsType NXOpen.) GridSettings
         Returns the option that indicates the grid settings   
            
         
        """
        pass
    @property
    def ModelBasedAlwaysStart(self) -> GeneralWorkFlowBuilder.ModelBasedAlwaysStartType:
        """
        Getter for property: ( GeneralWorkFlowBuilder.ModelBasedAlwaysStartType NXOpen.) ModelBasedAlwaysStart
         Returns the option that indicates action to be taken after inserting a sheet with no views   
            
         
        """
        pass
    @ModelBasedAlwaysStart.setter
    def ModelBasedAlwaysStart(self, modelBasedAlwaysStart: GeneralWorkFlowBuilder.ModelBasedAlwaysStartType):
        """
        Setter for property: ( GeneralWorkFlowBuilder.ModelBasedAlwaysStartType NXOpen.) ModelBasedAlwaysStart
         Returns the option that indicates action to be taken after inserting a sheet with no views   
            
         
        """
        pass
    @property
    def ModelBasedInsertSheet(self) -> bool:
        """
        Getter for property: (bool) ModelBasedInsertSheet
         Returns the flag indicating whether to automatically starts the insert sheet command when entering the drafting application if no drawing sheets exist   
            
         
        """
        pass
    @ModelBasedInsertSheet.setter
    def ModelBasedInsertSheet(self, modelBasedInsertSheet: bool):
        """
        Setter for property: (bool) ModelBasedInsertSheet
         Returns the flag indicating whether to automatically starts the insert sheet command when entering the drafting application if no drawing sheets exist   
            
         
        """
        pass
    @property
    def ModelBasedProjectedView(self) -> bool:
        """
        Getter for property: (bool) ModelBasedProjectedView
         Returns the flag indicating whether to automatically start the projected view command after inserting a model view.  
             
         
        """
        pass
    @ModelBasedProjectedView.setter
    def ModelBasedProjectedView(self, modelBasedProjectedView: bool):
        """
        Setter for property: (bool) ModelBasedProjectedView
         Returns the flag indicating whether to automatically start the projected view command after inserting a model view.  
             
         
        """
        pass
    @property
    def SettingsOrigination(self) -> GeneralWorkFlowBuilder.SettingsOrientationType:
        """
        Getter for property: ( GeneralWorkFlowBuilder.SettingsOrientationType NXOpen.) SettingsOrigination
         Returns the option that indicates the settings origination   
            
         
        """
        pass
    @SettingsOrigination.setter
    def SettingsOrigination(self, settingsOrigination: GeneralWorkFlowBuilder.SettingsOrientationType):
        """
        Setter for property: ( GeneralWorkFlowBuilder.SettingsOrientationType NXOpen.) SettingsOrigination
         Returns the option that indicates the settings origination   
            
         
        """
        pass
    @property
    def StandAloneInsertSheet(self) -> bool:
        """
        Getter for property: (bool) StandAloneInsertSheet
         Returns the flag indicating whether to automatically starts the insert sheet command when entering the drafting application
                if no drawing sheets exist.  
            
         
        """
        pass
    @StandAloneInsertSheet.setter
    def StandAloneInsertSheet(self, standAloneInsertSheet: bool):
        """
        Setter for property: (bool) StandAloneInsertSheet
         Returns the flag indicating whether to automatically starts the insert sheet command when entering the drafting application
                if no drawing sheets exist.  
            
         
        """
        pass
    @property
    def StandAloneProjectToView(self) -> bool:
        """
        Getter for property: (bool) StandAloneProjectToView
         Returns the flag indicating whether to automatically starts the projected view command after inserting a projected drawing view.  
            
         
        """
        pass
    @StandAloneProjectToView.setter
    def StandAloneProjectToView(self, standAloneProjectToView: bool):
        """
        Setter for property: (bool) StandAloneProjectToView
         Returns the flag indicating whether to automatically starts the projected view command after inserting a projected drawing view.  
            
         
        """
        pass
    @property
    def StandAloneProjectedView(self) -> bool:
        """
        Getter for property: (bool) StandAloneProjectedView
         Returns the flag indicating whether to automatically starts the projected view command after inserting a drawing view.  
            
         
        """
        pass
    @StandAloneProjectedView.setter
    def StandAloneProjectedView(self, standAloneProjectedView: bool):
        """
        Setter for property: (bool) StandAloneProjectedView
         Returns the flag indicating whether to automatically starts the projected view command after inserting a drawing view.  
            
         
        """
        pass
    @property
    def StandAloneViewCreation(self) -> bool:
        """
        Getter for property: (bool) StandAloneViewCreation
         Returns the flag indicating whether to automatically starts the drawing view command after inserting a sheet with no views.  
            
         
        """
        pass
    @StandAloneViewCreation.setter
    def StandAloneViewCreation(self, standAloneViewCreation: bool):
        """
        Setter for property: (bool) StandAloneViewCreation
         Returns the flag indicating whether to automatically starts the drawing view command after inserting a sheet with no views.  
            
         
        """
        pass
class HalfPictorialSectionLine(HalfSectionLine): 
    """ Half Pictorial Section Line is used to create a pictorial view with
        half of the part sectioned and the other half un-sectioned. Note that
        the Half Pictorial Section Line contains only one arrow, one bend,
        and one cut segment. """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class HalfSectionLineBuilder(NXOpen.TaggedObject): 
    """ Represents a NXOpen.Drawings.HalfSectionLineBuilder.
        This class is used to create or edit a
        NXOpen.Drawings.HalfSectionLine. """
    @property
    def BendLocation(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) BendLocation
         Returns the bend location   
            
         
        """
        pass
    @BendLocation.setter
    def BendLocation(self, bendLocation: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) BendLocation
         Returns the bend location   
            
         
        """
        pass
    @property
    def CutLocation(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) CutLocation
         Returns the cut location   
            
         
        """
        pass
    @CutLocation.setter
    def CutLocation(self, cutLocation: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) CutLocation
         Returns the cut location   
            
         
        """
        pass
    @property
    def EndLocation1(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) EndLocation1
         Returns the arrow location   
            
         
        """
        pass
    @EndLocation1.setter
    def EndLocation1(self, endLocation1: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) EndLocation1
         Returns the arrow location   
            
         
        """
        pass
class HalfSectionLine(BaseHalfSectionLine): 
    """ Half Section Line is used to create a view with half of the part
        sectioned and the other half un-sectioned. Half sections are similar
        to simple and stepped sections in that the cut segment is parallel
        to the defined hinge line. Note that the Half Section Line contains
        only one arrow, one bend, and one cut segment. """
    pass
import NXOpen
import NXOpen.Preferences
class HiddenLinesViewStyle(NXOpen.Object): 
    """ Represents set of Hidden Lines View Style Preferences applicable to drafting views. """
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
         Returns the color of hiddenline.  
           The value should be between 1 and 216.   
         
        """
        pass
    @HiddenlineColor.setter
    def HiddenlineColor(self, color: int):
        """
        Setter for property: (int) HiddenlineColor
         Returns the color of hiddenline.  
           The value should be between 1 and 216.   
         
        """
        pass
    @property
    def HiddenlineFont(self) -> NXOpen.Preferences.Font:
        """
        Getter for property: ( NXOpen.Preferences.Font) HiddenlineFont
         Returns the font of hiddenline   
            
         
        """
        pass
    @HiddenlineFont.setter
    def HiddenlineFont(self, font: NXOpen.Preferences.Font):
        """
        Setter for property: ( NXOpen.Preferences.Font) HiddenlineFont
         Returns the font of hiddenline   
            
         
        """
        pass
    @property
    def HiddenlineWidth(self) -> NXOpen.Preferences.Width:
        """
        Getter for property: ( NXOpen.Preferences.Width) HiddenlineWidth
         Returns the width of hiddenline   
            
         
        """
        pass
    @HiddenlineWidth.setter
    def HiddenlineWidth(self, width: NXOpen.Preferences.Width):
        """
        Setter for property: ( NXOpen.Preferences.Width) HiddenlineWidth
         Returns the width of hiddenline   
            
         
        """
        pass
    @property
    def IncludeModelCurves(self) -> bool:
        """
        Getter for property: (bool) IncludeModelCurves
         Returns the status of include model curves   
            
         
        """
        pass
    @IncludeModelCurves.setter
    def IncludeModelCurves(self, include_model_curves: bool):
        """
        Setter for property: (bool) IncludeModelCurves
         Returns the status of include model curves   
            
         
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
    def InterferingSolidsOption(self) -> NXOpen.Preferences.HiddenLineInterferingSolidsOption:
        """
        Getter for property: ( NXOpen.Preferences.HiddenLineInterferingSolidsOption) InterferingSolidsOption
         Returns the status of interfering solids.  
           This allows the correct rendering of hidden lines 
                    in a drawing member view with interfering solids.
                   
         
        """
        pass
    @InterferingSolidsOption.setter
    def InterferingSolidsOption(self, interfering_solids: NXOpen.Preferences.HiddenLineInterferingSolidsOption):
        """
        Setter for property: ( NXOpen.Preferences.HiddenLineInterferingSolidsOption) InterferingSolidsOption
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
    def SmallFeature(self) -> NXOpen.Preferences.HiddenLineSmallFeatureOption:
        """
        Getter for property: ( NXOpen.Preferences.HiddenLineSmallFeatureOption) SmallFeature
         Returns the small feature option.  
           This allows the simplification or removal of rendering of small features 
                    in large scale assembly drawings. Not all small features are considered for simplified rendering. 
                    Only if the boundary of a small feature lies completely within a face of the model is the small 
                    feature's display modified.
                   
         
        """
        pass
    @SmallFeature.setter
    def SmallFeature(self, small_feature: NXOpen.Preferences.HiddenLineSmallFeatureOption):
        """
        Setter for property: ( NXOpen.Preferences.HiddenLineSmallFeatureOption) SmallFeature
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
import NXOpen.GeometricUtilities
class HiddenObjectsBuilder(NXOpen.TaggedObject): 
    """ This builder allows the user to select a view in which
        component objects can be designated as hidden or shown """
    @property
    def Objects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Objects
         Returns the objects   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class HingeLineBuilder(NXOpen.TaggedObject): 
    """
    Represents a Drawings.HingeLineBuilder. A hinge line is a line displayed on the parent 
    view and used as a reference to rotate a child view in proper orthographic space.
    """
    class Hingeline(Enum):
        """
        Members Include: 
         |Inferred|  The option to infer a hinge line based on parent, child view position 
         |Defined|  The option for selecting hinge line using vector construction tools 

        """
        Inferred: int
        Defined: int
        @staticmethod
        def ValueOf(value: int) -> HingeLineBuilder.Hingeline:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns the infer associative setting   
            
         
        """
        pass
    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
         Returns the infer associative setting   
            
         
        """
        pass
    @property
    def ReverseDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseDirection
         Returns the reverse direction setting   
            
         
        """
        pass
    @ReverseDirection.setter
    def ReverseDirection(self, reverseDirection: bool):
        """
        Setter for property: (bool) ReverseDirection
         Returns the reverse direction setting   
            
         
        """
        pass
    @property
    def SpecifyVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) SpecifyVector
         Returns the direction for the hinge line   
            
         
        """
        pass
    @SpecifyVector.setter
    def SpecifyVector(self, specifyVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) SpecifyVector
         Returns the direction for the hinge line   
            
         
        """
        pass
    @property
    def VectorOption(self) -> HingeLineBuilder.Hingeline:
        """
        Getter for property: ( HingeLineBuilder.Hingeline NXOpen.) VectorOption
         Returns the vector option: Inferred or Defined   
            
         
        """
        pass
    @VectorOption.setter
    def VectorOption(self, vectorOption: HingeLineBuilder.Hingeline):
        """
        Setter for property: ( HingeLineBuilder.Hingeline NXOpen.) VectorOption
         Returns the vector option: Inferred or Defined   
            
         
        """
        pass
class HorizontalCenteringMarkType(Enum):
    """
    Members Include: 
     |NotSet|  None 
     |LeftArrow|  Left Arrow 
     |RightArrow|   Right Arrow 
     |LeftandRightArrow|  Left and Right Arrow 
     |LeftandRightLine| 

    """
    NotSet: int
    LeftArrow: int
    RightArrow: int
    LeftandRightArrow: int
    LeftandRightLine: int
    @staticmethod
    def ValueOf(value: int) -> HorizontalCenteringMarkType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.Preferences
class InheritPmiViewStyle(NXOpen.Object): 
    """ Represents set of InheritPmiViewStyle applicable to drafting views. """
    @property
    def CrosshatchPmiLwsv(self) -> bool:
        """
        Getter for property: (bool) CrosshatchPmiLwsv
         Returns the cross-hatch setting for the current inherited PMI Lightweight Section View   
            
         
        """
        pass
    @property
    def InheritPmiMode(self) -> NXOpen.Preferences.PmiOption:
        """
        Getter for property: ( NXOpen.Preferences.PmiOption) InheritPmiMode
         Returns the Inherit pmi mode.  
             
         
        """
        pass
    @InheritPmiMode.setter
    def InheritPmiMode(self, pmi_option: NXOpen.Preferences.PmiOption):
        """
        Setter for property: ( NXOpen.Preferences.PmiOption) InheritPmiMode
         Returns the Inherit pmi mode.  
             
         
        """
        pass
    @property
    def InheritPmiToDrawing(self) -> bool:
        """
        Getter for property: (bool) InheritPmiToDrawing
         Returns the status of pmi inherited to drawing.  
             
         
        """
        pass
    @InheritPmiToDrawing.setter
    def InheritPmiToDrawing(self, pmi_to_drawing: bool):
        """
        Setter for property: (bool) InheritPmiToDrawing
         Returns the status of pmi inherited to drawing.  
             
         
        """
        pass
    @property
    def InheritPmiTypeMask(self) -> int:
        """
        Getter for property: (int) InheritPmiTypeMask
         Returns the Inherit pmi type mask.  
             
         
        """
        pass
    @InheritPmiTypeMask.setter
    def InheritPmiTypeMask(self, pmi_type_mask: int):
        """
        Setter for property: (int) InheritPmiTypeMask
         Returns the Inherit pmi type mask.  
             
         
        """
        pass
    @property
    def PmiDimensionFromRevolved(self) -> bool:
        """
        Getter for property: (bool) PmiDimensionFromRevolved
         Returns the status of pmi inherited to drawing.  
             
         
        """
        pass
    @PmiDimensionFromRevolved.setter
    def PmiDimensionFromRevolved(self, pmiDimensionFromRevolved: bool):
        """
        Setter for property: (bool) PmiDimensionFromRevolved
         Returns the status of pmi inherited to drawing.  
             
         
        """
        pass
    def SetCrosshatchPmiLwsv(self, crosshatch: bool) -> None:
        """
         Controls whether the cut faces of an inherited PMI Lightweight
                    section view are cross-hatched or not.
                
        """
        pass
    def SetInheritGdt(self, gdt_option: NXOpen.Preferences.GdtOption) -> None:
        """
         Inherit GD and T option,that let you inherit GD and T display 
                    instances onto the drawing plane or into a drawing member view.
                
        """
        pass
class LabelPositionTypes(Enum):
    """
    Members Include: 
     |Above| 
     |Below| 

    """
    Above: int
    Below: int
    @staticmethod
    def ValueOf(value: int) -> LabelPositionTypes:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class LetterFormatTypes(Enum):
    """
    Members Include: 
     |A| 
     |AA| 
     |AA1| 

    """
    A: int
    AA: int
    AA1: int
    @staticmethod
    def ValueOf(value: int) -> LetterFormatTypes:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class MarkAsTemplateBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Drawings.MarkAsTemplateBuilder
    """
    class ActionTypeEnum(Enum):
        """
        Members Include: 
         |TemplateOnly| 
         |TemplateAndPax| 

        """
        TemplateOnly: int
        TemplateAndPax: int
        @staticmethod
        def ValueOf(value: int) -> MarkAsTemplateBuilder.ActionTypeEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ItemTypeEnum(Enum):
        """
        Members Include: 
         |Any| 
         |NXPart| 
         |NXDrawing| 

        """
        Any: int
        NXPart: int
        NXDrawing: int
        @staticmethod
        def ValueOf(value: int) -> MarkAsTemplateBuilder.ItemTypeEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RelationTypeEnum(Enum):
        """
        Members Include: 
         |Master| 
         |Specification| 
         |Manifestation| 

        """
        Master: int
        Specification: int
        Manifestation: int
        @staticmethod
        def ValueOf(value: int) -> MarkAsTemplateBuilder.RelationTypeEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TemplateTypeEnum(Enum):
        """
        Members Include: 
         |Sheet| 
         |ReferenceExistingPart| 
         |Standalone| 

        """
        Sheet: int
        ReferenceExistingPart: int
        Standalone: int
        @staticmethod
        def ValueOf(value: int) -> MarkAsTemplateBuilder.TemplateTypeEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ActionType(self) -> MarkAsTemplateBuilder.ActionTypeEnum:
        """
        Getter for property: ( MarkAsTemplateBuilder.ActionTypeEnum NXOpen.) ActionType
         Returns the action type of the part.  
            
         
        """
        pass
    @ActionType.setter
    def ActionType(self, actionType: MarkAsTemplateBuilder.ActionTypeEnum):
        """
        Setter for property: ( MarkAsTemplateBuilder.ActionTypeEnum NXOpen.) ActionType
         Returns the action type of the part.  
            
         
        """
        pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the detailed description for each template.  
             
         
        """
        pass
    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the detailed description for each template.  
             
         
        """
        pass
    @property
    def ItemType(self) -> MarkAsTemplateBuilder.ItemTypeEnum:
        """
        Getter for property: ( MarkAsTemplateBuilder.ItemTypeEnum NXOpen.) ItemType
         Returns the item type of the part.  
            
         
        """
        pass
    @ItemType.setter
    def ItemType(self, itemType: MarkAsTemplateBuilder.ItemTypeEnum):
        """
        Setter for property: ( MarkAsTemplateBuilder.ItemTypeEnum NXOpen.) ItemType
         Returns the item type of the part.  
            
         
        """
        pass
    @property
    def ItemTypeString(self) -> str:
        """
        Getter for property: (str) ItemTypeString
         Returns the item type string of the part.  
            
         
        """
        pass
    @ItemTypeString.setter
    def ItemTypeString(self, itemType: str):
        """
        Setter for property: (str) ItemTypeString
         Returns the item type string of the part.  
            
         
        """
        pass
    @property
    def PaxFileName(self) -> str:
        """
        Getter for property: (str) PaxFileName
         Returns the PAX file to be updated or created if it does not exist.  
             
         
        """
        pass
    @PaxFileName.setter
    def PaxFileName(self, filename: str):
        """
        Setter for property: (str) PaxFileName
         Returns the PAX file to be updated or created if it does not exist.  
             
         
        """
        pass
    @property
    def PresentationName(self) -> str:
        """
        Getter for property: (str) PresentationName
         Returns the presentation name of the template that will be displayed in the File-New dialog.  
              
         
        """
        pass
    @PresentationName.setter
    def PresentationName(self, presentationName: str):
        """
        Setter for property: (str) PresentationName
         Returns the presentation name of the template that will be displayed in the File-New dialog.  
              
         
        """
        pass
    @property
    def RelationType(self) -> MarkAsTemplateBuilder.RelationTypeEnum:
        """
        Getter for property: ( MarkAsTemplateBuilder.RelationTypeEnum NXOpen.) RelationType
         Returns the relation type is required only for the managed mode.  
           The available options are
                    Master
                    Specification
                    Manifestation
                  
         
        """
        pass
    @RelationType.setter
    def RelationType(self, relationType: MarkAsTemplateBuilder.RelationTypeEnum):
        """
        Setter for property: ( MarkAsTemplateBuilder.RelationTypeEnum NXOpen.) RelationType
         Returns the relation type is required only for the managed mode.  
           The available options are
                    Master
                    Specification
                    Manifestation
                  
         
        """
        pass
    @property
    def TemplateType(self) -> MarkAsTemplateBuilder.TemplateTypeEnum:
        """
        Getter for property: ( MarkAsTemplateBuilder.TemplateTypeEnum NXOpen.) TemplateType
         Returns the template Type will be one of the following:
                    Sheet
                    To save it as Sheet template.  
           When using Sheet templates, NX adds drawing sheets based on the template to the current work part. 
                    Master Model Drawing
                    To save it as Master Model Drawing template. When using Master Model Drawing templates, NX create a new master model drawing from the current part. NX creates a new drawing part from the template and includes the current model as a component.
                    2D-Drawing
                    To save it as 2D Drawing template. These are the templates used for 2D-drawings. These templates do not require a master model
                  
         
        """
        pass
    @TemplateType.setter
    def TemplateType(self, templateType: MarkAsTemplateBuilder.TemplateTypeEnum):
        """
        Setter for property: ( MarkAsTemplateBuilder.TemplateTypeEnum NXOpen.) TemplateType
         Returns the template Type will be one of the following:
                    Sheet
                    To save it as Sheet template.  
           When using Sheet templates, NX adds drawing sheets based on the template to the current work part. 
                    Master Model Drawing
                    To save it as Master Model Drawing template. When using Master Model Drawing templates, NX create a new master model drawing from the current part. NX creates a new drawing part from the template and includes the current model as a component.
                    2D-Drawing
                    To save it as 2D Drawing template. These are the templates used for 2D-drawings. These templates do not require a master model
                  
         
        """
        pass
class Method(Enum):
    """
    Members Include: 
     |NotSet|  To support legacy parts 
     |Standard|  Standard 
     |Custom| 

    """
    NotSet: int
    Standard: int
    Custom: int
    @staticmethod
    def ValueOf(value: int) -> Method:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class MultipleViewPlacementBuilder(NXOpen.TaggedObject): 
    """ This builder allows the user to create a Multiple View Placement """
    class Option(Enum):
        """
        Members Include: 
         |Center|  By Center 
         |Corners|  By Corners 

        """
        Center: int
        Corners: int
        @staticmethod
        def ValueOf(value: int) -> MultipleViewPlacementBuilder.Option:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AssociativeAlignment(self) -> bool:
        """
        Getter for property: (bool) AssociativeAlignment
         Returns the associative alignment toggle   
            
         
        """
        pass
    @AssociativeAlignment.setter
    def AssociativeAlignment(self, associative: bool):
        """
        Setter for property: (bool) AssociativeAlignment
         Returns the associative alignment toggle   
            
         
        """
        pass
    @property
    def OptionType(self) -> MultipleViewPlacementBuilder.Option:
        """
        Getter for property: ( MultipleViewPlacementBuilder.Option NXOpen.) OptionType
         Returns the placement option   
            
         
        """
        pass
    @OptionType.setter
    def OptionType(self, option: MultipleViewPlacementBuilder.Option):
        """
        Setter for property: ( MultipleViewPlacementBuilder.Option NXOpen.) OptionType
         Returns the placement option   
            
         
        """
        pass
    @property
    def ViewPlacementCenter(self) -> ViewPlacementBuilder:
        """
        Getter for property: ( ViewPlacementBuilder NXOpen.) ViewPlacementCenter
         Returns the view placement block for the center option   
            
         
        """
        pass
    @property
    def ViewPlacementFirstCorner(self) -> ViewPlacementBuilder:
        """
        Getter for property: ( ViewPlacementBuilder NXOpen.) ViewPlacementFirstCorner
         Returns the view placement block for the first corner   
            
         
        """
        pass
    @property
    def ViewPlacementSecondCorner(self) -> ViewPlacementBuilder:
        """
        Getter for property: ( ViewPlacementBuilder NXOpen.) ViewPlacementSecondCorner
         Returns the view placement block for the second corner   
            
         
        """
        pass
import NXOpen
class OrderManager(NXOpen.Object): 
    """ Represents an object that manages orders. An order represents the way 2D components are presented in the sketch node in the part navigator.
        There are two types of orders, system and user-defined. System orders cannot be modified."""
    def ApplyOrder(self, parentObject: NXOpen.Sketch, orderName: str) -> None:
        """
         Applies the order matching the specified name 
        """
        pass
    def CreateNewOrder(self, parentObject: NXOpen.Sketch, newOrderName: str, objectsInOrder: List[Component]) -> None:
        """
         Creates an order of the 2D Components provided in the list 
        """
        pass
    def DeleteOrder(self, parentObject: NXOpen.Sketch, newOrderName: str) -> None:
        """
         Delete the order matching the specified name 
        """
        pass
    def GetAvailableOrdersNames(self, parentObject: NXOpen.Sketch) -> List[str]:
        """
         Gets all available orders names for specified sketch parent 
         Returns ordersNames (List[str]): .
        """
        pass
    def GetCurrentOrderName(self, parentObject: NXOpen.Sketch) -> str:
        """
         Gets the current applied order name 
         Returns orderName (str): .
        """
        pass
    def IsSystemOrder(self, parentObject: NXOpen.Sketch, orderName: str) -> bool:
        """
         Validates the order matching the specified name is system order  
         Returns isSystem (bool): .
        """
        pass
    def RenameOrder(self, parentObject: NXOpen.Sketch, orderName: str, newOrderName: str) -> None:
        """
         Renames the order matching the specified name with the new name provided 
        """
        pass
    def Reorder(self, parentObject: NXOpen.Sketch, objectsInOrder: List[Component]) -> None:
        """
         Updates the current order based on the provided list of 2D components if the order is user-defined, and creates a new order otherwide 
        """
        pass
import NXOpen
import NXOpen.Preferences
class OrientationViewStyle(NXOpen.Object): 
    """ Represents set of Orientation View Style Preferences applicable to drafting views. """
    @property
    def HingeLine(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) HingeLine
         Returns the hinge line for an existing auxillary view.  
            
         
        """
        pass
    @HingeLine.setter
    def HingeLine(self, hinge_line: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) HingeLine
         Returns the hinge line for an existing auxillary view.  
            
         
        """
        pass
    @property
    def RotationPlane(self) -> NXOpen.Xform:
        """
        Getter for property: ( NXOpen.Xform) RotationPlane
         Returns the rotation plane.  
             
         
        """
        pass
    @RotationPlane.setter
    def RotationPlane(self, plane: NXOpen.Xform):
        """
        Setter for property: ( NXOpen.Xform) RotationPlane
         Returns the rotation plane.  
             
         
        """
        pass
    @property
    def RotationXDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) RotationXDirection
         Returns the rotation in x-direction for the drawing member view which stays 
                   parallel to the x-axis drawing coordinate.  
           The orientation of the view is 
                   associative to the x-direction.
                  
         
        """
        pass
    @RotationXDirection.setter
    def RotationXDirection(self, x_direction: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) RotationXDirection
         Returns the rotation in x-direction for the drawing member view which stays 
                   parallel to the x-axis drawing coordinate.  
           The orientation of the view is 
                   associative to the x-direction.
                  
         
        """
        pass
    def OrientView(self, matrix: NXOpen.Matrix3x3) -> None:
        """
         Orients the view.  
        """
        pass
    def Restore(self) -> None:
        """
         Removes the associativity to the defined plane (if it existed) and returns 
                  the member view to its orientation with the model with respect to the Absolute 
                  Coordinate System.
                
        """
        pass
    def ReverseHingeLine(self) -> None:
        """
         Reverse the hinge line. The direction of this vector 
                   determines how the view is rendered. 
                
        """
        pass
    def ReverseRotationVector(self) -> None:
        """
         Reverse the rotation vector. The direction of this vector 
                   determines how the view is rendered. 
                
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class OrientedSectionLineBuilder(NXOpen.TaggedObject): 
    """ Represents a NXOpen.Drawings.OrientedSectionLineBuilder.
        This class is used to create or edit a
        NXOpen.Drawings.OrientedSectionLine. """
    @property
    def CutLocation3D(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) CutLocation3D
         Returns the 3D cut location   
            
         
        """
        pass
    @CutLocation3D.setter
    def CutLocation3D(self, cutLocation3D: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) CutLocation3D
         Returns the 3D cut location   
            
         
        """
        pass
    @property
    def EndLocation1(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) EndLocation1
         Returns the end location 1 which determines the position of the
                    first arrow segment in the section line.  
             
         
        """
        pass
    @EndLocation1.setter
    def EndLocation1(self, endLocation1: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) EndLocation1
         Returns the end location 1 which determines the position of the
                    first arrow segment in the section line.  
             
         
        """
        pass
    @property
    def EndLocation2(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) EndLocation2
         Returns the end location 2 which determines the position of the
                    second arrow segment in the section line   
            
         
        """
        pass
    @EndLocation2.setter
    def EndLocation2(self, endLocation2: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) EndLocation2
         Returns the end location 2 which determines the position of the
                    second arrow segment in the section line   
            
         
        """
        pass
class OrientedSectionLine(SectionLine): 
    """ Represents a Oriented Section Line. """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class OvtBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.Drawings.OvtBuilder
    """
    @property
    def AssociativeOrientation(self) -> bool:
        """
        Getter for property: (bool) AssociativeOrientation
         Returns the associative orientation that specifies whether or not the view 
                    will be associative to the specified plane andor X direction   
            
         
        """
        pass
    @AssociativeOrientation.setter
    def AssociativeOrientation(self, associativeOrientation: bool):
        """
        Setter for property: (bool) AssociativeOrientation
         Returns the associative orientation that specifies whether or not the view 
                    will be associative to the specified plane andor X direction   
            
         
        """
        pass
    @property
    def NormalDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) NormalDirection
         Returns the vector that represents the normal direction for the view to be created or edited   
            
         
        """
        pass
    @NormalDirection.setter
    def NormalDirection(self, normalDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) NormalDirection
         Returns the vector that represents the normal direction for the view to be created or edited   
            
         
        """
        pass
    @property
    def XDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) XDirection
         Returns the x direction vector for the view to be created or edited   
            
         
        """
        pass
    @XDirection.setter
    def XDirection(self, xDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) XDirection
         Returns the x direction vector for the view to be created or edited   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ParentViewBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.Drawings.ParentViewBuilder.  This class
    is used to define a parent view when creating a drafting member view
    object.
    """
    @property
    def View(self) -> SelectDraftingView:
        """
        Getter for property: ( SelectDraftingView NXOpen.) View
         Returns the parent view   
            
         
        """
        pass
import NXOpen
import NXOpen.Preferences
class PerspectiveViewStyle(NXOpen.Object): 
    """ Represents set of PerspectiveViewStyle applicable to drafting views. """
    @property
    def BackClipping(self) -> bool:
        """
        Getter for property: (bool) BackClipping
         Returns the status of back clipping   
            
         
        """
        pass
    @BackClipping.setter
    def BackClipping(self, back_clipping: bool):
        """
        Setter for property: (bool) BackClipping
         Returns the status of back clipping   
            
         
        """
        pass
    @property
    def BackClippingDistance(self) -> float:
        """
        Getter for property: (float) BackClippingDistance
         Returns the value of back clipping distance   
            
         
        """
        pass
    @BackClippingDistance.setter
    def BackClippingDistance(self, back_clipping_distance: float):
        """
        Setter for property: (float) BackClippingDistance
         Returns the value of back clipping distance   
            
         
        """
        pass
    @property
    def FrontClipping(self) -> bool:
        """
        Getter for property: (bool) FrontClipping
         Returns the status of front clipping   
            
         
        """
        pass
    @FrontClipping.setter
    def FrontClipping(self, front_clipping: bool):
        """
        Setter for property: (bool) FrontClipping
         Returns the status of front clipping   
            
         
        """
        pass
    @property
    def FrontClippingDistance(self) -> float:
        """
        Getter for property: (float) FrontClippingDistance
         Returns the value of front clipping distance   
            
         
        """
        pass
    @FrontClippingDistance.setter
    def FrontClippingDistance(self, front_clipping_distance: float):
        """
        Setter for property: (float) FrontClippingDistance
         Returns the value of front clipping distance   
            
         
        """
        pass
    @property
    def Perspective(self) -> bool:
        """
        Getter for property: (bool) Perspective
         Returns the status of perspective   
            
         
        """
        pass
    @Perspective.setter
    def Perspective(self, perspective: bool):
        """
        Setter for property: (bool) Perspective
         Returns the status of perspective   
            
         
        """
        pass
    @property
    def PerspectiveDistance(self) -> float:
        """
        Getter for property: (float) PerspectiveDistance
         Returns the value of perspective distance   
            
         
        """
        pass
    @PerspectiveDistance.setter
    def PerspectiveDistance(self, perspective_distance: float):
        """
        Setter for property: (float) PerspectiveDistance
         Returns the value of perspective distance   
            
         
        """
        pass
class PictorialSectionLine(SteppedSectionLine): 
    """ A Pictorial Simple or Pictorial Stepped Section Line.

        This section line is used to create either a simple or stepped
        section cut from a pictorial parent member view. The section line
        displays as a pictorial section line.

        Pictorial Simple Section Line provides one cut to form a view that
        allows you to see the inside of a part. The view is created by
        dividing the part with a single cutting plane.

        Pictorial Stepped Section Line lets you create a section view which
        contains linear steps. You can make these steps by indicating multiple
        cuts, bends, and arrow segments. All bend and arrow segments are
        created perpendicular to cut segments. """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class PointAndAngleSectionLineBuilder(NXOpen.TaggedObject): 
    """ Represents a NXOpen.Drawings.PointAndAngleSectionLineBuilder.
        This class is used to create or edit a
        NXOpen.Drawings.PointAndAngleSectionLine. """
    @property
    def EndLocation1(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) EndLocation1
         Returns the end location 1 which determines the position of the
                    first arrow segment in the section line.  
             
         
        """
        pass
    @EndLocation1.setter
    def EndLocation1(self, endLocation1: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) EndLocation1
         Returns the end location 1 which determines the position of the
                    first arrow segment in the section line.  
             
         
        """
        pass
    @property
    def EndLocation2(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) EndLocation2
         Returns the end location 2 which determines the position of the
                    second arrow segment in the section line   
            
         
        """
        pass
    @EndLocation2.setter
    def EndLocation2(self, endLocation2: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) EndLocation2
         Returns the end location 2 which determines the position of the
                    second arrow segment in the section line   
            
         
        """
        pass
    @property
    def Leg1(self) -> SectionLineSegmentBuilderList:
        """
        Getter for property: ( SectionLineSegmentBuilderList NXOpen.) Leg1
         Returns the list of cut segments.  
          
                    The list will contain  NXOpen::Drawings::SectionLineSegmentBuilder 
                    segments of type  NXOpen::Drawings::SectionLineSegmentBuilder::TypesAngle  only.
                    Note that the segments are added in the order that they appear in this list.   
         
        """
        pass
class PointAndAngleSectionLine(SectionLine): 
    """ Point and Angle Section Line lets you create a view with multiple
        segment cuts with no bends. The section line is defined by a
        set of rotation points and angles. """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class PointToPointSectionLineBuilder(NXOpen.TaggedObject): 
    """ Represents a NXOpen.Drawings.PointToPointSectionLineBuilder.
        This class is used to create or edit a
        NXOpen.Drawings.PointToPointSectionLine. """
    @property
    def EndLocation1(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) EndLocation1
         Returns the end location 1 which determines the position of the
                    first arrow segment in the section line.  
             
         
        """
        pass
    @EndLocation1.setter
    def EndLocation1(self, endLocation1: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) EndLocation1
         Returns the end location 1 which determines the position of the
                    first arrow segment in the section line.  
             
         
        """
        pass
    @property
    def EndLocation2(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) EndLocation2
         Returns the end location 2 which determines the position of the
                    second arrow segment in the section line   
            
         
        """
        pass
    @EndLocation2.setter
    def EndLocation2(self, endLocation2: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) EndLocation2
         Returns the end location 2 which determines the position of the
                    second arrow segment in the section line   
            
         
        """
        pass
    @property
    def Leg1(self) -> SectionLineSegmentBuilderList:
        """
        Getter for property: ( SectionLineSegmentBuilderList NXOpen.) Leg1
         Returns the list of cut segments.  
          
                    The list will contain  NXOpen::Drawings::SectionLineSegmentBuilder::TypesCut 
                    type  NXOpen::Drawings::SectionLineSegmentBuilder  segments only.
                    Note that there is no order to the elements of this list since the order is
                    determined by the hinge or arrow direction.   
         
        """
        pass
class PointToPointSectionLine(BasePointToPointSectionLine): 
    """ Point to Point Section Line lets you create a view with multiple
        segment cuts with no bends.  The section line is defined by
        a set of rotation points. """
    pass
import NXOpen
class ProjectedViewBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Drawings.ProjectedView builder """
    @property
    def HiddenObjects(self) -> HiddenObjectsBuilder:
        """
        Getter for property: ( HiddenObjectsBuilder NXOpen.) HiddenObjects
         Returns the list of objects to not show in the view   
            
         
        """
        pass
    @property
    def NonSectionedObjects(self) -> HiddenObjectsBuilder:
        """
        Getter for property: ( HiddenObjectsBuilder NXOpen.) NonSectionedObjects
         Returns the list of objects to not section in the view   
            
         
        """
        pass
    @property
    def Parent(self) -> ParentViewBuilder:
        """
        Getter for property: ( ParentViewBuilder NXOpen.) Parent
         Returns the parent view   
            
         
        """
        pass
    @property
    def Placement(self) -> ViewPlacementBuilder:
        """
        Getter for property: ( ViewPlacementBuilder NXOpen.) Placement
         Returns the view position   
            
         
        """
        pass
    @property
    def SecondaryComponents(self) -> DraftingComponentSelectionBuilder:
        """
        Getter for property: ( DraftingComponentSelectionBuilder NXOpen.) SecondaryComponents
         Returns the list of secondary components in the view   
            
         
        """
        pass
    @property
    def Style(self) -> ViewStyleBuilder:
        """
        Getter for property: ( ViewStyleBuilder NXOpen.) Style
         Returns the view style   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ProjectedViewOrientationBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.Drawings.ProjectedViewOrientationBuilder
    """
    @property
    def NormalDirection(self) -> NXOpen.Xform:
        """
        Getter for property: ( NXOpen.Xform) NormalDirection
         Returns the xform that represents the orthographic projected view settings to be edited   
            
         
        """
        pass
    @NormalDirection.setter
    def NormalDirection(self, normalDirection: NXOpen.Xform):
        """
        Setter for property: ( NXOpen.Xform) NormalDirection
         Returns the xform that represents the orthographic projected view settings to be edited   
            
         
        """
        pass
    @property
    def XDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) XDirection
         Returns the x direction vector for the orthographic projected view settings to be edited   
            
         
        """
        pass
    @XDirection.setter
    def XDirection(self, xDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) XDirection
         Returns the x direction vector for the orthographic projected view settings to be edited   
            
         
        """
        pass
    def Restore(self) -> None:
        """
         Removes the associativity to the defined plane and x direction vector and restores 
                    the member view to its default orientation. 
                
        """
        pass
import NXOpen
import NXOpen.Preferences
class ProjectedViewStyle(NXOpen.Object): 
    """ Represents set of Projected View Style Preferences applicable to drafting views. """
    pass
class ProjectedView(DraftingView): 
    """ Represents a Projected View. This can be Auxilary View or Orthographic View """
    pass
class ReferenceShowTypes(Enum):
    """
    Members Include: 
     |SheetandZone| 
     |Sheet| 
     |Zone| 

    """
    SheetandZone: int
    Sheet: int
    Zone: int
    @staticmethod
    def ValueOf(value: int) -> ReferenceShowTypes:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class RefineDisplayBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Drawings.RefineDisplayBuilder.  This class is
    used to refine regions of lightweight drawing views.
    """
    @property
    def BoundaryPoint1(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) BoundaryPoint1
         Returns 
                the boundary point1 in drawing coordinates.  
            This represents one of the points which defines the region to
                to be refined. 
                If both boundary point1 and point2, are outside the view boundary, the view will not be refined
                  
         
        """
        pass
    @BoundaryPoint1.setter
    def BoundaryPoint1(self, boundaryPoint1: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) BoundaryPoint1
         Returns 
                the boundary point1 in drawing coordinates.  
            This represents one of the points which defines the region to
                to be refined. 
                If both boundary point1 and point2, are outside the view boundary, the view will not be refined
                  
         
        """
        pass
    @property
    def BoundaryPoint2(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) BoundaryPoint2
         Returns 
                the boundary point2 in drawing coordinates.  
            This represents one of the points which defines the region to
                to be refined. 
                If both boundary point1 and point2, are outside the view boundary, the view will not be refined
                  
         
        """
        pass
    @BoundaryPoint2.setter
    def BoundaryPoint2(self, boundaryPoint2: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) BoundaryPoint2
         Returns 
                the boundary point2 in drawing coordinates.  
            This represents one of the points which defines the region to
                to be refined. 
                If both boundary point1 and point2, are outside the view boundary, the view will not be refined
                  
         
        """
        pass
    @property
    def View(self) -> SelectDraftingView:
        """
        Getter for property: ( SelectDraftingView NXOpen.) View
         Returns the view to refine.  
            This must be a lightweight drawing view   
         
        """
        pass
import NXOpen
class RemoveObjectsBuilder(NXOpen.Builder): 
    """ Creates the builder for removing associated objects from the region   """
    @property
    def Selection(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Selection
         Returns the selection   
            
         
        """
        pass
    def SetRegion(self, region: DrawingRegion) -> None:
        """
         Set the region 
        """
        pass
import NXOpen
class RenderSet(NXOpen.NXObject): 
    """ Represents a RenderSet."""
    pass
import NXOpen
class ReportBuilder(NXOpen.Builder): 
    """
    Represents a Drawings.ReportBuilder.
    This class queries and sets settings specific to drafting data which will get converted to PMI.
    """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class RevolvedSectionLineBuilder(NXOpen.TaggedObject): 
    """ Represents a NXOpen.Drawings.RevolvedSectionLineBuilder.
        This class is used to create or edit a
        NXOpen.Drawings.RevolvedSectionLine. """
    @property
    def EndLocation1(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) EndLocation1
         Returns the end location 1 which determines the position of the
                    first arrow segment in the section line.  
             
         
        """
        pass
    @EndLocation1.setter
    def EndLocation1(self, endLocation1: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) EndLocation1
         Returns the end location 1 which determines the position of the
                    first arrow segment in the section line.  
             
         
        """
        pass
    @property
    def EndLocation2(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) EndLocation2
         Returns the end location 2 which determines the position of the
                    second arrow segment in the section line   
            
         
        """
        pass
    @EndLocation2.setter
    def EndLocation2(self, endLocation2: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) EndLocation2
         Returns the end location 2 which determines the position of the
                    second arrow segment in the section line   
            
         
        """
        pass
    @property
    def Leg1(self) -> SectionLineSegmentBuilderList:
        """
        Getter for property: ( SectionLineSegmentBuilderList NXOpen.) Leg1
         Returns the list of cut and bend segments for the first leg.  
          
                    The list will contain  NXOpen::Drawings::SectionLineSegmentBuilder::TypesCut 
                    and  NXOpen::Drawings::SectionLineSegmentBuilder::TypesBend  types
                    of  NXOpen::Drawings::SectionLineSegmentBuilder  segments.
                    Note that there is no order to the elements of this list since the order is
                    determined by the hinge and arrow direction.   
         
        """
        pass
    @property
    def Leg2(self) -> SectionLineSegmentBuilderList:
        """
        Getter for property: ( SectionLineSegmentBuilderList NXOpen.) Leg2
         Returns the list of cut and bend segments for the second leg.  
            This leg is
                    not valid if the single leg indicator is set.
                    The list will contain  NXOpen::Drawings::SectionLineSegmentBuilder::TypesCut 
                    and  NXOpen::Drawings::SectionLineSegmentBuilder::TypesBend  types
                    of  NXOpen::Drawings::SectionLineSegmentBuilder  segments.
                    Note that there is no order to the elements of this list since the order is
                    determined by the hinge and arrow direction.   
         
        """
        pass
    @property
    def RotationPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) RotationPoint
         Returns the rotation point.  
            The rotation point identifies position of the axis that
                    the section line is to revolve about.   
         
        """
        pass
    @RotationPoint.setter
    def RotationPoint(self, rotationPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) RotationPoint
         Returns the rotation point.  
            The rotation point identifies position of the axis that
                    the section line is to revolve about.   
         
        """
        pass
    @property
    def SingleLeg(self) -> bool:
        """
        Getter for property: (bool) SingleLeg
         Returns the single leg indicator.  
            Set this flag to true to create a revolved section line that
                    contains only one leg.   
         
        """
        pass
    @SingleLeg.setter
    def SingleLeg(self, singleLeg: bool):
        """
        Setter for property: (bool) SingleLeg
         Returns the single leg indicator.  
            Set this flag to true to create a revolved section line that
                    contains only one leg.   
         
        """
        pass
class RevolvedSectionLine(SectionLine): 
    """ Revolved Section Line is used to create section views which are
        revolved about an axis.  A revolved section line can contain a
        single revolved cut, or it can contain steps to form multiple cuts.
        In either case, all cut planes resulting from the section line cuts
        are revolved into a common plane for the Revolved Section View. """
    pass
class RotationSymbolTypes(Enum):
    """
    Members Include: 
     |NotSet| 
     |Full| 
     |Right| 
     |Left| 

    """
    NotSet: int
    Full: int
    Right: int
    Left: int
    @staticmethod
    def ValueOf(value: int) -> RotationSymbolTypes:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class ScalePositionTypes(Enum):
    """
    Members Include: 
     |Above| 
     |Below| 
     |Before| 
     |After| 

    """
    Above: int
    Below: int
    Before: int
    After: int
    @staticmethod
    def ValueOf(value: int) -> ScalePositionTypes:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class ScaleValueFormatTypes(Enum):
    """
    Members Include: 
     |Ratio| 
     |CommonFraction| 
     |SingleLineFraction| 
     |Nx| 

    """
    Ratio: int
    CommonFraction: int
    SingleLineFraction: int
    Nx: int
    @staticmethod
    def ValueOf(value: int) -> ScaleValueFormatTypes:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class SecondaryGeometryInViewsBuilder(NXOpen.Builder): 
    """ This builder allows the user to select existing view(s) in which
        component objects can be designated as secondary or primary """
    @property
    def Components(self) -> DraftingComponentSelectionBuilder:
        """
        Getter for property: ( DraftingComponentSelectionBuilder NXOpen.) Components
         Returns the components   
            
         
        """
        pass
    @property
    def Views(self) -> SelectDraftingViewList:
        """
        Getter for property: ( SelectDraftingViewList NXOpen.) Views
         Returns the views   
            
         
        """
        pass
import NXOpen
class SectionInViewBuilder(NXOpen.Builder): 
    """ This builder allows the user to select a view in which component or
        solid body objects can be designated as section, non-sectioned, or neither """
    class EditSxtype(Enum):
        """
        Members Include: 
         |MakeNonSectioned| 
         |MakeSectioned| 
         |RemoveViewSpecific| 

        """
        MakeNonSectioned: int
        MakeSectioned: int
        RemoveViewSpecific: int
        @staticmethod
        def ValueOf(value: int) -> SectionInViewBuilder.EditSxtype:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EditObjects(self) -> HiddenObjectsBuilder:
        """
        Getter for property: ( HiddenObjectsBuilder NXOpen.) EditObjects
         Returns the objects   
            
         
        """
        pass
    @property
    def EditType(self) -> SectionInViewBuilder.EditSxtype:
        """
        Getter for property: ( SectionInViewBuilder.EditSxtype NXOpen.) EditType
         Returns the type   
            
         
        """
        pass
    @EditType.setter
    def EditType(self, editType: SectionInViewBuilder.EditSxtype):
        """
        Setter for property: ( SectionInViewBuilder.EditSxtype NXOpen.) EditType
         Returns the type   
            
         
        """
        pass
    @property
    def Views(self) -> SelectDraftingViewList:
        """
        Getter for property: ( SelectDraftingViewList NXOpen.) Views
         Returns the views   
            
         
        """
        pass
import NXOpen
class SectionLineBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Drawings.SectionLineBuilder.
        This class is used to create or edit a
        NXOpen.Drawings.SectionLine. """
    class Types(Enum):
        """
        Members Include: 
         |SimpleOrStepped|  Creates or edits a NXOpen.Drawings.SteppedSectionLine 
         |Half|  Creates or edits a NXOpen.Drawings.HalfSectionLine 
         |Revolved|  Creates or edits a NXOpen.Drawings.RevolvedSectionLine 
         |PointToPoint|  Creates or edits a NXOpen.Drawings.PointToPointSectionLine 
         |PointAndAngle|  Creates or edits a NXOpen.Drawings.PointAndAngleSectionLine 
         |Pictorial|  Creates or edits a NXOpen.Drawings.PictorialSectionLine 
         |HalfPictorial|  Creates or edits a NXOpen.Drawings.HalfPictorialSectionLine 
         |Oriented|  Creates or edits a NXOpen.Drawings.OrientedSectionLine 

        """
        SimpleOrStepped: int
        Half: int
        Revolved: int
        PointToPoint: int
        PointAndAngle: int
        Pictorial: int
        HalfPictorial: int
        Oriented: int
        @staticmethod
        def ValueOf(value: int) -> SectionLineBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ArrowDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ArrowDirection
         Returns the arrow direction.  
            The arrow direction defines the direction of
                    the section line arrows and must be perpendicular to the cut
                    direction.
                    The arrow direction is only used for
                     NXOpen::Drawings::SectionLineBuilder::TypesPictorial  ,
                     NXOpen::Drawings::SectionLineBuilder::TypesHalfPictorial  and
                     NXOpen::Drawings::SectionLineBuilder::TypesOriented  section lines   
         
        """
        pass
    @ArrowDirection.setter
    def ArrowDirection(self, arrowDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ArrowDirection
         Returns the arrow direction.  
            The arrow direction defines the direction of
                    the section line arrows and must be perpendicular to the cut
                    direction.
                    The arrow direction is only used for
                     NXOpen::Drawings::SectionLineBuilder::TypesPictorial  ,
                     NXOpen::Drawings::SectionLineBuilder::TypesHalfPictorial  and
                     NXOpen::Drawings::SectionLineBuilder::TypesOriented  section lines   
         
        """
        pass
    @property
    def CutDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) CutDirection
         Returns the cut direction.  
            The cut direction is a vector that specifies
                    the direction of the cutting plane. A vector arrow displays showing
                    the direction of the vector.
                    The cut direction is only used for
                     NXOpen::Drawings::SectionLineBuilder::TypesPictorial  ,
                     NXOpen::Drawings::SectionLineBuilder::TypesHalfPictorial  and
                     NXOpen::Drawings::SectionLineBuilder::TypesOriented  section lines   
         
        """
        pass
    @CutDirection.setter
    def CutDirection(self, cutDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) CutDirection
         Returns the cut direction.  
            The cut direction is a vector that specifies
                    the direction of the cutting plane. A vector arrow displays showing
                    the direction of the vector.
                    The cut direction is only used for
                     NXOpen::Drawings::SectionLineBuilder::TypesPictorial  ,
                     NXOpen::Drawings::SectionLineBuilder::TypesHalfPictorial  and
                     NXOpen::Drawings::SectionLineBuilder::TypesOriented  section lines   
         
        """
        pass
    @property
    def Half(self) -> HalfSectionLineBuilder:
        """
        Getter for property: ( HalfSectionLineBuilder NXOpen.) Half
         Returns the half section line data.  
          
                    Use the half section line data when the type is set to
                     NXOpen::Drawings::SectionLineBuilder::TypesHalf    
         
        """
        pass
    @property
    def HalfPictorial(self) -> HalfSectionLineBuilder:
        """
        Getter for property: ( HalfSectionLineBuilder NXOpen.) HalfPictorial
         Returns the half pictorial section line data.  
          
                    Use the half pictorial section line data when the type is set to
                     NXOpen::Drawings::SectionLineBuilder::TypesHalfPictorial    
         
        """
        pass
    @property
    def HingeDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) HingeDirection
         Returns the hinge direction.  
          
                    The hinge direction is only used for 
                     NXOpen::Drawings::SectionLineBuilder::TypesSimpleOrStepped  ,
                     NXOpen::Drawings::SectionLineBuilder::TypesHalf  ,
                     NXOpen::Drawings::SectionLineBuilder::TypesRevolved  ,
                     NXOpen::Drawings::SectionLineBuilder::TypesPointToPoint  , and
                     NXOpen::Drawings::SectionLineBuilder::TypesPointAndAngle  section lines   
         
        """
        pass
    @HingeDirection.setter
    def HingeDirection(self, hingeDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) HingeDirection
         Returns the hinge direction.  
          
                    The hinge direction is only used for 
                     NXOpen::Drawings::SectionLineBuilder::TypesSimpleOrStepped  ,
                     NXOpen::Drawings::SectionLineBuilder::TypesHalf  ,
                     NXOpen::Drawings::SectionLineBuilder::TypesRevolved  ,
                     NXOpen::Drawings::SectionLineBuilder::TypesPointToPoint  , and
                     NXOpen::Drawings::SectionLineBuilder::TypesPointAndAngle  section lines   
         
        """
        pass
    @property
    def Oriented(self) -> OrientedSectionLineBuilder:
        """
        Getter for property: ( OrientedSectionLineBuilder NXOpen.) Oriented
         Returns the simple 3D section line data.  
          
                    Use the simple 3D section line data when the type is set to
                     NXOpen::Drawings::SectionLineBuilder::TypesOriented    
         
        """
        pass
    @property
    def ParentView(self) -> ParentViewBuilder:
        """
        Getter for property: ( ParentViewBuilder NXOpen.) ParentView
         Returns the parent view.  
            The view that the section line will cut.   
         
        """
        pass
    @property
    def Pictorial(self) -> SteppedSectionLineBuilder:
        """
        Getter for property: ( SteppedSectionLineBuilder NXOpen.) Pictorial
         Returns the pictorial section line data.  
          
                    Use the pictorial section line data when the type is set to
                     NXOpen::Drawings::SectionLineBuilder::TypesPictorial    
         
        """
        pass
    @property
    def PointAndAngle(self) -> PointAndAngleSectionLineBuilder:
        """
        Getter for property: ( PointAndAngleSectionLineBuilder NXOpen.) PointAndAngle
         Returns the point and angle section line data.  
          
                    Use the point and angle section line data when the type is set to
                     NXOpen::Drawings::SectionLineBuilder::TypesPointAndAngle    
         
        """
        pass
    @property
    def PointToPoint(self) -> PointToPointSectionLineBuilder:
        """
        Getter for property: ( PointToPointSectionLineBuilder NXOpen.) PointToPoint
         Returns the point to point section line data.  
          
                    Use the point to point section line data when the type is set to
                     NXOpen::Drawings::SectionLineBuilder::TypesPointToPoint    
         
        """
        pass
    @property
    def Revolved(self) -> RevolvedSectionLineBuilder:
        """
        Getter for property: ( RevolvedSectionLineBuilder NXOpen.) Revolved
         Returns the revolved section line data.  
          
                    Use the revolved section line data when the type is set to
                     NXOpen::Drawings::SectionLineBuilder::TypesRevolved    
         
        """
        pass
    @property
    def SimpleOrStepped(self) -> SteppedSectionLineBuilder:
        """
        Getter for property: ( SteppedSectionLineBuilder NXOpen.) SimpleOrStepped
         Returns the simple or stepped section line data.  
          
                    Use the simple or stepped section line data when the type is set to
                     NXOpen::Drawings::SectionLineBuilder::TypesSimpleOrStepped    
         
        """
        pass
    @property
    def Style(self) -> SectionLineStyleBuilder:
        """
        Getter for property: ( SectionLineStyleBuilder NXOpen.) Style
         Returns the style.  
            The preferences of a section line.   
         
        """
        pass
    @property
    def Type(self) -> SectionLineBuilder.Types:
        """
        Getter for property: ( SectionLineBuilder.Types NXOpen.) Type
         Returns the section line type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: SectionLineBuilder.Types):
        """
        Setter for property: ( SectionLineBuilder.Types NXOpen.) Type
         Returns the section line type   
            
         
        """
        pass
import NXOpen
import NXOpen.Annotations
class SectionLineCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Drawings.SectionLines.   """
    def CreateSectionLineBuilder(self, sectionLine: SectionLine) -> SectionLineBuilder:
        """
         Creates the section line builder 
         Returns builder ( SectionLineBuilder NXOpen.): .
        """
        pass
    def CreateSectionLineSegmentBuilder(self) -> SectionLineSegmentBuilder:
        """
         Creates the section line segment builder 
         Returns builder ( SectionLineSegmentBuilder NXOpen.): .
        """
        pass
    def CreateSectionLineStyleBuilder(self, sectionline: SectionLine) -> SectionLineStyleBuilder:
        """
         Creates the Section Line Style Builder 
         Returns builder ( SectionLineStyleBuilder NXOpen.): .
        """
        pass
    def CreateSketchSectionLineBuilder(self, sectionLine: SectionLine) -> SketchSectionLineBuilder:
        """
         Creates the Sketch Section Line builder 
         Returns builder ( SketchSectionLineBuilder NXOpen.): .
        """
        pass
    def GenerateSectionLineLabelAttribute(self, note: NXOpen.Annotations.BaseNote) -> str:
        """
         Generates a parametric text attribute that is similar to the current section line label but contains the section line segment information.
                Note that the text in the section line note is not overwritten.
                
         Returns attribute (str): .
        """
        pass
import NXOpen
class SectionLineSegmentBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[SectionLineSegmentBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: SectionLineSegmentBuilder) -> None:
        """
         Appends an object to the list
            
        """
        pass
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
               not change, but the item at this index is set to NULL.
            
        """
        pass
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, obj: SectionLineSegmentBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: SectionLineSegmentBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: SectionLineSegmentBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> SectionLineSegmentBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( SectionLineSegmentBuilder NXOpen.):  object found at input index .
        """
        pass
    def GetContents(self) -> List[SectionLineSegmentBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( SectionLineSegmentBuilder List[NXOpe):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: SectionLineSegmentBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    def SetContents(self, objects: List[SectionLineSegmentBuilder]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    @overload
    def Swap(self, object1: SectionLineSegmentBuilder, object2: SectionLineSegmentBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SectionLineSegmentBuilder(NXOpen.TaggedObject): 
    """ Represents a NXOpen.Drawings.SectionLineSegmentBuilder.
        This class is used by the following classes to create andor edit a
        section line segment:
            NXOpen.Drawings.SteppedSectionLine
            NXOpen.Drawings.RevolvedSectionLine
            NXOpen.Drawings.PointToPointSectionLine
            NXOpen.Drawings.PointAndAngleSectionLine
            NXOpen.Drawings.PictorialSectionLine """
    class Types(Enum):
        """
        Members Include: 
         |Angle|  Section line cut segment used by:
                                                                     NXOpen.Drawings.PointAndAngleSectionLineBuilder. 
         |Cut|  Section line cut segment used by:
                                                                     NXOpen.Drawings.PointToPointSectionLineBuilder
                                                                     NXOpen.Drawings.RevolvedSectionLineBuilder
                                                                     NXOpen.Drawings.SteppedSectionLineBuilder 
         |Bend|  Section line bend segment used by:
                                                                     NXOpen.Drawings.PointToPointSectionLineBuilder
                                                                     NXOpen.Drawings.RevolvedSectionLineBuilder
                                                                     NXOpen.Drawings.SteppedSectionLineBuilder 

        """
        Angle: int
        Cut: int
        Bend: int
        @staticmethod
        def ValueOf(value: int) -> SectionLineSegmentBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Angle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Angle
         Returns the angle.  
            The segment angle is only valid for segments of type 
                  NXOpen::Drawings::SectionLineSegmentBuilder::TypesAngle  .
                The angle is defined to be the angle between the drawing's X direction
                and the segment.   
         
        """
        pass
    @property
    def Point(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Point
         Returns the point   
            
         
        """
        pass
    @Point.setter
    def Point(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Point
         Returns the point   
            
         
        """
        pass
    @property
    def Type(self) -> SectionLineSegmentBuilder.Types:
        """
        Getter for property: ( SectionLineSegmentBuilder.Types NXOpen.) Type
         Returns the section line segment type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: SectionLineSegmentBuilder.Types):
        """
        Setter for property: ( SectionLineSegmentBuilder.Types NXOpen.) Type
         Returns the section line segment type   
            
         
        """
        pass
import NXOpen
class SectionLineSegmentPointBuilder(NXOpen.TaggedObject): 
    """ Represents Section Line Segment Point Builder  """
    class SegmentTypes(Enum):
        """
        Members Include: 
         |Arrow| 
         |Cut| 
         |Bend| 

        """
        Arrow: int
        Cut: int
        Bend: int
        @staticmethod
        def ValueOf(value: int) -> SectionLineSegmentPointBuilder.SegmentTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Point(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Point
         Returns the section line segment  NXOpen::Point    
            
         
        """
        pass
    @Point.setter
    def Point(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Point
         Returns the section line segment  NXOpen::Point    
            
         
        """
        pass
    @property
    def SegmentType(self) -> SectionLineSegmentPointBuilder.SegmentTypes:
        """
        Getter for property: ( SectionLineSegmentPointBuilder.SegmentTypes NXOpen.) SegmentType
         Returns the segment type  
            
         
        """
        pass
    @SegmentType.setter
    def SegmentType(self, type: SectionLineSegmentPointBuilder.SegmentTypes):
        """
        Setter for property: ( SectionLineSegmentPointBuilder.SegmentTypes NXOpen.) SegmentType
         Returns the segment type  
            
         
        """
        pass
import NXOpen
class SectionLineSegmentPointListBuilder(NXOpen.TaggedObject): 
    """ Represents SectionLineSegmentPointListBuilder class.
        This class maintains a list of NXOpen.Drawings.SectionLineSegmentPointBuilder objects
        and manages them.
    """
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the number of  NXOpen::Drawings::SectionLineSegmentPointBuilder  objects in the list   
            
         
        """
        pass
    @overload
    def AddCutSegment(self, location: NXOpen.Point) -> SectionLineSegmentPointBuilder:
        """
         Creates a new NXOpen.Drawings.SectionLineSegmentPointBuilder object 
         Returns data ( SectionLineSegmentPointBuilder NXOpen.):  .
        """
        pass
    @overload
    def AddCutSegment(self, location: NXOpen.Point, referencedCutSegment: SectionLineSegmentPointBuilder) -> SectionLineSegmentPointBuilder:
        """
         Creates a new NXOpen.Drawings.SectionLineSegmentPointBuilder
                     In case of point to point section line ,new segment is added at location prior to reference cut segment specified.
                     If reference cut segment is not specified , new segment is added prior to last arrow segment.
         Returns data ( SectionLineSegmentPointBuilder NXOpen.):  .
        """
        pass
    def Append(self, pointData: SectionLineSegmentPointBuilder) -> None:
        """
         Appends NXOpen.Drawings.SectionLineSegmentPointBuilder object to the end of the list 
        """
        pass
    def Clear(self) -> None:
        """
         Deletes all NXOpen.Drawings.SectionLineSegmentPointBuilder objects from the list 
        """
        pass
    def CreateSectionLineSegmentPointBuilder(self) -> SectionLineSegmentPointBuilder:
        """
         Creates a new NXOpen.Drawings.SectionLineSegmentPointBuilder object 
         Returns data ( SectionLineSegmentPointBuilder NXOpen.):  .
        """
        pass
    @overload
    def Delete(self, point: SectionLineSegmentPointBuilder) -> None:
        """
         Deletes a given NXOpen.Drawings.SectionLineSegmentPointBuilder object from the list 
        """
        pass
    @overload
    def Delete(self, index: int) -> None:
        """
         Deletes NXOpen.Drawings.SectionLineSegmentPointBuilder object of a certain index from the list 
        """
        pass
    def FindItem(self, index: int) -> SectionLineSegmentPointBuilder:
        """
         Returns NXOpen.Drawings.SectionLineSegmentPointBuilder object at the input index. 
                    May be NULL if not found. 
         Returns points ( SectionLineSegmentPointBuilder NXOpen.):  object found at input index .
        """
        pass
    def GetContents(self) -> List[SectionLineSegmentPointBuilder]:
        """
         Queries all the NXOpen.Drawings.SectionLineSegmentPointBuilder objects 
         Returns points ( SectionLineSegmentPointBuilder List[NXOpe):  .
        """
        pass
    def GetIndex(self, point: SectionLineSegmentPointBuilder) -> int:
        """
         Finds index of NXOpen.Drawings.SectionLineSegmentPointBuilder object in the list 
         Returns index (int):  Equals -1 if not found .
        """
        pass
    def Insert(self, insert_before_index: int, point: SectionLineSegmentPointBuilder) -> None:
        """
         Inserts NXOpen.Drawings.SectionLineSegmentPointBuilder object in the list
                    before a given position 
        """
        pass
    def MoveSegment(self, point: SectionLineSegmentPointBuilder, pointspecified: NXOpen.Point) -> None:
        """
         Moves a given NXOpen.Drawings.SectionLineSegmentPointBuilder object from the list 
        """
        pass
    def SetContents(self, points: List[SectionLineSegmentPointBuilder]) -> None:
        """
         Sets array of NXOpen.Drawings.SectionLineSegmentPointBuilder objects in the list. 
        """
        pass
import NXOpen
class SectionLineSegmentsBuilder(NXOpen.TaggedObject): 
    """ Represents a class Drawings.SectionLineSegmentsBuilder.
    """
    @property
    def RotationPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) RotationPoint
         Returns the rotation point   
            
         
        """
        pass
    @RotationPoint.setter
    def RotationPoint(self, rotationPointTag: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) RotationPoint
         Returns the rotation point   
            
         
        """
        pass
    @property
    def SectionLineOnlyPlacementOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) SectionLineOnlyPlacementOrigin
         Returns the section line only placement origin center in inferred mode   
            
         
        """
        pass
    @SectionLineOnlyPlacementOrigin.setter
    def SectionLineOnlyPlacementOrigin(self, coordinates: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) SectionLineOnlyPlacementOrigin
         Returns the section line only placement origin center in inferred mode   
            
         
        """
        pass
    @property
    def SegmentLocation(self) -> SectionLineSegmentPointListBuilder:
        """
        Getter for property: ( SectionLineSegmentPointListBuilder NXOpen.) SegmentLocation
         Returns the segment location   
            
         
        """
        pass
    @property
    def SegmentLocationForSecondLeg(self) -> SectionLineSegmentPointListBuilder:
        """
        Getter for property: ( SectionLineSegmentPointListBuilder NXOpen.) SegmentLocationForSecondLeg
         Returns the segment location to add segments to revolved section line second leg   
            
         
        """
        pass
    @property
    def SingleLeg(self) -> bool:
        """
        Getter for property: (bool) SingleLeg
         Returns the single leg   
            
         
        """
        pass
    @SingleLeg.setter
    def SingleLeg(self, singleLeg: bool):
        """
        Setter for property: (bool) SingleLeg
         Returns the single leg   
            
         
        """
        pass
    def GetLongitudinalSectionData(self) -> Tuple[NXOpen.ICurve, float, float]:
        """
         Gets spline curve data for longitudinal section. 
         Returns A tuple consisting of (curve, startParam, endParam). 
         - curve is:  NXOpen.ICurve.
         - startParam is: float.
         - endParam is: float.

        """
        pass
    def SetLongitudinalSectionData(self, curve: NXOpen.ICurve, startParam: float, endParam: float) -> None:
        """
         Sets spline curve data for longitudinal section. 
                    The start parameter and the end parameter have to be on the valid part of the curve.
                    If curve is  then the existing curve will be used. 
        """
        pass
    def UpdateAfterParentViewMove(self) -> None:
        """
         Update the section line segments builder in case of parent view move 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SectionLineSettingsBuilder(NXOpen.TaggedObject): 
    """ Represents the Section Line Settings Builder (Drawings.SectionLineSettingsBuilder) which manages all the style attributes related
       to the section Line including label letter.
    """
    @property
    def ViewCommonViewLabel(self) -> ViewCommonViewLabelBuilder:
        """
        Getter for property: ( ViewCommonViewLabelBuilder NXOpen.) ViewCommonViewLabel
         Returns the view Common View label builder   
            
         
        """
        pass
    @property
    def ViewSectionLine(self) -> ViewSectionLineBuilder:
        """
        Getter for property: ( ViewSectionLineBuilder NXOpen.) ViewSectionLine
         Returns the Section Line builder   
            
         
        """
        pass
    def InheritSettingsFromCustomerDefault(self) -> None:
        """
         Inherit Settings From Customer Default 
        """
        pass
    def InheritSettingsFromPreferences(self) -> None:
        """
         Inherit Settings From Preference 
        """
        pass
    def InheritSettingsFromSelectedObjects(self, selectedObject: SectionLine) -> None:
        """
         Inherit Settings From Selected Objects 
        """
        pass
import NXOpen
class SectionLineStyleBuilder(NXOpen.Builder): 
    """ Represents a Drawings.SectionLineStyleBuiler.
        The SectionLineStyleBuilder is used to specify section line style.
    """
    class ArrowheadStyleType(Enum):
        """
        Members Include: 
         |Open| 
         |Closed| 
         |Filled| 

        """
        Open: int
        Closed: int
        Filled: int
        @staticmethod
        def ValueOf(value: int) -> SectionLineStyleBuilder.ArrowheadStyleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CreateSectionLineType(Enum):
        """
        Members Include: 
         |WithView| 
         |WithoutView| 

        """
        WithView: int
        WithoutView: int
        @staticmethod
        def ValueOf(value: int) -> SectionLineStyleBuilder.CreateSectionLineType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FontStyle(Enum):
        """
        Members Include: 
         |NotSet| 
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
        NotSet: int
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
        def ValueOf(value: int) -> SectionLineStyleBuilder.FontStyle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LabelLocationStyle(Enum):
        """
        Members Include: 
         |OnArrow| 
         |OnEnd| 

        """
        OnArrow: int
        OnEnd: int
        @staticmethod
        def ValueOf(value: int) -> SectionLineStyleBuilder.LabelLocationStyle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StandardStyle(Enum):
        """
        Members Include: 
         |AnsiStandard| 
         |IsoStandard| 
         |Iso128Standard| 
         |JisStandard| 
         |GbStandard| 
         |EskdStandard| 

        """
        AnsiStandard: int
        IsoStandard: int
        Iso128Standard: int
        JisStandard: int
        GbStandard: int
        EskdStandard: int
        @staticmethod
        def ValueOf(value: int) -> SectionLineStyleBuilder.StandardStyle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class WidthStyle(Enum):
        """
        Members Include: 
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
        def ValueOf(value: int) -> SectionLineStyleBuilder.WidthStyle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ArrowLength(self) -> float:
        """
        Getter for property: (float) ArrowLength
         Returns the arrow length   
            
         
        """
        pass
    @ArrowLength.setter
    def ArrowLength(self, arrowLength: float):
        """
        Setter for property: (float) ArrowLength
         Returns the arrow length   
            
         
        """
        pass
    @property
    def ArrowheadAngle(self) -> float:
        """
        Getter for property: (float) ArrowheadAngle
         Returns the arrowhead angle   
            
         
        """
        pass
    @ArrowheadAngle.setter
    def ArrowheadAngle(self, arrowheadAngle: float):
        """
        Setter for property: (float) ArrowheadAngle
         Returns the arrowhead angle   
            
         
        """
        pass
    @property
    def ArrowheadLength(self) -> float:
        """
        Getter for property: (float) ArrowheadLength
         Returns the arrowhead length   
            
         
        """
        pass
    @ArrowheadLength.setter
    def ArrowheadLength(self, arrowheadLength: float):
        """
        Setter for property: (float) ArrowheadLength
         Returns the arrowhead length   
            
         
        """
        pass
    @property
    def ArrowheadStyle(self) -> SectionLineStyleBuilder.ArrowheadStyleType:
        """
        Getter for property: ( SectionLineStyleBuilder.ArrowheadStyleType NXOpen.) ArrowheadStyle
         Returns the arrowhead style   
            
         
        """
        pass
    @ArrowheadStyle.setter
    def ArrowheadStyle(self, arrowheadStyle: SectionLineStyleBuilder.ArrowheadStyleType):
        """
        Setter for property: ( SectionLineStyleBuilder.ArrowheadStyleType NXOpen.) ArrowheadStyle
         Returns the arrowhead style   
            
         
        """
        pass
    @property
    def BorderToArrowDistance(self) -> float:
        """
        Getter for property: (float) BorderToArrowDistance
         Returns the border to arrow distance   
            
         
        """
        pass
    @BorderToArrowDistance.setter
    def BorderToArrowDistance(self, borderToArrowDistance: float):
        """
        Setter for property: (float) BorderToArrowDistance
         Returns the border to arrow distance   
            
         
        """
        pass
    @property
    def CreateSectionLine(self) -> SectionLineStyleBuilder.CreateSectionLineType:
        """
        Getter for property: ( SectionLineStyleBuilder.CreateSectionLineType NXOpen.) CreateSectionLine
         Returns a value that indicates whether or not to create a view for the section line   
            
         
        """
        pass
    @CreateSectionLine.setter
    def CreateSectionLine(self, createSectionLine: SectionLineStyleBuilder.CreateSectionLineType):
        """
        Setter for property: ( SectionLineStyleBuilder.CreateSectionLineType NXOpen.) CreateSectionLine
         Returns a value that indicates whether or not to create a view for the section line   
            
         
        """
        pass
    @property
    def DisplayJisrotationLetter(self) -> bool:
        """
        Getter for property: (bool) DisplayJisrotationLetter
         Returns the display jisrotation letter   
            
         
        """
        pass
    @DisplayJisrotationLetter.setter
    def DisplayJisrotationLetter(self, displayJISRotationLetter: bool):
        """
        Setter for property: (bool) DisplayJisrotationLetter
         Returns the display jisrotation letter   
            
         
        """
        pass
    @property
    def DisplayLabel(self) -> bool:
        """
        Getter for property: (bool) DisplayLabel
         Returns the display label   
            
         
        """
        pass
    @DisplayLabel.setter
    def DisplayLabel(self, displayLabel: bool):
        """
        Setter for property: (bool) DisplayLabel
         Returns the display label   
            
         
        """
        pass
    @property
    def Font(self) -> SectionLineStyleBuilder.FontStyle:
        """
        Getter for property: ( SectionLineStyleBuilder.FontStyle NXOpen.) Font
         Returns the font   
            
         
        """
        pass
    @Font.setter
    def Font(self, font: SectionLineStyleBuilder.FontStyle):
        """
        Setter for property: ( SectionLineStyleBuilder.FontStyle NXOpen.) Font
         Returns the font   
            
         
        """
        pass
    @property
    def LabelLocation(self) -> SectionLineStyleBuilder.LabelLocationStyle:
        """
        Getter for property: ( SectionLineStyleBuilder.LabelLocationStyle NXOpen.) LabelLocation
         Returns the label location   
            
         
        """
        pass
    @LabelLocation.setter
    def LabelLocation(self, labelLocation: SectionLineStyleBuilder.LabelLocationStyle):
        """
        Setter for property: ( SectionLineStyleBuilder.LabelLocationStyle NXOpen.) LabelLocation
         Returns the label location   
            
         
        """
        pass
    @property
    def Letter(self) -> str:
        """
        Getter for property: (str) Letter
         Returns the letter   
            
         
        """
        pass
    @Letter.setter
    def Letter(self, letter: str):
        """
        Setter for property: (str) Letter
         Returns the letter   
            
         
        """
        pass
    @property
    def LineLength(self) -> float:
        """
        Getter for property: (float) LineLength
         Returns the line length   
            
         
        """
        pass
    @LineLength.setter
    def LineLength(self, lineLength: float):
        """
        Setter for property: (float) LineLength
         Returns the line length   
            
         
        """
        pass
    @property
    def Offset(self) -> float:
        """
        Getter for property: (float) Offset
         Returns the offset   
            
         
        """
        pass
    @Offset.setter
    def Offset(self, offset: float):
        """
        Setter for property: (float) Offset
         Returns the offset   
            
         
        """
        pass
    @property
    def SelectLetter(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: ( NXOpen.SelectTaggedObject) SelectLetter
         Returns the selected note for jisrotation letter   
            
         
        """
        pass
    @property
    def Standard(self) -> SectionLineStyleBuilder.StandardStyle:
        """
        Getter for property: ( SectionLineStyleBuilder.StandardStyle NXOpen.) Standard
         Returns the standard   
            
         
        """
        pass
    @Standard.setter
    def Standard(self, standard: SectionLineStyleBuilder.StandardStyle):
        """
        Setter for property: ( SectionLineStyleBuilder.StandardStyle NXOpen.) Standard
         Returns the standard   
            
         
        """
        pass
    @property
    def StubLength(self) -> float:
        """
        Getter for property: (float) StubLength
         Returns the stub length   
            
         
        """
        pass
    @StubLength.setter
    def StubLength(self, stubLength: float):
        """
        Setter for property: (float) StubLength
         Returns the stub length   
            
         
        """
        pass
    @property
    def UseOffset(self) -> bool:
        """
        Getter for property: (bool) UseOffset
         Returns the use offset   
            
         
        """
        pass
    @UseOffset.setter
    def UseOffset(self, useOffset: bool):
        """
        Setter for property: (bool) UseOffset
         Returns the use offset   
            
         
        """
        pass
    @property
    def Width(self) -> SectionLineStyleBuilder.WidthStyle:
        """
        Getter for property: ( SectionLineStyleBuilder.WidthStyle NXOpen.) Width
         Returns the width   
            
         
        """
        pass
    @Width.setter
    def Width(self, width: SectionLineStyleBuilder.WidthStyle):
        """
        Setter for property: ( SectionLineStyleBuilder.WidthStyle NXOpen.) Width
         Returns the width   
            
         
        """
        pass
    def GetColor(self) -> NXOpen.NXColor:
        """
         Returns the color 
         Returns color ( NXOpen.NXColor): .
        """
        pass
    def SetColor(self, color: NXOpen.NXColor) -> None:
        """
         Sets the color 
        """
        pass
import NXOpen
class SectionLine(NXOpen.DisplayableObject): 
    """ Represents a Section Line."""
    @property
    def IsRetained(self) -> bool:
        """
        Getter for property: (bool) IsRetained
         Returns a flag indicating whether the section line is retained   
            
         
        """
        pass
import NXOpen
class SectionViewBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Drawings.SectionView builder """
    class SectionCutType(Enum):
        """
        Members Include: 
         |FullPart| 
         |SectionedPart| 

        """
        FullPart: int
        SectionedPart: int
        @staticmethod
        def ValueOf(value: int) -> SectionViewBuilder.SectionCutType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SectionLineType(Enum):
        """
        Members Include: 
         |SimpleStepped| 
         |Half| 
         |Revolved| 
         |PointToPoint| 
         |PointAndAngle| 

        """
        SimpleStepped: int
        Half: int
        Revolved: int
        PointToPoint: int
        PointAndAngle: int
        @staticmethod
        def ValueOf(value: int) -> SectionViewBuilder.SectionLineType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SectionViewModeType(Enum):
        """
        Members Include: 
         |Dynamic| 
         |StandAlone| 

        """
        Dynamic: int
        StandAlone: int
        @staticmethod
        def ValueOf(value: int) -> SectionViewBuilder.SectionViewModeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CreateFolded(self) -> bool:
        """
        Getter for property: (bool) CreateFolded
         Returns the create folded   
            
         
        """
        pass
    @CreateFolded.setter
    def CreateFolded(self, viewUnfolded: bool):
        """
        Setter for property: (bool) CreateFolded
         Returns the create folded   
            
         
        """
        pass
    @property
    def HiddenObjects(self) -> HiddenObjectsBuilder:
        """
        Getter for property: ( HiddenObjectsBuilder NXOpen.) HiddenObjects
         Returns the hidden objects   
            
         
        """
        pass
    @property
    def NonSectionedObjects(self) -> HiddenObjectsBuilder:
        """
        Getter for property: ( HiddenObjectsBuilder NXOpen.) NonSectionedObjects
         Returns the non sectioned objects   
            
         
        """
        pass
    @property
    def ParentView(self) -> ParentViewBuilder:
        """
        Getter for property: ( ParentViewBuilder NXOpen.) ParentView
         Returns the selected parent view   
            
         
        """
        pass
    @property
    def SecondaryComponents(self) -> DraftingComponentSelectionBuilder:
        """
        Getter for property: ( DraftingComponentSelectionBuilder NXOpen.) SecondaryComponents
         Returns the list of secondary objects in the view   
            
         
        """
        pass
    @property
    def SectionLine(self) -> SpecifySectionLineBuilder:
        """
        Getter for property: ( SpecifySectionLineBuilder NXOpen.) SectionLine
         Returns the section Line   
            
         
        """
        pass
    @property
    def SectionLineSegments(self) -> SectionLineSegmentsBuilder:
        """
        Getter for property: ( SectionLineSegmentsBuilder NXOpen.) SectionLineSegments
         Returns the section line segment builder   
            
         
        """
        pass
    @property
    def SectionViewMode(self) -> SectionViewBuilder.SectionViewModeType:
        """
        Getter for property: ( SectionViewBuilder.SectionViewModeType NXOpen.) SectionViewMode
         Returns the section line mode   
            
         
        """
        pass
    @SectionViewMode.setter
    def SectionViewMode(self, sectionViewMode: SectionViewBuilder.SectionViewModeType):
        """
        Setter for property: ( SectionViewBuilder.SectionViewModeType NXOpen.) SectionViewMode
         Returns the section line mode   
            
         
        """
        pass
    @property
    def SectionViewTool(self) -> SvtBuilder:
        """
        Getter for property: ( SvtBuilder NXOpen.) SectionViewTool
         Returns the section view tool   
            
         
        """
        pass
    @property
    def SectionViewType(self) -> SectionViewBuilder.SectionLineType:
        """
        Getter for property: ( SectionViewBuilder.SectionLineType NXOpen.) SectionViewType
         Returns the section line type   
            
         
        """
        pass
    @SectionViewType.setter
    def SectionViewType(self, sectionLineType: SectionViewBuilder.SectionLineType):
        """
        Setter for property: ( SectionViewBuilder.SectionLineType NXOpen.) SectionViewType
         Returns the section line type   
            
         
        """
        pass
    @property
    def ViewOrientation(self) -> ViewOrientationBuilder:
        """
        Getter for property: ( ViewOrientationBuilder NXOpen.) ViewOrientation
         Returns the view orientation   
            
         
        """
        pass
    @property
    def ViewPlacement(self) -> ViewPlacementBuilder:
        """
        Getter for property: ( ViewPlacementBuilder NXOpen.) ViewPlacement
         Returns the view placement   
            
         
        """
        pass
    @property
    def ViewStyle(self) -> ViewStyleBuilder:
        """
        Getter for property: ( ViewStyleBuilder NXOpen.) ViewStyle
         Returns the view style   
            
         
        """
        pass
    @property
    def ViewUnfolded(self) -> bool:
        """
        Getter for property: (bool) ViewUnfolded
         Returns the view unfolded toggle   
            
         
        """
        pass
    @ViewUnfolded.setter
    def ViewUnfolded(self, viewUnfolded: bool):
        """
        Setter for property: (bool) ViewUnfolded
         Returns the view unfolded toggle   
            
         
        """
        pass
import NXOpen
import NXOpen.Preferences
class SectionViewStyle(NXOpen.Object): 
    """ Represents set of Section View Style Preferences applicable to drafting views. """
    @property
    def AssemblyCrossHatching(self) -> bool:
        """
        Getter for property: (bool) AssemblyCrossHatching
         Returns the status of assembly cross hatching.  
           Controls the crosshatching angle
                    of adjacent solids in an assembly section view.  
                    Works when  Drawings::SectionViewStyle::CrossHatch  is True.  
                   
         
        """
        pass
    @AssemblyCrossHatching.setter
    def AssemblyCrossHatching(self, assembly_cross_hatching: bool):
        """
        Setter for property: (bool) AssemblyCrossHatching
         Returns the status of assembly cross hatching.  
           Controls the crosshatching angle
                    of adjacent solids in an assembly section view.  
                    Works when  Drawings::SectionViewStyle::CrossHatch  is True.  
                   
         
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
                    Works when  Drawings::SectionViewStyle::AssemblyCrossHatching  is True.  
                   
         
        """
        pass
    @CrosshatchAdjacencyTolarance.setter
    def CrosshatchAdjacencyTolarance(self, crosshatch_adjacency_tolarance: float):
        """
        Setter for property: (float) CrosshatchAdjacencyTolarance
         Returns the value of crosshatch adjacency tolarance.  
           Controls the crosshatching angle of adjacent 
                    solids in an assembly section view.  
                    Works when  Drawings::SectionViewStyle::AssemblyCrossHatching  is True.  
                   
         
        """
        pass
    @property
    def DisplaySectionLine(self) -> bool:
        """
        Getter for property: (bool) DisplaySectionLine
         Returns the status of display section line.  
           Suppress or display the sectio line in a section view.
                   
         
        """
        pass
    @DisplaySectionLine.setter
    def DisplaySectionLine(self, display_section_line: bool):
        """
        Setter for property: (bool) DisplaySectionLine
         Returns the status of display section line.  
           Suppress or display the sectio line in a section view.
                   
         
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
                    Works when  Drawings::SectionViewStyle::CrossHatch  is True.   
                   
         
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
                    Works when  Drawings::SectionViewStyle::CrossHatch  is True.   
                   
         
        """
        pass
    @property
    def RestrictCrosshatchAngle(self) -> bool:
        """
        Getter for property: (bool) RestrictCrosshatchAngle
         Returns    
            
         
        """
        pass
    @RestrictCrosshatchAngle.setter
    def RestrictCrosshatchAngle(self, restrict_crosshatch_angle: bool):
        """
        Setter for property: (bool) RestrictCrosshatchAngle
         Returns    
            
         
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
class SectionView(DraftingView): 
    """ Represents a Section View.  """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectDraftingViewList(NXOpen.TaggedObject): 
    """ Represents a list of objects on a selection list.
"""
    @property
    def DuplicatesAllowed(self) -> bool:
        """
        Getter for property: (bool) DuplicatesAllowed
         Returns whether duplicate objects are allowed in the selection list.  
          
              
         
        """
        pass
    @property
    def Size(self) -> int:
        """
        Getter for property: (int) Size
         Returns the number of objects in the list.  
          
              
         
        """
        pass
    @overload
    def Add(self, objectValue: DraftingView) -> bool:
        """
         Adds an object to the list
            
         Returns added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    def AddWithViews(self, objects: List[DraftingView], views: List[NXOpen.View]) -> bool:
        """
         Adds a set of objects with views to the list
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, objects: List[DraftingView]) -> bool:
        """
         Adds a set of objects to the list
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, input_selection_method: NXOpen.SelectionMethod) -> bool:
        """
         Adds the objects from a SelectionMethod to the list
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, selection: DraftingView, view: NXOpen.View, point: NXOpen.Point3d) -> bool:
        """
         Adds the object with the objects view and objects point
            
         Returns added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: DraftingView, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: DraftingView, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
         The object being selected with the objects view and objects point and snap information.
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, selection: DraftingView, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> bool:
        """
         The object being selected with CAE set object information.
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    def Clear(self) -> None:
        """
         Removes all items from the list.
            
        """
        pass
    def Contains(self, objectValue: DraftingView) -> bool:
        """
         Returns whether the specified object is already in the list or not.
            
         Returns list_contains (bool):  true if object is in the list, false otherwise .
        """
        pass
    def GetArray(self) -> List[DraftingView]:
        """
         Returns the list of objects in the selection list.
            
         Returns objects ( DraftingView List[NXOpe):  items in list .
        """
        pass
    def GetSelectObjectArray(self) -> List[NXOpen.SelectObject]:
        """
         Returns the list of SelectObjects in the selection list.
            
         Returns objects ( NXOpen.SelectObject Li):  items in list .
        """
        pass
    @overload
    def Remove(self, objectValue: DraftingView) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    def RemoveArray(self, objects: List[DraftingView]) -> bool:
        """
         Remove specified objects from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    @overload
    def Remove(self, objectValue: DraftingView, view: NXOpen.View) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object  view was not a member of the list .
        """
        pass
    @overload
    def Remove(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: DraftingView, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: DraftingView, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    @overload
    def Remove(self, input_selection_method: NXOpen.SelectionMethod) -> bool:
        """
         Removes the objects from a SelectionMethod from the list
            
         Returns removed (bool):  True if successfully removed all objects from the list;
                                            False if there was at least one object that was not a
                                            member of the list .
        """
        pass
    def SetArray(self, objects: List[DraftingView]) -> None:
        """
         Sets the list of objects in the selection list. This will clear any existing
            items in the list.
            
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectDraftingView(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""
    @property
    def Value(self) -> DraftingView:
        """
        Getter for property: ( DraftingView NXOpen.) Value
         Returns the object being selected
              
            
         
        """
        pass
    @Value.setter
    def Value(self, selection: DraftingView):
        """
        Setter for property: ( DraftingView NXOpen.) Value
         Returns the object being selected
              
            
         
        """
        pass
    @overload
    def GetValue(self) -> Tuple[DraftingView, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         Returns A tuple consisting of (selection, view, point). 
         - selection is:  DraftingView NXOpen.. selected object .
         - view is:  NXOpen.View. selected object view.
         - point is:  NXOpen.Point3d. selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, DraftingView, NXOpen.View, NXOpen.Point3d, DraftingView, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         Returns A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is:  NXOpen.InferSnapType.SnapType.  snap point type.
         - selection1 is:  DraftingView NXOpen.. first selected object .
         - view1 is:  NXOpen.View. first selected object view.
         - point1 is:  NXOpen.Point3d. first selected object point.
         - selection2 is:  DraftingView NXOpen.. second selected object .
         - view2 is:  NXOpen.View. second selected object view.
         - point2 is:  NXOpen.Point3d. second selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[DraftingView, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         Returns A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is:  DraftingView NXOpen.. selected object .
         - cae_sub_type is:  NXOpen.CaeObjectType.CaeSubType. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    @overload
    def SetValue(self, selection: DraftingView, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: DraftingView, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: DraftingView, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
    @overload
    def SetValue(self, selection: DraftingView, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectDrawingRegion(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""
    @property
    def Value(self) -> DrawingRegion:
        """
        Getter for property: ( DrawingRegion NXOpen.) Value
         Returns the object being selected
              
            
         
        """
        pass
    @Value.setter
    def Value(self, selection: DrawingRegion):
        """
        Setter for property: ( DrawingRegion NXOpen.) Value
         Returns the object being selected
              
            
         
        """
        pass
    @overload
    def GetValue(self) -> Tuple[DrawingRegion, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         Returns A tuple consisting of (selection, view, point). 
         - selection is:  DrawingRegion NXOpen.. selected object .
         - view is:  NXOpen.View. selected object view.
         - point is:  NXOpen.Point3d. selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, DrawingRegion, NXOpen.View, NXOpen.Point3d, DrawingRegion, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         Returns A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is:  NXOpen.InferSnapType.SnapType.  snap point type.
         - selection1 is:  DrawingRegion NXOpen.. first selected object .
         - view1 is:  NXOpen.View. first selected object view.
         - point1 is:  NXOpen.Point3d. first selected object point.
         - selection2 is:  DrawingRegion NXOpen.. second selected object .
         - view2 is:  NXOpen.View. second selected object view.
         - point2 is:  NXOpen.Point3d. second selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[DrawingRegion, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         Returns A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is:  DrawingRegion NXOpen.. selected object .
         - cae_sub_type is:  NXOpen.CaeObjectType.CaeSubType. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    @overload
    def SetValue(self, selection: DrawingRegion, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: DrawingRegion, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: DrawingRegion, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
    @overload
    def SetValue(self, selection: DrawingRegion, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectDrawingViewList(NXOpen.TaggedObject): 
    """ Represents a list of objects on a selection list.
"""
    @property
    def DuplicatesAllowed(self) -> bool:
        """
        Getter for property: (bool) DuplicatesAllowed
         Returns whether duplicate objects are allowed in the selection list.  
          
              
         
        """
        pass
    @property
    def Size(self) -> int:
        """
        Getter for property: (int) Size
         Returns the number of objects in the list.  
          
              
         
        """
        pass
    @overload
    def Add(self, objectValue: DrawingView) -> bool:
        """
         Adds an object to the list
            
         Returns added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    def AddWithViews(self, objects: List[DrawingView], views: List[NXOpen.View]) -> bool:
        """
         Adds a set of objects with views to the list
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, objects: List[DrawingView]) -> bool:
        """
         Adds a set of objects to the list
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, input_selection_method: NXOpen.SelectionMethod) -> bool:
        """
         Adds the objects from a SelectionMethod to the list
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, selection: DrawingView, view: NXOpen.View, point: NXOpen.Point3d) -> bool:
        """
         Adds the object with the objects view and objects point
            
         Returns added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: DrawingView, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: DrawingView, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
         The object being selected with the objects view and objects point and snap information.
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, selection: DrawingView, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> bool:
        """
         The object being selected with CAE set object information.
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    def Clear(self) -> None:
        """
         Removes all items from the list.
            
        """
        pass
    def Contains(self, objectValue: DrawingView) -> bool:
        """
         Returns whether the specified object is already in the list or not.
            
         Returns list_contains (bool):  true if object is in the list, false otherwise .
        """
        pass
    def GetArray(self) -> List[DrawingView]:
        """
         Returns the list of objects in the selection list.
            
         Returns objects ( DrawingView List[NXOpe):  items in list .
        """
        pass
    def GetSelectObjectArray(self) -> List[NXOpen.SelectObject]:
        """
         Returns the list of SelectObjects in the selection list.
            
         Returns objects ( NXOpen.SelectObject Li):  items in list .
        """
        pass
    @overload
    def Remove(self, objectValue: DrawingView) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    def RemoveArray(self, objects: List[DrawingView]) -> bool:
        """
         Remove specified objects from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    @overload
    def Remove(self, objectValue: DrawingView, view: NXOpen.View) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object  view was not a member of the list .
        """
        pass
    @overload
    def Remove(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: DrawingView, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: DrawingView, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    @overload
    def Remove(self, input_selection_method: NXOpen.SelectionMethod) -> bool:
        """
         Removes the objects from a SelectionMethod from the list
            
         Returns removed (bool):  True if successfully removed all objects from the list;
                                            False if there was at least one object that was not a
                                            member of the list .
        """
        pass
    def SetArray(self, objects: List[DrawingView]) -> None:
        """
         Sets the list of objects in the selection list. This will clear any existing
            items in the list.
            
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectDrawingView(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""
    @property
    def Value(self) -> DrawingView:
        """
        Getter for property: ( DrawingView NXOpen.) Value
         Returns the object being selected
              
            
         
        """
        pass
    @Value.setter
    def Value(self, selection: DrawingView):
        """
        Setter for property: ( DrawingView NXOpen.) Value
         Returns the object being selected
              
            
         
        """
        pass
    @overload
    def GetValue(self) -> Tuple[DrawingView, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         Returns A tuple consisting of (selection, view, point). 
         - selection is:  DrawingView NXOpen.. selected object .
         - view is:  NXOpen.View. selected object view.
         - point is:  NXOpen.Point3d. selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, DrawingView, NXOpen.View, NXOpen.Point3d, DrawingView, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         Returns A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is:  NXOpen.InferSnapType.SnapType.  snap point type.
         - selection1 is:  DrawingView NXOpen.. first selected object .
         - view1 is:  NXOpen.View. first selected object view.
         - point1 is:  NXOpen.Point3d. first selected object point.
         - selection2 is:  DrawingView NXOpen.. second selected object .
         - view2 is:  NXOpen.View. second selected object view.
         - point2 is:  NXOpen.Point3d. second selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[DrawingView, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         Returns A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is:  DrawingView NXOpen.. selected object .
         - cae_sub_type is:  NXOpen.CaeObjectType.CaeSubType. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    @overload
    def SetValue(self, selection: DrawingView, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: DrawingView, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: DrawingView, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
    @overload
    def SetValue(self, selection: DrawingView, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectModelViewBuilder(NXOpen.TaggedObject): 
    """ Represents a Select Model View builder that selects a model view
    """
    @property
    def SelectedView(self) -> NXOpen.ModelingView:
        """
        Getter for property: ( NXOpen.ModelingView) SelectedView
         Returns the selected view   
            
         
        """
        pass
    @SelectedView.setter
    def SelectedView(self, view: NXOpen.ModelingView):
        """
        Setter for property: ( NXOpen.ModelingView) SelectedView
         Returns the selected view   
            
         
        """
        pass
import NXOpen
class SelectRegionBuilder(NXOpen.Builder): 
    """ Creates the builder for associating the objects from the screen  """
    @property
    def SelectedRegion(self) -> SelectDrawingRegion:
        """
        Getter for property: ( SelectDrawingRegion NXOpen.) SelectedRegion
         Returns the get selected region   
            
         
        """
        pass
    def SetAssociatedObjects(self, associateObject: List[NXOpen.NXObject]) -> None:
        """
         Set the associated  object 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectSectionLine(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""
    @property
    def Value(self) -> SectionLine:
        """
        Getter for property: ( SectionLine NXOpen.) Value
         Returns the object being selected
              
            
         
        """
        pass
    @Value.setter
    def Value(self, selection: SectionLine):
        """
        Setter for property: ( SectionLine NXOpen.) Value
         Returns the object being selected
              
            
         
        """
        pass
    @overload
    def GetValue(self) -> Tuple[SectionLine, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         Returns A tuple consisting of (selection, view, point). 
         - selection is:  SectionLine NXOpen.. selected object .
         - view is:  NXOpen.View. selected object view.
         - point is:  NXOpen.Point3d. selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, SectionLine, NXOpen.View, NXOpen.Point3d, SectionLine, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         Returns A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is:  NXOpen.InferSnapType.SnapType.  snap point type.
         - selection1 is:  SectionLine NXOpen.. first selected object .
         - view1 is:  NXOpen.View. first selected object view.
         - point1 is:  NXOpen.Point3d. first selected object point.
         - selection2 is:  SectionLine NXOpen.. second selected object .
         - view2 is:  NXOpen.View. second selected object view.
         - point2 is:  NXOpen.Point3d. second selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[SectionLine, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         Returns A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is:  SectionLine NXOpen.. selected object .
         - cae_sub_type is:  NXOpen.CaeObjectType.CaeSubType. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    @overload
    def SetValue(self, selection: SectionLine, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: SectionLine, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: SectionLine, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
    @overload
    def SetValue(self, selection: SectionLine, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SettingsBuilder(NXOpen.TaggedObject): 
    """
    Represents a Drawings.SettingsBuilder.
    This class queries and sets settings.
    """
    @property
    def AnnotationSettings(self) -> AnnotationSettingsBuilder:
        """
        Getter for property: ( AnnotationSettingsBuilder NXOpen.) AnnotationSettings
         Returns the Annotation settings builder which stores the annotation settings   
            
         
        """
        pass
    @property
    def ConversionSettings(self) -> ConversionProcessSettingsBuilder:
        """
        Getter for property: ( ConversionProcessSettingsBuilder NXOpen.) ConversionSettings
         Returns the Component settings builder which stores the component settings   
            
         
        """
        pass
    @property
    def ViewSettings(self) -> ViewSettingsBuilder:
        """
        Getter for property: ( ViewSettingsBuilder NXOpen.) ViewSettings
         Returns the View settings builder which stores the view settings   
            
         
        """
        pass
    def SaveConfigurationFile(self, saveAsFile: str) -> None:
        """
         API used to save settings data 
        """
        pass
import NXOpen
import NXOpen.Preferences
class ShadingViewStyle(NXOpen.Object): 
    """ Represents set of Shading View style applicable to drafting views. """
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
    def RenderingStyle(self) -> NXOpen.Preferences.ShadingRenderingStyleOption:
        """
        Getter for property: ( NXOpen.Preferences.ShadingRenderingStyleOption) RenderingStyle
         Returns the rendering style.  
            
         
        """
        pass
    @RenderingStyle.setter
    def RenderingStyle(self, rendering_style_option: NXOpen.Preferences.ShadingRenderingStyleOption):
        """
        Setter for property: ( NXOpen.Preferences.ShadingRenderingStyleOption) RenderingStyle
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
    def ShadingTolerance(self) -> NXOpen.Preferences.ShadingToleranceOption:
        """
        Getter for property: ( NXOpen.Preferences.ShadingToleranceOption) ShadingTolerance
         Returns the shading tolerance.  
             
         
        """
        pass
    @ShadingTolerance.setter
    def ShadingTolerance(self, shading_tolerance: NXOpen.Preferences.ShadingToleranceOption):
        """
        Setter for property: ( NXOpen.Preferences.ShadingToleranceOption) ShadingTolerance
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
import NXOpen.GeometricUtilities
class SheetBorderSettingsBuilder(NXOpen.TaggedObject): 
    """
    Represents a  NXOpen.Drawings.SheetBorderSettingsBuilder.
    This class queries and sets sheet border settings preferences when creating a sheet border.
    """
    @property
    def ArrowAngle(self) -> float:
        """
        Getter for property: (float) ArrowAngle
         Returns the arrow angle   
            
         
        """
        pass
    @ArrowAngle.setter
    def ArrowAngle(self, arrowAngle: float):
        """
        Setter for property: (float) ArrowAngle
         Returns the arrow angle   
            
         
        """
        pass
    @property
    def ArrowDirection(self) -> ArrowDirectionType:
        """
        Getter for property: ( ArrowDirectionType NXOpen.) ArrowDirection
         Returns the arrow direction   
            
         
        """
        pass
    @ArrowDirection.setter
    def ArrowDirection(self, arrowDirection: ArrowDirectionType):
        """
        Setter for property: ( ArrowDirectionType NXOpen.) ArrowDirection
         Returns the arrow direction   
            
         
        """
        pass
    @property
    def ArrowHeadTail(self) -> float:
        """
        Getter for property: (float) ArrowHeadTail
         Returns the arrowhead tail   
            
         
        """
        pass
    @ArrowHeadTail.setter
    def ArrowHeadTail(self, arrowHeadTail: float):
        """
        Setter for property: (float) ArrowHeadTail
         Returns the arrowhead tail   
            
         
        """
        pass
    @property
    def ArrowLength(self) -> float:
        """
        Getter for property: (float) ArrowLength
         Returns the arrow length   
            
         
        """
        pass
    @ArrowLength.setter
    def ArrowLength(self, arrowLength: float):
        """
        Setter for property: (float) ArrowLength
         Returns the arrow length   
            
         
        """
        pass
    @property
    def ArrowStyle(self) -> ArrowStyleType:
        """
        Getter for property: ( ArrowStyleType NXOpen.) ArrowStyle
         Returns the arrow style   
            
         
        """
        pass
    @ArrowStyle.setter
    def ArrowStyle(self, arrowStyle: ArrowStyleType):
        """
        Setter for property: ( ArrowStyleType NXOpen.) ArrowStyle
         Returns the arrow style   
            
         
        """
        pass
    @property
    def BorderLineWidth(self) -> float:
        """
        Getter for property: (float) BorderLineWidth
         Returns the border line width   
            
         
        """
        pass
    @BorderLineWidth.setter
    def BorderLineWidth(self, borderLineWidth: float):
        """
        Setter for property: (float) BorderLineWidth
         Returns the border line width   
            
         
        """
        pass
    @property
    def CenteringMarkLength(self) -> float:
        """
        Getter for property: (float) CenteringMarkLength
         Returns the centering mark length   
            
         
        """
        pass
    @CenteringMarkLength.setter
    def CenteringMarkLength(self, centeringMarkLength: float):
        """
        Setter for property: (float) CenteringMarkLength
         Returns the centering mark length   
            
         
        """
        pass
    @property
    def CenteringMarksColorWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) CenteringMarksColorWidth
         Returns the centering marks color width   
            
         
        """
        pass
    @property
    def CenteringMarksExtension(self) -> float:
        """
        Getter for property: (float) CenteringMarksExtension
         Returns the centering marks extension   
            
         
        """
        pass
    @CenteringMarksExtension.setter
    def CenteringMarksExtension(self, centeringMarksExtension: float):
        """
        Setter for property: (float) CenteringMarksExtension
         Returns the centering marks extension   
            
         
        """
        pass
    @property
    def CenteringMarksHorizontal(self) -> HorizontalCenteringMarkType:
        """
        Getter for property: ( HorizontalCenteringMarkType NXOpen.) CenteringMarksHorizontal
         Returns the centering marks horizontal   
            
         
        """
        pass
    @CenteringMarksHorizontal.setter
    def CenteringMarksHorizontal(self, centeringMarksHorizontal: HorizontalCenteringMarkType):
        """
        Setter for property: ( HorizontalCenteringMarkType NXOpen.) CenteringMarksHorizontal
         Returns the centering marks horizontal   
            
         
        """
        pass
    @property
    def CenteringMarksVertical(self) -> VerticalCenteringMarkType:
        """
        Getter for property: ( VerticalCenteringMarkType NXOpen.) CenteringMarksVertical
         Returns the centering marks vertical   
            
         
        """
        pass
    @CenteringMarksVertical.setter
    def CenteringMarksVertical(self, centeringMarksVertical: VerticalCenteringMarkType):
        """
        Setter for property: ( VerticalCenteringMarkType NXOpen.) CenteringMarksVertical
         Returns the centering marks vertical   
            
         
        """
        pass
    @property
    def CreateBorders(self) -> bool:
        """
        Getter for property: (bool) CreateBorders
         Returns the create borders   
            
         
        """
        pass
    @CreateBorders.setter
    def CreateBorders(self, createBorders: bool):
        """
        Setter for property: (bool) CreateBorders
         Returns the create borders   
            
         
        """
        pass
    @property
    def CreateTrimmingMarks(self) -> bool:
        """
        Getter for property: (bool) CreateTrimmingMarks
         Returns the create trimming marks   
            
         
        """
        pass
    @CreateTrimmingMarks.setter
    def CreateTrimmingMarks(self, createTrimmingMarks: bool):
        """
        Setter for property: (bool) CreateTrimmingMarks
         Returns the create trimming marks   
            
         
        """
        pass
    @property
    def DisplaySheetSizeInBorder(self) -> bool:
        """
        Getter for property: (bool) DisplaySheetSizeInBorder
         Returns the display sheet size in border   
            
         
        """
        pass
    @DisplaySheetSizeInBorder.setter
    def DisplaySheetSizeInBorder(self, displaySheetSizeInBorder: bool):
        """
        Setter for property: (bool) DisplaySheetSizeInBorder
         Returns the display sheet size in border   
            
         
        """
        pass
    @property
    def DistanceFromInnerBorder(self) -> float:
        """
        Getter for property: (float) DistanceFromInnerBorder
         Returns the distance from inner border   
            
         
        """
        pass
    @DistanceFromInnerBorder.setter
    def DistanceFromInnerBorder(self, distanceInFromInnerBorder: float):
        """
        Setter for property: (float) DistanceFromInnerBorder
         Returns the distance from inner border   
            
         
        """
        pass
    @property
    def InnerLineCFW(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) InnerLineCFW
         Returns the inner border line's color, font and width   
            
         
        """
        pass
    @property
    def Method(self) -> Method:
        """
        Getter for property: ( Method NXOpen.) Method
         Returns the method   
            
         
        """
        pass
    @Method.setter
    def Method(self, method: Method):
        """
        Setter for property: ( Method NXOpen.) Method
         Returns the method   
            
         
        """
        pass
    @property
    def OuterLineCFW(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) OuterLineCFW
         Returns the outer border line's color, font and width   
            
         
        """
        pass
    @property
    def TrimmingMarkColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) TrimmingMarkColor
         Returns the trimming mark color   
            
         
        """
        pass
    @TrimmingMarkColor.setter
    def TrimmingMarkColor(self, trimmingMarkColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) TrimmingMarkColor
         Returns the trimming mark color   
            
         
        """
        pass
    @property
    def TrimmingMarkLength(self) -> float:
        """
        Getter for property: (float) TrimmingMarkLength
         Returns the trimming mark length   
            
         
        """
        pass
    @TrimmingMarkLength.setter
    def TrimmingMarkLength(self, trimmingMarkLength: float):
        """
        Setter for property: (float) TrimmingMarkLength
         Returns the trimming mark length   
            
         
        """
        pass
    @property
    def TrimmingMarkStyle(self) -> TrimmingMarkStyleType:
        """
        Getter for property: ( TrimmingMarkStyleType NXOpen.) TrimmingMarkStyle
         Returns the trimming mark style   
            
         
        """
        pass
    @TrimmingMarkStyle.setter
    def TrimmingMarkStyle(self, trimmingMarkStyle: TrimmingMarkStyleType):
        """
        Setter for property: ( TrimmingMarkStyleType NXOpen.) TrimmingMarkStyle
         Returns the trimming mark style   
            
         
        """
        pass
    @property
    def TrimmingMarkWidth(self) -> float:
        """
        Getter for property: (float) TrimmingMarkWidth
         Returns the trimming mark width   
            
         
        """
        pass
    @TrimmingMarkWidth.setter
    def TrimmingMarkWidth(self, trimmingMarkWidth: float):
        """
        Setter for property: (float) TrimmingMarkWidth
         Returns the trimming mark width   
            
         
        """
        pass
import NXOpen
class SheetDraftingViewCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Drawings.DraftingViews.   """
    def CreateBaseView(self, model_view: NXOpen.ModelingView, drawing_reference_point: NXOpen.Point3d, view_scale: float, inherit_clipping_boundry: bool) -> BaseView:
        """
         For the selected part adds the base view as well as returns the reference to  NXOpen.Drawings.DraftingView . 
                    An imported model view (base view) determines orthographic space on the drawing and is used as a reference to establish the alignment 
                    and scale for all subsequent projected views.
         Returns base_view ( BaseView NXOpen.):  Base view .
        """
        pass
    @overload
    def CreateProjectedView(self, parent_view: DraftingView, drawing_reference_point: NXOpen.Point3d) -> ProjectedView:
        """
         Lets you add a projected view (Orthoraphic View) for the selected parent view.
         Returns projected_view ( ProjectedView NXOpen.):  Projected view .
        """
        pass
    @overload
    def CreateProjectedView(self, parent_view: DraftingView, drawing_reference_point: NXOpen.Point3d, hinge_line: NXOpen.Direction) -> ProjectedView:
        """
         Lets you add a projected view (A View) for the selected parent view.
         Returns projected_view ( ProjectedView NXOpen.):  Projected view .
        """
        pass
    @overload
    def CreateProjectedView(self, parent_view: DraftingView, drawing_reference_point: NXOpen.Point3d, reverse_direction: bool) -> ProjectedView:
        """
         Lets you add a projected view (A View) for the selected parent view.
         Returns projected_view ( ProjectedView NXOpen.):  Projected view .
        """
        pass
    def DeleteView(self, current_view: DraftingView) -> None:
        """
         Lets you delete the view 
        """
        pass
    def FindObject(self, journal_identifier: str) -> DraftingView:
        """
         Finds the  NXOpen.Drawings.DraftingView  with the given identifier as recorded in a journal. 
                An object may not return the same value as its JournalIdentifier in different versions of 
                the software. However newer versions of the software should find the same object when 
                FindObject is passed older versions of its journal identifier. In general, this method 
                should not be used in handwritten code and exists to support record and playback of journals.
                An exception will be thrown if no object can be found with the given journal identifier. 
         Returns found ( DraftingView NXOpen.):  View with this identifier .
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SheetMarginSettingsBuilder(NXOpen.TaggedObject): 
    """ Represents the Drawing Sheet Margins Style Builder.
    """
    @property
    def BottomTrimmedMargin(self) -> float:
        """
        Getter for property: (float) BottomTrimmedMargin
         Returns the bottom margin   
            
         
        """
        pass
    @BottomTrimmedMargin.setter
    def BottomTrimmedMargin(self, bottomTrimmedMargin: float):
        """
        Setter for property: (float) BottomTrimmedMargin
         Returns the bottom margin   
            
         
        """
        pass
    @property
    def BottomUntrimmedMargin(self) -> float:
        """
        Getter for property: (float) BottomUntrimmedMargin
         Returns the bottom untrimmed margin   
            
         
        """
        pass
    @BottomUntrimmedMargin.setter
    def BottomUntrimmedMargin(self, bottomUntrimmedMargin: float):
        """
        Setter for property: (float) BottomUntrimmedMargin
         Returns the bottom untrimmed margin   
            
         
        """
        pass
    @property
    def CreateUntrimmedMargins(self) -> bool:
        """
        Getter for property: (bool) CreateUntrimmedMargins
         Returns the create untrimmed margins   
            
         
        """
        pass
    @CreateUntrimmedMargins.setter
    def CreateUntrimmedMargins(self, createUntrimmedMargins: bool):
        """
        Setter for property: (bool) CreateUntrimmedMargins
         Returns the create untrimmed margins   
            
         
        """
        pass
    @property
    def LeftTrimmedMargin(self) -> float:
        """
        Getter for property: (float) LeftTrimmedMargin
         Returns the left margin   
            
         
        """
        pass
    @LeftTrimmedMargin.setter
    def LeftTrimmedMargin(self, leftTrimmedMargin: float):
        """
        Setter for property: (float) LeftTrimmedMargin
         Returns the left margin   
            
         
        """
        pass
    @property
    def LeftUntrimmedMargin(self) -> float:
        """
        Getter for property: (float) LeftUntrimmedMargin
         Returns the left untrimmed margin   
            
         
        """
        pass
    @LeftUntrimmedMargin.setter
    def LeftUntrimmedMargin(self, leftUntrimmedMargin: float):
        """
        Setter for property: (float) LeftUntrimmedMargin
         Returns the left untrimmed margin   
            
         
        """
        pass
    @property
    def MarginLineColorFontWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) MarginLineColorFontWidth
         Returns the margin line color, font and width   
            
         
        """
        pass
    @property
    def RightTrimmedMargin(self) -> float:
        """
        Getter for property: (float) RightTrimmedMargin
         Returns the right margin   
            
         
        """
        pass
    @RightTrimmedMargin.setter
    def RightTrimmedMargin(self, rightTrimmedMargin: float):
        """
        Setter for property: (float) RightTrimmedMargin
         Returns the right margin   
            
         
        """
        pass
    @property
    def RightUntrimmedMargin(self) -> float:
        """
        Getter for property: (float) RightUntrimmedMargin
         Returns the right untrimmed margin   
            
         
        """
        pass
    @RightUntrimmedMargin.setter
    def RightUntrimmedMargin(self, rightUntrimmedMargin: float):
        """
        Setter for property: (float) RightUntrimmedMargin
         Returns the right untrimmed margin   
            
         
        """
        pass
    @property
    def TopTrimmedMargin(self) -> float:
        """
        Getter for property: (float) TopTrimmedMargin
         Returns the top margin   
            
         
        """
        pass
    @TopTrimmedMargin.setter
    def TopTrimmedMargin(self, topMargin: float):
        """
        Setter for property: (float) TopTrimmedMargin
         Returns the top margin   
            
         
        """
        pass
    @property
    def TopUntrimmedMargin(self) -> float:
        """
        Getter for property: (float) TopUntrimmedMargin
         Returns the top untrimmed margin   
            
         
        """
        pass
    @TopUntrimmedMargin.setter
    def TopUntrimmedMargin(self, topUntrimmedMargin: float):
        """
        Setter for property: (float) TopUntrimmedMargin
         Returns the top untrimmed margin   
            
         
        """
        pass
import NXOpen
class SheetSectionLineCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Drawings.SectionLines.   """
    pass
import NXOpen
class SheetTemplateManager(NXOpen.Object): 
    """ Represents a manager of NXOpen.Drawings.DraftingViews.   """
    def Create(self, pathToPartName: str) -> None:
        """
         Creates drawings via the sheet template, given a path to sheet template 
        """
        pass
import NXOpen
class SheetZoneReferenceBuilder(NXOpen.Builder): 
    """builder for creating sheet zone refernce control strings based on the selected attribute and view """
    @property
    def SelectView(self) -> SelectDraftingView:
        """
        Getter for property: ( SelectDraftingView NXOpen.) SelectView
         Returns the select view   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SheetZoneSettingsBuilder(NXOpen.TaggedObject): 
    """ Represents the Drawing Sheet Zone Setting Style Builder.
    """
    @property
    def ContinueZoneIndexingAcrossSheets(self) -> bool:
        """
        Getter for property: (bool) ContinueZoneIndexingAcrossSheets
         Returns the continue zone indexing across sheets   
            
         
        """
        pass
    @ContinueZoneIndexingAcrossSheets.setter
    def ContinueZoneIndexingAcrossSheets(self, continueZoneIndexingAcrossSheets: bool):
        """
        Setter for property: (bool) ContinueZoneIndexingAcrossSheets
         Returns the continue zone indexing across sheets   
            
         
        """
        pass
    @property
    def CornerZoneModification(self) -> float:
        """
        Getter for property: (float) CornerZoneModification
         Returns the corner zone modification   
            
         
        """
        pass
    @CornerZoneModification.setter
    def CornerZoneModification(self, cornerZoneModification: float):
        """
        Setter for property: (float) CornerZoneModification
         Returns the corner zone modification   
            
         
        """
        pass
    @property
    def CreateZoneLabels(self) -> bool:
        """
        Getter for property: (bool) CreateZoneLabels
         Returns the create zone labels   
            
         
        """
        pass
    @CreateZoneLabels.setter
    def CreateZoneLabels(self, createZoneLabels: bool):
        """
        Setter for property: (bool) CreateZoneLabels
         Returns the create zone labels   
            
         
        """
        pass
    @property
    def CreateZoneMarkings(self) -> bool:
        """
        Getter for property: (bool) CreateZoneMarkings
         Returns the create zone markings   
            
         
        """
        pass
    @CreateZoneMarkings.setter
    def CreateZoneMarkings(self, createZoneMarkings: bool):
        """
        Setter for property: (bool) CreateZoneMarkings
         Returns the create zone markings   
            
         
        """
        pass
    @property
    def CreateZones(self) -> bool:
        """
        Getter for property: (bool) CreateZones
         Returns the create zones   
            
         
        """
        pass
    @CreateZones.setter
    def CreateZones(self, createZones: bool):
        """
        Setter for property: (bool) CreateZones
         Returns the create zones   
            
         
        """
        pass
    @property
    def HorizontalSize(self) -> float:
        """
        Getter for property: (float) HorizontalSize
         Returns the horizontal size   
            
         
        """
        pass
    @HorizontalSize.setter
    def HorizontalSize(self, horizontalSize: float):
        """
        Setter for property: (float) HorizontalSize
         Returns the horizontal size   
            
         
        """
        pass
    @property
    def LabelColor(self) -> int:
        """
        Getter for property: (int) LabelColor
         Returns the labels color   
            
         
        """
        pass
    @LabelColor.setter
    def LabelColor(self, labelColor: int):
        """
        Setter for property: (int) LabelColor
         Returns the labels color   
            
         
        """
        pass
    @property
    def LabelFont(self) -> int:
        """
        Getter for property: (int) LabelFont
         Returns the labels font   
            
         
        """
        pass
    @LabelFont.setter
    def LabelFont(self, labelFont: int):
        """
        Setter for property: (int) LabelFont
         Returns the labels font   
            
         
        """
        pass
    @property
    def LabelHeight(self) -> float:
        """
        Getter for property: (float) LabelHeight
         Returns the label height   
            
         
        """
        pass
    @LabelHeight.setter
    def LabelHeight(self, labelHeight: float):
        """
        Setter for property: (float) LabelHeight
         Returns the label height   
            
         
        """
        pass
    @property
    def LabelItalicized(self) -> bool:
        """
        Getter for property: (bool) LabelItalicized
         Returns the labels font style   
            
         
        """
        pass
    @LabelItalicized.setter
    def LabelItalicized(self, italic: bool):
        """
        Setter for property: (bool) LabelItalicized
         Returns the labels font style   
            
         
        """
        pass
    @property
    def LabelWidth(self) -> int:
        """
        Getter for property: (int) LabelWidth
         Returns the labels width   
            
         
        """
        pass
    @LabelWidth.setter
    def LabelWidth(self, labelWidth: int):
        """
        Setter for property: (int) LabelWidth
         Returns the labels width   
            
         
        """
        pass
    @property
    def LabelsToSkip(self) -> str:
        """
        Getter for property: (str) LabelsToSkip
         Returns the labels to skip   
            
         
        """
        pass
    @LabelsToSkip.setter
    def LabelsToSkip(self, labelsToSkip: str):
        """
        Setter for property: (str) LabelsToSkip
         Returns the labels to skip   
            
         
        """
        pass
    @property
    def MarkingHeight(self) -> float:
        """
        Getter for property: (float) MarkingHeight
         Returns the marking height   
            
         
        """
        pass
    @MarkingHeight.setter
    def MarkingHeight(self, markingHeight: float):
        """
        Setter for property: (float) MarkingHeight
         Returns the marking height   
            
         
        """
        pass
    @property
    def MarkingLineColorWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) MarkingLineColorWidth
         Returns the marking line color width   
            
         
        """
        pass
    @property
    def Origin(self) -> ZoneOrigin:
        """
        Getter for property: ( ZoneOrigin NXOpen.) Origin
         Returns the origin   
            
         
        """
        pass
    @Origin.setter
    def Origin(self, origin: ZoneOrigin):
        """
        Setter for property: ( ZoneOrigin NXOpen.) Origin
         Returns the origin   
            
         
        """
        pass
    @property
    def VerticalSize(self) -> float:
        """
        Getter for property: (float) VerticalSize
         Returns the vertical size   
            
         
        """
        pass
    @VerticalSize.setter
    def VerticalSize(self, verticalSize: float):
        """
        Setter for property: (float) VerticalSize
         Returns the vertical size   
            
         
        """
        pass
import NXOpen
import NXOpen.Preferences
class ShipbuildingLinesViewStyle(NXOpen.Object): 
    """ Represents set of Shipbuilding Lines View Style applicable to drafting views. 
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
        def ValueOf(value: int) -> ShipbuildingLinesViewStyle.Lines:
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
        def ValueOf(value: int) -> ShipbuildingLinesViewStyle.ShipbuildingLines:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetColor(self, feature_name: str, lines_type: ShipbuildingLinesViewStyle.Lines) -> int:
        """
         Get line color 
         Returns color (int): .
        """
        pass
    def GetFont(self, feature_name: str, lines_type: ShipbuildingLinesViewStyle.Lines) -> NXOpen.Preferences.Font:
        """
         Get line font 
         Returns font ( NXOpen.Preferences.Font): .
        """
        pass
    def GetSingleLineRepresentation(self, feature_type: ShipbuildingLinesViewStyle.ShipbuildingLines, feature_name: str) -> bool:
        """
         Get single line status 
         Returns single_line (bool):  status that determines SLR for the feature .
        """
        pass
    def GetWidth(self, feature_name: str, lines_type: ShipbuildingLinesViewStyle.Lines) -> NXOpen.Preferences.Width:
        """
         Get line width 
         Returns width ( NXOpen.Preferences.Width): .
        """
        pass
    def SetColor(self, feature_name: str, lines_type: ShipbuildingLinesViewStyle.Lines, color: int) -> None:
        """
         The color of ship line. The value should be between UF_OBJ_MIN_COLOR and UF_OBJ_MAX_COLOR. 
        """
        pass
    def SetFont(self, feature_name: str, lines_type: ShipbuildingLinesViewStyle.Lines, font: NXOpen.Preferences.Font) -> None:
        """
         The font type of ship line.
        """
        pass
    def SetSingleLineRepresentation(self, feature_type: ShipbuildingLinesViewStyle.ShipbuildingLines, feature_name: str, single_line: bool) -> None:
        """
         Note: The initial values are set based on the customer defaults depending on 
                whether the feature is a Profile or a Plate.
                The status determines the single line representation for the ship feature in a view.
        """
        pass
    def SetWidth(self, feature_name: str, lines_type: ShipbuildingLinesViewStyle.Lines, width: NXOpen.Preferences.Width) -> None:
        """
         The width of hidden line or edges. 
        """
        pass
import NXOpen
class ShipDraftingViewLinesBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[ShipDraftingViewLinesBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: ShipDraftingViewLinesBuilder) -> None:
        """
         Appends an object to the list
            
        """
        pass
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
               not change, but the item at this index is set to NULL.
            
        """
        pass
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, obj: ShipDraftingViewLinesBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: ShipDraftingViewLinesBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: ShipDraftingViewLinesBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> ShipDraftingViewLinesBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( ShipDraftingViewLinesBuilder NXOpen.):  object found at input index .
        """
        pass
    def GetContents(self) -> List[ShipDraftingViewLinesBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( ShipDraftingViewLinesBuilder List[NXOpe):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: ShipDraftingViewLinesBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    def SetContents(self, objects: List[ShipDraftingViewLinesBuilder]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    @overload
    def Swap(self, object1: ShipDraftingViewLinesBuilder, object2: ShipDraftingViewLinesBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.Preferences
class ShipDraftingViewLinesBuilder(NXOpen.Builder): 
    """ Represents a ship view lines block """
    @property
    def NonSectionedHiddenColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) NonSectionedHiddenColor
         Returns the non-sectioned hidden color on the Ship Structure Lines   
            
         
        """
        pass
    @NonSectionedHiddenColor.setter
    def NonSectionedHiddenColor(self, nonSectionedHiddenColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) NonSectionedHiddenColor
         Returns the non-sectioned hidden color on the Ship Structure Lines   
            
         
        """
        pass
    @property
    def NonSectionedHiddenFont(self) -> NXOpen.Preferences.Font:
        """
        Getter for property: ( NXOpen.Preferences.Font) NonSectionedHiddenFont
         Returns the non-sectioned hidden font on the Ship Structure Lines   
            
         
        """
        pass
    @NonSectionedHiddenFont.setter
    def NonSectionedHiddenFont(self, nonSectionedHiddenFont: NXOpen.Preferences.Font):
        """
        Setter for property: ( NXOpen.Preferences.Font) NonSectionedHiddenFont
         Returns the non-sectioned hidden font on the Ship Structure Lines   
            
         
        """
        pass
    @property
    def NonSectionedHiddenWidth(self) -> NXOpen.Preferences.Width:
        """
        Getter for property: ( NXOpen.Preferences.Width) NonSectionedHiddenWidth
         Returns the non-sectioned hidden width on the Ship Structure Lines   
            
         
        """
        pass
    @NonSectionedHiddenWidth.setter
    def NonSectionedHiddenWidth(self, nonSectionedHiddenWidth: NXOpen.Preferences.Width):
        """
        Setter for property: ( NXOpen.Preferences.Width) NonSectionedHiddenWidth
         Returns the non-sectioned hidden width on the Ship Structure Lines   
            
         
        """
        pass
    @property
    def NonSectionedSecondaryHiddenColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) NonSectionedSecondaryHiddenColor
         Returns the Secondary non-sectioned hidden color on the Ship Structure Lines   
            
         
        """
        pass
    @NonSectionedSecondaryHiddenColor.setter
    def NonSectionedSecondaryHiddenColor(self, nonSectionedSecondaryHiddenColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) NonSectionedSecondaryHiddenColor
         Returns the Secondary non-sectioned hidden color on the Ship Structure Lines   
            
         
        """
        pass
    @property
    def NonSectionedSecondaryHiddenFont(self) -> NXOpen.Preferences.Font:
        """
        Getter for property: ( NXOpen.Preferences.Font) NonSectionedSecondaryHiddenFont
         Returns the Secondary non-sectioned hidden font on the Ship Structure Lines   
            
         
        """
        pass
    @NonSectionedSecondaryHiddenFont.setter
    def NonSectionedSecondaryHiddenFont(self, nonSectionedSecondaryHiddenFont: NXOpen.Preferences.Font):
        """
        Setter for property: ( NXOpen.Preferences.Font) NonSectionedSecondaryHiddenFont
         Returns the Secondary non-sectioned hidden font on the Ship Structure Lines   
            
         
        """
        pass
    @property
    def NonSectionedSecondaryHiddenWidth(self) -> NXOpen.Preferences.Width:
        """
        Getter for property: ( NXOpen.Preferences.Width) NonSectionedSecondaryHiddenWidth
         Returns the Secondary non-sectioned hidden width on the Ship Structure Lines   
            
         
        """
        pass
    @NonSectionedSecondaryHiddenWidth.setter
    def NonSectionedSecondaryHiddenWidth(self, nonSectionedSecondaryHiddenWidth: NXOpen.Preferences.Width):
        """
        Setter for property: ( NXOpen.Preferences.Width) NonSectionedSecondaryHiddenWidth
         Returns the Secondary non-sectioned hidden width on the Ship Structure Lines   
            
         
        """
        pass
    @property
    def NonSectionedSecondaryVisibleColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) NonSectionedSecondaryVisibleColor
         Returns the Secondary non-sectioned visible color on the Ship Structure Lines   
            
         
        """
        pass
    @NonSectionedSecondaryVisibleColor.setter
    def NonSectionedSecondaryVisibleColor(self, nonSectionedSecondaryVisibleColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) NonSectionedSecondaryVisibleColor
         Returns the Secondary non-sectioned visible color on the Ship Structure Lines   
            
         
        """
        pass
    @property
    def NonSectionedSecondaryVisibleFont(self) -> NXOpen.Preferences.Font:
        """
        Getter for property: ( NXOpen.Preferences.Font) NonSectionedSecondaryVisibleFont
         Returns the Secondary non-sectioned visible font on the Ship Structure Lines   
            
         
        """
        pass
    @NonSectionedSecondaryVisibleFont.setter
    def NonSectionedSecondaryVisibleFont(self, nonSectionedSecondaryVisibleFont: NXOpen.Preferences.Font):
        """
        Setter for property: ( NXOpen.Preferences.Font) NonSectionedSecondaryVisibleFont
         Returns the Secondary non-sectioned visible font on the Ship Structure Lines   
            
         
        """
        pass
    @property
    def NonSectionedSecondaryVisibleWidth(self) -> NXOpen.Preferences.Width:
        """
        Getter for property: ( NXOpen.Preferences.Width) NonSectionedSecondaryVisibleWidth
         Returns the Secondary non-sectioned visible width on the Ship Structure Lines   
            
         
        """
        pass
    @NonSectionedSecondaryVisibleWidth.setter
    def NonSectionedSecondaryVisibleWidth(self, nonSectionedSecondaryVisibleWidth: NXOpen.Preferences.Width):
        """
        Setter for property: ( NXOpen.Preferences.Width) NonSectionedSecondaryVisibleWidth
         Returns the Secondary non-sectioned visible width on the Ship Structure Lines   
            
         
        """
        pass
    @property
    def NonSectionedVisibleColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) NonSectionedVisibleColor
         Returns the non-sectioned visible color on the Ship Structure Lines   
            
         
        """
        pass
    @NonSectionedVisibleColor.setter
    def NonSectionedVisibleColor(self, nonSectionedVisibleColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) NonSectionedVisibleColor
         Returns the non-sectioned visible color on the Ship Structure Lines   
            
         
        """
        pass
    @property
    def NonSectionedVisibleFont(self) -> NXOpen.Preferences.Font:
        """
        Getter for property: ( NXOpen.Preferences.Font) NonSectionedVisibleFont
         Returns the non-sectioned visible font on the Ship Structure Lines   
            
         
        """
        pass
    @NonSectionedVisibleFont.setter
    def NonSectionedVisibleFont(self, nonSectionedVisibleFont: NXOpen.Preferences.Font):
        """
        Setter for property: ( NXOpen.Preferences.Font) NonSectionedVisibleFont
         Returns the non-sectioned visible font on the Ship Structure Lines   
            
         
        """
        pass
    @property
    def NonSectionedVisibleWidth(self) -> NXOpen.Preferences.Width:
        """
        Getter for property: ( NXOpen.Preferences.Width) NonSectionedVisibleWidth
         Returns the non-sectioned visible width on the Ship Structure Lines   
            
         
        """
        pass
    @NonSectionedVisibleWidth.setter
    def NonSectionedVisibleWidth(self, nonSectionedVisibleWidth: NXOpen.Preferences.Width):
        """
        Setter for property: ( NXOpen.Preferences.Width) NonSectionedVisibleWidth
         Returns the non-sectioned visible width on the Ship Structure Lines   
            
         
        """
        pass
    @property
    def SectionedHiddenColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) SectionedHiddenColor
         Returns the sectioned hidden color on the Ship Structure Lines   
            
         
        """
        pass
    @SectionedHiddenColor.setter
    def SectionedHiddenColor(self, sectionedHiddenColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) SectionedHiddenColor
         Returns the sectioned hidden color on the Ship Structure Lines   
            
         
        """
        pass
    @property
    def SectionedHiddenFont(self) -> NXOpen.Preferences.Font:
        """
        Getter for property: ( NXOpen.Preferences.Font) SectionedHiddenFont
         Returns the sectioned hidden font on the Ship Structure Lines   
            
         
        """
        pass
    @SectionedHiddenFont.setter
    def SectionedHiddenFont(self, sectionedHiddenFont: NXOpen.Preferences.Font):
        """
        Setter for property: ( NXOpen.Preferences.Font) SectionedHiddenFont
         Returns the sectioned hidden font on the Ship Structure Lines   
            
         
        """
        pass
    @property
    def SectionedHiddenWidth(self) -> NXOpen.Preferences.Width:
        """
        Getter for property: ( NXOpen.Preferences.Width) SectionedHiddenWidth
         Returns the sectioned hidden width on the Ship Structure Lines   
            
         
        """
        pass
    @SectionedHiddenWidth.setter
    def SectionedHiddenWidth(self, sectionedHiddenWidth: NXOpen.Preferences.Width):
        """
        Setter for property: ( NXOpen.Preferences.Width) SectionedHiddenWidth
         Returns the sectioned hidden width on the Ship Structure Lines   
            
         
        """
        pass
    @property
    def SectionedSecondaryHiddenColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) SectionedSecondaryHiddenColor
         Returns the Secondary sectioned hidden color on the Ship Structure Lines   
            
         
        """
        pass
    @SectionedSecondaryHiddenColor.setter
    def SectionedSecondaryHiddenColor(self, sectionedSecondaryHiddenColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) SectionedSecondaryHiddenColor
         Returns the Secondary sectioned hidden color on the Ship Structure Lines   
            
         
        """
        pass
    @property
    def SectionedSecondaryHiddenFont(self) -> NXOpen.Preferences.Font:
        """
        Getter for property: ( NXOpen.Preferences.Font) SectionedSecondaryHiddenFont
         Returns the Secondary sectioned hidden font on the Ship Structure Lines   
            
         
        """
        pass
    @SectionedSecondaryHiddenFont.setter
    def SectionedSecondaryHiddenFont(self, sectionedSecondaryHiddenFont: NXOpen.Preferences.Font):
        """
        Setter for property: ( NXOpen.Preferences.Font) SectionedSecondaryHiddenFont
         Returns the Secondary sectioned hidden font on the Ship Structure Lines   
            
         
        """
        pass
    @property
    def SectionedSecondaryHiddenWidth(self) -> NXOpen.Preferences.Width:
        """
        Getter for property: ( NXOpen.Preferences.Width) SectionedSecondaryHiddenWidth
         Returns the Secondary sectioned hidden width on the Ship Structure Lines   
            
         
        """
        pass
    @SectionedSecondaryHiddenWidth.setter
    def SectionedSecondaryHiddenWidth(self, sectionedSecondaryHiddenWidth: NXOpen.Preferences.Width):
        """
        Setter for property: ( NXOpen.Preferences.Width) SectionedSecondaryHiddenWidth
         Returns the Secondary sectioned hidden width on the Ship Structure Lines   
            
         
        """
        pass
    @property
    def SectionedSecondaryVisibleColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) SectionedSecondaryVisibleColor
         Returns the Secondary sectioned visible color on the Ship Structure Lines   
            
         
        """
        pass
    @SectionedSecondaryVisibleColor.setter
    def SectionedSecondaryVisibleColor(self, sectionedSecondaryVisibleColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) SectionedSecondaryVisibleColor
         Returns the Secondary sectioned visible color on the Ship Structure Lines   
            
         
        """
        pass
    @property
    def SectionedSecondaryVisibleFont(self) -> NXOpen.Preferences.Font:
        """
        Getter for property: ( NXOpen.Preferences.Font) SectionedSecondaryVisibleFont
         Returns the Secondary sectioned visible font on the Ship Structure Lines   
            
         
        """
        pass
    @SectionedSecondaryVisibleFont.setter
    def SectionedSecondaryVisibleFont(self, sectionedSecondaryVisibleFont: NXOpen.Preferences.Font):
        """
        Setter for property: ( NXOpen.Preferences.Font) SectionedSecondaryVisibleFont
         Returns the Secondary sectioned visible font on the Ship Structure Lines   
            
         
        """
        pass
    @property
    def SectionedSecondaryVisibleWidth(self) -> NXOpen.Preferences.Width:
        """
        Getter for property: ( NXOpen.Preferences.Width) SectionedSecondaryVisibleWidth
         Returns the Secondary sectioned visible width on the Ship Structure Lines   
            
         
        """
        pass
    @SectionedSecondaryVisibleWidth.setter
    def SectionedSecondaryVisibleWidth(self, sectionedSecondaryVisibleWidth: NXOpen.Preferences.Width):
        """
        Setter for property: ( NXOpen.Preferences.Width) SectionedSecondaryVisibleWidth
         Returns the Secondary sectioned visible width on the Ship Structure Lines   
            
         
        """
        pass
    @property
    def SectionedVisibleColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) SectionedVisibleColor
         Returns the sectioned visible color on the Ship Structure Lines   
            
         
        """
        pass
    @SectionedVisibleColor.setter
    def SectionedVisibleColor(self, sectionedVisibleColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) SectionedVisibleColor
         Returns the sectioned visible color on the Ship Structure Lines   
            
         
        """
        pass
    @property
    def SectionedVisibleFont(self) -> NXOpen.Preferences.Font:
        """
        Getter for property: ( NXOpen.Preferences.Font) SectionedVisibleFont
         Returns the sectioned visible font on the Ship Structure Lines   
            
         
        """
        pass
    @SectionedVisibleFont.setter
    def SectionedVisibleFont(self, sectionedVisibleFont: NXOpen.Preferences.Font):
        """
        Setter for property: ( NXOpen.Preferences.Font) SectionedVisibleFont
         Returns the sectioned visible font on the Ship Structure Lines   
            
         
        """
        pass
    @property
    def SectionedVisibleWidth(self) -> NXOpen.Preferences.Width:
        """
        Getter for property: ( NXOpen.Preferences.Width) SectionedVisibleWidth
         Returns the sectioned visible width on the Ship Structure Lines   
            
         
        """
        pass
    @SectionedVisibleWidth.setter
    def SectionedVisibleWidth(self, sectionedVisibleWidth: NXOpen.Preferences.Width):
        """
        Setter for property: ( NXOpen.Preferences.Width) SectionedVisibleWidth
         Returns the sectioned visible width on the Ship Structure Lines   
            
         
        """
        pass
    @property
    def SingleLineRepresentation(self) -> bool:
        """
        Getter for property: (bool) SingleLineRepresentation
         Returns the single line representation toggle   
            
         
        """
        pass
    @SingleLineRepresentation.setter
    def SingleLineRepresentation(self, singleLineRepresentation: bool):
        """
        Setter for property: (bool) SingleLineRepresentation
         Returns the single line representation toggle   
            
         
        """
        pass
import NXOpen
import NXOpen.Preferences
class ShipDraftingViewLinesViewStyle(NXOpen.Object): 
    """ Represents set of Ship Drafting Lines View Style applicable to drafting views. 
        Ship Drafting View lines are used for the features in Ship Design """
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
        def ValueOf(value: int) -> ShipDraftingViewLinesViewStyle.Lines:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetColor(self, feature_name: str, lines_type: ShipDraftingViewLinesViewStyle.Lines) -> NXOpen.NXColor:
        """
         Gets line color. 
         Returns color ( NXOpen.NXColor): .
        """
        pass
    def GetFont(self, feature_name: str, lines_type: ShipDraftingViewLinesViewStyle.Lines) -> NXOpen.Preferences.Font:
        """
         Gets line font. 
         Returns font ( NXOpen.Preferences.Font): .
        """
        pass
    def GetShipDrawingObject(self, feature_name: str) -> bool:
        """
         Get ship drawing object status. 
         Returns single_line (bool):  status that determines SLR for the feature .
        """
        pass
    def GetWidth(self, feature_name: str, lines_type: ShipDraftingViewLinesViewStyle.Lines) -> NXOpen.Preferences.Width:
        """
         Gets line width 
         Returns width ( NXOpen.Preferences.Width): .
        """
        pass
    def SetColor(self, feature_name: str, lines_type: ShipDraftingViewLinesViewStyle.Lines, color: NXOpen.NXColor) -> None:
        """
         The color of ship line. The value should be between UF_OBJ_MIN_COLOR and UF_OBJ_MAX_COLOR. 
        """
        pass
    def SetFont(self, feature_name: str, lines_type: ShipDraftingViewLinesViewStyle.Lines, font: NXOpen.Preferences.Font) -> None:
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
    def SetWidth(self, feature_name: str, lines_type: ShipDraftingViewLinesViewStyle.Lines, width: NXOpen.Preferences.Width) -> None:
        """
         The width of ship line. 
        """
        pass
import NXOpen
class ShipGeneralArrangementViewLinesBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[ShipGeneralArrangementViewLinesBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: ShipGeneralArrangementViewLinesBuilder) -> None:
        """
         Appends an object to the list
            
        """
        pass
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
               not change, but the item at this index is set to NULL.
            
        """
        pass
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, obj: ShipGeneralArrangementViewLinesBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: ShipGeneralArrangementViewLinesBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: ShipGeneralArrangementViewLinesBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> ShipGeneralArrangementViewLinesBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( ShipGeneralArrangementViewLinesBuilder NXOpen.):  object found at input index .
        """
        pass
    def GetContents(self) -> List[ShipGeneralArrangementViewLinesBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( ShipGeneralArrangementViewLinesBuilder List[NXOpe):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: ShipGeneralArrangementViewLinesBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    def SetContents(self, objects: List[ShipGeneralArrangementViewLinesBuilder]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    @overload
    def Swap(self, object1: ShipGeneralArrangementViewLinesBuilder, object2: ShipGeneralArrangementViewLinesBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.Preferences
class ShipGeneralArrangementViewLinesBuilder(NXOpen.Builder): 
    """ Represents a ship view lines block """
    @property
    def AttributeName(self) -> str:
        """
        Getter for property: (str) AttributeName
         Returns the attribute name   
            
         
        """
        pass
    @AttributeName.setter
    def AttributeName(self, attributeName: str):
        """
        Setter for property: (str) AttributeName
         Returns the attribute name   
            
         
        """
        pass
    @property
    def AttributeValue(self) -> str:
        """
        Getter for property: (str) AttributeValue
         Returns the attribute value   
            
         
        """
        pass
    @AttributeValue.setter
    def AttributeValue(self, attributeValue: str):
        """
        Setter for property: (str) AttributeValue
         Returns the attribute value   
            
         
        """
        pass
    @property
    def HiddenColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) HiddenColor
         Returns the hidden color on the Ship General Arrangement Lines   
            
         
        """
        pass
    @HiddenColor.setter
    def HiddenColor(self, hiddenColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) HiddenColor
         Returns the hidden color on the Ship General Arrangement Lines   
            
         
        """
        pass
    @property
    def HiddenFont(self) -> NXOpen.Preferences.Font:
        """
        Getter for property: ( NXOpen.Preferences.Font) HiddenFont
         Returns the hidden font on the Ship General Arrangement Lines   
            
         
        """
        pass
    @HiddenFont.setter
    def HiddenFont(self, hiddenFont: NXOpen.Preferences.Font):
        """
        Setter for property: ( NXOpen.Preferences.Font) HiddenFont
         Returns the hidden font on the Ship General Arrangement Lines   
            
         
        """
        pass
    @property
    def HiddenWidth(self) -> NXOpen.Preferences.Width:
        """
        Getter for property: ( NXOpen.Preferences.Width) HiddenWidth
         Returns the hidden width on the Ship General Arrangement Lines   
            
         
        """
        pass
    @HiddenWidth.setter
    def HiddenWidth(self, hiddenWidth: NXOpen.Preferences.Width):
        """
        Setter for property: ( NXOpen.Preferences.Width) HiddenWidth
         Returns the hidden width on the Ship General Arrangement Lines   
            
         
        """
        pass
    @property
    def VisibleColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) VisibleColor
         Returns the visible color on the General Arrangement View Lines   
            
         
        """
        pass
    @VisibleColor.setter
    def VisibleColor(self, visibleColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) VisibleColor
         Returns the visible color on the General Arrangement View Lines   
            
         
        """
        pass
    @property
    def VisibleFont(self) -> NXOpen.Preferences.Font:
        """
        Getter for property: ( NXOpen.Preferences.Font) VisibleFont
         Returns the nvisible font on the Ship General Arrangement Lines   
            
         
        """
        pass
    @VisibleFont.setter
    def VisibleFont(self, visibleFont: NXOpen.Preferences.Font):
        """
        Setter for property: ( NXOpen.Preferences.Font) VisibleFont
         Returns the nvisible font on the Ship General Arrangement Lines   
            
         
        """
        pass
    @property
    def VisibleWidth(self) -> NXOpen.Preferences.Width:
        """
        Getter for property: ( NXOpen.Preferences.Width) VisibleWidth
         Returns the visible width on the Ship General Arrangement Lines   
            
         
        """
        pass
    @VisibleWidth.setter
    def VisibleWidth(self, visibleWidth: NXOpen.Preferences.Width):
        """
        Setter for property: ( NXOpen.Preferences.Width) VisibleWidth
         Returns the visible width on the Ship General Arrangement Lines   
            
         
        """
        pass
import NXOpen
import NXOpen.Preferences
class ShipGeneralArrangementViewLinesViewStyle(NXOpen.Object): 
    """ Represents set of Ship General Arrangement Lines View Style applicable to drafting views. 
        Ship General Arrangement View lines are used for the bodies in Ship General Arrangement application """
    class Lines(Enum):
        """
        Members Include: 
         |Visible|  Visible
         |Hidden|  Hidden 

        """
        Visible: int
        Hidden: int
        @staticmethod
        def ValueOf(value: int) -> ShipGeneralArrangementViewLinesViewStyle.Lines:
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
    def GetColor(self, viewPlan: str, displayName: str, lines_type: ShipGeneralArrangementViewLinesViewStyle.Lines) -> NXOpen.NXColor:
        """
         Gets line color. 
         Returns color ( NXOpen.NXColor): .
        """
        pass
    def GetFont(self, viewPlan: str, displayName: str, lines_type: ShipGeneralArrangementViewLinesViewStyle.Lines) -> NXOpen.Preferences.Font:
        """
         Gets line font. 
         Returns font ( NXOpen.Preferences.Font): .
        """
        pass
    def GetWidth(self, viewPlan: str, displayName: str, lines_type: ShipGeneralArrangementViewLinesViewStyle.Lines) -> NXOpen.Preferences.Width:
        """
         Gets line width 
         Returns width ( NXOpen.Preferences.Width): .
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
    def SetColor(self, viewPlan: str, displayName: str, lines_type: ShipGeneralArrangementViewLinesViewStyle.Lines, color: NXOpen.NXColor) -> None:
        """
         The color of ship general arrangement line. The value should be between UF_OBJ_MIN_COLOR and UF_OBJ_MAX_COLOR. 
        """
        pass
    def SetFont(self, viewPlan: str, displayName: str, lines_type: ShipGeneralArrangementViewLinesViewStyle.Lines, font: NXOpen.Preferences.Font) -> None:
        """
         The font type of ship line.
        """
        pass
    def SetWidth(self, viewPlan: str, displayName: str, lines_type: ShipGeneralArrangementViewLinesViewStyle.Lines, width: NXOpen.Preferences.Width) -> None:
        """
         The width of ship line. 
        """
        pass
class SketchedHalfSectionLine(BaseHalfSectionLine): 
    """ Sketched Half Section Line is sketch based section line.
        It is used to create a view with half of the part
        sectioned and the other half un-sectioned. Half sections are similar
        to simple and stepped sections in that the cut segment is parallel
        to the defined hinge line. Note that the Half Section Line contains
        only one arrow, one bend, and one cut segment. """
    pass
class SketchedPointToPointSectionLine(BasePointToPointSectionLine): 
    """ Sketched Point to Point Section Line is sketch based section line.
        It lets you create a view with multiple segment cuts with no bends."""
    pass
class SketchedSteppedSectionLine(BaseSteppedSectionLine): 
    """ A Sketched Simple or Stepped Section Line is sketch based section line.

        Sketched Simple Section Line provides one cut to form a view that allows you
        to see the inside of a part. The view is created by dividing the part
        with a single cutting plane.

        Stepped Section Line lets you create a section view which contains
        linear steps. You can make these steps by indicating multiple cuts,
        bends, and arrow segments. All bend and arrow segments are created
        perpendicular to cut segments. """
    pass
import NXOpen
class SketchSectionLineBuilder(NXOpen.Builder): 
    """ Represents a Drawings.SectionLine builder """
    class SectionLineTypes(Enum):
        """
        Members Include: 
         |SimpleStepped| 
         |Half| 
         |PoinToPoint| 

        """
        SimpleStepped: int
        Half: int
        PoinToPoint: int
        @staticmethod
        def ValueOf(value: int) -> SketchSectionLineBuilder.SectionLineTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Type(Enum):
        """
        Members Include: 
         |StandAlone| 
         |Derived| 

        """
        StandAlone: int
        Derived: int
        @staticmethod
        def ValueOf(value: int) -> SketchSectionLineBuilder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AssociateToSketch(self) -> bool:
        """
        Getter for property: (bool) AssociateToSketch
         Returns the associate to sketch   
            
         
        """
        pass
    @AssociateToSketch.setter
    def AssociateToSketch(self, associateToSketch: bool):
        """
        Setter for property: (bool) AssociateToSketch
         Returns the associate to sketch   
            
         
        """
        pass
    @property
    def FoldedToggle(self) -> bool:
        """
        Getter for property: (bool) FoldedToggle
         Returns the folded toggle   
            
         
        """
        pass
    @FoldedToggle.setter
    def FoldedToggle(self, foldedToggle: bool):
        """
        Setter for property: (bool) FoldedToggle
         Returns the folded toggle   
            
         
        """
        pass
    @property
    def ParentView(self) -> ParentViewBuilder:
        """
        Getter for property: ( ParentViewBuilder NXOpen.) ParentView
         Returns the parent view   
            
         
        """
        pass
    @property
    def ReverseDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseDirection
         Returns the reverse direction   
            
         
        """
        pass
    @ReverseDirection.setter
    def ReverseDirection(self, reverseDirection: bool):
        """
        Setter for property: (bool) ReverseDirection
         Returns the reverse direction   
            
         
        """
        pass
    @property
    def SectionLineType(self) -> SketchSectionLineBuilder.SectionLineTypes:
        """
        Getter for property: ( SketchSectionLineBuilder.SectionLineTypes NXOpen.) SectionLineType
         Returns the section line type   
            
         
        """
        pass
    @SectionLineType.setter
    def SectionLineType(self, sectionLineType: SketchSectionLineBuilder.SectionLineTypes):
        """
        Setter for property: ( SketchSectionLineBuilder.SectionLineTypes NXOpen.) SectionLineType
         Returns the section line type   
            
         
        """
        pass
    @property
    def SectionType(self) -> SketchSectionLineBuilder.Type:
        """
        Getter for property: ( SketchSectionLineBuilder.Type NXOpen.) SectionType
         Returns the section type   
            
         
        """
        pass
    @SectionType.setter
    def SectionType(self, sectionType: SketchSectionLineBuilder.Type):
        """
        Setter for property: ( SketchSectionLineBuilder.Type NXOpen.) SectionType
         Returns the section type   
            
         
        """
        pass
    @property
    def Settings(self) -> SectionLineSettingsBuilder:
        """
        Getter for property: ( SectionLineSettingsBuilder NXOpen.) Settings
         Returns the settings   
            
         
        """
        pass
    @property
    def SketchSection(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) SketchSection
         Returns the sketch section   
            
         
        """
        pass
    @property
    def SourceView(self) -> SelectDraftingView:
        """
        Getter for property: ( SelectDraftingView NXOpen.) SourceView
         Returns the source view   
            
         
        """
        pass
    def SetSketch(self, sketch: NXOpen.Sketch) -> None:
        """
         Set the sketch 
        """
        pass
import NXOpen
import NXOpen.Preferences
class SmoothEdgesViewStyle(NXOpen.Object): 
    """ Represents set of Smooth Edges View Style Preferences applicable to drafting views. """
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
    def SmoothEdgeFont(self) -> NXOpen.Preferences.Font:
        """
        Getter for property: ( NXOpen.Preferences.Font) SmoothEdgeFont
         Returns the font of smooth edge.  
            
         
        """
        pass
    @SmoothEdgeFont.setter
    def SmoothEdgeFont(self, smooth_edge_font: NXOpen.Preferences.Font):
        """
        Setter for property: ( NXOpen.Preferences.Font) SmoothEdgeFont
         Returns the font of smooth edge.  
            
         
        """
        pass
    @property
    def SmoothEdgeTolerance(self) -> bool:
        """
        Getter for property: (bool) SmoothEdgeTolerance
         Returns the status of smooth edge angle tolerance.  
           If True, the value set in 
                    the Tolerance Data field is used. If False, the system default tolerance is used.
                   
         
        """
        pass
    @SmoothEdgeTolerance.setter
    def SmoothEdgeTolerance(self, smooth_edge_tolerance: bool):
        """
        Setter for property: (bool) SmoothEdgeTolerance
         Returns the status of smooth edge angle tolerance.  
           If True, the value set in 
                    the Tolerance Data field is used. If False, the system default tolerance is used.
                   
         
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
    def SmoothEdgeWidth(self) -> NXOpen.Preferences.Width:
        """
        Getter for property: ( NXOpen.Preferences.Width) SmoothEdgeWidth
         Returns the width of smooth edge.  
            
         
        """
        pass
    @SmoothEdgeWidth.setter
    def SmoothEdgeWidth(self, smooth_edge_width: NXOpen.Preferences.Width):
        """
        Setter for property: ( NXOpen.Preferences.Width) SmoothEdgeWidth
         Returns the width of smooth edge.  
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SpecifySectionLineBuilder(NXOpen.TaggedObject): 
    """ Select a section line """
    @property
    def SectionLine(self) -> SelectSectionLine:
        """
        Getter for property: ( SelectSectionLine NXOpen.) SectionLine
         Returns the section line   
            
         
        """
        pass
import NXOpen
class StandardViewsBuilder(NXOpen.Builder): 
    """ This builder allows the user to create a Drawing View """
    class Placement(Enum):
        """
        Members Include: 
         |Center| 
         |Corner| 

        """
        Center: int
        Corner: int
        @staticmethod
        def ValueOf(value: int) -> StandardViewsBuilder.Placement:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Type(Enum):
        """
        Members Include: 
         |FrontTop| front, top 
         |FrontRight| front, right 
         |FrontLeft| front, left 
         |FrontTopRight| front, top, right
         |FrontTopLeft| front, top, left 
         |FrontTopRightIso| front, top, right, iso
         |FrontTopLeftIso| front, top, left, iso

        """
        FrontTop: int
        FrontRight: int
        FrontLeft: int
        FrontTopRight: int
        FrontTopLeft: int
        FrontTopRightIso: int
        FrontTopLeftIso: int
        @staticmethod
        def ValueOf(value: int) -> StandardViewsBuilder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class View(Enum):
        """
        Members Include: 
         |Drawing|  drawing (2d) views 
         |Base|  base views 

        """
        Drawing: int
        Base: int
        @staticmethod
        def ValueOf(value: int) -> StandardViewsBuilder.View:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Autoscale(self) -> bool:
        """
        Getter for property: (bool) Autoscale
         Returns the autoscale mode for base view creation   
            
         
        """
        pass
    @Autoscale.setter
    def Autoscale(self, autoScale: bool):
        """
        Setter for property: (bool) Autoscale
         Returns the autoscale mode for base view creation   
            
         
        """
        pass
    @property
    def Coordinate(self) -> ViewCenterCoordinateBuilder:
        """
        Getter for property: ( ViewCenterCoordinateBuilder NXOpen.) Coordinate
         Returns the center coordinate   
            
         
        """
        pass
    @property
    def FirstCorner(self) -> ViewPlacementBuilder:
        """
        Getter for property: ( ViewPlacementBuilder NXOpen.) FirstCorner
         Returns the first corner view placement   
            
         
        """
        pass
    @property
    def HiddenObjects(self) -> HiddenObjectsBuilder:
        """
        Getter for property: ( HiddenObjectsBuilder NXOpen.) HiddenObjects
         Returns the list of objects to not show in the view   
            
         
        """
        pass
    @property
    def LayoutType(self) -> StandardViewsBuilder.Type:
        """
        Getter for property: ( StandardViewsBuilder.Type NXOpen.) LayoutType
         Returns the Layout type   
            
         
        """
        pass
    @LayoutType.setter
    def LayoutType(self, type: StandardViewsBuilder.Type):
        """
        Setter for property: ( StandardViewsBuilder.Type NXOpen.) LayoutType
         Returns the Layout type   
            
         
        """
        pass
    @property
    def MarginBetweenViews(self) -> float:
        """
        Getter for property: (float) MarginBetweenViews
         Returns the margin between views   
            
         
        """
        pass
    @MarginBetweenViews.setter
    def MarginBetweenViews(self, marginBetweenViews: float):
        """
        Setter for property: (float) MarginBetweenViews
         Returns the margin between views   
            
         
        """
        pass
    @property
    def MarginToBorder(self) -> float:
        """
        Getter for property: (float) MarginToBorder
         Returns the margin to border   
            
         
        """
        pass
    @MarginToBorder.setter
    def MarginToBorder(self, marginToBorder: float):
        """
        Setter for property: (float) MarginToBorder
         Returns the margin to border   
            
         
        """
        pass
    @property
    def MultipleViewPlacement(self) -> MultipleViewPlacementBuilder:
        """
        Getter for property: ( MultipleViewPlacementBuilder NXOpen.) MultipleViewPlacement
         Returns the multiple view placement   
            
         
        """
        pass
    @property
    def NonSectionedObjects(self) -> HiddenObjectsBuilder:
        """
        Getter for property: ( HiddenObjectsBuilder NXOpen.) NonSectionedObjects
         Returns the list of objects to not section in the view   
            
         
        """
        pass
    @property
    def Part(self) -> NXOpen.Part:
        """
        Getter for property: ( NXOpen.Part) Part
         Returns the part to use for base views   
            
         
        """
        pass
    @Part.setter
    def Part(self, part: NXOpen.Part):
        """
        Setter for property: ( NXOpen.Part) Part
         Returns the part to use for base views   
            
         
        """
        pass
    @property
    def PlacementType(self) -> StandardViewsBuilder.Placement:
        """
        Getter for property: ( StandardViewsBuilder.Placement NXOpen.) PlacementType
         Returns the Placement type   
            
         
        """
        pass
    @PlacementType.setter
    def PlacementType(self, type: StandardViewsBuilder.Placement):
        """
        Setter for property: ( StandardViewsBuilder.Placement NXOpen.) PlacementType
         Returns the Placement type   
            
         
        """
        pass
    @property
    def Scale(self) -> ViewScaleBuilder:
        """
        Getter for property: ( ViewScaleBuilder NXOpen.) Scale
         Returns the view scale   
            
         
        """
        pass
    @property
    def SecondCorner(self) -> ViewPlacementBuilder:
        """
        Getter for property: ( ViewPlacementBuilder NXOpen.) SecondCorner
         Returns the second corner view placement   
            
         
        """
        pass
    @property
    def SecondaryComponents(self) -> DraftingComponentSelectionBuilder:
        """
        Getter for property: ( DraftingComponentSelectionBuilder NXOpen.) SecondaryComponents
         Returns the list of secondary objects in the view   
            
         
        """
        pass
    @property
    def ViewPlacement(self) -> ViewPlacementBuilder:
        """
        Getter for property: ( ViewPlacementBuilder NXOpen.) ViewPlacement
         Returns the view placement   
            
         
        """
        pass
    @property
    def ViewStyle(self) -> ViewStyleBuilder:
        """
        Getter for property: ( ViewStyleBuilder NXOpen.) ViewStyle
         Returns the view style   
            
         
        """
        pass
    @property
    def ViewType(self) -> StandardViewsBuilder.View:
        """
        Getter for property: ( StandardViewsBuilder.View NXOpen.) ViewType
         Returns the view type   
            
         
        """
        pass
    @ViewType.setter
    def ViewType(self, viewType: StandardViewsBuilder.View):
        """
        Setter for property: ( StandardViewsBuilder.View NXOpen.) ViewType
         Returns the view type   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SteppedSectionLineBuilder(NXOpen.TaggedObject): 
    """ Represents a NXOpen.Drawings.SteppedSectionLineBuilder.
        This class is used to create or edit a
        NXOpen.Drawings.SteppedSectionLine. """
    @property
    def EndLocation1(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) EndLocation1
         Returns the end location 1 which determines the position of the
                    first arrow segment in the section line.  
             
         
        """
        pass
    @EndLocation1.setter
    def EndLocation1(self, endLocation1: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) EndLocation1
         Returns the end location 1 which determines the position of the
                    first arrow segment in the section line.  
             
         
        """
        pass
    @property
    def EndLocation2(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) EndLocation2
         Returns the end location 2 which determines the position of the
                    second arrow segment in the section line   
            
         
        """
        pass
    @EndLocation2.setter
    def EndLocation2(self, endLocation2: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) EndLocation2
         Returns the end location 2 which determines the position of the
                    second arrow segment in the section line   
            
         
        """
        pass
    @property
    def Leg1(self) -> SectionLineSegmentBuilderList:
        """
        Getter for property: ( SectionLineSegmentBuilderList NXOpen.) Leg1
         Returns the list of cut and bend segments.  
          
                    The list will contain  NXOpen::Drawings::SectionLineSegmentBuilder::TypesCut 
                    and  NXOpen::Drawings::SectionLineSegmentBuilder::TypesBend  types
                    of  NXOpen::Drawings::SectionLineSegmentBuilder  segments.
                    Note that there is no order to the elements of this list since the order is
                    determined by the hinge direction.   
         
        """
        pass
class SteppedSectionLine(BaseSteppedSectionLine): 
    """ A Simple or Stepped Section Line.

        Simple Section Line provides one cut to form a view that allows you
        to see the inside of a part. The view is created by dividing the part
        with a single cutting plane.

        Stepped Section Line lets you create a section view which contains
        linear steps. You can make these steps by indicating multiple cuts,
        bends, and arrow segments. All bend and arrow segments are created
        perpendicular to cut segments. """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class SvtBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.Drawings.SvtBuilder
    """
    @property
    def BackgroundFaces(self) -> NXOpen.SelectFaceList:
        """
        Getter for property: ( NXOpen.SelectFaceList) BackgroundFaces
         Returns the background faces that are to be shown in the section view.  
            When none are selected, all faces will be shown   
         
        """
        pass
    @property
    def NormalDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) NormalDirection
         Returns the vector that represents the normal direction for the view to be created or edited.  
          
                    The vector is used only if the Orientation flag is on.  The purpose of the direction
                    vectors is make a simple, simulated pictorial view.  Consequently it is expected that
                    a desireable orientation will need to be found interactive using the tool, and that
                    specification by vectors will be of marginal use.  The ability to specifiy the orientation
                    is being included only for completeness.   
         
        """
        pass
    @NormalDirection.setter
    def NormalDirection(self, normalDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) NormalDirection
         Returns the vector that represents the normal direction for the view to be created or edited.  
          
                    The vector is used only if the Orientation flag is on.  The purpose of the direction
                    vectors is make a simple, simulated pictorial view.  Consequently it is expected that
                    a desireable orientation will need to be found interactive using the tool, and that
                    specification by vectors will be of marginal use.  The ability to specifiy the orientation
                    is being included only for completeness.   
         
        """
        pass
    @property
    def Orientation(self) -> bool:
        """
        Getter for property: (bool) Orientation
         Returns the orientation flag that indicates whether or not the Section View Tool view should be used to orient the section view when it is placed   
            
         
        """
        pass
    @Orientation.setter
    def Orientation(self, orientation: bool):
        """
        Setter for property: (bool) Orientation
         Returns the orientation flag that indicates whether or not the Section View Tool view should be used to orient the section view when it is placed   
            
         
        """
        pass
    @property
    def XDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) XDirection
         Returns the x direction vector for the view to be created or edited.  
          
                    The vector is used only if the Orientation flag is on.  The purpose of the direction
                    vectors is make a simple, simulated pictorial view.  Consequently it is expected that
                    a desireable orientation will need to be found interactive using the tool, and that
                    specification by vectors will be of marginal use.  The ability to specifiy the orientation
                    is being included only for completeness.   
         
        """
        pass
    @XDirection.setter
    def XDirection(self, xDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) XDirection
         Returns the x direction vector for the view to be created or edited.  
          
                    The vector is used only if the Orientation flag is on.  The purpose of the direction
                    vectors is make a simple, simulated pictorial view.  Consequently it is expected that
                    a desireable orientation will need to be found interactive using the tool, and that
                    specification by vectors will be of marginal use.  The ability to specifiy the orientation
                    is being included only for completeness.   
         
        """
        pass
import NXOpen
import NXOpen.Preferences
class ThreadsViewStyle(NXOpen.Object): 
    """ Represents set of Threads View Style Preferences applicable to drafting views. 
        Allows to create ANSI and ISO thread representations for both internal 
        and external threads in drawing member views.
     """
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
         Returns the threads standard option   
            
         
        """
        pass
    @ThreadsStandardOptionData.setter
    def ThreadsStandardOptionData(self, threads_standard_option_data: int):
        """
        Setter for property: (int) ThreadsStandardOptionData
         Returns the threads standard option   
            
         
        """
        pass
import NXOpen
import NXOpen.Preferences
class TraceLinesViewStyle(NXOpen.Object): 
    """ Represents interface for Trace Lines View Style Preferences applicable to drafting views. """
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
         Returns the gap size   
            
         
        """
        pass
    @GapSize.setter
    def GapSize(self, gap_size: float):
        """
        Setter for property: (float) GapSize
         Returns the gap size   
            
         
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
    def HiddenFont(self) -> NXOpen.Preferences.Font:
        """
        Getter for property: ( NXOpen.Preferences.Font) HiddenFont
         Returns the hidden font   
            
         
        """
        pass
    @HiddenFont.setter
    def HiddenFont(self, hidden_font: NXOpen.Preferences.Font):
        """
        Setter for property: ( NXOpen.Preferences.Font) HiddenFont
         Returns the hidden font   
            
         
        """
        pass
    @property
    def HiddenWidth(self) -> NXOpen.Preferences.Width:
        """
        Getter for property: ( NXOpen.Preferences.Width) HiddenWidth
         Returns the hidden width   
            
         
        """
        pass
    @HiddenWidth.setter
    def HiddenWidth(self, hidden_width: NXOpen.Preferences.Width):
        """
        Setter for property: ( NXOpen.Preferences.Width) HiddenWidth
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
    def VisibleFont(self) -> NXOpen.Preferences.Font:
        """
        Getter for property: ( NXOpen.Preferences.Font) VisibleFont
         Returns the visible font   
            
         
        """
        pass
    @VisibleFont.setter
    def VisibleFont(self, visible_font: NXOpen.Preferences.Font):
        """
        Setter for property: ( NXOpen.Preferences.Font) VisibleFont
         Returns the visible font   
            
         
        """
        pass
    @property
    def VisibleWidth(self) -> NXOpen.Preferences.Width:
        """
        Getter for property: ( NXOpen.Preferences.Width) VisibleWidth
         Returns the visible width   
            
         
        """
        pass
    @VisibleWidth.setter
    def VisibleWidth(self, visible_width: NXOpen.Preferences.Width):
        """
        Setter for property: ( NXOpen.Preferences.Width) VisibleWidth
         Returns the visible width   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class TrackDrawingChangesGeneralBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.Drawings.TrackDrawingChangesGeneralBuilder
    """
    class BaselineOfComparisonType(Enum):
        """
        Members Include: 
         |Snapshot| 
         |TrackedChanges| 

        """
        Snapshot: int
        TrackedChanges: int
        @staticmethod
        def ValueOf(value: int) -> TrackDrawingChangesGeneralBuilder.BaselineOfComparisonType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CompareMethodType(Enum):
        """
        Members Include: 
         |AgainstAnotherDrawing| This option is used to compare different part over current part
         |AgainstSnapshotDataInActiveDrawing| This option is used to compare current part on itself
         |OpenSavedComparisonReport| This option is used to open a compare report that is saved in the current part

        """
        AgainstAnotherDrawing: int
        AgainstSnapshotDataInActiveDrawing: int
        OpenSavedComparisonReport: int
        @staticmethod
        def ValueOf(value: int) -> TrackDrawingChangesGeneralBuilder.CompareMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SnapshotDataToUseType(Enum):
        """
        Members Include: 
         |AskAtRunTime|  This option tells to show messages at rumtime 
         |AlwaysUseExistingData|  This option will use existing snapshot data 
         |AlwaysCreateNewData|  This option will always create new snapshot data
         |CreateNewDataifNoneExists|  This option will create new sanpshot data if none exists

        """
        AskAtRunTime: int
        AlwaysUseExistingData: int
        AlwaysCreateNewData: int
        CreateNewDataifNoneExists: int
        @staticmethod
        def ValueOf(value: int) -> TrackDrawingChangesGeneralBuilder.SnapshotDataToUseType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SymbolType(Enum):
        """
        Members Include: 
         |Circle| 
         |TriangleUp| 
         |TriangleDown| 
         |Square| 
         |Hexagon| 

        """
        Circle: int
        TriangleUp: int
        TriangleDown: int
        Square: int
        Hexagon: int
        @staticmethod
        def ValueOf(value: int) -> TrackDrawingChangesGeneralBuilder.SymbolType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BaselineOfComparison(self) -> TrackDrawingChangesGeneralBuilder.BaselineOfComparisonType:
        """
        Getter for property: ( TrackDrawingChangesGeneralBuilder.BaselineOfComparisonType NXOpen.) BaselineOfComparison
         Returns the baseline of comparison   
            
         
        """
        pass
    @BaselineOfComparison.setter
    def BaselineOfComparison(self, baselineOfComparison: TrackDrawingChangesGeneralBuilder.BaselineOfComparisonType):
        """
        Setter for property: ( TrackDrawingChangesGeneralBuilder.BaselineOfComparisonType NXOpen.) BaselineOfComparison
         Returns the baseline of comparison   
            
         
        """
        pass
    @property
    def ChangeSymbolLineColorFontWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) ChangeSymbolLineColorFontWidth
         Returns the change symbol line color font width   
            
         
        """
        pass
    @property
    def ChangeSymbolSize(self) -> float:
        """
        Getter for property: (float) ChangeSymbolSize
         Returns the change symbol size   
            
         
        """
        pass
    @ChangeSymbolSize.setter
    def ChangeSymbolSize(self, symbolSize: float):
        """
        Setter for property: (float) ChangeSymbolSize
         Returns the change symbol size   
            
         
        """
        pass
    @property
    def ChangeSymbolType(self) -> TrackDrawingChangesGeneralBuilder.SymbolType:
        """
        Getter for property: ( TrackDrawingChangesGeneralBuilder.SymbolType NXOpen.) ChangeSymbolType
         Returns the change symbol type   
            
         
        """
        pass
    @ChangeSymbolType.setter
    def ChangeSymbolType(self, symbolType: TrackDrawingChangesGeneralBuilder.SymbolType):
        """
        Setter for property: ( TrackDrawingChangesGeneralBuilder.SymbolType NXOpen.) ChangeSymbolType
         Returns the change symbol type   
            
         
        """
        pass
    @property
    def CompareMethod(self) -> TrackDrawingChangesGeneralBuilder.CompareMethodType:
        """
        Getter for property: ( TrackDrawingChangesGeneralBuilder.CompareMethodType NXOpen.) CompareMethod
         Returns the compare method    
            
         
        """
        pass
    @CompareMethod.setter
    def CompareMethod(self, compareMethod: TrackDrawingChangesGeneralBuilder.CompareMethodType):
        """
        Setter for property: ( TrackDrawingChangesGeneralBuilder.CompareMethodType NXOpen.) CompareMethod
         Returns the compare method    
            
         
        """
        pass
    @property
    def CompareTolerance(self) -> float:
        """
        Getter for property: (float) CompareTolerance
         Returns the compare tolerance   
            
         
        """
        pass
    @CompareTolerance.setter
    def CompareTolerance(self, compareTolerance: float):
        """
        Setter for property: (float) CompareTolerance
         Returns the compare tolerance   
            
         
        """
        pass
    @property
    def CreateOverlayDataWithSnapshotData(self) -> bool:
        """
        Getter for property: (bool) CreateOverlayDataWithSnapshotData
         Returns the create overlay data with snapshot data   
            
         
        """
        pass
    @CreateOverlayDataWithSnapshotData.setter
    def CreateOverlayDataWithSnapshotData(self, createOverlayDataWithSnapshotData: bool):
        """
        Setter for property: (bool) CreateOverlayDataWithSnapshotData
         Returns the create overlay data with snapshot data   
            
         
        """
        pass
    @property
    def DisplayChangeSymbol(self) -> bool:
        """
        Getter for property: (bool) DisplayChangeSymbol
         Returns the display change symbol   
            
         
        """
        pass
    @DisplayChangeSymbol.setter
    def DisplayChangeSymbol(self, displayChangeSymbol: bool):
        """
        Setter for property: (bool) DisplayChangeSymbol
         Returns the display change symbol   
            
         
        """
        pass
    @property
    def IncrementIDNumberPerReport(self) -> bool:
        """
        Getter for property: (bool) IncrementIDNumberPerReport
         Returns the increment id number per report   
            
         
        """
        pass
    @IncrementIDNumberPerReport.setter
    def IncrementIDNumberPerReport(self, incrementIDNumberPerReport: bool):
        """
        Setter for property: (bool) IncrementIDNumberPerReport
         Returns the increment id number per report   
            
         
        """
        pass
    @property
    def PreserveChangeSymbolDisplay(self) -> bool:
        """
        Getter for property: (bool) PreserveChangeSymbolDisplay
         Returns the preserve Change Symbol Display   
            
         
        """
        pass
    @PreserveChangeSymbolDisplay.setter
    def PreserveChangeSymbolDisplay(self, preserveChangeSymbolDisplay: bool):
        """
        Setter for property: (bool) PreserveChangeSymbolDisplay
         Returns the preserve Change Symbol Display   
            
         
        """
        pass
    @property
    def RestartIDNumbersWithNewReport(self) -> bool:
        """
        Getter for property: (bool) RestartIDNumbersWithNewReport
         Returns the restart id numbers with new report   
            
         
        """
        pass
    @RestartIDNumbersWithNewReport.setter
    def RestartIDNumbersWithNewReport(self, restartIDNumbersWithNewReport: bool):
        """
        Setter for property: (bool) RestartIDNumbersWithNewReport
         Returns the restart id numbers with new report   
            
         
        """
        pass
    @property
    def SnapshotDataToUse(self) -> TrackDrawingChangesGeneralBuilder.SnapshotDataToUseType:
        """
        Getter for property: ( TrackDrawingChangesGeneralBuilder.SnapshotDataToUseType NXOpen.) SnapshotDataToUse
         Returns the snapshot data to use   
            
         
        """
        pass
    @SnapshotDataToUse.setter
    def SnapshotDataToUse(self, snapshotDataToUse: TrackDrawingChangesGeneralBuilder.SnapshotDataToUseType):
        """
        Setter for property: ( TrackDrawingChangesGeneralBuilder.SnapshotDataToUseType NXOpen.) SnapshotDataToUse
         Returns the snapshot data to use   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class TrackDrawingChangesReportFilterBuilder(NXOpen.TaggedObject): 
    """
    Represents a Drawings.TrackDrawingChangesReportFilterBuilder
    """
    class Filter(Enum):
        """
        Members Include: 
         |Sheets|  Sheet Report Filter                         
         |Views|  Views Report Filter                         
         |DimensionsAll|  Dimension All Report Filter                 
         |DimensionsRetainedStatus|  Dimension Retained Status Report Filter     
         |DimensionsSize|  Dimension Size Report Filter                
         |DimensionsOrigin|  Dimension Origin Report Filter              
         |AnnotationNotes|  Annotation Notes Report Filter
         |AnnotationNotesRetainedStatus|  Annotation Notes Retained Status Report Filter
         |AnnotationNotesText|  Annotation Notes Text Report Filter
         |AnnotationNotesOrigin|  Annotation Notes Origin Report Filter
         |AnnotationNotesLeaderTerminator|  Annotation Notes Leader Terminator Report Filter
         |AnnotationFCF|  Annotation Feature Control Frame Report Filter
         |AnnotationFCFRetainedStatus|  Annotation Feature Control Frame Retained Status Report Filter
         |AnnotationFCFText|  Annotation Feature Control Frame Text Report Filter
         |AnnotationFCFOrigin|  Annotation Feature Control Frame Origin Report Filter
         |AnnotationFCFLeaderTerminator|  Annotation Feature Control Frame Leader Terminator Report Filter
         |AnnotationDFS|  Annotation Datum Feature Symbol Report Filter
         |AnnotationDFSRetainedStatus|  Annotation Datum Feature Symbol Retained Status Report Filter
         |AnnotationDFSText|  Annotation Datum Feature Symbol Text Report Filter
         |AnnotationDFSOrigin|  Annotation Datum Feature Symbol Origin Report Filter
         |AnnotationDFSLeaderTerminator|  Annotation Datum Feature Symbol Leader Terminator Report Filter
         |AnnotationDTS|  Annotation Datum Target Symbol Report Filter
         |AnnotationDTSRetainedStatus|  Annotation Datum Target Symbol Retained Status Report Filter
         |AnnotationDTSText|  Annotation Datum Target Symbol Text Report Filter
         |AnnotationDTSOrigin|  Annotation Datum Target Symbol Origin Report Filter
         |AnnotationDTSLeaderTerminator|  Annotation Datum Target Symbol LeaderTerminator Report Filter
         |AnnotationBalloons|  Annotation Balloons Report Filter
         |AnnotationBalloonsRetainedStatus|  Annotation Balloons Retained Status Report Filter
         |AnnotationBalloonsText|  Annotation Balloons Text Report Filter
         |AnnotationBalloonsOrigin|  Annotation Balloons Origin Report Filter
         |AnnotationBalloonsLeaderTerminator|  Annotation Balloons LeaderTerminator Report Filter
         |AnnotationEdgeConditionSymbols|  Annotation Edge Condition Symbols Report Filter
         |AnnotationEdgeConditionSymbolsRetainedStatus|  Annotation Edge Condition Symbols Retained Status Report Filter
         |AnnotationEdgeConditionSymbolsText|  Annotation Edge Condition Symbols Text Report Filter
         |AnnotationEdgeConditionSymbolsOrigin|  Annotation Edge Condition Symbols Origin Report Filter
         |AnnotationEdgeConditionSymbolsLeaderTerminator|  Annotation Edge Condition Symbols LeaderTerminator Report Filter
         |AnnotationSFS|  Annotation Surface Finish Symbol Report Filter
         |AnnotationSFSRetainedStatus|  Annotation Surface Finish Symbol Retained Status Report Filter
         |AnnotationSFSText|  Annotation Surface Finish Symbol Text Report Filter
         |AnnotationSFSOrigin|  Annotation Surface Finish Symbol Origin Report Filter
         |AnnotationSFSLeaderTerminator|  Annotation Surface Finish Symbol LeaderTerminator Report Filter
         |AnnotationWeldSymbol|  Annotation Weld Symbol Report Filter
         |AnnotationWeldSymbolRetainedStatus|  Annotation Weld Symbol Retained Status Report Filter
         |AnnotationWeldSymbolText|  Annotation Weld Symbol Text Report Filter
         |AnnotationWeldSymbolOrigin|  Annotation Weld Symbol Origin Report Filter
         |AnnotationWeldSymbolLeaderTerminator|  Annotation Weld Symbol LeaderTerminator Report Filter
         |AnnotationTPS|  Annotation Target Point Symbol Report Filter
         |AnnotationInterSymbol|  Annotation Intersection Symbol Report Filter
         |AnnotationCrosshatch|  Annotation Crosshatch Report Filter
         |AnnotationCenterlines|  Annotation Centerlines Report Filter
         |Symbols|  Symbols Report Filter
         |SymbolsRetainedStatus|  Symbols Retained Status Report Filter
         |SymbolsText|  Symbols Text Report Filter
         |SymbolsOrigin|  Symbols Origin Report Filter
         |SymbolsLeaderTerminator|  Symbols Leader Terminator Report Filter
         |Tables|  Tables Report Filter
         |PartsLists|  Parts Lists Report Filter
         |HoleTable|  Hole Table Report Filter
         |SketchCurvesLines|  Sketch Curves lines filter
         |SketchCurvesArcs|  Sketch Curves arcs filter
         |SketchCurvesCircles|  Sketch Curves circles filter
         |SketchCurvesConics|  Sketch Curves conics filter
         |SketchCurvesSplines|  Sketch Curves splines filter

        """
        Sheets: int
        Views: int
        DimensionsAll: int
        DimensionsRetainedStatus: int
        DimensionsSize: int
        DimensionsOrigin: int
        AnnotationNotes: int
        AnnotationNotesRetainedStatus: int
        AnnotationNotesText: int
        AnnotationNotesOrigin: int
        AnnotationNotesLeaderTerminator: int
        AnnotationFCF: int
        AnnotationFCFRetainedStatus: int
        AnnotationFCFText: int
        AnnotationFCFOrigin: int
        AnnotationFCFLeaderTerminator: int
        AnnotationDFS: int
        AnnotationDFSRetainedStatus: int
        AnnotationDFSText: int
        AnnotationDFSOrigin: int
        AnnotationDFSLeaderTerminator: int
        AnnotationDTS: int
        AnnotationDTSRetainedStatus: int
        AnnotationDTSText: int
        AnnotationDTSOrigin: int
        AnnotationDTSLeaderTerminator: int
        AnnotationBalloons: int
        AnnotationBalloonsRetainedStatus: int
        AnnotationBalloonsText: int
        AnnotationBalloonsOrigin: int
        AnnotationBalloonsLeaderTerminator: int
        AnnotationEdgeConditionSymbols: int
        AnnotationEdgeConditionSymbolsRetainedStatus: int
        AnnotationEdgeConditionSymbolsText: int
        AnnotationEdgeConditionSymbolsOrigin: int
        AnnotationEdgeConditionSymbolsLeaderTerminator: int
        AnnotationSFS: int
        AnnotationSFSRetainedStatus: int
        AnnotationSFSText: int
        AnnotationSFSOrigin: int
        AnnotationSFSLeaderTerminator: int
        AnnotationWeldSymbol: int
        AnnotationWeldSymbolRetainedStatus: int
        AnnotationWeldSymbolText: int
        AnnotationWeldSymbolOrigin: int
        AnnotationWeldSymbolLeaderTerminator: int
        AnnotationTPS: int
        AnnotationInterSymbol: int
        AnnotationCrosshatch: int
        AnnotationCenterlines: int
        Symbols: int
        SymbolsRetainedStatus: int
        SymbolsText: int
        SymbolsOrigin: int
        SymbolsLeaderTerminator: int
        Tables: int
        PartsLists: int
        HoleTable: int
        SketchCurvesLines: int
        SketchCurvesArcs: int
        SketchCurvesCircles: int
        SketchCurvesConics: int
        SketchCurvesSplines: int
        @staticmethod
        def ValueOf(value: int) -> TrackDrawingChangesReportFilterBuilder.Filter:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetReportFilterStatus(self, reportFilterType: TrackDrawingChangesReportFilterBuilder.Filter) -> bool:
        """
         Returns report filter status 
         Returns reportFilterStatus (bool): .
        """
        pass
    def SetReportFilterStatus(self, reportFilterType: TrackDrawingChangesReportFilterBuilder.Filter, reportFilterStatus: bool) -> None:
        """
         Sets report filter status 
        """
        pass
class TrimmingMarkStyleType(Enum):
    """
    Members Include: 
     |Triangle|  Triangle 
     |Corner| 

    """
    Triangle: int
    Corner: int
    @staticmethod
    def ValueOf(value: int) -> TrimmingMarkStyleType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class UpdateViewsBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Drawings.UpdateViewsBuilder
    """
    @property
    def Views(self) -> NXOpen.SelectObjectList:
        """
        Getter for property: ( NXOpen.SelectObjectList) Views
         Returns the selected views   
            
         
        """
        pass
class VerticalCenteringMarkType(Enum):
    """
    Members Include: 
     |NotSet|  None 
     |BottomArrow|  Bottom Arrow 
     |TopArrow|  Top Arrow 
     |BottomandTopArrow|  Bottom and Top Arrow 
     |BottomandTopLine| 

    """
    NotSet: int
    BottomArrow: int
    TopArrow: int
    BottomandTopArrow: int
    BottomandTopLine: int
    @staticmethod
    def ValueOf(value: int) -> VerticalCenteringMarkType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class View2dOrientBuilder(NXOpen.TaggedObject): 
    """ Represents the View 2D Orientation (Drawings.View2dOrientBuilder)
    """
    class CustomMethod(Enum):
        """
        Members Include: 
         |Angles|  axis rotations 
         |Vector|  cartesian vector

        """
        Angles: int
        Vector: int
        @staticmethod
        def ValueOf(value: int) -> View2dOrientBuilder.CustomMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Type(Enum):
        """
        Members Include: 
         |NotSet|  not oriented 
         |Top|  top view 
         |Front|  front view 
         |Right|  right view 
         |Back|  back view 
         |Bottom|  bottom view 
         |Left|  left view 
         |Iso|  isometric view 
         |Tri|  trimetric view 
         |Custom|  custom method used 

        """
        NotSet: int
        Top: int
        Front: int
        Right: int
        Back: int
        Bottom: int
        Left: int
        Iso: int
        Tri: int
        Custom: int
        @staticmethod
        def ValueOf(value: int) -> View2dOrientBuilder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CustomOrientationMethod(self) -> View2dOrientBuilder.CustomMethod:
        """
        Getter for property: ( View2dOrientBuilder.CustomMethod NXOpen.) CustomOrientationMethod
         Returns the custom orientation method   
            
         
        """
        pass
    @CustomOrientationMethod.setter
    def CustomOrientationMethod(self, methd: View2dOrientBuilder.CustomMethod):
        """
        Setter for property: ( View2dOrientBuilder.CustomMethod NXOpen.) CustomOrientationMethod
         Returns the custom orientation method   
            
         
        """
        pass
    @property
    def CustomXAngle(self) -> float:
        """
        Getter for property: (float) CustomXAngle
         Returns the orientation angle around the X axis   
            
         
        """
        pass
    @CustomXAngle.setter
    def CustomXAngle(self, angle: float):
        """
        Setter for property: (float) CustomXAngle
         Returns the orientation angle around the X axis   
            
         
        """
        pass
    @property
    def CustomYAngle(self) -> float:
        """
        Getter for property: (float) CustomYAngle
         Returns the orientation angle around the Y axis   
            
         
        """
        pass
    @CustomYAngle.setter
    def CustomYAngle(self, angle: float):
        """
        Setter for property: (float) CustomYAngle
         Returns the orientation angle around the Y axis   
            
         
        """
        pass
    @property
    def CustomZAngle(self) -> float:
        """
        Getter for property: (float) CustomZAngle
         Returns the orientation angle around the Z axis   
            
         
        """
        pass
    @CustomZAngle.setter
    def CustomZAngle(self, angle: float):
        """
        Setter for property: (float) CustomZAngle
         Returns the orientation angle around the Z axis   
            
         
        """
        pass
    @property
    def OrientationType(self) -> View2dOrientBuilder.Type:
        """
        Getter for property: ( View2dOrientBuilder.Type NXOpen.) OrientationType
         Returns the orientation type   
            
         
        """
        pass
    @OrientationType.setter
    def OrientationType(self, type: View2dOrientBuilder.Type):
        """
        Setter for property: ( View2dOrientBuilder.Type NXOpen.) OrientationType
         Returns the orientation type   
            
         
        """
        pass
    def GetCustomNormalX(self) -> float:
        """
         Returns the X component of the custom view-normal vector 
         Returns component (float):  returns the X component of view normal in global CS .
        """
        pass
    def GetCustomNormalY(self) -> float:
        """
         Returns the Y component of the custom view-normal vector 
         Returns component (float):  returns the Y component of view normal in global CS .
        """
        pass
    def GetCustomNormalZ(self) -> float:
        """
         Returns the Z component of the custom view-normal vector 
         Returns component (float):  returns the Z component of view normal in global CS .
        """
        pass
    def GetCustomPrimaryX(self) -> float:
        """
         Returns the X component of the custom view-primary vector 
         Returns component (float):  returns the X component of view primary vector in global CS .
        """
        pass
    def GetCustomPrimaryY(self) -> float:
        """
         Returns the Y component of the custom view-primary vector 
         Returns component (float):  returns the Y component of view primary vector in global CS .
        """
        pass
    def GetCustomPrimaryZ(self) -> float:
        """
        Returns the Z component of the custom view-primary vector 
         Returns component (float):  returns the Z component of view primary vector in global CS .
        """
        pass
    def GetInferredPrimary(self) -> bool:
        """
         Returns the option to infer the direction view X vector in 3D space 
         Returns inferred (bool):  returns the inferred option .
        """
        pass
    def SetCustomNormalX(self, component: float) -> None:
        """
        Sets the X component of the custom view-normal vector  
        """
        pass
    def SetCustomNormalY(self, component: float) -> None:
        """
         Sets the Y component of the custom view-normal vector 
        """
        pass
    def SetCustomNormalZ(self, component: float) -> None:
        """
         Sets the Z component of the custom view-normal vector 
        """
        pass
    def SetCustomPrimaryX(self, component: float) -> None:
        """
         Sets the X component of the custom view-primary vector 
        """
        pass
    def SetCustomPrimaryY(self, component: float) -> None:
        """
         Sets the Y component of the custom view-primary vector 
        """
        pass
    def SetCustomPrimaryZ(self, component: float) -> None:
        """
        Sets the Z component of the custom view-primary vector 
        """
        pass
    def SetInferredPrimary(self, inferred: bool) -> None:
        """
         Sets the option to infer the direction view X vector in 3D space 
        """
        pass
import NXOpen
class ViewAlignmentBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Drawings.ViewAlignmentBuilder.This class is used to construct the view alignment Builder """
    @property
    def CandidateView(self) -> DraftingView:
        """
        Getter for property: ( DraftingView NXOpen.) CandidateView
         Returns the candidate view in builder  
            
         
        """
        pass
    @CandidateView.setter
    def CandidateView(self, candidateView: DraftingView):
        """
        Setter for property: ( DraftingView NXOpen.) CandidateView
         Returns the candidate view in builder  
            
         
        """
        pass
    @property
    def InEditMode(self) -> bool:
        """
        Getter for property: (bool) InEditMode
         Returns the builder edit mode flag.  
          
                    There are two modes in the view alignment dialog, Create and Edit modes, and the flag determines the current mode. 
                    View alignment can be created in Create mode, and edited or deleted in Edit mode.   
         
        """
        pass
    @InEditMode.setter
    def InEditMode(self, inEditMode: bool):
        """
        Setter for property: (bool) InEditMode
         Returns the builder edit mode flag.  
          
                    There are two modes in the view alignment dialog, Create and Edit modes, and the flag determines the current mode. 
                    View alignment can be created in Create mode, and edited or deleted in Edit mode.   
         
        """
        pass
    @property
    def Placement(self) -> ViewPlacementBuilder:
        """
        Getter for property: ( ViewPlacementBuilder NXOpen.) Placement
         Returns the view placement component   
            
         
        """
        pass
    @property
    def SelectedAlignment(self) -> ViewAlignment:
        """
        Getter for property: ( ViewAlignment NXOpen.) SelectedAlignment
         Returns the selected alignment in builder.  
          
                    It needs to be set in edit mode as it specifies which alignment in the list
                    needs to be edited or deleted   
         
        """
        pass
    @SelectedAlignment.setter
    def SelectedAlignment(self, alignment: ViewAlignment):
        """
        Setter for property: ( ViewAlignment NXOpen.) SelectedAlignment
         Returns the selected alignment in builder.  
          
                    It needs to be set in edit mode as it specifies which alignment in the list
                    needs to be edited or deleted   
         
        """
        pass
    @property
    def View(self) -> SelectDraftingView:
        """
        Getter for property: ( SelectDraftingView NXOpen.) View
         Returns the select drafting view component   
            
         
        """
        pass
    def DeleteCurrentAlignment(self) -> None:
        """
         Deletes a view alignment that is stored as the current alignment in the builder 
        """
        pass
import NXOpen
class ViewAlignmentCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Drawings.ViewAlignments. """
    def CreateViewAlignmentBuilder(self) -> ViewAlignmentBuilder:
        """
         Creates a NXOpen.Drawings.ViewAlignmentBuilder 
         Returns builder ( ViewAlignmentBuilder NXOpen.): .
        """
        pass
    def FindObject(self, journal_identifier: str) -> ViewAlignment:
        """
         Finds the  NXOpen.Drawings.ViewAlignment  with the given identifier as recorded in a journal.
                An object may not return the same value as its JournalIdentifier in different versions of
                the software. However newer versions of the software should find the same object when
                FindObject is passed older versions of its journal identifier. In general, this method
                should not be used in handwritten code and exists to support record and playback of journals.
                An exception will be thrown if no object can be found with the given journal identifier. 
         Returns found ( ViewAlignment NXOpen.):  View alignment with this identifier .
        """
        pass
import NXOpen
class ViewAlignment(NXOpen.NXObject): 
    """  View Alignment object. This object represents an associative view alignment between two views. """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class ViewBoundaryBuilder(NXOpen.TaggedObject): 
    """ Represents the View Boundary (Drawings.ViewBoundaryBuilder)
    """
    class Type(Enum):
        """
        Members Include: 
         |Automatic|  automatic rectangle 
         |Manual|  top view 
         |BreakLine|  break line  detail 
         |Bound|  bound by objects 

        """
        Automatic: int
        Manual: int
        BreakLine: int
        Bound: int
        @staticmethod
        def ValueOf(value: int) -> ViewBoundaryBuilder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BoundaryPoint1(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) BoundaryPoint1
         Returns the first corner point   
            
         
        """
        pass
    @BoundaryPoint1.setter
    def BoundaryPoint1(self, boundaryPoint1: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) BoundaryPoint1
         Returns the first corner point   
            
         
        """
        pass
    @property
    def BoundaryPoint2(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) BoundaryPoint2
         Returns the second corner point   
            
         
        """
        pass
    @BoundaryPoint2.setter
    def BoundaryPoint2(self, boundaryPoint2: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) BoundaryPoint2
         Returns the second corner point   
            
         
        """
        pass
    @property
    def BoundaryType(self) -> ViewBoundaryBuilder.Type:
        """
        Getter for property: ( ViewBoundaryBuilder.Type NXOpen.) BoundaryType
         Returns the orientation type   
            
         
        """
        pass
    @BoundaryType.setter
    def BoundaryType(self, type: ViewBoundaryBuilder.Type):
        """
        Setter for property: ( ViewBoundaryBuilder.Type NXOpen.) BoundaryType
         Returns the orientation type   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ViewBreakBuilder(NXOpen.TaggedObject): 
    """ Represents a NXOpen.Drawings.ViewBreakBuilder """
    class Viewbreaklinestyle(Enum):
        """
        Members Include: 
         |Simple| 
         |Straight| 
         |Sawtooth| 
         |LongBreak| 
         |Tubular| 
         |SolidTubular| 
         |SolidRod| 
         |Jigsaw| 
         |Wood| 
         |CopyCurve| 
         |TemplateCurve| 

        """
        Simple: int
        Straight: int
        Sawtooth: int
        LongBreak: int
        Tubular: int
        SolidTubular: int
        SolidRod: int
        Jigsaw: int
        Wood: int
        CopyCurve: int
        TemplateCurve: int
        @staticmethod
        def ValueOf(value: int) -> ViewBreakBuilder.Viewbreaklinestyle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AddForeshorteningSymbol(self) -> bool:
        """
        Getter for property: (bool) AddForeshorteningSymbol
         Returns the foreshortening symbol addition   
            
         
        """
        pass
    @AddForeshorteningSymbol.setter
    def AddForeshorteningSymbol(self, propagateViewBreak: bool):
        """
        Setter for property: (bool) AddForeshorteningSymbol
         Returns the foreshortening symbol addition   
            
         
        """
        pass
    @property
    def BreakGap(self) -> float:
        """
        Getter for property: (float) BreakGap
         Returns the break gap   
            
         
        """
        pass
    @BreakGap.setter
    def BreakGap(self, breakGap: float):
        """
        Setter for property: (float) BreakGap
         Returns the break gap   
            
         
        """
        pass
    @property
    def BreakLineAmplitude(self) -> float:
        """
        Getter for property: (float) BreakLineAmplitude
         Returns the break line amplitude   
            
         
        """
        pass
    @BreakLineAmplitude.setter
    def BreakLineAmplitude(self, breakLineAmplitude: float):
        """
        Setter for property: (float) BreakLineAmplitude
         Returns the break line amplitude   
            
         
        """
        pass
    @property
    def BreakLineColorWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) BreakLineColorWidth
         Returns the break line color width   
            
         
        """
        pass
    @property
    def BreakLineExtension(self) -> float:
        """
        Getter for property: (float) BreakLineExtension
         Returns the break line extension   
            
         
        """
        pass
    @BreakLineExtension.setter
    def BreakLineExtension(self, breakLineExtension: float):
        """
        Setter for property: (float) BreakLineExtension
         Returns the break line extension   
            
         
        """
        pass
    @property
    def BreakLineStyle(self) -> ViewBreakBuilder.Viewbreaklinestyle:
        """
        Getter for property: ( ViewBreakBuilder.Viewbreaklinestyle NXOpen.) BreakLineStyle
         Returns the break line style   
            
         
        """
        pass
    @BreakLineStyle.setter
    def BreakLineStyle(self, breakLineStyle: ViewBreakBuilder.Viewbreaklinestyle):
        """
        Setter for property: ( ViewBreakBuilder.Viewbreaklinestyle NXOpen.) BreakLineStyle
         Returns the break line style   
            
         
        """
        pass
    @property
    def PropagateViewBreak(self) -> bool:
        """
        Getter for property: (bool) PropagateViewBreak
         Returns the propagate view break   
            
         
        """
        pass
    @PropagateViewBreak.setter
    def PropagateViewBreak(self, propagateViewBreak: bool):
        """
        Setter for property: (bool) PropagateViewBreak
         Returns the propagate view break   
            
         
        """
        pass
    @property
    def ShowBreakLines(self) -> bool:
        """
        Getter for property: (bool) ShowBreakLines
         Returns the show break lines   
            
         
        """
        pass
    @ShowBreakLines.setter
    def ShowBreakLines(self, showBreakLines: bool):
        """
        Setter for property: (bool) ShowBreakLines
         Returns the show break lines   
            
         
        """
        pass
import NXOpen
class ViewBreakCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Drawings.ViewBreaks. """
    def FindObject(self, journal_identifier: str) -> ViewBreak:
        """
         Finds the  NXOpen.Drawings.DraftingView  with the given identifier as recorded in a journal.
                An object may not return the same value as its JournalIdentifier in different versions of
                the software. However newer versions of the software should find the same object when
                FindObject is passed older versions of its journal identifier. In general, this method
                should not be used in handwritten code and exists to support record and playback of journals.
                An exception will be thrown if no object can be found with the given journal identifier. 
         Returns found ( ViewBreak NXOpen.):  View with this identifier .
        """
        pass
import NXOpen
class ViewBreak(NXOpen.NXObject): 
    """  ViewBreak - defines the portion of a view that gets hidden to
         produce a broken view """
    def GetViewBreakDisplayableObjectsAndOffsets(self) -> Tuple[List[NXOpen.Vector3d], List[NXOpen.DisplayableObject]]:
        """
         Returns an array of displayable object and theirs offsets representing the view break in the view.
         Returns A tuple consisting of (offsetPosition, display_objects). 
         - offsetPosition is:  NXOpen.Vector3d Li. .
         - display_objects is:  NXOpen.DisplayableObject Li. .

        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ViewCenterCoordinateBuilder(NXOpen.TaggedObject): 
    """ Represents the View center coodinate (Drawings.ViewCenterCoordinateBuilder)"""
    @property
    def XCoordinate(self) -> float:
        """
        Getter for property: (float) XCoordinate
         Returns the X center coordinate   
            
         
        """
        pass
    @XCoordinate.setter
    def XCoordinate(self, cenwcs: float):
        """
        Setter for property: (float) XCoordinate
         Returns the X center coordinate   
            
         
        """
        pass
    @property
    def XCoordinateExp(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) XCoordinateExp
         Returns the expression for the X coordinate   
            
         
        """
        pass
    @property
    def YCoordinate(self) -> float:
        """
        Getter for property: (float) YCoordinate
         Returns the Y center coordinate   
            
         
        """
        pass
    @YCoordinate.setter
    def YCoordinate(self, cenwcs: float):
        """
        Setter for property: (float) YCoordinate
         Returns the Y center coordinate   
            
         
        """
        pass
    @property
    def YCoordinateExp(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YCoordinateExp
         Returns the expression for the Y coordinate   
            
         
        """
        pass
    @property
    def ZCoordinate(self) -> float:
        """
        Getter for property: (float) ZCoordinate
         Returns the Z center coordinate   
            
         
        """
        pass
    @ZCoordinate.setter
    def ZCoordinate(self, cenwcs: float):
        """
        Setter for property: (float) ZCoordinate
         Returns the Z center coordinate   
            
         
        """
        pass
    @property
    def ZCoordinateExp(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ZCoordinateExp
         Returns the expression for the Z coordinate   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ViewCommonViewLabelBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.Drawings.ViewCommonViewLabelBuilder
    """
    class SecondaryAlignmentType(Enum):
        """
        Members Include: 
         |Inline| 
         |Subscript| 

        """
        Inline: int
        Subscript: int
        @staticmethod
        def ValueOf(value: int) -> ViewCommonViewLabelBuilder.SecondaryAlignmentType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SecondaryIndexingType(Enum):
        """
        Members Include: 
         |Alphabetic| 
         |Numeric| 

        """
        Alphabetic: int
        Numeric: int
        @staticmethod
        def ValueOf(value: int) -> ViewCommonViewLabelBuilder.SecondaryIndexingType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Letter(self) -> str:
        """
        Getter for property: (str) Letter
         Returns the letter   
            
         
        """
        pass
    @Letter.setter
    def Letter(self, letter: str):
        """
        Setter for property: (str) Letter
         Returns the letter   
            
         
        """
        pass
    @property
    def SecondaryAlignment(self) -> ViewCommonViewLabelBuilder.SecondaryAlignmentType:
        """
        Getter for property: ( ViewCommonViewLabelBuilder.SecondaryAlignmentType NXOpen.) SecondaryAlignment
         Returns the secondary alignment   
            
         
        """
        pass
    @SecondaryAlignment.setter
    def SecondaryAlignment(self, secondaryAlignment: ViewCommonViewLabelBuilder.SecondaryAlignmentType):
        """
        Setter for property: ( ViewCommonViewLabelBuilder.SecondaryAlignmentType NXOpen.) SecondaryAlignment
         Returns the secondary alignment   
            
         
        """
        pass
    @property
    def SecondaryIndexing(self) -> ViewCommonViewLabelBuilder.SecondaryIndexingType:
        """
        Getter for property: ( ViewCommonViewLabelBuilder.SecondaryIndexingType NXOpen.) SecondaryIndexing
         Returns the secondary indexing   
            
         
        """
        pass
    @SecondaryIndexing.setter
    def SecondaryIndexing(self, secondaryIndexing: ViewCommonViewLabelBuilder.SecondaryIndexingType):
        """
        Setter for property: ( ViewCommonViewLabelBuilder.SecondaryIndexingType NXOpen.) SecondaryIndexing
         Returns the secondary indexing   
            
         
        """
        pass
    @property
    def SubscriptSizeFactor(self) -> float:
        """
        Getter for property: (float) SubscriptSizeFactor
         Returns the subscript size factor   
            
         
        """
        pass
    @SubscriptSizeFactor.setter
    def SubscriptSizeFactor(self, subscriptSizeFactor: float):
        """
        Setter for property: (float) SubscriptSizeFactor
         Returns the subscript size factor   
            
         
        """
        pass
import NXOpen
class ViewCopyTo3dBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Drawings.ViewCopyTo3dBuilder.  This class
    is used to copy the contents of a drawing view to modeling space
    """
    class BoundingBoxOption(Enum):
        """
        Members Include: 
         |CurvesToCopy|  curves to copy 
         |EntireViews|  entire views 

        """
        CurvesToCopy: int
        EntireViews: int
        @staticmethod
        def ValueOf(value: int) -> ViewCopyTo3dBuilder.BoundingBoxOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DistanceFromViewPlaneOption(Enum):
        """
        Members Include: 
         |Automatic|  automatic distance calculation 
         |Specify|  specify distance 

        """
        Automatic: int
        Specify: int
        @staticmethod
        def ValueOf(value: int) -> ViewCopyTo3dBuilder.DistanceFromViewPlaneOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Option(Enum):
        """
        Members Include: 
         |Automatic|  automatic 
         |Specify|  specify 

        """
        Automatic: int
        Specify: int
        @staticmethod
        def ValueOf(value: int) -> ViewCopyTo3dBuilder.Option:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OutputOption(Enum):
        """
        Members Include: 
         |Sketches|  sketches 
         |SimpleCurves|  simple curves 
         |SketchesSolid|  sketches and solid body 
         |PartsGroup|  component parts from groups 

        """
        Sketches: int
        SimpleCurves: int
        SketchesSolid: int
        PartsGroup: int
        @staticmethod
        def ValueOf(value: int) -> ViewCopyTo3dBuilder.OutputOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |SelectedCurves|  selected curves 
         |SelectedViews|  selected views  

        """
        SelectedCurves: int
        SelectedViews: int
        @staticmethod
        def ValueOf(value: int) -> ViewCopyTo3dBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BoundingBox(self) -> ViewCopyTo3dBuilder.BoundingBoxOption:
        """
        Getter for property: ( ViewCopyTo3dBuilder.BoundingBoxOption NXOpen.) BoundingBox
         Returns the type of bounding box    
            
         
        """
        pass
    @BoundingBox.setter
    def BoundingBox(self, option: ViewCopyTo3dBuilder.BoundingBoxOption):
        """
        Setter for property: ( ViewCopyTo3dBuilder.BoundingBoxOption NXOpen.) BoundingBox
         Returns the type of bounding box    
            
         
        """
        pass
    @property
    def BoundingViews(self) -> SelectDrawingViewList:
        """
        Getter for property: ( SelectDrawingViewList NXOpen.) BoundingViews
         Returns the select views in the placement group   
            
         
        """
        pass
    @property
    def CreateSketches(self) -> bool:
        """
        Getter for property: (bool) CreateSketches
         Returns the flag indicating to create sketches in Modeling  
            
         
        """
        pass
    @CreateSketches.setter
    def CreateSketches(self, option: bool):
        """
        Setter for property: (bool) CreateSketches
         Returns the flag indicating to create sketches in Modeling  
            
         
        """
        pass
    @property
    def Curves(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Curves
         Returns the select curves for source group   
            
         
        """
        pass
    @property
    def DestinationPart(self) -> str:
        """
        Getter for property: (str) DestinationPart
         Returns the path to the destination part   
            
         
        """
        pass
    @DestinationPart.setter
    def DestinationPart(self, filename: str):
        """
        Setter for property: (str) DestinationPart
         Returns the path to the destination part   
            
         
        """
        pass
    @property
    def DistanceFromViewPlane(self) -> ViewCopyTo3dBuilder.DistanceFromViewPlaneOption:
        """
        Getter for property: ( ViewCopyTo3dBuilder.DistanceFromViewPlaneOption NXOpen.) DistanceFromViewPlane
         Returns the option specifying the distance from the view plane   
            
         
        """
        pass
    @DistanceFromViewPlane.setter
    def DistanceFromViewPlane(self, option: ViewCopyTo3dBuilder.DistanceFromViewPlaneOption):
        """
        Setter for property: ( ViewCopyTo3dBuilder.DistanceFromViewPlaneOption NXOpen.) DistanceFromViewPlane
         Returns the option specifying the distance from the view plane   
            
         
        """
        pass
    @property
    def ExtrudeSolidBody(self) -> bool:
        """
        Getter for property: (bool) ExtrudeSolidBody
         Returns the flag that indicates whether to extrude solid   
            
         
        """
        pass
    @ExtrudeSolidBody.setter
    def ExtrudeSolidBody(self, option: bool):
        """
        Setter for property: (bool) ExtrudeSolidBody
         Returns the flag that indicates whether to extrude solid   
            
         
        """
        pass
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Offset
         Returns the expression of clearance   
            
         
        """
        pass
    @property
    def Output(self) -> ViewCopyTo3dBuilder.OutputOption:
        """
        Getter for property: ( ViewCopyTo3dBuilder.OutputOption NXOpen.) Output
         Returns the option of output in the setting group    
            
         
        """
        pass
    @Output.setter
    def Output(self, option: ViewCopyTo3dBuilder.OutputOption):
        """
        Setter for property: ( ViewCopyTo3dBuilder.OutputOption NXOpen.) Output
         Returns the option of output in the setting group    
            
         
        """
        pass
    @property
    def ProcessSketchCurves(self) -> bool:
        """
        Getter for property: (bool) ProcessSketchCurves
         Returns the flag indicating to process sketch curves   
            
         
        """
        pass
    @ProcessSketchCurves.setter
    def ProcessSketchCurves(self, option: bool):
        """
        Setter for property: (bool) ProcessSketchCurves
         Returns the flag indicating to process sketch curves   
            
         
        """
        pass
    @property
    def ProcessViewCurves(self) -> bool:
        """
        Getter for property: (bool) ProcessViewCurves
         Returns the flag indicating to process view curves   
            
         
        """
        pass
    @ProcessViewCurves.setter
    def ProcessViewCurves(self, option: bool):
        """
        Setter for property: (bool) ProcessViewCurves
         Returns the flag indicating to process view curves   
            
         
        """
        pass
    @property
    def RepositionGeometry(self) -> bool:
        """
        Getter for property: (bool) RepositionGeometry
         Returns the flag that indicates whether to automatically reposition geometry   
            
         
        """
        pass
    @RepositionGeometry.setter
    def RepositionGeometry(self, option: bool):
        """
        Setter for property: (bool) RepositionGeometry
         Returns the flag that indicates whether to automatically reposition geometry   
            
         
        """
        pass
    @property
    def Type(self) -> ViewCopyTo3dBuilder.Types:
        """
        Getter for property: ( ViewCopyTo3dBuilder.Types NXOpen.) Type
         Returns the type of copy   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: ViewCopyTo3dBuilder.Types):
        """
        Setter for property: ( ViewCopyTo3dBuilder.Types NXOpen.) Type
         Returns the type of copy   
            
         
        """
        pass
    @property
    def View(self) -> SelectDrawingView:
        """
        Getter for property: ( SelectDrawingView NXOpen.) View
         Returns the selected view for previous single view selection    
            
         
        """
        pass
    @property
    def Views(self) -> SelectDrawingViewList:
        """
        Getter for property: ( SelectDrawingViewList NXOpen.) Views
         Returns the selected views for multiple views selection   
            
         
        """
        pass
    def Commit(self, offset: float, curves: bool, sketches: bool, option: int) -> None:
        """
         The copy of the selected view to modeling 
        """
        pass
import NXOpen
import NXOpen.Preferences
class ViewCreationWizardBuilder(NXOpen.Builder): 
    """ This builder allows the user to create a Drawing View """
    class Option(Enum):
        """
        Members Include: 
         |Automatic|  By Automatic 
         |Manual|  By Manual 

        """
        Automatic: int
        Manual: int
        @staticmethod
        def ValueOf(value: int) -> ViewCreationWizardBuilder.Option:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ResolutionOption(Enum):
        """
        Members Include: 
         |Coarse|  view display quality Coarse 
         |Medium|  view display quality Medium 
         |Fine|  view display quality Fine 

        """
        Coarse: int
        Medium: int
        Fine: int
        @staticmethod
        def ValueOf(value: int) -> ViewCreationWizardBuilder.ResolutionOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ViewBoundaryOption(Enum):
        """
        Members Include: 
         |Automatic|  view boundary Automatic 
         |Manual|  view boundary Manual 

        """
        Automatic: int
        Manual: int
        @staticmethod
        def ValueOf(value: int) -> ViewCreationWizardBuilder.ViewBoundaryOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ViewRepresentations(Enum):
        """
        Members Include: 
         |Exact|  View representation mode Exact 
         |SmartLightweight|  View representation mode Lightweight 
         |Lightweight|  View representation mode legacy Lightweight 
         |PreNx85Exact|  View representation mode legacy Exact 

        """
        Exact: int
        SmartLightweight: int
        Lightweight: int
        PreNx85Exact: int
        @staticmethod
        def ValueOf(value: int) -> ViewCreationWizardBuilder.ViewRepresentations:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AssociativeAlignment(self) -> bool:
        """
        Getter for property: (bool) AssociativeAlignment
         Returns the associative alignment toggle   
            
         
        """
        pass
    @AssociativeAlignment.setter
    def AssociativeAlignment(self, associative: bool):
        """
        Setter for property: (bool) AssociativeAlignment
         Returns the associative alignment toggle   
            
         
        """
        pass
    @property
    def AutoScale(self) -> bool:
        """
        Getter for property: (bool) AutoScale
         Returns the auto scale   
            
         
        """
        pass
    @AutoScale.setter
    def AutoScale(self, autoScale: bool):
        """
        Setter for property: (bool) AutoScale
         Returns the auto scale   
            
         
        """
        pass
    @property
    def BackView(self) -> bool:
        """
        Getter for property: (bool) BackView
         Returns the back view   
            
         
        """
        pass
    @BackView.setter
    def BackView(self, backView: bool):
        """
        Setter for property: (bool) BackView
         Returns the back view   
            
         
        """
        pass
    @property
    def BaseView(self) -> str:
        """
        Getter for property: (str) BaseView
         Returns the base view   
            
         
        """
        pass
    @BaseView.setter
    def BaseView(self, baseView: str):
        """
        Setter for property: (str) BaseView
         Returns the base view   
            
         
        """
        pass
    @property
    def BottomView(self) -> bool:
        """
        Getter for property: (bool) BottomView
         Returns the bottom view   
            
         
        """
        pass
    @BottomView.setter
    def BottomView(self, bottomView: bool):
        """
        Setter for property: (bool) BottomView
         Returns the bottom view   
            
         
        """
        pass
    @property
    def CenterLines(self) -> bool:
        """
        Getter for property: (bool) CenterLines
         Returns the center lines   
            
         
        """
        pass
    @CenterLines.setter
    def CenterLines(self, centerLines: bool):
        """
        Setter for property: (bool) CenterLines
         Returns the center lines   
            
         
        """
        pass
    @property
    def CrosshatchInheritedSectionViews(self) -> bool:
        """
        Getter for property: (bool) CrosshatchInheritedSectionViews
         Returns the crosshatch inherited section views   
            
         
        """
        pass
    @CrosshatchInheritedSectionViews.setter
    def CrosshatchInheritedSectionViews(self, crosshatchInheritedSectionViews: bool):
        """
        Setter for property: (bool) CrosshatchInheritedSectionViews
         Returns the crosshatch inherited section views   
            
         
        """
        pass
    @property
    def CustomViewSettingsBuilder(self) -> CustomViewSettingsBuilder:
        """
        Getter for property: ( CustomViewSettingsBuilder NXOpen.) CustomViewSettingsBuilder
         Returns the  NXOpen::Drawings::CustomViewSettingsBuilder  object   
            
         
        """
        pass
    @property
    def ExtractedEdges(self) -> bool:
        """
        Getter for property: (bool) ExtractedEdges
         Returns the extracted edges option   
            
         
        """
        pass
    @ExtractedEdges.setter
    def ExtractedEdges(self, extractedEdges: bool):
        """
        Setter for property: (bool) ExtractedEdges
         Returns the extracted edges option   
            
         
        """
        pass
    @property
    def FrontView(self) -> bool:
        """
        Getter for property: (bool) FrontView
         Returns the front view   
            
         
        """
        pass
    @FrontView.setter
    def FrontView(self, frontView: bool):
        """
        Setter for property: (bool) FrontView
         Returns the front view   
            
         
        """
        pass
    @property
    def HiddenLineColor(self) -> int:
        """
        Getter for property: (int) HiddenLineColor
         Returns the hidden line color   
            
         
        """
        pass
    @HiddenLineColor.setter
    def HiddenLineColor(self, hiddenLineColor: int):
        """
        Setter for property: (int) HiddenLineColor
         Returns the hidden line color   
            
         
        """
        pass
    @property
    def HiddenLineFont(self) -> int:
        """
        Getter for property: (int) HiddenLineFont
         Returns the hidden line font   
            
         
        """
        pass
    @HiddenLineFont.setter
    def HiddenLineFont(self, hiddenLineFont: int):
        """
        Setter for property: (int) HiddenLineFont
         Returns the hidden line font   
            
         
        """
        pass
    @property
    def HiddenLineWidth(self) -> int:
        """
        Getter for property: (int) HiddenLineWidth
         Returns the hidden line width   
            
         
        """
        pass
    @HiddenLineWidth.setter
    def HiddenLineWidth(self, hiddenLineWidth: int):
        """
        Setter for property: (int) HiddenLineWidth
         Returns the hidden line width   
            
         
        """
        pass
    @property
    def HiddenLines(self) -> bool:
        """
        Getter for property: (bool) HiddenLines
         Returns the hidden lines   
            
         
        """
        pass
    @HiddenLines.setter
    def HiddenLines(self, hiddenLines: bool):
        """
        Setter for property: (bool) HiddenLines
         Returns the hidden lines   
            
         
        """
        pass
    @property
    def IgnoreTitleBlock(self) -> bool:
        """
        Getter for property: (bool) IgnoreTitleBlock
         Returns the ignore title block   
            
         
        """
        pass
    @IgnoreTitleBlock.setter
    def IgnoreTitleBlock(self, ignoreTitleBlock: bool):
        """
        Setter for property: (bool) IgnoreTitleBlock
         Returns the ignore title block   
            
         
        """
        pass
    @property
    def InheritPMI(self) -> int:
        """
        Getter for property: (int) InheritPMI
         Returns the inherit pmi   
            
         
        """
        pass
    @InheritPMI.setter
    def InheritPMI(self, inheritPMI: int):
        """
        Setter for property: (int) InheritPMI
         Returns the inherit pmi   
            
         
        """
        pass
    @property
    def InheritPmiOntoDrawing(self) -> bool:
        """
        Getter for property: (bool) InheritPmiOntoDrawing
         Returns the inherit pmi onto drawing   
            
         
        """
        pass
    @InheritPmiOntoDrawing.setter
    def InheritPmiOntoDrawing(self, inheritPmiOntoDrawing: bool):
        """
        Setter for property: (bool) InheritPmiOntoDrawing
         Returns the inherit pmi onto drawing   
            
         
        """
        pass
    @property
    def IsometricView(self) -> bool:
        """
        Getter for property: (bool) IsometricView
         Returns the isometric view   
            
         
        """
        pass
    @IsometricView.setter
    def IsometricView(self, isometricView: bool):
        """
        Setter for property: (bool) IsometricView
         Returns the isometric view   
            
         
        """
        pass
    @property
    def LeftView(self) -> bool:
        """
        Getter for property: (bool) LeftView
         Returns the left view   
            
         
        """
        pass
    @LeftView.setter
    def LeftView(self, leftView: bool):
        """
        Setter for property: (bool) LeftView
         Returns the left view   
            
         
        """
        pass
    @property
    def LockMethod(self) -> NXOpen.Preferences.GeneralViewLockmethodOption:
        """
        Getter for property: ( NXOpen.Preferences.GeneralViewLockmethodOption) LockMethod
         Returns the lock method option   
            
         
        """
        pass
    @LockMethod.setter
    def LockMethod(self, lockMethod: NXOpen.Preferences.GeneralViewLockmethodOption):
        """
        Setter for property: ( NXOpen.Preferences.GeneralViewLockmethodOption) LockMethod
         Returns the lock method option   
            
         
        """
        pass
    @property
    def MarginBetweenViews(self) -> float:
        """
        Getter for property: (float) MarginBetweenViews
         Returns the margin between views   
            
         
        """
        pass
    @MarginBetweenViews.setter
    def MarginBetweenViews(self, marginBetweenViews: float):
        """
        Setter for property: (float) MarginBetweenViews
         Returns the margin between views   
            
         
        """
        pass
    @property
    def MarginToBorder(self) -> float:
        """
        Getter for property: (float) MarginToBorder
         Returns the margin to border   
            
         
        """
        pass
    @MarginToBorder.setter
    def MarginToBorder(self, marginToBorder: float):
        """
        Setter for property: (float) MarginToBorder
         Returns the margin to border   
            
         
        """
        pass
    @property
    def MultipleViewPlacement(self) -> MultipleViewPlacementBuilder:
        """
        Getter for property: ( MultipleViewPlacementBuilder NXOpen.) MultipleViewPlacement
         Returns the multiple view placement   
            
         
        """
        pass
    @property
    def OptimizeSettings(self) -> bool:
        """
        Getter for property: (bool) OptimizeSettings
         Returns the optimize view settings   
            
         
        """
        pass
    @OptimizeSettings.setter
    def OptimizeSettings(self, optimizeSettings: bool):
        """
        Setter for property: (bool) OptimizeSettings
         Returns the optimize view settings   
            
         
        """
        pass
    @property
    def OrientViewTool(self) -> OvtBuilder:
        """
        Getter for property: ( OvtBuilder NXOpen.) OrientViewTool
         Returns the orient view tool   
            
         
        """
        pass
    @property
    def Part(self) -> NXOpen.Part:
        """
        Getter for property: ( NXOpen.Part) Part
         Returns the part   
            
         
        """
        pass
    @Part.setter
    def Part(self, part: NXOpen.Part):
        """
        Setter for property: ( NXOpen.Part) Part
         Returns the part   
            
         
        """
        pass
    @property
    def PlacementOption(self) -> ViewCreationWizardBuilder.Option:
        """
        Getter for property: ( ViewCreationWizardBuilder.Option NXOpen.) PlacementOption
         Returns the placement option   
            
         
        """
        pass
    @PlacementOption.setter
    def PlacementOption(self, placementOption: ViewCreationWizardBuilder.Option):
        """
        Setter for property: ( ViewCreationWizardBuilder.Option NXOpen.) PlacementOption
         Returns the placement option   
            
         
        """
        pass
    @property
    def PmiDimensionFromRevolved(self) -> bool:
        """
        Getter for property: (bool) PmiDimensionFromRevolved
         Returns the inherit pmi from revolved sketches   
            
         
        """
        pass
    @PmiDimensionFromRevolved.setter
    def PmiDimensionFromRevolved(self, pmiDimensionFromRevolved: bool):
        """
        Setter for property: (bool) PmiDimensionFromRevolved
         Returns the inherit pmi from revolved sketches   
            
         
        """
        pass
    @property
    def PmiTypes(self) -> int:
        """
        Getter for property: (int) PmiTypes
         Returns the pmi types   
            
         
        """
        pass
    @PmiTypes.setter
    def PmiTypes(self, pmiTypes: int):
        """
        Setter for property: (int) PmiTypes
         Returns the pmi types   
            
         
        """
        pass
    @property
    def Resolution(self) -> ViewCreationWizardBuilder.ResolutionOption:
        """
        Getter for property: ( ViewCreationWizardBuilder.ResolutionOption NXOpen.) Resolution
         Returns the display quality option   
            
         
        """
        pass
    @Resolution.setter
    def Resolution(self, resolution: ViewCreationWizardBuilder.ResolutionOption):
        """
        Setter for property: ( ViewCreationWizardBuilder.ResolutionOption NXOpen.) Resolution
         Returns the display quality option   
            
         
        """
        pass
    @property
    def RightView(self) -> bool:
        """
        Getter for property: (bool) RightView
         Returns the right view   
            
         
        """
        pass
    @RightView.setter
    def RightView(self, rightView: bool):
        """
        Setter for property: (bool) RightView
         Returns the right view   
            
         
        """
        pass
    @property
    def Silhouettes(self) -> bool:
        """
        Getter for property: (bool) Silhouettes
         Returns the silhouettes   
            
         
        """
        pass
    @Silhouettes.setter
    def Silhouettes(self, silhouettes: bool):
        """
        Setter for property: (bool) Silhouettes
         Returns the silhouettes   
            
         
        """
        pass
    @property
    def SnapShot(self) -> bool:
        """
        Getter for property: (bool) SnapShot
         Returns the snapshot option   
            
         
        """
        pass
    @SnapShot.setter
    def SnapShot(self, snapShot: bool):
        """
        Setter for property: (bool) SnapShot
         Returns the snapshot option   
            
         
        """
        pass
    @property
    def SpecialBaseView(self) -> bool:
        """
        Getter for property: (bool) SpecialBaseView
         Returns the special base view   
            
         
        """
        pass
    @SpecialBaseView.setter
    def SpecialBaseView(self, specialBaseView: bool):
        """
        Setter for property: (bool) SpecialBaseView
         Returns the special base view   
            
         
        """
        pass
    @property
    def Tolerance(self) -> float:
        """
        Getter for property: (float) Tolerance
         Returns the tolerance option   
            
         
        """
        pass
    @Tolerance.setter
    def Tolerance(self, tolerance: float):
        """
        Setter for property: (float) Tolerance
         Returns the tolerance option   
            
         
        """
        pass
    @property
    def TopView(self) -> bool:
        """
        Getter for property: (bool) TopView
         Returns the top view   
            
         
        """
        pass
    @TopView.setter
    def TopView(self, topView: bool):
        """
        Setter for property: (bool) TopView
         Returns the top view   
            
         
        """
        pass
    @property
    def TrimetricView(self) -> bool:
        """
        Getter for property: (bool) TrimetricView
         Returns the trimetric view   
            
         
        """
        pass
    @TrimetricView.setter
    def TrimetricView(self, trimetricView: bool):
        """
        Setter for property: (bool) TrimetricView
         Returns the trimetric view   
            
         
        """
        pass
    @property
    def ViewBoundary(self) -> ViewCreationWizardBuilder.ViewBoundaryOption:
        """
        Getter for property: ( ViewCreationWizardBuilder.ViewBoundaryOption NXOpen.) ViewBoundary
         Returns the view boundary option   
            
         
        """
        pass
    @ViewBoundary.setter
    def ViewBoundary(self, viewBoundaryOption: ViewCreationWizardBuilder.ViewBoundaryOption):
        """
        Setter for property: ( ViewCreationWizardBuilder.ViewBoundaryOption NXOpen.) ViewBoundary
         Returns the view boundary option   
            
         
        """
        pass
    @property
    def ViewLabels(self) -> bool:
        """
        Getter for property: (bool) ViewLabels
         Returns the view labels   
            
         
        """
        pass
    @ViewLabels.setter
    def ViewLabels(self, dispViewLabels: bool):
        """
        Setter for property: (bool) ViewLabels
         Returns the view labels   
            
         
        """
        pass
    @property
    def ViewRepresentation(self) -> ViewCreationWizardBuilder.ViewRepresentations:
        """
        Getter for property: ( ViewCreationWizardBuilder.ViewRepresentations NXOpen.) ViewRepresentation
         Returns the view representation state   
            
         
        """
        pass
    @ViewRepresentation.setter
    def ViewRepresentation(self, viewRepresentation: ViewCreationWizardBuilder.ViewRepresentations):
        """
        Setter for property: ( ViewCreationWizardBuilder.ViewRepresentations NXOpen.) ViewRepresentation
         Returns the view representation state   
            
         
        """
        pass
    @property
    def ViewScale(self) -> ViewScaleBuilder:
        """
        Getter for property: ( ViewScaleBuilder NXOpen.) ViewScale
         Returns the view scale   
            
         
        """
        pass
    @property
    def ViewStyle(self) -> ViewStyleBuilder:
        """
        Getter for property: ( ViewStyleBuilder NXOpen.) ViewStyle
         Returns the view style   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ViewDetailLabelBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.Drawings.ViewDetailLabelBuilder
    """
    class LabelParentDisplayTypes(Enum):
        """
        Members Include: 
         |NotSet| 
         |Circle| 
         |Note| 
         |Label| 
         |Embedded| 
         |Boundary| 
         |LabelOnBoundary| 

        """
        NotSet: int
        Circle: int
        Note: int
        Label: int
        Embedded: int
        Boundary: int
        LabelOnBoundary: int
        @staticmethod
        def ValueOf(value: int) -> ViewDetailLabelBuilder.LabelParentDisplayTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LabelParentTextPlacement(Enum):
        """
        Members Include: 
         |BeforeOrAfterStub| 
         |AboveStub| 

        """
        BeforeOrAfterStub: int
        AboveStub: int
        @staticmethod
        def ValueOf(value: int) -> ViewDetailLabelBuilder.LabelParentTextPlacement:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CustomizedViewLabel(self) -> bool:
        """
        Getter for property: (bool) CustomizedViewLabel
         Returns the customized view label   
            
         
        """
        pass
    @CustomizedViewLabel.setter
    def CustomizedViewLabel(self, customizedViewLabel: bool):
        """
        Setter for property: (bool) CustomizedViewLabel
         Returns the customized view label   
            
         
        """
        pass
    @property
    def IncludeParentheses(self) -> bool:
        """
        Getter for property: (bool) IncludeParentheses
         Returns the include parentheses   
            
         
        """
        pass
    @IncludeParentheses.setter
    def IncludeParentheses(self, includeParentheses: bool):
        """
        Setter for property: (bool) IncludeParentheses
         Returns the include parentheses   
            
         
        """
        pass
    @property
    def LabelCharacterHeightFactor(self) -> float:
        """
        Getter for property: (float) LabelCharacterHeightFactor
         Returns the section vw label letter size factor   
            
         
        """
        pass
    @LabelCharacterHeightFactor.setter
    def LabelCharacterHeightFactor(self, labelCharacterHeightFactor: float):
        """
        Setter for property: (float) LabelCharacterHeightFactor
         Returns the section vw label letter size factor   
            
         
        """
        pass
    @property
    def LabelParentDisplay(self) -> ViewDetailLabelBuilder.LabelParentDisplayTypes:
        """
        Getter for property: ( ViewDetailLabelBuilder.LabelParentDisplayTypes NXOpen.) LabelParentDisplay
         Returns the label parent display   
            
         
        """
        pass
    @LabelParentDisplay.setter
    def LabelParentDisplay(self, labelParentDisplay: ViewDetailLabelBuilder.LabelParentDisplayTypes):
        """
        Setter for property: ( ViewDetailLabelBuilder.LabelParentDisplayTypes NXOpen.) LabelParentDisplay
         Returns the label parent display   
            
         
        """
        pass
    @property
    def LabelPosition(self) -> LabelPositionTypes:
        """
        Getter for property: ( LabelPositionTypes NXOpen.) LabelPosition
         Returns the label position   
            
         
        """
        pass
    @LabelPosition.setter
    def LabelPosition(self, labelPosition: LabelPositionTypes):
        """
        Setter for property: ( LabelPositionTypes NXOpen.) LabelPosition
         Returns the label position   
            
         
        """
        pass
    @property
    def LabelPrefix(self) -> str:
        """
        Getter for property: (str) LabelPrefix
         Returns the label prefix   
            
         
        """
        pass
    @LabelPrefix.setter
    def LabelPrefix(self, labelPrefix: str):
        """
        Setter for property: (str) LabelPrefix
         Returns the label prefix   
            
         
        """
        pass
    @property
    def LetterFormat(self) -> LetterFormatTypes:
        """
        Getter for property: ( LetterFormatTypes NXOpen.) LetterFormat
         Returns the letter format   
            
         
        """
        pass
    @LetterFormat.setter
    def LetterFormat(self, letterFormat: LetterFormatTypes):
        """
        Setter for property: ( LetterFormatTypes NXOpen.) LetterFormat
         Returns the letter format   
            
         
        """
        pass
    @property
    def ParentLabelPrefix(self) -> str:
        """
        Getter for property: (str) ParentLabelPrefix
         Returns the parent label prefix   
            
         
        """
        pass
    @ParentLabelPrefix.setter
    def ParentLabelPrefix(self, parentLabelPrefix: str):
        """
        Setter for property: (str) ParentLabelPrefix
         Returns the parent label prefix   
            
         
        """
        pass
    @property
    def PrefixCharacterHeightFactor(self) -> float:
        """
        Getter for property: (float) PrefixCharacterHeightFactor
         Returns the prefix character height factor   
            
         
        """
        pass
    @PrefixCharacterHeightFactor.setter
    def PrefixCharacterHeightFactor(self, prefixCharacterHeightFactor: float):
        """
        Setter for property: (float) PrefixCharacterHeightFactor
         Returns the prefix character height factor   
            
         
        """
        pass
    @property
    def ReferenceToShow(self) -> ReferenceShowTypes:
        """
        Getter for property: ( ReferenceShowTypes NXOpen.) ReferenceToShow
         Returns the reference to show   
            
         
        """
        pass
    @ReferenceToShow.setter
    def ReferenceToShow(self, referenceToShow: ReferenceShowTypes):
        """
        Setter for property: ( ReferenceShowTypes NXOpen.) ReferenceToShow
         Returns the reference to show   
            
         
        """
        pass
    @property
    def ScaleCharacterHeightFactor(self) -> float:
        """
        Getter for property: (float) ScaleCharacterHeightFactor
         Returns the scale character height factor   
            
         
        """
        pass
    @ScaleCharacterHeightFactor.setter
    def ScaleCharacterHeightFactor(self, scaleCharacterHeightFactor: float):
        """
        Setter for property: (float) ScaleCharacterHeightFactor
         Returns the scale character height factor   
            
         
        """
        pass
    @property
    def ScalePosition(self) -> ScalePositionTypes:
        """
        Getter for property: ( ScalePositionTypes NXOpen.) ScalePosition
         Returns the scale position   
            
         
        """
        pass
    @ScalePosition.setter
    def ScalePosition(self, scalePosition: ScalePositionTypes):
        """
        Setter for property: ( ScalePositionTypes NXOpen.) ScalePosition
         Returns the scale position   
            
         
        """
        pass
    @property
    def ScalePrefix(self) -> str:
        """
        Getter for property: (str) ScalePrefix
         Returns the scale prefix   
            
         
        """
        pass
    @ScalePrefix.setter
    def ScalePrefix(self, scalePrefix: str):
        """
        Setter for property: (str) ScalePrefix
         Returns the scale prefix   
            
         
        """
        pass
    @property
    def ShowViewLabel(self) -> bool:
        """
        Getter for property: (bool) ShowViewLabel
         Returns the show view label   
            
         
        """
        pass
    @ShowViewLabel.setter
    def ShowViewLabel(self, showViewLabel: bool):
        """
        Setter for property: (bool) ShowViewLabel
         Returns the show view label   
            
         
        """
        pass
    @property
    def ShowViewScale(self) -> bool:
        """
        Getter for property: (bool) ShowViewScale
         Returns the show view scale   
            
         
        """
        pass
    @ShowViewScale.setter
    def ShowViewScale(self, showViewScale: bool):
        """
        Setter for property: (bool) ShowViewScale
         Returns the show view scale   
            
         
        """
        pass
    @property
    def TextGapFactor(self) -> float:
        """
        Getter for property: (float) TextGapFactor
         Returns the text gap factor   
            
         
        """
        pass
    @TextGapFactor.setter
    def TextGapFactor(self, textGapFactor: float):
        """
        Setter for property: (float) TextGapFactor
         Returns the text gap factor   
            
         
        """
        pass
    @property
    def TextPlacement(self) -> ViewDetailLabelBuilder.LabelParentTextPlacement:
        """
        Getter for property: ( ViewDetailLabelBuilder.LabelParentTextPlacement NXOpen.) TextPlacement
         Returns the text placement   
            
         
        """
        pass
    @TextPlacement.setter
    def TextPlacement(self, textPlacement: ViewDetailLabelBuilder.LabelParentTextPlacement):
        """
        Setter for property: ( ViewDetailLabelBuilder.LabelParentTextPlacement NXOpen.) TextPlacement
         Returns the text placement   
            
         
        """
        pass
    @property
    def ValueFormat(self) -> ScaleValueFormatTypes:
        """
        Getter for property: ( ScaleValueFormatTypes NXOpen.) ValueFormat
         Returns the value format   
            
         
        """
        pass
    @ValueFormat.setter
    def ValueFormat(self, valueFormat: ScaleValueFormatTypes):
        """
        Setter for property: ( ScaleValueFormatTypes NXOpen.) ValueFormat
         Returns the value format   
            
         
        """
        pass
    @property
    def ViewLabelOption(self) -> ViewLabelTypes:
        """
        Getter for property: ( ViewLabelTypes NXOpen.) ViewLabelOption
         Returns the view label option   
            
         
        """
        pass
    @ViewLabelOption.setter
    def ViewLabelOption(self, viewLabelOption: ViewLabelTypes):
        """
        Setter for property: ( ViewLabelTypes NXOpen.) ViewLabelOption
         Returns the view label option   
            
         
        """
        pass
    def GetCustomizedViewLabelText(self) -> List[str]:
        """
         Returns the customized view label text 
         Returns customizedText (List[str]):  .
        """
        pass
    def SetCustomizedViewLabelText(self, customizedText: List[str]) -> None:
        """
         Sets the customized view label text 
        """
        pass
import NXOpen.Annotations
class ViewingDirectionArrowLabel(NXOpen.Annotations.Note): 
    """ This class represents a Drafting Viewing Direction Arrow Label.
    Object of this class will be created when projected view is created and cannot be independently """
    pass
import NXOpen.Annotations
class ViewingDirectionArrow(NXOpen.Annotations.BaseArrow): 
    """ This class represents a Drafting Viewing Direction Arrow.
    Object of this class will be created when projected view is created and cannot be independently """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class ViewLabelBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.Drawings.ViewLabelBuilder
    """
    @property
    def CustomizedViewLabel(self) -> bool:
        """
        Getter for property: (bool) CustomizedViewLabel
         Returns the customized view label   
            
         
        """
        pass
    @CustomizedViewLabel.setter
    def CustomizedViewLabel(self, customizedViewLabel: bool):
        """
        Setter for property: (bool) CustomizedViewLabel
         Returns the customized view label   
            
         
        """
        pass
    @property
    def IncludeParentheses(self) -> bool:
        """
        Getter for property: (bool) IncludeParentheses
         Returns the include parentheses   
            
         
        """
        pass
    @IncludeParentheses.setter
    def IncludeParentheses(self, includeParentheses: bool):
        """
        Setter for property: (bool) IncludeParentheses
         Returns the include parentheses   
            
         
        """
        pass
    @property
    def IncludeRotationAngle(self) -> bool:
        """
        Getter for property: (bool) IncludeRotationAngle
         Returns the include rotation angle   
            
         
        """
        pass
    @IncludeRotationAngle.setter
    def IncludeRotationAngle(self, includeRotationAngle: bool):
        """
        Setter for property: (bool) IncludeRotationAngle
         Returns the include rotation angle   
            
         
        """
        pass
    @property
    def IncludeRotationSymbol(self) -> bool:
        """
        Getter for property: (bool) IncludeRotationSymbol
         Returns the include rotation symbol   
            
         
        """
        pass
    @IncludeRotationSymbol.setter
    def IncludeRotationSymbol(self, includeRotationSymbol: bool):
        """
        Setter for property: (bool) IncludeRotationSymbol
         Returns the include rotation symbol   
            
         
        """
        pass
    @property
    def LabelCharacterHeightFactor(self) -> float:
        """
        Getter for property: (float) LabelCharacterHeightFactor
         Returns the label character height factor   
            
         
        """
        pass
    @LabelCharacterHeightFactor.setter
    def LabelCharacterHeightFactor(self, labelCharacterHeightFactor: float):
        """
        Setter for property: (float) LabelCharacterHeightFactor
         Returns the label character height factor   
            
         
        """
        pass
    @property
    def LabelPosition(self) -> LabelPositionTypes:
        """
        Getter for property: ( LabelPositionTypes NXOpen.) LabelPosition
         Returns the label position   
            
         
        """
        pass
    @LabelPosition.setter
    def LabelPosition(self, labelPosition: LabelPositionTypes):
        """
        Setter for property: ( LabelPositionTypes NXOpen.) LabelPosition
         Returns the label position   
            
         
        """
        pass
    @property
    def LabelPrefix(self) -> str:
        """
        Getter for property: (str) LabelPrefix
         Returns the label prefix   
            
         
        """
        pass
    @LabelPrefix.setter
    def LabelPrefix(self, labelPrefix: str):
        """
        Setter for property: (str) LabelPrefix
         Returns the label prefix   
            
         
        """
        pass
    @property
    def LetterFormat(self) -> LetterFormatTypes:
        """
        Getter for property: ( LetterFormatTypes NXOpen.) LetterFormat
         Returns the letter format   
            
         
        """
        pass
    @LetterFormat.setter
    def LetterFormat(self, letterFormat: LetterFormatTypes):
        """
        Setter for property: ( LetterFormatTypes NXOpen.) LetterFormat
         Returns the letter format   
            
         
        """
        pass
    @property
    def PrefixCharacterHeightFactor(self) -> float:
        """
        Getter for property: (float) PrefixCharacterHeightFactor
         Returns the prefix character height factor   
            
         
        """
        pass
    @PrefixCharacterHeightFactor.setter
    def PrefixCharacterHeightFactor(self, prefixCharacterHeightFactor: float):
        """
        Setter for property: (float) PrefixCharacterHeightFactor
         Returns the prefix character height factor   
            
         
        """
        pass
    @property
    def ReferenceToShow(self) -> ReferenceShowTypes:
        """
        Getter for property: ( ReferenceShowTypes NXOpen.) ReferenceToShow
         Returns the reference to show   
            
         
        """
        pass
    @ReferenceToShow.setter
    def ReferenceToShow(self, referenceToShow: ReferenceShowTypes):
        """
        Setter for property: ( ReferenceShowTypes NXOpen.) ReferenceToShow
         Returns the reference to show   
            
         
        """
        pass
    @property
    def RotationSymbolType(self) -> RotationSymbolTypes:
        """
        Getter for property: ( RotationSymbolTypes NXOpen.) RotationSymbolType
         Returns the rotation symbol type  
            
         
        """
        pass
    @RotationSymbolType.setter
    def RotationSymbolType(self, rotationSymbolType: RotationSymbolTypes):
        """
        Setter for property: ( RotationSymbolTypes NXOpen.) RotationSymbolType
         Returns the rotation symbol type  
            
         
        """
        pass
    @property
    def ScaleCharacterHeightFactor(self) -> float:
        """
        Getter for property: (float) ScaleCharacterHeightFactor
         Returns the scale character height factor   
            
         
        """
        pass
    @ScaleCharacterHeightFactor.setter
    def ScaleCharacterHeightFactor(self, scaleCharacterHeightFactor: float):
        """
        Setter for property: (float) ScaleCharacterHeightFactor
         Returns the scale character height factor   
            
         
        """
        pass
    @property
    def ScalePosition(self) -> ScalePositionTypes:
        """
        Getter for property: ( ScalePositionTypes NXOpen.) ScalePosition
         Returns the scale position   
            
         
        """
        pass
    @ScalePosition.setter
    def ScalePosition(self, scalePosition: ScalePositionTypes):
        """
        Setter for property: ( ScalePositionTypes NXOpen.) ScalePosition
         Returns the scale position   
            
         
        """
        pass
    @property
    def ScalePrefix(self) -> str:
        """
        Getter for property: (str) ScalePrefix
         Returns the scale prefix   
            
         
        """
        pass
    @ScalePrefix.setter
    def ScalePrefix(self, scalePrefix: str):
        """
        Setter for property: (str) ScalePrefix
         Returns the scale prefix   
            
         
        """
        pass
    @property
    def ShowViewLabel(self) -> bool:
        """
        Getter for property: (bool) ShowViewLabel
         Returns the show view label   
            
         
        """
        pass
    @ShowViewLabel.setter
    def ShowViewLabel(self, showViewLabel: bool):
        """
        Setter for property: (bool) ShowViewLabel
         Returns the show view label   
            
         
        """
        pass
    @property
    def ShowViewScale(self) -> bool:
        """
        Getter for property: (bool) ShowViewScale
         Returns the show view scale   
            
         
        """
        pass
    @ShowViewScale.setter
    def ShowViewScale(self, showViewScale: bool):
        """
        Setter for property: (bool) ShowViewScale
         Returns the show view scale   
            
         
        """
        pass
    @property
    def ValueFormat(self) -> ScaleValueFormatTypes:
        """
        Getter for property: ( ScaleValueFormatTypes NXOpen.) ValueFormat
         Returns the value format   
            
         
        """
        pass
    @ValueFormat.setter
    def ValueFormat(self, valueFormat: ScaleValueFormatTypes):
        """
        Setter for property: ( ScaleValueFormatTypes NXOpen.) ValueFormat
         Returns the value format   
            
         
        """
        pass
    @property
    def ViewLabelOption(self) -> ViewLabelTypes:
        """
        Getter for property: ( ViewLabelTypes NXOpen.) ViewLabelOption
         Returns the view label option   
            
         
        """
        pass
    @ViewLabelOption.setter
    def ViewLabelOption(self, viewLabelOption: ViewLabelTypes):
        """
        Setter for property: ( ViewLabelTypes NXOpen.) ViewLabelOption
         Returns the view label option   
            
         
        """
        pass
    def GetCustomizedViewLabelText(self) -> List[str]:
        """
         Returns the customized view label text 
         Returns customizedText (List[str]): .
        """
        pass
    def SetCustomizedViewLabelText(self, customizedText: List[str]) -> None:
        """
         Sets the customized view label text 
        """
        pass
class ViewLabelTypes(Enum):
    """
    Members Include: 
     |Name| 
     |Letter| 

    """
    Name: int
    Letter: int
    @staticmethod
    def ValueOf(value: int) -> ViewLabelTypes:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ViewOrientationBuilder(NXOpen.TaggedObject): 
    """
    Represents a ViewOrientationBuilder.
    The View Orientation Block is used to specify orientation of the view, and 
    the view being inherited or sectioned, if needed.
    """
    class Orientation(Enum):
        """
        Members Include: 
         |Orthographic|  Orthographic 
         |InheritOrientation|  Inherit Orientation from a View 
         |UseParentOrientation|  Use Parent View Orientation 
         |UseParentOrienation|  DO NOT USE Deprecated as of NX75 
         |SectionExisting|  Section an Existing View 

        """
        Orthographic: int
        InheritOrientation: int
        UseParentOrientation: int
        UseParentOrienation: int
        SectionExisting: int
        @staticmethod
        def ValueOf(value: int) -> ViewOrientationBuilder.Orientation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def OrientationType(self) -> ViewOrientationBuilder.Orientation:
        """
        Getter for property: ( ViewOrientationBuilder.Orientation NXOpen.) OrientationType
         Returns the orientation type   
            
         
        """
        pass
    @OrientationType.setter
    def OrientationType(self, orientationType: ViewOrientationBuilder.Orientation):
        """
        Setter for property: ( ViewOrientationBuilder.Orientation NXOpen.) OrientationType
         Returns the orientation type   
            
         
        """
        pass
    @property
    def SelectView(self) -> NXOpen.SelectView:
        """
        Getter for property: ( NXOpen.SelectView) SelectView
         Returns the select view   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ViewPlacementBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.Drawings.ViewPlacementBuilder.  This class
    is used to define the origin of a view.
    """
    class Method(Enum):
        """
        Members Include: 
         |Infer|  Infer the view position 
         |Horizontal|  Align the view horizontally to another view 
         |Vertical|  Align the view vertically to another view 
         |PerpendicularToLine|  Align the view along some line to another view 
         |Overlay|  Align the view on top of another view 
         |PerpendicularToHingeLine|  Align the view along the hinge line 
         |Max|  Should be the last enum in the list 

        """
        Infer: int
        Horizontal: int
        Vertical: int
        PerpendicularToLine: int
        Overlay: int
        PerpendicularToHingeLine: int
        Max: int
        @staticmethod
        def ValueOf(value: int) -> ViewPlacementBuilder.Method:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Option(Enum):
        """
        Members Include: 
         |ToView|  Align to the view centers 
         |ModelPoint|  Align to the same point in the alignment view and the view being edited 
         |PointToPoint|  Align a point in the alignment view to another point in the view being edited 

        """
        ToView: int
        ModelPoint: int
        PointToPoint: int
        @staticmethod
        def ValueOf(value: int) -> ViewPlacementBuilder.Option:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AlignmentMethod(self) -> ViewPlacementBuilder.Method:
        """
        Getter for property: ( ViewPlacementBuilder.Method NXOpen.) AlignmentMethod
         Returns the alignment method   
            
         
        """
        pass
    @AlignmentMethod.setter
    def AlignmentMethod(self, alignmentMethod: ViewPlacementBuilder.Method):
        """
        Setter for property: ( ViewPlacementBuilder.Method NXOpen.) AlignmentMethod
         Returns the alignment method   
            
         
        """
        pass
    @property
    def AlignmentOption(self) -> ViewPlacementBuilder.Option:
        """
        Getter for property: ( ViewPlacementBuilder.Option NXOpen.) AlignmentOption
         Returns the alignment option used to indicate what points in the views to align.  
          
                    The alignment option is not used when the alignment method is set
                    to  NXOpen::Drawings::ViewPlacementBuilder::MethodInfer .   
         
        """
        pass
    @AlignmentOption.setter
    def AlignmentOption(self, alignmentOption: ViewPlacementBuilder.Option):
        """
        Setter for property: ( ViewPlacementBuilder.Option NXOpen.) AlignmentOption
         Returns the alignment option used to indicate what points in the views to align.  
          
                    The alignment option is not used when the alignment method is set
                    to  NXOpen::Drawings::ViewPlacementBuilder::MethodInfer .   
         
        """
        pass
    @property
    def AlignmentPoint(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: ( NXOpen.SelectTaggedObject) AlignmentPoint
         Returns the point to align to.  
            This point is only required for the
                     NXOpen::Drawings::ViewPlacementBuilder::OptionModelPoint  and
                     NXOpen::Drawings::ViewPlacementBuilder::OptionPointToPoint  alignment options.
                    The point is required for all alignment methods except for
                     NXOpen::Drawings::ViewPlacementBuilder::MethodInfer .
                    This point may be specified by either selecting an object of
                     NXOpen::Point  class or not selecting an object and specifying
                    a  NXOpen::Point3d  selected object point.     
         
        """
        pass
    @property
    def AlignmentVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) AlignmentVector
         Returns the vector to align along.  
            The vector is only required for the
                     NXOpen::Drawings::ViewPlacementBuilder::MethodPerpendicularToLine  alignment
                    method.  The vector must be set regardless of the alignment option.   
         
        """
        pass
    @AlignmentVector.setter
    def AlignmentVector(self, alignmentVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) AlignmentVector
         Returns the vector to align along.  
            The vector is only required for the
                     NXOpen::Drawings::ViewPlacementBuilder::MethodPerpendicularToLine  alignment
                    method.  The vector must be set regardless of the alignment option.   
         
        """
        pass
    @property
    def AlignmentView(self) -> SelectDraftingView:
        """
        Getter for property: ( SelectDraftingView NXOpen.) AlignmentView
         Returns the view to align to.  
            The view is required for all alignment
                    options.  The view is required for all alignment methods except for
                     NXOpen::Drawings::ViewPlacementBuilder::MethodInfer .   
         
        """
        pass
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns the flag used to create a persistent alignment   
            
         
        """
        pass
    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
         Returns the flag used to create a persistent alignment   
            
         
        """
        pass
    @property
    def CandidatePoint(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: ( NXOpen.SelectTaggedObject) CandidatePoint
         Returns the point to align in the view being edited.  
            This point is only
                    required for the  NXOpen::Drawings::ViewPlacementBuilder::OptionPointToPoint 
                    alignment option.  The point is required for all alignment methods
                    except  NXOpen::Drawings::ViewPlacementBuilder::MethodInfer .
                    This point may be specified by either selecting an object of
                     NXOpen::Point  class or not selecting an object and specifying
                    a  NXOpen::Point3d  selected object point.   
         
        """
        pass
    @property
    def LockOffset(self) -> bool:
        """
        Getter for property: (bool) LockOffset
         Returns the lock offset flag.  
            Use the offset property if this flag is set
                    to true.   
         
        """
        pass
    @LockOffset.setter
    def LockOffset(self, lockOffset: bool):
        """
        Setter for property: (bool) LockOffset
         Returns the lock offset flag.  
            Use the offset property if this flag is set
                    to true.   
         
        """
        pass
    @property
    def Offset(self) -> float:
        """
        Getter for property: (float) Offset
         Returns the offset.  
            If the lock offset flag is set to true then the offset
                    will be applied.  The offset has no meaning when used with the
                     NXOpen::Drawings::ViewPlacementBuilder::MethodOverlay .  If the
                     NXOpen::Drawings::ViewPlacementBuilder::MethodInfer  method is set, then the offset
                    is defined as the distance from the view to its parent view.
                    For all other methods, the offset is defined as the distance along
                    the line being aligned to.   
         
        """
        pass
    @Offset.setter
    def Offset(self, offset: float):
        """
        Setter for property: (float) Offset
         Returns the offset.  
            If the lock offset flag is set to true then the offset
                    will be applied.  The offset has no meaning when used with the
                     NXOpen::Drawings::ViewPlacementBuilder::MethodOverlay .  If the
                     NXOpen::Drawings::ViewPlacementBuilder::MethodInfer  method is set, then the offset
                    is defined as the distance from the view to its parent view.
                    For all other methods, the offset is defined as the distance along
                    the line being aligned to.   
         
        """
        pass
    @property
    def Placement(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) Placement
         Returns the placement location.  
            The location may be specified by either
                    selecting an object of  NXOpen::Point  class or not
                    selecting an object and specifying a  NXOpen::Point3d 
                    selected object point.  If the alignment method is set to
                     NXOpen::Drawings::ViewPlacementBuilder::MethodInfer 
                    then the location defines the position of the view's center.
                    The location is not necessarily the position of the view.
                    The location provides a hint point that helps determine the view's
                    position based on the alignment method and alignment point specified.   
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ViewProjectedArrowSettingsBuilder(NXOpen.TaggedObject): 
    """ Represents a NXOpen.Drawings.ViewProjectedArrowSettingsBuilder """
    class DimensionsStyleType(Enum):
        """
        Members Include: 
         |Filled| 
         |Closed| 
         |Open| 

        """
        Filled: int
        Closed: int
        Open: int
        @staticmethod
        def ValueOf(value: int) -> ViewProjectedArrowSettingsBuilder.DimensionsStyleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DispalyLabelType(Enum):
        """
        Members Include: 
         |No| 
         |OnReferenceArrow| 
         |OnReferenceArrowAndView| 

        """
        No: int
        OnReferenceArrow: int
        OnReferenceArrowAndView: int
        @staticmethod
        def ValueOf(value: int) -> ViewProjectedArrowSettingsBuilder.DispalyLabelType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ArrowHeadAngle(self) -> float:
        """
        Getter for property: (float) ArrowHeadAngle
         Returns the arrow head angle   
            
         
        """
        pass
    @ArrowHeadAngle.setter
    def ArrowHeadAngle(self, arrowHeadAngle: float):
        """
        Setter for property: (float) ArrowHeadAngle
         Returns the arrow head angle   
            
         
        """
        pass
    @property
    def ArrowHeadLength(self) -> float:
        """
        Getter for property: (float) ArrowHeadLength
         Returns the arrow head length   
            
         
        """
        pass
    @ArrowHeadLength.setter
    def ArrowHeadLength(self, arrowHeadLength: float):
        """
        Setter for property: (float) ArrowHeadLength
         Returns the arrow head length   
            
         
        """
        pass
    @property
    def ArrowHeadStyle(self) -> ViewProjectedArrowSettingsBuilder.DimensionsStyleType:
        """
        Getter for property: ( ViewProjectedArrowSettingsBuilder.DimensionsStyleType NXOpen.) ArrowHeadStyle
         Returns the arrow head style   
            
         
        """
        pass
    @ArrowHeadStyle.setter
    def ArrowHeadStyle(self, arrowHeadStyle: ViewProjectedArrowSettingsBuilder.DimensionsStyleType):
        """
        Setter for property: ( ViewProjectedArrowSettingsBuilder.DimensionsStyleType NXOpen.) ArrowHeadStyle
         Returns the arrow head style   
            
         
        """
        pass
    @property
    def ArrowLineDistanceToGeometry(self) -> float:
        """
        Getter for property: (float) ArrowLineDistanceToGeometry
         Returns the arrow line distance to geometry   
            
         
        """
        pass
    @ArrowLineDistanceToGeometry.setter
    def ArrowLineDistanceToGeometry(self, arrowLineDistanceToGeometry: float):
        """
        Setter for property: (float) ArrowLineDistanceToGeometry
         Returns the arrow line distance to geometry   
            
         
        """
        pass
    @property
    def ArrowLineLength(self) -> float:
        """
        Getter for property: (float) ArrowLineLength
         Returns the arrow line length   
            
         
        """
        pass
    @ArrowLineLength.setter
    def ArrowLineLength(self, arrowLineLength: float):
        """
        Setter for property: (float) ArrowLineLength
         Returns the arrow line length   
            
         
        """
        pass
    @property
    def DisplayLabel(self) -> ViewProjectedArrowSettingsBuilder.DispalyLabelType:
        """
        Getter for property: ( ViewProjectedArrowSettingsBuilder.DispalyLabelType NXOpen.) DisplayLabel
         Returns the display label   
            
         
        """
        pass
    @DisplayLabel.setter
    def DisplayLabel(self, displayLabel: ViewProjectedArrowSettingsBuilder.DispalyLabelType):
        """
        Setter for property: ( ViewProjectedArrowSettingsBuilder.DispalyLabelType NXOpen.) DisplayLabel
         Returns the display label   
            
         
        """
        pass
    @property
    def LineColorFontWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) LineColorFontWidth
         Returns the line color font width0   
            
         
        """
        pass
    @property
    def SizeFactor(self) -> float:
        """
        Getter for property: (float) SizeFactor
         Returns the size factor   
            
         
        """
        pass
    @SizeFactor.setter
    def SizeFactor(self, sizeFactor: float):
        """
        Setter for property: (float) SizeFactor
         Returns the size factor   
            
         
        """
        pass
class ViewProjectedLabelBuilder(ViewLabelBuilder): 
    """
    Represents a NXOpen.Drawings.ViewProjectedLabelBuilder
    """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class ViewProjectedViewSettingsBuilder(NXOpen.TaggedObject): 
    """ Represents a NXOpen.Drawings.ViewProjectedViewSettingsBuilder """
    class DisplayArrowOnParentViewType(Enum):
        """
        Members Include: 
         |No| 
         |NonOrtho| 
         |All| 

        """
        No: int
        NonOrtho: int
        All: int
        @staticmethod
        def ValueOf(value: int) -> ViewProjectedViewSettingsBuilder.DisplayArrowOnParentViewType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DisplayArrowOnParentView(self) -> ViewProjectedViewSettingsBuilder.DisplayArrowOnParentViewType:
        """
        Getter for property: ( ViewProjectedViewSettingsBuilder.DisplayArrowOnParentViewType NXOpen.) DisplayArrowOnParentView
         Returns the display arrow on parent view   
            
         
        """
        pass
    @DisplayArrowOnParentView.setter
    def DisplayArrowOnParentView(self, displayArrowOnParentView: ViewProjectedViewSettingsBuilder.DisplayArrowOnParentViewType):
        """
        Setter for property: ( ViewProjectedViewSettingsBuilder.DisplayArrowOnParentViewType NXOpen.) DisplayArrowOnParentView
         Returns the display arrow on parent view   
            
         
        """
        pass
import NXOpen
class ViewProjectionBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Drawings.ViewProjectionBuilder.  This class
    is used to project the contents of a drafting member view to other views
    """
    class CurveType(Enum):
        """
        Members Include: 
         |Active|  Active 
         |Reference|  Reference 
         |NotSet|  None 

        """
        Active: int
        Reference: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> ViewProjectionBuilder.CurveType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |ProjectOnOnePlane|  on one plane 
         |ProjectOnTwoPlanes|  on two planes 

        """
        ProjectOnOnePlane: int
        ProjectOnTwoPlanes: int
        @staticmethod
        def ValueOf(value: int) -> ViewProjectionBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CurvePoints(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) CurvePoints
         Returns the curve and points   
            
         
        """
        pass
    @property
    def CurveTypeEdges(self) -> ViewProjectionBuilder.CurveType:
        """
        Getter for property: ( ViewProjectionBuilder.CurveType NXOpen.) CurveTypeEdges
         Returns the curve type edges in the setting group   
            
         
        """
        pass
    @CurveTypeEdges.setter
    def CurveTypeEdges(self, type: ViewProjectionBuilder.CurveType):
        """
        Setter for property: ( ViewProjectionBuilder.CurveType NXOpen.) CurveTypeEdges
         Returns the curve type edges in the setting group   
            
         
        """
        pass
    @property
    def CurveTypePlane1(self) -> ViewProjectionBuilder.CurveType:
        """
        Getter for property: ( ViewProjectionBuilder.CurveType NXOpen.) CurveTypePlane1
         Returns the curve type plane 1 in the setting group   
            
         
        """
        pass
    @CurveTypePlane1.setter
    def CurveTypePlane1(self, type: ViewProjectionBuilder.CurveType):
        """
        Setter for property: ( ViewProjectionBuilder.CurveType NXOpen.) CurveTypePlane1
         Returns the curve type plane 1 in the setting group   
            
         
        """
        pass
    @property
    def CurveTypePlane2(self) -> ViewProjectionBuilder.CurveType:
        """
        Getter for property: ( ViewProjectionBuilder.CurveType NXOpen.) CurveTypePlane2
         Returns the curve type plane 2 in the setting group , if the type is set to
                    one plane, the second plane information is ignored 
                  
            
         
        """
        pass
    @CurveTypePlane2.setter
    def CurveTypePlane2(self, type: ViewProjectionBuilder.CurveType):
        """
        Setter for property: ( ViewProjectionBuilder.CurveType NXOpen.) CurveTypePlane2
         Returns the curve type plane 2 in the setting group , if the type is set to
                    one plane, the second plane information is ignored 
                  
            
         
        """
        pass
    @property
    def FromView(self) -> NXOpen.View:
        """
        Getter for property: ( NXOpen.View) FromView
         Returns the from view   
            
         
        """
        pass
    @FromView.setter
    def FromView(self, fromview: NXOpen.View):
        """
        Setter for property: ( NXOpen.View) FromView
         Returns the from view   
            
         
        """
        pass
    @property
    def Plane1(self) -> ViewProjectionPlaneBuilder:
        """
        Getter for property: ( ViewProjectionPlaneBuilder NXOpen.) Plane1
         Returns the plane 1   
            
         
        """
        pass
    @property
    def Plane2(self) -> ViewProjectionPlaneBuilder:
        """
        Getter for property: ( ViewProjectionPlaneBuilder NXOpen.) Plane2
         Returns the plane 2, if the type is set to one plane, the second plane information is ignored   
            
         
        """
        pass
    @property
    def ToViews(self) -> SelectDraftingViewList:
        """
        Getter for property: ( SelectDraftingViewList NXOpen.) ToViews
         Returns the to views   
            
         
        """
        pass
    @property
    def Type(self) -> ViewProjectionBuilder.Types:
        """
        Getter for property: ( ViewProjectionBuilder.Types NXOpen.) Type
         Returns the type of the view projection  
            
         
        """
        pass
    @Type.setter
    def Type(self, type: ViewProjectionBuilder.Types):
        """
        Setter for property: ( ViewProjectionBuilder.Types NXOpen.) Type
         Returns the type of the view projection  
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ViewProjectionPlaneBuilder(NXOpen.TaggedObject): 
    """ Represents the View Projection Plane (Drawings.ViewProjectionPlaneBuilder)"""
    class PlaneOptions(Enum):
        """
        Members Include: 
         |Inferred|  Inferred plane from vector, point and plane view 
         |DepthValue|  Get plane using source view and depth value 

        """
        Inferred: int
        DepthValue: int
        @staticmethod
        def ValueOf(value: int) -> ViewProjectionPlaneBuilder.PlaneOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Axis(self) -> NXOpen.Axis:
        """
        Getter for property: ( NXOpen.Axis) Axis
         Returns the axis, define the vector and the point from which to infer the plane   
            
         
        """
        pass
    @Axis.setter
    def Axis(self, axis: NXOpen.Axis):
        """
        Setter for property: ( NXOpen.Axis) Axis
         Returns the axis, define the vector and the point from which to infer the plane   
            
         
        """
        pass
    @property
    def DepthValue(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DepthValue
         Returns the depth value   
            
         
        """
        pass
    @property
    def PlaneOption(self) -> ViewProjectionPlaneBuilder.PlaneOptions:
        """
        Getter for property: ( ViewProjectionPlaneBuilder.PlaneOptions NXOpen.) PlaneOption
         Returns the plane option, decide how to get the plane   
            
         
        """
        pass
    @PlaneOption.setter
    def PlaneOption(self, option: ViewProjectionPlaneBuilder.PlaneOptions):
        """
        Setter for property: ( ViewProjectionPlaneBuilder.PlaneOptions NXOpen.) PlaneOption
         Returns the plane option, decide how to get the plane   
            
         
        """
        pass
    @property
    def View(self) -> SelectDraftingView:
        """
        Getter for property: ( SelectDraftingView NXOpen.) View
         Returns the select view.  
           This defines the plane view.   
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ViewScaleBuilder(NXOpen.TaggedObject): 
    """ Represents the View Scale (Drawings.ViewScaleBuilder)
    """
    class Type(Enum):
        """
        Members Include: 
         |Ratio|  determine scale from numerator  denominator 
         |Expression|  determine scale from expression 

        """
        Ratio: int
        Expression: int
        @staticmethod
        def ValueOf(value: int) -> ViewScaleBuilder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Denominator(self) -> float:
        """
        Getter for property: (float) Denominator
         Returns the scale denominator   
            
         
        """
        pass
    @Denominator.setter
    def Denominator(self, denominator: float):
        """
        Setter for property: (float) Denominator
         Returns the scale denominator   
            
         
        """
        pass
    @property
    def Expression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Expression
         Returns the scale expression   
            
         
        """
        pass
    @Expression.setter
    def Expression(self, expression: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) Expression
         Returns the scale expression   
            
         
        """
        pass
    @property
    def Numerator(self) -> float:
        """
        Getter for property: (float) Numerator
         Returns the scale numerator   
            
         
        """
        pass
    @Numerator.setter
    def Numerator(self, numerator: float):
        """
        Setter for property: (float) Numerator
         Returns the scale numerator   
            
         
        """
        pass
    @property
    def ScaleType(self) -> ViewScaleBuilder.Type:
        """
        Getter for property: ( ViewScaleBuilder.Type NXOpen.) ScaleType
         Returns the scale type   
            
         
        """
        pass
    @ScaleType.setter
    def ScaleType(self, type: ViewScaleBuilder.Type):
        """
        Setter for property: ( ViewScaleBuilder.Type NXOpen.) ScaleType
         Returns the scale type   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ViewSectionLabelBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.Drawings.ViewSectionLabelBuilder
    """
    @property
    def CustomizedViewLabel(self) -> bool:
        """
        Getter for property: (bool) CustomizedViewLabel
         Returns the customized view label   
            
         
        """
        pass
    @CustomizedViewLabel.setter
    def CustomizedViewLabel(self, customizedViewLabel: bool):
        """
        Setter for property: (bool) CustomizedViewLabel
         Returns the customized view label   
            
         
        """
        pass
    @property
    def IncludeParentheses(self) -> bool:
        """
        Getter for property: (bool) IncludeParentheses
         Returns the include parentheses   
            
         
        """
        pass
    @IncludeParentheses.setter
    def IncludeParentheses(self, includeParentheses: bool):
        """
        Setter for property: (bool) IncludeParentheses
         Returns the include parentheses   
            
         
        """
        pass
    @property
    def IncludeRotationAngle(self) -> bool:
        """
        Getter for property: (bool) IncludeRotationAngle
         Returns the include rotation angle   
            
         
        """
        pass
    @IncludeRotationAngle.setter
    def IncludeRotationAngle(self, includeRotationAngle: bool):
        """
        Setter for property: (bool) IncludeRotationAngle
         Returns the include rotation angle   
            
         
        """
        pass
    @property
    def IncludeRotationSymbol(self) -> bool:
        """
        Getter for property: (bool) IncludeRotationSymbol
         Returns the include rotation symbol   
            
         
        """
        pass
    @IncludeRotationSymbol.setter
    def IncludeRotationSymbol(self, includeRotationSymbol: bool):
        """
        Setter for property: (bool) IncludeRotationSymbol
         Returns the include rotation symbol   
            
         
        """
        pass
    @property
    def LabelCharacterHeightFactor(self) -> float:
        """
        Getter for property: (float) LabelCharacterHeightFactor
         Returns the label character height factor   
            
         
        """
        pass
    @LabelCharacterHeightFactor.setter
    def LabelCharacterHeightFactor(self, labelCharacterHeightFactor: float):
        """
        Setter for property: (float) LabelCharacterHeightFactor
         Returns the label character height factor   
            
         
        """
        pass
    @property
    def LabelPosition(self) -> LabelPositionTypes:
        """
        Getter for property: ( LabelPositionTypes NXOpen.) LabelPosition
         Returns the label position   
            
         
        """
        pass
    @LabelPosition.setter
    def LabelPosition(self, labelPosition: LabelPositionTypes):
        """
        Setter for property: ( LabelPositionTypes NXOpen.) LabelPosition
         Returns the label position   
            
         
        """
        pass
    @property
    def LabelPrefix(self) -> str:
        """
        Getter for property: (str) LabelPrefix
         Returns the label prefix   
            
         
        """
        pass
    @LabelPrefix.setter
    def LabelPrefix(self, labelPrefix: str):
        """
        Setter for property: (str) LabelPrefix
         Returns the label prefix   
            
         
        """
        pass
    @property
    def LetterFormat(self) -> LetterFormatTypes:
        """
        Getter for property: ( LetterFormatTypes NXOpen.) LetterFormat
         Returns the letter format   
            
         
        """
        pass
    @LetterFormat.setter
    def LetterFormat(self, letterFormat: LetterFormatTypes):
        """
        Setter for property: ( LetterFormatTypes NXOpen.) LetterFormat
         Returns the letter format   
            
         
        """
        pass
    @property
    def PrefixCharacterHeightFactor(self) -> float:
        """
        Getter for property: (float) PrefixCharacterHeightFactor
         Returns the prefix character height factor   
            
         
        """
        pass
    @PrefixCharacterHeightFactor.setter
    def PrefixCharacterHeightFactor(self, prefixCharacterHeightFactor: float):
        """
        Setter for property: (float) PrefixCharacterHeightFactor
         Returns the prefix character height factor   
            
         
        """
        pass
    @property
    def ReferenceToShow(self) -> ReferenceShowTypes:
        """
        Getter for property: ( ReferenceShowTypes NXOpen.) ReferenceToShow
         Returns the reference to show   
            
         
        """
        pass
    @ReferenceToShow.setter
    def ReferenceToShow(self, referenceToShow: ReferenceShowTypes):
        """
        Setter for property: ( ReferenceShowTypes NXOpen.) ReferenceToShow
         Returns the reference to show   
            
         
        """
        pass
    @property
    def RotationSymbolType(self) -> RotationSymbolTypes:
        """
        Getter for property: ( RotationSymbolTypes NXOpen.) RotationSymbolType
         Returns the rotation symbol type  
            
         
        """
        pass
    @RotationSymbolType.setter
    def RotationSymbolType(self, rotationSymbolType: RotationSymbolTypes):
        """
        Setter for property: ( RotationSymbolTypes NXOpen.) RotationSymbolType
         Returns the rotation symbol type  
            
         
        """
        pass
    @property
    def ScaleCharacterHeightFactor(self) -> float:
        """
        Getter for property: (float) ScaleCharacterHeightFactor
         Returns the scale character height factor   
            
         
        """
        pass
    @ScaleCharacterHeightFactor.setter
    def ScaleCharacterHeightFactor(self, scaleCharacterHeightFactor: float):
        """
        Setter for property: (float) ScaleCharacterHeightFactor
         Returns the scale character height factor   
            
         
        """
        pass
    @property
    def ScalePosition(self) -> ScalePositionTypes:
        """
        Getter for property: ( ScalePositionTypes NXOpen.) ScalePosition
         Returns the scale position   
            
         
        """
        pass
    @ScalePosition.setter
    def ScalePosition(self, scalePosition: ScalePositionTypes):
        """
        Setter for property: ( ScalePositionTypes NXOpen.) ScalePosition
         Returns the scale position   
            
         
        """
        pass
    @property
    def ScalePrefix(self) -> str:
        """
        Getter for property: (str) ScalePrefix
         Returns the scale prefix   
            
         
        """
        pass
    @ScalePrefix.setter
    def ScalePrefix(self, scalePrefix: str):
        """
        Setter for property: (str) ScalePrefix
         Returns the scale prefix   
            
         
        """
        pass
    @property
    def ShowViewLabel(self) -> bool:
        """
        Getter for property: (bool) ShowViewLabel
         Returns the show view label   
            
         
        """
        pass
    @ShowViewLabel.setter
    def ShowViewLabel(self, showViewLabel: bool):
        """
        Setter for property: (bool) ShowViewLabel
         Returns the show view label   
            
         
        """
        pass
    @property
    def ShowViewScale(self) -> bool:
        """
        Getter for property: (bool) ShowViewScale
         Returns the show view scale   
            
         
        """
        pass
    @ShowViewScale.setter
    def ShowViewScale(self, showViewScale: bool):
        """
        Setter for property: (bool) ShowViewScale
         Returns the show view scale   
            
         
        """
        pass
    @property
    def ValueFormat(self) -> ScaleValueFormatTypes:
        """
        Getter for property: ( ScaleValueFormatTypes NXOpen.) ValueFormat
         Returns the section vw label scale value format   
            
         
        """
        pass
    @ValueFormat.setter
    def ValueFormat(self, valueFormat: ScaleValueFormatTypes):
        """
        Setter for property: ( ScaleValueFormatTypes NXOpen.) ValueFormat
         Returns the section vw label scale value format   
            
         
        """
        pass
    @property
    def ViewLabelOption(self) -> ViewLabelTypes:
        """
        Getter for property: ( ViewLabelTypes NXOpen.) ViewLabelOption
         Returns the view label option   
            
         
        """
        pass
    @ViewLabelOption.setter
    def ViewLabelOption(self, viewLabelOption: ViewLabelTypes):
        """
        Setter for property: ( ViewLabelTypes NXOpen.) ViewLabelOption
         Returns the view label option   
            
         
        """
        pass
    def GetCustomizedViewLabelText(self) -> List[str]:
        """
         Returns the customized view label text 
         Returns customizedText (List[str]): .
        """
        pass
    def SetCustomizedViewLabelText(self, customizedText: List[str]) -> None:
        """
         Sets the customized view label text 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ViewSectionLineBuilder(NXOpen.TaggedObject): 
    """ 
     Represents a NXOpen.Drawings.ViewSectionLineBuilder
    """
    class DisplayType(Enum):
        """
        Members Include: 
         |ArrowsAwayfromLine| 
         |ArrowstowardsLine| 
         |ThickEndsArrowstowardsLine| 
         |ThickEndsArrowsAwayfromLine| 

        """
        ArrowsAwayfromLine: int
        ArrowstowardsLine: int
        ThickEndsArrowstowardsLine: int
        ThickEndsArrowsAwayfromLine: int
        @staticmethod
        def ValueOf(value: int) -> ViewSectionLineBuilder.DisplayType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LocationType(Enum):
        """
        Members Include: 
         |OnArrow| 
         |OnEnd| 

        """
        OnArrow: int
        OnEnd: int
        @staticmethod
        def ValueOf(value: int) -> ViewSectionLineBuilder.LocationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ShowSectionLineType(Enum):
        """
        Members Include: 
         |WithSectionView| 
         |WithoutSectionView| 

        """
        WithSectionView: int
        WithoutSectionView: int
        @staticmethod
        def ValueOf(value: int) -> ViewSectionLineBuilder.ShowSectionLineType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StyleType(Enum):
        """
        Members Include: 
         |Open| 
         |Closed| 
         |Filled| 

        """
        Open: int
        Closed: int
        Filled: int
        @staticmethod
        def ValueOf(value: int) -> ViewSectionLineBuilder.StyleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ArrowLength(self) -> float:
        """
        Getter for property: (float) ArrowLength
         Returns the arrow length   
            
         
        """
        pass
    @ArrowLength.setter
    def ArrowLength(self, arrowLength: float):
        """
        Setter for property: (float) ArrowLength
         Returns the arrow length   
            
         
        """
        pass
    @property
    def ArrowheadAngle(self) -> float:
        """
        Getter for property: (float) ArrowheadAngle
         Returns the included angle for the arrowhead   
            
         
        """
        pass
    @ArrowheadAngle.setter
    def ArrowheadAngle(self, arrowheadAngle: float):
        """
        Setter for property: (float) ArrowheadAngle
         Returns the included angle for the arrowhead   
            
         
        """
        pass
    @property
    def ArrowheadLength(self) -> float:
        """
        Getter for property: (float) ArrowheadLength
         Returns the arrowhead length   
            
         
        """
        pass
    @ArrowheadLength.setter
    def ArrowheadLength(self, arrowheadLength: float):
        """
        Setter for property: (float) ArrowheadLength
         Returns the arrowhead length   
            
         
        """
        pass
    @property
    def BendAndEndSegmentWidthFactor(self) -> float:
        """
        Getter for property: (float) BendAndEndSegmentWidthFactor
         Returns the section line bend and end segment width factor   
            
         
        """
        pass
    @BendAndEndSegmentWidthFactor.setter
    def BendAndEndSegmentWidthFactor(self, bendAndEndSegmentWidthFactor: float):
        """
        Setter for property: (float) BendAndEndSegmentWidthFactor
         Returns the section line bend and end segment width factor   
            
         
        """
        pass
    @property
    def BorderToArrowDistance(self) -> float:
        """
        Getter for property: (float) BorderToArrowDistance
         Returns the border to arrow distance   
            
         
        """
        pass
    @BorderToArrowDistance.setter
    def BorderToArrowDistance(self, borderToArrowDistance: float):
        """
        Setter for property: (float) BorderToArrowDistance
         Returns the border to arrow distance   
            
         
        """
        pass
    @property
    def Display(self) -> bool:
        """
        Getter for property: (bool) Display
         Returns the display   
            
         
        """
        pass
    @Display.setter
    def Display(self, display: bool):
        """
        Setter for property: (bool) Display
         Returns the display   
            
         
        """
        pass
    @property
    def DisplayLettersOnBends(self) -> bool:
        """
        Getter for property: (bool) DisplayLettersOnBends
         Returns the display letters on bends   
            
         
        """
        pass
    @DisplayLettersOnBends.setter
    def DisplayLettersOnBends(self, displayLettersOnBends: bool):
        """
        Setter for property: (bool) DisplayLettersOnBends
         Returns the display letters on bends   
            
         
        """
        pass
    @property
    def DisplayRotationLetter(self) -> bool:
        """
        Getter for property: (bool) DisplayRotationLetter
         Returns the display rotation letter   
            
         
        """
        pass
    @DisplayRotationLetter.setter
    def DisplayRotationLetter(self, displayRotationLetter: bool):
        """
        Setter for property: (bool) DisplayRotationLetter
         Returns the display rotation letter   
            
         
        """
        pass
    @property
    def Gap(self) -> float:
        """
        Getter for property: (float) Gap
         Returns the gap   
            
         
        """
        pass
    @Gap.setter
    def Gap(self, gap: float):
        """
        Setter for property: (float) Gap
         Returns the gap   
            
         
        """
        pass
    @property
    def LabelLocation(self) -> ViewSectionLineBuilder.LocationType:
        """
        Getter for property: ( ViewSectionLineBuilder.LocationType NXOpen.) LabelLocation
         Returns the label location   
            
         
        """
        pass
    @LabelLocation.setter
    def LabelLocation(self, labelLocation: ViewSectionLineBuilder.LocationType):
        """
        Setter for property: ( ViewSectionLineBuilder.LocationType NXOpen.) LabelLocation
         Returns the label location   
            
         
        """
        pass
    @property
    def LineColorFontWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) LineColorFontWidth
         Returns the line color font width   
            
         
        """
        pass
    @property
    def LineLength(self) -> float:
        """
        Getter for property: (float) LineLength
         Returns the length of the end of the ESKD section line   
            
         
        """
        pass
    @LineLength.setter
    def LineLength(self, lineLength: float):
        """
        Setter for property: (float) LineLength
         Returns the length of the end of the ESKD section line   
            
         
        """
        pass
    @property
    def Overhang(self) -> float:
        """
        Getter for property: (float) Overhang
         Returns the stub length   
            
         
        """
        pass
    @Overhang.setter
    def Overhang(self, overhang: float):
        """
        Setter for property: (float) Overhang
         Returns the stub length   
            
         
        """
        pass
    @property
    def SelectRotationLetter(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: ( NXOpen.SelectTaggedObject) SelectRotationLetter
         Returns the selected objected should be note type only which is the desired location of the rotation point of the section line specified   
            
         
        """
        pass
    @property
    def ShowSectionLine(self) -> ViewSectionLineBuilder.ShowSectionLineType:
        """
        Getter for property: ( ViewSectionLineBuilder.ShowSectionLineType NXOpen.) ShowSectionLine
         Returns the value to show section line with or without view  
            
         
        """
        pass
    @ShowSectionLine.setter
    def ShowSectionLine(self, showSectionLine: ViewSectionLineBuilder.ShowSectionLineType):
        """
        Setter for property: ( ViewSectionLineBuilder.ShowSectionLineType NXOpen.) ShowSectionLine
         Returns the value to show section line with or without view  
            
         
        """
        pass
    @property
    def Style(self) -> ViewSectionLineBuilder.StyleType:
        """
        Getter for property: ( ViewSectionLineBuilder.StyleType NXOpen.) Style
         Returns the section line arrowhead style   
            
         
        """
        pass
    @Style.setter
    def Style(self, style: ViewSectionLineBuilder.StyleType):
        """
        Setter for property: ( ViewSectionLineBuilder.StyleType NXOpen.) Style
         Returns the section line arrowhead style   
            
         
        """
        pass
    @property
    def TypeStandard(self) -> ViewSectionLineBuilder.DisplayType:
        """
        Getter for property: ( ViewSectionLineBuilder.DisplayType NXOpen.) TypeStandard
         Returns the section line symbol display   
            
         
        """
        pass
    @TypeStandard.setter
    def TypeStandard(self, typeStandard: ViewSectionLineBuilder.DisplayType):
        """
        Setter for property: ( ViewSectionLineBuilder.DisplayType NXOpen.) TypeStandard
         Returns the section line symbol display   
            
         
        """
        pass
    @property
    def UseLineLength(self) -> bool:
        """
        Getter for property: (bool) UseLineLength
         Returns the use line length in case of ESKD section line   
            
         
        """
        pass
    @UseLineLength.setter
    def UseLineLength(self, uselineLength: bool):
        """
        Setter for property: (bool) UseLineLength
         Returns the use line length in case of ESKD section line   
            
         
        """
        pass
    @property
    def UseOffset(self) -> bool:
        """
        Getter for property: (bool) UseOffset
         Returns the use offset   
            
         
        """
        pass
    @UseOffset.setter
    def UseOffset(self, useOffset: bool):
        """
        Setter for property: (bool) UseOffset
         Returns the use offset   
            
         
        """
        pass
    def InheritSettingsFromCustomerDefault(self) -> None:
        """
         Inherit Settings From Customer Default 
        """
        pass
    def InheritSettingsFromPreferences(self) -> None:
        """
         Inherit Settings From Preference 
        """
        pass
    def InheritSettingsFromSelectedObjects(self, selectedObject: NXOpen.NXObject) -> None:
        """
         Inherit Settings From Selected Objects 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ViewSettingsBuilder(NXOpen.TaggedObject): 
    """
    Represents a Drawings.ViewSettingsBuilder.
    This class queries and sets settings specific to drawings data which will get converted to PMI.s
    """
    class RenderingStyleEnum(Enum):
        """
        Members Include: 
         |Shaded| 
         |DrawingViewSetting| 

        """
        Shaded: int
        DrawingViewSetting: int
        @staticmethod
        def ValueOf(value: int) -> ViewSettingsBuilder.RenderingStyleEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AddSheetName(self) -> bool:
        """
        Getter for property: (bool) AddSheetName
         Returns the add sheet name    
            
         
        """
        pass
    @AddSheetName.setter
    def AddSheetName(self, addSheetName: bool):
        """
        Setter for property: (bool) AddSheetName
         Returns the add sheet name    
            
         
        """
        pass
    @property
    def AddSheetNumber(self) -> bool:
        """
        Getter for property: (bool) AddSheetNumber
         Returns the add sheet number   
            
         
        """
        pass
    @AddSheetNumber.setter
    def AddSheetNumber(self, addSheetNumber: bool):
        """
        Setter for property: (bool) AddSheetNumber
         Returns the add sheet number   
            
         
        """
        pass
    @property
    def ApplyCrosshatchToSectionView(self) -> bool:
        """
        Getter for property: (bool) ApplyCrosshatchToSectionView
         Returns the apply crosshatch To section view    
            
         
        """
        pass
    @ApplyCrosshatchToSectionView.setter
    def ApplyCrosshatchToSectionView(self, applyCrosshatchToSectionView: bool):
        """
        Setter for property: (bool) ApplyCrosshatchToSectionView
         Returns the apply crosshatch To section view    
            
         
        """
        pass
    @property
    def ConvertAnnotation(self) -> bool:
        """
        Getter for property: (bool) ConvertAnnotation
         Returns the convert annotation    
            
         
        """
        pass
    @ConvertAnnotation.setter
    def ConvertAnnotation(self, convertAnnotation: bool):
        """
        Setter for property: (bool) ConvertAnnotation
         Returns the convert annotation    
            
         
        """
        pass
    @property
    def Prefix(self) -> str:
        """
        Getter for property: (str) Prefix
         Returns the prefix string   
            
         
        """
        pass
    @Prefix.setter
    def Prefix(self, prefix: str):
        """
        Setter for property: (str) Prefix
         Returns the prefix string   
            
         
        """
        pass
    @property
    def RenderingStyle(self) -> ViewSettingsBuilder.RenderingStyleEnum:
        """
        Getter for property: ( ViewSettingsBuilder.RenderingStyleEnum NXOpen.) RenderingStyle
         Returns the rendering style   
            
         
        """
        pass
    @RenderingStyle.setter
    def RenderingStyle(self, renderingStyle: ViewSettingsBuilder.RenderingStyleEnum):
        """
        Setter for property: ( ViewSettingsBuilder.RenderingStyleEnum NXOpen.) RenderingStyle
         Returns the rendering style   
            
         
        """
        pass
    @property
    def SectionGeometryTolerance(self) -> float:
        """
        Getter for property: (float) SectionGeometryTolerance
         Returns the section geometry tolerance   
            
         
        """
        pass
    @SectionGeometryTolerance.setter
    def SectionGeometryTolerance(self, sectionGeometryTolerance: float):
        """
        Setter for property: (float) SectionGeometryTolerance
         Returns the section geometry tolerance   
            
         
        """
        pass
    @property
    def Separator(self) -> str:
        """
        Getter for property: (str) Separator
         Returns the separator string   
            
         
        """
        pass
    @Separator.setter
    def Separator(self, separator: str):
        """
        Setter for property: (str) Separator
         Returns the separator string   
            
         
        """
        pass
    @property
    def UseAssemblyCrosshatch(self) -> bool:
        """
        Getter for property: (bool) UseAssemblyCrosshatch
         Returns the use assembly crosshatch    
            
         
        """
        pass
    @UseAssemblyCrosshatch.setter
    def UseAssemblyCrosshatch(self, useAssemblyCrosshatch: bool):
        """
        Setter for property: (bool) UseAssemblyCrosshatch
         Returns the use assembly crosshatch    
            
         
        """
        pass
import NXOpen
class ViewStyleAECViewLinesBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[ViewStyleAECViewLinesBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: ViewStyleAECViewLinesBuilder) -> None:
        """
         Appends an object to the list
            
        """
        pass
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
               not change, but the item at this index is set to NULL.
            
        """
        pass
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, obj: ViewStyleAECViewLinesBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: ViewStyleAECViewLinesBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: ViewStyleAECViewLinesBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> ViewStyleAECViewLinesBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( ViewStyleAECViewLinesBuilder NXOpen.):  object found at input index .
        """
        pass
    def GetContents(self) -> List[ViewStyleAECViewLinesBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( ViewStyleAECViewLinesBuilder List[NXOpe):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: ViewStyleAECViewLinesBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    def SetContents(self, objects: List[ViewStyleAECViewLinesBuilder]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    @overload
    def Swap(self, object1: ViewStyleAECViewLinesBuilder, object2: ViewStyleAECViewLinesBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.Preferences
class ViewStyleAECViewLinesBuilder(NXOpen.Builder): 
    """ 
    Represents a NXOpen.Drawings.ViewStyleAECViewLinesBuilder builder. This builder is used to 
    set the view lines color, font, width, show flag. 
    """
    @property
    def HiddenColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) HiddenColor
         Returns the hidden color on the AEC Structure Lines   
            
         
        """
        pass
    @HiddenColor.setter
    def HiddenColor(self, hiddenColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) HiddenColor
         Returns the hidden color on the AEC Structure Lines   
            
         
        """
        pass
    @property
    def HiddenFont(self) -> NXOpen.Preferences.Font:
        """
        Getter for property: ( NXOpen.Preferences.Font) HiddenFont
         Returns the hidden font on the AEC Structure Lines   
            
         
        """
        pass
    @HiddenFont.setter
    def HiddenFont(self, hiddenFont: NXOpen.Preferences.Font):
        """
        Setter for property: ( NXOpen.Preferences.Font) HiddenFont
         Returns the hidden font on the AEC Structure Lines   
            
         
        """
        pass
    @property
    def HiddenWidth(self) -> NXOpen.Preferences.Width:
        """
        Getter for property: ( NXOpen.Preferences.Width) HiddenWidth
         Returns the hidden width on the AEC Structure Lines   
            
         
        """
        pass
    @HiddenWidth.setter
    def HiddenWidth(self, hiddenWidth: NXOpen.Preferences.Width):
        """
        Setter for property: ( NXOpen.Preferences.Width) HiddenWidth
         Returns the hidden width on the AEC Structure Lines   
            
         
        """
        pass
    @property
    def ShowMultipleBodies(self) -> bool:
        """
        Getter for property: (bool) ShowMultipleBodies
         Returns the flag to indicate whether or not to show multiple bodies.  
             
         
        """
        pass
    @ShowMultipleBodies.setter
    def ShowMultipleBodies(self, showMultipleBodies: bool):
        """
        Setter for property: (bool) ShowMultipleBodies
         Returns the flag to indicate whether or not to show multiple bodies.  
             
         
        """
        pass
    @property
    def VisibleColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) VisibleColor
         Returns the visible color on the AEC Structure Lines   
            
         
        """
        pass
    @VisibleColor.setter
    def VisibleColor(self, visibleColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) VisibleColor
         Returns the visible color on the AEC Structure Lines   
            
         
        """
        pass
    @property
    def VisibleFont(self) -> NXOpen.Preferences.Font:
        """
        Getter for property: ( NXOpen.Preferences.Font) VisibleFont
         Returns the visible font on the AEC Structure Lines   
            
         
        """
        pass
    @VisibleFont.setter
    def VisibleFont(self, visibleFont: NXOpen.Preferences.Font):
        """
        Setter for property: ( NXOpen.Preferences.Font) VisibleFont
         Returns the visible font on the AEC Structure Lines   
            
         
        """
        pass
    @property
    def VisibleWidth(self) -> NXOpen.Preferences.Width:
        """
        Getter for property: ( NXOpen.Preferences.Width) VisibleWidth
         Returns the visible width on the AEC Structure Lines   
            
         
        """
        pass
    @VisibleWidth.setter
    def VisibleWidth(self, visibleWidth: NXOpen.Preferences.Width):
        """
        Setter for property: ( NXOpen.Preferences.Width) VisibleWidth
         Returns the visible width on the AEC Structure Lines   
            
         
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.GeometricUtilities
class ViewStyleBaseBuilder(NXOpen.TaggedObject): 
    """ Represents the BASE tab on the View Style Dialog (Drawings.ViewStyleBaseBuilder)
    """
    @property
    def Arrangement(self) -> NXOpen.Assemblies.ArrangementsBuilder:
        """
        Getter for property: ( NXOpen.Assemblies.ArrangementsBuilder) Arrangement
         Returns the arrangement on the BASE tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def ArrangementName(self) -> str:
        """
        Getter for property: (str) ArrangementName
         Returns the arrangement name on the BASE tab of the View Style Dialog   
            
         
        """
        pass
    @ArrangementName.setter
    def ArrangementName(self, arrangementName: str):
        """
        Setter for property: (str) ArrangementName
         Returns the arrangement name on the BASE tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def FacetedRepresentation(self) -> bool:
        """
        Getter for property: (bool) FacetedRepresentation
         Returns the faceted representation toggle on the BASE tab of the View Style Dialog   
            
         
        """
        pass
    @FacetedRepresentation.setter
    def FacetedRepresentation(self, facetedRepresentationToggle: bool):
        """
        Setter for property: (bool) FacetedRepresentation
         Returns the faceted representation toggle on the BASE tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def InheritClippingBoundary(self) -> bool:
        """
        Getter for property: (bool) InheritClippingBoundary
         Returns the inherit clipping boundary toggle on the BASE tab of the View Style Dialog   
            
         
        """
        pass
    @InheritClippingBoundary.setter
    def InheritClippingBoundary(self, inheritClippingBoundaryToggle: bool):
        """
        Setter for property: (bool) InheritClippingBoundary
         Returns the inherit clipping boundary toggle on the BASE tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Part(self) -> NXOpen.Part:
        """
        Getter for property: ( NXOpen.Part) Part
         Returns the part on the BASE tab of the View Style Dialog   
            
         
        """
        pass
    @Part.setter
    def Part(self, part: NXOpen.Part):
        """
        Setter for property: ( NXOpen.Part) Part
         Returns the part on the BASE tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def PartName(self) -> str:
        """
        Getter for property: (str) PartName
         Returns the part name on the BASE tab of the View Style Dialog   
            
         
        """
        pass
    @PartName.setter
    def PartName(self, partName: str):
        """
        Setter for property: (str) PartName
         Returns the part name on the BASE tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def TransferAnnotation(self) -> bool:
        """
        Getter for property: (bool) TransferAnnotation
         Returns the transfer annotation toggle on the BASE tab of the View Style Dialog   
            
         
        """
        pass
    @TransferAnnotation.setter
    def TransferAnnotation(self, transferAnnotationToggle: bool):
        """
        Setter for property: (bool) TransferAnnotation
         Returns the transfer annotation toggle on the BASE tab of the View Style Dialog   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
import NXOpen.SheetMetal
class ViewStyleBuilder(NXOpen.TaggedObject): 
    """ Represents the View Style Builder (Drawings.ViewStyleBuilder) which manages all the style attributes related
       to the view including base view, projected view, drawing view, detail view, broken view, section view etc.
       To obtain an instance of this class, we need to follow the steps: create a new view, click the view style 
       button, edit the view style attributes.
    """
    @property
    def ProjectedViewOrientation(self) -> ProjectedViewOrientationBuilder:
        """
        Getter for property: ( ProjectedViewOrientationBuilder NXOpen.) ProjectedViewOrientation
         Returns the projected view orientation builder   
            
         
        """
        pass
    @property
    def SecondaryComponents(self) -> ViewStyleSecondaryComponentsBuilder:
        """
        Getter for property: ( ViewStyleSecondaryComponentsBuilder NXOpen.) SecondaryComponents
         Returns the secondary components style builder of the view style builder which represents the secondary geometry tab on the View Style Dialog   
            
         
        """
        pass
    @property
    def ViewCommonViewLabel(self) -> ViewCommonViewLabelBuilder:
        """
        Getter for property: ( ViewCommonViewLabelBuilder NXOpen.) ViewCommonViewLabel
         Returns the view common label builder  
            
         
        """
        pass
    @property
    def ViewProjectedArrowSettings(self) -> ViewProjectedArrowSettingsBuilder:
        """
        Getter for property: ( ViewProjectedArrowSettingsBuilder NXOpen.) ViewProjectedArrowSettings
         Returns the projected Arrow Settings builder   
            
         
        """
        pass
    @property
    def ViewProjectedViewSettings(self) -> ViewProjectedViewSettingsBuilder:
        """
        Getter for property: ( ViewProjectedViewSettingsBuilder NXOpen.) ViewProjectedViewSettings
         Returns the projected View Settings builder   
            
         
        """
        pass
    @property
    def ViewSectionLineStyleBuilder(self) -> ViewSectionLineBuilder:
        """
        Getter for property: ( ViewSectionLineBuilder NXOpen.) ViewSectionLineStyleBuilder
         Returns the view section line builder  
            
         
        """
        pass
    @property
    def ViewStyleAecViewLinesList(self) -> ViewStyleAECViewLinesBuilderList:
        """
        Getter for property: ( ViewStyleAECViewLinesBuilderList NXOpen.) ViewStyleAecViewLinesList
         Returns the AEC View lines builder of the view style builder which represents the AEC drafting view lines on the View Style Dialog   
            
         
        """
        pass
    @property
    def ViewStyleBase(self) -> ViewStyleBaseBuilder:
        """
        Getter for property: ( ViewStyleBaseBuilder NXOpen.) ViewStyleBase
         Returns the Base style builder of the view style builder which represents the base tab on the View Style Dialog   
            
         
        """
        pass
    @property
    def ViewStyleDetail(self) -> ViewStyleDetailBuilder:
        """
        Getter for property: ( ViewStyleDetailBuilder NXOpen.) ViewStyleDetail
         Returns the Detail style builder of the view style builder which represents the detail tab on the View Style Dialog   
            
         
        """
        pass
    @property
    def ViewStyleGeneral(self) -> ViewStyleGeneralBuilder:
        """
        Getter for property: ( ViewStyleGeneralBuilder NXOpen.) ViewStyleGeneral
         Returns the General style builder of the view style builder which represents the general tab on the View Style Dialog   
            
         
        """
        pass
    @property
    def ViewStyleHiddenLines(self) -> ViewStyleHiddenLinesBuilder:
        """
        Getter for property: ( ViewStyleHiddenLinesBuilder NXOpen.) ViewStyleHiddenLines
         Returns the Hidden Lines style builder of the view style builder which represents the hidden lines tab on the View Style Dialog   
            
         
        """
        pass
    @property
    def ViewStyleInheritPmi(self) -> ViewStyleInheritPmiBuilder:
        """
        Getter for property: ( ViewStyleInheritPmiBuilder NXOpen.) ViewStyleInheritPmi
         Returns the Inherit PMI style builder of the view style builder which represents the inherit PMI tab on the View Style Dialog   
            
         
        """
        pass
    @property
    def ViewStyleOrientation(self) -> ViewStyleOrientationBuilder:
        """
        Getter for property: ( ViewStyleOrientationBuilder NXOpen.) ViewStyleOrientation
         Returns the Orientation style builder of the view style builder which represents the orientation tab on the View Style Dialog   
            
         
        """
        pass
    @property
    def ViewStylePerspective(self) -> ViewStylePerspectiveBuilder:
        """
        Getter for property: ( ViewStylePerspectiveBuilder NXOpen.) ViewStylePerspective
         Returns the Perspective style builder of the view style builder which represents the perspective tab on the View Style Dialog   
            
         
        """
        pass
    @property
    def ViewStyleProjected(self) -> ViewStyleProjectedBuilder:
        """
        Getter for property: ( ViewStyleProjectedBuilder NXOpen.) ViewStyleProjected
         Returns the projected style builder of the view style builder which represents the projected tab on the View Style Dialog   
            
         
        """
        pass
    @property
    def ViewStyleSection(self) -> ViewStyleSectionBuilder:
        """
        Getter for property: ( ViewStyleSectionBuilder NXOpen.) ViewStyleSection
         Returns the Section style builder of the view style builder which represents the section tab on the View Style Dialog   
            
         
        """
        pass
    @property
    def ViewStyleSectionConstraints(self) -> ViewStyleSectionConstraintsBuilder:
        """
        Getter for property: ( ViewStyleSectionConstraintsBuilder NXOpen.) ViewStyleSectionConstraints
         Returns the Section Constraints style builder of the view style builder which represents the section constraints tab on the View Style Dialog   
            
         
        """
        pass
    @property
    def ViewStyleShading(self) -> ViewStyleShadingBuilder:
        """
        Getter for property: ( ViewStyleShadingBuilder NXOpen.) ViewStyleShading
         Returns the Shading style builder of the view style builder which represents the shading tab on the View Style Dialog   
            
         
        """
        pass
    @property
    def ViewStyleShipDraftingViewLinesList(self) -> ShipDraftingViewLinesBuilderList:
        """
        Getter for property: ( ShipDraftingViewLinesBuilderList NXOpen.) ViewStyleShipDraftingViewLinesList
         Returns the Ship Drafting View lines builder of the view style builder which represents the ship drafting view lines on the View Style Dialog   
            
         
        """
        pass
    @property
    def ViewStyleShipGeneralArrangementViewLinesList(self) -> ShipGeneralArrangementViewLinesBuilderList:
        """
        Getter for property: ( ShipGeneralArrangementViewLinesBuilderList NXOpen.) ViewStyleShipGeneralArrangementViewLinesList
         Returns the Ship General Arrangement View lines builder of the view style builder which represents the ship drafting view lines on the View Style Dialog   
            
         
        """
        pass
    @property
    def ViewStyleSingleLineList(self) -> ViewStyleShipbuildingLinesBuilderList:
        """
        Getter for property: ( ViewStyleShipbuildingLinesBuilderList NXOpen.) ViewStyleSingleLineList
         Returns the Ship building lines style builder of the view style builder which represents the ship building lines tab on the View Style Dialog   
            
         
        """
        pass
    @property
    def ViewStyleSmoothEdges(self) -> ViewStyleSmoothEdgesBuilder:
        """
        Getter for property: ( ViewStyleSmoothEdgesBuilder NXOpen.) ViewStyleSmoothEdges
         Returns the Smooth Edges style builder of the view style builder which represents the smooth edges tab on the View Style Dialog   
            
         
        """
        pass
    @property
    def ViewStyleThreads(self) -> ViewStyleThreadsBuilder:
        """
        Getter for property: ( ViewStyleThreadsBuilder NXOpen.) ViewStyleThreads
         Returns the Threads style builder of the view style builder which represents the threads tab on the View Style Dialog   
            
         
        """
        pass
    @property
    def ViewStyleTraceLines(self) -> ViewStyleTraceLinesBuilder:
        """
        Getter for property: ( ViewStyleTraceLinesBuilder NXOpen.) ViewStyleTraceLines
         Returns the Trace lines style builder of the view style builder which represents the trace lines tab on the View Style Dialog   
            
         
        """
        pass
    @property
    def ViewStyleVirtualIntersections(self) -> ViewStyleVirtualIntersectionsBuilder:
        """
        Getter for property: ( ViewStyleVirtualIntersectionsBuilder NXOpen.) ViewStyleVirtualIntersections
         Returns the Virtual intersections style builder of the view style builder which represents the virtual intersections tab on the View Style Dialog   
            
         
        """
        pass
    @property
    def ViewStyleVisibleLines(self) -> ViewStyleVisibleLinesBuilder:
        """
        Getter for property: ( ViewStyleVisibleLinesBuilder NXOpen.) ViewStyleVisibleLines
         Returns the Visible lines style builder of the view style builder which represents the visible lines tab on the View Style Dialog   
            
         
        """
        pass
    def CreateAECViewLinesBuilder(self) -> ViewStyleAECViewLinesBuilder:
        """
         Creates a NXOpen.Drawings.ViewStyleAECViewLinesBuilder 
         Returns style ( ViewStyleAECViewLinesBuilder NXOpen.):  Returns the empty AEC View Lines sub-builder on View Style .
        """
        pass
    def FindAECViewLinesBuilderByName(self, structureName: str) -> ViewStyleAECViewLinesBuilder:
        """
         Gets the NXOpen.Drawings.ViewStyleAECViewLinesBuilder with the given view plan and display name 
         Returns aecViewLinesBuilder ( ViewStyleAECViewLinesBuilder NXOpen.):  Returns the AEC View Lines sub-builders with the given ObjectName .
        """
        pass
    def FindShipDraftingViewLinesBuilderByName(self, featureName: str, featureSubName: str) -> ShipDraftingViewLinesBuilder:
        """
         Gets the NXOpen.Drawings.ShipDraftingViewLinesBuilder with the given FeatureName and FeatureSubName 
         Returns shipDraftingViewLinesBuilder ( ShipDraftingViewLinesBuilder NXOpen.):  Returns the Ship Drafting View Lines sub-builders with the given FeatureName and FeatureSubName .
        """
        pass
    def FindShipGeneralArrangementViewLinesBuilderByName(self, viewPlan: str, displayName: str) -> ShipGeneralArrangementViewLinesBuilder:
        """
         Gets the NXOpen.Drawings.ShipGeneralArrangementViewLinesBuilder with the given view plan and display name 
         Returns shipGeneralArrangementViewLinesBuilder ( ShipGeneralArrangementViewLinesBuilder NXOpen.):  Returns the Ship General Arrangement View Lines sub-builders with the given ViewPlan and DisplayName .
        """
        pass
    def GetAllViewStyleFPCallouts(self) -> List[ViewStyleFPCalloutsBuilder]:
        """
         Retrieves all the Callouts on the Flat Pattern Tab on the View Style Dialog 
         Returns calloutBuilders ( ViewStyleFPCalloutsBuilder List[NXOpe):  Returns all the Flat Pattern Callout sub-builders on View Style .
        """
        pass
    def GetAllViewStyleFPCurves(self) -> List[ViewStyleFPCurvesBuilder]:
        """
         Retrieves all the Curves on the Flat Pattern Tab on the View Style Dialog 
         Returns curveBuilders ( ViewStyleFPCurvesBuilder List[NXOpe):  Returns all the Flat Pattern Curve sub-builders on View Style .
        """
        pass
    def GetViewStyleFPCallout(self, type: str) -> ViewStyleFPCalloutsBuilder:
        """
         Retrieves a specified Callout on the Flat Pattern Tab on the View Style Dialog 
         Returns calloutBuilder ( ViewStyleFPCalloutsBuilder NXOpen.):  Returns the particular Flat Pattern Callout sub-builder on View Style .
        """
        pass
    def GetViewStyleFPCalloutConfig(self) -> ViewStyleFPCalloutConfigBuilder:
        """
         Retrieves the callout configuration on the Flat Pattern Tab on the View Style Dialog 
         Returns calloutConfigBuilder ( ViewStyleFPCalloutConfigBuilder NXOpen.):  Returns the Flat Pattern Callout Config sub-builder on View Style .
        """
        pass
    def GetViewStyleFPCurve(self, type: NXOpen.SheetMetal.FlatPatternSettings.FlatPatternObjectType) -> ViewStyleFPCurvesBuilder:
        """
         Retrieves a specified Curve on the Flat Pattern Tab on the View Style Dialog 
         Returns curveBuilder ( ViewStyleFPCurvesBuilder NXOpen.):  Returns the particular Flat Pattern Curve sub-builder on View Style .
        """
        pass
    def InheritSettingsFromCustomerDefault(self) -> None:
        """
         Inherit Settings From Customer Default 
        """
        pass
    def InheritSettingsFromPreferences(self) -> None:
        """
         Inherit Settings From Preference 
        """
        pass
    def InheritSettingsFromSelectedObjects(self, selectedObject: NXOpen.NXObject) -> None:
        """
         Inherit Settings From Selected Objects 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
import NXOpen.Preferences
class ViewStyleDetailBuilder(NXOpen.TaggedObject): 
    """ Represents the DETAIL tab on the View Style Dialog (Drawings.ViewStyleDetailBuilder)
    """
    @property
    def Align(self) -> bool:
        """
        Getter for property: (bool) Align
         Returns the align toggle on the DETAIL tab of the View Style Dialog   
            
         
        """
        pass
    @Align.setter
    def Align(self, alignToggle: bool):
        """
        Setter for property: (bool) Align
         Returns the align toggle on the DETAIL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Circular(self) -> bool:
        """
        Getter for property: (bool) Circular
         Returns the circular toggle on the DETAIL tab of the View Style Dialog   
            
         
        """
        pass
    @Circular.setter
    def Circular(self, circularToggle: bool):
        """
        Setter for property: (bool) Circular
         Returns the circular toggle on the DETAIL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def ClipViewBoundary(self) -> bool:
        """
        Getter for property: (bool) ClipViewBoundary
         Returns the clip boundary toggle on the DETAIL tab of the View Style Dialog   
            
         
        """
        pass
    @ClipViewBoundary.setter
    def ClipViewBoundary(self, clipViewBoundaryToggle: bool):
        """
        Setter for property: (bool) ClipViewBoundary
         Returns the clip boundary toggle on the DETAIL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def CreateIndependentDetailView(self) -> bool:
        """
        Getter for property: (bool) CreateIndependentDetailView
         Returns the create independent detail view toggle on the DETAIL tab of the View Style Dialog   
            
         
        """
        pass
    @CreateIndependentDetailView.setter
    def CreateIndependentDetailView(self, createIndependentDetailViewToggle: bool):
        """
        Setter for property: (bool) CreateIndependentDetailView
         Returns the create independent detail view toggle on the DETAIL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Offset(self) -> bool:
        """
        Getter for property: (bool) Offset
         Returns the offset toggle on the DETAIL tab of the View Style Dialog   
            
         
        """
        pass
    @Offset.setter
    def Offset(self, offsetToggle: bool):
        """
        Setter for property: (bool) Offset
         Returns the offset toggle on the DETAIL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Orient(self) -> bool:
        """
        Getter for property: (bool) Orient
         Returns the orient toggle on the DETAIL tab of the View Style Dialog   
            
         
        """
        pass
    @Orient.setter
    def Orient(self, orientToggle: bool):
        """
        Setter for property: (bool) Orient
         Returns the orient toggle on the DETAIL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Scale(self) -> bool:
        """
        Getter for property: (bool) Scale
         Returns the scale toggle on the DETAIL tab of the View Style Dialog   
            
         
        """
        pass
    @Scale.setter
    def Scale(self, scaleToggle: bool):
        """
        Setter for property: (bool) Scale
         Returns the scale toggle on the DETAIL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Sheet(self) -> bool:
        """
        Getter for property: (bool) Sheet
         Returns the sheet toggle on the DETAIL tab of the View Style Dialog   
            
         
        """
        pass
    @Sheet.setter
    def Sheet(self, sheetToggle: bool):
        """
        Setter for property: (bool) Sheet
         Returns the sheet toggle on the DETAIL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def ViewBoundaryColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) ViewBoundaryColor
         Returns the view boundary color on the DETAIL tab of the View Style Dialog   
            
         
        """
        pass
    @ViewBoundaryColor.setter
    def ViewBoundaryColor(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) ViewBoundaryColor
         Returns the view boundary color on the DETAIL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def ViewBoundaryFont(self) -> NXOpen.Preferences.Font:
        """
        Getter for property: ( NXOpen.Preferences.Font) ViewBoundaryFont
         Returns the view boundary font on the DETAIL tab of the View Style Dialog   
            
         
        """
        pass
    @ViewBoundaryFont.setter
    def ViewBoundaryFont(self, font: NXOpen.Preferences.Font):
        """
        Setter for property: ( NXOpen.Preferences.Font) ViewBoundaryFont
         Returns the view boundary font on the DETAIL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def ViewBoundaryWidth(self) -> NXOpen.Preferences.Width:
        """
        Getter for property: ( NXOpen.Preferences.Width) ViewBoundaryWidth
         Returns the view boundary width on the DETAIL tab of the View Style Dialog   
            
         
        """
        pass
    @ViewBoundaryWidth.setter
    def ViewBoundaryWidth(self, width: NXOpen.Preferences.Width):
        """
        Setter for property: ( NXOpen.Preferences.Width) ViewBoundaryWidth
         Returns the view boundary width on the DETAIL tab of the View Style Dialog   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ViewStyleFPCalloutConfigBuilder(NXOpen.TaggedObject): 
    """ Represents the Callout section of the Flat Pattern tab on the View Style Dialog (Drawings.ViewStyleFPCalloutsBuilder)
    """
    class OrientationType(Enum):
        """
        Members Include: 
         |Leadered|  Leadered 
         |Aligned|  Aligned 

        """
        Leadered: int
        Aligned: int
        @staticmethod
        def ValueOf(value: int) -> ViewStyleFPCalloutConfigBuilder.OrientationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetContents(self, calloutType: str) -> List[str]:
        """
         Returns the contents for a Flat Pattern callout type 
         Returns contents (List[str]):  The contents for the callout type. .
        """
        pass
    def GetOrientationType(self) -> ViewStyleFPCalloutConfigBuilder.OrientationType:
        """
         Returns the orientation type for flat pattern callouts. 
         Returns orientation ( ViewStyleFPCalloutConfigBuilder.OrientationType NXOpen.):  The orientation type for the flat pattern callouts. .
        """
        pass
    def SetContents(self, calloutType: str, contents: List[str]) -> None:
        """
         Sets the contents for a Flat Pattern callout type 
        """
        pass
    def SetOrientationType(self, orientation: ViewStyleFPCalloutConfigBuilder.OrientationType) -> None:
        """
         Sets the orientation type for flat pattern callouts. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ViewStyleFPCalloutsBuilder(NXOpen.TaggedObject): 
    """ Represents the Callout section of the Flat Pattern tab on the View Style Dialog (Drawings.ViewStyleFPCalloutsBuilder)
    """
    @property
    def State(self) -> bool:
        """
        Getter for property: (bool) State
         Returns the state toggle on the Callout section of the Flat Pattern tab of the View Style Dialog   
            
         
        """
        pass
    @State.setter
    def State(self, stateToggle: bool):
        """
        Setter for property: (bool) State
         Returns the state toggle on the Callout section of the Flat Pattern tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Type(self) -> str:
        """
        Getter for property: (str) Type
         Returns the type of Flat Pattern Callout   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
import NXOpen.Preferences
import NXOpen.SheetMetal
class ViewStyleFPCurvesBuilder(NXOpen.TaggedObject): 
    """ Represents the Curve section of the Flat Pattern tab on the View Style Dialog (Drawings.ViewStyleFPCurvesBuilder)
    """
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) Color
         Returns the color on the Curve section of the Flat Pattern tab of the View Style Dialog   
            
         
        """
        pass
    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) Color
         Returns the color on the Curve section of the Flat Pattern tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Font(self) -> NXOpen.Preferences.Font:
        """
        Getter for property: ( NXOpen.Preferences.Font) Font
         Returns the font on the Curve section of the Flat Pattern tab of the View Style Dialog   
            
         
        """
        pass
    @Font.setter
    def Font(self, font: NXOpen.Preferences.Font):
        """
        Setter for property: ( NXOpen.Preferences.Font) Font
         Returns the font on the Curve section of the Flat Pattern tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def State(self) -> bool:
        """
        Getter for property: (bool) State
         Returns the state toggle on the Curve section of the Flat Pattern tab of the View Style Dialog   
            
         
        """
        pass
    @State.setter
    def State(self, stateToggle: bool):
        """
        Setter for property: (bool) State
         Returns the state toggle on the Curve section of the Flat Pattern tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Type(self) -> NXOpen.SheetMetal.FlatPatternSettings.FlatPatternObjectType:
        """
        Getter for property: ( NXOpen.SheetMetal.FlatPatternSettings.FlatPatternObjectType) Type
         Returns the type of Flat Pattern Curve   
            
         
        """
        pass
    @property
    def Width(self) -> NXOpen.Preferences.Width:
        """
        Getter for property: ( NXOpen.Preferences.Width) Width
         Returns the width on the Curve section of the Flat Pattern tab of the View Style Dialog   
            
         
        """
        pass
    @Width.setter
    def Width(self, width: NXOpen.Preferences.Width):
        """
        Setter for property: ( NXOpen.Preferences.Width) Width
         Returns the width on the Curve section of the Flat Pattern tab of the View Style Dialog   
            
         
        """
        pass
import NXOpen
import NXOpen.Annotations
import NXOpen.GeometricUtilities
class ViewStyleFrameBarBuilder(NXOpen.TaggedObject): 
    """ Represents view style frame bar builder (Drawings.ViewStyleFrameBarBuilder) which manages all the
       position attributes which are necessary for create a frame bar.
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
    def HorizontalPosition(self) -> NXOpen.Annotations.BaseFrameBarBuilder.HorizontalPositionType:
        """
        Getter for property: ( NXOpen.Annotations.BaseFrameBarBuilder.HorizontalPositionType) HorizontalPosition
         Returns the horizontal position   
            
         
        """
        pass
    @HorizontalPosition.setter
    def HorizontalPosition(self, horizontalPosition: NXOpen.Annotations.BaseFrameBarBuilder.HorizontalPositionType):
        """
        Setter for property: ( NXOpen.Annotations.BaseFrameBarBuilder.HorizontalPositionType) HorizontalPosition
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
    def VerticalPosition(self) -> NXOpen.Annotations.BaseFrameBarBuilder.VerticalPositionType:
        """
        Getter for property: ( NXOpen.Annotations.BaseFrameBarBuilder.VerticalPositionType) VerticalPosition
         Returns the vertical position   
            
         
        """
        pass
    @VerticalPosition.setter
    def VerticalPosition(self, verticalPosition: NXOpen.Annotations.BaseFrameBarBuilder.VerticalPositionType):
        """
        Setter for property: ( NXOpen.Annotations.BaseFrameBarBuilder.VerticalPositionType) VerticalPosition
         Returns the vertical position   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
import NXOpen.Preferences
class ViewStyleGeneralBuilder(NXOpen.TaggedObject): 
    """ Represents view style general builder (Drawings.ViewStyleGeneralBuilder) which manages all the general
       attributes which are necessary for all the views.
       To obtain an instance of the class, we need to follow the steps: creat a new view, click the view style
       button on the view dialog, edit the view style general tab.
    """
    @property
    def AngleDecimalPointCharacter(self) -> NXOpen.Preferences.DecimalPointCharacter:
        """
        Getter for property: ( NXOpen.Preferences.DecimalPointCharacter) AngleDecimalPointCharacter
         Returns the decimal point character to use for view angle display.  
             
         
        """
        pass
    @AngleDecimalPointCharacter.setter
    def AngleDecimalPointCharacter(self, decimalPointCharacter: NXOpen.Preferences.DecimalPointCharacter):
        """
        Setter for property: ( NXOpen.Preferences.DecimalPointCharacter) AngleDecimalPointCharacter
         Returns the decimal point character to use for view angle display.  
             
         
        """
        pass
    @property
    def AngleFormat(self) -> NXOpen.Preferences.AngleFormat:
        """
        Getter for property: ( NXOpen.Preferences.AngleFormat) AngleFormat
         Returns the format to use for view angle display.  
             
         
        """
        pass
    @AngleFormat.setter
    def AngleFormat(self, angleFormat: NXOpen.Preferences.AngleFormat):
        """
        Setter for property: ( NXOpen.Preferences.AngleFormat) AngleFormat
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
    def AnglePrecision(self, anglePrecision: int):
        """
        Setter for property: (int) AnglePrecision
         Returns the precision to use for view angle display.  
             
         
        """
        pass
    @property
    def AngleSetting(self) -> AssociativeAngleBuilder:
        """
        Getter for property: ( AssociativeAngleBuilder NXOpen.) AngleSetting
         Returns the angle value on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def AngleShowLeadingZeros(self) -> bool:
        """
        Getter for property: (bool) AngleShowLeadingZeros
         Returns the status of leading zeros display in view angle.  
             
         
        """
        pass
    @AngleShowLeadingZeros.setter
    def AngleShowLeadingZeros(self, showLeadingZeros: bool):
        """
        Setter for property: (bool) AngleShowLeadingZeros
         Returns the status of leading zeros display in view angle.  
             
         
        """
        pass
    @property
    def AngleShowTrailingZeros(self) -> bool:
        """
        Getter for property: (bool) AngleShowTrailingZeros
         Returns the status of trailing zeros display in view angle.  
             
         
        """
        pass
    @AngleShowTrailingZeros.setter
    def AngleShowTrailingZeros(self, showTrailingZeros: bool):
        """
        Setter for property: (bool) AngleShowTrailingZeros
         Returns the status of trailing zeros display in view angle.  
             
         
        """
        pass
    @property
    def AngleValue(self) -> float:
        """
        Getter for property: (float) AngleValue
         Returns the angle value on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @AngleValue.setter
    def AngleValue(self, angleValue: float):
        """
        Setter for property: (float) AngleValue
         Returns the angle value on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def AutomaticAnchorPoint(self) -> bool:
        """
        Getter for property: (bool) AutomaticAnchorPoint
         Returns the automatic anchor point toggle on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @AutomaticAnchorPoint.setter
    def AutomaticAnchorPoint(self, automaticAnchorPointToggle: bool):
        """
        Setter for property: (bool) AutomaticAnchorPoint
         Returns the automatic anchor point toggle on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def AutomaticUpdate(self) -> bool:
        """
        Getter for property: (bool) AutomaticUpdate
         Returns the automatic update toggle on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @AutomaticUpdate.setter
    def AutomaticUpdate(self, automaticUpdateToggle: bool):
        """
        Setter for property: (bool) AutomaticUpdate
         Returns the automatic update toggle on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def BoundaryStatus(self) -> bool:
        """
        Getter for property: (bool) BoundaryStatus
         Returns the boundary status toggle on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @BoundaryStatus.setter
    def BoundaryStatus(self, boundaryStatusToggle: bool):
        """
        Setter for property: (bool) BoundaryStatus
         Returns the boundary status toggle on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Centerlines(self) -> bool:
        """
        Getter for property: (bool) Centerlines
         Returns the centerlines toggle on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @Centerlines.setter
    def Centerlines(self, centerlinesToggle: bool):
        """
        Setter for property: (bool) Centerlines
         Returns the centerlines toggle on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def DisplayId(self) -> NXOpen.Preferences.GeneralDisplayIdOption:
        """
        Getter for property: ( NXOpen.Preferences.GeneralDisplayIdOption) DisplayId
         Returns the display identifier option on the GENERAL tab of the View Style Dialog, it controls whether
                    the orientation or the name of the view is displayed in the graphic window
                  
            
         
        """
        pass
    @DisplayId.setter
    def DisplayId(self, option: NXOpen.Preferences.GeneralDisplayIdOption):
        """
        Setter for property: ( NXOpen.Preferences.GeneralDisplayIdOption) DisplayId
         Returns the display identifier option on the GENERAL tab of the View Style Dialog, it controls whether
                    the orientation or the name of the view is displayed in the graphic window
                  
            
         
        """
        pass
    @property
    def ExtractedEdges(self) -> NXOpen.Preferences.GeneralExtractedEdgesOption:
        """
        Getter for property: ( NXOpen.Preferences.GeneralExtractedEdgesOption) ExtractedEdges
         Returns the extracted edges option on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @ExtractedEdges.setter
    def ExtractedEdges(self, extractedEdgesOption: NXOpen.Preferences.GeneralExtractedEdgesOption):
        """
        Setter for property: ( NXOpen.Preferences.GeneralExtractedEdgesOption) ExtractedEdges
         Returns the extracted edges option on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def FramebarHorizontal(self) -> bool:
        """
        Getter for property: (bool) FramebarHorizontal
         Returns the horizontal framebar toggle on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @FramebarHorizontal.setter
    def FramebarHorizontal(self, framebarHorizontalToggle: bool):
        """
        Setter for property: (bool) FramebarHorizontal
         Returns the horizontal framebar toggle on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def FramebarVertical(self) -> bool:
        """
        Getter for property: (bool) FramebarVertical
         Returns the vertical framebar toggle on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @FramebarVertical.setter
    def FramebarVertical(self, framebarVerticalToggle: bool):
        """
        Setter for property: (bool) FramebarVertical
         Returns the vertical framebar toggle on the GENERAL tab of the View Style Dialog   
            
         
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
    def LockmethodView(self) -> NXOpen.Preferences.GeneralViewLockmethodOption:
        """
        Getter for property: ( NXOpen.Preferences.GeneralViewLockmethodOption) LockmethodView
         Returns the lock method setting on the Configuration tab of the View Style Dialog   
            
         
        """
        pass
    @LockmethodView.setter
    def LockmethodView(self, lockMethodView: NXOpen.Preferences.GeneralViewLockmethodOption):
        """
        Setter for property: ( NXOpen.Preferences.GeneralViewLockmethodOption) LockmethodView
         Returns the lock method setting on the Configuration tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Reference(self) -> bool:
        """
        Getter for property: (bool) Reference
         Returns the reference toggle on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @Reference.setter
    def Reference(self, referenceToggle: bool):
        """
        Setter for property: (bool) Reference
         Returns the reference toggle on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Scale(self) -> ViewScaleBuilder:
        """
        Getter for property: ( ViewScaleBuilder NXOpen.) Scale
         Returns the scale definition on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def ScaleLabel(self) -> bool:
        """
        Getter for property: (bool) ScaleLabel
         Returns the scale label toggle on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @ScaleLabel.setter
    def ScaleLabel(self, scaleLabelToggle: bool):
        """
        Setter for property: (bool) ScaleLabel
         Returns the scale label toggle on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Silhouettes(self) -> bool:
        """
        Getter for property: (bool) Silhouettes
         Returns the silhouettes toggle on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @Silhouettes.setter
    def Silhouettes(self, silhouettesToggle: bool):
        """
        Setter for property: (bool) Silhouettes
         Returns the silhouettes toggle on the GENERAL tab of the View Style Dialog   
            
         
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
    def Tolerance(self) -> NXOpen.Preferences.GeneralToleranceOption:
        """
        Getter for property: ( NXOpen.Preferences.GeneralToleranceOption) Tolerance
         Returns the tolerance option on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @Tolerance.setter
    def Tolerance(self, toleranceOption: NXOpen.Preferences.GeneralToleranceOption):
        """
        Setter for property: ( NXOpen.Preferences.GeneralToleranceOption) Tolerance
         Returns the tolerance option on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def ToleranceValue(self) -> float:
        """
        Getter for property: (float) ToleranceValue
         Returns the tolerance value on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @ToleranceValue.setter
    def ToleranceValue(self, toleranceValue: float):
        """
        Setter for property: (float) ToleranceValue
         Returns the tolerance value on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def UVGrid(self) -> bool:
        """
        Getter for property: (bool) UVGrid
         Returns the uvgrid toggle on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @UVGrid.setter
    def UVGrid(self, uVGridToggle: bool):
        """
        Setter for property: (bool) UVGrid
         Returns the uvgrid toggle on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def ViewLabel(self) -> bool:
        """
        Getter for property: (bool) ViewLabel
         Returns the view label toggle on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @ViewLabel.setter
    def ViewLabel(self, viewLabelToggle: bool):
        """
        Setter for property: (bool) ViewLabel
         Returns the view label toggle on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def ViewQuality(self) -> NXOpen.Preferences.GeneralViewQualityOption:
        """
        Getter for property: ( NXOpen.Preferences.GeneralViewQualityOption) ViewQuality
         Returns the view quality option on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @ViewQuality.setter
    def ViewQuality(self, viewQualityOption: NXOpen.Preferences.GeneralViewQualityOption):
        """
        Setter for property: ( NXOpen.Preferences.GeneralViewQualityOption) ViewQuality
         Returns the view quality option on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def ViewRepresentation(self) -> NXOpen.Preferences.GeneralViewRepresentationOption:
        """
        Getter for property: ( NXOpen.Preferences.GeneralViewRepresentationOption) ViewRepresentation
         Returns the view representation option on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @ViewRepresentation.setter
    def ViewRepresentation(self, viewRepresentation: NXOpen.Preferences.GeneralViewRepresentationOption):
        """
        Setter for property: ( NXOpen.Preferences.GeneralViewRepresentationOption) ViewRepresentation
         Returns the view representation option on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def ViewStyleFrameBar(self) -> ViewStyleFrameBarBuilder:
        """
        Getter for property: ( ViewStyleFrameBarBuilder NXOpen.) ViewStyleFrameBar
         Returns the frame bar builder   
            
         
        """
        pass
    @property
    def WireframeColorSource(self) -> NXOpen.Preferences.GeneralWireframeColorSourceOption:
        """
        Getter for property: ( NXOpen.Preferences.GeneralWireframeColorSourceOption) WireframeColorSource
         Returns the wireframe color source option on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    @WireframeColorSource.setter
    def WireframeColorSource(self, wireframeColorSourceOption: NXOpen.Preferences.GeneralWireframeColorSourceOption):
        """
        Setter for property: ( NXOpen.Preferences.GeneralWireframeColorSourceOption) WireframeColorSource
         Returns the wireframe color source option on the GENERAL tab of the View Style Dialog   
            
         
        """
        pass
    def GetRenderSet(self) -> List[RenderSet]:
        """
         Gets the render sets on the GENERAL tab of the View Style Dialog 
         Returns renderSets ( RenderSet List[NXOpe):  Returns the render sets that are on the general sub-builder .
        """
        pass
    def SetRenderSet(self, renderSets: List[RenderSet]) -> None:
        """
         Sets the render sets on the GENERAL tab of the View Style Dialog 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
import NXOpen.Preferences
class ViewStyleHiddenLinesBuilder(NXOpen.TaggedObject): 
    """ Represents the HIDDEN LINES tab on the View Style Dialog (Drawings.ViewStyleHiddenLinesBuilder)
    """
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) Color
         Returns the color on the HIDDEN LINES tab of the View Style Dialog   
            
         
        """
        pass
    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) Color
         Returns the color on the HIDDEN LINES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def EdgesHiddenByEdges(self) -> bool:
        """
        Getter for property: (bool) EdgesHiddenByEdges
         Returns the edges hidden by edges toggle on the HIDDEN LINES tab of the View Style Dialog   
            
         
        """
        pass
    @EdgesHiddenByEdges.setter
    def EdgesHiddenByEdges(self, edgesHiddenByEdgesToggle: bool):
        """
        Setter for property: (bool) EdgesHiddenByEdges
         Returns the edges hidden by edges toggle on the HIDDEN LINES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Font(self) -> NXOpen.Preferences.Font:
        """
        Getter for property: ( NXOpen.Preferences.Font) Font
         Returns the font on the HIDDEN LINES tab of the View Style Dialog   
            
         
        """
        pass
    @Font.setter
    def Font(self, font: NXOpen.Preferences.Font):
        """
        Setter for property: ( NXOpen.Preferences.Font) Font
         Returns the font on the HIDDEN LINES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def HiddenLine(self) -> bool:
        """
        Getter for property: (bool) HiddenLine
         Returns the hidden line toggle on the HIDDEN LINES tab of the View Style Dialog   
            
         
        """
        pass
    @HiddenLine.setter
    def HiddenLine(self, hiddenLineToggle: bool):
        """
        Setter for property: (bool) HiddenLine
         Returns the hidden line toggle on the HIDDEN LINES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def IncludeModelCurves(self) -> bool:
        """
        Getter for property: (bool) IncludeModelCurves
         Returns the include model curves toggle on the HIDDEN LINES tab of the View Style Dialog   
            
         
        """
        pass
    @IncludeModelCurves.setter
    def IncludeModelCurves(self, includeModelCurvesToggle: bool):
        """
        Setter for property: (bool) IncludeModelCurves
         Returns the include model curves toggle on the HIDDEN LINES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def IncludeModelCurvesOption(self) -> NXOpen.Preferences.IncludeModelCurvesOption:
        """
        Getter for property: ( NXOpen.Preferences.IncludeModelCurvesOption) IncludeModelCurvesOption
         Returns the include model curves option on the HIDDEN LINES tab of the View Style Dialog   
            
         
        """
        pass
    @IncludeModelCurvesOption.setter
    def IncludeModelCurvesOption(self, includeModelCurvesOptionData: NXOpen.Preferences.IncludeModelCurvesOption):
        """
        Setter for property: ( NXOpen.Preferences.IncludeModelCurvesOption) IncludeModelCurvesOption
         Returns the include model curves option on the HIDDEN LINES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def InterferingSolids(self) -> NXOpen.Preferences.HiddenLineInterferingSolidsOption:
        """
        Getter for property: ( NXOpen.Preferences.HiddenLineInterferingSolidsOption) InterferingSolids
         Returns the interfering solids toggle on the HIDDEN LINES tab of the View Style Dialog   
            
         
        """
        pass
    @InterferingSolids.setter
    def InterferingSolids(self, interferingSolidsOption: NXOpen.Preferences.HiddenLineInterferingSolidsOption):
        """
        Setter for property: ( NXOpen.Preferences.HiddenLineInterferingSolidsOption) InterferingSolids
         Returns the interfering solids toggle on the HIDDEN LINES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def ReferenceEdgesOnly(self) -> bool:
        """
        Getter for property: (bool) ReferenceEdgesOnly
         Returns the reference edges only toggle on the HIDDEN LINES tab of the View Style Dialog   
            
         
        """
        pass
    @ReferenceEdgesOnly.setter
    def ReferenceEdgesOnly(self, referenceEdgesOnlyToggle: bool):
        """
        Setter for property: (bool) ReferenceEdgesOnly
         Returns the reference edges only toggle on the HIDDEN LINES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def SelfHidden(self) -> bool:
        """
        Getter for property: (bool) SelfHidden
         Returns the self hidden toggle on the HIDDEN LINES tab of the View Style Dialog   
            
         
        """
        pass
    @SelfHidden.setter
    def SelfHidden(self, selfHiddenToggle: bool):
        """
        Setter for property: (bool) SelfHidden
         Returns the self hidden toggle on the HIDDEN LINES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def SmallFeature(self) -> NXOpen.Preferences.HiddenLineSmallFeatureOption:
        """
        Getter for property: ( NXOpen.Preferences.HiddenLineSmallFeatureOption) SmallFeature
         Returns the small feature option on the HIDDEN LINES tab of the View Style Dialog   
            
         
        """
        pass
    @SmallFeature.setter
    def SmallFeature(self, smallFeatureOption: NXOpen.Preferences.HiddenLineSmallFeatureOption):
        """
        Setter for property: ( NXOpen.Preferences.HiddenLineSmallFeatureOption) SmallFeature
         Returns the small feature option on the HIDDEN LINES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def SmallFeaturesTolerance(self) -> float:
        """
        Getter for property: (float) SmallFeaturesTolerance
         Returns the small features tolerance on the HIDDEN LINES tab of the View Style Dialog   
            
         
        """
        pass
    @SmallFeaturesTolerance.setter
    def SmallFeaturesTolerance(self, smallFeaturesTolerance: float):
        """
        Setter for property: (float) SmallFeaturesTolerance
         Returns the small features tolerance on the HIDDEN LINES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Width(self) -> NXOpen.Preferences.Width:
        """
        Getter for property: ( NXOpen.Preferences.Width) Width
         Returns the width on the HIDDEN LINES tab of the View Style Dialog   
            
         
        """
        pass
    @Width.setter
    def Width(self, width: NXOpen.Preferences.Width):
        """
        Setter for property: ( NXOpen.Preferences.Width) Width
         Returns the width on the HIDDEN LINES tab of the View Style Dialog   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
import NXOpen.Preferences
class ViewStyleInheritPmiBuilder(NXOpen.TaggedObject): 
    """ Represents the INHERIT PMI tab on the View Style Dialog (Drawings.ViewStyleInheritPmiBuilder)
    """
    @property
    def CrosshatchPmiLwsv(self) -> bool:
        """
        Getter for property: (bool) CrosshatchPmiLwsv
         Returns the cross-hatch setting for the current inherited PMI Lightweight Section View   
            
         
        """
        pass
    @CrosshatchPmiLwsv.setter
    def CrosshatchPmiLwsv(self, crosshatch: bool):
        """
        Setter for property: (bool) CrosshatchPmiLwsv
         Returns the cross-hatch setting for the current inherited PMI Lightweight Section View   
            
         
        """
        pass
    @property
    def Gdt(self) -> NXOpen.Preferences.GdtOption:
        """
        Getter for property: ( NXOpen.Preferences.GdtOption) Gdt
         Returns the gdt option on the INHERIT PMI tab of the View Style Dialog   
            
         
        """
        pass
    @Gdt.setter
    def Gdt(self, gdtOption: NXOpen.Preferences.GdtOption):
        """
        Setter for property: ( NXOpen.Preferences.GdtOption) Gdt
         Returns the gdt option on the INHERIT PMI tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Pmi(self) -> NXOpen.Preferences.PmiOption:
        """
        Getter for property: ( NXOpen.Preferences.PmiOption) Pmi
         Returns the pmi option on the INHERIT PMI tab of the View Style Dialog   
            
         
        """
        pass
    @Pmi.setter
    def Pmi(self, pmiOption: NXOpen.Preferences.PmiOption):
        """
        Setter for property: ( NXOpen.Preferences.PmiOption) Pmi
         Returns the pmi option on the INHERIT PMI tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def PmiFromRevolved(self) -> bool:
        """
        Getter for property: (bool) PmiFromRevolved
         Returns the 'Show PMI Dimensions from Revolved Sketches' toggle on the INHERIT PMI tab of the View Style Dialog   
            
         
        """
        pass
    @PmiFromRevolved.setter
    def PmiFromRevolved(self, pmiFromRevolvedToggle: bool):
        """
        Setter for property: (bool) PmiFromRevolved
         Returns the 'Show PMI Dimensions from Revolved Sketches' toggle on the INHERIT PMI tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def PmiToDrawing(self) -> bool:
        """
        Getter for property: (bool) PmiToDrawing
         Returns the 'pmi to drawing' toggle on the INHERIT PMI tab of the View Style Dialog   
            
         
        """
        pass
    @PmiToDrawing.setter
    def PmiToDrawing(self, pmiToDrawingToggle: bool):
        """
        Setter for property: (bool) PmiToDrawing
         Returns the 'pmi to drawing' toggle on the INHERIT PMI tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def PmiTypeMask(self) -> int:
        """
        Getter for property: (int) PmiTypeMask
         Returns the type mask on the INHERIT PMI tab of the View Style Dialog   
            
         
        """
        pass
    @PmiTypeMask.setter
    def PmiTypeMask(self, pmiTypeMask: int):
        """
        Setter for property: (int) PmiTypeMask
         Returns the type mask on the INHERIT PMI tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def ReferenceSetBehavior(self) -> NXOpen.Preferences.ReferenceSetBehavior:
        """
        Getter for property: ( NXOpen.Preferences.ReferenceSetBehavior) ReferenceSetBehavior
         Returns the reference set option   
            
         
        """
        pass
    @ReferenceSetBehavior.setter
    def ReferenceSetBehavior(self, pmiOption: NXOpen.Preferences.ReferenceSetBehavior):
        """
        Setter for property: ( NXOpen.Preferences.ReferenceSetBehavior) ReferenceSetBehavior
         Returns the reference set option   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ViewStyleOrientationBuilder(NXOpen.TaggedObject): 
    """ Represents the ORIENTATION tab on the View Style Dialog (Drawings.ViewStyleOrientationBuilder)
    """
    @property
    def HingeLine(self) -> HingeLineBuilder:
        """
        Getter for property: ( HingeLineBuilder NXOpen.) HingeLine
         Returns the view hinge line definition on the ORIENTATION tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Ovt(self) -> OvtBuilder:
        """
        Getter for property: ( OvtBuilder NXOpen.) Ovt
         Returns the view orientation definition on the ORIENTATION tab of the View Style Dialog   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ViewStylePerspectiveBuilder(NXOpen.TaggedObject): 
    """ Represents the PERSPECTIVE tab on the View Style Dialog (Drawings.ViewStylePerspectiveBuilder)
    """
    @property
    def BackClip(self) -> bool:
        """
        Getter for property: (bool) BackClip
         Returns the back clip toggle on the PERSPECTIVE tab of the View Style Dialog   
            
         
        """
        pass
    @BackClip.setter
    def BackClip(self, backClipToggle: bool):
        """
        Setter for property: (bool) BackClip
         Returns the back clip toggle on the PERSPECTIVE tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def BackClipDistance(self) -> float:
        """
        Getter for property: (float) BackClipDistance
         Returns the back clip distance data on the PERSPECTIVE tab of the View Style Dialog   
            
         
        """
        pass
    @BackClipDistance.setter
    def BackClipDistance(self, backClipDistanceData: float):
        """
        Setter for property: (float) BackClipDistance
         Returns the back clip distance data on the PERSPECTIVE tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def FrontClip(self) -> bool:
        """
        Getter for property: (bool) FrontClip
         Returns the front clip toggle on the PERSPECTIVE tab of the View Style Dialog   
            
         
        """
        pass
    @FrontClip.setter
    def FrontClip(self, frontClipToggle: bool):
        """
        Setter for property: (bool) FrontClip
         Returns the front clip toggle on the PERSPECTIVE tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def FrontClipDistance(self) -> float:
        """
        Getter for property: (float) FrontClipDistance
         Returns the front clip distance data on the PERSPECTIVE tab of the View Style Dialog   
            
         
        """
        pass
    @FrontClipDistance.setter
    def FrontClipDistance(self, frontClipDistanceData: float):
        """
        Setter for property: (float) FrontClipDistance
         Returns the front clip distance data on the PERSPECTIVE tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Perspective(self) -> bool:
        """
        Getter for property: (bool) Perspective
         Returns the perspective toggle on the PERSPECTIVE tab of the View Style Dialog   
            
         
        """
        pass
    @Perspective.setter
    def Perspective(self, perspectiveToggle: bool):
        """
        Setter for property: (bool) Perspective
         Returns the perspective toggle on the PERSPECTIVE tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def PerspectiveDistance(self) -> float:
        """
        Getter for property: (float) PerspectiveDistance
         Returns the perspective distance data on the PERSPECTIVE tab of the View Style Dialog   
            
         
        """
        pass
    @PerspectiveDistance.setter
    def PerspectiveDistance(self, perspectiveDistanceData: float):
        """
        Setter for property: (float) PerspectiveDistance
         Returns the perspective distance data on the PERSPECTIVE tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def ViewOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) ViewOrigin
         Returns the perspective view origin on the PERSPECTIVE tab of the View Style Dialog   
            
         
        """
        pass
    @ViewOrigin.setter
    def ViewOrigin(self, viewOrigin: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) ViewOrigin
         Returns the perspective view origin on the PERSPECTIVE tab of the View Style Dialog   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ViewStyleProjectedBuilder(NXOpen.TaggedObject): 
    """ Represents the PROJECTED tab on the View Style Dialog (Drawings.ViewStyleProjectedBuilder)
    """
    @property
    def Align(self) -> bool:
        """
        Getter for property: (bool) Align
         Returns the projected view style align toggle on the PROJECTED tab of the View Style Dialog   
            
         
        """
        pass
    @Align.setter
    def Align(self, alignToggle: bool):
        """
        Setter for property: (bool) Align
         Returns the projected view style align toggle on the PROJECTED tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Gdt(self) -> bool:
        """
        Getter for property: (bool) Gdt
         Returns the projected view style gdt toggle on the PROJECTED tab of the View Style Dialog   
            
         
        """
        pass
    @Gdt.setter
    def Gdt(self, gdtToggle: bool):
        """
        Setter for property: (bool) Gdt
         Returns the projected view style gdt toggle on the PROJECTED tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Offset(self) -> bool:
        """
        Getter for property: (bool) Offset
         Returns the projected view style offset toggle on the PROJECTED tab of the View Style Dialog   
            
         
        """
        pass
    @Offset.setter
    def Offset(self, offsetToggle: bool):
        """
        Setter for property: (bool) Offset
         Returns the projected view style offset toggle on the PROJECTED tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Orient(self) -> bool:
        """
        Getter for property: (bool) Orient
         Returns the projected view style orient toggle on the PROJECTED tab of the View Style Dialog   
            
         
        """
        pass
    @Orient.setter
    def Orient(self, orientToggle: bool):
        """
        Setter for property: (bool) Orient
         Returns the projected view style orient toggle on the PROJECTED tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Scale(self) -> bool:
        """
        Getter for property: (bool) Scale
         Returns the projected view style scale toggle on the PROJECTED tab of the View Style Dialog   
            
         
        """
        pass
    @Scale.setter
    def Scale(self, scaleToggle: bool):
        """
        Setter for property: (bool) Scale
         Returns the projected view style scale toggle on the PROJECTED tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Sheet(self) -> bool:
        """
        Getter for property: (bool) Sheet
         Returns the projected view style sheet toggle on the PROJECTED tab of the View Style Dialog   
            
         
        """
        pass
    @Sheet.setter
    def Sheet(self, sheetToggle: bool):
        """
        Setter for property: (bool) Sheet
         Returns the projected view style sheet toggle on the PROJECTED tab of the View Style Dialog   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ViewStyleSecondaryComponentsBuilder(NXOpen.TaggedObject): 
    """ Represents the Secondary Geometry tab on the View Style Dialog (Drawings.ViewStyleHiddenLinesBuilder)
    """
    @property
    def PrimaryHiddenBySecondaryCFW(self) -> VisibleAndHiddenLinesColorFontWidthBuilder:
        """
        Getter for property: ( VisibleAndHiddenLinesColorFontWidthBuilder NXOpen.) PrimaryHiddenBySecondaryCFW
         Returns the visible and hidden lines color, font, and width of primary geometry that is hidden by secondary geometry.  
             
         
        """
        pass
    @property
    def ProcessPrimaryHiddenBySecondary(self) -> bool:
        """
        Getter for property: (bool) ProcessPrimaryHiddenBySecondary
         Returns the Primary Geometry Hidden by Secondary Geometry toggle on Secondary Geometry tab of View Style Dialog.  
           
                If true, the primary geometry display properties are processed with respect to the secondary geometry.  
         
        """
        pass
    @ProcessPrimaryHiddenBySecondary.setter
    def ProcessPrimaryHiddenBySecondary(self, processPrimaryHiddenBySecondary: bool):
        """
        Setter for property: (bool) ProcessPrimaryHiddenBySecondary
         Returns the Primary Geometry Hidden by Secondary Geometry toggle on Secondary Geometry tab of View Style Dialog.  
           
                If true, the primary geometry display properties are processed with respect to the secondary geometry.  
         
        """
        pass
    @property
    def ProcessSecondaryComponents(self) -> bool:
        """
        Getter for property: (bool) ProcessSecondaryComponents
         Returns the Secondary Geometry toggle on Secondary Geometry tab of View Style Dialog.  
           
                If true, the secondary geometry display properties are processed separately from the primary geometry.  
         
        """
        pass
    @ProcessSecondaryComponents.setter
    def ProcessSecondaryComponents(self, processSecondaryComponents: bool):
        """
        Setter for property: (bool) ProcessSecondaryComponents
         Returns the Secondary Geometry toggle on Secondary Geometry tab of View Style Dialog.  
           
                If true, the secondary geometry display properties are processed separately from the primary geometry.  
         
        """
        pass
    @property
    def ProcessSecondaryHiddenByPrimary(self) -> bool:
        """
        Getter for property: (bool) ProcessSecondaryHiddenByPrimary
         Returns the Secondary Geometry Hidden by Primary Geometry toggle on Secondary Geometry tab of View Style Dialog.  
           
                If true, the secondary geometry display properties are processed with respect to the primary geometry.  
         
        """
        pass
    @ProcessSecondaryHiddenByPrimary.setter
    def ProcessSecondaryHiddenByPrimary(self, processSecondaryHiddenByPrimary: bool):
        """
        Setter for property: (bool) ProcessSecondaryHiddenByPrimary
         Returns the Secondary Geometry Hidden by Primary Geometry toggle on Secondary Geometry tab of View Style Dialog.  
           
                If true, the secondary geometry display properties are processed with respect to the primary geometry.  
         
        """
        pass
    @property
    def SecondaryComponentsCFW(self) -> VisibleAndHiddenLinesColorFontWidthBuilder:
        """
        Getter for property: ( VisibleAndHiddenLinesColorFontWidthBuilder NXOpen.) SecondaryComponentsCFW
         Returns the visible and hidden lines color, font, and width of secondary geometry.  
            
         
        """
        pass
    @property
    def SecondaryHiddenByPrimaryCFW(self) -> VisibleAndHiddenLinesColorFontWidthBuilder:
        """
        Getter for property: ( VisibleAndHiddenLinesColorFontWidthBuilder NXOpen.) SecondaryHiddenByPrimaryCFW
         Returns the visible and hidden lines color, font, and width of secondary geometry that is hidden by primary geometry.  
             
         
        """
        pass
    @property
    def ShowSmoothEdges(self) -> bool:
        """
        Getter for property: (bool) ShowSmoothEdges
         Returns the Show Smooth Edges toggle on Secondary Geometry tab of View Style Dialog.  
           
                If true, the smooth edges are displayed for secondary geometry.  
         
        """
        pass
    @ShowSmoothEdges.setter
    def ShowSmoothEdges(self, showSmoothEdges: bool):
        """
        Setter for property: (bool) ShowSmoothEdges
         Returns the Show Smooth Edges toggle on Secondary Geometry tab of View Style Dialog.  
           
                If true, the smooth edges are displayed for secondary geometry.  
         
        """
        pass
    @property
    def ShowVirtualIntersections(self) -> bool:
        """
        Getter for property: (bool) ShowVirtualIntersections
         Returns the Show Virtual Intersections toggle on Secondary Geometry tab of View Style Dialog.  
          
                If true, the virtual intersection lines are displayed for secondary geometry.  
         
        """
        pass
    @ShowVirtualIntersections.setter
    def ShowVirtualIntersections(self, showVirtualIntersections: bool):
        """
        Setter for property: (bool) ShowVirtualIntersections
         Returns the Show Virtual Intersections toggle on Secondary Geometry tab of View Style Dialog.  
          
                If true, the virtual intersection lines are displayed for secondary geometry.  
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ViewStyleSectionBuilder(NXOpen.TaggedObject): 
    """ Represents the SECTION tab on the View Style Dialog (Drawings.ViewStyleSectionBuilder)
    """
    @property
    def AdjacencyToleranceData(self) -> float:
        """
        Getter for property: (float) AdjacencyToleranceData
         Returns the adjacency tolerance on the SECTION tab of the View Style Dialog   
            
         
        """
        pass
    @AdjacencyToleranceData.setter
    def AdjacencyToleranceData(self, adjacencyToleranceData: float):
        """
        Setter for property: (float) AdjacencyToleranceData
         Returns the adjacency tolerance on the SECTION tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def AssemblyTolerance(self) -> bool:
        """
        Getter for property: (bool) AssemblyTolerance
         Returns the assembly tolerance toggle on the SECTION tab of the View Style Dialog   
            
         
        """
        pass
    @AssemblyTolerance.setter
    def AssemblyTolerance(self, assemblyToleranceToggle: bool):
        """
        Setter for property: (bool) AssemblyTolerance
         Returns the assembly tolerance toggle on the SECTION tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Background(self) -> bool:
        """
        Getter for property: (bool) Background
         Returns the background toggle on the SECTION tab of the View Style Dialog   
            
         
        """
        pass
    @Background.setter
    def Background(self, backgroundToggle: bool):
        """
        Setter for property: (bool) Background
         Returns the background toggle on the SECTION tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Bendlines(self) -> bool:
        """
        Getter for property: (bool) Bendlines
         Returns the bendlines toggle on the SECTION tab of the View Style Dialog   
            
         
        """
        pass
    @Bendlines.setter
    def Bendlines(self, bendlinesToggle: bool):
        """
        Setter for property: (bool) Bendlines
         Returns the bendlines toggle on the SECTION tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Crosshatch(self) -> bool:
        """
        Getter for property: (bool) Crosshatch
         Returns the crosshatch toggle on the SECTION tab of the View Style Dialog   
            
         
        """
        pass
    @Crosshatch.setter
    def Crosshatch(self, crosshatchToggle: bool):
        """
        Setter for property: (bool) Crosshatch
         Returns the crosshatch toggle on the SECTION tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def DisplaySectionLine(self) -> bool:
        """
        Getter for property: (bool) DisplaySectionLine
         Returns the display section line toggle on the SECTION tab of the View Style Dialog   
            
         
        """
        pass
    @DisplaySectionLine.setter
    def DisplaySectionLine(self, displaySectionLine: bool):
        """
        Setter for property: (bool) DisplaySectionLine
         Returns the display section line toggle on the SECTION tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Foreground(self) -> bool:
        """
        Getter for property: (bool) Foreground
         Returns the foreground toggle on the SECTION tab of the View Style Dialog   
            
         
        """
        pass
    @Foreground.setter
    def Foreground(self, foregroundToggle: bool):
        """
        Setter for property: (bool) Foreground
         Returns the foreground toggle on the SECTION tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def HiddenLineHatching(self) -> bool:
        """
        Getter for property: (bool) HiddenLineHatching
         Returns the hidden line hatching toggle on the SECTION tab of the View Style Dialog   
            
         
        """
        pass
    @HiddenLineHatching.setter
    def HiddenLineHatching(self, hiddenLineHatchingToggle: bool):
        """
        Setter for property: (bool) HiddenLineHatching
         Returns the hidden line hatching toggle on the SECTION tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def RestrictCrosshatchAngle(self) -> bool:
        """
        Getter for property: (bool) RestrictCrosshatchAngle
         Returns the restrict crosshatch angle toggle on the SECTION tab of the View Style Dialog   
            
         
        """
        pass
    @RestrictCrosshatchAngle.setter
    def RestrictCrosshatchAngle(self, restrictCrosshatchAngleToggle: bool):
        """
        Setter for property: (bool) RestrictCrosshatchAngle
         Returns the restrict crosshatch angle toggle on the SECTION tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def SheetBodies(self) -> bool:
        """
        Getter for property: (bool) SheetBodies
         Returns the sheet bodies toggle on the SECTION tab of the View Style Dialog   
            
         
        """
        pass
    @SheetBodies.setter
    def SheetBodies(self, sheetBodiesToggle: bool):
        """
        Setter for property: (bool) SheetBodies
         Returns the sheet bodies toggle on the SECTION tab of the View Style Dialog   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ViewStyleSectionConstraintsBuilder(NXOpen.TaggedObject): 
    """ Represents the SECTION CONSTRAINTS tab on the View Style Dialog (Drawings.ViewStyleSectionConstraintsBuilder)
    """
    @property
    def Align(self) -> bool:
        """
        Getter for property: (bool) Align
         Returns the align toggle on the SECTION CONSTRAINTS tab of the View Style Dialog   
            
         
        """
        pass
    @Align.setter
    def Align(self, alignToggle: bool):
        """
        Setter for property: (bool) Align
         Returns the align toggle on the SECTION CONSTRAINTS tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Offset(self) -> bool:
        """
        Getter for property: (bool) Offset
         Returns the offset toggle on the SECTION CONSTRAINTS tab of the View Style Dialog   
            
         
        """
        pass
    @Offset.setter
    def Offset(self, offsetToggle: bool):
        """
        Setter for property: (bool) Offset
         Returns the offset toggle on the SECTION CONSTRAINTS tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Orient(self) -> bool:
        """
        Getter for property: (bool) Orient
         Returns the orient toggle on the SECTION CONSTRAINTS tab of the View Style Dialog   
            
         
        """
        pass
    @Orient.setter
    def Orient(self, orientToggle: bool):
        """
        Setter for property: (bool) Orient
         Returns the orient toggle on the SECTION CONSTRAINTS tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Scale(self) -> bool:
        """
        Getter for property: (bool) Scale
         Returns the scale toggle on the SECTION CONSTRAINTS tab of the View Style Dialog   
            
         
        """
        pass
    @Scale.setter
    def Scale(self, scaleToggle: bool):
        """
        Setter for property: (bool) Scale
         Returns the scale toggle on the SECTION CONSTRAINTS tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Sheet(self) -> bool:
        """
        Getter for property: (bool) Sheet
         Returns the sheet toggle on the SECTION CONSTRAINTS tab of the View Style Dialog   
            
         
        """
        pass
    @Sheet.setter
    def Sheet(self, sheetToggle: bool):
        """
        Setter for property: (bool) Sheet
         Returns the sheet toggle on the SECTION CONSTRAINTS tab of the View Style Dialog   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
import NXOpen.Preferences
class ViewStyleShadingBuilder(NXOpen.TaggedObject): 
    """ Represents the SHADING tab on the View Style Dialog (Drawings.ViewStyleShadingBuilder)
    """
    @property
    def AngleTolerance(self) -> float:
        """
        Getter for property: (float) AngleTolerance
         Returns the angle tolerance data on the SHADING tab of the View Style Dialog   
            
         
        """
        pass
    @AngleTolerance.setter
    def AngleTolerance(self, angleToleranceData: float):
        """
        Setter for property: (float) AngleTolerance
         Returns the angle tolerance data on the SHADING tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def CutFaceColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) CutFaceColor
         Returns the cut face color on the SHADING tab of the View Style Dialog   
            
         
        """
        pass
    @CutFaceColor.setter
    def CutFaceColor(self, cutFaceColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) CutFaceColor
         Returns the cut face color on the SHADING tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def EdgeTolerance(self) -> float:
        """
        Getter for property: (float) EdgeTolerance
         Returns the edge tolerance data on the SHADING tab of the View Style Dialog   
            
         
        """
        pass
    @EdgeTolerance.setter
    def EdgeTolerance(self, edgeToleranceData: float):
        """
        Setter for property: (float) EdgeTolerance
         Returns the edge tolerance data on the SHADING tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def FaceTolerance(self) -> float:
        """
        Getter for property: (float) FaceTolerance
         Returns the face tolerance data on the SHADING tab of the View Style Dialog   
            
         
        """
        pass
    @FaceTolerance.setter
    def FaceTolerance(self, faceToleranceData: float):
        """
        Setter for property: (float) FaceTolerance
         Returns the face tolerance data on the SHADING tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def HiddenWireframeColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) HiddenWireframeColor
         Returns the hidden wireframe color on the SHADING tab of the View Style Dialog   
            
         
        """
        pass
    @HiddenWireframeColor.setter
    def HiddenWireframeColor(self, hiddenWireframeColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) HiddenWireframeColor
         Returns the hidden wireframe color on the SHADING tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def RenderingStyle(self) -> NXOpen.Preferences.ShadingRenderingStyleOption:
        """
        Getter for property: ( NXOpen.Preferences.ShadingRenderingStyleOption) RenderingStyle
         Returns the rendering style option on the SHADING tab of the View Style Dialog   
            
         
        """
        pass
    @RenderingStyle.setter
    def RenderingStyle(self, renderingStyleOption: NXOpen.Preferences.ShadingRenderingStyleOption):
        """
        Setter for property: ( NXOpen.Preferences.ShadingRenderingStyleOption) RenderingStyle
         Returns the rendering style option on the SHADING tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def ShadeTolerance(self) -> NXOpen.Preferences.ShadingToleranceOption:
        """
        Getter for property: ( NXOpen.Preferences.ShadingToleranceOption) ShadeTolerance
         Returns the shade tolerance option on the SHADING tab of the View Style Dialog   
            
         
        """
        pass
    @ShadeTolerance.setter
    def ShadeTolerance(self, shadeToleranceOption: NXOpen.Preferences.ShadingToleranceOption):
        """
        Setter for property: ( NXOpen.Preferences.ShadingToleranceOption) ShadeTolerance
         Returns the shade tolerance option on the SHADING tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def ShininessScale(self) -> float:
        """
        Getter for property: (float) ShininessScale
         Returns the shininess scale data on the SHADING tab of the View Style Dialog   
            
         
        """
        pass
    @ShininessScale.setter
    def ShininessScale(self, shininessScaleData: float):
        """
        Setter for property: (float) ShininessScale
         Returns the shininess scale data on the SHADING tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def TwoSidedLight(self) -> bool:
        """
        Getter for property: (bool) TwoSidedLight
         Returns the two sided light toggle on the SHADING tab of the View Style Dialog   
            
         
        """
        pass
    @TwoSidedLight.setter
    def TwoSidedLight(self, twoSidedLightToggle: bool):
        """
        Setter for property: (bool) TwoSidedLight
         Returns the two sided light toggle on the SHADING tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def VisibleWireframeColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) VisibleWireframeColor
         Returns the visible wireframe color on the SHADING tab of the View Style Dialog   
            
         
        """
        pass
    @VisibleWireframeColor.setter
    def VisibleWireframeColor(self, visibleWireframeColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) VisibleWireframeColor
         Returns the visible wireframe color on the SHADING tab of the View Style Dialog   
            
         
        """
        pass
import NXOpen
class ViewStyleShipbuildingLinesBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[ViewStyleShipbuildingLinesBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: ViewStyleShipbuildingLinesBuilder) -> None:
        """
         Appends an object to the list
            
        """
        pass
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
               not change, but the item at this index is set to NULL.
            
        """
        pass
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, obj: ViewStyleShipbuildingLinesBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: ViewStyleShipbuildingLinesBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: ViewStyleShipbuildingLinesBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> ViewStyleShipbuildingLinesBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( ViewStyleShipbuildingLinesBuilder NXOpen.):  object found at input index .
        """
        pass
    def GetContents(self) -> List[ViewStyleShipbuildingLinesBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( ViewStyleShipbuildingLinesBuilder List[NXOpe):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: ViewStyleShipbuildingLinesBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    def SetContents(self, objects: List[ViewStyleShipbuildingLinesBuilder]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    @overload
    def Swap(self, object1: ViewStyleShipbuildingLinesBuilder, object2: ViewStyleShipbuildingLinesBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
import NXOpen.Preferences
class ViewStyleShipbuildingLinesBuilder(NXOpen.TaggedObject): 
    """ Represents the Shipbuilding LINES tab on the View Style Dialog (Drawings.ViewStyleShipbuildingLinesBuilder)
    """
    @property
    def HiddenColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) HiddenColor
         Returns the hidden line color on the SHIPBUILDING LINES tab of the View Style Dialog   
            
         
        """
        pass
    @HiddenColor.setter
    def HiddenColor(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) HiddenColor
         Returns the hidden line color on the SHIPBUILDING LINES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def HiddenFont(self) -> NXOpen.Preferences.Font:
        """
        Getter for property: ( NXOpen.Preferences.Font) HiddenFont
         Returns the hidden line font on the SHIPBUILDING LINES tab of the View Style Dialog   
            
         
        """
        pass
    @HiddenFont.setter
    def HiddenFont(self, font: NXOpen.Preferences.Font):
        """
        Setter for property: ( NXOpen.Preferences.Font) HiddenFont
         Returns the hidden line font on the SHIPBUILDING LINES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def HiddenWidth(self) -> NXOpen.Preferences.Width:
        """
        Getter for property: ( NXOpen.Preferences.Width) HiddenWidth
         Returns the hidden line width on the SHIPBUILDING LINES tab of the View Style Dialog   
            
         
        """
        pass
    @HiddenWidth.setter
    def HiddenWidth(self, width: NXOpen.Preferences.Width):
        """
        Setter for property: ( NXOpen.Preferences.Width) HiddenWidth
         Returns the hidden line width on the SHIPBUILDING LINES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def SingleLineRepresentation(self) -> bool:
        """
        Getter for property: (bool) SingleLineRepresentation
         Returns the Shipbuilding line toggle on the SHIPBUILDING LINES tab of the View Style Dialog   
            
         
        """
        pass
    @SingleLineRepresentation.setter
    def SingleLineRepresentation(self, singleLineToggle: bool):
        """
        Setter for property: (bool) SingleLineRepresentation
         Returns the Shipbuilding line toggle on the SHIPBUILDING LINES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def VisibleColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) VisibleColor
         Returns the visible line color on the SHIPBUILDING LINES tab of the View Style Dialog   
            
         
        """
        pass
    @VisibleColor.setter
    def VisibleColor(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) VisibleColor
         Returns the visible line color on the SHIPBUILDING LINES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def VisibleFont(self) -> NXOpen.Preferences.Font:
        """
        Getter for property: ( NXOpen.Preferences.Font) VisibleFont
         Returns the visible line font on the SHIPBUILDING LINES tab of the View Style Dialog   
            
         
        """
        pass
    @VisibleFont.setter
    def VisibleFont(self, font: NXOpen.Preferences.Font):
        """
        Setter for property: ( NXOpen.Preferences.Font) VisibleFont
         Returns the visible line font on the SHIPBUILDING LINES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def VisibleWidth(self) -> NXOpen.Preferences.Width:
        """
        Getter for property: ( NXOpen.Preferences.Width) VisibleWidth
         Returns the visible line width on the SHIPBUILDING LINES tab of the View Style Dialog   
            
         
        """
        pass
    @VisibleWidth.setter
    def VisibleWidth(self, width: NXOpen.Preferences.Width):
        """
        Setter for property: ( NXOpen.Preferences.Width) VisibleWidth
         Returns the visible line width on the SHIPBUILDING LINES tab of the View Style Dialog   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
import NXOpen.Preferences
class ViewStyleSmoothEdgesBuilder(NXOpen.TaggedObject): 
    """ Represents the SMOOTH EDGES tab on the View Style Dialog (Drawings.ViewStyleSmoothEdgesBuilder)
    """
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) Color
         Returns the color on the SMOOTH EDGES tab of the View Style Dialog   
            
         
        """
        pass
    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) Color
         Returns the color on the SMOOTH EDGES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def EndGaps(self) -> bool:
        """
        Getter for property: (bool) EndGaps
         Returns the end gaps toggle on the SMOOTH EDGES tab of the View Style Dialog   
            
         
        """
        pass
    @EndGaps.setter
    def EndGaps(self, endGapsToggle: bool):
        """
        Setter for property: (bool) EndGaps
         Returns the end gaps toggle on the SMOOTH EDGES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def EndGapsDistance(self) -> float:
        """
        Getter for property: (float) EndGapsDistance
         Returns the end gaps data on the SMOOTH EDGES tab of the View Style Dialog   
            
         
        """
        pass
    @EndGapsDistance.setter
    def EndGapsDistance(self, endGapsData: float):
        """
        Setter for property: (float) EndGapsDistance
         Returns the end gaps data on the SMOOTH EDGES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Font(self) -> NXOpen.Preferences.Font:
        """
        Getter for property: ( NXOpen.Preferences.Font) Font
         Returns the font on the SMOOTH EDGES tab of the View Style Dialog   
            
         
        """
        pass
    @Font.setter
    def Font(self, font: NXOpen.Preferences.Font):
        """
        Setter for property: ( NXOpen.Preferences.Font) Font
         Returns the font on the SMOOTH EDGES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def SmoothEdge(self) -> bool:
        """
        Getter for property: (bool) SmoothEdge
         Returns the smooth edge toggle on the SMOOTH EDGES tab of the View Style Dialog   
            
         
        """
        pass
    @SmoothEdge.setter
    def SmoothEdge(self, smoothEdgeToggle: bool):
        """
        Setter for property: (bool) SmoothEdge
         Returns the smooth edge toggle on the SMOOTH EDGES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Tolerance(self) -> bool:
        """
        Getter for property: (bool) Tolerance
         Returns the angle tolerance toggle on the SMOOTH EDGES tab of the View Style Dialog   
            
         
        """
        pass
    @Tolerance.setter
    def Tolerance(self, toleranceToggle: bool):
        """
        Setter for property: (bool) Tolerance
         Returns the angle tolerance toggle on the SMOOTH EDGES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def ToleranceValue(self) -> float:
        """
        Getter for property: (float) ToleranceValue
         Returns the angle tolerance data on the SMOOTH EDGES tab of the View Style Dialog   
            
         
        """
        pass
    @ToleranceValue.setter
    def ToleranceValue(self, toleranceData: float):
        """
        Setter for property: (float) ToleranceValue
         Returns the angle tolerance data on the SMOOTH EDGES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Width(self) -> NXOpen.Preferences.Width:
        """
        Getter for property: ( NXOpen.Preferences.Width) Width
         Returns the width on the SMOOTH EDGES tab of the View Style Dialog   
            
         
        """
        pass
    @Width.setter
    def Width(self, width: NXOpen.Preferences.Width):
        """
        Setter for property: ( NXOpen.Preferences.Width) Width
         Returns the width on the SMOOTH EDGES tab of the View Style Dialog   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ViewStyleThreadsBuilder(NXOpen.TaggedObject): 
    """ Represents the THREADS tab on the View Style Dialog (Drawings.ViewStyleThreadsBuilder)
    """
    @property
    def MinimumPitchFieldData(self) -> float:
        """
        Getter for property: (float) MinimumPitchFieldData
         Returns the minimum pitch field on the THREADS tab of the View Style Dialog   
            
         
        """
        pass
    @MinimumPitchFieldData.setter
    def MinimumPitchFieldData(self, minimumPitchFieldData: float):
        """
        Setter for property: (float) MinimumPitchFieldData
         Returns the minimum pitch field on the THREADS tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def OverrideVisibleThreadColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) OverrideVisibleThreadColor
         Returns the override thread color on the THREADS tab of the View Style Dialog   
            
         
        """
        pass
    @OverrideVisibleThreadColor.setter
    def OverrideVisibleThreadColor(self, overrideVisibleThreadColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) OverrideVisibleThreadColor
         Returns the override thread color on the THREADS tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def StandardData(self) -> int:
        """
        Getter for property: (int) StandardData
         Returns the standard option data on the THREADS tab of the View Style Dialog 
                    StandardData = 0 = None
                    StandardData = 1 = Simplified-Full Arc
                    StandardData = 4 = Simplified-34 Arc
                    StandardData = 2 = Schematic
                    StandardData = 3 = Detailed-Full Arc
                    StandardData = 5 = Detailed-34 Arc  
            
         
        """
        pass
    @StandardData.setter
    def StandardData(self, standardOptionData: int):
        """
        Setter for property: (int) StandardData
         Returns the standard option data on the THREADS tab of the View Style Dialog 
                    StandardData = 0 = None
                    StandardData = 1 = Simplified-Full Arc
                    StandardData = 4 = Simplified-34 Arc
                    StandardData = 2 = Schematic
                    StandardData = 3 = Detailed-Full Arc
                    StandardData = 5 = Detailed-34 Arc  
            
         
        """
        pass
    @property
    def TrueHiddenLine(self) -> bool:
        """
        Getter for property: (bool) TrueHiddenLine
         Returns the true hidden line toggle on the THREADS tab of the View Style Dialog   
            
         
        """
        pass
    @TrueHiddenLine.setter
    def TrueHiddenLine(self, trueHiddenLineToggle: bool):
        """
        Setter for property: (bool) TrueHiddenLine
         Returns the true hidden line toggle on the THREADS tab of the View Style Dialog   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
import NXOpen.Preferences
class ViewStyleTraceLinesBuilder(NXOpen.TaggedObject): 
    """ Represents the TRACE LINES tab on the View Style Dialog (Drawings.ViewStyleTraceLinesBuilder)
    """
    @property
    def CreateGaps(self) -> bool:
        """
        Getter for property: (bool) CreateGaps
         Returns the create gaps toggle on the TRACE LINES tab of the View Style Dialog   
            
         
        """
        pass
    @CreateGaps.setter
    def CreateGaps(self, createGapsToggle: bool):
        """
        Setter for property: (bool) CreateGaps
         Returns the create gaps toggle on the TRACE LINES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def GapSize(self) -> float:
        """
        Getter for property: (float) GapSize
         Returns the gap size on the TRACE LINES tab of the View Style Dialog   
            
         
        """
        pass
    @GapSize.setter
    def GapSize(self, gapSize: float):
        """
        Setter for property: (float) GapSize
         Returns the gap size on the TRACE LINES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def HiddenColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) HiddenColor
         Returns the hidden color on the TRACE LINES tab of the View Style Dialog   
            
         
        """
        pass
    @HiddenColor.setter
    def HiddenColor(self, hiddenColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) HiddenColor
         Returns the hidden color on the TRACE LINES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def HiddenFont(self) -> NXOpen.Preferences.Font:
        """
        Getter for property: ( NXOpen.Preferences.Font) HiddenFont
         Returns the hidden font on the TRACE LINES tab of the View Style Dialog   
            
         
        """
        pass
    @HiddenFont.setter
    def HiddenFont(self, hiddenFont: NXOpen.Preferences.Font):
        """
        Setter for property: ( NXOpen.Preferences.Font) HiddenFont
         Returns the hidden font on the TRACE LINES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def HiddenWidth(self) -> NXOpen.Preferences.Width:
        """
        Getter for property: ( NXOpen.Preferences.Width) HiddenWidth
         Returns the hidden width on the TRACE LINES tab of the View Style Dialog   
            
         
        """
        pass
    @HiddenWidth.setter
    def HiddenWidth(self, hiddenWidth: NXOpen.Preferences.Width):
        """
        Setter for property: ( NXOpen.Preferences.Width) HiddenWidth
         Returns the hidden width on the TRACE LINES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def VisibleColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) VisibleColor
         Returns the visible color on the TRACE LINES tab of the View Style Dialog   
            
         
        """
        pass
    @VisibleColor.setter
    def VisibleColor(self, visibleColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) VisibleColor
         Returns the visible color on the TRACE LINES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def VisibleFont(self) -> NXOpen.Preferences.Font:
        """
        Getter for property: ( NXOpen.Preferences.Font) VisibleFont
         Returns the visible font on the TRACE LINES tab of the View Style Dialog   
            
         
        """
        pass
    @VisibleFont.setter
    def VisibleFont(self, font: NXOpen.Preferences.Font):
        """
        Setter for property: ( NXOpen.Preferences.Font) VisibleFont
         Returns the visible font on the TRACE LINES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def VisibleWidth(self) -> NXOpen.Preferences.Width:
        """
        Getter for property: ( NXOpen.Preferences.Width) VisibleWidth
         Returns the visible width on the TRACE LINES tab of the View Style Dialog   
            
         
        """
        pass
    @VisibleWidth.setter
    def VisibleWidth(self, width: NXOpen.Preferences.Width):
        """
        Setter for property: ( NXOpen.Preferences.Width) VisibleWidth
         Returns the visible width on the TRACE LINES tab of the View Style Dialog   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
import NXOpen.Preferences
class ViewStyleVirtualIntersectionsBuilder(NXOpen.TaggedObject): 
    """ Represents the VIRTUAL INTERSECTIONS tab on the View Style Dialog (Drawings.ViewStyleVirtualIntersectionsBuilder)
    """
    @property
    def AdjacentBlends(self) -> bool:
        """
        Getter for property: (bool) AdjacentBlends
         Returns the adjacent blends toggle on the VIRTUAL INTERSECTIONS tab of the View Style Dialog   
            
         
        """
        pass
    @AdjacentBlends.setter
    def AdjacentBlends(self, adjacentBlendsToggle: bool):
        """
        Setter for property: (bool) AdjacentBlends
         Returns the adjacent blends toggle on the VIRTUAL INTERSECTIONS tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) Color
         Returns the color on the VIRTUAL INTERSECTIONS tab of the View Style Dialog   
            
         
        """
        pass
    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) Color
         Returns the color on the VIRTUAL INTERSECTIONS tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def EndGaps(self) -> bool:
        """
        Getter for property: (bool) EndGaps
         Returns the end gaps toggle on the VIRTUAL INTERSECTIONS tab of the View Style Dialog   
            
         
        """
        pass
    @EndGaps.setter
    def EndGaps(self, endGapsToggle: bool):
        """
        Setter for property: (bool) EndGaps
         Returns the end gaps toggle on the VIRTUAL INTERSECTIONS tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def EndGapsDistance(self) -> float:
        """
        Getter for property: (float) EndGapsDistance
         Returns the end gaps data on the VIRTUAL INTERSECTIONS tab of the View Style Dialog   
            
         
        """
        pass
    @EndGapsDistance.setter
    def EndGapsDistance(self, endGapsData: float):
        """
        Setter for property: (float) EndGapsDistance
         Returns the end gaps data on the VIRTUAL INTERSECTIONS tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Font(self) -> NXOpen.Preferences.Font:
        """
        Getter for property: ( NXOpen.Preferences.Font) Font
         Returns the font on the VIRTUAL INTERSECTIONS tab of the View Style Dialog   
            
         
        """
        pass
    @Font.setter
    def Font(self, font: NXOpen.Preferences.Font):
        """
        Setter for property: ( NXOpen.Preferences.Font) Font
         Returns the font on the VIRTUAL INTERSECTIONS tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def VirtualIntersections(self) -> bool:
        """
        Getter for property: (bool) VirtualIntersections
         Returns the virtual intersections toggle on the VIRTUAL INTERSECTIONS tab of the View Style Dialog   
            
         
        """
        pass
    @VirtualIntersections.setter
    def VirtualIntersections(self, virtualIntersectionsToggle: bool):
        """
        Setter for property: (bool) VirtualIntersections
         Returns the virtual intersections toggle on the VIRTUAL INTERSECTIONS tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def Width(self) -> NXOpen.Preferences.Width:
        """
        Getter for property: ( NXOpen.Preferences.Width) Width
         Returns the width on the VIRTUAL INTERSECTIONS tab of the View Style Dialog   
            
         
        """
        pass
    @Width.setter
    def Width(self, width: NXOpen.Preferences.Width):
        """
        Setter for property: ( NXOpen.Preferences.Width) Width
         Returns the width on the VIRTUAL INTERSECTIONS tab of the View Style Dialog   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
import NXOpen.Preferences
class ViewStyleVisibleLinesBuilder(NXOpen.TaggedObject): 
    """ Represents the VISIBLE LINES tab on the View Style Dialog (Drawings.ViewStyleVisibleLinesBuilder)
    """
    @property
    def VisibleColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) VisibleColor
         Returns the visible color on the VISIBLE LINES tab of the View Style Dialog   
            
         
        """
        pass
    @VisibleColor.setter
    def VisibleColor(self, visibleColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) VisibleColor
         Returns the visible color on the VISIBLE LINES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def VisibleFont(self) -> NXOpen.Preferences.Font:
        """
        Getter for property: ( NXOpen.Preferences.Font) VisibleFont
         Returns the visible font on the VISIBLE LINES tab of the View Style Dialog   
            
         
        """
        pass
    @VisibleFont.setter
    def VisibleFont(self, font: NXOpen.Preferences.Font):
        """
        Setter for property: ( NXOpen.Preferences.Font) VisibleFont
         Returns the visible font on the VISIBLE LINES tab of the View Style Dialog   
            
         
        """
        pass
    @property
    def VisibleWidth(self) -> NXOpen.Preferences.Width:
        """
        Getter for property: ( NXOpen.Preferences.Width) VisibleWidth
         Returns the visible width on the VISIBLE LINES tab of the View Style Dialog   
            
         
        """
        pass
    @VisibleWidth.setter
    def VisibleWidth(self, width: NXOpen.Preferences.Width):
        """
        Setter for property: ( NXOpen.Preferences.Width) VisibleWidth
         Returns the visible width on the VISIBLE LINES tab of the View Style Dialog   
            
         
        """
        pass
import NXOpen
class ViewStyle(NXOpen.Object): 
    """ Represents set of style applicable to drafting views. """
    @property
    def General() -> GeneralViewStyle:
        """
         Returns object for doing View style settings applicable to General 
        """
        pass
    @property
    def BaseView() -> BaseViewStyle:
        """
         Returns object for doing View style settings applicable to Basedata 
        """
        pass
    @property
    def Projected() -> ProjectedViewStyle:
        """
         Returns object for doing View style settings applicable to Projected 
        """
        pass
    @property
    def InheritPmi() -> InheritPmiViewStyle:
        """
         Returns object for doing View style settings applicable to InheritPmi 
        """
        pass
    @property
    def Section() -> SectionViewStyle:
        """
         Returns object for doing View style settings applicable to Section 
        """
        pass
    @property
    def VirtualIntersections() -> VirtualIntersectionsViewStyle:
        """
         Returns object for doing View style settings applicable to VirtualIntersections 
        """
        pass
    @property
    def SmoothEdges() -> SmoothEdgesViewStyle:
        """
         Returns object for doing View style settings applicable to SmoothEdges 
        """
        pass
    @property
    def Perspective() -> PerspectiveViewStyle:
        """
         Returns object for doing View style settings applicable to Perspective 
        """
        pass
    @property
    def Orientation() -> OrientationViewStyle:
        """
         Returns object for doing View style settings applicable to Orientation 
        """
        pass
    @property
    def VisibleLines() -> VisibleLinesViewStyle:
        """
         Returns object for doing View style settings applicable to VisibleLines 
        """
        pass
    @property
    def Threads() -> ThreadsViewStyle:
        """
         Returns object for doing View style settings applicable to Threads 
        """
        pass
    @property
    def TraceLines() -> TraceLinesViewStyle:
        """
         Returns object for doing View style settings applicable to TraceLines 
        """
        pass
    @property
    def HiddenLines() -> HiddenLinesViewStyle:
        """
         Returns object for doing View style settings applicable to HiddenLines 
        """
        pass
    @property
    def Shading() -> ShadingViewStyle:
        """
         Returns object for doing View style settings applicable to Shading 
        """
        pass
    @property
    def FlatPattern() -> FlatPatternViewStyle:
        """
         Returns object for doing View style settings applicable to Flat Pattern Views. 
        """
        pass
    @property
    def ShipbuildingLines() -> ShipbuildingLinesViewStyle:
        """
         Returns object for doing View style settings applicable to Ship Lines. 
        """
        pass
    @property
    def ShipDraftingViewLines() -> ShipDraftingViewLinesViewStyle:
        """
         Returns object for doing View style settings applicable to Ship Drafting View Lines. 
        """
        pass
    @property
    def ShipGeneralArrangementViewLines() -> ShipGeneralArrangementViewLinesViewStyle:
        """
         Returns object for doing View style settings applicable to Ship General Arrangement View Lines. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ViewWorkflowBuilder(NXOpen.TaggedObject): 
    """ Represents a NXOpen.Drawings.ViewWorkflowBuilder """
    class Display(Enum):
        """
        Members Include: 
         |DisplayandEmphasize| 
         |CurvesOnly| 

        """
        DisplayandEmphasize: int
        CurvesOnly: int
        @staticmethod
        def ValueOf(value: int) -> ViewWorkflowBuilder.Display:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class HandlingBodiesType(Enum):
        """
        Members Include: 
         |OmitBodiesfromView| 
         |StopUpdateandNotifyUser| 
         |StopUpdate| 
         |Generate| 

        """
        OmitBodiesfromView: int
        StopUpdateandNotifyUser: int
        StopUpdate: int
        Generate: int
        @staticmethod
        def ValueOf(value: int) -> ViewWorkflowBuilder.HandlingBodiesType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Handlingbodies(Enum):
        """
        Members Include: 
         |OmitBodiesfromView| 
         |StopUpdateandNotifyUser| 
         |StopUpdate| 
         |Generate| 

        """
        OmitBodiesfromView: int
        StopUpdateandNotifyUser: int
        StopUpdate: int
        Generate: int
        @staticmethod
        def ValueOf(value: int) -> ViewWorkflowBuilder.Handlingbodies:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Splarcs(Enum):
        """
        Members Include: 
         |Always| 
         |NeverForAutomatic| 
         |Never| 

        """
        Always: int
        NeverForAutomatic: int
        Never: int
        @staticmethod
        def ValueOf(value: int) -> ViewWorkflowBuilder.Splarcs:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Style(Enum):
        """
        Members Include: 
         |Border| 
         |Wireframe| 
         |HiddenWireframe| 
         |Shaded| 

        """
        Border: int
        Wireframe: int
        HiddenWireframe: int
        Shaded: int
        @staticmethod
        def ValueOf(value: int) -> ViewWorkflowBuilder.Style:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ActiveSketchViewColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) ActiveSketchViewColor
         Returns the active views border color   
            
         
        """
        pass
    @ActiveSketchViewColor.setter
    def ActiveSketchViewColor(self, activeSketchViewColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) ActiveSketchViewColor
         Returns the active views border color   
            
         
        """
        pass
    @property
    def AssociativeAlignment(self) -> bool:
        """
        Getter for property: (bool) AssociativeAlignment
         Returns the associative alignment enable alignement between views  
            
         
        """
        pass
    @AssociativeAlignment.setter
    def AssociativeAlignment(self, associativeAlignment: bool):
        """
        Setter for property: (bool) AssociativeAlignment
         Returns the associative alignment enable alignement between views  
            
         
        """
        pass
    @property
    def BorderColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) BorderColor
         Returns the border color of view   
            
         
        """
        pass
    @BorderColor.setter
    def BorderColor(self, borderColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) BorderColor
         Returns the border color of view   
            
         
        """
        pass
    @property
    def CursorTracking(self) -> bool:
        """
        Getter for property: (bool) CursorTracking
         Returns the cursor tracking enable XCYC coordinates in dynamic input boxes when placing a view on a drawing   
            
         
        """
        pass
    @CursorTracking.setter
    def CursorTracking(self, cursorTracking: bool):
        """
        Setter for property: (bool) CursorTracking
         Returns the cursor tracking enable XCYC coordinates in dynamic input boxes when placing a view on a drawing   
            
         
        """
        pass
    @property
    def DisplayBorders(self) -> bool:
        """
        Getter for property: (bool) DisplayBorders
         Returns the display view borders on the the drawing   
            
         
        """
        pass
    @DisplayBorders.setter
    def DisplayBorders(self, displayBorders: bool):
        """
        Setter for property: (bool) DisplayBorders
         Returns the display view borders on the the drawing   
            
         
        """
        pass
    @property
    def EnableSmoothEdgesForLWView(self) -> bool:
        """
        Getter for property: (bool) EnableSmoothEdgesForLWView
         Returns the setting is not needed anymore because the smooth edges are correctly supported now for smart lightweight views.  
           We recommend removing this call from existing programs.   
         
        """
        pass
    @EnableSmoothEdgesForLWView.setter
    def EnableSmoothEdgesForLWView(self, enableSmoothEdgesForLWView: bool):
        """
        Setter for property: (bool) EnableSmoothEdgesForLWView
         Returns the setting is not needed anymore because the smooth edges are correctly supported now for smart lightweight views.  
           We recommend removing this call from existing programs.   
         
        """
        pass
    @property
    def FaceDisplay(self) -> ViewWorkflowBuilder.Display:
        """
        Getter for property: ( ViewWorkflowBuilder.Display NXOpen.) FaceDisplay
         Returns the face display provides options in an extracted edge view that are available for selection   
            
         
        """
        pass
    @FaceDisplay.setter
    def FaceDisplay(self, faceDisplay: ViewWorkflowBuilder.Display):
        """
        Setter for property: ( ViewWorkflowBuilder.Display NXOpen.) FaceDisplay
         Returns the face display provides options in an extracted edge view that are available for selection   
            
         
        """
        pass
    @property
    def HandlingBodies(self) -> ViewWorkflowBuilder.Handlingbodies:
        """
        Getter for property: ( ViewWorkflowBuilder.Handlingbodies NXOpen.) HandlingBodies
         Returns the handling bodies provides option for update view without lightweight data   
            
         
        """
        pass
    @HandlingBodies.setter
    def HandlingBodies(self, handlingBodies: ViewWorkflowBuilder.Handlingbodies):
        """
        Setter for property: ( ViewWorkflowBuilder.Handlingbodies NXOpen.) HandlingBodies
         Returns the handling bodies provides option for update view without lightweight data   
            
         
        """
        pass
    @property
    def HandlingBodiesTypes(self) -> ViewWorkflowBuilder.HandlingBodiesType:
        """
        Getter for property: ( ViewWorkflowBuilder.HandlingBodiesType NXOpen.) HandlingBodiesTypes
         Returns the handling bodies provides option for update view without lightweight data   
            
         
        """
        pass
    @HandlingBodiesTypes.setter
    def HandlingBodiesTypes(self, handlingBodiesTypes: ViewWorkflowBuilder.HandlingBodiesType):
        """
        Setter for property: ( ViewWorkflowBuilder.HandlingBodiesType NXOpen.) HandlingBodiesTypes
         Returns the handling bodies provides option for update view without lightweight data   
            
         
        """
        pass
    @property
    def LargeAssemblyStepThreshold(self) -> int:
        """
        Getter for property: (int) LargeAssemblyStepThreshold
         Returns the large assembly step threshold option establishes the minimum number of components (loaded or unloaded) a part may have to be considered a 
                    large assembly.  
           When the number of components exceeds this number, the View Creation Wizard provides an extra step 
                    to optimize part settings for large assemblies. A value of zero will force the system to always use the optimized 
                    part settings for large assemblies   
         
        """
        pass
    @LargeAssemblyStepThreshold.setter
    def LargeAssemblyStepThreshold(self, largeAssemblyStepThreshold: int):
        """
        Setter for property: (int) LargeAssemblyStepThreshold
         Returns the large assembly step threshold option establishes the minimum number of components (loaded or unloaded) a part may have to be considered a 
                    large assembly.  
           When the number of components exceeds this number, the View Creation Wizard provides an extra step 
                    to optimize part settings for large assemblies. A value of zero will force the system to always use the optimized 
                    part settings for large assemblies   
         
        """
        pass
    @property
    def LoadComponentsOnDemand(self) -> bool:
        """
        Getter for property: (bool) LoadComponentsOnDemand
         Returns whether or not to load the components on demand for smart lightweight views   
            
         
        """
        pass
    @LoadComponentsOnDemand.setter
    def LoadComponentsOnDemand(self, loadComponentsOnDemand: bool):
        """
        Setter for property: (bool) LoadComponentsOnDemand
         Returns whether or not to load the components on demand for smart lightweight views   
            
         
        """
        pass
    @property
    def OnLegacyViewUpdate(self) -> bool:
        """
        Getter for property: (bool) OnLegacyViewUpdate
         Returns the on legacy view update determines whether or not components should be loaded as needed to update lightweight views   
            
         
        """
        pass
    @OnLegacyViewUpdate.setter
    def OnLegacyViewUpdate(self, onLegacyViewUpdate: bool):
        """
        Setter for property: (bool) OnLegacyViewUpdate
         Returns the on legacy view update determines whether or not components should be loaded as needed to update lightweight views   
            
         
        """
        pass
    @property
    def OnViewSelection(self) -> bool:
        """
        Getter for property: (bool) OnViewSelection
         Returns the on view selection determines whether or not components should be loaded as needed for selection in lightweight 
                    views for accurate dimensioning   
            
         
        """
        pass
    @OnViewSelection.setter
    def OnViewSelection(self, onViewSelection: bool):
        """
        Setter for property: (bool) OnViewSelection
         Returns the on view selection determines whether or not components should be loaded as needed for selection in lightweight 
                    views for accurate dimensioning   
            
         
        """
        pass
    @property
    def PreviewStyle(self) -> ViewWorkflowBuilder.Style:
        """
        Getter for property: ( ViewWorkflowBuilder.Style NXOpen.) PreviewStyle
         Returns the style of the preview when adding a view to the drawing   
            
         
        """
        pass
    @PreviewStyle.setter
    def PreviewStyle(self, previewStyle: ViewWorkflowBuilder.Style):
        """
        Setter for property: ( ViewWorkflowBuilder.Style NXOpen.) PreviewStyle
         Returns the style of the preview when adding a view to the drawing   
            
         
        """
        pass
    @property
    def SelectGeometryProjectedAsArcs(self) -> ViewWorkflowBuilder.Splarcs:
        """
        Getter for property: ( ViewWorkflowBuilder.Splarcs NXOpen.) SelectGeometryProjectedAsArcs
         Returns the Select Geometry Projected as Arcs provides options for selection of SPLARCs entity for centerlines and Annotations   
            
         
        """
        pass
    @SelectGeometryProjectedAsArcs.setter
    def SelectGeometryProjectedAsArcs(self, selectGeometryProjectedAsArcs: ViewWorkflowBuilder.Splarcs):
        """
        Setter for property: ( ViewWorkflowBuilder.Splarcs NXOpen.) SelectGeometryProjectedAsArcs
         Returns the Select Geometry Projected as Arcs provides options for selection of SPLARCs entity for centerlines and Annotations   
            
         
        """
        pass
    @property
    def ShowFacetEdges(self) -> bool:
        """
        Getter for property: (bool) ShowFacetEdges
         Returns the show facet edges determines whether or not facet edges will be shown on shaded faces when displaying a drawing sheet   
            
         
        """
        pass
    @ShowFacetEdges.setter
    def ShowFacetEdges(self, showFacetEdges: bool):
        """
        Setter for property: (bool) ShowFacetEdges
         Returns the show facet edges determines whether or not facet edges will be shown on shaded faces when displaying a drawing sheet   
            
         
        """
        pass
    @property
    def UseLineAntialiasing(self) -> bool:
        """
        Getter for property: (bool) UseLineAntialiasing
         Returns the use line antialiasing   
            
         
        """
        pass
    @UseLineAntialiasing.setter
    def UseLineAntialiasing(self, useLineAntialiasing: bool):
        """
        Setter for property: (bool) UseLineAntialiasing
         Returns the use line antialiasing   
            
         
        """
        pass
    @property
    def UseTranslucency(self) -> bool:
        """
        Getter for property: (bool) UseTranslucency
         Returns the use translucency determines translucency settings for faces when displaying a drawing sheet   
            
         
        """
        pass
    @UseTranslucency.setter
    def UseTranslucency(self, useTranslucency: bool):
        """
        Setter for property: (bool) UseTranslucency
         Returns the use translucency determines translucency settings for faces when displaying a drawing sheet   
            
         
        """
        pass
import NXOpen
import NXOpen.Preferences
class VirtualIntersectionsViewStyle(NXOpen.Object): 
    """ Represents set of Virtual Intersections View Style Preferences applicable to drafting views.
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
    def AdjacentBlendsFont(self) -> NXOpen.Preferences.Font:
        """
        Getter for property: ( NXOpen.Preferences.Font) AdjacentBlendsFont
         Returns the font of adjacent blends.  
            
         
        """
        pass
    @AdjacentBlendsFont.setter
    def AdjacentBlendsFont(self, adjacent_blends_font: NXOpen.Preferences.Font):
        """
        Setter for property: ( NXOpen.Preferences.Font) AdjacentBlendsFont
         Returns the font of adjacent blends.  
            
         
        """
        pass
    @property
    def AdjacentBlendsWidth(self) -> NXOpen.Preferences.Width:
        """
        Getter for property: ( NXOpen.Preferences.Width) AdjacentBlendsWidth
         Returns the width of adjacent blends.  
            
         
        """
        pass
    @AdjacentBlendsWidth.setter
    def AdjacentBlendsWidth(self, adjacent_blends_width: NXOpen.Preferences.Width):
        """
        Setter for property: ( NXOpen.Preferences.Width) AdjacentBlendsWidth
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
import NXOpen.GeometricUtilities
class VisibleAndHiddenLinesColorFontWidthBuilder(NXOpen.TaggedObject): 
    """
    Represent a NXOpen.Drawings.VisibleAndHiddenLinesColorFontWidthBuilder
    """
    @property
    def HiddenCFW(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) HiddenCFW
         Returns the hidden lines color, font, and width.  
            
         
        """
        pass
    @property
    def VisibleCFW(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) VisibleCFW
         Returns the visible lines color, font, and width.  
            
         
        """
        pass
import NXOpen
import NXOpen.Preferences
class VisibleLinesViewStyle(NXOpen.Object): 
    """ Represents set of Visible Lines View Style Preferences applicable to drafting views. """
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
    def VisibleFont(self) -> NXOpen.Preferences.Font:
        """
        Getter for property: ( NXOpen.Preferences.Font) VisibleFont
         Returns the visible font.  
            
         
        """
        pass
    @VisibleFont.setter
    def VisibleFont(self, visible_font: NXOpen.Preferences.Font):
        """
        Setter for property: ( NXOpen.Preferences.Font) VisibleFont
         Returns the visible font.  
            
         
        """
        pass
    @property
    def VisibleWidth(self) -> NXOpen.Preferences.Width:
        """
        Getter for property: ( NXOpen.Preferences.Width) VisibleWidth
         Returns the visible width.  
            
         
        """
        pass
    @VisibleWidth.setter
    def VisibleWidth(self, visible_width: NXOpen.Preferences.Width):
        """
        Setter for property: ( NXOpen.Preferences.Width) VisibleWidth
         Returns the visible width.  
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class VisualDrawingComparePrefsBuilder(NXOpen.TaggedObject): 
    """ 
    This class gets and sets components of Visual Overlay in Drafting Preferences.
    """
    class VisualDrawingComparePrefsMethodType(Enum):
        """
        Members Include: 
         |AgainstAnotherDrawing|  This option is used to overlay different part over current part 
         |AgainstOverlayDatainActiveDrawing|  This option is used to overlay current part on itself 

        """
        AgainstAnotherDrawing: int
        AgainstOverlayDatainActiveDrawing: int
        @staticmethod
        def ValueOf(value: int) -> VisualDrawingComparePrefsBuilder.VisualDrawingComparePrefsMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class VisualDrawingComparePrefsOverlayDataToUse(Enum):
        """
        Members Include: 
         |AskatRuntime|  This option tells to show messages at rumtime 
         |AlwaysUseExistingData|  This option will use existing data to overlay 
         |AlwaysCreateNewData|  This option will always create new data
         |CreateNewDataifNoneExists|  This option will create new data if none exists

        """
        AskatRuntime: int
        AlwaysUseExistingData: int
        AlwaysCreateNewData: int
        CreateNewDataifNoneExists: int
        @staticmethod
        def ValueOf(value: int) -> VisualDrawingComparePrefsBuilder.VisualDrawingComparePrefsOverlayDataToUse:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CompareMethodType(self) -> VisualDrawingComparePrefsBuilder.VisualDrawingComparePrefsMethodType:
        """
        Getter for property: ( VisualDrawingComparePrefsBuilder.VisualDrawingComparePrefsMethodType NXOpen.) CompareMethodType
         Returns the compare method type   
            
         
        """
        pass
    @CompareMethodType.setter
    def CompareMethodType(self, compareMethodType: VisualDrawingComparePrefsBuilder.VisualDrawingComparePrefsMethodType):
        """
        Setter for property: ( VisualDrawingComparePrefsBuilder.VisualDrawingComparePrefsMethodType NXOpen.) CompareMethodType
         Returns the compare method type   
            
         
        """
        pass
    @property
    def OverlayColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) OverlayColor
         Returns the overlay color   
            
         
        """
        pass
    @OverlayColor.setter
    def OverlayColor(self, overlayColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) OverlayColor
         Returns the overlay color   
            
         
        """
        pass
    @property
    def OverlayDataToUse(self) -> VisualDrawingComparePrefsBuilder.VisualDrawingComparePrefsOverlayDataToUse:
        """
        Getter for property: ( VisualDrawingComparePrefsBuilder.VisualDrawingComparePrefsOverlayDataToUse NXOpen.) OverlayDataToUse
         Returns the overlay data to use   
            
         
        """
        pass
    @OverlayDataToUse.setter
    def OverlayDataToUse(self, overlayDataToUse: VisualDrawingComparePrefsBuilder.VisualDrawingComparePrefsOverlayDataToUse):
        """
        Setter for property: ( VisualDrawingComparePrefsBuilder.VisualDrawingComparePrefsOverlayDataToUse NXOpen.) OverlayDataToUse
         Returns the overlay data to use   
            
         
        """
        pass
class ZoneOrigin(Enum):
    """
    Members Include: 
     |BottomRight|  Bottom Right 
     |TopLeft|  Top Left 
     |TopRight|  Top Right 
     |BottomLeft| 

    """
    BottomRight: int
    TopLeft: int
    TopRight: int
    BottomLeft: int
    @staticmethod
    def ValueOf(value: int) -> ZoneOrigin:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
