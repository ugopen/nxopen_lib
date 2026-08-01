from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class AnalysisManager(NXOpen.Object): 
    """ Represents the collection of analysis commands. Inputs to this class can be convergent objects."""
    @property
    def AnalysisObjects() -> AnalysisObjectCollection:
        """
         Returns the AnalysisObjectCollection instance belonging to this part 
        """
        pass
    def CreateDeviationCheckingObject(self) -> DeviationChecking:
        """
         Creates a deviation checking object 
         Returns builder ( DeviationChecking NXOpen.Geom):  DeviationChecking object.
        """
        pass
    def CreateExamineGeometryObject(self) -> ExamineGeometry:
        """
         Creates an examine geometry object 
         Returns builder ( ExamineGeometry NXOpen.Geom):  Examine
                                                                                            Geometry object .
        """
        pass
    def CreateGeometricPropertiesObject(self) -> GeometricProperties:
        """
         Creates a geometric properties object 
         Returns builder ( GeometricProperties NXOpen.Geom): 
                                                                                    Geometric
                                                                                    Properties object .
        """
        pass
    def CreateSimpleInterferenceObject(self) -> SimpleInterference:
        """
         Creates a simple interference object 
         Returns builder ( SimpleInterference NXOpen.Geom): 
                                                                                     Simple Interference object .
        """
        pass
    def CreateSolidDensityObject(self) -> SolidDensity:
        """
         Creates a solid density object 
         Returns builder ( SolidDensity NXOpen.Geom):  SolidDensity object.
        """
        pass
import NXOpen
class AnalysisObjectCollectionEx(NXOpen.Object): 
    """ Collection of analysis objects """
    def CreateDistanceAnalysisBuilder(self, distanceAO: NXOpen.DisplayableObject) -> DistanceAnalysisBuilder:
        """
         Creates a distance analysis builder. 
         Returns distanceBuilder ( DistanceAnalysisBuilder NXOpen.Geom):  distance analysis builder .
        """
        pass
    def CreateDistanceAnalysisBuilder1(self, distanceAO: NXOpen.DisplayableObject) -> DistanceAnalysisBuilder1:
        """
         Creates a distance analysis builder. 
         Returns distanceBuilder ( DistanceAnalysisBuilder1 NXOpen.Geom):  distance analysis builder .
        """
        pass
    def CreatePerformancePredictorBuilder(self, perfPredictAO: PerformancePredictor) -> PerformancePredictorBuilder:
        """
         Creates a GeometricAnalysis.PerformancePredictorBuilder  
         Returns perfPredictBuilder ( PerformancePredictorBuilder NXOpen.Geom):  NXOpen.GeometricAnalysis.PerformancePredictorBuilder with this name. .
        """
        pass
    def CreateRadiusAnalysisBuilder(self, radiusAO: NXOpen.DisplayableObject) -> RadiusAnalysisBuilder:
        """
         Creates a radius analysis builder. 
         Returns radiusBuilder ( RadiusAnalysisBuilder NXOpen.Geom):  radius analysis builder .
        """
        pass
    def CreateRadiusAnalysisBuilder1(self, radiusAO: NXOpen.DisplayableObject) -> RadiusAnalysisBuilder1:
        """
         Creates a radius analysis builder. 
         Returns radiusBuilder ( RadiusAnalysisBuilder1 NXOpen.Geom):  radius analysis builder .
        """
        pass
    def CreateReflectionAnalysisBuilder(self, reflectionAO: NXOpen.DisplayableObject) -> ReflectionAnalysisBuilder:
        """
         Creates a reflection analysis builder. 
         Returns reflectionBuilder ( ReflectionAnalysisBuilder NXOpen.Geom):  reflection analysis builder .
        """
        pass
    def CreateReflectionAnalysisBuilder1(self, reflectionAO: NXOpen.DisplayableObject) -> ReflectionAnalysisBuilder1:
        """
         Creates a reflection analysis builder. 
         Returns reflectionBuilder ( ReflectionAnalysisBuilder1 NXOpen.Geom):  reflection analysis builder .
        """
        pass
    def CreateSheetBoundaryAnalysisBuilder(self, sheetBoundaryAnalysisAO: SheetBoundaryAnalysis) -> SheetBoundaryAnalysisBuilder:
        """
         Creates a GeometricAnalysis.SheetBoundaryAnalysisBuilder  
         Returns sheetBoundaryBuilder ( SheetBoundaryAnalysisBuilder NXOpen.Geom):  sheet boundary analysis builder .
        """
        pass
    def CreateSlopeAnalysisBuilder(self, slopeAO: NXOpen.DisplayableObject) -> SlopeAnalysisBuilder:
        """
         Creates a slope analysis builder. 
         Returns slopeBuilder ( SlopeAnalysisBuilder NXOpen.Geom):  slope analysis builder .
        """
        pass
    def CreateSlopeAnalysisBuilder1(self, slopeAO: NXOpen.DisplayableObject) -> SlopeAnalysisBuilder1:
        """
         Creates a slope analysis builder. 
         Returns slopeBuilder ( SlopeAnalysisBuilder1 NXOpen.Geom):  slope analysis builder .
        """
        pass
import NXOpen
import NXOpen.GeometricAnalysis.SectionAnalysis
class AnalysisObjectCollection(NXOpen.TaggedObjectCollection): 
    """ Create a AnalysisObjectCollection """
    @property
    def CurveAnalysisDisplayObject() -> CurveAnalysisDisplay:
        """
         Returns object for displaying curve analysis information 
        """
        pass
    @property
    def SurfaceAnalysisDisplayObject() -> SurfaceAnalysisDisplay:
        """
         Returns object for displaying surface analysis information 
        """
        pass
    @property
    def AnalysisObjectsEx() -> AnalysisObjectCollectionEx:
        """
         Returns the AnalysisObjectCollectionEx instance belonging to this part 
        """
        pass
    def CreateCurveContinuityBuilder(self, ccao_object: NXOpen.DisplayableObject) -> CurveContinuityBuilder:
        """
         Creates a Curve Continuity Builder 
         Returns ccao_builder ( CurveContinuityBuilder NXOpen.Geom):  Curve Continuity AO builder .
        """
        pass
    def CreateCurveCurvatureAnalysisBuilder(self, caao_object: NXOpen.DisplayableObject) -> CurveCurvatureAnalysisBuilder:
        """
         Creates a curve curvature analysis builder 
         Returns caao_builder ( CurveCurvatureAnalysisBuilder NXOpen.Geom):  Curve Curvature Analysis builder .
        """
        pass
    def CreateDeviationGaugeBuilder(self, ddao_object: NXOpen.DisplayableObject) -> DeviationGaugeBuilder:
        """
         Creates a  Deviation Gauge Builder 
         Returns devgg_builder ( DeviationGaugeBuilder NXOpen.Geom):  DeviationGauge builder .
        """
        pass
    def CreateDraftAnalysisBuilder(self, dao_object: NXOpen.DisplayableObject) -> DraftAnalysisBuilder:
        """
         Creates a draft analysis builder 
         Returns dao_builder ( DraftAnalysisBuilder NXOpen.Geom):  draft analysis builder .
        """
        pass
    def CreateFaceCurvatureAnalysisBuilder(self, fcao_object: NXOpen.DisplayableObject) -> FaceCurvatureAnalysisBuilder:
        """
         Creates a face curvature analysis builder 
         Returns fcao_builder ( FaceCurvatureAnalysisBuilder NXOpen.Geom):  face curvature analysis builder .
        """
        pass
    def CreateGapFlushnessBuilder(self, gfao_object: GapFlushness) -> GapFlushnessBuilder:
        """
         Creates a gap and flushness builder 
         Returns gfao_builder ( GapFlushnessBuilder NXOpen.Geom):  Gap and Flushness builder .
        """
        pass
    def CreateHighlightLinesAnalysisBuilder(self, hpao_object: NXOpen.DisplayableObject) -> HighlightLinesAnalysisBuilder:
        """
         Creates a Highlight Lines Analysis builder 
         Returns builder ( HighlightLinesAnalysisBuilder NXOpen.Geom):  Highlight Lines Analysis builder .
        """
        pass
    def CreateLocalRadiusAnalysisBuilder(self, lrao: LocalRadiusAnalysis) -> LocalRadiusAnalysisBuilder:
        """
         Creates a NXOpen.GeometricAnalysis.LocalRadiusAnalysisBuilder 
         Returns builder ( LocalRadiusAnalysisBuilder NXOpen.Geom): .
        """
        pass
    def CreateSectionAnalysisBuilder(self, msao_object: SectionAnalysisObject) -> NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder:
        """
         Creates a Section Analysis object builder 
         Returns msao_builder ( NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder):  Section Analysis builder .
        """
        pass
    def CreateSectionAnalysisExBuilder(self, csao_object: NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExObject) -> NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder:
        """
         Creates a Section Analysis builder of a new version
         Returns csao_builder ( NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder):  Section Analysis builder .
        """
        pass
    def CreateSurfaceContinuityAnalysisBuilder(self, scao_object: NXOpen.DisplayableObject) -> SurfaceContinuityAnalysisBuilder:
        """
         Creates a surface continuity analysis builder 
         Returns scao_builder ( SurfaceContinuityAnalysisBuilder NXOpen.Geom):  Surface Continuity Analysis builder .
        """
        pass
    def CreateSurfaceIntersectionBuilder(self, siao_object: NXOpen.DisplayableObject) -> SurfaceIntersectionBuilder:
        """
         Creates a surface intersection  builder 
         Returns siao_builder ( SurfaceIntersectionBuilder NXOpen.Geom):  surface intersection builder .
        """
        pass
import NXOpen
class AnalysisObject(NXOpen.DisplayableObject): 
    """ Represents an Analysis Object   """
    pass
import NXOpen
import NXOpen.Validate
class AnalysisResultCollection(NXOpen.TaggedObjectCollection): 
    """
     Represents an NX NXOpen.GeometricAnalysis.AnalysisResultCollection object.
    """
    def CreateContactAnalysisBuilder(self, persistentResult: NXOpen.Validate.AnalysisResult) -> ContactAnalysisBuilder:
        """
         Creates a contact analysis builder. 
         Returns contactBuilder ( ContactAnalysisBuilder NXOpen.Geom): .
        """
        pass
    def CreateContactAnalysisSectionCurveBuilder(self, view: NXOpen.ModelingView, contactAnalysisBuilder: ContactAnalysisBuilder) -> ContactAnalysisSectionCurveBuilder:
        """
         Creates a contact analysis Section Curve builder. 
         Returns contactAnalysisSectionCurveBuilder ( ContactAnalysisSectionCurveBuilder NXOpen.Geom): .
        """
        pass
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
class ContactAnalysisBuilder(NXOpen.Builder): 
    """ Represents a Contact Analysis builder. 
        The Contact analysis will be performed on selected Sheet or Solid Bodies.
        And the Radius Analysis will be carried out on the ball touching areas
        The Output for the Contact Analysis will be Areas Touched by Ball and Areas Not Touched by ball 
        The Output for radius Analysis will be Sharp Areas, Intermediate areas and Smooth areas
        Also The results can be modulated for different resolutions"""
    @property
    def AreasNotTouchedByBall(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) AreasNotTouchedByBall
         Returns the Color for Areas Not Touched by Ball of Given Ball Diameter   
            
         
        """
        pass
    @AreasNotTouchedByBall.setter
    def AreasNotTouchedByBall(self, areasNotTouchedByBall: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) AreasNotTouchedByBall
         Returns the Color for Areas Not Touched by Ball of Given Ball Diameter   
            
         
        """
        pass
    @property
    def AreasTouchedByBall(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) AreasTouchedByBall
         Returns the Color for Areas Touched by Ball of Given Ball Diameter   
            
         
        """
        pass
    @AreasTouchedByBall.setter
    def AreasTouchedByBall(self, areasTouchedByBall: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) AreasTouchedByBall
         Returns the Color for Areas Touched by Ball of Given Ball Diameter   
            
         
        """
        pass
    @property
    def AutomaticUpdate(self) -> bool:
        """
        Getter for property: (bool) AutomaticUpdate
         Returns the toggle that automatic update   
            
         
        """
        pass
    @AutomaticUpdate.setter
    def AutomaticUpdate(self, automaticUpdate: bool):
        """
        Setter for property: (bool) AutomaticUpdate
         Returns the toggle that automatic update   
            
         
        """
        pass
    @property
    def BallDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BallDiameter
         Returns the Ball Diameter for Ball Contact Analysis   
            
         
        """
        pass
    @property
    def BodySelection(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BodySelection
         Returns the body selection on which the Contact analysis and Radius Analysis will be carried out  
            
         
        """
        pass
    @property
    def CreateMinRadiusPoints(self) -> bool:
        """
        Getter for property: (bool) CreateMinRadiusPoints
         Returns the toggle to Create and label the minimum radius point from all the sharp regions    
            
         
        """
        pass
    @CreateMinRadiusPoints.setter
    def CreateMinRadiusPoints(self, createMinRadiusPoints: bool):
        """
        Setter for property: (bool) CreateMinRadiusPoints
         Returns the toggle to Create and label the minimum radius point from all the sharp regions    
            
         
        """
        pass
    @property
    def CreatePointsAtStepDist(self) -> bool:
        """
        Getter for property: (bool) CreatePointsAtStepDist
         Returns the toggle to create equidistant points at given step distance    
            
         
        """
        pass
    @CreatePointsAtStepDist.setter
    def CreatePointsAtStepDist(self, createPointsAtStepDist: bool):
        """
        Setter for property: (bool) CreatePointsAtStepDist
         Returns the toggle to create equidistant points at given step distance    
            
         
        """
        pass
    @property
    def DisplayContourCurves(self) -> bool:
        """
        Getter for property: (bool) DisplayContourCurves
         Returns the toggle to Display Contour Curves   
            
         
        """
        pass
    @DisplayContourCurves.setter
    def DisplayContourCurves(self, displayContourCurves: bool):
        """
        Setter for property: (bool) DisplayContourCurves
         Returns the toggle to Display Contour Curves   
            
         
        """
        pass
    @property
    def DisplayResolution(self) -> NXOpen.GeometricUtilities.DisplayResolutionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.DisplayResolutionBuilder) DisplayResolution
         Returns the disp resolution will decide the fineness of faceting triangles   
            
         
        """
        pass
    @property
    def EnableRadiusAnalysis(self) -> bool:
        """
        Getter for property: (bool) EnableRadiusAnalysis
         Returns the toggle that enables radius analysis   
            
         
        """
        pass
    @EnableRadiusAnalysis.setter
    def EnableRadiusAnalysis(self, enableRadiusAnalysis: bool):
        """
        Setter for property: (bool) EnableRadiusAnalysis
         Returns the toggle that enables radius analysis   
            
         
        """
        pass
    @property
    def ExternalBallDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ExternalBallDiameter
         Returns the External Ball Diameter for Fold Measurement Analysis    
            
         
        """
        pass
    @property
    def GeometricConstraintDataManager(self) -> NXOpen.Features.GeometricConstraintDataManager:
        """
        Getter for property: ( NXOpen.Features.GeometricConstraintDataManager) GeometricConstraintDataManager
         Returns the Geometric Constraint Data Manager builder  
            
         
        """
        pass
    @property
    def HemishpericalBallDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) HemishpericalBallDiameter
         Returns the Hemispherical Ball Diameter for Ram Apparatus Analysis     
            
         
        """
        pass
    @property
    def IntermediateAreas(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) IntermediateAreas
         Returns the Color for Areas Where the Radius is Between Minimum Radius and Maximum Radius    
            
         
        """
        pass
    @IntermediateAreas.setter
    def IntermediateAreas(self, intermediateAreas: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) IntermediateAreas
         Returns the Color for Areas Where the Radius is Between Minimum Radius and Maximum Radius    
            
         
        """
        pass
    @property
    def InternalBallDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InternalBallDiameter
         Returns the Internal Ball Diameter for Fold Measurement Analysis   
            
         
        """
        pass
    @property
    def MaximumRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumRadius
         Returns the maximum radius is Threshold for smooth areas
                    Areas exceeding this threshold are considered as smooth areas   
            
         
        """
        pass
    @property
    def MinimumRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumRadius
         Returns the minimum radius is Threshold for smooth areas
                    Areas having less radius than this threshold are considered as Sharp Areas.  
             
         
        """
        pass
    @property
    def Normals(self) -> FaceAnalysisNormalsBuilder:
        """
        Getter for property: ( FaceAnalysisNormalsBuilder NXOpen.Geom) Normals
         Returns the Contact analysis normals.  
             
         
        """
        pass
    @property
    def ProtrusionLimit(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ProtrusionLimit
         Returns the protrusion limit is Threshold for Ram Apparatus Analysis and Fold Measurement Analysis   
            
         
        """
        pass
    @property
    def RamDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RamDiameter
         Returns the Ram Diameter for Ram Apparatus Analysis   
            
         
        """
        pass
    @property
    def SharpAreas(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) SharpAreas
         Returns the color for Sharp Areas Where the Radius is Less than Minimum Radius    
            
         
        """
        pass
    @SharpAreas.setter
    def SharpAreas(self, sharpAreas: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) SharpAreas
         Returns the color for Sharp Areas Where the Radius is Less than Minimum Radius    
            
         
        """
        pass
    @property
    def ShowOnlyContactAnalysisAreas(self) -> bool:
        """
        Getter for property: (bool) ShowOnlyContactAnalysisAreas
         Returns the toggle to Show only Ball touching Areas   
            
         
        """
        pass
    @ShowOnlyContactAnalysisAreas.setter
    def ShowOnlyContactAnalysisAreas(self, showOnlyContactAnalysisAreas: bool):
        """
        Setter for property: (bool) ShowOnlyContactAnalysisAreas
         Returns the toggle to Show only Ball touching Areas   
            
         
        """
        pass
    @property
    def ShowOnlySharpAreas(self) -> bool:
        """
        Getter for property: (bool) ShowOnlySharpAreas
         Returns the toggle that enables show only sharp areas
                    the Radius Analysis will be performed on the Ball touching Areas   
            
         
        """
        pass
    @ShowOnlySharpAreas.setter
    def ShowOnlySharpAreas(self, showOnlySharpAreas: bool):
        """
        Setter for property: (bool) ShowOnlySharpAreas
         Returns the toggle that enables show only sharp areas
                    the Radius Analysis will be performed on the Ball touching Areas   
            
         
        """
        pass
    @property
    def SmoothAreas(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) SmoothAreas
         Returns the Color for Smooth Areas Where the Radius is Less Than Minimum Radius   
            
         
        """
        pass
    @SmoothAreas.setter
    def SmoothAreas(self, smoothAreas: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) SmoothAreas
         Returns the Color for Smooth Areas Where the Radius is Less Than Minimum Radius   
            
         
        """
        pass
    @property
    def StepDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StepDistance
         Returns the step distance to Create equidistant points on selected bodies   
            
         
        """
        pass
    def AddGCPoint(self, face: NXOpen.Face, point: NXOpen.Point) -> None:
        """
         Add geometric constraint point to checker 
        """
        pass
    def ClearGConstraintPointData(self) -> None:
        """
         Clear geometric constraint points from checker 
        """
        pass
    def CreateCheckPoints(self) -> None:
        """
         Create Check Points 
        """
        pass
    def CreateSectionCurves(self) -> ContactAnalysisSectionCurveBuilder:
        """
         Create Section Curves 
         Returns sectionCurveBuilder ( ContactAnalysisSectionCurveBuilder NXOpen.Geom): .
        """
        pass
    def DeleteGCPoint(self, point: NXOpen.Point) -> None:
        """
         Delete geometric constraint point from checker 
        """
        pass
    def SaveContourCurves(self) -> None:
        """
         Create Save Contour Curves 
        """
        pass
    def SetGCPoint(self, face: NXOpen.Face, point: NXOpen.Point) -> None:
        """
         Set geometric constraint point to checker 
        """
        pass
    def Update(self) -> None:
        """
         Update the checker 
        """
        pass
import NXOpen.Validate
class ContactAnalysisResult(NXOpen.Validate.AnalysisResult): 
    """
     Represents an NX NXOpen.GeometricAnalysis.ContactAnalysisResult object.
    """
    pass
import NXOpen
import NXOpen.Display
class ContactAnalysisSectionCurveBuilder(NXOpen.Display.DynamicSectionBuilder): 
    """ Represents Section Curve Builder in Contact Analysis
    After Contact Analysis to visualize how the analysis is performed at certain point Section curves is used
    User can select a point, A ball is placed at the selected point.
    The plane of the section is constructed from selected point, sphere center and the plane of minimum radius at that point
    the section curves and section preview is displayed
    Section Curves can be saved"""
    @property
    def BallDiameter(self) -> float:
        """
        Getter for property: (float) BallDiameter
         Returns the Ball diameter of contact Analysis  
            
         
        """
        pass
    @BallDiameter.setter
    def BallDiameter(self, ballDiameter: float):
        """
        Setter for property: (float) BallDiameter
         Returns the Ball diameter of contact Analysis  
            
         
        """
        pass
    @property
    def DisplaySlice(self) -> bool:
        """
        Getter for property: (bool) DisplaySlice
         Returns the toggle to display section view i.  
          e. slice  
         
        """
        pass
    @DisplaySlice.setter
    def DisplaySlice(self, displaySlice: bool):
        """
        Setter for property: (bool) DisplaySlice
         Returns the toggle to display section view i.  
          e. slice  
         
        """
        pass
    @property
    def PointToPlaceSphere(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) PointToPlaceSphere
         Returns the point to place sphere 
                    This points should be only on faces of selected bodies for Contact Analysis  
            
         
        """
        pass
    @PointToPlaceSphere.setter
    def PointToPlaceSphere(self, pointToPlaceSphere: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) PointToPlaceSphere
         Returns the point to place sphere 
                    This points should be only on faces of selected bodies for Contact Analysis  
            
         
        """
        pass
    @property
    def SectionBoundary(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SectionBoundary
         Returns the range of circle up to which the Section curves will be trimmed   
            
         
        """
        pass
    @property
    def SectionCurveColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) SectionCurveColor
         Returns the Color for Section Curves   
            
         
        """
        pass
    @SectionCurveColor.setter
    def SectionCurveColor(self, curveColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) SectionCurveColor
         Returns the Color for Section Curves   
            
         
        """
        pass
    def OrientToPlane(self) -> None:
        """
         Rotate the view to the section plane 
        """
        pass
import NXOpen
class CurveAnalysisDisplay(NXOpen.Object): 
    """ Represents a tool to control whether to show a curve's poles,knots,combs,peaks and inflections """
    class ShowFlagType(Enum):
        """
        Members Include: 
         |Pole|  show pole   
         |Comb|  show comb 
         |Inflection|  show inflection 
         |Peak|  show peak      
         |Knot|  show knot      
         |Endpoint|  show endpoint  

        """
        Pole: int
        Comb: int
        Inflection: int
        Peak: int
        Knot: int
        Endpoint: int
        @staticmethod
        def ValueOf(value: int) -> CurveAnalysisDisplay.ShowFlagType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetAnalysisRecord(self, curve: NXOpen.Curve) -> CurveAnalysisRecord:
        """
         Gets analysis record 
         Returns record ( CurveAnalysisRecord NXOpen.Geom):  curve analysis record .
        """
        pass
    def GetShowEndPoints(self, curve: NXOpen.Curve) -> bool:
        """
         Gets a flag representing end points display state of a curve
         Returns show (bool):  .
        """
        pass
    def GetShowKnot(self, curve: NXOpen.Curve) -> bool:
        """
         Gets a flag representing knots display state of a b-spline curve
         Returns show (bool):  .
        """
        pass
    def GetShowPole(self, curve: NXOpen.Curve) -> bool:
        """
         Gets a flag representing poles display state of a b-spline curve
         Returns show (bool):  .
        """
        pass
    def NewRecord(self) -> CurveAnalysisRecord:
        """
         Creats a curve analysis record 
         Returns record ( CurveAnalysisRecord NXOpen.Geom): .
        """
        pass
    def SetAnalysisRecord(self, curve: NXOpen.Curve, record: CurveAnalysisRecord) -> None:
        """
         Sets analysis record 
        """
        pass
    def SetShowEndPoints(self, curve: NXOpen.Curve, show: bool) -> None:
        """
         Sets a flag representing end points display state of a curve
        """
        pass
    def SetShowFlag(self, curve: NXOpen.Curve, choice: CurveAnalysisDisplay.ShowFlagType, on: bool) -> None:
        """
         Sets show flags 
        """
        pass
    def SetShowKnot(self, curve: NXOpen.Curve, show: bool) -> None:
        """
         Sets a flag representing knots display state of a b-spline curve
        """
        pass
    def SetShowPole(self, curve: NXOpen.Curve, show: bool) -> None:
        """
         Sets a flag representing poles display state of a b-spline curve 
        """
        pass
    def ShowCurveEndPoints(self, curves: List[NXOpen.Curve], show: bool) -> None:
        """
         Shows or hides end points display of curves
        """
        pass
