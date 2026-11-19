from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class DrawDirectionBuilder(NXOpen.Builder): 
    """ Represents a Builder for DrawDirectionBuilder functionality"""
    class DrawDirection(Enum):
        """
        Members Include: 
         |Vector|  vector; 
         |Orientation|  orientation; 

        """
        Vector: int
        Orientation: int
        @staticmethod
        def ValueOf(value: int) -> DrawDirectionBuilder.DrawDirection:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DrawOption(self) -> DrawDirectionBuilder.DrawDirection:
        """
        Getter for property: ( DrawDirectionBuilder.DrawDirection NXOpen.Pla) DrawOption
         Returns the preference   
            
         
        """
        pass
    @DrawOption.setter
    def DrawOption(self, drawOption: DrawDirectionBuilder.DrawDirection):
        """
        Setter for property: ( DrawDirectionBuilder.DrawDirection NXOpen.Pla) DrawOption
         Returns the preference   
            
         
        """
        pass
    @property
    def DrawOrientation(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: ( NXOpen.Matrix3x3) DrawOrientation
         Returns the orientation   
            
         
        """
        pass
    @DrawOrientation.setter
    def DrawOrientation(self, drawOrientation: NXOpen.Matrix3x3):
        """
        Setter for property: ( NXOpen.Matrix3x3) DrawOrientation
         Returns the orientation   
            
         
        """
        pass
    @property
    def DrawOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) DrawOrigin
         Returns the draw origin   
            
         
        """
        pass
    @DrawOrigin.setter
    def DrawOrigin(self, drawOrigin: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) DrawOrigin
         Returns the draw origin   
            
         
        """
        pass
    @property
    def DrawVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) DrawVector
         Returns the vector   
            
         
        """
        pass
    @DrawVector.setter
    def DrawVector(self, vector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) DrawVector
         Returns the vector   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class IdentifierDataBuilder(NXOpen.TaggedObject): 
    """ Identifier Data. This represents data used for a identifier element in 
        a PlasticDesigner.IdentifierDataBuilder """
    @property
    def Faces(self) -> NXOpen.SelectFaceList:
        """
        Getter for property: ( NXOpen.SelectFaceList) Faces
         Returns the face selection list   
            
         
        """
        pass
    @property
    def HighlightColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) HighlightColor
         Returns the highlight color   
            
         
        """
        pass
    @HighlightColor.setter
    def HighlightColor(self, highlightColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) HighlightColor
         Returns the highlight color   
            
         
        """
        pass
    @property
    def HighlightStatus(self) -> bool:
        """
        Getter for property: (bool) HighlightStatus
         Returns the highlight status   
            
         
        """
        pass
    @HighlightStatus.setter
    def HighlightStatus(self, isHighlighted: bool):
        """
        Setter for property: (bool) HighlightStatus
         Returns the highlight status   
            
         
        """
        pass
    @property
    def Label(self) -> str:
        """
        Getter for property: (str) Label
         Returns the label   
            
         
        """
        pass
    @Label.setter
    def Label(self, label: str):
        """
        Setter for property: (str) Label
         Returns the label   
            
         
        """
        pass
import NXOpen
class Manager(NXOpen.Object): 
    """ Represents the Plastic Designer Manager class."""
    def CreateDrawDirectionBuilder(part: NXOpen.Part) -> DrawDirectionBuilder:
        """
         Creates a PlasticDesigner.DrawDirectionBuilder 
         Returns builder ( DrawDirectionBuilder NXOpen.Pla):  Plastic Designer DrawDirectionBuilder Builder.
        """
        pass
    def CreatePreferencesBuilder(part: NXOpen.Part) -> PreferencesBuilder:
        """
         Creates a PlasticDesigner.PreferencesBuilder 
         Returns builder ( PreferencesBuilder NXOpen.Pla):  Plastic Designer Preferences Builder.
        """
        pass
    def CreateSurfaceIdentifierBuilder(part: NXOpen.Part) -> SurfaceIdentifierBuilder:
        """
         Creates a PlasticDesigner.SurfaceIdentifierBuilder 
         Returns builder ( SurfaceIdentifierBuilder NXOpen.Pla):  Surface Identifier Builder.
        """
        pass
    def PerformFeatureValidation(body: NXOpen.Body) -> None:
        """
         Performs Feature Validation 
        """
        pass
    def PerformMoldabilityValidation(body: NXOpen.Body) -> None:
        """
         Performs Moldability Validation 
        """
        pass
