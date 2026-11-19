from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class AnimationCameraBuilder(CameraBuilder): 
    """
Represents a animation camera builder
"""
    @property
    def CameraConstrainedPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) CameraConstrainedPoint
         Returns the camera constrained point   
            
         
        """
        pass
    @CameraConstrainedPoint.setter
    def CameraConstrainedPoint(self, cameraConstrainedPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) CameraConstrainedPoint
         Returns the camera constrained point   
            
         
        """
        pass
    @property
    def CameraConstrainedUpperVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) CameraConstrainedUpperVector
         Returns the camera constrained upper vector   
            
         
        """
        pass
    @CameraConstrainedUpperVector.setter
    def CameraConstrainedUpperVector(self, cameraUpperVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) CameraConstrainedUpperVector
         Returns the camera constrained upper vector   
            
         
        """
        pass
    @property
    def CameraPositioningConstrained(self) -> bool:
        """
        Getter for property: (bool) CameraPositioningConstrained
         Returns the camera positioning constrained   
            
         
        """
        pass
    @CameraPositioningConstrained.setter
    def CameraPositioningConstrained(self, positioningConstrained: bool):
        """
        Setter for property: (bool) CameraPositioningConstrained
         Returns the camera positioning constrained   
            
         
        """
        pass
    @property
    def CameraTransformSource(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: ( NXOpen.SelectTaggedObject) CameraTransformSource
         Returns the camera transform source   
            
         
        """
        pass
    @property
    def TargetConstrainedPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) TargetConstrainedPoint
         Returns the target constrained point   
            
         
        """
        pass
    @TargetConstrainedPoint.setter
    def TargetConstrainedPoint(self, position: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) TargetConstrainedPoint
         Returns the target constrained point   
            
         
        """
        pass
    @property
    def TargetPositioningConstrained(self) -> bool:
        """
        Getter for property: (bool) TargetPositioningConstrained
         Returns the target positioning constrained   
            
         
        """
        pass
    @TargetPositioningConstrained.setter
    def TargetPositioningConstrained(self, positioningConstrained: bool):
        """
        Setter for property: (bool) TargetPositioningConstrained
         Returns the target positioning constrained   
            
         
        """
        pass
    @property
    def TargetTransformSource(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: ( NXOpen.SelectTaggedObject) TargetTransformSource
         Returns the target transform source   
            
         
        """
        pass
import NXOpen
class AnimationCameraCollection(NXOpen.TaggedObjectCollection): 
    """
Represents a collection of animation cameras
"""
    def CreateAnimationCameraBuilder(self, camera: AnimationCamera) -> AnimationCameraBuilder:
        """
         Creates a NXOpen.Display.AnimationCameraBuilder object if camera is . 
         Returns builder ( AnimationCameraBuilder NXOpen):  return camera builder .
        """
        pass
    def FindObject(self, journal_identifier: str) -> AnimationCamera:
        """
         Finds the  NXOpen.Display.AnimationCamera  with the given identifier as recorded in a journal. 
         Returns found ( AnimationCamera NXOpen):  Animation camera found .
        """
        pass
class AnimationCamera(Camera): 
    """ Represents a animaiton camera """
    pass
import NXOpen
class Background(NXOpen.Builder): 
    """
    Represents a NXOpen.Display.Background
    Background defines how background pixels are displayed.  The background
    resides on a virtual plane at the back of a view.  This background is used
    for display in Studio rendering style and High Quality Images.
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return .
    """
    class BackgroundDomeType(Enum):
        """
        Members Include: 
         |Finite|  finite 3D dome
         |Infinite|  infinite 3D dome

        """
        Finite: int
        Infinite: int
        @staticmethod
        def ValueOf(value: int) -> Background.BackgroundDomeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class BackgroundImageType(Enum):
        """
        Members Include: 
         |LightBackground1|  Predefined light background 1 
         |LightBackground2|  Predefined light background 2 
         |DarkBackground1|  Predefined dark background 1 
         |DarkBackground2|  Predefined dark background 2 
         |ClassicBackground1|  Predefined classic background 1 
         |ClassicBackground2|  Predefined classic background 2 
         |SystemBackground|  Predefined system background 
         |CustomImage|  Custom image background 

        """
        LightBackground1: int
        LightBackground2: int
        DarkBackground1: int
        DarkBackground2: int
        ClassicBackground1: int
        ClassicBackground2: int
        SystemBackground: int
        CustomImage: int
        @staticmethod
        def ValueOf(value: int) -> Background.BackgroundImageType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CategoryType(Enum):
        """
        Members Include: 
         |Flat|  2D Background 
         |Dome|  3D Dome 

        """
        Flat: int
        Dome: int
        @staticmethod
        def ValueOf(value: int) -> Background.CategoryType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ShadedType(Enum):
        """
        Members Include: 
         |SystemBackground|  a system background 
         |Plain|  single color background 
         |Graduated|  two color background, which varies between them 
         |Image|  an image file displayed in the background 

        """
        SystemBackground: int
        Plain: int
        Graduated: int
        Image: int
        @staticmethod
        def ValueOf(value: int) -> Background.ShadedType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SystemBackgroundType(Enum):
        """
        Members Include: 
         |White|  Plain white Colored background 
         |Light|  Plain light Colored background 
         |GraduatedLight|  Graduated light colored background 
         |GraduatedDark|  Graduated dark colored background 
         |Dark|  Plain dark Colored background 
         |LightImage|  Light theme Iamge background 
         |DarkImage|  Dark theme Iamge background 

        """
        White: int
        Light: int
        GraduatedLight: int
        GraduatedDark: int
        Dark: int
        LightImage: int
        DarkImage: int
        @staticmethod
        def ValueOf(value: int) -> Background.SystemBackgroundType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Type(Enum):
        """
        Members Include: 
         |Plain|  single color background 
         |Graduated|  two color background, which varies between them 
         |Image|  an image file displayed in the background 
         |HemiDome|  an 3D HDR image displayed in the background 

        """
        Plain: int
        Graduated: int
        Image: int
        HemiDome: int
        @staticmethod
        def ValueOf(value: int) -> Background.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BackgroundCategory(self) -> Background.CategoryType:
        """
        Getter for property: ( Background.CategoryType NXOpen) BackgroundCategory
         Returns the background 2D or 3D type   
            
         
        """
        pass
    @BackgroundCategory.setter
    def BackgroundCategory(self, backgroundCategoryType: Background.CategoryType):
        """
        Setter for property: ( Background.CategoryType NXOpen) BackgroundCategory
         Returns the background 2D or 3D type   
            
         
        """
        pass
    @property
    def BackgroundShadedViewsBackgroundImage(self) -> int:
        """
        Getter for property: (int) BackgroundShadedViewsBackgroundImage
         Returns the shaded background type   
            
         
        """
        pass
    @BackgroundShadedViewsBackgroundImage.setter
    def BackgroundShadedViewsBackgroundImage(self, backgroundImgType: int):
        """
        Setter for property: (int) BackgroundShadedViewsBackgroundImage
         Returns the shaded background type   
            
         
        """
        pass
    @property
    def BackgroundShadedViewsType(self) -> int:
        """
        Getter for property: (int) BackgroundShadedViewsType
         Returns the shaded background type   
            
         
        """
        pass
    @BackgroundShadedViewsType.setter
    def BackgroundShadedViewsType(self, backgroundType: int):
        """
        Setter for property: (int) BackgroundShadedViewsType
         Returns the shaded background type   
            
         
        """
        pass
    @property
    def BackgroundType(self) -> Background.Type:
        """
        Getter for property: ( Background.Type NXOpen) BackgroundType
         Returns the background type   
            
         
        """
        pass
    @BackgroundType.setter
    def BackgroundType(self, backgroundType: Background.Type):
        """
        Setter for property: ( Background.Type NXOpen) BackgroundType
         Returns the background type   
            
         
        """
        pass
    @property
    def BackgroundWireframeViewsType(self) -> int:
        """
        Getter for property: (int) BackgroundWireframeViewsType
         Returns the wireframe background type   
            
         
        """
        pass
    @BackgroundWireframeViewsType.setter
    def BackgroundWireframeViewsType(self, backgroundType: int):
        """
        Setter for property: (int) BackgroundWireframeViewsType
         Returns the wireframe background type   
            
         
        """
        pass
    @property
    def BackgroundWireframeViewsUsedShadedViewsSetting(self) -> bool:
        """
        Getter for property: (bool) BackgroundWireframeViewsUsedShadedViewsSetting
         Returns an option to used shaded views setting in wireframe views   
            
         
        """
        pass
    @BackgroundWireframeViewsUsedShadedViewsSetting.setter
    def BackgroundWireframeViewsUsedShadedViewsSetting(self, use_shaded_views_setting: bool):
        """
        Setter for property: (bool) BackgroundWireframeViewsUsedShadedViewsSetting
         Returns an option to used shaded views setting in wireframe views   
            
         
        """
        pass
    @property
    def DomeImage(self) -> Image:
        """
        Getter for property: ( Image NXOpen) DomeImage
         Returns the dome background's image builder   
            
         
        """
        pass
    @DomeImage.setter
    def DomeImage(self, dome_image_builder: Image):
        """
        Setter for property: ( Image NXOpen) DomeImage
         Returns the dome background's image builder   
            
         
        """
        pass
    @property
    def DomeImageFilename(self) -> str:
        """
        Getter for property: (str) DomeImageFilename
         Returns the background's dome image filename   
            
         
        """
        pass
    @DomeImageFilename.setter
    def DomeImageFilename(self, dome_image_file_name: str):
        """
        Setter for property: (str) DomeImageFilename
         Returns the background's dome image filename   
            
         
        """
        pass
    @property
    def DomeOrigin(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) DomeOrigin
         Returns the origin   
            
         
        """
        pass
    @DomeOrigin.setter
    def DomeOrigin(self, origin: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) DomeOrigin
         Returns the origin   
            
         
        """
        pass
    @property
    def DomeSize(self) -> float:
        """
        Getter for property: (float) DomeSize
         Returns the dome size   
            
         
        """
        pass
    @DomeSize.setter
    def DomeSize(self, dome_size: float):
        """
        Setter for property: (float) DomeSize
         Returns the dome size   
            
         
        """
        pass
    @property
    def DomeType(self) -> Background.BackgroundDomeType:
        """
        Getter for property: ( Background.BackgroundDomeType NXOpen) DomeType
         Returns the dome type   
            
         
        """
        pass
    @DomeType.setter
    def DomeType(self, domeType: Background.BackgroundDomeType):
        """
        Setter for property: ( Background.BackgroundDomeType NXOpen) DomeType
         Returns the dome type   
            
         
        """
        pass
    @property
    def Image(self) -> Image:
        """
        Getter for property: ( Image NXOpen) Image
         Returns the background's image builder   
            
         
        """
        pass
    @Image.setter
    def Image(self, image_builder: Image):
        """
        Setter for property: ( Image NXOpen) Image
         Returns the background's image builder   
            
         
        """
        pass
    @property
    def ImageFilename(self) -> str:
        """
        Getter for property: (str) ImageFilename
         Returns the background's image filename   
            
         
        """
        pass
    @ImageFilename.setter
    def ImageFilename(self, image_file_name: str):
        """
        Setter for property: (str) ImageFilename
         Returns the background's image filename   
            
         
        """
        pass
    @property
    def ImageHorizon(self) -> float:
        """
        Getter for property: (float) ImageHorizon
         Returns the dome image horizon   
            
         
        """
        pass
    @ImageHorizon.setter
    def ImageHorizon(self, imageHorizon: float):
        """
        Setter for property: (float) ImageHorizon
         Returns the dome image horizon   
            
         
        """
        pass
    @property
    def ImageRotation(self) -> float:
        """
        Getter for property: (float) ImageRotation
         Returns the image rotation angle (in degrees)   
            
         
        """
        pass
    @ImageRotation.setter
    def ImageRotation(self, imageRotation: float):
        """
        Setter for property: (float) ImageRotation
         Returns the image rotation angle (in degrees)   
            
         
        """
        pass
    @property
    def ImageUpVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ImageUpVector
         Returns the image up vector direction, relative to the absolute coordinate system   
            
         
        """
        pass
    @ImageUpVector.setter
    def ImageUpVector(self, imageUpVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ImageUpVector
         Returns the image up vector direction, relative to the absolute coordinate system   
            
         
        """
        pass
    @property
    def UseStageSizeAndOrientation(self) -> bool:
        """
        Getter for property: (bool) UseStageSizeAndOrientation
         Returns whether to use stage Size and Orientation   
            
         
        """
        pass
    @UseStageSizeAndOrientation.setter
    def UseStageSizeAndOrientation(self, use_stage_size_and_orientation: bool):
        """
        Setter for property: (bool) UseStageSizeAndOrientation
         Returns whether to use stage Size and Orientation   
            
         
        """
        pass
    def GetBackgroundShadedViewsGraduatedBottom(self) -> List[float]:
        """
         Returns the shaded background graduated bottom color 
         Returns bottomColor (List[float]):  Array of 3 rgb values, each between 0 and 1 .
        """
        pass
    def GetBackgroundShadedViewsGraduatedTop(self) -> List[float]:
        """
         Returns the shaded background graduated top color 
         Returns topColor (List[float]):  Array of 3 rgb values, each between 0 and 1 .
        """
        pass
    def GetBackgroundShadedViewsPlain(self) -> List[float]:
        """
         Returns the shaded background plain color 
         Returns plainColor (List[float]):  Array of 3 rgb values, each between 0 and 1 .
        """
        pass
    def GetBackgroundWireframeViewsGraduatedBottom(self) -> List[float]:
        """
         Returns the wireframe background graduated bottom color 
         Returns bottomColor (List[float]):  Array of 3 rgb values, each between 0 and 1 .
        """
        pass
    def GetBackgroundWireframeViewsGraduatedTop(self) -> List[float]:
        """
         Returns the wireframe background graduated top color 
         Returns topColor (List[float]):  Array of 3 rgb values, each between 0 and 1 .
        """
        pass
    def GetBackgroundWireframeViewsPlain(self) -> List[float]:
        """
         Returns the wireframe background plain color 
         Returns plainColor (List[float]):  Array of 3 rgb values, each between 0 and 1 .
        """
        pass
    def GetBottomColor(self) -> List[float]:
        """
         Returns the bottom color 
         Returns bottomColor (List[float]):  Array of 3 rgb values, each between 0 and 1 .
        """
        pass
    def GetTopColor(self) -> List[float]:
        """
         Returns the top color 
         Returns topColor (List[float]):  Array of 3 rgb values, each between 0 and 1 .
        """
        pass
    def ImageFileSelect(self) -> None:
        """
         Gets an image file using file selection. 
        """
        pass
    def SetBackgroundShadedViewsGraduatedBottom(self, bottomColor: List[float]) -> None:
        """
         Set the shaded background graduated bottom color 
        """
        pass
    def SetBackgroundShadedViewsGraduatedTop(self, topColor: List[float]) -> None:
        """
         Set the shaded background graduated top color 
        """
        pass
    def SetBackgroundShadedViewsPlain(self, plainColor: List[float]) -> None:
        """
         Set the shaded background plain color 
        """
        pass
    def SetBackgroundWireframeViewsGraduatedBottom(self, bottomColor: List[float]) -> None:
        """
         Set the wireframe background graduated bottom color 
        """
        pass
    def SetBackgroundWireframeViewsGraduatedTop(self, topColor: List[float]) -> None:
        """
         Set the wireframe background graduated top color 
        """
        pass
    def SetBackgroundWireframeViewsPlain(self, plainColor: List[float]) -> None:
        """
         Set the wireframe background plain color 
        """
        pass
    def SetBottomColor(self, bottomColor: List[float]) -> None:
        """
         Sets the bottom color 
        """
        pass
    def SetTopColor(self, topColor: List[float]) -> None:
        """
         Sets the top color 
        """
        pass
    def ShadedBackgroundOptionDark(self) -> None:
        """
         Sets shaded view background to a dark color. 
        """
        pass
    def ShadedBackgroundOptionDarkImage(self) -> None:
        """
         Sets shaded view background to use a dark-colored image. 
        """
        pass
    def ShadedBackgroundOptionGraduatedDark(self) -> None:
        """
         Sets shaded view background to graduated dark gray. 
        """
        pass
    def ShadedBackgroundOptionGraduatedLight(self) -> None:
        """
         Sets shaded view background to graduated light gray. 
        """
        pass
    def ShadedBackgroundOptionLight(self) -> None:
        """
         Sets shaded view background to a light color. 
        """
        pass
    def ShadedBackgroundOptionLightImage(self) -> None:
        """
         Sets shaded view background to use a light-colored image. 
        """
        pass
    def ShadedBackgroundOptionWhite(self) -> None:
        """
         Sets shaded view background to white. 
        """
        pass
    def WireframeBackgroundOptionDark(self) -> None:
        """
         Sets wireframe view background to a dark color. 
        """
        pass
    def WireframeBackgroundOptionGraduatedDark(self) -> None:
        """
         Sets wireframe view background to graduated dark gray. 
        """
        pass
    def WireframeBackgroundOptionGraduatedLight(self) -> None:
        """
         Sets wireframe view background to graduated light gray. 
        """
        pass
    def WireframeBackgroundOptionLight(self) -> None:
        """
         Sets wireframe view background to a light color. 
        """
        pass
    def WireframeBackgroundOptionWhite(self) -> None:
        """
         Sets wireframe view background to white. 
        """
        pass
import NXOpen
class BoundedGridBuilder(GridBuilder): 
    """ Represents the builder for creating a bounded grid NXOpen.Display.BoundedGrid. 
     """
    class LabelReferenceType(Enum):
        """
        Members Include: 
         |Local|  Use local grid origin 
                                                                            to determine grid 
                                                                            line offset labels 
         |Wcs|  Use projection of WCS origin on the
                                                                            grid plane to determine grid line offset 
                                                                            labels 
         |Absolute|  Use projection of absolute origin on the
                                                                            grid plane to determine grid line offset
                                                                            labels 

        """
        Local: int
        Wcs: int
        Absolute: int
        @staticmethod
        def ValueOf(value: int) -> BoundedGridBuilder.LabelReferenceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ShowLabelType(Enum):
        """
        Members Include: 
         |Always|  Always show label 
         |ParalleltoView|  Show labels when grid 
                                                                      orientation is aligned with 
                                                                      the view orientation 
         |NotSet|  Never show labels 

        """
        Always: int
        ParalleltoView: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> BoundedGridBuilder.ShowLabelType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns the associative   
            
         
        """
        pass
    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
         Returns the associative   
            
         
        """
        pass
    @property
    def LabelReference(self) -> BoundedGridBuilder.LabelReferenceType:
        """
        Getter for property: ( BoundedGridBuilder.LabelReferenceType NXOpen) LabelReference
         Returns the label reference   
            
         
        """
        pass
    @LabelReference.setter
    def LabelReference(self, labelReference: BoundedGridBuilder.LabelReferenceType):
        """
        Setter for property: ( BoundedGridBuilder.LabelReferenceType NXOpen) LabelReference
         Returns the label reference   
            
         
        """
        pass
    @property
    def LocalOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) LocalOrigin
         Returns the local origin   
            
         
        """
        pass
    @LocalOrigin.setter
    def LocalOrigin(self, localOrigin: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) LocalOrigin
         Returns the local origin   
            
         
        """
        pass
    @property
    def SectionCurveSettings(self) -> SectionCurveSettingsBuilder:
        """
        Getter for property: ( SectionCurveSettingsBuilder NXOpen) SectionCurveSettings
         Returns the curve settings builder   
            
         
        """
        pass
    @property
    def ShowLabel(self) -> BoundedGridBuilder.ShowLabelType:
        """
        Getter for property: ( BoundedGridBuilder.ShowLabelType NXOpen) ShowLabel
         Returns the show labels   
            
         
        """
        pass
    @ShowLabel.setter
    def ShowLabel(self, showLabelType: BoundedGridBuilder.ShowLabelType):
        """
        Setter for property: ( BoundedGridBuilder.ShowLabelType NXOpen) ShowLabel
         Returns the show labels   
            
         
        """
        pass
    def GetCornerPoints(self) -> Tuple[bool, NXOpen.Point3d, NXOpen.Point3d, NXOpen.Point3d, NXOpen.Point3d]:
        """
         Gets corner points of the grid 
         Returns A tuple consisting of (validCornerPoints, point1, point2, point3, point4). 
         - validCornerPoints is: bool. Flag indicating whether the
                                                                corner points are valid .
         - point1 is:  NXOpen.Point3d. First corner point .
         - point2 is:  NXOpen.Point3d. Second corner point .
         - point3 is:  NXOpen.Point3d. Third corner point .
         - point4 is:  NXOpen.Point3d. Fourth corner point .

        """
        pass
    def SaveCurves(self, groupName: str) -> None:
        """
         Creates curves by intersecting the bounded grid with all bodies in 
                    the part of the grid object. The bodies that are visible in the work
                    view are intersected. The curves are added to the group created with 
                    the specified name. The group is displayed in the part navigator. The
                    curves are created in the work part. These curves are not associated
                    with the grid. These are just snapshot curves that can be used for
                    modeling purposes. If the customer default "Load SolidsSheets when
                    Saving Section Curves" is enabled, the Save Copy of Section Curves 
                    command in the datum plane grid dialog will cause solidsheet bodies 
                    to be loaded into memory for any visible lightweight bodies on the 
                    section plane. This may increase the time and memory used by the 
                    operation, but will ensure fully accurate section curves.
                 
        """
        pass
    def SetCornerPoints(self, point1: NXOpen.Point3d, point2: NXOpen.Point3d, point3: NXOpen.Point3d, point4: NXOpen.Point3d) -> bool:
        """
         Sets corner points of the grid 
         Returns validCornerPoints (bool):  Flag indicating whether the
                                                                corner points are valid .
        """
        pass
class BoundedGrid(Grid): 
    """ Represents a bounded grid """
    pass
import NXOpen
class BoxShipGridBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Display.BoxShipGridBuilder builder"""
    def CalculateBoxDataFromGrid(self) -> None:
        """
         Calculates builder information from the existing grid 
        """
        pass
    def CalculateBoxFromActiveView(self, forceCalculation: bool) -> None:
        """
         Calculates the bounding box from the current active view and update the box grid. 
        """
        pass
    def DeleteBoxGrid(self) -> None:
        """
         Delete existing box grid, if any  
        """
        pass
    def RotateBoxGrid(self) -> None:
        """
         Rotates box grid with current position 
        """
        pass
    def UpdateBoxGrid(self, forceUpdate: bool) -> None:
        """
         Updates box grid with current box geometry 
        """
        pass
import NXOpen
class CameraBuilder(NXOpen.Builder): 
    """
Represents a NXOpen.Display.CameraBuilder
"""
    class Aperture(Enum):
        """
        Members Include: 
         |F28|  f2.8 
         |F56|  f5.6 
         |F8|  f8   
         |F11|  f11  
         |F16|  f16  
         |F22|  f22     

        """
        F28: int
        F56: int
        F8: int
        F11: int
        F16: int
        F22: int
        @staticmethod
        def ValueOf(value: int) -> CameraBuilder.Aperture:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class AspectRatio(Enum):
        """
        Members Include: 
         |GraphicsWindow|  Aspect ratio of graphics window 
         |ImageBasedBackground|  Aspect ratio of image-based background in studio view
         |SquareFormat|  Aspect ratio 1:1, square format
         |StandardPhotoPrintFormat|  Aspect ratio 3:2, 6x4 standard photo print format
         |StandardVideoFormat|  Aspect ratio 4:3, standard video format
         |HdtvFormat|  Aspect ratio 16:9, HDTV format
         |UserDefined|  Custom aspect ratio by specifying the width and height

        """
        GraphicsWindow: int
        ImageBasedBackground: int
        SquareFormat: int
        StandardPhotoPrintFormat: int
        StandardVideoFormat: int
        HdtvFormat: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> CameraBuilder.AspectRatio:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FovMeasured(Enum):
        """
        Members Include: 
         |Horizontally|  Horizontal 
         |Vertically|  Vertical  

        """
        Horizontally: int
        Vertically: int
        @staticmethod
        def ValueOf(value: int) -> CameraBuilder.FovMeasured:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LensAngle(Enum):
        """
        Members Include: 
         |Stock|  Stock Lenses 
         |Fov|  Field of View 
         |Magnification|  Magnification 

        """
        Stock: int
        Fov: int
        Magnification: int
        @staticmethod
        def ValueOf(value: int) -> CameraBuilder.LensAngle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LensFlare(Enum):
        """
        Members Include: 
         |Standard|  Standard lens 
         |S35|  35mm 
         |S50|  50mm 
         |S105|  105mm 
         |Polygonal|  polygonal 
         |P35|  35mm poly 
         |P50|  50mm poly 
         |P105|  105mm poly 
         |Spark|  spark lens 
         |Star|  star lens 

        """
        Standard: int
        S35: int
        S50: int
        S105: int
        Polygonal: int
        P35: int
        P50: int
        P105: int
        Spark: int
        Star: int
        @staticmethod
        def ValueOf(value: int) -> CameraBuilder.LensFlare:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StockLens(Enum):
        """
        Members Include: 
         |S28|  28mm 
         |S35|  35mm 
         |S50|  50mm 
         |S70|  70mm 
         |S105|  105mm 
         |S135|  135mm 
         |S210|  210mm 
         |S300|  300mm 

        """
        S28: int
        S35: int
        S50: int
        S70: int
        S105: int
        S135: int
        S210: int
        S300: int
        @staticmethod
        def ValueOf(value: int) -> CameraBuilder.StockLens:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |Parallel|   Parallel Projection 
         |Perspective|  Perspective Projection 

        """
        Parallel: int
        Perspective: int
        @staticmethod
        def ValueOf(value: int) -> CameraBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ApertureType(self) -> CameraBuilder.Aperture:
        """
        Getter for property: ( CameraBuilder.Aperture NXOpen) ApertureType
         Returns the aperture   
            
         
        """
        pass
    @ApertureType.setter
    def ApertureType(self, apertureType: CameraBuilder.Aperture):
        """
        Setter for property: ( CameraBuilder.Aperture NXOpen) ApertureType
         Returns the aperture   
            
         
        """
        pass
    @property
    def AspectRatioHeight(self) -> float:
        """
        Getter for property: (float) AspectRatioHeight
         Returns the aspect ratio height from camera.  
           The aspect ratio height range is 0.01 to 100.   
         
        """
        pass
    @AspectRatioHeight.setter
    def AspectRatioHeight(self, aspectRatioHeight: float):
        """
        Setter for property: (float) AspectRatioHeight
         Returns the aspect ratio height from camera.  
           The aspect ratio height range is 0.01 to 100.   
         
        """
        pass
    @property
    def AspectRatioType(self) -> CameraBuilder.AspectRatio:
        """
        Getter for property: ( CameraBuilder.AspectRatio NXOpen) AspectRatioType
         Returns the aspect ratio type from camera   
            
         
        """
        pass
    @AspectRatioType.setter
    def AspectRatioType(self, aspectRatioType: CameraBuilder.AspectRatio):
        """
        Setter for property: ( CameraBuilder.AspectRatio NXOpen) AspectRatioType
         Returns the aspect ratio type from camera   
            
         
        """
        pass
    @property
    def AspectRatioWidth(self) -> float:
        """
        Getter for property: (float) AspectRatioWidth
         Returns the aspect ratio width from camera.  
           The aspect ratio width range is 0.01 to 100.   
         
        """
        pass
    @AspectRatioWidth.setter
    def AspectRatioWidth(self, aspectRatioWidth: float):
        """
        Setter for property: (float) AspectRatioWidth
         Returns the aspect ratio width from camera.  
           The aspect ratio width range is 0.01 to 100.   
         
        """
        pass
    @property
    def BackClippingDistance(self) -> float:
        """
        Getter for property: (float) BackClippingDistance
         Returns the back clipping distance   
            
         
        """
        pass
    @BackClippingDistance.setter
    def BackClippingDistance(self, backClippingDistance: float):
        """
        Setter for property: (float) BackClippingDistance
         Returns the back clipping distance   
            
         
        """
        pass
    @property
    def CameraMatrix(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: ( NXOpen.Matrix3x3) CameraMatrix
         Returns the camera rotation matrix   
            
         
        """
        pass
    @CameraMatrix.setter
    def CameraMatrix(self, camera_matrix: NXOpen.Matrix3x3):
        """
        Setter for property: ( NXOpen.Matrix3x3) CameraMatrix
         Returns the camera rotation matrix   
            
         
        """
        pass
    @property
    def CameraName(self) -> str:
        """
        Getter for property: (str) CameraName
         Returns the camera name as a TEXT string.  
            Note that internally the camera name
                is stored as a char string.  Any characters which cannot be
                mapped to 8-bit characters will be replaced by # characters.
                Two commits are needed for set when a new camera is created.   
         
        """
        pass
    @CameraName.setter
    def CameraName(self, camera_name: str):
        """
        Setter for property: (str) CameraName
         Returns the camera name as a TEXT string.  
            Note that internally the camera name
                is stored as a char string.  Any characters which cannot be
                mapped to 8-bit characters will be replaced by # characters.
                Two commits are needed for set when a new camera is created.   
         
        """
        pass
    @property
    def CameraNameChar(self) -> str:
        """
        Getter for property: (str) CameraNameChar
         Returns the camera name as a char string.  
           
                Two commits are needed for set when a new camera is created.   
         
        """
        pass
    @CameraNameChar.setter
    def CameraNameChar(self, camera_name: str):
        """
        Setter for property: (str) CameraNameChar
         Returns the camera name as a char string.  
           
                Two commits are needed for set when a new camera is created.   
         
        """
        pass
    @property
    def CameraPosition(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) CameraPosition
         Returns the coordinates of the camera point   
            
         
        """
        pass
    @CameraPosition.setter
    def CameraPosition(self, position: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) CameraPosition
         Returns the coordinates of the camera point   
            
         
        """
        pass
    @property
    def DepthOfFieldToggle(self) -> bool:
        """
        Getter for property: (bool) DepthOfFieldToggle
         Returns the depth of field toggle   
            
         
        """
        pass
    @DepthOfFieldToggle.setter
    def DepthOfFieldToggle(self, depthOfFieldToggle: bool):
        """
        Setter for property: (bool) DepthOfFieldToggle
         Returns the depth of field toggle   
            
         
        """
        pass
    @property
    def FieldOfViewAngle(self) -> float:
        """
        Getter for property: (float) FieldOfViewAngle
         Returns the field of view angle.  
            Note that this property only make sense
                when camera type is JA_DISPLAY_CAMERA_BUILDER_types_perspective.
                Set field of view angle only works when the lens angle type
                is JA_DISPLAY_CAMERA_BUILDER_lens_angle_fov.   
         
        """
        pass
    @FieldOfViewAngle.setter
    def FieldOfViewAngle(self, fieldOfViewAngle: float):
        """
        Setter for property: (float) FieldOfViewAngle
         Returns the field of view angle.  
            Note that this property only make sense
                when camera type is JA_DISPLAY_CAMERA_BUILDER_types_perspective.
                Set field of view angle only works when the lens angle type
                is JA_DISPLAY_CAMERA_BUILDER_lens_angle_fov.   
         
        """
        pass
    @property
    def FieldOfViewMeasured(self) -> CameraBuilder.FovMeasured:
        """
        Getter for property: ( CameraBuilder.FovMeasured NXOpen) FieldOfViewMeasured
         Returns the field of view measured   
            
         
        """
        pass
    @FieldOfViewMeasured.setter
    def FieldOfViewMeasured(self, fovMeasuredType: CameraBuilder.FovMeasured):
        """
        Setter for property: ( CameraBuilder.FovMeasured NXOpen) FieldOfViewMeasured
         Returns the field of view measured   
            
         
        """
        pass
    @property
    def FocalDistance(self) -> float:
        """
        Getter for property: (float) FocalDistance
         Returns the focal distance   
            
         
        """
        pass
    @FocalDistance.setter
    def FocalDistance(self, focalDistance: float):
        """
        Setter for property: (float) FocalDistance
         Returns the focal distance   
            
         
        """
        pass
    @property
    def FrontClippingDistance(self) -> float:
        """
        Getter for property: (float) FrontClippingDistance
         Returns the front clipping distance   
            
         
        """
        pass
    @FrontClippingDistance.setter
    def FrontClippingDistance(self, frontClippingDistance: float):
        """
        Setter for property: (float) FrontClippingDistance
         Returns the front clipping distance   
            
         
        """
        pass
    @property
    def HiddenLensFlareToggle(self) -> bool:
        """
        Getter for property: (bool) HiddenLensFlareToggle
         Returns the hidden lens flare toggle   
            
         
        """
        pass
    @HiddenLensFlareToggle.setter
    def HiddenLensFlareToggle(self, hiddenLensFlareToggle: bool):
        """
        Setter for property: (bool) HiddenLensFlareToggle
         Returns the hidden lens flare toggle   
            
         
        """
        pass
    @property
    def LensAngleType(self) -> CameraBuilder.LensAngle:
        """
        Getter for property: ( CameraBuilder.LensAngle NXOpen) LensAngleType
         Returns the lens angle   
            
         
        """
        pass
    @LensAngleType.setter
    def LensAngleType(self, lensAngleType: CameraBuilder.LensAngle):
        """
        Setter for property: ( CameraBuilder.LensAngle NXOpen) LensAngleType
         Returns the lens angle   
            
         
        """
        pass
    @property
    def LensFlareIntensity(self) -> float:
        """
        Getter for property: (float) LensFlareIntensity
         Returns the lens flare intensity   
            
         
        """
        pass
    @LensFlareIntensity.setter
    def LensFlareIntensity(self, lensFlareIntensity: float):
        """
        Setter for property: (float) LensFlareIntensity
         Returns the lens flare intensity   
            
         
        """
        pass
    @property
    def LensFlareToggle(self) -> bool:
        """
        Getter for property: (bool) LensFlareToggle
         Returns the lens flare toggle   
            
         
        """
        pass
    @LensFlareToggle.setter
    def LensFlareToggle(self, lensFlareToggle: bool):
        """
        Setter for property: (bool) LensFlareToggle
         Returns the lens flare toggle   
            
         
        """
        pass
    @property
    def LensFlareType(self) -> CameraBuilder.LensFlare:
        """
        Getter for property: ( CameraBuilder.LensFlare NXOpen) LensFlareType
         Returns the lens flare type   
            
         
        """
        pass
    @LensFlareType.setter
    def LensFlareType(self, lensFlareType: CameraBuilder.LensFlare):
        """
        Setter for property: ( CameraBuilder.LensFlare NXOpen) LensFlareType
         Returns the lens flare type   
            
         
        """
        pass
    @property
    def Magnification(self) -> float:
        """
        Getter for property: (float) Magnification
         Returns the magnification.  
            Note that set magnification only works when the lens angle type
                is JA_DISPLAY_CAMERA_BUILDER_lens_angle_magnification.   
         
        """
        pass
    @Magnification.setter
    def Magnification(self, magnification: float):
        """
        Setter for property: (float) Magnification
         Returns the magnification.  
            Note that set magnification only works when the lens angle type
                is JA_DISPLAY_CAMERA_BUILDER_lens_angle_magnification.   
         
        """
        pass
    @property
    def PerspectiveDistance(self) -> float:
        """
        Getter for property: (float) PerspectiveDistance
         Returns the perspective distance.  
            Note that the perspective distance should not
                set inside of the front clipping plane.  So please check the front clipping
                distance before set the perspective distance.   
         
        """
        pass
    @PerspectiveDistance.setter
    def PerspectiveDistance(self, perspectiveDistance: float):
        """
        Setter for property: (float) PerspectiveDistance
         Returns the perspective distance.  
            Note that the perspective distance should not
                set inside of the front clipping plane.  So please check the front clipping
                distance before set the perspective distance.   
         
        """
        pass
    @property
    def StockLensType(self) -> CameraBuilder.StockLens:
        """
        Getter for property: ( CameraBuilder.StockLens NXOpen) StockLensType
         Returns the stock lens type   
            
         
        """
        pass
    @StockLensType.setter
    def StockLensType(self, stockLensType: CameraBuilder.StockLens):
        """
        Setter for property: ( CameraBuilder.StockLens NXOpen) StockLensType
         Returns the stock lens type   
            
         
        """
        pass
    @property
    def TargetMatrix(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: ( NXOpen.Matrix3x3) TargetMatrix
         Returns the target point rotation matrix   
            
         
        """
        pass
    @TargetMatrix.setter
    def TargetMatrix(self, matrix: NXOpen.Matrix3x3):
        """
        Setter for property: ( NXOpen.Matrix3x3) TargetMatrix
         Returns the target point rotation matrix   
            
         
        """
        pass
    @property
    def TargetPosition(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) TargetPosition
         Returns the coordinates of the target point   
            
         
        """
        pass
    @TargetPosition.setter
    def TargetPosition(self, position: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) TargetPosition
         Returns the coordinates of the target point   
            
         
        """
        pass
    @property
    def Type(self) -> CameraBuilder.Types:
        """
        Getter for property: ( CameraBuilder.Types NXOpen) Type
         Returns the camera type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: CameraBuilder.Types):
        """
        Setter for property: ( CameraBuilder.Types NXOpen) Type
         Returns the camera type   
            
         
        """
        pass
    @property
    def UseTargetPoint(self) -> bool:
        """
        Getter for property: (bool) UseTargetPoint
         Returns whether to use the target point   
            
         
        """
        pass
    @UseTargetPoint.setter
    def UseTargetPoint(self, useTargetPoint: bool):
        """
        Setter for property: (bool) UseTargetPoint
         Returns whether to use the target point   
            
         
        """
        pass
import NXOpen
class CameraCollection(NXOpen.TaggedObjectCollection): 
    """
Represents a collection cameras
"""
    @overload
    def CreateCameraBuilder(self, camera: Camera) -> CameraBuilder:
        """
         Creates a NXOpen.Display.CameraBuilder object if camera is . 
                Otherwise, a Camera object will be edited. If camera is not  and the camera is
                associated with a view other than the work view, then the camera will be applied to
                the current work view. 
         Returns builder ( CameraBuilder NXOpen):  return camera builder .
        """
        pass
    @overload
    def CreateCameraBuilder(self, camera: Camera, applyCameraToView: bool) -> CameraBuilder:
        """
         Creates a NXOpen.Display.CameraBuilder object if camera is .
                Otherwise, a Camera object will be edited. If camera is not  and the camera is
                associated with a view other than the work view, then the camera will be applied to the
                current work view if and only if applyCameraToView is true. 
             
         Returns builder ( CameraBuilder NXOpen):  return camera builder .
        """
        pass
    @overload
    def CreateCameraBuilder(self, view: NXOpen.View, layout: NXOpen.Layout, camera: Camera) -> CameraBuilder:
        """
         Creates a NXOpen.Display.CameraBuilder object if camera is .
                Otherwise, a Camera object will be edited.  Initializes the camera with data from the view
                in the layout.  If camera is not  and the camera is associated with a view other
                than the work view, then the camera will be applied to the current work view. 
            
         Returns builder ( CameraBuilder NXOpen):  return camera builder .
        """
        pass
    @overload
    def CreateCameraBuilder(self, view: NXOpen.View, layout: NXOpen.Layout, camera: Camera, applyCameraToView: bool) -> CameraBuilder:
        """
         Creates a NXOpen.Display.CameraBuilder object if camera is .
                Otherwise, a Camera object will be edited.  Initializes the camera with data from the view
                in the layout.  If camera is not  and the camera is associated with a view other
                than the work view, then the camera will be applied to the current work view if and only if
                applyCameraToView is truel.
            
         Returns builder ( CameraBuilder NXOpen):  return camera builder .
        """
        pass
    def FindObject(self, journal_identifier: str) -> Camera:
        """
         Finds the  NXOpen.Display.Camera  with the given identifier as recorded in a journal. 
            An object may not return the same value as its JournalIdentifier in different versions of 
            the software. However newer versions of the software should find the same object when 
            FindObject is passed older versions of its journal identifier. In general, this method 
            should not be used in handwritten code and exists to support record and playback of journals.
            An exception will be thrown if no object can be found with the given journal identifier. 
         Returns found ( Camera NXOpen):  Camera found .
        """
        pass
import NXOpen
class Camera(NXOpen.NXObject): 
    """ Represents a camera """
    def ApplyToView(self, view: NXOpen.ModelingView) -> None:
        """
         Applies the parameters of a camera to a view 
        """
        pass
    def CopyToClipboard(self) -> None:
        """
         Copies the parameters of a camera to the operating system clipboard 
        """
        pass
    def ListInformation(self) -> None:
        """
         Writes information about a camera to the listing device 
        """
        pass
import NXOpen
class DatumPlaneGridBuilder(BoundedGridBuilder): 
    """ Represents the builder for adding a datum plane grid NXOpen.Display.DatumPlaneGrid 
        to a datum plane.
    """
    class GridOrientationType(Enum):
        """
        Members Include: 
         |FromDatumPlane|  Grid display matches
                                                                                        datum plane display 
         |Custom|  Grid size, location, and
                                                                               orientation can be customized 
                                                                               using the manipulator controls 

        """
        FromDatumPlane: int
        Custom: int
        @staticmethod
        def ValueOf(value: int) -> DatumPlaneGridBuilder.GridOrientationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def GridOrientation(self) -> DatumPlaneGridBuilder.GridOrientationType:
        """
        Getter for property: ( DatumPlaneGridBuilder.GridOrientationType NXOpen) GridOrientation
         Returns the grid orientation   
            
         
        """
        pass
    @GridOrientation.setter
    def GridOrientation(self, gridOrientation: DatumPlaneGridBuilder.GridOrientationType):
        """
        Setter for property: ( DatumPlaneGridBuilder.GridOrientationType NXOpen) GridOrientation
         Returns the grid orientation   
            
         
        """
        pass
    def GetDatumPlanes(self) -> List[NXOpen.DatumPlane]:
        """
         Get the list of datum planes. 
         Returns datumPlanes ( NXOpen.DatumPlane Li):  datum plane list .
        """
        pass
    def SetDatumPlanes(self, datumPlanes: List[NXOpen.DatumPlane]) -> None:
        """
         Set the list of datum planes.  When editing an existing datum plane grid, 
                    only a single datum plane may be set and it must meet the following conditions:
                    - one that currently does not have a grid associated to it
                    - one that matches NXOpen.Display.DatumPlaneGridBuilder.GetDatumPlanes
                
        """
        pass
class DatumPlaneGrid(BoundedGrid): 
    """ Represents a grid on a datum plane """
    pass
import NXOpen
class DecalBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Display.DecalBuilder 
        This class is restricted to being called from a program running during an 
        Interactive NX session.  If run from a non-interactive session it will 
        return .
    """
    class Anchor(Enum):
        """
        Members Include: 
         |TopLeft|  anchor at top left corner of decal image
         |Center|  anchor in the middle of decal image 
         |BottomLeft|  anchor at the bottom left corner of decal image 
         |TopMiddle|  anchor at top middle corner of decal image
         |TopRight|  anchor at top right corner of decal image
         |LeftMiddle|  anchor at left middle corner of decal image
         |RightMiddle|  anchor at right middle corner of decal image
         |BottomMiddle|  anchor at bottom middle corner of decal image
         |BottomRight|  anchor at bottom right corner of decal image

        """
        TopLeft: int
        Center: int
        BottomLeft: int
        TopMiddle: int
        TopRight: int
        LeftMiddle: int
        RightMiddle: int
        BottomMiddle: int
        BottomRight: int
        @staticmethod
        def ValueOf(value: int) -> DecalBuilder.Anchor:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DecalIllumination(Enum):
        """
        Members Include: 
         |UseUnderlyingMaterial|  base decal reflectivity on underlying material 
         |UseDecalMaterial|  set decal's reflectivity  

        """
        UseUnderlyingMaterial: int
        UseDecalMaterial: int
        @staticmethod
        def ValueOf(value: int) -> DecalBuilder.DecalIllumination:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DecalReflectivities(Enum):
        """
        Members Include: 
         |UseMatte| 
         |UsePlastic| 
         |UseMirror| 
         |UseMetal| 
         |UseGlass| 

        """
        UseMatte: int
        UsePlastic: int
        UseMirror: int
        UseMetal: int
        UseGlass: int
        @staticmethod
        def ValueOf(value: int) -> DecalBuilder.DecalReflectivities:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ImageSize(Enum):
        """
        Members Include: 
         |TrueSize|  use true image size 
         |OneTwentyEight|  resize image to 128 x 128
         |TwoFiftySix|  resize iamge to 256 x 256
         |FiveTwelve|  resize image to 512 x 512
         |OneOTwoFour|  resize image to 1024 x1024
         |TwoOFourEight|  resize image to 2048x2048
         |FourONineSix|  resize image to 4096x 4096

        """
        TrueSize: int
        OneTwentyEight: int
        TwoFiftySix: int
        FiveTwelve: int
        OneOTwoFour: int
        TwoOFourEight: int
        FourONineSix: int
        @staticmethod
        def ValueOf(value: int) -> DecalBuilder.ImageSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Projection(Enum):
        """
        Members Include: 
         |Planar|  planar projection type 
         |Cylindrical|  cylindrical projection type 
         |Spherical|  spherical projection type 
         |Uv|  UV map projection type 

        """
        Planar: int
        Cylindrical: int
        Spherical: int
        Uv: int
        @staticmethod
        def ValueOf(value: int) -> DecalBuilder.Projection:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Scaling(Enum):
        """
        Members Include: 
         |ToFace|  scale the decal based on face size 
         |ToImageSize|  scale the decal based on true decal image size
         |ToUniformScale|  scale the decal based on uniform scale 
         |ToNonUniformScale|  scale the decal based on both width and height scale 

        """
        ToFace: int
        ToImageSize: int
        ToUniformScale: int
        ToNonUniformScale: int
        @staticmethod
        def ValueOf(value: int) -> DecalBuilder.Scaling:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AnchorType(self) -> DecalBuilder.Anchor:
        """
        Getter for property: ( DecalBuilder.Anchor NXOpen) AnchorType
         Returns the anchor type   
            
         
        """
        pass
    @AnchorType.setter
    def AnchorType(self, anchorType: DecalBuilder.Anchor):
        """
        Setter for property: ( DecalBuilder.Anchor NXOpen) AnchorType
         Returns the anchor type   
            
         
        """
        pass
    @property
    def AspectRatio(self) -> float:
        """
        Getter for property: (float) AspectRatio
         Returns the decal image aspect ratio   
            
         
        """
        pass
    @AspectRatio.setter
    def AspectRatio(self, aspectRatio: float):
        """
        Setter for property: (float) AspectRatio
         Returns the decal image aspect ratio   
            
         
        """
        pass
    @property
    def AxialRotation(self) -> float:
        """
        Getter for property: (float) AxialRotation
         Returns the decal axial rotation   
            
         
        """
        pass
    @AxialRotation.setter
    def AxialRotation(self, axialRotation: float):
        """
        Setter for property: (float) AxialRotation
         Returns the decal axial rotation   
            
         
        """
        pass
    @property
    def DecalName(self) -> str:
        """
        Getter for property: (str) DecalName
         Returns the decal name   
            
         
        """
        pass
    @DecalName.setter
    def DecalName(self, decalName: str):
        """
        Setter for property: (str) DecalName
         Returns the decal name   
            
         
        """
        pass
    @property
    def DecalReflectivity(self) -> float:
        """
        Getter for property: (float) DecalReflectivity
         Returns the decal reflectivity   
            
         
        """
        pass
    @DecalReflectivity.setter
    def DecalReflectivity(self, decalReflectivity: float):
        """
        Setter for property: (float) DecalReflectivity
         Returns the decal reflectivity   
            
         
        """
        pass
    @property
    def EnableEngraving(self) -> bool:
        """
        Getter for property: (bool) EnableEngraving
         Returns the engraving enable toggle   
            
         
        """
        pass
    @EnableEngraving.setter
    def EnableEngraving(self, enableEngraving: bool):
        """
        Setter for property: (bool) EnableEngraving
         Returns the engraving enable toggle   
            
         
        """
        pass
    @property
    def EngravingAmplitude(self) -> float:
        """
        Getter for property: (float) EngravingAmplitude
         Returns the decal engraving amplitude   
            
         
        """
        pass
    @EngravingAmplitude.setter
    def EngravingAmplitude(self, engravingAmplitude: float):
        """
        Setter for property: (float) EngravingAmplitude
         Returns the decal engraving amplitude   
            
         
        """
        pass
    @property
    def EngravingSoftness(self) -> float:
        """
        Getter for property: (float) EngravingSoftness
         Returns the engraving softness   
            
         
        """
        pass
    @EngravingSoftness.setter
    def EngravingSoftness(self, engravingSoftness: float):
        """
        Setter for property: (float) EngravingSoftness
         Returns the engraving softness   
            
         
        """
        pass
    @property
    def HeightScale(self) -> float:
        """
        Getter for property: (float) HeightScale
         Returns the decal height scale   
            
         
        """
        pass
    @HeightScale.setter
    def HeightScale(self, height_scale: float):
        """
        Setter for property: (float) HeightScale
         Returns the decal height scale   
            
         
        """
        pass
    @property
    def IlluminationType(self) -> DecalBuilder.DecalIllumination:
        """
        Getter for property: ( DecalBuilder.DecalIllumination NXOpen) IlluminationType
         Returns the illumination type   
            
         
        """
        pass
    @IlluminationType.setter
    def IlluminationType(self, illuminationType: DecalBuilder.DecalIllumination):
        """
        Setter for property: ( DecalBuilder.DecalIllumination NXOpen) IlluminationType
         Returns the illumination type   
            
         
        """
        pass
    @property
    def Image(self) -> Image:
        """
        Getter for property: ( Image NXOpen) Image
         Returns the image builder   
            
         
        """
        pass
    @Image.setter
    def Image(self, image_builder: Image):
        """
        Setter for property: ( Image NXOpen) Image
         Returns the image builder   
            
         
        """
        pass
    @property
    def ImageFilename(self) -> str:
        """
        Getter for property: (str) ImageFilename
         Returns the decal image file name   
            
         
        """
        pass
    @ImageFilename.setter
    def ImageFilename(self, image_file_name: str):
        """
        Setter for property: (str) ImageFilename
         Returns the decal image file name   
            
         
        """
        pass
    @property
    def ImageSizeType(self) -> DecalBuilder.ImageSize:
        """
        Getter for property: ( DecalBuilder.ImageSize NXOpen) ImageSizeType
         Returns the image size type   
            
         
        """
        pass
    @ImageSizeType.setter
    def ImageSizeType(self, imageSizeType: DecalBuilder.ImageSize):
        """
        Setter for property: ( DecalBuilder.ImageSize NXOpen) ImageSizeType
         Returns the image size type   
            
         
        """
        pass
    @property
    def NormalVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) NormalVector
         Returns the decal normal vector   
            
         
        """
        pass
    @NormalVector.setter
    def NormalVector(self, normalVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) NormalVector
         Returns the decal normal vector   
            
         
        """
        pass
    @property
    def NormalVectorValue(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) NormalVectorValue
         Returns the decal normal vector value   
            
         
        """
        pass
    @NormalVectorValue.setter
    def NormalVectorValue(self, normalVectorValue: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) NormalVectorValue
         Returns the decal normal vector value   
            
         
        """
        pass
    @property
    def Object(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Object
         Returns the object(face, body and facetted body) to apply the decal to   
            
         
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
    def OriginPosition(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) OriginPosition
         Returns the origin_pos   
            
         
        """
        pass
    @OriginPosition.setter
    def OriginPosition(self, originPosition: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) OriginPosition
         Returns the origin_pos   
            
         
        """
        pass
    @property
    def OverwriteExistingFile(self) -> bool:
        """
        Getter for property: (bool) OverwriteExistingFile
         Returns the overwrite existing file option - true to overwrite and return no error, false to return error   
            
         
        """
        pass
    @OverwriteExistingFile.setter
    def OverwriteExistingFile(self, overwrite_exiting_file: bool):
        """
        Setter for property: (bool) OverwriteExistingFile
         Returns the overwrite existing file option - true to overwrite and return no error, false to return error   
            
         
        """
        pass
    @property
    def ProjectionType(self) -> DecalBuilder.Projection:
        """
        Getter for property: ( DecalBuilder.Projection NXOpen) ProjectionType
         Returns the projection type   
            
         
        """
        pass
    @ProjectionType.setter
    def ProjectionType(self, projectionType: DecalBuilder.Projection):
        """
        Setter for property: ( DecalBuilder.Projection NXOpen) ProjectionType
         Returns the projection type   
            
         
        """
        pass
    @property
    def ReflectivityType(self) -> DecalBuilder.DecalReflectivities:
        """
        Getter for property: ( DecalBuilder.DecalReflectivities NXOpen) ReflectivityType
         Returns the reflectivity type   
            
         
        """
        pass
    @ReflectivityType.setter
    def ReflectivityType(self, reflectivityType: DecalBuilder.DecalReflectivities):
        """
        Setter for property: ( DecalBuilder.DecalReflectivities NXOpen) ReflectivityType
         Returns the reflectivity type   
            
         
        """
        pass
    @property
    def Rotation(self) -> float:
        """
        Getter for property: (float) Rotation
         Returns the decal rotation   
            
         
        """
        pass
    @Rotation.setter
    def Rotation(self, rotation: float):
        """
        Setter for property: (float) Rotation
         Returns the decal rotation   
            
         
        """
        pass
    @property
    def RotationX(self) -> float:
        """
        Getter for property: (float) RotationX
         Returns the X value of rotation around the origin point   
            
         
        """
        pass
    @RotationX.setter
    def RotationX(self, rotationX: float):
        """
        Setter for property: (float) RotationX
         Returns the X value of rotation around the origin point   
            
         
        """
        pass
    @property
    def RotationY(self) -> float:
        """
        Getter for property: (float) RotationY
         Returns the Y value of rotation around the origin point   
            
         
        """
        pass
    @RotationY.setter
    def RotationY(self, rotationY: float):
        """
        Setter for property: (float) RotationY
         Returns the Y value of rotation around the origin point   
            
         
        """
        pass
    @property
    def RotationZ(self) -> float:
        """
        Getter for property: (float) RotationZ
         Returns the Z value of rotation around the origin point   
            
         
        """
        pass
    @RotationZ.setter
    def RotationZ(self, rotationZ: float):
        """
        Setter for property: (float) RotationZ
         Returns the Z value of rotation around the origin point   
            
         
        """
        pass
    @property
    def Scale(self) -> float:
        """
        Getter for property: (float) Scale
         Returns the decal scale   
            
         
        """
        pass
    @Scale.setter
    def Scale(self, scale: float):
        """
        Setter for property: (float) Scale
         Returns the decal scale   
            
         
        """
        pass
    @property
    def ScalingType(self) -> DecalBuilder.Scaling:
        """
        Getter for property: ( DecalBuilder.Scaling NXOpen) ScalingType
         Returns the scaling type   
            
         
        """
        pass
    @ScalingType.setter
    def ScalingType(self, scalingType: DecalBuilder.Scaling):
        """
        Setter for property: ( DecalBuilder.Scaling NXOpen) ScalingType
         Returns the scaling type   
            
         
        """
        pass
    @property
    def StencilPreview(self) -> bool:
        """
        Getter for property: (bool) StencilPreview
         Returns the stencil preview toggle   
            
         
        """
        pass
    @StencilPreview.setter
    def StencilPreview(self, stencilPreview: bool):
        """
        Setter for property: (bool) StencilPreview
         Returns the stencil preview toggle   
            
         
        """
        pass
    @property
    def TranslationX(self) -> float:
        """
        Getter for property: (float) TranslationX
         Returns the X direction of translation   
            
         
        """
        pass
    @TranslationX.setter
    def TranslationX(self, translationX: float):
        """
        Setter for property: (float) TranslationX
         Returns the X direction of translation   
            
         
        """
        pass
    @property
    def TranslationY(self) -> float:
        """
        Getter for property: (float) TranslationY
         Returns the Y direction of translation   
            
         
        """
        pass
    @TranslationY.setter
    def TranslationY(self, translationY: float):
        """
        Setter for property: (float) TranslationY
         Returns the Y direction of translation   
            
         
        """
        pass
    @property
    def TranslationZ(self) -> float:
        """
        Getter for property: (float) TranslationZ
         Returns the Z direction of translation   
            
         
        """
        pass
    @TranslationZ.setter
    def TranslationZ(self, translationZ: float):
        """
        Setter for property: (float) TranslationZ
         Returns the Z direction of translation   
            
         
        """
        pass
    @property
    def TransparencyTolerance(self) -> int:
        """
        Getter for property: (int) TransparencyTolerance
         Returns the transparency tolerance   
            
         
        """
        pass
    @TransparencyTolerance.setter
    def TransparencyTolerance(self, transparencyTolerance: int):
        """
        Setter for property: (int) TransparencyTolerance
         Returns the transparency tolerance   
            
         
        """
        pass
    @property
    def UpVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) UpVector
         Returns the decal up vector   
            
         
        """
        pass
    @UpVector.setter
    def UpVector(self, upVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) UpVector
         Returns the decal up vector   
            
         
        """
        pass
    @property
    def UpVectorValue(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) UpVectorValue
         Returns the decal up vector value   
            
         
        """
        pass
    @UpVectorValue.setter
    def UpVectorValue(self, upVectorValue: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) UpVectorValue
         Returns the decal up vector value   
            
         
        """
        pass
    @property
    def WidthScale(self) -> float:
        """
        Getter for property: (float) WidthScale
         Returns the decal width scale   
            
         
        """
        pass
    @WidthScale.setter
    def WidthScale(self, width_scale: float):
        """
        Setter for property: (float) WidthScale
         Returns the decal width scale   
            
         
        """
        pass
    def GetImagesInPart(self) -> List[str]:
        """
         Provide a list of names of the NXOpen.Display.ImageData
                objects saved in current part file.
                
         Returns imageSimpleName (List[str]):  Array of NXOpen.Display.ImageData names .
        """
        pass
    def GetTransparencyColor(self) -> List[float]:
        """
         Returns the transparency color 
         Returns transparencyColor (List[float]): .
        """
        pass
    def SetImageFromPart(self, imageName: str) -> None:
        """
         Set a NXOpen.Display.ImageData object currently
                stored in the part as the image used by the builder.
                
        """
        pass
    def SetTransparencyColor(self, transparencyColor: List[float]) -> None:
        """
         Sets the transparency color 
        """
        pass
import NXOpen
class DecalCollection(NXOpen.TaggedObjectCollection): 
    """
Represents a collection decal material texture 
This class is restricted to being called from a program running during an 
Interactive NX session.  If run from a non-interactive session it will 
return .
"""
    def CreateDecalBuilder(self, decal: NXOpen.TaggedObject) -> DecalBuilder:
        """
         Creates a NXOpen.Display.DecalBuilder object if decal is .  Otherwise, a Decal object will be edited 
         Returns builder ( DecalBuilder NXOpen):  return decal builder .
        """
        pass
    def CreateDecalBuilderFull(self, decal: NXOpen.TaggedObject) -> DecalBuilder:
        """
         Creates a NXOpen.Display.DecalBuilder object if decal is .  
            If not, the Decal object will be edited. Its referenced image object NXOpen.Display.Image 
            is also created in Decal object with related image NXOpen APIs available. 
         Returns builder ( DecalBuilder NXOpen):  return decal builder .
        """
        pass
    def CreateDecalStickerBuilder(self, decal: NXOpen.TaggedObject) -> DecalStickerBuilder:
        """
         Creates a NXOpen.Display.DecalStickerBuilder 
         Returns builder ( DecalStickerBuilder NXOpen):   .
        """
        pass
    def FindDecalObject(self, journal_identifier: str) -> NXOpen.Decal:
        """
         Finds the  NXOpen.Decal  with the given identifier as recorded in a journal. 
            An object may not return the same value as its JournalIdentifier in different versions of 
            the software. However newer versions of the software should find the same object when 
            FindObject is passed older versions of its journal identifier. In general, this method 
            should not be used in handwritten code and exists to support record and playback of journals.
            An exception will be thrown if no object can be found with the given journal identifier. 
         Returns found_decal ( NXOpen.Decal):  Decal found .
        """
        pass
import NXOpen
class DecalStickerBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Display.DecalStickerBuilder """
    class AnchorTypes(Enum):
        """
        Members Include: 
         |BottomLeft| 
         |BottomCenter| 
         |BottomRight| 
         |MiddleLeft| 
         |MiddleCenter| 
         |MiddleRight| 
         |TopLeft| 
         |TopCenter| 
         |TopRight| 

        """
        BottomLeft: int
        BottomCenter: int
        BottomRight: int
        MiddleLeft: int
        MiddleCenter: int
        MiddleRight: int
        TopLeft: int
        TopCenter: int
        TopRight: int
        @staticmethod
        def ValueOf(value: int) -> DecalStickerBuilder.AnchorTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PixelSizes(Enum):
        """
        Members Include: 
         |TrueSize| 
         |OneTwentyEight| 
         |TwoFiftySix| 
         |FiveTwleve| 
         |OneZeroTwoFour| 
         |TwoZeroFourEight| 
         |FourZeroNineSix| 

        """
        TrueSize: int
        OneTwentyEight: int
        TwoFiftySix: int
        FiveTwleve: int
        OneZeroTwoFour: int
        TwoZeroFourEight: int
        FourZeroNineSix: int
        @staticmethod
        def ValueOf(value: int) -> DecalStickerBuilder.PixelSizes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ProjectionTypes(Enum):
        """
        Members Include: 
         |Planar| 
         |Cylindrical| 
         |Spherical| 
         |Uv| 

        """
        Planar: int
        Cylindrical: int
        Spherical: int
        Uv: int
        @staticmethod
        def ValueOf(value: int) -> DecalStickerBuilder.ProjectionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ReflectivityTypes(Enum):
        """
        Members Include: 
         |FromVisualMaterial| 
         |Matte| 
         |Plastic| 
         |Mirror| 
         |Metal| 
         |Glass| 

        """
        FromVisualMaterial: int
        Matte: int
        Plastic: int
        Mirror: int
        Metal: int
        Glass: int
        @staticmethod
        def ValueOf(value: int) -> DecalStickerBuilder.ReflectivityTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ScalingMethodTypes(Enum):
        """
        Members Include: 
         |UserDefined| 
         |ImageSize| 

        """
        UserDefined: int
        ImageSize: int
        @staticmethod
        def ValueOf(value: int) -> DecalStickerBuilder.ScalingMethodTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TransparencyTypes(Enum):
        """
        Members Include: 
         |NotSet| 
         |FromImage| 
         |PixelColor| 

        """
        NotSet: int
        FromImage: int
        PixelColor: int
        @staticmethod
        def ValueOf(value: int) -> DecalStickerBuilder.TransparencyTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Color:
        """
         Color definition 
         DecalStickerBuilderColor_Struct NXOpen is an alias for  DecalStickerBuilder.Color NXOpen.
        """
        @property
        def Color1(self) -> float:
            """
            Getter for property Color1
            """
            pass
        @Color1.setter
        def Color1(self, value: float):
            """
            Getter for property Color1Setter for property Color1
            """
            pass
        @property
        def Color2(self) -> float:
            """
            Getter for property Color2
            """
            pass
        @Color2.setter
        def Color2(self, value: float):
            """
            Getter for property Color2Setter for property Color2
            """
            pass
        @property
        def Color3(self) -> float:
            """
            Getter for property Color3
            """
            pass
        @Color3.setter
        def Color3(self, value: float):
            """
            Getter for property Color3Setter for property Color3
            """
            pass
    @property
    def AnchorType(self) -> DecalStickerBuilder.AnchorTypes:
        """
        Getter for property: ( DecalStickerBuilder.AnchorTypes NXOpen) AnchorType
         Returns the anchor   
            
         
        """
        pass
    @AnchorType.setter
    def AnchorType(self, anchor: DecalStickerBuilder.AnchorTypes):
        """
        Setter for property: ( DecalStickerBuilder.AnchorTypes NXOpen) AnchorType
         Returns the anchor   
            
         
        """
        pass
    @property
    def Bump(self) -> bool:
        """
        Getter for property: (bool) Bump
         Returns the flag indicating if bump effect should be applied.  
             
         
        """
        pass
    @Bump.setter
    def Bump(self, bump: bool):
        """
        Setter for property: (bool) Bump
         Returns the flag indicating if bump effect should be applied.  
             
         
        """
        pass
    @property
    def DecalName(self) -> str:
        """
        Getter for property: (str) DecalName
         Returns the decal name   
            
         
        """
        pass
    @DecalName.setter
    def DecalName(self, decalName: str):
        """
        Setter for property: (str) DecalName
         Returns the decal name   
            
         
        """
        pass
    @property
    def FaceOrBody(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) FaceOrBody
         Returns the face or body   
            
         
        """
        pass
    @property
    def FilterDecalImages(self) -> bool:
        """
        Getter for property: (bool) FilterDecalImages
         Returns the flag indicating if decal images should be filtered.  
             
         
        """
        pass
    @FilterDecalImages.setter
    def FilterDecalImages(self, filterDecalImages: bool):
        """
        Setter for property: (bool) FilterDecalImages
         Returns the flag indicating if decal images should be filtered.  
             
         
        """
        pass
    @property
    def FitPreview(self) -> bool:
        """
        Getter for property: (bool) FitPreview
         Returns the flag indicating if image preview should be shown.  
             
         
        """
        pass
    @FitPreview.setter
    def FitPreview(self, fitPreview: bool):
        """
        Setter for property: (bool) FitPreview
         Returns the flag indicating if image preview should be shown.  
             
         
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
    def ImageName(self) -> str:
        """
        Getter for property: (str) ImageName
         Returns the image selector   
            
         
        """
        pass
    @ImageName.setter
    def ImageName(self, decalName: str):
        """
        Setter for property: (str) ImageName
         Returns the image selector   
            
         
        """
        pass
    @property
    def LockAspectRatio(self) -> bool:
        """
        Getter for property: (bool) LockAspectRatio
         Returns the flag indicating if aspect ratio should be locked.  
             
         
        """
        pass
    @LockAspectRatio.setter
    def LockAspectRatio(self, lockAspectRatio: bool):
        """
        Setter for property: (bool) LockAspectRatio
         Returns the flag indicating if aspect ratio should be locked.  
             
         
        """
        pass
    @property
    def MaximumPixelSize(self) -> DecalStickerBuilder.PixelSizes:
        """
        Getter for property: ( DecalStickerBuilder.PixelSizes NXOpen) MaximumPixelSize
         Returns the maximum pixel size   
            
         
        """
        pass
    @MaximumPixelSize.setter
    def MaximumPixelSize(self, maximumPixelSize: DecalStickerBuilder.PixelSizes):
        """
        Setter for property: ( DecalStickerBuilder.PixelSizes NXOpen) MaximumPixelSize
         Returns the maximum pixel size   
            
         
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
    def PixelColorTolerance(self) -> int:
        """
        Getter for property: (int) PixelColorTolerance
         Returns the pixel color tolerance   
            
         
        """
        pass
    @PixelColorTolerance.setter
    def PixelColorTolerance(self, pixelColorTolerance: int):
        """
        Setter for property: (int) PixelColorTolerance
         Returns the pixel color tolerance   
            
         
        """
        pass
    @property
    def ProjectionType(self) -> DecalStickerBuilder.ProjectionTypes:
        """
        Getter for property: ( DecalStickerBuilder.ProjectionTypes NXOpen) ProjectionType
         Returns the projection   
            
         
        """
        pass
    @ProjectionType.setter
    def ProjectionType(self, projection: DecalStickerBuilder.ProjectionTypes):
        """
        Setter for property: ( DecalStickerBuilder.ProjectionTypes NXOpen) ProjectionType
         Returns the projection   
            
         
        """
        pass
    @property
    def ReflectivityType(self) -> DecalStickerBuilder.ReflectivityTypes:
        """
        Getter for property: ( DecalStickerBuilder.ReflectivityTypes NXOpen) ReflectivityType
         Returns the reflectivity type   
            
         
        """
        pass
    @ReflectivityType.setter
    def ReflectivityType(self, reflectivityType: DecalStickerBuilder.ReflectivityTypes):
        """
        Setter for property: ( DecalStickerBuilder.ReflectivityTypes NXOpen) ReflectivityType
         Returns the reflectivity type   
            
         
        """
        pass
    @property
    def RotationAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RotationAngle
         Returns the rotation angle   
            
         
        """
        pass
    @property
    def ScalingMethodType(self) -> DecalStickerBuilder.ScalingMethodTypes:
        """
        Getter for property: ( DecalStickerBuilder.ScalingMethodTypes NXOpen) ScalingMethodType
         Returns the scaling method   
            
         
        """
        pass
    @ScalingMethodType.setter
    def ScalingMethodType(self, scalingMethod: DecalStickerBuilder.ScalingMethodTypes):
        """
        Setter for property: ( DecalStickerBuilder.ScalingMethodTypes NXOpen) ScalingMethodType
         Returns the scaling method   
            
         
        """
        pass
    @property
    def Strength(self) -> float:
        """
        Getter for property: (float) Strength
         Returns the strength   
            
         
        """
        pass
    @Strength.setter
    def Strength(self, strength: float):
        """
        Setter for property: (float) Strength
         Returns the strength   
            
         
        """
        pass
    @property
    def TransparencyType(self) -> DecalStickerBuilder.TransparencyTypes:
        """
        Getter for property: ( DecalStickerBuilder.TransparencyTypes NXOpen) TransparencyType
         Returns the transparency   
            
         
        """
        pass
    @TransparencyType.setter
    def TransparencyType(self, transparency: DecalStickerBuilder.TransparencyTypes):
        """
        Setter for property: ( DecalStickerBuilder.TransparencyTypes NXOpen) TransparencyType
         Returns the transparency   
            
         
        """
        pass
    @property
    def UVTransformationData(self) -> UVTransformationData:
        """
        Getter for property: ( UVTransformationData NXOpen) UVTransformationData
         Returns the transformation data used for editing of pre-NX1980 decal sticker having UV projection type.  
             
         
        """
        pass
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Width
         Returns the width   
            
         
        """
        pass
    def GetManipulatorData(self) -> Tuple[NXOpen.Point3d, NXOpen.Matrix3x3]:
        """
         Returns origin and coordinate system of the manipulator tool used to orient the image. 
         Returns A tuple consisting of (origin, csys). 
         - origin is:  NXOpen.Point3d.
         - csys is:  NXOpen.Matrix3x3.

        """
        pass
    def GetTransparencyPixelColor(self) -> DecalStickerBuilder.Color:
        """
         Returns the transparency pixel color 
         Returns transparencyColor ( DecalStickerBuilder.Color NXOpen): .
        """
        pass
    def ResetImageSize(self) -> None:
        """
         Resets the image size. 
        """
        pass
    def SetManipulatorData(self, origin: NXOpen.Point3d, csys: NXOpen.Matrix3x3) -> None:
        """
         Sets origin and coordinate system of the manipulator tool used to orient the image. 
        """
        pass
    def SetTransparencyPixelColor(self, transparencyColor: DecalStickerBuilder.Color) -> None:
        """
         Sets the transparency pixel color 
        """
        pass
    def UpdateDecalStickerOnImageDimensionChange(self) -> None:
        """
         Updates the decal sticker to reflect change in image rotation angle, width or height. 
        """
        pass
import NXOpen
class DownloadOfflineRenderingBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Display.DownloadOfflineRenderingBuilder.
    Download Offline Rendering lists the batch jobs initiated in Ray Traced Studio
    Save Animation. Download Offline Rendering will show job progress and additional job details.
    .
    """
    class FrameRateType(Enum):
        """
        Members Include: 
         |Fps15|  15 frames per second 
         |Fps24|  24 frames per second 
         |Fps30|  30 frames per second 
         |Fps60|  60 frames per second 
         |Fps120|  120 frames per second 
         |UserDefined|  User Defined frame rate 

        """
        Fps15: int
        Fps24: int
        Fps30: int
        Fps60: int
        Fps120: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> DownloadOfflineRenderingBuilder.FrameRateType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AVICompression(self) -> int:
        """
        Getter for property: (int) AVICompression
         Returnsthe compression type for Microsoft AVIs   
            
         
        """
        pass
    @AVICompression.setter
    def AVICompression(self, aviCompression: int):
        """
        Setter for property: (int) AVICompression
         Returnsthe compression type for Microsoft AVIs   
            
         
        """
        pass
    @property
    def AVIFileName(self) -> str:
        """
        Getter for property: (str) AVIFileName
         Returns the Download Offline Rendering AVI file browser   
            
         
        """
        pass
    @AVIFileName.setter
    def AVIFileName(self, aviFileName: str):
        """
        Setter for property: (str) AVIFileName
         Returns the Download Offline Rendering AVI file browser   
            
         
        """
        pass
    @property
    def CustomFrameRate(self) -> int:
        """
        Getter for property: (int) CustomFrameRate
         Returnsthe user-defined frames per second rate for the animation   
            
         
        """
        pass
    @CustomFrameRate.setter
    def CustomFrameRate(self, frameRate: int):
        """
        Setter for property: (int) CustomFrameRate
         Returnsthe user-defined frames per second rate for the animation   
            
         
        """
        pass
    @property
    def FrameRate(self) -> DownloadOfflineRenderingBuilder.FrameRateType:
        """
        Getter for property: ( DownloadOfflineRenderingBuilder.FrameRateType NXOpen) FrameRate
         Returnsthe frames per second rate for the animation   
            
         
        """
        pass
    @FrameRate.setter
    def FrameRate(self, frameRate: DownloadOfflineRenderingBuilder.FrameRateType):
        """
        Setter for property: ( DownloadOfflineRenderingBuilder.FrameRateType NXOpen) FrameRate
         Returnsthe frames per second rate for the animation   
            
         
        """
        pass
    @property
    def SelectedBatchJob(self) -> str:
        """
        Getter for property: (str) SelectedBatchJob
         Returnsthe batch job details of the specified batch job.  
              
         
        """
        pass
    @SelectedBatchJob.setter
    def SelectedBatchJob(self, jobName: str):
        """
        Setter for property: (str) SelectedBatchJob
         Returnsthe batch job details of the specified batch job.  
              
         
        """
        pass
import NXOpen
class DynamicSectionBuilder(NXOpen.Builder): 
    """ Represents a Dynamic Section Builder used for creating sections. 
      
        
        The dynamic sectioning is performed on a displayable part that is
        displayed in the modeling work view.It is possible to specify the view 
        after creating the builder. However, the specified view must be
        modeling work view. This operation is meant to be performed in an 
        interactive mode with visual feedback.
             
              
        Builder Creation:
        
        
        The dynamic section builder can be used to create new dynamic
        section objects OR to edit an existing section object. 
        
        See Display.DynamicSectionCollection.CreateSectionBuilder 
        
        When a view is specified during the builder creation, the dynamic
        section object will be activated in the view. When the dynamic
        section object is activated in the view, view clipping and
        capping is enabled. However, it is not necessary to specify the
        view.
         

           
        There are three different types of sections that are currently
        being supported.
        
        
        
        
            One Plane Section
            Two Parallel Planes Section
            Box Section
        
        
        
        
        User can switch between these types at any time.
        
        
        
        Assembly and Modeling Operations
        
        
        
        
            Create section curves by intersecting all clipping planes  
                with all bodies in the scene
            Create a datum plane from the active section plane.
            Load components that are near or intersecting with the active
                section plane.
        
        
        
        
        All the APIs accept geometric data such as plane origin, plane normal
        in the absolute coordinate system.
        
        
        
        Saving changes
        
      
        
        Builder.Commit method will activate the section
        object in the modeling view. It returns the dynamic section object tag.
        
        
        
        Section Plane Families:
        
        
        
        An important issue with dynamic sectioning is the ability to easily 
        define a group of related cross-section planes. A group of related 
        cross-section planes will be known as a Plane Family. An 
        important idea in understanding a plane family is the concept of a 
        defining or a Base Plane. The base plane of the plane family 
        is the starting point (i.e. plane) for the plane family. All planes 
        in the family are related by an offset to the base plane. There are 
        two types of plane families: 
        
        
        
        
            Linear 
            Axi-Symmetric
        
        
        
        
        Linear Plane Family
        
        
        
        A linear plane family is defined by an infinite group of parallel 
        planes. All of the planes in a linear family are parallel to its 
        base plane (i.e. along the base plane normal at some linear offset 
        value). This is illustrated below with a base plane and three
        parallel planes to it that are members of the plane family.
        
      
        
        Base Plane
        
        
        |   |   |   | 
        |   |   |   | 
        |   |   |   | == Nomal to all planes.
        |   |   |   | 
        |   |   |   | 
        
      
        
        Axi-Symmetric Plane Family
        
      
        
        An axi-symmetric plane family is defined by rotating the base plane about 
        one of the three primary axes. There are an infinite number of planes in 
        an axi-symmetric plane family similar to a linear plane family. This is 
        illustrated below with a base plane and three planes rotated about the 
        z-axis.
        
        
        
          

                \   |   
                 \  |   
                  \ |    
                   \|____  Base Plane
        
      
        Switching between plane families
        

        
        Methods defining a new linear family
        
          
          
        
            Display.DynamicSectionBuilder.AlternatePlane
            Display.DynamicSectionBuilder.PlaneX
            Display.DynamicSectionBuilder.PlaneY
            Display.DynamicSectionBuilder.PlaneZ
            Display.DynamicSectionBuilder.SetNormal
            Display.DynamicSectionBuilder.SetOffset
            Display.DynamicSectionBuilder.SetOffsetByPoint
            Display.DynamicSectionBuilder.SetOrigin
            Display.DynamicSectionBuilder.SetPlane
        
        
                        
        
        Following methods define a new axi-symmetric family
        
          
        
        
            Display.DynamicSectionBuilder.SetRotationAngle
            Display.DynamicSectionBuilder.SetRotationMatrix       
        
        

        
        Transition between plane families
        

        When a method defining a new linear family is invoked, then if 
        
        
        
            the current plane is in a linear family, it will stay in the family.
            the current plane is in a axi-symmetric family, it becomes the base 
                plane of the linear family.
        
        
        
        The same thing happens when a method defining a new axi-symmetric plane           
        is invoked. 
        
        
        
        Examples:
        
        
        1. Linear Family
        
        
        
        Goal: User wants to create a series of sections along X axis.
        
        
        
        API sequence:
        
        
        
        planeX  - Create a plane with base plane at X = 0 
                      See Display.DynamicSectionBuilder.PlaneX
        SetOffset( 50 ) - Plane at X = 50 
        SetOffset( 100 ) - Plane at X = 100 
        SetOffset( 0 ) - Plane at X = 0 
        
        
        2. Axi-symmetric Family
        
        
        
        Goal: User wants to create a series of sections by planes rotated 
              around X axis of the section plane.
        
        
        
        API sequence:
        
        
        SetRotation( X, 45 ) - The current plane becomes base plane. Then 
                               the plane rotated around X axis by 45 
                               degrees. 
        SetRotation( X, 90 ) - Plane rotated around X axis by 90 degrees. 
        SetRotation( X, 90 ) - Plane rotated around X axis by 0 degrees. 
                               Back to original position.
                
        
     """
    @property
    def BoxExtentDelayUpdate(self) -> bool:
        """
        Getter for property: (bool) BoxExtentDelayUpdate
         Returns the delay box extent update.  
           This determines if the
                    box section extent updates are delayed when selection list is modified
                    (see  Display::DynamicSectionBuilder::BoxExtentObjects ).
                      
                    If true then use  Display::DynamicSectionBuilder::UpdateBoxExtents  
                    to update the box section. If false then update happens immediately.
                      
                      
                    Use  Display::DynamicSectionBuilder::BoxExtentSupported 
                    to determine if extent construction is supported before querying or
                    setting extent attributes.
                      
                   
         
        """
        pass
    @BoxExtentDelayUpdate.setter
    def BoxExtentDelayUpdate(self, delayUpdate: bool):
        """
        Setter for property: (bool) BoxExtentDelayUpdate
         Returns the delay box extent update.  
           This determines if the
                    box section extent updates are delayed when selection list is modified
                    (see  Display::DynamicSectionBuilder::BoxExtentObjects ).
                      
                    If true then use  Display::DynamicSectionBuilder::UpdateBoxExtents  
                    to update the box section. If false then update happens immediately.
                      
                      
                    Use  Display::DynamicSectionBuilder::BoxExtentSupported 
                    to determine if extent construction is supported before querying or
                    setting extent attributes.
                      
                   
         
        """
        pass
    @property
    def BoxExtentMargin(self) -> float:
        """
        Getter for property: (float) BoxExtentMargin
         Returns the margin for box section extents 
                      
                    Use  Display::DynamicSectionBuilder::BoxExtentSupported 
                    to determine if extent construction is supported before querying or
                    setting extent attributes.  
          
                      
                   
         
        """
        pass
    @BoxExtentMargin.setter
    def BoxExtentMargin(self, margin: float):
        """
        Setter for property: (float) BoxExtentMargin
         Returns the margin for box section extents 
                      
                    Use  Display::DynamicSectionBuilder::BoxExtentSupported 
                    to determine if extent construction is supported before querying or
                    setting extent attributes.  
          
                      
                   
         
        """
        pass
    @property
    def BoxExtentObjects(self) -> NXOpen.SelectINXObjectList:
        """
        Getter for property: ( NXOpen.SelectINXObjectList) BoxExtentObjects
         Returns the objects that define the extents for box section.  
           
                   
                    Absence of the object list indicates that the extent construction
                    is not supported.
                   
         
        """
        pass
    @property
    def BoxExtentSupported(self) -> bool:
        """
        Getter for property: (bool) BoxExtentSupported
         Returns the box extent support.  
          
                    This is used to determine if the box extent construction is supported. Any
                    box extent related APIs will not function when the extent construction
                    is not supported.
                  
         
        """
        pass
    @property
    def CapColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) CapColor
         Returns the cap color.  
           Used when cap color type is 
                     Display::DynamicSectionTypes::CapColorOptionAny  
                   
         
        """
        pass
    @CapColor.setter
    def CapColor(self, capColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) CapColor
         Returns the cap color.  
           Used when cap color type is 
                     Display::DynamicSectionTypes::CapColorOptionAny  
                   
         
        """
        pass
    @property
    def CapColorOption(self) -> DynamicSectionTypes.CapColorOption:
        """
        Getter for property: ( DynamicSectionTypes.CapColorOption NXOpen) CapColorOption
         Returns the cap color option   
            
         
        """
        pass
    @CapColorOption.setter
    def CapColorOption(self, capColorOption: DynamicSectionTypes.CapColorOption):
        """
        Setter for property: ( DynamicSectionTypes.CapColorOption NXOpen) CapColorOption
         Returns the cap color option   
            
         
        """
        pass
    @property
    def ClipType(self) -> DynamicSectionTypes.Clip:
        """
        Getter for property: ( DynamicSectionTypes.Clip NXOpen) ClipType
         Returns the clip type   
            
         
        """
        pass
    @ClipType.setter
    def ClipType(self, clipType: DynamicSectionTypes.Clip):
        """
        Setter for property: ( DynamicSectionTypes.Clip NXOpen) ClipType
         Returns the clip type   
            
         
        """
        pass
    @property
    def CsysType(self) -> DynamicSectionTypes.CoordinateSystem:
        """
        Getter for property: ( DynamicSectionTypes.CoordinateSystem NXOpen) CsysType
         Returns the coordinate system used for creating section plane along
                    X, Y or Z principal planes.  
           Specifying the coordinate system has no 
                    effect on the current section geometry.
                      
                    This is used in conjunction with
                     NXOpen::Display::DynamicSectionBuilder::DefaultPlaneAxis 
                    to determine default plane constructed by following methods.
                     NXOpen::Display::DynamicSectionBuilder::SetDefaultPlane 
                     NXOpen::Display::DynamicSectionBuilder::SetDefaults 
                      
                   
         
        """
        pass
    @CsysType.setter
    def CsysType(self, csys: DynamicSectionTypes.CoordinateSystem):
        """
        Setter for property: ( DynamicSectionTypes.CoordinateSystem NXOpen) CsysType
         Returns the coordinate system used for creating section plane along
                    X, Y or Z principal planes.  
           Specifying the coordinate system has no 
                    effect on the current section geometry.
                      
                    This is used in conjunction with
                     NXOpen::Display::DynamicSectionBuilder::DefaultPlaneAxis 
                    to determine default plane constructed by following methods.
                     NXOpen::Display::DynamicSectionBuilder::SetDefaultPlane 
                     NXOpen::Display::DynamicSectionBuilder::SetDefaults 
                      
                   
         
        """
        pass
    @property
    def CurveColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) CurveColor
         Returns the curve color.  
           Used when the curve color option is set to
                     Display::DynamicSectionTypes::CurveColorOptionAny .
                   
         
        """
        pass
    @CurveColor.setter
    def CurveColor(self, curveColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) CurveColor
         Returns the curve color.  
           Used when the curve color option is set to
                     Display::DynamicSectionTypes::CurveColorOptionAny .
                   
         
        """
        pass
    @property
    def CurveColorOption(self) -> DynamicSectionTypes.CurveColorOption:
        """
        Getter for property: ( DynamicSectionTypes.CurveColorOption NXOpen) CurveColorOption
         Returns the curve color option   
            
         
        """
        pass
    @CurveColorOption.setter
    def CurveColorOption(self, curveColorOption: DynamicSectionTypes.CurveColorOption):
        """
        Setter for property: ( DynamicSectionTypes.CurveColorOption NXOpen) CurveColorOption
         Returns the curve color option   
            
         
        """
        pass
    @property
    def CurveFont(self) -> NXOpen.DisplayableObject.ObjectFont:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectFont) CurveFont
         Returns the curve font   
            
         
        """
        pass
    @CurveFont.setter
    def CurveFont(self, curveFont: NXOpen.DisplayableObject.ObjectFont):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectFont) CurveFont
         Returns the curve font   
            
         
        """
        pass
    @property
    def CurveWidth(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectWidth) CurveWidth
         Returns the curve width   
            
         
        """
        pass
    @CurveWidth.setter
    def CurveWidth(self, curveWidth: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectWidth) CurveWidth
         Returns the curve width   
            
         
        """
        pass
    @property
    def DefaultPlaneAxis(self) -> DynamicSectionTypes.Axis:
        """
        Getter for property: ( DynamicSectionTypes.Axis NXOpen) DefaultPlaneAxis
         Returns the axis indicating the default plane normal.  
           
                     Display::DynamicSectionTypes::AxisNone  is 
                    invalid. For example; specify 
                     Display::DynamicSectionTypes::AxisZ  to use 
                    XY plane as the default plane.
                    Specifying the default plane has no effect on the current 
                    section geometry.
                      
                    This is used in conjunction with
                     NXOpen::Display::DynamicSectionBuilder::CsysType 
                    to determine default plane constructed by following methods.
                     NXOpen::Display::DynamicSectionBuilder::SetDefaultPlane 
                     NXOpen::Display::DynamicSectionBuilder::SetDefaults 
                      
                   
         
        """
        pass
    @DefaultPlaneAxis.setter
    def DefaultPlaneAxis(self, planeAxis: DynamicSectionTypes.Axis):
        """
        Setter for property: ( DynamicSectionTypes.Axis NXOpen) DefaultPlaneAxis
         Returns the axis indicating the default plane normal.  
           
                     Display::DynamicSectionTypes::AxisNone  is 
                    invalid. For example; specify 
                     Display::DynamicSectionTypes::AxisZ  to use 
                    XY plane as the default plane.
                    Specifying the default plane has no effect on the current 
                    section geometry.
                      
                    This is used in conjunction with
                     NXOpen::Display::DynamicSectionBuilder::CsysType 
                    to determine default plane constructed by following methods.
                     NXOpen::Display::DynamicSectionBuilder::SetDefaultPlane 
                     NXOpen::Display::DynamicSectionBuilder::SetDefaults 
                      
                   
         
        """
        pass
    @property
    def DeferCurveUpdate(self) -> bool:
        """
        Getter for property: (bool) DeferCurveUpdate
         Returns the defer curve update property.  
           This property can be used to reduce number of
                    curve updates when performing a series of attribute changes on the dynamic
                    section. After the changes are done, undefer the curve update. Undeferring
                    will update the curves, if and only if, curve update is required based on
                    the applied changes.
                   
         
        """
        pass
    @DeferCurveUpdate.setter
    def DeferCurveUpdate(self, deferCurveUpdate: bool):
        """
        Setter for property: (bool) DeferCurveUpdate
         Returns the defer curve update property.  
           This property can be used to reduce number of
                    curve updates when performing a series of attribute changes on the dynamic
                    section. After the changes are done, undefer the curve update. Undeferring
                    will update the curves, if and only if, curve update is required based on
                    the applied changes.
                   
         
        """
        pass
    @property
    def InterferenceColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) InterferenceColor
         Returns the interference color.  
             
         
        """
        pass
    @InterferenceColor.setter
    def InterferenceColor(self, interferenceColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) InterferenceColor
         Returns the interference color.  
             
         
        """
        pass
    @property
    def LayerSettings(self) -> LayerSettingsBuilder:
        """
        Getter for property: ( LayerSettingsBuilder NXOpen) LayerSettings
         Returns the layer settings builder 
                    
            
         
        """
        pass
    @property
    def LockPlanes(self) -> bool:
        """
        Getter for property: (bool) LockPlanes
         Returns the lock planes flag.  
           The planes can be locked in case of Two Parallel
                    Planes and Box Section. When locked the planes will move together.
                   
         
        """
        pass
    @LockPlanes.setter
    def LockPlanes(self, lockPlanes: bool):
        """
        Setter for property: (bool) LockPlanes
         Returns the lock planes flag.  
           The planes can be locked in case of Two Parallel
                    Planes and Box Section. When locked the planes will move together.
                   
         
        """
        pass
    @property
    def NumberInSeries(self) -> int:
        """
        Getter for property: (int) NumberInSeries
         Returns the number of requested section planes in the current section series.  
             
         
        """
        pass
    @NumberInSeries.setter
    def NumberInSeries(self, numberSectionsRequested: int):
        """
        Setter for property: (int) NumberInSeries
         Returns the number of requested section planes in the current section series.  
             
         
        """
        pass
    @property
    def ReverseSeries(self) -> bool:
        """
        Getter for property: (bool) ReverseSeries
         Returns the reverse series flag   
            
         
        """
        pass
    @ReverseSeries.setter
    def ReverseSeries(self, reverseSeries: bool):
        """
        Setter for property: (bool) ReverseSeries
         Returns the reverse series flag   
            
         
        """
        pass
    @property
    def SeriesSpacing(self) -> float:
        """
        Getter for property: (float) SeriesSpacing
         Returns the section plane spacing in the current section series.  
             
         
        """
        pass
    @SeriesSpacing.setter
    def SeriesSpacing(self, sectionSpacing: float):
        """
        Setter for property: (float) SeriesSpacing
         Returns the section plane spacing in the current section series.  
             
         
        """
        pass
    @property
    def ShowCap(self) -> bool:
        """
        Getter for property: (bool) ShowCap
         Returns the cap on off flag   
            
         
        """
        pass
    @ShowCap.setter
    def ShowCap(self, showCap: bool):
        """
        Setter for property: (bool) ShowCap
         Returns the cap on off flag   
            
         
        """
        pass
    @property
    def ShowClip(self) -> bool:
        """
        Getter for property: (bool) ShowClip
         Returns the clip on off flag   
            
         
        """
        pass
    @ShowClip.setter
    def ShowClip(self, showClip: bool):
        """
        Setter for property: (bool) ShowClip
         Returns the clip on off flag   
            
         
        """
        pass
    @property
    def ShowCurves(self) -> bool:
        """
        Getter for property: (bool) ShowCurves
         Returns the curve on off flag.  
          
                
                                 
                    When the dynamic section object is visible in the view, the
                    curves from the section object are shown in that view.            
                      
                    
         
        """
        pass
    @ShowCurves.setter
    def ShowCurves(self, showCurves: bool):
        """
        Setter for property: (bool) ShowCurves
         Returns the curve on off flag.  
          
                
                                 
                    When the dynamic section object is visible in the view, the
                    curves from the section object are shown in that view.            
                      
                    
         
        """
        pass
    @property
    def ShowGrid(self) -> bool:
        """
        Getter for property: (bool) ShowGrid
         Returns the show grid display flag   
            
         
        """
        pass
    @ShowGrid.setter
    def ShowGrid(self, showGrid: bool):
        """
        Setter for property: (bool) ShowGrid
         Returns the show grid display flag   
            
         
        """
        pass
    @property
    def ShowInterference(self) -> bool:
        """
        Getter for property: (bool) ShowInterference
         Returns the interference on off flag.  
             
         
        """
        pass
    @ShowInterference.setter
    def ShowInterference(self, showInterference: bool):
        """
        Setter for property: (bool) ShowInterference
         Returns the interference on off flag.  
             
         
        """
        pass
    @property
    def ShowViewer(self) -> bool:
        """
        Getter for property: (bool) ShowViewer
         Returns the 2D viewer display flag   
            
         
        """
        pass
    @ShowViewer.setter
    def ShowViewer(self, showViewer: bool):
        """
        Setter for property: (bool) ShowViewer
         Returns the 2D viewer display flag   
            
         
        """
        pass
    @property
    def Type(self) -> DynamicSectionTypes.Type:
        """
        Getter for property: ( DynamicSectionTypes.Type NXOpen) Type
         Returns the section type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: DynamicSectionTypes.Type):
        """
        Setter for property: ( DynamicSectionTypes.Type NXOpen) Type
         Returns the section type   
            
         
        """
        pass
    @property
    def View(self) -> NXOpen.ModelingView:
        """
        Getter for property: ( NXOpen.ModelingView) View
         Returns the modeling view in which section object edits are being done.  
          
                      
                    Display.DynamicSectionBuilder.View method is
                    present for legacy reasons. 
                    
                    Use  Display::DynamicSectionBuilder::EditView  instead.
                                  
                   
         
        """
        pass
    @View.setter
    def View(self, view: NXOpen.ModelingView):
        """
        Setter for property: ( NXOpen.ModelingView) View
         Returns the modeling view in which section object edits are being done.  
          
                      
                    Display.DynamicSectionBuilder.View method is
                    present for legacy reasons. 
                    
                    Use  Display::DynamicSectionBuilder::EditView  instead.
                                  
                   
         
        """
        pass
    def AlternatePlane(self) -> None:
        """
         Cycle through planes that are 90 degrees aligned to the current section plane.
                    For example, for a XY plane with normal along positive Z axis, invoking 
                    this method will cycle through the planes in the following order.
                    
                    - YZ plane with normal along X axis
                    - XZ plane with normal along Y axis
                    - XY plane with normal along Z axis
                    
                  
                    The section offset and rotation matrix are updated.                
                 
        """
        pass
    def CreateDatumPlane(self) -> NXOpen.DatumPlane:
        """
         Creates a datum plane from the active section plane. 
         Returns datumPlane ( NXOpen.DatumPlane):  Datum plane .
        """
        pass
    def EditView(self, view: NXOpen.ModelingView) -> None:
        """
          Edits the section object in the modeling view.
                    
                    The view being edited must be the modeling view. This is provided
                    to handle scenarios when the working view is changed when sectioning
                    is in progress. It is the responsibility of user to save pending
                    changes using Builder.Commit method. Otherwise,
                    any existing changes will be lost.
                    
                 
        """
        pass
    def ExportSectionCurves(self, groupName: str, fileName: str) -> Tuple[NXOpen.Part, int]:
        """
         Exports section curves in the group into a part file.
                 
         Returns A tuple consisting of (partTag, numSectionCurves). 
         - partTag is:  NXOpen.Part. Tag of the exported part .
         - numSectionCurves is: int. Number of section curves .

        """
        pass
    def GetActivePlane(self) -> Tuple[DynamicSectionTypes.Axis, DynamicSectionTypes.ActivePlane]:
        """
         Gets the active plane in the section. 
                   See Display.DynamicSectionBuilder.SetActivePlane 
                   for details. 
                 
         Returns A tuple consisting of (planeAxis, activePlane). 
         - planeAxis is:  DynamicSectionTypes.Axis NXOpen. .
         - activePlane is:  DynamicSectionTypes.ActivePlane NXOpen. .

        """
        pass
    def GetAllPlanesGeometry(self) -> Tuple[List[NXOpen.Point3d], List[NXOpen.Matrix3x3]]:
        """
         Gets geometry for all planes of the section.
                    
                    Numnber of planes depends on NXOpen.Display.DynamicSectionBuilder.Type. 
                    Z direction of the plane matrix is the plane normal.
                    
                
         Returns A tuple consisting of (planeOrigins, planeMetrices). 
         - planeOrigins is:  NXOpen.Point3d Li. .
         - planeMetrices is:  NXOpen.Matrix3x3 Li. .

        """
        pass
    def GetAssociativePlane(self) -> NXOpen.Plane:
        """
         The dynamic section associative plane.
                    The defined associative smart plane will be returned; otherwise NULL will be returned.
                    
                    Associative plane can be specified only if the builder supports associativity 
                    (see Display.DynamicSectionBuilder.IsAssociativitySupported).            
                    
                 
         Returns planeTag ( NXOpen.Plane):  Plane .
        """
        pass
    def GetBoundingBox(self) -> Tuple[NXOpen.Point3d, NXOpen.Point3d]:
        """
         Gets bounding box used by the section.
                    
                    The bounding box is used to compute offset limits (see
                    NXOpen.Display.DynamicSectionBuilder.GetOffsetLimits).
                    
                    It is possible that there is no valid bounding box associated with
                    the section. The box is invalid if the X coordinate of min corner 
                    point is larger than the X coordinate of max corner point.
                
         Returns A tuple consisting of (minCornerPt, maxCornerPt). 
         - minCornerPt is:  NXOpen.Point3d. .
         - maxCornerPt is:  NXOpen.Point3d.

        """
        pass
    def GetGridSettings(self) -> PlaneGridBuilder:
        """
         Creates a grid settings builder from the active section plane. 
         Returns gridBuilder ( PlaneGridBuilder NXOpen): .
        """
        pass
    def GetName(self) -> str:
        """
         Gets the section name. Caller is expected to free the memory.
                  
         Returns sectionName (str): .
        """
        pass
    def GetNormal(self) -> NXOpen.Vector3d:
        """
         Gets the normal of the section plane 
         Returns normal ( NXOpen.Vector3d):  Section plane normal .
        """
        pass
    def GetOffset(self) -> float:
        """
         Gets the the plane offset. 
         Returns offset (float): .
        """
        pass
    def GetOffsetLimits(self) -> Tuple[float, float]:
        """
         Gets minimum and maximum offset limits.
                    
                    Offset limits are dependent on the active section plane. They
                    are determined based on the model bounding box and location
                    of the active section plane. 
                    
                    
                    Display.DynamicSectionBuilder.SetOffset
                    can specify offset outside the offset limits. In that case the
                    offset limits are extended to include the specified offset.  
                              
                 
         Returns A tuple consisting of (minimumOffset, maximumOffset). 
         - minimumOffset is: float. Minimum offset .
         - maximumOffset is: float. Minimum offset .

        """
        pass
    def GetOrigin(self) -> NXOpen.Point3d:
        """
         Gets the section origin. 
         Returns origin ( NXOpen.Point3d):  Section origin .
        """
        pass
    def GetPlaneGeometry(self, axisType: DynamicSectionTypes.Axis, planeType: DynamicSectionTypes.ActivePlane) -> Tuple[NXOpen.Point3d, NXOpen.Matrix3x3]:
        """
         Gets geometry of specified plane of the section.
                    
                    Valid values for section axis and active plane depends on 
                    NXOpen.Display.DynamicSectionBuilder.Type. 
                    See NXOpen.Display.DynamicSectionBuilder.SetActivePlane 
                    for more details on how to specify axis and active plane type. Z direction
                    of plane matrix is the plane normal.
                    
                
         Returns A tuple consisting of (origin, matrix). 
         - origin is:  NXOpen.Point3d. Plane origin .
         - matrix is:  NXOpen.Matrix3x3. Plane matrix .

        """
        pass
    def GetPlaneThickness(self) -> float:
        """
         Gets the thickness between active plane pair. This is valid
                    when the section contains more than one clipping plane. When the
                    section planes are locked, setting thickness will not alter the 
                    current thickness.
                 
         Returns planeThickness (float): .
        """
        pass
    def GetRotationAngle(self, rotationAxis: DynamicSectionTypes.Axis) -> float:
        """
         Gets rotation angle for specified axis. 
         Returns angle (float):  Rotation angle in degrees .
        """
        pass
    def GetRotationMatrix(self) -> NXOpen.Matrix3x3:
        """
         Gets the section rotation matrix 
         Returns rotationMatrix ( NXOpen.Matrix3x3):  Rotation matrix .
        """
        pass
    def IsAssociativitySupported(self) -> bool:
        """
         Determines if an associative section plane is supported.
                
         Returns isSupported (bool): .
        """
        pass
    def IsDefaultPlane(self) -> bool:
        """
         Indicates whether the section plane is at the default location.
                    Section plane is at the default location when builder creates
                    a new section using default plane parameters (specified in the
                    customer defaults) andor when the section plane location is reset using
                    NXOpen.Display.DynamicSectionBuilder.SetDefaultPlane
                    or NXOpen.Display.DynamicSectionBuilder.SetDefaults.
                    Modifying section plane thereafter will reset the default plane
                    state.
                 
         Returns isDefaultPlane (bool): .
        """
        pass
    def LoadAllIntersecting(self) -> Tuple[bool, NXOpen.PartLoadStatus]:
        """
         Loads all components that intersect the current section plane. Errors
                    are reported by the part load status. Caller is expected to destroy
                    the memory used by load status object.
                 
         Returns A tuple consisting of (componentsLoaded, loadStatus). 
         - componentsLoaded is: bool. New component loaded flag .
         - loadStatus is:  NXOpen.PartLoadStatus.
                        Errors occurred during loading of parts. .

        """
        pass
    def LoadNearIntersecting(self) -> Tuple[bool, NXOpen.PartLoadStatus]:
        """
         Loads components that intersect the current section plane and are  
                    near the section plane origin. The distance used for which components 
                    are "near" the section plane origin is determined internally. Errors 
                    are reported by the part load status. Caller is expected to destroy 
                    the memory used by load status object.
                 
         Returns A tuple consisting of (componentsLoaded, loadStatus). 
         - componentsLoaded is: bool. New component loaded flag .
         - loadStatus is:  NXOpen.PartLoadStatus.
                        Errors occurred during loading of parts. .

        """
        pass
    def OffsetOriginInPlane(self, xOffset: float, yOffset: float) -> None:
        """
         Offsets section origin within current section plane.
                    
                    The section is moved to new location along in the section plane.
                    The offsets are w.r.t. current origin along the X and Y
                    axis of the section plane respectively.         
                 
        """
        pass
    def PlaneX(self) -> None:
        """
         Creates a plane along X direction.
                    
                    The plane is created with the base plane at the origin with normal 
                    along X axis of the coordinate system 
                    Display.DynamicSectionBuilder.CsysType.
                    
                    
                    The location of the plane depends on the bounding box of all
                    parts displayed in the view. The plane is positioned at the center
                    of the bounding box.
                    
                    
                    Section offset and rotation matrix are updated.
                    
                    
                    Section thickness is recomputed based on the bounding box.
                    
                 
        """
        pass
    def PlaneY(self) -> None:
        """
         Creates a plane along Y direction.
                    
                    The plane is created with the base plane at the origin with normal 
                    along Y axis of the coordinate system 
                    Display.DynamicSectionBuilder.CsysType.
                    
                    
                    The location of the plane depends on the bounding box of all
                    parts displayed in the view. The plane is positioned at the center
                    of the bounding box.
                    
                    
                    Section offset and rotation matrix are updated.
                    
                      
                    Section thickness is recomputed based on the bounding box. 
                        
                 
        """
        pass
    def PlaneZ(self) -> None:
        """
         Creates a plane along Z direction. 
                    
                    The plane is created with the base plane at the origin with normal  
                    along Z axis of the coordinate system 
                    Display.DynamicSectionBuilder.CsysType.
                    
                    
                    The location of the plane depends on the bounding box of all
                    parts displayed in the view. The plane is positioned at the center
                    of the bounding box.
                    
                    
                    Section offset and rotation matrix are updated.
                    
                       
                    Section thickness is recomputed based on the bounding box.     
                             
                 
        """
        pass
    def RestoreView(self) -> None:
        """
         Restores the section to the saved section in the view database. 
        """
        pass
    def ReverseDirection(self) -> None:
        """
         Reverses the plane direction. This will flip the side of the model
                    being clipped.
                    
                    Section rotation matrix is updated.      
                    
                 
        """
        pass
    def SaveCurves(self, group_name: str) -> None:
        """
         Creates curves by intersecting all clipping planes of the section with 
                    all visible bodies in the scene and adds them to the group created with the 
                    specified name. The group is displayed in the part navigator. If the 
                    customer default "Load SolidsSheets when Saving Section Curves" is 
                    enabled, then this will load exact solidsheet bodies for the visible 
                    lightweight bodies intersecting the clipping planes. This may increase 
                    the time and memory used by the operation, but will ensure exact 
                    section curves.
                 
        """
        pass
    def SetActivePlane(self, planeAxis: DynamicSectionTypes.Axis, activePlane: DynamicSectionTypes.ActivePlane) -> None:
        """
         Sets the active plane in the section 
                   
                    
                    Single Plane:
                    
                    
                        Display.DynamicSectionTypes.Axis.Z is the
                        active axis. There is no secondary plane. Only primary plane exists.
                    
                    
                    
                    Two Parallel Plane Section:
                    
                    
                        Display.DynamicSectionTypes.Axis.Z is the 
                        active axis and primarysecondary plane can be activated.
                    
                    
                    Box Section:
                    
                    
                        The active plane pair can be selected by specifying the planeAxis
                        Given an axis, the primarysecondary planes can be activated.
                    
                    
                        E.g. To activate primary plane along the local X axis use
                             Display.DynamicSectionTypes.Axis.X and 
                             Display.DynamicSectionTypes.ActivePlane.Primary.
                                           
                 
        """
        pass
    def SetAllPlanesGeometry(self, planeOrigins: List[NXOpen.Point3d], planeMetrices: List[NXOpen.Matrix3x3]) -> bool:
        """
         Sets geometry for all planes of the section.
                    
                    Numnber of planes specified must be consistent with the current 
                    NXOpen.Display.DynamicSectionBuilder.Type.
                    
                
         Returns geometryChanged (bool):  Indicates if section geometry changed. .
        """
        pass
    def SetAssociativePlane(self, planeTag: NXOpen.Plane) -> None:
        """
         Makes dynamic section associative to the specified plane
                    The plane must be a smart plane; otherwise an error will be reported.
                    
                    Associative plane can be specified only if the builder supports associativity 
                    (see Display.DynamicSectionBuilder.IsAssociativitySupported).            
                    
                 
        """
        pass
    def SetBoundingBox(self, minCornerPt: NXOpen.Point3d, maxCornerPt: NXOpen.Point3d) -> None:
        """
         Sets bounding box for the section.
                    
                    The bounding box is used to compute offset limits (see
                    NXOpen.Display.DynamicSectionBuilder.GetOffsetLimits).
                    Specifying bounding box has no effect on current section geometry.
                    
                    
                    The bounding box impacts construction of default section geometry.            
                    NXOpen.Display.DynamicSectionBuilder.SetDefaultPlane
                    NXOpen.Display.DynamicSectionBuilder.SetDefaults
                    
                
        """
        pass
    def SetDefaultPlane(self) -> None:
        """
         Set current section plane to its default definition. This will 
                    only modify section plane geometry.
                    
                    Following properties affect the default section plane geometry.
                    NXOpen.Display.DynamicSectionBuilder.DefaultPlaneAxis
                    NXOpen.Display.DynamicSectionBuilder.CsysType
                    
                 
        """
        pass
    def SetDefaults(self) -> None:
        """
         Set current section to the default values. This will modify
                    all section geometry as well as section attributes.
                    
                    Following properties affect the default section plane geometry.
                    NXOpen.Display.DynamicSectionBuilder.DefaultPlaneAxis
                    NXOpen.Display.DynamicSectionBuilder.CsysType
                    
                 
        """
        pass
    def SetName(self, sectionName: str) -> bool:
        """
         Sets the section name. 
                    
                    The specified name will be validated. A section is expected to have a
                    unique name in a part. The name may be modified to make it unique within
                    the part.
                    
                 
         Returns modified (bool):  If specified name was modified to 
                                                     ensure uniqueness .
        """
        pass
    def SetNormal(self, normal: NXOpen.Vector3d) -> None:
        """
         Sets the normal of the section plane 
                    
                    Section offset and rotation matrix are updated.
                    
                 
        """
        pass
    def SetOffset(self, offset: float) -> None:
        """
         Sets the the plane offset. When there are more than one
                    clipping planes in the section, the active clipping plane will be 
                    not be allowed to cross-over the non-active clipping plane.
                    
                    If Display.DynamicSectionBuilder.LockPlanes
                    is off, section thickness is updated.
                    
                 
        """
        pass
    def SetOffsetByPoint(self, point: NXOpen.Point3d) -> None:
        """
         This method offsets the active clipping plane such that the plane 
                    passes through the specified point. When there are more than one
                    clipping planes in the section, the active clipping plane will be 
                    not be allowed to cross-over the non-active clipping plane.
                    
                    See Display.DynamicSectionBuilder.SetOffset
                    
                 
        """
        pass
    def SetOrigin(self, origin: NXOpen.Point3d) -> None:
        """
         Sets the section origin. 
                    
                    The section is moved to new location. It obeys the lock flag
                    Display.DynamicSectionBuilder.LockPlanes.
                    if it is a multiple plane section.
                    
                    Section offset is updated.
                 
        """
        pass
    def SetPlane(self, axisOrigin: NXOpen.Point3d, origin: NXOpen.Point3d, rotationMatrix: NXOpen.Matrix3x3) -> None:
        """
         Sets a section plane to be the specified plane 
                    The plane is created at the specified origin with the
                    specified rotation matrix. The axis origin can be same as
                    the plane origin. To defind a linear plane family from the
                    absolute origin, define axis origin as {0, 0, 0}. The section
                    offset will reflect the distance of the plane from the
                    axis origin.
                    
                    Section offset and rotation matrix are updated.
                    
                 
        """
        pass
    def SetPlaneThickness(self, planeThickness: float) -> None:
        """
         Sets the thickness between active plane pair. This property is only available
                    when the section contains more than one clipping plane. When the
                    section planes are locked, setting thickness will not alter the 
                    current thickness.
                 
        """
        pass
    def SetRotationAngle(self, rotationAxis: DynamicSectionTypes.Axis, angle: float) -> None:
        """
         Rotates the section about specified axis by the specified angle.
                    If a rotation already exists about the specified axis, then 
                    the section is rotated such that the total rotation angle is 
                    set to the specified angle. Rotation about only one axis is 
                    active at a time.
                    
                    1. Create plane with normal along Z.
                    2. Display.DynamicSectionBuilder.SetRotationAngle( X, 30 )
                       Rotates plane around X axis by 30 degrees
                    3. Display.DynamicSectionBuilder.SetRotationAngle( X, 45 )
                       Incremental rotation of 45 - 30 = 15 degrees.
                    
                     
                    Section offset and rotation matrix are updated.
                    
                 
        """
        pass
    def SetRotationMatrix(self, rotationAxis: DynamicSectionTypes.Axis, rotationMatrix: NXOpen.Matrix3x3) -> None:
        """
         Sets the section rotation matrix
                    
                    Specify Display.DynamicSectionTypes.Axis.None 
                    if the axis about which rotation was performed is not known.
                    
                    
                    Section offset and rotation matrix are updated.
                    
                 
        """
        pass
    def ShowCurvePreview(self, showCurvePreview: bool) -> None:
        """
         Showhide curve preview.      
                               
                    When editing a view section, curve preview can be shown
                    while the editing is in progress. The preview is removed once 
                    the changes are committed on the builder or when the builder 
                    is destroyed.      
                    
                    
                    Hiding preview will remove the section series preview too.
                    
                  
        """
        pass
    def ShowSectionCurves(self, showCurves: bool) -> None:
        """
         Shows the section curves in the view associated with the builder.
                    If no view is associated with the builder, then the curves are 
                    Shown in the current work view.
                 
        """
        pass
    def UpdateBoxExtents(self) -> None:
        """
         Update box section display by recomputing the box extents if necessary. 
                    
                    Use Display.DynamicSectionBuilder.BoxExtentSupported
                    to determine if extent construction is supported before querying or
                    setting extent attributes.
                    
                
        """
        pass
import NXOpen
class DynamicSectionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of dynamic section objects """
    def CopySections(self, sections: List[DynamicSection], deleteOriginals: bool) -> List[DynamicSection]:
        """
         Copies the specified dynamic sections in the part. A copy of each
                    specified dynamic section will be created and then added to the part. 
                    It is  ensured that each dynamic section object in the part has a 
                    unique name. Hence, it is possible that the name of a pasted section  
                    object is different from that of the input section object if its name 
                    clashes with an existing section object in the part.
                    
                    The section objects being copied must have been loaded in the memory.
                    Otherwise this method will throw an exception.
                    
                
         Returns copiedSections ( DynamicSection List[NXOp):  Copied section objects in the part. .
        """
        pass
    @overload
    def CreateSectionBuilder(self, section: DynamicSection, view: NXOpen.ModelingView) -> DynamicSectionBuilder:
        """
         Creates a NXOpen.Display.DynamicSectionBuilder object if the section 
                    is . Otherwise, a Section object will be edited.
                    
                    The specified view can be , in which case the section object is not 
                    activated in any view.
                    
                 
         Returns builder ( DynamicSectionBuilder NXOpen):  .
        """
        pass
    @overload
    def CreateSectionBuilder(self, view: NXOpen.ModelingView) -> DynamicSectionBuilder:
        """
         Creates a NXOpen.Display.DynamicSectionBuilder object that is used
                    to edit a section object in the specified view. If no section object is available
                    for the view, then a new one is created.
                    
                    The specified view can not be , otherwise an exception will be raised.
                    
                 
         Returns builder ( DynamicSectionBuilder NXOpen):   .
        """
        pass
    def DeleteSections(self, addUndoMark: bool, sections: List[DynamicSection]) -> None:
        """
         Deletes the specified dynamic sections in the part. All views in
                    which the dynamic sections were active are updated to reflect the
                    change. An update will be performed to remove deleted objects.
                
        """
        pass
    def FindObject(self, journalIdentifier: str) -> DynamicSection:
        """
         Finds the  NXOpen.Display.DynamicSection  with the given identifier as 
                    recorded in a journal. An object may not return the same value as its JournalIdentifier
                    in different versions of the software. However newer versions of the software should find 
                    the same object when FindObject is passed older versions of its journal identifier. In general,
                    this method should not be used in handwritten code and exists to support record and 
                    playback of journals.
                    
                    An exception will be thrown if no object can be found with the given journal identifier. 
                    
                
         Returns section ( DynamicSection NXOpen):  Section found .
        """
        pass
    def MoveToDefaultLayer(self, dynamicSections: List[DynamicSection]) -> None:
        """
         Moves the specified dynamic sections in the part to default layer. 
                    The default settings are obtained from the view sectioning 
                    customer defaults. 
        """
        pass
import NXOpen
class DynamicSectionCut(NXOpen.NXObject): 
    """ Represents a dynamic section-cut generated by sectioning an object
        such as a NXOpen.IBody or a 
        NXOpen.Assemblies.Component. 
    """
    @property
    def CutObject(self) -> NXOpen.INXObject:
        """
        Getter for property: ( NXOpen.INXObject) CutObject
         Returns the object from which this section-cut is generated.  
          
                    E.g.; a body, a body occurrence, a component.
                   
         
        """
        pass
    @overload
    def PrepareForMeasure(self, contextOccurrence: NXOpen.NXObject, view: NXOpen.View) -> None:
        """
         Prepares the section-cut for measurement. This may create
                    curves necessary to do measurement operation. The curves
                    are created from the currently loaded representation of the
                    NXOpen.Display.DynamicSectionCut.CutObject. 
                    For example, if a solid is loaded lightweight, then the curves
                    are created from lightweight representation. The curves are
                    displayed as part of preparation for measurement. The curves
                    may be detroyed at the end of measure operation (see
                    NXOpen.Session.DeleteTransientDynamicSectionCutData.
                 
        """
        pass
    @overload
    def PrepareForMeasure(self, exactMeasure: bool, contextOccurrence: NXOpen.NXObject, view: NXOpen.View) -> None:
        """
         Prepares the section-cut for measurement. This may create
                    curves necessary to do measurement operation. If exact
                    measurement is requested, then exact representation of 
                    NXOpen.Display.DynamicSectionCut.CutObject 
                    is loaded on-demand. Otherwise, the measurement is performed
                    based on the currently loaded representation of the
                    NXOpen.Display.DynamicSectionCut.CutObject.
                    For example, if a solid body is loaded lightweight, then
                    lightweight representation will be used for measurement if
                    exact measurement is not requested. If The curves are
                    displayed as part of preparation for measurement. The curves
                    may be detroyed at the end of measure operation (see
                    NXOpen.Session.DeleteTransientDynamicSectionCutData.
                 
        """
        pass
import NXOpen
class DynamicSectionTypes(NXOpen.Object): 
    """ Represents a enumerations used by Dynamic Section Builder. """
    class ActivePlane(Enum):
        """
        Members Include: 
         |Primary|  Primary 
         |Secondary|  Secondary 

        """
        Primary: int
        Secondary: int
        @staticmethod
        def ValueOf(value: int) -> DynamicSectionTypes.ActivePlane:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Axis(Enum):
        """
        Members Include: 
         |NotSet|  Arbitrary axis 
         |X|  X axis 
         |Y|  Y axis 
         |Z|  Z axis 

        """
        NotSet: int
        X: int
        Y: int
        Z: int
        @staticmethod
        def ValueOf(value: int) -> DynamicSectionTypes.Axis:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CapColorOption(Enum):
        """
        Members Include: 
         |Body|  Use body color 
         |Any|  User-specified color is used 

        """
        Body: int
        Any: int
        @staticmethod
        def ValueOf(value: int) -> DynamicSectionTypes.CapColorOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Clip(Enum):
        """
        Members Include: 
         |Section|  One sided clip 
         |Slice|  Slice type clip 

        """
        Section: int
        Slice: int
        @staticmethod
        def ValueOf(value: int) -> DynamicSectionTypes.Clip:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CoordinateSystem(Enum):
        """
        Members Include: 
         |Absolute|  Absolute 
         |Wcs|  WCS 

        """
        Absolute: int
        Wcs: int
        @staticmethod
        def ValueOf(value: int) -> DynamicSectionTypes.CoordinateSystem:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CurveColorOption(Enum):
        """
        Members Include: 
         |Body|  Use body color 
         |Any|  Use specified color 

        """
        Body: int
        Any: int
        @staticmethod
        def ValueOf(value: int) -> DynamicSectionTypes.CurveColorOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Type(Enum):
        """
        Members Include: 
         |OnePlane|  One plane section 
         |TwoParallelPlanes|  Two parallel plane section 
         |Box|  Box section 

        """
        OnePlane: int
        TwoParallelPlanes: int
        Box: int
        @staticmethod
        def ValueOf(value: int) -> DynamicSectionTypes.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
import NXOpen
class DynamicSection(NXOpen.NXObject): 
    """ Represents a dynamic section """
    def UpdateSectionCuts(self, updateOption: NXOpen.Update.Option) -> None:
        """
         Updates the section-cuts (curves) associated with the dynamic 
                    section object if they are out-of-date.
                    
                    
                    If the section object is out-of-date, then it is first logged for 
                    update. If update option is NXOpen.Update.Option.Now, 
                    then the update is performed immediately. If the user wants to update 
                    multiple section objects, then it is optimal to specify the update option 
                    as NXOpen.Update.Option.Later and perform 
                    update at the end using NXOpen.Update.DoUpdate.
                    
                    
                    
                    An valid undo mark NXOpen.Session.UndoMarkId must have been 
                    set so that the session can be rolled back successfully if an error occurs.
                    See NXOpen.Session.SetUndoMark.
                    
                
        """
        pass
import NXOpen
class EntitySelectionPlane(NXOpen.DisplayableObject): 
    """ Represents a grid on a datum plane """
    pass
import NXOpen
class EnvironmentBuilder(NXOpen.Builder): 
    """
    Represents a Display.EnvironmentBuilder
    This controls environment image, tone mapping, and stages.
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return .
    """
    class GlobalFinishType(Enum):
        """
        Members Include: 
         |ShinyPlastic|  Shiny Plastic global finish effect 
         |ClassicSatin|  Classic Satin global finish effect 
         |MattePlastic|  Matte Plastic global finish effect 
         |Flat|  Flat global finish effect 
         |UserDefined|  Original global finish effect 

        """
        ShinyPlastic: int
        ClassicSatin: int
        MattePlastic: int
        Flat: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> EnvironmentBuilder.GlobalFinishType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class GroundPlaneTypes(Enum):
        """
        Members Include: 
         |Yz|  Use yz plane for the ground. 
         |Xz|  Use xz plane for the ground. 
         |Xy|  Use xy plane for the ground. 
         |UserDefined|  Use user defined plane for the ground. 

        """
        Yz: int
        Xz: int
        Xy: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> EnvironmentBuilder.GroundPlaneTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class HdrTypes(Enum):
        """
        Members Include: 
         |NotSet|  No image based lighting 
         |Lighting1|  
         |Lighting2|  
         |Lighting3|  

        """
        NotSet: int
        Lighting1: int
        Lighting2: int
        Lighting3: int
        @staticmethod
        def ValueOf(value: int) -> EnvironmentBuilder.HdrTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ImageBlurType(Enum):
        """
        Members Include: 
         |NotSet| 
         |Low| 
         |Medium| 
         |High| 

        """
        NotSet: int
        Low: int
        Medium: int
        High: int
        @staticmethod
        def ValueOf(value: int) -> EnvironmentBuilder.ImageBlurType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ImageUpVectorTypes(Enum):
        """
        Members Include: 
         |AlignWithFloorPlane| 
         |UserDefined| 

        """
        AlignWithFloorPlane: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> EnvironmentBuilder.ImageUpVectorTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ToneMappingTypes(Enum):
        """
        Members Include: 
         |SystemScene| 
         |UserDefined| 

        """
        SystemScene: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> EnvironmentBuilder.ToneMappingTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ColorSaturation(self) -> float:
        """
        Getter for property: (float) ColorSaturation
         Returns the image-based lighting color saturation   
            
         
        """
        pass
    @ColorSaturation.setter
    def ColorSaturation(self, color_saturation: float):
        """
        Setter for property: (float) ColorSaturation
         Returns the image-based lighting color saturation   
            
         
        """
        pass
    @property
    def DisplayStyle(self) -> NXOpen.View.DisplayStyleType:
        """
        Getter for property: ( NXOpen.View.DisplayStyleType) DisplayStyle
         Returns the display style whose environment is being modified.  
           Shaded and Studio styles have independent environment settings.  
         
        """
        pass
    @property
    def EnvironmentShadedViewsFixGroundPlaneOffset(self) -> bool:
        """
        Getter for property: (bool) EnvironmentShadedViewsFixGroundPlaneOffset
         Returns the ground plane offset in shaded mode   
            
         
        """
        pass
    @EnvironmentShadedViewsFixGroundPlaneOffset.setter
    def EnvironmentShadedViewsFixGroundPlaneOffset(self, fix_plane_offset: bool):
        """
        Setter for property: (bool) EnvironmentShadedViewsFixGroundPlaneOffset
         Returns the ground plane offset in shaded mode   
            
         
        """
        pass
    @property
    def EnvironmentShadedViewsGlobalFinish(self) -> int:
        """
        Getter for property: (int) EnvironmentShadedViewsGlobalFinish
         Returns the global finish in shaded mode   
            
         
        """
        pass
    @EnvironmentShadedViewsGlobalFinish.setter
    def EnvironmentShadedViewsGlobalFinish(self, global_finish: int):
        """
        Setter for property: (int) EnvironmentShadedViewsGlobalFinish
         Returns the global finish in shaded mode   
            
         
        """
        pass
    @property
    def EnvironmentShadedViewsGroundPlane(self) -> int:
        """
        Getter for property: (int) EnvironmentShadedViewsGroundPlane
         Returns the ground plane in shaded mode   
            
         
        """
        pass
    @EnvironmentShadedViewsGroundPlane.setter
    def EnvironmentShadedViewsGroundPlane(self, ground_plane: int):
        """
        Setter for property: (int) EnvironmentShadedViewsGroundPlane
         Returns the ground plane in shaded mode   
            
         
        """
        pass
    @property
    def EnvironmentShadedViewsGroundPlaneCustom(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) EnvironmentShadedViewsGroundPlaneCustom
         Returns the user defined ground plane in shaded mode  
            
         
        """
        pass
    @EnvironmentShadedViewsGroundPlaneCustom.setter
    def EnvironmentShadedViewsGroundPlaneCustom(self, groundPlaneCustom: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) EnvironmentShadedViewsGroundPlaneCustom
         Returns the user defined ground plane in shaded mode  
            
         
        """
        pass
    @property
    def EnvironmentShadedViewsGroundPlaneOffset(self) -> float:
        """
        Getter for property: (float) EnvironmentShadedViewsGroundPlaneOffset
         Returns the ground plane offset in shaded mode   
            
         
        """
        pass
    @EnvironmentShadedViewsGroundPlaneOffset.setter
    def EnvironmentShadedViewsGroundPlaneOffset(self, plane_offset: float):
        """
        Setter for property: (float) EnvironmentShadedViewsGroundPlaneOffset
         Returns the ground plane offset in shaded mode   
            
         
        """
        pass
    @property
    def EnvironmentShadedViewsGroundRefReflectivity(self) -> float:
        """
        Getter for property: (float) EnvironmentShadedViewsGroundRefReflectivity
         Returns the ground floor reflectivity in shaded mode   
            
         
        """
        pass
    @EnvironmentShadedViewsGroundRefReflectivity.setter
    def EnvironmentShadedViewsGroundRefReflectivity(self, floor_reflectivity: float):
        """
        Setter for property: (float) EnvironmentShadedViewsGroundRefReflectivity
         Returns the ground floor reflectivity in shaded mode   
            
         
        """
        pass
    @property
    def EnvironmentShadedViewsShowGroundReflection(self) -> bool:
        """
        Getter for property: (bool) EnvironmentShadedViewsShowGroundReflection
         Returns the ground reflection for shaded mode   
            
         
        """
        pass
    @EnvironmentShadedViewsShowGroundReflection.setter
    def EnvironmentShadedViewsShowGroundReflection(self, enableShadedViewsGroundRefl: bool):
        """
        Setter for property: (bool) EnvironmentShadedViewsShowGroundReflection
         Returns the ground reflection for shaded mode   
            
         
        """
        pass
    @property
    def GroundGlossiness(self) -> float:
        """
        Getter for property: (float) GroundGlossiness
         Returns the ground glossiness   
            
         
        """
        pass
    @GroundGlossiness.setter
    def GroundGlossiness(self, groundGlossiness: float):
        """
        Setter for property: (float) GroundGlossiness
         Returns the ground glossiness   
            
         
        """
        pass
    @property
    def GroundPlaneType(self) -> EnvironmentBuilder.GroundPlaneTypes:
        """
        Getter for property: ( EnvironmentBuilder.GroundPlaneTypes NXOpen) GroundPlaneType
         Returns the ground orientation define   
            
         
        """
        pass
    @GroundPlaneType.setter
    def GroundPlaneType(self, planeType: EnvironmentBuilder.GroundPlaneTypes):
        """
        Setter for property: ( EnvironmentBuilder.GroundPlaneTypes NXOpen) GroundPlaneType
         Returns the ground orientation define   
            
         
        """
        pass
    @property
    def GroundReflection(self) -> bool:
        """
        Getter for property: (bool) GroundReflection
         Returns whether to enable ground reflection   
            
         
        """
        pass
    @GroundReflection.setter
    def GroundReflection(self, groundReflection: bool):
        """
        Setter for property: (bool) GroundReflection
         Returns whether to enable ground reflection   
            
         
        """
        pass
    @property
    def GroundVisibility(self) -> bool:
        """
        Getter for property: (bool) GroundVisibility
         Returns whether to enable ground visibility or not   
            
         
        """
        pass
    @GroundVisibility.setter
    def GroundVisibility(self, groundVisibility: bool):
        """
        Setter for property: (bool) GroundVisibility
         Returns whether to enable ground visibility or not   
            
         
        """
        pass
    @property
    def Hdr(self) -> EnvironmentBuilder.HdrTypes:
        """
        Getter for property: ( EnvironmentBuilder.HdrTypes NXOpen) Hdr
         Returns the pre-defined HDR used for Shaded display style only.  
            
         
        """
        pass
    @Hdr.setter
    def Hdr(self, hdrType: EnvironmentBuilder.HdrTypes):
        """
        Setter for property: ( EnvironmentBuilder.HdrTypes NXOpen) Hdr
         Returns the pre-defined HDR used for Shaded display style only.  
            
         
        """
        pass
    @property
    def Image(self) -> Image:
        """
        Getter for property: ( Image NXOpen) Image
         Returns the image-based lighting's image builder   
            
         
        """
        pass
    @Image.setter
    def Image(self, image_builder: Image):
        """
        Setter for property: ( Image NXOpen) Image
         Returns the image-based lighting's image builder   
            
         
        """
        pass
    @property
    def ImageBlur(self) -> EnvironmentBuilder.ImageBlurType:
        """
        Getter for property: ( EnvironmentBuilder.ImageBlurType NXOpen) ImageBlur
         Returns the blurr of the lighting image   
            
         
        """
        pass
    @ImageBlur.setter
    def ImageBlur(self, image_blurr: EnvironmentBuilder.ImageBlurType):
        """
        Setter for property: ( EnvironmentBuilder.ImageBlurType NXOpen) ImageBlur
         Returns the blurr of the lighting image   
            
         
        """
        pass
    @property
    def ImageFilename(self) -> str:
        """
        Getter for property: (str) ImageFilename
         Returns the image filename used for image-based lighting   
            
         
        """
        pass
    @ImageFilename.setter
    def ImageFilename(self, image_file_name: str):
        """
        Setter for property: (str) ImageFilename
         Returns the image filename used for image-based lighting   
            
         
        """
        pass
    @property
    def ImageRotation(self) -> float:
        """
        Getter for property: (float) ImageRotation
         Returns the image rotation angle (in degrees)   
            
         
        """
        pass
    @ImageRotation.setter
    def ImageRotation(self, imageRotation: float):
        """
        Setter for property: (float) ImageRotation
         Returns the image rotation angle (in degrees)   
            
         
        """
        pass
    @property
    def ImageUpVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ImageUpVector
         Returns the image up vector direction, relative to the absolute coordinate system   
            
         
        """
        pass
    @ImageUpVector.setter
    def ImageUpVector(self, imageUpVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ImageUpVector
         Returns the image up vector direction, relative to the absolute coordinate system   
            
         
        """
        pass
    @property
    def ImageUpVectorCoordinate(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) ImageUpVectorCoordinate
         Returns the image up vector coordinate, relative to the absolute coordinate system   
            
         
        """
        pass
    @ImageUpVectorCoordinate.setter
    def ImageUpVectorCoordinate(self, imageUpVector: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) ImageUpVectorCoordinate
         Returns the image up vector coordinate, relative to the absolute coordinate system   
            
         
        """
        pass
    @property
    def ImageUpVectorType(self) -> EnvironmentBuilder.ImageUpVectorTypes:
        """
        Getter for property: ( EnvironmentBuilder.ImageUpVectorTypes NXOpen) ImageUpVectorType
         Returns the image up vector define   
            
         
        """
        pass
    @ImageUpVectorType.setter
    def ImageUpVectorType(self, imageUpVector: EnvironmentBuilder.ImageUpVectorTypes):
        """
        Setter for property: ( EnvironmentBuilder.ImageUpVectorTypes NXOpen) ImageUpVectorType
         Returns the image up vector define   
            
         
        """
        pass
    @property
    def LightIntensity(self) -> float:
        """
        Getter for property: (float) LightIntensity
         Returns the intensity of the light effects   
            
         
        """
        pass
    @LightIntensity.setter
    def LightIntensity(self, lightIntensity: float):
        """
        Setter for property: (float) LightIntensity
         Returns the intensity of the light effects   
            
         
        """
        pass
    @property
    def LwrtAngle(self) -> float:
        """
        Getter for property: (float) LwrtAngle
         Returns the angle of the lwrt image-based lighting light effects   
            
         
        """
        pass
    @LwrtAngle.setter
    def LwrtAngle(self, lwrt_angle: float):
        """
        Setter for property: (float) LwrtAngle
         Returns the angle of the lwrt image-based lighting light effects   
            
         
        """
        pass
    @property
    def LwrtIntensity(self) -> float:
        """
        Getter for property: (float) LwrtIntensity
         Returns the intensity of the lwrt image-based lighting light effects   
            
         
        """
        pass
    @LwrtIntensity.setter
    def LwrtIntensity(self, lwrt_intensity: float):
        """
        Setter for property: (float) LwrtIntensity
         Returns the intensity of the lwrt image-based lighting light effects   
            
         
        """
        pass
    @property
    def LwrtQuality(self) -> float:
        """
        Getter for property: (float) LwrtQuality
         Returns the quality of the lwrt image-based lighting light effects 1 to 7   
            
         
        """
        pass
    @LwrtQuality.setter
    def LwrtQuality(self, lwrt_quality: float):
        """
        Setter for property: (float) LwrtQuality
         Returns the quality of the lwrt image-based lighting light effects 1 to 7   
            
         
        """
        pass
    @property
    def OffsetExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OffsetExpression
         Returns the environment offset expression  
            
         
        """
        pass
    @property
    def Reflectivity(self) -> float:
        """
        Getter for property: (float) Reflectivity
         Returns the ground reflectivity   
            
         
        """
        pass
    @Reflectivity.setter
    def Reflectivity(self, reflectivity: float):
        """
        Setter for property: (float) Reflectivity
         Returns the ground reflectivity   
            
         
        """
        pass
    @property
    def SizeExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SizeExpression
         Returns the environment size expression  
            
         
        """
        pass
    @property
    def SpecifyGroundPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) SpecifyGroundPlane
         Returns the specify ground plane   
            
         
        """
        pass
    @SpecifyGroundPlane.setter
    def SpecifyGroundPlane(self, specifyPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) SpecifyGroundPlane
         Returns the specify ground plane   
            
         
        """
        pass
    @property
    def UseEnvironment(self) -> bool:
        """
        Getter for property: (bool) UseEnvironment
         Returns whether image-based lighting (IBL) is enabled   
            
         
        """
        pass
    @UseEnvironment.setter
    def UseEnvironment(self, useIBL: bool):
        """
        Setter for property: (bool) UseEnvironment
         Returns whether image-based lighting (IBL) is enabled   
            
         
        """
        pass
    @property
    def UseLightsForShadowCatcherInLwrt(self) -> bool:
        """
        Getter for property: (bool) UseLightsForShadowCatcherInLwrt
         Returns whether Advanced Studio display (lwrt) uses individual light sources or image-based lighting for shadow catcher   
            
         
        """
        pass
    @UseLightsForShadowCatcherInLwrt.setter
    def UseLightsForShadowCatcherInLwrt(self, useLightsForShadowCatcherInLwrt: bool):
        """
        Setter for property: (bool) UseLightsForShadowCatcherInLwrt
         Returns whether Advanced Studio display (lwrt) uses individual light sources or image-based lighting for shadow catcher   
            
         
        """
        pass
    @property
    def UseLwrtEnvironment(self) -> bool:
        """
        Getter for property: (bool) UseLwrtEnvironment
         Returns whether image-based lighting is enabled in Advanced Studio (lwrt) display   
            
         
        """
        pass
    @UseLwrtEnvironment.setter
    def UseLwrtEnvironment(self, useLwrtIBL: bool):
        """
        Setter for property: (bool) UseLwrtEnvironment
         Returns whether image-based lighting is enabled in Advanced Studio (lwrt) display   
            
         
        """
        pass
    @property
    def ViewFitToStage(self) -> bool:
        """
        Getter for property: (bool) ViewFitToStage
         Returns whether to fit view to stage   
            
         
        """
        pass
    @ViewFitToStage.setter
    def ViewFitToStage(self, viewFitToStage: bool):
        """
        Setter for property: (bool) ViewFitToStage
         Returns whether to fit view to stage   
            
         
        """
        pass
    def AlignFloorPlane(self, specifyFloorPlane: NXOpen.Plane) -> None:
        """
         The environment's floor aligns with the given plane. 
        """
        pass
    def CommitAndDisplay(self, view: NXOpen.View, update_ibl_display: bool, update_env_cube_display: bool) -> None:
        """
         Saves the attributes and optionally updates the display of image-based lighting 
        """
        pass
    def CommitOffset(self, view: NXOpen.View) -> None:
        """
         Updates the data and display for a change to the ground's offset 
        """
        pass
    def FloorXaxis(self) -> None:
        """
         The environment's floor to align with the WCS x-axis 
        """
        pass
    def FloorYaxis(self) -> None:
        """
         The environment's floor to align with the WCS y-axis 
        """
        pass
    def FloorZaxis(self) -> None:
        """
         The environment's floor to align with the WCS z-axis 
        """
        pass
    def GetGroundReflectionColor(self) -> List[float]:
        """
         Returns the ground reflection color 
         Returns groundReflectionColor (List[float]): .
        """
        pass
    def SetGroundReflectionColor(self, groundReflectionColor: List[float]) -> None:
        """
         Sets the ground reflection color 
        """
        pass
import NXOpen
class ExtractScene(NXOpen.Builder): 
    """ Represents a NXOpen.Display.ExtractScene
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return .
    """
    @property
    def SceneName(self) -> str:
        """
        Getter for property: (str) SceneName
         Returns the scene name   
            
         
        """
        pass
    @SceneName.setter
    def SceneName(self, sceneName: str):
        """
        Setter for property: (str) SceneName
         Returns the scene name   
            
         
        """
        pass
    def GetSceneDescription(self) -> List[str]:
        """
         Returns the scene description 
         Returns sceneDescription (List[str]): .
        """
        pass
    def ImageFileSelect(self) -> None:
        """
         Gets an image file using file selection. 
        """
        pass
    def Information(self) -> None:
        """
         The scene information 
        """
        pass
    def SetSceneDescription(self, sceneDescription: List[str]) -> None:
        """
         Sets the scene description 
        """
        pass
import NXOpen
class FacetSettingsBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Display.FacetSettingsBuilder
    """
    class AdvVisToleranceSetting(Enum):
        """
        Members Include: 
         |Coarse| 
         |Standard| 
         |Fine| 
         |ExtraFine| 
         |SuperFine| 
         |UltraFine| 
         |UserDefined| 

        """
        Coarse: int
        Standard: int
        Fine: int
        ExtraFine: int
        SuperFine: int
        UltraFine: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> FacetSettingsBuilder.AdvVisToleranceSetting:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FacetScale(Enum):
        """
        Members Include: 
         |Fixed|  Adjusts tolerances by a constant value 
         |Part|  Adjusts tolerances by scale derived from bounding box of objects to facet in part 
         |View|  Adjusts tolerances by view scale 

        """
        Fixed: int
        Part: int
        View: int
        @staticmethod
        def ValueOf(value: int) -> FacetSettingsBuilder.FacetScale:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FacetToViewRatio(Enum):
        """
        Members Include: 
         |Automatic| 
         |UserDefined| 

        """
        Automatic: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> FacetSettingsBuilder.FacetToViewRatio:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FacetUpdate(Enum):
        """
        Members Include: 
         |VisibleObjects| 
         |AllObjects| 
         |NotSet| 

        """
        VisibleObjects: int
        AllObjects: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> FacetSettingsBuilder.FacetUpdate:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ShadedToleranceSetting(Enum):
        """
        Members Include: 
         |Coarse| 
         |Standard| 
         |Fine| 
         |ExtraFine| 
         |UltraFine| 
         |UserDefined| 

        """
        Coarse: int
        Standard: int
        Fine: int
        ExtraFine: int
        UltraFine: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> FacetSettingsBuilder.ShadedToleranceSetting:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AdvVisAlignFacets(self) -> bool:
        """
        Getter for property: (bool) AdvVisAlignFacets
         Returns the state of whether facets for advanced visualization views should be aligned along
                    common edges.  
            Using this option will generally increase the quality of the facets
                    but the facet generation will generally take longer.    
         
        """
        pass
    @AdvVisAlignFacets.setter
    def AdvVisAlignFacets(self, advVisAlignFacets: bool):
        """
        Setter for property: (bool) AdvVisAlignFacets
         Returns the state of whether facets for advanced visualization views should be aligned along
                    common edges.  
            Using this option will generally increase the quality of the facets
                    but the facet generation will generally take longer.    
         
        """
        pass
    @property
    def AdvVisFacetRatio(self) -> float:
        """
        Getter for property: (float) AdvVisFacetRatio
         Returns the facet ratio to use for Advanced Visualization Views   
            
         
        """
        pass
    @AdvVisFacetRatio.setter
    def AdvVisFacetRatio(self, advVisFacetRatio: float):
        """
        Setter for property: (float) AdvVisFacetRatio
         Returns the facet ratio to use for Advanced Visualization Views   
            
         
        """
        pass
    @property
    def AdvVisFacetScale(self) -> FacetSettingsBuilder.FacetScale:
        """
        Getter for property: ( FacetSettingsBuilder.FacetScale NXOpen) AdvVisFacetScale
         Returns the facet scale to use for Advanced Visualization Views   
            
         
        """
        pass
    @AdvVisFacetScale.setter
    def AdvVisFacetScale(self, advVisFacetScale: FacetSettingsBuilder.FacetScale):
        """
        Setter for property: ( FacetSettingsBuilder.FacetScale NXOpen) AdvVisFacetScale
         Returns the facet scale to use for Advanced Visualization Views   
            
         
        """
        pass
    @property
    def AdvVisFacetToViewRatio(self) -> FacetSettingsBuilder.FacetToViewRatio:
        """
        Getter for property: ( FacetSettingsBuilder.FacetToViewRatio NXOpen) AdvVisFacetToViewRatio
         Returns the facet to view ratio to use for Advanced Visualization Views   
            
         
        """
        pass
    @AdvVisFacetToViewRatio.setter
    def AdvVisFacetToViewRatio(self, advVisFacetToViewRatio: FacetSettingsBuilder.FacetToViewRatio):
        """
        Setter for property: ( FacetSettingsBuilder.FacetToViewRatio NXOpen) AdvVisFacetToViewRatio
         Returns the facet to view ratio to use for Advanced Visualization Views   
            
         
        """
        pass
    @property
    def AdvVisRefinementFactor(self) -> float:
        """
        Getter for property: (float) AdvVisRefinementFactor
         Returns the refinement factor to use for Advanced Visualization Views   
            
         
        """
        pass
    @AdvVisRefinementFactor.setter
    def AdvVisRefinementFactor(self, advVisRefinementFactor: float):
        """
        Setter for property: (float) AdvVisRefinementFactor
         Returns the refinement factor to use for Advanced Visualization Views   
            
         
        """
        pass
    @property
    def AdvVisTolerance(self) -> FacetSettingsBuilder.AdvVisToleranceSetting:
        """
        Getter for property: ( FacetSettingsBuilder.AdvVisToleranceSetting NXOpen) AdvVisTolerance
         Returns the tolerance setting to use for Advanced Visualization Views   
            
         
        """
        pass
    @AdvVisTolerance.setter
    def AdvVisTolerance(self, advVisTolerance: FacetSettingsBuilder.AdvVisToleranceSetting):
        """
        Setter for property: ( FacetSettingsBuilder.AdvVisToleranceSetting NXOpen) AdvVisTolerance
         Returns the tolerance setting to use for Advanced Visualization Views   
            
         
        """
        pass
    @property
    def AdvVisUpdate(self) -> FacetSettingsBuilder.FacetUpdate:
        """
        Getter for property: ( FacetSettingsBuilder.FacetUpdate NXOpen) AdvVisUpdate
         Returns the update mode to use for Advanced Visualization Views   
            
         
        """
        pass
    @AdvVisUpdate.setter
    def AdvVisUpdate(self, advVisUpdate: FacetSettingsBuilder.FacetUpdate):
        """
        Setter for property: ( FacetSettingsBuilder.FacetUpdate NXOpen) AdvVisUpdate
         Returns the update mode to use for Advanced Visualization Views   
            
         
        """
        pass
    @property
    def FullLoadToSaveDisplayFacets(self) -> bool:
        """
        Getter for property: (bool) FullLoadToSaveDisplayFacets
         Returns the state of whether component parts should be fully loaded in order to 
                    mark them as modified during regeneration of display facets.  
          
                    See  NXOpen::Display::FacetSettingsBuilder::RegenerateDisplayFacets  
                   
         
        """
        pass
    @FullLoadToSaveDisplayFacets.setter
    def FullLoadToSaveDisplayFacets(self, fullLoadToSaveDisplayFacets: bool):
        """
        Setter for property: (bool) FullLoadToSaveDisplayFacets
         Returns the state of whether component parts should be fully loaded in order to 
                    mark them as modified during regeneration of display facets.  
          
                    See  NXOpen::Display::FacetSettingsBuilder::RegenerateDisplayFacets  
                   
         
        """
        pass
    @property
    def ShadedAlignFacets(self) -> bool:
        """
        Getter for property: (bool) ShadedAlignFacets
         Returns the state of whether facets for shaded views should be aligned along
                    common edges.  
            Using this option will generally increase the quality of the facets
                    but the facet generation will generally take longer.    
         
        """
        pass
    @ShadedAlignFacets.setter
    def ShadedAlignFacets(self, shadedAlignFacets: bool):
        """
        Setter for property: (bool) ShadedAlignFacets
         Returns the state of whether facets for shaded views should be aligned along
                    common edges.  
            Using this option will generally increase the quality of the facets
                    but the facet generation will generally take longer.    
         
        """
        pass
    @property
    def ShadedFacetRatio(self) -> float:
        """
        Getter for property: (float) ShadedFacetRatio
         Returns the facet ratio to use for Shaded Views   
            
         
        """
        pass
    @ShadedFacetRatio.setter
    def ShadedFacetRatio(self, shadedFacetRatio: float):
        """
        Setter for property: (float) ShadedFacetRatio
         Returns the facet ratio to use for Shaded Views   
            
         
        """
        pass
    @property
    def ShadedFacetScale(self) -> FacetSettingsBuilder.FacetScale:
        """
        Getter for property: ( FacetSettingsBuilder.FacetScale NXOpen) ShadedFacetScale
         Returns the facet scale to use for Shaded Views   
            
         
        """
        pass
    @ShadedFacetScale.setter
    def ShadedFacetScale(self, shadedFacetScale: FacetSettingsBuilder.FacetScale):
        """
        Setter for property: ( FacetSettingsBuilder.FacetScale NXOpen) ShadedFacetScale
         Returns the facet scale to use for Shaded Views   
            
         
        """
        pass
    @property
    def ShadedFacetToViewRatio(self) -> FacetSettingsBuilder.FacetToViewRatio:
        """
        Getter for property: ( FacetSettingsBuilder.FacetToViewRatio NXOpen) ShadedFacetToViewRatio
         Returns the facet to view ratio to use for Shaded Views   
            
         
        """
        pass
    @ShadedFacetToViewRatio.setter
    def ShadedFacetToViewRatio(self, shadedFacetToViewRatio: FacetSettingsBuilder.FacetToViewRatio):
        """
        Setter for property: ( FacetSettingsBuilder.FacetToViewRatio NXOpen) ShadedFacetToViewRatio
         Returns the facet to view ratio to use for Shaded Views   
            
         
        """
        pass
    @property
    def ShadedRefinementFactor(self) -> float:
        """
        Getter for property: (float) ShadedRefinementFactor
         Returns the refinement factor to use for Shaded Views   
            
         
        """
        pass
    @ShadedRefinementFactor.setter
    def ShadedRefinementFactor(self, shadedRefinementFactor: float):
        """
        Setter for property: (float) ShadedRefinementFactor
         Returns the refinement factor to use for Shaded Views   
            
         
        """
        pass
    @property
    def ShadedTolerance(self) -> FacetSettingsBuilder.ShadedToleranceSetting:
        """
        Getter for property: ( FacetSettingsBuilder.ShadedToleranceSetting NXOpen) ShadedTolerance
         Returns the tolerance setting to use for Shaded Views   
            
         
        """
        pass
    @ShadedTolerance.setter
    def ShadedTolerance(self, shadedTolerance: FacetSettingsBuilder.ShadedToleranceSetting):
        """
        Setter for property: ( FacetSettingsBuilder.ShadedToleranceSetting NXOpen) ShadedTolerance
         Returns the tolerance setting to use for Shaded Views   
            
         
        """
        pass
    @property
    def ShadedUpdate(self) -> FacetSettingsBuilder.FacetUpdate:
        """
        Getter for property: ( FacetSettingsBuilder.FacetUpdate NXOpen) ShadedUpdate
         Returns the update mode to use for Shaded Views   
            
         
        """
        pass
    @ShadedUpdate.setter
    def ShadedUpdate(self, shadedUpdate: FacetSettingsBuilder.FacetUpdate):
        """
        Setter for property: ( FacetSettingsBuilder.FacetUpdate NXOpen) ShadedUpdate
         Returns the update mode to use for Shaded Views   
            
         
        """
        pass
    @property
    def ShowFacetEdges(self) -> bool:
        """
        Getter for property: (bool) ShowFacetEdges
         Returns the state of whether facet edges should be shown for shaded solid and sheet bodies   
            
         
        """
        pass
    @ShowFacetEdges.setter
    def ShowFacetEdges(self, showFacetEdges: bool):
        """
        Setter for property: (bool) ShowFacetEdges
         Returns the state of whether facet edges should be shown for shaded solid and sheet bodies   
            
         
        """
        pass
    def GetAdvVisAngleTol(self, advVisTolerance: FacetSettingsBuilder.AdvVisToleranceSetting) -> float:
        """
         Returns the angle tolerance for a given tolerance set for Advanced Visualization Views 
         Returns advVisAngleTol (float): .
        """
        pass
    def GetAdvVisEdgeTol(self, advVisTolerance: FacetSettingsBuilder.AdvVisToleranceSetting) -> float:
        """
         Returns the edge tolerance for a given tolerance set for Advanced Visualization Views 
         Returns advVisEdgeTol (float): .
        """
        pass
    def GetAdvVisFaceTol(self, advVisTolerance: FacetSettingsBuilder.AdvVisToleranceSetting) -> float:
        """
         Returns the face tolerance for a given tolerance set for Advanced Visualization Views 
         Returns advVisFaceTol (float): .
        """
        pass
    def GetAdvVisWidthTol(self, advVisTolerance: FacetSettingsBuilder.AdvVisToleranceSetting) -> float:
        """
         Returns the width tolerance for a given tolerance set for Advanced Visualization Views 
         Returns advVisWidthTol (float): .
        """
        pass
    def GetShadedAngleTol(self, shadedTolerance: FacetSettingsBuilder.ShadedToleranceSetting) -> float:
        """
         Returns the angle tolerance for a given tolerance set for Shaded Views 
         Returns shadedAngleTol (float): .
        """
        pass
    def GetShadedEdgeTol(self, shadedTolerance: FacetSettingsBuilder.ShadedToleranceSetting) -> float:
        """
         Returns the edge tolerance for a given tolerance set for Shaded Views 
         Returns shadedEdgeTol (float): .
        """
        pass
    def GetShadedFaceTol(self, shadedTolerance: FacetSettingsBuilder.ShadedToleranceSetting) -> float:
        """
         Returns the face tolerance for a given tolerance set for Shaded Views 
         Returns shadedFaceTol (float): .
        """
        pass
    def RegenerateDisplayFacets(self, deleteSavedDisplayFacets: bool, regenerateChildren: bool, partScope: NXOpen.BasePart) -> None:
        """
         Regenerates display specific cached facets in the specified part.
                    
                    Display facets that are currently saved in the part can be deleted
                    along with the transient display facets. Deleting saved display 
                    facets will mark the part as modified. Builder changes will be 
                    committed before regenerating display facets.  Display facets are
                    generated only for components in Assemblies.Component.RepresentationMode.Exact or 
                    Assemblies.Component.RepresentationMode.Partial mode (see
                    NXOpen.Assemblies.Component.GetComponentRepresentationMode).
                    
                    
                    NXOpen.Display.FacetSettingsBuilder.FullLoadToSaveDisplayFacets 
                    controls whether component parts for which display facets are generated can be
                    loaded fully in order to mark them as modified.
                    
                 
        """
        pass
    def SetAdvVisAngleTol(self, advVisTolerance: FacetSettingsBuilder.AdvVisToleranceSetting, advVisAngleTol: float) -> None:
        """
         Sets the angle tolerance for a given tolerance set for Advanced Visualization Views 
        """
        pass
    def SetAdvVisEdgeTol(self, advVisTolerance: FacetSettingsBuilder.AdvVisToleranceSetting, advVisEdgeTol: float) -> None:
        """
         Sets the edge tolerance for a given tolerance set for Advanced Visualization Views 
        """
        pass
    def SetAdvVisFaceTol(self, advVisTolerance: FacetSettingsBuilder.AdvVisToleranceSetting, advVisFaceTol: float) -> None:
        """
         Sets the face tolerance for a given tolerance set for Advanced Visualization Views 
        """
        pass
    def SetAdvVisWidthTol(self, advVisTolerance: FacetSettingsBuilder.AdvVisToleranceSetting, advVisWidthTol: float) -> None:
        """
         Sets the width tolerance for a given tolerance set for Advanced Visualization Views 
        """
        pass
    def SetShadedAngleTol(self, shadedTolerance: FacetSettingsBuilder.ShadedToleranceSetting, shadedAngleTol: float) -> None:
        """
         Sets the angle tolerance for a given tolerance set for Shaded Views 
        """
        pass
    def SetShadedEdgeTol(self, shadedTolerance: FacetSettingsBuilder.ShadedToleranceSetting, shadedEdgeTol: float) -> None:
        """
         Sets the edge toleramce for a given tolerance set for Shaded Views 
        """
        pass
    def SetShadedFaceTol(self, shadedTolerance: FacetSettingsBuilder.ShadedToleranceSetting, shadedFaceTol: float) -> None:
        """
         Sets the face tolerance for a given tolerance set for Shaded Views 
        """
        pass
import NXOpen
class GlobalIlluminationBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Display.GlobalIlluminationBuilder.
    Global Illumination provides simulation of real-world lighting using 
    image-based lighting.  Image-Based Lighting replaces the Lights in a 
    view with lighting effects derived from a given image.  Global
    Illumination Final Gather settings affect the Ray Traced Studio 
    photo-realistic display of the work view.
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return .
    """
    @property
    def IntensityDouble(self) -> float:
        """
        Getter for property: (float) IntensityDouble
         Returns the intensity control affects the brightness of the Ray Traced Studio lighting and depends on the global illumination image used   
            
         
        """
        pass
    @IntensityDouble.setter
    def IntensityDouble(self, intensityDouble: float):
        """
        Setter for property: (float) IntensityDouble
         Returns the intensity control affects the brightness of the Ray Traced Studio lighting and depends on the global illumination image used   
            
         
        """
        pass
    @property
    def StaticFinalGatherQuality(self) -> float:
        """
        Getter for property: (float) StaticFinalGatherQuality
         Returns the static final gather quality affects Ray Traced Studio static (still) image rendering   
            
         
        """
        pass
    @StaticFinalGatherQuality.setter
    def StaticFinalGatherQuality(self, staticFinalGatherQuality: float):
        """
        Setter for property: (float) StaticFinalGatherQuality
         Returns the static final gather quality affects Ray Traced Studio static (still) image rendering   
            
         
        """
        pass
    @property
    def StationaryFinalGatherQuality(self) -> float:
        """
        Getter for property: (float) StationaryFinalGatherQuality
         Returns the stationary final gather quality affects Ray Traced Studio rendering when dynamic operations stop   
            
         
        """
        pass
    @StationaryFinalGatherQuality.setter
    def StationaryFinalGatherQuality(self, stationaryFinalGatherQuality: float):
        """
        Setter for property: (float) StationaryFinalGatherQuality
         Returns the stationary final gather quality affects Ray Traced Studio rendering when dynamic operations stop   
            
         
        """
        pass
import NXOpen
class GridBuilder(NXOpen.Builder): 
    """ Represents the builder for adding a grid NXOpen.Display.Grid
    """
    class LineStyleType(Enum):
        """
        Members Include: 
         |Solid|  
         |Dashed|  
         |Phantom|  
         |Centerline|  
         |Dotted|  
         |Longdash|  
         |Dotdash|  
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
        Longdash: int
        Dotdash: int
        Eight: int
        Nine: int
        Ten: int
        Eleven: int
        @staticmethod
        def ValueOf(value: int) -> GridBuilder.LineStyleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LineWeightType(Enum):
        """
        Members Include: 
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
        def ValueOf(value: int) -> GridBuilder.LineWeightType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def LineColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) LineColor
         Returns the line color   
            
         
        """
        pass
    @LineColor.setter
    def LineColor(self, lineColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) LineColor
         Returns the line color   
            
         
        """
        pass
    @property
    def MajorLineSpacing(self) -> float:
        """
        Getter for property: (float) MajorLineSpacing
         Returns the major line spacing   
            
         
        """
        pass
    @MajorLineSpacing.setter
    def MajorLineSpacing(self, majorLineSpacing: float):
        """
        Setter for property: (float) MajorLineSpacing
         Returns the major line spacing   
            
         
        """
        pass
    @property
    def MajorLineStyle(self) -> GridBuilder.LineStyleType:
        """
        Getter for property: ( GridBuilder.LineStyleType NXOpen) MajorLineStyle
         Returns the major line style   
            
         
        """
        pass
    @MajorLineStyle.setter
    def MajorLineStyle(self, majorLineStyle: GridBuilder.LineStyleType):
        """
        Setter for property: ( GridBuilder.LineStyleType NXOpen) MajorLineStyle
         Returns the major line style   
            
         
        """
        pass
    @property
    def MajorLineWeight(self) -> GridBuilder.LineWeightType:
        """
        Getter for property: ( GridBuilder.LineWeightType NXOpen) MajorLineWeight
         Returns the major line weight   
            
         
        """
        pass
    @MajorLineWeight.setter
    def MajorLineWeight(self, majorLineWeight: GridBuilder.LineWeightType):
        """
        Setter for property: ( GridBuilder.LineWeightType NXOpen) MajorLineWeight
         Returns the major line weight   
            
         
        """
        pass
    @property
    def MinorLineStyle(self) -> GridBuilder.LineStyleType:
        """
        Getter for property: ( GridBuilder.LineStyleType NXOpen) MinorLineStyle
         Returns the minor line style   
            
         
        """
        pass
    @MinorLineStyle.setter
    def MinorLineStyle(self, minorLineStyle: GridBuilder.LineStyleType):
        """
        Setter for property: ( GridBuilder.LineStyleType NXOpen) MinorLineStyle
         Returns the minor line style   
            
         
        """
        pass
    @property
    def MinorLineWeight(self) -> GridBuilder.LineWeightType:
        """
        Getter for property: ( GridBuilder.LineWeightType NXOpen) MinorLineWeight
         Returns the minor line weight   
            
         
        """
        pass
    @MinorLineWeight.setter
    def MinorLineWeight(self, minorLineWeight: GridBuilder.LineWeightType):
        """
        Setter for property: ( GridBuilder.LineWeightType NXOpen) MinorLineWeight
         Returns the minor line weight   
            
         
        """
        pass
    @property
    def MinorLinesPerMajor(self) -> int:
        """
        Getter for property: (int) MinorLinesPerMajor
         Returns the minor lines per major   
            
         
        """
        pass
    @MinorLinesPerMajor.setter
    def MinorLinesPerMajor(self, minorLinesPerMajor: int):
        """
        Setter for property: (int) MinorLinesPerMajor
         Returns the minor lines per major   
            
         
        """
        pass
    @property
    def Show(self) -> bool:
        """
        Getter for property: (bool) Show
         Returns the show   
            
         
        """
        pass
    @Show.setter
    def Show(self, show: bool):
        """
        Setter for property: (bool) Show
         Returns the show   
            
         
        """
        pass
    @property
    def ShowMajorLines(self) -> bool:
        """
        Getter for property: (bool) ShowMajorLines
         Returns the show major lines   
            
         
        """
        pass
    @ShowMajorLines.setter
    def ShowMajorLines(self, showMajorLines: bool):
        """
        Setter for property: (bool) ShowMajorLines
         Returns the show major lines   
            
         
        """
        pass
    @property
    def ShowOnTop(self) -> bool:
        """
        Getter for property: (bool) ShowOnTop
         Returns the show on top   
            
         
        """
        pass
    @ShowOnTop.setter
    def ShowOnTop(self, showOnTop: bool):
        """
        Setter for property: (bool) ShowOnTop
         Returns the show on top   
            
         
        """
        pass
    @property
    def SnapPointsPerMinor(self) -> int:
        """
        Getter for property: (int) SnapPointsPerMinor
         Returns the snap points per minor   
            
         
        """
        pass
    @SnapPointsPerMinor.setter
    def SnapPointsPerMinor(self, snapPointsPerMinor: int):
        """
        Setter for property: (int) SnapPointsPerMinor
         Returns the snap points per minor   
            
         
        """
        pass
    @property
    def SnapToGrid(self) -> bool:
        """
        Getter for property: (bool) SnapToGrid
         Returns the snap to grid   
            
         
        """
        pass
    @SnapToGrid.setter
    def SnapToGrid(self, snapToGrid: bool):
        """
        Setter for property: (bool) SnapToGrid
         Returns the snap to grid   
            
         
        """
        pass
    def InheritSettings(self, grid: Grid) -> None:
        """
         Inherits the settings from the specified grid. These includes
                    settings such as 
                    Display.GridBuilder.MajorLineSpacing.
                 
        """
        pass
import NXOpen
class GridCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of plane grid objects """
    def CreateBoxShipGridBuilder(self) -> BoxShipGridBuilder:
        """
         Creates a NXOpen.Display.BoxShipGridBuilder object
                    used to build a box grid on a plane.
                 
         Returns builder ( BoxShipGridBuilder NXOpen):  ship box grid builder .
        """
        pass
    @overload
    def CreateDatumPlaneGridBuilder(self, grid: DatumPlaneGrid) -> DatumPlaneGridBuilder:
        """
         Creates a NXOpen.Display.DatumPlaneGridBuilder object
                    used to edit the supplied datum plane grid.
                 
         Returns builder ( DatumPlaneGridBuilder NXOpen):  datum plane grid builder .
        """
        pass
    @overload
    def CreateDatumPlaneGridBuilder(self, datumPlanes: List[NXOpen.DatumPlane]) -> DatumPlaneGridBuilder:
        """
         Creates a NXOpen.Display.DatumPlaneGridBuilder object 
                    used to build datum plane grids based on the supplied datum plane list.
                 
         Returns builder ( DatumPlaneGridBuilder NXOpen):  datum plane grid builder .
        """
        pass
    def CreatePlanarShipGridBuilder(self, grid: PlanarShipGrid) -> PlanarShipGridBuilder:
        """
         Creates a NXOpen.Display.PlanarShipGridBuilder object
                    used to build a planar ship grid on a datum plane.
                    If the grid is not , the planar ship grid object will be edited.
                 
         Returns builder ( PlanarShipGridBuilder NXOpen):  planar ship grid builder .
        """
        pass
    def CreatePlaneGridBuilder(self, grid: PlaneGrid) -> PlaneGridBuilder:
        """
         Creates a NXOpen.Display.PlaneGridBuilder object
                    used to build a bounded grid on a plane.
                    
                    If the grid is not , the planar grid object will be edited.
                 
         Returns builder ( PlaneGridBuilder NXOpen):  plane grid builder .
        """
        pass
    def FindObject(self, journalIdentifier: str) -> Grid:
        """
         Finds the NXOpen.Display.Grid with the given identifier  
                    as recorded in a journal. An object may not return the same value as 
                    its JournalIdentifier in different versions of the software. However  
                    newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In 
                    general,this method should not be used in handwritten code and exists 
                    to support record and playback of journals.
                    
                    An exception will be thrown if no object can be found with the given 
                    journal identifier. 
                    
                
         Returns grid ( Grid NXOpen):  Grid found .
        """
        pass
    def GetDatumPlaneGrid(self, datumPlane: NXOpen.DatumPlane) -> DatumPlaneGrid:
        """
         Finds the datum grid associated with the specified datum plane.
                 
         Returns datumPlaneGrid ( DatumPlaneGrid NXOpen):  Datum plane grid.  indicates no grid is associated
                            with the datum plane. .
        """
        pass
import NXOpen
class Grid(NXOpen.DisplayableObject): 
    """ Represents a grid """
    pass
import NXOpen
class IDynamicSectionCutCreator(NXOpen.INXObject): 
    """ Represents a dynamic section-cut creator that generates dynamic
        section-cuts (see NXOpen.Display.DynamicSectionCut).
        
        Examples of dynamic section-cut creator are:
        NXOpen.Display.DynamicSection
        NXOpen.Display.Grid
        
     """
    @abstractmethod
    def Find(self, journalIdentifier: str) -> DynamicSectionCut:
        """
         Finds the  NXOpen.Display.DynamicSectionCut  
                with the given identifier as recorded in a journal. An object may 
                not return the same value as its JournalIdentifier in different 
                versions of  the software. However newer versions of the software 
                should find the same object when FindObject is passed older versions 
                of its journal identifier. In general, this method should not be 
                used in handwritten code and exists to support record and playback 
                of journals.
                An exception will be thrown if no object can be found with the 
                given journal identifier. 
         Returns sectionCut ( DynamicSectionCut NXOpen):  .
        """
        pass
    @abstractmethod
    def GetSectionCuts(self, contextOccurrence: NXOpen.NXObject, view: NXOpen.View) -> List[DynamicSectionCut]:
        """
         Gets section-cuts generated by the sectioning the model shown
                    in the specified view. 
                    View must belong to the same part as the section-cut creator. If
                    no view is specified, then section-cuts generated from the 
                    sectionable entities in the part are returned.
                    
                    If a view is specified, then NXOpen.Assemblies.Explosion
                    active in the view is used to get section-cuts for the explosion.
                    If the view does not have any active explosion, then
                    section-cuts generated from the sectionable entities in the part 
                    are returned. 
                 
         Returns sectionCuts ( DynamicSectionCut List[NXOp):  .
        """
        pass
import NXOpen
class ImageBaseBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Display.ImageBaseBuilder.
    Serves as the base class for all NXOpen.Display.ImageBase builders.
    NXOpen.Display.ImageBase base class provides definition, orientation,
    sizing, and display setting controls for image based objects. 
    """
    class BasePointChoices(Enum):
        """
        Members Include: 
         |BottomLeft|  bottom left 
         |BottomCenter|  bottom center 
         |BottomRight|  bottom left 
         |MiddleLeft|  middle left 
         |MiddleCenter|  middle center 
         |MiddleRight|  middle right 
         |TopLeft|  top left 
         |TopCenter|  top center 
         |TopRight|  top right 
         |UserDefined|  user defined 

        """
        BottomLeft: int
        BottomCenter: int
        BottomRight: int
        MiddleLeft: int
        MiddleCenter: int
        MiddleRight: int
        TopLeft: int
        TopCenter: int
        TopRight: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> ImageBaseBuilder.BasePointChoices:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ImageColorModes(Enum):
        """
        Members Include: 
         |Rgb|  rgb color mode 
         |Greyscale|  grey scale color mode 
         |Monochrome|  monochrome color mode 

        """
        Rgb: int
        Greyscale: int
        Monochrome: int
        @staticmethod
        def ValueOf(value: int) -> ImageBaseBuilder.ImageColorModes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class InsertionPoint(Enum):
        """
        Members Include: 
         |Default|  default insertion point type 
         |UserDefined|  user defined insertion point type 

        """
        Default: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> ImageBaseBuilder.InsertionPoint:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ReferenceDirection(Enum):
        """
        Members Include: 
         |Horizontal|  horizontal reference direction 
         |Vertical|  vertical reference direction 

        """
        Horizontal: int
        Vertical: int
        @staticmethod
        def ValueOf(value: int) -> ImageBaseBuilder.ReferenceDirection:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SizeOptions(Enum):
        """
        Members Include: 
         |UserDefined|  user defined option 
         |ImageSize|  image size option 
         |ReferenceScaling|  reference scaling option 

        """
        UserDefined: int
        ImageSize: int
        ReferenceScaling: int
        @staticmethod
        def ValueOf(value: int) -> ImageBaseBuilder.SizeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TransparencyColorFrom(Enum):
        """
        Members Include: 
         |NotSet|  No Transparency Color 
         |FromImage|  Transparency Color from image 
         |PixelColor| 

        """
        NotSet: int
        FromImage: int
        PixelColor: int
        @staticmethod
        def ValueOf(value: int) -> ImageBaseBuilder.TransparencyColorFrom:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BasePointChoice(self) -> ImageBaseBuilder.BasePointChoices:
        """
        Getter for property: ( ImageBaseBuilder.BasePointChoices NXOpen) BasePointChoice
         Returns the image reference base point choice.  
           If you choose 
                 NXOpen::Display::ImageBaseBuilder::BasePointChoicesUserDefined , 
                use  NXOpen::Display::ImageBaseBuilder::SetUserBasePoint  
                to set a point as the User-Defined point. 
                  
         
        """
        pass
    @BasePointChoice.setter
    def BasePointChoice(self, basePoint: ImageBaseBuilder.BasePointChoices):
        """
        Setter for property: ( ImageBaseBuilder.BasePointChoices NXOpen) BasePointChoice
         Returns the image reference base point choice.  
           If you choose 
                 NXOpen::Display::ImageBaseBuilder::BasePointChoicesUserDefined , 
                use  NXOpen::Display::ImageBaseBuilder::SetUserBasePoint  
                to set a point as the User-Defined point. 
                  
         
        """
        pass
    @property
    def ColorMode(self) -> ImageBaseBuilder.ImageColorModes:
        """
        Getter for property: ( ImageBaseBuilder.ImageColorModes NXOpen) ColorMode
         Returns the color mode to display the image.  
             
         
        """
        pass
    @ColorMode.setter
    def ColorMode(self, colorMode: ImageBaseBuilder.ImageColorModes):
        """
        Setter for property: ( ImageBaseBuilder.ImageColorModes NXOpen) ColorMode
         Returns the color mode to display the image.  
             
         
        """
        pass
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Height
         Returns   the height of the image as an  NXOpen::Expression .  
           
                The returned  NXOpen::Expression  is not associative to this object. 
         
                When  NXOpen::Display::ImageBaseBuilder::SizeOption  
                is set to  NXOpen::Display::ImageBaseBuilder::SizeOptionsUserDefined ,
                set the size of the image using  NXOpen::Display::ImageBaseBuilder::SetCornerPoints .
                  
         
        """
        pass
    @property
    def ImageFile(self) -> str:
        """
        Getter for property: (str) ImageFile
         Returns the image file   
            
         
        """
        pass
    @ImageFile.setter
    def ImageFile(self, filename: str):
        """
        Setter for property: (str) ImageFile
         Returns the image file   
            
         
        """
        pass
    @property
    def ImageReferencePoint1(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) ImageReferencePoint1
         Returns   the image reference point1.  
           Only valid when 
                 NXOpen::Display::ImageBaseBuilder::SizeOption  is set to 
                 NXOpen::Display::ImageBaseBuilder::SizeOptionsReferenceScaling . 
         
                Reference Scaling provides sizing the image by defining image reference 
                points and matching them with corresponding model reference points.
                  
         
        """
        pass
    @ImageReferencePoint1.setter
    def ImageReferencePoint1(self, imageReferencePoint1: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) ImageReferencePoint1
         Returns   the image reference point1.  
           Only valid when 
                 NXOpen::Display::ImageBaseBuilder::SizeOption  is set to 
                 NXOpen::Display::ImageBaseBuilder::SizeOptionsReferenceScaling . 
         
                Reference Scaling provides sizing the image by defining image reference 
                points and matching them with corresponding model reference points.
                  
         
        """
        pass
    @property
    def ImageReferencePoint2(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) ImageReferencePoint2
         Returns   the image reference point2.  
           Only valid when 
                 NXOpen::Display::ImageBaseBuilder::SizeOption  is set to 
                 NXOpen::Display::ImageBaseBuilder::SizeOptionsReferenceScaling . 
         
                Reference Scaling provides sizing the image by defining image reference 
                points and matching them with corresponding model reference points.
                  
         
        """
        pass
    @ImageReferencePoint2.setter
    def ImageReferencePoint2(self, imageReferencePoint2: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) ImageReferencePoint2
         Returns   the image reference point2.  
           Only valid when 
                 NXOpen::Display::ImageBaseBuilder::SizeOption  is set to 
                 NXOpen::Display::ImageBaseBuilder::SizeOptionsReferenceScaling . 
         
                Reference Scaling provides sizing the image by defining image reference 
                points and matching them with corresponding model reference points.
                  
         
        """
        pass
    @property
    def ImageReferencePoint3(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) ImageReferencePoint3
         Returns   the image reference point3.  
           Only valid when 
                 NXOpen::Display::ImageBaseBuilder::SizeOption  is set to 
                 NXOpen::Display::ImageBaseBuilder::SizeOptionsReferenceScaling 
                and  NXOpen::Display::ImageBaseBuilder::LockAspectRatio  
                is False. 
         
                Reference Scaling provides sizing the image by defining image reference 
                points and matching them with corresponding model reference points.
                  
         
        """
        pass
    @ImageReferencePoint3.setter
    def ImageReferencePoint3(self, imageReferencePoint3: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) ImageReferencePoint3
         Returns   the image reference point3.  
           Only valid when 
                 NXOpen::Display::ImageBaseBuilder::SizeOption  is set to 
                 NXOpen::Display::ImageBaseBuilder::SizeOptionsReferenceScaling 
                and  NXOpen::Display::ImageBaseBuilder::LockAspectRatio  
                is False. 
         
                Reference Scaling provides sizing the image by defining image reference 
                points and matching them with corresponding model reference points.
                  
         
        """
        pass
    @property
    def InsertionPointLocation(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) InsertionPointLocation
         Returns the insertion point of the image   
            
         
        """
        pass
    @InsertionPointLocation.setter
    def InsertionPointLocation(self, insertPoint: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) InsertionPointLocation
         Returns the insertion point of the image   
            
         
        """
        pass
    @property
    def InsertionPointOption(self) -> ImageBaseBuilder.InsertionPoint:
        """
        Getter for property: ( ImageBaseBuilder.InsertionPoint NXOpen) InsertionPointOption
         Returns the image insertion point type   
            
         
        """
        pass
    @InsertionPointOption.setter
    def InsertionPointOption(self, insertPoint: ImageBaseBuilder.InsertionPoint):
        """
        Setter for property: ( ImageBaseBuilder.InsertionPoint NXOpen) InsertionPointOption
         Returns the image insertion point type   
            
         
        """
        pass
    @property
    def LockAspectRatio(self) -> bool:
        """
        Getter for property: (bool) LockAspectRatio
         Returns the lock aspect ratio   
            
         
        """
        pass
    @LockAspectRatio.setter
    def LockAspectRatio(self, lockAspectRatio: bool):
        """
        Setter for property: (bool) LockAspectRatio
         Returns the lock aspect ratio   
            
         
        """
        pass
    @property
    def ModelReferencePoint1(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) ModelReferencePoint1
         Returns   the model reference point1.  
           Only valid when 
                 NXOpen::Display::ImageBaseBuilder::SizeOption  is set to 
                 NXOpen::Display::ImageBaseBuilder::SizeOptionsReferenceScaling . 
         
                Reference Scaling provides sizing the image by defining image reference 
                points and matching them with corresponding model reference points.
                  
         
        """
        pass
    @ModelReferencePoint1.setter
    def ModelReferencePoint1(self, modelReferencePoint1: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) ModelReferencePoint1
         Returns   the model reference point1.  
           Only valid when 
                 NXOpen::Display::ImageBaseBuilder::SizeOption  is set to 
                 NXOpen::Display::ImageBaseBuilder::SizeOptionsReferenceScaling . 
         
                Reference Scaling provides sizing the image by defining image reference 
                points and matching them with corresponding model reference points.
                  
         
        """
        pass
    @property
    def ModelReferencePoint2(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) ModelReferencePoint2
         Returns   the model reference point2.  
           Only valid when 
                 NXOpen::Display::ImageBaseBuilder::SizeOption  is set to 
                 NXOpen::Display::ImageBaseBuilder::SizeOptionsReferenceScaling . 
         
                Reference Scaling provides sizing the image by defining image reference 
                points and matching them with corresponding model reference points.
                  
         
        """
        pass
    @ModelReferencePoint2.setter
    def ModelReferencePoint2(self, modelReferencePoint2: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) ModelReferencePoint2
         Returns   the model reference point2.  
           Only valid when 
                 NXOpen::Display::ImageBaseBuilder::SizeOption  is set to 
                 NXOpen::Display::ImageBaseBuilder::SizeOptionsReferenceScaling . 
         
                Reference Scaling provides sizing the image by defining image reference 
                points and matching them with corresponding model reference points.
                  
         
        """
        pass
    @property
    def ModelReferencePoint3(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) ModelReferencePoint3
         Returns   the model reference point3.  
           Only valid when 
                 NXOpen::Display::ImageBaseBuilder::SizeOption  is set to 
                 NXOpen::Display::ImageBaseBuilder::SizeOptionsReferenceScaling 
                and  NXOpen::Display::ImageBaseBuilder::LockAspectRatio  
                is False. 
         
                Reference Scaling provides sizing the image by defining image reference 
                points and matching them with corresponding model reference points.
                  
         
        """
        pass
    @ModelReferencePoint3.setter
    def ModelReferencePoint3(self, modelReferencePoint3: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) ModelReferencePoint3
         Returns   the model reference point3.  
           Only valid when 
                 NXOpen::Display::ImageBaseBuilder::SizeOption  is set to 
                 NXOpen::Display::ImageBaseBuilder::SizeOptionsReferenceScaling 
                and  NXOpen::Display::ImageBaseBuilder::LockAspectRatio  
                is False. 
         
                Reference Scaling provides sizing the image by defining image reference 
                points and matching them with corresponding model reference points.
                  
         
        """
        pass
    @property
    def OverallTranslucency(self) -> int:
        """
        Getter for property: (int) OverallTranslucency
         Returns the overall translucency.  
           The range of this value is 0 to 100.   
         
        """
        pass
    @OverallTranslucency.setter
    def OverallTranslucency(self, overallTranslucency: int):
        """
        Setter for property: (int) OverallTranslucency
         Returns the overall translucency.  
           The range of this value is 0 to 100.   
         
        """
        pass
    @property
    def PixelColorTolerance(self) -> int:
        """
        Getter for property: (int) PixelColorTolerance
         Returns the transparency pixel color tolerance.  
           The range of this value is 
                0 to 255.
                  
         
        """
        pass
    @PixelColorTolerance.setter
    def PixelColorTolerance(self, colorTolerence: int):
        """
        Setter for property: (int) PixelColorTolerance
         Returns the transparency pixel color tolerance.  
           The range of this value is 
                0 to 255.
                  
         
        """
        pass
    @property
    def ReferenceDirectionOption(self) -> ImageBaseBuilder.ReferenceDirection:
        """
        Getter for property: ( ImageBaseBuilder.ReferenceDirection NXOpen) ReferenceDirectionOption
         Returns the image alignment reference direction type.  
          
                 NXOpen::Display::ImageBaseBuilder::ReferenceDirectionHorizontal 
                means rotate the image to align its horizontal direction with the user-specified 
                reference direction (if defined). 
                  
         
        """
        pass
    @ReferenceDirectionOption.setter
    def ReferenceDirectionOption(self, referenceDirection: ImageBaseBuilder.ReferenceDirection):
        """
        Setter for property: ( ImageBaseBuilder.ReferenceDirection NXOpen) ReferenceDirectionOption
         Returns the image alignment reference direction type.  
          
                 NXOpen::Display::ImageBaseBuilder::ReferenceDirectionHorizontal 
                means rotate the image to align its horizontal direction with the user-specified 
                reference direction (if defined). 
                  
         
        """
        pass
    @property
    def RotateAngleOfReferenceVector(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RotateAngleOfReferenceVector
         Returns the current rotation angle of image from aligned reference direction   
            
         
        """
        pass
    @property
    def SizeOption(self) -> ImageBaseBuilder.SizeOptions:
        """
        Getter for property: ( ImageBaseBuilder.SizeOptions NXOpen) SizeOption
         Returns the size option   
            
         
        """
        pass
    @SizeOption.setter
    def SizeOption(self, sizeOption: ImageBaseBuilder.SizeOptions):
        """
        Setter for property: ( ImageBaseBuilder.SizeOptions NXOpen) SizeOption
         Returns the size option   
            
         
        """
        pass
    @property
    def TransparencyColorOption(self) -> ImageBaseBuilder.TransparencyColorFrom:
        """
        Getter for property: ( ImageBaseBuilder.TransparencyColorFrom NXOpen) TransparencyColorOption
         Returns the transparency color option   
            
         
        """
        pass
    @TransparencyColorOption.setter
    def TransparencyColorOption(self, transparencyColorOption: ImageBaseBuilder.TransparencyColorFrom):
        """
        Setter for property: ( ImageBaseBuilder.TransparencyColorFrom NXOpen) TransparencyColorOption
         Returns the transparency color option   
            
         
        """
        pass
    @property
    def UserBasePoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) UserBasePoint
         Returns   the user defined base point.  
           Only valid when 
                 NXOpen::Display::ImageBaseBuilder::BasePointChoice  is set to 
                 NXOpen::Display::ImageBaseBuilder::BasePointChoicesUserDefined . 
          
                  
         
        """
        pass
    @UserBasePoint.setter
    def UserBasePoint(self, basePoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) UserBasePoint
         Returns   the user defined base point.  
           Only valid when 
                 NXOpen::Display::ImageBaseBuilder::BasePointChoice  is set to 
                 NXOpen::Display::ImageBaseBuilder::BasePointChoicesUserDefined . 
          
                  
         
        """
        pass
    @property
    def UserInsertionPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) UserInsertionPoint
         Returns the user defined insertion point   
            
         
        """
        pass
    @UserInsertionPoint.setter
    def UserInsertionPoint(self, insertPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) UserInsertionPoint
         Returns the user defined insertion point   
            
         
        """
        pass
    @property
    def UserReferenceDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) UserReferenceDirection
         Returns the user defined reference direction vector.  
           A direction normal to 
                the plane of the image is invalid.
                  
         
        """
        pass
    @UserReferenceDirection.setter
    def UserReferenceDirection(self, userDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) UserReferenceDirection
         Returns the user defined reference direction vector.  
           A direction normal to 
                the plane of the image is invalid.
                  
         
        """
        pass
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Width
         Returns   the width of the image as an  NXOpen::Expression .  
           
                The returned  NXOpen::Expression  is not associative to this object. 
         
                When  NXOpen::Display::ImageBaseBuilder::SizeOption  
                is set to  NXOpen::Display::ImageBaseBuilder::SizeOptionsUserDefined ,
                set the size of the image using  NXOpen::Display::ImageBaseBuilder::SetCornerPoints .
                  
         
        """
        pass
    def AlignImageToReferenceDirection(self) -> None:
        """
         Align Image to Reference Direction
        """
        pass
    def FlipHorizontal(self) -> None:
        """
         Flips the image horizontally. 
        """
        pass
    def FlipVertical(self) -> None:
        """
         Flips the image vertically. 
        """
        pass
    def GetBackgroundColor(self) -> List[float]:
        """
         Gets the background color (RGB value) of the image. Only valid
                when NXOpen.Display.ImageBaseBuilder.ColorMode
                is set to NXOpen.Display.ImageBaseBuilder.ImageColorModes.Greyscale.
                The length of the output array will always be 3.  Each color value of 
                the double array is in the range 0.0 to 1.0. 
                
         Returns backgroundColor (List[float]):  RGB color array .
        """
        pass
    def GetCornerPoints(self) -> Tuple[NXOpen.Point3d, NXOpen.Point3d, NXOpen.Point3d, NXOpen.Point3d]:
        """
         Get the image corner points. The points define a rectangular region
                and are ordered counter-clockwise.
                
         Returns A tuple consisting of (point1, point2, point3, point4). 
         - point1 is:  NXOpen.Point3d. first corner point of image .
         - point2 is:  NXOpen.Point3d. second corner point of image .
         - point3 is:  NXOpen.Point3d. third corner point of image .
         - point4 is:  NXOpen.Point3d. fourth corner point of image .

        """
        pass
    def GetForegroundColor(self) -> List[float]:
        """
         Gets the foreground color (RGB value) of the image. Only valid
                when NXOpen.Display.ImageBaseBuilder.ColorMode
                is set to NXOpen.Display.ImageBaseBuilder.ImageColorModes.Greyscale.
                The length of the output array will always be 3.  Each color value of 
                the double array is in the range 0.0 to 1.0. 
                
         Returns foregroundColor (List[float]):  RGB color array .
        """
        pass
    def GetImagesInPart(self) -> List[str]:
        """
         Provide a list of names of the NXOpen.Display.ImageData
                objects saved in current part file.
                
         Returns imageSimpleName (List[str]):  Array of NXOpen.Display.ImageData names .
        """
        pass
    def GetTransparentPixelColor(self) -> List[float]:
        """
         Gets the transparency color (RGB value) of the image. Only valid
                when NXOpen.Display.ImageBaseBuilder.TransparencyColorOption
                is set to NXOpen.Display.ImageBaseBuilder.TransparencyColorFrom.PixelColor.
                The length of the output array will always be 3.  Each color value of 
                the double array is in the range 0.0 to 1.0. 
                
         Returns transparencyColor (List[float]):  RGB color array .
        """
        pass
    def OrientViewToImage(self) -> None:
        """
         Orients and fits the work view's view direction along the reverse normal direction of the image 
        """
        pass
    def ResetImageSize(self) -> None:
        """
         Resets the image to its original size. 
        """
        pass
    def RotateLeft(self) -> None:
        """
         Rotates the image 90 degrees counter-clockwise. 
        """
        pass
    def RotateRight(self) -> None:
        """
         Rotates the image 90 degrees clockwise. 
        """
        pass
    def SetBackgroundColor(self, backgroundColor: List[float]) -> None:
        """
         Sets the background color (RGB value) of the image. Only valid
                when NXOpen.Display.ImageBaseBuilder.ColorMode
                is set to NXOpen.Display.ImageBaseBuilder.ImageColorModes.Greyscale.
                The length of the input array should always be 3.  Each color value of 
                the double array must be in the range 0.0 to 1.0. 
                
        """
        pass
    def SetCornerPoints(self, point1: NXOpen.Point3d, point2: NXOpen.Point3d, point3: NXOpen.Point3d, point4: NXOpen.Point3d) -> None:
        """
         Set the image corner points.  The points must define a rectangular
                region and be ordered counter-clockwise.
                
        """
        pass
    def SetForegroundColor(self, foregroundColor: List[float]) -> None:
        """
         Sets the foreground color (RGB value) of the image. Only valid
                when NXOpen.Display.ImageBaseBuilder.ColorMode
                is set to NXOpen.Display.ImageBaseBuilder.ImageColorModes.Greyscale.
                The length of the input array should always be 3.  Each color value of 
                the double array must be in the range 0.0 to 1.0. 
                
        """
        pass
    def SetImageFromPart(self, imageName: str) -> None:
        """
         Set a NXOpen.Display.ImageData object currently 
                stored in the part as the image used by the builder. 
                
        """
        pass
    def SetTransparentPixelColor(self, transparencyColor: List[float]) -> None:
        """
         Sets the transparency color (RGB value) of the image. Only valid
                when NXOpen.Display.ImageBaseBuilder.TransparencyColorOption
                is set to NXOpen.Display.ImageBaseBuilder.TransparencyColorFrom.PixelColor.
                The length of the input array should always be 3.  Each color value of 
                the double array must be in the range 0.0 to 1.0. 
                
        """
        pass
import NXOpen
class ImageBasedLighting(NXOpen.Builder): 
    """
    Represents a NXOpen.Display.ImageBasedLighting
    Image-based Lighting (IBL) is only performed in High Quality Image 
    renderings.  IBL replaces the Lights in a scene with lighting effects 
    derived from a given image.
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return .
    """
    class ImageBlurType(Enum):
        """
        Members Include: 
         |NotSet| 
         |Low| 
         |Medium| 
         |High| 

        """
        NotSet: int
        Low: int
        Medium: int
        High: int
        @staticmethod
        def ValueOf(value: int) -> ImageBasedLighting.ImageBlurType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ImageUpVectorTypes(Enum):
        """
        Members Include: 
         |AlignWithFloorPlane| 
         |UserDefined| 

        """
        AlignWithFloorPlane: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> ImageBasedLighting.ImageUpVectorTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ImagesType(Enum):
        """
        Members Include: 
         |Background|  Use the background image. 
         |Stage|  Use the stage. 
         |UserDefined|  Use the image file specified. 
         |LightingOnly|  only used for IBL

        """
        Background: int
        Stage: int
        UserDefined: int
        LightingOnly: int
        @staticmethod
        def ValueOf(value: int) -> ImageBasedLighting.ImagesType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ShadowsType(Enum):
        """
        Members Include: 
         |NotSet|  No shadows will be produced. 
         |SoftEdged|  Soft-edged,approximated shadows will be generated using a shadow
                                                                                       mapping algorithm. 
         |HardEdged|  Hard-edged, precise shadows will be generated using a ray-tracing
                                                                                       algorithm. 
         |TranslucentHard|  Hard-edged, precise shadows will be generated using a ray-tracing
                                                                                       algorithm.  Shadows from translucent objects will also be generated
                                                                                       and their color will be determined by the transparent object's
                                                                                       color. 

        """
        NotSet: int
        SoftEdged: int
        HardEdged: int
        TranslucentHard: int
        @staticmethod
        def ValueOf(value: int) -> ImageBasedLighting.ShadowsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Accuracy(self) -> float:
        """
        Getter for property: (float) Accuracy
         Returns the accuracy of the lighting and shadows produced from the given image   
            
         
        """
        pass
    @Accuracy.setter
    def Accuracy(self, accuracy: float):
        """
        Setter for property: (float) Accuracy
         Returns the accuracy of the lighting and shadows produced from the given image   
            
         
        """
        pass
    @property
    def ColorSaturation(self) -> float:
        """
        Getter for property: (float) ColorSaturation
         Returns the image-based lighting color saturation   
            
         
        """
        pass
    @ColorSaturation.setter
    def ColorSaturation(self, color_saturation: float):
        """
        Setter for property: (float) ColorSaturation
         Returns the image-based lighting color saturation   
            
         
        """
        pass
    @property
    def Image(self) -> Image:
        """
        Getter for property: ( Image NXOpen) Image
         Returns the image-based lighting's image builder   
            
         
        """
        pass
    @Image.setter
    def Image(self, image_builder: Image):
        """
        Setter for property: ( Image NXOpen) Image
         Returns the image-based lighting's image builder   
            
         
        """
        pass
    @property
    def ImageBlur(self) -> ImageBasedLighting.ImageBlurType:
        """
        Getter for property: ( ImageBasedLighting.ImageBlurType NXOpen) ImageBlur
         Returns the blurr of the lighting image   
            
         
        """
        pass
    @ImageBlur.setter
    def ImageBlur(self, image_blurr: ImageBasedLighting.ImageBlurType):
        """
        Setter for property: ( ImageBasedLighting.ImageBlurType NXOpen) ImageBlur
         Returns the blurr of the lighting image   
            
         
        """
        pass
    @property
    def ImageFilename(self) -> str:
        """
        Getter for property: (str) ImageFilename
         Returns the image filename used for image-based lighting   
            
         
        """
        pass
    @ImageFilename.setter
    def ImageFilename(self, image_file_name: str):
        """
        Setter for property: (str) ImageFilename
         Returns the image filename used for image-based lighting   
            
         
        """
        pass
    @property
    def ImageRotation(self) -> float:
        """
        Getter for property: (float) ImageRotation
         Returns the image rotation angle (in degrees)   
            
         
        """
        pass
    @ImageRotation.setter
    def ImageRotation(self, imageRotation: float):
        """
        Setter for property: (float) ImageRotation
         Returns the image rotation angle (in degrees)   
            
         
        """
        pass
    @property
    def ImageType(self) -> ImageBasedLighting.ImagesType:
        """
        Getter for property: ( ImageBasedLighting.ImagesType NXOpen) ImageType
         Returns the image type   
            
         
        """
        pass
    @ImageType.setter
    def ImageType(self, image_type: ImageBasedLighting.ImagesType):
        """
        Setter for property: ( ImageBasedLighting.ImagesType NXOpen) ImageType
         Returns the image type   
            
         
        """
        pass
    @property
    def ImageUpVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ImageUpVector
         Returns the image up vector direction, relative to the absolute coordinate system   
            
         
        """
        pass
    @ImageUpVector.setter
    def ImageUpVector(self, imageUpVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ImageUpVector
         Returns the image up vector direction, relative to the absolute coordinate system   
            
         
        """
        pass
    @property
    def ImageUpVectorType(self) -> ImageBasedLighting.ImageUpVectorTypes:
        """
        Getter for property: ( ImageBasedLighting.ImageUpVectorTypes NXOpen) ImageUpVectorType
         Returns the image up vector define   
            
         
        """
        pass
    @ImageUpVectorType.setter
    def ImageUpVectorType(self, imageUpVector: ImageBasedLighting.ImageUpVectorTypes):
        """
        Setter for property: ( ImageBasedLighting.ImageUpVectorTypes NXOpen) ImageUpVectorType
         Returns the image up vector define   
            
         
        """
        pass
    @property
    def Intensity(self) -> float:
        """
        Getter for property: (float) Intensity
         Returns the intensity of the image-based lighting light effects   
            
         
        """
        pass
    @Intensity.setter
    def Intensity(self, intensity: float):
        """
        Setter for property: (float) Intensity
         Returns the intensity of the image-based lighting light effects   
            
         
        """
        pass
    @property
    def LwrtAngle(self) -> float:
        """
        Getter for property: (float) LwrtAngle
         Returns the angle of the lwrt image-based lighting light effects   
            
         
        """
        pass
    @LwrtAngle.setter
    def LwrtAngle(self, lwrt_angle: float):
        """
        Setter for property: (float) LwrtAngle
         Returns the angle of the lwrt image-based lighting light effects   
            
         
        """
        pass
    @property
    def LwrtIntensity(self) -> float:
        """
        Getter for property: (float) LwrtIntensity
         Returns the intensity of the lwrt image-based lighting light effects   
            
         
        """
        pass
    @LwrtIntensity.setter
    def LwrtIntensity(self, lwrt_intensity: float):
        """
        Setter for property: (float) LwrtIntensity
         Returns the intensity of the lwrt image-based lighting light effects   
            
         
        """
        pass
    @property
    def LwrtQuality(self) -> float:
        """
        Getter for property: (float) LwrtQuality
         Returns the quality of the lwrt image-based lighting light effects 1 to 7   
            
         
        """
        pass
    @LwrtQuality.setter
    def LwrtQuality(self, lwrt_quality: float):
        """
        Setter for property: (float) LwrtQuality
         Returns the quality of the lwrt image-based lighting light effects 1 to 7   
            
         
        """
        pass
    @property
    def ShadowSoftness(self) -> float:
        """
        Getter for property: (float) ShadowSoftness
         Returns the image-based lighting shadow softness   
            
         
        """
        pass
    @ShadowSoftness.setter
    def ShadowSoftness(self, shadow_softness: float):
        """
        Setter for property: (float) ShadowSoftness
         Returns the image-based lighting shadow softness   
            
         
        """
        pass
    @property
    def ShadowType(self) -> ImageBasedLighting.ShadowsType:
        """
        Getter for property: ( ImageBasedLighting.ShadowsType NXOpen) ShadowType
         Returns the shadow type   
            
         
        """
        pass
    @ShadowType.setter
    def ShadowType(self, shadow_type: ImageBasedLighting.ShadowsType):
        """
        Setter for property: ( ImageBasedLighting.ShadowsType NXOpen) ShadowType
         Returns the shadow type   
            
         
        """
        pass
    @property
    def UseImageBasedLighting(self) -> bool:
        """
        Getter for property: (bool) UseImageBasedLighting
         Returns whether image-based lighting (IBL) is enabled   
            
         
        """
        pass
    @UseImageBasedLighting.setter
    def UseImageBasedLighting(self, useIBL: bool):
        """
        Setter for property: (bool) UseImageBasedLighting
         Returns whether image-based lighting (IBL) is enabled   
            
         
        """
        pass
    @property
    def UseLightsForShadowCatcherInHqi(self) -> bool:
        """
        Getter for property: (bool) UseLightsForShadowCatcherInHqi
         Returns whether high quality image generation (HQI) uses individual light sources or image-based lighting for shadow catcher   
            
         
        """
        pass
    @UseLightsForShadowCatcherInHqi.setter
    def UseLightsForShadowCatcherInHqi(self, useLightsForShadowCatcherInHqi: bool):
        """
        Setter for property: (bool) UseLightsForShadowCatcherInHqi
         Returns whether high quality image generation (HQI) uses individual light sources or image-based lighting for shadow catcher   
            
         
        """
        pass
    @property
    def UseLightsForShadowCatcherInLwrt(self) -> bool:
        """
        Getter for property: (bool) UseLightsForShadowCatcherInLwrt
         Returns whether Advanced Studio display (lwrt) uses individual light sources or image-based lighting for shadow catcher   
            
         
        """
        pass
    @UseLightsForShadowCatcherInLwrt.setter
    def UseLightsForShadowCatcherInLwrt(self, useLightsForShadowCatcherInLwrt: bool):
        """
        Setter for property: (bool) UseLightsForShadowCatcherInLwrt
         Returns whether Advanced Studio display (lwrt) uses individual light sources or image-based lighting for shadow catcher   
            
         
        """
        pass
    @property
    def UseLwrtImageBasedLighting(self) -> bool:
        """
        Getter for property: (bool) UseLwrtImageBasedLighting
         Returns whether image-based lighting is enabled in Advanced Studio (lwrt) display   
            
         
        """
        pass
    @UseLwrtImageBasedLighting.setter
    def UseLwrtImageBasedLighting(self, useLwrtIBL: bool):
        """
        Setter for property: (bool) UseLwrtImageBasedLighting
         Returns whether image-based lighting is enabled in Advanced Studio (lwrt) display   
            
         
        """
        pass
    def CommitAndDisplay(self, view: NXOpen.View, update_display: bool) -> None:
        """
         Saves the attributes and optionally updates the display of image-based lighting 
        """
        pass
import NXOpen
class ImageBase(NXOpen.DisplayableObject): 
    """ Represents a NXOpen.Display.ImageBase that provides  
    definition, orientation, sizing, and display setting controls for image 
    based objects. 
    """
    pass
import NXOpen
class ImageCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of image objects """
    def CreateRasterImageBuilder(self, image: RasterImage) -> RasterImageBuilder:
        """
         Creates a NXOpen.Display.RasterImageBuilder object
                    used to build an image.
                    
                    If the image is not , the image object will be edited.
                 
         Returns builder ( RasterImageBuilder NXOpen):  raster image builder .
        """
        pass
    def FindObject(self, journalIdentifier: str) -> ImageBase:
        """
         Finds the NXOpen.Display.ImageBase with the given identifier  
                    as recorded in a journal. An object may not return the same value as 
                    its JournalIdentifier in different versions of the software. However  
                    newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In 
                    general,this method should not be used in handwritten code and exists 
                    to support record and playback of journals.
                    
                    An exception will be thrown if no object can be found with the given 
                    journal identifier. 
                    
                
         Returns image ( ImageBase NXOpen):  Image found .
        """
        pass
import NXOpen
class ImageDataCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Display.ImageData 
    objects. The NXOpen.Display.ImageDataCollection also provides
    an iterator that iterates through all the NXOpen.Display.ImageData
    objects in the part.
    """
    def FindObject(self, journalIdentifier: str) -> ImageData:
        """
         Finds the NXOpen.Display.ImageData with the given identifier  
                    as recorded in a journal. An object may not return the same value as 
                    its JournalIdentifier in different versions of the software. However  
                    newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In 
                    general,this method should not be used in handwritten code and exists 
                    to support record and playback of journals.
                    
                    An exception will be thrown if no object can be found with the given 
                    journal identifier. 
                    
                
         Returns imageData ( ImageData NXOpen):  Image data found .
        """
        pass
import NXOpen
class ImageData(NXOpen.NXObject): 
    """ Represents a NXOpen.Display.ImageData that stores the 
    contents of a previously imported image file in the part.
    Display.ImageBaseBuilder.GetImagesInPart provides a
    list of names of the NXOpen.Display.ImageData saved in the 
    part file.
    Use Display.ImageBaseBuilder.SetImageFromPart to set
    a NXOpen.Display.ImageData object (by name) as the image used
    by the builder.
    """
    pass
import NXOpen
class Image(NXOpen.Builder): 
    """
    Represents a NXOpen.Display.Image
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return .
    """
    @property
    def ImagePreviewToggle(self) -> bool:
        """
        Getter for property: (bool) ImagePreviewToggle
         Returns the image preview toggle   
            
         
        """
        pass
    @ImagePreviewToggle.setter
    def ImagePreviewToggle(self, imagePreviewToggle: bool):
        """
        Setter for property: (bool) ImagePreviewToggle
         Returns the image preview toggle   
            
         
        """
        pass
    @property
    def PatternRepeatFactor(self) -> float:
        """
        Getter for property: (float) PatternRepeatFactor
         Returns the pattern repeat factor - the number of times the image repeats; non integer patternRepeatFactor numbers result in partial repeats.  
            
         
        """
        pass
    @PatternRepeatFactor.setter
    def PatternRepeatFactor(self, patternRepeatFactor: float):
        """
        Setter for property: (float) PatternRepeatFactor
         Returns the pattern repeat factor - the number of times the image repeats; non integer patternRepeatFactor numbers result in partial repeats.  
            
         
        """
        pass
    def ImageFileSelect(self) -> None:
        """
         Gets an image file using file selection. 
        """
        pass
    def ImagePaletteSelect(self) -> None:
        """
         Gets an image file from the image palette. 
        """
        pass
class IrayPlusMaterialAttributeEnum(IrayPlusMaterialAttribute): 
    """ Represents a IrayPlus Enum Attribute 
        This class is restricted to being called from a program running during an 
        Interactive NX session.  If run from a non-interactive session it will 
        return .
        """
    @property
    def EnumValue(self) -> int:
        """
        Getter for property: (int) EnumValue
         Returns the enum value   
            
         
        """
        pass
    @EnumValue.setter
    def EnumValue(self, enum_value: int):
        """
        Setter for property: (int) EnumValue
         Returns the enum value   
            
         
        """
        pass
import NXOpen
class IrayPlusMaterialAttribute(NXOpen.TaggedObject): 
    """ Represents an IrayPlus Attribute 
        This class is restricted to being called from a program running during an 
        Interactive NX session.  If run from a non-interactive session it will 
        return .
        """
    @property
    def ParameterName(self) -> str:
        """
        Getter for property: (str) ParameterName
         Returns the parameter name of specific material object.  
            
         
        """
        pass
    @ParameterName.setter
    def ParameterName(self, parameterName: str):
        """
        Setter for property: (str) ParameterName
         Returns the parameter name of specific material object.  
            
         
        """
        pass
    def GetValueAsString(self) -> str:
        """
         Gets an attribute's value as string for specific attribute object 
                    The attribute object can be queried from function:
                    NXOpen.Display.IrayPlusMaterialEditorBuilder.GetComponentParameter.
                    NOTE: The returned attribueValue TEXT should be freed (TEXT_free) by the caller.
                
         Returns attribueValue (str): .
        """
        pass
    def SetValueFromString(self, attribueValue: str) -> None:
        """
         Sets attribute's value for specific attribute object. 
                    Users can follow the steps: 
                    (1) Use NXOpen.Display.IrayPlusMaterialEditorBuilder.GetComponentParameter
                    to get all the attribute objects of specific material component.
                    (2)Iterate all these attribute objects. Find the specific attribute you want 
                    to modify. For example user want to ReflectionColour-ColourOffset in ClearCoat layer.
                    (3)Pass the attribute object and the new attribute value "1.000000000000000,
                    0.000000000000000,0.000000000000000" as parameter to call this function.
                
        """
        pass
import NXOpen
class IrayPlusMaterialEditorBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Display.IrayPlusMaterialEditorBuilder 
        This class is restricted to being called from a program running during an 
        Interactive NX session.  If run from a non-interactive session it will 
        return .

        The IrayPlusMaterialEditorBuilder used to manipulate specific material for IrayPlus.
        It maintained an IrayPlusMatAttribute based hierarchical structure corresponding to the 
        xml structure of IrayPlus material.

        The example of the hierarchical structure for material Varnished Cherry is:
        
        Material-Layers
                    -ClearCoat
                      -Attribute1
                      -Attribute2
                      -...
                -Base
                  -Attribute1
                  -Attribute2
                  -...
                -Geometry
                  -Attribute1
                  -Attribute2
                  -...
                -Global Texture Space
                  -Attribute1
                  -Attribute2
                  -...
        Each node in the hierarchy is an IrayPlusMatAttribute object.
        This structure been created when the IrayPlusMaterialEditorBuilder creating process.
        
        Example for general workflow of set parameter show bellow:
        (1)Use GetMaterialLayersInfo() to get names and unique names
         of all the layers and components of the material.
         For the example Varnished Cherry material. 
         It will return 4 names:[ClearCoat,Base,Geometry,Global Texture Space] and 4 unique names:[
         model2_'Varnished Cherry_Layer_198, Matte, BaseGeometry,Box].

        (2)Then we can use these name to call GetComponentInfo()
          to get the parameters of each component:
          If we use 'Base' as component name. The attribute number will return 18. The attribute list
          will return array like:[Base-Base Type, Base-Colour-Interface Type,...]
           
        (3)Use GetComponentParameter() to get attribute object of specific attribute name.
          We can use 'Base-Colour-Interface Type' as parameter to call GetComponentParameter().
          It will return the pointer of IrayPlusMatAttribute object of this attribute.User can 
          modify the value of the IrayPlusMatAttribute object.
          
        (4)Use SetComponentParameter() to set the value of attribute.
           After modify IrayPlusMatAttribute object returned by GetComponentParameter().
           We can use 'Base-Colour-Interface Type' and the pointer to IrayPlusMatAttribute object that
           been modified as parameter to call SetComponentParameter() to set the value into hierarchy.
           
        (5)If you did any change of hierarchy. You need to call builder's commit() function to
          make hierarchy apply to IrayPlus Rendeing engine to make all your modification have effect.

                 
        NOTE: The detail rule of using each function see comments of specific function.
         
    """
    class CoordinateSpaceType(Enum):
        """
        Members Include: 
         |Model|   Model Coordinate Space
         |World|   World Coordinate Space

        """
        Model: int
        World: int
        @staticmethod
        def ValueOf(value: int) -> IrayPlusMaterialEditorBuilder.CoordinateSpaceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LayerType(Enum):
        """
        Members Include: 
         |Coatings|   Coating layers
         |Base|   Base layer
         |Geometry|   Base Geometry layer
         |TextureSpace|   Global texture space layer
         |MaxNumber|   max layer type

        """
        Coatings: int
        Base: int
        Geometry: int
        TextureSpace: int
        MaxNumber: int
        @staticmethod
        def ValueOf(value: int) -> IrayPlusMaterialEditorBuilder.LayerType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MappingProjections(Enum):
        """
        Members Include: 
         |Uv| 
         |Planar| 
         |Box| 
         |Spherical| 
         |Cylindrical| 

        """
        Uv: int
        Planar: int
        Box: int
        Spherical: int
        Cylindrical: int
        @staticmethod
        def ValueOf(value: int) -> IrayPlusMaterialEditorBuilder.MappingProjections:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def MaterialName(self) -> str:
        """
        Getter for property: (str) MaterialName
         Returns the current material name of material editor builder.  
           
                    NOTE: the returned materialName should be freed via TEXT_free by caller.
                  
         
        """
        pass
    @MaterialName.setter
    def MaterialName(self, materialName: str):
        """
        Setter for property: (str) MaterialName
         Returns the current material name of material editor builder.  
           
                    NOTE: the returned materialName should be freed via TEXT_free by caller.
                  
         
        """
        pass
    @property
    def PreviewToggle(self) -> bool:
        """
        Getter for property: (bool) PreviewToggle
         Returns a boolean value that indicate whether the preview toggle is ON.  
           If preview toggle is true. 
                then the preview image of the material will be generated.  
         
        """
        pass
    @PreviewToggle.setter
    def PreviewToggle(self, toggle_on: bool):
        """
        Setter for property: (bool) PreviewToggle
         Returns a boolean value that indicate whether the preview toggle is ON.  
           If preview toggle is true. 
                then the preview image of the material will be generated.  
         
        """
        pass
    def AddComponent(self, componentType: str) -> Tuple[str, int]:
        """
         Adds a component to layers for specific layer type.
                
                    Let material ''Varnished Cherry' for example:
                    
                    If user wants to add 'Dir1' layer into Layers. They should use 'Dir1' to componentType paramter.
                    Then the added_layer_index output the added layer's new index. It will return 1 for 'Dir1' index 
                    .Because the 'ClearCoat' will be index 0. 
                    
                    componentUniqueName parameter will return the unique name of 'Dir1':
                    'model2_'Varnished Cherry_Layer_262'. 
                    
                    You can also add more than one layers for same type. You can add 'Dir1' into ''Varnished Cherry'
                    again. The added_layer_index would return 2. The componentUniqueName parameter will return the 
                    unique name of new added 'Dir2' : 'model2_'Varnished Cherry_Layer_281'
                    
                
         Returns A tuple consisting of (componentUniqueName, added_layer_index). 
         - componentUniqueName is: str.
         - added_layer_index is: int.

        """
        pass
    def ExportToMDLFile(self, export_mdl_file_name: str) -> None:
        """
         Exports current material of material editor builder into a MDL file. 
        """
        pass
    def ExportToXMLFile(self, export_xml_file_name: str) -> None:
        """
         Exports current material of material editor builder into a XML file. 
        """
        pass
    def GetComponentInfo(self, componentName: str) -> Tuple[IrayPlusMaterialAttribute, List[str]]:
        """
         Get all the attribute name of a component. The string attribute name format should be the component
                    name. 
                    
                    Let material ''Varnished Cherry' for example:
                    
                    If user wants to get component's sub attribute names of 'Base' component. They should input 'Base' as 
                    componentName paramter.
                    Then the attribueObject output the pointer to the IrayPlusMatAttribute object of 'Base' component in
                    the hierarchy. The attrib_list will return array of all the attribute name of the 'Base' component like
                    [Base-Base Type, Base-Colour-Interface Type,...]
                    
                    If user wants to get layer's sub attribute names of 'ClearCoat'. They should use '0' as componentName paramter.
                    Then the attribueObject output the pointer to the IrayPlusMatAttribute object of 'ClearCoat' layer in
                    the hierarchy. The attrib_list will return array of all the attribute name of the 'ClearCoat' layer like
                    [model2_'Varnished Cherry_Layer_198-Layer Type, model2_'Varnished Cherry_Layer_198-Colour-Interface Type,...]
                    
                    NOTE:User use 'model2_'Varnished Cherry_Layer_198' as paramter name to get and set attribute can ONLY in same
                    session. 
                    User should NOT use name like 'ClearCoat' or 'model2_'Varnished Cherry_Layer_198' as name parameter. 
                    Instead they should use index as name. The index value of each Layers is same as name position in unique_name_list.
                    This is because the unique name for each layers would change between each session.
                    
                
         Returns A tuple consisting of (attribueObject, attrib_list). 
         - attribueObject is:  IrayPlusMaterialAttribute NXOpen.
         - attrib_list is: List[str].

        """
        pass
    def GetComponentParameter(self, attribueName: str) -> IrayPlusMaterialAttribute:
        """
         Gets single attribute object for specific fomatted attribute name 
                    The string attribute name format should be : 
                    "layer name-interface name-attribute name"
                    
                    Let material ''Varnished Cherry' for example:
                    
                    If user wants to get 'Base' component's attribueObject of 'Base-Colour-Colour'. They should input 
                    'Base-Colour-Colour' as componentName paramter.
                    Then the attribueObject output the pointer to the IrayPlusMatAttribute object of 'Base-Colour-Colour' 
                    component in the hierarchy. 
                    
                    If user wants to get layer's sub attribute of 'ClearCoat'. They should use index in componentName paramter:
                    'Layers-0-ReflectionColour-ColourOffset'
                    Then the attribueObject output the pointer to the IrayPlusMatAttribute object of 'ReflectionColour-ColourOffset' 
                    attribute of 'ClearCoat' layer in the hierarchy. 
                    
                    NOTE:User use 'model2_'Varnished Cherry_Layer_198' as paramter name to get and set attribute can ONLY in same
                    session. 
                    User should NOT use name like 'ClearCoat' or 'model2_'Varnished Cherry_Layer_198' as name parameter. 
                    Instead they should use index as name. The index value of each Layers is same as name position in unique_name_list.
                    This is because the unique name for each layers would change between each session.
                    
                
         Returns attribueObject ( IrayPlusMaterialAttribute NXOpen): .
        """
        pass
    def GetComponentParameterValue(self, attribueName: str) -> str:
        """
         Gets attribute's value as string for specific fomatted attribute name 
                    The string attribute name format should be : 
                    "layer name-interface name-attribute name"
                    
                    Let material ''Varnished Cherry' for example:
                    
                    If user wants to get 'Base' component's value of 'Base-Colour-Colour'. They should input 
                    'Base-Colour-Colour' as componentName paramter.
                    attribueValue parameter will return  the string for the value of 'Base-Colour-Colour': 
                    "0.000000000000000,1.000000000000000,1.000000000000000"
                    
                    If user wants to get layer's sub attribute of 'ClearCoat'. They should use index in componentName paramter:
                    'Layers-0-ReflectionColour-ColourOffset'
                    
                    attribueValue parameter will return the value of 'ClearCoat''s 'ReflectionColour-ColourOffset' as a string : 
                    "1.000000000000000,0.000000000000000,0.000000000000000"
                    
                    NOTE:User use 'model2_'Varnished Cherry_Layer_198' as paramter name to get and set attribute can ONLY in same
                    session. 
                    User should NOT use name like 'ClearCoat' or 'model2_'Varnished Cherry_Layer_198' as name parameter. 
                    Instead they should use index as name. The index value of each Layers is same as name position in unique_name_list.
                    This is because the unique name for each layers would change between each session.
                
         Returns attribueValue (str): .
        """
        pass
    def GetImageParameterFullPath(self, imageAttribueName: str) -> str:
        """
         To return the absolute path of specific image type parameter.  
                    The format of imageAttribueName  should be : 
                    "layer name-interface name-attribute name"
                    
                    Let material ''Varnished Cherry' for example:
                    
                    If user wants to get image's full path of 'Base-Colour-TextureSpace-Image'. User should input 
                    'Base-Colour-TextureSpace-Image' as imageAttribueName paramter.
                    imageFullPath parameter will return  the string of full path. 
                    
                    If user wants to get layer's sub attribute of 'ClearCoat'. They should use index in imageAttribueName paramter:
                    'Layers-0-TextureSpace-Image'
                    
                    NOTE:User use 'model2_'Varnished Cherry_Layer_198' as paramter name to get and set attribute can ONLY in same
                    session. 
                    User should NOT use name like 'ClearCoat' or 'model2_'Varnished Cherry_Layer_198' as name parameter. 
                    Instead they should use index as name. The index value of each Layers is same as name position in unique_name_list.
                    This is because the unique name for each layers would change between each session.
                    If the 
                
         Returns imageFullPath (str): .
        """
        pass
    def GetMaterialLayersInfo(self) -> Tuple[List[str], List[str]]:
        """
         Get all the components unique name and type name of this material.
                    The order in list have meanings. The Layers's components are put into the list first.
                    So the index of component in list are same of index in Layers.
                    Other Base, Global TextureSplace are insert into the list after Layer's components.
                    
                    Use system material 'Varnished Cherry' as example. Set attribueName paramter to ''Varnished Cherry'.
                    It will return 4 items in type_list:[ClearCoat,Base,Geometry,Global Texture Space] 
                    and 4 item in unique_name_list:[model2_'Varnished Cherry_Layer_198, Matte, BaseGeometry,Box].
                    
                    The type_list output the type for sublayer in Layers and name for Base,Geometry,Global Texture Space.
                    The unique_name_list output the unique name of each layers and types for Base,Geometry,Global Texture Space.
                    
                    When user use these name to get or set attribute for the specific components. They should use 
                    'Base' 'Geometry' 'Global Texture Space' for fixed components. But for components in Layers. 
                    
                    NOTE:User use 'model2_'Varnished Cherry_Layer_198' as paramter name to get and set attribute can ONLY in same
                    session. 
                    User should NOT use name like 'ClearCoat' or 'model2_'Varnished Cherry_Layer_198' as name parameter. 
                    Instead they should use index as name. The index value of each Layers is same as name position in unique_name_list.
                    This is because the unique name for each layers would change between each session.
                    
                    For example if user want to set or get the attribute of ClearCoat of material ''Varnished Cherry'. They should
                    use '0' as the paramter name to call GetComponentParameter or SetComponentParameter.
                    
                
         Returns A tuple consisting of (type_list, unique_name_list). 
         - type_list is: List[str].
         - unique_name_list is: List[str].

        """
        pass
    def MoveComponent(self, index: int, componentType: str, move_up: bool) -> None:
        """
         Moves a component of layers up and down of layers stack.
                
                    Let material ''Varnished Cherry' for example:
                    If use changed the material has two Layers: Dir1 and ClearCoat.
                    Then user wants to move 'Dir1' layer down in Layers. They should use 1 as index paramter.
                    
                    The parameter componentType should input the layer type of the layer that you want to move.
                    This make the deleting more type safe.
                    User should set 'Dir1' as componentType for this example.
                    
                    move_up parameter should be 'false' for this example.
                
        """
        pass
    def RemoveComponent(self, index: int, componentType: str) -> None:
        """
         Removes a component to layers for specific layer index
                
                    Let material ''Varnished Cherry' for example:
                    If use changed the material has two Layers: Dir1 and ClearCoat.
                    Then user wants to remove 'Dir1' layer from Layers. They should use 1 as index paramter.
                    
                    The parameter componentType should input the layer type of the layer that you want to remove.
                    This make the deleting more type safe.
                    User should set 'Dir1' as componentType for this example.
                
        """
        pass
    def SaveToSystemStudioMaterials(self, save_xml_file_name: str) -> None:
        """
         Saves the material to System Studio Materials which is a directory under 
                ugphotoIrayPlus_ug_canned_mattex. 
        """
        pass
    def SetComponentParameter(self, attribueName: str, attribueObject: IrayPlusMaterialAttribute) -> List[str]:
        """
         Sets attribute object for specific fomatted attribute name 
                    The string attribute name format should be : 
                    "layer name-interface name-attribute name"
                    
                    Let material ''Varnished Cherry' for example:
                    
                    If user wants to set 'Base' component's attribueObject of 'Base-Colour-Colour'. They should input 
                    'Base-Colour-Colour' as attribueName paramter.
                    The attribueObject point to the IrayPlusMatAttribute which should have modified value for Colour.
                     
                    
                    If user wants to set layer's sub attribute of 'ClearCoat'. They should use index in attribueName paramter:
                    'Layers-0-ReflectionColour-ColourOffset'
                    The attribueObject point to the IrayPlusMatAttribute which should have modified value for ColourOffset.
                    
                    
                    The changed_attrib parameter will return all the attributs names effected by current modification.
                    then user could use this to figure out what should to requery.
                    
                    If user use 'Base-Base Type' to change base type to 'Metal'. Then all the attribute name in 'Base' will
                    be listed in changed_attrib. Because the interface type change will cause the sub attributes been changed
                    either.
                    
                    NOTE:User use 'model2_'Varnished Cherry_Layer_198' as paramter name to get and set attribute can ONLY in same
                    session. 
                    User should NOT use name like 'ClearCoat' or 'model2_'Varnished Cherry_Layer_198' as name parameter. 
                    Instead they should use index as name. The index value of each Layers is same as name position in unique_name_list.
                    This is because the unique name for each layers would change between each session.
                
         Returns changed_attrib (List[str]): .
        """
        pass
    def SetComponentParameterValue(self, attribueName: str, attribueValue: str) -> List[str]:
        """
         Sets attribute value for specific fomatted attribute name 
                    The string attribute name format should be : 
                    "layer name-interface name-attribute name"
                    
                    Let material ''Varnished Cherry' for example:
                    
                    If user wants to set 'Base' component's value of 'Base-Colour-Colour'. They should input 
                    'Base-Colour-Colour' as attribueName paramter.
                    attribueValue parameter will return  the string for the value of 'Base-Colour-Colour': 
                    "0.000000000000000,1.000000000000000,1.000000000000000"
                     
                    
                    If user wants to set layer's sub attribute value of 'ClearCoat'. They should use index in attribueName paramter:
                    'Layers-0-ReflectionColour-ColourOffset'
                     attribueValue parameter will return  the string for the value of 'ReflectionColour-ColourOffset' in 'ClearCoat': 
                    "1.000000000000000,0.000000000000000,0.000000000000000"
                    
                    The changed_attrib parameter will return all the attributs names effected by current modification.
                    then user could use this to figure out what should to requery.
                    
                    If user use 'Base-Base Type' to change base type to 'Metal'. Then all the attribute name in 'Base' will
                    be listed in changed_attrib. Because the interface type change will cause the sub attributes been changed
                    either.
                    
                    NOTE:User use 'model2_'Varnished Cherry_Layer_198' as paramter name to get and set attribute can ONLY in same
                    session. 
                    User should NOT use name like 'ClearCoat' or 'model2_'Varnished Cherry_Layer_198' as name parameter. 
                    Instead they should use index as name. The index value of each Layers is same as name position in unique_name_list.
                    This is because the unique name for each layers would change between each session.
                
         Returns changed_attrib (List[str]): .
        """
        pass
import NXOpen
class IrayPlusSimpleMaterialEditorBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Display.IrayPlusSimpleMaterialEditorBuilder 
        This class is restricted to being called from a program running during an 
        Interactive NX session.  If run from a non-interactive session it will 
        return .
    """
    class TextureSpace(Enum):
        """
        Members Include: 
         |Box| 
         |Planar| 
         |Cylindrical| 
         |Spherical| 
         |UVMap| 

        """
        Box: int
        Planar: int
        Cylindrical: int
        Spherical: int
        UVMap: int
        @staticmethod
        def ValueOf(value: int) -> IrayPlusSimpleMaterialEditorBuilder.TextureSpace:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AspectRatio(self) -> float:
        """
        Getter for property: (float) AspectRatio
         Returns the aspect ratio   
            
         
        """
        pass
    @AspectRatio.setter
    def AspectRatio(self, aspectRatio: float):
        """
        Setter for property: (float) AspectRatio
         Returns the aspect ratio   
            
         
        """
        pass
    @property
    def FileBrowser(self) -> str:
        """
        Getter for property: (str) FileBrowser
         Returns the file browser   
            
         
        """
        pass
    @FileBrowser.setter
    def FileBrowser(self, filename: str):
        """
        Setter for property: (str) FileBrowser
         Returns the file browser   
            
         
        """
        pass
    @property
    def LatitudeScale(self) -> float:
        """
        Getter for property: (float) LatitudeScale
         Returns the latitude scale   
            
         
        """
        pass
    @LatitudeScale.setter
    def LatitudeScale(self, latitudeScale: float):
        """
        Setter for property: (float) LatitudeScale
         Returns the latitude scale   
            
         
        """
        pass
    @property
    def LongitudeScale(self) -> float:
        """
        Getter for property: (float) LongitudeScale
         Returns the longitude scale   
            
         
        """
        pass
    @LongitudeScale.setter
    def LongitudeScale(self, longitudeScale: float):
        """
        Setter for property: (float) LongitudeScale
         Returns the longitude scale   
            
         
        """
        pass
    @property
    def NameString(self) -> str:
        """
        Getter for property: (str) NameString
         Returns the name string   
            
         
        """
        pass
    @NameString.setter
    def NameString(self, nameString: str):
        """
        Setter for property: (str) NameString
         Returns the name string   
            
         
        """
        pass
    @property
    def NormalVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) NormalVector
         Returns the normal vector   
            
         
        """
        pass
    @NormalVector.setter
    def NormalVector(self, normalVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) NormalVector
         Returns the normal vector   
            
         
        """
        pass
    @property
    def Scale(self) -> float:
        """
        Getter for property: (float) Scale
         Returns the scale   
            
         
        """
        pass
    @Scale.setter
    def Scale(self, scale: float):
        """
        Setter for property: (float) Scale
         Returns the scale   
            
         
        """
        pass
    @property
    def TextureSpaceEnum(self) -> IrayPlusSimpleMaterialEditorBuilder.TextureSpace:
        """
        Getter for property: ( IrayPlusSimpleMaterialEditorBuilder.TextureSpace NXOpen) TextureSpaceEnum
         Returns the texture space enum   
            
         
        """
        pass
    @TextureSpaceEnum.setter
    def TextureSpaceEnum(self, textureSpaceEnum: IrayPlusSimpleMaterialEditorBuilder.TextureSpace):
        """
        Setter for property: ( IrayPlusSimpleMaterialEditorBuilder.TextureSpace NXOpen) TextureSpaceEnum
         Returns the texture space enum   
            
         
        """
        pass
    @property
    def TexturedToggle(self) -> bool:
        """
        Getter for property: (bool) TexturedToggle
         Returns the textured toggle   
            
         
        """
        pass
    @TexturedToggle.setter
    def TexturedToggle(self, texturedToggle: bool):
        """
        Setter for property: (bool) TexturedToggle
         Returns the textured toggle   
            
         
        """
        pass
    @property
    def UScale(self) -> float:
        """
        Getter for property: (float) UScale
         Returns the u scale   
            
         
        """
        pass
    @UScale.setter
    def UScale(self, uScale: float):
        """
        Setter for property: (float) UScale
         Returns the u scale   
            
         
        """
        pass
    @property
    def UpVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) UpVector
         Returns the up vector   
            
         
        """
        pass
    @UpVector.setter
    def UpVector(self, upVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) UpVector
         Returns the up vector   
            
         
        """
        pass
    @property
    def VScale(self) -> float:
        """
        Getter for property: (float) VScale
         Returns the v scale   
            
         
        """
        pass
    @VScale.setter
    def VScale(self, vScale: float):
        """
        Setter for property: (float) VScale
         Returns the v scale   
            
         
        """
        pass
    def ExportXMLButton(self) -> None:
        """
         To export to a XML file 
        """
        pass
    def GetColorPicker(self) -> List[float]:
        """
         Returns the color picker 
         Returns colorPicker (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def SaveMaterialsButton(self) -> None:
        """
         To save to System Studio Materials 
        """
        pass
    def SetColorPicker(self, colorPicker: List[float]) -> None:
        """
         Sets the color picker 
        """
        pass
import NXOpen
class IrayPlusStudioAnimationBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Display.IrayPlusStudioAnimationBuilder.
    Ray Traced Studio Save Animation gives control to create high end rendered animations authored
    in NX Animation Designer.
    This class is restricted to being called from a program running during an
    Interactive NX session.  If run from a non-interactive session it will
    return .
    """
    class AnimationAutoCompletionType(Enum):
        """
        Members Include: 
         |Complex| the automatic completion criteria for a complex scene with numerous emissive materials, reflective materials, and shadows 
         |Normal| the automatic completion criteria for a normal scene with a balanced number of emissive materials, reflective materials, and shadows
         |Simple| the automatic completion criteria for a simple scene with a limited number of emissive materials, reflective materials, and shadows
         |NotSet| the option to apply no automatic completion criteria
         |Custom| the automatic completion criteria to specify a custom threshold for automatically detecting the completion of an image 

        """
        Complex: int
        Normal: int
        Simple: int
        NotSet: int
        Custom: int
        @staticmethod
        def ValueOf(value: int) -> IrayPlusStudioAnimationBuilder.AnimationAutoCompletionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class AnimationFileOutputType(Enum):
        """
        Members Include: 
         |MicrosoftAVI| a Microsoft AVI type movie file
         |SeriesofPNG| a series of PNG type images 
         |SeriesofJPG| a series of JPG type images 
         |SeriesofTIF| a series of TIF type images 

        """
        MicrosoftAVI: int
        SeriesofPNG: int
        SeriesofJPG: int
        SeriesofTIF: int
        @staticmethod
        def ValueOf(value: int) -> IrayPlusStudioAnimationBuilder.AnimationFileOutputType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class AnimationProcessingType(Enum):
        """
        Members Include: 
         |Interactive| the animation render is done via Ray Traced Studio in the current NX session
         |Offline| the animation render is submitted as a batch job to a remote server and rendered offline

        """
        Interactive: int
        Offline: int
        @staticmethod
        def ValueOf(value: int) -> IrayPlusStudioAnimationBuilder.AnimationProcessingType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class AnimationRenderDurationType(Enum):
        """
        Members Include: 
         |IterationsperFrame| the number of iterations specified to the renderer to reach for each animation frame 
         |TimeperFrame| the amount of time specified to the renderer to reach for each animation frame 
         |AutoComplete| the auto Complete criteria uses Iray+ based progressive completion criteria to determine render completion 
         |TimeLimitedAutoComplete| the auto Complete criteria uses Iray+ based progressive completion criteria to determine render completion and a designated time limit 

        """
        IterationsperFrame: int
        TimeperFrame: int
        AutoComplete: int
        TimeLimitedAutoComplete: int
        @staticmethod
        def ValueOf(value: int) -> IrayPlusStudioAnimationBuilder.AnimationRenderDurationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class AnimationRenderQualityType(Enum):
        """
        Members Include: 
         |Photoreal| the Ray Traced Studio Photoreal rendering quality 
         |QualityInteractive| the Ray Traced Studio Quality Interactive rendering quality
         |FastInteractive| the Ray Traced Studio Fast Interactive rendering quality 

        """
        Photoreal: int
        QualityInteractive: int
        FastInteractive: int
        @staticmethod
        def ValueOf(value: int) -> IrayPlusStudioAnimationBuilder.AnimationRenderQualityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class AnimationResolutionType(Enum):
        """
        Members Include: 
         |RenderWindow| the resolution derived from render window 
         |UserDefined| a User Defined resolution 

        """
        RenderWindow: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> IrayPlusStudioAnimationBuilder.AnimationResolutionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class AnimationTimeRangeType(Enum):
        """
        Members Include: 
         |EntireTimeline| the entire timeline of the animation 
         |UserDefined| the user defined range of time of the animation 

        """
        EntireTimeline: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> IrayPlusStudioAnimationBuilder.AnimationTimeRangeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FramesPerSecondRateType(Enum):
        """
        Members Include: 
         |Fps15|  15 frames per second 
         |Fps24|  24 frames per second 
         |Fps30|  30 frames per second 
         |Fps60|  60 frames per second 
         |Fps120|  120 frames per second 
         |UserDefined| a user defined frame rate 

        """
        Fps15: int
        Fps24: int
        Fps30: int
        Fps60: int
        Fps120: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> IrayPlusStudioAnimationBuilder.FramesPerSecondRateType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AnimationCustomEndTime(self) -> float:
        """
        Getter for property: (float) AnimationCustomEndTime
         Returnsthe user-defined end time of the animation.  
           The end time must be greater than 0.0 and
                also start at least 0.2 seconds after the user-defined start time   
         
        """
        pass
    @AnimationCustomEndTime.setter
    def AnimationCustomEndTime(self, animationCustomEndTime: float):
        """
        Setter for property: (float) AnimationCustomEndTime
         Returnsthe user-defined end time of the animation.  
           The end time must be greater than 0.0 and
                also start at least 0.2 seconds after the user-defined start time   
         
        """
        pass
    @property
    def AnimationCustomHeight(self) -> int:
        """
        Getter for property: (int) AnimationCustomHeight
         Returnsthe custom height of the animation   
            
         
        """
        pass
    @AnimationCustomHeight.setter
    def AnimationCustomHeight(self, animationCustomHeight: int):
        """
        Setter for property: (int) AnimationCustomHeight
         Returnsthe custom height of the animation   
            
         
        """
        pass
    @property
    def AnimationCustomStartTime(self) -> float:
        """
        Getter for property: (float) AnimationCustomStartTime
         Returnsthe user-defined start time of the animation.  
           The start time must be greater than 0.0
                and also start earlier than the user-defined end time.  
         
        """
        pass
    @AnimationCustomStartTime.setter
    def AnimationCustomStartTime(self, animationCustomStartTime: float):
        """
        Setter for property: (float) AnimationCustomStartTime
         Returnsthe user-defined start time of the animation.  
           The start time must be greater than 0.0
                and also start earlier than the user-defined end time.  
         
        """
        pass
    @property
    def AnimationCustomWidth(self) -> int:
        """
        Getter for property: (int) AnimationCustomWidth
         Returnsthe custom width of the animation   
            
         
        """
        pass
    @AnimationCustomWidth.setter
    def AnimationCustomWidth(self, animationCustomWidth: int):
        """
        Setter for property: (int) AnimationCustomWidth
         Returnsthe custom width of the animation   
            
         
        """
        pass
    @property
    def AnimationFileOutput(self) -> IrayPlusStudioAnimationBuilder.AnimationFileOutputType:
        """
        Getter for property: ( IrayPlusStudioAnimationBuilder.AnimationFileOutputType NXOpen) AnimationFileOutput
         Returnsthe output type of the animation   
            
         
        """
        pass
    @AnimationFileOutput.setter
    def AnimationFileOutput(self, animationFileOutput: IrayPlusStudioAnimationBuilder.AnimationFileOutputType):
        """
        Setter for property: ( IrayPlusStudioAnimationBuilder.AnimationFileOutputType NXOpen) AnimationFileOutput
         Returnsthe output type of the animation   
            
         
        """
        pass
    @property
    def AnimationFrameNumOfIterations(self) -> int:
        """
        Getter for property: (int) AnimationFrameNumOfIterations
         Returnsthe number limit of iterations specified to the renderer to resolve the animation frame.  
           The number
                limit of iterations must be greater than or equal to 20 iterations.  
         
        """
        pass
    @AnimationFrameNumOfIterations.setter
    def AnimationFrameNumOfIterations(self, animationFrameNumOfIterations: int):
        """
        Setter for property: (int) AnimationFrameNumOfIterations
         Returnsthe number limit of iterations specified to the renderer to resolve the animation frame.  
           The number
                limit of iterations must be greater than or equal to 20 iterations.  
         
        """
        pass
    @property
    def AnimationFrameTimeLimit(self) -> NXOpen.DateBuilder:
        """
        Getter for property: ( NXOpen.DateBuilder) AnimationFrameTimeLimit
         Returnsthe time limit specified to the renderer to resolve the animation frame   
            
         
        """
        pass
    @property
    def AnimationResolution(self) -> IrayPlusStudioAnimationBuilder.AnimationResolutionType:
        """
        Getter for property: ( IrayPlusStudioAnimationBuilder.AnimationResolutionType NXOpen) AnimationResolution
         Returnsthe animation resolution   
            
         
        """
        pass
    @AnimationResolution.setter
    def AnimationResolution(self, animationResolution: IrayPlusStudioAnimationBuilder.AnimationResolutionType):
        """
        Setter for property: ( IrayPlusStudioAnimationBuilder.AnimationResolutionType NXOpen) AnimationResolution
         Returnsthe animation resolution   
            
         
        """
        pass
    @property
    def AnimationSolution(self) -> str:
        """
        Getter for property: (str) AnimationSolution
         Returnsthe selected Animation Designer solution   
            
         
        """
        pass
    @AnimationSolution.setter
    def AnimationSolution(self, animationSolution: str):
        """
        Setter for property: (str) AnimationSolution
         Returnsthe selected Animation Designer solution   
            
         
        """
        pass
    @property
    def AutoCompletionCustomPixelRatio(self) -> float:
        """
        Getter for property: (float) AutoCompletionCustomPixelRatio
         Returnsthe automatic completion pixel ratio of the animation frame.  
           This controls the number of pixels as a 
                "ratio of the total pixel count that must converge to the Quality Completion Factor."  
         
        """
        pass
    @AutoCompletionCustomPixelRatio.setter
    def AutoCompletionCustomPixelRatio(self, autoCompletionCustomPixelRatio: float):
        """
        Setter for property: (float) AutoCompletionCustomPixelRatio
         Returnsthe automatic completion pixel ratio of the animation frame.  
           This controls the number of pixels as a 
                "ratio of the total pixel count that must converge to the Quality Completion Factor."  
         
        """
        pass
    @property
    def AutoCompletionCustomQualityFactor(self) -> float:
        """
        Getter for property: (float) AutoCompletionCustomQualityFactor
         Returnsthe automatic completion quality factor of the animation frame.  
           This control
                defines a quality factor relative to the scene. The quality factor has a linear
                scaling effect. For example, a quality factor set to 2.0 will roughly take twice as
                long to render a scene with an assigned quality factor of 1.0.  
         
        """
        pass
    @AutoCompletionCustomQualityFactor.setter
    def AutoCompletionCustomQualityFactor(self, autoCompletionCustomQualityFactor: float):
        """
        Setter for property: (float) AutoCompletionCustomQualityFactor
         Returnsthe automatic completion quality factor of the animation frame.  
           This control
                defines a quality factor relative to the scene. The quality factor has a linear
                scaling effect. For example, a quality factor set to 2.0 will roughly take twice as
                long to render a scene with an assigned quality factor of 1.0.  
         
        """
        pass
    @property
    def AutoCompletionType(self) -> IrayPlusStudioAnimationBuilder.AnimationAutoCompletionType:
        """
        Getter for property: ( IrayPlusStudioAnimationBuilder.AnimationAutoCompletionType NXOpen) AutoCompletionType
         Returnsthe automatic completion type for the animation   
            
         
        """
        pass
    @AutoCompletionType.setter
    def AutoCompletionType(self, autoCompletionType: IrayPlusStudioAnimationBuilder.AnimationAutoCompletionType):
        """
        Setter for property: ( IrayPlusStudioAnimationBuilder.AnimationAutoCompletionType NXOpen) AutoCompletionType
         Returnsthe automatic completion type for the animation   
            
         
        """
        pass
    @property
    def Caustics(self) -> bool:
        """
        Getter for property: (bool) Caustics
         Returnsthe use of caustics during the animation render, only available when the render quality is set to Photoreal   
            
         
        """
        pass
    @Caustics.setter
    def Caustics(self, caustics: bool):
        """
        Setter for property: (bool) Caustics
         Returnsthe use of caustics during the animation render, only available when the render quality is set to Photoreal   
            
         
        """
        pass
    @property
    def CustomFrameRate(self) -> int:
        """
        Getter for property: (int) CustomFrameRate
         Returnsthe custom frames per second rate for the animation   
            
         
        """
        pass
    @CustomFrameRate.setter
    def CustomFrameRate(self, customFrameRate: int):
        """
        Setter for property: (int) CustomFrameRate
         Returnsthe custom frames per second rate for the animation   
            
         
        """
        pass
    @property
    def Denoiser(self) -> bool:
        """
        Getter for property: (bool) Denoiser
         Returnsthe use of the Ray Traced Studio Denoiser during animation render   
            
         
        """
        pass
    @Denoiser.setter
    def Denoiser(self, denoiser: bool):
        """
        Setter for property: (bool) Denoiser
         Returnsthe use of the Ray Traced Studio Denoiser during animation render   
            
         
        """
        pass
    @property
    def FileInput(self) -> str:
        """
        Getter for property: (str) FileInput
         Returnsthe location where to save the animation and the file name, only available when the Output type is Microsoft AVI movie file   
            
         
        """
        pass
    @FileInput.setter
    def FileInput(self, fileInput: str):
        """
        Setter for property: (str) FileInput
         Returnsthe location where to save the animation and the file name, only available when the Output type is Microsoft AVI movie file   
            
         
        """
        pass
    @property
    def FolderInput(self) -> str:
        """
        Getter for property: (str) FolderInput
         Returnsthe directory location where to save the animation output, only available when a series of images is the Output type   
            
         
        """
        pass
    @FolderInput.setter
    def FolderInput(self, folderOutput: str):
        """
        Setter for property: (str) FolderInput
         Returnsthe directory location where to save the animation output, only available when a series of images is the Output type   
            
         
        """
        pass
    @property
    def FrameRate(self) -> IrayPlusStudioAnimationBuilder.FramesPerSecondRateType:
        """
        Getter for property: ( IrayPlusStudioAnimationBuilder.FramesPerSecondRateType NXOpen) FrameRate
         Returnsthe frames per second rate for the animation   
            
         
        """
        pass
    @FrameRate.setter
    def FrameRate(self, frameRate: IrayPlusStudioAnimationBuilder.FramesPerSecondRateType):
        """
        Setter for property: ( IrayPlusStudioAnimationBuilder.FramesPerSecondRateType NXOpen) FrameRate
         Returnsthe frames per second rate for the animation   
            
         
        """
        pass
    @property
    def LockAspectRatio(self) -> bool:
        """
        Getter for property: (bool) LockAspectRatio
         Returns the lock to the ratio for a custom animation resolution ratio   
            
         
        """
        pass
    @LockAspectRatio.setter
    def LockAspectRatio(self, lockAspectRatio: bool):
        """
        Setter for property: (bool) LockAspectRatio
         Returns the lock to the ratio for a custom animation resolution ratio   
            
         
        """
        pass
    @property
    def ProcessingType(self) -> IrayPlusStudioAnimationBuilder.AnimationProcessingType:
        """
        Getter for property: ( IrayPlusStudioAnimationBuilder.AnimationProcessingType NXOpen) ProcessingType
         Returnsthe processing type of the animation   
            
         
        """
        pass
    @ProcessingType.setter
    def ProcessingType(self, processingType: IrayPlusStudioAnimationBuilder.AnimationProcessingType):
        """
        Setter for property: ( IrayPlusStudioAnimationBuilder.AnimationProcessingType NXOpen) ProcessingType
         Returnsthe processing type of the animation   
            
         
        """
        pass
    @property
    def RemoteRender(self) -> bool:
        """
        Getter for property: (bool) RemoteRender
         Returnsthe use of remote rendering for the animation, only available during Interactive animation processing  
            
         
        """
        pass
    @RemoteRender.setter
    def RemoteRender(self, remoteRender: bool):
        """
        Setter for property: (bool) RemoteRender
         Returnsthe use of remote rendering for the animation, only available during Interactive animation processing  
            
         
        """
        pass
    @property
    def RenderDuration(self) -> IrayPlusStudioAnimationBuilder.AnimationRenderDurationType:
        """
        Getter for property: ( IrayPlusStudioAnimationBuilder.AnimationRenderDurationType NXOpen) RenderDuration
         Returnsthe render duration of each frame in the animation   
            
         
        """
        pass
    @RenderDuration.setter
    def RenderDuration(self, renderDuration: IrayPlusStudioAnimationBuilder.AnimationRenderDurationType):
        """
        Setter for property: ( IrayPlusStudioAnimationBuilder.AnimationRenderDurationType NXOpen) RenderDuration
         Returnsthe render duration of each frame in the animation   
            
         
        """
        pass
    @property
    def RenderQuality(self) -> IrayPlusStudioAnimationBuilder.AnimationRenderQualityType:
        """
        Getter for property: ( IrayPlusStudioAnimationBuilder.AnimationRenderQualityType NXOpen) RenderQuality
         Returnsthe level of rendering quality for the animation   
            
         
        """
        pass
    @RenderQuality.setter
    def RenderQuality(self, renderQuality: IrayPlusStudioAnimationBuilder.AnimationRenderQualityType):
        """
        Setter for property: ( IrayPlusStudioAnimationBuilder.AnimationRenderQualityType NXOpen) RenderQuality
         Returnsthe level of rendering quality for the animation   
            
         
        """
        pass
    @property
    def ScheduledTaskName(self) -> str:
        """
        Getter for property: (str) ScheduledTaskName
         Returns the scheduled animation render job name, only available for animations processed offline   
            
         
        """
        pass
    @ScheduledTaskName.setter
    def ScheduledTaskName(self, scheduledTaskName: str):
        """
        Setter for property: (str) ScheduledTaskName
         Returns the scheduled animation render job name, only available for animations processed offline   
            
         
        """
        pass
    @property
    def ScheduledTaskPriority(self) -> int:
        """
        Getter for property: (int) ScheduledTaskPriority
         Returns the priority of the animation on an offline renderer, only available for animations processed offline.  
          
                The range of priority is between 1 and 100, with 1 being the highest priority and 100 being the lowest priority.  
         
        """
        pass
    @ScheduledTaskPriority.setter
    def ScheduledTaskPriority(self, scheduledTaskPriority: int):
        """
        Setter for property: (int) ScheduledTaskPriority
         Returns the priority of the animation on an offline renderer, only available for animations processed offline.  
          
                The range of priority is between 1 and 100, with 1 being the highest priority and 100 being the lowest priority.  
         
        """
        pass
    @property
    def TimeRange(self) -> IrayPlusStudioAnimationBuilder.AnimationTimeRangeType:
        """
        Getter for property: ( IrayPlusStudioAnimationBuilder.AnimationTimeRangeType NXOpen) TimeRange
         Returnsthe Time Range for the animation   
            
         
        """
        pass
    @TimeRange.setter
    def TimeRange(self, timeRange: IrayPlusStudioAnimationBuilder.AnimationTimeRangeType):
        """
        Setter for property: ( IrayPlusStudioAnimationBuilder.AnimationTimeRangeType NXOpen) TimeRange
         Returnsthe Time Range for the animation   
            
         
        """
        pass
import NXOpen
class IRayPlusStudioEditorBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Display.IRayPlusStudioEditorBuilder.
    Ray Traced Studio Editor controls display and output of CPU-based real-time ray tracing.
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return .
    """
    class DynamicIRayPlusStudioRenderModeType(Enum):
        """
        Members Include: 
         |Photoreal|  Very good ray traced display quality when dynamic interaction stops 
         |QualityInteractive|  Good ray traced display quality with good performance when dynamic interaction stops 
         |FastInteractive|  The fastest ray traced display performance with preview quality when dynamic interaction stops 

        """
        Photoreal: int
        QualityInteractive: int
        FastInteractive: int
        @staticmethod
        def ValueOf(value: int) -> IRayPlusStudioEditorBuilder.DynamicIRayPlusStudioRenderModeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class IRayPlusStudioAutoCompletionType(Enum):
        """
        Members Include: 
         |Simple| the automatic completion criteria for a simple scene with a limited number of emissive materials, reflective materials, and shadows
         |Normal| the automatic completion criteria for a normal scene with a balanced number of emissive materials, reflective materials, and shadows
         |Complex| the automatic completion criteria for a complex scene with numerous emissive materials, reflective materials, and shadows 
         |NotSet| the option to apply no automatic completion criteria
         |Custom| the automatic completion criteria to specify a custom threshold for automatically detecting the completion of an image 

        """
        Simple: int
        Normal: int
        Complex: int
        NotSet: int
        Custom: int
        @staticmethod
        def ValueOf(value: int) -> IRayPlusStudioEditorBuilder.IRayPlusStudioAutoCompletionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class IRayPlusStudioLensType(Enum):
        """
        Members Include: 
         |Monospherical|  Mono Spherical 
         |Stereospherical|  Stereo Spherical 

        """
        Monospherical: int
        Stereospherical: int
        @staticmethod
        def ValueOf(value: int) -> IRayPlusStudioEditorBuilder.IRayPlusStudioLensType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class IRayPlusStudioRemoteRenderFormatType(Enum):
        """
        Members Include: 
         |H264| 
         |Lossless| 
         |Png| 
         |Jpeg| 

        """
        H264: int
        Lossless: int
        Png: int
        Jpeg: int
        @staticmethod
        def ValueOf(value: int) -> IRayPlusStudioEditorBuilder.IRayPlusStudioRemoteRenderFormatType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class IRayPlusStudioRemoteRenderType(Enum):
        """
        Members Include: 
         |Cluster|  Network Cluster 
         |Vca|  VCA 
         |SecuredCluster|  Secured Network Cluster

        """
        Cluster: int
        Vca: int
        SecuredCluster: int
        @staticmethod
        def ValueOf(value: int) -> IRayPlusStudioEditorBuilder.IRayPlusStudioRemoteRenderType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class IRayPlusStudioRemoteRenderVideoType(Enum):
        """
        Members Include: 
         |Streaming| 
         |Synchronous| 

        """
        Streaming: int
        Synchronous: int
        @staticmethod
        def ValueOf(value: int) -> IRayPlusStudioEditorBuilder.IRayPlusStudioRemoteRenderVideoType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class IRayPlusStudioStaticImageFileFormatType(Enum):
        """
        Members Include: 
         |Tif|  Tagged Image File Format (TIFF) file format 
         |Png|  Portable Network Graphic (PNG) file format 
         |Jpg|  Joint Photographic Experts Group (JPEG) file format 

        """
        Tif: int
        Png: int
        Jpg: int
        @staticmethod
        def ValueOf(value: int) -> IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageFileFormatType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class IRayPlusStudioStaticImageOrientationType(Enum):
        """
        Members Include: 
         |Landscape|  static image orientation where width is greater than height 
         |Portrait|  static image orientation where height is greater than width 

        """
        Landscape: int
        Portrait: int
        @staticmethod
        def ValueOf(value: int) -> IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageOrientationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class IRayPlusStudioStaticImageResolutionType(Enum):
        """
        Members Include: 
         |High|  static image output resolution of 300 DPI (dots per inch) 
         |Medium|  static image output resolution of 150 DPI (dots per inch) 
         |Low|  static image output resolution of 72 DPI (dots per inch) 
         |UserDefined|  user specified image output resolution in DPI (dots per inch) 

        """
        High: int
        Medium: int
        Low: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageResolutionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class IRayPlusStudioStaticImageSizeType(Enum):
        """
        Members Include: 
         |RenderWindow|  Ray Traced Studio window size used for static image output 
         |UserDefined|  user specified size for static image output 

        """
        RenderWindow: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageSizeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class IRayPlusStudioStaticImageUnitsType(Enum):
        """
        Members Include: 
         |Pixels|  static image size specified in pixel 
         |Millimeters|  static image size specified in millimeters 
         |Inches|  static image size specified in inches 

        """
        Pixels: int
        Millimeters: int
        Inches: int
        @staticmethod
        def ValueOf(value: int) -> IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageUnitsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class IRayPlusStudioStereoLayoutType(Enum):
        """
        Members Include: 
         |TopBottom|  Top-Bottom 
         |SideBySide|  Side-by-Side 

        """
        TopBottom: int
        SideBySide: int
        @staticmethod
        def ValueOf(value: int) -> IRayPlusStudioEditorBuilder.IRayPlusStudioStereoLayoutType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StaticRenderDurationType(Enum):
        """
        Members Include: 
         |NumberOfIterations| the number of iterations specified to the renderer to the static render 
         |TimeLimit| the amount of time specified to the renderer to reach for the static render 
         |AutoComplete| the auto Complete criteria uses Iray+ based progressive completion criteria to determine render completion 
         |TimeLimitedAutoComplete| the auto Complete criteria uses Iray+ based progressive completion criteria to determine render completion and a designated time limit 

        """
        NumberOfIterations: int
        TimeLimit: int
        AutoComplete: int
        TimeLimitedAutoComplete: int
        @staticmethod
        def ValueOf(value: int) -> IRayPlusStudioEditorBuilder.StaticRenderDurationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AutoCompletionCustomPixelRatio(self) -> float:
        """
        Getter for property: (float) AutoCompletionCustomPixelRatio
         Returns the Ray Traced Studio display static render auto-completion custom pixel ratio.  
           This controls
                "the number of pixels as a ratio of the total pixel count that must converge to the Quality Completion Factor."  
         
        """
        pass
    @AutoCompletionCustomPixelRatio.setter
    def AutoCompletionCustomPixelRatio(self, autoCompletionCustomPixelRatio: float):
        """
        Setter for property: (float) AutoCompletionCustomPixelRatio
         Returns the Ray Traced Studio display static render auto-completion custom pixel ratio.  
           This controls
                "the number of pixels as a ratio of the total pixel count that must converge to the Quality Completion Factor."  
         
        """
        pass
    @property
    def AutoCompletionCustomQualityFactor(self) -> float:
        """
        Getter for property: (float) AutoCompletionCustomQualityFactor
         Returns the Ray Traced Studio display static render auto-completion custom quality factor.  
           This control
                defines a quality factor relative to the scene. The quality factor has a linear
                scaling effect. For example, a quality factor set to 2.0 will roughly take twice as
                long to render a scene with an assigned quality factor of 1.0.  
         
        """
        pass
    @AutoCompletionCustomQualityFactor.setter
    def AutoCompletionCustomQualityFactor(self, autoCompletionCustomQualityFactor: float):
        """
        Setter for property: (float) AutoCompletionCustomQualityFactor
         Returns the Ray Traced Studio display static render auto-completion custom quality factor.  
           This control
                defines a quality factor relative to the scene. The quality factor has a linear
                scaling effect. For example, a quality factor set to 2.0 will roughly take twice as
                long to render a scene with an assigned quality factor of 1.0.  
         
        """
        pass
    @property
    def DynamicIRayPlusCaustics(self) -> bool:
        """
        Getter for property: (bool) DynamicIRayPlusCaustics
         Returns the Ray Traced Studio dynamic antialiasing quality when dynamic interaction stops   
            
         
        """
        pass
    @DynamicIRayPlusCaustics.setter
    def DynamicIRayPlusCaustics(self, dynamicIRayPlusCaustics: bool):
        """
        Setter for property: (bool) DynamicIRayPlusCaustics
         Returns the Ray Traced Studio dynamic antialiasing quality when dynamic interaction stops   
            
         
        """
        pass
    @property
    def DynamicIRayPlusStudioRenderMode(self) -> IRayPlusStudioEditorBuilder.DynamicIRayPlusStudioRenderModeType:
        """
        Getter for property: ( IRayPlusStudioEditorBuilder.DynamicIRayPlusStudioRenderModeType NXOpen) DynamicIRayPlusStudioRenderMode
         Returns the Ray Traced Studio dynamic display rendering mode   
            
         
        """
        pass
    @DynamicIRayPlusStudioRenderMode.setter
    def DynamicIRayPlusStudioRenderMode(self, dynamicIRayPlusStudioRenderMode: IRayPlusStudioEditorBuilder.DynamicIRayPlusStudioRenderModeType):
        """
        Setter for property: ( IRayPlusStudioEditorBuilder.DynamicIRayPlusStudioRenderModeType NXOpen) DynamicIRayPlusStudioRenderMode
         Returns the Ray Traced Studio dynamic display rendering mode   
            
         
        """
        pass
    @property
    def DynamicIRayPlusStudioTime(self) -> NXOpen.DateBuilder:
        """
        Getter for property: ( NXOpen.DateBuilder) DynamicIRayPlusStudioTime
         Returns the Ray Traced Studio dynamic display time-based rendering mode timer (read only)   
            
         
        """
        pass
    @property
    def EyeSeparation(self) -> float:
        """
        Getter for property: (float) EyeSeparation
         Returns the Ray Traced Studio display eye separation distance to use if rendering a stereo image   
            
         
        """
        pass
    @EyeSeparation.setter
    def EyeSeparation(self, eyeSeparation: float):
        """
        Setter for property: (float) EyeSeparation
         Returns the Ray Traced Studio display eye separation distance to use if rendering a stereo image   
            
         
        """
        pass
    @property
    def IRayPlusStudioDenoiserToggle(self) -> bool:
        """
        Getter for property: (bool) IRayPlusStudioDenoiserToggle
         Returns the Ray Traced Studio denoiser   
            
         
        """
        pass
    @IRayPlusStudioDenoiserToggle.setter
    def IRayPlusStudioDenoiserToggle(self, iRayPlusStudioDenoiserToggle: bool):
        """
        Setter for property: (bool) IRayPlusStudioDenoiserToggle
         Returns the Ray Traced Studio denoiser   
            
         
        """
        pass
    @property
    def IRayPlusStudioStaticImageDotsPerInch(self) -> int:
        """
        Getter for property: (int) IRayPlusStudioStaticImageDotsPerInch
         Returns the Ray Traced Studio static image dots per inch (DPI)   
            
         
        """
        pass
    @IRayPlusStudioStaticImageDotsPerInch.setter
    def IRayPlusStudioStaticImageDotsPerInch(self, iRayPlusStudioStaticImageDotsPerInch: int):
        """
        Setter for property: (int) IRayPlusStudioStaticImageDotsPerInch
         Returns the Ray Traced Studio static image dots per inch (DPI)   
            
         
        """
        pass
    @property
    def IRayPlusStudioStaticImageDoubleHeight(self) -> float:
        """
        Getter for property: (float) IRayPlusStudioStaticImageDoubleHeight
         Returns the Ray Traced Studio static image height   
            
         
        """
        pass
    @IRayPlusStudioStaticImageDoubleHeight.setter
    def IRayPlusStudioStaticImageDoubleHeight(self, iRayPlusStudioStaticImageDoubleHeight: float):
        """
        Setter for property: (float) IRayPlusStudioStaticImageDoubleHeight
         Returns the Ray Traced Studio static image height   
            
         
        """
        pass
    @property
    def IRayPlusStudioStaticImageDoubleWidth(self) -> float:
        """
        Getter for property: (float) IRayPlusStudioStaticImageDoubleWidth
         Returns the Ray Traced Studio static image width   
            
         
        """
        pass
    @IRayPlusStudioStaticImageDoubleWidth.setter
    def IRayPlusStudioStaticImageDoubleWidth(self, iRayPlusStudioStaticImageDoubleWidth: float):
        """
        Setter for property: (float) IRayPlusStudioStaticImageDoubleWidth
         Returns the Ray Traced Studio static image width   
            
         
        """
        pass
    @property
    def IRayPlusStudioStaticImageFileFormat(self) -> IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageFileFormatType:
        """
        Getter for property: ( IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageFileFormatType NXOpen) IRayPlusStudioStaticImageFileFormat
         Returns the Ray Traced Studio static output image file format   
            
         
        """
        pass
    @IRayPlusStudioStaticImageFileFormat.setter
    def IRayPlusStudioStaticImageFileFormat(self, iRayPlusStudioStaticImageFileFormat: IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageFileFormatType):
        """
        Setter for property: ( IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageFileFormatType NXOpen) IRayPlusStudioStaticImageFileFormat
         Returns the Ray Traced Studio static output image file format   
            
         
        """
        pass
    @property
    def IRayPlusStudioStaticImageLockAspectRatio(self) -> bool:
        """
        Getter for property: (bool) IRayPlusStudioStaticImageLockAspectRatio
         Returns the Ray Traced Studio static image aspect ratio will be maintained   
            
         
        """
        pass
    @IRayPlusStudioStaticImageLockAspectRatio.setter
    def IRayPlusStudioStaticImageLockAspectRatio(self, iRayPlusStudioStaticImageLockAspectRatio: bool):
        """
        Setter for property: (bool) IRayPlusStudioStaticImageLockAspectRatio
         Returns the Ray Traced Studio static image aspect ratio will be maintained   
            
         
        """
        pass
    @property
    def IRayPlusStudioStaticImageOrientation(self) -> IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageOrientationType:
        """
        Getter for property: ( IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageOrientationType NXOpen) IRayPlusStudioStaticImageOrientation
         Returns the Ray Traced Studio static image orientation   
            
         
        """
        pass
    @IRayPlusStudioStaticImageOrientation.setter
    def IRayPlusStudioStaticImageOrientation(self, iRayPlusStudioStaticImageOrientation: IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageOrientationType):
        """
        Setter for property: ( IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageOrientationType NXOpen) IRayPlusStudioStaticImageOrientation
         Returns the Ray Traced Studio static image orientation   
            
         
        """
        pass
    @property
    def IRayPlusStudioStaticImagePixelHeight(self) -> int:
        """
        Getter for property: (int) IRayPlusStudioStaticImagePixelHeight
         Returns the Ray Traced Studio static image pixel height   
            
         
        """
        pass
    @IRayPlusStudioStaticImagePixelHeight.setter
    def IRayPlusStudioStaticImagePixelHeight(self, iRayPlusStudioStaticImagePixelHeight: int):
        """
        Setter for property: (int) IRayPlusStudioStaticImagePixelHeight
         Returns the Ray Traced Studio static image pixel height   
            
         
        """
        pass
    @property
    def IRayPlusStudioStaticImagePixelWidth(self) -> int:
        """
        Getter for property: (int) IRayPlusStudioStaticImagePixelWidth
         Returns the Ray Traced Studio static image pixel width   
            
         
        """
        pass
    @IRayPlusStudioStaticImagePixelWidth.setter
    def IRayPlusStudioStaticImagePixelWidth(self, iRayPlusStudioStaticImagePixelWidth: int):
        """
        Setter for property: (int) IRayPlusStudioStaticImagePixelWidth
         Returns the Ray Traced Studio static image pixel width   
            
         
        """
        pass
    @property
    def IRayPlusStudioStaticImageResolution(self) -> IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageResolutionType:
        """
        Getter for property: ( IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageResolutionType NXOpen) IRayPlusStudioStaticImageResolution
         Returns the Ray Traced Studio static image resolution   
            
         
        """
        pass
    @IRayPlusStudioStaticImageResolution.setter
    def IRayPlusStudioStaticImageResolution(self, iRayPlusStudioStaticImageResolution: IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageResolutionType):
        """
        Setter for property: ( IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageResolutionType NXOpen) IRayPlusStudioStaticImageResolution
         Returns the Ray Traced Studio static image resolution   
            
         
        """
        pass
    @property
    def IRayPlusStudioStaticImageSize(self) -> IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageSizeType:
        """
        Getter for property: ( IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageSizeType NXOpen) IRayPlusStudioStaticImageSize
         Returns the Ray Traced Studio static image size   
            
         
        """
        pass
    @IRayPlusStudioStaticImageSize.setter
    def IRayPlusStudioStaticImageSize(self, iRayPlusStudioStaticImageSize: IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageSizeType):
        """
        Setter for property: ( IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageSizeType NXOpen) IRayPlusStudioStaticImageSize
         Returns the Ray Traced Studio static image size   
            
         
        """
        pass
    @property
    def IRayPlusStudioStaticImageUnits(self) -> IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageUnitsType:
        """
        Getter for property: ( IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageUnitsType NXOpen) IRayPlusStudioStaticImageUnits
         Returns the Ray Traced Studio static image units   
            
         
        """
        pass
    @IRayPlusStudioStaticImageUnits.setter
    def IRayPlusStudioStaticImageUnits(self, iRayPlusStudioStaticImageUnits: IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageUnitsType):
        """
        Setter for property: ( IRayPlusStudioEditorBuilder.IRayPlusStudioStaticImageUnitsType NXOpen) IRayPlusStudioStaticImageUnits
         Returns the Ray Traced Studio static image units   
            
         
        """
        pass
    @property
    def IRayPlusStudioStaticImageVrHeight(self) -> int:
        """
        Getter for property: (int) IRayPlusStudioStaticImageVrHeight
         Returns the Ray Traced Studio static image height when rendering a VR-ready image   
            
         
        """
        pass
    @IRayPlusStudioStaticImageVrHeight.setter
    def IRayPlusStudioStaticImageVrHeight(self, iRayPlusStudioStaticImageVrHeight: int):
        """
        Setter for property: (int) IRayPlusStudioStaticImageVrHeight
         Returns the Ray Traced Studio static image height when rendering a VR-ready image   
            
         
        """
        pass
    @property
    def IRayPlusStudioStaticImageVrWidth(self) -> int:
        """
        Getter for property: (int) IRayPlusStudioStaticImageVrWidth
         Returns the Ray Traced Studio static image width when rendering a VR-ready image   
            
         
        """
        pass
    @IRayPlusStudioStaticImageVrWidth.setter
    def IRayPlusStudioStaticImageVrWidth(self, iRayPlusStudioStaticImageVrWidth: int):
        """
        Setter for property: (int) IRayPlusStudioStaticImageVrWidth
         Returns the Ray Traced Studio static image width when rendering a VR-ready image   
            
         
        """
        pass
    @property
    def IRayPlusStudioshowStatusIndicator(self) -> bool:
        """
        Getter for property: (bool) IRayPlusStudioshowStatusIndicator
         Returns the Ray Traced Studio progess status indicator percent complete display   
            
         
        """
        pass
    @IRayPlusStudioshowStatusIndicator.setter
    def IRayPlusStudioshowStatusIndicator(self, iRayPlusStudioshowStatusIndicator: bool):
        """
        Setter for property: (bool) IRayPlusStudioshowStatusIndicator
         Returns the Ray Traced Studio progess status indicator percent complete display   
            
         
        """
        pass
    @property
    def LensType(self) -> IRayPlusStudioEditorBuilder.IRayPlusStudioLensType:
        """
        Getter for property: ( IRayPlusStudioEditorBuilder.IRayPlusStudioLensType NXOpen) LensType
         Returns the Ray Traced Studio display lens distortion type to use if rendering a VR-ready image   
            
         
        """
        pass
    @LensType.setter
    def LensType(self, lensType: IRayPlusStudioEditorBuilder.IRayPlusStudioLensType):
        """
        Setter for property: ( IRayPlusStudioEditorBuilder.IRayPlusStudioLensType NXOpen) LensType
         Returns the Ray Traced Studio display lens distortion type to use if rendering a VR-ready image   
            
         
        """
        pass
    @property
    def RemoteRenderFormat(self) -> IRayPlusStudioEditorBuilder.IRayPlusStudioRemoteRenderFormatType:
        """
        Getter for property: ( IRayPlusStudioEditorBuilder.IRayPlusStudioRemoteRenderFormatType NXOpen) RemoteRenderFormat
         Returns the Ray Traced Studio display remote rendering format   
            
         
        """
        pass
    @RemoteRenderFormat.setter
    def RemoteRenderFormat(self, remoteRenderFormatType: IRayPlusStudioEditorBuilder.IRayPlusStudioRemoteRenderFormatType):
        """
        Setter for property: ( IRayPlusStudioEditorBuilder.IRayPlusStudioRemoteRenderFormatType NXOpen) RemoteRenderFormat
         Returns the Ray Traced Studio display remote rendering format   
            
         
        """
        pass
    @property
    def RemoteRenderIP(self) -> str:
        """
        Getter for property: (str) RemoteRenderIP
         Returns the Ray Traced Studio display remote rendering IP address   
            
         
        """
        pass
    @RemoteRenderIP.setter
    def RemoteRenderIP(self, remoteRenderIP: str):
        """
        Setter for property: (str) RemoteRenderIP
         Returns the Ray Traced Studio display remote rendering IP address   
            
         
        """
        pass
    @property
    def RemoteRenderPassword(self) -> str:
        """
        Getter for property: (str) RemoteRenderPassword
         Returns the Ray Traced Studio display remote rendering client Password  
            
         
        """
        pass
    @RemoteRenderPassword.setter
    def RemoteRenderPassword(self, remoteRenderPassword: str):
        """
        Setter for property: (str) RemoteRenderPassword
         Returns the Ray Traced Studio display remote rendering client Password  
            
         
        """
        pass
    @property
    def RemoteRenderReserveNodes(self) -> int:
        """
        Getter for property: (int) RemoteRenderReserveNodes
         Returns the Ray Traced Studio display remote rendering client reserve nodes  
            
         
        """
        pass
    @RemoteRenderReserveNodes.setter
    def RemoteRenderReserveNodes(self, remoteRenderReserveNodes: int):
        """
        Setter for property: (int) RemoteRenderReserveNodes
         Returns the Ray Traced Studio display remote rendering client reserve nodes  
            
         
        """
        pass
    @property
    def RemoteRenderSecurityToken(self) -> str:
        """
        Getter for property: (str) RemoteRenderSecurityToken
         Returns the Ray Traced Studio display remote rendering security token   
            
         
        """
        pass
    @RemoteRenderSecurityToken.setter
    def RemoteRenderSecurityToken(self, remoteRenderSecurityToken: str):
        """
        Setter for property: (str) RemoteRenderSecurityToken
         Returns the Ray Traced Studio display remote rendering security token   
            
         
        """
        pass
    @property
    def RemoteRenderToggle(self) -> bool:
        """
        Getter for property: (bool) RemoteRenderToggle
         Returns the Ray Traced Studio display if remote rendering is used   
            
         
        """
        pass
    @RemoteRenderToggle.setter
    def RemoteRenderToggle(self, remoteRenderToggle: bool):
        """
        Setter for property: (bool) RemoteRenderToggle
         Returns the Ray Traced Studio display if remote rendering is used   
            
         
        """
        pass
    @property
    def RemoteRenderType(self) -> IRayPlusStudioEditorBuilder.IRayPlusStudioRemoteRenderType:
        """
        Getter for property: ( IRayPlusStudioEditorBuilder.IRayPlusStudioRemoteRenderType NXOpen) RemoteRenderType
         Returns the Ray Traced Studio display remote rendering type   
            
         
        """
        pass
    @RemoteRenderType.setter
    def RemoteRenderType(self, remoteRenderType: IRayPlusStudioEditorBuilder.IRayPlusStudioRemoteRenderType):
        """
        Setter for property: ( IRayPlusStudioEditorBuilder.IRayPlusStudioRemoteRenderType NXOpen) RemoteRenderType
         Returns the Ray Traced Studio display remote rendering type   
            
         
        """
        pass
    @property
    def RemoteRenderUsername(self) -> str:
        """
        Getter for property: (str) RemoteRenderUsername
         Returns the Ray Traced Studio display remote rendering client Username  
            
         
        """
        pass
    @RemoteRenderUsername.setter
    def RemoteRenderUsername(self, remoteRenderUsername: str):
        """
        Setter for property: (str) RemoteRenderUsername
         Returns the Ray Traced Studio display remote rendering client Username  
            
         
        """
        pass
    @property
    def RemoteRenderVideoMode(self) -> IRayPlusStudioEditorBuilder.IRayPlusStudioRemoteRenderVideoType:
        """
        Getter for property: ( IRayPlusStudioEditorBuilder.IRayPlusStudioRemoteRenderVideoType NXOpen) RemoteRenderVideoMode
         Returns the Ray Traced Studio display remote rendering video mode   
            
         
        """
        pass
    @RemoteRenderVideoMode.setter
    def RemoteRenderVideoMode(self, remoteRenderVideoType: IRayPlusStudioEditorBuilder.IRayPlusStudioRemoteRenderVideoType):
        """
        Setter for property: ( IRayPlusStudioEditorBuilder.IRayPlusStudioRemoteRenderVideoType NXOpen) RemoteRenderVideoMode
         Returns the Ray Traced Studio display remote rendering video mode   
            
         
        """
        pass
    @property
    def StaticAutoCompletionType(self) -> IRayPlusStudioEditorBuilder.IRayPlusStudioAutoCompletionType:
        """
        Getter for property: ( IRayPlusStudioEditorBuilder.IRayPlusStudioAutoCompletionType NXOpen) StaticAutoCompletionType
         Returns the Ray Traced Studio display static render auto-completion type   
            
         
        """
        pass
    @StaticAutoCompletionType.setter
    def StaticAutoCompletionType(self, autoCompletionType: IRayPlusStudioEditorBuilder.IRayPlusStudioAutoCompletionType):
        """
        Setter for property: ( IRayPlusStudioEditorBuilder.IRayPlusStudioAutoCompletionType NXOpen) StaticAutoCompletionType
         Returns the Ray Traced Studio display static render auto-completion type   
            
         
        """
        pass
    @property
    def StaticIRayPlusStudioTime(self) -> NXOpen.DateBuilder:
        """
        Getter for property: ( NXOpen.DateBuilder) StaticIRayPlusStudioTime
         Returns the Ray Traced Studio static display time-based rendering timer (read only)   
            
         
        """
        pass
    @property
    def StaticRenderDuration(self) -> IRayPlusStudioEditorBuilder.StaticRenderDurationType:
        """
        Getter for property: ( IRayPlusStudioEditorBuilder.StaticRenderDurationType NXOpen) StaticRenderDuration
         Returns the Ray Traced Studio display static render duration type   
            
         
        """
        pass
    @StaticRenderDuration.setter
    def StaticRenderDuration(self, staticRenderDuration: IRayPlusStudioEditorBuilder.StaticRenderDurationType):
        """
        Setter for property: ( IRayPlusStudioEditorBuilder.StaticRenderDurationType NXOpen) StaticRenderDuration
         Returns the Ray Traced Studio display static render duration type   
            
         
        """
        pass
    @property
    def StaticRenderNumberOfIterations(self) -> int:
        """
        Getter for property: (int) StaticRenderNumberOfIterations
         Returns the Ray Traced Studio static image number of iterations limit   
            
         
        """
        pass
    @StaticRenderNumberOfIterations.setter
    def StaticRenderNumberOfIterations(self, staticRenderNumberOfIterations: int):
        """
        Setter for property: (int) StaticRenderNumberOfIterations
         Returns the Ray Traced Studio static image number of iterations limit   
            
         
        """
        pass
    @property
    def StereoLayout(self) -> IRayPlusStudioEditorBuilder.IRayPlusStudioStereoLayoutType:
        """
        Getter for property: ( IRayPlusStudioEditorBuilder.IRayPlusStudioStereoLayoutType NXOpen) StereoLayout
         Returns the Ray Traced Studio display image layout to use if rendering a stereo image   
            
         
        """
        pass
    @StereoLayout.setter
    def StereoLayout(self, stereoLayout: IRayPlusStudioEditorBuilder.IRayPlusStudioStereoLayoutType):
        """
        Setter for property: ( IRayPlusStudioEditorBuilder.IRayPlusStudioStereoLayoutType NXOpen) StereoLayout
         Returns the Ray Traced Studio display image layout to use if rendering a stereo image   
            
         
        """
        pass
    @property
    def VrCamera(self) -> NXOpen.CartesianCoordinateSystem:
        """
        Getter for property: ( NXOpen.CartesianCoordinateSystem) VrCamera
         Returns the Ray Traced Studio display VR camera coordinate system   
            
         
        """
        pass
    @VrCamera.setter
    def VrCamera(self, vrCamera: NXOpen.CartesianCoordinateSystem):
        """
        Setter for property: ( NXOpen.CartesianCoordinateSystem) VrCamera
         Returns the Ray Traced Studio display VR camera coordinate system   
            
         
        """
        pass
    @property
    def VrEnabledToggle(self) -> bool:
        """
        Getter for property: (bool) VrEnabledToggle
         Returns the Ray Traced Studio display if the image will be rendered in a VR-ready format   
            
         
        """
        pass
    @VrEnabledToggle.setter
    def VrEnabledToggle(self, vrEnabledToggle: bool):
        """
        Setter for property: (bool) VrEnabledToggle
         Returns the Ray Traced Studio display if the image will be rendered in a VR-ready format   
            
         
        """
        pass
import NXOpen
class IRayPlusStudioPreferencesBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Display.IRayPlusStudioPreferencesBuilder.
    Ray Traced Studio Preferences controls display and output of CPU-based real-time ray tracing.
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return .
    """
    class DynamicIRayPlusStudioRenderModeType(Enum):
        """
        Members Include: 
         |Photoreal|  Very good ray traced display quality when dynamic interaction stops 
         |QualityInteractive|  Good ray traced display quality with good performance when dynamic interaction stops 
         |FastInteractive|  The fastest ray traced display performance with preview quality when dynamic interaction stops 

        """
        Photoreal: int
        QualityInteractive: int
        FastInteractive: int
        @staticmethod
        def ValueOf(value: int) -> IRayPlusStudioPreferencesBuilder.DynamicIRayPlusStudioRenderModeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class IRayPlusStudioAutoCompletionType(Enum):
        """
        Members Include: 
         |Simple| the automatic completion criteria for a simple scene with a limited number of emissive materials, reflective materials, and shadows
         |Normal| the automatic completion criteria for a normal scene with a balanced number of emissive materials, reflective materials, and shadows
         |Complex| the automatic completion criteria for a complex scene with numerous emissive materials, reflective materials, and shadows 
         |NotSet| the option to apply no automatic completion criteria
         |Custom| the automatic completion criteria to specify a custom threshold for automatically detecting the completion of an image 

        """
        Simple: int
        Normal: int
        Complex: int
        NotSet: int
        Custom: int
        @staticmethod
        def ValueOf(value: int) -> IRayPlusStudioPreferencesBuilder.IRayPlusStudioAutoCompletionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class IRayPlusStudioLensType(Enum):
        """
        Members Include: 
         |Monospherical|  Mono Spherical 
         |Stereospherical|  Stereo Spherical 

        """
        Monospherical: int
        Stereospherical: int
        @staticmethod
        def ValueOf(value: int) -> IRayPlusStudioPreferencesBuilder.IRayPlusStudioLensType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class IRayPlusStudioRemoteRenderFormatType(Enum):
        """
        Members Include: 
         |H264| 
         |Lossless| 
         |Png| 
         |Jpeg| 

        """
        H264: int
        Lossless: int
        Png: int
        Jpeg: int
        @staticmethod
        def ValueOf(value: int) -> IRayPlusStudioPreferencesBuilder.IRayPlusStudioRemoteRenderFormatType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class IRayPlusStudioRemoteRenderType(Enum):
        """
        Members Include: 
         |Cluster|  Network Cluster 
         |Vca|  VCA 
         |SecuredCluster|  Secured Network Cluster

        """
        Cluster: int
        Vca: int
        SecuredCluster: int
        @staticmethod
        def ValueOf(value: int) -> IRayPlusStudioPreferencesBuilder.IRayPlusStudioRemoteRenderType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class IRayPlusStudioRemoteRenderVideoType(Enum):
        """
        Members Include: 
         |Streaming| 
         |Synchronous| 

        """
        Streaming: int
        Synchronous: int
        @staticmethod
        def ValueOf(value: int) -> IRayPlusStudioPreferencesBuilder.IRayPlusStudioRemoteRenderVideoType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class IRayPlusStudioStaticImageFileFormatType(Enum):
        """
        Members Include: 
         |Tif|  Tagged Image File Format (TIFF) file format 
         |Png|  Portable Network Graphic (PNG) file format 
         |Jpg|  Joint Photographic Experts Group (JPEG) file format 

        """
        Tif: int
        Png: int
        Jpg: int
        @staticmethod
        def ValueOf(value: int) -> IRayPlusStudioPreferencesBuilder.IRayPlusStudioStaticImageFileFormatType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class IRayPlusStudioStaticImageOrientationType(Enum):
        """
        Members Include: 
         |Landscape|  static image orientation where width is greater than height 
         |Portrait|  static image orientation where height is greater than width 

        """
        Landscape: int
        Portrait: int
        @staticmethod
        def ValueOf(value: int) -> IRayPlusStudioPreferencesBuilder.IRayPlusStudioStaticImageOrientationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class IRayPlusStudioStaticImageResolutionType(Enum):
        """
        Members Include: 
         |High|  static image output resolution of 300 DPI (dots per inch) 
         |Medium|  static image output resolution of 150 DPI (dots per inch) 
         |Low|  static image output resolution of 72 DPI (dots per inch) 
         |UserDefined|  user specified image output resolution in DPI (dots per inch) 

        """
        High: int
        Medium: int
        Low: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> IRayPlusStudioPreferencesBuilder.IRayPlusStudioStaticImageResolutionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class IRayPlusStudioStaticImageSizeType(Enum):
        """
        Members Include: 
         |RenderWindow|  Ray Traced Studio window size used for static image output 
         |UserDefined|  user specified size for static image output 

        """
        RenderWindow: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> IRayPlusStudioPreferencesBuilder.IRayPlusStudioStaticImageSizeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class IRayPlusStudioStaticImageUnitsType(Enum):
        """
        Members Include: 
         |Pixels|  static image size specified in pixel 
         |Millimeters|  static image size specified in millimeters 
         |Inches|  static image size specified in inches 

        """
        Pixels: int
        Millimeters: int
        Inches: int
        @staticmethod
        def ValueOf(value: int) -> IRayPlusStudioPreferencesBuilder.IRayPlusStudioStaticImageUnitsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class IRayPlusStudioStereoLayoutType(Enum):
        """
        Members Include: 
         |TopBottom|  Top-Bottom 
         |SideBySide|  Side-by-Side 

        """
        TopBottom: int
        SideBySide: int
        @staticmethod
        def ValueOf(value: int) -> IRayPlusStudioPreferencesBuilder.IRayPlusStudioStereoLayoutType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StaticRenderDurationType(Enum):
        """
        Members Include: 
         |NumberOfIterations| the number of iterations specified to the renderer to the static render 
         |TimeLimit| the amount of time specified to the renderer to reach for the static render 
         |AutoComplete| the auto Complete criteria uses Iray+ based progressive completion criteria to determine render completion 
         |TimeLimitedAutoComplete| the auto Complete criteria uses Iray+ based progressive completion criteria to determine render completion and a designated time limit 

        """
        NumberOfIterations: int
        TimeLimit: int
        AutoComplete: int
        TimeLimitedAutoComplete: int
        @staticmethod
        def ValueOf(value: int) -> IRayPlusStudioPreferencesBuilder.StaticRenderDurationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AutoCompletionCustomPixelRatio(self) -> float:
        """
        Getter for property: (float) AutoCompletionCustomPixelRatio
         Returns the Ray Traced Studio display static render auto-completion custom pixel ratio.  
           This controls
                "the number of pixels as a ratio of the total pixel count that must converge to the Quality Completion Factor."  
         
        """
        pass
    @AutoCompletionCustomPixelRatio.setter
    def AutoCompletionCustomPixelRatio(self, autoCompletionCustomPixelRatio: float):
        """
        Setter for property: (float) AutoCompletionCustomPixelRatio
         Returns the Ray Traced Studio display static render auto-completion custom pixel ratio.  
           This controls
                "the number of pixels as a ratio of the total pixel count that must converge to the Quality Completion Factor."  
         
        """
        pass
    @property
    def AutoCompletionCustomQualityFactor(self) -> float:
        """
        Getter for property: (float) AutoCompletionCustomQualityFactor
         Returns the Ray Traced Studio display static render auto-completion custom quality factor.  
           This control
                defines a quality factor relative to the scene. The quality factor has a linear
                scaling effect. For example, a quality factor set to 2.0 will roughly take twice as
                long to render a scene with an assigned quality factor of 1.0.  
         
        """
        pass
    @AutoCompletionCustomQualityFactor.setter
    def AutoCompletionCustomQualityFactor(self, autoCompletionCustomQualityFactor: float):
        """
        Setter for property: (float) AutoCompletionCustomQualityFactor
         Returns the Ray Traced Studio display static render auto-completion custom quality factor.  
           This control
                defines a quality factor relative to the scene. The quality factor has a linear
                scaling effect. For example, a quality factor set to 2.0 will roughly take twice as
                long to render a scene with an assigned quality factor of 1.0.  
         
        """
        pass
    @property
    def DynamicIRayPlusCaustics(self) -> bool:
        """
        Getter for property: (bool) DynamicIRayPlusCaustics
         Returns the Ray Traced Studio dynamic antialiasing quality when dynamic interaction stops   
            
         
        """
        pass
    @DynamicIRayPlusCaustics.setter
    def DynamicIRayPlusCaustics(self, dynamicIRayPlusCaustics: bool):
        """
        Setter for property: (bool) DynamicIRayPlusCaustics
         Returns the Ray Traced Studio dynamic antialiasing quality when dynamic interaction stops   
            
         
        """
        pass
    @property
    def DynamicIRayPlusStudioRenderMode(self) -> IRayPlusStudioPreferencesBuilder.DynamicIRayPlusStudioRenderModeType:
        """
        Getter for property: ( IRayPlusStudioPreferencesBuilder.DynamicIRayPlusStudioRenderModeType NXOpen) DynamicIRayPlusStudioRenderMode
         Returns the Ray Traced Studio dynamic display rendering mode   
            
         
        """
        pass
    @DynamicIRayPlusStudioRenderMode.setter
    def DynamicIRayPlusStudioRenderMode(self, dynamicIRayPlusStudioRenderMode: IRayPlusStudioPreferencesBuilder.DynamicIRayPlusStudioRenderModeType):
        """
        Setter for property: ( IRayPlusStudioPreferencesBuilder.DynamicIRayPlusStudioRenderModeType NXOpen) DynamicIRayPlusStudioRenderMode
         Returns the Ray Traced Studio dynamic display rendering mode   
            
         
        """
        pass
    @property
    def DynamicIRayPlusStudioTime(self) -> NXOpen.DateBuilder:
        """
        Getter for property: ( NXOpen.DateBuilder) DynamicIRayPlusStudioTime
         Returns the Ray Traced Studio dynamic display time-based rendering mode timer (read only)   
            
         
        """
        pass
    @property
    def EyeSeparation(self) -> float:
        """
        Getter for property: (float) EyeSeparation
         Returns the Ray Traced Studio display eye separation distance to use if rendering a stereo image   
            
         
        """
        pass
    @EyeSeparation.setter
    def EyeSeparation(self, eyeSeparation: float):
        """
        Setter for property: (float) EyeSeparation
         Returns the Ray Traced Studio display eye separation distance to use if rendering a stereo image   
            
         
        """
        pass
    @property
    def IRayPlusStudioDenoiserToggle(self) -> bool:
        """
        Getter for property: (bool) IRayPlusStudioDenoiserToggle
         Returns the Ray Traced Studio denoiser   
            
         
        """
        pass
    @IRayPlusStudioDenoiserToggle.setter
    def IRayPlusStudioDenoiserToggle(self, iRayPlusStudioDenoiserToggle: bool):
        """
        Setter for property: (bool) IRayPlusStudioDenoiserToggle
         Returns the Ray Traced Studio denoiser   
            
         
        """
        pass
    @property
    def IRayPlusStudioOptimizePerformanceToggle(self) -> bool:
        """
        Getter for property: (bool) IRayPlusStudioOptimizePerformanceToggle
         Returns the IRay Plust Studio Optimize Performance Toggle means use stored precise geometry whenever they are available and 
                uses lightweight faceted geometry when there are no stored precise geometry available  
            
         
        """
        pass
    @IRayPlusStudioOptimizePerformanceToggle.setter
    def IRayPlusStudioOptimizePerformanceToggle(self, iRayPlusStudioOptimizePerformanceToggle: bool):
        """
        Setter for property: (bool) IRayPlusStudioOptimizePerformanceToggle
         Returns the IRay Plust Studio Optimize Performance Toggle means use stored precise geometry whenever they are available and 
                uses lightweight faceted geometry when there are no stored precise geometry available  
            
         
        """
        pass
    @property
    def IRayPlusStudioStaticImageDotsPerInch(self) -> int:
        """
        Getter for property: (int) IRayPlusStudioStaticImageDotsPerInch
         Returns the Ray Traced Studio static image dots per inch (DPI)   
            
         
        """
        pass
    @IRayPlusStudioStaticImageDotsPerInch.setter
    def IRayPlusStudioStaticImageDotsPerInch(self, iRayPlusStudioStaticImageDotsPerInch: int):
        """
        Setter for property: (int) IRayPlusStudioStaticImageDotsPerInch
         Returns the Ray Traced Studio static image dots per inch (DPI)   
            
         
        """
        pass
    @property
    def IRayPlusStudioStaticImageDoubleHeight(self) -> float:
        """
        Getter for property: (float) IRayPlusStudioStaticImageDoubleHeight
         Returns the Ray Traced Studio static image height   
            
         
        """
        pass
    @IRayPlusStudioStaticImageDoubleHeight.setter
    def IRayPlusStudioStaticImageDoubleHeight(self, iRayPlusStudioStaticImageDoubleHeight: float):
        """
        Setter for property: (float) IRayPlusStudioStaticImageDoubleHeight
         Returns the Ray Traced Studio static image height   
            
         
        """
        pass
    @property
    def IRayPlusStudioStaticImageDoubleWidth(self) -> float:
        """
        Getter for property: (float) IRayPlusStudioStaticImageDoubleWidth
         Returns the Ray Traced Studio static image width   
            
         
        """
        pass
    @IRayPlusStudioStaticImageDoubleWidth.setter
    def IRayPlusStudioStaticImageDoubleWidth(self, iRayPlusStudioStaticImageDoubleWidth: float):
        """
        Setter for property: (float) IRayPlusStudioStaticImageDoubleWidth
         Returns the Ray Traced Studio static image width   
            
         
        """
        pass
    @property
    def IRayPlusStudioStaticImageFileFormat(self) -> IRayPlusStudioPreferencesBuilder.IRayPlusStudioStaticImageFileFormatType:
        """
        Getter for property: ( IRayPlusStudioPreferencesBuilder.IRayPlusStudioStaticImageFileFormatType NXOpen) IRayPlusStudioStaticImageFileFormat
         Returns the Ray Traced Studio static output image file format   
            
         
        """
        pass
    @IRayPlusStudioStaticImageFileFormat.setter
    def IRayPlusStudioStaticImageFileFormat(self, iRayPlusStudioStaticImageFileFormat: IRayPlusStudioPreferencesBuilder.IRayPlusStudioStaticImageFileFormatType):
        """
        Setter for property: ( IRayPlusStudioPreferencesBuilder.IRayPlusStudioStaticImageFileFormatType NXOpen) IRayPlusStudioStaticImageFileFormat
         Returns the Ray Traced Studio static output image file format   
            
         
        """
        pass
    @property
    def IRayPlusStudioStaticImageLockAspectRatio(self) -> bool:
        """
        Getter for property: (bool) IRayPlusStudioStaticImageLockAspectRatio
         Returns the Ray Traced Studio static image aspect ratio will be maintained   
            
         
        """
        pass
    @IRayPlusStudioStaticImageLockAspectRatio.setter
    def IRayPlusStudioStaticImageLockAspectRatio(self, iRayPlusStudioStaticImageLockAspectRatio: bool):
        """
        Setter for property: (bool) IRayPlusStudioStaticImageLockAspectRatio
         Returns the Ray Traced Studio static image aspect ratio will be maintained   
            
         
        """
        pass
    @property
    def IRayPlusStudioStaticImageOrientation(self) -> IRayPlusStudioPreferencesBuilder.IRayPlusStudioStaticImageOrientationType:
        """
        Getter for property: ( IRayPlusStudioPreferencesBuilder.IRayPlusStudioStaticImageOrientationType NXOpen) IRayPlusStudioStaticImageOrientation
         Returns the Ray Traced Studio static image orientation   
            
         
        """
        pass
    @IRayPlusStudioStaticImageOrientation.setter
    def IRayPlusStudioStaticImageOrientation(self, iRayPlusStudioStaticImageOrientation: IRayPlusStudioPreferencesBuilder.IRayPlusStudioStaticImageOrientationType):
        """
        Setter for property: ( IRayPlusStudioPreferencesBuilder.IRayPlusStudioStaticImageOrientationType NXOpen) IRayPlusStudioStaticImageOrientation
         Returns the Ray Traced Studio static image orientation   
            
         
        """
        pass
    @property
    def IRayPlusStudioStaticImagePixelHeight(self) -> int:
        """
        Getter for property: (int) IRayPlusStudioStaticImagePixelHeight
         Returns the Ray Traced Studio static image pixel height   
            
         
        """
        pass
    @IRayPlusStudioStaticImagePixelHeight.setter
    def IRayPlusStudioStaticImagePixelHeight(self, iRayPlusStudioStaticImagePixelHeight: int):
        """
        Setter for property: (int) IRayPlusStudioStaticImagePixelHeight
         Returns the Ray Traced Studio static image pixel height   
            
         
        """
        pass
    @property
    def IRayPlusStudioStaticImagePixelWidth(self) -> int:
        """
        Getter for property: (int) IRayPlusStudioStaticImagePixelWidth
         Returns the Ray Traced Studio static image pixel width   
            
         
        """
        pass
    @IRayPlusStudioStaticImagePixelWidth.setter
    def IRayPlusStudioStaticImagePixelWidth(self, iRayPlusStudioStaticImagePixelWidth: int):
        """
        Setter for property: (int) IRayPlusStudioStaticImagePixelWidth
         Returns the Ray Traced Studio static image pixel width   
            
         
        """
        pass
    @property
    def IRayPlusStudioStaticImageResolution(self) -> IRayPlusStudioPreferencesBuilder.IRayPlusStudioStaticImageResolutionType:
        """
        Getter for property: ( IRayPlusStudioPreferencesBuilder.IRayPlusStudioStaticImageResolutionType NXOpen) IRayPlusStudioStaticImageResolution
         Returns the Ray Traced Studio static image resolution   
            
         
        """
        pass
    @IRayPlusStudioStaticImageResolution.setter
    def IRayPlusStudioStaticImageResolution(self, iRayPlusStudioStaticImageResolution: IRayPlusStudioPreferencesBuilder.IRayPlusStudioStaticImageResolutionType):
        """
        Setter for property: ( IRayPlusStudioPreferencesBuilder.IRayPlusStudioStaticImageResolutionType NXOpen) IRayPlusStudioStaticImageResolution
         Returns the Ray Traced Studio static image resolution   
            
         
        """
        pass
    @property
    def IRayPlusStudioStaticImageSize(self) -> IRayPlusStudioPreferencesBuilder.IRayPlusStudioStaticImageSizeType:
        """
        Getter for property: ( IRayPlusStudioPreferencesBuilder.IRayPlusStudioStaticImageSizeType NXOpen) IRayPlusStudioStaticImageSize
         Returns the Ray Traced Studio static image size   
            
         
        """
        pass
    @IRayPlusStudioStaticImageSize.setter
    def IRayPlusStudioStaticImageSize(self, iRayPlusStudioStaticImageSize: IRayPlusStudioPreferencesBuilder.IRayPlusStudioStaticImageSizeType):
        """
        Setter for property: ( IRayPlusStudioPreferencesBuilder.IRayPlusStudioStaticImageSizeType NXOpen) IRayPlusStudioStaticImageSize
         Returns the Ray Traced Studio static image size   
            
         
        """
        pass
    @property
    def IRayPlusStudioStaticImageUnits(self) -> IRayPlusStudioPreferencesBuilder.IRayPlusStudioStaticImageUnitsType:
        """
        Getter for property: ( IRayPlusStudioPreferencesBuilder.IRayPlusStudioStaticImageUnitsType NXOpen) IRayPlusStudioStaticImageUnits
         Returns the Ray Traced Studio static image units   
            
         
        """
        pass
    @IRayPlusStudioStaticImageUnits.setter
    def IRayPlusStudioStaticImageUnits(self, iRayPlusStudioStaticImageUnits: IRayPlusStudioPreferencesBuilder.IRayPlusStudioStaticImageUnitsType):
        """
        Setter for property: ( IRayPlusStudioPreferencesBuilder.IRayPlusStudioStaticImageUnitsType NXOpen) IRayPlusStudioStaticImageUnits
         Returns the Ray Traced Studio static image units   
            
         
        """
        pass
    @property
    def IRayPlusStudioStaticImageVrHeight(self) -> int:
        """
        Getter for property: (int) IRayPlusStudioStaticImageVrHeight
         Returns the Ray Traced Studio static image height when rendering a VR-ready image   
            
         
        """
        pass
    @IRayPlusStudioStaticImageVrHeight.setter
    def IRayPlusStudioStaticImageVrHeight(self, iRayPlusStudioStaticImageVrHeight: int):
        """
        Setter for property: (int) IRayPlusStudioStaticImageVrHeight
         Returns the Ray Traced Studio static image height when rendering a VR-ready image   
            
         
        """
        pass
    @property
    def IRayPlusStudioStaticImageVrWidth(self) -> int:
        """
        Getter for property: (int) IRayPlusStudioStaticImageVrWidth
         Returns the Ray Traced Studio static image width when rendering a VR-ready image   
            
         
        """
        pass
    @IRayPlusStudioStaticImageVrWidth.setter
    def IRayPlusStudioStaticImageVrWidth(self, iRayPlusStudioStaticImageVrWidth: int):
        """
        Setter for property: (int) IRayPlusStudioStaticImageVrWidth
         Returns the Ray Traced Studio static image width when rendering a VR-ready image   
            
         
        """
        pass
    @property
    def IRayPlusStudioshowStatusIndicator(self) -> bool:
        """
        Getter for property: (bool) IRayPlusStudioshowStatusIndicator
         Returns the Ray Traced Studio progess status indicator percent complete display   
            
         
        """
        pass
    @IRayPlusStudioshowStatusIndicator.setter
    def IRayPlusStudioshowStatusIndicator(self, iRayPlusStudioshowStatusIndicator: bool):
        """
        Setter for property: (bool) IRayPlusStudioshowStatusIndicator
         Returns the Ray Traced Studio progess status indicator percent complete display   
            
         
        """
        pass
    @property
    def LensType(self) -> IRayPlusStudioPreferencesBuilder.IRayPlusStudioLensType:
        """
        Getter for property: ( IRayPlusStudioPreferencesBuilder.IRayPlusStudioLensType NXOpen) LensType
         Returns the Ray Traced Studio display lens distortion type to use if rendering a VR-ready image   
            
         
        """
        pass
    @LensType.setter
    def LensType(self, lensType: IRayPlusStudioPreferencesBuilder.IRayPlusStudioLensType):
        """
        Setter for property: ( IRayPlusStudioPreferencesBuilder.IRayPlusStudioLensType NXOpen) LensType
         Returns the Ray Traced Studio display lens distortion type to use if rendering a VR-ready image   
            
         
        """
        pass
    @property
    def RemoteRenderFormat(self) -> IRayPlusStudioPreferencesBuilder.IRayPlusStudioRemoteRenderFormatType:
        """
        Getter for property: ( IRayPlusStudioPreferencesBuilder.IRayPlusStudioRemoteRenderFormatType NXOpen) RemoteRenderFormat
         Returns the Ray Traced Studio display remote rendering format   
            
         
        """
        pass
    @RemoteRenderFormat.setter
    def RemoteRenderFormat(self, remoteRenderFormatType: IRayPlusStudioPreferencesBuilder.IRayPlusStudioRemoteRenderFormatType):
        """
        Setter for property: ( IRayPlusStudioPreferencesBuilder.IRayPlusStudioRemoteRenderFormatType NXOpen) RemoteRenderFormat
         Returns the Ray Traced Studio display remote rendering format   
            
         
        """
        pass
    @property
    def RemoteRenderIP(self) -> str:
        """
        Getter for property: (str) RemoteRenderIP
         Returns the Ray Traced Studio display remote rendering IP address   
            
         
        """
        pass
    @RemoteRenderIP.setter
    def RemoteRenderIP(self, remoteRenderIP: str):
        """
        Setter for property: (str) RemoteRenderIP
         Returns the Ray Traced Studio display remote rendering IP address   
            
         
        """
        pass
    @property
    def RemoteRenderPassword(self) -> str:
        """
        Getter for property: (str) RemoteRenderPassword
         Returns the Ray Traced Studio display remote rendering client Password  
            
         
        """
        pass
    @RemoteRenderPassword.setter
    def RemoteRenderPassword(self, remoteRenderPassword: str):
        """
        Setter for property: (str) RemoteRenderPassword
         Returns the Ray Traced Studio display remote rendering client Password  
            
         
        """
        pass
    @property
    def RemoteRenderReserveNodes(self) -> int:
        """
        Getter for property: (int) RemoteRenderReserveNodes
         Returns the Ray Traced Studio display remote rendering client reserve nodes  
            
         
        """
        pass
    @RemoteRenderReserveNodes.setter
    def RemoteRenderReserveNodes(self, remoteRenderReserveNodes: int):
        """
        Setter for property: (int) RemoteRenderReserveNodes
         Returns the Ray Traced Studio display remote rendering client reserve nodes  
            
         
        """
        pass
    @property
    def RemoteRenderSecurityToken(self) -> str:
        """
        Getter for property: (str) RemoteRenderSecurityToken
         Returns the Ray Traced Studio display remote rendering security token   
            
         
        """
        pass
    @RemoteRenderSecurityToken.setter
    def RemoteRenderSecurityToken(self, remoteRenderSecurityToken: str):
        """
        Setter for property: (str) RemoteRenderSecurityToken
         Returns the Ray Traced Studio display remote rendering security token   
            
         
        """
        pass
    @property
    def RemoteRenderToggle(self) -> bool:
        """
        Getter for property: (bool) RemoteRenderToggle
         Returns the Ray Traced Studio display if remote rendering is used   
            
         
        """
        pass
    @RemoteRenderToggle.setter
    def RemoteRenderToggle(self, remoteRenderToggle: bool):
        """
        Setter for property: (bool) RemoteRenderToggle
         Returns the Ray Traced Studio display if remote rendering is used   
            
         
        """
        pass
    @property
    def RemoteRenderType(self) -> IRayPlusStudioPreferencesBuilder.IRayPlusStudioRemoteRenderType:
        """
        Getter for property: ( IRayPlusStudioPreferencesBuilder.IRayPlusStudioRemoteRenderType NXOpen) RemoteRenderType
         Returns the Ray Traced Studio display remote rendering type   
            
         
        """
        pass
    @RemoteRenderType.setter
    def RemoteRenderType(self, remoteRenderType: IRayPlusStudioPreferencesBuilder.IRayPlusStudioRemoteRenderType):
        """
        Setter for property: ( IRayPlusStudioPreferencesBuilder.IRayPlusStudioRemoteRenderType NXOpen) RemoteRenderType
         Returns the Ray Traced Studio display remote rendering type   
            
         
        """
        pass
    @property
    def RemoteRenderUsername(self) -> str:
        """
        Getter for property: (str) RemoteRenderUsername
         Returns the Ray Traced Studio display remote rendering client Username  
            
         
        """
        pass
    @RemoteRenderUsername.setter
    def RemoteRenderUsername(self, remoteRenderUsername: str):
        """
        Setter for property: (str) RemoteRenderUsername
         Returns the Ray Traced Studio display remote rendering client Username  
            
         
        """
        pass
    @property
    def RemoteRenderVideoMode(self) -> IRayPlusStudioPreferencesBuilder.IRayPlusStudioRemoteRenderVideoType:
        """
        Getter for property: ( IRayPlusStudioPreferencesBuilder.IRayPlusStudioRemoteRenderVideoType NXOpen) RemoteRenderVideoMode
         Returns the Ray Traced Studio display remote rendering video mode   
            
         
        """
        pass
    @RemoteRenderVideoMode.setter
    def RemoteRenderVideoMode(self, remoteRenderVideoType: IRayPlusStudioPreferencesBuilder.IRayPlusStudioRemoteRenderVideoType):
        """
        Setter for property: ( IRayPlusStudioPreferencesBuilder.IRayPlusStudioRemoteRenderVideoType NXOpen) RemoteRenderVideoMode
         Returns the Ray Traced Studio display remote rendering video mode   
            
         
        """
        pass
    @property
    def StaticAutoCompletionType(self) -> IRayPlusStudioPreferencesBuilder.IRayPlusStudioAutoCompletionType:
        """
        Getter for property: ( IRayPlusStudioPreferencesBuilder.IRayPlusStudioAutoCompletionType NXOpen) StaticAutoCompletionType
         Returns the Ray Traced Studio display static render auto-completion type   
            
         
        """
        pass
    @StaticAutoCompletionType.setter
    def StaticAutoCompletionType(self, autoCompletionType: IRayPlusStudioPreferencesBuilder.IRayPlusStudioAutoCompletionType):
        """
        Setter for property: ( IRayPlusStudioPreferencesBuilder.IRayPlusStudioAutoCompletionType NXOpen) StaticAutoCompletionType
         Returns the Ray Traced Studio display static render auto-completion type   
            
         
        """
        pass
    @property
    def StaticIRayPlusStudioTime(self) -> NXOpen.DateBuilder:
        """
        Getter for property: ( NXOpen.DateBuilder) StaticIRayPlusStudioTime
         Returns the Ray Traced Studio static display time-based rendering timer (read only)   
            
         
        """
        pass
    @property
    def StaticRenderDuration(self) -> IRayPlusStudioPreferencesBuilder.StaticRenderDurationType:
        """
        Getter for property: ( IRayPlusStudioPreferencesBuilder.StaticRenderDurationType NXOpen) StaticRenderDuration
         Returns the Ray Traced Studio display static render duration type   
            
         
        """
        pass
    @StaticRenderDuration.setter
    def StaticRenderDuration(self, staticRenderDuration: IRayPlusStudioPreferencesBuilder.StaticRenderDurationType):
        """
        Setter for property: ( IRayPlusStudioPreferencesBuilder.StaticRenderDurationType NXOpen) StaticRenderDuration
         Returns the Ray Traced Studio display static render duration type   
            
         
        """
        pass
    @property
    def StaticRenderNumberOfIterations(self) -> int:
        """
        Getter for property: (int) StaticRenderNumberOfIterations
         Returns the Ray Traced Studio static image number of iterations limit   
            
         
        """
        pass
    @StaticRenderNumberOfIterations.setter
    def StaticRenderNumberOfIterations(self, staticRenderNumberOfIterations: int):
        """
        Setter for property: (int) StaticRenderNumberOfIterations
         Returns the Ray Traced Studio static image number of iterations limit   
            
         
        """
        pass
    @property
    def StereoLayout(self) -> IRayPlusStudioPreferencesBuilder.IRayPlusStudioStereoLayoutType:
        """
        Getter for property: ( IRayPlusStudioPreferencesBuilder.IRayPlusStudioStereoLayoutType NXOpen) StereoLayout
         Returns the Ray Traced Studio display image layout to use if rendering a stereo image   
            
         
        """
        pass
    @StereoLayout.setter
    def StereoLayout(self, stereoLayout: IRayPlusStudioPreferencesBuilder.IRayPlusStudioStereoLayoutType):
        """
        Setter for property: ( IRayPlusStudioPreferencesBuilder.IRayPlusStudioStereoLayoutType NXOpen) StereoLayout
         Returns the Ray Traced Studio display image layout to use if rendering a stereo image   
            
         
        """
        pass
    @property
    def VrCamera(self) -> NXOpen.CartesianCoordinateSystem:
        """
        Getter for property: ( NXOpen.CartesianCoordinateSystem) VrCamera
         Returns the Ray Traced Studio display VR camera coordinate system   
            
         
        """
        pass
    @VrCamera.setter
    def VrCamera(self, vrCamera: NXOpen.CartesianCoordinateSystem):
        """
        Setter for property: ( NXOpen.CartesianCoordinateSystem) VrCamera
         Returns the Ray Traced Studio display VR camera coordinate system   
            
         
        """
        pass
    @property
    def VrEnabledToggle(self) -> bool:
        """
        Getter for property: (bool) VrEnabledToggle
         Returns the Ray Traced Studio display if the image will be rendered in a VR-ready format   
            
         
        """
        pass
    @VrEnabledToggle.setter
    def VrEnabledToggle(self, vrEnabledToggle: bool):
        """
        Setter for property: (bool) VrEnabledToggle
         Returns the Ray Traced Studio display if the image will be rendered in a VR-ready format   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class LayerSettingsBuilder(NXOpen.TaggedObject): 
    """
    Represents a builder for object layer settings.
    """
    class LayerOptionType(Enum):
        """
        Members Include: 
         |Maintain|  Maintain layer 
         |Original|  Original layer 
         |Work|  Work layer 
         |UserDefined|  User specified layer 

        """
        Maintain: int
        Original: int
        Work: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> LayerSettingsBuilder.LayerOptionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Layer(self) -> int:
        """
        Getter for property: (int) Layer
         Returns the layer.  
          
                      
                    Used when the layer option is set to
                     Display::LayerSettingsBuilder::LayerOptionTypeUserDefined
                     . See  NXOpen::Layer::Constants  for 
                    valid layer values.
                      
                   
         
        """
        pass
    @Layer.setter
    def Layer(self, layer: int):
        """
        Setter for property: (int) Layer
         Returns the layer.  
          
                      
                    Used when the layer option is set to
                     Display::LayerSettingsBuilder::LayerOptionTypeUserDefined
                     . See  NXOpen::Layer::Constants  for 
                    valid layer values.
                      
                   
         
        """
        pass
    @property
    def LayerOption(self) -> LayerSettingsBuilder.LayerOptionType:
        """
        Getter for property: ( LayerSettingsBuilder.LayerOptionType NXOpen) LayerOption
         Returns the layer option.  
          
                    
                      
                    Note that all layer options may not be supported by the builder.
                    Refer  Display::LayerSettingsBuilder::IsValidLayerOption
                      to determine supported options.
                      
                   
         
        """
        pass
    @LayerOption.setter
    def LayerOption(self, layerOption: LayerSettingsBuilder.LayerOptionType):
        """
        Setter for property: ( LayerSettingsBuilder.LayerOptionType NXOpen) LayerOption
         Returns the layer option.  
          
                    
                      
                    Note that all layer options may not be supported by the builder.
                    Refer  Display::LayerSettingsBuilder::IsValidLayerOption
                      to determine supported options.
                      
                   
         
        """
        pass
    def IsValidLayerOption(self, layerOption: LayerSettingsBuilder.LayerOptionType) -> bool:
        """
         Determines if the layer option is supported. 
                    
                    
                    The parent builder determines the validity of the layer options.
                    For example, following layer options are not relevant when the layer
                    is not being derived from another displayable object.
                    
                    Display.LayerSettingsBuilder.LayerOptionType.Maintain
                    Display.LayerSettingsBuilder.LayerOptionType.Original
                    
                    
                  
         Returns valid (bool): .
        """
        pass
import NXOpen
class LightBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Display.LightBuilder
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return .
    """
    class LightMode(Enum):
        """
        Members Include: 
         |FixedToObserver| 
         |FixedToThePart| 

        """
        FixedToObserver: int
        FixedToThePart: int
        @staticmethod
        def ValueOf(value: int) -> LightBuilder.LightMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ShadowType(Enum):
        """
        Members Include: 
         |NotSet|  No shadows will be produced. 
         |SoftEdged|  Soft-edged,approximated shadows will be generated using a shadow
                                                                               mapping algorithm. 
         |HardEdged|  Hard-edged, precise shadows will be generated using a ray-tracing
                                                                               algorithm. 
         |TranslucentHard|  Hard-edged, precise shadows will be generated using a ray-tracing
                                                                               algorithm.  Shadows from translucent objects will also be generated
                                                                               and their color will be determined by the transparent object's
                                                                               color. 

        """
        NotSet: int
        SoftEdged: int
        HardEdged: int
        TranslucentHard: int
        @staticmethod
        def ValueOf(value: int) -> LightBuilder.ShadowType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ConeAngle(self) -> float:
        """
        Getter for property: (float) ConeAngle
         Returns the cone angle - only applicable to spot light types   
            
         
        """
        pass
    @ConeAngle.setter
    def ConeAngle(self, coneAngle: float):
        """
        Setter for property: (float) ConeAngle
         Returns the cone angle - only applicable to spot light types   
            
         
        """
        pass
    @property
    def DestinationPosition(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) DestinationPosition
         Returns the destination position - only applicable to spot light types   
            
         
        """
        pass
    @DestinationPosition.setter
    def DestinationPosition(self, destinationPosition: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) DestinationPosition
         Returns the destination position - only applicable to spot light types   
            
         
        """
        pass
    @property
    def Intensity(self) -> float:
        """
        Getter for property: (float) Intensity
         Returns the brightness intensity for a given light   
            
         
        """
        pass
    @Intensity.setter
    def Intensity(self, intensity: float):
        """
        Setter for property: (float) Intensity
         Returns the brightness intensity for a given light   
            
         
        """
        pass
    @property
    def LightShadowType(self) -> LightBuilder.ShadowType:
        """
        Getter for property: ( LightBuilder.ShadowType NXOpen) LightShadowType
         Returns the light shadow type - not applicable to ambient or eye light types   
            
         
        """
        pass
    @LightShadowType.setter
    def LightShadowType(self, lightShadowType: LightBuilder.ShadowType):
        """
        Setter for property: ( LightBuilder.ShadowType NXOpen) LightShadowType
         Returns the light shadow type - not applicable to ambient or eye light types   
            
         
        """
        pass
    @property
    def LightType(self) -> LightType:
        """
        Getter for property: ( LightType NXOpen) LightType
         Returns the light type for a particular light   
            
         
        """
        pass
    @LightType.setter
    def LightType(self, lightType: LightType):
        """
        Setter for property: ( LightType NXOpen) LightType
         Returns the light type for a particular light   
            
         
        """
        pass
    @property
    def SourcePosition(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) SourcePosition
         Returns the source position - only applicable to spot and point light types   
            
         
        """
        pass
    @SourcePosition.setter
    def SourcePosition(self, sourcePosition: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) SourcePosition
         Returns the source position - only applicable to spot and point light types   
            
         
        """
        pass
    @property
    def UseWithAdvancedStudioImageBasedLighting(self) -> bool:
        """
        Getter for property: (bool) UseWithAdvancedStudioImageBasedLighting
         Returns the flag to indicate whether the given light is to be used with image based lighting in the advanced studio display.  
             
         
        """
        pass
    @UseWithAdvancedStudioImageBasedLighting.setter
    def UseWithAdvancedStudioImageBasedLighting(self, useWithAdvancedStudioIBL: bool):
        """
        Setter for property: (bool) UseWithAdvancedStudioImageBasedLighting
         Returns the flag to indicate whether the given light is to be used with image based lighting in the advanced studio display.  
             
         
        """
        pass
    @property
    def UseWithIbl(self) -> bool:
        """
        Getter for property: (bool) UseWithIbl
         Returns the use_with_ibl flag for a given light   
            
         
        """
        pass
    @UseWithIbl.setter
    def UseWithIbl(self, useWithIBL: bool):
        """
        Setter for property: (bool) UseWithIbl
         Returns the use_with_ibl flag for a given light   
            
         
        """
        pass
    @property
    def UseWithRayTracedImageBasedLighting(self) -> bool:
        """
        Getter for property: (bool) UseWithRayTracedImageBasedLighting
         Returns the flag to indicate whether the given light is to be used with image based lighting in ray traced rendering.  
             
         
        """
        pass
    @UseWithRayTracedImageBasedLighting.setter
    def UseWithRayTracedImageBasedLighting(self, useWithRayTracedIBL: bool):
        """
        Setter for property: (bool) UseWithRayTracedImageBasedLighting
         Returns the flag to indicate whether the given light is to be used with image based lighting in ray traced rendering.  
             
         
        """
        pass
import NXOpen
class Lighting(NXOpen.Builder): 
    """
    Represents a NXOpen.Display.Lighting
    Lights are used to illuminate the scene in Shaded and Studio rendering
    styles, as well as in High Quality Images.
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return .
    """
    class LightingCollectionType(Enum):
        """
        Members Include: 
         |Lighting1| 
         |Lighting2| 
         |Lighting3| 
         |Lighting4| 
         |Lighting5| 
         |UserDefined| 

        """
        Lighting1: int
        Lighting2: int
        Lighting3: int
        Lighting4: int
        Lighting5: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> Lighting.LightingCollectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LightingSet(Enum):
        """
        Members Include: 
         |Scene| 
         |Analysis| 

        """
        Scene: int
        Analysis: int
        @staticmethod
        def ValueOf(value: int) -> Lighting.LightingSet:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def LightsShadedViewsLightingCollection(self) -> Lighting.LightingCollectionType:
        """
        Getter for property: ( Lighting.LightingCollectionType NXOpen) LightsShadedViewsLightingCollection
         Returns the Shaded Views lighting collection   
            
         
        """
        pass
    @LightsShadedViewsLightingCollection.setter
    def LightsShadedViewsLightingCollection(self, lightingCollectionEnum: Lighting.LightingCollectionType):
        """
        Setter for property: ( Lighting.LightingCollectionType NXOpen) LightsShadedViewsLightingCollection
         Returns the Shaded Views lighting collection   
            
         
        """
        pass
    @property
    def LightsShadedViewsSceneDimmerValue(self) -> float:
        """
        Getter for property: (float) LightsShadedViewsSceneDimmerValue
         Returns the scene dimmer value   
            
         
        """
        pass
    @LightsShadedViewsSceneDimmerValue.setter
    def LightsShadedViewsSceneDimmerValue(self, sceneDimmerValue: float):
        """
        Setter for property: (float) LightsShadedViewsSceneDimmerValue
         Returns the scene dimmer value   
            
         
        """
        pass
    def EnableLightsOfLightSet(self, lightSet: Lighting.LightingSet) -> None:
        """
         Enables lights from the active light set 
        """
        pass
    def GetLightBuilderFromList(self, index: int) -> LightBuilder:
        """
         Returns a light builder, given by the index, in the array of lights assigned to the work view 
         Returns light ( LightBuilder NXOpen):  the light builder .
        """
        pass
    def GetNumLightBuilders(self) -> int:
        """
         Returns the total number of light builders in the given lighting list 
         Returns total_lights (int):  total lights in the light builder array .
        """
        pass
    def RemoveLightBuilderInList(self, lightName: str) -> None:
        """
         Removes a light builder by light name
        """
        pass
    @overload
    def SetLightBuilderInList(self, index: int, light: LightBuilder) -> None:
        """
         Sets a light builder in the array at the given index 
        """
        pass
    @overload
    def SetLightBuilderInList(self, lightName: str, lightIntensity: float) -> None:
        """
         Sets a light builder in the array at the given light name and intensity 
        """
        pass
class LightType(Enum):
    """
    Members Include: 
     |Ambient|  An ambient light provides global illumination
                                             for the scene.  It does not cause shadows, and illuminates
                                             all objects equally regardless of the orientation. You can
                                             control the intensity and color. 
     |Distant|  A distant light can be thought of as being
                                             located for all practical purposes infinitely far away,
                                             such as the sun.  You can control the intensity, color,
                                             and a vector that defines the direction of the light.
                                             A distant light can cast shadows in High Quality Images
                                             and requires the computation to determine shadowing. 
     |Eye|  An eye light is Located at the viewpoint or directly
                                             on the Z axis of the screen. You can control
                                             the color and intensity.  An eye light cannot cause
                                             shadows in your scene. 
     |Point|  A point light emits light equally in all directions.
                                             You can specify the location, intensity, and color.
                                             You can also set it to generate shadows in
                                             High Quality Images. The default position for
                                             point lights is in the right-hand corner
                                             of the view. 
     |Spot|  A spot light is the same as a point light,
                                             except that it is constrained by a cone shape.
                                             You can specify the location, intensity, and color.
                                             You can also set it to generate shadows in High Quality
                                             Images.  The default light source position for spot lights
                                             is in the upper right corner of the view.  The
                                             default target position is the center of the view. 
     |Scene|  A scene lights is a light whose parameters, except for
                                             intensity, are fixed.  Interactively, these lights
                                             may be modified only in the Basic Lights dialog,
                                             while the other light types may be modified only
                                             in the Advanced Lights dialog. 

    """
    Ambient: int
    Distant: int
    Eye: int
    Point: int
    Spot: int
    Scene: int
    @staticmethod
    def ValueOf(value: int) -> LightType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class NonProportionalZoom(NXOpen.Builder): 
    """ Provides non-proportional zoom capability """
    class MethodType(Enum):
        """
        Members Include: 
         |Rectangle|  Uses a rectangular region to be zoomed. 
         |Dynamic|  Defines a line to define aspect ratio of non-proportional zoom. 

        """
        Rectangle: int
        Dynamic: int
        @staticmethod
        def ValueOf(value: int) -> NonProportionalZoom.MethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AnchorCenter(self) -> bool:
        """
        Getter for property: (bool) AnchorCenter
         Returns a value indicating if the display will be recentered on the initial line endpoint   
            
         
        """
        pass
    @AnchorCenter.setter
    def AnchorCenter(self, anchorCenter: bool):
        """
        Setter for property: (bool) AnchorCenter
         Returns a value indicating if the display will be recentered on the initial line endpoint   
            
         
        """
        pass
    @property
    def Method(self) -> NonProportionalZoom.MethodType:
        """
        Getter for property: ( NonProportionalZoom.MethodType NXOpen) Method
         Returns the type of mouse interaction used to define the non-proportional zoom.  
             
         
        """
        pass
    @Method.setter
    def Method(self, method: NonProportionalZoom.MethodType):
        """
        Setter for property: ( NonProportionalZoom.MethodType NXOpen) Method
         Returns the type of mouse interaction used to define the non-proportional zoom.  
             
         
        """
        pass
    @property
    def ZoomSensitivity(self) -> int:
        """
        Getter for property: (int) ZoomSensitivity
         Returns the sensitivity of the zoom relative to the length of the drawn line   
            
         
        """
        pass
    @ZoomSensitivity.setter
    def ZoomSensitivity(self, sensitivity: int):
        """
        Setter for property: (int) ZoomSensitivity
         Returns the sensitivity of the zoom relative to the length of the drawn line   
            
         
        """
        pass
    def Enable(self, enable: bool) -> None:
        """
         Enables non-proportional zoom.
                 In batch mode, the the aspect ratio, scale and center of the view are modified,
                but no display occurs.  
        """
        pass
    def Finish(self, view: NXOpen.View) -> None:
        """
         Signals the completion of a non-proportional zoom defined by one or more pairs
                    of points defined by a mouse gesture. 
        """
        pass
    def FirstPoint(self, point1: NXOpen.Point3d, view: NXOpen.View) -> None:
        """
         Scales the specified view non-proportionally in the horizontal (X) and vertical (Y)
                dimensions, based on a mouse gesture defined by two points in a view.  Based on
                NXOpen.Display.NonProportionalZoom.MethodType setting, the gesture may be
                interpreted as a bounding box or a line, but will determine the XY aspect ratio and the zoom.
                 In batch mode, the the aspect ratio, scale and center of the view are modified,
                but no display occurs.  
        """
        pass
    def SecondPoint(self, point2: NXOpen.Point3d, view: NXOpen.View) -> None:
        """
         Scales the specified view non-proportionally in the horizontal (X) and vertical (Y)
                dimensions, based on a mouse gesture defined by two points in a view.  Call this once
                for every call to first point, to redefine a non-proportional zoom.
                 In batch mode, the the aspect ratio, scale and center of the view are modified,
                but no display occurs.  
        """
        pass
    def Start(self, view: NXOpen.View) -> None:
        """
         Prepares NX to receive one or more gestures delimited by pairs of points
                which define a non-proportional zoom.  This function records the display state
                to which the view will return when non-proportional zoom is disabled. In a typical
                scenario, call start.  Then call first point accompanied by one or more calls to
                second point, followed by a call to finish, followed optionaly by further 
                first pointsecond pointfinish combinations of calls. 
        """
        pass
import NXOpen
class PerspectiveOptionsBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Display.PerspectiveOptionsBuilder
    """
    @property
    def CameraDistance(self) -> float:
        """
        Getter for property: (float) CameraDistance
         Returns the camera distance:  The distance from the camera's position to the
                    target position in the work view view when it is a perspective view.  
          
                    The camera distance has no meaning for an orthographic view, so this property is not
                    applicable if the work view is an orthographic view.           
                  
         
        """
        pass
    @CameraDistance.setter
    def CameraDistance(self, cameraDistance: float):
        """
        Setter for property: (float) CameraDistance
         Returns the camera distance:  The distance from the camera's position to the
                    target position in the work view view when it is a perspective view.  
          
                    The camera distance has no meaning for an orthographic view, so this property is not
                    applicable if the work view is an orthographic view.           
                  
         
        """
        pass
    def ApplyLastDistanceChange(self) -> None:
        """
         Sets the work view to have the camera distance, which is the distance from the camera's
                    position to the target position in the work view which was specified in the last use of
                    NXOpen.Display.PerspectiveOptionsBuilder.CameraDistance
                    The camera distance has no meaning for an orthographic view, so this method does nothing
                    if the work view is an orthographic view.
                
        """
        pass
    def Cancel(self) -> None:
        """
         Cancels the Perspective Options Builder.  The camera distance of the work view
                    is restored to the value it had when the builder was created.
                    The camera distance has no meaning for an orthographic view, so this method does nothing
                    if the work view is an orthographic view.
                
        """
        pass
import NXOpen
class PlanarShipGridBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Display.PlanarShipGrid builder. """
    class IntersectOption(Enum):
        """
        Members Include: 
         |Everything|  all objects will be searched for intersections with the plane 
         |SelectedObjects|  only the selected objects will be searched for intersections with the plane 
         |ShipGridAndSelected|  intersect the ship grid and selected objects with the plane 

        """
        Everything: int
        SelectedObjects: int
        ShipGridAndSelected: int
        @staticmethod
        def ValueOf(value: int) -> PlanarShipGridBuilder.IntersectOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LabelDisplayOption(Enum):
        """
        Members Include: 
         |ShowAll|  Display label for every grid line 
         |ShowEveryOther|  Display label for every other grid line 
         |ShowEveryThird|  Display label for every third grid line 
         |ShowEveryFourth|  Display label for every fourth grid line 
         |HideAll|  Hide label for all grid lines 

        """
        ShowAll: int
        ShowEveryOther: int
        ShowEveryThird: int
        ShowEveryFourth: int
        HideAll: int
        @staticmethod
        def ValueOf(value: int) -> PlanarShipGridBuilder.LabelDisplayOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BasePlane(self) -> NXOpen.DatumPlane:
        """
        Getter for property: ( NXOpen.DatumPlane) BasePlane
         Returns the base plane where the planar ship grid is created.  
             
         
        """
        pass
    @BasePlane.setter
    def BasePlane(self, basePlane: NXOpen.DatumPlane):
        """
        Setter for property: ( NXOpen.DatumPlane) BasePlane
         Returns the base plane where the planar ship grid is created.  
             
         
        """
        pass
    @property
    def IntersectType(self) -> PlanarShipGridBuilder.IntersectOption:
        """
        Getter for property: ( PlanarShipGridBuilder.IntersectOption NXOpen) IntersectType
         Returns the value that determines how to find objects that intersect the plane.  
             
         
        """
        pass
    @IntersectType.setter
    def IntersectType(self, intersectType: PlanarShipGridBuilder.IntersectOption):
        """
        Setter for property: ( PlanarShipGridBuilder.IntersectOption NXOpen) IntersectType
         Returns the value that determines how to find objects that intersect the plane.  
             
         
        """
        pass
    @property
    def LabelColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) LabelColor
         Returns the grid line label color.  
           Only used if the color is not inherited from the intersected plane.  
         
        """
        pass
    @LabelColor.setter
    def LabelColor(self, labelColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) LabelColor
         Returns the grid line label color.  
           Only used if the color is not inherited from the intersected plane.  
         
        """
        pass
    @property
    def LabelDisplayType(self) -> PlanarShipGridBuilder.LabelDisplayOption:
        """
        Getter for property: ( PlanarShipGridBuilder.LabelDisplayOption NXOpen) LabelDisplayType
         Returns the setting that indicates what grid lines are to be labelled.  
             
         
        """
        pass
    @LabelDisplayType.setter
    def LabelDisplayType(self, labelDisplayType: PlanarShipGridBuilder.LabelDisplayOption):
        """
        Setter for property: ( PlanarShipGridBuilder.LabelDisplayOption NXOpen) LabelDisplayType
         Returns the setting that indicates what grid lines are to be labelled.  
             
         
        """
        pass
    @property
    def LabelSettingInheritted(self) -> bool:
        """
        Getter for property: (bool) LabelSettingInheritted
         Returns the setting that indicates whether the grid line label will inherit the intersected plane's color   
            
         
        """
        pass
    @LabelSettingInheritted.setter
    def LabelSettingInheritted(self, labelSettingInheritted: bool):
        """
        Setter for property: (bool) LabelSettingInheritted
         Returns the setting that indicates whether the grid line label will inherit the intersected plane's color   
            
         
        """
        pass
    @property
    def LineColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) LineColor
         Returns the grid line color.  
           Only used if the color is not inherited from the intersected plane.   
         
        """
        pass
    @LineColor.setter
    def LineColor(self, lineColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) LineColor
         Returns the grid line color.  
           Only used if the color is not inherited from the intersected plane.   
         
        """
        pass
    @property
    def LineFontType(self) -> NXOpen.DisplayableObject.ObjectFont:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectFont) LineFontType
         Returns the grid line font.  
           Only used if the font is not inherited from the intersected plane.   
         
        """
        pass
    @LineFontType.setter
    def LineFontType(self, lineFontType: NXOpen.DisplayableObject.ObjectFont):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectFont) LineFontType
         Returns the grid line font.  
           Only used if the font is not inherited from the intersected plane.   
         
        """
        pass
    @property
    def LineSettingInheritted(self) -> bool:
        """
        Getter for property: (bool) LineSettingInheritted
         Returns the setting that indicates whether the grid line will inherit the intersected plane's colorfontwidth.  
             
         
        """
        pass
    @LineSettingInheritted.setter
    def LineSettingInheritted(self, lineSettingInheritted: bool):
        """
        Setter for property: (bool) LineSettingInheritted
         Returns the setting that indicates whether the grid line will inherit the intersected plane's colorfontwidth.  
             
         
        """
        pass
    @property
    def LineWidthType(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectWidth) LineWidthType
         Returns the grid line width.  
           Only used if the width is not inherited from the intersected plane.   
         
        """
        pass
    @LineWidthType.setter
    def LineWidthType(self, lineWidthType: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectWidth) LineWidthType
         Returns the grid line width.  
           Only used if the width is not inherited from the intersected plane.   
         
        """
        pass
    def GetExtent(self) -> Tuple[bool, NXOpen.Point3d, NXOpen.Point3d, NXOpen.Point3d, NXOpen.Point3d]:
        """
                  Get corner points of the grid extent. The extent is a rectangle.
                  The four points: point1, point2, point3, point4 are in clockwise 
                  or counterclockwise direction.
                 
         Returns A tuple consisting of (valid, point1, point2, point3, point4). 
         - valid is: bool. Flag indicating whether the corner points are valid .
         - point1 is:  NXOpen.Point3d. First corner point .
         - point2 is:  NXOpen.Point3d. Second corner point .
         - point3 is:  NXOpen.Point3d. Third corner point .
         - point4 is:  NXOpen.Point3d. Fourth corner point .

        """
        pass
    def GetIntersectedObjects(self) -> List[NXOpen.TaggedObject]:
        """
         Get the objects that were searched to find intersections with the plane. 
         Returns intersectedObjects ( NXOpen.TaggedObject Li):  Array of intersected objects .
        """
        pass
    def SetExtent(self, point1: NXOpen.Point3d, point2: NXOpen.Point3d, point3: NXOpen.Point3d, point4: NXOpen.Point3d) -> bool:
        """
                  Set corner points for the grid extent. The extent is a rectangle.
                  The four points: point1, point2, point3, point4 should be in
                  clockwise or counterclockwise direction.
                 
         Returns valid (bool):  Flag indicating whether the corner points are valid .
        """
        pass
    def SetIntersectedObjects(self, intersectedObjects: List[NXOpen.TaggedObject]) -> None:
        """
         Set the objects that are to be searched to find intersections with the plane. 
        """
        pass
    def SetRealLineFontType(self, lineFontType: NXOpen.DisplayableObject.ObjectFont) -> None:
        """
         Sets the real font type. 
        """
        pass
    def SwitchLabelLocationX(self) -> None:
        """
         Switch label location in X direction. 
        """
        pass
    def SwitchLabelLocationY(self) -> None:
        """
         Switch label location in Y direction.
        """
        pass
    def SwitchLabelLocationZ(self) -> None:
        """
         Switch label location in Z direction. 
        """
        pass
import NXOpen
class PlanarShipGrid(EntitySelectionPlane): 
    """ Represents a planar ship grid. """
    def AddDatumPlanes(self, datumplaneTags: List[NXOpen.DatumPlane]) -> None:
        """
         Adds intersected datum planes into the planar grid. 
        """
        pass
    def IsDatumPlaneInGrid(self, datumplaneTag: NXOpen.DatumPlane) -> bool:
        """
         Returns the flag to indicate whether the specific datum plane is in grid or not. 
         Returns datumInGrid (bool): .
        """
        pass
    def RemoveDatumPlanes(self, datumplaneTags: List[NXOpen.DatumPlane]) -> None:
        """
         Removes the specific datum planes from the planar grid. 
        """
        pass
import NXOpen
class PlaneGridBuilder(BoundedGridBuilder): 
    """ Represents the builder for adding a bounded grid NXOpen.Display.PlaneGrid 
        to a plane.
    """
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
class PlaneGrid(BoundedGrid): 
    """ Represents a grid on a bounded plane """
    pass
import NXOpen
class PointCloudBuilder(NXOpen.Builder): 
    """ Represents a Display.PointCloudBuilder.
    NXOpen.Display.PointCloudis a cloud object based on an
    imported point data files file (e.g. a POD file from Bentley). The point data
    (list of coordinates) itself won't be stored within NX part file but an object
    ("Reference Point Cloud") is created which references to the point data file
    and stores several meta data like clipping areas, display and current location.
    When loaded the point cloud will be visible as defined in the object parameters.
    Access to the point cloud like display, measurement, blankingshowing, sectioning,
    POD file loading will requires license checkout of the new basic point cloud 
    license. For deleting a Reference Point Cloud object the license is not required.
    """
    class BrightnessModes(Enum):
        """
        Members Include: 
         |Uniform|  uniform 
         |Shaded|  Shaded 

        """
        Uniform: int
        Shaded: int
        @staticmethod
        def ValueOf(value: int) -> PointCloudBuilder.BrightnessModes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ColorModes(Enum):
        """
        Members Include: 
         |Individual|  individual 
         |Uniform|  uniform 

        """
        Individual: int
        Uniform: int
        @staticmethod
        def ValueOf(value: int) -> PointCloudBuilder.ColorModes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ClippingBoxesList(self) -> PointCloudClippingBoxesListItemBuilderList:
        """
        Getter for property: ( PointCloudClippingBoxesListItemBuilderList NXOpen) ClippingBoxesList
         Returns the list of  NXOpen::Display::PointCloudClippingBoxesListItemBuilder  defining the clipping boxes parameters.  
             
         
        """
        pass
    @property
    def LoadPointDataWithPart(self) -> bool:
        """
        Getter for property: (bool) LoadPointDataWithPart
         Returns the indication if the point cloud data will be loaded with part load.  
             
         
        """
        pass
    @LoadPointDataWithPart.setter
    def LoadPointDataWithPart(self, loadPointDataWithPart: bool):
        """
        Setter for property: (bool) LoadPointDataWithPart
         Returns the indication if the point cloud data will be loaded with part load.  
             
         
        """
        pass
    @property
    def PointBrightnessMode(self) -> PointCloudBuilder.BrightnessModes:
        """
        Getter for property: ( PointCloudBuilder.BrightnessModes NXOpen) PointBrightnessMode
         Returns the point brightness display mode   
            
         
        """
        pass
    @PointBrightnessMode.setter
    def PointBrightnessMode(self, pointBrightnessMode: PointCloudBuilder.BrightnessModes):
        """
        Setter for property: ( PointCloudBuilder.BrightnessModes NXOpen) PointBrightnessMode
         Returns the point brightness display mode   
            
         
        """
        pass
    @property
    def PointColorMode(self) -> PointCloudBuilder.ColorModes:
        """
        Getter for property: ( PointCloudBuilder.ColorModes NXOpen) PointColorMode
         Returns the point color display mode   
            
         
        """
        pass
    @PointColorMode.setter
    def PointColorMode(self, pointColorMode: PointCloudBuilder.ColorModes):
        """
        Setter for property: ( PointCloudBuilder.ColorModes NXOpen) PointColorMode
         Returns the point color display mode   
            
         
        """
        pass
    @property
    def PointDataFile(self) -> str:
        """
        Getter for property: (str) PointDataFile
         Returns the point cloud data file.  
             
         
        """
        pass
    @PointDataFile.setter
    def PointDataFile(self, filename: str):
        """
        Setter for property: (str) PointDataFile
         Returns the point cloud data file.  
             
         
        """
        pass
    @property
    def PointDensity(self) -> float:
        """
        Getter for property: (float) PointDensity
         Returns the point density   
            
         
        """
        pass
    @PointDensity.setter
    def PointDensity(self, pointDensity: float):
        """
        Setter for property: (float) PointDensity
         Returns the point density   
            
         
        """
        pass
    @property
    def PointSize(self) -> int:
        """
        Getter for property: (int) PointSize
         Returns the point size   
            
         
        """
        pass
    @PointSize.setter
    def PointSize(self, pointSize: int):
        """
        Setter for property: (int) PointSize
         Returns the point size   
            
         
        """
        pass
    def CreateClippingBoxesListItemBuilder(self) -> PointCloudClippingBoxesListItemBuilder:
        """
         Creates a Display.PointCloudClippingBoxesListItemBuilder. 
         Returns listitem ( PointCloudClippingBoxesListItemBuilder NXOpen): .
        """
        pass
    def LoadPointData(self) -> None:
        """
         Loads the selected point cloud data now. 
        """
        pass
import NXOpen
class PointCloudClippingBoxesListItemBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[PointCloudClippingBoxesListItemBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: PointCloudClippingBoxesListItemBuilder) -> None:
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
    def Erase(self, obj: PointCloudClippingBoxesListItemBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: PointCloudClippingBoxesListItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: PointCloudClippingBoxesListItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> PointCloudClippingBoxesListItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( PointCloudClippingBoxesListItemBuilder NXOpen):  object found at input index .
        """
        pass
    def GetContents(self) -> List[PointCloudClippingBoxesListItemBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( PointCloudClippingBoxesListItemBuilder List[NXOp):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: PointCloudClippingBoxesListItemBuilder) -> None:
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
    def SetContents(self, objects: List[PointCloudClippingBoxesListItemBuilder]) -> None:
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
    def Swap(self, object1: PointCloudClippingBoxesListItemBuilder, object2: PointCloudClippingBoxesListItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class PointCloudClippingBoxesListItemBuilder(NXOpen.TaggedObject): 
    """ Represents a NXOpen.Display.PointCloudClippingBoxesListItemBuilder 
    to create clipping regions for NXOpen.Display.PointCloud. 
     """
    class ClippingSides(Enum):
        """
        Members Include: 
         |Inside|  inside 
         |Outside|  outside 
         |NotSet|  none 

        """
        Inside: int
        Outside: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> PointCloudClippingBoxesListItemBuilder.ClippingSides:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ClippingEndPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) ClippingEndPoint
         Returns the end point of the clipping box diagonal   
            
         
        """
        pass
    @ClippingEndPoint.setter
    def ClippingEndPoint(self, clippingEndPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) ClippingEndPoint
         Returns the end point of the clipping box diagonal   
            
         
        """
        pass
    @property
    def ClippingSide(self) -> PointCloudClippingBoxesListItemBuilder.ClippingSides:
        """
        Getter for property: ( PointCloudClippingBoxesListItemBuilder.ClippingSides NXOpen) ClippingSide
         Returns the clipping side of the defined clipping box   
            
         
        """
        pass
    @ClippingSide.setter
    def ClippingSide(self, clippingSide: PointCloudClippingBoxesListItemBuilder.ClippingSides):
        """
        Setter for property: ( PointCloudClippingBoxesListItemBuilder.ClippingSides NXOpen) ClippingSide
         Returns the clipping side of the defined clipping box   
            
         
        """
        pass
    @property
    def ClippingStartPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) ClippingStartPoint
         Returns the start point of the clipping box diagonal.  
             
         
        """
        pass
    @ClippingStartPoint.setter
    def ClippingStartPoint(self, clippingStartPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) ClippingStartPoint
         Returns the start point of the clipping box diagonal.  
             
         
        """
        pass
    @property
    def Orientation(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: ( NXOpen.Matrix3x3) Orientation
         Returns the orientation of clipping box   
            
         
        """
        pass
import NXOpen
class PointCloudCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of point cloud objects """
    def CreatePointCloudBuilder(self, referencePointCloud: PointCloud) -> PointCloudBuilder:
        """
         Creates a NXOpen.Display.PointCloudBuilder object
                    used to build a point cloud.
                    If the referencePointCloud is not , the referencePointCloud object will be edited.
                 
         Returns builder ( PointCloudBuilder NXOpen):  Point cloud builder .
        """
        pass
    def FindObject(self, journalIdentifier: str) -> PointCloud:
        """
         Finds the NXOpen.Display.PointCloud with the given   
                    identifier as recorded in a journal. An object may not return the same  
                    value as its JournalIdentifier in different versions of the software.   
                    However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In 
                    general, this method should not be used in handwritten code and exists 
                    to support record and playback of journals.
                    
                    An exception will be thrown if no object can be found with the given 
                    journal identifier. 
                    
                
         Returns referencePointCloud ( PointCloud NXOpen):  Reference point cloud found .
        """
        pass
import NXOpen
class PointCloud(NXOpen.DisplayableObject): 
    """ Represents a NXOpen.Display.PointCloud imported from point data files. 
    """
    def Load(self) -> None:
        """
         Loads the selected point cloud. 
        """
        pass
    def Unload(self) -> None:
        """
         Unloads the selected point cloud. 
        """
        pass
import NXOpen
class RasterImageBuilder(ImageBaseBuilder): 
    """ Represents a NXOpen.Display.RasterImageBuilder. 
    NXOpen.Display.RasterImage provides placing an imported image 
    onto a plane (with controls for orientation, sizing, and display) to use as
    a reference in the model to create geometry. 
    """
    @property
    def Target(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) Target
         Returns the plane the raster image is placed onto   
            
         
        """
        pass
    @Target.setter
    def Target(self, targetObject: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) Target
         Returns the plane the raster image is placed onto   
            
         
        """
        pass
class RasterImage(ImageBase): 
    """ Represents a NXOpen.Display.RasterImage that provides 
    placing an imported image onto a plane (with controls for orientation, 
    sizing, and display) to use as a reference in the model to create geometry.
    """
    pass
import NXOpen
class RayTracedStudioBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Display.RayTracedStudioBuilder.
    Ray Traced Studio displays CPU-based real-time ray tracing results of a model
    dynamically.
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return .
    """
    class StationaryDisplayQualityType(Enum):
        """
        Members Include: 
         |High|  Very good ray traced display quality (Photoreal for Iray+) 
         |Medium|  Good ray traced display quality with good performance (Qualtiy Interactive for Iray+) 
         |Low|  The fastest ray traced display performance with preview quality (Fast Interactive for Iray+) 

        """
        High: int
        Medium: int
        Low: int
        @staticmethod
        def ValueOf(value: int) -> RayTracedStudioBuilder.StationaryDisplayQualityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Brightness(self) -> float:
        """
        Getter for property: (float) Brightness
         Returns the brightness for Iray Tonemap setting   
            
         
        """
        pass
    @Brightness.setter
    def Brightness(self, brightness: float):
        """
        Setter for property: (float) Brightness
         Returns the brightness for Iray Tonemap setting   
            
         
        """
        pass
    @property
    def StationaryQuality(self) -> RayTracedStudioBuilder.StationaryDisplayQualityType:
        """
        Getter for property: ( RayTracedStudioBuilder.StationaryDisplayQualityType NXOpen) StationaryQuality
         Returns the Ray Traced Studio stationary display quality when dynamic interaction stops   
            
         
        """
        pass
    @StationaryQuality.setter
    def StationaryQuality(self, stationaryQuality: RayTracedStudioBuilder.StationaryDisplayQualityType):
        """
        Setter for property: ( RayTracedStudioBuilder.StationaryDisplayQualityType NXOpen) StationaryQuality
         Returns the Ray Traced Studio stationary display quality when dynamic interaction stops   
            
         
        """
        pass
    def RayTracedAnimationPause(self) -> None:
        """
         Pause the Ray Traced Studio Animation render. 
        """
        pass
    def RayTracedAnimationResume(self) -> None:
        """
         Resume the Ray Traced Studio Animation render after it has been paused. 
        """
        pass
    def RayTracedAnimationStart(self) -> None:
        """
         Launch an RTS batch render job based on Animation Designer solution 
        """
        pass
    def RayTracedAnimationStop(self) -> None:
        """
         Stop the Ray Traced Studio Animation render after it has been paused. 
        """
        pass
    def RayTracedEditor(self) -> None:
        """
         Launch the Ray Traced Studio Editor command 
        """
        pass
    def RayTracedPreferences(self) -> None:
        """
         Launch the Ray Traced Studio Preferences command 
        """
        pass
    def RayTracedRenderingErase(self) -> None:
        """
         Erase Ray Traced Studio static (still) image from the Ray Traced Studio window 
        """
        pass
    def RayTracedRenderingSave(self) -> None:
        """
         Save a copy of the Ray Traced Studio static (still) image display from the window to an image file 
        """
        pass
    def RayTracedRenderingStart(self) -> None:
        """
         Start Ray Traced Studio static image rendering 
        """
        pass
    def StartRayTracedDisplay(self) -> None:
        """
         Start the Ray Traced Studio display after it has been stopped using the Stop action. 
        """
        pass
    def StopRayTracedDisplay(self) -> None:
        """
         Stop the Ray Traced Studio progressive display.  Use the Start action to re-start the display. 
        """
        pass
    def UpdateRayTracedDisplay(self) -> None:
        """
         Update the Ray Traced Studio display.  Use when geometry has changed to completely regenerate the display.  
        """
        pass
import NXOpen
class RayTracedStudioEditorBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Display.RayTracedStudioEditorBuilder.
    Ray Traced Studio Editor controls display and output of CPU-based real-time ray tracing.
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return .
    """
    class DynamicRayTracedStudioTilingQualityType(Enum):
        """
        Members Include: 
         |High|  Very small tiles used during progressive updates of ray traced display 
         |Medium|  Medium sized tiles used during progressive updates of ray traced display 
         |Low|  Larger tiles used during progressive updates of ray traced display for faster display time 

        """
        High: int
        Medium: int
        Low: int
        @staticmethod
        def ValueOf(value: int) -> RayTracedStudioEditorBuilder.DynamicRayTracedStudioTilingQualityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RayTracedStudioStaticImageFileFormatType(Enum):
        """
        Members Include: 
         |Tif|  Tagged Image File Format (TIFF) file format 
         |Png|  Portable Network Graphic (PNG) file format 
         |Jpg|  Joint Photographic Experts Group (JPEG) file format 

        """
        Tif: int
        Png: int
        Jpg: int
        @staticmethod
        def ValueOf(value: int) -> RayTracedStudioEditorBuilder.RayTracedStudioStaticImageFileFormatType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RayTracedStudioStaticImageOrientationType(Enum):
        """
        Members Include: 
         |Landscape|  static image orientation where width is greater than height 
         |Portrait|  static image orientation where height is greater than width 

        """
        Landscape: int
        Portrait: int
        @staticmethod
        def ValueOf(value: int) -> RayTracedStudioEditorBuilder.RayTracedStudioStaticImageOrientationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RayTracedStudioStaticImageResolutionType(Enum):
        """
        Members Include: 
         |High|  static image output resolution of 300 DPI (dots per inch) 
         |Medium|  static image output resolution of 150 DPI (dots per inch) 
         |Low|  static image output resolution of 72 DPI (dots per inch) 
         |UserDefined|  user specified image output resolution in DPI (dots per inch) 

        """
        High: int
        Medium: int
        Low: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> RayTracedStudioEditorBuilder.RayTracedStudioStaticImageResolutionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RayTracedStudioStaticImageSizeType(Enum):
        """
        Members Include: 
         |RenderWindow|  Ray Traced Studio window size used for static image output 
         |UserDefined|  user specified size for static image output 

        """
        RenderWindow: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> RayTracedStudioEditorBuilder.RayTracedStudioStaticImageSizeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RayTracedStudioStaticImageUnitsType(Enum):
        """
        Members Include: 
         |Pixels|  static image size specified in pixel 
         |Millimeters|  static image size specified in millimeters 
         |Inches|  static image size specified in inches 

        """
        Pixels: int
        Millimeters: int
        Inches: int
        @staticmethod
        def ValueOf(value: int) -> RayTracedStudioEditorBuilder.RayTracedStudioStaticImageUnitsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StaticAntialiasingType(Enum):
        """
        Members Include: 
         |High|  Very good antialiasing performed for static image rendering 
         |Medium|  Good antialiasing performed for static image rendering 
         |Low|  Coarse antialiasing performed for static image rendering 
         |NotSet|  No antialiasing performed to provide quick, preview of ray traced display for static image rendering 

        """
        High: int
        Medium: int
        Low: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> RayTracedStudioEditorBuilder.StaticAntialiasingType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StaticRayTracedStudioQualityType(Enum):
        """
        Members Include: 
         |High|  Very good ray traced display quality for static image rendering 
         |Medium|  Good quality ray traced display with good performance for static image rendering 
         |Low|  The fastest ray traced display performance with preview quality for static image rendering 
         |UserDefined|  User specified ray traced display quality for static image rendering 

        """
        High: int
        Medium: int
        Low: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> RayTracedStudioEditorBuilder.StaticRayTracedStudioQualityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StationaryAntialiasingType(Enum):
        """
        Members Include: 
         |Medium|  Good antialiasing performed when dynamic interaction stops 
         |Low|  Coarse antialiasing performed when dynamic interaction stops 
         |NotSet|  No antialiasing performed to provide quick, preview of ray traced display when dynamic interaction stops 

        """
        Medium: int
        Low: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> RayTracedStudioEditorBuilder.StationaryAntialiasingType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StationaryRayTracedStudioQualityType(Enum):
        """
        Members Include: 
         |High|  Very good ray traced display quality when dynamic interaction stops 
         |Medium|  Good ray traced display quality with good performance when dynamic interaction stops 
         |Low|  The fastest ray traced display performance with preview quality when dynamic interaction stops 

        """
        High: int
        Medium: int
        Low: int
        @staticmethod
        def ValueOf(value: int) -> RayTracedStudioEditorBuilder.StationaryRayTracedStudioQualityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DynamicRayTracedStudioTilingQuality(self) -> RayTracedStudioEditorBuilder.DynamicRayTracedStudioTilingQualityType:
        """
        Getter for property: ( RayTracedStudioEditorBuilder.DynamicRayTracedStudioTilingQualityType NXOpen) DynamicRayTracedStudioTilingQuality
         Returns the Ray Traced Studio tiling quality during interactive dynamic display   
            
         
        """
        pass
    @DynamicRayTracedStudioTilingQuality.setter
    def DynamicRayTracedStudioTilingQuality(self, dynamicRayTracedStudioTilingQuality: RayTracedStudioEditorBuilder.DynamicRayTracedStudioTilingQualityType):
        """
        Setter for property: ( RayTracedStudioEditorBuilder.DynamicRayTracedStudioTilingQualityType NXOpen) DynamicRayTracedStudioTilingQuality
         Returns the Ray Traced Studio tiling quality during interactive dynamic display   
            
         
        """
        pass
    @property
    def RayTracedStudioDisplayGamma(self) -> float:
        """
        Getter for property: (float) RayTracedStudioDisplayGamma
         Returns the Ray Traced Studio display gamma, controls the overall contrast or brightness of the image's midtone values.  
            A higher gamma value yields an overall brighter image.   
         
        """
        pass
    @RayTracedStudioDisplayGamma.setter
    def RayTracedStudioDisplayGamma(self, rayTracedStudioDisplayGamma: float):
        """
        Setter for property: (float) RayTracedStudioDisplayGamma
         Returns the Ray Traced Studio display gamma, controls the overall contrast or brightness of the image's midtone values.  
            A higher gamma value yields an overall brighter image.   
         
        """
        pass
    @property
    def RayTracedStudioStaticImageDotsPerInch(self) -> int:
        """
        Getter for property: (int) RayTracedStudioStaticImageDotsPerInch
         Returns the Ray Traced Studio static image dots per inch (DPI)   
            
         
        """
        pass
    @RayTracedStudioStaticImageDotsPerInch.setter
    def RayTracedStudioStaticImageDotsPerInch(self, rayTracedStudioStaticImageDotsPerInch: int):
        """
        Setter for property: (int) RayTracedStudioStaticImageDotsPerInch
         Returns the Ray Traced Studio static image dots per inch (DPI)   
            
         
        """
        pass
    @property
    def RayTracedStudioStaticImageDoubleHeight(self) -> float:
        """
        Getter for property: (float) RayTracedStudioStaticImageDoubleHeight
         Returns the Ray Traced Studio static image height   
            
         
        """
        pass
    @RayTracedStudioStaticImageDoubleHeight.setter
    def RayTracedStudioStaticImageDoubleHeight(self, rayTracedStudioStaticImageDoubleHeight: float):
        """
        Setter for property: (float) RayTracedStudioStaticImageDoubleHeight
         Returns the Ray Traced Studio static image height   
            
         
        """
        pass
    @property
    def RayTracedStudioStaticImageDoubleWidth(self) -> float:
        """
        Getter for property: (float) RayTracedStudioStaticImageDoubleWidth
         Returns the Ray Traced Studio static image width   
            
         
        """
        pass
    @RayTracedStudioStaticImageDoubleWidth.setter
    def RayTracedStudioStaticImageDoubleWidth(self, rayTracedStudioStaticImageDoubleWidth: float):
        """
        Setter for property: (float) RayTracedStudioStaticImageDoubleWidth
         Returns the Ray Traced Studio static image width   
            
         
        """
        pass
    @property
    def RayTracedStudioStaticImageFileFormat(self) -> RayTracedStudioEditorBuilder.RayTracedStudioStaticImageFileFormatType:
        """
        Getter for property: ( RayTracedStudioEditorBuilder.RayTracedStudioStaticImageFileFormatType NXOpen) RayTracedStudioStaticImageFileFormat
         Returns the Ray Traced Studio static output image file format   
            
         
        """
        pass
    @RayTracedStudioStaticImageFileFormat.setter
    def RayTracedStudioStaticImageFileFormat(self, rayTracedStudioStaticImageFileFormat: RayTracedStudioEditorBuilder.RayTracedStudioStaticImageFileFormatType):
        """
        Setter for property: ( RayTracedStudioEditorBuilder.RayTracedStudioStaticImageFileFormatType NXOpen) RayTracedStudioStaticImageFileFormat
         Returns the Ray Traced Studio static output image file format   
            
         
        """
        pass
    @property
    def RayTracedStudioStaticImageLockAspectRatio(self) -> bool:
        """
        Getter for property: (bool) RayTracedStudioStaticImageLockAspectRatio
         Returns the Ray Traced Studio static image aspect ratio will be maintained   
            
         
        """
        pass
    @RayTracedStudioStaticImageLockAspectRatio.setter
    def RayTracedStudioStaticImageLockAspectRatio(self, rayTracedStudioStaticImageLockAspectRatio: bool):
        """
        Setter for property: (bool) RayTracedStudioStaticImageLockAspectRatio
         Returns the Ray Traced Studio static image aspect ratio will be maintained   
            
         
        """
        pass
    @property
    def RayTracedStudioStaticImageOrientation(self) -> RayTracedStudioEditorBuilder.RayTracedStudioStaticImageOrientationType:
        """
        Getter for property: ( RayTracedStudioEditorBuilder.RayTracedStudioStaticImageOrientationType NXOpen) RayTracedStudioStaticImageOrientation
         Returns the Ray Traced Studio static image orientation   
            
         
        """
        pass
    @RayTracedStudioStaticImageOrientation.setter
    def RayTracedStudioStaticImageOrientation(self, rayTracedStudioStaticImageOrientation: RayTracedStudioEditorBuilder.RayTracedStudioStaticImageOrientationType):
        """
        Setter for property: ( RayTracedStudioEditorBuilder.RayTracedStudioStaticImageOrientationType NXOpen) RayTracedStudioStaticImageOrientation
         Returns the Ray Traced Studio static image orientation   
            
         
        """
        pass
    @property
    def RayTracedStudioStaticImagePixelHeight(self) -> int:
        """
        Getter for property: (int) RayTracedStudioStaticImagePixelHeight
         Returns the Ray Traced Studio static image pixel height   
            
         
        """
        pass
    @RayTracedStudioStaticImagePixelHeight.setter
    def RayTracedStudioStaticImagePixelHeight(self, rayTracedStudioStaticImagePixelHeight: int):
        """
        Setter for property: (int) RayTracedStudioStaticImagePixelHeight
         Returns the Ray Traced Studio static image pixel height   
            
         
        """
        pass
    @property
    def RayTracedStudioStaticImagePixelWidth(self) -> int:
        """
        Getter for property: (int) RayTracedStudioStaticImagePixelWidth
         Returns the Ray Traced Studio static image pixel width   
            
         
        """
        pass
    @RayTracedStudioStaticImagePixelWidth.setter
    def RayTracedStudioStaticImagePixelWidth(self, rayTracedStudioStaticImagePixelWidth: int):
        """
        Setter for property: (int) RayTracedStudioStaticImagePixelWidth
         Returns the Ray Traced Studio static image pixel width   
            
         
        """
        pass
    @property
    def RayTracedStudioStaticImageResolution(self) -> RayTracedStudioEditorBuilder.RayTracedStudioStaticImageResolutionType:
        """
        Getter for property: ( RayTracedStudioEditorBuilder.RayTracedStudioStaticImageResolutionType NXOpen) RayTracedStudioStaticImageResolution
         Returns the Ray Traced Studio static image resolution   
            
         
        """
        pass
    @RayTracedStudioStaticImageResolution.setter
    def RayTracedStudioStaticImageResolution(self, rayTracedStudioStaticImageResolution: RayTracedStudioEditorBuilder.RayTracedStudioStaticImageResolutionType):
        """
        Setter for property: ( RayTracedStudioEditorBuilder.RayTracedStudioStaticImageResolutionType NXOpen) RayTracedStudioStaticImageResolution
         Returns the Ray Traced Studio static image resolution   
            
         
        """
        pass
    @property
    def RayTracedStudioStaticImageSize(self) -> RayTracedStudioEditorBuilder.RayTracedStudioStaticImageSizeType:
        """
        Getter for property: ( RayTracedStudioEditorBuilder.RayTracedStudioStaticImageSizeType NXOpen) RayTracedStudioStaticImageSize
         Returns the Ray Traced Studio static image size   
            
         
        """
        pass
    @RayTracedStudioStaticImageSize.setter
    def RayTracedStudioStaticImageSize(self, rayTracedStudioStaticImageSize: RayTracedStudioEditorBuilder.RayTracedStudioStaticImageSizeType):
        """
        Setter for property: ( RayTracedStudioEditorBuilder.RayTracedStudioStaticImageSizeType NXOpen) RayTracedStudioStaticImageSize
         Returns the Ray Traced Studio static image size   
            
         
        """
        pass
    @property
    def RayTracedStudioStaticImageUnits(self) -> RayTracedStudioEditorBuilder.RayTracedStudioStaticImageUnitsType:
        """
        Getter for property: ( RayTracedStudioEditorBuilder.RayTracedStudioStaticImageUnitsType NXOpen) RayTracedStudioStaticImageUnits
         Returns the Ray Traced Studio static image units   
            
         
        """
        pass
    @RayTracedStudioStaticImageUnits.setter
    def RayTracedStudioStaticImageUnits(self, rayTracedStudioStaticImageUnits: RayTracedStudioEditorBuilder.RayTracedStudioStaticImageUnitsType):
        """
        Setter for property: ( RayTracedStudioEditorBuilder.RayTracedStudioStaticImageUnitsType NXOpen) RayTracedStudioStaticImageUnits
         Returns the Ray Traced Studio static image units   
            
         
        """
        pass
    @property
    def StaticAntialiasing(self) -> RayTracedStudioEditorBuilder.StaticAntialiasingType:
        """
        Getter for property: ( RayTracedStudioEditorBuilder.StaticAntialiasingType NXOpen) StaticAntialiasing
         Returns the Ray Traced Studio static image antialiasing quality   
            
         
        """
        pass
    @StaticAntialiasing.setter
    def StaticAntialiasing(self, staticAntialiasing: RayTracedStudioEditorBuilder.StaticAntialiasingType):
        """
        Setter for property: ( RayTracedStudioEditorBuilder.StaticAntialiasingType NXOpen) StaticAntialiasing
         Returns the Ray Traced Studio static image antialiasing quality   
            
         
        """
        pass
    @property
    def StaticRayTracedStudioQuality(self) -> RayTracedStudioEditorBuilder.StaticRayTracedStudioQualityType:
        """
        Getter for property: ( RayTracedStudioEditorBuilder.StaticRayTracedStudioQualityType NXOpen) StaticRayTracedStudioQuality
         Returns the Ray Traced Studio static image quality   
            
         
        """
        pass
    @StaticRayTracedStudioQuality.setter
    def StaticRayTracedStudioQuality(self, staticRayTracedStudioQuality: RayTracedStudioEditorBuilder.StaticRayTracedStudioQualityType):
        """
        Setter for property: ( RayTracedStudioEditorBuilder.StaticRayTracedStudioQualityType NXOpen) StaticRayTracedStudioQuality
         Returns the Ray Traced Studio static image quality   
            
         
        """
        pass
    @property
    def StaticRayTracedStudioRenderDepth(self) -> int:
        """
        Getter for property: (int) StaticRayTracedStudioRenderDepth
         Returns the Ray Traced Studio static image render depth, controls the iterations of ray tracing reflection and refraction calculations   
            
         
        """
        pass
    @StaticRayTracedStudioRenderDepth.setter
    def StaticRayTracedStudioRenderDepth(self, staticRayTracedStudioRenderDepth: int):
        """
        Setter for property: (int) StaticRayTracedStudioRenderDepth
         Returns the Ray Traced Studio static image render depth, controls the iterations of ray tracing reflection and refraction calculations   
            
         
        """
        pass
    @property
    def StationaryAntialiasing(self) -> RayTracedStudioEditorBuilder.StationaryAntialiasingType:
        """
        Getter for property: ( RayTracedStudioEditorBuilder.StationaryAntialiasingType NXOpen) StationaryAntialiasing
         Returns the Ray Traced Studio stationary antialiasing quality when dynamic interaction stops   
            
         
        """
        pass
    @StationaryAntialiasing.setter
    def StationaryAntialiasing(self, stationaryAntialiasing: RayTracedStudioEditorBuilder.StationaryAntialiasingType):
        """
        Setter for property: ( RayTracedStudioEditorBuilder.StationaryAntialiasingType NXOpen) StationaryAntialiasing
         Returns the Ray Traced Studio stationary antialiasing quality when dynamic interaction stops   
            
         
        """
        pass
    @property
    def StationaryRayTracedStudioQuality(self) -> RayTracedStudioEditorBuilder.StationaryRayTracedStudioQualityType:
        """
        Getter for property: ( RayTracedStudioEditorBuilder.StationaryRayTracedStudioQualityType NXOpen) StationaryRayTracedStudioQuality
         Returns the Ray Traced Studio stationary display quality when dynamic interaction stops   
            
         
        """
        pass
    @StationaryRayTracedStudioQuality.setter
    def StationaryRayTracedStudioQuality(self, stationaryRayTracedStudioQuality: RayTracedStudioEditorBuilder.StationaryRayTracedStudioQualityType):
        """
        Setter for property: ( RayTracedStudioEditorBuilder.StationaryRayTracedStudioQualityType NXOpen) StationaryRayTracedStudioQuality
         Returns the Ray Traced Studio stationary display quality when dynamic interaction stops   
            
         
        """
        pass
    @property
    def StationaryRayTracedStudioshowStatusIndicator(self) -> bool:
        """
        Getter for property: (bool) StationaryRayTracedStudioshowStatusIndicator
         Returns the stationary Ray Traced Studio progess status indicator percent complete display   
            
         
        """
        pass
    @StationaryRayTracedStudioshowStatusIndicator.setter
    def StationaryRayTracedStudioshowStatusIndicator(self, stationaryRayTracedStudioshowStatusIndicator: bool):
        """
        Setter for property: (bool) StationaryRayTracedStudioshowStatusIndicator
         Returns the stationary Ray Traced Studio progess status indicator percent complete display   
            
         
        """
        pass
import NXOpen
class RayTracedStudioPreferencesBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Display.RayTracedStudioPreferencesBuilder.
    Ray Traced Studio Preferences controls display and output of CPU-based real-time ray tracing.
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return .
    """
    class DynamicRayTracedStudioTilingQualityType(Enum):
        """
        Members Include: 
         |High|  Very small tiles used during progressive updates of ray traced display 
         |Medium|  Medium sized tiles used during progressive updates of ray traced display 
         |Low|  Larger tiles used during progressive updates of ray traced display for faster display time 

        """
        High: int
        Medium: int
        Low: int
        @staticmethod
        def ValueOf(value: int) -> RayTracedStudioPreferencesBuilder.DynamicRayTracedStudioTilingQualityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RayTracedStudioStaticImageFileFormatType(Enum):
        """
        Members Include: 
         |Tif|  Tagged Image File Format (TIFF) file format 
         |Png|  Portable Network Graphic (PNG) file format 
         |Jpg|  Joint Photographic Experts Group (JPEG) file format 

        """
        Tif: int
        Png: int
        Jpg: int
        @staticmethod
        def ValueOf(value: int) -> RayTracedStudioPreferencesBuilder.RayTracedStudioStaticImageFileFormatType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RayTracedStudioStaticImageOrientationType(Enum):
        """
        Members Include: 
         |Landscape|  static image orientation where width is greater than height 
         |Portrait|  static image orientation where height is greater than width 

        """
        Landscape: int
        Portrait: int
        @staticmethod
        def ValueOf(value: int) -> RayTracedStudioPreferencesBuilder.RayTracedStudioStaticImageOrientationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RayTracedStudioStaticImageResolutionType(Enum):
        """
        Members Include: 
         |High|  static image output resolution of 300 DPI (dots per inch) 
         |Medium|  static image output resolution of 150 DPI (dots per inch) 
         |Low|  static image output resolution of 72 DPI (dots per inch) 
         |UserDefined|  user specified image output resolution in DPI (dots per inch) 

        """
        High: int
        Medium: int
        Low: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> RayTracedStudioPreferencesBuilder.RayTracedStudioStaticImageResolutionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RayTracedStudioStaticImageSizeType(Enum):
        """
        Members Include: 
         |RenderWindow|  Ray Traced Studio window size used for static image output 
         |UserDefined|  user specified size for static image output 

        """
        RenderWindow: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> RayTracedStudioPreferencesBuilder.RayTracedStudioStaticImageSizeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RayTracedStudioStaticImageUnitsType(Enum):
        """
        Members Include: 
         |Pixels|  static image size specified in pixel 
         |Millimeters|  static image size specified in millimeters 
         |Inches|  static image size specified in inches 

        """
        Pixels: int
        Millimeters: int
        Inches: int
        @staticmethod
        def ValueOf(value: int) -> RayTracedStudioPreferencesBuilder.RayTracedStudioStaticImageUnitsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StaticAntialiasingType(Enum):
        """
        Members Include: 
         |High|  Very good antialiasing performed for static image rendering 
         |Medium|  Good antialiasing performed for static image rendering 
         |Low|  Coarse antialiasing performed for static image rendering 
         |NotSet|  No antialiasing performed to provide quick, preview of ray traced display for static image rendering 

        """
        High: int
        Medium: int
        Low: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> RayTracedStudioPreferencesBuilder.StaticAntialiasingType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StaticRayTracedStudioQualityType(Enum):
        """
        Members Include: 
         |High|  Very good ray traced display quality for static image rendering 
         |Medium|  Good quality ray traced display with good performance for static image rendering 
         |Low|  The fastest ray traced display performance with preview quality for static image rendering 
         |UserDefined|  User specified ray traced display quality for static image rendering 

        """
        High: int
        Medium: int
        Low: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> RayTracedStudioPreferencesBuilder.StaticRayTracedStudioQualityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StationaryAntialiasingType(Enum):
        """
        Members Include: 
         |Medium|  Good antialiasing performed when dynamic interaction stops 
         |Low|  Coarse antialiasing performed when dynamic interaction stops 
         |NotSet|  No antialiasing performed to provide quick, preview of ray traced display when dynamic interaction stops 

        """
        Medium: int
        Low: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> RayTracedStudioPreferencesBuilder.StationaryAntialiasingType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StationaryRayTracedStudioQualityType(Enum):
        """
        Members Include: 
         |High|  Very good ray traced display quality when dynamic interaction stops 
         |Medium|  Good ray traced display quality with good performance when dynamic interaction stops 
         |Low|  The fastest ray traced display performance with preview quality when dynamic interaction stops 

        """
        High: int
        Medium: int
        Low: int
        @staticmethod
        def ValueOf(value: int) -> RayTracedStudioPreferencesBuilder.StationaryRayTracedStudioQualityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DynamicRayTracedStudioTilingQuality(self) -> RayTracedStudioPreferencesBuilder.DynamicRayTracedStudioTilingQualityType:
        """
        Getter for property: ( RayTracedStudioPreferencesBuilder.DynamicRayTracedStudioTilingQualityType NXOpen) DynamicRayTracedStudioTilingQuality
         Returns the Ray Traced Studio tiling quality during interactive dynamic display   
            
         
        """
        pass
    @DynamicRayTracedStudioTilingQuality.setter
    def DynamicRayTracedStudioTilingQuality(self, dynamicRayTracedStudioTilingQuality: RayTracedStudioPreferencesBuilder.DynamicRayTracedStudioTilingQualityType):
        """
        Setter for property: ( RayTracedStudioPreferencesBuilder.DynamicRayTracedStudioTilingQualityType NXOpen) DynamicRayTracedStudioTilingQuality
         Returns the Ray Traced Studio tiling quality during interactive dynamic display   
            
         
        """
        pass
    @property
    def RayTracedStudioDisplayGamma(self) -> float:
        """
        Getter for property: (float) RayTracedStudioDisplayGamma
         Returns the Ray Traced Studio display gamma, controls the overall contrast or brightness of the image's midtone values.  
            A higher gamma value yields an overall brighter image.   
         
        """
        pass
    @RayTracedStudioDisplayGamma.setter
    def RayTracedStudioDisplayGamma(self, rayTracedStudioDisplayGamma: float):
        """
        Setter for property: (float) RayTracedStudioDisplayGamma
         Returns the Ray Traced Studio display gamma, controls the overall contrast or brightness of the image's midtone values.  
            A higher gamma value yields an overall brighter image.   
         
        """
        pass
    @property
    def RayTracedStudioStaticImageDotsPerInch(self) -> int:
        """
        Getter for property: (int) RayTracedStudioStaticImageDotsPerInch
         Returns the Ray Traced Studio static image dots per inch (DPI)   
            
         
        """
        pass
    @RayTracedStudioStaticImageDotsPerInch.setter
    def RayTracedStudioStaticImageDotsPerInch(self, rayTracedStudioStaticImageDotsPerInch: int):
        """
        Setter for property: (int) RayTracedStudioStaticImageDotsPerInch
         Returns the Ray Traced Studio static image dots per inch (DPI)   
            
         
        """
        pass
    @property
    def RayTracedStudioStaticImageDoubleHeight(self) -> float:
        """
        Getter for property: (float) RayTracedStudioStaticImageDoubleHeight
         Returns the Ray Traced Studio static image height   
            
         
        """
        pass
    @RayTracedStudioStaticImageDoubleHeight.setter
    def RayTracedStudioStaticImageDoubleHeight(self, rayTracedStudioStaticImageDoubleHeight: float):
        """
        Setter for property: (float) RayTracedStudioStaticImageDoubleHeight
         Returns the Ray Traced Studio static image height   
            
         
        """
        pass
    @property
    def RayTracedStudioStaticImageDoubleWidth(self) -> float:
        """
        Getter for property: (float) RayTracedStudioStaticImageDoubleWidth
         Returns the Ray Traced Studio static image width   
            
         
        """
        pass
    @RayTracedStudioStaticImageDoubleWidth.setter
    def RayTracedStudioStaticImageDoubleWidth(self, rayTracedStudioStaticImageDoubleWidth: float):
        """
        Setter for property: (float) RayTracedStudioStaticImageDoubleWidth
         Returns the Ray Traced Studio static image width   
            
         
        """
        pass
    @property
    def RayTracedStudioStaticImageFileFormat(self) -> RayTracedStudioPreferencesBuilder.RayTracedStudioStaticImageFileFormatType:
        """
        Getter for property: ( RayTracedStudioPreferencesBuilder.RayTracedStudioStaticImageFileFormatType NXOpen) RayTracedStudioStaticImageFileFormat
         Returns the Ray Traced Studio static output image file format   
            
         
        """
        pass
    @RayTracedStudioStaticImageFileFormat.setter
    def RayTracedStudioStaticImageFileFormat(self, rayTracedStudioStaticImageFileFormat: RayTracedStudioPreferencesBuilder.RayTracedStudioStaticImageFileFormatType):
        """
        Setter for property: ( RayTracedStudioPreferencesBuilder.RayTracedStudioStaticImageFileFormatType NXOpen) RayTracedStudioStaticImageFileFormat
         Returns the Ray Traced Studio static output image file format   
            
         
        """
        pass
    @property
    def RayTracedStudioStaticImageLockAspectRatio(self) -> bool:
        """
        Getter for property: (bool) RayTracedStudioStaticImageLockAspectRatio
         Returns the Ray Traced Studio static image aspect ratio will be maintained   
            
         
        """
        pass
    @RayTracedStudioStaticImageLockAspectRatio.setter
    def RayTracedStudioStaticImageLockAspectRatio(self, rayTracedStudioStaticImageLockAspectRatio: bool):
        """
        Setter for property: (bool) RayTracedStudioStaticImageLockAspectRatio
         Returns the Ray Traced Studio static image aspect ratio will be maintained   
            
         
        """
        pass
    @property
    def RayTracedStudioStaticImageOrientation(self) -> RayTracedStudioPreferencesBuilder.RayTracedStudioStaticImageOrientationType:
        """
        Getter for property: ( RayTracedStudioPreferencesBuilder.RayTracedStudioStaticImageOrientationType NXOpen) RayTracedStudioStaticImageOrientation
         Returns the Ray Traced Studio static image orientation   
            
         
        """
        pass
    @RayTracedStudioStaticImageOrientation.setter
    def RayTracedStudioStaticImageOrientation(self, rayTracedStudioStaticImageOrientation: RayTracedStudioPreferencesBuilder.RayTracedStudioStaticImageOrientationType):
        """
        Setter for property: ( RayTracedStudioPreferencesBuilder.RayTracedStudioStaticImageOrientationType NXOpen) RayTracedStudioStaticImageOrientation
         Returns the Ray Traced Studio static image orientation   
            
         
        """
        pass
    @property
    def RayTracedStudioStaticImagePixelHeight(self) -> int:
        """
        Getter for property: (int) RayTracedStudioStaticImagePixelHeight
         Returns the Ray Traced Studio static image pixel height   
            
         
        """
        pass
    @RayTracedStudioStaticImagePixelHeight.setter
    def RayTracedStudioStaticImagePixelHeight(self, rayTracedStudioStaticImagePixelHeight: int):
        """
        Setter for property: (int) RayTracedStudioStaticImagePixelHeight
         Returns the Ray Traced Studio static image pixel height   
            
         
        """
        pass
    @property
    def RayTracedStudioStaticImagePixelWidth(self) -> int:
        """
        Getter for property: (int) RayTracedStudioStaticImagePixelWidth
         Returns the Ray Traced Studio static image pixel width   
            
         
        """
        pass
    @RayTracedStudioStaticImagePixelWidth.setter
    def RayTracedStudioStaticImagePixelWidth(self, rayTracedStudioStaticImagePixelWidth: int):
        """
        Setter for property: (int) RayTracedStudioStaticImagePixelWidth
         Returns the Ray Traced Studio static image pixel width   
            
         
        """
        pass
    @property
    def RayTracedStudioStaticImageResolution(self) -> RayTracedStudioPreferencesBuilder.RayTracedStudioStaticImageResolutionType:
        """
        Getter for property: ( RayTracedStudioPreferencesBuilder.RayTracedStudioStaticImageResolutionType NXOpen) RayTracedStudioStaticImageResolution
         Returns the Ray Traced Studio static image resolution   
            
         
        """
        pass
    @RayTracedStudioStaticImageResolution.setter
    def RayTracedStudioStaticImageResolution(self, rayTracedStudioStaticImageResolution: RayTracedStudioPreferencesBuilder.RayTracedStudioStaticImageResolutionType):
        """
        Setter for property: ( RayTracedStudioPreferencesBuilder.RayTracedStudioStaticImageResolutionType NXOpen) RayTracedStudioStaticImageResolution
         Returns the Ray Traced Studio static image resolution   
            
         
        """
        pass
    @property
    def RayTracedStudioStaticImageSize(self) -> RayTracedStudioPreferencesBuilder.RayTracedStudioStaticImageSizeType:
        """
        Getter for property: ( RayTracedStudioPreferencesBuilder.RayTracedStudioStaticImageSizeType NXOpen) RayTracedStudioStaticImageSize
         Returns the Ray Traced Studio static image size   
            
         
        """
        pass
    @RayTracedStudioStaticImageSize.setter
    def RayTracedStudioStaticImageSize(self, rayTracedStudioStaticImageSize: RayTracedStudioPreferencesBuilder.RayTracedStudioStaticImageSizeType):
        """
        Setter for property: ( RayTracedStudioPreferencesBuilder.RayTracedStudioStaticImageSizeType NXOpen) RayTracedStudioStaticImageSize
         Returns the Ray Traced Studio static image size   
            
         
        """
        pass
    @property
    def RayTracedStudioStaticImageUnits(self) -> RayTracedStudioPreferencesBuilder.RayTracedStudioStaticImageUnitsType:
        """
        Getter for property: ( RayTracedStudioPreferencesBuilder.RayTracedStudioStaticImageUnitsType NXOpen) RayTracedStudioStaticImageUnits
         Returns the Ray Traced Studio static image units   
            
         
        """
        pass
    @RayTracedStudioStaticImageUnits.setter
    def RayTracedStudioStaticImageUnits(self, rayTracedStudioStaticImageUnits: RayTracedStudioPreferencesBuilder.RayTracedStudioStaticImageUnitsType):
        """
        Setter for property: ( RayTracedStudioPreferencesBuilder.RayTracedStudioStaticImageUnitsType NXOpen) RayTracedStudioStaticImageUnits
         Returns the Ray Traced Studio static image units   
            
         
        """
        pass
    @property
    def StaticAntialiasing(self) -> RayTracedStudioPreferencesBuilder.StaticAntialiasingType:
        """
        Getter for property: ( RayTracedStudioPreferencesBuilder.StaticAntialiasingType NXOpen) StaticAntialiasing
         Returns the Ray Traced Studio static image antialiasing quality   
            
         
        """
        pass
    @StaticAntialiasing.setter
    def StaticAntialiasing(self, staticAntialiasing: RayTracedStudioPreferencesBuilder.StaticAntialiasingType):
        """
        Setter for property: ( RayTracedStudioPreferencesBuilder.StaticAntialiasingType NXOpen) StaticAntialiasing
         Returns the Ray Traced Studio static image antialiasing quality   
            
         
        """
        pass
    @property
    def StaticRayTracedStudioQuality(self) -> RayTracedStudioPreferencesBuilder.StaticRayTracedStudioQualityType:
        """
        Getter for property: ( RayTracedStudioPreferencesBuilder.StaticRayTracedStudioQualityType NXOpen) StaticRayTracedStudioQuality
         Returns the Ray Traced Studio static image quality   
            
         
        """
        pass
    @StaticRayTracedStudioQuality.setter
    def StaticRayTracedStudioQuality(self, staticRayTracedStudioQuality: RayTracedStudioPreferencesBuilder.StaticRayTracedStudioQualityType):
        """
        Setter for property: ( RayTracedStudioPreferencesBuilder.StaticRayTracedStudioQualityType NXOpen) StaticRayTracedStudioQuality
         Returns the Ray Traced Studio static image quality   
            
         
        """
        pass
    @property
    def StaticRayTracedStudioRenderDepth(self) -> int:
        """
        Getter for property: (int) StaticRayTracedStudioRenderDepth
         Returns the Ray Traced Studio static image render depth, controls the iterations of ray tracing reflection and refraction calculations   
            
         
        """
        pass
    @StaticRayTracedStudioRenderDepth.setter
    def StaticRayTracedStudioRenderDepth(self, staticRayTracedStudioRenderDepth: int):
        """
        Setter for property: (int) StaticRayTracedStudioRenderDepth
         Returns the Ray Traced Studio static image render depth, controls the iterations of ray tracing reflection and refraction calculations   
            
         
        """
        pass
    @property
    def StationaryAntialiasing(self) -> RayTracedStudioPreferencesBuilder.StationaryAntialiasingType:
        """
        Getter for property: ( RayTracedStudioPreferencesBuilder.StationaryAntialiasingType NXOpen) StationaryAntialiasing
         Returns the Ray Traced Studio stationary antialiasing quality when dynamic interaction stops   
            
         
        """
        pass
    @StationaryAntialiasing.setter
    def StationaryAntialiasing(self, stationaryAntialiasing: RayTracedStudioPreferencesBuilder.StationaryAntialiasingType):
        """
        Setter for property: ( RayTracedStudioPreferencesBuilder.StationaryAntialiasingType NXOpen) StationaryAntialiasing
         Returns the Ray Traced Studio stationary antialiasing quality when dynamic interaction stops   
            
         
        """
        pass
    @property
    def StationaryRayTracedStudioQuality(self) -> RayTracedStudioPreferencesBuilder.StationaryRayTracedStudioQualityType:
        """
        Getter for property: ( RayTracedStudioPreferencesBuilder.StationaryRayTracedStudioQualityType NXOpen) StationaryRayTracedStudioQuality
         Returns the Ray Traced Studio stationary display quality when dynamic interaction stops   
            
         
        """
        pass
    @StationaryRayTracedStudioQuality.setter
    def StationaryRayTracedStudioQuality(self, stationaryRayTracedStudioQuality: RayTracedStudioPreferencesBuilder.StationaryRayTracedStudioQualityType):
        """
        Setter for property: ( RayTracedStudioPreferencesBuilder.StationaryRayTracedStudioQualityType NXOpen) StationaryRayTracedStudioQuality
         Returns the Ray Traced Studio stationary display quality when dynamic interaction stops   
            
         
        """
        pass
    @property
    def StationaryRayTracedStudioshowStatusIndicator(self) -> bool:
        """
        Getter for property: (bool) StationaryRayTracedStudioshowStatusIndicator
         Returns the stationary Ray Traced Studio progess status indicator percent complete display   
            
         
        """
        pass
    @StationaryRayTracedStudioshowStatusIndicator.setter
    def StationaryRayTracedStudioshowStatusIndicator(self, stationaryRayTracedStudioshowStatusIndicator: bool):
        """
        Setter for property: (bool) StationaryRayTracedStudioshowStatusIndicator
         Returns the stationary Ray Traced Studio progess status indicator percent complete display   
            
         
        """
        pass
import NXOpen
class Reflection(NXOpen.Builder): 
    """
    Represents a NXOpen.Display.Reflection
    Reflection defines the source of reflection in shiny objects for Studio
    rendering style or High Quality Images.
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return .
    """
    class Type(Enum):
        """
        Members Include: 
         |Background|  use the background for reflections 
         |Stage|  use the stage for reflections 
         |Ibl|  use the image-based lighting image for reflections 
         |Image|  use the given image file for reflection 

        """
        Background: int
        Stage: int
        Ibl: int
        Image: int
        @staticmethod
        def ValueOf(value: int) -> Reflection.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Image(self) -> Image:
        """
        Getter for property: ( Image NXOpen) Image
         Returns the reflections's image builder   
            
         
        """
        pass
    @Image.setter
    def Image(self, image_builder: Image):
        """
        Setter for property: ( Image NXOpen) Image
         Returns the reflections's image builder   
            
         
        """
        pass
    @property
    def ImageFilename(self) -> str:
        """
        Getter for property: (str) ImageFilename
         Returns the reflection's image filename   
            
         
        """
        pass
    @ImageFilename.setter
    def ImageFilename(self, image_file_name: str):
        """
        Setter for property: (str) ImageFilename
         Returns the reflection's image filename   
            
         
        """
        pass
    @property
    def ReflectionMap(self) -> Reflection.Type:
        """
        Getter for property: ( Reflection.Type NXOpen) ReflectionMap
         Returns the reflection type   
            
         
        """
        pass
    @ReflectionMap.setter
    def ReflectionMap(self, reflectionMap: Reflection.Type):
        """
        Setter for property: ( Reflection.Type NXOpen) ReflectionMap
         Returns the reflection type   
            
         
        """
        pass
import NXOpen
class SaveImageFileBrowserBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Display.SaveImageFileBrowserBuilder.
    Saves an image file using a file browser.
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return .
    """
    class FileFormats(Enum):
        """
        Members Include: 
         |Tif|  Tagged Image File Format (TIFF) file format 
         |Png|  Portable Network Graphic (PNG) file format 
         |Jpg|  Joint Photographic Experts Group (JPEG) file format 

        """
        Tif: int
        Png: int
        Jpg: int
        @staticmethod
        def ValueOf(value: int) -> SaveImageFileBrowserBuilder.FileFormats:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FileFormat(self) -> SaveImageFileBrowserBuilder.FileFormats:
        """
        Getter for property: ( SaveImageFileBrowserBuilder.FileFormats NXOpen) FileFormat
         Returns the Ray Traced Studio static image file format   
            
         
        """
        pass
    @FileFormat.setter
    def FileFormat(self, fileFormat: SaveImageFileBrowserBuilder.FileFormats):
        """
        Setter for property: ( SaveImageFileBrowserBuilder.FileFormats NXOpen) FileFormat
         Returns the Ray Traced Studio static image file format   
            
         
        """
        pass
    @property
    def NativeImageFileBrowser(self) -> str:
        """
        Getter for property: (str) NativeImageFileBrowser
         Returns the Ray Traced Studio static image file browser   
            
         
        """
        pass
    @NativeImageFileBrowser.setter
    def NativeImageFileBrowser(self, filename: str):
        """
        Setter for property: (str) NativeImageFileBrowser
         Returns the Ray Traced Studio static image file browser   
            
         
        """
        pass
    @property
    def UseTransparentBackground(self) -> bool:
        """
        Getter for property: (bool) UseTransparentBackground
         Returns the Ray Traced Studio static image transparent background setting   
            
         
        """
        pass
    @UseTransparentBackground.setter
    def UseTransparentBackground(self, useTransparentBackground: bool):
        """
        Setter for property: (bool) UseTransparentBackground
         Returns the Ray Traced Studio static image transparent background setting   
            
         
        """
        pass
import NXOpen
class Scene(NXOpen.Builder): 
    """
    Represents a NXOpen.Display.Scene
    A scene is comprised of background, stage, reflection, lights and 
    image-based lighting subobjects.  You optionally specify a scene for
    display in Studio rendering style and High Quality Images.
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return .
    """
    @property
    def Background(self) -> Background:
        """
        Getter for property: ( Background NXOpen) Background
         Returns the background - use to define how background pixels are displayed   
            
         
        """
        pass
    @property
    def EnvironmentBuilder(self) -> EnvironmentBuilder:
        """
        Getter for property: ( EnvironmentBuilder NXOpen) EnvironmentBuilder
         Returns the environment_builder - use to define the environment   
            
         
        """
        pass
    @property
    def ImageBasedLighting(self) -> ImageBasedLighting:
        """
        Getter for property: ( ImageBasedLighting NXOpen) ImageBasedLighting
         Returns the image-based lighting - optionally use to by-pass lights with 
                    image-based lighting, where lighting effects are derived from a
                    given image file   
            
         
        """
        pass
    @property
    def Lighting(self) -> Lighting:
        """
        Getter for property: ( Lighting NXOpen) Lighting
         Returns the lights - use to define light settings for the given lights   
            
         
        """
        pass
    @property
    def Reflection(self) -> Reflection:
        """
        Getter for property: ( Reflection NXOpen) Reflection
         Returns the reflection - use to define what will be reflected in shiny objects   
            
         
        """
        pass
    @property
    def Stage(self) -> Stage:
        """
        Getter for property: ( Stage NXOpen) Stage
         Returns the stage - use to optionally define a box that can have between 
                    one and six visible "walls"   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SectionCurveSettingsBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.Display.SectionCurveSettingsBuilder
    """
    class ColorOptionType(Enum):
        """
        Members Include: 
         |Body|  Use body color 
         |Any|  Use specified color 

        """
        Body: int
        Any: int
        @staticmethod
        def ValueOf(value: int) -> SectionCurveSettingsBuilder.ColorOptionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) Color
         Returns the curve color.  
           Used when the curve color option is set to
                     NXOpen::Display::SectionCurveSettingsBuilder::ColorOptionTypeAny
                     .
                   
         
        """
        pass
    @Color.setter
    def Color(self, curveColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) Color
         Returns the curve color.  
           Used when the curve color option is set to
                     NXOpen::Display::SectionCurveSettingsBuilder::ColorOptionTypeAny
                     .
                   
         
        """
        pass
    @property
    def ColorOption(self) -> SectionCurveSettingsBuilder.ColorOptionType:
        """
        Getter for property: ( SectionCurveSettingsBuilder.ColorOptionType NXOpen) ColorOption
         Returns the curve color option   
            
         
        """
        pass
    @ColorOption.setter
    def ColorOption(self, curveColorOption: SectionCurveSettingsBuilder.ColorOptionType):
        """
        Setter for property: ( SectionCurveSettingsBuilder.ColorOptionType NXOpen) ColorOption
         Returns the curve color option   
            
         
        """
        pass
    @property
    def Show(self) -> bool:
        """
        Getter for property: (bool) Show
         Returns the curve on off flag.  
             
         
        """
        pass
    @Show.setter
    def Show(self, showCurves: bool):
        """
        Setter for property: (bool) Show
         Returns the curve on off flag.  
             
         
        """
        pass
import NXOpen
class SelPrefCollection(NXOpen.TaggedObjectCollection): 
    """
Represents a collection SelPref
"""
    def CreateSelPref(self) -> SelPref:
        """
         Create a NXOpen.Display.SelPref object 
         Returns builder ( SelPref NXOpen): .
        """
        pass
import NXOpen
class SelPref(NXOpen.Builder): 
    """
    Represents a NXOpen.Display.SelPref
    """
    class FaceAnalysisViews(Enum):
        """
        Members Include: 
         |HighlightEdges|  highlight face by edges 
         |HighlightFaces|  highlight face by face 

        """
        HighlightEdges: int
        HighlightFaces: int
        @staticmethod
        def ValueOf(value: int) -> SelPref.FaceAnalysisViews:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Method(Enum):
        """
        Members Include: 
         |Simple|  chaining method simple 
         |Wcs|  chaining method wcs 
         |WcsLeft|  chaining method wcs left 
         |WcsRight|  chaining method wcs right 

        """
        Simple: int
        Wcs: int
        WcsLeft: int
        WcsRight: int
        @staticmethod
        def ValueOf(value: int) -> SelPref.Method:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MouseGesture(Enum):
        """
        Members Include: 
         |Lasso|  multi-select using lasso 
         |Rectangle|  multi-select using rectangle 
         |Circle|  multi-select using circle 

        """
        Lasso: int
        Rectangle: int
        Circle: int
        @staticmethod
        def ValueOf(value: int) -> SelPref.MouseGesture:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SelectionRadius(Enum):
        """
        Members Include: 
         |Medium|  selection ball size medium 
         |Small|  selection ball size small 
         |Large|  selection ball size large 

        """
        Medium: int
        Small: int
        Large: int
        @staticmethod
        def ValueOf(value: int) -> SelPref.SelectionRadius:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SelectionRule(Enum):
        """
        Members Include: 
         |Inside|  multi-select rule inside 
         |Outside|  multi-select rule outside 
         |Crossing|  multi-select rule crossing 
         |InsideCrossing|  multi-select rule inside or crossing 
         |OutsideCrossing|  multi-select rule outside or crossing

        """
        Inside: int
        Outside: int
        Crossing: int
        InsideCrossing: int
        OutsideCrossing: int
        @staticmethod
        def ValueOf(value: int) -> SelPref.SelectionRule:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ShadedViews(Enum):
        """
        Members Include: 
         |HighlightEdges|  highlight face by edges 
         |HighlightFaces|  highlight face by face 

        """
        HighlightEdges: int
        HighlightFaces: int
        @staticmethod
        def ValueOf(value: int) -> SelPref.ShadedViews:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Delay(self) -> int:
        """
        Getter for property: (int) Delay
         Returns the delay   
            
         
        """
        pass
    @Delay.setter
    def Delay(self, delay: int):
        """
        Setter for property: (int) Delay
         Returns the delay   
            
         
        """
        pass
    @property
    def FaceAnalysisViewsType(self) -> SelPref.FaceAnalysisViews:
        """
        Getter for property: ( SelPref.FaceAnalysisViews NXOpen) FaceAnalysisViewsType
         Returns the face analysis views type   
            
         
        """
        pass
    @FaceAnalysisViewsType.setter
    def FaceAnalysisViewsType(self, faceAnalysisViewsType: SelPref.FaceAnalysisViews):
        """
        Setter for property: ( SelPref.FaceAnalysisViews NXOpen) FaceAnalysisViewsType
         Returns the face analysis views type   
            
         
        """
        pass
    @property
    def HighlightHiddenEdgesToggle(self) -> bool:
        """
        Getter for property: (bool) HighlightHiddenEdgesToggle
         Returns the highlight hidden edges toggle   
            
         
        """
        pass
    @HighlightHiddenEdgesToggle.setter
    def HighlightHiddenEdgesToggle(self, highlightHiddenEdgesToggle: bool):
        """
        Setter for property: (bool) HighlightHiddenEdgesToggle
         Returns the highlight hidden edges toggle   
            
         
        """
        pass
    @property
    def HighlightOriginalToggle(self) -> bool:
        """
        Getter for property: (bool) HighlightOriginalToggle
         Returns the highlight original  
            
         
        """
        pass
    @HighlightOriginalToggle.setter
    def HighlightOriginalToggle(self, highlightOriginalToggle: bool):
        """
        Setter for property: (bool) HighlightOriginalToggle
         Returns the highlight original  
            
         
        """
        pass
    @property
    def HighlightSelectionOnRolloverToggle(self) -> bool:
        """
        Getter for property: (bool) HighlightSelectionOnRolloverToggle
         Returns the highlight selection on rollover toggle   
            
         
        """
        pass
    @HighlightSelectionOnRolloverToggle.setter
    def HighlightSelectionOnRolloverToggle(self, highlightSelectionOnRolloverToggle: bool):
        """
        Setter for property: (bool) HighlightSelectionOnRolloverToggle
         Returns the highlight selection on rollover toggle   
            
         
        """
        pass
    @property
    def HighlightWithThickWidthToggle(self) -> bool:
        """
        Getter for property: (bool) HighlightWithThickWidthToggle
         Returns the highlight with thick width toggle   
            
         
        """
        pass
    @HighlightWithThickWidthToggle.setter
    def HighlightWithThickWidthToggle(self, highlightWithThickWidthToggle: bool):
        """
        Setter for property: (bool) HighlightWithThickWidthToggle
         Returns the highlight with thick width toggle   
            
         
        """
        pass
    @property
    def MethodType(self) -> SelPref.Method:
        """
        Getter for property: ( SelPref.Method NXOpen) MethodType
         Returns the method type   
            
         
        """
        pass
    @MethodType.setter
    def MethodType(self, methodType: SelPref.Method):
        """
        Setter for property: ( SelPref.Method NXOpen) MethodType
         Returns the method type   
            
         
        """
        pass
    @property
    def MouseGestureType(self) -> SelPref.MouseGesture:
        """
        Getter for property: ( SelPref.MouseGesture NXOpen) MouseGestureType
         Returns the mouse gesture type   
            
         
        """
        pass
    @MouseGestureType.setter
    def MouseGestureType(self, mouseGestureType: SelPref.MouseGesture):
        """
        Setter for property: ( SelPref.MouseGesture NXOpen) MouseGestureType
         Returns the mouse gesture type   
            
         
        """
        pass
    @property
    def QuickPickLockDialogPosition(self) -> bool:
        """
        Getter for property: (bool) QuickPickLockDialogPosition
         Returns the quick pick lock dialog position   
            
         
        """
        pass
    @QuickPickLockDialogPosition.setter
    def QuickPickLockDialogPosition(self, quickPickLockDialogPosition: bool):
        """
        Setter for property: (bool) QuickPickLockDialogPosition
         Returns the quick pick lock dialog position   
            
         
        """
        pass
    @property
    def QuickPickOnDelayToggle(self) -> bool:
        """
        Getter for property: (bool) QuickPickOnDelayToggle
         Returns the quick pick on delay toggle   
            
         
        """
        pass
    @QuickPickOnDelayToggle.setter
    def QuickPickOnDelayToggle(self, quickPickOnDelayToggle: bool):
        """
        Setter for property: (bool) QuickPickOnDelayToggle
         Returns the quick pick on delay toggle   
            
         
        """
        pass
    @property
    def QuickPickSeeThruToggle(self) -> bool:
        """
        Getter for property: (bool) QuickPickSeeThruToggle
         Returns the quick pick see thru toggle   
            
         
        """
        pass
    @QuickPickSeeThruToggle.setter
    def QuickPickSeeThruToggle(self, quickPickSeeThruToggle: bool):
        """
        Setter for property: (bool) QuickPickSeeThruToggle
         Returns the quick pick see thru toggle   
            
         
        """
        pass
    @property
    def RolloverDelay(self) -> int:
        """
        Getter for property: (int) RolloverDelay
         Returns the rollover delay   
            
         
        """
        pass
    @RolloverDelay.setter
    def RolloverDelay(self, rolloverDelay: int):
        """
        Setter for property: (int) RolloverDelay
         Returns the rollover delay   
            
         
        """
        pass
    @property
    def SelectionRadiusType(self) -> SelPref.SelectionRadius:
        """
        Getter for property: ( SelPref.SelectionRadius NXOpen) SelectionRadiusType
         Returns the selection radius type   
            
         
        """
        pass
    @SelectionRadiusType.setter
    def SelectionRadiusType(self, selectionRadiusType: SelPref.SelectionRadius):
        """
        Setter for property: ( SelPref.SelectionRadius NXOpen) SelectionRadiusType
         Returns the selection radius type   
            
         
        """
        pass
    @property
    def SelectionRuleType(self) -> SelPref.SelectionRule:
        """
        Getter for property: ( SelPref.SelectionRule NXOpen) SelectionRuleType
         Returns the selection rule type   
            
         
        """
        pass
    @SelectionRuleType.setter
    def SelectionRuleType(self, selectionRuleType: SelPref.SelectionRule):
        """
        Setter for property: ( SelPref.SelectionRule NXOpen) SelectionRuleType
         Returns the selection rule type   
            
         
        """
        pass
    @property
    def ShadedViewsType(self) -> SelPref.ShadedViews:
        """
        Getter for property: ( SelPref.ShadedViews NXOpen) ShadedViewsType
         Returns the shaded views type   
            
         
        """
        pass
    @ShadedViewsType.setter
    def ShadedViewsType(self, shadedViewsType: SelPref.ShadedViews):
        """
        Setter for property: ( SelPref.ShadedViews NXOpen) ShadedViewsType
         Returns the shaded views type   
            
         
        """
        pass
    @property
    def ShowCrosshairsToggle(self) -> bool:
        """
        Getter for property: (bool) ShowCrosshairsToggle
         Returns the show crosshairs toggle   
            
         
        """
        pass
    @ShowCrosshairsToggle.setter
    def ShowCrosshairsToggle(self, showCrosshairsToggle: bool):
        """
        Setter for property: (bool) ShowCrosshairsToggle
         Returns the show crosshairs toggle   
            
         
        """
        pass
    @property
    def TangencyTolerance(self) -> float:
        """
        Getter for property: (float) TangencyTolerance
         Returns the tangency tolerance   
            
         
        """
        pass
    @TangencyTolerance.setter
    def TangencyTolerance(self, tangencyTolerance: float):
        """
        Setter for property: (float) TangencyTolerance
         Returns the tangency tolerance   
            
         
        """
        pass
    @property
    def Tolerance(self) -> float:
        """
        Getter for property: (float) Tolerance
         Returns the tolerance   
            
         
        """
        pass
    @Tolerance.setter
    def Tolerance(self, tolerance: float):
        """
        Setter for property: (float) Tolerance
         Returns the tolerance   
            
         
        """
        pass
    @property
    def TooltipOnRolloverToggle(self) -> bool:
        """
        Getter for property: (bool) TooltipOnRolloverToggle
         Returns the tooltip on rollover toggle   
            
         
        """
        pass
    @TooltipOnRolloverToggle.setter
    def TooltipOnRolloverToggle(self, tooltipOnRolloverToggle: bool):
        """
        Setter for property: (bool) TooltipOnRolloverToggle
         Returns the tooltip on rollover toggle   
            
         
        """
        pass
import NXOpen
class Shadows(NXOpen.Builder): 
    """
    Represents a NXOpen.Display.Shadows
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return .
    """
    class RealTimeState(Enum):
        """
        Members Include: 
         |Disabled|  Realtime is disabled 
         |EnvironmentShadowCatcherOnly|  Realtime Environment or shadow catcher only 
         |InterObject|  Realtime Inter-object shadows 

        """
        Disabled: int
        EnvironmentShadowCatcherOnly: int
        InterObject: int
        @staticmethod
        def ValueOf(value: int) -> Shadows.RealTimeState:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SsaoContrastType(Enum):
        """
        Members Include: 
         |NotSet|  no contrast
         |Low|  low contrast
         |Medium|  Medium contrast 
         |High|  High contrast 
         |ExtraHigh|  Extra High contrast 

        """
        NotSet: int
        Low: int
        Medium: int
        High: int
        ExtraHigh: int
        @staticmethod
        def ValueOf(value: int) -> Shadows.SsaoContrastType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SsaoQualityType(Enum):
        """
        Members Include: 
         |Low|  Low quality setting 
         |Medium|  Medium quality setting 
         |High|  High quality setting 
         |VeryHigh|  Very High quality setting 

        """
        Low: int
        Medium: int
        High: int
        VeryHigh: int
        @staticmethod
        def ValueOf(value: int) -> Shadows.SsaoQualityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AmbientOcclusion(self) -> bool:
        """
        Getter for property: (bool) AmbientOcclusion
         Returns the shadows SSAO ambient occlusion   
            
         
        """
        pass
    @AmbientOcclusion.setter
    def AmbientOcclusion(self, shadowsSSAODisplayEnabled: bool):
        """
        Setter for property: (bool) AmbientOcclusion
         Returns the shadows SSAO ambient occlusion   
            
         
        """
        pass
    @property
    def DisplayStyle(self) -> NXOpen.View.DisplayStyleType:
        """
        Getter for property: ( NXOpen.View.DisplayStyleType) DisplayStyle
         Returns the display style whose shadows is being modified.  
           Shaded and Studio have independent shadows settings.  
         
        """
        pass
    @property
    def GenerateHqiShadows(self) -> bool:
        """
        Getter for property: (bool) GenerateHqiShadows
         Returns the High Quality Image settings   
            
         
        """
        pass
    @GenerateHqiShadows.setter
    def GenerateHqiShadows(self, generateHQIShadows: bool):
        """
        Setter for property: (bool) GenerateHqiShadows
         Returns the High Quality Image settings   
            
         
        """
        pass
    @property
    def RealTimeType(self) -> Shadows.RealTimeState:
        """
        Getter for property: ( Shadows.RealTimeState NXOpen) RealTimeType
         Returns the Real Time Settings   
            
         
        """
        pass
    @RealTimeType.setter
    def RealTimeType(self, realTimeType: Shadows.RealTimeState):
        """
        Setter for property: ( Shadows.RealTimeState NXOpen) RealTimeType
         Returns the Real Time Settings   
            
         
        """
        pass
    @property
    def ShadowCatcherSelection(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) ShadowCatcherSelection
         Returns the Shadow Catcher Selection   
            
         
        """
        pass
    @property
    def ShadowsEnabled(self) -> bool:
        """
        Getter for property: (bool) ShadowsEnabled
         Returns the Overall Shadows   
            
         
        """
        pass
    @ShadowsEnabled.setter
    def ShadowsEnabled(self, shadowsEnabled: bool):
        """
        Setter for property: (bool) ShadowsEnabled
         Returns the Overall Shadows   
            
         
        """
        pass
    @property
    def ShadowsShadedViewsShowGroundShadows(self) -> bool:
        """
        Getter for property: (bool) ShadowsShadedViewsShowGroundShadows
         Returns the Ground Shadow in Shaded View   
            
         
        """
        pass
    @ShadowsShadedViewsShowGroundShadows.setter
    def ShadowsShadedViewsShowGroundShadows(self, enableShadows: bool):
        """
        Setter for property: (bool) ShadowsShadedViewsShowGroundShadows
         Returns the Ground Shadow in Shaded View   
            
         
        """
        pass
    @property
    def SoftShadowsBiasOffset(self) -> float:
        """
        Getter for property: (float) SoftShadowsBiasOffset
         Returns the Soft Shadows bias offset   
            
         
        """
        pass
    @SoftShadowsBiasOffset.setter
    def SoftShadowsBiasOffset(self, softShadowsBiasOffset: float):
        """
        Setter for property: (float) SoftShadowsBiasOffset
         Returns the Soft Shadows bias offset   
            
         
        """
        pass
    @property
    def SoftShadowsEdges(self) -> int:
        """
        Getter for property: (int) SoftShadowsEdges
         Returns the Soft Shadows edges (softness)   
            
         
        """
        pass
    @SoftShadowsEdges.setter
    def SoftShadowsEdges(self, softShadowsEdges: int):
        """
        Setter for property: (int) SoftShadowsEdges
         Returns the Soft Shadows edges (softness)   
            
         
        """
        pass
    @property
    def SoftShadowsEnabled(self) -> bool:
        """
        Getter for property: (bool) SoftShadowsEnabled
         Returns the Soft Shadows   
            
         
        """
        pass
    @SoftShadowsEnabled.setter
    def SoftShadowsEnabled(self, softShadowsEnabled: bool):
        """
        Setter for property: (bool) SoftShadowsEnabled
         Returns the Soft Shadows   
            
         
        """
        pass
    @property
    def SoftShadowsGradientClamp(self) -> float:
        """
        Getter for property: (float) SoftShadowsGradientClamp
         Returns the Soft Shadows gradient clamp   
            
         
        """
        pass
    @SoftShadowsGradientClamp.setter
    def SoftShadowsGradientClamp(self, softShadowsGradientClamps: float):
        """
        Setter for property: (float) SoftShadowsGradientClamp
         Returns the Soft Shadows gradient clamp   
            
         
        """
        pass
    @property
    def SoftShadowsQuality(self) -> int:
        """
        Getter for property: (int) SoftShadowsQuality
         Returns the Soft Shadows quality   
            
         
        """
        pass
    @SoftShadowsQuality.setter
    def SoftShadowsQuality(self, softShadowsQuality: int):
        """
        Setter for property: (int) SoftShadowsQuality
         Returns the Soft Shadows quality   
            
         
        """
        pass
    @property
    def SsaoBlurRadius(self) -> float:
        """
        Getter for property: (float) SsaoBlurRadius
         Returns the shadows SSAO Blur Radius   
            
         
        """
        pass
    @SsaoBlurRadius.setter
    def SsaoBlurRadius(self, blurRadius: float):
        """
        Setter for property: (float) SsaoBlurRadius
         Returns the shadows SSAO Blur Radius   
            
         
        """
        pass
    @property
    def SsaoContrast(self) -> Shadows.SsaoContrastType:
        """
        Getter for property: ( Shadows.SsaoContrastType NXOpen) SsaoContrast
         Returns the shadows SSAO contrast   
            
         
        """
        pass
    @SsaoContrast.setter
    def SsaoContrast(self, contrast: Shadows.SsaoContrastType):
        """
        Setter for property: ( Shadows.SsaoContrastType NXOpen) SsaoContrast
         Returns the shadows SSAO contrast   
            
         
        """
        pass
    @property
    def SsaoQuality(self) -> Shadows.SsaoQualityType:
        """
        Getter for property: ( Shadows.SsaoQualityType NXOpen) SsaoQuality
         Returns the shadows SSAO quality   
            
         
        """
        pass
    @SsaoQuality.setter
    def SsaoQuality(self, shadowsSSAOQuality: Shadows.SsaoQualityType):
        """
        Setter for property: ( Shadows.SsaoQualityType NXOpen) SsaoQuality
         Returns the shadows SSAO quality   
            
         
        """
        pass
    @property
    def SsaoRadius(self) -> float:
        """
        Getter for property: (float) SsaoRadius
         Returns the shadows SSAO radius   
            
         
        """
        pass
    @SsaoRadius.setter
    def SsaoRadius(self, radius: float):
        """
        Setter for property: (float) SsaoRadius
         Returns the shadows SSAO radius   
            
         
        """
        pass
    @property
    def UseShadowCatcher(self) -> bool:
        """
        Getter for property: (bool) UseShadowCatcher
         Returns the Shadow Catcher   
            
         
        """
        pass
    @UseShadowCatcher.setter
    def UseShadowCatcher(self, useShadowCatcher: bool):
        """
        Setter for property: (bool) UseShadowCatcher
         Returns the Shadow Catcher   
            
         
        """
        pass
    @property
    def View(self) -> NXOpen.View:
        """
        Getter for property: ( NXOpen.View) View
         Returns the view whose shadows is being modified.  
            
         
        """
        pass
import NXOpen
class Stage(NXOpen.Builder): 
    """
    Represents a NXOpen.Display.Stage
    A stage is an environment cube, a six-sided room, that can have between 
    one and six visible walls.  You optionally specify a stage in Studio 
    rendering styles and High Quality Images.

     This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will return .
    

    """
    class OrientationType(Enum):
        """
        Members Include: 
         |Yz|  Use yz plane for the stage floor. 
         |Xz|  Use xz plane for the stage floor. 
         |Xy|  Use xy plane for the stage floor. 
         |UserDefined|  Use user defined plane for the stage floor. 

        """
        Yz: int
        Xz: int
        Xy: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> Stage.OrientationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class WallType(Enum):
        """
        Members Include: 
         |Left|  The left wall of the stage. 
         |Right|  The right wall of the stage. 
         |Top|  The top wall or "ceiling" of the stage. 
         |Bottom|  The bottom wall or "floor" of the stage. 
         |Front|  The front wall of the stage. 
         |Back|  The back wall of the stage. 
         |Total|  The total number of walls in the stage. 

        """
        Left: int
        Right: int
        Top: int
        Bottom: int
        Front: int
        Back: int
        Total: int
        @staticmethod
        def ValueOf(value: int) -> Stage.WallType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FloorOrientationType(self) -> Stage.OrientationType:
        """
        Getter for property: ( Stage.OrientationType NXOpen) FloorOrientationType
         Returns the floor orientation define   
            
         
        """
        pass
    @FloorOrientationType.setter
    def FloorOrientationType(self, floorOrientationType: Stage.OrientationType):
        """
        Setter for property: ( Stage.OrientationType NXOpen) FloorOrientationType
         Returns the floor orientation define   
            
         
        """
        pass
    @property
    def Offset(self) -> float:
        """
        Getter for property: (float) Offset
         Returns the offset distance to translate the stage in the z-direction, in part units   
            
         
        """
        pass
    @Offset.setter
    def Offset(self, offset: float):
        """
        Setter for property: (float) Offset
         Returns the offset distance to translate the stage in the z-direction, in part units   
            
         
        """
        pass
    @property
    def OffsetExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OffsetExpression
         Returns the stage offset expression  
            
         
        """
        pass
    @property
    def Size(self) -> float:
        """
        Getter for property: (float) Size
         Returns the size all of the stage walls (length and width), in part units   
            
         
        """
        pass
    @Size.setter
    def Size(self, size: float):
        """
        Setter for property: (float) Size
         Returns the size all of the stage walls (length and width), in part units   
            
         
        """
        pass
    @property
    def SizeExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SizeExpression
         Returns the stage size expression  
            
         
        """
        pass
    @property
    def SpecifyFloorPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) SpecifyFloorPlane
         Returns the specify floor plane   
            
         
        """
        pass
    @SpecifyFloorPlane.setter
    def SpecifyFloorPlane(self, specifyFloorPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) SpecifyFloorPlane
         Returns the specify floor plane   
            
         
        """
        pass
    def AlignFloorPlane(self, specifyFloorPlane: NXOpen.Plane) -> None:
        """
         The stage's bottom wall (floor) aligns with the given plane. 
        """
        pass
    def CommitOffset(self, view: NXOpen.View) -> None:
        """
         Updates the data and display for a change to the stage's offset 
        """
        pass
    def CommitWall(self, view: NXOpen.View, current_wall_index: int, update_stage_database: bool) -> None:
        """
         Updates the data and display for a given wall 
        """
        pass
    def FloorXaxis(self) -> None:
        """
         The stage's bottom wall to align with the WCS x-axis 
        """
        pass
    def FloorYaxis(self) -> None:
        """
         The stage's bottom wall to align with the WCS y-axis 
        """
        pass
    def FloorZaxis(self) -> None:
        """
         The stage's bottom wall to align with the WCS z-axis 
        """
        pass
    def GetWallFromList(self, index: Stage.WallType) -> Wall:
        """
         Returns a wall builder, given by the index, in the array of walls for the given stage 
         Returns wall ( Wall NXOpen):  the wall .
        """
        pass
    def SetWallInList(self, index: Stage.WallType, wall: Wall) -> None:
        """
         Sets a wall builder in the array at the given index 
        """
        pass
import NXOpen
class StudioImageCaptureBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Display.StudioImageCaptureBuilder  
    This class is available in an interactive as well as in non-interactive session supporting headless graphics. 
    ."""
    class AASamplesEnumType(Enum):
        """
        Members Include: 
         |Sam0X|  Do not set sampling option 
         |Sam2X|  Set sampling at 2 times 
         |Sam4X|  Set sampling at 4 times 
         |Sam8X|  Set sampling at 8 times 
         |Sam16X|  Set sampling at 16 times 

        """
        Sam0X: int
        Sam2X: int
        Sam4X: int
        Sam8X: int
        Sam16X: int
        @staticmethod
        def ValueOf(value: int) -> StudioImageCaptureBuilder.AASamplesEnumType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class BackgroundOptions(Enum):
        """
        Members Include: 
         |Original|  Use the currently displayed background 
         |CustomColor|  Use the solid color set by Display.StudioImageCaptureBuilder.SetCustomBackgroundColor 
         |Transparent|  Use a transparent background (only available in PNG and TIFF file formats) 

        """
        Original: int
        CustomColor: int
        Transparent: int
        @staticmethod
        def ValueOf(value: int) -> StudioImageCaptureBuilder.BackgroundOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DPIEnumType(Enum):
        """
        Members Include: 
         |Dpi72|  Set image at 72 DPI resolution 
         |Dpi150|  Set image at 150 DPI resolution 
         |Dpi400|  Set image at 400 DPI resolution 

        """
        Dpi72: int
        Dpi150: int
        Dpi400: int
        @staticmethod
        def ValueOf(value: int) -> StudioImageCaptureBuilder.DPIEnumType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DrawingSizeEnumType(Enum):
        """
        Members Include: 
         |Isoa4|  Use ISO A4 drawing size 
         |Isoa3|  Use ISO A3 drawing size 
         |Isoa2|  Use ISO A2 drawing size 
         |Isoa1|  Use ISO A1 drawing size 
         |Isoa0|  Use ISO A0 drawing size 
         |Ansia|  Use ANSI A drawing size 
         |Ansib|  Use ANSI B drawing size 
         |Ansic|  Use ANSI C drawing size 
         |Ansid|  Use ANSI D drawing size 
         |Ansie|  Use ANSI E drawing size 
         |Custom|  Use custom defined drawing size 

        """
        Isoa4: int
        Isoa3: int
        Isoa2: int
        Isoa1: int
        Isoa0: int
        Ansia: int
        Ansib: int
        Ansic: int
        Ansid: int
        Ansie: int
        Custom: int
        @staticmethod
        def ValueOf(value: int) -> StudioImageCaptureBuilder.DrawingSizeEnumType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OrientEnumType(Enum):
        """
        Members Include: 
         |Landscape|  Capture image in landscape mode 
         |Portrait|  Capture image in portrait mode 

        """
        Landscape: int
        Portrait: int
        @staticmethod
        def ValueOf(value: int) -> StudioImageCaptureBuilder.OrientEnumType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SourceType(Enum):
        """
        Members Include: 
         |WorkView|  Create image from work view 
         |Window|  Create image from window of work view 

        """
        WorkView: int
        Window: int
        @staticmethod
        def ValueOf(value: int) -> StudioImageCaptureBuilder.SourceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class UnitsEnumType(Enum):
        """
        Members Include: 
         |Pixels|  Use pixel to define resolution 
         |Mm|  Use Millimeters to define resolution 
         |Inches|  Use Inched to define resolution 

        """
        Pixels: int
        Mm: int
        Inches: int
        @staticmethod
        def ValueOf(value: int) -> StudioImageCaptureBuilder.UnitsEnumType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AASamplesEnum(self) -> StudioImageCaptureBuilder.AASamplesEnumType:
        """
        Getter for property: ( StudioImageCaptureBuilder.AASamplesEnumType NXOpen) AASamplesEnum
         Returns the antialiasing samples enum   
            
         
        """
        pass
    @AASamplesEnum.setter
    def AASamplesEnum(self, aASamplesEnum: StudioImageCaptureBuilder.AASamplesEnumType):
        """
        Setter for property: ( StudioImageCaptureBuilder.AASamplesEnumType NXOpen) AASamplesEnum
         Returns the antialiasing samples enum   
            
         
        """
        pass
    @property
    def BackgroundOption(self) -> StudioImageCaptureBuilder.BackgroundOptions:
        """
        Getter for property: ( StudioImageCaptureBuilder.BackgroundOptions NXOpen) BackgroundOption
         Returns the background option of capture image   
            
         
        """
        pass
    @BackgroundOption.setter
    def BackgroundOption(self, backgroundOption: StudioImageCaptureBuilder.BackgroundOptions):
        """
        Setter for property: ( StudioImageCaptureBuilder.BackgroundOptions NXOpen) BackgroundOption
         Returns the background option of capture image   
            
         
        """
        pass
    @property
    def DpiEnum(self) -> StudioImageCaptureBuilder.DPIEnumType:
        """
        Getter for property: ( StudioImageCaptureBuilder.DPIEnumType NXOpen) DpiEnum
         Returns the dpi enum   
            
         
        """
        pass
    @DpiEnum.setter
    def DpiEnum(self, dpiEnum: StudioImageCaptureBuilder.DPIEnumType):
        """
        Setter for property: ( StudioImageCaptureBuilder.DPIEnumType NXOpen) DpiEnum
         Returns the dpi enum   
            
         
        """
        pass
    @property
    def DrawingSizeEnum(self) -> StudioImageCaptureBuilder.DrawingSizeEnumType:
        """
        Getter for property: ( StudioImageCaptureBuilder.DrawingSizeEnumType NXOpen) DrawingSizeEnum
         Returns the drawing size enum   
            
         
        """
        pass
    @DrawingSizeEnum.setter
    def DrawingSizeEnum(self, drawingSizeEnum: StudioImageCaptureBuilder.DrawingSizeEnumType):
        """
        Setter for property: ( StudioImageCaptureBuilder.DrawingSizeEnumType NXOpen) DrawingSizeEnum
         Returns the drawing size enum   
            
         
        """
        pass
    @property
    def EnhanceEdges(self) -> bool:
        """
        Getter for property: (bool) EnhanceEdges
         Returns the enhance edges of capture image   
            
         
        """
        pass
    @EnhanceEdges.setter
    def EnhanceEdges(self, enhanceEdges: bool):
        """
        Setter for property: (bool) EnhanceEdges
         Returns the enhance edges of capture image   
            
         
        """
        pass
    @property
    def NativeFileBrowser(self) -> str:
        """
        Getter for property: (str) NativeFileBrowser
         Returns the native file browser for image type to produce   
            
         
        """
        pass
    @NativeFileBrowser.setter
    def NativeFileBrowser(self, filename: str):
        """
        Setter for property: (str) NativeFileBrowser
         Returns the native file browser for image type to produce   
            
         
        """
        pass
    @property
    def OrientEnum(self) -> StudioImageCaptureBuilder.OrientEnumType:
        """
        Getter for property: ( StudioImageCaptureBuilder.OrientEnumType NXOpen) OrientEnum
         Returns the orient enum   
            
         
        """
        pass
    @OrientEnum.setter
    def OrientEnum(self, orientEnum: StudioImageCaptureBuilder.OrientEnumType):
        """
        Setter for property: ( StudioImageCaptureBuilder.OrientEnumType NXOpen) OrientEnum
         Returns the orient enum   
            
         
        """
        pass
    @property
    def Source(self) -> StudioImageCaptureBuilder.SourceType:
        """
        Getter for property: ( StudioImageCaptureBuilder.SourceType NXOpen) Source
         Returns the source of image capture   
            
         
        """
        pass
    @Source.setter
    def Source(self, source: StudioImageCaptureBuilder.SourceType):
        """
        Setter for property: ( StudioImageCaptureBuilder.SourceType NXOpen) Source
         Returns the source of image capture   
            
         
        """
        pass
    @property
    def UnitsEnum(self) -> StudioImageCaptureBuilder.UnitsEnumType:
        """
        Getter for property: ( StudioImageCaptureBuilder.UnitsEnumType NXOpen) UnitsEnum
         Returns the units enum   
            
         
        """
        pass
    @UnitsEnum.setter
    def UnitsEnum(self, unitsEnum: StudioImageCaptureBuilder.UnitsEnumType):
        """
        Setter for property: ( StudioImageCaptureBuilder.UnitsEnumType NXOpen) UnitsEnum
         Returns the units enum   
            
         
        """
        pass
    def GetCustomBackgroundColor(self) -> List[float]:
        """
         Gets the custom background color of capture image 
         Returns customBackgroundColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def GetImageDimensionsDouble(self) -> List[float]:
        """
         Gets the double image dimensions, height and width 
         Returns imageDimensionsDouble (List[float]):  array of 2 doubles .
        """
        pass
    def GetImageDimensionsInteger(self) -> List[int]:
        """
         Gets the integer image dimensions, height and width 
         Returns imageDimensionsInteger (List[int]):  array of 2 integers .
        """
        pass
    def SetCustomBackgroundColor(self, customBackgroundColor: List[float]) -> None:
        """
         Sets the custom background color of capture image 
        """
        pass
    def SetImageDimensionsDouble(self, imageDimensionsDouble: List[float]) -> None:
        """
         Sets the double image dimensions, height and width 
        """
        pass
    def SetImageDimensionsInteger(self, imageDimensionsInteger: List[int]) -> None:
        """
         Sets the integer image dimensions, height and width 
        """
        pass
import NXOpen
class TransientText(NXOpen.TransientObject): 
    """ Represents temporary text strings which can be used for Temporary Display """
    class StandardTextRef(Enum):
        """
        Members Include: 
         |SystemDefault|  Display the text using the system
                                                                                     default reference point position 
         |BaselineStart|  Display the text starting on the
                                                                                     baseline, at the left end of the
                                                                                     text box for left-to-right text,
                                                                                     or at the right end of the text box
                                                                                     for right-to-left text 
         |BaselineCenter|  Display the text with the given position
                                                                                  in the horizontal center of the text box
                                                                                  at the baseline 
         |BaselineEnd|  Display the text starting on the baseline,
                                                                                at the right end of the text box
                                                                                for left-to-right text,
                                                                                or at the left end of the text box
                                                                                for right-to-left text 
         |TopLeft|  Display the text with the given position
                                                                                in the top left of the text box 
         |TopCenter|  Display the text with the given position
                                                                                in the top center of the text box 
         |TopRight|  Display the text with the given position
                                                                                in the top right of the text box 
         |MiddleLeft|  Display the text with the given position
                                                                                in the middle left of the text box 
         |MiddleCenter|  Display the text with the given position
                                                                                in middle center of text box 
         |MiddleRight|  Display the text with the given position
                                                                                in middle right of text box 
         |BottomLeft|  Display the text with the given position
                                                                                in bottom left of text box 
         |BottomCenter|  Display the text with the given position
                                                                                in bottom center of text box 
         |BottomRight|  Display the text with the given position
                                                                                in bottom right of text box 

        """
        SystemDefault: int
        BaselineStart: int
        BaselineCenter: int
        BaselineEnd: int
        TopLeft: int
        TopCenter: int
        TopRight: int
        MiddleLeft: int
        MiddleCenter: int
        MiddleRight: int
        BottomLeft: int
        BottomCenter: int
        BottomRight: int
        @staticmethod
        def ValueOf(value: int) -> TransientText.StandardTextRef:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TextSize(Enum):
        """
        Members Include: 
         |Small| 
         |Normal| 
         |Medium| 
         |Large| 
         |NumSizes| 

        """
        Small: int
        Normal: int
        Medium: int
        Large: int
        NumSizes: int
        @staticmethod
        def ValueOf(value: int) -> TransientText.TextSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ViewType(Enum):
        """
        Members Include: 
         |WorkViewOnly|  
         |AllActiveViews|  
         |ViewOfLastCursor|  
         |AllViewsButDrawing|  
         |AllActiveMemberViews|  
         |FirstViewFound|  

        """
        WorkViewOnly: int
        AllActiveViews: int
        ViewOfLastCursor: int
        AllViewsButDrawing: int
        AllActiveMemberViews: int
        FirstViewFound: int
        @staticmethod
        def ValueOf(value: int) -> TransientText.ViewType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Color(self) -> int:
        """
        Getter for property: (int) Color
         Returns the index of the color to be used to display the transient text.  
           If not specified,
                    the System Color will be used.   
         
        """
        pass
    @Color.setter
    def Color(self, colorIndex: int):
        """
        Setter for property: (int) Color
         Returns the index of the color to be used to display the transient text.  
           If not specified,
                    the System Color will be used.   
         
        """
        pass
    @property
    def FontStyle(self) -> str:
        """
        Getter for property: (str) FontStyle
         Returns  the style of font to be used to display the transient text.  
           Every text font has at least
                     one style.  To determine which styles a font has, use UF_UGFONT_ask_font_styles.
                     If not specified, the default font style for the font will be used.  
         
        """
        pass
    @FontStyle.setter
    def FontStyle(self, fontStlye: str):
        """
        Setter for property: (str) FontStyle
         Returns  the style of font to be used to display the transient text.  
           Every text font has at least
                     one style.  To determine which styles a font has, use UF_UGFONT_ask_font_styles.
                     If not specified, the default font style for the font will be used.  
         
        """
        pass
    @property
    def ReferencePositionType(self) -> TransientText.StandardTextRef:
        """
        Getter for property: ( TransientText.StandardTextRef NXOpen) ReferencePositionType
         Returns the position of the text relative to positions on the text box   
            
         
        """
        pass
    @ReferencePositionType.setter
    def ReferencePositionType(self, referencePositionType: TransientText.StandardTextRef):
        """
        Setter for property: ( TransientText.StandardTextRef NXOpen) ReferencePositionType
         Returns the position of the text relative to positions on the text box   
            
         
        """
        pass
    @property
    def ScreenTextSize(self) -> TransientText.TextSize:
        """
        Getter for property: ( TransientText.TextSize NXOpen) ScreenTextSize
         Returns the approximate size of the text (small, mendium, large) as measured on
                    the graphics screen.  
            This property is not used by
                     Display::TransientText::DisplayTemporaryAbsoluteGeometry .   
         
        """
        pass
    @ScreenTextSize.setter
    def ScreenTextSize(self, textSize: TransientText.TextSize):
        """
        Setter for property: ( TransientText.TextSize NXOpen) ScreenTextSize
         Returns the approximate size of the text (small, mendium, large) as measured on
                    the graphics screen.  
            This property is not used by
                     Display::TransientText::DisplayTemporaryAbsoluteGeometry .   
         
        """
        pass
    def AddTextString(self, textString: str) -> None:
        """
         Adds a text string to the TransientText object.  A TransientText object
                    may have one or more text strings.  If an attempt is made to display
                    a TransientText object with zero text strings, an error will be returned. 
        """
        pass
    def DisplayTemporaryAbsRotScreenSizeGeometry(self, fontIndex: int, view: NXOpen.View, viewType: TransientText.ViewType, objectValue: NXOpen.DisplayableObject, position: NXOpen.Point3d) -> None:
        """
          Displays text as temporary display using screen geometry.  The text will be 
                     displayed on the XY plane of the absolute coordinate system.  Insure that 
                     you have set all needed properties before using this method.  This method 
                     is not supported for 2D output such as CGM.  Note that size of the text is 
                     fixed and therefore does not scale with the view.  See 
                     Display.TransientText.set_ScreenTextSize for how 
                     to set the desired size.  Further note that by default this screen size text is "flipped" 
                     within its bounding box if necessary to ensure the text remains readable (front 
                     facing and approximately upright). 
        """
        pass
    def DisplayTemporaryAbsoluteGeometry(self, fontIndex: int, view: NXOpen.View, viewType: TransientText.ViewType, objectValue: NXOpen.DisplayableObject, position: NXOpen.Point3d) -> None:
        """
         Displays text as temporary display using absolute geometry.  Insure that 
                    you have set all needed properties before using this method.  Note that 
                    the text will be displayed on the Absolute XY plane, and therefore will rotate 
                    as the view orientation is changed.  At some view orientations the text can 
                    appear upside down or even backwards.  Sizes are expressed in the units of the 
                    displayed part.  See Display.TransientText.SetAbsoluteTextSize 
                    for how to set the text size.  Note that the apparent size of the text is view scale 
                    dependent and therefore will appear larger or smaller on screen as the view scale 
                    is modified. 
        """
        pass
    def DisplayTemporaryScreenGeometry(self, fontIndex: int, view: NXOpen.View, viewType: TransientText.ViewType, objectValue: NXOpen.DisplayableObject, position: NXOpen.Point3d) -> None:
        """
         Displays text as temporary display using screen geometry.  Insure that 
                    you have set all needed properties before using this method.  This method 
                    is not supported for 2D output such as CGM. See 
                    Display.TransientText.set_ScreenTextSize for how to 
                    adjust the size of the text.  Note that the displayed text remains screen parallel 
                    and front-facing, and appears the same size regardless of view orientation or scale. 
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector. 
        """
        pass
    def GetAbsoluteTextSize(self) -> Tuple[float, float]:
        """
         Returns the size of the text, in absolute coordinate, in units of the displayed part.
                     These values are only only used by
                     Display.TransientText.DisplayTemporaryAbsoluteGeometry. 
         Returns A tuple consisting of (glyphWidth, glyphHeight). 
         - glyphWidth is: float. .
         - glyphHeight is: float.

        """
        pass
    def SetAbsoluteTextSize(self, glyphWidth: float, glyphHeight: float) -> None:
        """
         Sets the size of the text, in absolute coordinates, in units of the displayed part.
                    These values are only used by
                    Display.TransientText.DisplayTemporaryAbsoluteGeometry.
        """
        pass
import NXOpen
class TrueShadingBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Display.TrueShading builder """
    class BgdImageType(Enum):
        """
        Members Include: 
         |Image1|  Predefined image 1 background 
         |Image2|  Predefined image 2 background 
         |Image3|  Predefined image 3 background 
         |Image4|  Predefined image 4 background 
         |Image5|  Predefined image 5 background 
         |Image6|  Predefined image 6 background 
         |CustomImage|  Custom image background 

        """
        Image1: int
        Image2: int
        Image3: int
        Image4: int
        Image5: int
        Image6: int
        CustomImage: int
        @staticmethod
        def ValueOf(value: int) -> TrueShadingBuilder.BgdImageType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class BgdType(Enum):
        """
        Members Include: 
         |DarkGraduated|  Graduated dark colored background 
         |LightGraduated|  Graduated light colored background 
         |Black|  Plain dark Colored background 
         |White|  Plain light Colored background 
         |CustomPlain|  Customized plain colored background 
         |CustomGraduated|  Customized graduated colored background 
         |InheritShadedBackground|  Use same background color as in shaded display mode 
         |ImageBackground|  Use one of the predefined images as background 
         |PureWhite|  Plain light Colored background 

        """
        DarkGraduated: int
        LightGraduated: int
        Black: int
        White: int
        CustomPlain: int
        CustomGraduated: int
        InheritShadedBackground: int
        ImageBackground: int
        PureWhite: int
        @staticmethod
        def ValueOf(value: int) -> TrueShadingBuilder.BgdType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EnvironmentMapType(Enum):
        """
        Members Include: 
         |Default|  No reflection map 
         |MetalShiny1|  Shiny Metal Reflection 1 
         |MetalShiny2|  Shiny Metal Reflection 2 
         |MetalBrushed1|  Brushed Metal Reflection 1 
         |MetalBrushed2|  Brushed Metal Reflection 2 
         |Glossy1|  Glossy Reflection 1 
         |Glossy2|  Glossy Reflection 2 
         |SurfaceAnalysisLines|  Surface Analysis Lines Reflection 
         |SurfaceAnalysisHorizon|  Surface Analysis Horizontal Lines Reflection 
         |AutoPhotoStudio|  Automotive Lighting Reflection 
         |CustomImage|  Custom Image Reflection 

        """
        Default: int
        MetalShiny1: int
        MetalShiny2: int
        MetalBrushed1: int
        MetalBrushed2: int
        Glossy1: int
        Glossy2: int
        SurfaceAnalysisLines: int
        SurfaceAnalysisHorizon: int
        AutoPhotoStudio: int
        CustomImage: int
        @staticmethod
        def ValueOf(value: int) -> TrueShadingBuilder.EnvironmentMapType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MaterialType(Enum):
        """
        Members Include: 
         |GlobalWashShinyMetal|  Shiny Metal Wash 
         |GlobalWashBrushedMetal|  Brushed Metal Wash 
         |GlobalWashShinyPlastic|  Shiny Plastic Wash 
         |GlobalWashAnalysis|  Surface Analysis Wash 
         |GlobalWashFlat|  Low Sheen Plastic Wash 
         |GlobalRedGlossyPlastic|  Red Glossy Plastic 
         |GlobalBlueGlossyPlastic|  Blue Glossy Plastic 
         |GlobalGreenGlossyPlastic|  Green Glossy Plastic 
         |GlobalGrayGlossyPlastic|  Gray Glossy Plastic 
         |GlobalBlackGlossyPlastic|  Black Glossy Plastic 
         |GlobalBrownGlossyPlastic|  Brown Glossy Plastic 
         |GlobalYellowGlossyPlastic|  Yellow Glossy Plastic 
         |GlobalTealGlossyPlastic|  Teal Glossy Plastic 
         |GlobalWhiteGlossyPlastic|  White Glossy Plastic 
         |GlobalClearPlastic|  Clear Plastic 
         |GlobalChrome|  Chrome 
         |GlobalCopper|  Copper 
         |GlobalGold|  Gold 
         |GlobalBrass|  Brass 
         |GlobalSteel|  Steel 
         |GlobalBrushedChrome|  Brushed Chrome 
         |GlobalBrushedAluminum|  Brushed Aluminum 
         |GlobalBrushedTitanium|  Brushed Titanium 
         |GlobalGlassClear|  Clear Glass 
         |GlobalGlassSmokey|  Smokey Glass 
         |GlobalMetallicPaintRed|  Red Metallic Paint 
         |GlobalMetallicPaintGray|  Gray Metallic Paint 
         |GlobalMetallicPaintBlack|  Black Metallic Paint 
         |GlobalMetallicPaintBlue|  Blue Metallic Paint 
         |GlobalRubber|  Black Rubber 
         |OverrideRedGlossyPlastic|  Red Glossy Plastic 
         |OverrideBlueGlossyPlastic|  Blue Glossy Plastic 
         |OverrideGreenGlossyPlastic|  Green Glossy Plastic 
         |OverrideGrayGlossyPlastic|  Gray Glossy Plastic 
         |OverrideBlackGlossyPlastic|  Black Glossy Plastic 
         |OverrideBrownGlossyPlastic|  Brown Glossy Plastic 
         |OverrideYellowGlossyPlastic|  Yellow Glossy Plastic 
         |OverrideTealGlossyPlastic|  Teal Glossy Plastic 
         |OverrideWhiteGlossyPlastic|  White Glossy Plastic 
         |OverrideClearPlastic|  Clear Plastic 
         |OverrideChrome|  Chrome 
         |OverrideCopper|  Copper 
         |OverrideGold|  Gold 
         |OverrideBrass|  Brass 
         |OverrideSteel|  Steel 
         |OverrideBrushedChrome|  Brushed Chrome 
         |OverrideBrushedAluminum|  Brushed Aluminum 
         |OverrideBrushedTitanium|  Brushed Titanium 
         |OverrideGlassClear|  Clear Glass 
         |OverrideGlassSmokey|  Smokey Glass 
         |OverrideMetallicPaintRed|  Red Metallic Paint 
         |OverrideMetallicPaintGray|  Gray Metallic Paint 
         |OverrideMetallicPaintBlack|  Black Metallic Paint 
         |OverrideMetallicPaintBlue|  Blue Metallic Paint 
         |OverrideRubber|  Black Rubber 
         |OverrideRoughMetalMedGray|  Medium Grey Texture 
         |OverrideRoughMetalDkGray|  Dark Grey Texture 
         |OverrideRoughPlasticBlueGray|  Blue Grey Texture 
         |OverrideRoughPlasticTan|  Tan Texture 

        """
        GlobalWashShinyMetal: int
        GlobalWashBrushedMetal: int
        GlobalWashShinyPlastic: int
        GlobalWashAnalysis: int
        GlobalWashFlat: int
        GlobalRedGlossyPlastic: int
        GlobalBlueGlossyPlastic: int
        GlobalGreenGlossyPlastic: int
        GlobalGrayGlossyPlastic: int
        GlobalBlackGlossyPlastic: int
        GlobalBrownGlossyPlastic: int
        GlobalYellowGlossyPlastic: int
        GlobalTealGlossyPlastic: int
        GlobalWhiteGlossyPlastic: int
        GlobalClearPlastic: int
        GlobalChrome: int
        GlobalCopper: int
        GlobalGold: int
        GlobalBrass: int
        GlobalSteel: int
        GlobalBrushedChrome: int
        GlobalBrushedAluminum: int
        GlobalBrushedTitanium: int
        GlobalGlassClear: int
        GlobalGlassSmokey: int
        GlobalMetallicPaintRed: int
        GlobalMetallicPaintGray: int
        GlobalMetallicPaintBlack: int
        GlobalMetallicPaintBlue: int
        GlobalRubber: int
        OverrideRedGlossyPlastic: int
        OverrideBlueGlossyPlastic: int
        OverrideGreenGlossyPlastic: int
        OverrideGrayGlossyPlastic: int
        OverrideBlackGlossyPlastic: int
        OverrideBrownGlossyPlastic: int
        OverrideYellowGlossyPlastic: int
        OverrideTealGlossyPlastic: int
        OverrideWhiteGlossyPlastic: int
        OverrideClearPlastic: int
        OverrideChrome: int
        OverrideCopper: int
        OverrideGold: int
        OverrideBrass: int
        OverrideSteel: int
        OverrideBrushedChrome: int
        OverrideBrushedAluminum: int
        OverrideBrushedTitanium: int
        OverrideGlassClear: int
        OverrideGlassSmokey: int
        OverrideMetallicPaintRed: int
        OverrideMetallicPaintGray: int
        OverrideMetallicPaintBlack: int
        OverrideMetallicPaintBlue: int
        OverrideRubber: int
        OverrideRoughMetalMedGray: int
        OverrideRoughMetalDkGray: int
        OverrideRoughPlasticBlueGray: int
        OverrideRoughPlasticTan: int
        @staticmethod
        def ValueOf(value: int) -> TrueShadingBuilder.MaterialType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SHEDLightCollectionType(Enum):
        """
        Members Include: 
         |DefaultLights|  Scene lighting collection 1 
         |Lighting1|  Scene lighting collection 2 
         |Lighting2|  Scene lighting collection 3 
         |Lighting3|  Scene lighting collection 4 
         |Lighting4|  Scene lighting collection 5 
         |Custom|  Custom lighting configuration 

        """
        DefaultLights: int
        Lighting1: int
        Lighting2: int
        Lighting3: int
        Lighting4: int
        Custom: int
        @staticmethod
        def ValueOf(value: int) -> TrueShadingBuilder.SHEDLightCollectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SurfaceOrientType(Enum):
        """
        Members Include: 
         |NotSet|  Do not project shadows 
         |Bottom|  Project shadows onto the floor 
         |Back|  Project shadows onto the back wall 
         |BottomFixed|  Project shadows onto a fixed oriented floor 

        """
        NotSet: int
        Bottom: int
        Back: int
        BottomFixed: int
        @staticmethod
        def ValueOf(value: int) -> TrueShadingBuilder.SurfaceOrientType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BgdImageEnum(self) -> TrueShadingBuilder.BgdImageType:
        """
        Getter for property: ( TrueShadingBuilder.BgdImageType NXOpen) BgdImageEnum
         Returns the background image list enum   
            
         
        """
        pass
    @BgdImageEnum.setter
    def BgdImageEnum(self, bgdImageEnum: TrueShadingBuilder.BgdImageType):
        """
        Setter for property: ( TrueShadingBuilder.BgdImageType NXOpen) BgdImageEnum
         Returns the background image list enum   
            
         
        """
        pass
    @property
    def BgdImageFileBrowser(self) -> str:
        """
        Getter for property: (str) BgdImageFileBrowser
         Returns the background image filename   
            
         
        """
        pass
    @BgdImageFileBrowser.setter
    def BgdImageFileBrowser(self, filename: str):
        """
        Setter for property: (str) BgdImageFileBrowser
         Returns the background image filename   
            
         
        """
        pass
    @property
    def BgdTypeEnum(self) -> TrueShadingBuilder.BgdType:
        """
        Getter for property: ( TrueShadingBuilder.BgdType NXOpen) BgdTypeEnum
         Returns the background color or background image type enum   
            
         
        """
        pass
    @BgdTypeEnum.setter
    def BgdTypeEnum(self, bgdTypeEnum: TrueShadingBuilder.BgdType):
        """
        Setter for property: ( TrueShadingBuilder.BgdType NXOpen) BgdTypeEnum
         Returns the background color or background image type enum   
            
         
        """
        pass
    @property
    def EnvironmentMapEnum(self) -> TrueShadingBuilder.EnvironmentMapType:
        """
        Getter for property: ( TrueShadingBuilder.EnvironmentMapType NXOpen) EnvironmentMapEnum
         Returns the reflection environment map enum type   
            
         
        """
        pass
    @EnvironmentMapEnum.setter
    def EnvironmentMapEnum(self, environmentMapEnum: TrueShadingBuilder.EnvironmentMapType):
        """
        Setter for property: ( TrueShadingBuilder.EnvironmentMapType NXOpen) EnvironmentMapEnum
         Returns the reflection environment map enum type   
            
         
        """
        pass
    @property
    def EnvironmentMapFileBrowser(self) -> str:
        """
        Getter for property: (str) EnvironmentMapFileBrowser
         Returns the reflection environment map filename   
            
         
        """
        pass
    @EnvironmentMapFileBrowser.setter
    def EnvironmentMapFileBrowser(self, filename: str):
        """
        Setter for property: (str) EnvironmentMapFileBrowser
         Returns the reflection environment map filename   
            
         
        """
        pass
    @property
    def GlobalMaterialType(self) -> TrueShadingBuilder.MaterialType:
        """
        Getter for property: ( TrueShadingBuilder.MaterialType NXOpen) GlobalMaterialType
         Returns the globalMaterialType   
            
         
        """
        pass
    @GlobalMaterialType.setter
    def GlobalMaterialType(self, globalMaterialType: TrueShadingBuilder.MaterialType):
        """
        Setter for property: ( TrueShadingBuilder.MaterialType NXOpen) GlobalMaterialType
         Returns the globalMaterialType   
            
         
        """
        pass
    @property
    def InheritModelTogggle(self) -> bool:
        """
        Getter for property: (bool) InheritModelTogggle
         Returns the shadow plane grid to inherit Model grid attributes toggle   
            
         
        """
        pass
    @InheritModelTogggle.setter
    def InheritModelTogggle(self, inheritModelTogggle: bool):
        """
        Setter for property: (bool) InheritModelTogggle
         Returns the shadow plane grid to inherit Model grid attributes toggle   
            
         
        """
        pass
    @property
    def LightCollectionEnum(self) -> TrueShadingBuilder.SHEDLightCollectionType:
        """
        Getter for property: ( TrueShadingBuilder.SHEDLightCollectionType NXOpen) LightCollectionEnum
         Returns the light collection enum   
            
         
        """
        pass
    @LightCollectionEnum.setter
    def LightCollectionEnum(self, lightCollectionEnum: TrueShadingBuilder.SHEDLightCollectionType):
        """
        Setter for property: ( TrueShadingBuilder.SHEDLightCollectionType NXOpen) LightCollectionEnum
         Returns the light collection enum   
            
         
        """
        pass
    @property
    def LightDimmerValue(self) -> float:
        """
        Getter for property: (float) LightDimmerValue
         Returns the light dimmer value   
            
         
        """
        pass
    @LightDimmerValue.setter
    def LightDimmerValue(self, lightDimmerValue: float):
        """
        Setter for property: (float) LightDimmerValue
         Returns the light dimmer value   
            
         
        """
        pass
    @property
    def ObjSpecificSelection(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) ObjSpecificSelection
         Returns the selected object(s) list    
            
         
        """
        pass
    @property
    def PlanarReflectionToggle(self) -> bool:
        """
        Getter for property: (bool) PlanarReflectionToggle
         Returns the planar reflection visibility toggle   
            
         
        """
        pass
    @PlanarReflectionToggle.setter
    def PlanarReflectionToggle(self, planarReflectionToggle: bool):
        """
        Setter for property: (bool) PlanarReflectionToggle
         Returns the planar reflection visibility toggle   
            
         
        """
        pass
    @property
    def PlanarShadowToggle(self) -> bool:
        """
        Getter for property: (bool) PlanarShadowToggle
         Returns the planar shadow visibility toggle   
            
         
        """
        pass
    @PlanarShadowToggle.setter
    def PlanarShadowToggle(self, planarShadowToggle: bool):
        """
        Setter for property: (bool) PlanarShadowToggle
         Returns the planar shadow visibility toggle   
            
         
        """
        pass
    @property
    def PlaneGridToggle(self) -> bool:
        """
        Getter for property: (bool) PlaneGridToggle
         Returns the shadow plane grid visibility toggle   
            
         
        """
        pass
    @PlaneGridToggle.setter
    def PlaneGridToggle(self, planeGridToggle: bool):
        """
        Setter for property: (bool) PlaneGridToggle
         Returns the shadow plane grid visibility toggle   
            
         
        """
        pass
    @property
    def PlaneOffsetFixedToggle(self) -> bool:
        """
        Getter for property: (bool) PlaneOffsetFixedToggle
         Returns the shadow plane with fixed offset toggle   
            
         
        """
        pass
    @PlaneOffsetFixedToggle.setter
    def PlaneOffsetFixedToggle(self, planeOffsetFixedToggle: bool):
        """
        Setter for property: (bool) PlaneOffsetFixedToggle
         Returns the shadow plane with fixed offset toggle   
            
         
        """
        pass
    @property
    def PlaneOffsetValue(self) -> float:
        """
        Getter for property: (float) PlaneOffsetValue
         Returns the offset distance between the shadow plane and the nearest vertex of the displayed object   
            
         
        """
        pass
    @PlaneOffsetValue.setter
    def PlaneOffsetValue(self, planeOffsetValue: float):
        """
        Setter for property: (float) PlaneOffsetValue
         Returns the offset distance between the shadow plane and the nearest vertex of the displayed object   
            
         
        """
        pass
    @property
    def ReflectivityValue(self) -> float:
        """
        Getter for property: (float) ReflectivityValue
         Returns the reflectivity value   
            
         
        """
        pass
    @ReflectivityValue.setter
    def ReflectivityValue(self, reflectivityValue: float):
        """
        Setter for property: (float) ReflectivityValue
         Returns the reflectivity value   
            
         
        """
        pass
    @property
    def ShedModeToggle(self) -> bool:
        """
        Getter for property: (bool) ShedModeToggle
         Returns the True Shading display toggle state   
            
         
        """
        pass
    @ShedModeToggle.setter
    def ShedModeToggle(self, shedModeToggle: bool):
        """
        Setter for property: (bool) ShedModeToggle
         Returns the True Shading display toggle state   
            
         
        """
        pass
    @property
    def SnapFloorToggle(self) -> bool:
        """
        Getter for property: (bool) SnapFloorToggle
         Returns the toggle forces the shadow plane to snap to the nearest object vertex   
            
         
        """
        pass
    @SnapFloorToggle.setter
    def SnapFloorToggle(self, snapFloorToggle: bool):
        """
        Setter for property: (bool) SnapFloorToggle
         Returns the toggle forces the shadow plane to snap to the nearest object vertex   
            
         
        """
        pass
    @property
    def SoftShadowsToggle(self) -> bool:
        """
        Getter for property: (bool) SoftShadowsToggle
         Returns the soft shadows toggle   
            
         
        """
        pass
    @SoftShadowsToggle.setter
    def SoftShadowsToggle(self, softShadowsToggle: bool):
        """
        Setter for property: (bool) SoftShadowsToggle
         Returns the soft shadows toggle   
            
         
        """
        pass
    @property
    def SpecifyPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) SpecifyPlane
         Returns the custom plane definition for the shadow projection   
            
         
        """
        pass
    @SpecifyPlane.setter
    def SpecifyPlane(self, specifyPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) SpecifyPlane
         Returns the custom plane definition for the shadow projection   
            
         
        """
        pass
    @property
    def SurfaceOrientEnum(self) -> TrueShadingBuilder.SurfaceOrientType:
        """
        Getter for property: ( TrueShadingBuilder.SurfaceOrientType NXOpen) SurfaceOrientEnum
         Returns the shadow plane surface orientation enum   
            
         
        """
        pass
    @SurfaceOrientEnum.setter
    def SurfaceOrientEnum(self, surfaceOrientEnum: TrueShadingBuilder.SurfaceOrientType):
        """
        Setter for property: ( TrueShadingBuilder.SurfaceOrientType NXOpen) SurfaceOrientEnum
         Returns the shadow plane surface orientation enum   
            
         
        """
        pass
    def AssignOverrideMaterial(self, overrideMaterialType: TrueShadingBuilder.MaterialType) -> None:
        """
         Assigns an overriding material type to one or more selected objects 
        """
        pass
    def GButton0(self) -> None:
        """
         Global material button 1 
        """
        pass
    def GButton1(self) -> None:
        """
         Global material button 2 
        """
        pass
    def GButton10(self) -> None:
        """
         Global material button 11 
        """
        pass
    def GButton11(self) -> None:
        """
         Global material button 12 
        """
        pass
    def GButton12(self) -> None:
        """
         Global material button 13 
        """
        pass
    def GButton13(self) -> None:
        """
         Global material button 14 
        """
        pass
    def GButton14(self) -> None:
        """
         Global material button 15 
        """
        pass
    def GButton15(self) -> None:
        """
         Global material button 16 
        """
        pass
    def GButton16(self) -> None:
        """
         Global material button 17 
        """
        pass
    def GButton17(self) -> None:
        """
         Global material button 18 
        """
        pass
    def GButton18(self) -> None:
        """
         Global material button 19 
        """
        pass
    def GButton19(self) -> None:
        """
         Global material button 20 
        """
        pass
    def GButton2(self) -> None:
        """
         Global material button 3 
        """
        pass
    def GButton20(self) -> None:
        """
         Global material button 21 
        """
        pass
    def GButton21(self) -> None:
        """
         Global material button 22 
        """
        pass
    def GButton22(self) -> None:
        """
         Global material button 23 
        """
        pass
    def GButton23(self) -> None:
        """
         Global material button 24 
        """
        pass
    def GButton24(self) -> None:
        """
         Global material button 25 
        """
        pass
    def GButton25(self) -> None:
        """
         Global material button 26 
        """
        pass
    def GButton26(self) -> None:
        """
         Global material button 27 
        """
        pass
    def GButton27(self) -> None:
        """
         Global material button 28 
        """
        pass
    def GButton28(self) -> None:
        """
         Global material button 29 
        """
        pass
    def GButton29(self) -> None:
        """
         Global material button 30 
        """
        pass
    def GButton3(self) -> None:
        """
         Global material button 4 
        """
        pass
    def GButton4(self) -> None:
        """
         Global material button 5 
        """
        pass
    def GButton5(self) -> None:
        """
         Global material button 6 
        """
        pass
    def GButton6(self) -> None:
        """
         Global material button 7 
        """
        pass
    def GButton7(self) -> None:
        """
         Global material button 8 
        """
        pass
    def GButton8(self) -> None:
        """
         Global material button 9 
        """
        pass
    def GButton9(self) -> None:
        """
         Global material button 10 
        """
        pass
    def GetBgdBottomRgbcolorPicker(self) -> List[float]:
        """
         Returns the RGB values of background bottom color picker 
         Returns bgdBottomRGBColorPicker (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def GetBgdTopRgbcolorPicker(self) -> List[float]:
        """
         Returns the RGB values of background top color picker 
         Returns bgdTopRGBColorPicker (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def GetGridRgbcolorPicker(self) -> List[float]:
        """
         Returns the grid RGB color values picker 
         Returns gridRGBColorPicker (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def OButton0(self) -> None:
        """
         Per Object override material button 1 
        """
        pass
    def OButton1(self) -> None:
        """
         Per Object override material button 2 
        """
        pass
    def OButton10(self) -> None:
        """
         Per Object override material button 11 
        """
        pass
    def OButton11(self) -> None:
        """
         Per Object override material button 12 
        """
        pass
    def OButton12(self) -> None:
        """
         Per Object override material button 13 
        """
        pass
    def OButton13(self) -> None:
        """
         Per Object override material button 14 
        """
        pass
    def OButton14(self) -> None:
        """
         Per Object override material button 15 
        """
        pass
    def OButton15(self) -> None:
        """
         Per Object override material button 16 
        """
        pass
    def OButton16(self) -> None:
        """
         Per Object override material button 17 
        """
        pass
    def OButton17(self) -> None:
        """
         Per Object override material button 18 
        """
        pass
    def OButton18(self) -> None:
        """
         Per Object override material button 19 
        """
        pass
    def OButton19(self) -> None:
        """
         Per Object override material button 20 
        """
        pass
    def OButton2(self) -> None:
        """
         Per Object override material button 3 
        """
        pass
    def OButton20(self) -> None:
        """
         Per Object override material button 21 
        """
        pass
    def OButton21(self) -> None:
        """
         Per Object override material button 22 
        """
        pass
    def OButton22(self) -> None:
        """
         Per Object override material button 23 
        """
        pass
    def OButton23(self) -> None:
        """
         Per Object override material button 24 
        """
        pass
    def OButton24(self) -> None:
        """
         Per Object override material button 25 
        """
        pass
    def OButton25(self) -> None:
        """
         Per Object override material button 26 
        """
        pass
    def OButton26(self) -> None:
        """
         Per Object override material button 27 
        """
        pass
    def OButton27(self) -> None:
        """
         Per Object override material button 28 
        """
        pass
    def OButton28(self) -> None:
        """
         Per Object override material button 29 
        """
        pass
    def OButton3(self) -> None:
        """
         Per Object override material button 4 
        """
        pass
    def OButton4(self) -> None:
        """
         Per Object override material button 5 
        """
        pass
    def OButton5(self) -> None:
        """
         Per Object override material button 6 
        """
        pass
    def OButton6(self) -> None:
        """
         Per Object override material button 7 
        """
        pass
    def OButton7(self) -> None:
        """
         Per Object override material button 8 
        """
        pass
    def OButton8(self) -> None:
        """
         Per Object override material button 9 
        """
        pass
    def OButton9(self) -> None:
        """
         Per Object override material button 10 
        """
        pass
    def ORemoveButton(self) -> None:
        """
         Removes override material from selected object(s) 
        """
        pass
    def ProtectUpdate(self) -> None:
        """
         Protects update 
        """
        pass
    def SetBgdBottomRgbcolorPicker(self, bgdBottomRGBColorPicker: List[float]) -> None:
        """
         Sets the RGB values of background bottom color picker 
        """
        pass
    def SetBgdTopRgbcolorPicker(self, bgdTopRGBColorPicker: List[float]) -> None:
        """
         Sets the RGB values of background top color picker 
        """
        pass
    def SetGridRgbcolorPicker(self, gridRGBColorPicker: List[float]) -> None:
        """
         Sets the grid RGB color picker 
        """
        pass
import NXOpen
class TrueShadingCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection SHED objects
  """
    def CreateTrueShadingBuilder(self, sObj: TrueShading) -> TrueShadingBuilder:
        """
         Creates a NXOpen.Display.TrueShadingBuilder object 
                if SHED is .  Otherwise, a TrueShading object will be edited 
            
         Returns builder ( TrueShadingBuilder NXOpen):  return SHED object builder .
        """
        pass
    def FindObject(self, journal_identifier: str) -> TrueShading:
        """
         Finds the  NXOpen.Display.TrueShading  with the given identifier
                as recorded in a journal. An object may not return the same value as its 
                JournalIdentifier in different versions of the software. However newer versions 
                of the software should find the same object when FindObject is passed older versions 
                of its journal identifier. In general, this method should not be used in handwritten
                code and exists to support record and playback of journals.
                An exception will be thrown if no object found with the given journal identifier. 
            
         Returns found ( TrueShading NXOpen):  SHED object found .
        """
        pass
    def IsTrueShadeEnabled(self) -> bool:
        """
         Gets the True Shading flag from the input part.
             
         Returns enabled (bool):  Indicates if it is True Shading display style .
        """
        pass
import NXOpen
class TrueShading(NXOpen.NXObject): 
    """ Represents a True Shading object """
    pass
import NXOpen
class TrueStudioBuilder(NXOpen.Builder): 
    """ The TrueStudioBuillder manages Advanced Studio visualization display """
    class GlobalMaterial(Enum):
        """
        Members Include: 
         |PlasticColorwash|  Uses the object's color with plastic material characteristics. 
         |ShinyMetalColorwash|  Uses the object's color with shiny metal material characteristics.
         |Clay|  Overrides the object color with a clay material display. 
         |Plasticine|  Overrides the object color with a plasticine material display. 
         |Chrome|  Overrides the object color with a chrome material display. 

        """
        PlasticColorwash: int
        ShinyMetalColorwash: int
        Clay: int
        Plasticine: int
        Chrome: int
        @staticmethod
        def ValueOf(value: int) -> TrueStudioBuilder.GlobalMaterial:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RenderMethod(Enum):
        """
        Members Include: 
         |FullRender|  All rendering effects are honored. 
         |ImprovedRender|  Some rendering effects are not honored.  Can be faster than Full Render. 
         |PreviewRender|  Many rendering effects are not honored.  Faster than Full and Improved Render. 

        """
        FullRender: int
        ImprovedRender: int
        PreviewRender: int
        @staticmethod
        def ValueOf(value: int) -> TrueStudioBuilder.RenderMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def GlobalMaterialType(self) -> TrueStudioBuilder.GlobalMaterial:
        """
        Getter for property: ( TrueStudioBuilder.GlobalMaterial NXOpen) GlobalMaterialType
         Returns the Global Material Type is used in Advanced Studio display when no material has been applied to the object.  
             
         
        """
        pass
    @GlobalMaterialType.setter
    def GlobalMaterialType(self, globalMaterialType: TrueStudioBuilder.GlobalMaterial):
        """
        Setter for property: ( TrueStudioBuilder.GlobalMaterial NXOpen) GlobalMaterialType
         Returns the Global Material Type is used in Advanced Studio display when no material has been applied to the object.  
             
         
        """
        pass
    @property
    def ModeToggle(self) -> bool:
        """
        Getter for property: (bool) ModeToggle
         Returns the Mode Toggle controls whether Advanced Studio display is enabled.  
             
         
        """
        pass
    @ModeToggle.setter
    def ModeToggle(self, modeToggle: bool):
        """
        Setter for property: (bool) ModeToggle
         Returns the Mode Toggle controls whether Advanced Studio display is enabled.  
             
         
        """
        pass
    @property
    def RenderMethodType(self) -> TrueStudioBuilder.RenderMethod:
        """
        Getter for property: ( TrueStudioBuilder.RenderMethod NXOpen) RenderMethodType
         Returns the Render Method Type is used in Advanced Studio display to control the display quality and performance   
            
         
        """
        pass
    @RenderMethodType.setter
    def RenderMethodType(self, renderMethodType: TrueStudioBuilder.RenderMethod):
        """
        Setter for property: ( TrueStudioBuilder.RenderMethod NXOpen) RenderMethodType
         Returns the Render Method Type is used in Advanced Studio display to control the display quality and performance   
            
         
        """
        pass
import NXOpen
class TrueStudioCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection TrueStudio objects
  """
    def CreateTrueStudioBuilder(self, sObj: TrueStudio) -> TrueStudioBuilder:
        """
         Creates a NXOpen.Display.TrueStudioBuilder object 
                if TrueStudio is .  Otherwise, a TrueStudio object will be edited 
            
         Returns builder ( TrueStudioBuilder NXOpen):  return TrueStudio object builder .
        """
        pass
    def FindObject(self, journal_identifier: str) -> TrueStudio:
        """
         Finds the  NXOpen.Display.TrueStudio  with the given identifier
                as recorded in a journal. An object may not return the same value as its 
                JournalIdentifier in different versions of the software. However newer versions 
                of the software should find the same object when FindObject is passed older versions 
                of its journal identifier. In general, this method should not be used in handwritten
                code and exists to support record and playback of journals.
                An exception will be thrown if no object found with the given journal identifier. 
            
         Returns found ( TrueStudio NXOpen):  TrueStudio object found .
        """
        pass
import NXOpen
class TrueStudio(NXOpen.NXObject): 
    """ Represents a True Shading object """
    pass
import NXOpen
class UVMapBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Display.UVMapBuilder 
    """
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
    def ObjectToUnwrap(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) ObjectToUnwrap
         Returns the body or faces to unwrap   
            
         
        """
        pass
    @property
    def RipEdges(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) RipEdges
         Returns the rip edges   
            
         
        """
        pass
    @property
    def UDirection(self) -> NXOpen.SelectSelectObject:
        """
        Getter for property: ( NXOpen.SelectSelectObject) UDirection
         Returns the u direction   
            
         
        """
        pass
    @property
    def UVDiagnostics(self) -> bool:
        """
        Getter for property: (bool) UVDiagnostics
         Returns the flag indicating if mapped diagnostics image should be displayed or not.  
             
         
        """
        pass
    @UVDiagnostics.setter
    def UVDiagnostics(self, uvDiagnostics: bool):
        """
        Setter for property: (bool) UVDiagnostics
         Returns the flag indicating if mapped diagnostics image should be displayed or not.  
             
         
        """
        pass
import NXOpen
class UVMapCollection(NXOpen.TaggedObjectCollection): 
    """
    Represents a collection of UV Map object in a part.
    This class is restricted to being called from a program running during an
    Interactive NX session.  If run from a non-interactive session it will
    return .
    """
    def CreateUVMapBuilder(self, uvParam: UVMap) -> UVMapBuilder:
        """
         Creates a NXOpen.Display.UVMapBuilder. 
         Returns builder ( UVMapBuilder NXOpen):   .
        """
        pass
    def FindObject(self, journal_identifier: str) -> UVMap:
        """
         Finds the  NXOpen.Display.UVMap  with the given identifier as recorded in a journal.
                An object may not return the same value as its JournalIdentifier in different versions of
                the software. However newer versions of the software should find the same object when
                FindObject is passed older versions of its journal identifier. In general, this method
                should not be used in handwritten code and exists to support record and playback of journals.
                An exception will be thrown if no object can be found with the given journal identifier. 
         Returns foundUVparam ( UVMap NXOpen):  UVParam found .
        """
        pass
import NXOpen
class UVMap(NXOpen.NXObject): 
    """ Represents a NXOpen.Display.UVMap that provides  
    UV Mapping for selected faces.
    """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class UVTransformationData(NXOpen.TaggedObject): 
    """ Represents a NXOpen.Display.UVTransformationData. """
    @property
    def RotationX(self) -> float:
        """
        Getter for property: (float) RotationX
         Returns the X value of rotation around the origin point   
            
         
        """
        pass
    @RotationX.setter
    def RotationX(self, rotationX: float):
        """
        Setter for property: (float) RotationX
         Returns the X value of rotation around the origin point   
            
         
        """
        pass
    @property
    def RotationY(self) -> float:
        """
        Getter for property: (float) RotationY
         Returns the Y value of rotation around the origin point   
            
         
        """
        pass
    @RotationY.setter
    def RotationY(self, rotationY: float):
        """
        Setter for property: (float) RotationY
         Returns the Y value of rotation around the origin point   
            
         
        """
        pass
    @property
    def RotationZ(self) -> float:
        """
        Getter for property: (float) RotationZ
         Returns the Z value of rotation around the origin point   
            
         
        """
        pass
    @RotationZ.setter
    def RotationZ(self, rotationZ: float):
        """
        Setter for property: (float) RotationZ
         Returns the Z value of rotation around the origin point   
            
         
        """
        pass
    @property
    def TranslationX(self) -> float:
        """
        Getter for property: (float) TranslationX
         Returns the X direction of translation   
            
         
        """
        pass
    @TranslationX.setter
    def TranslationX(self, translationX: float):
        """
        Setter for property: (float) TranslationX
         Returns the X direction of translation   
            
         
        """
        pass
    @property
    def TranslationY(self) -> float:
        """
        Getter for property: (float) TranslationY
         Returns the Y direction of translation   
            
         
        """
        pass
    @TranslationY.setter
    def TranslationY(self, translationY: float):
        """
        Setter for property: (float) TranslationY
         Returns the Y direction of translation   
            
         
        """
        pass
    @property
    def TranslationZ(self) -> float:
        """
        Getter for property: (float) TranslationZ
         Returns the Z direction of translation   
            
         
        """
        pass
    @TranslationZ.setter
    def TranslationZ(self, translationZ: float):
        """
        Setter for property: (float) TranslationZ
         Returns the Z direction of translation   
            
         
        """
        pass
import NXOpen
class VisualMaterialCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection for NXOpen.Display.VisualMaterial. Supports only SVM and IrayPlus materials.
        If you want to import material file in mdl format, the API is in NXOpen.StudioMaterialManager. """
    def AssignMaterial(self, materialTag: VisualMaterial, objects: List[NXOpen.NXObject]) -> None:
        """
          Assign a created material to objects. 
        """
        pass
    def CreateMaterial(self, materialName: str) -> Tuple[VisualMaterial, str]:
        """
          Create a new material from system material canned. 
         Returns A tuple consisting of (material, newMaterialName). 
         - material is:  VisualMaterial NXOpen. the tag of  NXOpen.Display.VisualMaterial .
         - newMaterialName is: str. new material name .

        """
        pass
    def DeleteMaterial(self, materialTag: VisualMaterial) -> None:
        """
          Delete a material from the objects. 
        """
        pass
    def FindObject(self, name: str) -> VisualMaterial:
        """
         Finds the  VisualMaterialCollection  with the given name. 
         Returns found ( VisualMaterial NXOpen):   NXOpen.Display.VisualMaterial with this name. .
        """
        pass
    def GetMaterialByEntity(self, skipAppearanceMat: bool) -> Tuple[VisualMaterial, str]:
        """
         Get the visual material applied to the specific entity. 
         Returns A tuple consisting of (materialTag, materialName). 
         - materialTag is:  VisualMaterial NXOpen.
         - materialName is: str.

        """
        pass
    def GetMaterialByEntity2(self, entity: NXOpen.NXObject, skipAppearanceMat: bool) -> Tuple[VisualMaterial, str]:
        """
         Get the visual material applied to the specific entity. 
         Returns A tuple consisting of (materialTag, materialName). 
         - materialTag is:  VisualMaterial NXOpen.
         - materialName is: str.

        """
        pass
    def GetMaterialsInPart(self) -> Tuple[List[VisualMaterial], List[str]]:
        """
          Get list of current visual materials in the specific part. 
         Returns A tuple consisting of (materialTags, materialNames). 
         - materialTags is:  VisualMaterial List[NXOp.
         - materialNames is: List[str].

        """
        pass
    def GetMaterialsInPartByType(self, materialType: VisualMaterial.MaterialType) -> Tuple[List[VisualMaterial], List[str]]:
        """
          Get list of specific visual material type in the specific part. 
         Returns A tuple consisting of (materialTags, materialNames). 
         - materialTags is:  VisualMaterial List[NXOp.
         - materialNames is: List[str].

        """
        pass
    def RemoveMaterial(self, objects: List[NXOpen.NXObject]) -> None:
        """
          This removes all the materialtexture linked to the object.
                     It does not delete the materialstextures from the part. 
        """
        pass
import NXOpen
class VisualMaterialEditorBaseBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Display.VisualMaterialEditorBaseBuilder 
        This class is restricted to being called from a program running during an 
        Interactive NX session.  If run from a non-interactive session it will 
        return .
    """
    class MetallicBaseType(Enum):
        """
        Members Include: 
         |NonMetallic|   Base layer
         |Metallic|   Base layer

        """
        NonMetallic: int
        Metallic: int
        @staticmethod
        def ValueOf(value: int) -> VisualMaterialEditorBaseBuilder.MetallicBaseType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def LineardimBaseCornerRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LineardimBaseCornerRadius
         Returns the parameter that creates rounded corners without modeling the blends explicitly.  
           This setting is only visible in Ray Traced Studio.   
         
        """
        pass
    @property
    def MaterialName(self) -> str:
        """
        Getter for property: (str) MaterialName
         Returns the material name   
            
         
        """
        pass
    @MaterialName.setter
    def MaterialName(self, materialName: str):
        """
        Setter for property: (str) MaterialName
         Returns the material name   
            
         
        """
        pass
    @property
    def MetallicBase(self) -> VisualMaterialEditorBaseBuilder.MetallicBaseType:
        """
        Getter for property: ( VisualMaterialEditorBaseBuilder.MetallicBaseType NXOpen) MetallicBase
         Returns the basic type of material reflectance.  
           Only Non-metallic materials can be transparent and transmissive   
         
        """
        pass
    @MetallicBase.setter
    def MetallicBase(self, metallicBase: VisualMaterialEditorBaseBuilder.MetallicBaseType):
        """
        Setter for property: ( VisualMaterialEditorBaseBuilder.MetallicBaseType NXOpen) MetallicBase
         Returns the basic type of material reflectance.  
           Only Non-metallic materials can be transparent and transmissive   
         
        """
        pass
    def GetBaseColor(self) -> List[float]:
        """
         Returns the diffuse color of a Non-metallic material or the specular color of a Metallic material 
         Returns rGBColorPickerColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def GetBaseColorBlend(self) -> bool:
        """
         Returns whether the Color texture of the material is currently blended with the diffuse color 
         Returns blendToggle (bool): .
        """
        pass
    def GetBaseColorTexture(self) -> str:
        """
         Returns the filepath of the texture image used for the Color texture of the material 
         Returns filename (str): .
        """
        pass
    def GetBaseGeometryCutoutTexture(self) -> str:
        """
         Returns the filepath of the texture image used for the Cutout texture of the material 
         Returns filename (str): .
        """
        pass
    def GetBaseMicroSurfaceShadowTexture(self) -> str:
        """
         Returns the filepath of the texture image used for the Micro-surface Shadow texture of the material 
         Returns filename (str): .
        """
        pass
    def SetBaseColor(self, rGBColorPickerColor: List[float]) -> None:
        """
         The diffuse color of a Non-metallic material or the specular color of a Metallic material. Defines the overall color of the material with all the shadows and highlights taken out. 
        """
        pass
    def SetBaseColorBlend(self, blendToggle: bool) -> None:
        """
         The control to blend the diffuse color with the texture image 
        """
        pass
    def SetBaseColorTexture(self, filename: str) -> None:
        """
         Sets the texture image for the Color material parameter 
        """
        pass
    def SetBaseGeometryCutoutTexture(self, filename: str) -> None:
        """
         The parameter that creates holes in a thin-walled object using an opacity texture image without modelling the geometry explicitly. 
        """
        pass
    def SetBaseMicroSurfaceShadowTexture(self, filename: str) -> None:
        """
         The color parameter to simulate micro-occlusion in materials with natural grain (for example, leather) from a specified texture image. 
        """
        pass
import NXOpen
class VisualMaterialEditorBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Display.VisualMaterialEditorBuilder 
        This class is restricted to being called from a program running during an 
        Interactive NX session.  If run from a non-interactive session it will 
        return .
    """
    pass
import NXOpen
class VisualMaterialEditorCoatingBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Display.VisualMaterialEditorCoatingBuilder 
        This class is restricted to being called from a program running during an 
        Interactive NX session.  If run from a non-interactive session it will 
        return .
    """
    @property
    def ClearCoatLayer(self) -> bool:
        """
        Getter for property: (bool) ClearCoatLayer
         Returns the monochromatic layer on top of a material's surface simulating a clear lacquer finish.  
             
         
        """
        pass
    @ClearCoatLayer.setter
    def ClearCoatLayer(self, clearCoatLayer: bool):
        """
        Setter for property: (bool) ClearCoatLayer
         Returns the monochromatic layer on top of a material's surface simulating a clear lacquer finish.  
             
         
        """
        pass
    @property
    def ClearCoatRoughness(self) -> float:
        """
        Getter for property: (float) ClearCoatRoughness
         Returns the control of how shiny the Clear Coat is: 0 = perfect mirror, 1 = pure matte.  
             
         
        """
        pass
    @ClearCoatRoughness.setter
    def ClearCoatRoughness(self, clearCoatRoughness: float):
        """
        Setter for property: (float) ClearCoatRoughness
         Returns the control of how shiny the Clear Coat is: 0 = perfect mirror, 1 = pure matte.  
             
         
        """
        pass
    @property
    def ClearCoatWeight(self) -> float:
        """
        Getter for property: (float) ClearCoatWeight
         Returns the parameter that determines how strong the Clear Coat effect is: 0 = no effect, 1 = full effect   
            
         
        """
        pass
    @ClearCoatWeight.setter
    def ClearCoatWeight(self, clearCoatWeight: float):
        """
        Setter for property: (float) ClearCoatWeight
         Returns the parameter that determines how strong the Clear Coat effect is: 0 = no effect, 1 = full effect   
            
         
        """
        pass
    @property
    def MaterialName(self) -> str:
        """
        Getter for property: (str) MaterialName
         Returns the material name   
            
         
        """
        pass
    @MaterialName.setter
    def MaterialName(self, materialName: str):
        """
        Setter for property: (str) MaterialName
         Returns the material name   
            
         
        """
        pass
    def GetClearCoatBumpTexture(self) -> str:
        """
         Returns the filepath of the texture image used for the Clear Coat Bump texture of the material 
         Returns filename (str): .
        """
        pass
    def GetClearCoatRoughnessTexture(self) -> str:
        """
         Returns the filepath of the texture image used for the Clear Coat Roughness texture of the material 
         Returns filename (str): .
        """
        pass
    def GetClearCoatWeightTexture(self) -> str:
        """
         Returns the filepath of the texture image used for the Clear Coat Weight texture of the material 
         Returns filename (str): .
        """
        pass
    def SetClearCoatBumpTexture(self, filename: str) -> None:
        """
         Sets the texture image that defines the maximum height deviation for displacement mapping in current units. 
        """
        pass
    def SetClearCoatRoughnessTexture(self, filename: str) -> None:
        """
         Sets the texture image for the Clear Coat Roughness parameter 
        """
        pass
    def SetClearCoatWeightTexture(self, filename: str) -> None:
        """
         Sets the texture image for the Clear Coat Weight parameter 
        """
        pass
import NXOpen
class VisualMaterialEditorEmissionBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Display.VisualMaterialEditorEmissionBuilder 
        This class is restricted to being called from a program running during an 
        Interactive NX session.  If run from a non-interactive session it will 
        return .
    """
    class EmissionIntensityType(Enum):
        """
        Members Include: 
         |ConstantIntensity| 
         |ColorScalesIntensity| 

        """
        ConstantIntensity: int
        ColorScalesIntensity: int
        @staticmethod
        def ValueOf(value: int) -> VisualMaterialEditorEmissionBuilder.EmissionIntensityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EmissionProjectionDirectionType(Enum):
        """
        Members Include: 
         |AlignWithFloorPlane| 
         |UserDefined| 

        """
        AlignWithFloorPlane: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> VisualMaterialEditorEmissionBuilder.EmissionProjectionDirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EmissionUnitType(Enum):
        """
        Members Include: 
         |Lux| 
         |Lumen| 

        """
        Lux: int
        Lumen: int
        @staticmethod
        def ValueOf(value: int) -> VisualMaterialEditorEmissionBuilder.EmissionUnitType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EmissionIntensity(self) -> float:
        """
        Getter for property: (float) EmissionIntensity
         Returns the Emission intensity   
            
         
        """
        pass
    @EmissionIntensity.setter
    def EmissionIntensity(self, emissionIntensity: float):
        """
        Setter for property: (float) EmissionIntensity
         Returns the Emission intensity   
            
         
        """
        pass
    @property
    def EmissionIntensityMode(self) -> VisualMaterialEditorEmissionBuilder.EmissionIntensityType:
        """
        Getter for property: ( VisualMaterialEditorEmissionBuilder.EmissionIntensityType NXOpen) EmissionIntensityMode
         Returns the Emission intensity mode type for the Intensity parameter   
            
         
        """
        pass
    @EmissionIntensityMode.setter
    def EmissionIntensityMode(self, intensityMode: VisualMaterialEditorEmissionBuilder.EmissionIntensityType):
        """
        Setter for property: ( VisualMaterialEditorEmissionBuilder.EmissionIntensityType NXOpen) EmissionIntensityMode
         Returns the Emission intensity mode type for the Intensity parameter   
            
         
        """
        pass
    @property
    def EmissionProjectionDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) EmissionProjectionDirection
         Returns the Emission projection   
            
         
        """
        pass
    @EmissionProjectionDirection.setter
    def EmissionProjectionDirection(self, emissionProjectionDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) EmissionProjectionDirection
         Returns the Emission projection   
            
         
        """
        pass
    @property
    def EmissionRotationAngle(self) -> float:
        """
        Getter for property: (float) EmissionRotationAngle
         Returns the Emission rotation angle   
            
         
        """
        pass
    @EmissionRotationAngle.setter
    def EmissionRotationAngle(self, doubleEmissionRotationAngle: float):
        """
        Setter for property: (float) EmissionRotationAngle
         Returns the Emission rotation angle   
            
         
        """
        pass
    @property
    def EmissionUnits(self) -> VisualMaterialEditorEmissionBuilder.EmissionUnitType:
        """
        Getter for property: ( VisualMaterialEditorEmissionBuilder.EmissionUnitType NXOpen) EmissionUnits
         Returns the Photometric unit type for the Intensity parameter   
            
         
        """
        pass
    @EmissionUnits.setter
    def EmissionUnits(self, emissionUnits: VisualMaterialEditorEmissionBuilder.EmissionUnitType):
        """
        Setter for property: ( VisualMaterialEditorEmissionBuilder.EmissionUnitType NXOpen) EmissionUnits
         Returns the Photometric unit type for the Intensity parameter   
            
         
        """
        pass
    @property
    def EmitLight(self) -> bool:
        """
        Getter for property: (bool) EmitLight
         Returns the light emission parameter of a Siemens Visual Material.  
             
         
        """
        pass
    @EmitLight.setter
    def EmitLight(self, emitLight: bool):
        """
        Setter for property: (bool) EmitLight
         Returns the light emission parameter of a Siemens Visual Material.  
             
         
        """
        pass
    @property
    def MaterialName(self) -> str:
        """
        Getter for property: (str) MaterialName
         Returns the material name   
            
         
        """
        pass
    @MaterialName.setter
    def MaterialName(self, materialName: str):
        """
        Setter for property: (str) MaterialName
         Returns the material name   
            
         
        """
        pass
    @property
    def NativeFileBrowserEmissionPartFile(self) -> str:
        """
        Getter for property: (str) NativeFileBrowserEmissionPartFile
         Returns the Photometric Emission file   
            
         
        """
        pass
    @NativeFileBrowserEmissionPartFile.setter
    def NativeFileBrowserEmissionPartFile(self, filename: str):
        """
        Setter for property: (str) NativeFileBrowserEmissionPartFile
         Returns the Photometric Emission file   
            
         
        """
        pass
    @property
    def ProjectionDirectionType(self) -> VisualMaterialEditorEmissionBuilder.EmissionProjectionDirectionType:
        """
        Getter for property: ( VisualMaterialEditorEmissionBuilder.EmissionProjectionDirectionType NXOpen) ProjectionDirectionType
         Returns the Emission projection Type  
            
         
        """
        pass
    @ProjectionDirectionType.setter
    def ProjectionDirectionType(self, projectionDirectionType: VisualMaterialEditorEmissionBuilder.EmissionProjectionDirectionType):
        """
        Setter for property: ( VisualMaterialEditorEmissionBuilder.EmissionProjectionDirectionType NXOpen) ProjectionDirectionType
         Returns the Emission projection Type  
            
         
        """
        pass
    @property
    def UseEmissionProfile(self) -> bool:
        """
        Getter for property: (bool) UseEmissionProfile
         Returns the photometric emission profile representing a specific luminaire to the emissive material   
            
         
        """
        pass
    @UseEmissionProfile.setter
    def UseEmissionProfile(self, useEmissionProfile: bool):
        """
        Setter for property: (bool) UseEmissionProfile
         Returns the photometric emission profile representing a specific luminaire to the emissive material   
            
         
        """
        pass
    @property
    def UseIntensityFromFile(self) -> bool:
        """
        Getter for property: (bool) UseIntensityFromFile
         Returns the Use Intensity From File.  
          
                If UseIntensityFromFile=true, the total amount of light emitted by the material depends only on the intensity 
                i.e. the data values in the Light Profile determine the distribution of emission, but not the amount.
                If UseIntensityFromFile=false, both on the Intensity and the Light Profile i.e. the Intensity acts as a scale factor to multiply the data values in the Light Profile
                  
         
        """
        pass
    @UseIntensityFromFile.setter
    def UseIntensityFromFile(self, useIntensityFromFile: bool):
        """
        Setter for property: (bool) UseIntensityFromFile
         Returns the Use Intensity From File.  
          
                If UseIntensityFromFile=true, the total amount of light emitted by the material depends only on the intensity 
                i.e. the data values in the Light Profile determine the distribution of emission, but not the amount.
                If UseIntensityFromFile=false, both on the Intensity and the Light Profile i.e. the Intensity acts as a scale factor to multiply the data values in the Light Profile
                  
         
        """
        pass
    def GetEmissionColor(self) -> List[float]:
        """
         Returns the emission color 
         Returns rGBColorPickerColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def GetEmissionColorTexture(self) -> str:
        """
         Returns the filepath of the texture image used for the Emission Color texture of the material 
         Returns filename (str): .
        """
        pass
    def SetEmissionColor(self, rGBColorPickerColor: List[float]) -> None:
        """
         Sets the emission color 
        """
        pass
    def SetEmissionColorTexture(self, filename: str) -> None:
        """
         Sets the texture image for emission color of the material 
        """
        pass
import NXOpen
class VisualMaterialEditorFinishBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Display.VisualMaterialEditorFinishBuilder 
        This class is restricted to being called from a program running during an 
        Interactive NX session.  If run from a non-interactive session it will 
        return .
    """
    @property
    def FinishAnisotropic(self) -> float:
        """
        Getter for property: (float) FinishAnisotropic
         Returns the effect of reflections on brushed or machines surfaces where there are parallel scratches or grooves   
            
         
        """
        pass
    @FinishAnisotropic.setter
    def FinishAnisotropic(self, doubleFinishAnisotropic: float):
        """
        Setter for property: (float) FinishAnisotropic
         Returns the effect of reflections on brushed or machines surfaces where there are parallel scratches or grooves   
            
         
        """
        pass
    @property
    def FinishAnisotropicRotation(self) -> float:
        """
        Getter for property: (float) FinishAnisotropicRotation
         Returns the finish anisotropic rotation that controls the direction the reflection is stretched.  
             
         
        """
        pass
    @FinishAnisotropicRotation.setter
    def FinishAnisotropicRotation(self, finishAnisotropicRotation: float):
        """
        Setter for property: (float) FinishAnisotropicRotation
         Returns the finish anisotropic rotation that controls the direction the reflection is stretched.  
             
         
        """
        pass
    @property
    def FinishMetallicWeight(self) -> float:
        """
        Getter for property: (float) FinishMetallicWeight
         Returns the control to determine whether a material is to be treated as a Dielectric (0) or as a Conductor (1).  
           An intermediate value may be used as a mix of types.   
         
        """
        pass
    @FinishMetallicWeight.setter
    def FinishMetallicWeight(self, metallicWeight: float):
        """
        Setter for property: (float) FinishMetallicWeight
         Returns the control to determine whether a material is to be treated as a Dielectric (0) or as a Conductor (1).  
           An intermediate value may be used as a mix of types.   
         
        """
        pass
    @property
    def FinishRoughness(self) -> float:
        """
        Getter for property: (float) FinishRoughness
         Returns the shininess of the material.  
           A value of 0.0 defines a perfect mirror, a value of 1.0 defines a pure diffuser.   
         
        """
        pass
    @FinishRoughness.setter
    def FinishRoughness(self, doubleFinishRoughness: float):
        """
        Setter for property: (float) FinishRoughness
         Returns the shininess of the material.  
           A value of 0.0 defines a perfect mirror, a value of 1.0 defines a pure diffuser.   
         
        """
        pass
    @property
    def FinishSheenWeight(self) -> float:
        """
        Getter for property: (float) FinishSheenWeight
         Returns the shading of fabrics with a pronounced pile effect (for example, velvet).  
           A value of 0 disables sheen weight.   
         
        """
        pass
    @FinishSheenWeight.setter
    def FinishSheenWeight(self, doubleFinishSheenWeight: float):
        """
        Setter for property: (float) FinishSheenWeight
         Returns the shading of fabrics with a pronounced pile effect (for example, velvet).  
           A value of 0 disables sheen weight.   
         
        """
        pass
    @property
    def FinishSpecularWeight(self) -> float:
        """
        Getter for property: (float) FinishSpecularWeight
         Returns the amount of reflection for a Non-Metallic material.  
           A 0.5 value is physically accurate for most materials.   
         
        """
        pass
    @FinishSpecularWeight.setter
    def FinishSpecularWeight(self, doubleFinishSpecularWeight: float):
        """
        Setter for property: (float) FinishSpecularWeight
         Returns the amount of reflection for a Non-Metallic material.  
           A 0.5 value is physically accurate for most materials.   
         
        """
        pass
    @property
    def MaterialName(self) -> str:
        """
        Getter for property: (str) MaterialName
         Returns the material name   
            
         
        """
        pass
    @MaterialName.setter
    def MaterialName(self, materialName: str):
        """
        Setter for property: (str) MaterialName
         Returns the material name   
            
         
        """
        pass
    def GetFinishAnisotropicRotationTexture(self) -> str:
        """
         Returns the filepath of the texture image used for the Anisotropic Rotation texture of the material 
         Returns filename (str): .
        """
        pass
    def GetFinishAnisotropicTexture(self) -> str:
        """
         Returns the filepath of the texture image used for the Anisotropic texture of the material 
         Returns filename (str): .
        """
        pass
    def GetFinishBumpTexture(self) -> str:
        """
         Returns the filepath of the texture image used for the Bump texture of the material 
         Returns filename (str): .
        """
        pass
    def GetFinishMetallicWeightTexture(self) -> str:
        """
         Returns the filepath of the texture image used for the Metallic Weight texture of the material 
         Returns filename (str): .
        """
        pass
    def GetFinishRoughnessTexture(self) -> str:
        """
         Returns the filepath of the texture image used for the Roughness texture of the material 
         Returns filename (str): .
        """
        pass
    def GetFinishSheenTint(self) -> List[float]:
        """
         The color of sheen reflection to the defined RGB color. This parameter is not physically based and has no effect for a Conductor. 
         Returns rGBColorPickerColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def GetFinishSheenTintTexture(self) -> str:
        """
         Returns the filepath of the texture image used for the Sheen Tint texture of the material 
         Returns filename (str): .
        """
        pass
    def GetFinishSheenWeightTexture(self) -> str:
        """
         Returns the filepath of the texture image used for the Sheen Weight texture of the material 
         Returns filename (str): .
        """
        pass
    def GetFinishSpecularTint(self) -> List[float]:
        """
         Returns the RGB color picker color for the color of specular reflection (when viewed along the surface normal) 
         Returns rGBColorPickerColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def GetFinishSpecularTintTexture(self) -> str:
        """
         Returns the filepath of the texture image used for the Specular Tint texture of the material 
         Returns filename (str): .
        """
        pass
    def GetFinishSpecularWeightTexture(self) -> str:
        """
         Returns the filepath of the texture image used for the Specular Weight texture of the material 
         Returns filename (str): .
        """
        pass
    def SetFinishAnisotropicRotationTexture(self, filename: str) -> None:
        """
         Sets the texture image for the Anisotropic Rotation parameter 
        """
        pass
    def SetFinishAnisotropicTexture(self, filename: str) -> None:
        """
         Sets the texture image for the Anisotropic parameter 
        """
        pass
    def SetFinishBumpTexture(self, filename: str) -> None:
        """
         Sets the texture image for the material parameter that alters the shading normals based on a RGB texture to give a material the appearance of bumps 
        """
        pass
    def SetFinishMetallicWeightTexture(self, filename: str) -> None:
        """
         Sets the texture images of the Metallic Weight parameter 
        """
        pass
    def SetFinishRoughnessTexture(self, filename: str) -> None:
        """
         The texture image for the Roughness parameter. 
        """
        pass
    def SetFinishSheenTint(self, rGBColorPickerColor: List[float]) -> None:
        """
         Sets the color of sheen reflection to the defined RGB color. This parameter is not physically based and has no effect for a Conductor. 
        """
        pass
    def SetFinishSheenTintTexture(self, filename: str) -> None:
        """
         Sets the texture parameter for the Sheen Weight parameter 
        """
        pass
    def SetFinishSheenWeightTexture(self, filename: str) -> None:
        """
         Sets the texture parameter for the Sheen Weight parameter 
        """
        pass
    def SetFinishSpecularTint(self, rGBColorPickerColor: List[float]) -> None:
        """
         The color of specular reflection (when viewed along the surface normal) to the defined RGB Color. 
        """
        pass
    def SetFinishSpecularTintTexture(self, filename: str) -> None:
        """
         Sets the texture parameter for the Sheen Tint parameter 
        """
        pass
    def SetFinishSpecularWeightTexture(self, filename: str) -> None:
        """
         Sets the texture image for the Specular Weight parameter 
        """
        pass
import NXOpen
class VisualMaterialEditorSettingsBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Display.VisualMaterialEditorSettingsBuilder 
        This class is restricted to being called from a program running during an 
        Interactive NX session.  If run from a non-interactive session it will 
        return .
    """
    class EditorLevelType(Enum):
        """
        Members Include: 
         |Basic| 
         |Intermediate| 
         |Full| 

        """
        Basic: int
        Intermediate: int
        Full: int
        @staticmethod
        def ValueOf(value: int) -> VisualMaterialEditorSettingsBuilder.EditorLevelType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class GeometrySizeType(Enum):
        """
        Members Include: 
         |Small| 
         |Medium| 
         |Large| 
         |ExtraLarge| 

        """
        Small: int
        Medium: int
        Large: int
        ExtraLarge: int
        @staticmethod
        def ValueOf(value: int) -> VisualMaterialEditorSettingsBuilder.GeometrySizeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ModelGeometryType(Enum):
        """
        Members Include: 
         |NXShaderBall| 
         |Sphere| 
         |Cube| 
         |Cylinder| 
         |Plane| 
         |Fabric| 
         |Speedform| 

        """
        NXShaderBall: int
        Sphere: int
        Cube: int
        Cylinder: int
        Plane: int
        Fabric: int
        Speedform: int
        @staticmethod
        def ValueOf(value: int) -> VisualMaterialEditorSettingsBuilder.ModelGeometryType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EditorLevel(self) -> VisualMaterialEditorSettingsBuilder.EditorLevelType:
        """
        Getter for property: ( VisualMaterialEditorSettingsBuilder.EditorLevelType NXOpen) EditorLevel
         Returns the Visual Material Editor level   
            
         
        """
        pass
    @EditorLevel.setter
    def EditorLevel(self, editorLevel: VisualMaterialEditorSettingsBuilder.EditorLevelType):
        """
        Setter for property: ( VisualMaterialEditorSettingsBuilder.EditorLevelType NXOpen) EditorLevel
         Returns the Visual Material Editor level   
            
         
        """
        pass
    @property
    def GeometrySize(self) -> VisualMaterialEditorSettingsBuilder.GeometrySizeType:
        """
        Getter for property: ( VisualMaterialEditorSettingsBuilder.GeometrySizeType NXOpen) GeometrySize
         Returns the control to set the size of the geometry in the material thumbnail preview   
            
         
        """
        pass
    @GeometrySize.setter
    def GeometrySize(self, geometrySize: VisualMaterialEditorSettingsBuilder.GeometrySizeType):
        """
        Setter for property: ( VisualMaterialEditorSettingsBuilder.GeometrySizeType NXOpen) GeometrySize
         Returns the control to set the size of the geometry in the material thumbnail preview   
            
         
        """
        pass
    @property
    def MaterialName(self) -> str:
        """
        Getter for property: (str) MaterialName
         Returns the material name   
            
         
        """
        pass
    @MaterialName.setter
    def MaterialName(self, materialName: str):
        """
        Setter for property: (str) MaterialName
         Returns the material name   
            
         
        """
        pass
    @property
    def ModelGeometry(self) -> VisualMaterialEditorSettingsBuilder.ModelGeometryType:
        """
        Getter for property: ( VisualMaterialEditorSettingsBuilder.ModelGeometryType NXOpen) ModelGeometry
         Returns the control the set the type of geometry used in the material thumbnail preview   
            
         
        """
        pass
    @ModelGeometry.setter
    def ModelGeometry(self, modelGeometry: VisualMaterialEditorSettingsBuilder.ModelGeometryType):
        """
        Setter for property: ( VisualMaterialEditorSettingsBuilder.ModelGeometryType NXOpen) ModelGeometry
         Returns the control the set the type of geometry used in the material thumbnail preview   
            
         
        """
        pass
    @property
    def ThumbnailPreview(self) -> bool:
        """
        Getter for property: (bool) ThumbnailPreview
         Returns the control to display material thumbnail preview   
            
         
        """
        pass
    @ThumbnailPreview.setter
    def ThumbnailPreview(self, thumbnailPreview: bool):
        """
        Setter for property: (bool) ThumbnailPreview
         Returns the control to display material thumbnail preview   
            
         
        """
        pass
import NXOpen
class VisualMaterialEditorTexturesBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Display.VisualMaterialEditorTexturesBuilder 
        This class is restricted to being called from a program running during an 
        Interactive NX session.  If run from a non-interactive session it will 
        return .
    """
    class ParameterType(Enum):
        """
        Members Include: 
         |Albedo| 
         |Cutout| 
         |Bump| 
         |Roughness| 
         |Anisotropic| 
         |AnisotropicRotation| 
         |Transparency| 
         |EmissionColor| 
         |MicrosurfaceShadow| 
         |MetallicWeight| 
         |Translucency| 
         |ClearCoatRoughness| 
         |ClearCoatBump| 
         |ClearCoatWeight| 
         |Displacement| 
         |SheenWeight| 
         |SheenTint| 
         |Undefined| 

        """
        Albedo: int
        Cutout: int
        Bump: int
        Roughness: int
        Anisotropic: int
        AnisotropicRotation: int
        Transparency: int
        EmissionColor: int
        MicrosurfaceShadow: int
        MetallicWeight: int
        Translucency: int
        ClearCoatRoughness: int
        ClearCoatBump: int
        ClearCoatWeight: int
        Displacement: int
        SheenWeight: int
        SheenTint: int
        Undefined: int
        @staticmethod
        def ValueOf(value: int) -> VisualMaterialEditorTexturesBuilder.ParameterType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TexturesAnchorType(Enum):
        """
        Members Include: 
         |TopLeft| 
         |Center| 

        """
        TopLeft: int
        Center: int
        @staticmethod
        def ValueOf(value: int) -> VisualMaterialEditorTexturesBuilder.TexturesAnchorType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TexturesGammaType(Enum):
        """
        Members Include: 
         |Val22| 
         |Val18| 
         |Val10| 

        """
        Val22: int
        Val18: int
        Val10: int
        @staticmethod
        def ValueOf(value: int) -> VisualMaterialEditorTexturesBuilder.TexturesGammaType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TexturesWrapModeType(Enum):
        """
        Members Include: 
         |RepeatUV| 
         |SingleInstance| 
         |RepeatU| 
         |RepeatV| 

        """
        RepeatUV: int
        SingleInstance: int
        RepeatU: int
        RepeatV: int
        @staticmethod
        def ValueOf(value: int) -> VisualMaterialEditorTexturesBuilder.TexturesWrapModeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LocalTextureSpace:
        """
         Local texture space parameters. This data structure is used to define
                local texture space parameters for a specified visual material parameter.
         VisualMaterialEditorTexturesBuilderLocalTextureSpace_Struct NXOpen is an alias for  VisualMaterialEditorTexturesBuilder.LocalTextureSpace NXOpen.
        """
        @property
        def FlipU(self) -> bool:
            """
            Getter for property FlipU
            """
            pass
        @FlipU.setter
        def FlipU(self, value: bool):
            """
            Getter for property FlipUSetter for property FlipU
            """
            pass
        @property
        def FlipV(self) -> bool:
            """
            Getter for property FlipV
            """
            pass
        @FlipV.setter
        def FlipV(self, value: bool):
            """
            Getter for property FlipVSetter for property FlipV
            """
            pass
        @property
        def ScaleU(self) -> float:
            """
            Getter for property ScaleU
            """
            pass
        @ScaleU.setter
        def ScaleU(self, value: float):
            """
            Getter for property ScaleUSetter for property ScaleU
            """
            pass
        @property
        def ScaleV(self) -> float:
            """
            Getter for property ScaleV
            """
            pass
        @ScaleV.setter
        def ScaleV(self, value: float):
            """
            Getter for property ScaleVSetter for property ScaleV
            """
            pass
        @property
        def OffsetU(self) -> float:
            """
            Getter for property OffsetU
            """
            pass
        @OffsetU.setter
        def OffsetU(self, value: float):
            """
            Getter for property OffsetUSetter for property OffsetU
            """
            pass
        @property
        def OffsetV(self) -> float:
            """
            Getter for property OffsetV
            """
            pass
        @OffsetV.setter
        def OffsetV(self, value: float):
            """
            Getter for property OffsetVSetter for property OffsetV
            """
            pass
        @property
        def Rotation(self) -> float:
            """
            Getter for property Rotation
            """
            pass
        @Rotation.setter
        def Rotation(self, value: float):
            """
            Getter for property RotationSetter for property Rotation
            """
            pass
        @property
        def WrapType(self) -> VisualMaterialEditorTexturesBuilder.TexturesWrapModeType:
            """
            Getter for property WrapType
            """
            pass
        @WrapType.setter
        def WrapType(self, value: VisualMaterialEditorTexturesBuilder.TexturesWrapModeType):
            """
            Getter for property WrapTypeSetter for property WrapType
            """
            pass
        @property
        def AnchorType(self) -> VisualMaterialEditorTexturesBuilder.TexturesAnchorType:
            """
            Getter for property AnchorType
            """
            pass
        @AnchorType.setter
        def AnchorType(self, value: VisualMaterialEditorTexturesBuilder.TexturesAnchorType):
            """
            Getter for property AnchorTypeSetter for property AnchorType
            """
            pass
        @property
        def ResizeLocalTextureSpace(self) -> bool:
            """
            Getter for property ResizeLocalTextureSpace
            """
            pass
        @ResizeLocalTextureSpace.setter
        def ResizeLocalTextureSpace(self, value: bool):
            """
            Getter for property ResizeLocalTextureSpaceSetter for property ResizeLocalTextureSpace
            """
            pass
        @property
        def OffsetLocalTextureSpace(self) -> bool:
            """
            Getter for property OffsetLocalTextureSpace
            """
            pass
        @OffsetLocalTextureSpace.setter
        def OffsetLocalTextureSpace(self, value: bool):
            """
            Getter for property OffsetLocalTextureSpaceSetter for property OffsetLocalTextureSpace
            """
            pass
    class ColorFloatTextureParameters:
        """
          Texture parameters for color and float textures. This data structure is used to set or get texture parameters
                of a texture for a material parameter. 
         VisualMaterialEditorTexturesBuilderColorFloatTextureParameters_Struct NXOpen is an alias for  VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters NXOpen.
        """
        @property
        def Filename(self) -> str:
            """
            Getter for property Filename
            """
            pass
        @Filename.setter
        def Filename(self, value: str):
            """
            Getter for property FilenameSetter for property Filename
            """
            pass
        @property
        def LocalTextureSpace(self) -> VisualMaterialEditorTexturesBuilder.LocalTextureSpace:
            """
            Getter for property LocalTextureSpace
            """
            pass
        @LocalTextureSpace.setter
        def LocalTextureSpace(self, value: VisualMaterialEditorTexturesBuilder.LocalTextureSpace):
            """
            Getter for property LocalTextureSpaceSetter for property LocalTextureSpace
            """
            pass
        @property
        def GammaType(self) -> VisualMaterialEditorTexturesBuilder.TexturesGammaType:
            """
            Getter for property GammaType
            """
            pass
        @GammaType.setter
        def GammaType(self, value: VisualMaterialEditorTexturesBuilder.TexturesGammaType):
            """
            Getter for property GammaTypeSetter for property GammaType
            """
            pass
        @property
        def ColorScale(self) -> float:
            """
            Getter for property ColorScale
            """
            pass
        @ColorScale.setter
        def ColorScale(self, value: float):
            """
            Getter for property ColorScaleSetter for property ColorScale
            """
            pass
    class NormalTextureParameters:
        """
         Normal Texture parameters. This data structure is used to set or get texture parameters
                of a texture for a material parameter. Use for Clear Coat Bump and Bump textures 
         VisualMaterialEditorTexturesBuilderNormalTextureParameters_Struct NXOpen is an alias for  VisualMaterialEditorTexturesBuilder.NormalTextureParameters NXOpen.
        """
        @property
        def Filename(self) -> str:
            """
            Getter for property Filename
            """
            pass
        @Filename.setter
        def Filename(self, value: str):
            """
            Getter for property FilenameSetter for property Filename
            """
            pass
        @property
        def Amplitude(self) -> float:
            """
            Getter for property Amplitude
            """
            pass
        @Amplitude.setter
        def Amplitude(self, value: float):
            """
            Getter for property AmplitudeSetter for property Amplitude
            """
            pass
        @property
        def LocalTextureSpace(self) -> VisualMaterialEditorTexturesBuilder.LocalTextureSpace:
            """
            Getter for property LocalTextureSpace
            """
            pass
        @LocalTextureSpace.setter
        def LocalTextureSpace(self, value: VisualMaterialEditorTexturesBuilder.LocalTextureSpace):
            """
            Getter for property LocalTextureSpaceSetter for property LocalTextureSpace
            """
            pass
    @property
    def Amplitude(self) -> float:
        """
        Getter for property: (float) Amplitude
         Returns the Textures amplitude   
            
         
        """
        pass
    @Amplitude.setter
    def Amplitude(self, amplitude: float):
        """
        Setter for property: (float) Amplitude
         Returns the Textures amplitude   
            
         
        """
        pass
    @property
    def MaterialName(self) -> str:
        """
        Getter for property: (str) MaterialName
         Returns the material name  
            
         
        """
        pass
    @MaterialName.setter
    def MaterialName(self, materialName: str):
        """
        Setter for property: (str) MaterialName
         Returns the material name  
            
         
        """
        pass
    @property
    def NativeFileBrowserAdv(self) -> str:
        """
        Getter for property: (str) NativeFileBrowserAdv
         Returns the Advanced Native File Browser   
            
         
        """
        pass
    @NativeFileBrowserAdv.setter
    def NativeFileBrowserAdv(self, filename: str):
        """
        Setter for property: (str) NativeFileBrowserAdv
         Returns the Advanced Native File Browser   
            
         
        """
        pass
    @property
    def NativeFileBrowserAll(self) -> str:
        """
        Getter for property: (str) NativeFileBrowserAll
         Returns the Material Author Native File Browser   
            
         
        """
        pass
    @NativeFileBrowserAll.setter
    def NativeFileBrowserAll(self, filename: str):
        """
        Setter for property: (str) NativeFileBrowserAll
         Returns the Material Author Native File Browser   
            
         
        """
        pass
    @property
    def NativeFileBrowserEssentials(self) -> str:
        """
        Getter for property: (str) NativeFileBrowserEssentials
         Returns the Essentials native file browser   
            
         
        """
        pass
    @NativeFileBrowserEssentials.setter
    def NativeFileBrowserEssentials(self, filename: str):
        """
        Setter for property: (str) NativeFileBrowserEssentials
         Returns the Essentials native file browser   
            
         
        """
        pass
    @property
    def TexturesAnchor(self) -> VisualMaterialEditorTexturesBuilder.TexturesAnchorType:
        """
        Getter for property: ( VisualMaterialEditorTexturesBuilder.TexturesAnchorType NXOpen) TexturesAnchor
         Returns the textures placement anchor type   
            
         
        """
        pass
    @TexturesAnchor.setter
    def TexturesAnchor(self, texturesAnchor: VisualMaterialEditorTexturesBuilder.TexturesAnchorType):
        """
        Setter for property: ( VisualMaterialEditorTexturesBuilder.TexturesAnchorType NXOpen) TexturesAnchor
         Returns the textures placement anchor type   
            
         
        """
        pass
    @property
    def TexturesColorScale(self) -> float:
        """
        Getter for property: (float) TexturesColorScale
         Returns the Textures color scale   
            
         
        """
        pass
    @TexturesColorScale.setter
    def TexturesColorScale(self, doubleTexturesColorScale: float):
        """
        Setter for property: (float) TexturesColorScale
         Returns the Textures color scale   
            
         
        """
        pass
    @property
    def TexturesFlipU(self) -> bool:
        """
        Getter for property: (bool) TexturesFlipU
         Returns the Texture placement Flip U   
            
         
        """
        pass
    @TexturesFlipU.setter
    def TexturesFlipU(self, toggleTexturesFlipU: bool):
        """
        Setter for property: (bool) TexturesFlipU
         Returns the Texture placement Flip U   
            
         
        """
        pass
    @property
    def TexturesFlipV(self) -> bool:
        """
        Getter for property: (bool) TexturesFlipV
         Returns the Texture placement Flip V   
            
         
        """
        pass
    @TexturesFlipV.setter
    def TexturesFlipV(self, toggleTexturesFlipV: bool):
        """
        Setter for property: (bool) TexturesFlipV
         Returns the Texture placement Flip V   
            
         
        """
        pass
    @property
    def TexturesOffsetU(self) -> float:
        """
        Getter for property: (float) TexturesOffsetU
         Returns the textures placement offset U   
            
         
        """
        pass
    @TexturesOffsetU.setter
    def TexturesOffsetU(self, doubleTexturesOffsetU: float):
        """
        Setter for property: (float) TexturesOffsetU
         Returns the textures placement offset U   
            
         
        """
        pass
    @property
    def TexturesOffsetV(self) -> float:
        """
        Getter for property: (float) TexturesOffsetV
         Returns the textures placement offset V   
            
         
        """
        pass
    @TexturesOffsetV.setter
    def TexturesOffsetV(self, doubleTexturesOffsetV: float):
        """
        Setter for property: (float) TexturesOffsetV
         Returns the textures placement offset V   
            
         
        """
        pass
    @property
    def TexturesRotationAngle(self) -> float:
        """
        Getter for property: (float) TexturesRotationAngle
         Returns the texture rotation angle   
            
         
        """
        pass
    @TexturesRotationAngle.setter
    def TexturesRotationAngle(self, doubleTexturesRotationAngle: float):
        """
        Setter for property: (float) TexturesRotationAngle
         Returns the texture rotation angle   
            
         
        """
        pass
    @property
    def TexturesSelectTextureSize(self) -> bool:
        """
        Getter for property: (bool) TexturesSelectTextureSize
         Returns the texture parameter that specifies how material textures will be mapped onto geometry.  
             
         
        """
        pass
    @TexturesSelectTextureSize.setter
    def TexturesSelectTextureSize(self, toggleTexturesSelectTextureSize: bool):
        """
        Setter for property: (bool) TexturesSelectTextureSize
         Returns the texture parameter that specifies how material textures will be mapped onto geometry.  
             
         
        """
        pass
    @property
    def TexturesSelectedTexturePlacement(self) -> bool:
        """
        Getter for property: (bool) TexturesSelectedTexturePlacement
         Returns the Selected Texture Placement   
            
         
        """
        pass
    @TexturesSelectedTexturePlacement.setter
    def TexturesSelectedTexturePlacement(self, toggleTexturesSelectedTexturePlacement: bool):
        """
        Setter for property: (bool) TexturesSelectedTexturePlacement
         Returns the Selected Texture Placement   
            
         
        """
        pass
    @property
    def TexturesSizeScaleU(self) -> float:
        """
        Getter for property: (float) TexturesSizeScaleU
         Returns the texture size scale U factor   
            
         
        """
        pass
    @TexturesSizeScaleU.setter
    def TexturesSizeScaleU(self, doubleTexturesSizeScaleU: float):
        """
        Setter for property: (float) TexturesSizeScaleU
         Returns the texture size scale U factor   
            
         
        """
        pass
    @property
    def TexturesSizeScaleV(self) -> float:
        """
        Getter for property: (float) TexturesSizeScaleV
         Returns the texture size scale V factor   
            
         
        """
        pass
    @TexturesSizeScaleV.setter
    def TexturesSizeScaleV(self, doubleTexturesSizeScaleV: float):
        """
        Setter for property: (float) TexturesSizeScaleV
         Returns the texture size scale V factor   
            
         
        """
        pass
    @property
    def TexturesTextureGamma(self) -> VisualMaterialEditorTexturesBuilder.TexturesGammaType:
        """
        Getter for property: ( VisualMaterialEditorTexturesBuilder.TexturesGammaType NXOpen) TexturesTextureGamma
         Returns the Textures color gamma   
            
         
        """
        pass
    @TexturesTextureGamma.setter
    def TexturesTextureGamma(self, textureGamma: VisualMaterialEditorTexturesBuilder.TexturesGammaType):
        """
        Setter for property: ( VisualMaterialEditorTexturesBuilder.TexturesGammaType NXOpen) TexturesTextureGamma
         Returns the Textures color gamma   
            
         
        """
        pass
    @property
    def TexturesWrapMode(self) -> VisualMaterialEditorTexturesBuilder.TexturesWrapModeType:
        """
        Getter for property: ( VisualMaterialEditorTexturesBuilder.TexturesWrapModeType NXOpen) TexturesWrapMode
         Returns the Textures Wrap mode   
            
         
        """
        pass
    @TexturesWrapMode.setter
    def TexturesWrapMode(self, wrapMode: VisualMaterialEditorTexturesBuilder.TexturesWrapModeType):
        """
        Setter for property: ( VisualMaterialEditorTexturesBuilder.TexturesWrapModeType NXOpen) TexturesWrapMode
         Returns the Textures Wrap mode   
            
         
        """
        pass
    def DeleteTexture(self, parameter: VisualMaterialEditorTexturesBuilder.ParameterType) -> None:
        """
         Delete the texture for a specified SVM parameter. If the parameter specified is not a varying type,
                meaning there is no texture assigned, there will be no operation done. 
        """
        pass
    def GetAlbedoTexture(self) -> VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters:
        """
         Returns the Albedo texture parameters 
         Returns textureParameters ( VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters NXOpen): .
        """
        pass
    def GetAnisotropicRotationTexture(self) -> VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters:
        """
         Returns the Anisotropic Rotation texture parameters 
         Returns textureParameters ( VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters NXOpen): .
        """
        pass
    def GetAnisotropicTexture(self) -> VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters:
        """
         Returns the Anisotropic texture parameters 
         Returns textureParameters ( VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters NXOpen): .
        """
        pass
    def GetBumpTexture(self) -> VisualMaterialEditorTexturesBuilder.NormalTextureParameters:
        """
         Returns the Bump texture parameters 
         Returns textureParameters ( VisualMaterialEditorTexturesBuilder.NormalTextureParameters NXOpen): .
        """
        pass
    def GetClearCoatBumpTexture(self) -> VisualMaterialEditorTexturesBuilder.NormalTextureParameters:
        """
         Returns the Clear Coat Bump texture parameters 
         Returns textureParameters ( VisualMaterialEditorTexturesBuilder.NormalTextureParameters NXOpen): .
        """
        pass
    def GetClearCoatRoughnessTexture(self) -> VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters:
        """
         Returns the Clear Coat Roughness texture parameters 
         Returns textureParameters ( VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters NXOpen): .
        """
        pass
    def GetClearCoatWeightTexture(self) -> VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters:
        """
         Returns the Clear Coat Weight texture parameters 
         Returns textureParameters ( VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters NXOpen): .
        """
        pass
    def GetCutoutTexture(self) -> VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters:
        """
         Returns the Cutout texture parameters 
         Returns textureParameters ( VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters NXOpen): .
        """
        pass
    def GetDisplacementHeightTexture(self) -> VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters:
        """
         Returns the Displacement Height texture parameters 
         Returns textureParameters ( VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters NXOpen): .
        """
        pass
    def GetEmissionColorTexture(self) -> VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters:
        """
         Returns the Emission Color texture parameters 
         Returns textureParameters ( VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters NXOpen): .
        """
        pass
    def GetMetallicWeightTexture(self) -> VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters:
        """
         Returns the Metallic Weight texture parameters 
         Returns textureParameters ( VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters NXOpen): .
        """
        pass
    def GetMicroSurfaceShadowTexture(self) -> VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters:
        """
         Returns the Micro-surface Shadow texture parameters 
         Returns textureParameters ( VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters NXOpen): .
        """
        pass
    def GetRoughnessTexture(self) -> VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters:
        """
         Returns the Roughness texture parameters 
         Returns textureParameters ( VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters NXOpen): .
        """
        pass
    def GetSheenTintTexture(self) -> VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters:
        """
         Returns the Sheen Tint texture parameters 
         Returns textureParameters ( VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters NXOpen): .
        """
        pass
    def GetSheenWeightTexture(self) -> VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters:
        """
         Returns the Sheen Weight texture parameters 
         Returns textureParameters ( VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters NXOpen): .
        """
        pass
    def GetTransmissionTranslucencyTexture(self) -> VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters:
        """
         Returns the Transmission Translucency texture parameters 
         Returns textureParameters ( VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters NXOpen): .
        """
        pass
    def GetTransmissionTransparencyTexture(self) -> VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters:
        """
         Returns the Transmission Transparency texture parameters 
         Returns textureParameters ( VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters NXOpen): .
        """
        pass
    def SetAlbedoTexture(self, textureParameters: VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters) -> None:
        """
         The Albedo texture parameters 
        """
        pass
    def SetAnisotropicRotationTexture(self, textureParameters: VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters) -> None:
        """
         The Anisotropic Rotation texture parameters 
        """
        pass
    def SetAnisotropicTexture(self, textureParameters: VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters) -> None:
        """
         The Anisotropic texture parameters 
        """
        pass
    def SetBumpTexture(self, textureParameters: VisualMaterialEditorTexturesBuilder.NormalTextureParameters) -> None:
        """
         The Bump texture parameters 
        """
        pass
    def SetClearCoatBumpTexture(self, textureParameters: VisualMaterialEditorTexturesBuilder.NormalTextureParameters) -> None:
        """
         The Clear Coat Bump texture parameters 
        """
        pass
    def SetClearCoatRoughnessTexture(self, textureParameters: VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters) -> None:
        """
         The Clear Coat Roughness texture parameters 
        """
        pass
    def SetClearCoatWeightTexture(self, textureParameters: VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters) -> None:
        """
         The Clear Coat Weight texture parameters 
        """
        pass
    def SetCutoutTexture(self, textureParameters: VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters) -> None:
        """
         The Cutout texture parameters 
        """
        pass
    def SetDisplacementHeightTexture(self, textureParameters: VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters) -> None:
        """
         The Displacement Height texture parameters 
        """
        pass
    def SetEmissionColorTexture(self, textureParameters: VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters) -> None:
        """
         The Emission Color texture parameters 
        """
        pass
    def SetMetallicWeightTexture(self, textureParameters: VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters) -> None:
        """
         The Metallic Weight texture parameters 
        """
        pass
    def SetMicroSurfaceShadowTexture(self, textureParameters: VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters) -> None:
        """
         The Micro-surface Shadow texture parameters 
        """
        pass
    def SetRoughnessTexture(self, textureParameters: VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters) -> None:
        """
         The Roughness texture parameters 
        """
        pass
    def SetSheenTintTexture(self, textureParameters: VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters) -> None:
        """
         The Sheen Tint texture parameters 
        """
        pass
    def SetSheenWeightTexture(self, textureParameters: VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters) -> None:
        """
         The Sheen Weight texture parameters 
        """
        pass
    def SetTexturesAdvancedDelete(self) -> None:
        """
         The Advanced command to delete the texture image of a specified material parameter 
        """
        pass
    def SetTexturesAdvancedSync(self) -> None:
        """
         The Advanced command to reload the texture image of a specified material parameter 
        """
        pass
    def SetTexturesAdvancedVisibility(self) -> None:
        """
         The Advanced command to hide the texture image of a specified material parameter 
        """
        pass
    def SetTexturesAllDelete(self) -> None:
        """
         The Material Author command to delete the texture image of a specified material parameter 
        """
        pass
    def SetTexturesAllSync(self) -> None:
        """
         The Material Author command to reload the texture image of a specified material parameter 
        """
        pass
    def SetTexturesAllVisibility(self) -> None:
        """
         The Material Author command to hide the texture image of a specified material parameter 
        """
        pass
    def SetTexturesEssentialsDelete(self) -> None:
        """
         The Essentials command to delete the texture image of a specified material parameter 
        """
        pass
    def SetTexturesEssentialsSync(self) -> None:
        """
         The Essentials command to reload the texture image of a specified material parameter 
        """
        pass
    def SetTexturesEssentialsVisibility(self) -> None:
        """
         The Essentials command to hide the texture image of a specified material parameter 
        """
        pass
    def SetTransmissionTranslucencyTexture(self, textureParameters: VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters) -> None:
        """
         The Transmission Translucency texture parameters 
        """
        pass
    def SetTransmissionTransparencyTexture(self, textureParameters: VisualMaterialEditorTexturesBuilder.ColorFloatTextureParameters) -> None:
        """
         The Transmission Transparency texture parameters 
        """
        pass
import NXOpen
class VisualMaterialEditorTextureSpaceBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Display.VisualMaterialEditorTextureSpaceBuilder 
        This class is restricted to being called from a program running during an 
        Interactive NX session.  If run from a non-interactive session it will 
        return .
    """
    class CoordinateSystemType(Enum):
        """
        Members Include: 
         |RelativetoPart| 
         |RelativetoWorld| 

        """
        RelativetoPart: int
        RelativetoWorld: int
        @staticmethod
        def ValueOf(value: int) -> VisualMaterialEditorTextureSpaceBuilder.CoordinateSystemType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TextureSpaceAnchorType(Enum):
        """
        Members Include: 
         |BottomLeft| 
         |TopLeft| 
         |Center| 

        """
        BottomLeft: int
        TopLeft: int
        Center: int
        @staticmethod
        def ValueOf(value: int) -> VisualMaterialEditorTextureSpaceBuilder.TextureSpaceAnchorType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TextureSpaceType(Enum):
        """
        Members Include: 
         |Box| 
         |Planar| 
         |Uv| 
         |Spherical| 
         |Cylindrical| 

        """
        Box: int
        Planar: int
        Uv: int
        Spherical: int
        Cylindrical: int
        @staticmethod
        def ValueOf(value: int) -> VisualMaterialEditorTextureSpaceBuilder.TextureSpaceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def LineardimTextureSpaceScaleU(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LineardimTextureSpaceScaleU
         Returns the Texture Space Linear U dimension to specify the texture size in current work part units.  
             
         
        """
        pass
    @property
    def LineardimTextureSpaceScaleV(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LineardimTextureSpaceScaleV
         Returns the Texture Space Linear V dimension to specify the texture size in current work part units.  
             
         
        """
        pass
    @property
    def LineardimTextureSpaceScaleW(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LineardimTextureSpaceScaleW
         Returns the Texture Space Linear W dimension to specify the texture size in current work part units.  
             
         
        """
        pass
    @property
    def MaterialName(self) -> str:
        """
        Getter for property: (str) MaterialName
         Returns the material name   
            
         
        """
        pass
    @MaterialName.setter
    def MaterialName(self, materialName: str):
        """
        Setter for property: (str) MaterialName
         Returns the material name   
            
         
        """
        pass
    @property
    def PointTextureSpaceOrigin(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) PointTextureSpaceOrigin
         Returns the texture space origin point   
            
         
        """
        pass
    @PointTextureSpaceOrigin.setter
    def PointTextureSpaceOrigin(self, pointTextureSpaceOrigin: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) PointTextureSpaceOrigin
         Returns the texture space origin point   
            
         
        """
        pass
    @property
    def TextureSpace(self) -> VisualMaterialEditorTextureSpaceBuilder.TextureSpaceType:
        """
        Getter for property: ( VisualMaterialEditorTextureSpaceBuilder.TextureSpaceType NXOpen) TextureSpace
         Returns the Texture Space type for the material   
            
         
        """
        pass
    @TextureSpace.setter
    def TextureSpace(self, enumTextureSpaceType: VisualMaterialEditorTextureSpaceBuilder.TextureSpaceType):
        """
        Setter for property: ( VisualMaterialEditorTextureSpaceBuilder.TextureSpaceType NXOpen) TextureSpace
         Returns the Texture Space type for the material   
            
         
        """
        pass
    @property
    def TextureSpaceAnchor(self) -> VisualMaterialEditorTextureSpaceBuilder.TextureSpaceAnchorType:
        """
        Getter for property: ( VisualMaterialEditorTextureSpaceBuilder.TextureSpaceAnchorType NXOpen) TextureSpaceAnchor
         Returns the texture space anchor type   
            
         
        """
        pass
    @TextureSpaceAnchor.setter
    def TextureSpaceAnchor(self, enumTextureSpaceAnchor: VisualMaterialEditorTextureSpaceBuilder.TextureSpaceAnchorType):
        """
        Setter for property: ( VisualMaterialEditorTextureSpaceBuilder.TextureSpaceAnchorType NXOpen) TextureSpaceAnchor
         Returns the texture space anchor type   
            
         
        """
        pass
    @property
    def TextureSpaceCoordinateSpace(self) -> VisualMaterialEditorTextureSpaceBuilder.CoordinateSystemType:
        """
        Getter for property: ( VisualMaterialEditorTextureSpaceBuilder.CoordinateSystemType NXOpen) TextureSpaceCoordinateSpace
         Returns the Texture coordinate space   
            
         
        """
        pass
    @TextureSpaceCoordinateSpace.setter
    def TextureSpaceCoordinateSpace(self, enumTextureSpaceCoordinateSpace: VisualMaterialEditorTextureSpaceBuilder.CoordinateSystemType):
        """
        Setter for property: ( VisualMaterialEditorTextureSpaceBuilder.CoordinateSystemType NXOpen) TextureSpaceCoordinateSpace
         Returns the Texture coordinate space   
            
         
        """
        pass
    @property
    def TextureSpaceFlipU(self) -> bool:
        """
        Getter for property: (bool) TextureSpaceFlipU
         Returns the flip U value to reverse the texture in the horizontal direction   
            
         
        """
        pass
    @TextureSpaceFlipU.setter
    def TextureSpaceFlipU(self, toggleTextureSpaceFlipU: bool):
        """
        Setter for property: (bool) TextureSpaceFlipU
         Returns the flip U value to reverse the texture in the horizontal direction   
            
         
        """
        pass
    @property
    def TextureSpaceFlipV(self) -> bool:
        """
        Getter for property: (bool) TextureSpaceFlipV
         Returns the flip V value to reverse the texture in the vertical direction   
            
         
        """
        pass
    @TextureSpaceFlipV.setter
    def TextureSpaceFlipV(self, toggleTextureSpaceFlipV: bool):
        """
        Setter for property: (bool) TextureSpaceFlipV
         Returns the flip V value to reverse the texture in the vertical direction   
            
         
        """
        pass
    @property
    def TextureSpaceOffsetU(self) -> float:
        """
        Getter for property: (float) TextureSpaceOffsetU
         Returns the offset U value   
            
         
        """
        pass
    @TextureSpaceOffsetU.setter
    def TextureSpaceOffsetU(self, doubleTextureSpaceOffsetU: float):
        """
        Setter for property: (float) TextureSpaceOffsetU
         Returns the offset U value   
            
         
        """
        pass
    @property
    def TextureSpaceOffsetV(self) -> float:
        """
        Getter for property: (float) TextureSpaceOffsetV
         Returns the offset V value   
            
         
        """
        pass
    @TextureSpaceOffsetV.setter
    def TextureSpaceOffsetV(self, doubleTextureSpaceOffsetV: float):
        """
        Setter for property: (float) TextureSpaceOffsetV
         Returns the offset V value   
            
         
        """
        pass
    @property
    def TextureSpaceRotationAngle(self) -> float:
        """
        Getter for property: (float) TextureSpaceRotationAngle
         Returns the texture rotation angle in degrees around the Anchor Point   
            
         
        """
        pass
    @TextureSpaceRotationAngle.setter
    def TextureSpaceRotationAngle(self, doubleTextureSpaceRotationAngle: float):
        """
        Setter for property: (float) TextureSpaceRotationAngle
         Returns the texture rotation angle in degrees around the Anchor Point   
            
         
        """
        pass
    @property
    def TextureSpaceUniformScale(self) -> bool:
        """
        Getter for property: (bool) TextureSpaceUniformScale
         Returns the toggle to set all dimensions for textures to be equal or define them individually   
            
         
        """
        pass
    @TextureSpaceUniformScale.setter
    def TextureSpaceUniformScale(self, toggleTextureSpaceUniformScale: bool):
        """
        Setter for property: (bool) TextureSpaceUniformScale
         Returns the toggle to set all dimensions for textures to be equal or define them individually   
            
         
        """
        pass
    @property
    def VectorTextureSpaceNormal(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) VectorTextureSpaceNormal
         Returns the Texture Space normal vector   
            
         
        """
        pass
    @VectorTextureSpaceNormal.setter
    def VectorTextureSpaceNormal(self, vectorTextureSpaceNormal: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) VectorTextureSpaceNormal
         Returns the Texture Space normal vector   
            
         
        """
        pass
    @property
    def VectorTextureSpaceUp(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) VectorTextureSpaceUp
         Returns the texture space up vector   
            
         
        """
        pass
    @VectorTextureSpaceUp.setter
    def VectorTextureSpaceUp(self, vectorTextureSpaceUp: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) VectorTextureSpaceUp
         Returns the texture space up vector   
            
         
        """
        pass
import NXOpen
class VisualMaterialEditorTransmissionBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Display.VisualMaterialEditorTransmissionBuilder 
        This class is restricted to being called from a program running during an 
        Interactive NX session.  If run from a non-interactive session it will 
        return .
    """
    @property
    def LineardimTransmissionAttenuationDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LineardimTransmissionAttenuationDistance
         Returns the distance over which light will be absorbed as it passes through the material.  
             
         
        """
        pass
    @property
    def LineardimTransmissionScatterDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LineardimTransmissionScatterDistance
         Returns the maximum height deviation defined for displacement mapping in current units.  
             
         
        """
        pass
    @property
    def MaterialName(self) -> str:
        """
        Getter for property: (str) MaterialName
         Returns the material name   
            
         
        """
        pass
    @MaterialName.setter
    def MaterialName(self, materialName: str):
        """
        Setter for property: (str) MaterialName
         Returns the material name   
            
         
        """
        pass
    @property
    def TransmissionAbbeNumber(self) -> float:
        """
        Getter for property: (float) TransmissionAbbeNumber
         Returns the Abbe Number for Solid Volume materials.  
              
         
        """
        pass
    @TransmissionAbbeNumber.setter
    def TransmissionAbbeNumber(self, doubleTransmissionAbbeNumber: float):
        """
        Setter for property: (float) TransmissionAbbeNumber
         Returns the Abbe Number for Solid Volume materials.  
              
         
        """
        pass
    @property
    def TransmissionIOR(self) -> float:
        """
        Getter for property: (float) TransmissionIOR
         Returns the Index of Refraction for Solid Volume materials.  
             
         
        """
        pass
    @TransmissionIOR.setter
    def TransmissionIOR(self, doubleTransmissionIOR: float):
        """
        Setter for property: (float) TransmissionIOR
         Returns the Index of Refraction for Solid Volume materials.  
             
         
        """
        pass
    @property
    def TransmissionSolidVolume(self) -> bool:
        """
        Getter for property: (bool) TransmissionSolidVolume
         Returns the Solid Volume toggle.  
           When On, the material is capable of refracting transmissive rays. When off, the material is treated as non-refractive surface   
         
        """
        pass
    @TransmissionSolidVolume.setter
    def TransmissionSolidVolume(self, toggleTransmissionSolidVolume: bool):
        """
        Setter for property: (bool) TransmissionSolidVolume
         Returns the Solid Volume toggle.  
           When On, the material is capable of refracting transmissive rays. When off, the material is treated as non-refractive surface   
         
        """
        pass
    @property
    def TransmissionSubSurfaceScatter(self) -> bool:
        """
        Getter for property: (bool) TransmissionSubSurfaceScatter
         Returns the toggle to randomly scatter the rays to make the material appear cloudy.  
           This setting is only visible in Ray Traced Studio.   
         
        """
        pass
    @TransmissionSubSurfaceScatter.setter
    def TransmissionSubSurfaceScatter(self, toggleTransmissionSubSurfaceScatter: bool):
        """
        Setter for property: (bool) TransmissionSubSurfaceScatter
         Returns the toggle to randomly scatter the rays to make the material appear cloudy.  
           This setting is only visible in Ray Traced Studio.   
         
        """
        pass
    @property
    def TransmissionTranslucency(self) -> float:
        """
        Getter for property: (float) TransmissionTranslucency
         Returns the value of roughness used for transmission which affects the clarity of the material, useful for defining milky plastics or sandblasted glass   
            
         
        """
        pass
    @TransmissionTranslucency.setter
    def TransmissionTranslucency(self, doubleTransmissionTranslucency: float):
        """
        Setter for property: (float) TransmissionTranslucency
         Returns the value of roughness used for transmission which affects the clarity of the material, useful for defining milky plastics or sandblasted glass   
            
         
        """
        pass
    @property
    def TransmissionTransparency(self) -> float:
        """
        Getter for property: (float) TransmissionTransparency
         Returns the value of light that is transmitted through the material: 0 = disabled (opaque) , 1 = fully transparent   
            
         
        """
        pass
    @TransmissionTransparency.setter
    def TransmissionTransparency(self, doubleTransmissionTransparency: float):
        """
        Setter for property: (float) TransmissionTransparency
         Returns the value of light that is transmitted through the material: 0 = disabled (opaque) , 1 = fully transparent   
            
         
        """
        pass
    def GetTransmissionAttenuationColor(self) -> List[float]:
        """
         Returns the RGB color for the Attenuation Color parameter 
         Returns rGBColorPickerColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def GetTransmissionTranslucencyTexture(self) -> str:
        """
         Returns the filepath of the texture image used for the Translucency texture of the material 
         Returns filename (str): .
        """
        pass
    def GetTransmissionTransparencyTexture(self) -> str:
        """
         Returns the filepath of the texture image used for the Transparency texture of the material 
         Returns filename (str): .
        """
        pass
    def SetTransmissionAttenuationColor(self, rGBColorPickerColor: List[float]) -> None:
        """
         Sets the RGB color for the Attenuation Color parameter 
        """
        pass
    def SetTransmissionTranslucencyTexture(self, filename: str) -> None:
        """
         Sets the texture image for the Translucency parameter 
        """
        pass
    def SetTransmissionTransparencyTexture(self, filename: str) -> None:
        """
         Sets the texture images for the Transparency parameter 
        """
        pass
import NXOpen
class VisualMaterialEditorUtilitiesBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Display.VisualMaterialEditorUtilitiesBuilder 
        This class is restricted to being called from a program running during an 
        Interactive NX session.  If run from a non-interactive session it will 
        return .
    """
    @property
    def MaterialName(self) -> str:
        """
        Getter for property: (str) MaterialName
         Returns the material name   
            
         
        """
        pass
    @MaterialName.setter
    def MaterialName(self, materialName: str):
        """
        Setter for property: (str) MaterialName
         Returns the material name   
            
         
        """
        pass
    def ExportToSVMFile(self, filename: str) -> None:
        """
         The command to export the current material 
        """
        pass
    def SaveToSystemStudioMaterials(self, filename: str) -> None:
        """
         Sets the current edited material to the Studio Materials Palette 
        """
        pass
import NXOpen
class VisualMaterial(NXOpen.NXObject): 
    """ Represents a visual material."""
    class MaterialType(Enum):
        """
        Members Include: 
         |Svm|  SVM material type 
         |IrayPlus|  IrayPlus material type

        """
        Svm: int
        IrayPlus: int
        @staticmethod
        def ValueOf(value: int) -> VisualMaterial.MaterialType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the visual material name.  
             
         
        """
        pass
    @property
    def Type(self) -> VisualMaterial.MaterialType:
        """
        Getter for property: ( VisualMaterial.MaterialType NXOpen) Type
         Returns the visual material type.  
             
         
        """
        pass
import NXOpen
class Wall(NXOpen.Builder): 
    """
    Represents a NXOpen.Display.Wall
    This class is restricted to being called from a program running during an 
    Interactive NX session.  If run from a non-interactive session it will 
    return .
    """
    class MaterialTextureType(Enum):
        """
        Members Include: 
         |ShadowCatcher|  The wall is transparent, and is used to display
                                                                      shadows.  Use this to cast shadows onto a "virtual"
                                                                      background image of an environment. 
         |ImageFile|  The wall uses image for tiling. For example, use this on
                                                                      a "bottom" wall to display a tiled shiny floor. 
         |Invisible|  The wall is not displayed.  For example, use this
                                                                      on all the walls except the "bottom" if you only
                                                                      need to display a floor. 

        """
        ShadowCatcher: int
        ImageFile: int
        Invisible: int
        @staticmethod
        def ValueOf(value: int) -> Wall.MaterialTextureType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MaterialType(Enum):
        """
        Members Include: 
         |ShadowCatcher|  The wall is transparent, and is used to display
                                                                      shadows.  Use this to cast shadows onto a "virtual"
                                                                      background image of an environment. 
         |Reflective|  The wall is reflective.  For example, use this on
                                                                      a "bottom" wall to display a shiny floor. 
         |Invisible|  The wall is not displayed.  For example, use this
                                                                      on all the walls except the "bottom" if you only
                                                                      need to display a floor. 

        """
        ShadowCatcher: int
        Reflective: int
        Invisible: int
        @staticmethod
        def ValueOf(value: int) -> Wall.MaterialType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Image(self) -> Image:
        """
        Getter for property: ( Image NXOpen) Image
         Returns the walls's image builder   
            
         
        """
        pass
    @Image.setter
    def Image(self, image_builder: Image):
        """
        Setter for property: ( Image NXOpen) Image
         Returns the walls's image builder   
            
         
        """
        pass
    @property
    def ImageFilename(self) -> str:
        """
        Getter for property: (str) ImageFilename
         Returns the stage wall's image filename   
            
         
        """
        pass
    @ImageFilename.setter
    def ImageFilename(self, image_file_name: str):
        """
        Setter for property: (str) ImageFilename
         Returns the stage wall's image filename   
            
         
        """
        pass
    @property
    def PatternRepeatFactor(self) -> float:
        """
        Getter for property: (float) PatternRepeatFactor
         Returns the pattern repeat factor - the number of times the image repeats   
            
         
        """
        pass
    @PatternRepeatFactor.setter
    def PatternRepeatFactor(self, patternRepeatFactor: float):
        """
        Setter for property: (float) PatternRepeatFactor
         Returns the pattern repeat factor - the number of times the image repeats   
            
         
        """
        pass
    @property
    def Reflectivity(self) -> float:
        """
        Getter for property: (float) Reflectivity
         Returns the reflectivity of a wall - the percentage of the environment reflected off of the wall   
            
         
        """
        pass
    @Reflectivity.setter
    def Reflectivity(self, reflectivity: float):
        """
        Setter for property: (float) Reflectivity
         Returns the reflectivity of a wall - the percentage of the environment reflected off of the wall   
            
         
        """
        pass
    @property
    def WallMaterialTextureType(self) -> Wall.MaterialTextureType:
        """
        Getter for property: ( Wall.MaterialTextureType NXOpen) WallMaterialTextureType
         Returns the wall material texture type - either shadow_catcher, image file, or invisible   
            
         
        """
        pass
    @WallMaterialTextureType.setter
    def WallMaterialTextureType(self, wallMaterialType: Wall.MaterialTextureType):
        """
        Setter for property: ( Wall.MaterialTextureType NXOpen) WallMaterialTextureType
         Returns the wall material texture type - either shadow_catcher, image file, or invisible   
            
         
        """
        pass
    @property
    def WallMaterialType(self) -> Wall.MaterialType:
        """
        Getter for property: ( Wall.MaterialType NXOpen) WallMaterialType
         Returns the wall material type - either shadow_catcher, reflective, or invisible   
            
         
        """
        pass
    @WallMaterialType.setter
    def WallMaterialType(self, wallMaterialType: Wall.MaterialType):
        """
        Setter for property: ( Wall.MaterialType NXOpen) WallMaterialType
         Returns the wall material type - either shadow_catcher, reflective, or invisible   
            
         
        """
        pass