import NXOpen
class CurveAnalysisRecord(NXOpen.TransientObject): 
    """ Represents the information regarding how to display a curve's poles, knots, combs, peaks and inflections """
    class DirectionOptionType(Enum):
        """
        Members Include: 
         |NotSet|  no direction   
         |PlaneOfCurve|  best fit plane 
         |SpecifyVector|  specify vector 
         |WorkView|  work view      

        """
        NotSet: int
        PlaneOfCurve: int
        SpecifyVector: int
        WorkView: int
        @staticmethod
        def ValueOf(value: int) -> CurveAnalysisRecord.DirectionOptionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CombDensity(self) -> int:
        """
        Getter for property: (int) CombDensity
         Returns the comb density   
            
         
        """
        pass
    @CombDensity.setter
    def CombDensity(self, density: int):
        """
        Setter for property: (int) CombDensity
         Returns the comb density   
            
         
        """
        pass
    @property
    def CombInterneedleDensity(self) -> int:
        """
        Getter for property: (int) CombInterneedleDensity
         Returns the comb interneedle density   
            
         
        """
        pass
    @CombInterneedleDensity.setter
    def CombInterneedleDensity(self, interneedle_density: int):
        """
        Setter for property: (int) CombInterneedleDensity
         Returns the comb interneedle density   
            
         
        """
        pass
    @property
    def CombMaxLength(self) -> float:
        """
        Getter for property: (float) CombMaxLength
         Returns the comb maximum length   
            
         
        """
        pass
    @CombMaxLength.setter
    def CombMaxLength(self, max_length: float):
        """
        Setter for property: (float) CombMaxLength
         Returns the comb maximum length   
            
         
        """
        pass
    @property
    def CombScaleFactor(self) -> float:
        """
        Getter for property: (float) CombScaleFactor
         Returns the comb scale factor   
            
         
        """
        pass
    @CombScaleFactor.setter
    def CombScaleFactor(self, factor: float):
        """
        Setter for property: (float) CombScaleFactor
         Returns the comb scale factor   
            
         
        """
        pass
    @property
    def Direction(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) Direction
         Returns the diection   
            
         
        """
        pass
    @Direction.setter
    def Direction(self, direction: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) Direction
         Returns the diection   
            
         
        """
        pass
    @property
    def DirectionOption(self) -> CurveAnalysisRecord.DirectionOptionType:
        """
        Getter for property: ( CurveAnalysisRecord.DirectionOptionType NXOpen.Geom) DirectionOption
         Returns the direction option   
            
         
        """
        pass
    @DirectionOption.setter
    def DirectionOption(self, direction_option: CurveAnalysisRecord.DirectionOptionType):
        """
        Setter for property: ( CurveAnalysisRecord.DirectionOptionType NXOpen.Geom) DirectionOption
         Returns the direction option   
            
         
        """
        pass
    @property
    def End(self) -> float:
        """
        Getter for property: (float) End
         Returns the end parameter   
            
         
        """
        pass
    @End.setter
    def End(self, end: float):
        """
        Setter for property: (float) End
         Returns the end parameter   
            
         
        """
        pass
    @property
    def ShowComb(self) -> bool:
        """
        Getter for property: (bool) ShowComb
         Returns the flag to show comb   
            
         
        """
        pass
    @ShowComb.setter
    def ShowComb(self, on: bool):
        """
        Setter for property: (bool) ShowComb
         Returns the flag to show comb   
            
         
        """
        pass
    @property
    def ShowInflection(self) -> bool:
        """
        Getter for property: (bool) ShowInflection
         Returns the flag to show inflection   
            
         
        """
        pass
    @ShowInflection.setter
    def ShowInflection(self, on: bool):
        """
        Setter for property: (bool) ShowInflection
         Returns the flag to show inflection   
            
         
        """
        pass
    @property
    def ShowKnot(self) -> bool:
        """
        Getter for property: (bool) ShowKnot
         Returns the flag to show knot   
            
         
        """
        pass
    @ShowKnot.setter
    def ShowKnot(self, on: bool):
        """
        Setter for property: (bool) ShowKnot
         Returns the flag to show knot   
            
         
        """
        pass
    @property
    def ShowPeak(self) -> bool:
        """
        Getter for property: (bool) ShowPeak
         Returns the flag to show peak   
            
         
        """
        pass
    @ShowPeak.setter
    def ShowPeak(self, on: bool):
        """
        Setter for property: (bool) ShowPeak
         Returns the flag to show peak   
            
         
        """
        pass
    @property
    def ShowPole(self) -> bool:
        """
        Getter for property: (bool) ShowPole
         Returns the flag to show pole   
            
         
        """
        pass
    @ShowPole.setter
    def ShowPole(self, on: bool):
        """
        Setter for property: (bool) ShowPole
         Returns the flag to show pole   
            
         
        """
        pass
    @property
    def Start(self) -> float:
        """
        Getter for property: (float) Start
         Returns the start parameter, range from 0 to 100   
            
         
        """
        pass
    @Start.setter
    def Start(self, start: float):
        """
        Setter for property: (float) Start
         Returns the start parameter, range from 0 to 100   
            
         
        """
        pass
    @property
    def UseMaxLength(self) -> bool:
        """
        Getter for property: (bool) UseMaxLength
         Returns the flag to limit the maximum length of the comb   
            
         
        """
        pass
    @UseMaxLength.setter
    def UseMaxLength(self, on: bool):
        """
        Setter for property: (bool) UseMaxLength
         Returns the flag to limit the maximum length of the comb   
            
         
        """
        pass
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. 
        """
        pass
import NXOpen
class CurveContinuityBuilder(NXOpen.Builder): 
    """ Represents a curve continuity builder """
    class Type(Enum):
        """
        Members Include: 
         |CurvetoObject|  curve to object 
         |Multicurve|  multicurve 

        """
        CurvetoObject: int
        Multicurve: int
        @staticmethod
        def ValueOf(value: int) -> CurveContinuityBuilder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngularThreshold(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) AngularThreshold
         Returns the angular threshold   
            
         
        """
        pass
    @property
    def ContinuityType(self) -> CurveContinuityBuilder.Type:
        """
        Getter for property: ( CurveContinuityBuilder.Type NXOpen.Geom) ContinuityType
         Returns the curve continuity type   
            
         
        """
        pass
    @ContinuityType.setter
    def ContinuityType(self, continuityType: CurveContinuityBuilder.Type):
        """
        Setter for property: ( CurveContinuityBuilder.Type NXOpen.Geom) ContinuityType
         Returns the curve continuity type   
            
         
        """
        pass
    @property
    def DistanceThreshold(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DistanceThreshold
         Returns the distance threshold   
            
         
        """
        pass
    @property
    def DynamicLabel(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) DynamicLabel
         Returns the location for dynamic label   
            
         
        """
        pass
    @property
    def EndPointX(self) -> float:
        """
        Getter for property: (float) EndPointX
         Returns the end point x value   
            
         
        """
        pass
    @EndPointX.setter
    def EndPointX(self, endPointX: float):
        """
        Setter for property: (float) EndPointX
         Returns the end point x value   
            
         
        """
        pass
    @property
    def EndPointY(self) -> float:
        """
        Getter for property: (float) EndPointY
         Returns the end point y value   
            
         
        """
        pass
    @EndPointY.setter
    def EndPointY(self, endPointY: float):
        """
        Setter for property: (float) EndPointY
         Returns the end point y value   
            
         
        """
        pass
    @property
    def EndPointZ(self) -> float:
        """
        Getter for property: (float) EndPointZ
         Returns the end point z value   
            
         
        """
        pass
    @EndPointZ.setter
    def EndPointZ(self, endPointZ: float):
        """
        Setter for property: (float) EndPointZ
         Returns the end point z value   
            
         
        """
        pass
    @property
    def G0Check(self) -> bool:
        """
        Getter for property: (bool) G0Check
         Returns the G0 check   
            
         
        """
        pass
    @G0Check.setter
    def G0Check(self, g0Check: bool):
        """
        Setter for property: (bool) G0Check
         Returns the G0 check   
            
         
        """
        pass
    @property
    def G0Check2(self) -> bool:
        """
        Getter for property: (bool) G0Check2
         Returns the G0 check for multicurve   
            
         
        """
        pass
    @G0Check2.setter
    def G0Check2(self, g0Check2: bool):
        """
        Setter for property: (bool) G0Check2
         Returns the G0 check for multicurve   
            
         
        """
        pass
    @property
    def G0Tolerance(self) -> float:
        """
        Getter for property: (float) G0Tolerance
         Returns the g0 tolerance   
            
         
        """
        pass
    @G0Tolerance.setter
    def G0Tolerance(self, g0Tolerance: float):
        """
        Setter for property: (float) G0Tolerance
         Returns the g0 tolerance   
            
         
        """
        pass
    @property
    def G1Check(self) -> bool:
        """
        Getter for property: (bool) G1Check
         Returns the G1 check   
            
         
        """
        pass
    @G1Check.setter
    def G1Check(self, g1Check: bool):
        """
        Setter for property: (bool) G1Check
         Returns the G1 check   
            
         
        """
        pass
    @property
    def G1Check2(self) -> bool:
        """
        Getter for property: (bool) G1Check2
         Returns the G1 check for multicurve   
            
         
        """
        pass
    @G1Check2.setter
    def G1Check2(self, g1Check2: bool):
        """
        Setter for property: (bool) G1Check2
         Returns the G1 check for multicurve   
            
         
        """
        pass
    @property
    def G1Tolerance(self) -> float:
        """
        Getter for property: (float) G1Tolerance
         Returns the g1 tolerance   
            
         
        """
        pass
    @G1Tolerance.setter
    def G1Tolerance(self, g1Tolerance: float):
        """
        Setter for property: (float) G1Tolerance
         Returns the g1 tolerance   
            
         
        """
        pass
    @property
    def G2Check(self) -> bool:
        """
        Getter for property: (bool) G2Check
         Returns the G2 check   
            
         
        """
        pass
    @G2Check.setter
    def G2Check(self, g2Check: bool):
        """
        Setter for property: (bool) G2Check
         Returns the G2 check   
            
         
        """
        pass
    @property
    def G2Check2(self) -> bool:
        """
        Getter for property: (bool) G2Check2
         Returns the G2 check for multicurve   
            
         
        """
        pass
    @G2Check2.setter
    def G2Check2(self, g2Check2: bool):
        """
        Setter for property: (bool) G2Check2
         Returns the G2 check for multicurve   
            
         
        """
        pass
    @property
    def G2Tolerance(self) -> float:
        """
        Getter for property: (float) G2Tolerance
         Returns the g2 tolerance   
            
         
        """
        pass
    @G2Tolerance.setter
    def G2Tolerance(self, g2Tolerance: float):
        """
        Setter for property: (float) G2Tolerance
         Returns the g2 tolerance   
            
         
        """
        pass
    @property
    def G3Check(self) -> bool:
        """
        Getter for property: (bool) G3Check
         Returns the G3 check   
            
         
        """
        pass
    @G3Check.setter
    def G3Check(self, g3Check: bool):
        """
        Setter for property: (bool) G3Check
         Returns the G3 check   
            
         
        """
        pass
    @property
    def G3Check2(self) -> bool:
        """
        Getter for property: (bool) G3Check2
         Returns the G3 check for multicurve   
            
         
        """
        pass
    @G3Check2.setter
    def G3Check2(self, g3Check2: bool):
        """
        Setter for property: (bool) G3Check2
         Returns the G3 check for multicurve   
            
         
        """
        pass
    @property
    def G3Tolerance(self) -> float:
        """
        Getter for property: (float) G3Tolerance
         Returns the g3 tolerance   
            
         
        """
        pass
    @G3Tolerance.setter
    def G3Tolerance(self, g3Tolerance: float):
        """
        Setter for property: (float) G3Tolerance
         Returns the g3 tolerance   
            
         
        """
        pass
    @property
    def MultiCurve(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) MultiCurve
         Returns the multiple curve   
            
         
        """
        pass
    @property
    def SelectCurve(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) SelectCurve
         Returns the select curve   
            
         
        """
        pass
    @property
    def SelectObject(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) SelectObject
         Returns the select object   
            
         
        """
        pass
    @property
    def ShowDeviation(self) -> bool:
        """
        Getter for property: (bool) ShowDeviation
         Returns the show deviation label   
            
         
        """
        pass
    @ShowDeviation.setter
    def ShowDeviation(self, showDeviation: bool):
        """
        Setter for property: (bool) ShowDeviation
         Returns the show deviation label   
            
         
        """
        pass
    @property
    def ShowMarkup(self) -> bool:
        """
        Getter for property: (bool) ShowMarkup
         Returns the show tolerance markup   
            
         
        """
        pass
    @ShowMarkup.setter
    def ShowMarkup(self, showMarkup: bool):
        """
        Setter for property: (bool) ShowMarkup
         Returns the show tolerance markup   
            
         
        """
        pass
    @property
    def ShowMaximum(self) -> bool:
        """
        Getter for property: (bool) ShowMaximum
         Returns the show maximum label   
            
         
        """
        pass
    @ShowMaximum.setter
    def ShowMaximum(self, showMaximum: bool):
        """
        Setter for property: (bool) ShowMaximum
         Returns the show maximum label   
            
         
        """
        pass
    @property
    def ShowMinimum(self) -> bool:
        """
        Getter for property: (bool) ShowMinimum
         Returns the show minimum label   
            
         
        """
        pass
    @ShowMinimum.setter
    def ShowMinimum(self, showMinimum: bool):
        """
        Setter for property: (bool) ShowMinimum
         Returns the show minimum label   
            
         
        """
        pass
    @property
    def ShowNeedle(self) -> bool:
        """
        Getter for property: (bool) ShowNeedle
         Returns the show needle   
            
         
        """
        pass
    @ShowNeedle.setter
    def ShowNeedle(self, showNeedle: bool):
        """
        Setter for property: (bool) ShowNeedle
         Returns the show needle   
            
         
        """
        pass
    @property
    def ShowOutOfTolerance(self) -> bool:
        """
        Getter for property: (bool) ShowOutOfTolerance
         Returns the show out of tolerance only   
            
         
        """
        pass
    @ShowOutOfTolerance.setter
    def ShowOutOfTolerance(self, showOutOfTolerance: bool):
        """
        Setter for property: (bool) ShowOutOfTolerance
         Returns the show out of tolerance only   
            
         
        """
        pass
    def ResetShowDeviation(self) -> None:
        """
         Prepare to toggle deviation label 
        """
        pass
class CurveContinuity(AnalysisObject): 
    """ Represents a Curve Continuity Analysis builder """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class CurveCurvatureAnalysisBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.GeometricAnalysis.CurveCurvatureAnalysis builder """
    class CalculationMethod(Enum):
        """
        Members Include: 
         |Curvature|  needle of curvature value 
         |RadiusofCurvature|  needle of radius of curvature value 

        """
        Curvature: int
        RadiusofCurvature: int
        @staticmethod
        def ValueOf(value: int) -> CurveCurvatureAnalysisBuilder.CalculationMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DisplayStyle(Enum):
        """
        Members Include: 
         |Linear|  linear needle 
         |Logarithmic|  logarithmic needle 

        """
        Linear: int
        Logarithmic: int
        @staticmethod
        def ValueOf(value: int) -> CurveCurvatureAnalysisBuilder.DisplayStyle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LabelValues(Enum):
        """
        Members Include: 
         |Curvature|  label showing curvature value 
         |RadiusofCurvature|  label showing radius of curvature value 

        """
        Curvature: int
        RadiusofCurvature: int
        @staticmethod
        def ValueOf(value: int) -> CurveCurvatureAnalysisBuilder.LabelValues:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class NeedleDirection(Enum):
        """
        Members Include: 
         |Inside|  needle pointing inside  
         |Outside|  needle pointing outside 

        """
        Inside: int
        Outside: int
        @staticmethod
        def ValueOf(value: int) -> CurveCurvatureAnalysisBuilder.NeedleDirection:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ProjectionTypes(Enum):
        """
        Members Include: 
         |NotSet|  no projection  
         |CurvePlane|  best fit plane 
         |Vector|  specify vector 
         |View|  view plane     
         |Xyz|  specify x,y,z plane 

        """
        NotSet: int
        CurvePlane: int
        Vector: int
        View: int
        Xyz: int
        @staticmethod
        def ValueOf(value: int) -> CurveCurvatureAnalysisBuilder.ProjectionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class XyzTypes(Enum):
        """
        Members Include: 
         |X|  x-axis plane 
         |Y|  y-axis plane 
         |Z|  z-axis plane 

        """
        X: int
        Y: int
        Z: int
        @staticmethod
        def ValueOf(value: int) -> CurveCurvatureAnalysisBuilder.XyzTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CombOptions(self) -> NXOpen.GeometricUtilities.CombOptionsBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.CombOptionsBuilder) CombOptions
         Returns the comb display block options   
            
         
        """
        pass
    @property
    def CombRange(self) -> NXOpen.GeometricUtilities.CurveRangeBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.CurveRangeBuilder) CombRange
         Returns the comb range   
            
         
        """
        pass
    @property
    def DynamicProjection(self) -> bool:
        """
        Getter for property: (bool) DynamicProjection
         Returns the dynamic projection   
            
         
        """
        pass
    @DynamicProjection.setter
    def DynamicProjection(self, dynamicProjection: bool):
        """
        Setter for property: (bool) DynamicProjection
         Returns the dynamic projection   
            
         
        """
        pass
    @property
    def Method(self) -> CurveCurvatureAnalysisBuilder.CalculationMethod:
        """
        Getter for property: ( CurveCurvatureAnalysisBuilder.CalculationMethod NXOpen.Geom) Method
         Returns the method   
            
         
        """
        pass
    @Method.setter
    def Method(self, method: CurveCurvatureAnalysisBuilder.CalculationMethod):
        """
        Setter for property: ( CurveCurvatureAnalysisBuilder.CalculationMethod NXOpen.Geom) Method
         Returns the method   
            
         
        """
        pass
    @property
    def Projection(self) -> CurveCurvatureAnalysisBuilder.ProjectionTypes:
        """
        Getter for property: ( CurveCurvatureAnalysisBuilder.ProjectionTypes NXOpen.Geom) Projection
         Returns the projection   
            
         
        """
        pass
    @Projection.setter
    def Projection(self, projection: CurveCurvatureAnalysisBuilder.ProjectionTypes):
        """
        Setter for property: ( CurveCurvatureAnalysisBuilder.ProjectionTypes NXOpen.Geom) Projection
         Returns the projection   
            
         
        """
        pass
    @property
    def ReverseDirection(self) -> int:
        """
        Getter for property: (int) ReverseDirection
         Returns the reverse direction   
            
         
        """
        pass
    @ReverseDirection.setter
    def ReverseDirection(self, reverseDirection: int):
        """
        Setter for property: (int) ReverseDirection
         Returns the reverse direction   
            
         
        """
        pass
    @property
    def SelectedCurves(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SelectedCurves
         Returns the selected curves andor edges   
            
         
        """
        pass
    @property
    def ShowCombs(self) -> bool:
        """
        Getter for property: (bool) ShowCombs
         Returns the show combs   
            
         
        """
        pass
    @ShowCombs.setter
    def ShowCombs(self, showCombs: bool):
        """
        Setter for property: (bool) ShowCombs
         Returns the show combs   
            
         
        """
        pass
    @property
    def ShowInflections(self) -> bool:
        """
        Getter for property: (bool) ShowInflections
         Returns the show inflections   
            
         
        """
        pass
    @ShowInflections.setter
    def ShowInflections(self, showInflections: bool):
        """
        Setter for property: (bool) ShowInflections
         Returns the show inflections   
            
         
        """
        pass
    @property
    def ShowMaxLabels(self) -> bool:
        """
        Getter for property: (bool) ShowMaxLabels
         Returns the show max labels   
            
         
        """
        pass
    @ShowMaxLabels.setter
    def ShowMaxLabels(self, showMaxLabels: bool):
        """
        Setter for property: (bool) ShowMaxLabels
         Returns the show max labels   
            
         
        """
        pass
    @property
    def ShowMinLabels(self) -> bool:
        """
        Getter for property: (bool) ShowMinLabels
         Returns the show min labels   
            
         
        """
        pass
    @ShowMinLabels.setter
    def ShowMinLabels(self, showMinLabels: bool):
        """
        Setter for property: (bool) ShowMinLabels
         Returns the show min labels   
            
         
        """
        pass
    @property
    def ShowPeaks(self) -> bool:
        """
        Getter for property: (bool) ShowPeaks
         Returns the show peaks   
            
         
        """
        pass
    @ShowPeaks.setter
    def ShowPeaks(self, showPeaks: bool):
        """
        Setter for property: (bool) ShowPeaks
         Returns the show peaks   
            
         
        """
        pass
    @property
    def Style(self) -> CurveCurvatureAnalysisBuilder.DisplayStyle:
        """
        Getter for property: ( CurveCurvatureAnalysisBuilder.DisplayStyle NXOpen.Geom) Style
         Returns the style   
            
         
        """
        pass
    @Style.setter
    def Style(self, style: CurveCurvatureAnalysisBuilder.DisplayStyle):
        """
        Setter for property: ( CurveCurvatureAnalysisBuilder.DisplayStyle NXOpen.Geom) Style
         Returns the style   
            
         
        """
        pass
    @property
    def Vector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) Vector
         Returns the vector   
            
         
        """
        pass
    @Vector.setter
    def Vector(self, vector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) Vector
         Returns the vector   
            
         
        """
        pass
    @property
    def Xyz(self) -> CurveCurvatureAnalysisBuilder.XyzTypes:
        """
        Getter for property: ( CurveCurvatureAnalysisBuilder.XyzTypes NXOpen.Geom) Xyz
         Returns the xyz   
            
         
        """
        pass
    @Xyz.setter
    def Xyz(self, xyz: CurveCurvatureAnalysisBuilder.XyzTypes):
        """
        Setter for property: ( CurveCurvatureAnalysisBuilder.XyzTypes NXOpen.Geom) Xyz
         Returns the xyz   
            
         
        """
        pass
    def CreateDumbInflectionPoints(self) -> List[NXOpen.Point]:
        """
         Create inflection points 
         Returns pointArray ( NXOpen.Point Li): .
        """
        pass
    def CreateDumbPeakPoints(self) -> List[NXOpen.Point]:
        """
         Create peak points 
         Returns pointArray ( NXOpen.Point Li): .
        """
        pass
    def GetCurveRange(self, index: int) -> NXOpen.GeometricUtilities.CurveRangeBuilder:
        """
         Returns the NXOpen.GeometricUtilities.CurveRangeBuilder object at a given index from the list 
         Returns combRange ( NXOpen.GeometricUtilities.CurveRangeBuilder): .
        """
        pass
    def GetCurveRangeListLength(self) -> int:
        """
         Get the number of NXOpen.GeometricUtilities.CurveRangeBuilder objects in the list
         Returns length (int): .
        """
        pass
    def UpdateWorkView(self) -> None:
        """
         Update work view with a given view matrix 
        """
        pass
class CurveCurvatureAnalysis(AnalysisObject): 
    """ Represents a CurveCurvatureAnalysis builder """
    pass
import NXOpen
class DeviationChecking(NXOpen.Builder): 
    """
    Represents a NXOpen.GeometricAnalysis.DeviationChecking
    """
    class DeviationOptions(Enum):
        """
        Members Include: 
         |NoDeviations|  show no
                   deviations 
         |AllDeviations|  show all
                   deviations 
         |MaximumDistance|  show
                   maximum distance deviation 
         |MinimumDistance|  show
                   minimum distance deviation 
         |MaximumAngle|  show maximum
                   angle deviation 
         |MinimumAngle|  show minimum
                   angle deviation 

        """
        NoDeviations: int
        AllDeviations: int
        MaximumDistance: int
        MinimumDistance: int
        MaximumAngle: int
        MinimumAngle: int
        @staticmethod
        def ValueOf(value: int) -> DeviationChecking.DeviationOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |CurveToCurve|  check 
                    curveedge to curveedge deviation 
         |CurveToFace|  check curveedge
                    to face deviation 
         |EdgeToFace|  check edge to face
                    deviation 
         |FaceToFace|  check face to face
                    deviation 
         |EdgeToEdge|  check edge to edge
                    deviation 

        """
        CurveToCurve: int
        CurveToFace: int
        EdgeToFace: int
        FaceToFace: int
        EdgeToEdge: int
        @staticmethod
        def ValueOf(value: int) -> DeviationChecking.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngleTolerance(self) -> float:
        """
        Getter for property: (float) AngleTolerance
         Returns the angle tolerance to be used for the deviation checking   
            
         
        """
        pass
    @AngleTolerance.setter
    def AngleTolerance(self, angleTolerance: float):
        """
        Setter for property: (float) AngleTolerance
         Returns the angle tolerance to be used for the deviation checking   
            
         
        """
        pass
    @property
    def Curve(self) -> NXOpen.SelectIBaseCurve:
        """
        Getter for property: ( NXOpen.SelectIBaseCurve) Curve
         Returns the curve  - required for the deviation checking when
                   NXOpen::GeometricAnalysis::DeviationChecking::SetType  is set to
                   NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToFace .  
           
                    
         
        """
        pass
    @property
    def DeviationOption(self) -> DeviationChecking.DeviationOptions:
        """
        Getter for property: ( DeviationChecking.DeviationOptions NXOpen.Geom) DeviationOption
         Returns the number or type of deviations to be shown for the deviation checking   
            
         
        """
        pass
    @DeviationOption.setter
    def DeviationOption(self, deviationOption: DeviationChecking.DeviationOptions):
        """
        Setter for property: ( DeviationChecking.DeviationOptions NXOpen.Geom) DeviationOption
         Returns the number or type of deviations to be shown for the deviation checking   
            
         
        """
        pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance to be used for the deviation checking   
            
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance to be used for the deviation checking   
            
         
        """
        pass
    @property
    def FaceOfFirstEdge(self) -> NXOpen.SelectIParameterizedSurface:
        """
        Getter for property: ( NXOpen.SelectIParameterizedSurface) FaceOfFirstEdge
         Returns the face associated with the first edge or edge  - required for the deviation checking when
                   NXOpen::GeometricAnalysis::DeviationChecking::SetType  is set to
                   NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToEdge 
                  or
                   NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToFace .  
           
                    
         
        """
        pass
    @property
    def FaceOfSecondEdge(self) -> NXOpen.SelectIParameterizedSurface:
        """
        Getter for property: ( NXOpen.SelectIParameterizedSurface) FaceOfSecondEdge
         Returns the face associated with the second edge  - required for the deviation checking when
                   NXOpen::GeometricAnalysis::DeviationChecking::SetType  is set to
                   NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToEdge .  
          
                    
         
        """
        pass
    @property
    def FirstCurve(self) -> NXOpen.SelectIBaseCurve:
        """
        Getter for property: ( NXOpen.SelectIBaseCurve) FirstCurve
         Returns the first curve or edge - required for the deviation checking when
                   NXOpen::GeometricAnalysis::DeviationChecking::SetType  is set to
                   NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToCurve .  
           
                    
         
        """
        pass
    @property
    def FirstEdge(self) -> NXOpen.SelectIBaseCurve:
        """
        Getter for property: ( NXOpen.SelectIBaseCurve) FirstEdge
         Returns the first edge or edge  - required for the deviation checking when
                   NXOpen::GeometricAnalysis::DeviationChecking::SetType  is set to
                   NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToEdge 
                  or
                   NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToFace .  
           
                    
         
        """
        pass
    @property
    def FirstFace(self) -> NXOpen.SelectIParameterizedSurface:
        """
        Getter for property: ( NXOpen.SelectIParameterizedSurface) FirstFace
         Returns the first face - required for the deviation checking when
                   NXOpen::GeometricAnalysis::DeviationChecking::SetType  is set to
                   NXOpen::GeometricAnalysis::DeviationChecking::TypesFaceToFace .  
           
                    
         
        """
        pass
    @property
    def NumberCheckPoints(self) -> int:
        """
        Getter for property: (int) NumberCheckPoints
         Returns the number of check points to be shown for the deviation checking  -
                  required when  NXOpen::GeometricAnalysis::DeviationChecking::SetType  is set to
                   NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToCurve 
                  or
                   NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToFace 
                  or
                   NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToFace 
                  or
                   NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToEdge .  
          
                    
         
        """
        pass
    @NumberCheckPoints.setter
    def NumberCheckPoints(self, numberCheckPoints: int):
        """
        Setter for property: (int) NumberCheckPoints
         Returns the number of check points to be shown for the deviation checking  -
                  required when  NXOpen::GeometricAnalysis::DeviationChecking::SetType  is set to
                   NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToCurve 
                  or
                   NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToFace 
                  or
                   NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToFace 
                  or
                   NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToEdge .  
          
                    
         
        """
        pass
    @property
    def NumberUcheckPoints(self) -> int:
        """
        Getter for property: (int) NumberUcheckPoints
         Returns the number of u check points to be shown for the deviation checking
                  - required when  NXOpen::GeometricAnalysis::DeviationChecking::SetType  is set to
                   NXOpen::GeometricAnalysis::DeviationChecking::TypesFaceToFace 
                    
            
         
        """
        pass
    @NumberUcheckPoints.setter
    def NumberUcheckPoints(self, numberUCheckPoints: int):
        """
        Setter for property: (int) NumberUcheckPoints
         Returns the number of u check points to be shown for the deviation checking
                  - required when  NXOpen::GeometricAnalysis::DeviationChecking::SetType  is set to
                   NXOpen::GeometricAnalysis::DeviationChecking::TypesFaceToFace 
                    
            
         
        """
        pass
    @property
    def NumberVcheckPoints(self) -> int:
        """
        Getter for property: (int) NumberVcheckPoints
         Returns the number of v check points to be shown for the deviation checking
                  - required when  NXOpen::GeometricAnalysis::DeviationChecking::SetType  is set to
                   NXOpen::GeometricAnalysis::DeviationChecking::TypesFaceToFace 
                    
            
         
        """
        pass
    @NumberVcheckPoints.setter
    def NumberVcheckPoints(self, numberVCheckPoints: int):
        """
        Setter for property: (int) NumberVcheckPoints
         Returns the number of v check points to be shown for the deviation checking
                  - required when  NXOpen::GeometricAnalysis::DeviationChecking::SetType  is set to
                   NXOpen::GeometricAnalysis::DeviationChecking::TypesFaceToFace 
                    
            
         
        """
        pass
    @property
    def SecondCurve(self) -> NXOpen.SelectIBaseCurve:
        """
        Getter for property: ( NXOpen.SelectIBaseCurve) SecondCurve
         Returns the second curve or edge - required for the deviation checking when
                   NXOpen::GeometricAnalysis::DeviationChecking::SetType  is set to
                   NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToCurve .  
           
                    
         
        """
        pass
    @property
    def SecondEdge(self) -> NXOpen.SelectIBaseCurve:
        """
        Getter for property: ( NXOpen.SelectIBaseCurve) SecondEdge
         Returns the second edge - required for the deviation checking when
                   NXOpen::GeometricAnalysis::DeviationChecking::SetType  is set to
                   NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToEdge .  
          
                    
         
        """
        pass
    @property
    def SecondFace(self) -> NXOpen.SelectIParameterizedSurface:
        """
        Getter for property: ( NXOpen.SelectIParameterizedSurface) SecondFace
         Returns the second face - required for the deviation checking when
                   NXOpen::GeometricAnalysis::DeviationChecking::SetType  is set to
                   NXOpen::GeometricAnalysis::DeviationChecking::TypesFaceToFace 
                  or the face  - required for the deviation checking when  NXOpen::GeometricAnalysis::DeviationChecking::SetType  is set to
                   NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToFace 
                  or
                   NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToFace .  
           
                    
         
        """
        pass
    @property
    def Type(self) -> DeviationChecking.Types:
        """
        Getter for property: ( DeviationChecking.Types NXOpen.Geom) Type
         Returns the deviation checking type.  
           Depending on the value of the deviation
                  checking type, different inputs are required. See the
                  documentation for each of the inputs.   
         
        """
        pass
    @Type.setter
    def Type(self, type: DeviationChecking.Types):
        """
        Setter for property: ( DeviationChecking.Types NXOpen.Geom) Type
         Returns the deviation checking type.  
           Depending on the value of the deviation
                  checking type, different inputs are required. See the
                  documentation for each of the inputs.   
         
        """
        pass
    def Check(self) -> None:
        """
         Performs deviation checking.  Before calling this method, set
                    property NXOpen.GeometricAnalysis.DeviationChecking.Type to specify the type of 
                    deviation checking, and the two objects (curvefaceedge) to be used the deviation
                    checking. The type of the objects required
                    depends on NXOpen.GeometricAnalysis.DeviationChecking.Type set above. Also set the
                    number check points to be displayed or u and v check points, the
                    distance tolerance, and the angle tolerance before calling the
                    method NXOpen.GeometricAnalysis.DeviationChecking.Check. 
                    NXOpen.GeometricAnalysis.DeviationChecking.Check displays the
                    deviation as per the specification above in the graphics and lists
                    in the information window of NX.
                    
        """
        pass
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
class DeviationGaugeBuilder(NXOpen.Builder): 
    """ DeviationGaugeBuilder class  """
    class AdditionalValuesLabelType(Enum):
        """
        Members Include: 
         |UserDefined|   User Defined  
         |Intermediate|  Intermediate  
         |All|  All  
         |NotSet|  None  

        """
        UserDefined: int
        Intermediate: int
        All: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> DeviationGaugeBuilder.AdditionalValuesLabelType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ColorPlotTypes(Enum):
        """
        Members Include: 
         |Blend|   Blend 
         |Stepped|   Stepped 
         |NotSet|   None  

        """
        Blend: int
        Stepped: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> DeviationGaugeBuilder.ColorPlotTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MeasurementMethodType(Enum):
        """
        Members Include: 
         |ThreeDim|  3D  
         |XyzDirection|  XYZ direction  
         |WorkView|  Work view     
         |VectorComponent|  Vector component    
         |Plane|  Plane   
         |AlongVector|  Along vector   

        """
        ThreeDim: int
        XyzDirection: int
        WorkView: int
        VectorComponent: int
        Plane: int
        AlongVector: int
        @staticmethod
        def ValueOf(value: int) -> DeviationGaugeBuilder.MeasurementMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MinMaxType(Enum):
        """
        Members Include: 
         |Minmax|  MinimumMaximum      
         |Minimum|  Minimum  
         |Maximum|  Maximum  
         |NotSet|  None  

        """
        Minmax: int
        Minimum: int
        Maximum: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> DeviationGaugeBuilder.MinMaxType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ReportingPerTypes(Enum):
        """
        Members Include: 
         |AnalysisObject|   Per Analysis Object 
         |Target|   Per Target Object  
         |Reference|   Per Reference Object 

        """
        AnalysisObject: int
        Target: int
        Reference: int
        @staticmethod
        def ValueOf(value: int) -> DeviationGaugeBuilder.ReportingPerTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class XyzDirectionType(Enum):
        """
        Members Include: 
         |X|  X direction 
         |Y|  Y direction 
         |Z|  Z direction 

        """
        X: int
        Y: int
        Z: int
        @staticmethod
        def ValueOf(value: int) -> DeviationGaugeBuilder.XyzDirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ColorPlotType(self) -> DeviationGaugeBuilder.ColorPlotTypes:
        """
        Getter for property: ( DeviationGaugeBuilder.ColorPlotTypes NXOpen.Geom) ColorPlotType
         Returns the color plot type   
            
         
        """
        pass
    @ColorPlotType.setter
    def ColorPlotType(self, colorPlotType: DeviationGaugeBuilder.ColorPlotTypes):
        """
        Setter for property: ( DeviationGaugeBuilder.ColorPlotTypes NXOpen.Geom) ColorPlotType
         Returns the color plot type   
            
         
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
    def CurveRangeControl(self) -> NXOpen.GeometricUtilities.CurveRangeBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.CurveRangeBuilder) CurveRangeControl
         Returns the curve range     
            
         
        """
        pass
    @property
    def DeviationIntervals(self) -> int:
        """
        Getter for property: (int) DeviationIntervals
         Returns the number of deviation intervals   
            
         
        """
        pass
    @DeviationIntervals.setter
    def DeviationIntervals(self, deviationIntervals: int):
        """
        Setter for property: (int) DeviationIntervals
         Returns the number of deviation intervals   
            
         
        """
        pass
    @property
    def HasAbsoluteColorPlot(self) -> bool:
        """
        Getter for property: (bool) HasAbsoluteColorPlot
         Returns a value indicating whether to plot using absolute value     
            
         
        """
        pass
    @HasAbsoluteColorPlot.setter
    def HasAbsoluteColorPlot(self, absoluteColorPlot: bool):
        """
        Setter for property: (bool) HasAbsoluteColorPlot
         Returns a value indicating whether to plot using absolute value     
            
         
        """
        pass
    @property
    def HasAdditionalValuesLabel(self) -> DeviationGaugeBuilder.AdditionalValuesLabelType:
        """
        Getter for property: ( DeviationGaugeBuilder.AdditionalValuesLabelType NXOpen.Geom) HasAdditionalValuesLabel
         Returns a value indicating whether to add additional values label   
            
         
        """
        pass
    @HasAdditionalValuesLabel.setter
    def HasAdditionalValuesLabel(self, additionalValuesLabel: DeviationGaugeBuilder.AdditionalValuesLabelType):
        """
        Setter for property: ( DeviationGaugeBuilder.AdditionalValuesLabelType NXOpen.Geom) HasAdditionalValuesLabel
         Returns a value indicating whether to add additional values label   
            
         
        """
        pass
    @property
    def HasCrossCurveDeviationLabel(self) -> bool:
        """
        Getter for property: (bool) HasCrossCurveDeviationLabel
         Returns a value indicating whether to display cross_curve deviation label   
            
         
        """
        pass
    @HasCrossCurveDeviationLabel.setter
    def HasCrossCurveDeviationLabel(self, crossCurveDeviationLabel: bool):
        """
        Setter for property: (bool) HasCrossCurveDeviationLabel
         Returns a value indicating whether to display cross_curve deviation label   
            
         
        """
        pass
    @property
    def HasInfoLabel(self) -> bool:
        """
        Getter for property: (bool) HasInfoLabel
         Returns a value indicating whether to enable floating info label   
            
         
        """
        pass
    @HasInfoLabel.setter
    def HasInfoLabel(self, infoLabel: bool):
        """
        Setter for property: (bool) HasInfoLabel
         Returns a value indicating whether to enable floating info label   
            
         
        """
        pass
    @property
    def HasInnerToleranceLabel(self) -> bool:
        """
        Getter for property: (bool) HasInnerToleranceLabel
         Returns a value indicating whether to display inner tolerance label   
            
         
        """
        pass
    @HasInnerToleranceLabel.setter
    def HasInnerToleranceLabel(self, innerToleranceLabel: bool):
        """
        Setter for property: (bool) HasInnerToleranceLabel
         Returns a value indicating whether to display inner tolerance label   
            
         
        """
        pass
    @property
    def HasMaximumValueLabel(self) -> bool:
        """
        Getter for property: (bool) HasMaximumValueLabel
         Returns a value indicating whether to display maximum value label   
            
         
        """
        pass
    @HasMaximumValueLabel.setter
    def HasMaximumValueLabel(self, maximumValueLabel: bool):
        """
        Setter for property: (bool) HasMaximumValueLabel
         Returns a value indicating whether to display maximum value label   
            
         
        """
        pass
    @property
    def HasMinimumValueLabel(self) -> bool:
        """
        Getter for property: (bool) HasMinimumValueLabel
         Returns a value indicating whether to display minimum value label   
            
         
        """
        pass
    @HasMinimumValueLabel.setter
    def HasMinimumValueLabel(self, minimumValueLabel: bool):
        """
        Setter for property: (bool) HasMinimumValueLabel
         Returns a value indicating whether to display minimum value label   
            
         
        """
        pass
    @property
    def InnerTolerance(self) -> float:
        """
        Getter for property: (float) InnerTolerance
         Returns the inner tolerance   
            
         
        """
        pass
    @InnerTolerance.setter
    def InnerTolerance(self, innerTolerance: float):
        """
        Setter for property: (float) InnerTolerance
         Returns the inner tolerance   
            
         
        """
        pass
    @property
    def IsColorMapDisplayed(self) -> bool:
        """
        Getter for property: (bool) IsColorMapDisplayed
         Returns a value indicating whether to display color map    
            
         
        """
        pass
    @IsColorMapDisplayed.setter
    def IsColorMapDisplayed(self, isColorMapDisplayed: bool):
        """
        Setter for property: (bool) IsColorMapDisplayed
         Returns a value indicating whether to display color map    
            
         
        """
        pass
    @property
    def IsDirectionReversed(self) -> bool:
        """
        Getter for property: (bool) IsDirectionReversed
         Returns a value indicating whether to reverse the direction   
            
         
        """
        pass
    @IsDirectionReversed.setter
    def IsDirectionReversed(self, reverseDirection: bool):
        """
        Setter for property: (bool) IsDirectionReversed
         Returns a value indicating whether to reverse the direction   
            
         
        """
        pass
    @property
    def IsLabelDisplayed(self) -> bool:
        """
        Getter for property: (bool) IsLabelDisplayed
         Returns  a value indicating whether to display label     
            
         
        """
        pass
    @IsLabelDisplayed.setter
    def IsLabelDisplayed(self, labelDisplayed: bool):
        """
        Setter for property: (bool) IsLabelDisplayed
         Returns  a value indicating whether to display label     
            
         
        """
        pass
    @property
    def IsMarkerDisplayed(self) -> bool:
        """
        Getter for property: (bool) IsMarkerDisplayed
         Returns a value indicating whether to display marker    
            
         
        """
        pass
    @IsMarkerDisplayed.setter
    def IsMarkerDisplayed(self, isMarkerDisplayed: bool):
        """
        Setter for property: (bool) IsMarkerDisplayed
         Returns a value indicating whether to display marker    
            
         
        """
        pass
    @property
    def IsNeedlePlotDisplayed(self) -> bool:
        """
        Getter for property: (bool) IsNeedlePlotDisplayed
         Returns a value indicating whether to display needle plot    
            
         
        """
        pass
    @IsNeedlePlotDisplayed.setter
    def IsNeedlePlotDisplayed(self, isNeedlePlotDisplayed: bool):
        """
        Setter for property: (bool) IsNeedlePlotDisplayed
         Returns a value indicating whether to display needle plot    
            
         
        """
        pass
    @property
    def MaxCheckingAngle(self) -> float:
        """
        Getter for property: (float) MaxCheckingAngle
         Returns the maximum checking angle   
            
         
        """
        pass
    @MaxCheckingAngle.setter
    def MaxCheckingAngle(self, maxCheckingAngle: float):
        """
        Setter for property: (float) MaxCheckingAngle
         Returns the maximum checking angle   
            
         
        """
        pass
    @property
    def MaxCheckingDistance(self) -> float:
        """
        Getter for property: (float) MaxCheckingDistance
         Returns the maximum checking distance   
            
         
        """
        pass
    @MaxCheckingDistance.setter
    def MaxCheckingDistance(self, maxCheckingDistance: float):
        """
        Setter for property: (float) MaxCheckingDistance
         Returns the maximum checking distance   
            
         
        """
        pass
    @property
    def MeasurementMethod(self) -> DeviationGaugeBuilder.MeasurementMethodType:
        """
        Getter for property: ( DeviationGaugeBuilder.MeasurementMethodType NXOpen.Geom) MeasurementMethod
         Returns the measurement method   
            
         
        """
        pass
    @MeasurementMethod.setter
    def MeasurementMethod(self, measurementMethod: DeviationGaugeBuilder.MeasurementMethodType):
        """
        Setter for property: ( DeviationGaugeBuilder.MeasurementMethodType NXOpen.Geom) MeasurementMethod
         Returns the measurement method   
            
         
        """
        pass
    @property
    def MeasurementSamples(self) -> int:
        """
        Getter for property: (int) MeasurementSamples
         Returns the number of measurement samples   
            
         
        """
        pass
    @MeasurementSamples.setter
    def MeasurementSamples(self, measurementSamples: int):
        """
        Setter for property: (int) MeasurementSamples
         Returns the number of measurement samples   
            
         
        """
        pass
    @property
    def MinMaxOption(self) -> DeviationGaugeBuilder.MinMaxType:
        """
        Getter for property: ( DeviationGaugeBuilder.MinMaxType NXOpen.Geom) MinMaxOption
         Returns the min_max type   
            
         
        """
        pass
    @MinMaxOption.setter
    def MinMaxOption(self, minMax: DeviationGaugeBuilder.MinMaxType):
        """
        Setter for property: ( DeviationGaugeBuilder.MinMaxType NXOpen.Geom) MinMaxOption
         Returns the min_max type   
            
         
        """
        pass
    @property
    def NeedleScale(self) -> float:
        """
        Getter for property: (float) NeedleScale
         Returns the needle scale   
            
         
        """
        pass
    @NeedleScale.setter
    def NeedleScale(self, needleScale: float):
        """
        Setter for property: (float) NeedleScale
         Returns the needle scale   
            
         
        """
        pass
    @property
    def NegativeInnerTolerance(self) -> float:
        """
        Getter for property: (float) NegativeInnerTolerance
         Returns the negative inner tolerance   
            
         
        """
        pass
    @NegativeInnerTolerance.setter
    def NegativeInnerTolerance(self, negativennerTolerance: float):
        """
        Setter for property: (float) NegativeInnerTolerance
         Returns the negative inner tolerance   
            
         
        """
        pass
    @property
    def NegativeOuterTolerance(self) -> float:
        """
        Getter for property: (float) NegativeOuterTolerance
         Returns the negative outer tolerance   
            
         
        """
        pass
    @NegativeOuterTolerance.setter
    def NegativeOuterTolerance(self, negativeOuterTolerance: float):
        """
        Setter for property: (float) NegativeOuterTolerance
         Returns the negative outer tolerance   
            
         
        """
        pass
    @property
    def OuterTolerance(self) -> float:
        """
        Getter for property: (float) OuterTolerance
         Returns the outer tolerance   
            
         
        """
        pass
    @OuterTolerance.setter
    def OuterTolerance(self, outerTolerance: float):
        """
        Setter for property: (float) OuterTolerance
         Returns the outer tolerance   
            
         
        """
        pass
    @property
    def Plane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) Plane
         Returns the plane for measurement direction   
            
         
        """
        pass
    @Plane.setter
    def Plane(self, plane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) Plane
         Returns the plane for measurement direction   
            
         
        """
        pass
    @property
    def PositiveInnerTolerance(self) -> float:
        """
        Getter for property: (float) PositiveInnerTolerance
         Returns the positive inner tolerance   
            
         
        """
        pass
    @PositiveInnerTolerance.setter
    def PositiveInnerTolerance(self, positiveInnerTolerance: float):
        """
        Setter for property: (float) PositiveInnerTolerance
         Returns the positive inner tolerance   
            
         
        """
        pass
    @property
    def PositiveOuterTolerance(self) -> float:
        """
        Getter for property: (float) PositiveOuterTolerance
         Returns the positive outer tolerance   
            
         
        """
        pass
    @PositiveOuterTolerance.setter
    def PositiveOuterTolerance(self, positiveOuterTolerance: float):
        """
        Setter for property: (float) PositiveOuterTolerance
         Returns the positive outer tolerance   
            
         
        """
        pass
    @property
    def ReferenceObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) ReferenceObjects
         Returns the reference object   
            
         
        """
        pass
    @property
    def ReportingPerType(self) -> DeviationGaugeBuilder.ReportingPerTypes:
        """
        Getter for property: ( DeviationGaugeBuilder.ReportingPerTypes NXOpen.Geom) ReportingPerType
         Returns the reporting per option   
            
         
        """
        pass
    @ReportingPerType.setter
    def ReportingPerType(self, reportingPerType: DeviationGaugeBuilder.ReportingPerTypes):
        """
        Setter for property: ( DeviationGaugeBuilder.ReportingPerTypes NXOpen.Geom) ReportingPerType
         Returns the reporting per option   
            
         
        """
        pass
    @property
    def SpatialResolution(self) -> float:
        """
        Getter for property: (float) SpatialResolution
         Returns the maximum checking angle   
            
         
        """
        pass
    @SpatialResolution.setter
    def SpatialResolution(self, spatialResolution: float):
        """
        Setter for property: (float) SpatialResolution
         Returns the maximum checking angle   
            
         
        """
        pass
    @property
    def SuggestScaleFactor(self) -> bool:
        """
        Getter for property: (bool) SuggestScaleFactor
         Returns a value indicating whether to use automatic scale factor   
            
         
        """
        pass
    @SuggestScaleFactor.setter
    def SuggestScaleFactor(self, suggestScaleFactor: bool):
        """
        Setter for property: (bool) SuggestScaleFactor
         Returns a value indicating whether to use automatic scale factor   
            
         
        """
        pass
    @property
    def SurfaceRangeControl(self) -> NXOpen.GeometricUtilities.SurfaceRangeBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.SurfaceRangeBuilder) SurfaceRangeControl
         Returns the surface range     
            
         
        """
        pass
    @property
    def TargetObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) TargetObjects
         Returns the target object   
            
         
        """
        pass
    @property
    def UseDefiningPoints(self) -> bool:
        """
        Getter for property: (bool) UseDefiningPoints
         Returns  a value indicating whether to use defining points.  
           Available only if target is curve with defining points     
         
        """
        pass
    @UseDefiningPoints.setter
    def UseDefiningPoints(self, useDefiningPoints: bool):
        """
        Setter for property: (bool) UseDefiningPoints
         Returns  a value indicating whether to use defining points.  
           Available only if target is curve with defining points     
         
        """
        pass
    @property
    def VectorComponentDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) VectorComponentDirection
         Returns the direction vector.  
           Not used if the measurement method is ThreeDim or Plane   
         
        """
        pass
    @VectorComponentDirection.setter
    def VectorComponentDirection(self, vectorComponentDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) VectorComponentDirection
         Returns the direction vector.  
           Not used if the measurement method is ThreeDim or Plane   
         
        """
        pass
    @property
    def XyzDirection(self) -> DeviationGaugeBuilder.XyzDirectionType:
        """
        Getter for property: ( DeviationGaugeBuilder.XyzDirectionType NXOpen.Geom) XyzDirection
         Returns the xyz direction   
            
         
        """
        pass
    @XyzDirection.setter
    def XyzDirection(self, xyzDirection: DeviationGaugeBuilder.XyzDirectionType):
        """
        Setter for property: ( DeviationGaugeBuilder.XyzDirectionType NXOpen.Geom) XyzDirection
         Returns the xyz direction   
            
         
        """
        pass
    def AddDynamicPoints(self) -> None:
        """
         Adds dynamic points to the Deviation Gauge. 
        """
        pass
    def AddPMILabel(self, snappedObject: NXOpen.NXObject) -> None:
        """
         Add a PMI label in specified position to represent the deviation value. 
        """
        pass