import NXOpen
class PreferencesBuilder(NXOpen.Builder): 
    """ Plastic Plastic Application Manager"""
    @property
    def BossBaseRadiusToNominalWallThickness(self) -> bool:
        """
        Getter for property: (bool) BossBaseRadiusToNominalWallThickness
         Returns the boss feature validation base radius to nominal wall thickness ratio   
            
         
        """
        pass
    @BossBaseRadiusToNominalWallThickness.setter
    def BossBaseRadiusToNominalWallThickness(self, bossBaseRadiusToNominalWallThick: bool):
        """
        Setter for property: (bool) BossBaseRadiusToNominalWallThickness
         Returns the boss feature validation base radius to nominal wall thickness ratio   
            
         
        """
        pass
    @property
    def BossBaseRadiusToNominalWallThicknessLimit(self) -> float:
        """
        Getter for property: (float) BossBaseRadiusToNominalWallThicknessLimit
         Returns the boss feature validation base radius to nominal wall thickness ratio limit   
            
         
        """
        pass
    @BossBaseRadiusToNominalWallThicknessLimit.setter
    def BossBaseRadiusToNominalWallThicknessLimit(self, bossBaseRadiusToNominalWallThickLimit: float):
        """
        Setter for property: (float) BossBaseRadiusToNominalWallThicknessLimit
         Returns the boss feature validation base radius to nominal wall thickness ratio limit   
            
         
        """
        pass
    @property
    def BossColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) BossColor
         Returns the boss feature validation color   
            
         
        """
        pass
    @BossColor.setter
    def BossColor(self, bossColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) BossColor
         Returns the boss feature validation color   
            
         
        """
        pass
    @property
    def BossHeightToNominalWallThickness(self) -> bool:
        """
        Getter for property: (bool) BossHeightToNominalWallThickness
         Returns the boss feature validation height to nominal wall thickness ratio   
            
         
        """
        pass
    @BossHeightToNominalWallThickness.setter
    def BossHeightToNominalWallThickness(self, heightToNominalWallThickness: bool):
        """
        Setter for property: (bool) BossHeightToNominalWallThickness
         Returns the boss feature validation height to nominal wall thickness ratio   
            
         
        """
        pass
    @property
    def BossHeightToNominalWallThicknessLimit(self) -> float:
        """
        Getter for property: (float) BossHeightToNominalWallThicknessLimit
         Returns the boss feature validation height to nominal wall thickness ratio limit   
            
         
        """
        pass
    @BossHeightToNominalWallThicknessLimit.setter
    def BossHeightToNominalWallThicknessLimit(self, heightToNominalWallThicknessLimit: float):
        """
        Setter for property: (float) BossHeightToNominalWallThicknessLimit
         Returns the boss feature validation height to nominal wall thickness ratio limit   
            
         
        """
        pass
    @property
    def BossHeightToOuterDiameter(self) -> bool:
        """
        Getter for property: (bool) BossHeightToOuterDiameter
         Returns the boss feature validation height to outer diameter ratio   
            
         
        """
        pass
    @BossHeightToOuterDiameter.setter
    def BossHeightToOuterDiameter(self, heightToOuterDiameter: bool):
        """
        Setter for property: (bool) BossHeightToOuterDiameter
         Returns the boss feature validation height to outer diameter ratio   
            
         
        """
        pass
    @property
    def BossHeightToOuterDiameterLimit(self) -> float:
        """
        Getter for property: (float) BossHeightToOuterDiameterLimit
         Returns the boss feature validation height to outer diameter ratio limit   
            
         
        """
        pass
    @BossHeightToOuterDiameterLimit.setter
    def BossHeightToOuterDiameterLimit(self, heightToOuterDiameterLimit: float):
        """
        Setter for property: (float) BossHeightToOuterDiameterLimit
         Returns the boss feature validation height to outer diameter ratio limit   
            
         
        """
        pass
    @property
    def BossMaximumOuterToInnerDiameterThickness(self) -> bool:
        """
        Getter for property: (bool) BossMaximumOuterToInnerDiameterThickness
         Returns the boss feature validation maximum outer to inner diameter thickness   
            
         
        """
        pass
    @BossMaximumOuterToInnerDiameterThickness.setter
    def BossMaximumOuterToInnerDiameterThickness(self, outerToInnerDiameterThick: bool):
        """
        Setter for property: (bool) BossMaximumOuterToInnerDiameterThickness
         Returns the boss feature validation maximum outer to inner diameter thickness   
            
         
        """
        pass
    @property
    def BossMaximumOuterToInnerDiameterThicknessLimit(self) -> float:
        """
        Getter for property: (float) BossMaximumOuterToInnerDiameterThicknessLimit
         Returns the boss feature validation maximum outer to inner diameter thickness limit   
            
         
        """
        pass
    @BossMaximumOuterToInnerDiameterThicknessLimit.setter
    def BossMaximumOuterToInnerDiameterThicknessLimit(self, outerToInnerDiameterThickLimit: float):
        """
        Setter for property: (float) BossMaximumOuterToInnerDiameterThicknessLimit
         Returns the boss feature validation maximum outer to inner diameter thickness limit   
            
         
        """
        pass
    @property
    def BossMinimumDraftOnInnerDiameter(self) -> bool:
        """
        Getter for property: (bool) BossMinimumDraftOnInnerDiameter
         Returns the boss feature validation minimum draft on inner diameter   
            
         
        """
        pass
    @BossMinimumDraftOnInnerDiameter.setter
    def BossMinimumDraftOnInnerDiameter(self, bossDraftOnInnerDia: bool):
        """
        Setter for property: (bool) BossMinimumDraftOnInnerDiameter
         Returns the boss feature validation minimum draft on inner diameter   
            
         
        """
        pass
    @property
    def BossMinimumDraftOnInnerDiameterLimit(self) -> float:
        """
        Getter for property: (float) BossMinimumDraftOnInnerDiameterLimit
         Returns the boss feature validation minimum draft on inner diameter limit   
            
         
        """
        pass
    @BossMinimumDraftOnInnerDiameterLimit.setter
    def BossMinimumDraftOnInnerDiameterLimit(self, bossDraftOnInnerDiaLimit: float):
        """
        Setter for property: (float) BossMinimumDraftOnInnerDiameterLimit
         Returns the boss feature validation minimum draft on inner diameter limit   
            
         
        """
        pass
    @property
    def BossMinimumDraftOnOuterDiameter(self) -> bool:
        """
        Getter for property: (bool) BossMinimumDraftOnOuterDiameter
         Returns the boss feature validation minimum draft on outer diameter   
            
         
        """
        pass
    @BossMinimumDraftOnOuterDiameter.setter
    def BossMinimumDraftOnOuterDiameter(self, bossDraftOnOuterDia: bool):
        """
        Setter for property: (bool) BossMinimumDraftOnOuterDiameter
         Returns the boss feature validation minimum draft on outer diameter   
            
         
        """
        pass
    @property
    def BossMinimumDraftOnOuterDiameterLimit(self) -> float:
        """
        Getter for property: (float) BossMinimumDraftOnOuterDiameterLimit
         Returns the boss feature validation minimum draft on outer diameter limit   
            
         
        """
        pass
    @BossMinimumDraftOnOuterDiameterLimit.setter
    def BossMinimumDraftOnOuterDiameterLimit(self, bossDraftOnOuterDiaLimit: float):
        """
        Setter for property: (float) BossMinimumDraftOnOuterDiameterLimit
         Returns the boss feature validation minimum draft on outer diameter limit   
            
         
        """
        pass
    @property
    def BossMinimumRadiusAtBase(self) -> bool:
        """
        Getter for property: (bool) BossMinimumRadiusAtBase
         Returns the boss feature validation minimum radius at base   
            
         
        """
        pass
    @BossMinimumRadiusAtBase.setter
    def BossMinimumRadiusAtBase(self, radiusAtBase: bool):
        """
        Setter for property: (bool) BossMinimumRadiusAtBase
         Returns the boss feature validation minimum radius at base   
            
         
        """
        pass
    @property
    def BossMinimumRadiusAtBaseLimit(self) -> float:
        """
        Getter for property: (float) BossMinimumRadiusAtBaseLimit
         Returns the boss feature validation minimum radius at base limit   
            
         
        """
        pass
    @BossMinimumRadiusAtBaseLimit.setter
    def BossMinimumRadiusAtBaseLimit(self, radiusAtBaseLimit: float):
        """
        Setter for property: (float) BossMinimumRadiusAtBaseLimit
         Returns the boss feature validation minimum radius at base limit   
            
         
        """
        pass
    @property
    def BossMinimumRadiusAtTop(self) -> bool:
        """
        Getter for property: (bool) BossMinimumRadiusAtTop
         Returns the boss feature validation minimum radius at top   
            
         
        """
        pass
    @BossMinimumRadiusAtTop.setter
    def BossMinimumRadiusAtTop(self, radiusAtTop: bool):
        """
        Setter for property: (bool) BossMinimumRadiusAtTop
         Returns the boss feature validation minimum radius at top   
            
         
        """
        pass
    @property
    def BossMinimumRadiusAtTopLimit(self) -> float:
        """
        Getter for property: (float) BossMinimumRadiusAtTopLimit
         Returns the boss feature validation minimum radius at top limit   
            
         
        """
        pass
    @BossMinimumRadiusAtTopLimit.setter
    def BossMinimumRadiusAtTopLimit(self, radiusAtTopLimit: float):
        """
        Setter for property: (float) BossMinimumRadiusAtTopLimit
         Returns the boss feature validation minimum radius at top limit   
            
         
        """
        pass
    @property
    def BossMinimumWallDistance(self) -> bool:
        """
        Getter for property: (bool) BossMinimumWallDistance
         Returns the boss feature validation minimum wall distance   
            
         
        """
        pass
    @BossMinimumWallDistance.setter
    def BossMinimumWallDistance(self, minimumWallDistance: bool):
        """
        Setter for property: (bool) BossMinimumWallDistance
         Returns the boss feature validation minimum wall distance   
            
         
        """
        pass
    @property
    def BossMinimumWallDistanceLimit(self) -> float:
        """
        Getter for property: (float) BossMinimumWallDistanceLimit
         Returns the boss feature validation minimum wall distance limit   
            
         
        """
        pass
    @BossMinimumWallDistanceLimit.setter
    def BossMinimumWallDistanceLimit(self, minimumWallDistanceLimit: float):
        """
        Setter for property: (float) BossMinimumWallDistanceLimit
         Returns the boss feature validation minimum wall distance limit   
            
         
        """
        pass
    @property
    def BossOuterToInnerDiameter(self) -> bool:
        """
        Getter for property: (bool) BossOuterToInnerDiameter
         Returns the boss feature validation outer to inner diameter ratio   
            
         
        """
        pass
    @BossOuterToInnerDiameter.setter
    def BossOuterToInnerDiameter(self, outerToInnerDiameter: bool):
        """
        Setter for property: (bool) BossOuterToInnerDiameter
         Returns the boss feature validation outer to inner diameter ratio   
            
         
        """
        pass
    @property
    def BossOuterToInnerDiameterLimit(self) -> float:
        """
        Getter for property: (float) BossOuterToInnerDiameterLimit
         Returns the boss feature validation outer to inner diameter ratio limit   
            
         
        """
        pass
    @BossOuterToInnerDiameterLimit.setter
    def BossOuterToInnerDiameterLimit(self, outerToInnerDiameterLimit: float):
        """
        Setter for property: (float) BossOuterToInnerDiameterLimit
         Returns the boss feature validation outer to inner diameter ratio limit   
            
         
        """
        pass
    @property
    def HousingColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) HousingColor
         Returns the housing feature validation color   
            
         
        """
        pass
    @HousingColor.setter
    def HousingColor(self, housingColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) HousingColor
         Returns the housing feature validation color   
            
         
        """
        pass
    @property
    def HousingMaximumThicknessAtBase(self) -> bool:
        """
        Getter for property: (bool) HousingMaximumThicknessAtBase
         Returns the housing feature validation maximum thickness at base   
            
         
        """
        pass
    @HousingMaximumThicknessAtBase.setter
    def HousingMaximumThicknessAtBase(self, housingMaximumThicknessAtBase: bool):
        """
        Setter for property: (bool) HousingMaximumThicknessAtBase
         Returns the housing feature validation maximum thickness at base   
            
         
        """
        pass
    @property
    def HousingMaximumThicknessAtBaseLimit(self) -> float:
        """
        Getter for property: (float) HousingMaximumThicknessAtBaseLimit
         Returns the housing feature validation maximum thickness at base limit   
            
         
        """
        pass
    @HousingMaximumThicknessAtBaseLimit.setter
    def HousingMaximumThicknessAtBaseLimit(self, housingMaximumThicknessAtBaseLimit: float):
        """
        Setter for property: (float) HousingMaximumThicknessAtBaseLimit
         Returns the housing feature validation maximum thickness at base limit   
            
         
        """
        pass
    @property
    def HousingMinimumDraftOnLifterSideFaces(self) -> bool:
        """
        Getter for property: (bool) HousingMinimumDraftOnLifterSideFaces
         Returns the housing feature validation minimum draft on lifter side faces   
            
         
        """
        pass
    @HousingMinimumDraftOnLifterSideFaces.setter
    def HousingMinimumDraftOnLifterSideFaces(self, housingMinimumDraftOnLifterFaces: bool):
        """
        Setter for property: (bool) HousingMinimumDraftOnLifterSideFaces
         Returns the housing feature validation minimum draft on lifter side faces   
            
         
        """
        pass
    @property
    def HousingMinimumDraftOnLifterSideFacesLimit(self) -> float:
        """
        Getter for property: (float) HousingMinimumDraftOnLifterSideFacesLimit
         Returns the housing feature validation minimum draft on lifter side faces limit   
            
         
        """
        pass
    @HousingMinimumDraftOnLifterSideFacesLimit.setter
    def HousingMinimumDraftOnLifterSideFacesLimit(self, housingMinimumDraftOnLifterFacesLimit: float):
        """
        Setter for property: (float) HousingMinimumDraftOnLifterSideFacesLimit
         Returns the housing feature validation minimum draft on lifter side faces limit   
            
         
        """
        pass
    @property
    def HousingMinimumDraftOnOuterFaces(self) -> bool:
        """
        Getter for property: (bool) HousingMinimumDraftOnOuterFaces
         Returns the housing feature validation minimum draft on outer faces   
            
         
        """
        pass
    @HousingMinimumDraftOnOuterFaces.setter
    def HousingMinimumDraftOnOuterFaces(self, housingMinimumDraftOnOuterFaces: bool):
        """
        Setter for property: (bool) HousingMinimumDraftOnOuterFaces
         Returns the housing feature validation minimum draft on outer faces   
            
         
        """
        pass
    @property
    def HousingMinimumDraftOnOuterFacesLimit(self) -> float:
        """
        Getter for property: (float) HousingMinimumDraftOnOuterFacesLimit
         Returns the housing feature validation minimum draft on outer faces limit   
            
         
        """
        pass
    @HousingMinimumDraftOnOuterFacesLimit.setter
    def HousingMinimumDraftOnOuterFacesLimit(self, housingMinimumDraftOnOuterFacesLimit: float):
        """
        Setter for property: (float) HousingMinimumDraftOnOuterFacesLimit
         Returns the housing feature validation minimum draft on outer faces limit   
            
         
        """
        pass
    @property
    def HousingMinimumRadiusOnInnerFaces(self) -> bool:
        """
        Getter for property: (bool) HousingMinimumRadiusOnInnerFaces
         Returns the housing feature validation minimum radius on outer edges   
            
         
        """
        pass
    @HousingMinimumRadiusOnInnerFaces.setter
    def HousingMinimumRadiusOnInnerFaces(self, housingMinimumRadiusOnInnerFaces: bool):
        """
        Setter for property: (bool) HousingMinimumRadiusOnInnerFaces
         Returns the housing feature validation minimum radius on outer edges   
            
         
        """
        pass
    @property
    def HousingMinimumRadiusOnInnerFacesLimit(self) -> float:
        """
        Getter for property: (float) HousingMinimumRadiusOnInnerFacesLimit
         Returns the housing feature validation minimum radius on outer edges limit   
            
         
        """
        pass
    @HousingMinimumRadiusOnInnerFacesLimit.setter
    def HousingMinimumRadiusOnInnerFacesLimit(self, housingMinimumRadiusOnInnerFacesLimit: float):
        """
        Setter for property: (float) HousingMinimumRadiusOnInnerFacesLimit
         Returns the housing feature validation minimum radius on outer edges limit   
            
         
        """
        pass
    @property
    def HousingMinimumRadiusOnOuterFaces(self) -> bool:
        """
        Getter for property: (bool) HousingMinimumRadiusOnOuterFaces
         Returns the housing feature validation minimum radius on outer edges   
            
         
        """
        pass
    @HousingMinimumRadiusOnOuterFaces.setter
    def HousingMinimumRadiusOnOuterFaces(self, housingMinimumRadiusOnOuterFaces: bool):
        """
        Setter for property: (bool) HousingMinimumRadiusOnOuterFaces
         Returns the housing feature validation minimum radius on outer edges   
            
         
        """
        pass
    @property
    def HousingMinimumRadiusOnOuterFacesLimit(self) -> float:
        """
        Getter for property: (float) HousingMinimumRadiusOnOuterFacesLimit
         Returns the housing feature validation minimum radius on outer edges limit   
            
         
        """
        pass
    @HousingMinimumRadiusOnOuterFacesLimit.setter
    def HousingMinimumRadiusOnOuterFacesLimit(self, housingMinimumRadiusOnOuterFacesLimit: float):
        """
        Setter for property: (float) HousingMinimumRadiusOnOuterFacesLimit
         Returns the housing feature validation minimum radius on outer edges limit   
            
         
        """
        pass
    @property
    def ManufacturingProcess(self) -> str:
        """
        Getter for property: (str) ManufacturingProcess
         Returns the manufacturing process   
            
         
        """
        pass
    @ManufacturingProcess.setter
    def ManufacturingProcess(self, manufacturingProcess: str):
        """
        Setter for property: (str) ManufacturingProcess
         Returns the manufacturing process   
            
         
        """
        pass
    @property
    def MarkAsPlasticPart(self) -> bool:
        """
        Getter for property: (bool) MarkAsPlasticPart
         Returns the mark as plastic part   
            
         
        """
        pass
    @MarkAsPlasticPart.setter
    def MarkAsPlasticPart(self, markAsPlasticPart: bool):
        """
        Setter for property: (bool) MarkAsPlasticPart
         Returns the mark as plastic part   
            
         
        """
        pass
    @property
    def NegativeDraft(self) -> bool:
        """
        Getter for property: (bool) NegativeDraft
         Returns the moldability validation negative draft   
            
         
        """
        pass
    @NegativeDraft.setter
    def NegativeDraft(self, negativeDraft: bool):
        """
        Setter for property: (bool) NegativeDraft
         Returns the moldability validation negative draft   
            
         
        """
        pass
    @property
    def NegativeDraftColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) NegativeDraftColor
         Returns the moldability validation negative draft color   
            
         
        """
        pass
    @NegativeDraftColor.setter
    def NegativeDraftColor(self, negativeDraftColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) NegativeDraftColor
         Returns the moldability validation negative draft color   
            
         
        """
        pass
    @property
    def NegativeDraftLimit(self) -> float:
        """
        Getter for property: (float) NegativeDraftLimit
         Returns the moldability validation negative draft limit   
            
         
        """
        pass
    @NegativeDraftLimit.setter
    def NegativeDraftLimit(self, negativeDraftLimit: float):
        """
        Setter for property: (float) NegativeDraftLimit
         Returns the moldability validation negative draft limit   
            
         
        """
        pass
    @property
    def PositiveDraft(self) -> bool:
        """
        Getter for property: (bool) PositiveDraft
         Returns the moldability validation positive draft   
            
         
        """
        pass
    @PositiveDraft.setter
    def PositiveDraft(self, positiveDraft: bool):
        """
        Setter for property: (bool) PositiveDraft
         Returns the moldability validation positive draft   
            
         
        """
        pass
    @property
    def PositiveDraftColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) PositiveDraftColor
         Returns the moldability validation positive draft color   
            
         
        """
        pass
    @PositiveDraftColor.setter
    def PositiveDraftColor(self, positiveDraftColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) PositiveDraftColor
         Returns the moldability validation positive draft color   
            
         
        """
        pass
    @property
    def PositiveDraftLimit(self) -> float:
        """
        Getter for property: (float) PositiveDraftLimit
         Returns the moldability validation positive draft limit   
            
         
        """
        pass
    @PositiveDraftLimit.setter
    def PositiveDraftLimit(self, positiveDraftLimit: float):
        """
        Setter for property: (float) PositiveDraftLimit
         Returns the moldability validation positive draft limit   
            
         
        """
        pass
    @property
    def RibColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) RibColor
         Returns the rib feature validation color   
            
         
        """
        pass
    @RibColor.setter
    def RibColor(self, ribColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) RibColor
         Returns the rib feature validation color   
            
         
        """
        pass
    @property
    def RibHeightToNominalWallThickness(self) -> bool:
        """
        Getter for property: (bool) RibHeightToNominalWallThickness
         Returns the rib feature validation height to nominal wall thickness ratio   
            
         
        """
        pass
    @RibHeightToNominalWallThickness.setter
    def RibHeightToNominalWallThickness(self, heightToNominalWallThickness: bool):
        """
        Setter for property: (bool) RibHeightToNominalWallThickness
         Returns the rib feature validation height to nominal wall thickness ratio   
            
         
        """
        pass
    @property
    def RibHeightToNominalWallThicknessLimit(self) -> float:
        """
        Getter for property: (float) RibHeightToNominalWallThicknessLimit
         Returns the rib feature validation height to nominal wall thickness ratio limit   
            
         
        """
        pass
    @RibHeightToNominalWallThicknessLimit.setter
    def RibHeightToNominalWallThicknessLimit(self, heightToNominalWallThicknessLimit: float):
        """
        Setter for property: (float) RibHeightToNominalWallThicknessLimit
         Returns the rib feature validation height to nominal wall thickness ratio limit   
            
         
        """
        pass
    @property
    def RibMinimumRadiusAtBase(self) -> bool:
        """
        Getter for property: (bool) RibMinimumRadiusAtBase
         Returns the rib feature validation minimum radius at base   
            
         
        """
        pass
    @RibMinimumRadiusAtBase.setter
    def RibMinimumRadiusAtBase(self, radiusAtBase: bool):
        """
        Setter for property: (bool) RibMinimumRadiusAtBase
         Returns the rib feature validation minimum radius at base   
            
         
        """
        pass
    @property
    def RibMinimumRadiusAtBaseLimit(self) -> float:
        """
        Getter for property: (float) RibMinimumRadiusAtBaseLimit
         Returns the rib feature validation minimum radius at base limit   
            
         
        """
        pass
    @RibMinimumRadiusAtBaseLimit.setter
    def RibMinimumRadiusAtBaseLimit(self, radiusAtBaseLimit: float):
        """
        Setter for property: (float) RibMinimumRadiusAtBaseLimit
         Returns the rib feature validation minimum radius at base limit   
            
         
        """
        pass
    @property
    def RibMinimumThicknessAtTop(self) -> bool:
        """
        Getter for property: (bool) RibMinimumThicknessAtTop
         Returns the rib feature validation minimum thickness at top   
            
         
        """
        pass
    @RibMinimumThicknessAtTop.setter
    def RibMinimumThicknessAtTop(self, thicknessAtTop: bool):
        """
        Setter for property: (bool) RibMinimumThicknessAtTop
         Returns the rib feature validation minimum thickness at top   
            
         
        """
        pass
    @property
    def RibMinimumThicknessAtTopLimit(self) -> float:
        """
        Getter for property: (float) RibMinimumThicknessAtTopLimit
         Returns the rib feature validation minimum thickness at top limit   
            
         
        """
        pass
    @RibMinimumThicknessAtTopLimit.setter
    def RibMinimumThicknessAtTopLimit(self, thicknessAtTopLimit: float):
        """
        Setter for property: (float) RibMinimumThicknessAtTopLimit
         Returns the rib feature validation minimum thickness at top limit   
            
         
        """
        pass
    @property
    def RibThicknessToNominalWallThickness(self) -> bool:
        """
        Getter for property: (bool) RibThicknessToNominalWallThickness
         Returns the rib feature validation thickness to nominal wall thickness ratio   
            
         
        """
        pass
    @RibThicknessToNominalWallThickness.setter
    def RibThicknessToNominalWallThickness(self, ribThicknessToNominalWallThk: bool):
        """
        Setter for property: (bool) RibThicknessToNominalWallThickness
         Returns the rib feature validation thickness to nominal wall thickness ratio   
            
         
        """
        pass
    @property
    def RibThicknessToNominalWallThicknessLimit(self) -> float:
        """
        Getter for property: (float) RibThicknessToNominalWallThicknessLimit
         Returns the rib feature validation thickness to nominal wall thickness ratio limit   
            
         
        """
        pass
    @RibThicknessToNominalWallThicknessLimit.setter
    def RibThicknessToNominalWallThicknessLimit(self, ribThicknessToNominalWallThkLimit: float):
        """
        Setter for property: (float) RibThicknessToNominalWallThicknessLimit
         Returns the rib feature validation thickness to nominal wall thickness ratio limit   
            
         
        """
        pass
    @property
    def SharpCorners(self) -> bool:
        """
        Getter for property: (bool) SharpCorners
         Returns the moldability validation sharp corners   
            
         
        """
        pass
    @SharpCorners.setter
    def SharpCorners(self, sharpCorners: bool):
        """
        Setter for property: (bool) SharpCorners
         Returns the moldability validation sharp corners   
            
         
        """
        pass
    @property
    def SharpCornersColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) SharpCornersColor
         Returns the moldability validation sharp corners color   
            
         
        """
        pass
    @SharpCornersColor.setter
    def SharpCornersColor(self, sharpCornersColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) SharpCornersColor
         Returns the moldability validation sharp corners color   
            
         
        """
        pass
    @property
    def SharpCornersLimit(self) -> float:
        """
        Getter for property: (float) SharpCornersLimit
         Returns the moldability validation sharp corners limit   
            
         
        """
        pass
    @SharpCornersLimit.setter
    def SharpCornersLimit(self, sharpCornersLimit: float):
        """
        Setter for property: (float) SharpCornersLimit
         Returns the moldability validation sharp corners limit   
            
         
        """
        pass
    @property
    def SnapJointColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) SnapJointColor
         Returns the snap joint feature validation color   
            
         
        """
        pass
    @SnapJointColor.setter
    def SnapJointColor(self, snapJointColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) SnapJointColor
         Returns the snap joint feature validation color   
            
         
        """
        pass
    @property
    def SnapJointMaximumThicknessAtBase(self) -> bool:
        """
        Getter for property: (bool) SnapJointMaximumThicknessAtBase
         Returns the snap joint feature validation maximum thickness at base   
            
         
        """
        pass
    @SnapJointMaximumThicknessAtBase.setter
    def SnapJointMaximumThicknessAtBase(self, snapJointMaximumThicknessAtBase: bool):
        """
        Setter for property: (bool) SnapJointMaximumThicknessAtBase
         Returns the snap joint feature validation maximum thickness at base   
            
         
        """
        pass
    @property
    def SnapJointMaximumThicknessAtBaseLimit(self) -> float:
        """
        Getter for property: (float) SnapJointMaximumThicknessAtBaseLimit
         Returns the snap joint feature validation maximum thickness at base limit   
            
         
        """
        pass
    @SnapJointMaximumThicknessAtBaseLimit.setter
    def SnapJointMaximumThicknessAtBaseLimit(self, snapJointMaximumThicknessAtBaseLimit: float):
        """
        Setter for property: (float) SnapJointMaximumThicknessAtBaseLimit
         Returns the snap joint feature validation maximum thickness at base limit   
            
         
        """
        pass
    @property
    def SnapJointMinimumDraftOnOuterFaces(self) -> bool:
        """
        Getter for property: (bool) SnapJointMinimumDraftOnOuterFaces
         Returns the snap joint feature validation minimum draft on outer faces   
            
         
        """
        pass
    @SnapJointMinimumDraftOnOuterFaces.setter
    def SnapJointMinimumDraftOnOuterFaces(self, snapJointMinimumDraftOnOuterFaces: bool):
        """
        Setter for property: (bool) SnapJointMinimumDraftOnOuterFaces
         Returns the snap joint feature validation minimum draft on outer faces   
            
         
        """
        pass
    @property
    def SnapJointMinimumDraftOnOuterFacesLimit(self) -> float:
        """
        Getter for property: (float) SnapJointMinimumDraftOnOuterFacesLimit
         Returns the snap joint feature validation minimum draft on outer faces limit   
            
         
        """
        pass
    @SnapJointMinimumDraftOnOuterFacesLimit.setter
    def SnapJointMinimumDraftOnOuterFacesLimit(self, snapJointMinimumDraftOnOuterFacesLimit: float):
        """
        Setter for property: (float) SnapJointMinimumDraftOnOuterFacesLimit
         Returns the snap joint feature validation minimum draft on outer faces limit   
            
         
        """
        pass
    @property
    def SnapJointMinimumWidthAtBase(self) -> bool:
        """
        Getter for property: (bool) SnapJointMinimumWidthAtBase
         Returns the snap joint feature validation minimum width at base   
            
         
        """
        pass
    @SnapJointMinimumWidthAtBase.setter
    def SnapJointMinimumWidthAtBase(self, snapJointMinimumWidthAtBase: bool):
        """
        Setter for property: (bool) SnapJointMinimumWidthAtBase
         Returns the snap joint feature validation minimum width at base   
            
         
        """
        pass
    @property
    def SnapJointMinimumWidthAtBaseLimit(self) -> float:
        """
        Getter for property: (float) SnapJointMinimumWidthAtBaseLimit
         Returns the snap joint feature validation minimum width at base limit   
            
         
        """
        pass
    @SnapJointMinimumWidthAtBaseLimit.setter
    def SnapJointMinimumWidthAtBaseLimit(self, snapJointMinimumWidthAtBaseLimit: float):
        """
        Setter for property: (float) SnapJointMinimumWidthAtBaseLimit
         Returns the snap joint feature validation minimum width at base limit   
            
         
        """
        pass
    @property
    def SnapJointPermissibleDeflection(self) -> bool:
        """
        Getter for property: (bool) SnapJointPermissibleDeflection
         Returns the snap joint feature validation of permissible deflection   
            
         
        """
        pass
    @SnapJointPermissibleDeflection.setter
    def SnapJointPermissibleDeflection(self, snapJointPermissibleDeflection: bool):
        """
        Setter for property: (bool) SnapJointPermissibleDeflection
         Returns the snap joint feature validation of permissible deflection   
            
         
        """
        pass
    @property
    def SnapJointPermissibleDeflectionLimit(self) -> float:
        """
        Getter for property: (float) SnapJointPermissibleDeflectionLimit
         Returns the snap joint feature validation permissible deflection limit   
            
         
        """
        pass
    @SnapJointPermissibleDeflectionLimit.setter
    def SnapJointPermissibleDeflectionLimit(self, snapJointPermissibleDeflectionLimit: float):
        """
        Setter for property: (float) SnapJointPermissibleDeflectionLimit
         Returns the snap joint feature validation permissible deflection limit   
            
         
        """
        pass
    @property
    def SnapJointPermissibleStrain(self) -> float:
        """
        Getter for property: (float) SnapJointPermissibleStrain
         Returns the snap joint feature permissible strain   
            
         
        """
        pass
    @SnapJointPermissibleStrain.setter
    def SnapJointPermissibleStrain(self, snapJointPermissibleStrain: float):
        """
        Setter for property: (float) SnapJointPermissibleStrain
         Returns the snap joint feature permissible strain   
            
         
        """
        pass
    @property
    def ThickWalls(self) -> bool:
        """
        Getter for property: (bool) ThickWalls
         Returns the moldability validation thick walls   
            
         
        """
        pass
    @ThickWalls.setter
    def ThickWalls(self, thickWalls: bool):
        """
        Setter for property: (bool) ThickWalls
         Returns the moldability validation thick walls   
            
         
        """
        pass
    @property
    def ThickWallsColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) ThickWallsColor
         Returns the moldability validation thick walls color   
            
         
        """
        pass
    @ThickWallsColor.setter
    def ThickWallsColor(self, thickWallsColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) ThickWallsColor
         Returns the moldability validation thick walls color   
            
         
        """
        pass
    @property
    def ThickWallsLimit(self) -> float:
        """
        Getter for property: (float) ThickWallsLimit
         Returns the moldability validation thick walls limit   
            
         
        """
        pass
    @ThickWallsLimit.setter
    def ThickWallsLimit(self, thickWallsLimit: float):
        """
        Setter for property: (float) ThickWallsLimit
         Returns the moldability validation thick walls limit   
            
         
        """
        pass
    @property
    def ThinWalls(self) -> bool:
        """
        Getter for property: (bool) ThinWalls
         Returns the moldability validation thin walls   
            
         
        """
        pass
    @ThinWalls.setter
    def ThinWalls(self, thinWalls: bool):
        """
        Setter for property: (bool) ThinWalls
         Returns the moldability validation thin walls   
            
         
        """
        pass
    @property
    def ThinWallsColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) ThinWallsColor
         Returns the moldability validation thin walls color   
            
         
        """
        pass
    @ThinWallsColor.setter
    def ThinWallsColor(self, thinWallsColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) ThinWallsColor
         Returns the moldability validation thin walls color   
            
         
        """
        pass
    @property
    def ThinWallsLimit(self) -> float:
        """
        Getter for property: (float) ThinWallsLimit
         Returns the moldability validation thin walls limit   
            
         
        """
        pass
    @ThinWallsLimit.setter
    def ThinWallsLimit(self, thinWallsLimit: float):
        """
        Setter for property: (float) ThinWallsLimit
         Returns the moldability validation thin walls limit   
            
         
        """
        pass
    @property
    def UndercutRegions(self) -> bool:
        """
        Getter for property: (bool) UndercutRegions
         Returns the moldability validation undercut regions   
            
         
        """
        pass
    @UndercutRegions.setter
    def UndercutRegions(self, undercutRegions: bool):
        """
        Setter for property: (bool) UndercutRegions
         Returns the moldability validation undercut regions   
            
         
        """
        pass
    @property
    def UndercutRegionsColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) UndercutRegionsColor
         Returns the moldability validation undercut regions color   
            
         
        """
        pass
    @UndercutRegionsColor.setter
    def UndercutRegionsColor(self, undercutRegionsColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) UndercutRegionsColor
         Returns the moldability validation undercut regions color   
            
         
        """
        pass
    @property
    def VerticalWalls(self) -> bool:
        """
        Getter for property: (bool) VerticalWalls
         Returns the moldability validation vertical walls   
            
         
        """
        pass
    @VerticalWalls.setter
    def VerticalWalls(self, verticalWalls: bool):
        """
        Setter for property: (bool) VerticalWalls
         Returns the moldability validation vertical walls   
            
         
        """
        pass
    @property
    def VerticalWallsColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) VerticalWallsColor
         Returns the moldability validation vertical walls color   
            
         
        """
        pass
    @VerticalWallsColor.setter
    def VerticalWallsColor(self, verticalWallsColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) VerticalWallsColor
         Returns the moldability validation vertical walls color   
            
         
        """
        pass
