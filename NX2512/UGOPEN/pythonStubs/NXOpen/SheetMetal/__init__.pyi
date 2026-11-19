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
import NXOpen.Annotations
class SheetMetalPMISettingsBuilder(NXOpen.Annotations.BaseApplicationStyleBuilder): 
    """ Represents a NXOpen.SheetMetal.SheetMetalPMISettingsBuilder."""
    class BendParameterType(Enum):
        """
        Members Include: 
         |BendRadius| 
         |BendAngle| 
         |NeutralFactor| 

        """
        BendRadius: int
        BendAngle: int
        NeutralFactor: int
        @staticmethod
        def ValueOf(value: int) -> SheetMetalPMISettingsBuilder.BendParameterType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class BendParameters(Enum):
        """
        Members Include: 
         |BendSeqid| 
         |Name| 
         |Direction| 
         |Radius| 
         |OutsideBendAngle| 
         |InsideBendAngle| 
         |NeutralFactor| 
         |LineBreak| 

        """
        BendSeqid: int
        Name: int
        Direction: int
        Radius: int
        OutsideBendAngle: int
        InsideBendAngle: int
        NeutralFactor: int
        LineBreak: int
        @staticmethod
        def ValueOf(value: int) -> SheetMetalPMISettingsBuilder.BendParameters:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class BodyParameterType(Enum):
        """
        Members Include: 
         |Materialthickness| 
         |PhysicalMaterial| 
         |Material| 

        """
        Materialthickness: int
        PhysicalMaterial: int
        Material: int
        @staticmethod
        def ValueOf(value: int) -> SheetMetalPMISettingsBuilder.BodyParameterType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FlatpatternBendDataType(Enum):
        """
        Members Include: 
         |BendRadius| 
         |BendAngle| 
         |NeutralFactor| 
         |BendName| 
         |BendDirection| 
         |BendSeqId| 
         |InsideBendAngle| 

        """
        BendRadius: int
        BendAngle: int
        NeutralFactor: int
        BendName: int
        BendDirection: int
        BendSeqId: int
        InsideBendAngle: int
        @staticmethod
        def ValueOf(value: int) -> SheetMetalPMISettingsBuilder.FlatpatternBendDataType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FlatpatternJoggleParametersType(Enum):
        """
        Members Include: 
         |JoggleRunout| 
         |JoggleDepth| 

        """
        JoggleRunout: int
        JoggleDepth: int
        @staticmethod
        def ValueOf(value: int) -> SheetMetalPMISettingsBuilder.FlatpatternJoggleParametersType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FlatpatternLighteningCutoutParametersType(Enum):
        """
        Members Include: 
         |HoleDiameter| 
         |CutoutDiameter| 

        """
        HoleDiameter: int
        CutoutDiameter: int
        @staticmethod
        def ValueOf(value: int) -> SheetMetalPMISettingsBuilder.FlatpatternLighteningCutoutParametersType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FlatpatternNotePropertiesType(Enum):
        """
        Members Include: 
         |InteriorCutoutCount| 
         |ExteriorCutLength| 
         |InteriorCutLength| 
         |MinimumX| 
         |MinimumY| 
         |TotalCutLength| 
         |MaterialThickness| 

        """
        InteriorCutoutCount: int
        ExteriorCutLength: int
        InteriorCutLength: int
        MinimumX: int
        MinimumY: int
        TotalCutLength: int
        MaterialThickness: int
        @staticmethod
        def ValueOf(value: int) -> SheetMetalPMISettingsBuilder.FlatpatternNotePropertiesType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FpProperties(Enum):
        """
        Members Include: 
         |IntCutoutCount| 
         |ExtCutoutLength| 
         |IntCutoutLength| 
         |MinXLength| 
         |MinYLength| 
         |TotalCutLength| 
         |MaterialThickness| 
         |LineBreak| 

        """
        IntCutoutCount: int
        ExtCutoutLength: int
        IntCutoutLength: int
        MinXLength: int
        MinYLength: int
        TotalCutLength: int
        MaterialThickness: int
        LineBreak: int
        @staticmethod
        def ValueOf(value: int) -> SheetMetalPMISettingsBuilder.FpProperties:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LabelPlacementTypes(Enum):
        """
        Members Include: 
         |HorizontalWithLeader| 
         |AlignWithFlatPatternLines| 

        """
        HorizontalWithLeader: int
        AlignWithFlatPatternLines: int
        @staticmethod
        def ValueOf(value: int) -> SheetMetalPMISettingsBuilder.LabelPlacementTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PmiLayerOptions(Enum):
        """
        Members Include: 
         |Default| 
         |Specify| 

        """
        Default: int
        Specify: int
        @staticmethod
        def ValueOf(value: int) -> SheetMetalPMISettingsBuilder.PmiLayerOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SmPmiNoteType(Enum):
        """
        Members Include: 
         |FlatPatternPropertiesNote| 

        """
        FlatPatternPropertiesNote: int
        @staticmethod
        def ValueOf(value: int) -> SheetMetalPMISettingsBuilder.SmPmiNoteType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SmPmiType(Enum):
        """
        Members Include: 
         |Bend| 
         |Body| 
         |BendSequenceIdLabel| 
         |HoleParameterLabel| 
         |JoggleLabel| 
         |ToolIdLabel| 
         |LighteningCutoutLabel| 

        """
        Bend: int
        Body: int
        BendSequenceIdLabel: int
        HoleParameterLabel: int
        JoggleLabel: int
        ToolIdLabel: int
        LighteningCutoutLabel: int
        @staticmethod
        def ValueOf(value: int) -> SheetMetalPMISettingsBuilder.SmPmiType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngularDecimalPlaces(self) -> int:
        """
        Getter for property: (int) AngularDecimalPlaces
         Returns the angular decimal places setting.  
           Only values from 0 to 6 (both inclusive) are valid.  
         
        """
        pass
    @AngularDecimalPlaces.setter
    def AngularDecimalPlaces(self, angularDecimalPlaces: int):
        """
        Setter for property: (int) AngularDecimalPlaces
         Returns the angular decimal places setting.  
           Only values from 0 to 6 (both inclusive) are valid.  
         
        """
        pass
    @property
    def BlindHoleText(self) -> str:
        """
        Getter for property: (str) BlindHoleText
         Returns the text for blind hole in flat pattern hole details label.  
            
         
        """
        pass
    @BlindHoleText.setter
    def BlindHoleText(self, blindHoleText: str):
        """
        Setter for property: (str) BlindHoleText
         Returns the text for blind hole in flat pattern hole details label.  
            
         
        """
        pass
    @property
    def CreateFlatPatternBendLabel(self) -> bool:
        """
        Getter for property: (bool) CreateFlatPatternBendLabel
         Returns the create flat pattern bend label setting.  
            
         
        """
        pass
    @CreateFlatPatternBendLabel.setter
    def CreateFlatPatternBendLabel(self, createFlatPatternBendLabel: bool):
        """
        Setter for property: (bool) CreateFlatPatternBendLabel
         Returns the create flat pattern bend label setting.  
            
         
        """
        pass
    @property
    def CreateFlatPatternHoleDetailsLabel(self) -> bool:
        """
        Getter for property: (bool) CreateFlatPatternHoleDetailsLabel
         Returns the create flat pattern hole details label setting.  
            
         
        """
        pass
    @CreateFlatPatternHoleDetailsLabel.setter
    def CreateFlatPatternHoleDetailsLabel(self, createFlatPatternHoleDetailsLabel: bool):
        """
        Setter for property: (bool) CreateFlatPatternHoleDetailsLabel
         Returns the create flat pattern hole details label setting.  
            
         
        """
        pass
    @property
    def CreateFlatPatternJoggleLabel(self) -> bool:
        """
        Getter for property: (bool) CreateFlatPatternJoggleLabel
         Returns the create flat pattern joggle label setting.  
            
         
        """
        pass
    @CreateFlatPatternJoggleLabel.setter
    def CreateFlatPatternJoggleLabel(self, createFlatPatternJoggleLabel: bool):
        """
        Setter for property: (bool) CreateFlatPatternJoggleLabel
         Returns the create flat pattern joggle label setting.  
            
         
        """
        pass
    @property
    def CreateFlatPatternLighteningCutoutLabel(self) -> bool:
        """
        Getter for property: (bool) CreateFlatPatternLighteningCutoutLabel
         Returns the create flat pattern lightening cutout label setting.  
            
         
        """
        pass
    @CreateFlatPatternLighteningCutoutLabel.setter
    def CreateFlatPatternLighteningCutoutLabel(self, createFlatPatternLCutoutLabel: bool):
        """
        Setter for property: (bool) CreateFlatPatternLighteningCutoutLabel
         Returns the create flat pattern lightening cutout label setting.  
            
         
        """
        pass
    @property
    def CreateFlatPatternNote(self) -> bool:
        """
        Getter for property: (bool) CreateFlatPatternNote
         Returns the create flat pattern note setting.  
            
         
        """
        pass
    @CreateFlatPatternNote.setter
    def CreateFlatPatternNote(self, createFlatPatternNote: bool):
        """
        Setter for property: (bool) CreateFlatPatternNote
         Returns the create flat pattern note setting.  
            
         
        """
        pass
    @property
    def CreateFlatPatternToolIDLabel(self) -> bool:
        """
        Getter for property: (bool) CreateFlatPatternToolIDLabel
         Returns the create flat pattern tool id label setting.  
            
         
        """
        pass
    @CreateFlatPatternToolIDLabel.setter
    def CreateFlatPatternToolIDLabel(self, createFlatPatternToolIdLabel: bool):
        """
        Setter for property: (bool) CreateFlatPatternToolIDLabel
         Returns the create flat pattern tool id label setting.  
            
         
        """
        pass
    @property
    def DecimalPlaces(self) -> int:
        """
        Getter for property: (int) DecimalPlaces
         Returns the decimal places setting.  
           Only values from 0 to 6 are valid.  
         
        """
        pass
    @DecimalPlaces.setter
    def DecimalPlaces(self, decimalPlaces: int):
        """
        Setter for property: (int) DecimalPlaces
         Returns the decimal places setting.  
           Only values from 0 to 6 are valid.  
         
        """
        pass
    @property
    def FlatPatternHoleDetailsPrefix(self) -> str:
        """
        Getter for property: (str) FlatPatternHoleDetailsPrefix
         Returns the prefix characters for flat pattern hole details label.  
            
         
        """
        pass
    @FlatPatternHoleDetailsPrefix.setter
    def FlatPatternHoleDetailsPrefix(self, prefix: str):
        """
        Setter for property: (str) FlatPatternHoleDetailsPrefix
         Returns the prefix characters for flat pattern hole details label.  
            
         
        """
        pass
    @property
    def FlatPatternHoleDetailsSuffix(self) -> str:
        """
        Getter for property: (str) FlatPatternHoleDetailsSuffix
         Returns the suffix characters for flat pattern hole details label.  
            
         
        """
        pass
    @FlatPatternHoleDetailsSuffix.setter
    def FlatPatternHoleDetailsSuffix(self, suffix: str):
        """
        Setter for property: (str) FlatPatternHoleDetailsSuffix
         Returns the suffix characters for flat pattern hole details label.  
            
         
        """
        pass
    @property
    def FlatPatternToolIDPrefix(self) -> str:
        """
        Getter for property: (str) FlatPatternToolIDPrefix
         Returns the prefix characters for flat pattern tool ID label.  
            
         
        """
        pass
    @FlatPatternToolIDPrefix.setter
    def FlatPatternToolIDPrefix(self, prefix: str):
        """
        Setter for property: (str) FlatPatternToolIDPrefix
         Returns the prefix characters for flat pattern tool ID label.  
            
         
        """
        pass
    @property
    def FlatPatternToolIDSuffix(self) -> str:
        """
        Getter for property: (str) FlatPatternToolIDSuffix
         Returns the suffix characters for flat pattern tool ID label.  
            
         
        """
        pass
    @FlatPatternToolIDSuffix.setter
    def FlatPatternToolIDSuffix(self, suffix: str):
        """
        Setter for property: (str) FlatPatternToolIDSuffix
         Returns the suffix characters for flat pattern tool ID label.  
            
         
        """
        pass
    @property
    def IncludeBendAngle(self) -> bool:
        """
        Getter for property: (bool) IncludeBendAngle
         Returns the include bend angle setting.  
            
         
        """
        pass
    @IncludeBendAngle.setter
    def IncludeBendAngle(self, includeBendAngle: bool):
        """
        Setter for property: (bool) IncludeBendAngle
         Returns the include bend angle setting.  
            
         
        """
        pass
    @property
    def IncludeBendRadius(self) -> bool:
        """
        Getter for property: (bool) IncludeBendRadius
         Returns the include bend radius setting.  
            
         
        """
        pass
    @IncludeBendRadius.setter
    def IncludeBendRadius(self, includeBendRadius: bool):
        """
        Setter for property: (bool) IncludeBendRadius
         Returns the include bend radius setting.  
            
         
        """
        pass
    @property
    def IncludeCutoutDiameterInFlatPatternLabel(self) -> bool:
        """
        Getter for property: (bool) IncludeCutoutDiameterInFlatPatternLabel
         Returns the include cutout diameter in flat pattern lightening cutout setting.  
            
         
        """
        pass
    @IncludeCutoutDiameterInFlatPatternLabel.setter
    def IncludeCutoutDiameterInFlatPatternLabel(self, includeCutoutDiameter: bool):
        """
        Setter for property: (bool) IncludeCutoutDiameterInFlatPatternLabel
         Returns the include cutout diameter in flat pattern lightening cutout setting.  
            
         
        """
        pass
    @property
    def IncludeHoleDiameterInFlatPatternLabel(self) -> bool:
        """
        Getter for property: (bool) IncludeHoleDiameterInFlatPatternLabel
         Returns the include hole diameter in flat pattern lightening cutout label setting.  
            
         
        """
        pass
    @IncludeHoleDiameterInFlatPatternLabel.setter
    def IncludeHoleDiameterInFlatPatternLabel(self, includeHoleDiameter: bool):
        """
        Setter for property: (bool) IncludeHoleDiameterInFlatPatternLabel
         Returns the include hole diameter in flat pattern lightening cutout label setting.  
            
         
        """
        pass
    @property
    def IncludeJoggleDepthInFlatPatternLabel(self) -> bool:
        """
        Getter for property: (bool) IncludeJoggleDepthInFlatPatternLabel
         Returns the include joggle depth in flat pattern joggle label setting.  
            
         
        """
        pass
    @IncludeJoggleDepthInFlatPatternLabel.setter
    def IncludeJoggleDepthInFlatPatternLabel(self, includeJoggleDepth: bool):
        """
        Setter for property: (bool) IncludeJoggleDepthInFlatPatternLabel
         Returns the include joggle depth in flat pattern joggle label setting.  
            
         
        """
        pass
    @property
    def IncludeJoggleRunoutInFlatPatternLabel(self) -> bool:
        """
        Getter for property: (bool) IncludeJoggleRunoutInFlatPatternLabel
         Returns the include joggle runout in flat pattern joggle label setting.  
            
         
        """
        pass
    @IncludeJoggleRunoutInFlatPatternLabel.setter
    def IncludeJoggleRunoutInFlatPatternLabel(self, includeJoggleRunout: bool):
        """
        Setter for property: (bool) IncludeJoggleRunoutInFlatPatternLabel
         Returns the include joggle runout in flat pattern joggle label setting.  
            
         
        """
        pass
    @property
    def IncludeMaterial(self) -> bool:
        """
        Getter for property: (bool) IncludeMaterial
         Returns the include sm material setting.  
            
         
        """
        pass
    @IncludeMaterial.setter
    def IncludeMaterial(self, includeSmMaterial: bool):
        """
        Setter for property: (bool) IncludeMaterial
         Returns the include sm material setting.  
            
         
        """
        pass
    @property
    def IncludeNeutralFactor(self) -> bool:
        """
        Getter for property: (bool) IncludeNeutralFactor
         Returns the include neutral factor setting.  
            
         
        """
        pass
    @IncludeNeutralFactor.setter
    def IncludeNeutralFactor(self, includeNeutralFactor: bool):
        """
        Setter for property: (bool) IncludeNeutralFactor
         Returns the include neutral factor setting.  
            
         
        """
        pass
    @property
    def IncludePhysicalMaterial(self) -> bool:
        """
        Getter for property: (bool) IncludePhysicalMaterial
         Returns the include physical material setting.  
            
         
        """
        pass
    @IncludePhysicalMaterial.setter
    def IncludePhysicalMaterial(self, includePhysicalMaterial: bool):
        """
        Setter for property: (bool) IncludePhysicalMaterial
         Returns the include physical material setting.  
            
         
        """
        pass
    @property
    def IncludeThickness(self) -> bool:
        """
        Getter for property: (bool) IncludeThickness
         Returns the include material thickness setting.  
            
         
        """
        pass
    @IncludeThickness.setter
    def IncludeThickness(self, includeMaterialhickness: bool):
        """
        Setter for property: (bool) IncludeThickness
         Returns the include material thickness setting.  
            
         
        """
        pass
    @property
    def LabelPlacementType(self) -> SheetMetalPMISettingsBuilder.LabelPlacementTypes:
        """
        Getter for property: ( SheetMetalPMISettingsBuilder.LabelPlacementTypes NXOpen.S) LabelPlacementType
         Returns the sheet metal pmi orientation   
            
         
        """
        pass
    @LabelPlacementType.setter
    def LabelPlacementType(self, labelPlacementType: SheetMetalPMISettingsBuilder.LabelPlacementTypes):
        """
        Setter for property: ( SheetMetalPMISettingsBuilder.LabelPlacementTypes NXOpen.S) LabelPlacementType
         Returns the sheet metal pmi orientation   
            
         
        """
        pass
    @property
    def PmiLabelType(self) -> SheetMetalPMISettingsBuilder.SmPmiType:
        """
        Getter for property: ( SheetMetalPMISettingsBuilder.SmPmiType NXOpen.S) PmiLabelType
         Returns the sheet metal pmi type   
            
         
        """
        pass
    @PmiLabelType.setter
    def PmiLabelType(self, type: SheetMetalPMISettingsBuilder.SmPmiType):
        """
        Setter for property: ( SheetMetalPMISettingsBuilder.SmPmiType NXOpen.S) PmiLabelType
         Returns the sheet metal pmi type   
            
         
        """
        pass
    @property
    def PmiLayer(self) -> int:
        """
        Getter for property: (int) PmiLayer
         Returns the flat pattern PMI layer setting.  
           Only values from  to 256 (both inclusive) are valid.  
         
        """
        pass
    @PmiLayer.setter
    def PmiLayer(self, layer: int):
        """
        Setter for property: (int) PmiLayer
         Returns the flat pattern PMI layer setting.  
           Only values from  to 256 (both inclusive) are valid.  
         
        """
        pass
    @property
    def PmiLayerOption(self) -> SheetMetalPMISettingsBuilder.PmiLayerOptions:
        """
        Getter for property: ( SheetMetalPMISettingsBuilder.PmiLayerOptions NXOpen.S) PmiLayerOption
         Returns the layer option.  
            
         
        """
        pass
    @PmiLayerOption.setter
    def PmiLayerOption(self, layerOption: SheetMetalPMISettingsBuilder.PmiLayerOptions):
        """
        Setter for property: ( SheetMetalPMISettingsBuilder.PmiLayerOptions NXOpen.S) PmiLayerOption
         Returns the layer option.  
            
         
        """
        pass
    @property
    def PmiNoteType(self) -> SheetMetalPMISettingsBuilder.SmPmiNoteType:
        """
        Getter for property: ( SheetMetalPMISettingsBuilder.SmPmiNoteType NXOpen.S) PmiNoteType
         Returns the sheet metal pmi note type   
            
         
        """
        pass
    @PmiNoteType.setter
    def PmiNoteType(self, type: SheetMetalPMISettingsBuilder.SmPmiNoteType):
        """
        Setter for property: ( SheetMetalPMISettingsBuilder.SmPmiNoteType NXOpen.S) PmiNoteType
         Returns the sheet metal pmi note type   
            
         
        """
        pass
    @property
    def ThroughHoleText(self) -> str:
        """
        Getter for property: (str) ThroughHoleText
         Returns the text for through hole in flat pattern hole details label.  
            
         
        """
        pass
    @ThroughHoleText.setter
    def ThroughHoleText(self, throughHoleText: str):
        """
        Setter for property: (str) ThroughHoleText
         Returns the text for through hole in flat pattern hole details label.  
            
         
        """
        pass
    def GetFlatPatternBendParameters(self) -> List[SheetMetalPMISettingsBuilder.BendParameters]:
        """
         Returns flat pattern bend labels 
         Returns fpBendParameters ( SheetMetalPMISettingsBuilder.BendParameters List[NXOpen): .
        """
        pass
    def GetFlatPatternPropertiesNote(self) -> List[SheetMetalPMISettingsBuilder.FpProperties]:
        """
         Returns flat pattern properties note 
         Returns fpProperties ( SheetMetalPMISettingsBuilder.FpProperties List[NXOpen): .
        """
        pass
    def GetPrefixForBendParameterType(self, parameterType: SheetMetalPMISettingsBuilder.BendParameterType) -> str:
        """
         Gets prefix for bend parameter type.
         Returns prefix (str): .
        """
        pass
    def GetPrefixForBodyParameterType(self, parameterType: SheetMetalPMISettingsBuilder.BodyParameterType) -> str:
        """
         Gets prefix for body parameter type.
         Returns prefix (str): .
        """
        pass
    def GetPrefixForFlatPatternBendDataType(self, parameterType: SheetMetalPMISettingsBuilder.FlatpatternBendDataType) -> str:
        """
         Gets prefix for flat pattern bend data type.
         Returns prefix (str): .
        """
        pass
    def GetPrefixForFlatPatternJogggleParameterType(self, parameterType: SheetMetalPMISettingsBuilder.FlatpatternJoggleParametersType) -> str:
        """
         Gets prefix for flat pattern joggle parameter type.
         Returns prefix (str): .
        """
        pass
    def GetPrefixForFlatPatternLighteningCutoutParameterType(self, parameterType: SheetMetalPMISettingsBuilder.FlatpatternLighteningCutoutParametersType) -> str:
        """
         Gets prefix for flat pattern lightening cutout parameter type.
         Returns prefix (str): .
        """
        pass
    def GetPrefixForFlatPatternNotePropertiesType(self, parameterType: SheetMetalPMISettingsBuilder.FlatpatternNotePropertiesType) -> str:
        """
         Gets prefix for flat pattern note properties type.
         Returns prefix (str): .
        """
        pass
    def GetSuffixForBendParameterType(self, parameterType: SheetMetalPMISettingsBuilder.BendParameterType) -> str:
        """
         Gets suffix for bend parameter type.
         Returns suffix (str): .
        """
        pass
    def GetSuffixForBodyParameterType(self, parameterType: SheetMetalPMISettingsBuilder.BodyParameterType) -> str:
        """
         Gets suffix for body parameter type.
         Returns suffix (str): .
        """
        pass
    def GetSuffixForFlatPatternBendDataType(self, parameterType: SheetMetalPMISettingsBuilder.FlatpatternBendDataType) -> str:
        """
         Gets suffix for flat pattern bend data type.
         Returns suffix (str): .
        """
        pass
    def GetSuffixForFlatPatternJogggleParameterType(self, parameterType: SheetMetalPMISettingsBuilder.FlatpatternJoggleParametersType) -> str:
        """
         Gets suffix for flat pattern joggle parameter type.
         Returns suffix (str): .
        """
        pass
    def GetSuffixForFlatPatternLighteningCutoutParameterType(self, parameterType: SheetMetalPMISettingsBuilder.FlatpatternLighteningCutoutParametersType) -> str:
        """
         Gets suffix for flat pattern lightening cutout parameter type.
         Returns suffix (str): .
        """
        pass
    def GetSuffixForFlatPatternNotePropertiesType(self, parameterType: SheetMetalPMISettingsBuilder.FlatpatternNotePropertiesType) -> str:
        """
         Gets suffix for flat pattern note properties type.
         Returns suffix (str): .
        """
        pass
    def SetFlatPatternBendParameters(self, fpBendParameters: List[SheetMetalPMISettingsBuilder.BendParameters]) -> None:
        """
         Sets flat pattern bend labels 
        """
        pass
    def SetFlatPatternPropertiesNote(self, fpProperties: List[SheetMetalPMISettingsBuilder.FpProperties]) -> None:
        """
         Sets flat pattern properties note
        """
        pass
    def SetPrefixForBendParameterType(self, parameterType: SheetMetalPMISettingsBuilder.BendParameterType, prefix: str) -> None:
        """
         Sets prefix for bend parameter type.
        """
        pass
    def SetPrefixForBodyParameterType(self, parameterType: SheetMetalPMISettingsBuilder.BodyParameterType, prefix: str) -> None:
        """
         Sets prefix for body parameter type.
        """
        pass
    def SetPrefixForFlatPatternBendDataType(self, parameterType: SheetMetalPMISettingsBuilder.FlatpatternBendDataType, prefix: str) -> None:
        """
         Sets prefix for flat pattern bend data type.
        """
        pass
    def SetPrefixForFlatPatternJoggleParameterType(self, parameterType: SheetMetalPMISettingsBuilder.FlatpatternJoggleParametersType, prefix: str) -> None:
        """
         Sets prefix for flat pattern joggle parameter type.
        """
        pass
    def SetPrefixForFlatPatternLighteningCutoutParameterType(self, parameterType: SheetMetalPMISettingsBuilder.FlatpatternLighteningCutoutParametersType, prefix: str) -> None:
        """
         Sets prefix for flat pattern lightening cutout parameter type.
        """
        pass
    def SetPrefixForFlatPatternNotePropertiesType(self, parameterType: SheetMetalPMISettingsBuilder.FlatpatternNotePropertiesType, prefix: str) -> None:
        """
         Sets prefix for flat pattern note properties type.
        """
        pass
    def SetSuffixForBendParameterType(self, parameterType: SheetMetalPMISettingsBuilder.BendParameterType, suffix: str) -> None:
        """
         Sets suffix for bend parameter type.
        """
        pass
    def SetSuffixForBodyParameterType(self, parameterType: SheetMetalPMISettingsBuilder.BodyParameterType, suffix: str) -> None:
        """
         Sets suffix for body parameter type.
        """
        pass
    def SetSuffixForFlatPatternBendDataType(self, parameterType: SheetMetalPMISettingsBuilder.FlatpatternBendDataType, suffix: str) -> None:
        """
         Sets suffix for flat pattern bend data type.
        """
        pass
    def SetSuffixForFlatPatternJoggleParameterType(self, parameterType: SheetMetalPMISettingsBuilder.FlatpatternJoggleParametersType, suffix: str) -> None:
        """
         Sets suffix for flat pattern joggle parameter type.
        """
        pass
    def SetSuffixForFlatPatternLighteningCutoutParameterType(self, parameterType: SheetMetalPMISettingsBuilder.FlatpatternLighteningCutoutParametersType, suffix: str) -> None:
        """
         Sets suffix for flat pattern lightening cutout parameter type.
        """
        pass
    def SetSuffixForFlatPatternNotePropertiesType(self, parameterType: SheetMetalPMISettingsBuilder.FlatpatternNotePropertiesType, suffix: str) -> None:
        """
         Sets suffix for flat pattern note properties type.
        """
        pass