class DeviationGauge(AnalysisObject): 
    """ Deviation Gauge analysis object class """
    pass
import NXOpen
import NXOpen.Features
class DistanceAnalysisBuilder1(NXOpen.Builder): 
    """ Represents a Distance Analysis builder. """
    class DisplayModes(Enum):
        """
        Members Include: 
         |Fringe|  Display in fringe. 
         |Hedgehog|  Display in hedgehog. 
         |ContourLines|  Display in contour lines. 

        """
        Fringe: int
        Hedgehog: int
        ContourLines: int
        @staticmethod
        def ValueOf(value: int) -> DistanceAnalysisBuilder1.DisplayModes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DataRange(self) -> FaceAnalysisDataRangeBuilder:
        """
        Getter for property: ( FaceAnalysisDataRangeBuilder NXOpen.Geom) DataRange
         Returns the distance analysis data range.  
             
         
        """
        pass
    @property
    def DisplayMode(self) -> DistanceAnalysisBuilder1.DisplayModes:
        """
        Getter for property: ( DistanceAnalysisBuilder1.DisplayModes NXOpen.Geom) DisplayMode
         Returns the display mode.  
             
         
        """
        pass
    @DisplayMode.setter
    def DisplayMode(self, displayMode: DistanceAnalysisBuilder1.DisplayModes):
        """
        Setter for property: ( DistanceAnalysisBuilder1.DisplayModes NXOpen.Geom) DisplayMode
         Returns the display mode.  
             
         
        """
        pass
    @property
    def DisplaySettings(self) -> FaceAnalysisDisplayBuilder:
        """
        Getter for property: ( FaceAnalysisDisplayBuilder NXOpen.Geom) DisplaySettings
         Returns the distance analysis display settings.  
             
         
        """
        pass
    @property
    def DynamicLabel(self) -> NXOpen.Features.GeometricConstraintDataManager:
        """
        Getter for property: ( NXOpen.Features.GeometricConstraintDataManager) DynamicLabel
         Returns the dynamic label   
            
         
        """
        pass
    @property
    def Faces(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) Faces
         Returns the face to apply distance analysis.  
             
         
        """
        pass
    @property
    def Normals(self) -> FaceAnalysisNormalsBuilder:
        """
        Getter for property: ( FaceAnalysisNormalsBuilder NXOpen.Geom) Normals
         Returns the distance analysis normals.  
             
         
        """
        pass
    @property
    def NumberOfContourLines(self) -> int:
        """
        Getter for property: (int) NumberOfContourLines
         Returns the number of contour lines.  
             
         
        """
        pass
    @NumberOfContourLines.setter
    def NumberOfContourLines(self, numberOfContourLines: int):
        """
        Setter for property: (int) NumberOfContourLines
         Returns the number of contour lines.  
             
         
        """
        pass
    @property
    def Plane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) Plane
         Returns the reference plane for distance analysis.  
            
         
        """
        pass
    @Plane.setter
    def Plane(self, plane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) Plane
         Returns the reference plane for distance analysis.  
            
         
        """
        pass
    @property
    def SpikeLength(self) -> float:
        """
        Getter for property: (float) SpikeLength
         Returns the spike length.  
             
         
        """
        pass
    @SpikeLength.setter
    def SpikeLength(self, spikeLength: float):
        """
        Setter for property: (float) SpikeLength
         Returns the spike length.  
             
         
        """
        pass
    def StartDistanceAnalysis(self) -> None:
        """
         Start distance analysis. 
        """
        pass
    def UpdateDisplayOnPlaneChange(self) -> None:
        """
         Update display after plane changes. 
        """
        pass
import NXOpen
import NXOpen.Features
class DistanceAnalysisBuilder(NXOpen.Builder): 
    """ Represents a Distance Analysis builder. """
    class DisplayModes(Enum):
        """
        Members Include: 
         |Fringe|  Display in fringe. 
         |Hedgehog|  Display in hedgehog. 
         |ContourLines|  Display in contour lines. 

        """
        Fringe: int
        Hedgehog: int
        ContourLines: int
        @staticmethod
        def ValueOf(value: int) -> DistanceAnalysisBuilder.DisplayModes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DataRange(self) -> FaceAnalysisDataRangeBuilder:
        """
        Getter for property: ( FaceAnalysisDataRangeBuilder NXOpen.Geom) DataRange
         Returns the distance analysis data range.  
             
         
        """
        pass
    @property
    def DisplayMode(self) -> DistanceAnalysisBuilder.DisplayModes:
        """
        Getter for property: ( DistanceAnalysisBuilder.DisplayModes NXOpen.Geom) DisplayMode
         Returns the display mode.  
             
         
        """
        pass
    @DisplayMode.setter
    def DisplayMode(self, displayMode: DistanceAnalysisBuilder.DisplayModes):
        """
        Setter for property: ( DistanceAnalysisBuilder.DisplayModes NXOpen.Geom) DisplayMode
         Returns the display mode.  
             
         
        """
        pass
    @property
    def DisplaySettings(self) -> FaceAnalysisDisplayBuilder:
        """
        Getter for property: ( FaceAnalysisDisplayBuilder NXOpen.Geom) DisplaySettings
         Returns the distance analysis display settings.  
             
         
        """
        pass
    @property
    def DynamicLabel(self) -> NXOpen.Features.GeometricConstraintDataManager:
        """
        Getter for property: ( NXOpen.Features.GeometricConstraintDataManager) DynamicLabel
         Returns the dynamic label   
            
         
        """
        pass
    @property
    def Faces(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) Faces
         Returns the face to apply distance analysis.  
             
         
        """
        pass
    @property
    def Normals(self) -> FaceAnalysisNormalsBuilder:
        """
        Getter for property: ( FaceAnalysisNormalsBuilder NXOpen.Geom) Normals
         Returns the distance analysis normals.  
             
         
        """
        pass
    @property
    def NumberOfContourLines(self) -> int:
        """
        Getter for property: (int) NumberOfContourLines
         Returns the number of contour lines.  
             
         
        """
        pass
    @NumberOfContourLines.setter
    def NumberOfContourLines(self, numberOfContourLines: int):
        """
        Setter for property: (int) NumberOfContourLines
         Returns the number of contour lines.  
             
         
        """
        pass
    @property
    def Plane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) Plane
         Returns the reference plane for distance analysis.  
            
         
        """
        pass
    @Plane.setter
    def Plane(self, plane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) Plane
         Returns the reference plane for distance analysis.  
            
         
        """
        pass
    @property
    def SpikeLength(self) -> float:
        """
        Getter for property: (float) SpikeLength
         Returns the spike length.  
             
         
        """
        pass
    @SpikeLength.setter
    def SpikeLength(self, spikeLength: float):
        """
        Setter for property: (float) SpikeLength
         Returns the spike length.  
             
         
        """
        pass
    def StartDistanceAnalysis(self) -> None:
        """
         Start distance analysis. 
        """
        pass
    def UpdateDisplayOnPlaneChange(self) -> None:
        """
         Update display after plane changes. 
        """
        pass