import NXOpen
class SurfaceIdentifierBuilder(NXOpen.Builder): 
    """ Surface Identifier builder """
    def AddIdentifier(self, label: str, highlightColor: NXOpen.NXColor, faces: List[NXOpen.Face]) -> IdentifierDataBuilder:
        """
         Creates a PlasticDesigner.IdentifierDataBuilder and append it to the identifier data list. 
                    If PlasticDesigner.IdentifierDataBuilder with same label already exist,
                    then existing instance will be returned by setting remaining input parameters 
         Returns databuilder ( IdentifierDataBuilder NXOpen.Pla):  PlasticDesigner.IdentifierDataBuilder instance.
        """
        pass
    def DeleteIdentifier(self, label: str) -> None:
        """
         Remove and delete an identifier corresponding to input label.
        """
        pass
    def GetIdentifier(self, label: str) -> IdentifierDataBuilder:
        """
         Returns the identifier corresponding to input label. Return  if identifier not found
         Returns databuilder ( IdentifierDataBuilder NXOpen.Pla):   PlasticDesigner.IdentifierDataBuilder instance.
        """
        pass
    def GetIdentifiers(self) -> List[IdentifierDataBuilder]:
        """
         Returns the array of identifiers
         Returns identifiers ( IdentifierDataBuilder List[NXOpen.P):  array of PlasticDesigner.IdentifierDataBuilder instances.
        """
        pass
