from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class CurveFromStrokeData(NXOpen.Builder): 
    """ Represents  NXOpen.Features.DrawShapes.CurveFromStrokeData 
        allowing user to define curve using drag gesture.
    """
    class DetectionSensitivityOption(Enum):
        """
        Members Include: 
         |Low|  For creating primitives, the strokes can have large deviations from an ideal circle, line, etc.; For creating splines, the output spline will be rather smooth with larger deviations to the stroke. 
         |Standard|  For creating primitives, the strokes can have medium deviations from an ideal circle, line, etc.; For creating splines, the output spline will be a tradeoff between smoothness and accuracy to the stroke. 
         |High|  For creating primitives, the strokes can have only small deviations from an ideal circle, line, etc.; For creating splines, the output spline will be rather bumpy with small deviations to the stroke.

        """
        Low: int
        Standard: int
        High: int
        @staticmethod
        def ValueOf(value: int) -> CurveFromStrokeData.DetectionSensitivityOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CanCreatePrimitives(self) -> bool:
        """
        Getter for property: (bool) CanCreatePrimitives
         Returns the value indicating if primitive curve should be created   
            
         
        """
        pass
    @CanCreatePrimitives.setter
    def CanCreatePrimitives(self, canCreatePrimitive: bool):
        """
        Setter for property: (bool) CanCreatePrimitives
         Returns the value indicating if primitive curve should be created   
            
         
        """
        pass
    @property
    def CanMergeConnectedStrokes(self) -> bool:
        """
        Getter for property: (bool) CanMergeConnectedStrokes
         Returns the flag indicating if selected strokes should be merged.  
             
         
        """
        pass
    @CanMergeConnectedStrokes.setter
    def CanMergeConnectedStrokes(self, canMergeConnectedStrokes: bool):
        """
        Setter for property: (bool) CanMergeConnectedStrokes
         Returns the flag indicating if selected strokes should be merged.  
             
         
        """
        pass
    @property
    def DetectionSensitivity(self) -> CurveFromStrokeData.DetectionSensitivityOption:
        """
        Getter for property: ( CurveFromStrokeData.DetectionSensitivityOption NXOpen.Featu) DetectionSensitivity
         Returns the value indicating detection sensitivity.  
           The smaller the sensitivity,
                    the more accurate the stroke must be to be recognized as primitive.   
         
        """
        pass
    @DetectionSensitivity.setter
    def DetectionSensitivity(self, detectionSensitivity: CurveFromStrokeData.DetectionSensitivityOption):
        """
        Setter for property: ( CurveFromStrokeData.DetectionSensitivityOption NXOpen.Featu) DetectionSensitivity
         Returns the value indicating detection sensitivity.  
           The smaller the sensitivity,
                    the more accurate the stroke must be to be recognized as primitive.   
         
        """
        pass
    @property
    def Strokes(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) Strokes
         Returns the object enabling drawing of the curve   
            
         
        """
        pass
    def SetMergeTolerance(self, mergeTolerance: float) -> None:
        """
         Distance tolerance used to decide if two strokes should be merged. 
        """
        pass
import NXOpen
class DeleteData(NXOpen.Builder): 
    """ Represents  NXOpen.Features.DrawShapes.DeleteData 
        allowing user to delete strokes and curves.
    """
    @property
    def Objects(self) -> NXOpen.SelectCurveList:
        """
        Getter for property: ( NXOpen.SelectCurveList) Objects
         Returns the objects   
            
         
        """
        pass
import NXOpen
class DivideBuilder(NXOpen.Builder): 
    """ Represents  NXOpen.Features.DrawShapes.DivideBuilder 
            allowing user to divide curves.
        """
    @property
    def Targets(self) -> NXOpen.SelectCurveList:
        """
        Getter for property: ( NXOpen.SelectCurveList) Targets
         Returns the curves to be divided   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class DrawCurveData(NXOpen.Builder): 
    """ Represents  NXOpen.Features.DrawShapes.DrawCurveData 
        allowing user to define curve using drag gesture.
    """
    class DetectionSensitivityOption(Enum):
        """
        Members Include: 
         |Low|  For creating primitives, the strokes can have large deviations from an ideal circle, line, etc.; For creating splines, the output spline will be rather smooth with larger deviations to the stroke. 
         |Standard|  For creating primitives, the strokes can have medium deviations from an ideal circle, line, etc.; For creating splines, the output spline will be a tradeoff between smoothness and accuracy to the stroke.
         |High|  For creating primitives, the strokes can have only small deviations from an ideal circle, line, etc.; For creating splines, the output spline will be rather bumpy with small deviations to the stroke.

        """
        Low: int
        Standard: int
        High: int
        @staticmethod
        def ValueOf(value: int) -> DrawCurveData.DetectionSensitivityOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SnapToOptions(Enum):
        """
        Members Include: 
         |NotSet|  No snapping. 
         |Curve|  Snap to point on curve, including curve end points .
         |CurveWithTangent|  Snap to point on curve with tangent continuity.
         |ParallelCurve|  Snap parallel to curve or tangent continuous string of curves.
         |IsoparametricGrid|  Snap to isoparametric grid.

        """
        NotSet: int
        Curve: int
        CurveWithTangent: int
        ParallelCurve: int
        IsoparametricGrid: int
        @staticmethod
        def ValueOf(value: int) -> DrawCurveData.SnapToOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SnappingOption(Enum):
        """
        Members Include: 
         |NotSet|  No snapping. 
         |CurveEndPoints|  Snap to curve end points.
         |IsoparametricGrid|  Snap to isoparametric grid.

        """
        NotSet: int
        CurveEndPoints: int
        IsoparametricGrid: int
        @staticmethod
        def ValueOf(value: int) -> DrawCurveData.SnappingOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CanCreatePrimitives(self) -> bool:
        """
        Getter for property: (bool) CanCreatePrimitives
         Returns the value indicating if primitive curve should be created   
            
         
        """
        pass
    @CanCreatePrimitives.setter
    def CanCreatePrimitives(self, canCreatePrimitive: bool):
        """
        Setter for property: (bool) CanCreatePrimitives
         Returns the value indicating if primitive curve should be created   
            
         
        """
        pass
    @property
    def CanDrawOnNearestFace(self) -> bool:
        """
        Getter for property: (bool) CanDrawOnNearestFace
         Returns the flag indicating if curves should be created only on the nearest face in view direction and 
                    not on faces on the back of a body.  
           This option decreases the drawing performance.   
         
        """
        pass
    @CanDrawOnNearestFace.setter
    def CanDrawOnNearestFace(self, doNearFaceProjection: bool):
        """
        Setter for property: (bool) CanDrawOnNearestFace
         Returns the flag indicating if curves should be created only on the nearest face in view direction and 
                    not on faces on the back of a body.  
           This option decreases the drawing performance.   
         
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
    def DetectionSensitivity(self) -> DrawCurveData.DetectionSensitivityOption:
        """
        Getter for property: ( DrawCurveData.DetectionSensitivityOption NXOpen.Featu) DetectionSensitivity
         Returns the value indicating detection sensitivity.  
           The smaller the sensitivity,
                    the more accurate the stroke must be to be recognized as primitive.   
         
        """
        pass
    @DetectionSensitivity.setter
    def DetectionSensitivity(self, detectionSensitivity: DrawCurveData.DetectionSensitivityOption):
        """
        Setter for property: ( DrawCurveData.DetectionSensitivityOption NXOpen.Featu) DetectionSensitivity
         Returns the value indicating detection sensitivity.  
           The smaller the sensitivity,
                    the more accurate the stroke must be to be recognized as primitive.   
         
        """
        pass
    @property
    def OversketchExistingCurves(self) -> bool:
        """
        Getter for property: (bool) OversketchExistingCurves
         Returns the value indicating if existing curves should be over sketched   
            
         
        """
        pass
    @OversketchExistingCurves.setter
    def OversketchExistingCurves(self, oversketchExistingCurves: bool):
        """
        Setter for property: (bool) OversketchExistingCurves
         Returns the value indicating if existing curves should be over sketched   
            
         
        """
        pass
    @property
    def ParallelCurveTargets(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) ParallelCurveTargets
         Returns the target curves of parallel curve drawing   
            
         
        """
        pass
    @property
    def SnapToOption(self) -> DrawCurveData.SnapToOptions:
        """
        Getter for property: ( DrawCurveData.SnapToOptions NXOpen.Featu) SnapToOption
         Returns the value indicating snapping option.  
             
         
        """
        pass
    @SnapToOption.setter
    def SnapToOption(self, snapping: DrawCurveData.SnapToOptions):
        """
        Setter for property: ( DrawCurveData.SnapToOptions NXOpen.Featu) SnapToOption
         Returns the value indicating snapping option.  
             
         
        """
        pass
    @property
    def Snapping(self) -> DrawCurveData.SnappingOption:
        """
        Getter for property: ( DrawCurveData.SnappingOption NXOpen.Featu) Snapping
         Returns the value indicating snapping option.  
             
         
        """
        pass
    @Snapping.setter
    def Snapping(self, snapping: DrawCurveData.SnappingOption):
        """
        Setter for property: ( DrawCurveData.SnappingOption NXOpen.Featu) Snapping
         Returns the value indicating snapping option.  
             
         
        """
        pass
    @property
    def StrokeGesture(self) -> NXOpen.GeometricUtilities.StrokeGestureData:
        """
        Getter for property: ( NXOpen.GeometricUtilities.StrokeGestureData) StrokeGesture
         Returns the object enabling drawing of the curve   
            
         
        """
        pass
    @property
    def Thickness(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectWidth) Thickness
         Returns the thickness   
            
         
        """
        pass
    @Thickness.setter
    def Thickness(self, thickness: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectWidth) Thickness
         Returns the thickness   
            
         
        """
        pass
    def SetOverSketchTolerance(self, overSketchTolerance: float) -> None:
        """
         Distance tolerance used to decide if newly drawn curve is considered as over-sketched curve on pre-existing curve. 
        """
        pass