class DistanceAnalysis(AnalysisObject): 
    """ Represents a distance analysis  """
    pass
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
class DraftAnalysisBuilder(NXOpen.Builder): 
    """ Represents a Draft Analysis builder """
    class DrawDirection(Enum):
        """
        Members Include: 
         |Vector|  vector; 
         |Orientation|  orientation; 

        """
        Vector: int
        Orientation: int
        @staticmethod
        def ValueOf(value: int) -> DraftAnalysisBuilder.DrawDirection:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SelectOutput(Enum):
        """
        Members Include: 
         |AnalysisObject|  analysis object; 
         |Isoclines|  isoclines; 
         |Both|  analysis object and isoclines; 

        """
        AnalysisObject: int
        Isoclines: int
        Both: int
        @staticmethod
        def ValueOf(value: int) -> DraftAnalysisBuilder.SelectOutput:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CoupleLimit(self) -> bool:
        """
        Getter for property: (bool) CoupleLimit
         Returns the coupling limit   
            
         
        """
        pass
    @CoupleLimit.setter
    def CoupleLimit(self, coupleLimit: bool):
        """
        Setter for property: (bool) CoupleLimit
         Returns the coupling limit   
            
         
        """
        pass
    @property
    def CreateCSYS(self) -> bool:
        """
        Getter for property: (bool) CreateCSYS
         Returns the datum CSYS creation   
            
         
        """
        pass
    @CreateCSYS.setter
    def CreateCSYS(self, createCSYS: bool):
        """
        Setter for property: (bool) CreateCSYS
         Returns the datum CSYS creation   
            
         
        """
        pass
    @property
    def DrawOption(self) -> DraftAnalysisBuilder.DrawDirection:
        """
        Getter for property: ( DraftAnalysisBuilder.DrawDirection NXOpen.Geom) DrawOption
         Returns the draw option   
            
         
        """
        pass
    @DrawOption.setter
    def DrawOption(self, drawOption: DraftAnalysisBuilder.DrawDirection):
        """
        Setter for property: ( DraftAnalysisBuilder.DrawDirection NXOpen.Geom) DrawOption
         Returns the draw option   
            
         
        """
        pass
    @property
    def DrawOrientation(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: ( NXOpen.Matrix3x3) DrawOrientation
         Returns the draw orientation   
            
         
        """
        pass
    @DrawOrientation.setter
    def DrawOrientation(self, drawOrientation: NXOpen.Matrix3x3):
        """
        Setter for property: ( NXOpen.Matrix3x3) DrawOrientation
         Returns the draw orientation   
            
         
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
         Returns the draw vector   
            
         
        """
        pass
    @DrawVector.setter
    def DrawVector(self, drawVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) DrawVector
         Returns the draw vector   
            
         
        """
        pass
    @property
    def DynamicLabel(self) -> NXOpen.Features.GeometricConstraintDataManager:
        """
        Getter for property: ( NXOpen.Features.GeometricConstraintDataManager) DynamicLabel
         Returns the constraint manager   
            
         
        """
        pass
    @property
    def JoinIsocline(self) -> bool:
        """
        Getter for property: (bool) JoinIsocline
         Returns the joining isocline   
            
         
        """
        pass
    @JoinIsocline.setter
    def JoinIsocline(self, joinIsocline: bool):
        """
        Setter for property: (bool) JoinIsocline
         Returns the joining isocline   
            
         
        """
        pass
    @property
    def LimitAngleNegative(self) -> float:
        """
        Getter for property: (float) LimitAngleNegative
         Returns the negative limit angle   
            
         
        """
        pass
    @LimitAngleNegative.setter
    def LimitAngleNegative(self, limitAngleNeg: float):
        """
        Setter for property: (float) LimitAngleNegative
         Returns the negative limit angle   
            
         
        """
        pass
    @property
    def LimitAnglePositive(self) -> float:
        """
        Getter for property: (float) LimitAnglePositive
         Returns the positive limit angle   
            
         
        """
        pass
    @LimitAnglePositive.setter
    def LimitAnglePositive(self, limitAnglePos: float):
        """
        Setter for property: (float) LimitAnglePositive
         Returns the positive limit angle   
            
         
        """
        pass
    @property
    def OutputOption(self) -> DraftAnalysisBuilder.SelectOutput:
        """
        Getter for property: ( DraftAnalysisBuilder.SelectOutput NXOpen.Geom) OutputOption
         Returns the output option   
            
         
        """
        pass
    @OutputOption.setter
    def OutputOption(self, outputOption: DraftAnalysisBuilder.SelectOutput):
        """
        Setter for property: ( DraftAnalysisBuilder.SelectOutput NXOpen.Geom) OutputOption
         Returns the output option   
            
         
        """
        pass
    @property
    def Resolution(self) -> NXOpen.GeometricUtilities.DisplayResolutionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.DisplayResolutionBuilder) Resolution
         Returns the display resolution   
            
         
        """
        pass
    @property
    def ReverseIndividual(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: ( NXOpen.SelectDisplayableObject) ReverseIndividual
         Returns the individual face normal  
            
         
        """
        pass
    @property
    def SelectObject(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) SelectObject
         Returns the faces or facet bodies   
            
         
        """
        pass
    @property
    def ShowIsoclineNegative(self) -> bool:
        """
        Getter for property: (bool) ShowIsoclineNegative
         Returns the negative isocline   
            
         
        """
        pass
    @ShowIsoclineNegative.setter
    def ShowIsoclineNegative(self, showIsoclineNeg: bool):
        """
        Setter for property: (bool) ShowIsoclineNegative
         Returns the negative isocline   
            
         
        """
        pass
    @property
    def ShowIsoclinePositive(self) -> bool:
        """
        Getter for property: (bool) ShowIsoclinePositive
         Returns the positive isocline   
            
         
        """
        pass
    @ShowIsoclinePositive.setter
    def ShowIsoclinePositive(self, showIsoclinePos: bool):
        """
        Setter for property: (bool) ShowIsoclinePositive
         Returns the positive isocline   
            
         
        """
        pass
    @property
    def ShowPartingLine(self) -> bool:
        """
        Getter for property: (bool) ShowPartingLine
         Returns the show parting line   
            
         
        """
        pass
    @ShowPartingLine.setter
    def ShowPartingLine(self, showPartingLine: bool):
        """
        Setter for property: (bool) ShowPartingLine
         Returns the show parting line   
            
         
        """
        pass
    @property
    def SwitchDisplayMode(self) -> bool:
        """
        Getter for property: (bool) SwitchDisplayMode
         Returns the toggle to switch display mode   
            
         
        """
        pass
    @SwitchDisplayMode.setter
    def SwitchDisplayMode(self, switchDisplayMode: bool):
        """
        Setter for property: (bool) SwitchDisplayMode
         Returns the toggle to switch display mode   
            
         
        """
        pass
    @property
    def TranslucencyInsideNegative(self) -> int:
        """
        Getter for property: (int) TranslucencyInsideNegative
         Returns the negative inside translucency   
            
         
        """
        pass
    @TranslucencyInsideNegative.setter
    def TranslucencyInsideNegative(self, translucencyInsideNeg: int):
        """
        Setter for property: (int) TranslucencyInsideNegative
         Returns the negative inside translucency   
            
         
        """
        pass
    @property
    def TranslucencyInsidePositive(self) -> int:
        """
        Getter for property: (int) TranslucencyInsidePositive
         Returns the positive inside translucency   
            
         
        """
        pass
    @TranslucencyInsidePositive.setter
    def TranslucencyInsidePositive(self, translucencyInsidePos: int):
        """
        Setter for property: (int) TranslucencyInsidePositive
         Returns the positive inside translucency   
            
         
        """
        pass
    @property
    def TranslucencyOutsideNegative(self) -> int:
        """
        Getter for property: (int) TranslucencyOutsideNegative
         Returns the negative outside tanslucency   
            
         
        """
        pass
    @TranslucencyOutsideNegative.setter
    def TranslucencyOutsideNegative(self, translucencyOutsideNeg: int):
        """
        Setter for property: (int) TranslucencyOutsideNegative
         Returns the negative outside tanslucency   
            
         
        """
        pass
    @property
    def TranslucencyOutsidePositive(self) -> int:
        """
        Getter for property: (int) TranslucencyOutsidePositive
         Returns the positive outside translucenty   
            
         
        """
        pass
    @TranslucencyOutsidePositive.setter
    def TranslucencyOutsidePositive(self, translucencyOutsidePos: int):
        """
        Setter for property: (int) TranslucencyOutsidePositive
         Returns the positive outside translucenty   
            
         
        """
        pass
    def AddDynamicPoints(self) -> None:
        """
         Adds dynamic points to the draft analysis object 
        """
        pass
    def DeleteDynamicLabels(self, deletedLabels: List[bool]) -> None:
        """
         Deletes dynamic labels whose corresponding positions are set to true in the array 
        """
        pass
    def DeselectFaces(self, faces: List[NXOpen.DisplayableObject]) -> None:
        """
         Deselects faces 
        """
        pass
    def GetColorInsideNegative(self) -> List[float]:
        """
         Returns the negative inside color 
         Returns colorInsideNeg (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def GetColorInsidePositive(self) -> List[float]:
        """
         Returns the positive inside color 
         Returns colorInsidePos (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def GetColorOutsideNegative(self) -> List[float]:
        """
         Returns the negative outside color 
         Returns colorOutsideNeg (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def GetColorOutsidePositive(self) -> List[float]:
        """
         Returns the positive outside color 
         Returns colorOutsidePos (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def RemoveLabelParents(self, parents: List[NXOpen.DisplayableObject]) -> None:
        """
         Removes dynamic label parents 
        """
        pass
    def ReverseAllNormals(self) -> None:
        """
         Reverses all normals 
        """
        pass
    def ReverseNormal(self, face: NXOpen.DisplayableObject) -> None:
        """
         Reverses individual face normal 
        """
        pass
    def SetColorInsideNegative(self, colorInsideNeg: List[float]) -> None:
        """
         Sets the negative inside color 
        """
        pass
    def SetColorInsidePositive(self, colorInsidePos: List[float]) -> None:
        """
         Sets the positive inside color 
        """
        pass
    def SetColorOutsideNegative(self, colorOutsideNeg: List[float]) -> None:
        """
         Sets the negative outside color 
        """
        pass
    def SetColorOutsidePositive(self, colorOutsidePos: List[float]) -> None:
        """
         Sets the positive outside color 
        """
        pass
    def SetDynamicNormal(self, index: int, normal: NXOpen.Vector3d) -> None:
        """
         Sets dynamic normal 
        """
        pass
    def SetDynamicParent(self, index: int, parent: NXOpen.DisplayableObject) -> None:
        """
         Sets dynamic parent 
        """
        pass
    def SetTotalDynamicNormals(self, total: int) -> None:
        """
         Sets number of dynamic normals 
        """
        pass
    def UpdateReverseMap(self) -> None:
        """
         Updates reverse map 
        """
        pass
class DraftAnalysis(AnalysisObject): 
    """ Represents a Draft Analysis builder """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class DupinBuilder(NXOpen.TaggedObject): 
    """ The Dupin Indicatrix is a tool to geometrically display the surface curvature at a specified point on a surface. """
    @property
    def AnalysisPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) AnalysisPoint
         Returns the point location defining where the analysis should be done.  
             
         
        """
        pass
    @AnalysisPoint.setter
    def AnalysisPoint(self, analysisPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) AnalysisPoint
         Returns the point location defining where the analysis should be done.  
             
         
        """
        pass
    @property
    def Angle(self) -> float:
        """
        Getter for property: (float) Angle
         Returns the deviation in degrees from the minimum curvature.  
           This value is used to rotate the normal curvature about the specified point.   
         
        """
        pass
    @Angle.setter
    def Angle(self, angle: float):
        """
        Setter for property: (float) Angle
         Returns the deviation in degrees from the minimum curvature.  
           This value is used to rotate the normal curvature about the specified point.   
         
        """
        pass
    @property
    def FlatnessTolerance(self) -> float:
        """
        Getter for property: (float) FlatnessTolerance
         Returns the tolerance that defines at the specified point if an area is flat.  
             
         
        """
        pass
    @FlatnessTolerance.setter
    def FlatnessTolerance(self, flatnessTolerance: float):
        """
        Setter for property: (float) FlatnessTolerance
         Returns the tolerance that defines at the specified point if an area is flat.  
             
         
        """
        pass
    @property
    def Scale(self) -> float:
        """
        Getter for property: (float) Scale
         Returns the scale factor to apply to the display of the dupin indicatrix.  
             
         
        """
        pass
    @Scale.setter
    def Scale(self, scale: float):
        """
        Setter for property: (float) Scale
         Returns the scale factor to apply to the display of the dupin indicatrix.  
             
         
        """
        pass
    def ResetAnalysisPoint(self) -> None:
        """
         Reset the analysis point to accept dynamic input. 
        """
        pass
import NXOpen
class ExamineGeometry(NXOpen.Builder): 
    """ Represents the Examine Geometry class
     """
    class Check(Enum):
        """
        Members Include: 
         |ObjectTiny|  ObjectTiny 
         |ObjectMisaligned|  ObjectMisaligned 
         |BodyDataStructures|  BodyDataStructures 
         |BodyConsistency|  BodyConsistency 
         |BodyFaceIntersections|  BodyFaceIntersections 
         |BodySheetBoundaries|  BodySheetBoundaries 
         |FaceSmoothness|  FaceSmoothness 
         |FaceSelfIntersection|  FaceSelfIntersection 
         |FaceSpikesCuts|  FaceSpikesCuts 
         |EdgeSmoothness|  EdgeSmoothness 
         |EdgeTolerances|  EdgeTolerances 
         |NumChecks|  Number of Checks 

        """
        ObjectTiny: int
        ObjectMisaligned: int
        BodyDataStructures: int
        BodyConsistency: int
        BodyFaceIntersections: int
        BodySheetBoundaries: int
        FaceSmoothness: int
        FaceSelfIntersection: int
        FaceSpikesCuts: int
        EdgeSmoothness: int
        EdgeTolerances: int
        NumChecks: int
        @staticmethod
        def ValueOf(value: int) -> ExamineGeometry.Check:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CheckCriteriaAngle(self) -> float:
        """
        Getter for property: (float) CheckCriteriaAngle
         Returns the Check Criteria Angle   
            
         
        """
        pass
    @CheckCriteriaAngle.setter
    def CheckCriteriaAngle(self, angle: float):
        """
        Setter for property: (float) CheckCriteriaAngle
         Returns the Check Criteria Angle   
            
         
        """
        pass
    @property
    def CheckCriteriaDistance(self) -> float:
        """
        Getter for property: (float) CheckCriteriaDistance
         Returns the Check Criteria Distance   
            
         
        """
        pass
    @CheckCriteriaDistance.setter
    def CheckCriteriaDistance(self, distance: float):
        """
        Setter for property: (float) CheckCriteriaDistance
         Returns the Check Criteria Distance   
            
         
        """
        pass
    @property
    def ObjectsToExamine(self) -> NXOpen.SelectObjectList:
        """
        Getter for property: ( NXOpen.SelectObjectList) ObjectsToExamine
         Returns the Objects to examine   
            
         
        """
        pass
    def ClearAllChecks(self) -> None:
        """
         Clear or unset all types of checks 
        """
        pass
    def ClearCheck(self, check: ExamineGeometry.Check) -> None:
        """
         Clear or unset a specified type of check 
        """
        pass
    def DisplayResultsAsInfo(self) -> None:
        """
         Displays the results in the information window 
        """
        pass
    def Examine(self) -> None:
        """
         Examines the geometry.  Before calling this method, use 
                    NXOpen.GeometricAnalysis.ExamineGeometry.SetCheck and NXOpen.GeometricAnalysis.ExamineGeometry.ClearCheck 
                    to specify which checks to perform and use NXOpen.GeometricAnalysis.ExamineGeometry.ObjectsToExamine 
                    to specify which objects to examine.  After calling this method, 
                    use NXOpen.GeometricAnalysis.ExamineGeometry.GetResults and 
                    NXOpen.GeometricAnalysis.ExamineGeometry.GetFailedObjects to get the results. 
        """
        pass
    def GetFailedObjects(self, check: ExamineGeometry.Check) -> List[NXOpen.NXObject]:
        """
         Returns the objects that failed a given type of check.  You should 
                call NXOpen.GeometricAnalysis.ExamineGeometry.Examine before calling this method.   
         Returns objects ( NXOpen.NXObject Li):  Objects that
                 failed above check during Examine Geometry .
        """
        pass
    def GetResults(self) -> List[int]:
        """
         Returns an array containing the number of objects that failed each check.
                      You should call NXOpen.GeometricAnalysis.ExamineGeometry.Examine before calling this 
                      method.    The array contains an entry for each check in the
                      NXOpen.GeometricAnalysis.ExamineGeometry.Check enumeration.  The nth item in the array corresponds to
                      the nth check in the NXOpen.GeometricAnalysis.ExamineGeometry.Check enumeration.  For example, the 
                      first item in the array is the number of objects that failed the 
                      GeometricAnalysis.ExamineGeometry.Check.ObjectTiny check.  
                      The corresponding entry in the array will be as follows:
                      
                      
                       -1    errors
                       0    Check not performed as check is not selected
                       -2    a type of NXOpen.GeometricAnalysis.ExamineGeometry.Check is selected, no objects relevant to that type 
                            of NXOpen.GeometricAnalysis.ExamineGeometry.Check are selected. For example, no bodies are selected yet the 
                            GeometricAnalysis.ExamineGeometry.Check.BodyDataStructures check is
                            set or selected. 
                       -3    NXOpen.GeometricAnalysis.ExamineGeometry.Check not performed as other relevant NXOpen.GeometricAnalysis.ExamineGeometry.Check failed. This occurs when 
                            GeometricAnalysis.ExamineGeometry.Check.BodyConsistency
                            andor GeometricAnalysis.ExamineGeometry.Check.BodyFaceIntersections check is set along with 
                            GeometricAnalysis.ExamineGeometry.Check.BodyDataStructures check.
                            If GeometricAnalysis.ExamineGeometry.Check.BodyDataStructures check
                            failed, GeometricAnalysis.ExamineGeometry.Check.BodyConsistency
                            andor
                            GeometricAnalysis.ExamineGeometry.Check.BodyFaceIntersections will
                            not be performed.  
                     
         Returns results (List[int]):  Results of Examine Geometry .
        """
        pass
    def HighlightResult(self, check: ExamineGeometry.Check) -> bool:
        """
         Highlights results of a specified type of check. If the
                 highlighting fails for some of the entities, it returns True, otherwise
                 False.  Highlighting can fail when the entities are corrupt or missing
                 the information needed to display properly. Remaining entities are highlighted 
                 when highlighting fails for some entities. 
         Returns failed (bool):  Return status of the method.
                                                           If return values equals
                                                           false, display was successful. 
                                                           if return value is true,
                                                           display of some objects
                                                           failed. .
        """
        pass
    def SetAllChecks(self) -> None:
        """
         Set all types of checks to examine 
        """
        pass
    def SetCheck(self, check: ExamineGeometry.Check) -> None:
        """
         Set a specified type of check for examine geometry 
        """
        pass
    def UnhighlightAllResults(self) -> None:
        """
         Unhighlight all results 
        """
        pass
    def UnhighlightResult(self, check: ExamineGeometry.Check) -> None:
        """
         Unhighlight results of a specified type of check
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class FaceAnalysisDataRangeBuilder(NXOpen.TaggedObject): 
    """ Represents data range functions used by Face Analysis. """
    class ColorScaleOptions(Enum):
        """
        Members Include: 
         |Automatic|  System determined colors and intervals. 
         |UserDefined|  User defined colors and intervals. 

        """
        Automatic: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> FaceAnalysisDataRangeBuilder.ColorScaleOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class NumberOfColorsOptions(Enum):
        """
        Members Include: 
         |Two|  Display in 2  colors. 
         |Three|  Display in 3  colors. 
         |Four|  Display in 4  colors. 
         |Five|  Display in 5  colors. 
         |Six|  Display in 6  colors. 
         |Seven|  Display in 7  colors. 
         |Eight|  Display in 8  colors. 
         |Nine|  Display in 9  colors. 
         |Ten|  Display in 10 colors. 
         |Eleven|  Display in 11 colors. 
         |Twelve|  Display in 12 colors. 

        """
        Two: int
        Three: int
        Four: int
        Five: int
        Six: int
        Seven: int
        Eight: int
        Nine: int
        Ten: int
        Eleven: int
        Twelve: int
        @staticmethod
        def ValueOf(value: int) -> FaceAnalysisDataRangeBuilder.NumberOfColorsOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ColorScaleOption(self) -> FaceAnalysisDataRangeBuilder.ColorScaleOptions:
        """
        Getter for property: ( FaceAnalysisDataRangeBuilder.ColorScaleOptions NXOpen.Geom) ColorScaleOption
         Returns the intervals option.  
             
         
        """
        pass
    @ColorScaleOption.setter
    def ColorScaleOption(self, colorScaleOption: FaceAnalysisDataRangeBuilder.ColorScaleOptions):
        """
        Setter for property: ( FaceAnalysisDataRangeBuilder.ColorScaleOptions NXOpen.Geom) ColorScaleOption
         Returns the intervals option.  
             
         
        """
        pass
    @property
    def IsFixed(self) -> bool:
        """
        Getter for property: (bool) IsFixed
         Returns the value indicating the range is fixed or not.  
             
         
        """
        pass
    @IsFixed.setter
    def IsFixed(self, isFixed: bool):
        """
        Setter for property: (bool) IsFixed
         Returns the value indicating the range is fixed or not.  
             
         
        """
        pass
    @property
    def Max(self) -> float:
        """
        Getter for property: (float) Max
         Returns the maximum data range.  
             
         
        """
        pass
    @Max.setter
    def Max(self, max: float):
        """
        Setter for property: (float) Max
         Returns the maximum data range.  
             
         
        """
        pass
    @property
    def Middle(self) -> float:
        """
        Getter for property: (float) Middle
         Returns the middle data range value.  
             
         
        """
        pass
    @Middle.setter
    def Middle(self, middle: float):
        """
        Setter for property: (float) Middle
         Returns the middle data range value.  
             
         
        """
        pass
    @property
    def MiddleScale(self) -> float:
        """
        Getter for property: (float) MiddleScale
         Returns the middle value scale for data range.  
             
         
        """
        pass
    @MiddleScale.setter
    def MiddleScale(self, middleScale: float):
        """
        Setter for property: (float) MiddleScale
         Returns the middle value scale for data range.  
             
         
        """
        pass
    @property
    def Min(self) -> float:
        """
        Getter for property: (float) Min
         Returns the minimum data range.  
             
         
        """
        pass
    @Min.setter
    def Min(self, min: float):
        """
        Setter for property: (float) Min
         Returns the minimum data range.  
             
         
        """
        pass
    @property
    def NumberOfColors(self) -> FaceAnalysisDataRangeBuilder.NumberOfColorsOptions:
        """
        Getter for property: ( FaceAnalysisDataRangeBuilder.NumberOfColorsOptions NXOpen.Geom) NumberOfColors
         Returns the number of colors when color scale option is set to Automatic.  
             
         
        """
        pass
    @NumberOfColors.setter
    def NumberOfColors(self, numberOfColors: FaceAnalysisDataRangeBuilder.NumberOfColorsOptions):
        """
        Setter for property: ( FaceAnalysisDataRangeBuilder.NumberOfColorsOptions NXOpen.Geom) NumberOfColors
         Returns the number of colors when color scale option is set to Automatic.  
             
         
        """
        pass
    @property
    def UserDefinedColorScale(self) -> NXOpen.GeometricUtilities.UserDefinedColorScaleData:
        """
        Getter for property: ( NXOpen.GeometricUtilities.UserDefinedColorScaleData) UserDefinedColorScale
         Returns the User Defined Color Scale.  
             
         
        """
        pass
    @property
    def ZoomScale(self) -> float:
        """
        Getter for property: (float) ZoomScale
         Returns the zoom scale.  
             
         
        """
        pass
    @ZoomScale.setter
    def ZoomScale(self, scaleSlider: float):
        """
        Setter for property: (float) ZoomScale
         Returns the zoom scale.  
             
         
        """
        pass
    def ResetData(self) -> None:
        """
         Resets data range. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class FaceAnalysisDisplayBuilder(NXOpen.TaggedObject): 
    """ Represents a set of display settings used by Face Analysis. """
    class ColorLegendOptions(Enum):
        """
        Members Include: 
         |Blend|  Blended color display. 
         |Sharp|  Sharp color display. 

        """
        Blend: int
        Sharp: int
        @staticmethod
        def ValueOf(value: int) -> FaceAnalysisDisplayBuilder.ColorLegendOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ColorsOptions(Enum):
        """
        Members Include: 
         |Two|  Display in 2  colors. 
         |Three|  Display in 3  colors. 
         |Four|  Display in 4  colors. 
         |Five|  Display in 5  colors. 
         |Six|  Display in 6  colors. 
         |Seven|  Display in 7  colors. 
         |Eight|  Display in 8  colors. 
         |Nine|  Display in 9  colors. 
         |Ten|  Display in 10 colors. 
         |Eleven|  Display in 11 colors. 
         |Twelve|  Display in 12 colors. 

        """
        Two: int
        Three: int
        Four: int
        Five: int
        Six: int
        Seven: int
        Eight: int
        Nine: int
        Ten: int
        Eleven: int
        Twelve: int
        @staticmethod
        def ValueOf(value: int) -> FaceAnalysisDisplayBuilder.ColorsOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CanShowFacet(self) -> bool:
        """
        Getter for property: (bool) CanShowFacet
         Returns the flag indicating if facets should be shown.  
             
         
        """
        pass
    @CanShowFacet.setter
    def CanShowFacet(self, canShowFacet: bool):
        """
        Setter for property: (bool) CanShowFacet
         Returns the flag indicating if facets should be shown.  
             
         
        """
        pass
    @property
    def ColorLegendOption(self) -> FaceAnalysisDisplayBuilder.ColorLegendOptions:
        """
        Getter for property: ( FaceAnalysisDisplayBuilder.ColorLegendOptions NXOpen.Geom) ColorLegendOption
         Returns the color legend option.  
             
         
        """
        pass
    @ColorLegendOption.setter
    def ColorLegendOption(self, colorLegendOption: FaceAnalysisDisplayBuilder.ColorLegendOptions):
        """
        Setter for property: ( FaceAnalysisDisplayBuilder.ColorLegendOptions NXOpen.Geom) ColorLegendOption
         Returns the color legend option.  
             
         
        """
        pass
    @property
    def DisplayResolution(self) -> NXOpen.GeometricUtilities.DisplayResolutionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.DisplayResolutionBuilder) DisplayResolution
         Returns the display resolution.  
             
         
        """
        pass
    @property
    def NumberOfColors(self) -> FaceAnalysisDisplayBuilder.ColorsOptions:
        """
        Getter for property: ( FaceAnalysisDisplayBuilder.ColorsOptions NXOpen.Geom) NumberOfColors
         Returns the number of colors.  
             
         
        """
        pass
    @NumberOfColors.setter
    def NumberOfColors(self, numberOfColors: FaceAnalysisDisplayBuilder.ColorsOptions):
        """
        Setter for property: ( FaceAnalysisDisplayBuilder.ColorsOptions NXOpen.Geom) NumberOfColors
         Returns the number of colors.  
             
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class FaceAnalysisNormalsBuilder(NXOpen.TaggedObject): 
    """ Represents reverse normal functions used by Face Analysis. """
    @property
    def FaceToReverseNormal(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) FaceToReverseNormal
         Returns the face to reverse normal   
            
         
        """
        pass
    @property
    def Point(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Point
         Returns the point to redirect normals  
            
         
        """
        pass
    @Point.setter
    def Point(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Point
         Returns the point to redirect normals  
            
         
        """
        pass
    def RestoreAll(self) -> None:
        """
         Restores all face normals. 
        """
        pass
class FaceAnalysis(AnalysisObject): 
    """ Represents a face analysis  """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class FaceCurvatureAnalysisBuilder(NXOpen.Builder): 
    """
        Represents a NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder builder.
        Use NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder to compute different
        types of curvature analysis for selected faces.  The result of the curvature analysis is
        displayed as color maps and contour lines on the faces.  For more details see the NX
        documentation for Face Curvature Analysis.
    """
    class CurvatureTypes(Enum):
        """
        Members Include: 
         |Gaussian|  Gausssian 
         |Absolute|  Absolute 
         |Minimum|  Minimum 
         |Maximum|  Maximum 
         |Mean|  Mean 
         |Normal|  Normal 
         |Sectional|  Sectional 
         |U|  U 
         |V|  V 
         |Radius|  Minimum radius 

        """
        Gaussian: int
        Absolute: int
        Minimum: int
        Maximum: int
        Mean: int
        Normal: int
        Sectional: int
        U: int
        V: int
        Radius: int
        @staticmethod
        def ValueOf(value: int) -> FaceCurvatureAnalysisBuilder.CurvatureTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DirectionTypes(Enum):
        """
        Members Include: 
         |Primitive|  vector or plane 
         |Manipulator|  orientation maninpulator 

        """
        Primitive: int
        Manipulator: int
        @staticmethod
        def ValueOf(value: int) -> FaceCurvatureAnalysisBuilder.DirectionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DisplayTypes(Enum):
        """
        Members Include: 
         |Colormap|  Color Map only 
         |Contours|  Contours 
         |ColormapAndContours|  Color Map and Contours 

        """
        Colormap: int
        Contours: int
        ColormapAndContours: int
        @staticmethod
        def ValueOf(value: int) -> FaceCurvatureAnalysisBuilder.DisplayTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ScaleTypes(Enum):
        """
        Members Include: 
         |Linear|  Linear Scaling (No Scaling) 
         |Log|  Log Scaling 
         |Area|  Equalized by Area 

        """
        Linear: int
        Log: int
        Area: int
        @staticmethod
        def ValueOf(value: int) -> FaceCurvatureAnalysisBuilder.ScaleTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ContourRefinement(self) -> int:
        """
        Getter for property: (int) ContourRefinement
         Returns the contour refinement level, in the range 0-6.  
           Increasing values compute more detailed and
                    accurate contour lines on the face.   
         
        """
        pass
    @ContourRefinement.setter
    def ContourRefinement(self, contourRefinement: int):
        """
        Setter for property: (int) ContourRefinement
         Returns the contour refinement level, in the range 0-6.  
           Increasing values compute more detailed and
                    accurate contour lines on the face.   
         
        """
        pass
    @property
    def ContourShift(self) -> float:
        """
        Getter for property: (float) ContourShift
         Returns the starting contour shift or bias value, as % of the standard contour interval.  
           Valid values are -100 to 100.   
         
        """
        pass
    @ContourShift.setter
    def ContourShift(self, contourShift: float):
        """
        Setter for property: (float) ContourShift
         Returns the starting contour shift or bias value, as % of the standard contour interval.  
           Valid values are -100 to 100.   
         
        """
        pass
    @property
    def CurvatureSectionPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) CurvatureSectionPlane
         Returns the section curvature plane when sectional curvature values are to be computed and displayed.  
             
         
        """
        pass
    @CurvatureSectionPlane.setter
    def CurvatureSectionPlane(self, curvatureSectionPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) CurvatureSectionPlane
         Returns the section curvature plane when sectional curvature values are to be computed and displayed.  
             
         
        """
        pass
    @property
    def CurvatureType(self) -> FaceCurvatureAnalysisBuilder.CurvatureTypes:
        """
        Getter for property: ( FaceCurvatureAnalysisBuilder.CurvatureTypes NXOpen.Geom) CurvatureType
         Returns the curvature type to compute and display.  
            
         
        """
        pass
    @CurvatureType.setter
    def CurvatureType(self, curvatureType: FaceCurvatureAnalysisBuilder.CurvatureTypes):
        """
        Setter for property: ( FaceCurvatureAnalysisBuilder.CurvatureTypes NXOpen.Geom) CurvatureType
         Returns the curvature type to compute and display.  
            
         
        """
        pass
    @property
    def DisplayType(self) -> FaceCurvatureAnalysisBuilder.DisplayTypes:
        """
        Getter for property: ( FaceCurvatureAnalysisBuilder.DisplayTypes NXOpen.Geom) DisplayType
         Returns the display type for curvature values.  
              
         
        """
        pass
    @DisplayType.setter
    def DisplayType(self, displayType: FaceCurvatureAnalysisBuilder.DisplayTypes):
        """
        Setter for property: ( FaceCurvatureAnalysisBuilder.DisplayTypes NXOpen.Geom) DisplayType
         Returns the display type for curvature values.  
              
         
        """
        pass
    @property
    def MapCenter(self) -> float:
        """
        Getter for property: (float) MapCenter
         Returns the center point of the color mapping and contouring, as % of the full range of
                    curvature values present in the data.  
          
                  
         
        """
        pass
    @MapCenter.setter
    def MapCenter(self, mapCenter: float):
        """
        Setter for property: (float) MapCenter
         Returns the center point of the color mapping and contouring, as % of the full range of
                    curvature values present in the data.  
          
                  
         
        """
        pass
    @property
    def MapRange(self) -> float:
        """
        Getter for property: (float) MapRange
         Returns the color map and contour range, as % of the full range of curvature values present in the data.  
             
         
        """
        pass
    @MapRange.setter
    def MapRange(self, mapRange: float):
        """
        Setter for property: (float) MapRange
         Returns the color map and contour range, as % of the full range of curvature values present in the data.  
             
         
        """
        pass
    @property
    def NormalOption(self) -> FaceCurvatureAnalysisBuilder.DirectionTypes:
        """
        Getter for property: ( FaceCurvatureAnalysisBuilder.DirectionTypes NXOpen.Geom) NormalOption
         Returns the normal for the case of normal curvature type.  
             
         
        """
        pass
    @NormalOption.setter
    def NormalOption(self, normalOption: FaceCurvatureAnalysisBuilder.DirectionTypes):
        """
        Setter for property: ( FaceCurvatureAnalysisBuilder.DirectionTypes NXOpen.Geom) NormalOption
         Returns the normal for the case of normal curvature type.  
             
         
        """
        pass
    @property
    def NormalOrientation(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: ( NXOpen.Matrix3x3) NormalOrientation
         Returns the normal orientation when the normal curvature values are to be computed and displayed.  
             
         
        """
        pass
    @NormalOrientation.setter
    def NormalOrientation(self, normalOrientation: NXOpen.Matrix3x3):
        """
        Setter for property: ( NXOpen.Matrix3x3) NormalOrientation
         Returns the normal orientation when the normal curvature values are to be computed and displayed.  
             
         
        """
        pass
    @property
    def NormalOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) NormalOrigin
         Returns the normal origin when normal curvature values are to be computed and displayed.  
            
         
        """
        pass
    @NormalOrigin.setter
    def NormalOrigin(self, normalOrigin: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) NormalOrigin
         Returns the normal origin when normal curvature values are to be computed and displayed.  
            
         
        """
        pass
    @property
    def NormalVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) NormalVector
         Returns the normal vector for the case when normal curvature values are to be computed and displayed.  
            
         
        """
        pass
    @NormalVector.setter
    def NormalVector(self, normalVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) NormalVector
         Returns the normal vector for the case when normal curvature values are to be computed and displayed.  
            
         
        """
        pass
    @property
    def NumberOfContours(self) -> int:
        """
        Getter for property: (int) NumberOfContours
         Returns the number of contour lines to compute and display.  
             
         
        """
        pass
    @NumberOfContours.setter
    def NumberOfContours(self, numberOfContours: int):
        """
        Setter for property: (int) NumberOfContours
         Returns the number of contour lines to compute and display.  
             
         
        """
        pass
    @property
    def Resolution(self) -> NXOpen.GeometricUtilities.DisplayResolutionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.DisplayResolutionBuilder) Resolution
         Returns the tesselation resolution to use for curvature color map and contours.  
             
         
        """
        pass
    @property
    def ReverseIndividual(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: ( NXOpen.SelectDisplayableObject) ReverseIndividual
         Returns the individual face normal.  
             
         
        """
        pass
    @property
    def ScaleType(self) -> FaceCurvatureAnalysisBuilder.ScaleTypes:
        """
        Getter for property: ( FaceCurvatureAnalysisBuilder.ScaleTypes NXOpen.Geom) ScaleType
         Returns the scaling type of curvature values.  
             
         
        """
        pass
    @ScaleType.setter
    def ScaleType(self, scaleType: FaceCurvatureAnalysisBuilder.ScaleTypes):
        """
        Setter for property: ( FaceCurvatureAnalysisBuilder.ScaleTypes NXOpen.Geom) ScaleType
         Returns the scaling type of curvature values.  
             
         
        """
        pass
    @property
    def SectionOption(self) -> FaceCurvatureAnalysisBuilder.DirectionTypes:
        """
        Getter for property: ( FaceCurvatureAnalysisBuilder.DirectionTypes NXOpen.Geom) SectionOption
         Returns whether to use a section plane or maninpulator for sectional curvatures.  
             
         
        """
        pass
    @SectionOption.setter
    def SectionOption(self, sectionOption: FaceCurvatureAnalysisBuilder.DirectionTypes):
        """
        Setter for property: ( FaceCurvatureAnalysisBuilder.DirectionTypes NXOpen.Geom) SectionOption
         Returns whether to use a section plane or maninpulator for sectional curvatures.  
             
         
        """
        pass
    @property
    def SectionOrientation(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: ( NXOpen.Matrix3x3) SectionOrientation
         Returns the section orientation for sectional curvatures.  
             
         
        """
        pass
    @SectionOrientation.setter
    def SectionOrientation(self, sectionOrientation: NXOpen.Matrix3x3):
        """
        Setter for property: ( NXOpen.Matrix3x3) SectionOrientation
         Returns the section orientation for sectional curvatures.  
             
         
        """
        pass
    @property
    def SectionOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) SectionOrigin
         Returns the section origin for sectional curvatures.  
             
         
        """
        pass
    @SectionOrigin.setter
    def SectionOrigin(self, sectionOrigin: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) SectionOrigin
         Returns the section origin for sectional curvatures.  
             
         
        """
        pass
    @property
    def SelectObject(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) SelectObject
         Returns the faces on which to perform curvature analysis.  
             
         
        """
        pass
    @property
    def ShowZeroContour(self) -> bool:
        """
        Getter for property: (bool) ShowZeroContour
         Returns the option to show zero curvature contour line.  
             
         
        """
        pass
    @ShowZeroContour.setter
    def ShowZeroContour(self, showZeroContour: bool):
        """
        Setter for property: (bool) ShowZeroContour
         Returns the option to show zero curvature contour line.  
             
         
        """
        pass
    def DeselectFaces(self, faces: List[NXOpen.DisplayableObject]) -> None:
        """
         Deselects faces 
        """
        pass
    def ReverseAllNormals(self) -> None:
        """
         Reverses all normals. 
        """
        pass
    def ReverseIndividualNormal(self, face: NXOpen.DisplayableObject) -> None:
        """
         Reverses an individual face normal. 
        """
        pass
    def UpdateReverseMap(self) -> None:
        """
         Updates reverse map. 
        """
        pass
class FaceCurvatureAnalysis(AnalysisObject): 
    """ Represents a Face Curvature Analysis builder """
    pass
import NXOpen
class GapFlushnessBuilder(NXOpen.Builder): 
    """ GapFlushnessBuilder class  """
    class DisplayOptions(Enum):
        """
        Members Include: 
         |GapOnly|  gap only
         |FlushnessOnly|  flushness only
         |Both|  both 

        """
        GapOnly: int
        FlushnessOnly: int
        Both: int
        @staticmethod
        def ValueOf(value: int) -> GapFlushnessBuilder.DisplayOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EvaluationModes(Enum):
        """
        Members Include: 
         |Point|  at point 
         |CurveNumber|  along curve and number  
         |Curve|  along curve and distance

        """
        Point: int
        CurveNumber: int
        Curve: int
        @staticmethod
        def ValueOf(value: int) -> GapFlushnessBuilder.EvaluationModes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EvaluationTypes(Enum):
        """
        Members Include: 
         |Absolute|  absolute 
         |Visual|  visual   

        """
        Absolute: int
        Visual: int
        @staticmethod
        def ValueOf(value: int) -> GapFlushnessBuilder.EvaluationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PanelTypes(Enum):
        """
        Members Include: 
         |Hem|  type hem 
         |Flange|  type flange
         |Wall|  type wall 

        """
        Hem: int
        Flange: int
        Wall: int
        @staticmethod
        def ValueOf(value: int) -> GapFlushnessBuilder.PanelTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SectionAlignments(Enum):
        """
        Members Include: 
         |Curve|  curve
         |CurveView|  curve in view
         |SpecifiedDirection|  specified direction 

        """
        Curve: int
        CurveView: int
        SpecifiedDirection: int
        @staticmethod
        def ValueOf(value: int) -> GapFlushnessBuilder.SectionAlignments:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SectionCurveOptions(Enum):
        """
        Members Include: 
         |ContactCurve|  use contact curve
         |UserDefined|  use user defined curve 

        """
        ContactCurve: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> GapFlushnessBuilder.SectionCurveOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BasePanelFaces(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BasePanelFaces
         Returns the Base Panel face selection      
            
         
        """
        pass
    @property
    def BasePanelInnerContactCurves(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) BasePanelInnerContactCurves
         Returns the Base Panel inner contact section   
            
         
        """
        pass
    @property
    def BasePanelOuterContactCurves(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) BasePanelOuterContactCurves
         Returns the Base Panel outer contact section    
            
         
        """
        pass
    @property
    def BasePanelType(self) -> GapFlushnessBuilder.PanelTypes:
        """
        Getter for property: ( GapFlushnessBuilder.PanelTypes NXOpen.Geom) BasePanelType
         Returns the Base Panel type     
            
         
        """
        pass
    @BasePanelType.setter
    def BasePanelType(self, panel_type: GapFlushnessBuilder.PanelTypes):
        """
        Setter for property: ( GapFlushnessBuilder.PanelTypes NXOpen.Geom) BasePanelType
         Returns the Base Panel type     
            
         
        """
        pass
    @property
    def CrossSectionCurveOption(self) -> GapFlushnessBuilder.SectionCurveOptions:
        """
        Getter for property: ( GapFlushnessBuilder.SectionCurveOptions NXOpen.Geom) CrossSectionCurveOption
         Returns the cross section curve option       
            
         
        """
        pass
    @CrossSectionCurveOption.setter
    def CrossSectionCurveOption(self, section_curve_option: GapFlushnessBuilder.SectionCurveOptions):
        """
        Setter for property: ( GapFlushnessBuilder.SectionCurveOptions NXOpen.Geom) CrossSectionCurveOption
         Returns the cross section curve option       
            
         
        """
        pass
    @property
    def CrossSectionCurves(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) CrossSectionCurves
         Returns the Cross Section Curves   
            
         
        """
        pass
    @property
    def EvaluationMode(self) -> GapFlushnessBuilder.EvaluationModes:
        """
        Getter for property: ( GapFlushnessBuilder.EvaluationModes NXOpen.Geom) EvaluationMode
         Returns the evaluation Method      
            
         
        """
        pass
    @EvaluationMode.setter
    def EvaluationMode(self, evaluation_mode: GapFlushnessBuilder.EvaluationModes):
        """
        Setter for property: ( GapFlushnessBuilder.EvaluationModes NXOpen.Geom) EvaluationMode
         Returns the evaluation Method      
            
         
        """
        pass
    @property
    def EvaluationPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) EvaluationPoint
         Returns the evaluation point       
            
         
        """
        pass
    @EvaluationPoint.setter
    def EvaluationPoint(self, evaluationPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) EvaluationPoint
         Returns the evaluation point       
            
         
        """
        pass
    @property
    def EvaluationType(self) -> GapFlushnessBuilder.EvaluationTypes:
        """
        Getter for property: ( GapFlushnessBuilder.EvaluationTypes NXOpen.Geom) EvaluationType
         Returns the evaluation type   
            
         
        """
        pass
    @EvaluationType.setter
    def EvaluationType(self, evaluation_type: GapFlushnessBuilder.EvaluationTypes):
        """
        Setter for property: ( GapFlushnessBuilder.EvaluationTypes NXOpen.Geom) EvaluationType
         Returns the evaluation type   
            
         
        """
        pass
    @property
    def IsNegativeToleranceLabelDisplayed(self) -> bool:
        """
        Getter for property: (bool) IsNegativeToleranceLabelDisplayed
         Returns the Label Display negative tolerance       
            
         
        """
        pass
    @IsNegativeToleranceLabelDisplayed.setter
    def IsNegativeToleranceLabelDisplayed(self, showlabel_negative: bool):
        """
        Setter for property: (bool) IsNegativeToleranceLabelDisplayed
         Returns the Label Display negative tolerance       
            
         
        """
        pass
    @property
    def IsNominalLabelDisplayed(self) -> bool:
        """
        Getter for property: (bool) IsNominalLabelDisplayed
         Returns the Label Display Nominal       
            
         
        """
        pass
    @IsNominalLabelDisplayed.setter
    def IsNominalLabelDisplayed(self, showlabel_nominal: bool):
        """
        Setter for property: (bool) IsNominalLabelDisplayed
         Returns the Label Display Nominal       
            
         
        """
        pass
    @property
    def IsPositiveToleranceLabelDisplayed(self) -> bool:
        """
        Getter for property: (bool) IsPositiveToleranceLabelDisplayed
         Returns the Label Display positive tolerance      
            
         
        """
        pass
    @IsPositiveToleranceLabelDisplayed.setter
    def IsPositiveToleranceLabelDisplayed(self, showlabel_positive: bool):
        """
        Setter for property: (bool) IsPositiveToleranceLabelDisplayed
         Returns the Label Display positive tolerance      
            
         
        """
        pass
    @property
    def LabelDisplayOption(self) -> GapFlushnessBuilder.DisplayOptions:
        """
        Getter for property: ( GapFlushnessBuilder.DisplayOptions NXOpen.Geom) LabelDisplayOption
         Returns the display option type      
            
         
        """
        pass
    @LabelDisplayOption.setter
    def LabelDisplayOption(self, display_option: GapFlushnessBuilder.DisplayOptions):
        """
        Setter for property: ( GapFlushnessBuilder.DisplayOptions NXOpen.Geom) LabelDisplayOption
         Returns the display option type      
            
         
        """
        pass
    @property
    def NegativeFlushnessTolerance(self) -> float:
        """
        Getter for property: (float) NegativeFlushnessTolerance
         Returns the negative tolerance for flushness        
            
         
        """
        pass
    @NegativeFlushnessTolerance.setter
    def NegativeFlushnessTolerance(self, negativeTolFlush: float):
        """
        Setter for property: (float) NegativeFlushnessTolerance
         Returns the negative tolerance for flushness        
            
         
        """
        pass
    @property
    def NegativeGapTolerance(self) -> float:
        """
        Getter for property: (float) NegativeGapTolerance
         Returns the negative tolerance for gap       
            
         
        """
        pass
    @NegativeGapTolerance.setter
    def NegativeGapTolerance(self, negativeTolGap: float):
        """
        Setter for property: (float) NegativeGapTolerance
         Returns the negative tolerance for gap       
            
         
        """
        pass
    @property
    def NominalFlushness(self) -> float:
        """
        Getter for property: (float) NominalFlushness
         Returns the nominal value  for flushness        
            
         
        """
        pass
    @NominalFlushness.setter
    def NominalFlushness(self, nominalFlush: float):
        """
        Setter for property: (float) NominalFlushness
         Returns the nominal value  for flushness        
            
         
        """
        pass
    @property
    def NominalGap(self) -> float:
        """
        Getter for property: (float) NominalGap
         Returns the nominal value  for gap         
            
         
        """
        pass
    @NominalGap.setter
    def NominalGap(self, nominalGap: float):
        """
        Setter for property: (float) NominalGap
         Returns the nominal value  for gap         
            
         
        """
        pass
    @property
    def PositiveFlushnessTolerance(self) -> float:
        """
        Getter for property: (float) PositiveFlushnessTolerance
         Returns the positive tolerance for flushness    
            
         
        """
        pass
    @PositiveFlushnessTolerance.setter
    def PositiveFlushnessTolerance(self, positiveTolFlush: float):
        """
        Setter for property: (float) PositiveFlushnessTolerance
         Returns the positive tolerance for flushness    
            
         
        """
        pass
    @property
    def PositiveGapTolerance(self) -> float:
        """
        Getter for property: (float) PositiveGapTolerance
         Returns the positive tolerance for gap        
            
         
        """
        pass
    @PositiveGapTolerance.setter
    def PositiveGapTolerance(self, positiveTolGap: float):
        """
        Setter for property: (float) PositiveGapTolerance
         Returns the positive tolerance for gap        
            
         
        """
        pass
    @property
    def PreviewOption(self) -> bool:
        """
        Getter for property: (bool) PreviewOption
         Returns the preview option   
            
         
        """
        pass
    @PreviewOption.setter
    def PreviewOption(self, previewOption: bool):
        """
        Setter for property: (bool) PreviewOption
         Returns the preview option   
            
         
        """
        pass
    @property
    def SampleDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SampleDistance
         Returns the Sample Distance        
            
         
        """
        pass
    @property
    def SampleNumber(self) -> int:
        """
        Getter for property: (int) SampleNumber
         Returns the sample number   
            
         
        """
        pass
    @SampleNumber.setter
    def SampleNumber(self, sampleNumber: int):
        """
        Setter for property: (int) SampleNumber
         Returns the sample number   
            
         
        """
        pass
    @property
    def SecondPanelFaces(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SecondPanelFaces
         Returns the Second Panel face selection        
            
         
        """
        pass
    @property
    def SecondPanelInnerContactCurves(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) SecondPanelInnerContactCurves
         Returns the Second Panel inner contact section    
            
         
        """
        pass
    @property
    def SecondPanelOuterContactCurves(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) SecondPanelOuterContactCurves
         Returns the Second Panel outer contact section   
            
         
        """
        pass
    @property
    def SecondPanelType(self) -> GapFlushnessBuilder.PanelTypes:
        """
        Getter for property: ( GapFlushnessBuilder.PanelTypes NXOpen.Geom) SecondPanelType
         Returns the Second Panel type     
            
         
        """
        pass
    @SecondPanelType.setter
    def SecondPanelType(self, panel_type: GapFlushnessBuilder.PanelTypes):
        """
        Setter for property: ( GapFlushnessBuilder.PanelTypes NXOpen.Geom) SecondPanelType
         Returns the Second Panel type     
            
         
        """
        pass
    @property
    def SectionAlignment(self) -> GapFlushnessBuilder.SectionAlignments:
        """
        Getter for property: ( GapFlushnessBuilder.SectionAlignments NXOpen.Geom) SectionAlignment
         Returns the Section Alignment       
            
         
        """
        pass
    @SectionAlignment.setter
    def SectionAlignment(self, section_alignment: GapFlushnessBuilder.SectionAlignments):
        """
        Setter for property: ( GapFlushnessBuilder.SectionAlignments NXOpen.Geom) SectionAlignment
         Returns the Section Alignment       
            
         
        """
        pass
    @property
    def SectionAlignmentDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) SectionAlignmentDirection
         Returns the section alignment vector       
            
         
        """
        pass
    @SectionAlignmentDirection.setter
    def SectionAlignmentDirection(self, sectionAlignmentDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) SectionAlignmentDirection
         Returns the section alignment vector       
            
         
        """
        pass
    @property
    def ShowOutRangeLabels(self) -> bool:
        """
        Getter for property: (bool) ShowOutRangeLabels
         Returns the show out of range labels   
            
         
        """
        pass
    @ShowOutRangeLabels.setter
    def ShowOutRangeLabels(self, showOutRangeLabels: bool):
        """
        Setter for property: (bool) ShowOutRangeLabels
         Returns the show out of range labels   
            
         
        """
        pass
class GapFlushness(AnalysisObject): 
    """ Gap and Flushness analysis object class """
    pass
import NXOpen
class GeometricProperties(NXOpen.Builder): 
    """ Represents the Geometric Properties class. This class can be used to
      find local geometric properties of faces, edges, curves, CAE faces, and CAE
      edgescurves at a given point.
     """
    class Entity(Enum):
        """
        Members Include: 
         |Face|  Face 
         |Edge|  Either a modeling edge or a curve. 
         |CaeFace|  CAE Face 
         |CaeCurve|  CAE Curve 

        """
        Face: int
        Edge: int
        CaeFace: int
        CaeCurve: int
        @staticmethod
        def ValueOf(value: int) -> GeometricProperties.Entity:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OutputType(Enum):
        """
        Members Include: 
         |Dynamic|  Properties of an entity are displayed first on the dialog
                                                                      itself on mouse over. These properties are listed on in the
                                                                      information window upon selection of a point. 
         |Static|  Propeties of the selected entities are displayed in the
                                                                    information window. 

        """
        Dynamic: int
        Static: int
        @staticmethod
        def ValueOf(value: int) -> GeometricProperties.OutputType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Status(Enum):
        """
        Members Include: 
         |Success|  Success 
         |InvalidInput|  Input specified is not
                                                                       valid.
         |Failed|  Failed to find all geometric
                                                                 properties

        """
        Success: int
        InvalidInput: int
        Failed: int
        @staticmethod
        def ValueOf(value: int) -> GeometricProperties.Status:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CaeCurve:
        """
         CAE EdgeCurve Geometric Properties 
         GeometricPropertiesCaeCurve_Struct NXOpen.Geom is an alias for  GeometricProperties.CaeCurve NXOpen.Geom.
        """
        @property
        def ArcLengthParameter(self) -> float:
            """
            Getter for property ArcLengthParameter
            ArcLength parametrization

            """
            pass
        @ArcLengthParameter.setter
        def ArcLengthParameter(self, value: float):
            """
            Getter for property ArcLengthParameter
            ArcLength parametrization
            Setter for property ArcLengthParameter
            ArcLength parametrization

            """
            pass
        @property
        def UnitArcLengthParameter(self) -> float:
            """
            Getter for property UnitArcLengthParameter
            UnitArcLength parametrization

            """
            pass
        @UnitArcLengthParameter.setter
        def UnitArcLengthParameter(self, value: float):
            """
            Getter for property UnitArcLengthParameter
            UnitArcLength parametrization
            Setter for property UnitArcLengthParameter
            UnitArcLength parametrization

            """
            pass
        @property
        def ClosestPointInWcs(self) -> NXOpen.Point3d:
            """
            Getter for property ClosestPointInWcs
            closest point on curve in Work Part Coordinates

            """
            pass
        @ClosestPointInWcs.setter
        def ClosestPointInWcs(self, value: NXOpen.Point3d):
            """
            Getter for property ClosestPointInWcs
            closest point on curve in Work Part Coordinates
            Setter for property ClosestPointInWcs
            closest point on curve in Work Part Coordinates

            """
            pass
        @property
        def NormalInWcs(self) -> NXOpen.Vector3d:
            """
            Getter for property NormalInWcs
            normal of closest point in Work Part Coordinates

            """
            pass
        @NormalInWcs.setter
        def NormalInWcs(self, value: NXOpen.Vector3d):
            """
            Getter for property NormalInWcs
            normal of closest point in Work Part Coordinates
            Setter for property NormalInWcs
            normal of closest point in Work Part Coordinates

            """
            pass
        @property
        def TangentInWcs(self) -> NXOpen.Vector3d:
            """
            Getter for property TangentInWcs
            tangent of closest point in Work Part Coordinates

            """
            pass
        @TangentInWcs.setter
        def TangentInWcs(self, value: NXOpen.Vector3d):
            """
            Getter for property TangentInWcs
            tangent of closest point in Work Part Coordinates
            Setter for property TangentInWcs
            tangent of closest point in Work Part Coordinates

            """
            pass
        @property
        def Tangent(self) -> NXOpen.Vector3d:
            """
            Getter for property Tangent
            tangent of closest point in Root Part Coordinates

            """
            pass
        @Tangent.setter
        def Tangent(self, value: NXOpen.Vector3d):
            """
            Getter for property Tangent
            tangent of closest point in Root Part Coordinates
            Setter for property Tangent
            tangent of closest point in Root Part Coordinates

            """
            pass
        @property
        def Normal(self) -> NXOpen.Vector3d:
            """
            Getter for property Normal
            normal of closest point in Root Part Coordinates

            """
            pass
        @Normal.setter
        def Normal(self, value: NXOpen.Vector3d):
            """
            Getter for property Normal
            normal of closest point in Root Part Coordinates
            Setter for property Normal
            normal of closest point in Root Part Coordinates

            """
            pass
        @property
        def ClosestPoint(self) -> NXOpen.Point3d:
            """
            Getter for property ClosestPoint
            closest point on curve in Root Part Coordinates

            """
            pass
        @ClosestPoint.setter
        def ClosestPoint(self, value: NXOpen.Point3d):
            """
            Getter for property ClosestPoint
            closest point on curve in Root Part Coordinates
            Setter for property ClosestPoint
            closest point on curve in Root Part Coordinates

            """
            pass
    class CaeFace:
        """
         CAE Face Geometric Properties 
         GeometricPropertiesCaeFace_Struct NXOpen.Geom is an alias for  GeometricProperties.CaeFace NXOpen.Geom.
        """
        @property
        def ClosestPoint(self) -> NXOpen.Vector3d:
            """
            Getter for property ClosestPoint
            closest point on face in Root Part Coordinates

            """
            pass
        @ClosestPoint.setter
        def ClosestPoint(self, value: NXOpen.Vector3d):
            """
            Getter for property ClosestPoint
            closest point on face in Root Part Coordinates
            Setter for property ClosestPoint
            closest point on face in Root Part Coordinates

            """
            pass
        @property
        def UParameter(self) -> float:
            """
            Getter for property UParameter
            u parameter of the closest point in Root Part Coordinates

            """
            pass
        @UParameter.setter
        def UParameter(self, value: float):
            """
            Getter for property UParameter
            u parameter of the closest point in Root Part Coordinates
            Setter for property UParameter
            u parameter of the closest point in Root Part Coordinates

            """
            pass
        @property
        def VParameter(self) -> float:
            """
            Getter for property VParameter
            v parameter of the closest point in Root Part Coordinates

            """
            pass
        @VParameter.setter
        def VParameter(self, value: float):
            """
            Getter for property VParameter
            v parameter of the closest point in Root Part Coordinates
            Setter for property VParameter
            v parameter of the closest point in Root Part Coordinates

            """
            pass
        @property
        def Normal(self) -> NXOpen.Vector3d:
            """
            Getter for property Normal
            normal at the closest point in Root Part Coordinates

            """
            pass
        @Normal.setter
        def Normal(self, value: NXOpen.Vector3d):
            """
            Getter for property Normal
            normal at the closest point in Root Part Coordinates
            Setter for property Normal
            normal at the closest point in Root Part Coordinates

            """
            pass
        @property
        def ClosestPointInWcs(self) -> NXOpen.Point3d:
            """
            Getter for property ClosestPointInWcs
            closest point in Work Part Coordinates

            """
            pass
        @ClosestPointInWcs.setter
        def ClosestPointInWcs(self, value: NXOpen.Point3d):
            """
            Getter for property ClosestPointInWcs
            closest point in Work Part Coordinates
            Setter for property ClosestPointInWcs
            closest point in Work Part Coordinates

            """
            pass
        @property
        def NormalInWcs(self) -> NXOpen.Vector3d:
            """
            Getter for property NormalInWcs
            normal in Work Part Coordinates

            """
            pass
        @NormalInWcs.setter
        def NormalInWcs(self, value: NXOpen.Vector3d):
            """
            Getter for property NormalInWcs
            normal in Work Part Coordinates
            Setter for property NormalInWcs
            normal in Work Part Coordinates

            """
            pass
        @property
        def UDerivative(self) -> NXOpen.Vector3d:
            """
            Getter for property UDerivative
            Derivative in U, Root Part Coordinates

            """
            pass
        @UDerivative.setter
        def UDerivative(self, value: NXOpen.Vector3d):
            """
            Getter for property UDerivative
            Derivative in U, Root Part Coordinates
            Setter for property UDerivative
            Derivative in U, Root Part Coordinates

            """
            pass
        @property
        def VDerivative(self) -> NXOpen.Vector3d:
            """
            Getter for property VDerivative
            Derivative in V, Root Part Coordinates

            """
            pass
        @VDerivative.setter
        def VDerivative(self, value: NXOpen.Vector3d):
            """
            Getter for property VDerivative
            Derivative in V, Root Part Coordinates
            Setter for property VDerivative
            Derivative in V, Root Part Coordinates

            """
            pass
        @property
        def UDerivativeInWcs(self) -> NXOpen.Vector3d:
            """
            Getter for property UDerivativeInWcs
            Derivative in U in Work Part Coordinates

            """
            pass
        @UDerivativeInWcs.setter
        def UDerivativeInWcs(self, value: NXOpen.Vector3d):
            """
            Getter for property UDerivativeInWcs
            Derivative in U in Work Part Coordinates
            Setter for property UDerivativeInWcs
            Derivative in U in Work Part Coordinates

            """
            pass
        @property
        def VDerivativeInWcs(self) -> NXOpen.Vector3d:
            """
            Getter for property VDerivativeInWcs
            Derivative in V in Work Part Coordinates

            """
            pass
        @VDerivativeInWcs.setter
        def VDerivativeInWcs(self, value: NXOpen.Vector3d):
            """
            Getter for property VDerivativeInWcs
            Derivative in V in Work Part Coordinates
            Setter for property VDerivativeInWcs
            Derivative in V in Work Part Coordinates

            """
            pass
    class Edge:
        """
         EdgeCurve Geometric Properties 
         GeometricPropertiesEdge_Struct NXOpen.Geom is an alias for  GeometricProperties.Edge NXOpen.Geom.
        """
        @property
        def ParameterPercentage(self) -> float:
            """
            Getter for property ParameterPercentage
            Curve Parameter Percentage

            """
            pass
        @ParameterPercentage.setter
        def ParameterPercentage(self, value: float):
            """
            Getter for property ParameterPercentage
            Curve Parameter Percentage
            Setter for property ParameterPercentage
            Curve Parameter Percentage

            """
            pass
        @property
        def Parameter(self) -> float:
            """
            Getter for property Parameter
            Curve Parameter

            """
            pass
        @Parameter.setter
        def Parameter(self, value: float):
            """
            Getter for property Parameter
            Curve Parameter
            Setter for property Parameter
            Curve Parameter

            """
            pass
        @property
        def PositionInWcs(self) -> NXOpen.Point3d:
            """
            Getter for property PositionInWcs
            XYZ Position in Work Part coordinates

            """
            pass
        @PositionInWcs.setter
        def PositionInWcs(self, value: NXOpen.Point3d):
            """
            Getter for property PositionInWcs
            XYZ Position in Work Part coordinates
            Setter for property PositionInWcs
            XYZ Position in Work Part coordinates

            """
            pass
        @property
        def Position(self) -> NXOpen.Point3d:
            """
            Getter for property Position
            XYZ Position in Root Part coordinates

            """
            pass
        @Position.setter
        def Position(self, value: NXOpen.Point3d):
            """
            Getter for property Position
            XYZ Position in Root Part coordinates
            Setter for property Position
            XYZ Position in Root Part coordinates

            """
            pass
        @property
        def TangentInWcs(self) -> NXOpen.Vector3d:
            """
            Getter for property TangentInWcs
            Tangent Vector in Work Part coordinates

            """
            pass
        @TangentInWcs.setter
        def TangentInWcs(self, value: NXOpen.Vector3d):
            """
            Getter for property TangentInWcs
            Tangent Vector in Work Part coordinates
            Setter for property TangentInWcs
            Tangent Vector in Work Part coordinates

            """
            pass
        @property
        def Tangent(self) -> NXOpen.Vector3d:
            """
            Getter for property Tangent
            Tangent Vector in Root Part coordinates

            """
            pass
        @Tangent.setter
        def Tangent(self, value: NXOpen.Vector3d):
            """
            Getter for property Tangent
            Tangent Vector in Root Part coordinates
            Setter for property Tangent
            Tangent Vector in Root Part coordinates

            """
            pass
        @property
        def NormalInWcs(self) -> NXOpen.Vector3d:
            """
            Getter for property NormalInWcs
            Curve Normal in Work Part coordinates

            """
            pass
        @NormalInWcs.setter
        def NormalInWcs(self, value: NXOpen.Vector3d):
            """
            Getter for property NormalInWcs
            Curve Normal in Work Part coordinates
            Setter for property NormalInWcs
            Curve Normal in Work Part coordinates

            """
            pass
        @property
        def Normal(self) -> NXOpen.Vector3d:
            """
            Getter for property Normal
            Curve Normal in Root Part coordinates

            """
            pass
        @Normal.setter
        def Normal(self, value: NXOpen.Vector3d):
            """
            Getter for property Normal
            Curve Normal in Root Part coordinates
            Setter for property Normal
            Curve Normal in Root Part coordinates

            """
            pass
        @property
        def BinormalInWcs(self) -> NXOpen.Vector3d:
            """
            Getter for property BinormalInWcs
            Curve Binormal in Work Part coordinates

            """
            pass
        @BinormalInWcs.setter
        def BinormalInWcs(self, value: NXOpen.Vector3d):
            """
            Getter for property BinormalInWcs
            Curve Binormal in Work Part coordinates
            Setter for property BinormalInWcs
            Curve Binormal in Work Part coordinates

            """
            pass
        @property
        def Binormal(self) -> NXOpen.Vector3d:
            """
            Getter for property Binormal
            Curve Binormal in Root Part coordinates

            """
            pass
        @Binormal.setter
        def Binormal(self, value: NXOpen.Vector3d):
            """
            Getter for property Binormal
            Curve Binormal in Root Part coordinates
            Setter for property Binormal
            Curve Binormal in Root Part coordinates

            """
            pass
        @property
        def Torsion(self) -> float:
            """
            Getter for property Torsion
            Curve Torsion

            """
            pass
        @Torsion.setter
        def Torsion(self, value: float):
            """
            Getter for property Torsion
            Curve Torsion
            Setter for property Torsion
            Curve Torsion

            """
            pass
        @property
        def Curvature(self) -> float:
            """
            Getter for property Curvature
            Curvature of the Curve

            """
            pass
        @Curvature.setter
        def Curvature(self, value: float):
            """
            Getter for property Curvature
            Curvature of the Curve
            Setter for property Curvature
            Curvature of the Curve

            """
            pass
    class Face:
        """
         Face Geometric Properties 
         GeometricPropertiesFace_Struct NXOpen.Geom is an alias for  GeometricProperties.Face NXOpen.Geom.
        """
        @property
        def UParamater(self) -> float:
            """
            Getter for property UParamater
            U parameter

            """
            pass
        @UParamater.setter
        def UParamater(self, value: float):
            """
            Getter for property UParamater
            U parameter
            Setter for property UParamater
            U parameter

            """
            pass
        @property
        def VParamater(self) -> float:
            """
            Getter for property VParamater
            V parameter

            """
            pass
        @VParamater.setter
        def VParamater(self, value: float):
            """
            Getter for property VParamater
            V parameter
            Setter for property VParamater
            V parameter

            """
            pass
        @property
        def PositionInWcs(self) -> NXOpen.Point3d:
            """
            Getter for property PositionInWcs
            XYZ Position in Work Part coordinates

            """
            pass
        @PositionInWcs.setter
        def PositionInWcs(self, value: NXOpen.Point3d):
            """
            Getter for property PositionInWcs
            XYZ Position in Work Part coordinates
            Setter for property PositionInWcs
            XYZ Position in Work Part coordinates

            """
            pass
        @property
        def UDerivativeInWcs(self) -> NXOpen.Vector3d:
            """
            Getter for property UDerivativeInWcs
            Derivative Vector in U direction - Work Part  Coordinates

            """
            pass
        @UDerivativeInWcs.setter
        def UDerivativeInWcs(self, value: NXOpen.Vector3d):
            """
            Getter for property UDerivativeInWcs
            Derivative Vector in U direction - Work Part  Coordinates
            Setter for property UDerivativeInWcs
            Derivative Vector in U direction - Work Part  Coordinates

            """
            pass
        @property
        def VDerivativeInWcs(self) -> NXOpen.Vector3d:
            """
            Getter for property VDerivativeInWcs
            Derivative Vector in V direction - Work Part  Coordinates

            """
            pass
        @VDerivativeInWcs.setter
        def VDerivativeInWcs(self, value: NXOpen.Vector3d):
            """
            Getter for property VDerivativeInWcs
            Derivative Vector in V direction - Work Part  Coordinates
            Setter for property VDerivativeInWcs
            Derivative Vector in V direction - Work Part  Coordinates

            """
            pass
        @property
        def NormalInWcs(self) -> NXOpen.Vector3d:
            """
            Getter for property NormalInWcs
            Unitized Face Normal - Work Part Coordinates

            """
            pass
        @NormalInWcs.setter
        def NormalInWcs(self, value: NXOpen.Vector3d):
            """
            Getter for property NormalInWcs
            Unitized Face Normal - Work Part Coordinates
            Setter for property NormalInWcs
            Unitized Face Normal - Work Part Coordinates

            """
            pass
        @property
        def Position(self) -> NXOpen.Point3d:
            """
            Getter for property Position
            XYZ Position

            """
            pass
        @Position.setter
        def Position(self, value: NXOpen.Point3d):
            """
            Getter for property Position
            XYZ Position
            Setter for property Position
            XYZ Position

            """
            pass
        @property
        def UDerivative(self) -> NXOpen.Vector3d:
            """
            Getter for property UDerivative
            Derivative Vector in U direction -  Root Part Coordinates

            """
            pass
        @UDerivative.setter
        def UDerivative(self, value: NXOpen.Vector3d):
            """
            Getter for property UDerivative
            Derivative Vector in U direction -  Root Part Coordinates
            Setter for property UDerivative
            Derivative Vector in U direction -  Root Part Coordinates

            """
            pass
        @property
        def VDerivative(self) -> NXOpen.Vector3d:
            """
            Getter for property VDerivative
            Derivative Vector in V direction - Root Part  Coordinates

            """
            pass
        @VDerivative.setter
        def VDerivative(self, value: NXOpen.Vector3d):
            """
            Getter for property VDerivative
            Derivative Vector in V direction - Root Part  Coordinates
            Setter for property VDerivative
            Derivative Vector in V direction - Root Part  Coordinates

            """
            pass
        @property
        def Normal(self) -> NXOpen.Vector3d:
            """
            Getter for property Normal
            Unitized Face Normal - Root Part Coordinates

            """
            pass
        @Normal.setter
        def Normal(self, value: NXOpen.Vector3d):
            """
            Getter for property Normal
            Unitized Face Normal - Root Part Coordinates
            Setter for property Normal
            Unitized Face Normal - Root Part Coordinates

            """
            pass
        @property
        def InvOfMinRadiusOfCurvature(self) -> float:
            """
            Getter for property InvOfMinRadiusOfCurvature
            Inverse of Minumum  Radius of                                    Curvature, 1(minimum radius of curvature)

            """
            pass
        @InvOfMinRadiusOfCurvature.setter
        def InvOfMinRadiusOfCurvature(self, value: float):
            """
            Getter for property InvOfMinRadiusOfCurvature
            Inverse of Minumum  Radius of                                    Curvature, 1(minimum radius of curvature)
            Setter for property InvOfMinRadiusOfCurvature
            Inverse of Minumum  Radius of                                    Curvature, 1(minimum radius of curvature)

            """
            pass
        @property
        def InvOfMaxRadiusOfCurvature(self) -> float:
            """
            Getter for property InvOfMaxRadiusOfCurvature
            Inverse of Maximum Radius of                                    Curvature,  1(maximum radius of curvature).

            """
            pass
        @InvOfMaxRadiusOfCurvature.setter
        def InvOfMaxRadiusOfCurvature(self, value: float):
            """
            Getter for property InvOfMaxRadiusOfCurvature
            Inverse of Maximum Radius of                                    Curvature,  1(maximum radius of curvature).
            Setter for property InvOfMaxRadiusOfCurvature
            Inverse of Maximum Radius of                                    Curvature,  1(maximum radius of curvature).

            """
            pass
    @property
    def ObjectsForAnalysis(self) -> NXOpen.SelectObjectList:
        """
        Getter for property: ( NXOpen.SelectObjectList) ObjectsForAnalysis
         Returns the Objects for analysis   
            
         
        """
        pass
    @property
    def OutputMethod(self) -> GeometricProperties.OutputType:
        """
        Getter for property: ( GeometricProperties.OutputType NXOpen.Geom) OutputMethod
         Returns the output method   
            
         
        """
        pass
    @OutputMethod.setter
    def OutputMethod(self, output_method: GeometricProperties.OutputType):
        """
        Setter for property: ( GeometricProperties.OutputType NXOpen.Geom) OutputMethod
         Returns the output method   
            
         
        """
        pass
    def GetCaeCurveProperties(self, entityTag: NXOpen.NXObject, absPoint: NXOpen.Point3d) -> Tuple[GeometricProperties.Status, GeometricProperties.CaeCurve]:
        """
         Returns CAE curve local properties at the given point 
         Returns A tuple consisting of (status, caeCurve). 
         - status is:  GeometricProperties.Status NXOpen.Geom. Return status .
         - caeCurve is:  GeometricProperties.CaeCurve NXOpen.Geom. CAE EdgeCurve Properties .

        """
        pass
    def GetCaeFaceProperties(self, entityTag: NXOpen.NXObject, absPoint: NXOpen.Point3d) -> Tuple[GeometricProperties.Status, GeometricProperties.CaeFace]:
        """
         Returns CAE face local properties at the given point 
         Returns A tuple consisting of (status, caeFace). 
         - status is:  GeometricProperties.Status NXOpen.Geom. Return status .
         - caeFace is:  GeometricProperties.CaeFace NXOpen.Geom. CAE Face Properties .

        """
        pass
    def GetEdgeProperties(self, entityTag: NXOpen.NXObject, absPoint: NXOpen.Point3d) -> Tuple[GeometricProperties.Status, GeometricProperties.Edge]:
        """
         Returns edgecurve local properties at the given point 
         Returns A tuple consisting of (status, edge). 
         - status is:  GeometricProperties.Status NXOpen.Geom. Return status .
         - edge is:  GeometricProperties.Edge NXOpen.Geom. EdgeCurve Properties .

        """
        pass
    def GetFaceProperties(self, entityTag: NXOpen.NXObject, absPoint: NXOpen.Point3d) -> Tuple[GeometricProperties.Status, GeometricProperties.Face]:
        """
         Returns face local properties at the given point 
         Returns A tuple consisting of (status, face). 
         - status is:  GeometricProperties.Status NXOpen.Geom. Return status .
         - face is:  GeometricProperties.Face NXOpen.Geom. Face Properties .

        """
        pass
    @overload
    def ListProperties(self, entityTag: NXOpen.NXObject, absPoint: NXOpen.Point3d) -> GeometricProperties.Status:
        """
         Displays the local properties of the specified object at the
                      given point in the listing window 
         Returns status ( GeometricProperties.Status NXOpen.Geom):  Return status .
        """
        pass
    @overload
    def ListProperties(self, absPoint: NXOpen.Point3d) -> GeometricProperties.Status:
        """
         Displays the local properties of
                       ObjectsForAnalysis at the given point in 
                       the listing window.  
         Returns status ( GeometricProperties.Status NXOpen.Geom):  Return status .
        """
        pass
    def Reset(self) -> None:
        """
         Clears all markers showing the local geometric properties in the graphics window 
        """
        pass
import NXOpen
class HighlightLinesAnalysisBuilder(NXOpen.Builder): 
    """
    Represents a
    NXOpen.GeometricAnalysis.HighlightLinesAnalysis
    builder. Highlight Lines Analysis function can produce both reflection lines and projection
    lines which are used to evaluate the surface quality and continuity between adjacent surfaces.
    """
    class DisplayMethods(Enum):
        """
        Members Include: 
         |Reflection|  Create reflection lines 
         |Projection|  Create projection lines 

        """
        Reflection: int
        Projection: int
        @staticmethod
        def ValueOf(value: int) -> HighlightLinesAnalysisBuilder.DisplayMethods:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DisplayModes(Enum):
        """
        Members Include: 
         |Polyline|  Polyline 
         |ZebraMap|  Zebra Map 

        """
        Polyline: int
        ZebraMap: int
        @staticmethod
        def ValueOf(value: int) -> HighlightLinesAnalysisBuilder.DisplayModes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class IsoclineDirection(Enum):
        """
        Members Include: 
         |Vector|  vector; 
         |Orientation|  orientation; 

        """
        Vector: int
        Orientation: int
        @staticmethod
        def ValueOf(value: int) -> HighlightLinesAnalysisBuilder.IsoclineDirection:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LightPlacements(Enum):
        """
        Members Include: 
         |Uniform|  Uniform: Lights are placed uniformly on light plane 
         |ThroughPoints|  Through Points: A highlight line is guaranteed to pass through a surface point. 
         |BetweenPoints|  Between Points: Two highlight lines are guaranteed to
                pass through two given surface points. More highlight lines
                are created between these two highlight lines when light
                number is more than two. 

        """
        Uniform: int
        ThroughPoints: int
        BetweenPoints: int
        @staticmethod
        def ValueOf(value: int) -> HighlightLinesAnalysisBuilder.LightPlacements:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LightPlaneOptions(Enum):
        """
        Members Include: 
         |YZ|  Uses YC-ZC plane as light plane 
         |ZX|  Uses XC-ZC plane as light plane 
         |XY|  Uses XC-YC plane as light plane 
         |Arbitrary|  Uses an arbitrary plane as light plane 

        """
        YZ: int
        ZX: int
        XY: int
        Arbitrary: int
        @staticmethod
        def ValueOf(value: int) -> HighlightLinesAnalysisBuilder.LightPlaneOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OutputOption(Enum):
        """
        Members Include: 
         |AnalysisObject|  Analysis Object 
         |HighlightCurves|  Highlight Curves 
         |Both|  Both Analysis Object and Highlight Curves 

        """
        AnalysisObject: int
        HighlightCurves: int
        Both: int
        @staticmethod
        def ValueOf(value: int) -> HighlightLinesAnalysisBuilder.OutputOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Resolutions(Enum):
        """
        Members Include: 
         |Coarse|  Coarse 
         |Standard|  Standard 
         |Fine|  Fine 
         |ExtraFine|  Extra Fine 
         |SuperFine|  Super Fine 
         |UltraFine|  Ultra Fine 

        """
        Coarse: int
        Standard: int
        Fine: int
        ExtraFine: int
        SuperFine: int
        UltraFine: int
        @staticmethod
        def ValueOf(value: int) -> HighlightLinesAnalysisBuilder.Resolutions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |Uniform|  Uniform: Lights are placed uniformly on light plane 
         |ThroughPoints|  Through Points: A highlight line is guaranteed to pass through a surface point. 
         |BetweenPoints|  Between Points: Two highlight lines are guaranteed to
                pass through two given surface points. More highlight lines
                are created between these two highlight lines when light
                number is more than two. 

        """
        Uniform: int
        ThroughPoints: int
        BetweenPoints: int
        @staticmethod
        def ValueOf(value: int) -> HighlightLinesAnalysisBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types2(Enum):
        """
        Members Include: 
         |Reflection|  Create reflection lines 
         |Projection|  Create projection lines 
         |Isoclines|  Create isoclines 
         |Zebra|  Create zebra contour lines 

        """
        Reflection: int
        Projection: int
        Isoclines: int
        Zebra: int
        @staticmethod
        def ValueOf(value: int) -> HighlightLinesAnalysisBuilder.Types2:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BetweenPoints(self) -> NXOpen.SelectPointList:
        """
        Getter for property: ( NXOpen.SelectPointList) BetweenPoints
         Returns the between points   
            
         
        """
        pass
    @property
    def DisplayMethod(self) -> HighlightLinesAnalysisBuilder.DisplayMethods:
        """
        Getter for property: ( HighlightLinesAnalysisBuilder.DisplayMethods NXOpen.Geom) DisplayMethod
         Returns the display method   
            
         
        """
        pass
    @DisplayMethod.setter
    def DisplayMethod(self, displayMethod: HighlightLinesAnalysisBuilder.DisplayMethods):
        """
        Setter for property: ( HighlightLinesAnalysisBuilder.DisplayMethods NXOpen.Geom) DisplayMethod
         Returns the display method   
            
         
        """
        pass
    @property
    def DisplayMode(self) -> HighlightLinesAnalysisBuilder.DisplayModes:
        """
        Getter for property: ( HighlightLinesAnalysisBuilder.DisplayModes NXOpen.Geom) DisplayMode
         Returns the analysis display   
            
         
        """
        pass
    @DisplayMode.setter
    def DisplayMode(self, display: HighlightLinesAnalysisBuilder.DisplayModes):
        """
        Setter for property: ( HighlightLinesAnalysisBuilder.DisplayModes NXOpen.Geom) DisplayMode
         Returns the analysis display   
            
         
        """
        pass
    @property
    def EndIsoAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndIsoAngle
         Returns the end angle for isoclines (uniform)   
            
         
        """
        pass
    @property
    def Faces(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) Faces
         Returns the face list   
            
         
        """
        pass
    @property
    def IsReflectionLocked(self) -> bool:
        """
        Getter for property: (bool) IsReflectionLocked
         Returns the lock reflection.  
           When the lock is on, the reflection lines will be freezed
                while the view is changing. Otherwise, the reflection lines
                will be updated continuously while view is changing.   
         
        """
        pass
    @IsReflectionLocked.setter
    def IsReflectionLocked(self, isReflectionLocked: bool):
        """
        Setter for property: (bool) IsReflectionLocked
         Returns the lock reflection.  
           When the lock is on, the reflection lines will be freezed
                while the view is changing. Otherwise, the reflection lines
                will be updated continuously while view is changing.   
         
        """
        pass
    @property
    def IsoclineOption(self) -> HighlightLinesAnalysisBuilder.IsoclineDirection:
        """
        Getter for property: ( HighlightLinesAnalysisBuilder.IsoclineDirection NXOpen.Geom) IsoclineOption
         Returns the isocline reference direction   
            
         
        """
        pass
    @IsoclineOption.setter
    def IsoclineOption(self, option: HighlightLinesAnalysisBuilder.IsoclineDirection):
        """
        Setter for property: ( HighlightLinesAnalysisBuilder.IsoclineDirection NXOpen.Geom) IsoclineOption
         Returns the isocline reference direction   
            
         
        """
        pass
    @property
    def IsoclineOrientation(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: ( NXOpen.Matrix3x3) IsoclineOrientation
         Returns the isocline orirentation   
            
         
        """
        pass
    @IsoclineOrientation.setter
    def IsoclineOrientation(self, isoclineOrientation: NXOpen.Matrix3x3):
        """
        Setter for property: ( NXOpen.Matrix3x3) IsoclineOrientation
         Returns the isocline orirentation   
            
         
        """
        pass
    @property
    def IsoclineOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) IsoclineOrigin
         Returns the isocline origin   
            
         
        """
        pass
    @IsoclineOrigin.setter
    def IsoclineOrigin(self, isoclineOrigin: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) IsoclineOrigin
         Returns the isocline origin   
            
         
        """
        pass
    @property
    def IsoclineVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) IsoclineVector
         Returns the vector to define isoclines   
            
         
        """
        pass
    @IsoclineVector.setter
    def IsoclineVector(self, isoclineVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) IsoclineVector
         Returns the vector to define isoclines   
            
         
        """
        pass
    @property
    def LightDiffuseness(self) -> float:
        """
        Getter for property: (float) LightDiffuseness
         Returns the ratio of blended texels to all light texels.  
           It is used by reflection contours   
         
        """
        pass
    @LightDiffuseness.setter
    def LightDiffuseness(self, lightDiffuseness: float):
        """
        Setter for property: (float) LightDiffuseness
         Returns the ratio of blended texels to all light texels.  
           It is used by reflection contours   
         
        """
        pass
    @property
    def LightNumber(self) -> int:
        """
        Getter for property: (int) LightNumber
         Returns the number of lights.  
           It's used by Uniform type and Between Points type.   
         
        """
        pass
    @LightNumber.setter
    def LightNumber(self, lightNumber: int):
        """
        Setter for property: (int) LightNumber
         Returns the number of lights.  
           It's used by Uniform type and Between Points type.   
         
        """
        pass
    @property
    def LightPlacement(self) -> HighlightLinesAnalysisBuilder.LightPlacements:
        """
        Getter for property: ( HighlightLinesAnalysisBuilder.LightPlacements NXOpen.Geom) LightPlacement
         Returns the light placement   
            
         
        """
        pass
    @LightPlacement.setter
    def LightPlacement(self, placement: HighlightLinesAnalysisBuilder.LightPlacements):
        """
        Setter for property: ( HighlightLinesAnalysisBuilder.LightPlacements NXOpen.Geom) LightPlacement
         Returns the light placement   
            
         
        """
        pass
    @property
    def LightPlaneOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) LightPlaneOrigin
         Returns the origin of the light plane   
            
         
        """
        pass
    @property
    def LightPlaneXAxis(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) LightPlaneXAxis
         Returns the x-axis of the light plane   
            
         
        """
        pass
    @property
    def LightPlaneYAxis(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) LightPlaneYAxis
         Returns the y-axis of the light plane   
            
         
        """
        pass
    @property
    def LightSpacing(self) -> float:
        """
        Getter for property: (float) LightSpacing
         Returns the light spacing between two adjacent lights.  
           It's used by Uniform type   
         
        """
        pass
    @LightSpacing.setter
    def LightSpacing(self, lightSpacing: float):
        """
        Setter for property: (float) LightSpacing
         Returns the light spacing between two adjacent lights.  
           It's used by Uniform type   
         
        """
        pass
    @property
    def LightWidth(self) -> float:
        """
        Getter for property: (float) LightWidth
         Returns the ratio of light size to light spacing.  
           It is used by reflection contours   
         
        """
        pass
    @LightWidth.setter
    def LightWidth(self, lightWidth: float):
        """
        Setter for property: (float) LightWidth
         Returns the ratio of light size to light spacing.  
           It is used by reflection contours   
         
        """
        pass
    @property
    def Output(self) -> HighlightLinesAnalysisBuilder.OutputOption:
        """
        Getter for property: ( HighlightLinesAnalysisBuilder.OutputOption NXOpen.Geom) Output
         Returns the output   
            
         
        """
        pass
    @Output.setter
    def Output(self, output: HighlightLinesAnalysisBuilder.OutputOption):
        """
        Setter for property: ( HighlightLinesAnalysisBuilder.OutputOption NXOpen.Geom) Output
         Returns the output   
            
         
        """
        pass
    @property
    def Resolution(self) -> HighlightLinesAnalysisBuilder.Resolutions:
        """
        Getter for property: ( HighlightLinesAnalysisBuilder.Resolutions NXOpen.Geom) Resolution
         Returns the resolution.  
             
         
        """
        pass
    @Resolution.setter
    def Resolution(self, resolution: HighlightLinesAnalysisBuilder.Resolutions):
        """
        Setter for property: ( HighlightLinesAnalysisBuilder.Resolutions NXOpen.Geom) Resolution
         Returns the resolution.  
             
         
        """
        pass
    @property
    def StartIsoAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartIsoAngle
         Returns the start angle for isoclines (uniform)   
            
         
        """
        pass
    @property
    def ThroughPoints(self) -> NXOpen.SelectPointList:
        """
        Getter for property: ( NXOpen.SelectPointList) ThroughPoints
         Returns the through points   
            
         
        """
        pass
    @property
    def Type(self) -> HighlightLinesAnalysisBuilder.Types:
        """
        Getter for property: ( HighlightLinesAnalysisBuilder.Types NXOpen.Geom) Type
         Returns the type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: HighlightLinesAnalysisBuilder.Types):
        """
        Setter for property: ( HighlightLinesAnalysisBuilder.Types NXOpen.Geom) Type
         Returns the type   
            
         
        """
        pass
    @property
    def Type2(self) -> HighlightLinesAnalysisBuilder.Types2:
        """
        Getter for property: ( HighlightLinesAnalysisBuilder.Types2 NXOpen.Geom) Type2
         Returns the display type   
            
         
        """
        pass
    @Type2.setter
    def Type2(self, type: HighlightLinesAnalysisBuilder.Types2):
        """
        Setter for property: ( HighlightLinesAnalysisBuilder.Types2 NXOpen.Geom) Type2
         Returns the display type   
            
         
        """
        pass
    def GetBrightColor(self) -> List[float]:
        """
         Gets the color of the bright (lit) areas of reflection contours 
         Returns brightColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def GetDarkColor(self) -> List[float]:
        """
         Gets the color of the dark (unlit) areas of reflection contours 
         Returns darkColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def ReinitializePlane(self) -> None:
        """
         Reinitialize light plane based on the selected faces. If
                more faces are selected, you may need to change
                light plane, so the light plane could be better centered. 
        """
        pass
    def SetBrightColor(self, brightColor: List[float]) -> None:
        """
         Sets the color of the bright (lit) areas of reflection contours 
        """
        pass
    def SetDarkColor(self, darkColor: List[float]) -> None:
        """
         Sets the color of the dark (unlit) areas of reflection contours 
        """
        pass
    def SetLightPlaneOrigin(self, origin: NXOpen.Point3d) -> None:
        """
         Sets the origin of the light plane. 
        """
        pass
    def SetLightPlaneXAxis(self, xAxis: NXOpen.Vector3d) -> None:
        """
         Sets the x-axis of the light plane. 
        """
        pass
    def SetLightPlaneYAxis(self, yAxis: NXOpen.Vector3d) -> None:
        """
         Sets the y-axis of the light plane. 
        """
        pass
class HighlightLinesAnalysis(AnalysisObject): 
    """ Represents a Highlight Lines Analysis object. Highlight Lines
    Analysis function can produce both reflection lines and projection
    lines which are used to evaluate the surface quality and
    continuity between adjacent surfaces. """
    pass
import NXOpen
import NXOpen.Features
class LocalRadiusAnalysisBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.GeometricAnalysis.LocalRadiusAnalysis builder """
    @property
    def SelectionPoint(self) -> NXOpen.Features.GeometricConstraintDataManager:
        """
        Getter for property: ( NXOpen.Features.GeometricConstraintDataManager) SelectionPoint
         Returns the selection point   
            
         
        """
        pass
    @property
    def VisibilityCoordinates(self) -> bool:
        """
        Getter for property: (bool) VisibilityCoordinates
         Returns the toggle coordinates   
            
         
        """
        pass
    @VisibilityCoordinates.setter
    def VisibilityCoordinates(self, visibilityCoordinates: bool):
        """
        Setter for property: (bool) VisibilityCoordinates
         Returns the toggle coordinates   
            
         
        """
        pass
    @property
    def VisibilityMaxRadius(self) -> bool:
        """
        Getter for property: (bool) VisibilityMaxRadius
         Returns the toggle max radius show   
            
         
        """
        pass
    @VisibilityMaxRadius.setter
    def VisibilityMaxRadius(self, visibilityMaxRadius: bool):
        """
        Setter for property: (bool) VisibilityMaxRadius
         Returns the toggle max radius show   
            
         
        """
        pass
    @property
    def VisibilityMinMaxRadiusTangent(self) -> bool:
        """
        Getter for property: (bool) VisibilityMinMaxRadiusTangent
         Returns the toggle min radius tangent   
            
         
        """
        pass
    @VisibilityMinMaxRadiusTangent.setter
    def VisibilityMinMaxRadiusTangent(self, visibilityMinMaxRadiusTangent: bool):
        """
        Setter for property: (bool) VisibilityMinMaxRadiusTangent
         Returns the toggle min radius tangent   
            
         
        """
        pass
    @property
    def VisibilityMinRadius(self) -> bool:
        """
        Getter for property: (bool) VisibilityMinRadius
         Returns the toggle min radius show   
            
         
        """
        pass
    @VisibilityMinRadius.setter
    def VisibilityMinRadius(self, visibilityMinRadius: bool):
        """
        Setter for property: (bool) VisibilityMinRadius
         Returns the toggle min radius show   
            
         
        """
        pass
    @property
    def VisibilityRadius(self) -> bool:
        """
        Getter for property: (bool) VisibilityRadius
         Returns the toggle radius show   
            
         
        """
        pass
    @VisibilityRadius.setter
    def VisibilityRadius(self, visibilityRadius: bool):
        """
        Setter for property: (bool) VisibilityRadius
         Returns the toggle radius show   
            
         
        """
        pass
    @property
    def VisibilityURadius(self) -> bool:
        """
        Getter for property: (bool) VisibilityURadius
         Returns the toggle uradius show   
            
         
        """
        pass
    @VisibilityURadius.setter
    def VisibilityURadius(self, visibilityURadius: bool):
        """
        Setter for property: (bool) VisibilityURadius
         Returns the toggle uradius show   
            
         
        """
        pass
    @property
    def VisibilityUV(self) -> bool:
        """
        Getter for property: (bool) VisibilityUV
         Returns the toggle uv   
            
         
        """
        pass
    @VisibilityUV.setter
    def VisibilityUV(self, visibilityUV: bool):
        """
        Setter for property: (bool) VisibilityUV
         Returns the toggle uv   
            
         
        """
        pass
    @property
    def VisibilityUVTangent(self) -> bool:
        """
        Getter for property: (bool) VisibilityUVTangent
         Returns the toggle max radius tangent   
            
         
        """
        pass
    @VisibilityUVTangent.setter
    def VisibilityUVTangent(self, visibilityUVTangent: bool):
        """
        Setter for property: (bool) VisibilityUVTangent
         Returns the toggle max radius tangent   
            
         
        """
        pass
    @property
    def VisibilityVRadius(self) -> bool:
        """
        Getter for property: (bool) VisibilityVRadius
         Returns the toggle vradius show   
            
         
        """
        pass
    @VisibilityVRadius.setter
    def VisibilityVRadius(self, visibilityVRadius: bool):
        """
        Setter for property: (bool) VisibilityVRadius
         Returns the toggle vradius show   
            
         
        """
        pass
    def ButtonOpenInformationWindow(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
class LocalRadiusAnalysis(AnalysisObject): 
    """ Builder for Local Radius Analysis (formerly Dynamic Radius) """
    pass
import NXOpen
import NXOpen.DesignSimulation
class PerformancePredictorBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.GeometricAnalysis.PerformancePredictorBuilder """
    @property
    def Study(self) -> NXOpen.DesignSimulation.StudyBuilder:
        """
        Getter for property: ( NXOpen.DesignSimulation.StudyBuilder) Study
         Returns the study builder  
            
         
        """
        pass
import NXOpen
import NXOpen.DesignSimulation
class PerformancePredictor(AnalysisObject): 
    """ Represents a NXOpen.GeometricAnalysis.PerformancePredictor """
    class SolveOption(Enum):
        """
        Members Include: 
         |Foreground|  Analysis will run in the foreground so that the user needs to wait during processing. 
         |Background|  Analysis will run in the background so that the user can proceed working with NX. 

        """
        Foreground: int
        Background: int
        @staticmethod
        def ValueOf(value: int) -> PerformancePredictor.SolveOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Study(self) -> NXOpen.DesignSimulation.Study:
        """
        Getter for property: ( NXOpen.DesignSimulation.Study) Study
         Returns the active study of Performance Predictor   
            
         
        """
        pass
    def Activate(self) -> None:
        """
         Activates Performance Predictor
        """
        pass
    def Analyze(self, solveOption: PerformancePredictor.SolveOption) -> None:
        """
         Solves this NXOpen.GeometricAnalysis.PerformancePredictor if the analysis is fully setup and ready to solve.
                This method will return after pre-processing and launching the analysis process depending on the NXOpen.GeometricAnalysis.PerformancePredictor.SolveOption passed in this method.
                
        """
        pass
    def CloneSimulation(self) -> PerformancePredictor:
        """
         Clones (copies) a NXOpen.GeometricAnalysis.PerformancePredictor object and returns the cloned (copied) object if successful. 
         Returns clonedSolution ( PerformancePredictor NXOpen.Geom): .
        """
        pass
    def Deactivate(self) -> None:
        """
         Deactivates Performance Predictor
        """
        pass
    def FindObject(self, journalIdentifier: str) -> NXOpen.INXObject:
        """
         Finds the NXOpen.DesignSimulation.Study with the given identifier.
                    An exception will be thrown if no object can be found with given name. 
         Returns study ( NXOpen.INXObject):  An object matching the journal identifier. .
        """
        pass
    def RemoveResults(self) -> None:
        """
         Remove results from Performance Predictor
        """
        pass
import NXOpen
import NXOpen.Features
class RadiusAnalysisBuilder1(NXOpen.Builder): 
    """ Represents a Radius Analysis builder. """
    class DisplayModes(Enum):
        """
        Members Include: 
         |Fringe|  Display in fringe. 
         |Hedgehog|  Display in hedgehog. 
         |ContourLines|  Display in contour lines. 

        """
        Fringe: int
        Hedgehog: int
        ContourLines: int
        @staticmethod
        def ValueOf(value: int) -> RadiusAnalysisBuilder1.DisplayModes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |Gaussian|  Gaussian radius. 
         |Minimum|  Minimum radius. 
         |Maximum|  Maximum radius. 
         |Mean|  Mean radius. 
         |Normal|  Normal radius. 
         |Sectional|  Sectional radius. 
         |U|  Radius in U direction. 
         |V|  Radius in V direction. 

        """
        Gaussian: int
        Minimum: int
        Maximum: int
        Mean: int
        Normal: int
        Sectional: int
        U: int
        V: int
        @staticmethod
        def ValueOf(value: int) -> RadiusAnalysisBuilder1.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DataRange(self) -> FaceAnalysisDataRangeBuilder:
        """
        Getter for property: ( FaceAnalysisDataRangeBuilder NXOpen.Geom) DataRange
         Returns the radius analysis data range.  
             
         
        """
        pass
    @property
    def DisplayMode(self) -> RadiusAnalysisBuilder1.DisplayModes:
        """
        Getter for property: ( RadiusAnalysisBuilder1.DisplayModes NXOpen.Geom) DisplayMode
         Returns the display mode.  
             
         
        """
        pass
    @DisplayMode.setter
    def DisplayMode(self, displayMode: RadiusAnalysisBuilder1.DisplayModes):
        """
        Setter for property: ( RadiusAnalysisBuilder1.DisplayModes NXOpen.Geom) DisplayMode
         Returns the display mode.  
             
         
        """
        pass
    @property
    def DisplaySettings(self) -> FaceAnalysisDisplayBuilder:
        """
        Getter for property: ( FaceAnalysisDisplayBuilder NXOpen.Geom) DisplaySettings
         Returns the radius analysis display settings.  
             
         
        """
        pass
    @property
    def DynamicLabel(self) -> NXOpen.Features.GeometricConstraintDataManager:
        """
        Getter for property: ( NXOpen.Features.GeometricConstraintDataManager) DynamicLabel
         Returns the dynamic label   
            
         
        """
        pass
    @property
    def Faces(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) Faces
         Returns the face to apply radius analysis.  
             
         
        """
        pass
    @property
    def Normals(self) -> FaceAnalysisNormalsBuilder:
        """
        Getter for property: ( FaceAnalysisNormalsBuilder NXOpen.Geom) Normals
         Returns the radius analysis normals.  
             
         
        """
        pass
    @property
    def NumberOfContourLines(self) -> int:
        """
        Getter for property: (int) NumberOfContourLines
         Returns the number of contour lines.  
             
         
        """
        pass
    @NumberOfContourLines.setter
    def NumberOfContourLines(self, numberOfContourLines: int):
        """
        Setter for property: (int) NumberOfContourLines
         Returns the number of contour lines.  
             
         
        """
        pass
    @property
    def Plane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) Plane
         Returns the reference plane used for  NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1::TypesSectional .  
             
         
        """
        pass
    @Plane.setter
    def Plane(self, plane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) Plane
         Returns the reference plane used for  NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1::TypesSectional .  
             
         
        """
        pass
    @property
    def SpikeLength(self) -> float:
        """
        Getter for property: (float) SpikeLength
         Returns the spike length.  
             
         
        """
        pass
    @SpikeLength.setter
    def SpikeLength(self, spikeLength: float):
        """
        Setter for property: (float) SpikeLength
         Returns the spike length.  
             
         
        """
        pass
    @property
    def Type(self) -> RadiusAnalysisBuilder1.Types:
        """
        Getter for property: ( RadiusAnalysisBuilder1.Types NXOpen.Geom) Type
         Returns the radius type.  
             
         
        """
        pass
    @Type.setter
    def Type(self, type: RadiusAnalysisBuilder1.Types):
        """
        Setter for property: ( RadiusAnalysisBuilder1.Types NXOpen.Geom) Type
         Returns the radius type.  
             
         
        """
        pass
    @property
    def Vector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) Vector
         Returns the reference vector for  NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1::TypesNormal .  
             
         
        """
        pass
    @Vector.setter
    def Vector(self, vector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) Vector
         Returns the reference vector for  NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1::TypesNormal .  
             
         
        """
        pass
    def StartRadiusAnalysis(self) -> None:
        """
         Start radius analysis. 
        """
        pass
    def UpdateDisplayOnPlaneChange(self) -> None:
        """
         Update display after plane changes. 
        """
        pass
import NXOpen
import NXOpen.Features
class RadiusAnalysisBuilder(NXOpen.Builder): 
    """ Represents a Radius Analysis builder. """
    class DisplayModes(Enum):
        """
        Members Include: 
         |Fringe|  Display in fringe. 
         |Hedgehog|  Display in hedgehog. 
         |ContourLines|  Display in contour lines. 

        """
        Fringe: int
        Hedgehog: int
        ContourLines: int
        @staticmethod
        def ValueOf(value: int) -> RadiusAnalysisBuilder.DisplayModes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |Gaussian|  Gaussian radius. 
         |Minimum|  Minimum radius. 
         |Maximum|  Maximum radius. 
         |Mean|  Mean radius. 
         |Normal|  Normal radius. 
         |Sectional|  Sectional radius. 
         |U|  Radius in U direction. 
         |V|  Radius in V direction. 

        """
        Gaussian: int
        Minimum: int
        Maximum: int
        Mean: int
        Normal: int
        Sectional: int
        U: int
        V: int
        @staticmethod
        def ValueOf(value: int) -> RadiusAnalysisBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DataRange(self) -> FaceAnalysisDataRangeBuilder:
        """
        Getter for property: ( FaceAnalysisDataRangeBuilder NXOpen.Geom) DataRange
         Returns the radius analysis data range.  
             
         
        """
        pass
    @property
    def DisplayMode(self) -> RadiusAnalysisBuilder.DisplayModes:
        """
        Getter for property: ( RadiusAnalysisBuilder.DisplayModes NXOpen.Geom) DisplayMode
         Returns the display mode.  
             
         
        """
        pass
    @DisplayMode.setter
    def DisplayMode(self, displayMode: RadiusAnalysisBuilder.DisplayModes):
        """
        Setter for property: ( RadiusAnalysisBuilder.DisplayModes NXOpen.Geom) DisplayMode
         Returns the display mode.  
             
         
        """
        pass
    @property
    def DisplaySettings(self) -> FaceAnalysisDisplayBuilder:
        """
        Getter for property: ( FaceAnalysisDisplayBuilder NXOpen.Geom) DisplaySettings
         Returns the radius analysis display settings.  
             
         
        """
        pass
    @property
    def DynamicLabel(self) -> NXOpen.Features.GeometricConstraintDataManager:
        """
        Getter for property: ( NXOpen.Features.GeometricConstraintDataManager) DynamicLabel
         Returns the dynamic label   
            
         
        """
        pass
    @property
    def Faces(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) Faces
         Returns the face to apply radius analysis.  
             
         
        """
        pass
    @property
    def Normals(self) -> FaceAnalysisNormalsBuilder:
        """
        Getter for property: ( FaceAnalysisNormalsBuilder NXOpen.Geom) Normals
         Returns the radius analysis normals.  
             
         
        """
        pass
    @property
    def NumberOfContourLines(self) -> int:
        """
        Getter for property: (int) NumberOfContourLines
         Returns the number of contour lines.  
             
         
        """
        pass
    @NumberOfContourLines.setter
    def NumberOfContourLines(self, numberOfContourLines: int):
        """
        Setter for property: (int) NumberOfContourLines
         Returns the number of contour lines.  
             
         
        """
        pass
    @property
    def Plane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) Plane
         Returns the reference plane used for  NXOpen::GeometricAnalysis::RadiusAnalysisBuilder::TypesSectional .  
             
         
        """
        pass
    @Plane.setter
    def Plane(self, plane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) Plane
         Returns the reference plane used for  NXOpen::GeometricAnalysis::RadiusAnalysisBuilder::TypesSectional .  
             
         
        """
        pass
    @property
    def SpikeLength(self) -> float:
        """
        Getter for property: (float) SpikeLength
         Returns the spike length.  
             
         
        """
        pass
    @SpikeLength.setter
    def SpikeLength(self, spikeLength: float):
        """
        Setter for property: (float) SpikeLength
         Returns the spike length.  
             
         
        """
        pass
    @property
    def Type(self) -> RadiusAnalysisBuilder.Types:
        """
        Getter for property: ( RadiusAnalysisBuilder.Types NXOpen.Geom) Type
         Returns the radius type.  
             
         
        """
        pass
    @Type.setter
    def Type(self, type: RadiusAnalysisBuilder.Types):
        """
        Setter for property: ( RadiusAnalysisBuilder.Types NXOpen.Geom) Type
         Returns the radius type.  
             
         
        """
        pass
    @property
    def Vector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) Vector
         Returns the reference vector for  NXOpen::GeometricAnalysis::RadiusAnalysisBuilder::TypesNormal .  
             
         
        """
        pass
    @Vector.setter
    def Vector(self, vector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) Vector
         Returns the reference vector for  NXOpen::GeometricAnalysis::RadiusAnalysisBuilder::TypesNormal .  
             
         
        """
        pass
    def StartRadiusAnalysis(self) -> None:
        """
         Start radius analysis. 
        """
        pass
    def UpdateDisplayOnPlaneChange(self) -> None:
        """
         Update display after plane changes. 
        """
        pass
