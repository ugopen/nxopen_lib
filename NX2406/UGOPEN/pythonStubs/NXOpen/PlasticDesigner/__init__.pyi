from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents a Builder for DrawDirectionBuilder functionality <br> To create a new instance of this class, use @link NXOpen::PlasticDesigner::Manager::CreateDrawDirectionBuilder  NXOpen::PlasticDesigner::Manager::CreateDrawDirectionBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class DrawDirectionBuilder(NXOpen.Builder): 
    """ Represents a Builder for DrawDirectionBuilder functionality"""


    ##  define draw direction items 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Vector</term><description> 
    ##  vector; </description> </item><item><term> 
    ## Orientation</term><description> 
    ##  orientation; </description> </item></list>
    class DrawDirection(Enum):
        """
        Members Include: <Vector> <Orientation>
        """
        Vector: int
        Orientation: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DrawDirectionBuilder.DrawDirection:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link DrawDirectionBuilder.DrawDirection NXOpen.PlasticDesigner.DrawDirectionBuilder.DrawDirection@endlink) DrawOption
    ##  Returns the preference   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return DrawDirectionBuilder.DrawDirection
    @property
    def DrawOption(self) -> DrawDirectionBuilder.DrawDirection:
        """
        Getter for property: (@link DrawDirectionBuilder.DrawDirection NXOpen.PlasticDesigner.DrawDirectionBuilder.DrawDirection@endlink) DrawOption
         Returns the preference   
            
         
        """
        pass
    
    ## Setter for property: (@link DrawDirectionBuilder.DrawDirection NXOpen.PlasticDesigner.DrawDirectionBuilder.DrawDirection@endlink) DrawOption

    ##  Returns the preference   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @DrawOption.setter
    def DrawOption(self, drawOption: DrawDirectionBuilder.DrawDirection):
        """
        Setter for property: (@link DrawDirectionBuilder.DrawDirection NXOpen.PlasticDesigner.DrawDirectionBuilder.DrawDirection@endlink) DrawOption
         Returns the preference   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) DrawOrientation
    ##  Returns the orientation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Matrix3x3
    @property
    def DrawOrientation(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) DrawOrientation
         Returns the orientation   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) DrawOrientation

    ##  Returns the orientation   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @DrawOrientation.setter
    def DrawOrientation(self, drawOrientation: NXOpen.Matrix3x3):
        """
        Setter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) DrawOrientation
         Returns the orientation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) DrawOrigin
    ##  Returns the draw origin   
    ##     
    ##  
    ## Getter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def DrawOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) DrawOrigin
         Returns the draw origin   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) DrawOrigin

    ##  Returns the draw origin   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @DrawOrigin.setter
    def DrawOrigin(self, drawOrigin: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) DrawOrigin
         Returns the draw origin   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DrawVector
    ##  Returns the vector   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def DrawVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DrawVector
         Returns the vector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DrawVector

    ##  Returns the vector   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @DrawVector.setter
    def DrawVector(self, vector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DrawVector
         Returns the vector   
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Identifier Data. This represents data used for a identifier element in 
##         a @link PlasticDesigner::IdentifierDataBuilder PlasticDesigner::IdentifierDataBuilder@endlink  
## 
##   <br>  Created in NX2312.0.0  <br> 

class IdentifierDataBuilder(NXOpen.TaggedObject): 
    """ Identifier Data. This represents data used for a identifier element in 
        a <ja_class>PlasticDesigner.IdentifierDataBuilder</ja_class> """


    ## Getter for property: (@link NXOpen.SelectFaceList NXOpen.SelectFaceList@endlink) Faces
    ##  Returns the face selection list   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.SelectFaceList
    @property
    def Faces(self) -> NXOpen.SelectFaceList:
        """
        Getter for property: (@link NXOpen.SelectFaceList NXOpen.SelectFaceList@endlink) Faces
         Returns the face selection list   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) HighlightColor
    ##  Returns the highlight color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def HighlightColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) HighlightColor
         Returns the highlight color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) HighlightColor

    ##  Returns the highlight color   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @HighlightColor.setter
    def HighlightColor(self, highlightColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) HighlightColor
         Returns the highlight color   
            
         
        """
        pass
    
    ## Getter for property: (bool) HighlightStatus
    ##  Returns the highlight status   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def HighlightStatus(self) -> bool:
        """
        Getter for property: (bool) HighlightStatus
         Returns the highlight status   
            
         
        """
        pass
    
    ## Setter for property: (bool) HighlightStatus

    ##  Returns the highlight status   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @HighlightStatus.setter
    def HighlightStatus(self, isHighlighted: bool):
        """
        Setter for property: (bool) HighlightStatus
         Returns the highlight status   
            
         
        """
        pass
    
    ## Getter for property: (str) Label
    ##  Returns the label   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return str
    @property
    def Label(self) -> str:
        """
        Getter for property: (str) Label
         Returns the label   
            
         
        """
        pass
    
    ## Setter for property: (str) Label

    ##  Returns the label   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @Label.setter
    def Label(self, label: str):
        """
        Setter for property: (str) Label
         Returns the label   
            
         
        """
        pass
    
import NXOpen
##  Represents the Plastic Designer Manager class. <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class Manager(NXOpen.Object): 
    """ Represents the Plastic Designer Manager class."""


    ##  Creates a @link PlasticDesigner::DrawDirectionBuilder PlasticDesigner::DrawDirectionBuilder@endlink  
    ##  @return builder (@link DrawDirectionBuilder NXOpen.PlasticDesigner.DrawDirectionBuilder@endlink):  Plastic Designer DrawDirectionBuilder Builder.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateDrawDirectionBuilder(part: NXOpen.Part) -> DrawDirectionBuilder:
        """
         Creates a @link PlasticDesigner::DrawDirectionBuilder PlasticDesigner::DrawDirectionBuilder@endlink  
         @return builder (@link DrawDirectionBuilder NXOpen.PlasticDesigner.DrawDirectionBuilder@endlink):  Plastic Designer DrawDirectionBuilder Builder.
        """
        pass
    
    ##  Creates a @link PlasticDesigner::PreferencesBuilder PlasticDesigner::PreferencesBuilder@endlink  
    ##  @return builder (@link PreferencesBuilder NXOpen.PlasticDesigner.PreferencesBuilder@endlink):  Plastic Designer Preferences Builder.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreatePreferencesBuilder(part: NXOpen.Part) -> PreferencesBuilder:
        """
         Creates a @link PlasticDesigner::PreferencesBuilder PlasticDesigner::PreferencesBuilder@endlink  
         @return builder (@link PreferencesBuilder NXOpen.PlasticDesigner.PreferencesBuilder@endlink):  Plastic Designer Preferences Builder.
        """
        pass
    
    ##  Creates a @link PlasticDesigner::SurfaceIdentifierBuilder PlasticDesigner::SurfaceIdentifierBuilder@endlink  
    ##  @return builder (@link SurfaceIdentifierBuilder NXOpen.PlasticDesigner.SurfaceIdentifierBuilder@endlink):  Surface Identifier Builder.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateSurfaceIdentifierBuilder(part: NXOpen.Part) -> SurfaceIdentifierBuilder:
        """
         Creates a @link PlasticDesigner::SurfaceIdentifierBuilder PlasticDesigner::SurfaceIdentifierBuilder@endlink  
         @return builder (@link SurfaceIdentifierBuilder NXOpen.PlasticDesigner.SurfaceIdentifierBuilder@endlink):  Surface Identifier Builder.
        """
        pass
    
    ##  Performs Feature Validation 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## <param name="body"> (@link NXOpen.Body NXOpen.Body@endlink) </param>
    def PerformFeatureValidation(body: NXOpen.Body) -> None:
        """
         Performs Feature Validation 
        """
        pass
    
    ##  Performs Moldability Validation 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## <param name="body"> (@link NXOpen.Body NXOpen.Body@endlink) </param>
    def PerformMoldabilityValidation(body: NXOpen.Body) -> None:
        """
         Performs Moldability Validation 
        """
        pass
    
import NXOpen
##  Plastic Plastic Application Manager <br> To create a new instance of this class, use @link NXOpen::PlasticDesigner::Manager::CreatePreferencesBuilder  NXOpen::PlasticDesigner::Manager::CreatePreferencesBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class PreferencesBuilder(NXOpen.Builder): 
    """ Plastic Plastic Application Manager"""


    ## Getter for property: (bool) BossBaseRadiusToNominalWallThickness
    ##  Returns the boss feature validation base radius to nominal wall thickness ratio   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def BossBaseRadiusToNominalWallThickness(self) -> bool:
        """
        Getter for property: (bool) BossBaseRadiusToNominalWallThickness
         Returns the boss feature validation base radius to nominal wall thickness ratio   
            
         
        """
        pass
    
    ## Setter for property: (bool) BossBaseRadiusToNominalWallThickness

    ##  Returns the boss feature validation base radius to nominal wall thickness ratio   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @BossBaseRadiusToNominalWallThickness.setter
    def BossBaseRadiusToNominalWallThickness(self, bossBaseRadiusToNominalWallThick: bool):
        """
        Setter for property: (bool) BossBaseRadiusToNominalWallThickness
         Returns the boss feature validation base radius to nominal wall thickness ratio   
            
         
        """
        pass
    
    ## Getter for property: (float) BossBaseRadiusToNominalWallThicknessLimit
    ##  Returns the boss feature validation base radius to nominal wall thickness ratio limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return float
    @property
    def BossBaseRadiusToNominalWallThicknessLimit(self) -> float:
        """
        Getter for property: (float) BossBaseRadiusToNominalWallThicknessLimit
         Returns the boss feature validation base radius to nominal wall thickness ratio limit   
            
         
        """
        pass
    
    ## Setter for property: (float) BossBaseRadiusToNominalWallThicknessLimit

    ##  Returns the boss feature validation base radius to nominal wall thickness ratio limit   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @BossBaseRadiusToNominalWallThicknessLimit.setter
    def BossBaseRadiusToNominalWallThicknessLimit(self, bossBaseRadiusToNominalWallThickLimit: float):
        """
        Setter for property: (float) BossBaseRadiusToNominalWallThicknessLimit
         Returns the boss feature validation base radius to nominal wall thickness ratio limit   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) BossColor
    ##  Returns the boss feature validation color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def BossColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) BossColor
         Returns the boss feature validation color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) BossColor

    ##  Returns the boss feature validation color   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @BossColor.setter
    def BossColor(self, bossColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) BossColor
         Returns the boss feature validation color   
            
         
        """
        pass
    
    ## Getter for property: (bool) BossHeightToNominalWallThickness
    ##  Returns the boss feature validation height to nominal wall thickness ratio   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def BossHeightToNominalWallThickness(self) -> bool:
        """
        Getter for property: (bool) BossHeightToNominalWallThickness
         Returns the boss feature validation height to nominal wall thickness ratio   
            
         
        """
        pass
    
    ## Setter for property: (bool) BossHeightToNominalWallThickness

    ##  Returns the boss feature validation height to nominal wall thickness ratio   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @BossHeightToNominalWallThickness.setter
    def BossHeightToNominalWallThickness(self, heightToNominalWallThickness: bool):
        """
        Setter for property: (bool) BossHeightToNominalWallThickness
         Returns the boss feature validation height to nominal wall thickness ratio   
            
         
        """
        pass
    
    ## Getter for property: (float) BossHeightToNominalWallThicknessLimit
    ##  Returns the boss feature validation height to nominal wall thickness ratio limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return float
    @property
    def BossHeightToNominalWallThicknessLimit(self) -> float:
        """
        Getter for property: (float) BossHeightToNominalWallThicknessLimit
         Returns the boss feature validation height to nominal wall thickness ratio limit   
            
         
        """
        pass
    
    ## Setter for property: (float) BossHeightToNominalWallThicknessLimit

    ##  Returns the boss feature validation height to nominal wall thickness ratio limit   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @BossHeightToNominalWallThicknessLimit.setter
    def BossHeightToNominalWallThicknessLimit(self, heightToNominalWallThicknessLimit: float):
        """
        Setter for property: (float) BossHeightToNominalWallThicknessLimit
         Returns the boss feature validation height to nominal wall thickness ratio limit   
            
         
        """
        pass
    
    ## Getter for property: (bool) BossHeightToOuterDiameter
    ##  Returns the boss feature validation height to outer diameter ratio   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def BossHeightToOuterDiameter(self) -> bool:
        """
        Getter for property: (bool) BossHeightToOuterDiameter
         Returns the boss feature validation height to outer diameter ratio   
            
         
        """
        pass
    
    ## Setter for property: (bool) BossHeightToOuterDiameter

    ##  Returns the boss feature validation height to outer diameter ratio   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @BossHeightToOuterDiameter.setter
    def BossHeightToOuterDiameter(self, heightToOuterDiameter: bool):
        """
        Setter for property: (bool) BossHeightToOuterDiameter
         Returns the boss feature validation height to outer diameter ratio   
            
         
        """
        pass
    
    ## Getter for property: (float) BossHeightToOuterDiameterLimit
    ##  Returns the boss feature validation height to outer diameter ratio limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return float
    @property
    def BossHeightToOuterDiameterLimit(self) -> float:
        """
        Getter for property: (float) BossHeightToOuterDiameterLimit
         Returns the boss feature validation height to outer diameter ratio limit   
            
         
        """
        pass
    
    ## Setter for property: (float) BossHeightToOuterDiameterLimit

    ##  Returns the boss feature validation height to outer diameter ratio limit   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @BossHeightToOuterDiameterLimit.setter
    def BossHeightToOuterDiameterLimit(self, heightToOuterDiameterLimit: float):
        """
        Setter for property: (float) BossHeightToOuterDiameterLimit
         Returns the boss feature validation height to outer diameter ratio limit   
            
         
        """
        pass
    
    ## Getter for property: (bool) BossMaximumOuterToInnerDiameterThickness
    ##  Returns the boss feature validation maximum outer to inner diameter thickness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def BossMaximumOuterToInnerDiameterThickness(self) -> bool:
        """
        Getter for property: (bool) BossMaximumOuterToInnerDiameterThickness
         Returns the boss feature validation maximum outer to inner diameter thickness   
            
         
        """
        pass
    
    ## Setter for property: (bool) BossMaximumOuterToInnerDiameterThickness

    ##  Returns the boss feature validation maximum outer to inner diameter thickness   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @BossMaximumOuterToInnerDiameterThickness.setter
    def BossMaximumOuterToInnerDiameterThickness(self, outerToInnerDiameterThick: bool):
        """
        Setter for property: (bool) BossMaximumOuterToInnerDiameterThickness
         Returns the boss feature validation maximum outer to inner diameter thickness   
            
         
        """
        pass
    
    ## Getter for property: (float) BossMaximumOuterToInnerDiameterThicknessLimit
    ##  Returns the boss feature validation maximum outer to inner diameter thickness limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return float
    @property
    def BossMaximumOuterToInnerDiameterThicknessLimit(self) -> float:
        """
        Getter for property: (float) BossMaximumOuterToInnerDiameterThicknessLimit
         Returns the boss feature validation maximum outer to inner diameter thickness limit   
            
         
        """
        pass
    
    ## Setter for property: (float) BossMaximumOuterToInnerDiameterThicknessLimit

    ##  Returns the boss feature validation maximum outer to inner diameter thickness limit   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @BossMaximumOuterToInnerDiameterThicknessLimit.setter
    def BossMaximumOuterToInnerDiameterThicknessLimit(self, outerToInnerDiameterThickLimit: float):
        """
        Setter for property: (float) BossMaximumOuterToInnerDiameterThicknessLimit
         Returns the boss feature validation maximum outer to inner diameter thickness limit   
            
         
        """
        pass
    
    ## Getter for property: (bool) BossMinimumDraftOnInnerDiameter
    ##  Returns the boss feature validation minimum draft on inner diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def BossMinimumDraftOnInnerDiameter(self) -> bool:
        """
        Getter for property: (bool) BossMinimumDraftOnInnerDiameter
         Returns the boss feature validation minimum draft on inner diameter   
            
         
        """
        pass
    
    ## Setter for property: (bool) BossMinimumDraftOnInnerDiameter

    ##  Returns the boss feature validation minimum draft on inner diameter   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @BossMinimumDraftOnInnerDiameter.setter
    def BossMinimumDraftOnInnerDiameter(self, bossDraftOnInnerDia: bool):
        """
        Setter for property: (bool) BossMinimumDraftOnInnerDiameter
         Returns the boss feature validation minimum draft on inner diameter   
            
         
        """
        pass
    
    ## Getter for property: (float) BossMinimumDraftOnInnerDiameterLimit
    ##  Returns the boss feature validation minimum draft on inner diameter limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return float
    @property
    def BossMinimumDraftOnInnerDiameterLimit(self) -> float:
        """
        Getter for property: (float) BossMinimumDraftOnInnerDiameterLimit
         Returns the boss feature validation minimum draft on inner diameter limit   
            
         
        """
        pass
    
    ## Setter for property: (float) BossMinimumDraftOnInnerDiameterLimit

    ##  Returns the boss feature validation minimum draft on inner diameter limit   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @BossMinimumDraftOnInnerDiameterLimit.setter
    def BossMinimumDraftOnInnerDiameterLimit(self, bossDraftOnInnerDiaLimit: float):
        """
        Setter for property: (float) BossMinimumDraftOnInnerDiameterLimit
         Returns the boss feature validation minimum draft on inner diameter limit   
            
         
        """
        pass
    
    ## Getter for property: (bool) BossMinimumDraftOnOuterDiameter
    ##  Returns the boss feature validation minimum draft on outer diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def BossMinimumDraftOnOuterDiameter(self) -> bool:
        """
        Getter for property: (bool) BossMinimumDraftOnOuterDiameter
         Returns the boss feature validation minimum draft on outer diameter   
            
         
        """
        pass
    
    ## Setter for property: (bool) BossMinimumDraftOnOuterDiameter

    ##  Returns the boss feature validation minimum draft on outer diameter   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @BossMinimumDraftOnOuterDiameter.setter
    def BossMinimumDraftOnOuterDiameter(self, bossDraftOnOuterDia: bool):
        """
        Setter for property: (bool) BossMinimumDraftOnOuterDiameter
         Returns the boss feature validation minimum draft on outer diameter   
            
         
        """
        pass
    
    ## Getter for property: (float) BossMinimumDraftOnOuterDiameterLimit
    ##  Returns the boss feature validation minimum draft on outer diameter limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return float
    @property
    def BossMinimumDraftOnOuterDiameterLimit(self) -> float:
        """
        Getter for property: (float) BossMinimumDraftOnOuterDiameterLimit
         Returns the boss feature validation minimum draft on outer diameter limit   
            
         
        """
        pass
    
    ## Setter for property: (float) BossMinimumDraftOnOuterDiameterLimit

    ##  Returns the boss feature validation minimum draft on outer diameter limit   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @BossMinimumDraftOnOuterDiameterLimit.setter
    def BossMinimumDraftOnOuterDiameterLimit(self, bossDraftOnOuterDiaLimit: float):
        """
        Setter for property: (float) BossMinimumDraftOnOuterDiameterLimit
         Returns the boss feature validation minimum draft on outer diameter limit   
            
         
        """
        pass
    
    ## Getter for property: (bool) BossMinimumRadiusAtBase
    ##  Returns the boss feature validation minimum radius at base   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def BossMinimumRadiusAtBase(self) -> bool:
        """
        Getter for property: (bool) BossMinimumRadiusAtBase
         Returns the boss feature validation minimum radius at base   
            
         
        """
        pass
    
    ## Setter for property: (bool) BossMinimumRadiusAtBase

    ##  Returns the boss feature validation minimum radius at base   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @BossMinimumRadiusAtBase.setter
    def BossMinimumRadiusAtBase(self, radiusAtBase: bool):
        """
        Setter for property: (bool) BossMinimumRadiusAtBase
         Returns the boss feature validation minimum radius at base   
            
         
        """
        pass
    
    ## Getter for property: (float) BossMinimumRadiusAtBaseLimit
    ##  Returns the boss feature validation minimum radius at base limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return float
    @property
    def BossMinimumRadiusAtBaseLimit(self) -> float:
        """
        Getter for property: (float) BossMinimumRadiusAtBaseLimit
         Returns the boss feature validation minimum radius at base limit   
            
         
        """
        pass
    
    ## Setter for property: (float) BossMinimumRadiusAtBaseLimit

    ##  Returns the boss feature validation minimum radius at base limit   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @BossMinimumRadiusAtBaseLimit.setter
    def BossMinimumRadiusAtBaseLimit(self, radiusAtBaseLimit: float):
        """
        Setter for property: (float) BossMinimumRadiusAtBaseLimit
         Returns the boss feature validation minimum radius at base limit   
            
         
        """
        pass
    
    ## Getter for property: (bool) BossMinimumRadiusAtTop
    ##  Returns the boss feature validation minimum radius at top   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def BossMinimumRadiusAtTop(self) -> bool:
        """
        Getter for property: (bool) BossMinimumRadiusAtTop
         Returns the boss feature validation minimum radius at top   
            
         
        """
        pass
    
    ## Setter for property: (bool) BossMinimumRadiusAtTop

    ##  Returns the boss feature validation minimum radius at top   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @BossMinimumRadiusAtTop.setter
    def BossMinimumRadiusAtTop(self, radiusAtTop: bool):
        """
        Setter for property: (bool) BossMinimumRadiusAtTop
         Returns the boss feature validation minimum radius at top   
            
         
        """
        pass
    
    ## Getter for property: (float) BossMinimumRadiusAtTopLimit
    ##  Returns the boss feature validation minimum radius at top limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return float
    @property
    def BossMinimumRadiusAtTopLimit(self) -> float:
        """
        Getter for property: (float) BossMinimumRadiusAtTopLimit
         Returns the boss feature validation minimum radius at top limit   
            
         
        """
        pass
    
    ## Setter for property: (float) BossMinimumRadiusAtTopLimit

    ##  Returns the boss feature validation minimum radius at top limit   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @BossMinimumRadiusAtTopLimit.setter
    def BossMinimumRadiusAtTopLimit(self, radiusAtTopLimit: float):
        """
        Setter for property: (float) BossMinimumRadiusAtTopLimit
         Returns the boss feature validation minimum radius at top limit   
            
         
        """
        pass
    
    ## Getter for property: (bool) BossMinimumWallDistance
    ##  Returns the boss feature validation minimum wall distance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def BossMinimumWallDistance(self) -> bool:
        """
        Getter for property: (bool) BossMinimumWallDistance
         Returns the boss feature validation minimum wall distance   
            
         
        """
        pass
    
    ## Setter for property: (bool) BossMinimumWallDistance

    ##  Returns the boss feature validation minimum wall distance   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @BossMinimumWallDistance.setter
    def BossMinimumWallDistance(self, minimumWallDistance: bool):
        """
        Setter for property: (bool) BossMinimumWallDistance
         Returns the boss feature validation minimum wall distance   
            
         
        """
        pass
    
    ## Getter for property: (float) BossMinimumWallDistanceLimit
    ##  Returns the boss feature validation minimum wall distance limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return float
    @property
    def BossMinimumWallDistanceLimit(self) -> float:
        """
        Getter for property: (float) BossMinimumWallDistanceLimit
         Returns the boss feature validation minimum wall distance limit   
            
         
        """
        pass
    
    ## Setter for property: (float) BossMinimumWallDistanceLimit

    ##  Returns the boss feature validation minimum wall distance limit   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @BossMinimumWallDistanceLimit.setter
    def BossMinimumWallDistanceLimit(self, minimumWallDistanceLimit: float):
        """
        Setter for property: (float) BossMinimumWallDistanceLimit
         Returns the boss feature validation minimum wall distance limit   
            
         
        """
        pass
    
    ## Getter for property: (bool) BossOuterToInnerDiameter
    ##  Returns the boss feature validation outer to inner diameter ratio   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def BossOuterToInnerDiameter(self) -> bool:
        """
        Getter for property: (bool) BossOuterToInnerDiameter
         Returns the boss feature validation outer to inner diameter ratio   
            
         
        """
        pass
    
    ## Setter for property: (bool) BossOuterToInnerDiameter

    ##  Returns the boss feature validation outer to inner diameter ratio   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @BossOuterToInnerDiameter.setter
    def BossOuterToInnerDiameter(self, outerToInnerDiameter: bool):
        """
        Setter for property: (bool) BossOuterToInnerDiameter
         Returns the boss feature validation outer to inner diameter ratio   
            
         
        """
        pass
    
    ## Getter for property: (float) BossOuterToInnerDiameterLimit
    ##  Returns the boss feature validation outer to inner diameter ratio limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return float
    @property
    def BossOuterToInnerDiameterLimit(self) -> float:
        """
        Getter for property: (float) BossOuterToInnerDiameterLimit
         Returns the boss feature validation outer to inner diameter ratio limit   
            
         
        """
        pass
    
    ## Setter for property: (float) BossOuterToInnerDiameterLimit

    ##  Returns the boss feature validation outer to inner diameter ratio limit   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @BossOuterToInnerDiameterLimit.setter
    def BossOuterToInnerDiameterLimit(self, outerToInnerDiameterLimit: float):
        """
        Setter for property: (float) BossOuterToInnerDiameterLimit
         Returns the boss feature validation outer to inner diameter ratio limit   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) HousingColor
    ##  Returns the housing feature validation color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def HousingColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) HousingColor
         Returns the housing feature validation color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) HousingColor

    ##  Returns the housing feature validation color   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @HousingColor.setter
    def HousingColor(self, housingColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) HousingColor
         Returns the housing feature validation color   
            
         
        """
        pass
    
    ## Getter for property: (bool) HousingMaximumThicknessAtBase
    ##  Returns the housing feature validation maximum thickness at base   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def HousingMaximumThicknessAtBase(self) -> bool:
        """
        Getter for property: (bool) HousingMaximumThicknessAtBase
         Returns the housing feature validation maximum thickness at base   
            
         
        """
        pass
    
    ## Setter for property: (bool) HousingMaximumThicknessAtBase

    ##  Returns the housing feature validation maximum thickness at base   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @HousingMaximumThicknessAtBase.setter
    def HousingMaximumThicknessAtBase(self, housingMaximumThicknessAtBase: bool):
        """
        Setter for property: (bool) HousingMaximumThicknessAtBase
         Returns the housing feature validation maximum thickness at base   
            
         
        """
        pass
    
    ## Getter for property: (float) HousingMaximumThicknessAtBaseLimit
    ##  Returns the housing feature validation maximum thickness at base limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def HousingMaximumThicknessAtBaseLimit(self) -> float:
        """
        Getter for property: (float) HousingMaximumThicknessAtBaseLimit
         Returns the housing feature validation maximum thickness at base limit   
            
         
        """
        pass
    
    ## Setter for property: (float) HousingMaximumThicknessAtBaseLimit

    ##  Returns the housing feature validation maximum thickness at base limit   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @HousingMaximumThicknessAtBaseLimit.setter
    def HousingMaximumThicknessAtBaseLimit(self, housingMaximumThicknessAtBaseLimit: float):
        """
        Setter for property: (float) HousingMaximumThicknessAtBaseLimit
         Returns the housing feature validation maximum thickness at base limit   
            
         
        """
        pass
    
    ## Getter for property: (bool) HousingMinimumDraftOnLifterSideFaces
    ##  Returns the housing feature validation minimum draft on lifter side faces   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def HousingMinimumDraftOnLifterSideFaces(self) -> bool:
        """
        Getter for property: (bool) HousingMinimumDraftOnLifterSideFaces
         Returns the housing feature validation minimum draft on lifter side faces   
            
         
        """
        pass
    
    ## Setter for property: (bool) HousingMinimumDraftOnLifterSideFaces

    ##  Returns the housing feature validation minimum draft on lifter side faces   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @HousingMinimumDraftOnLifterSideFaces.setter
    def HousingMinimumDraftOnLifterSideFaces(self, housingMinimumDraftOnLifterFaces: bool):
        """
        Setter for property: (bool) HousingMinimumDraftOnLifterSideFaces
         Returns the housing feature validation minimum draft on lifter side faces   
            
         
        """
        pass
    
    ## Getter for property: (float) HousingMinimumDraftOnLifterSideFacesLimit
    ##  Returns the housing feature validation minimum draft on lifter side faces limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def HousingMinimumDraftOnLifterSideFacesLimit(self) -> float:
        """
        Getter for property: (float) HousingMinimumDraftOnLifterSideFacesLimit
         Returns the housing feature validation minimum draft on lifter side faces limit   
            
         
        """
        pass
    
    ## Setter for property: (float) HousingMinimumDraftOnLifterSideFacesLimit

    ##  Returns the housing feature validation minimum draft on lifter side faces limit   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @HousingMinimumDraftOnLifterSideFacesLimit.setter
    def HousingMinimumDraftOnLifterSideFacesLimit(self, housingMinimumDraftOnLifterFacesLimit: float):
        """
        Setter for property: (float) HousingMinimumDraftOnLifterSideFacesLimit
         Returns the housing feature validation minimum draft on lifter side faces limit   
            
         
        """
        pass
    
    ## Getter for property: (bool) HousingMinimumDraftOnOuterFaces
    ##  Returns the housing feature validation minimum draft on outer faces   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def HousingMinimumDraftOnOuterFaces(self) -> bool:
        """
        Getter for property: (bool) HousingMinimumDraftOnOuterFaces
         Returns the housing feature validation minimum draft on outer faces   
            
         
        """
        pass
    
    ## Setter for property: (bool) HousingMinimumDraftOnOuterFaces

    ##  Returns the housing feature validation minimum draft on outer faces   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @HousingMinimumDraftOnOuterFaces.setter
    def HousingMinimumDraftOnOuterFaces(self, housingMinimumDraftOnOuterFaces: bool):
        """
        Setter for property: (bool) HousingMinimumDraftOnOuterFaces
         Returns the housing feature validation minimum draft on outer faces   
            
         
        """
        pass
    
    ## Getter for property: (float) HousingMinimumDraftOnOuterFacesLimit
    ##  Returns the housing feature validation minimum draft on outer faces limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def HousingMinimumDraftOnOuterFacesLimit(self) -> float:
        """
        Getter for property: (float) HousingMinimumDraftOnOuterFacesLimit
         Returns the housing feature validation minimum draft on outer faces limit   
            
         
        """
        pass
    
    ## Setter for property: (float) HousingMinimumDraftOnOuterFacesLimit

    ##  Returns the housing feature validation minimum draft on outer faces limit   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @HousingMinimumDraftOnOuterFacesLimit.setter
    def HousingMinimumDraftOnOuterFacesLimit(self, housingMinimumDraftOnOuterFacesLimit: float):
        """
        Setter for property: (float) HousingMinimumDraftOnOuterFacesLimit
         Returns the housing feature validation minimum draft on outer faces limit   
            
         
        """
        pass
    
    ## Getter for property: (bool) HousingMinimumRadiusOnInnerFaces
    ##  Returns the housing feature validation minimum radius on outer edges   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def HousingMinimumRadiusOnInnerFaces(self) -> bool:
        """
        Getter for property: (bool) HousingMinimumRadiusOnInnerFaces
         Returns the housing feature validation minimum radius on outer edges   
            
         
        """
        pass
    
    ## Setter for property: (bool) HousingMinimumRadiusOnInnerFaces

    ##  Returns the housing feature validation minimum radius on outer edges   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @HousingMinimumRadiusOnInnerFaces.setter
    def HousingMinimumRadiusOnInnerFaces(self, housingMinimumRadiusOnInnerFaces: bool):
        """
        Setter for property: (bool) HousingMinimumRadiusOnInnerFaces
         Returns the housing feature validation minimum radius on outer edges   
            
         
        """
        pass
    
    ## Getter for property: (float) HousingMinimumRadiusOnInnerFacesLimit
    ##  Returns the housing feature validation minimum radius on outer edges limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def HousingMinimumRadiusOnInnerFacesLimit(self) -> float:
        """
        Getter for property: (float) HousingMinimumRadiusOnInnerFacesLimit
         Returns the housing feature validation minimum radius on outer edges limit   
            
         
        """
        pass
    
    ## Setter for property: (float) HousingMinimumRadiusOnInnerFacesLimit

    ##  Returns the housing feature validation minimum radius on outer edges limit   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @HousingMinimumRadiusOnInnerFacesLimit.setter
    def HousingMinimumRadiusOnInnerFacesLimit(self, housingMinimumRadiusOnInnerFacesLimit: float):
        """
        Setter for property: (float) HousingMinimumRadiusOnInnerFacesLimit
         Returns the housing feature validation minimum radius on outer edges limit   
            
         
        """
        pass
    
    ## Getter for property: (bool) HousingMinimumRadiusOnOuterFaces
    ##  Returns the housing feature validation minimum radius on outer edges   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def HousingMinimumRadiusOnOuterFaces(self) -> bool:
        """
        Getter for property: (bool) HousingMinimumRadiusOnOuterFaces
         Returns the housing feature validation minimum radius on outer edges   
            
         
        """
        pass
    
    ## Setter for property: (bool) HousingMinimumRadiusOnOuterFaces

    ##  Returns the housing feature validation minimum radius on outer edges   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @HousingMinimumRadiusOnOuterFaces.setter
    def HousingMinimumRadiusOnOuterFaces(self, housingMinimumRadiusOnOuterFaces: bool):
        """
        Setter for property: (bool) HousingMinimumRadiusOnOuterFaces
         Returns the housing feature validation minimum radius on outer edges   
            
         
        """
        pass
    
    ## Getter for property: (float) HousingMinimumRadiusOnOuterFacesLimit
    ##  Returns the housing feature validation minimum radius on outer edges limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def HousingMinimumRadiusOnOuterFacesLimit(self) -> float:
        """
        Getter for property: (float) HousingMinimumRadiusOnOuterFacesLimit
         Returns the housing feature validation minimum radius on outer edges limit   
            
         
        """
        pass
    
    ## Setter for property: (float) HousingMinimumRadiusOnOuterFacesLimit

    ##  Returns the housing feature validation minimum radius on outer edges limit   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @HousingMinimumRadiusOnOuterFacesLimit.setter
    def HousingMinimumRadiusOnOuterFacesLimit(self, housingMinimumRadiusOnOuterFacesLimit: float):
        """
        Setter for property: (float) HousingMinimumRadiusOnOuterFacesLimit
         Returns the housing feature validation minimum radius on outer edges limit   
            
         
        """
        pass
    
    ## Getter for property: (str) ManufacturingProcess
    ##  Returns the manufacturing process   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def ManufacturingProcess(self) -> str:
        """
        Getter for property: (str) ManufacturingProcess
         Returns the manufacturing process   
            
         
        """
        pass
    
    ## Setter for property: (str) ManufacturingProcess

    ##  Returns the manufacturing process   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ManufacturingProcess.setter
    def ManufacturingProcess(self, manufacturingProcess: str):
        """
        Setter for property: (str) ManufacturingProcess
         Returns the manufacturing process   
            
         
        """
        pass
    
    ## Getter for property: (bool) MarkAsPlasticPart
    ##  Returns the mark as plastic part   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def MarkAsPlasticPart(self) -> bool:
        """
        Getter for property: (bool) MarkAsPlasticPart
         Returns the mark as plastic part   
            
         
        """
        pass
    
    ## Setter for property: (bool) MarkAsPlasticPart

    ##  Returns the mark as plastic part   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @MarkAsPlasticPart.setter
    def MarkAsPlasticPart(self, markAsPlasticPart: bool):
        """
        Setter for property: (bool) MarkAsPlasticPart
         Returns the mark as plastic part   
            
         
        """
        pass
    
    ## Getter for property: (bool) NegativeDraft
    ##  Returns the moldability validation negative draft   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def NegativeDraft(self) -> bool:
        """
        Getter for property: (bool) NegativeDraft
         Returns the moldability validation negative draft   
            
         
        """
        pass
    
    ## Setter for property: (bool) NegativeDraft

    ##  Returns the moldability validation negative draft   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @NegativeDraft.setter
    def NegativeDraft(self, negativeDraft: bool):
        """
        Setter for property: (bool) NegativeDraft
         Returns the moldability validation negative draft   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) NegativeDraftColor
    ##  Returns the moldability validation negative draft color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def NegativeDraftColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) NegativeDraftColor
         Returns the moldability validation negative draft color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) NegativeDraftColor

    ##  Returns the moldability validation negative draft color   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @NegativeDraftColor.setter
    def NegativeDraftColor(self, negativeDraftColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) NegativeDraftColor
         Returns the moldability validation negative draft color   
            
         
        """
        pass
    
    ## Getter for property: (float) NegativeDraftLimit
    ##  Returns the moldability validation negative draft limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return float
    @property
    def NegativeDraftLimit(self) -> float:
        """
        Getter for property: (float) NegativeDraftLimit
         Returns the moldability validation negative draft limit   
            
         
        """
        pass
    
    ## Setter for property: (float) NegativeDraftLimit

    ##  Returns the moldability validation negative draft limit   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @NegativeDraftLimit.setter
    def NegativeDraftLimit(self, negativeDraftLimit: float):
        """
        Setter for property: (float) NegativeDraftLimit
         Returns the moldability validation negative draft limit   
            
         
        """
        pass
    
    ## Getter for property: (bool) PositiveDraft
    ##  Returns the moldability validation positive draft   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def PositiveDraft(self) -> bool:
        """
        Getter for property: (bool) PositiveDraft
         Returns the moldability validation positive draft   
            
         
        """
        pass
    
    ## Setter for property: (bool) PositiveDraft

    ##  Returns the moldability validation positive draft   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @PositiveDraft.setter
    def PositiveDraft(self, positiveDraft: bool):
        """
        Setter for property: (bool) PositiveDraft
         Returns the moldability validation positive draft   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) PositiveDraftColor
    ##  Returns the moldability validation positive draft color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def PositiveDraftColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) PositiveDraftColor
         Returns the moldability validation positive draft color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) PositiveDraftColor

    ##  Returns the moldability validation positive draft color   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @PositiveDraftColor.setter
    def PositiveDraftColor(self, positiveDraftColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) PositiveDraftColor
         Returns the moldability validation positive draft color   
            
         
        """
        pass
    
    ## Getter for property: (float) PositiveDraftLimit
    ##  Returns the moldability validation positive draft limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return float
    @property
    def PositiveDraftLimit(self) -> float:
        """
        Getter for property: (float) PositiveDraftLimit
         Returns the moldability validation positive draft limit   
            
         
        """
        pass
    
    ## Setter for property: (float) PositiveDraftLimit

    ##  Returns the moldability validation positive draft limit   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @PositiveDraftLimit.setter
    def PositiveDraftLimit(self, positiveDraftLimit: float):
        """
        Setter for property: (float) PositiveDraftLimit
         Returns the moldability validation positive draft limit   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) RibColor
    ##  Returns the rib feature validation color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def RibColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) RibColor
         Returns the rib feature validation color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) RibColor

    ##  Returns the rib feature validation color   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @RibColor.setter
    def RibColor(self, ribColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) RibColor
         Returns the rib feature validation color   
            
         
        """
        pass
    
    ## Getter for property: (bool) RibHeightToNominalWallThickness
    ##  Returns the rib feature validation height to nominal wall thickness ratio   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def RibHeightToNominalWallThickness(self) -> bool:
        """
        Getter for property: (bool) RibHeightToNominalWallThickness
         Returns the rib feature validation height to nominal wall thickness ratio   
            
         
        """
        pass
    
    ## Setter for property: (bool) RibHeightToNominalWallThickness

    ##  Returns the rib feature validation height to nominal wall thickness ratio   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @RibHeightToNominalWallThickness.setter
    def RibHeightToNominalWallThickness(self, heightToNominalWallThickness: bool):
        """
        Setter for property: (bool) RibHeightToNominalWallThickness
         Returns the rib feature validation height to nominal wall thickness ratio   
            
         
        """
        pass
    
    ## Getter for property: (float) RibHeightToNominalWallThicknessLimit
    ##  Returns the rib feature validation height to nominal wall thickness ratio limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return float
    @property
    def RibHeightToNominalWallThicknessLimit(self) -> float:
        """
        Getter for property: (float) RibHeightToNominalWallThicknessLimit
         Returns the rib feature validation height to nominal wall thickness ratio limit   
            
         
        """
        pass
    
    ## Setter for property: (float) RibHeightToNominalWallThicknessLimit

    ##  Returns the rib feature validation height to nominal wall thickness ratio limit   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @RibHeightToNominalWallThicknessLimit.setter
    def RibHeightToNominalWallThicknessLimit(self, heightToNominalWallThicknessLimit: float):
        """
        Setter for property: (float) RibHeightToNominalWallThicknessLimit
         Returns the rib feature validation height to nominal wall thickness ratio limit   
            
         
        """
        pass
    
    ## Getter for property: (bool) RibMinimumRadiusAtBase
    ##  Returns the rib feature validation minimum radius at base   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def RibMinimumRadiusAtBase(self) -> bool:
        """
        Getter for property: (bool) RibMinimumRadiusAtBase
         Returns the rib feature validation minimum radius at base   
            
         
        """
        pass
    
    ## Setter for property: (bool) RibMinimumRadiusAtBase

    ##  Returns the rib feature validation minimum radius at base   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @RibMinimumRadiusAtBase.setter
    def RibMinimumRadiusAtBase(self, radiusAtBase: bool):
        """
        Setter for property: (bool) RibMinimumRadiusAtBase
         Returns the rib feature validation minimum radius at base   
            
         
        """
        pass
    
    ## Getter for property: (float) RibMinimumRadiusAtBaseLimit
    ##  Returns the rib feature validation minimum radius at base limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return float
    @property
    def RibMinimumRadiusAtBaseLimit(self) -> float:
        """
        Getter for property: (float) RibMinimumRadiusAtBaseLimit
         Returns the rib feature validation minimum radius at base limit   
            
         
        """
        pass
    
    ## Setter for property: (float) RibMinimumRadiusAtBaseLimit

    ##  Returns the rib feature validation minimum radius at base limit   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @RibMinimumRadiusAtBaseLimit.setter
    def RibMinimumRadiusAtBaseLimit(self, radiusAtBaseLimit: float):
        """
        Setter for property: (float) RibMinimumRadiusAtBaseLimit
         Returns the rib feature validation minimum radius at base limit   
            
         
        """
        pass
    
    ## Getter for property: (bool) RibMinimumThicknessAtTop
    ##  Returns the rib feature validation minimum thickness at top   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def RibMinimumThicknessAtTop(self) -> bool:
        """
        Getter for property: (bool) RibMinimumThicknessAtTop
         Returns the rib feature validation minimum thickness at top   
            
         
        """
        pass
    
    ## Setter for property: (bool) RibMinimumThicknessAtTop

    ##  Returns the rib feature validation minimum thickness at top   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @RibMinimumThicknessAtTop.setter
    def RibMinimumThicknessAtTop(self, thicknessAtTop: bool):
        """
        Setter for property: (bool) RibMinimumThicknessAtTop
         Returns the rib feature validation minimum thickness at top   
            
         
        """
        pass
    
    ## Getter for property: (float) RibMinimumThicknessAtTopLimit
    ##  Returns the rib feature validation minimum thickness at top limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return float
    @property
    def RibMinimumThicknessAtTopLimit(self) -> float:
        """
        Getter for property: (float) RibMinimumThicknessAtTopLimit
         Returns the rib feature validation minimum thickness at top limit   
            
         
        """
        pass
    
    ## Setter for property: (float) RibMinimumThicknessAtTopLimit

    ##  Returns the rib feature validation minimum thickness at top limit   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @RibMinimumThicknessAtTopLimit.setter
    def RibMinimumThicknessAtTopLimit(self, thicknessAtTopLimit: float):
        """
        Setter for property: (float) RibMinimumThicknessAtTopLimit
         Returns the rib feature validation minimum thickness at top limit   
            
         
        """
        pass
    
    ## Getter for property: (bool) RibThicknessToNominalWallThickness
    ##  Returns the rib feature validation thickness to nominal wall thickness ratio   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def RibThicknessToNominalWallThickness(self) -> bool:
        """
        Getter for property: (bool) RibThicknessToNominalWallThickness
         Returns the rib feature validation thickness to nominal wall thickness ratio   
            
         
        """
        pass
    
    ## Setter for property: (bool) RibThicknessToNominalWallThickness

    ##  Returns the rib feature validation thickness to nominal wall thickness ratio   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @RibThicknessToNominalWallThickness.setter
    def RibThicknessToNominalWallThickness(self, ribThicknessToNominalWallThk: bool):
        """
        Setter for property: (bool) RibThicknessToNominalWallThickness
         Returns the rib feature validation thickness to nominal wall thickness ratio   
            
         
        """
        pass
    
    ## Getter for property: (float) RibThicknessToNominalWallThicknessLimit
    ##  Returns the rib feature validation thickness to nominal wall thickness ratio limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return float
    @property
    def RibThicknessToNominalWallThicknessLimit(self) -> float:
        """
        Getter for property: (float) RibThicknessToNominalWallThicknessLimit
         Returns the rib feature validation thickness to nominal wall thickness ratio limit   
            
         
        """
        pass
    
    ## Setter for property: (float) RibThicknessToNominalWallThicknessLimit

    ##  Returns the rib feature validation thickness to nominal wall thickness ratio limit   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @RibThicknessToNominalWallThicknessLimit.setter
    def RibThicknessToNominalWallThicknessLimit(self, ribThicknessToNominalWallThkLimit: float):
        """
        Setter for property: (float) RibThicknessToNominalWallThicknessLimit
         Returns the rib feature validation thickness to nominal wall thickness ratio limit   
            
         
        """
        pass
    
    ## Getter for property: (bool) SharpCorners
    ##  Returns the moldability validation sharp corners   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def SharpCorners(self) -> bool:
        """
        Getter for property: (bool) SharpCorners
         Returns the moldability validation sharp corners   
            
         
        """
        pass
    
    ## Setter for property: (bool) SharpCorners

    ##  Returns the moldability validation sharp corners   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @SharpCorners.setter
    def SharpCorners(self, sharpCorners: bool):
        """
        Setter for property: (bool) SharpCorners
         Returns the moldability validation sharp corners   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) SharpCornersColor
    ##  Returns the moldability validation sharp corners color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def SharpCornersColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) SharpCornersColor
         Returns the moldability validation sharp corners color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) SharpCornersColor

    ##  Returns the moldability validation sharp corners color   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @SharpCornersColor.setter
    def SharpCornersColor(self, sharpCornersColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) SharpCornersColor
         Returns the moldability validation sharp corners color   
            
         
        """
        pass
    
    ## Getter for property: (float) SharpCornersLimit
    ##  Returns the moldability validation sharp corners limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return float
    @property
    def SharpCornersLimit(self) -> float:
        """
        Getter for property: (float) SharpCornersLimit
         Returns the moldability validation sharp corners limit   
            
         
        """
        pass
    
    ## Setter for property: (float) SharpCornersLimit

    ##  Returns the moldability validation sharp corners limit   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @SharpCornersLimit.setter
    def SharpCornersLimit(self, sharpCornersLimit: float):
        """
        Setter for property: (float) SharpCornersLimit
         Returns the moldability validation sharp corners limit   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) SnapJointColor
    ##  Returns the snap joint feature validation color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def SnapJointColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) SnapJointColor
         Returns the snap joint feature validation color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) SnapJointColor

    ##  Returns the snap joint feature validation color   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @SnapJointColor.setter
    def SnapJointColor(self, snapJointColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) SnapJointColor
         Returns the snap joint feature validation color   
            
         
        """
        pass
    
    ## Getter for property: (bool) SnapJointMaximumThicknessAtBase
    ##  Returns the snap joint feature validation maximum thickness at base   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def SnapJointMaximumThicknessAtBase(self) -> bool:
        """
        Getter for property: (bool) SnapJointMaximumThicknessAtBase
         Returns the snap joint feature validation maximum thickness at base   
            
         
        """
        pass
    
    ## Setter for property: (bool) SnapJointMaximumThicknessAtBase

    ##  Returns the snap joint feature validation maximum thickness at base   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @SnapJointMaximumThicknessAtBase.setter
    def SnapJointMaximumThicknessAtBase(self, snapJointMaximumThicknessAtBase: bool):
        """
        Setter for property: (bool) SnapJointMaximumThicknessAtBase
         Returns the snap joint feature validation maximum thickness at base   
            
         
        """
        pass
    
    ## Getter for property: (float) SnapJointMaximumThicknessAtBaseLimit
    ##  Returns the snap joint feature validation maximum thickness at base limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def SnapJointMaximumThicknessAtBaseLimit(self) -> float:
        """
        Getter for property: (float) SnapJointMaximumThicknessAtBaseLimit
         Returns the snap joint feature validation maximum thickness at base limit   
            
         
        """
        pass
    
    ## Setter for property: (float) SnapJointMaximumThicknessAtBaseLimit

    ##  Returns the snap joint feature validation maximum thickness at base limit   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @SnapJointMaximumThicknessAtBaseLimit.setter
    def SnapJointMaximumThicknessAtBaseLimit(self, snapJointMaximumThicknessAtBaseLimit: float):
        """
        Setter for property: (float) SnapJointMaximumThicknessAtBaseLimit
         Returns the snap joint feature validation maximum thickness at base limit   
            
         
        """
        pass
    
    ## Getter for property: (bool) SnapJointMinimumDraftOnOuterFaces
    ##  Returns the snap joint feature validation minimum draft on outer faces   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def SnapJointMinimumDraftOnOuterFaces(self) -> bool:
        """
        Getter for property: (bool) SnapJointMinimumDraftOnOuterFaces
         Returns the snap joint feature validation minimum draft on outer faces   
            
         
        """
        pass
    
    ## Setter for property: (bool) SnapJointMinimumDraftOnOuterFaces

    ##  Returns the snap joint feature validation minimum draft on outer faces   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @SnapJointMinimumDraftOnOuterFaces.setter
    def SnapJointMinimumDraftOnOuterFaces(self, snapJointMinimumDraftOnOuterFaces: bool):
        """
        Setter for property: (bool) SnapJointMinimumDraftOnOuterFaces
         Returns the snap joint feature validation minimum draft on outer faces   
            
         
        """
        pass
    
    ## Getter for property: (float) SnapJointMinimumDraftOnOuterFacesLimit
    ##  Returns the snap joint feature validation minimum draft on outer faces limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def SnapJointMinimumDraftOnOuterFacesLimit(self) -> float:
        """
        Getter for property: (float) SnapJointMinimumDraftOnOuterFacesLimit
         Returns the snap joint feature validation minimum draft on outer faces limit   
            
         
        """
        pass
    
    ## Setter for property: (float) SnapJointMinimumDraftOnOuterFacesLimit

    ##  Returns the snap joint feature validation minimum draft on outer faces limit   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @SnapJointMinimumDraftOnOuterFacesLimit.setter
    def SnapJointMinimumDraftOnOuterFacesLimit(self, snapJointMinimumDraftOnOuterFacesLimit: float):
        """
        Setter for property: (float) SnapJointMinimumDraftOnOuterFacesLimit
         Returns the snap joint feature validation minimum draft on outer faces limit   
            
         
        """
        pass
    
    ## Getter for property: (bool) SnapJointMinimumWidthAtBase
    ##  Returns the snap joint feature validation minimum width at base   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def SnapJointMinimumWidthAtBase(self) -> bool:
        """
        Getter for property: (bool) SnapJointMinimumWidthAtBase
         Returns the snap joint feature validation minimum width at base   
            
         
        """
        pass
    
    ## Setter for property: (bool) SnapJointMinimumWidthAtBase

    ##  Returns the snap joint feature validation minimum width at base   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @SnapJointMinimumWidthAtBase.setter
    def SnapJointMinimumWidthAtBase(self, snapJointMinimumWidthAtBase: bool):
        """
        Setter for property: (bool) SnapJointMinimumWidthAtBase
         Returns the snap joint feature validation minimum width at base   
            
         
        """
        pass
    
    ## Getter for property: (float) SnapJointMinimumWidthAtBaseLimit
    ##  Returns the snap joint feature validation minimum width at base limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def SnapJointMinimumWidthAtBaseLimit(self) -> float:
        """
        Getter for property: (float) SnapJointMinimumWidthAtBaseLimit
         Returns the snap joint feature validation minimum width at base limit   
            
         
        """
        pass
    
    ## Setter for property: (float) SnapJointMinimumWidthAtBaseLimit

    ##  Returns the snap joint feature validation minimum width at base limit   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @SnapJointMinimumWidthAtBaseLimit.setter
    def SnapJointMinimumWidthAtBaseLimit(self, snapJointMinimumWidthAtBaseLimit: float):
        """
        Setter for property: (float) SnapJointMinimumWidthAtBaseLimit
         Returns the snap joint feature validation minimum width at base limit   
            
         
        """
        pass
    
    ## Getter for property: (bool) SnapJointPermissibleDeflection
    ##  Returns the snap joint feature validation of permissible deflection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def SnapJointPermissibleDeflection(self) -> bool:
        """
        Getter for property: (bool) SnapJointPermissibleDeflection
         Returns the snap joint feature validation of permissible deflection   
            
         
        """
        pass
    
    ## Setter for property: (bool) SnapJointPermissibleDeflection

    ##  Returns the snap joint feature validation of permissible deflection   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @SnapJointPermissibleDeflection.setter
    def SnapJointPermissibleDeflection(self, snapJointPermissibleDeflection: bool):
        """
        Setter for property: (bool) SnapJointPermissibleDeflection
         Returns the snap joint feature validation of permissible deflection   
            
         
        """
        pass
    
    ## Getter for property: (float) SnapJointPermissibleDeflectionLimit
    ##  Returns the snap joint feature validation permissible deflection limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def SnapJointPermissibleDeflectionLimit(self) -> float:
        """
        Getter for property: (float) SnapJointPermissibleDeflectionLimit
         Returns the snap joint feature validation permissible deflection limit   
            
         
        """
        pass
    
    ## Setter for property: (float) SnapJointPermissibleDeflectionLimit

    ##  Returns the snap joint feature validation permissible deflection limit   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @SnapJointPermissibleDeflectionLimit.setter
    def SnapJointPermissibleDeflectionLimit(self, snapJointPermissibleDeflectionLimit: float):
        """
        Setter for property: (float) SnapJointPermissibleDeflectionLimit
         Returns the snap joint feature validation permissible deflection limit   
            
         
        """
        pass
    
    ## Getter for property: (float) SnapJointPermissibleStrain
    ##  Returns the snap joint feature permissible strain   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def SnapJointPermissibleStrain(self) -> float:
        """
        Getter for property: (float) SnapJointPermissibleStrain
         Returns the snap joint feature permissible strain   
            
         
        """
        pass
    
    ## Setter for property: (float) SnapJointPermissibleStrain

    ##  Returns the snap joint feature permissible strain   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @SnapJointPermissibleStrain.setter
    def SnapJointPermissibleStrain(self, snapJointPermissibleStrain: float):
        """
        Setter for property: (float) SnapJointPermissibleStrain
         Returns the snap joint feature permissible strain   
            
         
        """
        pass
    
    ## Getter for property: (bool) ThickWalls
    ##  Returns the moldability validation thick walls   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def ThickWalls(self) -> bool:
        """
        Getter for property: (bool) ThickWalls
         Returns the moldability validation thick walls   
            
         
        """
        pass
    
    ## Setter for property: (bool) ThickWalls

    ##  Returns the moldability validation thick walls   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ThickWalls.setter
    def ThickWalls(self, thickWalls: bool):
        """
        Setter for property: (bool) ThickWalls
         Returns the moldability validation thick walls   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ThickWallsColor
    ##  Returns the moldability validation thick walls color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def ThickWallsColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ThickWallsColor
         Returns the moldability validation thick walls color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ThickWallsColor

    ##  Returns the moldability validation thick walls color   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ThickWallsColor.setter
    def ThickWallsColor(self, thickWallsColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ThickWallsColor
         Returns the moldability validation thick walls color   
            
         
        """
        pass
    
    ## Getter for property: (float) ThickWallsLimit
    ##  Returns the moldability validation thick walls limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return float
    @property
    def ThickWallsLimit(self) -> float:
        """
        Getter for property: (float) ThickWallsLimit
         Returns the moldability validation thick walls limit   
            
         
        """
        pass
    
    ## Setter for property: (float) ThickWallsLimit

    ##  Returns the moldability validation thick walls limit   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ThickWallsLimit.setter
    def ThickWallsLimit(self, thickWallsLimit: float):
        """
        Setter for property: (float) ThickWallsLimit
         Returns the moldability validation thick walls limit   
            
         
        """
        pass
    
    ## Getter for property: (bool) ThinWalls
    ##  Returns the moldability validation thin walls   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def ThinWalls(self) -> bool:
        """
        Getter for property: (bool) ThinWalls
         Returns the moldability validation thin walls   
            
         
        """
        pass
    
    ## Setter for property: (bool) ThinWalls

    ##  Returns the moldability validation thin walls   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ThinWalls.setter
    def ThinWalls(self, thinWalls: bool):
        """
        Setter for property: (bool) ThinWalls
         Returns the moldability validation thin walls   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ThinWallsColor
    ##  Returns the moldability validation thin walls color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def ThinWallsColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ThinWallsColor
         Returns the moldability validation thin walls color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ThinWallsColor

    ##  Returns the moldability validation thin walls color   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ThinWallsColor.setter
    def ThinWallsColor(self, thinWallsColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ThinWallsColor
         Returns the moldability validation thin walls color   
            
         
        """
        pass
    
    ## Getter for property: (float) ThinWallsLimit
    ##  Returns the moldability validation thin walls limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return float
    @property
    def ThinWallsLimit(self) -> float:
        """
        Getter for property: (float) ThinWallsLimit
         Returns the moldability validation thin walls limit   
            
         
        """
        pass
    
    ## Setter for property: (float) ThinWallsLimit

    ##  Returns the moldability validation thin walls limit   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ThinWallsLimit.setter
    def ThinWallsLimit(self, thinWallsLimit: float):
        """
        Setter for property: (float) ThinWallsLimit
         Returns the moldability validation thin walls limit   
            
         
        """
        pass
    
    ## Getter for property: (bool) UndercutRegions
    ##  Returns the moldability validation undercut regions   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def UndercutRegions(self) -> bool:
        """
        Getter for property: (bool) UndercutRegions
         Returns the moldability validation undercut regions   
            
         
        """
        pass
    
    ## Setter for property: (bool) UndercutRegions

    ##  Returns the moldability validation undercut regions   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @UndercutRegions.setter
    def UndercutRegions(self, undercutRegions: bool):
        """
        Setter for property: (bool) UndercutRegions
         Returns the moldability validation undercut regions   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) UndercutRegionsColor
    ##  Returns the moldability validation undercut regions color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def UndercutRegionsColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) UndercutRegionsColor
         Returns the moldability validation undercut regions color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) UndercutRegionsColor

    ##  Returns the moldability validation undercut regions color   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @UndercutRegionsColor.setter
    def UndercutRegionsColor(self, undercutRegionsColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) UndercutRegionsColor
         Returns the moldability validation undercut regions color   
            
         
        """
        pass
    
    ## Getter for property: (bool) VerticalWalls
    ##  Returns the moldability validation vertical walls   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def VerticalWalls(self) -> bool:
        """
        Getter for property: (bool) VerticalWalls
         Returns the moldability validation vertical walls   
            
         
        """
        pass
    
    ## Setter for property: (bool) VerticalWalls

    ##  Returns the moldability validation vertical walls   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @VerticalWalls.setter
    def VerticalWalls(self, verticalWalls: bool):
        """
        Setter for property: (bool) VerticalWalls
         Returns the moldability validation vertical walls   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) VerticalWallsColor
    ##  Returns the moldability validation vertical walls color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def VerticalWallsColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) VerticalWallsColor
         Returns the moldability validation vertical walls color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) VerticalWallsColor

    ##  Returns the moldability validation vertical walls color   
    ##     
    ##  
    ## Setter License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @VerticalWallsColor.setter
    def VerticalWallsColor(self, verticalWallsColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) VerticalWallsColor
         Returns the moldability validation vertical walls color   
            
         
        """
        pass
    
import NXOpen
##  Surface Identifier builder  <br> To create a new instance of this class, use @link NXOpen::PlasticDesigner::Manager::CreateSurfaceIdentifierBuilder  NXOpen::PlasticDesigner::Manager::CreateSurfaceIdentifierBuilder @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class SurfaceIdentifierBuilder(NXOpen.Builder): 
    """ Surface Identifier builder """


    ##  Creates a @link PlasticDesigner::IdentifierDataBuilder PlasticDesigner::IdentifierDataBuilder@endlink  and append it to the identifier data list. 
    ##             If @link PlasticDesigner::IdentifierDataBuilder PlasticDesigner::IdentifierDataBuilder@endlink  with same label already exist,
    ##             then existing instance will be returned by setting remaining input parameters 
    ##  @return databuilder (@link IdentifierDataBuilder NXOpen.PlasticDesigner.IdentifierDataBuilder@endlink):  @link PlasticDesigner::IdentifierDataBuilder PlasticDesigner::IdentifierDataBuilder@endlink  instance.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ## <param name="label"> (str)  Label </param>
    ## <param name="highlightColor"> (@link NXOpen.NXColor NXOpen.NXColor@endlink)  Highlight color </param>
    ## <param name="faces"> (@link NXOpen.Face List[NXOpen.Face]@endlink)  Faces</param>
    def AddIdentifier(self, label: str, highlightColor: NXOpen.NXColor, faces: List[NXOpen.Face]) -> IdentifierDataBuilder:
        """
         Creates a @link PlasticDesigner::IdentifierDataBuilder PlasticDesigner::IdentifierDataBuilder@endlink  and append it to the identifier data list. 
                    If @link PlasticDesigner::IdentifierDataBuilder PlasticDesigner::IdentifierDataBuilder@endlink  with same label already exist,
                    then existing instance will be returned by setting remaining input parameters 
         @return databuilder (@link IdentifierDataBuilder NXOpen.PlasticDesigner.IdentifierDataBuilder@endlink):  @link PlasticDesigner::IdentifierDataBuilder PlasticDesigner::IdentifierDataBuilder@endlink  instance.
        """
        pass
    
    ##  Remove and delete an identifier corresponding to input label.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_plastics_base (" NX Plastic Designer Base")
    ## 
    ## <param name="label"> (str)  Label </param>
    def DeleteIdentifier(self, label: str) -> None:
        """
         Remove and delete an identifier corresponding to input label.
        """
        pass
    
    ##  Returns the identifier corresponding to input label. Return NULL if identifier not found
    ##  @return databuilder (@link IdentifierDataBuilder NXOpen.PlasticDesigner.IdentifierDataBuilder@endlink):   @link PlasticDesigner::IdentifierDataBuilder PlasticDesigner::IdentifierDataBuilder@endlink  instance.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="label"> (str)  Label </param>
    def GetIdentifier(self, label: str) -> IdentifierDataBuilder:
        """
         Returns the identifier corresponding to input label. Return NULL if identifier not found
         @return databuilder (@link IdentifierDataBuilder NXOpen.PlasticDesigner.IdentifierDataBuilder@endlink):   @link PlasticDesigner::IdentifierDataBuilder PlasticDesigner::IdentifierDataBuilder@endlink  instance.
        """
        pass
    
    ##  Returns the array of identifiers
    ##  @return identifiers (@link IdentifierDataBuilder List[NXOpen.PlasticDesigner.IdentifierDataBuilder]@endlink):  array of @link PlasticDesigner::IdentifierDataBuilder PlasticDesigner::IdentifierDataBuilder@endlink  instances.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def GetIdentifiers(self) -> List[IdentifierDataBuilder]:
        """
         Returns the array of identifiers
         @return identifiers (@link IdentifierDataBuilder List[NXOpen.PlasticDesigner.IdentifierDataBuilder]@endlink):  array of @link PlasticDesigner::IdentifierDataBuilder PlasticDesigner::IdentifierDataBuilder@endlink  instances.
        """
        pass
    
## @package NXOpen.PlasticDesigner
## Classes, Enums and Structs under NXOpen.PlasticDesigner namespace

##  @link DrawDirectionBuilderDrawDirection NXOpen.PlasticDesigner.DrawDirectionBuilderDrawDirection @endlink is an alias for @link DrawDirectionBuilder.DrawDirection NXOpen.PlasticDesigner.DrawDirectionBuilder.DrawDirection@endlink
DrawDirectionBuilderDrawDirection = DrawDirectionBuilder.DrawDirection