import NXOpen
class DrawShapeCollection(NXOpen.Object): 
    """ Collection of Draw Shape tools. """
    def CreateCurveFromStrokeData(self) -> CurveFromStrokeData:
        """
         Creates a NXOpen.Features.DrawShapes.CurveFromStrokeData 
         Returns builder ( CurveFromStrokeData NXOpen.Featu): .
        """
        pass
    def CreateDeleteData(self) -> DeleteData:
        """
         Creates a NXOpen.Features.DrawShapes.DeleteData 
         Returns builder ( DeleteData NXOpen.Featu): .
        """
        pass
    def CreateDivideBuilder(self) -> DivideBuilder:
        """
         Creates a NXOpen.Features.DrawShapes.DivideBuilder 
         Returns builder ( DivideBuilder NXOpen.Featu): .
        """
        pass
    def CreateDrawCurveData(self) -> DrawCurveData:
        """
         Creates a NXOpen.Features.DrawShapes.DrawCurveData 
         Returns builder ( DrawCurveData NXOpen.Featu): .
        """
        pass
    def CreateDrawShapeData(self) -> DrawShapeData:
        """
         Creates a NXOpen.Features.DrawShapes.DrawShapeData 
         Returns builder ( DrawShapeData NXOpen.Featu): .
        """
        pass
    def CreateDrawStrokeData(self) -> DrawStrokeData:
        """
         Creates a NXOpen.Features.DrawShapes.DrawStrokeData 
         Returns builder ( DrawStrokeData NXOpen.Featu): .
        """
        pass
    def CreateEditCurveBuilder(self, curveToEdit: NXOpen.Curve) -> EditCurveBuilder:
        """
         Creates a NXOpen.Features.DrawShapes.EditCurveBuilder 
         Returns builder ( EditCurveBuilder NXOpen.Featu): .
        """
        pass
    def CreateEditDisplayBuilder(self) -> EditDisplayBuilder:
        """
         Creates a NXOpen.Features.DrawShapes.EditDisplayBuilder 
         Returns builder ( EditDisplayBuilder NXOpen.Featu): .
        """
        pass
    def CreateEraseBuilder(self) -> EraseBuilder:
        """
         Creates a NXOpen.Features.DrawShapes.EraseBuilder 
         Returns builder ( EraseBuilder NXOpen.Featu): .
        """
        pass
    def CreateExtendBuilder(self) -> ExtendBuilder:
        """
         Creates a NXOpen.Features.DrawShapes.ExtendBuilder 
         Returns builder ( ExtendBuilder NXOpen.Featu): .
        """
        pass
    def CreateFilletBuilder(self) -> FilletBuilder:
        """
         Creates a NXOpen.Features.DrawShapes.FilletBuilder 
         Returns builder ( FilletBuilder NXOpen.Featu): .
        """
        pass
    def CreateIntersectionCurveBuilder(self) -> IntersectionCurveBuilder:
        """
         Creates a NXOpen.Features.DrawShapes.IntersectionCurveBuilder 
         Returns builder ( IntersectionCurveBuilder NXOpen.Featu): .
        """
        pass
    def CreateMirrorData(self) -> MirrorData:
        """
         Creates a NXOpen.Features.DrawShapes.MirrorData 
         Returns builder ( MirrorData NXOpen.Featu): .
        """
        pass
    def CreateOffsetCurveData(self) -> OffsetCurveData:
        """
         Creates a NXOpen.Features.DrawShapes.OffsetCurveData 
         Returns builder ( OffsetCurveData NXOpen.Featu): .
        """
        pass
    def CreateProjectCurveBuilder(self) -> ProjectCurveBuilder:
        """
         Creates a NXOpen.Features.DrawShapes.ProjectCurveBuilder 
         Returns builder ( ProjectCurveBuilder NXOpen.Featu): .
        """
        pass
    def CreateStartSymmetryModeBuilder(self) -> StartSymmetryModeBuilder:
        """
         Creates a NXOpen.Features.DrawShapes.StartSymmetryModeBuilder. 
         Returns builder ( StartSymmetryModeBuilder NXOpen.Featu): .
        """
        pass
    def CreateTransformData(self) -> TransformData:
        """
         Creates a NXOpen.Features.DrawShapes.TransformData 
         Returns builder ( TransformData NXOpen.Featu): .
        """
        pass
    def CreateTrimBuilder(self) -> TrimBuilder:
        """
         Creates a NXOpen.Features.DrawShapes.TrimBuilder 
         Returns builder ( TrimBuilder NXOpen.Featu): .
        """
        pass
    def StopSymmetryMode(self) -> bool:
        """
         Stops the symmetry mode. 
         Returns atLeastOneSymmetryCurveDeleted (bool):  The flag indicating if at least one curve was deleted during stopping of the symmetry mode.
                        When symmetry mode is stopped, symmetric curves are normally retained. A curve may be deleted if it does not have a drawing base supporting it.
                        This may happen for NXOpen.Features.DrawShapes.DrawShapeData.DrawingBaseTypes.Faces  type of drawing base. .
        """
        pass