class RadiusAnalysis(AnalysisObject): 
    """ Represents a Radius analysis  """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class ReflectionAnalysisBuilder1(NXOpen.Builder): 
    """ Represents a Reflection Analysis builder. """
    class ImageMovementTypes(Enum):
        """
        Members Include: 
         |Horizontal|  Move image in horizonal direction. 
         |Vertical|  Move image in vertical direction. 
         |Rotate|  Rotate image. 

        """
        Horizontal: int
        Vertical: int
        Rotate: int
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder1.ImageMovementTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ImageSizeOption(Enum):
        """
        Members Include: 
         |KeepCurrent|  Keep current size. 
         |ReduceScale|  Reduce scale size. 

        """
        KeepCurrent: int
        ReduceScale: int
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder1.ImageSizeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LineImageTypes(Enum):
        """
        Members Include: 
         |BlackLines|  Black lines. 
         |BlackandWhiteLines|  Black and lines. 
         |ColoredLines|  Colored lines. 

        """
        BlackLines: int
        BlackandWhiteLines: int
        ColoredLines: int
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder1.LineImageTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LineOrientationType(Enum):
        """
        Members Include: 
         |Horizontal|  Horizontal. 
         |Vertical|  Vertical. 
         |Both|  Both horizontal and vertical. 

        """
        Horizontal: int
        Vertical: int
        Both: int
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder1.LineOrientationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LineThicknessType(Enum):
        """
        Members Include: 
         |Thin|  Thin. 
         |Normal|  Normal. 
         |Thick|  Thick. 

        """
        Thin: int
        Normal: int
        Thick: int
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder1.LineThicknessType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class NumberOfLinesOptions(Enum):
        """
        Members Include: 
         |One|  1 reflection line. 
         |Two|  2 reflection line. 
         |Four|  4 reflection line. 
         |Eight|  8 reflection line. 
         |Sixteen|  16 reflection line. 
         |ThirtyTwo|  32 reflection line. 
         |SixtyFour|  64 reflection line. 
         |OneTwoEight|  128 reflection line. 
         |TwoFiveSix|  256 reflection line. 

        """
        One: int
        Two: int
        Four: int
        Eight: int
        Sixteen: int
        ThirtyTwo: int
        SixtyFour: int
        OneTwoEight: int
        TwoFiveSix: int
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder1.NumberOfLinesOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SceneImageType(Enum):
        """
        Members Include: 
         |SimulatedHorizon|  Simulated horizon. 
         |PhotoHorizon|  Photo horizon. 
         |SphericalRoom|  Spherical room. 
         |SphericalLightTubesRoom|  Spherical light tubes room. 
         |DaytimeHorizon|  Daytime horizon. 
         |MagentaSunset|  Magenta sunset. 
         |SphericalHorizon|  Spherical horizon. 
         |CylindricalRoom|  Cylindrical room. 
         |MonochromeHorizon|  Monochrome horizon. 
         |SmoothGrayScale|  Smooth gray scale. 
         |SharpGrayScale|  Sharp gray scale. 
         |SphericalTubes|  Spherical tubes. 

        """
        SimulatedHorizon: int
        PhotoHorizon: int
        SphericalRoom: int
        SphericalLightTubesRoom: int
        DaytimeHorizon: int
        MagentaSunset: int
        SphericalHorizon: int
        CylindricalRoom: int
        MonochromeHorizon: int
        SmoothGrayScale: int
        SharpGrayScale: int
        SphericalTubes: int
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder1.SceneImageType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |LineImages|  Line image. 
         |SceneImages|  Scene image. 
         |ImageFromFile|  Image from file. 

        """
        LineImages: int
        SceneImages: int
        ImageFromFile: int
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder1.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DisplayResolution(self) -> NXOpen.GeometricUtilities.DisplayResolutionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.DisplayResolutionBuilder) DisplayResolution
         Returns the display resolution.  
             
         
        """
        pass
    @property
    def FaceReflectivityScale(self) -> int:
        """
        Getter for property: (int) FaceReflectivityScale
         Returns the face reflectivity scale from 0 to 100.  
             
         
        """
        pass
    @FaceReflectivityScale.setter
    def FaceReflectivityScale(self, faceReflectivityScale: int):
        """
        Setter for property: (int) FaceReflectivityScale
         Returns the face reflectivity scale from 0 to 100.  
             
         
        """
        pass
    @property
    def Faces(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) Faces
         Returns the face to apply reflection analysis.  
             
         
        """
        pass
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
         Returns the file browser.  
             
         
        """
        pass
    @FileName.setter
    def FileName(self, filename: str):
        """
        Setter for property: (str) FileName
         Returns the file browser.  
             
         
        """
        pass
    @property
    def ImageMovementType(self) -> ReflectionAnalysisBuilder1.ImageMovementTypes:
        """
        Getter for property: ( ReflectionAnalysisBuilder1.ImageMovementTypes NXOpen.Geom) ImageMovementType
         Returns the orientation to move reflection lines.  
             
         
        """
        pass
    @ImageMovementType.setter
    def ImageMovementType(self, imageMovementType: ReflectionAnalysisBuilder1.ImageMovementTypes):
        """
        Setter for property: ( ReflectionAnalysisBuilder1.ImageMovementTypes NXOpen.Geom) ImageMovementType
         Returns the orientation to move reflection lines.  
             
         
        """
        pass
    @property
    def ImagePosition(self) -> int:
        """
        Getter for property: (int) ImagePosition
         Returns the moving image scale.  
             
         
        """
        pass
    @ImagePosition.setter
    def ImagePosition(self, imagePosition: int):
        """
        Setter for property: (int) ImagePosition
         Returns the moving image scale.  
             
         
        """
        pass
    @property
    def ImageSizeSetting(self) -> ReflectionAnalysisBuilder1.ImageSizeOption:
        """
        Getter for property: ( ReflectionAnalysisBuilder1.ImageSizeOption NXOpen.Geom) ImageSizeSetting
         Returns the image size setting.  
             
         
        """
        pass
    @ImageSizeSetting.setter
    def ImageSizeSetting(self, imageSizeSetting: ReflectionAnalysisBuilder1.ImageSizeOption):
        """
        Setter for property: ( ReflectionAnalysisBuilder1.ImageSizeOption NXOpen.Geom) ImageSizeSetting
         Returns the image size setting.  
             
         
        """
        pass
    @property
    def LineImageType(self) -> ReflectionAnalysisBuilder1.LineImageTypes:
        """
        Getter for property: ( ReflectionAnalysisBuilder1.LineImageTypes NXOpen.Geom) LineImageType
         Returns the image type.  
             
         
        """
        pass
    @LineImageType.setter
    def LineImageType(self, lineImageType: ReflectionAnalysisBuilder1.LineImageTypes):
        """
        Setter for property: ( ReflectionAnalysisBuilder1.LineImageTypes NXOpen.Geom) LineImageType
         Returns the image type.  
             
         
        """
        pass
    @property
    def LineNumber(self) -> ReflectionAnalysisBuilder1.NumberOfLinesOptions:
        """
        Getter for property: ( ReflectionAnalysisBuilder1.NumberOfLinesOptions NXOpen.Geom) LineNumber
         Returns the reflection line number.  
             
         
        """
        pass
    @LineNumber.setter
    def LineNumber(self, lineNumber: ReflectionAnalysisBuilder1.NumberOfLinesOptions):
        """
        Setter for property: ( ReflectionAnalysisBuilder1.NumberOfLinesOptions NXOpen.Geom) LineNumber
         Returns the reflection line number.  
             
         
        """
        pass
    @property
    def LineOrientation(self) -> ReflectionAnalysisBuilder1.LineOrientationType:
        """
        Getter for property: ( ReflectionAnalysisBuilder1.LineOrientationType NXOpen.Geom) LineOrientation
         Returns the reflection line orientation.  
             
         
        """
        pass
    @LineOrientation.setter
    def LineOrientation(self, lineOrientation: ReflectionAnalysisBuilder1.LineOrientationType):
        """
        Setter for property: ( ReflectionAnalysisBuilder1.LineOrientationType NXOpen.Geom) LineOrientation
         Returns the reflection line orientation.  
             
         
        """
        pass
    @property
    def LineThickness(self) -> ReflectionAnalysisBuilder1.LineThicknessType:
        """
        Getter for property: ( ReflectionAnalysisBuilder1.LineThicknessType NXOpen.Geom) LineThickness
         Returns the reflection line thickness.  
             
         
        """
        pass
    @LineThickness.setter
    def LineThickness(self, lineThickness: ReflectionAnalysisBuilder1.LineThicknessType):
        """
        Setter for property: ( ReflectionAnalysisBuilder1.LineThicknessType NXOpen.Geom) LineThickness
         Returns the reflection line thickness.  
             
         
        """
        pass
    @property
    def Normals(self) -> FaceAnalysisNormalsBuilder:
        """
        Getter for property: ( FaceAnalysisNormalsBuilder NXOpen.Geom) Normals
         Returns the reflection analysis normals.  
             
         
        """
        pass
    @property
    def SceneImageOption(self) -> ReflectionAnalysisBuilder1.SceneImageType:
        """
        Getter for property: ( ReflectionAnalysisBuilder1.SceneImageType NXOpen.Geom) SceneImageOption
         Returns the scene image option.  
             
         
        """
        pass
    @SceneImageOption.setter
    def SceneImageOption(self, sceneImageOption: ReflectionAnalysisBuilder1.SceneImageType):
        """
        Setter for property: ( ReflectionAnalysisBuilder1.SceneImageType NXOpen.Geom) SceneImageOption
         Returns the scene image option.  
             
         
        """
        pass
    @property
    def ShowFacetEdge(self) -> bool:
        """
        Getter for property: (bool) ShowFacetEdge
         Returns the flag indicating if facet edges should be shown.  
             
         
        """
        pass
    @ShowFacetEdge.setter
    def ShowFacetEdge(self, showFacetEdge: bool):
        """
        Setter for property: (bool) ShowFacetEdge
         Returns the flag indicating if facet edges should be shown.  
             
         
        """
        pass
    @property
    def Type(self) -> ReflectionAnalysisBuilder1.Types:
        """
        Getter for property: ( ReflectionAnalysisBuilder1.Types NXOpen.Geom) Type
         Returns the reflection analysis type.  
             
         
        """
        pass
    @Type.setter
    def Type(self, type: ReflectionAnalysisBuilder1.Types):
        """
        Setter for property: ( ReflectionAnalysisBuilder1.Types NXOpen.Geom) Type
         Returns the reflection analysis type.  
             
         
        """
        pass
    def StartReflectionAnalysis(self) -> None:
        """
         Start reflection analysis. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ReflectionAnalysisBuilder(NXOpen.Builder): 
    """ Represents a Reflection Analysis builder. """
    class ImageMovementTypes(Enum):
        """
        Members Include: 
         |Horizontal|  Move image in horizonal direction. 
         |Vertical|  Move image in vertical direction. 
         |Rotate|  Rotate image. 

        """
        Horizontal: int
        Vertical: int
        Rotate: int
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder.ImageMovementTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ImageSizeOption(Enum):
        """
        Members Include: 
         |KeepCurrent|  Keep current size. 
         |ReduceScale|  Reduce scale size. 

        """
        KeepCurrent: int
        ReduceScale: int
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder.ImageSizeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LineImageTypes(Enum):
        """
        Members Include: 
         |BlackLines|  Black lines. 
         |BlackandWhiteLines|  Black and lines. 
         |ColoredLines|  Colored lines. 

        """
        BlackLines: int
        BlackandWhiteLines: int
        ColoredLines: int
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder.LineImageTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LineOrientationType(Enum):
        """
        Members Include: 
         |Horizontal|  Horizontal. 
         |Vertical|  Vertical. 
         |Both|  Both horizontal and vertical. 

        """
        Horizontal: int
        Vertical: int
        Both: int
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder.LineOrientationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LineThicknessType(Enum):
        """
        Members Include: 
         |Thin|  Thin. 
         |Normal|  Normal. 
         |Thick|  Thick. 

        """
        Thin: int
        Normal: int
        Thick: int
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder.LineThicknessType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class NumberOfLinesOptions(Enum):
        """
        Members Include: 
         |One|  1 reflection line. 
         |Two|  2 reflection line. 
         |Four|  4 reflection line. 
         |Eight|  8 reflection line. 
         |Sixteen|  16 reflection line. 
         |ThirtyTwo|  32 reflection line. 
         |SixtyFour|  64 reflection line. 
         |OneTwoEight|  128 reflection line. 
         |TwoFiveSix|  256 reflection line. 

        """
        One: int
        Two: int
        Four: int
        Eight: int
        Sixteen: int
        ThirtyTwo: int
        SixtyFour: int
        OneTwoEight: int
        TwoFiveSix: int
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder.NumberOfLinesOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SceneImageType(Enum):
        """
        Members Include: 
         |SimulatedHorizon|  Simulated horizon. 
         |PhotoHorizon|  Photo horizon. 
         |SphericalRoom|  Spherical room. 
         |SphericalLightTubesRoom|  Spherical light tubes room. 
         |DaytimeHorizon|  Daytime horizon. 
         |MagentaSunset|  Magenta sunset. 
         |SphericalHorizon|  Spherical horizon. 
         |CylindricalRoom|  Cylindrical room. 
         |MonochromeHorizon|  Monochrome horizon. 
         |SmoothGrayScale|  Smooth gray scale. 
         |SharpGrayScale|  Sharp gray scale. 
         |SphericalTubes|  Spherical tubes. 

        """
        SimulatedHorizon: int
        PhotoHorizon: int
        SphericalRoom: int
        SphericalLightTubesRoom: int
        DaytimeHorizon: int
        MagentaSunset: int
        SphericalHorizon: int
        CylindricalRoom: int
        MonochromeHorizon: int
        SmoothGrayScale: int
        SharpGrayScale: int
        SphericalTubes: int
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder.SceneImageType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |LineImages|  Line image. 
         |SceneImages|  Scene image. 
         |ImageFromFile|  Image from file. 

        """
        LineImages: int
        SceneImages: int
        ImageFromFile: int
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DisplayResolution(self) -> NXOpen.GeometricUtilities.DisplayResolutionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.DisplayResolutionBuilder) DisplayResolution
         Returns the display resolution.  
             
         
        """
        pass
    @property
    def FaceReflectivityScale(self) -> int:
        """
        Getter for property: (int) FaceReflectivityScale
         Returns the face reflectivity scale from 0 to 100.  
             
         
        """
        pass
    @FaceReflectivityScale.setter
    def FaceReflectivityScale(self, faceReflectivityScale: int):
        """
        Setter for property: (int) FaceReflectivityScale
         Returns the face reflectivity scale from 0 to 100.  
             
         
        """
        pass
    @property
    def Faces(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) Faces
         Returns the face to apply reflection analysis.  
             
         
        """
        pass
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
         Returns the file browser.  
             
         
        """
        pass
    @FileName.setter
    def FileName(self, filename: str):
        """
        Setter for property: (str) FileName
         Returns the file browser.  
             
         
        """
        pass
    @property
    def ImageMovementType(self) -> ReflectionAnalysisBuilder.ImageMovementTypes:
        """
        Getter for property: ( ReflectionAnalysisBuilder.ImageMovementTypes NXOpen.Geom) ImageMovementType
         Returns the orientation to move reflection lines.  
             
         
        """
        pass
    @ImageMovementType.setter
    def ImageMovementType(self, imageMovementType: ReflectionAnalysisBuilder.ImageMovementTypes):
        """
        Setter for property: ( ReflectionAnalysisBuilder.ImageMovementTypes NXOpen.Geom) ImageMovementType
         Returns the orientation to move reflection lines.  
             
         
        """
        pass
    @property
    def ImagePosition(self) -> int:
        """
        Getter for property: (int) ImagePosition
         Returns the moving image scale.  
             
         
        """
        pass
    @ImagePosition.setter
    def ImagePosition(self, imagePosition: int):
        """
        Setter for property: (int) ImagePosition
         Returns the moving image scale.  
             
         
        """
        pass
    @property
    def ImageSizeSetting(self) -> ReflectionAnalysisBuilder.ImageSizeOption:
        """
        Getter for property: ( ReflectionAnalysisBuilder.ImageSizeOption NXOpen.Geom) ImageSizeSetting
         Returns the image size setting.  
             
         
        """
        pass
    @ImageSizeSetting.setter
    def ImageSizeSetting(self, imageSizeSetting: ReflectionAnalysisBuilder.ImageSizeOption):
        """
        Setter for property: ( ReflectionAnalysisBuilder.ImageSizeOption NXOpen.Geom) ImageSizeSetting
         Returns the image size setting.  
             
         
        """
        pass
    @property
    def LineImageType(self) -> ReflectionAnalysisBuilder.LineImageTypes:
        """
        Getter for property: ( ReflectionAnalysisBuilder.LineImageTypes NXOpen.Geom) LineImageType
         Returns the image type.  
             
         
        """
        pass
    @LineImageType.setter
    def LineImageType(self, lineImageType: ReflectionAnalysisBuilder.LineImageTypes):
        """
        Setter for property: ( ReflectionAnalysisBuilder.LineImageTypes NXOpen.Geom) LineImageType
         Returns the image type.  
             
         
        """
        pass
    @property
    def LineNumber(self) -> ReflectionAnalysisBuilder.NumberOfLinesOptions:
        """
        Getter for property: ( ReflectionAnalysisBuilder.NumberOfLinesOptions NXOpen.Geom) LineNumber
         Returns the reflection line number.  
             
         
        """
        pass
    @LineNumber.setter
    def LineNumber(self, lineNumber: ReflectionAnalysisBuilder.NumberOfLinesOptions):
        """
        Setter for property: ( ReflectionAnalysisBuilder.NumberOfLinesOptions NXOpen.Geom) LineNumber
         Returns the reflection line number.  
             
         
        """
        pass
    @property
    def LineOrientation(self) -> ReflectionAnalysisBuilder.LineOrientationType:
        """
        Getter for property: ( ReflectionAnalysisBuilder.LineOrientationType NXOpen.Geom) LineOrientation
         Returns the reflection line orientation.  
             
         
        """
        pass
    @LineOrientation.setter
    def LineOrientation(self, lineOrientation: ReflectionAnalysisBuilder.LineOrientationType):
        """
        Setter for property: ( ReflectionAnalysisBuilder.LineOrientationType NXOpen.Geom) LineOrientation
         Returns the reflection line orientation.  
             
         
        """
        pass
    @property
    def LineThickness(self) -> ReflectionAnalysisBuilder.LineThicknessType:
        """
        Getter for property: ( ReflectionAnalysisBuilder.LineThicknessType NXOpen.Geom) LineThickness
         Returns the reflection line thickness.  
             
         
        """
        pass
    @LineThickness.setter
    def LineThickness(self, lineThickness: ReflectionAnalysisBuilder.LineThicknessType):
        """
        Setter for property: ( ReflectionAnalysisBuilder.LineThicknessType NXOpen.Geom) LineThickness
         Returns the reflection line thickness.  
             
         
        """
        pass
    @property
    def Normals(self) -> FaceAnalysisNormalsBuilder:
        """
        Getter for property: ( FaceAnalysisNormalsBuilder NXOpen.Geom) Normals
         Returns the reflection analysis normals.  
             
         
        """
        pass
    @property
    def SceneImageOption(self) -> ReflectionAnalysisBuilder.SceneImageType:
        """
        Getter for property: ( ReflectionAnalysisBuilder.SceneImageType NXOpen.Geom) SceneImageOption
         Returns the scene image option.  
             
         
        """
        pass
    @SceneImageOption.setter
    def SceneImageOption(self, sceneImageOption: ReflectionAnalysisBuilder.SceneImageType):
        """
        Setter for property: ( ReflectionAnalysisBuilder.SceneImageType NXOpen.Geom) SceneImageOption
         Returns the scene image option.  
             
         
        """
        pass
    @property
    def ShowFacetEdge(self) -> bool:
        """
        Getter for property: (bool) ShowFacetEdge
         Returns the flag indicating if facet edges should be shown.  
             
         
        """
        pass
    @ShowFacetEdge.setter
    def ShowFacetEdge(self, showFacetEdge: bool):
        """
        Setter for property: (bool) ShowFacetEdge
         Returns the flag indicating if facet edges should be shown.  
             
         
        """
        pass
    @property
    def Type(self) -> ReflectionAnalysisBuilder.Types:
        """
        Getter for property: ( ReflectionAnalysisBuilder.Types NXOpen.Geom) Type
         Returns the reflection analysis type.  
             
         
        """
        pass
    @Type.setter
    def Type(self, type: ReflectionAnalysisBuilder.Types):
        """
        Setter for property: ( ReflectionAnalysisBuilder.Types NXOpen.Geom) Type
         Returns the reflection analysis type.  
             
         
        """
        pass
    def StartReflectionAnalysis(self) -> None:
        """
         Start reflection analysis. 
        """
        pass
class ReflectionAnalysis(AnalysisObject): 
    """ Represents a Reflection analysis  """
    pass
class SectionAnalysisObject(AnalysisObject): 
    """ Represents a Section Analysis object. Section Analysis
    generates planar, circular, or isoparametric sections across faces and faceted bodies 
    to help evaluating sectional curvature flow of faces and surface quality and 
    characteristics in general. Section Analysis object update dynamically on geometry 
    changes of the sectioned faces and faceted bodies. """
    pass
import NXOpen
class SheetBoundaryAnalysisBuilder(NXOpen.Builder): 
    """ Represents a GeometricAnalysis.SheetBoundaryAnalysis builder """
    @property
    def Bodies(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Bodies
         Returns the input bodies   
            
         
        """
        pass
    @property
    def EmphasisColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) EmphasisColor
         Returns the emphasis color   
            
         
        """
        pass
    @EmphasisColor.setter
    def EmphasisColor(self, emphasisColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) EmphasisColor
         Returns the emphasis color   
            
         
        """
        pass
    @property
    def LineWidth(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectWidth) LineWidth
         Returns the line width   
            
         
        """
        pass
    @LineWidth.setter
    def LineWidth(self, lineWidth: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectWidth) LineWidth
         Returns the line width   
            
         
        """
        pass
    @property
    def ShowBoundaryVertices(self) -> bool:
        """
        Getter for property: (bool) ShowBoundaryVertices
         Returns the option to display boundary vertices   
            
         
        """
        pass
    @ShowBoundaryVertices.setter
    def ShowBoundaryVertices(self, showBoundaryVertices: bool):
        """
        Setter for property: (bool) ShowBoundaryVertices
         Returns the option to display boundary vertices   
            
         
        """
        pass
class SheetBoundaryAnalysis(AnalysisObject): 
    """Represents a sheet boundary analysis builder """
    pass
import NXOpen
class SimpleInterference(NXOpen.Builder): 
    """ Represents the Simple Interference object. A
      NXOpen.GeometricAnalysis.SimpleInterference object
      takes two solid bodies as inputs and the type of interference results to
      be produced. It can report the first pair of interfering faces between
      two solids or all pairs of interfering faces. It can also
      create the interference solid(s) between two bodies.
     """
    class FaceInterferenceMethod(Enum):
        """
        Members Include: 
         |FirstPairOnly|  Find first pair of interfering faces 
         |AllPairs|  Find
                                             all pairs of interfering faces. 

        """
        FirstPairOnly: int
        AllPairs: int
        @staticmethod
        def ValueOf(value: int) -> SimpleInterference.FaceInterferenceMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class InterferenceMethod(Enum):
        """
        Members Include: 
         |InterferingFaces|  Find
                                                                 interfering faces. 
         |InterferenceSolid|  Create
                                                                   interference solid. 

        """
        InterferingFaces: int
        InterferenceSolid: int
        @staticmethod
        def ValueOf(value: int) -> SimpleInterference.InterferenceMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Result(Enum):
        """
        Members Include: 
         |NoInterference|  No interference
                                                   exists between the input bodies. 
         |OnlyEdgesOrFacesInterfere| 
                                                   Only faces or edges interfere and no
                                                   solid interference exists between
                                                   the input bodies. 
         |InterferenceExists|  Interference
                                                   exists between the input bodies. Use
                                                   NXOpen.GeometricAnalysis.SimpleInterference.GetInterferenceResults to
                                                   obtain the pairs of faces interfering
                                                   or interference solid(s) created
                                                   between the input bodies. 
         |CanNotPerformCheck|  An unknown
                                                   error has occured while performing
                                                   the interference check. Check could 
                                                   not be performed between
                                                   the input bodies.

        """
        NoInterference: int
        OnlyEdgesOrFacesInterfere: int
        InterferenceExists: int
        CanNotPerformCheck: int
        @staticmethod
        def ValueOf(value: int) -> SimpleInterference.Result:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FaceInterferenceType(self) -> SimpleInterference.FaceInterferenceMethod:
        """
        Getter for property: ( SimpleInterference.FaceInterferenceMethod NXOpen.Geom) FaceInterferenceType
         Returns the FaceInterferenceType.  
          
                      NXOpen.GeometricAnalysis.SimpleInterference.FaceInterferenceType is used when 
                       NXOpen::GeometricAnalysis::SimpleInterference::SetInterferenceType  is set to
                       NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferingFaces , 
                      i.e., create pair(s) of interfering faces between two solids. A
                      value of  NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceMethodFirstPairOnly  
                      for NXOpen.GeometricAnalysis.SimpleInterference.FaceInterferenceType reports only the first
                      pair of interfering faces and value of
                       NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceMethodAllPairs  
                      reports all pairs of interfering faces between two bodies.   
         
        """
        pass
    @FaceInterferenceType.setter
    def FaceInterferenceType(self, faceInterferenceType: SimpleInterference.FaceInterferenceMethod):
        """
        Setter for property: ( SimpleInterference.FaceInterferenceMethod NXOpen.Geom) FaceInterferenceType
         Returns the FaceInterferenceType.  
          
                      NXOpen.GeometricAnalysis.SimpleInterference.FaceInterferenceType is used when 
                       NXOpen::GeometricAnalysis::SimpleInterference::SetInterferenceType  is set to
                       NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferingFaces , 
                      i.e., create pair(s) of interfering faces between two solids. A
                      value of  NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceMethodFirstPairOnly  
                      for NXOpen.GeometricAnalysis.SimpleInterference.FaceInterferenceType reports only the first
                      pair of interfering faces and value of
                       NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceMethodAllPairs  
                      reports all pairs of interfering faces between two bodies.   
         
        """
        pass
    @property
    def FirstBody(self) -> NXOpen.SelectObject:
        """
        Getter for property: ( NXOpen.SelectObject) FirstBody
         Returns the First Body   
            
         
        """
        pass
    @property
    def InterferenceType(self) -> SimpleInterference.InterferenceMethod:
        """
        Getter for property: ( SimpleInterference.InterferenceMethod NXOpen.Geom) InterferenceType
         Returns the InterferenceType.  
           A value of
                      NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferingFaces   for
                      NXOpen.GeometricAnalysis.SimpleInterference.InterferenceType reports 
                      the pairs of interfering faces between two solids.  You can also
                      further specify to report only the first pair of interfering faces or 
                      all pairs of interfering faces by 
                       NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceType . A value of
                       NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferenceSolid  for
                       NXOpen::GeometricAnalysis::SimpleInterference::SetInterferenceType  creates the 
                      interference solid(s) between the two input bodies.   
         
        """
        pass
    @InterferenceType.setter
    def InterferenceType(self, interferenceType: SimpleInterference.InterferenceMethod):
        """
        Setter for property: ( SimpleInterference.InterferenceMethod NXOpen.Geom) InterferenceType
         Returns the InterferenceType.  
           A value of
                      NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferingFaces   for
                      NXOpen.GeometricAnalysis.SimpleInterference.InterferenceType reports 
                      the pairs of interfering faces between two solids.  You can also
                      further specify to report only the first pair of interfering faces or 
                      all pairs of interfering faces by 
                       NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceType . A value of
                       NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferenceSolid  for
                       NXOpen::GeometricAnalysis::SimpleInterference::SetInterferenceType  creates the 
                      interference solid(s) between the two input bodies.   
         
        """
        pass
    @property
    def SecondBody(self) -> NXOpen.SelectObject:
        """
        Getter for property: ( NXOpen.SelectObject) SecondBody
         Returns the Second Body   
            
         
        """
        pass
    def GetInterferenceResults(self) -> List[NXOpen.NXObject]:
        """
         Returns the pair(s) of interfering faces or solid(s) of interference
                      between the input bodies. nObjects will be 0 if there is no face or
                      solid interference between the input bodies. If the
                      NXOpen.GeometricAnalysis.SimpleInterference.InterferenceType is
                      NXOpen.GeometricAnalysis.SimpleInterference.InterferenceMethod.InterferingFaces, pair(s) of
                      interfering faces are returned. The first two objects represent the first pair of
                      interfering faces, and next two objects represent the second pair
                      of interering faces and so on. If the
                      NXOpen.GeometricAnalysis.SimpleInterference.FaceInterferenceType is
                      NXOpen.GeometricAnalysis.SimpleInterference.FaceInterferenceMethod.FirstPairOnly,
                      only the first pair of interfering faces are returned.
                     
         Returns results ( NXOpen.NXObject Li):  Results of Simple Interference .
        """
        pass
    def HighlightNextPair(self) -> bool:
        """
         Highlights the pairs of interfering faces after a
                      NXOpen.GeometricAnalysis.SimpleInterference.PerformCheck. This method is applicable only
                      when NXOpen.GeometricAnalysis.SimpleInterference.InterferenceType is set to
                      NXOpen.GeometricAnalysis.SimpleInterference.InterferenceMethod.InterferingFaces and
                      NXOpen.GeometricAnalysis.SimpleInterference.FaceInterferenceType is set to
                      NXOpen.GeometricAnalysis.SimpleInterference.FaceInterferenceMethod.AllPairs. When
                      highlighting the next pair, current pair of faces is
                      unhighlighted. Return value is set to true if there are more
                      pairs of faces to be highlighted. If the last pair is reached 
                      (i.e., the pair being highlighted in this call is the last pair 
                      of faces), return value is set to false.
         Returns morePairs (bool):  Indicates if there are
                                                                any more pairs left . .
        """
        pass
    def PerformCheck(self) -> SimpleInterference.Result:
        """
         Perform Interference Check. NXOpen.GeometricAnalysis.SimpleInterference.PerformCheck
                      should be called after specifiying input bodies to be checked, i.e.,
                      NXOpen.GeometricAnalysis.SimpleInterference.FirstBody
                      and NXOpen.GeometricAnalysis.SimpleInterference.SecondBody. 
                      The return value NXOpen.GeometricAnalysis.SimpleInterference.Result specifies the type of
                      interference existing between the input bodies. Use
                      NXOpen.GeometricAnalysis.SimpleInterference.GetInterferenceResults to obtain the interfering faces
                      or solid(s) of interference between the input bodis.
                     
         Returns result ( SimpleInterference.Result NXOpen.Geom):  Indicates
                         the type of interference existing between the input bodies. .
        """
        pass
    def Reset(self) -> None:
        """
         Frees up resourcesresults associated with
                     NXOpen.GeometricAnalysis.SimpleInterference object after a
                     call to NXOpen.GeometricAnalysis.SimpleInterference.PerformCheck.
                     NXOpen.GeometricAnalysis.SimpleInterference.PerformCheck is followed by
                     NXOpen.GeometricAnalysis.SimpleInterference.GetInterferenceResults and the
                     NXOpen.GeometricAnalysis.SimpleInterference.Reset. 
        """
        pass