import NXOpen
class DrawShapeData(NXOpen.Builder): 
    """ Represents  NXOpen.Features.DrawShapes.DrawShapeData 
        allowing user to define input faces or datums for Draw Shape
    """
    class DrawingBaseTypes(Enum):
        """
        Members Include: 
         |Faces| 
         |Plane| 

        """
        Faces: int
        Plane: int
        @staticmethod
        def ValueOf(value: int) -> DrawShapeData.DrawingBaseTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns whether to create the associative output or non associative output  
            
         
        """
        pass
    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
         Returns whether to create the associative output or non associative output  
            
         
        """
        pass
    @property
    def CoordinateSystem(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) CoordinateSystem
         Returns the coordinate system.  
           XY Plane of the coordinate system is used as drawing base.   
         
        """
        pass
    @CoordinateSystem.setter
    def CoordinateSystem(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) CoordinateSystem
         Returns the coordinate system.  
           XY Plane of the coordinate system is used as drawing base.   
         
        """
        pass
    @property
    def DrawingBaseType(self) -> DrawShapeData.DrawingBaseTypes:
        """
        Getter for property: ( DrawShapeData.DrawingBaseTypes NXOpen.Featu) DrawingBaseType
         Returns the drawing base type   
            
         
        """
        pass
    @DrawingBaseType.setter
    def DrawingBaseType(self, type: DrawShapeData.DrawingBaseTypes):
        """
        Setter for property: ( DrawShapeData.DrawingBaseTypes NXOpen.Featu) DrawingBaseType
         Returns the drawing base type   
            
         
        """
        pass
    @property
    def Faces(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Faces
         Returns the faces   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class DrawStrokeData(NXOpen.Builder): 
    """ Represents  NXOpen.Features.DrawShapes.DrawStrokeData 
        allowing user to define stroke using drag gesture.
    """
    @property
    def CanDrawOnNearestFace(self) -> bool:
        """
        Getter for property: (bool) CanDrawOnNearestFace
         Returns the flag indicating if stroke should be created only on the nearest face in view direction and 
                    not on faces on the back of a body.  
           This option decreases the drawing performance.   
         
        """
        pass
    @CanDrawOnNearestFace.setter
    def CanDrawOnNearestFace(self, doNearFaceProjection: bool):
        """
        Setter for property: (bool) CanDrawOnNearestFace
         Returns the flag indicating if stroke should be created only on the nearest face in view direction and 
                    not on faces on the back of a body.  
           This option decreases the drawing performance.   
         
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
    def StrokeGesture(self) -> NXOpen.GeometricUtilities.StrokeGestureData:
        """
        Getter for property: ( NXOpen.GeometricUtilities.StrokeGestureData) StrokeGesture
         Returns the object enabling drawing of the stroke   
            
         
        """
        pass
    @property
    def Thickness(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectWidth) Thickness
         Returns the thickness   
            
         
        """
        pass
    @Thickness.setter
    def Thickness(self, thickness: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectWidth) Thickness
         Returns the thickness   
            
         
        """
        pass
import NXOpen
import NXOpen.Features
class EditCurveBuilder(NXOpen.Builder): 
    """ Represents  NXOpen.Features.DrawShapes.EditCurveBuilder 
        allowing user to a edit curve.
    """
    class CircleDefinitionOption(Enum):
        """
        Members Include: 
         |ThreePoints| 
         |CenterandRadius| 

        """
        ThreePoints: int
        CenterandRadius: int
        @staticmethod
        def ValueOf(value: int) -> EditCurveBuilder.CircleDefinitionOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CircleDefinitionOptions(self) -> EditCurveBuilder.CircleDefinitionOption:
        """
        Getter for property: ( EditCurveBuilder.CircleDefinitionOption NXOpen.Featu) CircleDefinitionOptions
         Returns the circle definition options   
            
         
        """
        pass
    @CircleDefinitionOptions.setter
    def CircleDefinitionOptions(self, circleDefinitionOptions: EditCurveBuilder.CircleDefinitionOption):
        """
        Setter for property: ( EditCurveBuilder.CircleDefinitionOption NXOpen.Featu) CircleDefinitionOptions
         Returns the circle definition options   
            
         
        """
        pass
    @property
    def ConstraintManager(self) -> NXOpen.Features.GeometricConstraintDataManager:
        """
        Getter for property: ( NXOpen.Features.GeometricConstraintDataManager) ConstraintManager
         Returns the constraint manager   
            
         
        """
        pass
    @property
    def IsClosed(self) -> bool:
        """
        Getter for property: (bool) IsClosed
         Returns the flag indicating if spline can be closed   
            
         
        """
        pass
    @IsClosed.setter
    def IsClosed(self, isClosed: bool):
        """
        Setter for property: (bool) IsClosed
         Returns the flag indicating if spline can be closed   
            
         
        """
        pass
    @property
    def PointNumber(self) -> int:
        """
        Getter for property: (int) PointNumber
         Returns the value indicating number of defining points a spline should have.  
           Use this parameter to reduce the number
                    of points on a spline.
                  
         
        """
        pass
    @PointNumber.setter
    def PointNumber(self, pointNumber: int):
        """
        Setter for property: (int) PointNumber
         Returns the value indicating number of defining points a spline should have.  
           Use this parameter to reduce the number
                    of points on a spline.
                  
         
        """
        pass
    @property
    def Radius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Radius
         Returns the radius   
            
         
        """
        pass
    def EvaluateCurve(self) -> None:
        """
         Evaluates the curve after editing defining data. 
        """
        pass
    def UpdateConstraintManagerPostPointEdit(self) -> None:
        """
         Updates the constraint manager after point is edited. 
        """
        pass
import NXOpen
class EditDisplayBuilder(NXOpen.Builder): 
    """ Represents  NXOpen.Features.DrawShapes.EditDisplayBuilder 
        allowing user to edit display of strokes and curves.
    """
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
    def Objects(self) -> NXOpen.SelectCurveList:
        """
        Getter for property: ( NXOpen.SelectCurveList) Objects
         Returns the objects   
            
         
        """
        pass
    @property
    def Thickness(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectWidth) Thickness
         Returns the thickness   
            
         
        """
        pass
    @Thickness.setter
    def Thickness(self, thickness: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectWidth) Thickness
         Returns the thickness   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class EraseBuilder(NXOpen.Builder): 
    """ Represents  NXOpen.Features.DrawShapes.EraseBuilder 
            allowing user to erase strokes or curves.
        """
    @property
    def StrokeGesture(self) -> NXOpen.GeometricUtilities.StrokeGestureData:
        """
        Getter for property: ( NXOpen.GeometricUtilities.StrokeGestureData) StrokeGesture
         Returns the object enabling erasing strokes or curves   
            
         
        """
        pass
    @property
    def Thickness(self) -> float:
        """
        Getter for property: (float) Thickness
         Returns the thickness   
            
         
        """
        pass
    @Thickness.setter
    def Thickness(self, thickness: float):
        """
        Setter for property: (float) Thickness
         Returns the thickness   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ExtendBuilder(NXOpen.Builder): 
    """ Represents  NXOpen.Features.DrawShapes.ExtendBuilder 
            allowing user to extend strokes or curves.
        """
    @property
    def BoundaryObjects(self) -> NXOpen.SelectCurveList:
        """
        Getter for property: ( NXOpen.SelectCurveList) BoundaryObjects
         Returns the boundary objects   
            
         
        """
        pass
    @property
    def ExtendBound(self) -> bool:
        """
        Getter for property: (bool) ExtendBound
         Returns the flag to control the ability to extend to extension of the boundary   
            
         
        """
        pass
    @ExtendBound.setter
    def ExtendBound(self, extendBound: bool):
        """
        Setter for property: (bool) ExtendBound
         Returns the flag to control the ability to extend to extension of the boundary   
            
         
        """
        pass
    @property
    def Targets(self) -> NXOpen.GeometricUtilities.CrayonSelectionData:
        """
        Getter for property: ( NXOpen.GeometricUtilities.CrayonSelectionData) Targets
         Returns the points indicating trimming location on the object to be extended   
            
         
        """
        pass
import NXOpen
class FilletBuilder(NXOpen.Builder): 
    """ Represents  NXOpen.Features.DrawShapes.FilletBuilder 
            allowing user to create a fillet between two curves.
        """
    class PlacementData:
        """
         Contains placement information for creating a fillet. 
         FilletBuilderPlacementData_Struct NXOpen.Featu is an alias for  FilletBuilder.PlacementData NXOpen.Featu.
        """
        @property
        def Position(self) -> NXOpen.Point3d:
            """
            Getter for property Position
            The point at which fillet is placed

            """
            pass
        @Position.setter
        def Position(self, value: NXOpen.Point3d):
            """
            Getter for property Position
            The point at which fillet is placed
            Setter for property Position
            The point at which fillet is placed

            """
            pass
        @property
        def ViewMatrix(self) -> NXOpen.Matrix3x3:
            """
            Getter for property ViewMatrix
            The view matrix while placing the fillet

            """
            pass
        @ViewMatrix.setter
        def ViewMatrix(self, value: NXOpen.Matrix3x3):
            """
            Getter for property ViewMatrix
            The view matrix while placing the fillet
            Setter for property ViewMatrix
            The view matrix while placing the fillet

            """
            pass
    @property
    def CreateAlternateFillet(self) -> bool:
        """
        Getter for property: (bool) CreateAlternateFillet
         Returns the flag to create alternate fillet   
            
         
        """
        pass
    @CreateAlternateFillet.setter
    def CreateAlternateFillet(self, createAlternateFillet: bool):
        """
        Setter for property: (bool) CreateAlternateFillet
         Returns the flag to create alternate fillet   
            
         
        """
        pass
    @property
    def FirstCurve(self) -> NXOpen.SelectCurve:
        """
        Getter for property: ( NXOpen.SelectCurve) FirstCurve
         Returns the first curve   
            
         
        """
        pass
    @property
    def SecondCurve(self) -> NXOpen.SelectCurve:
        """
        Getter for property: ( NXOpen.SelectCurve) SecondCurve
         Returns the second curve   
            
         
        """
        pass
    @property
    def TrimInputCurves(self) -> bool:
        """
        Getter for property: (bool) TrimInputCurves
         Returns the flag to control the ability to trim input curves   
            
         
        """
        pass
    @TrimInputCurves.setter
    def TrimInputCurves(self, trimInputs: bool):
        """
        Setter for property: (bool) TrimInputCurves
         Returns the flag to control the ability to trim input curves   
            
         
        """
        pass
    def SetPlacementData(self, placementData: FilletBuilder.PlacementData) -> None:
        """
         Sets the placement data for fillet. 
        """
        pass
import NXOpen
class IntersectionCurveBuilder(NXOpen.Builder): 
    """ Represents  NXOpen.Features.DrawShapes.IntersectionCurveBuilder 
       allowing the user to intersection existing faces andor planes from outside the Draw Shape feature with the drawing base and create them as drawn curves of the feature.
   """
    @property
    def DrawingBases(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) DrawingBases
         Returns the faces of the drawing base.  
           These entities can only be a sub-set of drawing bases.  
         
        """
        pass
    @property
    def FacesOrPlane(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FacesOrPlane
         Returns the faces or datum planes from outside the Draw Shape feature to intersect them with the drawing base   
            
         
        """
        pass
import NXOpen
class MirrorData(NXOpen.Builder): 
    """ Represents  NXOpen.Features.DrawShapes.MirrorData 
        allowing user to mirror curves.
    """
    @property
    def Objects(self) -> NXOpen.SelectCurveList:
        """
        Getter for property: ( NXOpen.SelectCurveList) Objects
         Returns the objects   
            
         
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
import NXOpen
class OffsetCurveData(NXOpen.Builder): 
    """ Represents  NXOpen.Features.DrawShapes.OffsetCurveData 
        allowing user to offset curve.
    """
    class SharpCornerTreatment(Enum):
        """
        Members Include: 
         |Keep| 
         |Round| 

        """
        Keep: int
        Round: int
        @staticmethod
        def ValueOf(value: int) -> OffsetCurveData.SharpCornerTreatment:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CornerTreatment(self) -> OffsetCurveData.SharpCornerTreatment:
        """
        Getter for property: ( OffsetCurveData.SharpCornerTreatment NXOpen.Featu) CornerTreatment
         Returns the corner treatment   
            
         
        """
        pass
    @CornerTreatment.setter
    def CornerTreatment(self, cornerTreatment: OffsetCurveData.SharpCornerTreatment):
        """
        Setter for property: ( OffsetCurveData.SharpCornerTreatment NXOpen.Featu) CornerTreatment
         Returns the corner treatment   
            
         
        """
        pass
    @property
    def CurvesToOffset(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) CurvesToOffset
         Returns the curves to offset   
            
         
        """
        pass
    @property
    def OffsetDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OffsetDistance
         Returns the offset distance   
            
         
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
    def RoundRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RoundRadius
         Returns the round radius   
            
         
        """
        pass
    def DisplayPreviewCurves(self) -> None:
        """
         Displays curve preview. 
        """
        pass
    def UpdateOnCurveSelection(self, seedEntity: NXOpen.Curve, seedPoint: NXOpen.Point3d) -> None:
        """
         Updates internal data based on the selected seed curve and point. 
        """
        pass
import NXOpen
class ProjectCurveBuilder(NXOpen.Builder): 
    """ Represents  NXOpen.Features.DrawShapes.ProjectCurveBuilder 
            allowing user to project existing curves from outside of Draw Shape feature to the drawing base and create them as drawn curves of the feature.
        """
    class ProjectionDirectionType(Enum):
        """
        Members Include: 
         |NormaltoDrawingBase|  Curves will be projected along local face normal of drawing base 
         |AlongVector|  User specifies a vector for uniform drawing projection 

        """
        NormaltoDrawingBase: int
        AlongVector: int
        @staticmethod
        def ValueOf(value: int) -> ProjectCurveBuilder.ProjectionDirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Curves(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Curves
         Returns the curves to project   
            
         
        """
        pass
    @property
    def DrawingBaseFaces(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) DrawingBaseFaces
         Returns the faces or plane to project curves on.  
           These entities can only be a sub-set of drawing bases.   
         
        """
        pass
    @property
    def HideInputCurves(self) -> bool:
        """
        Getter for property: (bool) HideInputCurves
         Returns the value indicating if input curves should be hidden.  
             
         
        """
        pass
    @HideInputCurves.setter
    def HideInputCurves(self, hideInputCurves: bool):
        """
        Setter for property: (bool) HideInputCurves
         Returns the value indicating if input curves should be hidden.  
             
         
        """
        pass
    @property
    def ProjectBothSides(self) -> bool:
        """
        Getter for property: (bool) ProjectBothSides
         Returns the value indicating if projection should be done in both the sides of the specified direction.  
             
         
        """
        pass
    @ProjectBothSides.setter
    def ProjectBothSides(self, projectBothSides: bool):
        """
        Setter for property: (bool) ProjectBothSides
         Returns the value indicating if projection should be done in both the sides of the specified direction.  
             
         
        """
        pass
    @property
    def ProjectNearestPoint(self) -> bool:
        """
        Getter for property: (bool) ProjectNearestPoint
         Returns the value indicating if curves should be projected to the nearest point on drawing base in a given direction.  
             
         
        """
        pass
    @ProjectNearestPoint.setter
    def ProjectNearestPoint(self, projectNearestPoint: bool):
        """
        Setter for property: (bool) ProjectNearestPoint
         Returns the value indicating if curves should be projected to the nearest point on drawing base in a given direction.  
             
         
        """
        pass
    @property
    def ProjectionDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ProjectionDirection
         Returns the direction   
            
         
        """
        pass
    @ProjectionDirection.setter
    def ProjectionDirection(self, direction: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ProjectionDirection
         Returns the direction   
            
         
        """
        pass
    @property
    def ProjectionDirectionOption(self) -> ProjectCurveBuilder.ProjectionDirectionType:
        """
        Getter for property: ( ProjectCurveBuilder.ProjectionDirectionType NXOpen.Featu) ProjectionDirectionOption
         Returns the projection direction option   
            
         
        """
        pass
    @ProjectionDirectionOption.setter
    def ProjectionDirectionOption(self, projectionDir: ProjectCurveBuilder.ProjectionDirectionType):
        """
        Setter for property: ( ProjectCurveBuilder.ProjectionDirectionType NXOpen.Featu) ProjectionDirectionOption
         Returns the projection direction option   
            
         
        """
        pass
import NXOpen
class StartSymmetryModeBuilder(NXOpen.Builder): 
    """ Represents  NXOpen.Features.DrawShapes.StartSymmetryModeBuilder 
        allowing user to start symmetry mode.
    """
    @property
    def CreateSymmetricCopiesOfExistingCurves(self) -> bool:
        """
        Getter for property: (bool) CreateSymmetricCopiesOfExistingCurves
         Returns the Create Symmetric Copies of Exisitng Curves   
            
         
        """
        pass
    @CreateSymmetricCopiesOfExistingCurves.setter
    def CreateSymmetricCopiesOfExistingCurves(self, createSymmetricCopiesOfExistingCurves: bool):
        """
        Setter for property: (bool) CreateSymmetricCopiesOfExistingCurves
         Returns the Create Symmetric Copies of Exisitng Curves   
            
         
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
import NXOpen
import NXOpen.GeometricUtilities
class TransformData(NXOpen.Builder): 
    """ Represents  NXOpen.Features.DrawShapes.TransformData 
        allowing user to delete strokes and curves.
    """
    class ResultOptions(Enum):
        """
        Members Include: 
         |MoveOriginal| 
         |CopyOriginal| 

        """
        MoveOriginal: int
        CopyOriginal: int
        @staticmethod
        def ValueOf(value: int) -> TransformData.ResultOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ScalingOptions(Enum):
        """
        Members Include: 
         |Linear| 
         |Planar| 
         |Uniform| 

        """
        Linear: int
        Planar: int
        Uniform: int
        @staticmethod
        def ValueOf(value: int) -> TransformData.ScalingOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CanMoveToolOnly(self) -> bool:
        """
        Getter for property: (bool) CanMoveToolOnly
         Returns the can move tool only   
            
         
        """
        pass
    @CanMoveToolOnly.setter
    def CanMoveToolOnly(self, canMoveToolOnly: bool):
        """
        Setter for property: (bool) CanMoveToolOnly
         Returns the can move tool only   
            
         
        """
        pass
    @property
    def CanRelocateToolToSelection(self) -> bool:
        """
        Getter for property: (bool) CanRelocateToolToSelection
         Returns the can relocate tool to selection   
            
         
        """
        pass
    @CanRelocateToolToSelection.setter
    def CanRelocateToolToSelection(self, canRelocateToolToSelection: bool):
        """
        Setter for property: (bool) CanRelocateToolToSelection
         Returns the can relocate tool to selection   
            
         
        """
        pass
    @property
    def CanReorientToolToSelection(self) -> bool:
        """
        Getter for property: (bool) CanReorientToolToSelection
         Returns the can reorient tool to selection   
            
         
        """
        pass
    @CanReorientToolToSelection.setter
    def CanReorientToolToSelection(self, canReorientToolToSelection: bool):
        """
        Setter for property: (bool) CanReorientToolToSelection
         Returns the can reorient tool to selection   
            
         
        """
        pass
    @property
    def NumberOfCopies(self) -> int:
        """
        Getter for property: (int) NumberOfCopies
         Returns the number of copies   
            
         
        """
        pass
    @NumberOfCopies.setter
    def NumberOfCopies(self, numberOfCopies: int):
        """
        Setter for property: (int) NumberOfCopies
         Returns the number of copies   
            
         
        """
        pass
    @property
    def ObjectsToTransform(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) ObjectsToTransform
         Returns the objects to be transformed   
            
         
        """
        pass
    @property
    def ResultOption(self) -> TransformData.ResultOptions:
        """
        Getter for property: ( TransformData.ResultOptions NXOpen.Featu) ResultOption
         Returns the result option   
            
         
        """
        pass
    @ResultOption.setter
    def ResultOption(self, resultOption: TransformData.ResultOptions):
        """
        Setter for property: ( TransformData.ResultOptions NXOpen.Featu) ResultOption
         Returns the result option   
            
         
        """
        pass
    @property
    def Scaling(self) -> TransformData.ScalingOptions:
        """
        Getter for property: ( TransformData.ScalingOptions NXOpen.Featu) Scaling
         Returns the scaling   
            
         
        """
        pass
    @Scaling.setter
    def Scaling(self, scaling: TransformData.ScalingOptions):
        """
        Setter for property: ( TransformData.ScalingOptions NXOpen.Featu) Scaling
         Returns the scaling   
            
         
        """
        pass
    @property
    def Transformer(self) -> NXOpen.GeometricUtilities.TransformerData:
        """
        Getter for property: ( NXOpen.GeometricUtilities.TransformerData) Transformer
         Returns the transformation tool.  
           The tool allows user to transform the pasted topology.   
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class TrimBuilder(NXOpen.Builder): 
    """ Represents  NXOpen.Features.DrawShapes.TrimBuilder 
            allowing user to trim strokes or curves.
        """
    @property
    def BoundaryObjects(self) -> NXOpen.SelectCurveList:
        """
        Getter for property: ( NXOpen.SelectCurveList) BoundaryObjects
         Returns the boundary objects   
            
         
        """
        pass
    @property
    def ExtendBound(self) -> bool:
        """
        Getter for property: (bool) ExtendBound
         Returns the flag to control the ability to trim to extension of the boundary   
            
         
        """
        pass
    @ExtendBound.setter
    def ExtendBound(self, extendBound: bool):
        """
        Setter for property: (bool) ExtendBound
         Returns the flag to control the ability to trim to extension of the boundary   
            
         
        """
        pass
    @property
    def Point(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: ( NXOpen.SelectDisplayableObject) Point
         Returns the point indicating snapped location on the object to be trimmed   
            
         
        """
        pass
    @property
    def Targets(self) -> NXOpen.GeometricUtilities.CrayonSelectionData:
        """
        Getter for property: ( NXOpen.GeometricUtilities.CrayonSelectionData) Targets
         Returns the points indicating trimming location on the object to be trimmed   
            
         
        """
        pass