import NXOpen
import NXOpen.Features
class SlopeAnalysisBuilder1(NXOpen.Builder): 
    """ Represents a Slope Analysis builder. """
    class DisplayModes(Enum):
        """
        Members Include: 
         |Fringe|  Display in fringe. 
         |Hedgehog|  Display in hedgehog. 
         |ContourLines|  Display in contour lines. 

        """
        Fringe: int
        Hedgehog: int
        ContourLines: int
        @staticmethod
        def ValueOf(value: int) -> SlopeAnalysisBuilder1.DisplayModes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DataRange(self) -> FaceAnalysisDataRangeBuilder:
        """
        Getter for property: ( FaceAnalysisDataRangeBuilder NXOpen.Geom) DataRange
         Returns the slope analysis data range.  
             
         
        """
        pass
    @property
    def DisplayMode(self) -> SlopeAnalysisBuilder1.DisplayModes:
        """
        Getter for property: ( SlopeAnalysisBuilder1.DisplayModes NXOpen.Geom) DisplayMode
         Returns the display mode.  
             
         
        """
        pass
    @DisplayMode.setter
    def DisplayMode(self, displayMode: SlopeAnalysisBuilder1.DisplayModes):
        """
        Setter for property: ( SlopeAnalysisBuilder1.DisplayModes NXOpen.Geom) DisplayMode
         Returns the display mode.  
             
         
        """
        pass
    @property
    def DisplaySettings(self) -> FaceAnalysisDisplayBuilder:
        """
        Getter for property: ( FaceAnalysisDisplayBuilder NXOpen.Geom) DisplaySettings
         Returns the slope analysis display settings.  
             
         
        """
        pass
    @property
    def DynamicLabel(self) -> NXOpen.Features.GeometricConstraintDataManager:
        """
        Getter for property: ( NXOpen.Features.GeometricConstraintDataManager) DynamicLabel
         Returns the dynamic label   
            
         
        """
        pass
    @property
    def Faces(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) Faces
         Returns the face to apply slope analysis.  
             
         
        """
        pass
    @property
    def Normals(self) -> FaceAnalysisNormalsBuilder:
        """
        Getter for property: ( FaceAnalysisNormalsBuilder NXOpen.Geom) Normals
         Returns the slope analysis normals.  
             
         
        """
        pass
    @property
    def NumberOfContourLines(self) -> int:
        """
        Getter for property: (int) NumberOfContourLines
         Returns the number of contour lines.  
             
         
        """
        pass
    @NumberOfContourLines.setter
    def NumberOfContourLines(self, numberOfContourLines: int):
        """
        Setter for property: (int) NumberOfContourLines
         Returns the number of contour lines.  
             
         
        """
        pass
    @property
    def PmiPoint(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) PmiPoint
         Returns the point to draw labels.  
             
         
        """
        pass
    @property
    def SpikeLength(self) -> float:
        """
        Getter for property: (float) SpikeLength
         Returns the spike length.  
             
         
        """
        pass
    @SpikeLength.setter
    def SpikeLength(self, spikeLength: float):
        """
        Setter for property: (float) SpikeLength
         Returns the spike length.  
             
         
        """
        pass
    @property
    def Vector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) Vector
         Returns the reference vector used for slope analysis.  
             
         
        """
        pass
    @Vector.setter
    def Vector(self, vector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) Vector
         Returns the reference vector used for slope analysis.  
             
         
        """
        pass
    def CreatePMILabel(self, location: NXOpen.Point3d, face: NXOpen.DisplayableObject) -> None:
        """
         Create a PMI label. 
        """
        pass
    def StartSlopeAnalysis(self) -> None:
        """
         Start slope analysis. 
        """
        pass
    def UpdateDisplayOnVectorChange(self) -> None:
        """
         Update display after vector changes. 
        """
        pass
import NXOpen
import NXOpen.Features
class SlopeAnalysisBuilder(NXOpen.Builder): 
    """ Represents a Slope Analysis builder. """
    class DisplayModes(Enum):
        """
        Members Include: 
         |Fringe| 
         |Hedgehog| 
         |ContourLines| 

        """
        Fringe: int
        Hedgehog: int
        ContourLines: int
        @staticmethod
        def ValueOf(value: int) -> SlopeAnalysisBuilder.DisplayModes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DataRange(self) -> FaceAnalysisDataRangeBuilder:
        """
        Getter for property: ( FaceAnalysisDataRangeBuilder NXOpen.Geom) DataRange
         Returns the slope analysis data range.  
             
         
        """
        pass
    @property
    def DisplayMode(self) -> SlopeAnalysisBuilder.DisplayModes:
        """
        Getter for property: ( SlopeAnalysisBuilder.DisplayModes NXOpen.Geom) DisplayMode
         Returns the display mode.  
             
         
        """
        pass
    @DisplayMode.setter
    def DisplayMode(self, displayMode: SlopeAnalysisBuilder.DisplayModes):
        """
        Setter for property: ( SlopeAnalysisBuilder.DisplayModes NXOpen.Geom) DisplayMode
         Returns the display mode.  
             
         
        """
        pass
    @property
    def DisplaySettings(self) -> FaceAnalysisDisplayBuilder:
        """
        Getter for property: ( FaceAnalysisDisplayBuilder NXOpen.Geom) DisplaySettings
         Returns the slope analysis display settings.  
             
         
        """
        pass
    @property
    def DynamicLabel(self) -> NXOpen.Features.GeometricConstraintDataManager:
        """
        Getter for property: ( NXOpen.Features.GeometricConstraintDataManager) DynamicLabel
         Returns the dynamic label   
            
         
        """
        pass
    @property
    def Faces(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) Faces
         Returns the face to apply slope analysis.  
             
         
        """
        pass
    @property
    def Normals(self) -> FaceAnalysisNormalsBuilder:
        """
        Getter for property: ( FaceAnalysisNormalsBuilder NXOpen.Geom) Normals
         Returns the slope analysis normals.  
             
         
        """
        pass
    @property
    def NumberOfContourLines(self) -> int:
        """
        Getter for property: (int) NumberOfContourLines
         Returns the number of contour lines.  
             
         
        """
        pass
    @NumberOfContourLines.setter
    def NumberOfContourLines(self, numberOfContourLines: int):
        """
        Setter for property: (int) NumberOfContourLines
         Returns the number of contour lines.  
             
         
        """
        pass
    @property
    def PmiPoint(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) PmiPoint
         Returns the point to draw labels.  
             
         
        """
        pass
    @property
    def SpikeLength(self) -> float:
        """
        Getter for property: (float) SpikeLength
         Returns the spike length.  
             
         
        """
        pass
    @SpikeLength.setter
    def SpikeLength(self, spikeLength: float):
        """
        Setter for property: (float) SpikeLength
         Returns the spike length.  
             
         
        """
        pass
    @property
    def Vector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) Vector
         Returns the reference vector used for slope analysis.  
             
         
        """
        pass
    @Vector.setter
    def Vector(self, vector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) Vector
         Returns the reference vector used for slope analysis.  
             
         
        """
        pass
    def CreatePMILabel(self, location: NXOpen.Point3d, face: NXOpen.DisplayableObject) -> None:
        """
         Create a PMI label. 
        """
        pass
    def StartSlopeAnalysis(self) -> None:
        """
         Start slope analysis. 
        """
        pass
class SlopeAnalysis(AnalysisObject): 
    """ Represents a Slope analysis  """
    pass
import NXOpen
class SolidDensity(NXOpen.Builder): 
    """
      Represents a NXOpen.GeometricAnalysis.SolidDensity
     """
    class UnitsType(Enum):
        """
        Members Include: 
         |PoundsPerCubicInches|  lbmin^3 
         |PoundsPerCubicFeet|  lbmft^3 
         |GramsPerCubicCentimeters|  gcm^3 
         |KilogramsPerCubicMeters|  kgm^3 

        """
        PoundsPerCubicInches: int
        PoundsPerCubicFeet: int
        GramsPerCubicCentimeters: int
        KilogramsPerCubicMeters: int
        @staticmethod
        def ValueOf(value: int) -> SolidDensity.UnitsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Density(self) -> float:
        """
        Getter for property: (float) Density
         Returns the Solid Density.  
            NXOpen::GeometricAnalysis::SolidDensity::SetUnits  must be specified before
                  specifying the density. When  NXOpen::GeometricAnalysis::SolidDensity::SetUnits  is changed, 
                   NXOpen::GeometricAnalysis::SolidDensity::Density  value is recomputed to reflect the change
                  in units. Set  NXOpen::GeometricAnalysis::SolidDensity::SetUnits  first, then
                   NXOpen::GeometricAnalysis::SolidDensity::SetDensity  to set specify the density along
                  with its units.   
         
        """
        pass
    @Density.setter
    def Density(self, density: float):
        """
        Setter for property: (float) Density
         Returns the Solid Density.  
            NXOpen::GeometricAnalysis::SolidDensity::SetUnits  must be specified before
                  specifying the density. When  NXOpen::GeometricAnalysis::SolidDensity::SetUnits  is changed, 
                   NXOpen::GeometricAnalysis::SolidDensity::Density  value is recomputed to reflect the change
                  in units. Set  NXOpen::GeometricAnalysis::SolidDensity::SetUnits  first, then
                   NXOpen::GeometricAnalysis::SolidDensity::SetDensity  to set specify the density along
                  with its units.   
         
        """
        pass
    @property
    def Solids(self) -> NXOpen.SelectObjectList:
        """
        Getter for property: ( NXOpen.SelectObjectList) Solids
         Returns the solids to set density for   
            
         
        """
        pass
    @property
    def Units(self) -> SolidDensity.UnitsType:
        """
        Getter for property: ( SolidDensity.UnitsType NXOpen.Geom) Units
         Returns the density units for  NXOpen::GeometricAnalysis::SolidDensity .  
           
                  When  NXOpen::GeometricAnalysis::SolidDensity::SetUnits  is changed,  NXOpen::GeometricAnalysis::SolidDensity::Density 
                  value is recomputed to reflect the change in units. Set
                   NXOpen::GeometricAnalysis::SolidDensity::SetUnits  first, then
                   NXOpen::GeometricAnalysis::SolidDensity::SetDensity  to set specify the density with
                  units.   
         
        """
        pass
    @Units.setter
    def Units(self, units: SolidDensity.UnitsType):
        """
        Setter for property: ( SolidDensity.UnitsType NXOpen.Geom) Units
         Returns the density units for  NXOpen::GeometricAnalysis::SolidDensity .  
           
                  When  NXOpen::GeometricAnalysis::SolidDensity::SetUnits  is changed,  NXOpen::GeometricAnalysis::SolidDensity::Density 
                  value is recomputed to reflect the change in units. Set
                   NXOpen::GeometricAnalysis::SolidDensity::SetUnits  first, then
                   NXOpen::GeometricAnalysis::SolidDensity::SetDensity  to set specify the density with
                  units.   
         
        """
        pass
import NXOpen
class SurfaceAnalysisDisplay(NXOpen.Object): 
    """ Represents a tool control whether to show a surface's poles and knots """
    class ShowFlagType(Enum):
        """
        Members Include: 
         |Pole|  show pole   
         |Knot|  show knot   

        """
        Pole: int
        Knot: int
        @staticmethod
        def ValueOf(value: int) -> SurfaceAnalysisDisplay.ShowFlagType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def SetShowFlag(self, surface: NXOpen.DisplayableObject, choice: SurfaceAnalysisDisplay.ShowFlagType, on: bool) -> None:
        """
         Sets show flags 
        """
        pass
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
class SurfaceContinuityAnalysisBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.GeometricAnalysis.SurfaceContinuityAnalysis builder """
    class CurvatureType(Enum):
        """
        Members Include: 
         |Sectional| 
         |Gaussian| 
         |Mean| 
         |Absolute| 

        """
        Sectional: int
        Gaussian: int
        Mean: int
        Absolute: int
        @staticmethod
        def ValueOf(value: int) -> SurfaceContinuityAnalysisBuilder.CurvatureType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ReportingType(Enum):
        """
        Members Include: 
         |Analysis| 
         |Pair| 

        """
        Analysis: int
        Pair: int
        @staticmethod
        def ValueOf(value: int) -> SurfaceContinuityAnalysisBuilder.ReportingType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |EdgeToEdge| 
         |EdgeToFace| 
         |MultiFace| 

        """
        EdgeToEdge: int
        EdgeToFace: int
        MultiFace: int
        @staticmethod
        def ValueOf(value: int) -> SurfaceContinuityAnalysisBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngularThreshold(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) AngularThreshold
         Returns the angular threshold   
            
         
        """
        pass
    @property
    def CombOptions(self) -> NXOpen.GeometricUtilities.CombOptionsBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.CombOptionsBuilder) CombOptions
         Returns the comb display block options   
            
         
        """
        pass
    @property
    def CurvatureCheck(self) -> SurfaceContinuityAnalysisBuilder.CurvatureType:
        """
        Getter for property: ( SurfaceContinuityAnalysisBuilder.CurvatureType NXOpen.Geom) CurvatureCheck
         Returns the curvature check   
            
         
        """
        pass
    @CurvatureCheck.setter
    def CurvatureCheck(self, curvatureCheck: SurfaceContinuityAnalysisBuilder.CurvatureType):
        """
        Setter for property: ( SurfaceContinuityAnalysisBuilder.CurvatureType NXOpen.Geom) CurvatureCheck
         Returns the curvature check   
            
         
        """
        pass
    @property
    def DistanceThreshold(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DistanceThreshold
         Returns the distance threshold   
            
         
        """
        pass
    @property
    def DynamicLabel(self) -> NXOpen.Features.GeometricConstraintDataManager:
        """
        Getter for property: ( NXOpen.Features.GeometricConstraintDataManager) DynamicLabel
         Returns the constraint manager   
            
         
        """
        pass
    @property
    def Face(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Face
         Returns the (second) faces.  
           Used only if the type is EdgeFace   
         
        """
        pass
    @property
    def FirstEdge(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) FirstEdge
         Returns the first edges or faces   
            
         
        """
        pass
    @property
    def G0(self) -> bool:
        """
        Getter for property: (bool) G0
         Returns the g0 toggle   
            
         
        """
        pass
    @G0.setter
    def G0(self, g0: bool):
        """
        Setter for property: (bool) G0
         Returns the g0 toggle   
            
         
        """
        pass
    @property
    def G0Tolerance(self) -> float:
        """
        Getter for property: (float) G0Tolerance
         Returns the g0 tolerance   
            
         
        """
        pass
    @G0Tolerance.setter
    def G0Tolerance(self, g0Tolerance: float):
        """
        Setter for property: (float) G0Tolerance
         Returns the g0 tolerance   
            
         
        """
        pass
    @property
    def G1(self) -> bool:
        """
        Getter for property: (bool) G1
         Returns the g1 toggle   
            
         
        """
        pass
    @G1.setter
    def G1(self, g1: bool):
        """
        Setter for property: (bool) G1
         Returns the g1 toggle   
            
         
        """
        pass
    @property
    def G1Tolerance(self) -> float:
        """
        Getter for property: (float) G1Tolerance
         Returns the g1 tolerance   
            
         
        """
        pass
    @G1Tolerance.setter
    def G1Tolerance(self, g1Tolerance: float):
        """
        Setter for property: (float) G1Tolerance
         Returns the g1 tolerance   
            
         
        """
        pass
    @property
    def G2(self) -> bool:
        """
        Getter for property: (bool) G2
         Returns the g2 toggle   
            
         
        """
        pass
    @G2.setter
    def G2(self, g2: bool):
        """
        Setter for property: (bool) G2
         Returns the g2 toggle   
            
         
        """
        pass
    @property
    def G2Tolerance(self) -> float:
        """
        Getter for property: (float) G2Tolerance
         Returns the g2 tolerance   
            
         
        """
        pass
    @G2Tolerance.setter
    def G2Tolerance(self, g2Tolerance: float):
        """
        Setter for property: (float) G2Tolerance
         Returns the g2 tolerance   
            
         
        """
        pass
    @property
    def G3(self) -> bool:
        """
        Getter for property: (bool) G3
         Returns the g3 toggle   
            
         
        """
        pass
    @G3.setter
    def G3(self, g3: bool):
        """
        Setter for property: (bool) G3
         Returns the g3 toggle   
            
         
        """
        pass
    @property
    def G3Tolerance(self) -> float:
        """
        Getter for property: (float) G3Tolerance
         Returns the g3 tolerance   
            
         
        """
        pass
    @G3Tolerance.setter
    def G3Tolerance(self, g3Tolerance: float):
        """
        Setter for property: (float) G3Tolerance
         Returns the g3 tolerance   
            
         
        """
        pass
    @property
    def MultiFace(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) MultiFace
         Returns the objects for multi-face   
            
         
        """
        pass
    @property
    def ReportPer(self) -> int:
        """
        Getter for property: (int) ReportPer
         Returns the reporting type   
            
         
        """
        pass
    @ReportPer.setter
    def ReportPer(self, reportPer: int):
        """
        Setter for property: (int) ReportPer
         Returns the reporting type   
            
         
        """
        pass
    @property
    def SecondEdge(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SecondEdge
         Returns the second edges or faces.  
           Used only if the type is EdgeEdge   
         
        """
        pass
    @property
    def ShowOutOfTolerance(self) -> bool:
        """
        Getter for property: (bool) ShowOutOfTolerance
         Returns the out of tolerance only flag   
            
         
        """
        pass
    @ShowOutOfTolerance.setter
    def ShowOutOfTolerance(self, outTolerance: bool):
        """
        Setter for property: (bool) ShowOutOfTolerance
         Returns the out of tolerance only flag   
            
         
        """
        pass
    @property
    def ToleranceMarkup(self) -> bool:
        """
        Getter for property: (bool) ToleranceMarkup
         Returns the tolerance markup flag   
            
         
        """
        pass
    @ToleranceMarkup.setter
    def ToleranceMarkup(self, markup: bool):
        """
        Setter for property: (bool) ToleranceMarkup
         Returns the tolerance markup flag   
            
         
        """
        pass
    @property
    def Type(self) -> SurfaceContinuityAnalysisBuilder.Types:
        """
        Getter for property: ( SurfaceContinuityAnalysisBuilder.Types NXOpen.Geom) Type
         Returns the type of analysis to perform   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: SurfaceContinuityAnalysisBuilder.Types):
        """
        Setter for property: ( SurfaceContinuityAnalysisBuilder.Types NXOpen.Geom) Type
         Returns the type of analysis to perform   
            
         
        """
        pass
    def DeselectFirstEdgeFace(self, edge: NXOpen.DisplayableObject, face: NXOpen.DisplayableObject) -> None:
        """
         Deselection of first edge or face 
        """
        pass
    def DeselectSecondEdgeFace(self, edge: NXOpen.DisplayableObject, face: NXOpen.DisplayableObject) -> None:
        """
         Deselection of second edge or face 
        """
        pass
    def GetFace1Array(self) -> List[NXOpen.Face]:
        """
         Returns the edge1 array not used 
         Returns faces ( NXOpen.Face Li):  .
        """
        pass
    def GetGxResult(self, continuity: int) -> bool:
        """
         Get G0, G1, G2, or G3 result 
         Returns isGxGood (bool): .
        """
        pass
    def SelectFirstEdgeFace(self, edge: NXOpen.DisplayableObject, face: NXOpen.DisplayableObject) -> None:
        """
          Selection of first edge or face 
        """
        pass
    def SelectSecondEdgeFace(self, edge: NXOpen.DisplayableObject, face: NXOpen.DisplayableObject) -> None:
        """
          Selection of second edge or face 
        """
        pass
    def UpdateFace(self, face: NXOpen.Face, selection_point: NXOpen.Point3d) -> None:
        """
         User selects or deselects face, update builder m_edge2, m_face2 
        """
        pass
    def UpdateFirstEdgeFace(self, edge_or_face: NXOpen.DisplayableObject, selection_point: NXOpen.Point3d) -> None:
        """
         The user selects or deselects first edge or face, update builder m_edge1, m_face1 
        """
        pass
    def UpdateSecondEdgeFace(self, edge_or_face: NXOpen.DisplayableObject, selection_point: NXOpen.Point3d) -> None:
        """
         User selects or deselects second edge or face, update builder m_edge2, m_face2 
        """
        pass
class SurfaceContinuityAnalysis(AnalysisObject): 
    """ Represents a SurfaceContinuityAnalysis builder """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class SurfaceIntersectionBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.GeometricAnalysis.SurfaceIntersection builder """
    class CalculationTypes(Enum):
        """
        Members Include: 
         |Curvature|  needle of curvature value 
         |RadiusofCurvature|  needle of radius of curvature value 

        """
        Curvature: int
        RadiusofCurvature: int
        @staticmethod
        def ValueOf(value: int) -> SurfaceIntersectionBuilder.CalculationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DirectionTypes(Enum):
        """
        Members Include: 
         |Inside|  needle pointing inside  
         |Outside|  needle pointing outside 

        """
        Inside: int
        Outside: int
        @staticmethod
        def ValueOf(value: int) -> SurfaceIntersectionBuilder.DirectionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LabelValues(Enum):
        """
        Members Include: 
         |Curvature|  label showing curvature value 
         |RadiusOfCurvature|  label showing radius of curvature value 

        """
        Curvature: int
        RadiusOfCurvature: int
        @staticmethod
        def ValueOf(value: int) -> SurfaceIntersectionBuilder.LabelValues:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class NormalTypes(Enum):
        """
        Members Include: 
         |FaceSet1|  linear needle 
         |FaceSet2|  logarithmic needle 

        """
        FaceSet1: int
        FaceSet2: int
        @staticmethod
        def ValueOf(value: int) -> SurfaceIntersectionBuilder.NormalTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ProjectionTypes(Enum):
        """
        Members Include: 
         |NotSet|  no projection  
         |Normal|  face normal 
         |Vector|  specify vector 
         |View|  view plane     
         |Xyz|  specify x,y,z plane 

        """
        NotSet: int
        Normal: int
        Vector: int
        View: int
        Xyz: int
        @staticmethod
        def ValueOf(value: int) -> SurfaceIntersectionBuilder.ProjectionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ScalingTypes(Enum):
        """
        Members Include: 
         |Linear|  linear needle 
         |Logarithmic|  logarithmic needle 

        """
        Linear: int
        Logarithmic: int
        @staticmethod
        def ValueOf(value: int) -> SurfaceIntersectionBuilder.ScalingTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class XyzTypes(Enum):
        """
        Members Include: 
         |X|  x-axis plane 
         |Y|  y-axis plane 
         |Z|  z-axis plane 

        """
        X: int
        Y: int
        Z: int
        @staticmethod
        def ValueOf(value: int) -> SurfaceIntersectionBuilder.XyzTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CalculationMethod(self) -> SurfaceIntersectionBuilder.CalculationTypes:
        """
        Getter for property: ( SurfaceIntersectionBuilder.CalculationTypes NXOpen.Geom) CalculationMethod
         Returns the calculation method   
            
         
        """
        pass
    @CalculationMethod.setter
    def CalculationMethod(self, calculationMethod: SurfaceIntersectionBuilder.CalculationTypes):
        """
        Setter for property: ( SurfaceIntersectionBuilder.CalculationTypes NXOpen.Geom) CalculationMethod
         Returns the calculation method   
            
         
        """
        pass
    @property
    def CombOptions(self) -> NXOpen.GeometricUtilities.CombOptionsBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.CombOptionsBuilder) CombOptions
         Returns the comb display block options   
            
         
        """
        pass
    @property
    def DynamicProjection(self) -> bool:
        """
        Getter for property: (bool) DynamicProjection
         Returns the dynamic projection   
            
         
        """
        pass
    @DynamicProjection.setter
    def DynamicProjection(self, dynamicProjection: bool):
        """
        Setter for property: (bool) DynamicProjection
         Returns the dynamic projection   
            
         
        """
        pass
    @property
    def FirstFaceSet(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FirstFaceSet
         Returns the first selected face set   
            
         
        """
        pass
    @property
    def NeedleDirection(self) -> SurfaceIntersectionBuilder.DirectionTypes:
        """
        Getter for property: ( SurfaceIntersectionBuilder.DirectionTypes NXOpen.Geom) NeedleDirection
         Returns the needle direction   
            
         
        """
        pass
    @NeedleDirection.setter
    def NeedleDirection(self, needleDirection: SurfaceIntersectionBuilder.DirectionTypes):
        """
        Setter for property: ( SurfaceIntersectionBuilder.DirectionTypes NXOpen.Geom) NeedleDirection
         Returns the needle direction   
            
         
        """
        pass
    @property
    def ProjectionNormalFace(self) -> SurfaceIntersectionBuilder.NormalTypes:
        """
        Getter for property: ( SurfaceIntersectionBuilder.NormalTypes NXOpen.Geom) ProjectionNormalFace
         Returns the face normal projection   
            
         
        """
        pass
    @ProjectionNormalFace.setter
    def ProjectionNormalFace(self, normalFace: SurfaceIntersectionBuilder.NormalTypes):
        """
        Setter for property: ( SurfaceIntersectionBuilder.NormalTypes NXOpen.Geom) ProjectionNormalFace
         Returns the face normal projection   
            
         
        """
        pass
    @property
    def ProjectionOption(self) -> SurfaceIntersectionBuilder.ProjectionTypes:
        """
        Getter for property: ( SurfaceIntersectionBuilder.ProjectionTypes NXOpen.Geom) ProjectionOption
         Returns the projection option  
            
         
        """
        pass
    @ProjectionOption.setter
    def ProjectionOption(self, projectionOption: SurfaceIntersectionBuilder.ProjectionTypes):
        """
        Setter for property: ( SurfaceIntersectionBuilder.ProjectionTypes NXOpen.Geom) ProjectionOption
         Returns the projection option  
            
         
        """
        pass
    @property
    def ProjectionXYZ(self) -> SurfaceIntersectionBuilder.XyzTypes:
        """
        Getter for property: ( SurfaceIntersectionBuilder.XyzTypes NXOpen.Geom) ProjectionXYZ
         Returns the xyz projection   
            
         
        """
        pass
    @ProjectionXYZ.setter
    def ProjectionXYZ(self, projectionXYZ: SurfaceIntersectionBuilder.XyzTypes):
        """
        Setter for property: ( SurfaceIntersectionBuilder.XyzTypes NXOpen.Geom) ProjectionXYZ
         Returns the xyz projection   
            
         
        """
        pass
    @property
    def ScalingMethod(self) -> SurfaceIntersectionBuilder.ScalingTypes:
        """
        Getter for property: ( SurfaceIntersectionBuilder.ScalingTypes NXOpen.Geom) ScalingMethod
         Returns the scaling method   
            
         
        """
        pass
    @ScalingMethod.setter
    def ScalingMethod(self, scalingMethod: SurfaceIntersectionBuilder.ScalingTypes):
        """
        Setter for property: ( SurfaceIntersectionBuilder.ScalingTypes NXOpen.Geom) ScalingMethod
         Returns the scaling method   
            
         
        """
        pass
    @property
    def SecondFaceSet(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SecondFaceSet
         Returns the second selected face set   
            
         
        """
        pass
    @property
    def Vector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) Vector
         Returns the vector   
            
         
        """
        pass
    @Vector.setter
    def Vector(self, vector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) Vector
         Returns the vector   
            
         
        """
        pass
    def UpdateWorkView(self) -> None:
        """
         Update work view with a given view matrix 
        """
        pass
class SurfaceIntersection(AnalysisObject): 
    """ Represents a SurfaceIntersection builder """
    pass
