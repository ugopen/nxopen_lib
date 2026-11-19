from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents the collection of analysis commands. Inputs to this class can be convergent objects. <br> To obtain an instance of this class, refer to @link NXOpen::BasePart  NXOpen::BasePart @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class AnalysisManager(NXOpen.Object): 
    """ Represents the collection of analysis commands. Inputs to this class can be convergent objects."""


    ##  Returns the AnalysisObjectCollection instance belonging to this part 
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @link AnalysisObjectCollection NXOpen.GeometricAnalysis.AnalysisObjectCollection@endlink
    @property
    def AnalysisObjects() -> AnalysisObjectCollection:
        """
         Returns the AnalysisObjectCollection instance belonging to this part 
        """
        pass
    
    ##  Creates a deviation checking object 
    ##  @return builder (@link DeviationChecking NXOpen.GeometricAnalysis.DeviationChecking@endlink):  DeviationChecking object.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def CreateDeviationCheckingObject(self) -> DeviationChecking:
        """
         Creates a deviation checking object 
         @return builder (@link DeviationChecking NXOpen.GeometricAnalysis.DeviationChecking@endlink):  DeviationChecking object.
        """
        pass
    
    ##  Creates an examine geometry object 
    ##  @return builder (@link ExamineGeometry NXOpen.GeometricAnalysis.ExamineGeometry@endlink):  Examine
    ##                                                                                     Geometry object .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def CreateExamineGeometryObject(self) -> ExamineGeometry:
        """
         Creates an examine geometry object 
         @return builder (@link ExamineGeometry NXOpen.GeometricAnalysis.ExamineGeometry@endlink):  Examine
                                                                                            Geometry object .
        """
        pass
    
    ##  Creates a geometric properties object 
    ##  @return builder (@link GeometricProperties NXOpen.GeometricAnalysis.GeometricProperties@endlink): 
    ##                                                                             Geometric
    ##                                                                             Properties object .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def CreateGeometricPropertiesObject(self) -> GeometricProperties:
        """
         Creates a geometric properties object 
         @return builder (@link GeometricProperties NXOpen.GeometricAnalysis.GeometricProperties@endlink): 
                                                                                    Geometric
                                                                                    Properties object .
        """
        pass
    
    ##  Creates a simple interference object 
    ##  @return builder (@link SimpleInterference NXOpen.GeometricAnalysis.SimpleInterference@endlink): 
    ##                                                                              Simple Interference object .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def CreateSimpleInterferenceObject(self) -> SimpleInterference:
        """
         Creates a simple interference object 
         @return builder (@link SimpleInterference NXOpen.GeometricAnalysis.SimpleInterference@endlink): 
                                                                                     Simple Interference object .
        """
        pass
    
    ##  Creates a solid density object 
    ##  @return builder (@link SolidDensity NXOpen.GeometricAnalysis.SolidDensity@endlink):  SolidDensity object.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def CreateSolidDensityObject(self) -> SolidDensity:
        """
         Creates a solid density object 
         @return builder (@link SolidDensity NXOpen.GeometricAnalysis.SolidDensity@endlink):  SolidDensity object.
        """
        pass
    
import NXOpen
##  Collection of analysis objects  <br> To obtain an instance of this class, refer to @link NXOpen::GeometricAnalysis::AnalysisObjectCollection  NXOpen::GeometricAnalysis::AnalysisObjectCollection @endlink  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class AnalysisObjectCollectionEx(NXOpen.Object): 
    """ Collection of analysis objects """


    ##  Creates a distance analysis builder. 
    ##  @return distanceBuilder (@link DistanceAnalysisBuilder NXOpen.GeometricAnalysis.DistanceAnalysisBuilder@endlink):  distance analysis builder .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link CreateDistanceAnalysisBuilder1 CreateDistanceAnalysisBuilder1@endlink  instead.  <br> 

    ## License requirements: gateway ("UG GATEWAY")
    ## 
    ## <param name="distanceAO"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink)  DistanceAO </param>
    def CreateDistanceAnalysisBuilder(self, distanceAO: NXOpen.DisplayableObject) -> DistanceAnalysisBuilder:
        """
         Creates a distance analysis builder. 
         @return distanceBuilder (@link DistanceAnalysisBuilder NXOpen.GeometricAnalysis.DistanceAnalysisBuilder@endlink):  distance analysis builder .
        """
        pass
    
    ##  Creates a distance analysis builder. 
    ##  @return distanceBuilder (@link DistanceAnalysisBuilder1 NXOpen.GeometricAnalysis.DistanceAnalysisBuilder1@endlink):  distance analysis builder .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: gateway ("UG GATEWAY")
    ## 
    ## <param name="distanceAO"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink)  DistanceAO </param>
    def CreateDistanceAnalysisBuilder1(self, distanceAO: NXOpen.DisplayableObject) -> DistanceAnalysisBuilder1:
        """
         Creates a distance analysis builder. 
         @return distanceBuilder (@link DistanceAnalysisBuilder1 NXOpen.GeometricAnalysis.DistanceAnalysisBuilder1@endlink):  distance analysis builder .
        """
        pass
    
    ##  Creates a @link GeometricAnalysis::PerformancePredictorBuilder GeometricAnalysis::PerformancePredictorBuilder@endlink   
    ##  @return perfPredictBuilder (@link PerformancePredictorBuilder NXOpen.GeometricAnalysis.PerformancePredictorBuilder@endlink):  @link NXOpen::GeometricAnalysis::PerformancePredictorBuilder NXOpen::GeometricAnalysis::PerformancePredictorBuilder@endlink  with this name. .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="perfPredictAO"> (@link PerformancePredictor NXOpen.GeometricAnalysis.PerformancePredictor@endlink)  @link NXOpen::GeometricAnalysis::PerformancePredictor NXOpen::GeometricAnalysis::PerformancePredictor@endlink  </param>
    def CreatePerformancePredictorBuilder(self, perfPredictAO: PerformancePredictor) -> PerformancePredictorBuilder:
        """
         Creates a @link GeometricAnalysis::PerformancePredictorBuilder GeometricAnalysis::PerformancePredictorBuilder@endlink   
         @return perfPredictBuilder (@link PerformancePredictorBuilder NXOpen.GeometricAnalysis.PerformancePredictorBuilder@endlink):  @link NXOpen::GeometricAnalysis::PerformancePredictorBuilder NXOpen::GeometricAnalysis::PerformancePredictorBuilder@endlink  with this name. .
        """
        pass
    
    ##  Creates a radius analysis builder. 
    ##  @return radiusBuilder (@link RadiusAnalysisBuilder NXOpen.GeometricAnalysis.RadiusAnalysisBuilder@endlink):  radius analysis builder .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link CreateRadiusAnalysisBuilder1 CreateRadiusAnalysisBuilder1@endlink  instead.  <br> 

    ## License requirements: gateway ("UG GATEWAY")
    ## 
    ## <param name="radiusAO"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink)  RadiusAO </param>
    def CreateRadiusAnalysisBuilder(self, radiusAO: NXOpen.DisplayableObject) -> RadiusAnalysisBuilder:
        """
         Creates a radius analysis builder. 
         @return radiusBuilder (@link RadiusAnalysisBuilder NXOpen.GeometricAnalysis.RadiusAnalysisBuilder@endlink):  radius analysis builder .
        """
        pass
    
    ##  Creates a radius analysis builder. 
    ##  @return radiusBuilder (@link RadiusAnalysisBuilder1 NXOpen.GeometricAnalysis.RadiusAnalysisBuilder1@endlink):  radius analysis builder .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: gateway ("UG GATEWAY")
    ## 
    ## <param name="radiusAO"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink)  RadiusAO </param>
    def CreateRadiusAnalysisBuilder1(self, radiusAO: NXOpen.DisplayableObject) -> RadiusAnalysisBuilder1:
        """
         Creates a radius analysis builder. 
         @return radiusBuilder (@link RadiusAnalysisBuilder1 NXOpen.GeometricAnalysis.RadiusAnalysisBuilder1@endlink):  radius analysis builder .
        """
        pass
    
    ##  Creates a reflection analysis builder. 
    ##  @return reflectionBuilder (@link ReflectionAnalysisBuilder NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder@endlink):  reflection analysis builder .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link CreateReflectionAnalysisBuilder1 CreateReflectionAnalysisBuilder1@endlink  instead.  <br> 

    ## License requirements: gateway ("UG GATEWAY")
    ## 
    ## <param name="reflectionAO"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink)  ReflectionAO </param>
    def CreateReflectionAnalysisBuilder(self, reflectionAO: NXOpen.DisplayableObject) -> ReflectionAnalysisBuilder:
        """
         Creates a reflection analysis builder. 
         @return reflectionBuilder (@link ReflectionAnalysisBuilder NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder@endlink):  reflection analysis builder .
        """
        pass
    
    ##  Creates a reflection analysis builder. 
    ##  @return reflectionBuilder (@link ReflectionAnalysisBuilder1 NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1@endlink):  reflection analysis builder .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: gateway ("UG GATEWAY")
    ## 
    ## <param name="reflectionAO"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink)  ReflectionAO </param>
    def CreateReflectionAnalysisBuilder1(self, reflectionAO: NXOpen.DisplayableObject) -> ReflectionAnalysisBuilder1:
        """
         Creates a reflection analysis builder. 
         @return reflectionBuilder (@link ReflectionAnalysisBuilder1 NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1@endlink):  reflection analysis builder .
        """
        pass
    
    ##  Creates a @link GeometricAnalysis::SheetBoundaryAnalysisBuilder GeometricAnalysis::SheetBoundaryAnalysisBuilder@endlink   
    ##  @return sheetBoundaryBuilder (@link SheetBoundaryAnalysisBuilder NXOpen.GeometricAnalysis.SheetBoundaryAnalysisBuilder@endlink):  sheet boundary analysis builder .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: gateway ("UG GATEWAY")
    ## 
    ## <param name="sheetBoundaryAnalysisAO"> (@link SheetBoundaryAnalysis NXOpen.GeometricAnalysis.SheetBoundaryAnalysis@endlink)  @link NXOpen::GeometricAnalysis::SheetBoundaryAnalysis NXOpen::GeometricAnalysis::SheetBoundaryAnalysis@endlink  to be edited </param>
    def CreateSheetBoundaryAnalysisBuilder(self, sheetBoundaryAnalysisAO: SheetBoundaryAnalysis) -> SheetBoundaryAnalysisBuilder:
        """
         Creates a @link GeometricAnalysis::SheetBoundaryAnalysisBuilder GeometricAnalysis::SheetBoundaryAnalysisBuilder@endlink   
         @return sheetBoundaryBuilder (@link SheetBoundaryAnalysisBuilder NXOpen.GeometricAnalysis.SheetBoundaryAnalysisBuilder@endlink):  sheet boundary analysis builder .
        """
        pass
    
    ##  Creates a slope analysis builder. 
    ##  @return slopeBuilder (@link SlopeAnalysisBuilder NXOpen.GeometricAnalysis.SlopeAnalysisBuilder@endlink):  slope analysis builder .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link CreateSlopeAnalysisBuilder1 CreateSlopeAnalysisBuilder1@endlink  instead.  <br> 

    ## License requirements: gateway ("UG GATEWAY")
    ## 
    ## <param name="slopeAO"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink)  SlopeAO </param>
    def CreateSlopeAnalysisBuilder(self, slopeAO: NXOpen.DisplayableObject) -> SlopeAnalysisBuilder:
        """
         Creates a slope analysis builder. 
         @return slopeBuilder (@link SlopeAnalysisBuilder NXOpen.GeometricAnalysis.SlopeAnalysisBuilder@endlink):  slope analysis builder .
        """
        pass
    
    ##  Creates a slope analysis builder. 
    ##  @return slopeBuilder (@link SlopeAnalysisBuilder1 NXOpen.GeometricAnalysis.SlopeAnalysisBuilder1@endlink):  slope analysis builder .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: gateway ("UG GATEWAY")
    ## 
    ## <param name="slopeAO"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink)  SlopeAO </param>
    def CreateSlopeAnalysisBuilder1(self, slopeAO: NXOpen.DisplayableObject) -> SlopeAnalysisBuilder1:
        """
         Creates a slope analysis builder. 
         @return slopeBuilder (@link SlopeAnalysisBuilder1 NXOpen.GeometricAnalysis.SlopeAnalysisBuilder1@endlink):  slope analysis builder .
        """
        pass
    
import NXOpen
import NXOpen.GeometricAnalysis.SectionAnalysis
##  Create a AnalysisObjectCollection  <br> To obtain an instance of this class, refer to @link NXOpen::GeometricAnalysis::AnalysisManager  NXOpen::GeometricAnalysis::AnalysisManager @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class AnalysisObjectCollection(NXOpen.TaggedObjectCollection): 
    """ Create a AnalysisObjectCollection """


    ##  Returns object for displaying curve analysis information 
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @link CurveAnalysisDisplay NXOpen.GeometricAnalysis.CurveAnalysisDisplay@endlink
    @property
    def CurveAnalysisDisplayObject() -> CurveAnalysisDisplay:
        """
         Returns object for displaying curve analysis information 
        """
        pass
    
    ##  Returns object for displaying surface analysis information 
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @link SurfaceAnalysisDisplay NXOpen.GeometricAnalysis.SurfaceAnalysisDisplay@endlink
    @property
    def SurfaceAnalysisDisplayObject() -> SurfaceAnalysisDisplay:
        """
         Returns object for displaying surface analysis information 
        """
        pass
    
    ##  Returns the AnalysisObjectCollectionEx instance belonging to this part 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @link AnalysisObjectCollectionEx NXOpen.GeometricAnalysis.AnalysisObjectCollectionEx@endlink
    @property
    def AnalysisObjectsEx() -> AnalysisObjectCollectionEx:
        """
         Returns the AnalysisObjectCollectionEx instance belonging to this part 
        """
        pass
    
    ##  Creates a Curve Continuity Builder 
    ##  @return ccao_builder (@link CurveContinuityBuilder NXOpen.GeometricAnalysis.CurveContinuityBuilder@endlink):  Curve Continuity AO builder .
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: gateway ("UG GATEWAY")
    ## 
    ## <param name="ccao_object"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink)  CCAO </param>
    def CreateCurveContinuityBuilder(self, ccao_object: NXOpen.DisplayableObject) -> CurveContinuityBuilder:
        """
         Creates a Curve Continuity Builder 
         @return ccao_builder (@link CurveContinuityBuilder NXOpen.GeometricAnalysis.CurveContinuityBuilder@endlink):  Curve Continuity AO builder .
        """
        pass
    
    ##  Creates a curve curvature analysis builder 
    ##  @return caao_builder (@link CurveCurvatureAnalysisBuilder NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilder@endlink):  Curve Curvature Analysis builder .
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: gateway ("UG GATEWAY")
    ## 
    ## <param name="caao_object"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink) Curve Curvature Analysis </param>
    def CreateCurveCurvatureAnalysisBuilder(self, caao_object: NXOpen.DisplayableObject) -> CurveCurvatureAnalysisBuilder:
        """
         Creates a curve curvature analysis builder 
         @return caao_builder (@link CurveCurvatureAnalysisBuilder NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilder@endlink):  Curve Curvature Analysis builder .
        """
        pass
    
    ##  Creates a  Deviation Gauge Builder 
    ##  @return devgg_builder (@link DeviationGaugeBuilder NXOpen.GeometricAnalysis.DeviationGaugeBuilder@endlink):  DeviationGauge builder .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="ddao_object"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink)  DDAO  </param>
    def CreateDeviationGaugeBuilder(self, ddao_object: NXOpen.DisplayableObject) -> DeviationGaugeBuilder:
        """
         Creates a  Deviation Gauge Builder 
         @return devgg_builder (@link DeviationGaugeBuilder NXOpen.GeometricAnalysis.DeviationGaugeBuilder@endlink):  DeviationGauge builder .
        """
        pass
    
    ##  Creates a draft analysis builder 
    ##  @return dao_builder (@link DraftAnalysisBuilder NXOpen.GeometricAnalysis.DraftAnalysisBuilder@endlink):  draft analysis builder .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="dao_object"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink)  DAO </param>
    def CreateDraftAnalysisBuilder(self, dao_object: NXOpen.DisplayableObject) -> DraftAnalysisBuilder:
        """
         Creates a draft analysis builder 
         @return dao_builder (@link DraftAnalysisBuilder NXOpen.GeometricAnalysis.DraftAnalysisBuilder@endlink):  draft analysis builder .
        """
        pass
    
    ##  Creates a face curvature analysis builder 
    ##  @return fcao_builder (@link FaceCurvatureAnalysisBuilder NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder@endlink):  face curvature analysis builder .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="fcao_object"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink)  FCAO </param>
    def CreateFaceCurvatureAnalysisBuilder(self, fcao_object: NXOpen.DisplayableObject) -> FaceCurvatureAnalysisBuilder:
        """
         Creates a face curvature analysis builder 
         @return fcao_builder (@link FaceCurvatureAnalysisBuilder NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder@endlink):  face curvature analysis builder .
        """
        pass
    
    ##  Creates a gap and flushness builder 
    ##  @return gfao_builder (@link GapFlushnessBuilder NXOpen.GeometricAnalysis.GapFlushnessBuilder@endlink):  Gap and Flushness builder .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="gfao_object"> (@link GapFlushness NXOpen.GeometricAnalysis.GapFlushness@endlink)  Gap and Flushness  </param>
    def CreateGapFlushnessBuilder(self, gfao_object: GapFlushness) -> GapFlushnessBuilder:
        """
         Creates a gap and flushness builder 
         @return gfao_builder (@link GapFlushnessBuilder NXOpen.GeometricAnalysis.GapFlushnessBuilder@endlink):  Gap and Flushness builder .
        """
        pass
    
    ##  Creates a Highlight Lines Analysis builder 
    ##  @return builder (@link HighlightLinesAnalysisBuilder NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder@endlink):  Highlight Lines Analysis builder .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="hpao_object"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink)  Highlight Lines Analysis object </param>
    def CreateHighlightLinesAnalysisBuilder(self, hpao_object: NXOpen.DisplayableObject) -> HighlightLinesAnalysisBuilder:
        """
         Creates a Highlight Lines Analysis builder 
         @return builder (@link HighlightLinesAnalysisBuilder NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder@endlink):  Highlight Lines Analysis builder .
        """
        pass
    
    ##  Creates a @link NXOpen::GeometricAnalysis::LocalRadiusAnalysisBuilder NXOpen::GeometricAnalysis::LocalRadiusAnalysisBuilder@endlink  
    ##  @return builder (@link LocalRadiusAnalysisBuilder NXOpen.GeometricAnalysis.LocalRadiusAnalysisBuilder@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="lrao"> (@link LocalRadiusAnalysis NXOpen.GeometricAnalysis.LocalRadiusAnalysis@endlink) </param>
    def CreateLocalRadiusAnalysisBuilder(self, lrao: LocalRadiusAnalysis) -> LocalRadiusAnalysisBuilder:
        """
         Creates a @link NXOpen::GeometricAnalysis::LocalRadiusAnalysisBuilder NXOpen::GeometricAnalysis::LocalRadiusAnalysisBuilder@endlink  
         @return builder (@link LocalRadiusAnalysisBuilder NXOpen.GeometricAnalysis.LocalRadiusAnalysisBuilder@endlink): .
        """
        pass
    
    ##  Creates a Section Analysis object builder 
    ##  @return msao_builder (@link NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder@endlink):  Section Analysis builder .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="msao_object"> (@link SectionAnalysisObject NXOpen.GeometricAnalysis.SectionAnalysisObject@endlink)  Section Analysis object </param>
    def CreateSectionAnalysisBuilder(self, msao_object: SectionAnalysisObject) -> NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder:
        """
         Creates a Section Analysis object builder 
         @return msao_builder (@link NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder@endlink):  Section Analysis builder .
        """
        pass
    
    ##  Creates a Section Analysis builder of a new version
    ##  @return csao_builder (@link NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder@endlink):  Section Analysis builder .
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE") OR nx_mcd_core ("Mechatronics Concept Designer")
    ## 
    ## <param name="csao_object"> (@link NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExObject NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExObject@endlink)  Section Analysis object </param>
    def CreateSectionAnalysisExBuilder(self, csao_object: NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExObject) -> NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder:
        """
         Creates a Section Analysis builder of a new version
         @return csao_builder (@link NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder@endlink):  Section Analysis builder .
        """
        pass
    
    ##  Creates a surface continuity analysis builder 
    ##  @return scao_builder (@link SurfaceContinuityAnalysisBuilder NXOpen.GeometricAnalysis.SurfaceContinuityAnalysisBuilder@endlink):  Surface Continuity Analysis builder .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: gateway ("UG GATEWAY")
    ## 
    ## <param name="scao_object"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink)  Surface Continuity Analysis </param>
    def CreateSurfaceContinuityAnalysisBuilder(self, scao_object: NXOpen.DisplayableObject) -> SurfaceContinuityAnalysisBuilder:
        """
         Creates a surface continuity analysis builder 
         @return scao_builder (@link SurfaceContinuityAnalysisBuilder NXOpen.GeometricAnalysis.SurfaceContinuityAnalysisBuilder@endlink):  Surface Continuity Analysis builder .
        """
        pass
    
    ##  Creates a surface intersection  builder 
    ##  @return siao_builder (@link SurfaceIntersectionBuilder NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder@endlink):  surface intersection builder .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="siao_object"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink) surface intersection </param>
    def CreateSurfaceIntersectionBuilder(self, siao_object: NXOpen.DisplayableObject) -> SurfaceIntersectionBuilder:
        """
         Creates a surface intersection  builder 
         @return siao_builder (@link SurfaceIntersectionBuilder NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder@endlink):  surface intersection builder .
        """
        pass
    
import NXOpen
##  Represents an Analysis Object    <br> This is an abstract class, and cannot be instantiated  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class AnalysisObject(NXOpen.DisplayableObject): 
    """ Represents an Analysis Object   """
    pass


import NXOpen
import NXOpen.Validate
## 
##      Represents an NX @link NXOpen::GeometricAnalysis::AnalysisResultCollection NXOpen::GeometricAnalysis::AnalysisResultCollection@endlink  object.
##      <br> To obtain an instance of this class, refer to @link NXOpen::BasePart  NXOpen::BasePart @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class AnalysisResultCollection(NXOpen.TaggedObjectCollection): 
    """
     Represents an NX <ja_class>NXOpen.GeometricAnalysis.AnalysisResultCollection</ja_class> object.
    """


    ##  Creates a contact analysis builder. 
    ##  @return contactBuilder (@link ContactAnalysisBuilder NXOpen.GeometricAnalysis.ContactAnalysisBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="persistentResult"> (@link NXOpen.Validate.AnalysisResult NXOpen.Validate.AnalysisResult@endlink)  Analysis Result </param>
    def CreateContactAnalysisBuilder(self, persistentResult: NXOpen.Validate.AnalysisResult) -> ContactAnalysisBuilder:
        """
         Creates a contact analysis builder. 
         @return contactBuilder (@link ContactAnalysisBuilder NXOpen.GeometricAnalysis.ContactAnalysisBuilder@endlink): .
        """
        pass
    
    ##  Creates a contact analysis Section Curve builder. 
    ##  @return contactAnalysisSectionCurveBuilder (@link ContactAnalysisSectionCurveBuilder NXOpen.GeometricAnalysis.ContactAnalysisSectionCurveBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="view"> (@link NXOpen.ModelingView NXOpen.ModelingView@endlink)  Modeling View </param>
    ## <param name="contactAnalysisBuilder"> (@link ContactAnalysisBuilder NXOpen.GeometricAnalysis.ContactAnalysisBuilder@endlink) GeometricAnalysis.ContactAnalysisBuilder</param>
    def CreateContactAnalysisSectionCurveBuilder(self, view: NXOpen.ModelingView, contactAnalysisBuilder: ContactAnalysisBuilder) -> ContactAnalysisSectionCurveBuilder:
        """
         Creates a contact analysis Section Curve builder. 
         @return contactAnalysisSectionCurveBuilder (@link ContactAnalysisSectionCurveBuilder NXOpen.GeometricAnalysis.ContactAnalysisSectionCurveBuilder@endlink): .
        """
        pass
    
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
##  Represents a Contact Analysis builder. 
##         The Contact analysis will be performed on selected Sheet or Solid Bodies.
##         And the Radius Analysis will be carried out on the ball touching areas
##         The Output for the Contact Analysis will be Areas Touched by Ball and Areas Not Touched by ball 
##         The Output for radius Analysis will be Sharp Areas, Intermediate areas and Smooth areas
##         Also The results can be modulated for different resolutions <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisResultCollection::CreateContactAnalysisBuilder  NXOpen::GeometricAnalysis::AnalysisResultCollection::CreateContactAnalysisBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AutomaticUpdate </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## BallDiameter.Value </term> <description> 
##  
## 165.000 (millimeters part), 6.496 (inches part) </description> </item> 
## 
## <item><term> 
##  
## CreateMinRadiusPoints </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## CreatePointsAtStepDist </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DisplayContourCurves </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolution.AngleTolerance </term> <description> 
##  
## 15.0 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolution.EdgeTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolution.FaceTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolution.Resolution </term> <description> 
##  
## Standard </description> </item> 
## 
## <item><term> 
##  
## DisplayResolution.WidthTolerance </term> <description> 
##  
## 0.3 </description> </item> 
## 
## <item><term> 
##  
## EnableRadiusAnalysis </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ExternalBallDiameter.Value </term> <description> 
##  
## 165.000 (millimeters part), 6.496 (inches part) </description> </item> 
## 
## <item><term> 
##  
## HemishpericalBallDiameter.Value </term> <description> 
##  
## 165.000 (millimeters part), 6.496 (inches part) </description> </item> 
## 
## <item><term> 
##  
## InternalBallDiameter.Value </term> <description> 
##  
## 100.000 (millimeters part), 3.937 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MaximumRadius.Value </term> <description> 
##  
## 5.000 (millimeters part), 0.197 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MinimumRadius.Value </term> <description> 
##  
## 2.500 (millimeters part), 0.098 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ProtrusionLimit.Value </term> <description> 
##  
## 5.000 (millimeters part), 0.197 (inches part) </description> </item> 
## 
## <item><term> 
##  
## RamDiameter.Value </term> <description> 
##  
## 50.000 (millimeters part), 1.969 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ShowOnlyContactAnalysisAreas </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ShowOnlySharpAreas </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## StepDistance.Value </term> <description> 
##  
## 50.000 (millimeters part), 1.969 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1953.0.0  <br> 

class ContactAnalysisBuilder(NXOpen.Builder): 
    """ Represents a Contact Analysis builder. 
        The Contact analysis will be performed on selected Sheet or Solid Bodies.
        And the Radius Analysis will be carried out on the ball touching areas
        The Output for the Contact Analysis will be Areas Touched by Ball and Areas Not Touched by ball 
        The Output for radius Analysis will be Sharp Areas, Intermediate areas and Smooth areas
        Also The results can be modulated for different resolutions"""


    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) AreasNotTouchedByBall
    ##  Returns the Color for Areas Not Touched by Ball of Given Ball Diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def AreasNotTouchedByBall(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) AreasNotTouchedByBall
         Returns the Color for Areas Not Touched by Ball of Given Ball Diameter   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) AreasNotTouchedByBall

    ##  Returns the Color for Areas Not Touched by Ball of Given Ball Diameter   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @AreasNotTouchedByBall.setter
    def AreasNotTouchedByBall(self, areasNotTouchedByBall: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) AreasNotTouchedByBall
         Returns the Color for Areas Not Touched by Ball of Given Ball Diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) AreasTouchedByBall
    ##  Returns the Color for Areas Touched by Ball of Given Ball Diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def AreasTouchedByBall(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) AreasTouchedByBall
         Returns the Color for Areas Touched by Ball of Given Ball Diameter   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) AreasTouchedByBall

    ##  Returns the Color for Areas Touched by Ball of Given Ball Diameter   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @AreasTouchedByBall.setter
    def AreasTouchedByBall(self, areasTouchedByBall: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) AreasTouchedByBall
         Returns the Color for Areas Touched by Ball of Given Ball Diameter   
            
         
        """
        pass
    
    ## Getter for property: (bool) AutomaticUpdate
    ##  Returns the toggle that automatic update   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def AutomaticUpdate(self) -> bool:
        """
        Getter for property: (bool) AutomaticUpdate
         Returns the toggle that automatic update   
            
         
        """
        pass
    
    ## Setter for property: (bool) AutomaticUpdate

    ##  Returns the toggle that automatic update   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @AutomaticUpdate.setter
    def AutomaticUpdate(self, automaticUpdate: bool):
        """
        Setter for property: (bool) AutomaticUpdate
         Returns the toggle that automatic update   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BallDiameter
    ##  Returns the Ball Diameter for Ball Contact Analysis   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def BallDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BallDiameter
         Returns the Ball Diameter for Ball Contact Analysis   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BodySelection
    ##  Returns the body selection on which the Contact analysis and Radius Analysis will be carried out  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def BodySelection(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BodySelection
         Returns the body selection on which the Contact analysis and Radius Analysis will be carried out  
            
         
        """
        pass
    
    ## Getter for property: (bool) CreateMinRadiusPoints
    ##  Returns the toggle to Create and label the minimum radius point from all the sharp regions    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def CreateMinRadiusPoints(self) -> bool:
        """
        Getter for property: (bool) CreateMinRadiusPoints
         Returns the toggle to Create and label the minimum radius point from all the sharp regions    
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateMinRadiusPoints

    ##  Returns the toggle to Create and label the minimum radius point from all the sharp regions    
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @CreateMinRadiusPoints.setter
    def CreateMinRadiusPoints(self, createMinRadiusPoints: bool):
        """
        Setter for property: (bool) CreateMinRadiusPoints
         Returns the toggle to Create and label the minimum radius point from all the sharp regions    
            
         
        """
        pass
    
    ## Getter for property: (bool) CreatePointsAtStepDist
    ##  Returns the toggle to create equidistant points at given step distance    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def CreatePointsAtStepDist(self) -> bool:
        """
        Getter for property: (bool) CreatePointsAtStepDist
         Returns the toggle to create equidistant points at given step distance    
            
         
        """
        pass
    
    ## Setter for property: (bool) CreatePointsAtStepDist

    ##  Returns the toggle to create equidistant points at given step distance    
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @CreatePointsAtStepDist.setter
    def CreatePointsAtStepDist(self, createPointsAtStepDist: bool):
        """
        Setter for property: (bool) CreatePointsAtStepDist
         Returns the toggle to create equidistant points at given step distance    
            
         
        """
        pass
    
    ## Getter for property: (bool) DisplayContourCurves
    ##  Returns the toggle to Display Contour Curves   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def DisplayContourCurves(self) -> bool:
        """
        Getter for property: (bool) DisplayContourCurves
         Returns the toggle to Display Contour Curves   
            
         
        """
        pass
    
    ## Setter for property: (bool) DisplayContourCurves

    ##  Returns the toggle to Display Contour Curves   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @DisplayContourCurves.setter
    def DisplayContourCurves(self, displayContourCurves: bool):
        """
        Setter for property: (bool) DisplayContourCurves
         Returns the toggle to Display Contour Curves   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.DisplayResolutionBuilder NXOpen.GeometricUtilities.DisplayResolutionBuilder@endlink) DisplayResolution
    ##  Returns the disp resolution will decide the fineness of faceting triangles   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.DisplayResolutionBuilder
    @property
    def DisplayResolution(self) -> NXOpen.GeometricUtilities.DisplayResolutionBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.DisplayResolutionBuilder NXOpen.GeometricUtilities.DisplayResolutionBuilder@endlink) DisplayResolution
         Returns the disp resolution will decide the fineness of faceting triangles   
            
         
        """
        pass
    
    ## Getter for property: (bool) EnableRadiusAnalysis
    ##  Returns the toggle that enables radius analysis   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def EnableRadiusAnalysis(self) -> bool:
        """
        Getter for property: (bool) EnableRadiusAnalysis
         Returns the toggle that enables radius analysis   
            
         
        """
        pass
    
    ## Setter for property: (bool) EnableRadiusAnalysis

    ##  Returns the toggle that enables radius analysis   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @EnableRadiusAnalysis.setter
    def EnableRadiusAnalysis(self, enableRadiusAnalysis: bool):
        """
        Setter for property: (bool) EnableRadiusAnalysis
         Returns the toggle that enables radius analysis   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExternalBallDiameter
    ##  Returns the External Ball Diameter for Fold Measurement Analysis    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ExternalBallDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExternalBallDiameter
         Returns the External Ball Diameter for Fold Measurement Analysis    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Features.GeometricConstraintDataManager NXOpen.Features.GeometricConstraintDataManager@endlink) GeometricConstraintDataManager
    ##  Returns the Geometric Constraint Data Manager builder  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Features.GeometricConstraintDataManager
    @property
    def GeometricConstraintDataManager(self) -> NXOpen.Features.GeometricConstraintDataManager:
        """
        Getter for property: (@link NXOpen.Features.GeometricConstraintDataManager NXOpen.Features.GeometricConstraintDataManager@endlink) GeometricConstraintDataManager
         Returns the Geometric Constraint Data Manager builder  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HemishpericalBallDiameter
    ##  Returns the Hemispherical Ball Diameter for Ram Apparatus Analysis     
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def HemishpericalBallDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) HemishpericalBallDiameter
         Returns the Hemispherical Ball Diameter for Ram Apparatus Analysis     
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) IntermediateAreas
    ##  Returns the Color for Areas Where the Radius is Between Minimum Radius and Maximum Radius    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def IntermediateAreas(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) IntermediateAreas
         Returns the Color for Areas Where the Radius is Between Minimum Radius and Maximum Radius    
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) IntermediateAreas

    ##  Returns the Color for Areas Where the Radius is Between Minimum Radius and Maximum Radius    
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @IntermediateAreas.setter
    def IntermediateAreas(self, intermediateAreas: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) IntermediateAreas
         Returns the Color for Areas Where the Radius is Between Minimum Radius and Maximum Radius    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InternalBallDiameter
    ##  Returns the Internal Ball Diameter for Fold Measurement Analysis   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def InternalBallDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InternalBallDiameter
         Returns the Internal Ball Diameter for Fold Measurement Analysis   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaximumRadius
    ##  Returns the maximum radius is Threshold for smooth areas
    ##             Areas exceeding this threshold are considered as smooth areas   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaximumRadius(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaximumRadius
         Returns the maximum radius is Threshold for smooth areas
                    Areas exceeding this threshold are considered as smooth areas   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MinimumRadius
    ##  Returns the minimum radius is Threshold for smooth areas
    ##             Areas having less radius than this threshold are considered as Sharp Areas.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MinimumRadius(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MinimumRadius
         Returns the minimum radius is Threshold for smooth areas
                    Areas having less radius than this threshold are considered as Sharp Areas.  
             
         
        """
        pass
    
    ## Getter for property: (@link FaceAnalysisNormalsBuilder NXOpen.GeometricAnalysis.FaceAnalysisNormalsBuilder@endlink) Normals
    ##  Returns the Contact analysis normals.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return FaceAnalysisNormalsBuilder
    @property
    def Normals(self) -> FaceAnalysisNormalsBuilder:
        """
        Getter for property: (@link FaceAnalysisNormalsBuilder NXOpen.GeometricAnalysis.FaceAnalysisNormalsBuilder@endlink) Normals
         Returns the Contact analysis normals.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProtrusionLimit
    ##  Returns the protrusion limit is Threshold for Ram Apparatus Analysis and Fold Measurement Analysis   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ProtrusionLimit(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ProtrusionLimit
         Returns the protrusion limit is Threshold for Ram Apparatus Analysis and Fold Measurement Analysis   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RamDiameter
    ##  Returns the Ram Diameter for Ram Apparatus Analysis   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RamDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RamDiameter
         Returns the Ram Diameter for Ram Apparatus Analysis   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) SharpAreas
    ##  Returns the color for Sharp Areas Where the Radius is Less than Minimum Radius    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def SharpAreas(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) SharpAreas
         Returns the color for Sharp Areas Where the Radius is Less than Minimum Radius    
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) SharpAreas

    ##  Returns the color for Sharp Areas Where the Radius is Less than Minimum Radius    
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @SharpAreas.setter
    def SharpAreas(self, sharpAreas: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) SharpAreas
         Returns the color for Sharp Areas Where the Radius is Less than Minimum Radius    
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowOnlyContactAnalysisAreas
    ##  Returns the toggle to Show only Ball touching Areas   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def ShowOnlyContactAnalysisAreas(self) -> bool:
        """
        Getter for property: (bool) ShowOnlyContactAnalysisAreas
         Returns the toggle to Show only Ball touching Areas   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowOnlyContactAnalysisAreas

    ##  Returns the toggle to Show only Ball touching Areas   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ShowOnlyContactAnalysisAreas.setter
    def ShowOnlyContactAnalysisAreas(self, showOnlyContactAnalysisAreas: bool):
        """
        Setter for property: (bool) ShowOnlyContactAnalysisAreas
         Returns the toggle to Show only Ball touching Areas   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowOnlySharpAreas
    ##  Returns the toggle that enables show only sharp areas
    ##             the Radius Analysis will be performed on the Ball touching Areas   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def ShowOnlySharpAreas(self) -> bool:
        """
        Getter for property: (bool) ShowOnlySharpAreas
         Returns the toggle that enables show only sharp areas
                    the Radius Analysis will be performed on the Ball touching Areas   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowOnlySharpAreas

    ##  Returns the toggle that enables show only sharp areas
    ##             the Radius Analysis will be performed on the Ball touching Areas   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ShowOnlySharpAreas.setter
    def ShowOnlySharpAreas(self, showOnlySharpAreas: bool):
        """
        Setter for property: (bool) ShowOnlySharpAreas
         Returns the toggle that enables show only sharp areas
                    the Radius Analysis will be performed on the Ball touching Areas   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) SmoothAreas
    ##  Returns the Color for Smooth Areas Where the Radius is Less Than Minimum Radius   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def SmoothAreas(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) SmoothAreas
         Returns the Color for Smooth Areas Where the Radius is Less Than Minimum Radius   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) SmoothAreas

    ##  Returns the Color for Smooth Areas Where the Radius is Less Than Minimum Radius   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @SmoothAreas.setter
    def SmoothAreas(self, smoothAreas: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) SmoothAreas
         Returns the Color for Smooth Areas Where the Radius is Less Than Minimum Radius   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StepDistance
    ##  Returns the step distance to Create equidistant points on selected bodies   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def StepDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StepDistance
         Returns the step distance to Create equidistant points on selected bodies   
            
         
        """
        pass
    
    ##  Add geometric constraint point to checker 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="face"> (@link NXOpen.Face NXOpen.Face@endlink) </param>
    ## <param name="point"> (@link NXOpen.Point NXOpen.Point@endlink) </param>
    def AddGCPoint(self, face: NXOpen.Face, point: NXOpen.Point) -> None:
        """
         Add geometric constraint point to checker 
        """
        pass
    
    ##  Clear geometric constraint points from checker 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    def ClearGConstraintPointData(self) -> None:
        """
         Clear geometric constraint points from checker 
        """
        pass
    
    ##  Create Check Points 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    def CreateCheckPoints(self) -> None:
        """
         Create Check Points 
        """
        pass
    
    ##  Create Section Curves 
    ##  @return sectionCurveBuilder (@link ContactAnalysisSectionCurveBuilder NXOpen.GeometricAnalysis.ContactAnalysisSectionCurveBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    def CreateSectionCurves(self) -> ContactAnalysisSectionCurveBuilder:
        """
         Create Section Curves 
         @return sectionCurveBuilder (@link ContactAnalysisSectionCurveBuilder NXOpen.GeometricAnalysis.ContactAnalysisSectionCurveBuilder@endlink): .
        """
        pass
    
    ##  Delete geometric constraint point from checker 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="point"> (@link NXOpen.Point NXOpen.Point@endlink) </param>
    def DeleteGCPoint(self, point: NXOpen.Point) -> None:
        """
         Delete geometric constraint point from checker 
        """
        pass
    
    ##  Create Save Contour Curves 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    def SaveContourCurves(self) -> None:
        """
         Create Save Contour Curves 
        """
        pass
    
    ##  Set geometric constraint point to checker 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="face"> (@link NXOpen.Face NXOpen.Face@endlink) </param>
    ## <param name="point"> (@link NXOpen.Point NXOpen.Point@endlink) </param>
    def SetGCPoint(self, face: NXOpen.Face, point: NXOpen.Point) -> None:
        """
         Set geometric constraint point to checker 
        """
        pass
    
    ##  Update the checker 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    def Update(self) -> None:
        """
         Update the checker 
        """
        pass
    
import NXOpen.Validate
## 
##      Represents an NX @link NXOpen::GeometricAnalysis::ContactAnalysisResult NXOpen::GeometricAnalysis::ContactAnalysisResult@endlink  object.
##     
## 
##   <br>  Created in NX1980.0.0  <br> 

class ContactAnalysisResult(NXOpen.Validate.AnalysisResult): 
    """
     Represents an NX <ja_class>NXOpen.GeometricAnalysis.ContactAnalysisResult</ja_class> object.
    """
    pass


import NXOpen
import NXOpen.Display
##  Represents Section Curve Builder in Contact Analysis
##     After Contact Analysis to visualize how the analysis is performed at certain point Section curves is used
##     User can select a point, A ball is placed at the selected point.
##     The plane of the section is constructed from selected point, sphere center and the plane of minimum radius at that point
##     the section curves and section preview is displayed
##     Section Curves can be saved <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisResultCollection::CreateContactAnalysisSectionCurveBuilder  NXOpen::GeometricAnalysis::AnalysisResultCollection::CreateContactAnalysisSectionCurveBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## BoxExtentDelayUpdate </term> <description> 
##  
## false </description> </item> 
## 
## <item><term> 
##  
## CapColorOption </term> <description> 
##  
## Any </description> </item> 
## 
## <item><term> 
##  
## ClipType </term> <description> 
##  
## Section </description> </item> 
## 
## <item><term> 
##  
## CurveColorOption </term> <description> 
##  
## Any </description> </item> 
## 
## <item><term> 
##  
## CurveFont </term> <description> 
##  
## Solid </description> </item> 
## 
## <item><term> 
##  
## CurveWidth </term> <description> 
##  
## Two </description> </item> 
## 
## <item><term> 
##  
## DisplaySlice </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## LockPlanes </term> <description> 
##  
## true </description> </item> 
## 
## <item><term> 
##  
## SectionBoundary.Value </term> <description> 
##  
## 300 (millimeters part), 11.812 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ShowCap </term> <description> 
##  
## true </description> </item> 
## 
## <item><term> 
##  
## ShowClip </term> <description> 
##  
## true </description> </item> 
## 
## <item><term> 
##  
## ShowCurves (deprecated) </term> <description> 
##  
## false </description> </item> 
## 
## <item><term> 
##  
## ShowGrid </term> <description> 
##  
## false </description> </item> 
## 
## <item><term> 
##  
## ShowInterference </term> <description> 
##  
## false </description> </item> 
## 
## <item><term> 
##  
## ShowViewer </term> <description> 
##  
## false </description> </item> 
## 
## <item><term> 
##  
## Type </term> <description> 
##  
## OnePlane </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1980.0.0  <br> 

class ContactAnalysisSectionCurveBuilder(NXOpen.Display.DynamicSectionBuilder): 
    """ Represents Section Curve Builder in Contact Analysis
    After Contact Analysis to visualize how the analysis is performed at certain point Section curves is used
    User can select a point, A ball is placed at the selected point.
    The plane of the section is constructed from selected point, sphere center and the plane of minimum radius at that point
    the section curves and section preview is displayed
    Section Curves can be saved"""


    ## Getter for property: (float) BallDiameter
    ##  Returns the Ball diameter of contact Analysis  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return float
    @property
    def BallDiameter(self) -> float:
        """
        Getter for property: (float) BallDiameter
         Returns the Ball diameter of contact Analysis  
            
         
        """
        pass
    
    ## Setter for property: (float) BallDiameter

    ##  Returns the Ball diameter of contact Analysis  
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @BallDiameter.setter
    def BallDiameter(self, ballDiameter: float):
        """
        Setter for property: (float) BallDiameter
         Returns the Ball diameter of contact Analysis  
            
         
        """
        pass
    
    ## Getter for property: (bool) DisplaySlice
    ##  Returns the toggle to display section view i.  
    ##   e. slice  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def DisplaySlice(self) -> bool:
        """
        Getter for property: (bool) DisplaySlice
         Returns the toggle to display section view i.  
          e. slice  
         
        """
        pass
    
    ## Setter for property: (bool) DisplaySlice

    ##  Returns the toggle to display section view i.  
    ##   e. slice  
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @DisplaySlice.setter
    def DisplaySlice(self, displaySlice: bool):
        """
        Setter for property: (bool) DisplaySlice
         Returns the toggle to display section view i.  
          e. slice  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointToPlaceSphere
    ##  Returns the point to place sphere 
    ##             This points should be only on faces of selected bodies for Contact Analysis  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def PointToPlaceSphere(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointToPlaceSphere
         Returns the point to place sphere 
                    This points should be only on faces of selected bodies for Contact Analysis  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointToPlaceSphere

    ##  Returns the point to place sphere 
    ##             This points should be only on faces of selected bodies for Contact Analysis  
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @PointToPlaceSphere.setter
    def PointToPlaceSphere(self, pointToPlaceSphere: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointToPlaceSphere
         Returns the point to place sphere 
                    This points should be only on faces of selected bodies for Contact Analysis  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SectionBoundary
    ##  Returns the range of circle up to which the Section curves will be trimmed   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SectionBoundary(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SectionBoundary
         Returns the range of circle up to which the Section curves will be trimmed   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) SectionCurveColor
    ##  Returns the Color for Section Curves   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def SectionCurveColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) SectionCurveColor
         Returns the Color for Section Curves   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) SectionCurveColor

    ##  Returns the Color for Section Curves   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @SectionCurveColor.setter
    def SectionCurveColor(self, curveColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) SectionCurveColor
         Returns the Color for Section Curves   
            
         
        """
        pass
    
    ##  Rotate the view to the section plane 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    def OrientToPlane(self) -> None:
        """
         Rotate the view to the section plane 
        """
        pass
    
import NXOpen
##  Represents a tool to control whether to show a curve's poles,knots,combs,peaks and inflections  <br> To obtain an instance of this class, refer to @link NXOpen::GeometricAnalysis::AnalysisObjectCollection  NXOpen::GeometricAnalysis::AnalysisObjectCollection @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class CurveAnalysisDisplay(NXOpen.Object): 
    """ Represents a tool to control whether to show a curve's poles,knots,combs,peaks and inflections """


    ##  Show flag types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Pole</term><description> 
    ##  show pole   </description> </item><item><term> 
    ## Comb</term><description> 
    ##  show comb </description> </item><item><term> 
    ## Inflection</term><description> 
    ##  show inflection </description> </item><item><term> 
    ## Peak</term><description> 
    ##  show peak      </description> </item><item><term> 
    ## Knot</term><description> 
    ##  show knot      </description> </item><item><term> 
    ## Endpoint</term><description> 
    ##  show endpoint  </description> </item></list>
    class ShowFlagType(Enum):
        """
        Members Include: <Pole> <Comb> <Inflection> <Peak> <Knot> <Endpoint>
        """
        Pole: int
        Comb: int
        Inflection: int
        Peak: int
        Knot: int
        Endpoint: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CurveAnalysisDisplay.ShowFlagType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Gets analysis record 
    ##  @return record (@link CurveAnalysisRecord NXOpen.GeometricAnalysis.CurveAnalysisRecord@endlink):  curve analysis record .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveCurvatureAnalysis NXOpen::GeometricAnalysis::CurveCurvatureAnalysis@endlink .  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="curve"> (@link NXOpen.Curve NXOpen.Curve@endlink)  curve </param>
    def GetAnalysisRecord(self, curve: NXOpen.Curve) -> CurveAnalysisRecord:
        """
         Gets analysis record 
         @return record (@link CurveAnalysisRecord NXOpen.GeometricAnalysis.CurveAnalysisRecord@endlink):  curve analysis record .
        """
        pass
    
    ##  Gets a flag representing end points display state of a curve
    ##  @return show (bool):  .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="curve"> (@link NXOpen.Curve NXOpen.Curve@endlink)  curve </param>
    def GetShowEndPoints(self, curve: NXOpen.Curve) -> bool:
        """
         Gets a flag representing end points display state of a curve
         @return show (bool):  .
        """
        pass
    
    ##  Gets a flag representing knots display state of a b-spline curve
    ##  @return show (bool):  .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="curve"> (@link NXOpen.Curve NXOpen.Curve@endlink)  curve </param>
    def GetShowKnot(self, curve: NXOpen.Curve) -> bool:
        """
         Gets a flag representing knots display state of a b-spline curve
         @return show (bool):  .
        """
        pass
    
    ##  Gets a flag representing poles display state of a b-spline curve
    ##  @return show (bool):  .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="curve"> (@link NXOpen.Curve NXOpen.Curve@endlink)  curve </param>
    def GetShowPole(self, curve: NXOpen.Curve) -> bool:
        """
         Gets a flag representing poles display state of a b-spline curve
         @return show (bool):  .
        """
        pass
    
    ##  Creats a curve analysis record 
    ##  @return record (@link CurveAnalysisRecord NXOpen.GeometricAnalysis.CurveAnalysisRecord@endlink): .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveCurvatureAnalysis NXOpen::GeometricAnalysis::CurveCurvatureAnalysis@endlink .  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    def NewRecord(self) -> CurveAnalysisRecord:
        """
         Creats a curve analysis record 
         @return record (@link CurveAnalysisRecord NXOpen.GeometricAnalysis.CurveAnalysisRecord@endlink): .
        """
        pass
    
    ##  Sets analysis record 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveCurvatureAnalysis NXOpen::GeometricAnalysis::CurveCurvatureAnalysis@endlink .  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="curve"> (@link NXOpen.Curve NXOpen.Curve@endlink)  curve </param>
    ## <param name="record"> (@link CurveAnalysisRecord NXOpen.GeometricAnalysis.CurveAnalysisRecord@endlink)  curve analysis record </param>
    def SetAnalysisRecord(self, curve: NXOpen.Curve, record: CurveAnalysisRecord) -> None:
        """
         Sets analysis record 
        """
        pass
    
    ##  Sets a flag representing end points display state of a curve
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="curve"> (@link NXOpen.Curve NXOpen.Curve@endlink)  curve </param>
    ## <param name="show"> (bool)  </param>
    def SetShowEndPoints(self, curve: NXOpen.Curve, show: bool) -> None:
        """
         Sets a flag representing end points display state of a curve
        """
        pass
    
    ##  Sets show flags 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveCurvatureAnalysis NXOpen::GeometricAnalysis::CurveCurvatureAnalysis@endlink .  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="curve"> (@link NXOpen.Curve NXOpen.Curve@endlink)  curve </param>
    ## <param name="choice"> (@link CurveAnalysisDisplay.ShowFlagType NXOpen.GeometricAnalysis.CurveAnalysisDisplay.ShowFlagType@endlink)  pole/comb/inflection/peak/knot </param>
    ## <param name="on"> (bool)  true/false to show flags </param>
    def SetShowFlag(self, curve: NXOpen.Curve, choice: CurveAnalysisDisplay.ShowFlagType, on: bool) -> None:
        """
         Sets show flags 
        """
        pass
    
    ##  Sets a flag representing knots display state of a b-spline curve
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="curve"> (@link NXOpen.Curve NXOpen.Curve@endlink)  curve </param>
    ## <param name="show"> (bool)  </param>
    def SetShowKnot(self, curve: NXOpen.Curve, show: bool) -> None:
        """
         Sets a flag representing knots display state of a b-spline curve
        """
        pass
    
    ##  Sets a flag representing poles display state of a b-spline curve 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="curve"> (@link NXOpen.Curve NXOpen.Curve@endlink)  curve </param>
    ## <param name="show"> (bool)  </param>
    def SetShowPole(self, curve: NXOpen.Curve, show: bool) -> None:
        """
         Sets a flag representing poles display state of a b-spline curve 
        """
        pass
    
    ##  Shows or hides end points display of curves
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="curves"> (@link NXOpen.Curve List[NXOpen.Curve]@endlink) </param>
    ## <param name="show"> (bool)  </param>
    def ShowCurveEndPoints(self, curves: List[NXOpen.Curve], show: bool) -> None:
        """
         Shows or hides end points display of curves
        """
        pass
    
import NXOpen
##  Represents the information regarding how to display a curve's poles, knots, combs, peaks and inflections 
## 
##   <br>  Created in NX6.0.0  <br> 
## 
##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveAnalysisDisplay NXOpen::GeometricAnalysis::CurveAnalysisDisplay@endlink .  <br> 

class CurveAnalysisRecord(NXOpen.TransientObject): 
    """ Represents the information regarding how to display a curve's poles, knots, combs, peaks and inflections """


    ##  Direction option types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  no direction   </description> </item><item><term> 
    ## PlaneOfCurve</term><description> 
    ##  best fit plane </description> </item><item><term> 
    ## SpecifyVector</term><description> 
    ##  specify vector </description> </item><item><term> 
    ## WorkView</term><description> 
    ##  work view      </description> </item></list>
    class DirectionOptionType(Enum):
        """
        Members Include: <NotSet> <PlaneOfCurve> <SpecifyVector> <WorkView>
        """
        NotSet: int
        PlaneOfCurve: int
        SpecifyVector: int
        WorkView: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CurveAnalysisRecord.DirectionOptionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (int) CombDensity
    ##  Returns the comb density   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveAnalysisDisplay NXOpen::GeometricAnalysis::CurveAnalysisDisplay@endlink .  <br> 

    ## @return int
    @property
    def CombDensity(self) -> int:
        """
        Getter for property: (int) CombDensity
         Returns the comb density   
            
         
        """
        pass
    
    ## Setter for property: (int) CombDensity

    ##  Returns the comb density   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveAnalysisDisplay NXOpen::GeometricAnalysis::CurveAnalysisDisplay@endlink .  <br> 

    @CombDensity.setter
    def CombDensity(self, density: int):
        """
        Setter for property: (int) CombDensity
         Returns the comb density   
            
         
        """
        pass
    
    ## Getter for property: (int) CombInterneedleDensity
    ##  Returns the comb interneedle density   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveAnalysisDisplay NXOpen::GeometricAnalysis::CurveAnalysisDisplay@endlink .  <br> 

    ## @return int
    @property
    def CombInterneedleDensity(self) -> int:
        """
        Getter for property: (int) CombInterneedleDensity
         Returns the comb interneedle density   
            
         
        """
        pass
    
    ## Setter for property: (int) CombInterneedleDensity

    ##  Returns the comb interneedle density   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveAnalysisDisplay NXOpen::GeometricAnalysis::CurveAnalysisDisplay@endlink .  <br> 

    @CombInterneedleDensity.setter
    def CombInterneedleDensity(self, interneedle_density: int):
        """
        Setter for property: (int) CombInterneedleDensity
         Returns the comb interneedle density   
            
         
        """
        pass
    
    ## Getter for property: (float) CombMaxLength
    ##  Returns the comb maximum length   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveAnalysisDisplay NXOpen::GeometricAnalysis::CurveAnalysisDisplay@endlink .  <br> 

    ## @return float
    @property
    def CombMaxLength(self) -> float:
        """
        Getter for property: (float) CombMaxLength
         Returns the comb maximum length   
            
         
        """
        pass
    
    ## Setter for property: (float) CombMaxLength

    ##  Returns the comb maximum length   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveAnalysisDisplay NXOpen::GeometricAnalysis::CurveAnalysisDisplay@endlink .  <br> 

    @CombMaxLength.setter
    def CombMaxLength(self, max_length: float):
        """
        Setter for property: (float) CombMaxLength
         Returns the comb maximum length   
            
         
        """
        pass
    
    ## Getter for property: (float) CombScaleFactor
    ##  Returns the comb scale factor   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveAnalysisDisplay NXOpen::GeometricAnalysis::CurveAnalysisDisplay@endlink .  <br> 

    ## @return float
    @property
    def CombScaleFactor(self) -> float:
        """
        Getter for property: (float) CombScaleFactor
         Returns the comb scale factor   
            
         
        """
        pass
    
    ## Setter for property: (float) CombScaleFactor

    ##  Returns the comb scale factor   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveAnalysisDisplay NXOpen::GeometricAnalysis::CurveAnalysisDisplay@endlink .  <br> 

    @CombScaleFactor.setter
    def CombScaleFactor(self, factor: float):
        """
        Setter for property: (float) CombScaleFactor
         Returns the comb scale factor   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) Direction
    ##  Returns the diection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveAnalysisDisplay NXOpen::GeometricAnalysis::CurveAnalysisDisplay@endlink .  <br> 

    ## @return NXOpen.Vector3d
    @property
    def Direction(self) -> NXOpen.Vector3d:
        """
        Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) Direction
         Returns the diection   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) Direction

    ##  Returns the diection   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveAnalysisDisplay NXOpen::GeometricAnalysis::CurveAnalysisDisplay@endlink .  <br> 

    @Direction.setter
    def Direction(self, direction: NXOpen.Vector3d):
        """
        Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) Direction
         Returns the diection   
            
         
        """
        pass
    
    ## Getter for property: (@link CurveAnalysisRecord.DirectionOptionType NXOpen.GeometricAnalysis.CurveAnalysisRecord.DirectionOptionType@endlink) DirectionOption
    ##  Returns the direction option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveAnalysisDisplay NXOpen::GeometricAnalysis::CurveAnalysisDisplay@endlink .  <br> 

    ## @return CurveAnalysisRecord.DirectionOptionType
    @property
    def DirectionOption(self) -> CurveAnalysisRecord.DirectionOptionType:
        """
        Getter for property: (@link CurveAnalysisRecord.DirectionOptionType NXOpen.GeometricAnalysis.CurveAnalysisRecord.DirectionOptionType@endlink) DirectionOption
         Returns the direction option   
            
         
        """
        pass
    
    ## Setter for property: (@link CurveAnalysisRecord.DirectionOptionType NXOpen.GeometricAnalysis.CurveAnalysisRecord.DirectionOptionType@endlink) DirectionOption

    ##  Returns the direction option   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveAnalysisDisplay NXOpen::GeometricAnalysis::CurveAnalysisDisplay@endlink .  <br> 

    @DirectionOption.setter
    def DirectionOption(self, direction_option: CurveAnalysisRecord.DirectionOptionType):
        """
        Setter for property: (@link CurveAnalysisRecord.DirectionOptionType NXOpen.GeometricAnalysis.CurveAnalysisRecord.DirectionOptionType@endlink) DirectionOption
         Returns the direction option   
            
         
        """
        pass
    
    ## Getter for property: (float) End
    ##  Returns the end parameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveAnalysisDisplay NXOpen::GeometricAnalysis::CurveAnalysisDisplay@endlink .  <br> 

    ## @return float
    @property
    def End(self) -> float:
        """
        Getter for property: (float) End
         Returns the end parameter   
            
         
        """
        pass
    
    ## Setter for property: (float) End

    ##  Returns the end parameter   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveAnalysisDisplay NXOpen::GeometricAnalysis::CurveAnalysisDisplay@endlink .  <br> 

    @End.setter
    def End(self, end: float):
        """
        Setter for property: (float) End
         Returns the end parameter   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowComb
    ##  Returns the flag to show comb   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveAnalysisDisplay NXOpen::GeometricAnalysis::CurveAnalysisDisplay@endlink .  <br> 

    ## @return bool
    @property
    def ShowComb(self) -> bool:
        """
        Getter for property: (bool) ShowComb
         Returns the flag to show comb   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowComb

    ##  Returns the flag to show comb   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveAnalysisDisplay NXOpen::GeometricAnalysis::CurveAnalysisDisplay@endlink .  <br> 

    @ShowComb.setter
    def ShowComb(self, on: bool):
        """
        Setter for property: (bool) ShowComb
         Returns the flag to show comb   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowInflection
    ##  Returns the flag to show inflection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveAnalysisDisplay NXOpen::GeometricAnalysis::CurveAnalysisDisplay@endlink .  <br> 

    ## @return bool
    @property
    def ShowInflection(self) -> bool:
        """
        Getter for property: (bool) ShowInflection
         Returns the flag to show inflection   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowInflection

    ##  Returns the flag to show inflection   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveAnalysisDisplay NXOpen::GeometricAnalysis::CurveAnalysisDisplay@endlink .  <br> 

    @ShowInflection.setter
    def ShowInflection(self, on: bool):
        """
        Setter for property: (bool) ShowInflection
         Returns the flag to show inflection   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowKnot
    ##  Returns the flag to show knot   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveAnalysisDisplay NXOpen::GeometricAnalysis::CurveAnalysisDisplay@endlink .  <br> 

    ## @return bool
    @property
    def ShowKnot(self) -> bool:
        """
        Getter for property: (bool) ShowKnot
         Returns the flag to show knot   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowKnot

    ##  Returns the flag to show knot   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveAnalysisDisplay NXOpen::GeometricAnalysis::CurveAnalysisDisplay@endlink .  <br> 

    @ShowKnot.setter
    def ShowKnot(self, on: bool):
        """
        Setter for property: (bool) ShowKnot
         Returns the flag to show knot   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowPeak
    ##  Returns the flag to show peak   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveAnalysisDisplay NXOpen::GeometricAnalysis::CurveAnalysisDisplay@endlink .  <br> 

    ## @return bool
    @property
    def ShowPeak(self) -> bool:
        """
        Getter for property: (bool) ShowPeak
         Returns the flag to show peak   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowPeak

    ##  Returns the flag to show peak   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveAnalysisDisplay NXOpen::GeometricAnalysis::CurveAnalysisDisplay@endlink .  <br> 

    @ShowPeak.setter
    def ShowPeak(self, on: bool):
        """
        Setter for property: (bool) ShowPeak
         Returns the flag to show peak   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowPole
    ##  Returns the flag to show pole   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveAnalysisDisplay NXOpen::GeometricAnalysis::CurveAnalysisDisplay@endlink .  <br> 

    ## @return bool
    @property
    def ShowPole(self) -> bool:
        """
        Getter for property: (bool) ShowPole
         Returns the flag to show pole   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowPole

    ##  Returns the flag to show pole   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveAnalysisDisplay NXOpen::GeometricAnalysis::CurveAnalysisDisplay@endlink .  <br> 

    @ShowPole.setter
    def ShowPole(self, on: bool):
        """
        Setter for property: (bool) ShowPole
         Returns the flag to show pole   
            
         
        """
        pass
    
    ## Getter for property: (float) Start
    ##  Returns the start parameter, range from 0 to 100   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveAnalysisDisplay NXOpen::GeometricAnalysis::CurveAnalysisDisplay@endlink .  <br> 

    ## @return float
    @property
    def Start(self) -> float:
        """
        Getter for property: (float) Start
         Returns the start parameter, range from 0 to 100   
            
         
        """
        pass
    
    ## Setter for property: (float) Start

    ##  Returns the start parameter, range from 0 to 100   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveAnalysisDisplay NXOpen::GeometricAnalysis::CurveAnalysisDisplay@endlink .  <br> 

    @Start.setter
    def Start(self, start: float):
        """
        Setter for property: (float) Start
         Returns the start parameter, range from 0 to 100   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseMaxLength
    ##  Returns the flag to limit the maximum length of the comb   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveAnalysisDisplay NXOpen::GeometricAnalysis::CurveAnalysisDisplay@endlink .  <br> 

    ## @return bool
    @property
    def UseMaxLength(self) -> bool:
        """
        Getter for property: (bool) UseMaxLength
         Returns the flag to limit the maximum length of the comb   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseMaxLength

    ##  Returns the flag to limit the maximum length of the comb   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveAnalysisDisplay NXOpen::GeometricAnalysis::CurveAnalysisDisplay@endlink .  <br> 

    @UseMaxLength.setter
    def UseMaxLength(self, on: bool):
        """
        Setter for property: (bool) UseMaxLength
         Returns the flag to limit the maximum length of the comb   
            
         
        """
        pass
    
    ##  Free resources associated with the instance. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::GeometricAnalysis::CurveAnalysisDisplay NXOpen::GeometricAnalysis::CurveAnalysisDisplay@endlink .  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. 
        """
        pass
    
import NXOpen
##  Represents a curve continuity builder  <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisObjectCollection::CreateCurveContinuityBuilder  NXOpen::GeometricAnalysis::AnalysisObjectCollection::CreateCurveContinuityBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AngularThreshold.Value </term> <description> 
##  
## 15.0 </description> </item> 
## 
## <item><term> 
##  
## ContinuityType </term> <description> 
##  
## Multicurve </description> </item> 
## 
## <item><term> 
##  
## DistanceThreshold.Value </term> <description> 
##  
## 10.0 (millimeters part), 0.5 (inches part) </description> </item> 
## 
## <item><term> 
##  
## EndPointX </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## EndPointY </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## EndPointZ </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## G0Check </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## G0Check2 </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## G0Tolerance </term> <description> 
##  
## 0.01 </description> </item> 
## 
## <item><term> 
##  
## G1Check </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## G1Check2 </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## G1Tolerance </term> <description> 
##  
## 0.5 </description> </item> 
## 
## <item><term> 
##  
## G2Check </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## G2Check2 </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## G2Tolerance </term> <description> 
##  
## 0.5 </description> </item> 
## 
## <item><term> 
##  
## G3Check </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## G3Check2 </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## G3Tolerance </term> <description> 
##  
## 0.5 </description> </item> 
## 
## <item><term> 
##  
## ShowDeviation </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## ShowMarkup </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## ShowMaximum </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ShowMinimum </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ShowNeedle </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## ShowOutOfTolerance </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX7.0.0  <br> 

class CurveContinuityBuilder(NXOpen.Builder): 
    """ Represents a curve continuity builder """


    ##  Define curve continuity types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## CurvetoObject</term><description> 
    ##  curve to object </description> </item><item><term> 
    ## Multicurve</term><description> 
    ##  multicurve </description> </item></list>
    class Type(Enum):
        """
        Members Include: <CurvetoObject> <Multicurve>
        """
        CurvetoObject: int
        Multicurve: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CurveContinuityBuilder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) AngularThreshold
    ##  Returns the angular threshold   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.Expression
    @property
    def AngularThreshold(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) AngularThreshold
         Returns the angular threshold   
            
         
        """
        pass
    
    ## Getter for property: (@link CurveContinuityBuilder.Type NXOpen.GeometricAnalysis.CurveContinuityBuilder.Type@endlink) ContinuityType
    ##  Returns the curve continuity type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return CurveContinuityBuilder.Type
    @property
    def ContinuityType(self) -> CurveContinuityBuilder.Type:
        """
        Getter for property: (@link CurveContinuityBuilder.Type NXOpen.GeometricAnalysis.CurveContinuityBuilder.Type@endlink) ContinuityType
         Returns the curve continuity type   
            
         
        """
        pass
    
    ## Setter for property: (@link CurveContinuityBuilder.Type NXOpen.GeometricAnalysis.CurveContinuityBuilder.Type@endlink) ContinuityType

    ##  Returns the curve continuity type   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @ContinuityType.setter
    def ContinuityType(self, continuityType: CurveContinuityBuilder.Type):
        """
        Setter for property: (@link CurveContinuityBuilder.Type NXOpen.GeometricAnalysis.CurveContinuityBuilder.Type@endlink) ContinuityType
         Returns the curve continuity type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceThreshold
    ##  Returns the distance threshold   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.Expression
    @property
    def DistanceThreshold(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceThreshold
         Returns the distance threshold   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) DynamicLabel
    ##  Returns the location for dynamic label   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def DynamicLabel(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) DynamicLabel
         Returns the location for dynamic label   
            
         
        """
        pass
    
    ## Getter for property: (float) EndPointX
    ##  Returns the end point x value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return float
    @property
    def EndPointX(self) -> float:
        """
        Getter for property: (float) EndPointX
         Returns the end point x value   
            
         
        """
        pass
    
    ## Setter for property: (float) EndPointX

    ##  Returns the end point x value   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @EndPointX.setter
    def EndPointX(self, endPointX: float):
        """
        Setter for property: (float) EndPointX
         Returns the end point x value   
            
         
        """
        pass
    
    ## Getter for property: (float) EndPointY
    ##  Returns the end point y value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return float
    @property
    def EndPointY(self) -> float:
        """
        Getter for property: (float) EndPointY
         Returns the end point y value   
            
         
        """
        pass
    
    ## Setter for property: (float) EndPointY

    ##  Returns the end point y value   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @EndPointY.setter
    def EndPointY(self, endPointY: float):
        """
        Setter for property: (float) EndPointY
         Returns the end point y value   
            
         
        """
        pass
    
    ## Getter for property: (float) EndPointZ
    ##  Returns the end point z value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return float
    @property
    def EndPointZ(self) -> float:
        """
        Getter for property: (float) EndPointZ
         Returns the end point z value   
            
         
        """
        pass
    
    ## Setter for property: (float) EndPointZ

    ##  Returns the end point z value   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @EndPointZ.setter
    def EndPointZ(self, endPointZ: float):
        """
        Setter for property: (float) EndPointZ
         Returns the end point z value   
            
         
        """
        pass
    
    ## Getter for property: (bool) G0Check
    ##  Returns the G0 check   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return bool
    @property
    def G0Check(self) -> bool:
        """
        Getter for property: (bool) G0Check
         Returns the G0 check   
            
         
        """
        pass
    
    ## Setter for property: (bool) G0Check

    ##  Returns the G0 check   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @G0Check.setter
    def G0Check(self, g0Check: bool):
        """
        Setter for property: (bool) G0Check
         Returns the G0 check   
            
         
        """
        pass
    
    ## Getter for property: (bool) G0Check2
    ##  Returns the G0 check for multicurve   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def G0Check2(self) -> bool:
        """
        Getter for property: (bool) G0Check2
         Returns the G0 check for multicurve   
            
         
        """
        pass
    
    ## Setter for property: (bool) G0Check2

    ##  Returns the G0 check for multicurve   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @G0Check2.setter
    def G0Check2(self, g0Check2: bool):
        """
        Setter for property: (bool) G0Check2
         Returns the G0 check for multicurve   
            
         
        """
        pass
    
    ## Getter for property: (float) G0Tolerance
    ##  Returns the g0 tolerance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def G0Tolerance(self) -> float:
        """
        Getter for property: (float) G0Tolerance
         Returns the g0 tolerance   
            
         
        """
        pass
    
    ## Setter for property: (float) G0Tolerance

    ##  Returns the g0 tolerance   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @G0Tolerance.setter
    def G0Tolerance(self, g0Tolerance: float):
        """
        Setter for property: (float) G0Tolerance
         Returns the g0 tolerance   
            
         
        """
        pass
    
    ## Getter for property: (bool) G1Check
    ##  Returns the G1 check   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return bool
    @property
    def G1Check(self) -> bool:
        """
        Getter for property: (bool) G1Check
         Returns the G1 check   
            
         
        """
        pass
    
    ## Setter for property: (bool) G1Check

    ##  Returns the G1 check   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @G1Check.setter
    def G1Check(self, g1Check: bool):
        """
        Setter for property: (bool) G1Check
         Returns the G1 check   
            
         
        """
        pass
    
    ## Getter for property: (bool) G1Check2
    ##  Returns the G1 check for multicurve   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def G1Check2(self) -> bool:
        """
        Getter for property: (bool) G1Check2
         Returns the G1 check for multicurve   
            
         
        """
        pass
    
    ## Setter for property: (bool) G1Check2

    ##  Returns the G1 check for multicurve   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @G1Check2.setter
    def G1Check2(self, g1Check2: bool):
        """
        Setter for property: (bool) G1Check2
         Returns the G1 check for multicurve   
            
         
        """
        pass
    
    ## Getter for property: (float) G1Tolerance
    ##  Returns the g1 tolerance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def G1Tolerance(self) -> float:
        """
        Getter for property: (float) G1Tolerance
         Returns the g1 tolerance   
            
         
        """
        pass
    
    ## Setter for property: (float) G1Tolerance

    ##  Returns the g1 tolerance   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @G1Tolerance.setter
    def G1Tolerance(self, g1Tolerance: float):
        """
        Setter for property: (float) G1Tolerance
         Returns the g1 tolerance   
            
         
        """
        pass
    
    ## Getter for property: (bool) G2Check
    ##  Returns the G2 check   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return bool
    @property
    def G2Check(self) -> bool:
        """
        Getter for property: (bool) G2Check
         Returns the G2 check   
            
         
        """
        pass
    
    ## Setter for property: (bool) G2Check

    ##  Returns the G2 check   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @G2Check.setter
    def G2Check(self, g2Check: bool):
        """
        Setter for property: (bool) G2Check
         Returns the G2 check   
            
         
        """
        pass
    
    ## Getter for property: (bool) G2Check2
    ##  Returns the G2 check for multicurve   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def G2Check2(self) -> bool:
        """
        Getter for property: (bool) G2Check2
         Returns the G2 check for multicurve   
            
         
        """
        pass
    
    ## Setter for property: (bool) G2Check2

    ##  Returns the G2 check for multicurve   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @G2Check2.setter
    def G2Check2(self, g2Check2: bool):
        """
        Setter for property: (bool) G2Check2
         Returns the G2 check for multicurve   
            
         
        """
        pass
    
    ## Getter for property: (float) G2Tolerance
    ##  Returns the g2 tolerance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def G2Tolerance(self) -> float:
        """
        Getter for property: (float) G2Tolerance
         Returns the g2 tolerance   
            
         
        """
        pass
    
    ## Setter for property: (float) G2Tolerance

    ##  Returns the g2 tolerance   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @G2Tolerance.setter
    def G2Tolerance(self, g2Tolerance: float):
        """
        Setter for property: (float) G2Tolerance
         Returns the g2 tolerance   
            
         
        """
        pass
    
    ## Getter for property: (bool) G3Check
    ##  Returns the G3 check   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return bool
    @property
    def G3Check(self) -> bool:
        """
        Getter for property: (bool) G3Check
         Returns the G3 check   
            
         
        """
        pass
    
    ## Setter for property: (bool) G3Check

    ##  Returns the G3 check   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @G3Check.setter
    def G3Check(self, g3Check: bool):
        """
        Setter for property: (bool) G3Check
         Returns the G3 check   
            
         
        """
        pass
    
    ## Getter for property: (bool) G3Check2
    ##  Returns the G3 check for multicurve   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def G3Check2(self) -> bool:
        """
        Getter for property: (bool) G3Check2
         Returns the G3 check for multicurve   
            
         
        """
        pass
    
    ## Setter for property: (bool) G3Check2

    ##  Returns the G3 check for multicurve   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @G3Check2.setter
    def G3Check2(self, g3Check2: bool):
        """
        Setter for property: (bool) G3Check2
         Returns the G3 check for multicurve   
            
         
        """
        pass
    
    ## Getter for property: (float) G3Tolerance
    ##  Returns the g3 tolerance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def G3Tolerance(self) -> float:
        """
        Getter for property: (float) G3Tolerance
         Returns the g3 tolerance   
            
         
        """
        pass
    
    ## Setter for property: (float) G3Tolerance

    ##  Returns the g3 tolerance   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @G3Tolerance.setter
    def G3Tolerance(self, g3Tolerance: float):
        """
        Setter for property: (float) G3Tolerance
         Returns the g3 tolerance   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) MultiCurve
    ##  Returns the multiple curve   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def MultiCurve(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) MultiCurve
         Returns the multiple curve   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) SelectCurve
    ##  Returns the select curve   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def SelectCurve(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) SelectCurve
         Returns the select curve   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) SelectObject
    ##  Returns the select object   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def SelectObject(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) SelectObject
         Returns the select object   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowDeviation
    ##  Returns the show deviation label   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def ShowDeviation(self) -> bool:
        """
        Getter for property: (bool) ShowDeviation
         Returns the show deviation label   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowDeviation

    ##  Returns the show deviation label   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @ShowDeviation.setter
    def ShowDeviation(self, showDeviation: bool):
        """
        Setter for property: (bool) ShowDeviation
         Returns the show deviation label   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowMarkup
    ##  Returns the show tolerance markup   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def ShowMarkup(self) -> bool:
        """
        Getter for property: (bool) ShowMarkup
         Returns the show tolerance markup   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowMarkup

    ##  Returns the show tolerance markup   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @ShowMarkup.setter
    def ShowMarkup(self, showMarkup: bool):
        """
        Setter for property: (bool) ShowMarkup
         Returns the show tolerance markup   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowMaximum
    ##  Returns the show maximum label   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def ShowMaximum(self) -> bool:
        """
        Getter for property: (bool) ShowMaximum
         Returns the show maximum label   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowMaximum

    ##  Returns the show maximum label   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @ShowMaximum.setter
    def ShowMaximum(self, showMaximum: bool):
        """
        Setter for property: (bool) ShowMaximum
         Returns the show maximum label   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowMinimum
    ##  Returns the show minimum label   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def ShowMinimum(self) -> bool:
        """
        Getter for property: (bool) ShowMinimum
         Returns the show minimum label   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowMinimum

    ##  Returns the show minimum label   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @ShowMinimum.setter
    def ShowMinimum(self, showMinimum: bool):
        """
        Setter for property: (bool) ShowMinimum
         Returns the show minimum label   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowNeedle
    ##  Returns the show needle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return bool
    @property
    def ShowNeedle(self) -> bool:
        """
        Getter for property: (bool) ShowNeedle
         Returns the show needle   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowNeedle

    ##  Returns the show needle   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @ShowNeedle.setter
    def ShowNeedle(self, showNeedle: bool):
        """
        Setter for property: (bool) ShowNeedle
         Returns the show needle   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowOutOfTolerance
    ##  Returns the show out of tolerance only   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def ShowOutOfTolerance(self) -> bool:
        """
        Getter for property: (bool) ShowOutOfTolerance
         Returns the show out of tolerance only   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowOutOfTolerance

    ##  Returns the show out of tolerance only   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @ShowOutOfTolerance.setter
    def ShowOutOfTolerance(self, showOutOfTolerance: bool):
        """
        Setter for property: (bool) ShowOutOfTolerance
         Returns the show out of tolerance only   
            
         
        """
        pass
    
    ##  Prepare to toggle deviation label 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: gateway ("UG GATEWAY")
    def ResetShowDeviation(self) -> None:
        """
         Prepare to toggle deviation label 
        """
        pass
    
##  Represents a Curve Continuity Analysis builder  <br> To create or edit an instance of this class, use @link NXOpen::GeometricAnalysis::CurveContinuityBuilder  NXOpen::GeometricAnalysis::CurveContinuityBuilder @endlink  <br> 
## 
##   <br>  Created in NX7.0.0  <br> 

class CurveContinuity(AnalysisObject): 
    """ Represents a Curve Continuity Analysis builder """
    pass


import NXOpen
import NXOpen.GeometricUtilities
##  Represents a @link NXOpen::GeometricAnalysis::CurveCurvatureAnalysis NXOpen::GeometricAnalysis::CurveCurvatureAnalysis@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisObjectCollection::CreateCurveCurvatureAnalysisBuilder  NXOpen::GeometricAnalysis::AnalysisObjectCollection::CreateCurveCurvatureAnalysisBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## CombRange.AnchorPosition </term> <description> 
##  
## Start </description> </item> 
## 
## <item><term> 
##  
## DynamicProjection </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## Method </term> <description> 
##  
## Curvature </description> </item> 
## 
## <item><term> 
##  
## Projection </term> <description> 
##  
## None </description> </item> 
## 
## <item><term> 
##  
## ReverseDirection </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ShowInflections </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ShowPeaks </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## Style </term> <description> 
##  
## Linear </description> </item> 
## 
## <item><term> 
##  
## Xyz </term> <description> 
##  
## X </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX7.0.0  <br> 

class CurveCurvatureAnalysisBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.GeometricAnalysis.CurveCurvatureAnalysis</ja_class> builder """


    ##  Enumeration for needle calculation method 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Curvature</term><description> 
    ##  needle of curvature value </description> </item><item><term> 
    ## RadiusofCurvature</term><description> 
    ##  needle of radius of curvature value </description> </item></list>
    class CalculationMethod(Enum):
        """
        Members Include: <Curvature> <RadiusofCurvature>
        """
        Curvature: int
        RadiusofCurvature: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CurveCurvatureAnalysisBuilder.CalculationMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Enumeration for needle display type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Linear</term><description> 
    ##  linear needle </description> </item><item><term> 
    ## Logarithmic</term><description> 
    ##  logarithmic needle </description> </item></list>
    class DisplayStyle(Enum):
        """
        Members Include: <Linear> <Logarithmic>
        """
        Linear: int
        Logarithmic: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CurveCurvatureAnalysisBuilder.DisplayStyle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Enumeration for label computation method 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Curvature</term><description> 
    ##  label showing curvature value </description> </item><item><term> 
    ## RadiusofCurvature</term><description> 
    ##  label showing radius of curvature value </description> </item></list>
    class LabelValues(Enum):
        """
        Members Include: <Curvature> <RadiusofCurvature>
        """
        Curvature: int
        RadiusofCurvature: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CurveCurvatureAnalysisBuilder.LabelValues:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Enumeration for needle direction type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Inside</term><description> 
    ##  needle pointing inside  </description> </item><item><term> 
    ## Outside</term><description> 
    ##  needle pointing outside </description> </item></list>
    class NeedleDirection(Enum):
        """
        Members Include: <Inside> <Outside>
        """
        Inside: int
        Outside: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CurveCurvatureAnalysisBuilder.NeedleDirection:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Projection plane types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  no projection  </description> </item><item><term> 
    ## CurvePlane</term><description> 
    ##  best fit plane </description> </item><item><term> 
    ## Vector</term><description> 
    ##  specify vector </description> </item><item><term> 
    ## View</term><description> 
    ##  view plane     </description> </item><item><term> 
    ## Xyz</term><description> 
    ##  specify x,y,z plane </description> </item></list>
    class ProjectionTypes(Enum):
        """
        Members Include: <NotSet> <CurvePlane> <Vector> <View> <Xyz>
        """
        NotSet: int
        CurvePlane: int
        Vector: int
        View: int
        Xyz: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CurveCurvatureAnalysisBuilder.ProjectionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Enumeration for X, Y or Z projection plane 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## X</term><description> 
    ##  x-axis plane </description> </item><item><term> 
    ## Y</term><description> 
    ##  y-axis plane </description> </item><item><term> 
    ## Z</term><description> 
    ##  z-axis plane </description> </item></list>
    class XyzTypes(Enum):
        """
        Members Include: <X> <Y> <Z>
        """
        X: int
        Y: int
        Z: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CurveCurvatureAnalysisBuilder.XyzTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.CombOptionsBuilder NXOpen.GeometricUtilities.CombOptionsBuilder@endlink) CombOptions
    ##  Returns the comb display block options   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.CombOptionsBuilder
    @property
    def CombOptions(self) -> NXOpen.GeometricUtilities.CombOptionsBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.CombOptionsBuilder NXOpen.GeometricUtilities.CombOptionsBuilder@endlink) CombOptions
         Returns the comb display block options   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.CurveRangeBuilder NXOpen.GeometricUtilities.CurveRangeBuilder@endlink) CombRange
    ##  Returns the comb range   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.CurveRangeBuilder
    @property
    def CombRange(self) -> NXOpen.GeometricUtilities.CurveRangeBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.CurveRangeBuilder NXOpen.GeometricUtilities.CurveRangeBuilder@endlink) CombRange
         Returns the comb range   
            
         
        """
        pass
    
    ## Getter for property: (bool) DynamicProjection
    ##  Returns the dynamic projection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return bool
    @property
    def DynamicProjection(self) -> bool:
        """
        Getter for property: (bool) DynamicProjection
         Returns the dynamic projection   
            
         
        """
        pass
    
    ## Setter for property: (bool) DynamicProjection

    ##  Returns the dynamic projection   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @DynamicProjection.setter
    def DynamicProjection(self, dynamicProjection: bool):
        """
        Setter for property: (bool) DynamicProjection
         Returns the dynamic projection   
            
         
        """
        pass
    
    ## Getter for property: (@link CurveCurvatureAnalysisBuilder.CalculationMethod NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilder.CalculationMethod@endlink) Method
    ##  Returns the method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return CurveCurvatureAnalysisBuilder.CalculationMethod
    @property
    def Method(self) -> CurveCurvatureAnalysisBuilder.CalculationMethod:
        """
        Getter for property: (@link CurveCurvatureAnalysisBuilder.CalculationMethod NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilder.CalculationMethod@endlink) Method
         Returns the method   
            
         
        """
        pass
    
    ## Setter for property: (@link CurveCurvatureAnalysisBuilder.CalculationMethod NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilder.CalculationMethod@endlink) Method

    ##  Returns the method   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @Method.setter
    def Method(self, method: CurveCurvatureAnalysisBuilder.CalculationMethod):
        """
        Setter for property: (@link CurveCurvatureAnalysisBuilder.CalculationMethod NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilder.CalculationMethod@endlink) Method
         Returns the method   
            
         
        """
        pass
    
    ## Getter for property: (@link CurveCurvatureAnalysisBuilder.ProjectionTypes NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilder.ProjectionTypes@endlink) Projection
    ##  Returns the projection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return CurveCurvatureAnalysisBuilder.ProjectionTypes
    @property
    def Projection(self) -> CurveCurvatureAnalysisBuilder.ProjectionTypes:
        """
        Getter for property: (@link CurveCurvatureAnalysisBuilder.ProjectionTypes NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilder.ProjectionTypes@endlink) Projection
         Returns the projection   
            
         
        """
        pass
    
    ## Setter for property: (@link CurveCurvatureAnalysisBuilder.ProjectionTypes NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilder.ProjectionTypes@endlink) Projection

    ##  Returns the projection   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @Projection.setter
    def Projection(self, projection: CurveCurvatureAnalysisBuilder.ProjectionTypes):
        """
        Setter for property: (@link CurveCurvatureAnalysisBuilder.ProjectionTypes NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilder.ProjectionTypes@endlink) Projection
         Returns the projection   
            
         
        """
        pass
    
    ## Getter for property: (int) ReverseDirection
    ##  Returns the reverse direction   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return int
    @property
    def ReverseDirection(self) -> int:
        """
        Getter for property: (int) ReverseDirection
         Returns the reverse direction   
            
         
        """
        pass
    
    ## Setter for property: (int) ReverseDirection

    ##  Returns the reverse direction   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @ReverseDirection.setter
    def ReverseDirection(self, reverseDirection: int):
        """
        Setter for property: (int) ReverseDirection
         Returns the reverse direction   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SelectedCurves
    ##  Returns the selected curves and/or edges   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def SelectedCurves(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SelectedCurves
         Returns the selected curves and/or edges   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowCombs
    ##  Returns the show combs   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return bool
    @property
    def ShowCombs(self) -> bool:
        """
        Getter for property: (bool) ShowCombs
         Returns the show combs   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowCombs

    ##  Returns the show combs   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @ShowCombs.setter
    def ShowCombs(self, showCombs: bool):
        """
        Setter for property: (bool) ShowCombs
         Returns the show combs   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowInflections
    ##  Returns the show inflections   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return bool
    @property
    def ShowInflections(self) -> bool:
        """
        Getter for property: (bool) ShowInflections
         Returns the show inflections   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowInflections

    ##  Returns the show inflections   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @ShowInflections.setter
    def ShowInflections(self, showInflections: bool):
        """
        Setter for property: (bool) ShowInflections
         Returns the show inflections   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowMaxLabels
    ##  Returns the show max labels   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.1  <br> 

    ## @return bool
    @property
    def ShowMaxLabels(self) -> bool:
        """
        Getter for property: (bool) ShowMaxLabels
         Returns the show max labels   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowMaxLabels

    ##  Returns the show max labels   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.1  <br> 

    @ShowMaxLabels.setter
    def ShowMaxLabels(self, showMaxLabels: bool):
        """
        Setter for property: (bool) ShowMaxLabels
         Returns the show max labels   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowMinLabels
    ##  Returns the show min labels   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.1  <br> 

    ## @return bool
    @property
    def ShowMinLabels(self) -> bool:
        """
        Getter for property: (bool) ShowMinLabels
         Returns the show min labels   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowMinLabels

    ##  Returns the show min labels   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.1  <br> 

    @ShowMinLabels.setter
    def ShowMinLabels(self, showMinLabels: bool):
        """
        Setter for property: (bool) ShowMinLabels
         Returns the show min labels   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowPeaks
    ##  Returns the show peaks   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return bool
    @property
    def ShowPeaks(self) -> bool:
        """
        Getter for property: (bool) ShowPeaks
         Returns the show peaks   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowPeaks

    ##  Returns the show peaks   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @ShowPeaks.setter
    def ShowPeaks(self, showPeaks: bool):
        """
        Setter for property: (bool) ShowPeaks
         Returns the show peaks   
            
         
        """
        pass
    
    ## Getter for property: (@link CurveCurvatureAnalysisBuilder.DisplayStyle NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilder.DisplayStyle@endlink) Style
    ##  Returns the style   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return CurveCurvatureAnalysisBuilder.DisplayStyle
    @property
    def Style(self) -> CurveCurvatureAnalysisBuilder.DisplayStyle:
        """
        Getter for property: (@link CurveCurvatureAnalysisBuilder.DisplayStyle NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilder.DisplayStyle@endlink) Style
         Returns the style   
            
         
        """
        pass
    
    ## Setter for property: (@link CurveCurvatureAnalysisBuilder.DisplayStyle NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilder.DisplayStyle@endlink) Style

    ##  Returns the style   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @Style.setter
    def Style(self, style: CurveCurvatureAnalysisBuilder.DisplayStyle):
        """
        Setter for property: (@link CurveCurvatureAnalysisBuilder.DisplayStyle NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilder.DisplayStyle@endlink) Style
         Returns the style   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector
    ##  Returns the vector   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def Vector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector
         Returns the vector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector

    ##  Returns the vector   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @Vector.setter
    def Vector(self, vector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector
         Returns the vector   
            
         
        """
        pass
    
    ## Getter for property: (@link CurveCurvatureAnalysisBuilder.XyzTypes NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilder.XyzTypes@endlink) Xyz
    ##  Returns the xyz   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return CurveCurvatureAnalysisBuilder.XyzTypes
    @property
    def Xyz(self) -> CurveCurvatureAnalysisBuilder.XyzTypes:
        """
        Getter for property: (@link CurveCurvatureAnalysisBuilder.XyzTypes NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilder.XyzTypes@endlink) Xyz
         Returns the xyz   
            
         
        """
        pass
    
    ## Setter for property: (@link CurveCurvatureAnalysisBuilder.XyzTypes NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilder.XyzTypes@endlink) Xyz

    ##  Returns the xyz   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @Xyz.setter
    def Xyz(self, xyz: CurveCurvatureAnalysisBuilder.XyzTypes):
        """
        Setter for property: (@link CurveCurvatureAnalysisBuilder.XyzTypes NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilder.XyzTypes@endlink) Xyz
         Returns the xyz   
            
         
        """
        pass
    
    ##  Create inflection points 
    ##  @return pointArray (@link NXOpen.Point List[NXOpen.Point]@endlink): .
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    def CreateDumbInflectionPoints(self) -> List[NXOpen.Point]:
        """
         Create inflection points 
         @return pointArray (@link NXOpen.Point List[NXOpen.Point]@endlink): .
        """
        pass
    
    ##  Create peak points 
    ##  @return pointArray (@link NXOpen.Point List[NXOpen.Point]@endlink): .
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    def CreateDumbPeakPoints(self) -> List[NXOpen.Point]:
        """
         Create peak points 
         @return pointArray (@link NXOpen.Point List[NXOpen.Point]@endlink): .
        """
        pass
    
    ##  Returns the @link NXOpen::GeometricUtilities::CurveRangeBuilder NXOpen::GeometricUtilities::CurveRangeBuilder@endlink  object at a given index from the list 
    ##  @return combRange (@link NXOpen.GeometricUtilities.CurveRangeBuilder NXOpen.GeometricUtilities.CurveRangeBuilder@endlink): .
    ## 
    ##   <br>  Created in NX8.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int) </param>
    def GetCurveRange(self, index: int) -> NXOpen.GeometricUtilities.CurveRangeBuilder:
        """
         Returns the @link NXOpen::GeometricUtilities::CurveRangeBuilder NXOpen::GeometricUtilities::CurveRangeBuilder@endlink  object at a given index from the list 
         @return combRange (@link NXOpen.GeometricUtilities.CurveRangeBuilder NXOpen.GeometricUtilities.CurveRangeBuilder@endlink): .
        """
        pass
    
    ##  Get the number of @link NXOpen::GeometricUtilities::CurveRangeBuilder NXOpen::GeometricUtilities::CurveRangeBuilder@endlink  objects in the list
    ##  @return length (int): .
    ## 
    ##   <br>  Created in NX8.0.1  <br> 

    ## License requirements: None.
    def GetCurveRangeListLength(self) -> int:
        """
         Get the number of @link NXOpen::GeometricUtilities::CurveRangeBuilder NXOpen::GeometricUtilities::CurveRangeBuilder@endlink  objects in the list
         @return length (int): .
        """
        pass
    
    ##  Update work view with a given view matrix 
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: None.
    def UpdateWorkView(self) -> None:
        """
         Update work view with a given view matrix 
        """
        pass
    
##  Represents a CurveCurvatureAnalysis builder  <br> To create or edit an instance of this class, use @link NXOpen::GeometricAnalysis::CurveCurvatureAnalysisBuilder  NXOpen::GeometricAnalysis::CurveCurvatureAnalysisBuilder @endlink  <br> 
## 
##   <br>  Created in NX7.0.0  <br> 

class CurveCurvatureAnalysis(AnalysisObject): 
    """ Represents a CurveCurvatureAnalysis builder """
    pass


import NXOpen
## 
##     Represents a @link NXOpen::GeometricAnalysis::DeviationChecking NXOpen::GeometricAnalysis::DeviationChecking@endlink 
##      <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisManager::CreateDeviationCheckingObject  NXOpen::GeometricAnalysis::AnalysisManager::CreateDeviationCheckingObject @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class DeviationChecking(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.GeometricAnalysis.DeviationChecking</ja_class>
    """


    ##  the deviation type to be shown 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NoDeviations</term><description> 
    ##  show no
    ##            deviations </description> </item><item><term> 
    ## AllDeviations</term><description> 
    ##  show all
    ##            deviations </description> </item><item><term> 
    ## MaximumDistance</term><description> 
    ##  show
    ##            maximum distance deviation </description> </item><item><term> 
    ## MinimumDistance</term><description> 
    ##  show
    ##            minimum distance deviation </description> </item><item><term> 
    ## MaximumAngle</term><description> 
    ##  show maximum
    ##            angle deviation </description> </item><item><term> 
    ## MinimumAngle</term><description> 
    ##  show minimum
    ##            angle deviation </description> </item></list>
    class DeviationOptions(Enum):
        """
        Members Include: <NoDeviations> <AllDeviations> <MaximumDistance> <MinimumDistance> <MaximumAngle> <MinimumAngle>
        """
        NoDeviations: int
        AllDeviations: int
        MaximumDistance: int
        MinimumDistance: int
        MaximumAngle: int
        MinimumAngle: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DeviationChecking.DeviationOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the type of deviation checking to be performed 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## CurveToCurve</term><description> 
    ##  check 
    ##             curve/edge to curve/edge deviation </description> </item><item><term> 
    ## CurveToFace</term><description> 
    ##  check curve/edge
    ##             to face deviation </description> </item><item><term> 
    ## EdgeToFace</term><description> 
    ##  check edge to face
    ##             deviation </description> </item><item><term> 
    ## FaceToFace</term><description> 
    ##  check face to face
    ##             deviation </description> </item><item><term> 
    ## EdgeToEdge</term><description> 
    ##  check edge to edge
    ##             deviation </description> </item></list>
    class Types(Enum):
        """
        Members Include: <CurveToCurve> <CurveToFace> <EdgeToFace> <FaceToFace> <EdgeToEdge>
        """
        CurveToCurve: int
        CurveToFace: int
        EdgeToFace: int
        FaceToFace: int
        EdgeToEdge: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DeviationChecking.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) AngleTolerance
    ##  Returns the angle tolerance to be used for the deviation checking   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return float
    @property
    def AngleTolerance(self) -> float:
        """
        Getter for property: (float) AngleTolerance
         Returns the angle tolerance to be used for the deviation checking   
            
         
        """
        pass
    
    ## Setter for property: (float) AngleTolerance

    ##  Returns the angle tolerance to be used for the deviation checking   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @AngleTolerance.setter
    def AngleTolerance(self, angleTolerance: float):
        """
        Setter for property: (float) AngleTolerance
         Returns the angle tolerance to be used for the deviation checking   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectIBaseCurve NXOpen.SelectIBaseCurve@endlink) Curve
    ##  Returns the curve  - required for the deviation checking when
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToFace NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToFace@endlink .  
    ##    
    ##             
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SelectIBaseCurve
    @property
    def Curve(self) -> NXOpen.SelectIBaseCurve:
        """
        Getter for property: (@link NXOpen.SelectIBaseCurve NXOpen.SelectIBaseCurve@endlink) Curve
         Returns the curve  - required for the deviation checking when
                  @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
                  @link NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToFace NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToFace@endlink .  
           
                    
         
        """
        pass
    
    ## Getter for property: (@link DeviationChecking.DeviationOptions NXOpen.GeometricAnalysis.DeviationChecking.DeviationOptions@endlink) DeviationOption
    ##  Returns the number or type of deviations to be shown for the deviation checking   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return DeviationChecking.DeviationOptions
    @property
    def DeviationOption(self) -> DeviationChecking.DeviationOptions:
        """
        Getter for property: (@link DeviationChecking.DeviationOptions NXOpen.GeometricAnalysis.DeviationChecking.DeviationOptions@endlink) DeviationOption
         Returns the number or type of deviations to be shown for the deviation checking   
            
         
        """
        pass
    
    ## Setter for property: (@link DeviationChecking.DeviationOptions NXOpen.GeometricAnalysis.DeviationChecking.DeviationOptions@endlink) DeviationOption

    ##  Returns the number or type of deviations to be shown for the deviation checking   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @DeviationOption.setter
    def DeviationOption(self, deviationOption: DeviationChecking.DeviationOptions):
        """
        Setter for property: (@link DeviationChecking.DeviationOptions NXOpen.GeometricAnalysis.DeviationChecking.DeviationOptions@endlink) DeviationOption
         Returns the number or type of deviations to be shown for the deviation checking   
            
         
        """
        pass
    
    ## Getter for property: (float) DistanceTolerance
    ##  Returns the distance tolerance to be used for the deviation checking   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return float
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance to be used for the deviation checking   
            
         
        """
        pass
    
    ## Setter for property: (float) DistanceTolerance

    ##  Returns the distance tolerance to be used for the deviation checking   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance to be used for the deviation checking   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectIParameterizedSurface NXOpen.SelectIParameterizedSurface@endlink) FaceOfFirstEdge
    ##  Returns the face associated with the first edge or edge  - required for the deviation checking when
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToEdge NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToEdge@endlink 
    ##           or
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToFace NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToFace@endlink .  
    ##    
    ##             
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SelectIParameterizedSurface
    @property
    def FaceOfFirstEdge(self) -> NXOpen.SelectIParameterizedSurface:
        """
        Getter for property: (@link NXOpen.SelectIParameterizedSurface NXOpen.SelectIParameterizedSurface@endlink) FaceOfFirstEdge
         Returns the face associated with the first edge or edge  - required for the deviation checking when
                  @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
                  @link NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToEdge NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToEdge@endlink 
                  or
                  @link NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToFace NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToFace@endlink .  
           
                    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectIParameterizedSurface NXOpen.SelectIParameterizedSurface@endlink) FaceOfSecondEdge
    ##  Returns the face associated with the second edge  - required for the deviation checking when
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToEdge NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToEdge@endlink .  
    ##   
    ##             
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SelectIParameterizedSurface
    @property
    def FaceOfSecondEdge(self) -> NXOpen.SelectIParameterizedSurface:
        """
        Getter for property: (@link NXOpen.SelectIParameterizedSurface NXOpen.SelectIParameterizedSurface@endlink) FaceOfSecondEdge
         Returns the face associated with the second edge  - required for the deviation checking when
                  @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
                  @link NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToEdge NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToEdge@endlink .  
          
                    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectIBaseCurve NXOpen.SelectIBaseCurve@endlink) FirstCurve
    ##  Returns the first curve or edge - required for the deviation checking when
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToCurve NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToCurve@endlink .  
    ##    
    ##             
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SelectIBaseCurve
    @property
    def FirstCurve(self) -> NXOpen.SelectIBaseCurve:
        """
        Getter for property: (@link NXOpen.SelectIBaseCurve NXOpen.SelectIBaseCurve@endlink) FirstCurve
         Returns the first curve or edge - required for the deviation checking when
                  @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
                  @link NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToCurve NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToCurve@endlink .  
           
                    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectIBaseCurve NXOpen.SelectIBaseCurve@endlink) FirstEdge
    ##  Returns the first edge or edge  - required for the deviation checking when
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToEdge NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToEdge@endlink 
    ##           or
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToFace NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToFace@endlink .  
    ##    
    ##             
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SelectIBaseCurve
    @property
    def FirstEdge(self) -> NXOpen.SelectIBaseCurve:
        """
        Getter for property: (@link NXOpen.SelectIBaseCurve NXOpen.SelectIBaseCurve@endlink) FirstEdge
         Returns the first edge or edge  - required for the deviation checking when
                  @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
                  @link NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToEdge NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToEdge@endlink 
                  or
                  @link NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToFace NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToFace@endlink .  
           
                    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectIParameterizedSurface NXOpen.SelectIParameterizedSurface@endlink) FirstFace
    ##  Returns the first face - required for the deviation checking when
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::TypesFaceToFace NXOpen::GeometricAnalysis::DeviationChecking::TypesFaceToFace@endlink .  
    ##    
    ##             
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SelectIParameterizedSurface
    @property
    def FirstFace(self) -> NXOpen.SelectIParameterizedSurface:
        """
        Getter for property: (@link NXOpen.SelectIParameterizedSurface NXOpen.SelectIParameterizedSurface@endlink) FirstFace
         Returns the first face - required for the deviation checking when
                  @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
                  @link NXOpen::GeometricAnalysis::DeviationChecking::TypesFaceToFace NXOpen::GeometricAnalysis::DeviationChecking::TypesFaceToFace@endlink .  
           
                    
         
        """
        pass
    
    ## Getter for property: (int) NumberCheckPoints
    ##  Returns the number of check points to be shown for the deviation checking  -
    ##           required when @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToCurve NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToCurve@endlink 
    ##           or
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToFace NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToFace@endlink 
    ##           or
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToFace NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToFace@endlink 
    ##           or
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToEdge NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToEdge@endlink .  
    ##   
    ##             
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return int
    @property
    def NumberCheckPoints(self) -> int:
        """
        Getter for property: (int) NumberCheckPoints
         Returns the number of check points to be shown for the deviation checking  -
                  required when @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
                  @link NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToCurve NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToCurve@endlink 
                  or
                  @link NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToFace NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToFace@endlink 
                  or
                  @link NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToFace NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToFace@endlink 
                  or
                  @link NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToEdge NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToEdge@endlink .  
          
                    
         
        """
        pass
    
    ## Setter for property: (int) NumberCheckPoints

    ##  Returns the number of check points to be shown for the deviation checking  -
    ##           required when @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToCurve NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToCurve@endlink 
    ##           or
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToFace NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToFace@endlink 
    ##           or
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToFace NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToFace@endlink 
    ##           or
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToEdge NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToEdge@endlink .  
    ##   
    ##             
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @NumberCheckPoints.setter
    def NumberCheckPoints(self, numberCheckPoints: int):
        """
        Setter for property: (int) NumberCheckPoints
         Returns the number of check points to be shown for the deviation checking  -
                  required when @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
                  @link NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToCurve NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToCurve@endlink 
                  or
                  @link NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToFace NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToFace@endlink 
                  or
                  @link NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToFace NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToFace@endlink 
                  or
                  @link NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToEdge NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToEdge@endlink .  
          
                    
         
        """
        pass
    
    ## Getter for property: (int) NumberUcheckPoints
    ##  Returns the number of u check points to be shown for the deviation checking
    ##           - required when @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::TypesFaceToFace NXOpen::GeometricAnalysis::DeviationChecking::TypesFaceToFace@endlink 
    ##             
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return int
    @property
    def NumberUcheckPoints(self) -> int:
        """
        Getter for property: (int) NumberUcheckPoints
         Returns the number of u check points to be shown for the deviation checking
                  - required when @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
                  @link NXOpen::GeometricAnalysis::DeviationChecking::TypesFaceToFace NXOpen::GeometricAnalysis::DeviationChecking::TypesFaceToFace@endlink 
                    
            
         
        """
        pass
    
    ## Setter for property: (int) NumberUcheckPoints

    ##  Returns the number of u check points to be shown for the deviation checking
    ##           - required when @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::TypesFaceToFace NXOpen::GeometricAnalysis::DeviationChecking::TypesFaceToFace@endlink 
    ##             
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @NumberUcheckPoints.setter
    def NumberUcheckPoints(self, numberUCheckPoints: int):
        """
        Setter for property: (int) NumberUcheckPoints
         Returns the number of u check points to be shown for the deviation checking
                  - required when @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
                  @link NXOpen::GeometricAnalysis::DeviationChecking::TypesFaceToFace NXOpen::GeometricAnalysis::DeviationChecking::TypesFaceToFace@endlink 
                    
            
         
        """
        pass
    
    ## Getter for property: (int) NumberVcheckPoints
    ##  Returns the number of v check points to be shown for the deviation checking
    ##           - required when @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::TypesFaceToFace NXOpen::GeometricAnalysis::DeviationChecking::TypesFaceToFace@endlink 
    ##             
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return int
    @property
    def NumberVcheckPoints(self) -> int:
        """
        Getter for property: (int) NumberVcheckPoints
         Returns the number of v check points to be shown for the deviation checking
                  - required when @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
                  @link NXOpen::GeometricAnalysis::DeviationChecking::TypesFaceToFace NXOpen::GeometricAnalysis::DeviationChecking::TypesFaceToFace@endlink 
                    
            
         
        """
        pass
    
    ## Setter for property: (int) NumberVcheckPoints

    ##  Returns the number of v check points to be shown for the deviation checking
    ##           - required when @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::TypesFaceToFace NXOpen::GeometricAnalysis::DeviationChecking::TypesFaceToFace@endlink 
    ##             
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @NumberVcheckPoints.setter
    def NumberVcheckPoints(self, numberVCheckPoints: int):
        """
        Setter for property: (int) NumberVcheckPoints
         Returns the number of v check points to be shown for the deviation checking
                  - required when @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
                  @link NXOpen::GeometricAnalysis::DeviationChecking::TypesFaceToFace NXOpen::GeometricAnalysis::DeviationChecking::TypesFaceToFace@endlink 
                    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectIBaseCurve NXOpen.SelectIBaseCurve@endlink) SecondCurve
    ##  Returns the second curve or edge - required for the deviation checking when
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToCurve NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToCurve@endlink .  
    ##    
    ##             
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SelectIBaseCurve
    @property
    def SecondCurve(self) -> NXOpen.SelectIBaseCurve:
        """
        Getter for property: (@link NXOpen.SelectIBaseCurve NXOpen.SelectIBaseCurve@endlink) SecondCurve
         Returns the second curve or edge - required for the deviation checking when
                  @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
                  @link NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToCurve NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToCurve@endlink .  
           
                    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectIBaseCurve NXOpen.SelectIBaseCurve@endlink) SecondEdge
    ##  Returns the second edge - required for the deviation checking when
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToEdge NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToEdge@endlink .  
    ##   
    ##             
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SelectIBaseCurve
    @property
    def SecondEdge(self) -> NXOpen.SelectIBaseCurve:
        """
        Getter for property: (@link NXOpen.SelectIBaseCurve NXOpen.SelectIBaseCurve@endlink) SecondEdge
         Returns the second edge - required for the deviation checking when
                  @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
                  @link NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToEdge NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToEdge@endlink .  
          
                    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectIParameterizedSurface NXOpen.SelectIParameterizedSurface@endlink) SecondFace
    ##  Returns the second face - required for the deviation checking when
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::TypesFaceToFace NXOpen::GeometricAnalysis::DeviationChecking::TypesFaceToFace@endlink 
    ##           or the face  - required for the deviation checking when @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToFace NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToFace@endlink 
    ##           or
    ##           @link NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToFace NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToFace@endlink .  
    ##    
    ##             
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SelectIParameterizedSurface
    @property
    def SecondFace(self) -> NXOpen.SelectIParameterizedSurface:
        """
        Getter for property: (@link NXOpen.SelectIParameterizedSurface NXOpen.SelectIParameterizedSurface@endlink) SecondFace
         Returns the second face - required for the deviation checking when
                  @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
                  @link NXOpen::GeometricAnalysis::DeviationChecking::TypesFaceToFace NXOpen::GeometricAnalysis::DeviationChecking::TypesFaceToFace@endlink 
                  or the face  - required for the deviation checking when @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  is set to
                  @link NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToFace NXOpen::GeometricAnalysis::DeviationChecking::TypesCurveToFace@endlink 
                  or
                  @link NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToFace NXOpen::GeometricAnalysis::DeviationChecking::TypesEdgeToFace@endlink .  
           
                    
         
        """
        pass
    
    ## Getter for property: (@link DeviationChecking.Types NXOpen.GeometricAnalysis.DeviationChecking.Types@endlink) Type
    ##  Returns the deviation checking type.  
    ##    Depending on the value of the deviation
    ##           checking type, different inputs are required. See the
    ##           documentation for each of the inputs.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return DeviationChecking.Types
    @property
    def Type(self) -> DeviationChecking.Types:
        """
        Getter for property: (@link DeviationChecking.Types NXOpen.GeometricAnalysis.DeviationChecking.Types@endlink) Type
         Returns the deviation checking type.  
           Depending on the value of the deviation
                  checking type, different inputs are required. See the
                  documentation for each of the inputs.   
         
        """
        pass
    
    ## Setter for property: (@link DeviationChecking.Types NXOpen.GeometricAnalysis.DeviationChecking.Types@endlink) Type

    ##  Returns the deviation checking type.  
    ##    Depending on the value of the deviation
    ##           checking type, different inputs are required. See the
    ##           documentation for each of the inputs.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @Type.setter
    def Type(self, type: DeviationChecking.Types):
        """
        Setter for property: (@link DeviationChecking.Types NXOpen.GeometricAnalysis.DeviationChecking.Types@endlink) Type
         Returns the deviation checking type.  
           Depending on the value of the deviation
                  checking type, different inputs are required. See the
                  documentation for each of the inputs.   
         
        """
        pass
    
    ##  Performs deviation checking.  Before calling this method, set
    ##             property @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  to specify the type of 
    ##             deviation checking, and the two objects (curve/face/edge) to be used the deviation
    ##             checking. The type of the objects required
    ##             depends on @link NXOpen::GeometricAnalysis::DeviationChecking::Type NXOpen::GeometricAnalysis::DeviationChecking::Type@endlink  set above. Also set the
    ##             number check points to be displayed or u and v check points, the
    ##             distance tolerance, and the angle tolerance before calling the
    ##             method @link NXOpen::GeometricAnalysis::DeviationChecking::Check NXOpen::GeometricAnalysis::DeviationChecking::Check@endlink . 
    ##             @link NXOpen::GeometricAnalysis::DeviationChecking::Check NXOpen::GeometricAnalysis::DeviationChecking::Check@endlink  displays the
    ##             deviation as per the specification above in the graphics and lists
    ##             in the information window of NX.
    ##             
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def Check(self) -> None:
        """
         Performs deviation checking.  Before calling this method, set
                    property @link NXOpen::GeometricAnalysis::DeviationChecking::SetType NXOpen::GeometricAnalysis::DeviationChecking::SetType@endlink  to specify the type of 
                    deviation checking, and the two objects (curve/face/edge) to be used the deviation
                    checking. The type of the objects required
                    depends on @link NXOpen::GeometricAnalysis::DeviationChecking::Type NXOpen::GeometricAnalysis::DeviationChecking::Type@endlink  set above. Also set the
                    number check points to be displayed or u and v check points, the
                    distance tolerance, and the angle tolerance before calling the
                    method @link NXOpen::GeometricAnalysis::DeviationChecking::Check NXOpen::GeometricAnalysis::DeviationChecking::Check@endlink . 
                    @link NXOpen::GeometricAnalysis::DeviationChecking::Check NXOpen::GeometricAnalysis::DeviationChecking::Check@endlink  displays the
                    deviation as per the specification above in the graphics and lists
                    in the information window of NX.
                    
        """
        pass
    
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
##  DeviationGaugeBuilder class   <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisObjectCollection::CreateDeviationGaugeBuilder  NXOpen::GeometricAnalysis::AnalysisObjectCollection::CreateDeviationGaugeBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ColorPlotType </term> <description> 
##  
## Blend </description> </item> 
## 
## <item><term> 
##  
## CurveRangeControl.AnchorPosition </term> <description> 
##  
## Start </description> </item> 
## 
## <item><term> 
##  
## DeviationIntervals </term> <description> 
##  
## 5 </description> </item> 
## 
## <item><term> 
##  
## HasAbsoluteColorPlot </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## HasAdditionalValuesLabel </term> <description> 
##  
## None </description> </item> 
## 
## <item><term> 
##  
## HasMaximumValueLabel </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## HasMinimumValueLabel </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## InnerTolerance </term> <description> 
##  
## 0.1 </description> </item> 
## 
## <item><term> 
##  
## IsLabelDisplayed </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## IsMarkerDisplayed </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## IsNeedlePlotDisplayed </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## MaxCheckingAngle </term> <description> 
##  
## 5 </description> </item> 
## 
## <item><term> 
##  
## MaxCheckingDistance </term> <description> 
##  
## 1 (millimeters part), 0.5 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MeasurementMethod </term> <description> 
##  
## ThreeDim </description> </item> 
## 
## <item><term> 
##  
## MeasurementSamples </term> <description> 
##  
## 20 </description> </item> 
## 
## <item><term> 
##  
## MinMaxOption </term> <description> 
##  
## Minmax </description> </item> 
## 
## <item><term> 
##  
## NeedleScale </term> <description> 
##  
## 1.0 </description> </item> 
## 
## <item><term> 
##  
## NegativeInnerTolerance </term> <description> 
##  
## -0.001 </description> </item> 
## 
## <item><term> 
##  
## NegativeOuterTolerance </term> <description> 
##  
## -0.001 </description> </item> 
## 
## <item><term> 
##  
## OuterTolerance </term> <description> 
##  
## 0.1 </description> </item> 
## 
## <item><term> 
##  
## PositiveInnerTolerance </term> <description> 
##  
## 0.001 </description> </item> 
## 
## <item><term> 
##  
## PositiveOuterTolerance </term> <description> 
##  
## 0.001 </description> </item> 
## 
## <item><term> 
##  
## ReportingPerType </term> <description> 
##  
## AnalysisObject </description> </item> 
## 
## <item><term> 
##  
## SpatialResolution </term> <description> 
##  
## 0.1 </description> </item> 
## 
## <item><term> 
##  
## SurfaceRangeControl.AnchorPosition </term> <description> 
##  
## Vertex1 </description> </item> 
## 
## <item><term> 
##  
## XyzDirection </term> <description> 
##  
## X </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX6.0.0  <br> 

class DeviationGaugeBuilder(NXOpen.Builder): 
    """ DeviationGaugeBuilder class  """


    ##  This enum represents the Deviation Gauge  Analysis Object additional values label type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## UserDefined</term><description> 
    ##   User Defined  </description> </item><item><term> 
    ## Intermediate</term><description> 
    ##  Intermediate  </description> </item><item><term> 
    ## All</term><description> 
    ##  All  </description> </item><item><term> 
    ## NotSet</term><description> 
    ##  None  </description> </item></list>
    class AdditionalValuesLabelType(Enum):
        """
        Members Include: <UserDefined> <Intermediate> <All> <NotSet>
        """
        UserDefined: int
        Intermediate: int
        All: int
        NotSet: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DeviationGaugeBuilder.AdditionalValuesLabelType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum represents the Deviation Gauge  Analysis Object color plot types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Blend</term><description> 
    ##   Blend </description> </item><item><term> 
    ## Stepped</term><description> 
    ##   Stepped </description> </item><item><term> 
    ## NotSet</term><description> 
    ##   None  </description> </item></list>
    class ColorPlotTypes(Enum):
        """
        Members Include: <Blend> <Stepped> <NotSet>
        """
        Blend: int
        Stepped: int
        NotSet: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DeviationGaugeBuilder.ColorPlotTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum represents the Deviation Gauge  Analysis Object evaluation types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ThreeDim</term><description> 
    ##  3D  </description> </item><item><term> 
    ## XyzDirection</term><description> 
    ##  XYZ direction  </description> </item><item><term> 
    ## WorkView</term><description> 
    ##  Work view     </description> </item><item><term> 
    ## VectorComponent</term><description> 
    ##  Vector component    </description> </item><item><term> 
    ## Plane</term><description> 
    ##  Plane   </description> </item><item><term> 
    ## AlongVector</term><description> 
    ##  Along vector   </description> </item></list>
    class MeasurementMethodType(Enum):
        """
        Members Include: <ThreeDim> <XyzDirection> <WorkView> <VectorComponent> <Plane> <AlongVector>
        """
        ThreeDim: int
        XyzDirection: int
        WorkView: int
        VectorComponent: int
        Plane: int
        AlongVector: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DeviationGaugeBuilder.MeasurementMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum represents the Deviation Gauge  Analysis Object min max type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Minmax</term><description> 
    ##  Minimum/Maximum      </description> </item><item><term> 
    ## Minimum</term><description> 
    ##  Minimum  </description> </item><item><term> 
    ## Maximum</term><description> 
    ##  Maximum  </description> </item><item><term> 
    ## NotSet</term><description> 
    ##  None  </description> </item></list>
    class MinMaxType(Enum):
        """
        Members Include: <Minmax> <Minimum> <Maximum> <NotSet>
        """
        Minmax: int
        Minimum: int
        Maximum: int
        NotSet: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DeviationGaugeBuilder.MinMaxType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum represents the Deviation Gauge  Analysis Object reporting per setting 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## AnalysisObject</term><description> 
    ##   Per Analysis Object </description> </item><item><term> 
    ## Target</term><description> 
    ##   Per Target Object  </description> </item><item><term> 
    ## Reference</term><description> 
    ##   Per Reference Object </description> </item></list>
    class ReportingPerTypes(Enum):
        """
        Members Include: <AnalysisObject> <Target> <Reference>
        """
        AnalysisObject: int
        Target: int
        Reference: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DeviationGaugeBuilder.ReportingPerTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum represents the Deviation Gauge Analysis Object X, Y, Z direction options 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## X</term><description> 
    ##  X direction </description> </item><item><term> 
    ## Y</term><description> 
    ##  Y direction </description> </item><item><term> 
    ## Z</term><description> 
    ##  Z direction </description> </item></list>
    class XyzDirectionType(Enum):
        """
        Members Include: <X> <Y> <Z>
        """
        X: int
        Y: int
        Z: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DeviationGaugeBuilder.XyzDirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link DeviationGaugeBuilder.ColorPlotTypes NXOpen.GeometricAnalysis.DeviationGaugeBuilder.ColorPlotTypes@endlink) ColorPlotType
    ##  Returns the color plot type   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return DeviationGaugeBuilder.ColorPlotTypes
    @property
    def ColorPlotType(self) -> DeviationGaugeBuilder.ColorPlotTypes:
        """
        Getter for property: (@link DeviationGaugeBuilder.ColorPlotTypes NXOpen.GeometricAnalysis.DeviationGaugeBuilder.ColorPlotTypes@endlink) ColorPlotType
         Returns the color plot type   
            
         
        """
        pass
    
    ## Setter for property: (@link DeviationGaugeBuilder.ColorPlotTypes NXOpen.GeometricAnalysis.DeviationGaugeBuilder.ColorPlotTypes@endlink) ColorPlotType

    ##  Returns the color plot type   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ColorPlotType.setter
    def ColorPlotType(self, colorPlotType: DeviationGaugeBuilder.ColorPlotTypes):
        """
        Setter for property: (@link DeviationGaugeBuilder.ColorPlotTypes NXOpen.GeometricAnalysis.DeviationGaugeBuilder.ColorPlotTypes@endlink) ColorPlotType
         Returns the color plot type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Features.GeometricConstraintDataManager NXOpen.Features.GeometricConstraintDataManager@endlink) ConstraintManager
    ##  Returns the constraint manager   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return NXOpen.Features.GeometricConstraintDataManager
    @property
    def ConstraintManager(self) -> NXOpen.Features.GeometricConstraintDataManager:
        """
        Getter for property: (@link NXOpen.Features.GeometricConstraintDataManager NXOpen.Features.GeometricConstraintDataManager@endlink) ConstraintManager
         Returns the constraint manager   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.CurveRangeBuilder NXOpen.GeometricUtilities.CurveRangeBuilder@endlink) CurveRangeControl
    ##  Returns the curve range     
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.CurveRangeBuilder
    @property
    def CurveRangeControl(self) -> NXOpen.GeometricUtilities.CurveRangeBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.CurveRangeBuilder NXOpen.GeometricUtilities.CurveRangeBuilder@endlink) CurveRangeControl
         Returns the curve range     
            
         
        """
        pass
    
    ## Getter for property: (int) DeviationIntervals
    ##  Returns the number of deviation intervals   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return int
    @property
    def DeviationIntervals(self) -> int:
        """
        Getter for property: (int) DeviationIntervals
         Returns the number of deviation intervals   
            
         
        """
        pass
    
    ## Setter for property: (int) DeviationIntervals

    ##  Returns the number of deviation intervals   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @DeviationIntervals.setter
    def DeviationIntervals(self, deviationIntervals: int):
        """
        Setter for property: (int) DeviationIntervals
         Returns the number of deviation intervals   
            
         
        """
        pass
    
    ## Getter for property: (bool) HasAbsoluteColorPlot
    ##  Returns a value indicating whether to plot using absolute value     
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def HasAbsoluteColorPlot(self) -> bool:
        """
        Getter for property: (bool) HasAbsoluteColorPlot
         Returns a value indicating whether to plot using absolute value     
            
         
        """
        pass
    
    ## Setter for property: (bool) HasAbsoluteColorPlot

    ##  Returns a value indicating whether to plot using absolute value     
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @HasAbsoluteColorPlot.setter
    def HasAbsoluteColorPlot(self, absoluteColorPlot: bool):
        """
        Setter for property: (bool) HasAbsoluteColorPlot
         Returns a value indicating whether to plot using absolute value     
            
         
        """
        pass
    
    ## Getter for property: (@link DeviationGaugeBuilder.AdditionalValuesLabelType NXOpen.GeometricAnalysis.DeviationGaugeBuilder.AdditionalValuesLabelType@endlink) HasAdditionalValuesLabel
    ##  Returns a value indicating whether to add additional values label   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return DeviationGaugeBuilder.AdditionalValuesLabelType
    @property
    def HasAdditionalValuesLabel(self) -> DeviationGaugeBuilder.AdditionalValuesLabelType:
        """
        Getter for property: (@link DeviationGaugeBuilder.AdditionalValuesLabelType NXOpen.GeometricAnalysis.DeviationGaugeBuilder.AdditionalValuesLabelType@endlink) HasAdditionalValuesLabel
         Returns a value indicating whether to add additional values label   
            
         
        """
        pass
    
    ## Setter for property: (@link DeviationGaugeBuilder.AdditionalValuesLabelType NXOpen.GeometricAnalysis.DeviationGaugeBuilder.AdditionalValuesLabelType@endlink) HasAdditionalValuesLabel

    ##  Returns a value indicating whether to add additional values label   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @HasAdditionalValuesLabel.setter
    def HasAdditionalValuesLabel(self, additionalValuesLabel: DeviationGaugeBuilder.AdditionalValuesLabelType):
        """
        Setter for property: (@link DeviationGaugeBuilder.AdditionalValuesLabelType NXOpen.GeometricAnalysis.DeviationGaugeBuilder.AdditionalValuesLabelType@endlink) HasAdditionalValuesLabel
         Returns a value indicating whether to add additional values label   
            
         
        """
        pass
    
    ## Getter for property: (bool) HasCrossCurveDeviationLabel
    ##  Returns a value indicating whether to display cross_curve deviation label   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def HasCrossCurveDeviationLabel(self) -> bool:
        """
        Getter for property: (bool) HasCrossCurveDeviationLabel
         Returns a value indicating whether to display cross_curve deviation label   
            
         
        """
        pass
    
    ## Setter for property: (bool) HasCrossCurveDeviationLabel

    ##  Returns a value indicating whether to display cross_curve deviation label   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @HasCrossCurveDeviationLabel.setter
    def HasCrossCurveDeviationLabel(self, crossCurveDeviationLabel: bool):
        """
        Setter for property: (bool) HasCrossCurveDeviationLabel
         Returns a value indicating whether to display cross_curve deviation label   
            
         
        """
        pass
    
    ## Getter for property: (bool) HasInfoLabel
    ##  Returns a value indicating whether to enable floating info label   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def HasInfoLabel(self) -> bool:
        """
        Getter for property: (bool) HasInfoLabel
         Returns a value indicating whether to enable floating info label   
            
         
        """
        pass
    
    ## Setter for property: (bool) HasInfoLabel

    ##  Returns a value indicating whether to enable floating info label   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @HasInfoLabel.setter
    def HasInfoLabel(self, infoLabel: bool):
        """
        Setter for property: (bool) HasInfoLabel
         Returns a value indicating whether to enable floating info label   
            
         
        """
        pass
    
    ## Getter for property: (bool) HasInnerToleranceLabel
    ##  Returns a value indicating whether to display inner tolerance label   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def HasInnerToleranceLabel(self) -> bool:
        """
        Getter for property: (bool) HasInnerToleranceLabel
         Returns a value indicating whether to display inner tolerance label   
            
         
        """
        pass
    
    ## Setter for property: (bool) HasInnerToleranceLabel

    ##  Returns a value indicating whether to display inner tolerance label   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @HasInnerToleranceLabel.setter
    def HasInnerToleranceLabel(self, innerToleranceLabel: bool):
        """
        Setter for property: (bool) HasInnerToleranceLabel
         Returns a value indicating whether to display inner tolerance label   
            
         
        """
        pass
    
    ## Getter for property: (bool) HasMaximumValueLabel
    ##  Returns a value indicating whether to display maximum value label   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def HasMaximumValueLabel(self) -> bool:
        """
        Getter for property: (bool) HasMaximumValueLabel
         Returns a value indicating whether to display maximum value label   
            
         
        """
        pass
    
    ## Setter for property: (bool) HasMaximumValueLabel

    ##  Returns a value indicating whether to display maximum value label   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @HasMaximumValueLabel.setter
    def HasMaximumValueLabel(self, maximumValueLabel: bool):
        """
        Setter for property: (bool) HasMaximumValueLabel
         Returns a value indicating whether to display maximum value label   
            
         
        """
        pass
    
    ## Getter for property: (bool) HasMinimumValueLabel
    ##  Returns a value indicating whether to display minimum value label   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def HasMinimumValueLabel(self) -> bool:
        """
        Getter for property: (bool) HasMinimumValueLabel
         Returns a value indicating whether to display minimum value label   
            
         
        """
        pass
    
    ## Setter for property: (bool) HasMinimumValueLabel

    ##  Returns a value indicating whether to display minimum value label   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @HasMinimumValueLabel.setter
    def HasMinimumValueLabel(self, minimumValueLabel: bool):
        """
        Setter for property: (bool) HasMinimumValueLabel
         Returns a value indicating whether to display minimum value label   
            
         
        """
        pass
    
    ## Getter for property: (float) InnerTolerance
    ##  Returns the inner tolerance   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return float
    @property
    def InnerTolerance(self) -> float:
        """
        Getter for property: (float) InnerTolerance
         Returns the inner tolerance   
            
         
        """
        pass
    
    ## Setter for property: (float) InnerTolerance

    ##  Returns the inner tolerance   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @InnerTolerance.setter
    def InnerTolerance(self, innerTolerance: float):
        """
        Setter for property: (float) InnerTolerance
         Returns the inner tolerance   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsColorMapDisplayed
    ##  Returns a value indicating whether to display color map    
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def IsColorMapDisplayed(self) -> bool:
        """
        Getter for property: (bool) IsColorMapDisplayed
         Returns a value indicating whether to display color map    
            
         
        """
        pass
    
    ## Setter for property: (bool) IsColorMapDisplayed

    ##  Returns a value indicating whether to display color map    
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @IsColorMapDisplayed.setter
    def IsColorMapDisplayed(self, isColorMapDisplayed: bool):
        """
        Setter for property: (bool) IsColorMapDisplayed
         Returns a value indicating whether to display color map    
            
         
        """
        pass
    
    ## Getter for property: (bool) IsDirectionReversed
    ##  Returns a value indicating whether to reverse the direction   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def IsDirectionReversed(self) -> bool:
        """
        Getter for property: (bool) IsDirectionReversed
         Returns a value indicating whether to reverse the direction   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsDirectionReversed

    ##  Returns a value indicating whether to reverse the direction   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @IsDirectionReversed.setter
    def IsDirectionReversed(self, reverseDirection: bool):
        """
        Setter for property: (bool) IsDirectionReversed
         Returns a value indicating whether to reverse the direction   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsLabelDisplayed
    ##  Returns  a value indicating whether to display label     
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def IsLabelDisplayed(self) -> bool:
        """
        Getter for property: (bool) IsLabelDisplayed
         Returns  a value indicating whether to display label     
            
         
        """
        pass
    
    ## Setter for property: (bool) IsLabelDisplayed

    ##  Returns  a value indicating whether to display label     
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @IsLabelDisplayed.setter
    def IsLabelDisplayed(self, labelDisplayed: bool):
        """
        Setter for property: (bool) IsLabelDisplayed
         Returns  a value indicating whether to display label     
            
         
        """
        pass
    
    ## Getter for property: (bool) IsMarkerDisplayed
    ##  Returns a value indicating whether to display marker    
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def IsMarkerDisplayed(self) -> bool:
        """
        Getter for property: (bool) IsMarkerDisplayed
         Returns a value indicating whether to display marker    
            
         
        """
        pass
    
    ## Setter for property: (bool) IsMarkerDisplayed

    ##  Returns a value indicating whether to display marker    
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @IsMarkerDisplayed.setter
    def IsMarkerDisplayed(self, isMarkerDisplayed: bool):
        """
        Setter for property: (bool) IsMarkerDisplayed
         Returns a value indicating whether to display marker    
            
         
        """
        pass
    
    ## Getter for property: (bool) IsNeedlePlotDisplayed
    ##  Returns a value indicating whether to display needle plot    
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def IsNeedlePlotDisplayed(self) -> bool:
        """
        Getter for property: (bool) IsNeedlePlotDisplayed
         Returns a value indicating whether to display needle plot    
            
         
        """
        pass
    
    ## Setter for property: (bool) IsNeedlePlotDisplayed

    ##  Returns a value indicating whether to display needle plot    
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @IsNeedlePlotDisplayed.setter
    def IsNeedlePlotDisplayed(self, isNeedlePlotDisplayed: bool):
        """
        Setter for property: (bool) IsNeedlePlotDisplayed
         Returns a value indicating whether to display needle plot    
            
         
        """
        pass
    
    ## Getter for property: (float) MaxCheckingAngle
    ##  Returns the maximum checking angle   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return float
    @property
    def MaxCheckingAngle(self) -> float:
        """
        Getter for property: (float) MaxCheckingAngle
         Returns the maximum checking angle   
            
         
        """
        pass
    
    ## Setter for property: (float) MaxCheckingAngle

    ##  Returns the maximum checking angle   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @MaxCheckingAngle.setter
    def MaxCheckingAngle(self, maxCheckingAngle: float):
        """
        Setter for property: (float) MaxCheckingAngle
         Returns the maximum checking angle   
            
         
        """
        pass
    
    ## Getter for property: (float) MaxCheckingDistance
    ##  Returns the maximum checking distance   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return float
    @property
    def MaxCheckingDistance(self) -> float:
        """
        Getter for property: (float) MaxCheckingDistance
         Returns the maximum checking distance   
            
         
        """
        pass
    
    ## Setter for property: (float) MaxCheckingDistance

    ##  Returns the maximum checking distance   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @MaxCheckingDistance.setter
    def MaxCheckingDistance(self, maxCheckingDistance: float):
        """
        Setter for property: (float) MaxCheckingDistance
         Returns the maximum checking distance   
            
         
        """
        pass
    
    ## Getter for property: (@link DeviationGaugeBuilder.MeasurementMethodType NXOpen.GeometricAnalysis.DeviationGaugeBuilder.MeasurementMethodType@endlink) MeasurementMethod
    ##  Returns the measurement method   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return DeviationGaugeBuilder.MeasurementMethodType
    @property
    def MeasurementMethod(self) -> DeviationGaugeBuilder.MeasurementMethodType:
        """
        Getter for property: (@link DeviationGaugeBuilder.MeasurementMethodType NXOpen.GeometricAnalysis.DeviationGaugeBuilder.MeasurementMethodType@endlink) MeasurementMethod
         Returns the measurement method   
            
         
        """
        pass
    
    ## Setter for property: (@link DeviationGaugeBuilder.MeasurementMethodType NXOpen.GeometricAnalysis.DeviationGaugeBuilder.MeasurementMethodType@endlink) MeasurementMethod

    ##  Returns the measurement method   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @MeasurementMethod.setter
    def MeasurementMethod(self, measurementMethod: DeviationGaugeBuilder.MeasurementMethodType):
        """
        Setter for property: (@link DeviationGaugeBuilder.MeasurementMethodType NXOpen.GeometricAnalysis.DeviationGaugeBuilder.MeasurementMethodType@endlink) MeasurementMethod
         Returns the measurement method   
            
         
        """
        pass
    
    ## Getter for property: (int) MeasurementSamples
    ##  Returns the number of measurement samples   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return int
    @property
    def MeasurementSamples(self) -> int:
        """
        Getter for property: (int) MeasurementSamples
         Returns the number of measurement samples   
            
         
        """
        pass
    
    ## Setter for property: (int) MeasurementSamples

    ##  Returns the number of measurement samples   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @MeasurementSamples.setter
    def MeasurementSamples(self, measurementSamples: int):
        """
        Setter for property: (int) MeasurementSamples
         Returns the number of measurement samples   
            
         
        """
        pass
    
    ## Getter for property: (@link DeviationGaugeBuilder.MinMaxType NXOpen.GeometricAnalysis.DeviationGaugeBuilder.MinMaxType@endlink) MinMaxOption
    ##  Returns the min_max type   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return DeviationGaugeBuilder.MinMaxType
    @property
    def MinMaxOption(self) -> DeviationGaugeBuilder.MinMaxType:
        """
        Getter for property: (@link DeviationGaugeBuilder.MinMaxType NXOpen.GeometricAnalysis.DeviationGaugeBuilder.MinMaxType@endlink) MinMaxOption
         Returns the min_max type   
            
         
        """
        pass
    
    ## Setter for property: (@link DeviationGaugeBuilder.MinMaxType NXOpen.GeometricAnalysis.DeviationGaugeBuilder.MinMaxType@endlink) MinMaxOption

    ##  Returns the min_max type   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @MinMaxOption.setter
    def MinMaxOption(self, minMax: DeviationGaugeBuilder.MinMaxType):
        """
        Setter for property: (@link DeviationGaugeBuilder.MinMaxType NXOpen.GeometricAnalysis.DeviationGaugeBuilder.MinMaxType@endlink) MinMaxOption
         Returns the min_max type   
            
         
        """
        pass
    
    ## Getter for property: (float) NeedleScale
    ##  Returns the needle scale   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return float
    @property
    def NeedleScale(self) -> float:
        """
        Getter for property: (float) NeedleScale
         Returns the needle scale   
            
         
        """
        pass
    
    ## Setter for property: (float) NeedleScale

    ##  Returns the needle scale   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @NeedleScale.setter
    def NeedleScale(self, needleScale: float):
        """
        Setter for property: (float) NeedleScale
         Returns the needle scale   
            
         
        """
        pass
    
    ## Getter for property: (float) NegativeInnerTolerance
    ##  Returns the negative inner tolerance   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return float
    @property
    def NegativeInnerTolerance(self) -> float:
        """
        Getter for property: (float) NegativeInnerTolerance
         Returns the negative inner tolerance   
            
         
        """
        pass
    
    ## Setter for property: (float) NegativeInnerTolerance

    ##  Returns the negative inner tolerance   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @NegativeInnerTolerance.setter
    def NegativeInnerTolerance(self, negativennerTolerance: float):
        """
        Setter for property: (float) NegativeInnerTolerance
         Returns the negative inner tolerance   
            
         
        """
        pass
    
    ## Getter for property: (float) NegativeOuterTolerance
    ##  Returns the negative outer tolerance   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return float
    @property
    def NegativeOuterTolerance(self) -> float:
        """
        Getter for property: (float) NegativeOuterTolerance
         Returns the negative outer tolerance   
            
         
        """
        pass
    
    ## Setter for property: (float) NegativeOuterTolerance

    ##  Returns the negative outer tolerance   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @NegativeOuterTolerance.setter
    def NegativeOuterTolerance(self, negativeOuterTolerance: float):
        """
        Setter for property: (float) NegativeOuterTolerance
         Returns the negative outer tolerance   
            
         
        """
        pass
    
    ## Getter for property: (float) OuterTolerance
    ##  Returns the outer tolerance   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return float
    @property
    def OuterTolerance(self) -> float:
        """
        Getter for property: (float) OuterTolerance
         Returns the outer tolerance   
            
         
        """
        pass
    
    ## Setter for property: (float) OuterTolerance

    ##  Returns the outer tolerance   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @OuterTolerance.setter
    def OuterTolerance(self, outerTolerance: float):
        """
        Setter for property: (float) OuterTolerance
         Returns the outer tolerance   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane
    ##  Returns the plane for measurement direction   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.Plane
    @property
    def Plane(self) -> NXOpen.Plane:
        """
        Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane
         Returns the plane for measurement direction   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane

    ##  Returns the plane for measurement direction   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @Plane.setter
    def Plane(self, plane: NXOpen.Plane):
        """
        Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane
         Returns the plane for measurement direction   
            
         
        """
        pass
    
    ## Getter for property: (float) PositiveInnerTolerance
    ##  Returns the positive inner tolerance   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return float
    @property
    def PositiveInnerTolerance(self) -> float:
        """
        Getter for property: (float) PositiveInnerTolerance
         Returns the positive inner tolerance   
            
         
        """
        pass
    
    ## Setter for property: (float) PositiveInnerTolerance

    ##  Returns the positive inner tolerance   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @PositiveInnerTolerance.setter
    def PositiveInnerTolerance(self, positiveInnerTolerance: float):
        """
        Setter for property: (float) PositiveInnerTolerance
         Returns the positive inner tolerance   
            
         
        """
        pass
    
    ## Getter for property: (float) PositiveOuterTolerance
    ##  Returns the positive outer tolerance   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return float
    @property
    def PositiveOuterTolerance(self) -> float:
        """
        Getter for property: (float) PositiveOuterTolerance
         Returns the positive outer tolerance   
            
         
        """
        pass
    
    ## Setter for property: (float) PositiveOuterTolerance

    ##  Returns the positive outer tolerance   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @PositiveOuterTolerance.setter
    def PositiveOuterTolerance(self, positiveOuterTolerance: float):
        """
        Setter for property: (float) PositiveOuterTolerance
         Returns the positive outer tolerance   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) ReferenceObjects
    ##  Returns the reference object   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def ReferenceObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) ReferenceObjects
         Returns the reference object   
            
         
        """
        pass
    
    ## Getter for property: (@link DeviationGaugeBuilder.ReportingPerTypes NXOpen.GeometricAnalysis.DeviationGaugeBuilder.ReportingPerTypes@endlink) ReportingPerType
    ##  Returns the reporting per option   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return DeviationGaugeBuilder.ReportingPerTypes
    @property
    def ReportingPerType(self) -> DeviationGaugeBuilder.ReportingPerTypes:
        """
        Getter for property: (@link DeviationGaugeBuilder.ReportingPerTypes NXOpen.GeometricAnalysis.DeviationGaugeBuilder.ReportingPerTypes@endlink) ReportingPerType
         Returns the reporting per option   
            
         
        """
        pass
    
    ## Setter for property: (@link DeviationGaugeBuilder.ReportingPerTypes NXOpen.GeometricAnalysis.DeviationGaugeBuilder.ReportingPerTypes@endlink) ReportingPerType

    ##  Returns the reporting per option   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @ReportingPerType.setter
    def ReportingPerType(self, reportingPerType: DeviationGaugeBuilder.ReportingPerTypes):
        """
        Setter for property: (@link DeviationGaugeBuilder.ReportingPerTypes NXOpen.GeometricAnalysis.DeviationGaugeBuilder.ReportingPerTypes@endlink) ReportingPerType
         Returns the reporting per option   
            
         
        """
        pass
    
    ## Getter for property: (float) SpatialResolution
    ##  Returns the maximum checking angle   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return float
    @property
    def SpatialResolution(self) -> float:
        """
        Getter for property: (float) SpatialResolution
         Returns the maximum checking angle   
            
         
        """
        pass
    
    ## Setter for property: (float) SpatialResolution

    ##  Returns the maximum checking angle   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @SpatialResolution.setter
    def SpatialResolution(self, spatialResolution: float):
        """
        Setter for property: (float) SpatialResolution
         Returns the maximum checking angle   
            
         
        """
        pass
    
    ## Getter for property: (bool) SuggestScaleFactor
    ##  Returns a value indicating whether to use automatic scale factor   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def SuggestScaleFactor(self) -> bool:
        """
        Getter for property: (bool) SuggestScaleFactor
         Returns a value indicating whether to use automatic scale factor   
            
         
        """
        pass
    
    ## Setter for property: (bool) SuggestScaleFactor

    ##  Returns a value indicating whether to use automatic scale factor   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @SuggestScaleFactor.setter
    def SuggestScaleFactor(self, suggestScaleFactor: bool):
        """
        Setter for property: (bool) SuggestScaleFactor
         Returns a value indicating whether to use automatic scale factor   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.SurfaceRangeBuilder NXOpen.GeometricUtilities.SurfaceRangeBuilder@endlink) SurfaceRangeControl
    ##  Returns the surface range     
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.SurfaceRangeBuilder
    @property
    def SurfaceRangeControl(self) -> NXOpen.GeometricUtilities.SurfaceRangeBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.SurfaceRangeBuilder NXOpen.GeometricUtilities.SurfaceRangeBuilder@endlink) SurfaceRangeControl
         Returns the surface range     
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) TargetObjects
    ##  Returns the target object   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def TargetObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) TargetObjects
         Returns the target object   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseDefiningPoints
    ##  Returns  a value indicating whether to use defining points.  
    ##    Available only if target is curve with defining points     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def UseDefiningPoints(self) -> bool:
        """
        Getter for property: (bool) UseDefiningPoints
         Returns  a value indicating whether to use defining points.  
           Available only if target is curve with defining points     
         
        """
        pass
    
    ## Setter for property: (bool) UseDefiningPoints

    ##  Returns  a value indicating whether to use defining points.  
    ##    Available only if target is curve with defining points     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @UseDefiningPoints.setter
    def UseDefiningPoints(self, useDefiningPoints: bool):
        """
        Setter for property: (bool) UseDefiningPoints
         Returns  a value indicating whether to use defining points.  
           Available only if target is curve with defining points     
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) VectorComponentDirection
    ##  Returns the direction vector.  
    ##    Not used if the measurement method is ThreeDim or Plane   
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def VectorComponentDirection(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) VectorComponentDirection
         Returns the direction vector.  
           Not used if the measurement method is ThreeDim or Plane   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) VectorComponentDirection

    ##  Returns the direction vector.  
    ##    Not used if the measurement method is ThreeDim or Plane   
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @VectorComponentDirection.setter
    def VectorComponentDirection(self, vectorComponentDirection: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) VectorComponentDirection
         Returns the direction vector.  
           Not used if the measurement method is ThreeDim or Plane   
         
        """
        pass
    
    ## Getter for property: (@link DeviationGaugeBuilder.XyzDirectionType NXOpen.GeometricAnalysis.DeviationGaugeBuilder.XyzDirectionType@endlink) XyzDirection
    ##  Returns the xyz direction   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return DeviationGaugeBuilder.XyzDirectionType
    @property
    def XyzDirection(self) -> DeviationGaugeBuilder.XyzDirectionType:
        """
        Getter for property: (@link DeviationGaugeBuilder.XyzDirectionType NXOpen.GeometricAnalysis.DeviationGaugeBuilder.XyzDirectionType@endlink) XyzDirection
         Returns the xyz direction   
            
         
        """
        pass
    
    ## Setter for property: (@link DeviationGaugeBuilder.XyzDirectionType NXOpen.GeometricAnalysis.DeviationGaugeBuilder.XyzDirectionType@endlink) XyzDirection

    ##  Returns the xyz direction   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @XyzDirection.setter
    def XyzDirection(self, xyzDirection: DeviationGaugeBuilder.XyzDirectionType):
        """
        Setter for property: (@link DeviationGaugeBuilder.XyzDirectionType NXOpen.GeometricAnalysis.DeviationGaugeBuilder.XyzDirectionType@endlink) XyzDirection
         Returns the xyz direction   
            
         
        """
        pass
    
    ##  Adds dynamic points to the Deviation Gauge. 
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    def AddDynamicPoints(self) -> None:
        """
         Adds dynamic points to the Deviation Gauge. 
        """
        pass
    
    ##  Add a PMI label in specified position to represent the deviation value. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="snappedObject"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  The face or curve which the PMI label pointed to. </param>
    def AddPMILabel(self, snappedObject: NXOpen.NXObject) -> None:
        """
         Add a PMI label in specified position to represent the deviation value. 
        """
        pass
    
##  Deviation Gauge analysis object class  <br> To create or edit an instance of this class, use @link NXOpen::GeometricAnalysis::DeviationGaugeBuilder  NXOpen::GeometricAnalysis::DeviationGaugeBuilder @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class DeviationGauge(AnalysisObject): 
    """ Deviation Gauge analysis object class """
    pass


import NXOpen
import NXOpen.Features
##  Represents a Distance Analysis builder.  <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisObjectCollectionEx::CreateDistanceAnalysisBuilder1  NXOpen::GeometricAnalysis::AnalysisObjectCollectionEx::CreateDistanceAnalysisBuilder1 @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DataRange.IsFixed </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## DataRange.Max </term> <description> 
##  
## 0.010000 </description> </item> 
## 
## <item><term> 
##  
## DataRange.Middle </term> <description> 
##  
## 0.000000 </description> </item> 
## 
## <item><term> 
##  
## DataRange.MiddleScale </term> <description> 
##  
## 0.000000 </description> </item> 
## 
## <item><term> 
##  
## DataRange.Min </term> <description> 
##  
## -0.010000 </description> </item> 
## 
## <item><term> 
##  
## DataRange.NumberOfColors </term> <description> 
##  
## Seven </description> </item> 
## 
## <item><term> 
##  
## DataRange.UserDefinedColorScale.NumberOfColors </term> <description> 
##  
## Seven </description> </item> 
## 
## <item><term> 
##  
## DataRange.ZoomScale </term> <description> 
##  
## 8 </description> </item> 
## 
## <item><term> 
##  
## DisplayMode </term> <description> 
##  
## Fringe </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.CanShowFacet </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.ColorLegendOption </term> <description> 
##  
## Blend </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.DisplayResolution.AngleTolerance </term> <description> 
##  
## 15.0 </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.DisplayResolution.EdgeTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.DisplayResolution.FaceTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.DisplayResolution.Resolution </term> <description> 
##  
## Standard </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.DisplayResolution.WidthTolerance </term> <description> 
##  
## 0.3 </description> </item> 
## 
## <item><term> 
##  
## NumberOfContourLines </term> <description> 
##  
## 8 </description> </item> 
## 
## <item><term> 
##  
## SpikeLength </term> <description> 
##  
## 25.4 (millimeters part), 1.0 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2312.0.0  <br> 

class DistanceAnalysisBuilder1(NXOpen.Builder): 
    """ Represents a Distance Analysis builder. """


    ##  The display type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Fringe</term><description> 
    ##  Display in fringe. </description> </item><item><term> 
    ## Hedgehog</term><description> 
    ##  Display in hedgehog. </description> </item><item><term> 
    ## ContourLines</term><description> 
    ##  Display in contour lines. </description> </item></list>
    class DisplayModes(Enum):
        """
        Members Include: <Fringe> <Hedgehog> <ContourLines>
        """
        Fringe: int
        Hedgehog: int
        ContourLines: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DistanceAnalysisBuilder1.DisplayModes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link FaceAnalysisDataRangeBuilder NXOpen.GeometricAnalysis.FaceAnalysisDataRangeBuilder@endlink) DataRange
    ##  Returns the distance analysis data range.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return FaceAnalysisDataRangeBuilder
    @property
    def DataRange(self) -> FaceAnalysisDataRangeBuilder:
        """
        Getter for property: (@link FaceAnalysisDataRangeBuilder NXOpen.GeometricAnalysis.FaceAnalysisDataRangeBuilder@endlink) DataRange
         Returns the distance analysis data range.  
             
         
        """
        pass
    
    ## Getter for property: (@link DistanceAnalysisBuilder1.DisplayModes NXOpen.GeometricAnalysis.DistanceAnalysisBuilder1.DisplayModes@endlink) DisplayMode
    ##  Returns the display mode.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return DistanceAnalysisBuilder1.DisplayModes
    @property
    def DisplayMode(self) -> DistanceAnalysisBuilder1.DisplayModes:
        """
        Getter for property: (@link DistanceAnalysisBuilder1.DisplayModes NXOpen.GeometricAnalysis.DistanceAnalysisBuilder1.DisplayModes@endlink) DisplayMode
         Returns the display mode.  
             
         
        """
        pass
    
    ## Setter for property: (@link DistanceAnalysisBuilder1.DisplayModes NXOpen.GeometricAnalysis.DistanceAnalysisBuilder1.DisplayModes@endlink) DisplayMode

    ##  Returns the display mode.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @DisplayMode.setter
    def DisplayMode(self, displayMode: DistanceAnalysisBuilder1.DisplayModes):
        """
        Setter for property: (@link DistanceAnalysisBuilder1.DisplayModes NXOpen.GeometricAnalysis.DistanceAnalysisBuilder1.DisplayModes@endlink) DisplayMode
         Returns the display mode.  
             
         
        """
        pass
    
    ## Getter for property: (@link FaceAnalysisDisplayBuilder NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilder@endlink) DisplaySettings
    ##  Returns the distance analysis display settings.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return FaceAnalysisDisplayBuilder
    @property
    def DisplaySettings(self) -> FaceAnalysisDisplayBuilder:
        """
        Getter for property: (@link FaceAnalysisDisplayBuilder NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilder@endlink) DisplaySettings
         Returns the distance analysis display settings.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Features.GeometricConstraintDataManager NXOpen.Features.GeometricConstraintDataManager@endlink) DynamicLabel
    ##  Returns the dynamic label   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Features.GeometricConstraintDataManager
    @property
    def DynamicLabel(self) -> NXOpen.Features.GeometricConstraintDataManager:
        """
        Getter for property: (@link NXOpen.Features.GeometricConstraintDataManager NXOpen.Features.GeometricConstraintDataManager@endlink) DynamicLabel
         Returns the dynamic label   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Faces
    ##  Returns the face to apply distance analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def Faces(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Faces
         Returns the face to apply distance analysis.  
             
         
        """
        pass
    
    ## Getter for property: (int) NumberOfContourLines
    ##  Returns the number of contour lines.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return int
    @property
    def NumberOfContourLines(self) -> int:
        """
        Getter for property: (int) NumberOfContourLines
         Returns the number of contour lines.  
             
         
        """
        pass
    
    ## Setter for property: (int) NumberOfContourLines

    ##  Returns the number of contour lines.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @NumberOfContourLines.setter
    def NumberOfContourLines(self, numberOfContourLines: int):
        """
        Setter for property: (int) NumberOfContourLines
         Returns the number of contour lines.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane
    ##  Returns the reference plane for distance analysis.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Plane
    @property
    def Plane(self) -> NXOpen.Plane:
        """
        Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane
         Returns the reference plane for distance analysis.  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane

    ##  Returns the reference plane for distance analysis.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @Plane.setter
    def Plane(self, plane: NXOpen.Plane):
        """
        Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane
         Returns the reference plane for distance analysis.  
            
         
        """
        pass
    
    ## Getter for property: (float) SpikeLength
    ##  Returns the spike length.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def SpikeLength(self) -> float:
        """
        Getter for property: (float) SpikeLength
         Returns the spike length.  
             
         
        """
        pass
    
    ## Setter for property: (float) SpikeLength

    ##  Returns the spike length.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @SpikeLength.setter
    def SpikeLength(self, spikeLength: float):
        """
        Setter for property: (float) SpikeLength
         Returns the spike length.  
             
         
        """
        pass
    
    ##  Start distance analysis. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def StartDistanceAnalysis(self) -> None:
        """
         Start distance analysis. 
        """
        pass
    
    ##  Update display after plane changes. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def UpdateDisplayOnPlaneChange(self) -> None:
        """
         Update display after plane changes. 
        """
        pass
    
import NXOpen
import NXOpen.Features
##  Represents a Distance Analysis builder.  <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisObjectCollectionEx::CreateDistanceAnalysisBuilder  NXOpen::GeometricAnalysis::AnalysisObjectCollectionEx::CreateDistanceAnalysisBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DataRange.IsFixed (deprecated) </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## DataRange.Max (deprecated) </term> <description> 
##  
## 0.010000 </description> </item> 
## 
## <item><term> 
##  
## DataRange.Middle (deprecated) </term> <description> 
##  
## 0.000000 </description> </item> 
## 
## <item><term> 
##  
## DataRange.MiddleScale (deprecated) </term> <description> 
##  
## 0.000000 </description> </item> 
## 
## <item><term> 
##  
## DataRange.Min (deprecated) </term> <description> 
##  
## -0.010000 </description> </item> 
## 
## <item><term> 
##  
## DataRange.ZoomScale (deprecated) </term> <description> 
##  
## 8 </description> </item> 
## 
## <item><term> 
##  
## DisplayMode (deprecated) </term> <description> 
##  
## Fringe </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.CanShowFacet (deprecated) </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.ColorLegendOption (deprecated) </term> <description> 
##  
## Blend </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.DisplayResolution.AngleTolerance (deprecated) </term> <description> 
##  
## 15.0 </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.DisplayResolution.EdgeTolerance (deprecated) </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.DisplayResolution.FaceTolerance (deprecated) </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.DisplayResolution.Resolution (deprecated) </term> <description> 
##  
## Standard </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.DisplayResolution.WidthTolerance (deprecated) </term> <description> 
##  
## 0.3 </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.NumberOfColors (deprecated) </term> <description> 
##  
## Seven </description> </item> 
## 
## <item><term> 
##  
## NumberOfContourLines (deprecated) </term> <description> 
##  
## 8 </description> </item> 
## 
## <item><term> 
##  
## SpikeLength (deprecated) </term> <description> 
##  
## 25.4 (millimeters part), 1.0 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX11.0.0  <br> 
## 
##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1 NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1@endlink  instead.  <br> 

class DistanceAnalysisBuilder(NXOpen.Builder): 
    """ Represents a Distance Analysis builder. """


    ##  The display type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Fringe</term><description> 
    ##  Display in fringe. </description> </item><item><term> 
    ## Hedgehog</term><description> 
    ##  Display in hedgehog. </description> </item><item><term> 
    ## ContourLines</term><description> 
    ##  Display in contour lines. </description> </item></list>
    class DisplayModes(Enum):
        """
        Members Include: <Fringe> <Hedgehog> <ContourLines>
        """
        Fringe: int
        Hedgehog: int
        ContourLines: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DistanceAnalysisBuilder.DisplayModes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link FaceAnalysisDataRangeBuilder NXOpen.GeometricAnalysis.FaceAnalysisDataRangeBuilder@endlink) DataRange
    ##  Returns the distance analysis data range.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1 NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1@endlink  instead.  <br> 

    ## @return FaceAnalysisDataRangeBuilder
    @property
    def DataRange(self) -> FaceAnalysisDataRangeBuilder:
        """
        Getter for property: (@link FaceAnalysisDataRangeBuilder NXOpen.GeometricAnalysis.FaceAnalysisDataRangeBuilder@endlink) DataRange
         Returns the distance analysis data range.  
             
         
        """
        pass
    
    ## Getter for property: (@link DistanceAnalysisBuilder.DisplayModes NXOpen.GeometricAnalysis.DistanceAnalysisBuilder.DisplayModes@endlink) DisplayMode
    ##  Returns the display mode.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1 NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1@endlink  instead.  <br> 

    ## @return DistanceAnalysisBuilder.DisplayModes
    @property
    def DisplayMode(self) -> DistanceAnalysisBuilder.DisplayModes:
        """
        Getter for property: (@link DistanceAnalysisBuilder.DisplayModes NXOpen.GeometricAnalysis.DistanceAnalysisBuilder.DisplayModes@endlink) DisplayMode
         Returns the display mode.  
             
         
        """
        pass
    
    ## Setter for property: (@link DistanceAnalysisBuilder.DisplayModes NXOpen.GeometricAnalysis.DistanceAnalysisBuilder.DisplayModes@endlink) DisplayMode

    ##  Returns the display mode.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1 NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1@endlink  instead.  <br> 

    @DisplayMode.setter
    def DisplayMode(self, displayMode: DistanceAnalysisBuilder.DisplayModes):
        """
        Setter for property: (@link DistanceAnalysisBuilder.DisplayModes NXOpen.GeometricAnalysis.DistanceAnalysisBuilder.DisplayModes@endlink) DisplayMode
         Returns the display mode.  
             
         
        """
        pass
    
    ## Getter for property: (@link FaceAnalysisDisplayBuilder NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilder@endlink) DisplaySettings
    ##  Returns the distance analysis display settings.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1 NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1@endlink  instead.  <br> 

    ## @return FaceAnalysisDisplayBuilder
    @property
    def DisplaySettings(self) -> FaceAnalysisDisplayBuilder:
        """
        Getter for property: (@link FaceAnalysisDisplayBuilder NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilder@endlink) DisplaySettings
         Returns the distance analysis display settings.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Features.GeometricConstraintDataManager NXOpen.Features.GeometricConstraintDataManager@endlink) DynamicLabel
    ##  Returns the dynamic label   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1 NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1@endlink  instead.  <br> 

    ## @return NXOpen.Features.GeometricConstraintDataManager
    @property
    def DynamicLabel(self) -> NXOpen.Features.GeometricConstraintDataManager:
        """
        Getter for property: (@link NXOpen.Features.GeometricConstraintDataManager NXOpen.Features.GeometricConstraintDataManager@endlink) DynamicLabel
         Returns the dynamic label   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Faces
    ##  Returns the face to apply distance analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1 NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1@endlink  instead.  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def Faces(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Faces
         Returns the face to apply distance analysis.  
             
         
        """
        pass
    
    ## Getter for property: (@link FaceAnalysisNormalsBuilder NXOpen.GeometricAnalysis.FaceAnalysisNormalsBuilder@endlink) Normals
    ##  Returns the distance analysis normals.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1 NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1@endlink  instead.  <br> 

    ## @return FaceAnalysisNormalsBuilder
    @property
    def Normals(self) -> FaceAnalysisNormalsBuilder:
        """
        Getter for property: (@link FaceAnalysisNormalsBuilder NXOpen.GeometricAnalysis.FaceAnalysisNormalsBuilder@endlink) Normals
         Returns the distance analysis normals.  
             
         
        """
        pass
    
    ## Getter for property: (int) NumberOfContourLines
    ##  Returns the number of contour lines.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1 NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1@endlink  instead.  <br> 

    ## @return int
    @property
    def NumberOfContourLines(self) -> int:
        """
        Getter for property: (int) NumberOfContourLines
         Returns the number of contour lines.  
             
         
        """
        pass
    
    ## Setter for property: (int) NumberOfContourLines

    ##  Returns the number of contour lines.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1 NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1@endlink  instead.  <br> 

    @NumberOfContourLines.setter
    def NumberOfContourLines(self, numberOfContourLines: int):
        """
        Setter for property: (int) NumberOfContourLines
         Returns the number of contour lines.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane
    ##  Returns the reference plane for distance analysis.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1 NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1@endlink  instead.  <br> 

    ## @return NXOpen.Plane
    @property
    def Plane(self) -> NXOpen.Plane:
        """
        Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane
         Returns the reference plane for distance analysis.  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane

    ##  Returns the reference plane for distance analysis.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1 NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1@endlink  instead.  <br> 

    @Plane.setter
    def Plane(self, plane: NXOpen.Plane):
        """
        Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane
         Returns the reference plane for distance analysis.  
            
         
        """
        pass
    
    ## Getter for property: (float) SpikeLength
    ##  Returns the spike length.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1 NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1@endlink  instead.  <br> 

    ## @return float
    @property
    def SpikeLength(self) -> float:
        """
        Getter for property: (float) SpikeLength
         Returns the spike length.  
             
         
        """
        pass
    
    ## Setter for property: (float) SpikeLength

    ##  Returns the spike length.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1 NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1@endlink  instead.  <br> 

    @SpikeLength.setter
    def SpikeLength(self, spikeLength: float):
        """
        Setter for property: (float) SpikeLength
         Returns the spike length.  
             
         
        """
        pass
    
    ##  Start distance analysis. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1 NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1@endlink  instead.  <br> 

    ## License requirements: None.
    def StartDistanceAnalysis(self) -> None:
        """
         Start distance analysis. 
        """
        pass
    
    ##  Update display after plane changes. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1 NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1@endlink  instead.  <br> 

    ## License requirements: None.
    def UpdateDisplayOnPlaneChange(self) -> None:
        """
         Update display after plane changes. 
        """
        pass
    
##  Represents a distance analysis   <br> To create or edit an instance of this class, use @link NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1  NXOpen::GeometricAnalysis::DistanceAnalysisBuilder1 @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class DistanceAnalysis(AnalysisObject): 
    """ Represents a distance analysis  """
    pass


import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
##  Represents a Draft Analysis builder  <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisObjectCollection::CreateDraftAnalysisBuilder  NXOpen::GeometricAnalysis::AnalysisObjectCollection::CreateDraftAnalysisBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## CoupleLimit </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## CreateCSYS </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DrawOption </term> <description> 
##  
## Orientation </description> </item> 
## 
## <item><term> 
##  
## JoinIsocline </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## LimitAngleNegative </term> <description> 
##  
## -5 </description> </item> 
## 
## <item><term> 
##  
## LimitAnglePositive </term> <description> 
##  
## 5 </description> </item> 
## 
## <item><term> 
##  
## OutputOption </term> <description> 
##  
## AnalysisObject </description> </item> 
## 
## <item><term> 
##  
## Resolution.AngleTolerance </term> <description> 
##  
## 15.0 </description> </item> 
## 
## <item><term> 
##  
## Resolution.EdgeTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## Resolution.FaceTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## Resolution.Resolution </term> <description> 
##  
## Standard </description> </item> 
## 
## <item><term> 
##  
## Resolution.WidthTolerance </term> <description> 
##  
## 0.3 </description> </item> 
## 
## <item><term> 
##  
## ShowIsoclineNegative </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ShowIsoclinePositive </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ShowPartingLine </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## SwitchDisplayMode </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## TranslucencyInsideNegative </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## TranslucencyInsidePositive </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## TranslucencyOutsideNegative </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## TranslucencyOutsidePositive </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX8.0.0  <br> 

class DraftAnalysisBuilder(NXOpen.Builder): 
    """ Represents a Draft Analysis builder """


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
        def ValueOf(value: int) -> DraftAnalysisBuilder.DrawDirection:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  define output options 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## AnalysisObject</term><description> 
    ##  analysis object; </description> </item><item><term> 
    ## Isoclines</term><description> 
    ##  isoclines; </description> </item><item><term> 
    ## Both</term><description> 
    ##  analysis object and isoclines; </description> </item></list>
    class SelectOutput(Enum):
        """
        Members Include: <AnalysisObject> <Isoclines> <Both>
        """
        AnalysisObject: int
        Isoclines: int
        Both: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DraftAnalysisBuilder.SelectOutput:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) CoupleLimit
    ##  Returns the coupling limit   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return bool
    @property
    def CoupleLimit(self) -> bool:
        """
        Getter for property: (bool) CoupleLimit
         Returns the coupling limit   
            
         
        """
        pass
    
    ## Setter for property: (bool) CoupleLimit

    ##  Returns the coupling limit   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @CoupleLimit.setter
    def CoupleLimit(self, coupleLimit: bool):
        """
        Setter for property: (bool) CoupleLimit
         Returns the coupling limit   
            
         
        """
        pass
    
    ## Getter for property: (bool) CreateCSYS
    ##  Returns the datum CSYS creation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.1  <br> 

    ## @return bool
    @property
    def CreateCSYS(self) -> bool:
        """
        Getter for property: (bool) CreateCSYS
         Returns the datum CSYS creation   
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateCSYS

    ##  Returns the datum CSYS creation   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX8.0.1  <br> 

    @CreateCSYS.setter
    def CreateCSYS(self, createCSYS: bool):
        """
        Setter for property: (bool) CreateCSYS
         Returns the datum CSYS creation   
            
         
        """
        pass
    
    ## Getter for property: (@link DraftAnalysisBuilder.DrawDirection NXOpen.GeometricAnalysis.DraftAnalysisBuilder.DrawDirection@endlink) DrawOption
    ##  Returns the draw option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return DraftAnalysisBuilder.DrawDirection
    @property
    def DrawOption(self) -> DraftAnalysisBuilder.DrawDirection:
        """
        Getter for property: (@link DraftAnalysisBuilder.DrawDirection NXOpen.GeometricAnalysis.DraftAnalysisBuilder.DrawDirection@endlink) DrawOption
         Returns the draw option   
            
         
        """
        pass
    
    ## Setter for property: (@link DraftAnalysisBuilder.DrawDirection NXOpen.GeometricAnalysis.DraftAnalysisBuilder.DrawDirection@endlink) DrawOption

    ##  Returns the draw option   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @DrawOption.setter
    def DrawOption(self, drawOption: DraftAnalysisBuilder.DrawDirection):
        """
        Setter for property: (@link DraftAnalysisBuilder.DrawDirection NXOpen.GeometricAnalysis.DraftAnalysisBuilder.DrawDirection@endlink) DrawOption
         Returns the draw option   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) DrawOrientation
    ##  Returns the draw orientation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.Matrix3x3
    @property
    def DrawOrientation(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) DrawOrientation
         Returns the draw orientation   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) DrawOrientation

    ##  Returns the draw orientation   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @DrawOrientation.setter
    def DrawOrientation(self, drawOrientation: NXOpen.Matrix3x3):
        """
        Setter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) DrawOrientation
         Returns the draw orientation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) DrawOrigin
    ##  Returns the draw origin   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

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
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @DrawOrigin.setter
    def DrawOrigin(self, drawOrigin: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) DrawOrigin
         Returns the draw origin   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DrawVector
    ##  Returns the draw vector   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def DrawVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DrawVector
         Returns the draw vector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DrawVector

    ##  Returns the draw vector   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @DrawVector.setter
    def DrawVector(self, drawVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DrawVector
         Returns the draw vector   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Features.GeometricConstraintDataManager NXOpen.Features.GeometricConstraintDataManager@endlink) DynamicLabel
    ##  Returns the constraint manager   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.Features.GeometricConstraintDataManager
    @property
    def DynamicLabel(self) -> NXOpen.Features.GeometricConstraintDataManager:
        """
        Getter for property: (@link NXOpen.Features.GeometricConstraintDataManager NXOpen.Features.GeometricConstraintDataManager@endlink) DynamicLabel
         Returns the constraint manager   
            
         
        """
        pass
    
    ## Getter for property: (bool) JoinIsocline
    ##  Returns the joining isocline   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return bool
    @property
    def JoinIsocline(self) -> bool:
        """
        Getter for property: (bool) JoinIsocline
         Returns the joining isocline   
            
         
        """
        pass
    
    ## Setter for property: (bool) JoinIsocline

    ##  Returns the joining isocline   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @JoinIsocline.setter
    def JoinIsocline(self, joinIsocline: bool):
        """
        Setter for property: (bool) JoinIsocline
         Returns the joining isocline   
            
         
        """
        pass
    
    ## Getter for property: (float) LimitAngleNegative
    ##  Returns the negative limit angle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return float
    @property
    def LimitAngleNegative(self) -> float:
        """
        Getter for property: (float) LimitAngleNegative
         Returns the negative limit angle   
            
         
        """
        pass
    
    ## Setter for property: (float) LimitAngleNegative

    ##  Returns the negative limit angle   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @LimitAngleNegative.setter
    def LimitAngleNegative(self, limitAngleNeg: float):
        """
        Setter for property: (float) LimitAngleNegative
         Returns the negative limit angle   
            
         
        """
        pass
    
    ## Getter for property: (float) LimitAnglePositive
    ##  Returns the positive limit angle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return float
    @property
    def LimitAnglePositive(self) -> float:
        """
        Getter for property: (float) LimitAnglePositive
         Returns the positive limit angle   
            
         
        """
        pass
    
    ## Setter for property: (float) LimitAnglePositive

    ##  Returns the positive limit angle   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @LimitAnglePositive.setter
    def LimitAnglePositive(self, limitAnglePos: float):
        """
        Setter for property: (float) LimitAnglePositive
         Returns the positive limit angle   
            
         
        """
        pass
    
    ## Getter for property: (@link DraftAnalysisBuilder.SelectOutput NXOpen.GeometricAnalysis.DraftAnalysisBuilder.SelectOutput@endlink) OutputOption
    ##  Returns the output option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return DraftAnalysisBuilder.SelectOutput
    @property
    def OutputOption(self) -> DraftAnalysisBuilder.SelectOutput:
        """
        Getter for property: (@link DraftAnalysisBuilder.SelectOutput NXOpen.GeometricAnalysis.DraftAnalysisBuilder.SelectOutput@endlink) OutputOption
         Returns the output option   
            
         
        """
        pass
    
    ## Setter for property: (@link DraftAnalysisBuilder.SelectOutput NXOpen.GeometricAnalysis.DraftAnalysisBuilder.SelectOutput@endlink) OutputOption

    ##  Returns the output option   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @OutputOption.setter
    def OutputOption(self, outputOption: DraftAnalysisBuilder.SelectOutput):
        """
        Setter for property: (@link DraftAnalysisBuilder.SelectOutput NXOpen.GeometricAnalysis.DraftAnalysisBuilder.SelectOutput@endlink) OutputOption
         Returns the output option   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.DisplayResolutionBuilder NXOpen.GeometricUtilities.DisplayResolutionBuilder@endlink) Resolution
    ##  Returns the display resolution   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.DisplayResolutionBuilder
    @property
    def Resolution(self) -> NXOpen.GeometricUtilities.DisplayResolutionBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.DisplayResolutionBuilder NXOpen.GeometricUtilities.DisplayResolutionBuilder@endlink) Resolution
         Returns the display resolution   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) ReverseIndividual
    ##  Returns the individual face normal  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObject
    @property
    def ReverseIndividual(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) ReverseIndividual
         Returns the individual face normal  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectObject
    ##  Returns the faces or facet bodies   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def SelectObject(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectObject
         Returns the faces or facet bodies   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowIsoclineNegative
    ##  Returns the negative isocline   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return bool
    @property
    def ShowIsoclineNegative(self) -> bool:
        """
        Getter for property: (bool) ShowIsoclineNegative
         Returns the negative isocline   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowIsoclineNegative

    ##  Returns the negative isocline   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @ShowIsoclineNegative.setter
    def ShowIsoclineNegative(self, showIsoclineNeg: bool):
        """
        Setter for property: (bool) ShowIsoclineNegative
         Returns the negative isocline   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowIsoclinePositive
    ##  Returns the positive isocline   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return bool
    @property
    def ShowIsoclinePositive(self) -> bool:
        """
        Getter for property: (bool) ShowIsoclinePositive
         Returns the positive isocline   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowIsoclinePositive

    ##  Returns the positive isocline   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @ShowIsoclinePositive.setter
    def ShowIsoclinePositive(self, showIsoclinePos: bool):
        """
        Setter for property: (bool) ShowIsoclinePositive
         Returns the positive isocline   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowPartingLine
    ##  Returns the show parting line   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return bool
    @property
    def ShowPartingLine(self) -> bool:
        """
        Getter for property: (bool) ShowPartingLine
         Returns the show parting line   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowPartingLine

    ##  Returns the show parting line   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @ShowPartingLine.setter
    def ShowPartingLine(self, showPartingLine: bool):
        """
        Setter for property: (bool) ShowPartingLine
         Returns the show parting line   
            
         
        """
        pass
    
    ## Getter for property: (bool) SwitchDisplayMode
    ##  Returns the toggle to switch display mode   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def SwitchDisplayMode(self) -> bool:
        """
        Getter for property: (bool) SwitchDisplayMode
         Returns the toggle to switch display mode   
            
         
        """
        pass
    
    ## Setter for property: (bool) SwitchDisplayMode

    ##  Returns the toggle to switch display mode   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @SwitchDisplayMode.setter
    def SwitchDisplayMode(self, switchDisplayMode: bool):
        """
        Setter for property: (bool) SwitchDisplayMode
         Returns the toggle to switch display mode   
            
         
        """
        pass
    
    ## Getter for property: (int) TranslucencyInsideNegative
    ##  Returns the negative inside translucency   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return int
    @property
    def TranslucencyInsideNegative(self) -> int:
        """
        Getter for property: (int) TranslucencyInsideNegative
         Returns the negative inside translucency   
            
         
        """
        pass
    
    ## Setter for property: (int) TranslucencyInsideNegative

    ##  Returns the negative inside translucency   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @TranslucencyInsideNegative.setter
    def TranslucencyInsideNegative(self, translucencyInsideNeg: int):
        """
        Setter for property: (int) TranslucencyInsideNegative
         Returns the negative inside translucency   
            
         
        """
        pass
    
    ## Getter for property: (int) TranslucencyInsidePositive
    ##  Returns the positive inside translucency   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return int
    @property
    def TranslucencyInsidePositive(self) -> int:
        """
        Getter for property: (int) TranslucencyInsidePositive
         Returns the positive inside translucency   
            
         
        """
        pass
    
    ## Setter for property: (int) TranslucencyInsidePositive

    ##  Returns the positive inside translucency   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @TranslucencyInsidePositive.setter
    def TranslucencyInsidePositive(self, translucencyInsidePos: int):
        """
        Setter for property: (int) TranslucencyInsidePositive
         Returns the positive inside translucency   
            
         
        """
        pass
    
    ## Getter for property: (int) TranslucencyOutsideNegative
    ##  Returns the negative outside tanslucency   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return int
    @property
    def TranslucencyOutsideNegative(self) -> int:
        """
        Getter for property: (int) TranslucencyOutsideNegative
         Returns the negative outside tanslucency   
            
         
        """
        pass
    
    ## Setter for property: (int) TranslucencyOutsideNegative

    ##  Returns the negative outside tanslucency   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @TranslucencyOutsideNegative.setter
    def TranslucencyOutsideNegative(self, translucencyOutsideNeg: int):
        """
        Setter for property: (int) TranslucencyOutsideNegative
         Returns the negative outside tanslucency   
            
         
        """
        pass
    
    ## Getter for property: (int) TranslucencyOutsidePositive
    ##  Returns the positive outside translucenty   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return int
    @property
    def TranslucencyOutsidePositive(self) -> int:
        """
        Getter for property: (int) TranslucencyOutsidePositive
         Returns the positive outside translucenty   
            
         
        """
        pass
    
    ## Setter for property: (int) TranslucencyOutsidePositive

    ##  Returns the positive outside translucenty   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @TranslucencyOutsidePositive.setter
    def TranslucencyOutsidePositive(self, translucencyOutsidePos: int):
        """
        Setter for property: (int) TranslucencyOutsidePositive
         Returns the positive outside translucenty   
            
         
        """
        pass
    
    ##  Adds dynamic points to the draft analysis object 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    def AddDynamicPoints(self) -> None:
        """
         Adds dynamic points to the draft analysis object 
        """
        pass
    
    ##  Deletes dynamic labels whose corresponding positions are set to true in the array 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="deletedLabels"> (List[bool]) </param>
    def DeleteDynamicLabels(self, deletedLabels: List[bool]) -> None:
        """
         Deletes dynamic labels whose corresponding positions are set to true in the array 
        """
        pass
    
    ##  Deselects faces 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="faces"> (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink) </param>
    def DeselectFaces(self, faces: List[NXOpen.DisplayableObject]) -> None:
        """
         Deselects faces 
        """
        pass
    
    ##  Returns the negative inside color 
    ##  @return colorInsideNeg (List[float]):  Array of 3 RGB values, each between 0 and 1 .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    def GetColorInsideNegative(self) -> List[float]:
        """
         Returns the negative inside color 
         @return colorInsideNeg (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    
    ##  Returns the positive inside color 
    ##  @return colorInsidePos (List[float]):  Array of 3 RGB values, each between 0 and 1 .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    def GetColorInsidePositive(self) -> List[float]:
        """
         Returns the positive inside color 
         @return colorInsidePos (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    
    ##  Returns the negative outside color 
    ##  @return colorOutsideNeg (List[float]):  Array of 3 RGB values, each between 0 and 1 .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    def GetColorOutsideNegative(self) -> List[float]:
        """
         Returns the negative outside color 
         @return colorOutsideNeg (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    
    ##  Returns the positive outside color 
    ##  @return colorOutsidePos (List[float]):  Array of 3 RGB values, each between 0 and 1 .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    def GetColorOutsidePositive(self) -> List[float]:
        """
         Returns the positive outside color 
         @return colorOutsidePos (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    
    ##  Removes dynamic label parents 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="parents"> (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink) </param>
    def RemoveLabelParents(self, parents: List[NXOpen.DisplayableObject]) -> None:
        """
         Removes dynamic label parents 
        """
        pass
    
    ##  Reverses all normals 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    def ReverseAllNormals(self) -> None:
        """
         Reverses all normals 
        """
        pass
    
    ##  Reverses individual face normal 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="face"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink) </param>
    def ReverseNormal(self, face: NXOpen.DisplayableObject) -> None:
        """
         Reverses individual face normal 
        """
        pass
    
    ##  Sets the negative inside color 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="colorInsideNeg"> (List[float])  Array of 3 RGB values, each between 0 and 1 </param>
    def SetColorInsideNegative(self, colorInsideNeg: List[float]) -> None:
        """
         Sets the negative inside color 
        """
        pass
    
    ##  Sets the positive inside color 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="colorInsidePos"> (List[float])  Array of 3 RGB values, each between 0 and 1 </param>
    def SetColorInsidePositive(self, colorInsidePos: List[float]) -> None:
        """
         Sets the positive inside color 
        """
        pass
    
    ##  Sets the negative outside color 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="colorOutsideNeg"> (List[float])  Array of 3 RGB values, each between 0 and 1 </param>
    def SetColorOutsideNegative(self, colorOutsideNeg: List[float]) -> None:
        """
         Sets the negative outside color 
        """
        pass
    
    ##  Sets the positive outside color 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="colorOutsidePos"> (List[float])  Array of 3 RGB values, each between 0 and 1 </param>
    def SetColorOutsidePositive(self, colorOutsidePos: List[float]) -> None:
        """
         Sets the positive outside color 
        """
        pass
    
    ##  Sets dynamic normal 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="normal"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) </param>
    def SetDynamicNormal(self, index: int, normal: NXOpen.Vector3d) -> None:
        """
         Sets dynamic normal 
        """
        pass
    
    ##  Sets dynamic parent 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="parent"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink) </param>
    def SetDynamicParent(self, index: int, parent: NXOpen.DisplayableObject) -> None:
        """
         Sets dynamic parent 
        """
        pass
    
    ##  Sets number of dynamic normals 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="total"> (int) </param>
    def SetTotalDynamicNormals(self, total: int) -> None:
        """
         Sets number of dynamic normals 
        """
        pass
    
    ##  Updates reverse map 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    def UpdateReverseMap(self) -> None:
        """
         Updates reverse map 
        """
        pass
    
##  Represents a Draft Analysis builder  <br> To create or edit an instance of this class, use @link NXOpen::GeometricAnalysis::DraftAnalysisBuilder  NXOpen::GeometricAnalysis::DraftAnalysisBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.0.0  <br> 

class DraftAnalysis(AnalysisObject): 
    """ Represents a Draft Analysis builder """
    pass


import NXOpen
import NXOpen.GeometricUtilities
##  The Dupin Indicatrix is a tool to geometrically display the surface curvature at a specified point on a surface. 
## 
##   <br>  Created in NX8.0.0  <br> 

class DupinBuilder(NXOpen.TaggedObject): 
    """ The Dupin Indicatrix is a tool to geometrically display the surface curvature at a specified point on a surface. """


    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) AnalysisPoint
    ##  Returns the point location defining where the analysis should be done.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def AnalysisPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) AnalysisPoint
         Returns the point location defining where the analysis should be done.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) AnalysisPoint

    ##  Returns the point location defining where the analysis should be done.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @AnalysisPoint.setter
    def AnalysisPoint(self, analysisPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) AnalysisPoint
         Returns the point location defining where the analysis should be done.  
             
         
        """
        pass
    
    ## Getter for property: (float) Angle
    ##  Returns the deviation in degrees from the minimum curvature.  
    ##    This value is used to rotate the normal curvature about the specified point.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return float
    @property
    def Angle(self) -> float:
        """
        Getter for property: (float) Angle
         Returns the deviation in degrees from the minimum curvature.  
           This value is used to rotate the normal curvature about the specified point.   
         
        """
        pass
    
    ## Setter for property: (float) Angle

    ##  Returns the deviation in degrees from the minimum curvature.  
    ##    This value is used to rotate the normal curvature about the specified point.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @Angle.setter
    def Angle(self, angle: float):
        """
        Setter for property: (float) Angle
         Returns the deviation in degrees from the minimum curvature.  
           This value is used to rotate the normal curvature about the specified point.   
         
        """
        pass
    
    ## Getter for property: (float) FlatnessTolerance
    ##  Returns the tolerance that defines at the specified point if an area is flat.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return float
    @property
    def FlatnessTolerance(self) -> float:
        """
        Getter for property: (float) FlatnessTolerance
         Returns the tolerance that defines at the specified point if an area is flat.  
             
         
        """
        pass
    
    ## Setter for property: (float) FlatnessTolerance

    ##  Returns the tolerance that defines at the specified point if an area is flat.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @FlatnessTolerance.setter
    def FlatnessTolerance(self, flatnessTolerance: float):
        """
        Setter for property: (float) FlatnessTolerance
         Returns the tolerance that defines at the specified point if an area is flat.  
             
         
        """
        pass
    
    ## Getter for property: (float) Scale
    ##  Returns the scale factor to apply to the display of the dupin indicatrix.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return float
    @property
    def Scale(self) -> float:
        """
        Getter for property: (float) Scale
         Returns the scale factor to apply to the display of the dupin indicatrix.  
             
         
        """
        pass
    
    ## Setter for property: (float) Scale

    ##  Returns the scale factor to apply to the display of the dupin indicatrix.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @Scale.setter
    def Scale(self, scale: float):
        """
        Setter for property: (float) Scale
         Returns the scale factor to apply to the display of the dupin indicatrix.  
             
         
        """
        pass
    
    ##  Reset the analysis point to accept dynamic input. 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    def ResetAnalysisPoint(self) -> None:
        """
         Reset the analysis point to accept dynamic input. 
        """
        pass
    
import NXOpen
##  Represents the Examine Geometry class
##       <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisManager::CreateExamineGeometryObject  NXOpen::GeometricAnalysis::AnalysisManager::CreateExamineGeometryObject @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class ExamineGeometry(NXOpen.Builder): 
    """ Represents the Examine Geometry class
     """


    ##  Types of checks 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ObjectTiny</term><description> 
    ##  ObjectTiny </description> </item><item><term> 
    ## ObjectMisaligned</term><description> 
    ##  ObjectMisaligned </description> </item><item><term> 
    ## BodyDataStructures</term><description> 
    ##  BodyDataStructures </description> </item><item><term> 
    ## BodyConsistency</term><description> 
    ##  BodyConsistency </description> </item><item><term> 
    ## BodyFaceIntersections</term><description> 
    ##  BodyFaceIntersections </description> </item><item><term> 
    ## BodySheetBoundaries</term><description> 
    ##  BodySheetBoundaries </description> </item><item><term> 
    ## FaceSmoothness</term><description> 
    ##  FaceSmoothness </description> </item><item><term> 
    ## FaceSelfIntersection</term><description> 
    ##  FaceSelfIntersection </description> </item><item><term> 
    ## FaceSpikesCuts</term><description> 
    ##  FaceSpikesCuts </description> </item><item><term> 
    ## EdgeSmoothness</term><description> 
    ##  EdgeSmoothness </description> </item><item><term> 
    ## EdgeTolerances</term><description> 
    ##  EdgeTolerances </description> </item><item><term> 
    ## NumChecks</term><description> 
    ##  Number of Checks </description> </item></list>
    class Check(Enum):
        """
        Members Include: <ObjectTiny> <ObjectMisaligned> <BodyDataStructures> <BodyConsistency> <BodyFaceIntersections> <BodySheetBoundaries> <FaceSmoothness> <FaceSelfIntersection> <FaceSpikesCuts> <EdgeSmoothness> <EdgeTolerances> <NumChecks>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ExamineGeometry.Check:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) CheckCriteriaAngle
    ##  Returns the Check Criteria Angle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def CheckCriteriaAngle(self) -> float:
        """
        Getter for property: (float) CheckCriteriaAngle
         Returns the Check Criteria Angle   
            
         
        """
        pass
    
    ## Setter for property: (float) CheckCriteriaAngle

    ##  Returns the Check Criteria Angle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @CheckCriteriaAngle.setter
    def CheckCriteriaAngle(self, angle: float):
        """
        Setter for property: (float) CheckCriteriaAngle
         Returns the Check Criteria Angle   
            
         
        """
        pass
    
    ## Getter for property: (float) CheckCriteriaDistance
    ##  Returns the Check Criteria Distance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def CheckCriteriaDistance(self) -> float:
        """
        Getter for property: (float) CheckCriteriaDistance
         Returns the Check Criteria Distance   
            
         
        """
        pass
    
    ## Setter for property: (float) CheckCriteriaDistance

    ##  Returns the Check Criteria Distance   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @CheckCriteriaDistance.setter
    def CheckCriteriaDistance(self, distance: float):
        """
        Setter for property: (float) CheckCriteriaDistance
         Returns the Check Criteria Distance   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectObjectList NXOpen.SelectObjectList@endlink) ObjectsToExamine
    ##  Returns the Objects to examine   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.SelectObjectList
    @property
    def ObjectsToExamine(self) -> NXOpen.SelectObjectList:
        """
        Getter for property: (@link NXOpen.SelectObjectList NXOpen.SelectObjectList@endlink) ObjectsToExamine
         Returns the Objects to examine   
            
         
        """
        pass
    
    ##  Clear or unset all types of checks 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def ClearAllChecks(self) -> None:
        """
         Clear or unset all types of checks 
        """
        pass
    
    ##  Clear or unset a specified type of check 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="check"> (@link ExamineGeometry.Check NXOpen.GeometricAnalysis.ExamineGeometry.Check@endlink)  Type of Check </param>
    def ClearCheck(self, check: ExamineGeometry.Check) -> None:
        """
         Clear or unset a specified type of check 
        """
        pass
    
    ##  Displays the results in the information window 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def DisplayResultsAsInfo(self) -> None:
        """
         Displays the results in the information window 
        """
        pass
    
    ##  Examines the geometry.  Before calling this method, use 
    ##             @link NXOpen::GeometricAnalysis::ExamineGeometry::SetCheck NXOpen::GeometricAnalysis::ExamineGeometry::SetCheck@endlink  and @link NXOpen::GeometricAnalysis::ExamineGeometry::ClearCheck NXOpen::GeometricAnalysis::ExamineGeometry::ClearCheck@endlink  
    ##             to specify which checks to perform and use @link NXOpen::GeometricAnalysis::ExamineGeometry::ObjectsToExamine NXOpen::GeometricAnalysis::ExamineGeometry::ObjectsToExamine@endlink  
    ##             to specify which objects to examine.  After calling this method, 
    ##             use @link NXOpen::GeometricAnalysis::ExamineGeometry::GetResults NXOpen::GeometricAnalysis::ExamineGeometry::GetResults@endlink  and 
    ##             @link NXOpen::GeometricAnalysis::ExamineGeometry::GetFailedObjects NXOpen::GeometricAnalysis::ExamineGeometry::GetFailedObjects@endlink  to get the results. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def Examine(self) -> None:
        """
         Examines the geometry.  Before calling this method, use 
                    @link NXOpen::GeometricAnalysis::ExamineGeometry::SetCheck NXOpen::GeometricAnalysis::ExamineGeometry::SetCheck@endlink  and @link NXOpen::GeometricAnalysis::ExamineGeometry::ClearCheck NXOpen::GeometricAnalysis::ExamineGeometry::ClearCheck@endlink  
                    to specify which checks to perform and use @link NXOpen::GeometricAnalysis::ExamineGeometry::ObjectsToExamine NXOpen::GeometricAnalysis::ExamineGeometry::ObjectsToExamine@endlink  
                    to specify which objects to examine.  After calling this method, 
                    use @link NXOpen::GeometricAnalysis::ExamineGeometry::GetResults NXOpen::GeometricAnalysis::ExamineGeometry::GetResults@endlink  and 
                    @link NXOpen::GeometricAnalysis::ExamineGeometry::GetFailedObjects NXOpen::GeometricAnalysis::ExamineGeometry::GetFailedObjects@endlink  to get the results. 
        """
        pass
    
    ##  Returns the objects that failed a given type of check.  You should 
    ##         call @link NXOpen::GeometricAnalysis::ExamineGeometry::Examine NXOpen::GeometricAnalysis::ExamineGeometry::Examine@endlink  before calling this method.   
    ##  @return objects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  Objects that
    ##          failed above check during Examine Geometry .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="check"> (@link ExamineGeometry.Check NXOpen.GeometricAnalysis.ExamineGeometry.Check@endlink)  Type of Check </param>
    def GetFailedObjects(self, check: ExamineGeometry.Check) -> List[NXOpen.NXObject]:
        """
         Returns the objects that failed a given type of check.  You should 
                call @link NXOpen::GeometricAnalysis::ExamineGeometry::Examine NXOpen::GeometricAnalysis::ExamineGeometry::Examine@endlink  before calling this method.   
         @return objects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  Objects that
                 failed above check during Examine Geometry .
        """
        pass
    
    ##  Returns an array containing the number of objects that failed each check.
    ##               You should call @link NXOpen::GeometricAnalysis::ExamineGeometry::Examine NXOpen::GeometricAnalysis::ExamineGeometry::Examine@endlink  before calling this 
    ##               method.    The array contains an entry for each check in the
    ##               @link NXOpen::GeometricAnalysis::ExamineGeometry::Check NXOpen::GeometricAnalysis::ExamineGeometry::Check@endlink  enumeration.  The nth item in the array corresponds to
    ##               the nth check in the @link NXOpen::GeometricAnalysis::ExamineGeometry::Check NXOpen::GeometricAnalysis::ExamineGeometry::Check@endlink  enumeration.  For example, the 
    ##               first item in the array is the number of objects that failed the 
    ##               @link GeometricAnalysis::ExamineGeometry::CheckObjectTiny GeometricAnalysis::ExamineGeometry::CheckObjectTiny@endlink  check.  
    ##               The corresponding entry in the array will be as follows:
    ##                <br>  <br> 
    ##               <ul>
    ##               <li> <b>-1</b>    errors</li>
    ##               <li> <b>0</b>    Check not performed as check is not selected</li>
    ##               <li> <b>-2</b>    a type of @link NXOpen::GeometricAnalysis::ExamineGeometry::Check NXOpen::GeometricAnalysis::ExamineGeometry::Check@endlink  is selected, no objects relevant to that type 
    ##                     of @link NXOpen::GeometricAnalysis::ExamineGeometry::Check NXOpen::GeometricAnalysis::ExamineGeometry::Check@endlink  are selected. For example, no bodies are selected yet the 
    ##                     @link GeometricAnalysis::ExamineGeometry::CheckBodyDataStructures GeometricAnalysis::ExamineGeometry::CheckBodyDataStructures@endlink  check is
    ##                     set or selected. </li>
    ##               <li> <b>-3</b>    @link NXOpen::GeometricAnalysis::ExamineGeometry::Check NXOpen::GeometricAnalysis::ExamineGeometry::Check@endlink  not performed as other relevant @link NXOpen::GeometricAnalysis::ExamineGeometry::Check NXOpen::GeometricAnalysis::ExamineGeometry::Check@endlink  failed. This occurs when 
    ##                     @link GeometricAnalysis::ExamineGeometry::CheckBodyConsistency GeometricAnalysis::ExamineGeometry::CheckBodyConsistency@endlink 
    ##                     and/or @link GeometricAnalysis::ExamineGeometry::CheckBodyFaceIntersections GeometricAnalysis::ExamineGeometry::CheckBodyFaceIntersections@endlink  check is set along with 
    ##                     @link GeometricAnalysis::ExamineGeometry::CheckBodyDataStructures GeometricAnalysis::ExamineGeometry::CheckBodyDataStructures@endlink  check.
    ##                     If @link GeometricAnalysis::ExamineGeometry::CheckBodyDataStructures GeometricAnalysis::ExamineGeometry::CheckBodyDataStructures@endlink  check
    ##                     failed, @link GeometricAnalysis::ExamineGeometry::CheckBodyConsistency GeometricAnalysis::ExamineGeometry::CheckBodyConsistency@endlink 
    ##                     and/or
    ##                     @link GeometricAnalysis::ExamineGeometry::CheckBodyFaceIntersections GeometricAnalysis::ExamineGeometry::CheckBodyFaceIntersections@endlink  will
    ##                     not be performed. </li> 
    ##             </ul> 
    ##  @return results (List[int]):  Results of Examine Geometry .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetResults(self) -> List[int]:
        """
         Returns an array containing the number of objects that failed each check.
                      You should call @link NXOpen::GeometricAnalysis::ExamineGeometry::Examine NXOpen::GeometricAnalysis::ExamineGeometry::Examine@endlink  before calling this 
                      method.    The array contains an entry for each check in the
                      @link NXOpen::GeometricAnalysis::ExamineGeometry::Check NXOpen::GeometricAnalysis::ExamineGeometry::Check@endlink  enumeration.  The nth item in the array corresponds to
                      the nth check in the @link NXOpen::GeometricAnalysis::ExamineGeometry::Check NXOpen::GeometricAnalysis::ExamineGeometry::Check@endlink  enumeration.  For example, the 
                      first item in the array is the number of objects that failed the 
                      @link GeometricAnalysis::ExamineGeometry::CheckObjectTiny GeometricAnalysis::ExamineGeometry::CheckObjectTiny@endlink  check.  
                      The corresponding entry in the array will be as follows:
                       <br>  <br> 
                      <ul>
                      <li> <b>-1</b>    errors</li>
                      <li> <b>0</b>    Check not performed as check is not selected</li>
                      <li> <b>-2</b>    a type of @link NXOpen::GeometricAnalysis::ExamineGeometry::Check NXOpen::GeometricAnalysis::ExamineGeometry::Check@endlink  is selected, no objects relevant to that type 
                            of @link NXOpen::GeometricAnalysis::ExamineGeometry::Check NXOpen::GeometricAnalysis::ExamineGeometry::Check@endlink  are selected. For example, no bodies are selected yet the 
                            @link GeometricAnalysis::ExamineGeometry::CheckBodyDataStructures GeometricAnalysis::ExamineGeometry::CheckBodyDataStructures@endlink  check is
                            set or selected. </li>
                      <li> <b>-3</b>    @link NXOpen::GeometricAnalysis::ExamineGeometry::Check NXOpen::GeometricAnalysis::ExamineGeometry::Check@endlink  not performed as other relevant @link NXOpen::GeometricAnalysis::ExamineGeometry::Check NXOpen::GeometricAnalysis::ExamineGeometry::Check@endlink  failed. This occurs when 
                            @link GeometricAnalysis::ExamineGeometry::CheckBodyConsistency GeometricAnalysis::ExamineGeometry::CheckBodyConsistency@endlink 
                            and/or @link GeometricAnalysis::ExamineGeometry::CheckBodyFaceIntersections GeometricAnalysis::ExamineGeometry::CheckBodyFaceIntersections@endlink  check is set along with 
                            @link GeometricAnalysis::ExamineGeometry::CheckBodyDataStructures GeometricAnalysis::ExamineGeometry::CheckBodyDataStructures@endlink  check.
                            If @link GeometricAnalysis::ExamineGeometry::CheckBodyDataStructures GeometricAnalysis::ExamineGeometry::CheckBodyDataStructures@endlink  check
                            failed, @link GeometricAnalysis::ExamineGeometry::CheckBodyConsistency GeometricAnalysis::ExamineGeometry::CheckBodyConsistency@endlink 
                            and/or
                            @link GeometricAnalysis::ExamineGeometry::CheckBodyFaceIntersections GeometricAnalysis::ExamineGeometry::CheckBodyFaceIntersections@endlink  will
                            not be performed. </li> 
                    </ul> 
         @return results (List[int]):  Results of Examine Geometry .
        """
        pass
    
    ##  Highlights results of a specified type of check. If the
    ##          highlighting fails for some of the entities, it returns True, otherwise
    ##          False.  Highlighting can fail when the entities are corrupt or missing
    ##          the information needed to display properly. Remaining entities are highlighted 
    ##          when highlighting fails for some entities. 
    ##  @return failed (bool):  Return status of the method.
    ##                                                    If return values equals
    ##                                                    false, display was successful. 
    ##                                                    if return value is true,
    ##                                                    display of some objects
    ##                                                    failed. .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="check"> (@link ExamineGeometry.Check NXOpen.GeometricAnalysis.ExamineGeometry.Check@endlink)  Type of Check </param>
    def HighlightResult(self, check: ExamineGeometry.Check) -> bool:
        """
         Highlights results of a specified type of check. If the
                 highlighting fails for some of the entities, it returns True, otherwise
                 False.  Highlighting can fail when the entities are corrupt or missing
                 the information needed to display properly. Remaining entities are highlighted 
                 when highlighting fails for some entities. 
         @return failed (bool):  Return status of the method.
                                                           If return values equals
                                                           false, display was successful. 
                                                           if return value is true,
                                                           display of some objects
                                                           failed. .
        """
        pass
    
    ##  Set all types of checks to examine 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def SetAllChecks(self) -> None:
        """
         Set all types of checks to examine 
        """
        pass
    
    ##  Set a specified type of check for examine geometry 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="check"> (@link ExamineGeometry.Check NXOpen.GeometricAnalysis.ExamineGeometry.Check@endlink)  Type of Check </param>
    def SetCheck(self, check: ExamineGeometry.Check) -> None:
        """
         Set a specified type of check for examine geometry 
        """
        pass
    
    ##  Unhighlight all results 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def UnhighlightAllResults(self) -> None:
        """
         Unhighlight all results 
        """
        pass
    
    ##  Unhighlight results of a specified type of check
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="check"> (@link ExamineGeometry.Check NXOpen.GeometricAnalysis.ExamineGeometry.Check@endlink)  Type of Check </param>
    def UnhighlightResult(self, check: ExamineGeometry.Check) -> None:
        """
         Unhighlight results of a specified type of check
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents data range functions used by Face Analysis. 
## 
##   <br>  Created in NX11.0.0  <br> 

class FaceAnalysisDataRangeBuilder(NXOpen.TaggedObject): 
    """ Represents data range functions used by Face Analysis. """


    ##  the option for defining colors and intervals. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Automatic</term><description> 
    ##  System determined colors and intervals. </description> </item><item><term> 
    ## UserDefined</term><description> 
    ##  User defined colors and intervals. </description> </item></list>
    class ColorScaleOptions(Enum):
        """
        Members Include: <Automatic> <UserDefined>
        """
        Automatic: int
        UserDefined: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FaceAnalysisDataRangeBuilder.ColorScaleOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The option indicating number of colors to be used for display when color scale option is set to Automatic. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Two</term><description> 
    ##  Display in 2  colors. </description> </item><item><term> 
    ## Three</term><description> 
    ##  Display in 3  colors. </description> </item><item><term> 
    ## Four</term><description> 
    ##  Display in 4  colors. </description> </item><item><term> 
    ## Five</term><description> 
    ##  Display in 5  colors. </description> </item><item><term> 
    ## Six</term><description> 
    ##  Display in 6  colors. </description> </item><item><term> 
    ## Seven</term><description> 
    ##  Display in 7  colors. </description> </item><item><term> 
    ## Eight</term><description> 
    ##  Display in 8  colors. </description> </item><item><term> 
    ## Nine</term><description> 
    ##  Display in 9  colors. </description> </item><item><term> 
    ## Ten</term><description> 
    ##  Display in 10 colors. </description> </item><item><term> 
    ## Eleven</term><description> 
    ##  Display in 11 colors. </description> </item><item><term> 
    ## Twelve</term><description> 
    ##  Display in 12 colors. </description> </item></list>
    class NumberOfColorsOptions(Enum):
        """
        Members Include: <Two> <Three> <Four> <Five> <Six> <Seven> <Eight> <Nine> <Ten> <Eleven> <Twelve>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FaceAnalysisDataRangeBuilder.NumberOfColorsOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link FaceAnalysisDataRangeBuilder.ColorScaleOptions NXOpen.GeometricAnalysis.FaceAnalysisDataRangeBuilder.ColorScaleOptions@endlink) ColorScaleOption
    ##  Returns the intervals option.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return FaceAnalysisDataRangeBuilder.ColorScaleOptions
    @property
    def ColorScaleOption(self) -> FaceAnalysisDataRangeBuilder.ColorScaleOptions:
        """
        Getter for property: (@link FaceAnalysisDataRangeBuilder.ColorScaleOptions NXOpen.GeometricAnalysis.FaceAnalysisDataRangeBuilder.ColorScaleOptions@endlink) ColorScaleOption
         Returns the intervals option.  
             
         
        """
        pass
    
    ## Setter for property: (@link FaceAnalysisDataRangeBuilder.ColorScaleOptions NXOpen.GeometricAnalysis.FaceAnalysisDataRangeBuilder.ColorScaleOptions@endlink) ColorScaleOption

    ##  Returns the intervals option.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @ColorScaleOption.setter
    def ColorScaleOption(self, colorScaleOption: FaceAnalysisDataRangeBuilder.ColorScaleOptions):
        """
        Setter for property: (@link FaceAnalysisDataRangeBuilder.ColorScaleOptions NXOpen.GeometricAnalysis.FaceAnalysisDataRangeBuilder.ColorScaleOptions@endlink) ColorScaleOption
         Returns the intervals option.  
             
         
        """
        pass
    
    ## Getter for property: (bool) IsFixed
    ##  Returns the value indicating the range is fixed or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def IsFixed(self) -> bool:
        """
        Getter for property: (bool) IsFixed
         Returns the value indicating the range is fixed or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) IsFixed

    ##  Returns the value indicating the range is fixed or not.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @IsFixed.setter
    def IsFixed(self, isFixed: bool):
        """
        Setter for property: (bool) IsFixed
         Returns the value indicating the range is fixed or not.  
             
         
        """
        pass
    
    ## Getter for property: (float) Max
    ##  Returns the maximum data range.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return float
    @property
    def Max(self) -> float:
        """
        Getter for property: (float) Max
         Returns the maximum data range.  
             
         
        """
        pass
    
    ## Setter for property: (float) Max

    ##  Returns the maximum data range.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Max.setter
    def Max(self, max: float):
        """
        Setter for property: (float) Max
         Returns the maximum data range.  
             
         
        """
        pass
    
    ## Getter for property: (float) Middle
    ##  Returns the middle data range value.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return float
    @property
    def Middle(self) -> float:
        """
        Getter for property: (float) Middle
         Returns the middle data range value.  
             
         
        """
        pass
    
    ## Setter for property: (float) Middle

    ##  Returns the middle data range value.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Middle.setter
    def Middle(self, middle: float):
        """
        Setter for property: (float) Middle
         Returns the middle data range value.  
             
         
        """
        pass
    
    ## Getter for property: (float) MiddleScale
    ##  Returns the middle value scale for data range.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return float
    @property
    def MiddleScale(self) -> float:
        """
        Getter for property: (float) MiddleScale
         Returns the middle value scale for data range.  
             
         
        """
        pass
    
    ## Setter for property: (float) MiddleScale

    ##  Returns the middle value scale for data range.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @MiddleScale.setter
    def MiddleScale(self, middleScale: float):
        """
        Setter for property: (float) MiddleScale
         Returns the middle value scale for data range.  
             
         
        """
        pass
    
    ## Getter for property: (float) Min
    ##  Returns the minimum data range.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return float
    @property
    def Min(self) -> float:
        """
        Getter for property: (float) Min
         Returns the minimum data range.  
             
         
        """
        pass
    
    ## Setter for property: (float) Min

    ##  Returns the minimum data range.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Min.setter
    def Min(self, min: float):
        """
        Setter for property: (float) Min
         Returns the minimum data range.  
             
         
        """
        pass
    
    ## Getter for property: (@link FaceAnalysisDataRangeBuilder.NumberOfColorsOptions NXOpen.GeometricAnalysis.FaceAnalysisDataRangeBuilder.NumberOfColorsOptions@endlink) NumberOfColors
    ##  Returns the number of colors when color scale option is set to Automatic.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return FaceAnalysisDataRangeBuilder.NumberOfColorsOptions
    @property
    def NumberOfColors(self) -> FaceAnalysisDataRangeBuilder.NumberOfColorsOptions:
        """
        Getter for property: (@link FaceAnalysisDataRangeBuilder.NumberOfColorsOptions NXOpen.GeometricAnalysis.FaceAnalysisDataRangeBuilder.NumberOfColorsOptions@endlink) NumberOfColors
         Returns the number of colors when color scale option is set to Automatic.  
             
         
        """
        pass
    
    ## Setter for property: (@link FaceAnalysisDataRangeBuilder.NumberOfColorsOptions NXOpen.GeometricAnalysis.FaceAnalysisDataRangeBuilder.NumberOfColorsOptions@endlink) NumberOfColors

    ##  Returns the number of colors when color scale option is set to Automatic.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @NumberOfColors.setter
    def NumberOfColors(self, numberOfColors: FaceAnalysisDataRangeBuilder.NumberOfColorsOptions):
        """
        Setter for property: (@link FaceAnalysisDataRangeBuilder.NumberOfColorsOptions NXOpen.GeometricAnalysis.FaceAnalysisDataRangeBuilder.NumberOfColorsOptions@endlink) NumberOfColors
         Returns the number of colors when color scale option is set to Automatic.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.UserDefinedColorScaleData NXOpen.GeometricUtilities.UserDefinedColorScaleData@endlink) UserDefinedColorScale
    ##  Returns the User Defined Color Scale.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.UserDefinedColorScaleData
    @property
    def UserDefinedColorScale(self) -> NXOpen.GeometricUtilities.UserDefinedColorScaleData:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.UserDefinedColorScaleData NXOpen.GeometricUtilities.UserDefinedColorScaleData@endlink) UserDefinedColorScale
         Returns the User Defined Color Scale.  
             
         
        """
        pass
    
    ## Getter for property: (float) ZoomScale
    ##  Returns the zoom scale.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return float
    @property
    def ZoomScale(self) -> float:
        """
        Getter for property: (float) ZoomScale
         Returns the zoom scale.  
             
         
        """
        pass
    
    ## Setter for property: (float) ZoomScale

    ##  Returns the zoom scale.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @ZoomScale.setter
    def ZoomScale(self, scaleSlider: float):
        """
        Setter for property: (float) ZoomScale
         Returns the zoom scale.  
             
         
        """
        pass
    
    ##  Resets data range. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def ResetData(self) -> None:
        """
         Resets data range. 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a set of display settings used by Face Analysis. 
## 
##   <br>  Created in NX11.0.0  <br> 

class FaceAnalysisDisplayBuilder(NXOpen.TaggedObject): 
    """ Represents a set of display settings used by Face Analysis. """


    ##  Represents color legend type in display. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Blend</term><description> 
    ##  Blended color display. </description> </item><item><term> 
    ## Sharp</term><description> 
    ##  Sharp color display. </description> </item></list>
    class ColorLegendOptions(Enum):
        """
        Members Include: <Blend> <Sharp>
        """
        Blend: int
        Sharp: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FaceAnalysisDisplayBuilder.ColorLegendOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The option indicating number of colors to be used for display. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Two</term><description> 
    ##  Display in 2  colors. </description> </item><item><term> 
    ## Three</term><description> 
    ##  Display in 3  colors. </description> </item><item><term> 
    ## Four</term><description> 
    ##  Display in 4  colors. </description> </item><item><term> 
    ## Five</term><description> 
    ##  Display in 5  colors. </description> </item><item><term> 
    ## Six</term><description> 
    ##  Display in 6  colors. </description> </item><item><term> 
    ## Seven</term><description> 
    ##  Display in 7  colors. </description> </item><item><term> 
    ## Eight</term><description> 
    ##  Display in 8  colors. </description> </item><item><term> 
    ## Nine</term><description> 
    ##  Display in 9  colors. </description> </item><item><term> 
    ## Ten</term><description> 
    ##  Display in 10 colors. </description> </item><item><term> 
    ## Eleven</term><description> 
    ##  Display in 11 colors. </description> </item><item><term> 
    ## Twelve</term><description> 
    ##  Display in 12 colors. </description> </item></list>
    class ColorsOptions(Enum):
        """
        Members Include: <Two> <Three> <Four> <Five> <Six> <Seven> <Eight> <Nine> <Ten> <Eleven> <Twelve>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FaceAnalysisDisplayBuilder.ColorsOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) CanShowFacet
    ##  Returns the flag indicating if facets should be shown.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def CanShowFacet(self) -> bool:
        """
        Getter for property: (bool) CanShowFacet
         Returns the flag indicating if facets should be shown.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CanShowFacet

    ##  Returns the flag indicating if facets should be shown.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @CanShowFacet.setter
    def CanShowFacet(self, canShowFacet: bool):
        """
        Setter for property: (bool) CanShowFacet
         Returns the flag indicating if facets should be shown.  
             
         
        """
        pass
    
    ## Getter for property: (@link FaceAnalysisDisplayBuilder.ColorLegendOptions NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilder.ColorLegendOptions@endlink) ColorLegendOption
    ##  Returns the color legend option.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return FaceAnalysisDisplayBuilder.ColorLegendOptions
    @property
    def ColorLegendOption(self) -> FaceAnalysisDisplayBuilder.ColorLegendOptions:
        """
        Getter for property: (@link FaceAnalysisDisplayBuilder.ColorLegendOptions NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilder.ColorLegendOptions@endlink) ColorLegendOption
         Returns the color legend option.  
             
         
        """
        pass
    
    ## Setter for property: (@link FaceAnalysisDisplayBuilder.ColorLegendOptions NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilder.ColorLegendOptions@endlink) ColorLegendOption

    ##  Returns the color legend option.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @ColorLegendOption.setter
    def ColorLegendOption(self, colorLegendOption: FaceAnalysisDisplayBuilder.ColorLegendOptions):
        """
        Setter for property: (@link FaceAnalysisDisplayBuilder.ColorLegendOptions NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilder.ColorLegendOptions@endlink) ColorLegendOption
         Returns the color legend option.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.DisplayResolutionBuilder NXOpen.GeometricUtilities.DisplayResolutionBuilder@endlink) DisplayResolution
    ##  Returns the display resolution.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.DisplayResolutionBuilder
    @property
    def DisplayResolution(self) -> NXOpen.GeometricUtilities.DisplayResolutionBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.DisplayResolutionBuilder NXOpen.GeometricUtilities.DisplayResolutionBuilder@endlink) DisplayResolution
         Returns the display resolution.  
             
         
        """
        pass
    
    ## Getter for property: (@link FaceAnalysisDisplayBuilder.ColorsOptions NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilder.ColorsOptions@endlink) NumberOfColors
    ##  Returns the number of colors.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return FaceAnalysisDisplayBuilder.ColorsOptions
    @property
    def NumberOfColors(self) -> FaceAnalysisDisplayBuilder.ColorsOptions:
        """
        Getter for property: (@link FaceAnalysisDisplayBuilder.ColorsOptions NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilder.ColorsOptions@endlink) NumberOfColors
         Returns the number of colors.  
             
         
        """
        pass
    
    ## Setter for property: (@link FaceAnalysisDisplayBuilder.ColorsOptions NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilder.ColorsOptions@endlink) NumberOfColors

    ##  Returns the number of colors.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @NumberOfColors.setter
    def NumberOfColors(self, numberOfColors: FaceAnalysisDisplayBuilder.ColorsOptions):
        """
        Setter for property: (@link FaceAnalysisDisplayBuilder.ColorsOptions NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilder.ColorsOptions@endlink) NumberOfColors
         Returns the number of colors.  
             
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents reverse normal functions used by Face Analysis. 
## 
##   <br>  Created in NX11.0.0  <br> 

class FaceAnalysisNormalsBuilder(NXOpen.TaggedObject): 
    """ Represents reverse normal functions used by Face Analysis. """


    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) FaceToReverseNormal
    ##  Returns the face to reverse normal   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def FaceToReverseNormal(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) FaceToReverseNormal
         Returns the face to reverse normal   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point
    ##  Returns the point to redirect normals  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def Point(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point
         Returns the point to redirect normals  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point

    ##  Returns the point to redirect normals  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @Point.setter
    def Point(self, point: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point
         Returns the point to redirect normals  
            
         
        """
        pass
    
    ##  Restores all face normals. 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    def RestoreAll(self) -> None:
        """
         Restores all face normals. 
        """
        pass
    
##  Represents a face analysis   <br> To create or edit an instance of this class, use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder  NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder @endlink  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 
## 
##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::DistanceAnalysis NXOpen::GeometricAnalysis::DistanceAnalysis@endlink , @link NXOpen::GeometricAnalysis::RadiusAnalysis NXOpen::GeometricAnalysis::RadiusAnalysis@endlink , @link NXOpen::GeometricAnalysis::ReflectionAnalysis NXOpen::GeometricAnalysis::ReflectionAnalysis@endlink  Or @link NXOpen::GeometricAnalysis::SlopeAnalysis NXOpen::GeometricAnalysis::SlopeAnalysis@endlink  instead.  <br> 

class FaceAnalysis(AnalysisObject): 
    """ Represents a face analysis  """
    pass


import NXOpen
import NXOpen.GeometricUtilities
## 
##         Represents a @link NXOpen::GeometricAnalysis::FaceCurvatureAnalysisBuilder NXOpen::GeometricAnalysis::FaceCurvatureAnalysisBuilder@endlink  builder.
##         Use @link NXOpen::GeometricAnalysis::FaceCurvatureAnalysisBuilder NXOpen::GeometricAnalysis::FaceCurvatureAnalysisBuilder@endlink  to compute different
##         types of curvature analysis for selected faces.  The result of the curvature analysis is
##         displayed as color maps and contour lines on the faces.  For more details see the NX
##         documentation for Face Curvature Analysis.
##      <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisObjectCollection::CreateFaceCurvatureAnalysisBuilder  NXOpen::GeometricAnalysis::AnalysisObjectCollection::CreateFaceCurvatureAnalysisBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ContourRefinement </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ContourShift </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DisplayType </term> <description> 
##  
## Colormap </description> </item> 
## 
## <item><term> 
##  
## MapCenter </term> <description> 
##  
## 50 </description> </item> 
## 
## <item><term> 
##  
## MapRange </term> <description> 
##  
## 100 </description> </item> 
## 
## <item><term> 
##  
## NormalOption </term> <description> 
##  
## Manipulator </description> </item> 
## 
## <item><term> 
##  
## NumberOfContours </term> <description> 
##  
## 10 </description> </item> 
## 
## <item><term> 
##  
## Resolution.AngleTolerance </term> <description> 
##  
## 15.0 </description> </item> 
## 
## <item><term> 
##  
## Resolution.EdgeTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## Resolution.FaceTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## Resolution.Resolution </term> <description> 
##  
## Standard </description> </item> 
## 
## <item><term> 
##  
## Resolution.WidthTolerance </term> <description> 
##  
## 0.3 </description> </item> 
## 
## <item><term> 
##  
## SectionOption </term> <description> 
##  
## Manipulator </description> </item> 
## 
## <item><term> 
##  
## ShowZeroContour </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX9.0.0  <br> 

class FaceCurvatureAnalysisBuilder(NXOpen.Builder): 
    """
        Represents a <ja_class>NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder</ja_class> builder.
        Use <ja_class>NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder</ja_class> to compute different
        types of curvature analysis for selected faces.  The result of the curvature analysis is
        displayed as color maps and contour lines on the faces.  For more details see the NX
        documentation for Face Curvature Analysis.
    """


    ##  Represents the face curvature types. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Gaussian</term><description> 
    ##  Gausssian </description> </item><item><term> 
    ## Absolute</term><description> 
    ##  Absolute </description> </item><item><term> 
    ## Minimum</term><description> 
    ##  Minimum </description> </item><item><term> 
    ## Maximum</term><description> 
    ##  Maximum </description> </item><item><term> 
    ## Mean</term><description> 
    ##  Mean </description> </item><item><term> 
    ## Normal</term><description> 
    ##  Normal </description> </item><item><term> 
    ## Sectional</term><description> 
    ##  Sectional </description> </item><item><term> 
    ## U</term><description> 
    ##  U </description> </item><item><term> 
    ## V</term><description> 
    ##  V </description> </item><item><term> 
    ## Radius</term><description> 
    ##  Minimum radius </description> </item></list>
    class CurvatureTypes(Enum):
        """
        Members Include: <Gaussian> <Absolute> <Minimum> <Maximum> <Mean> <Normal> <Sectional> <U> <V> <Radius>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FaceCurvatureAnalysisBuilder.CurvatureTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Methods of specifiying the direction for normal and section curvatures.
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Primitive</term><description> 
    ##  vector or plane </description> </item><item><term> 
    ## Manipulator</term><description> 
    ##  orientation maninpulator </description> </item></list>
    class DirectionTypes(Enum):
        """
        Members Include: <Primitive> <Manipulator>
        """
        Primitive: int
        Manipulator: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FaceCurvatureAnalysisBuilder.DirectionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the display types. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Colormap</term><description> 
    ##  Color Map only </description> </item><item><term> 
    ## Contours</term><description> 
    ##  Contours </description> </item><item><term> 
    ## ColormapAndContours</term><description> 
    ##  Color Map and Contours </description> </item></list>
    class DisplayTypes(Enum):
        """
        Members Include: <Colormap> <Contours> <ColormapAndContours>
        """
        Colormap: int
        Contours: int
        ColormapAndContours: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FaceCurvatureAnalysisBuilder.DisplayTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the scaling types for curvature values.
    ##          
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Linear</term><description> 
    ##  Linear Scaling (No Scaling) </description> </item><item><term> 
    ## Log</term><description> 
    ##  Log Scaling </description> </item><item><term> 
    ## Area</term><description> 
    ##  Equalized by Area </description> </item></list>
    class ScaleTypes(Enum):
        """
        Members Include: <Linear> <Log> <Area>
        """
        Linear: int
        Log: int
        Area: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FaceCurvatureAnalysisBuilder.ScaleTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (int) ContourRefinement
    ##  Returns the contour refinement level, in the range 0-6.  
    ##    Increasing values compute more detailed and
    ##             accurate contour lines on the face.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def ContourRefinement(self) -> int:
        """
        Getter for property: (int) ContourRefinement
         Returns the contour refinement level, in the range 0-6.  
           Increasing values compute more detailed and
                    accurate contour lines on the face.   
         
        """
        pass
    
    ## Setter for property: (int) ContourRefinement

    ##  Returns the contour refinement level, in the range 0-6.  
    ##    Increasing values compute more detailed and
    ##             accurate contour lines on the face.   
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ContourRefinement.setter
    def ContourRefinement(self, contourRefinement: int):
        """
        Setter for property: (int) ContourRefinement
         Returns the contour refinement level, in the range 0-6.  
           Increasing values compute more detailed and
                    accurate contour lines on the face.   
         
        """
        pass
    
    ## Getter for property: (float) ContourShift
    ##  Returns the starting contour shift or bias value, as % of the standard contour interval.  
    ##    Valid values are -100 to 100.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def ContourShift(self) -> float:
        """
        Getter for property: (float) ContourShift
         Returns the starting contour shift or bias value, as % of the standard contour interval.  
           Valid values are -100 to 100.   
         
        """
        pass
    
    ## Setter for property: (float) ContourShift

    ##  Returns the starting contour shift or bias value, as % of the standard contour interval.  
    ##    Valid values are -100 to 100.   
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ContourShift.setter
    def ContourShift(self, contourShift: float):
        """
        Setter for property: (float) ContourShift
         Returns the starting contour shift or bias value, as % of the standard contour interval.  
           Valid values are -100 to 100.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) CurvatureSectionPlane
    ##  Returns the section curvature plane when sectional curvature values are to be computed and displayed.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Plane
    @property
    def CurvatureSectionPlane(self) -> NXOpen.Plane:
        """
        Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) CurvatureSectionPlane
         Returns the section curvature plane when sectional curvature values are to be computed and displayed.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) CurvatureSectionPlane

    ##  Returns the section curvature plane when sectional curvature values are to be computed and displayed.  
    ##      
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @CurvatureSectionPlane.setter
    def CurvatureSectionPlane(self, curvatureSectionPlane: NXOpen.Plane):
        """
        Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) CurvatureSectionPlane
         Returns the section curvature plane when sectional curvature values are to be computed and displayed.  
             
         
        """
        pass
    
    ## Getter for property: (@link FaceCurvatureAnalysisBuilder.CurvatureTypes NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder.CurvatureTypes@endlink) CurvatureType
    ##  Returns the curvature type to compute and display.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return FaceCurvatureAnalysisBuilder.CurvatureTypes
    @property
    def CurvatureType(self) -> FaceCurvatureAnalysisBuilder.CurvatureTypes:
        """
        Getter for property: (@link FaceCurvatureAnalysisBuilder.CurvatureTypes NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder.CurvatureTypes@endlink) CurvatureType
         Returns the curvature type to compute and display.  
            
         
        """
        pass
    
    ## Setter for property: (@link FaceCurvatureAnalysisBuilder.CurvatureTypes NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder.CurvatureTypes@endlink) CurvatureType

    ##  Returns the curvature type to compute and display.  
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @CurvatureType.setter
    def CurvatureType(self, curvatureType: FaceCurvatureAnalysisBuilder.CurvatureTypes):
        """
        Setter for property: (@link FaceCurvatureAnalysisBuilder.CurvatureTypes NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder.CurvatureTypes@endlink) CurvatureType
         Returns the curvature type to compute and display.  
            
         
        """
        pass
    
    ## Getter for property: (@link FaceCurvatureAnalysisBuilder.DisplayTypes NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder.DisplayTypes@endlink) DisplayType
    ##  Returns the display type for curvature values.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return FaceCurvatureAnalysisBuilder.DisplayTypes
    @property
    def DisplayType(self) -> FaceCurvatureAnalysisBuilder.DisplayTypes:
        """
        Getter for property: (@link FaceCurvatureAnalysisBuilder.DisplayTypes NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder.DisplayTypes@endlink) DisplayType
         Returns the display type for curvature values.  
              
         
        """
        pass
    
    ## Setter for property: (@link FaceCurvatureAnalysisBuilder.DisplayTypes NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder.DisplayTypes@endlink) DisplayType

    ##  Returns the display type for curvature values.  
    ##       
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @DisplayType.setter
    def DisplayType(self, displayType: FaceCurvatureAnalysisBuilder.DisplayTypes):
        """
        Setter for property: (@link FaceCurvatureAnalysisBuilder.DisplayTypes NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder.DisplayTypes@endlink) DisplayType
         Returns the display type for curvature values.  
              
         
        """
        pass
    
    ## Getter for property: (float) MapCenter
    ##  Returns the center point of the color mapping and contouring, as % of the full range of
    ##             curvature values present in the data.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def MapCenter(self) -> float:
        """
        Getter for property: (float) MapCenter
         Returns the center point of the color mapping and contouring, as % of the full range of
                    curvature values present in the data.  
          
                  
         
        """
        pass
    
    ## Setter for property: (float) MapCenter

    ##  Returns the center point of the color mapping and contouring, as % of the full range of
    ##             curvature values present in the data.  
    ##   
    ##           
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @MapCenter.setter
    def MapCenter(self, mapCenter: float):
        """
        Setter for property: (float) MapCenter
         Returns the center point of the color mapping and contouring, as % of the full range of
                    curvature values present in the data.  
          
                  
         
        """
        pass
    
    ## Getter for property: (float) MapRange
    ##  Returns the color map and contour range, as % of the full range of curvature values present in the data.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def MapRange(self) -> float:
        """
        Getter for property: (float) MapRange
         Returns the color map and contour range, as % of the full range of curvature values present in the data.  
             
         
        """
        pass
    
    ## Setter for property: (float) MapRange

    ##  Returns the color map and contour range, as % of the full range of curvature values present in the data.  
    ##      
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @MapRange.setter
    def MapRange(self, mapRange: float):
        """
        Setter for property: (float) MapRange
         Returns the color map and contour range, as % of the full range of curvature values present in the data.  
             
         
        """
        pass
    
    ## Getter for property: (@link FaceCurvatureAnalysisBuilder.DirectionTypes NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder.DirectionTypes@endlink) NormalOption
    ##  Returns the normal for the case of normal curvature type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return FaceCurvatureAnalysisBuilder.DirectionTypes
    @property
    def NormalOption(self) -> FaceCurvatureAnalysisBuilder.DirectionTypes:
        """
        Getter for property: (@link FaceCurvatureAnalysisBuilder.DirectionTypes NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder.DirectionTypes@endlink) NormalOption
         Returns the normal for the case of normal curvature type.  
             
         
        """
        pass
    
    ## Setter for property: (@link FaceCurvatureAnalysisBuilder.DirectionTypes NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder.DirectionTypes@endlink) NormalOption

    ##  Returns the normal for the case of normal curvature type.  
    ##      
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @NormalOption.setter
    def NormalOption(self, normalOption: FaceCurvatureAnalysisBuilder.DirectionTypes):
        """
        Setter for property: (@link FaceCurvatureAnalysisBuilder.DirectionTypes NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder.DirectionTypes@endlink) NormalOption
         Returns the normal for the case of normal curvature type.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) NormalOrientation
    ##  Returns the normal orientation when the normal curvature values are to be computed and displayed.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Matrix3x3
    @property
    def NormalOrientation(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) NormalOrientation
         Returns the normal orientation when the normal curvature values are to be computed and displayed.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) NormalOrientation

    ##  Returns the normal orientation when the normal curvature values are to be computed and displayed.  
    ##      
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @NormalOrientation.setter
    def NormalOrientation(self, normalOrientation: NXOpen.Matrix3x3):
        """
        Setter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) NormalOrientation
         Returns the normal orientation when the normal curvature values are to be computed and displayed.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) NormalOrigin
    ##  Returns the normal origin when normal curvature values are to be computed and displayed.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def NormalOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) NormalOrigin
         Returns the normal origin when normal curvature values are to be computed and displayed.  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) NormalOrigin

    ##  Returns the normal origin when normal curvature values are to be computed and displayed.  
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @NormalOrigin.setter
    def NormalOrigin(self, normalOrigin: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) NormalOrigin
         Returns the normal origin when normal curvature values are to be computed and displayed.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) NormalVector
    ##  Returns the normal vector for the case when normal curvature values are to be computed and displayed.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def NormalVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) NormalVector
         Returns the normal vector for the case when normal curvature values are to be computed and displayed.  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) NormalVector

    ##  Returns the normal vector for the case when normal curvature values are to be computed and displayed.  
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @NormalVector.setter
    def NormalVector(self, normalVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) NormalVector
         Returns the normal vector for the case when normal curvature values are to be computed and displayed.  
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfContours
    ##  Returns the number of contour lines to compute and display.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def NumberOfContours(self) -> int:
        """
        Getter for property: (int) NumberOfContours
         Returns the number of contour lines to compute and display.  
             
         
        """
        pass
    
    ## Setter for property: (int) NumberOfContours

    ##  Returns the number of contour lines to compute and display.  
    ##      
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @NumberOfContours.setter
    def NumberOfContours(self, numberOfContours: int):
        """
        Setter for property: (int) NumberOfContours
         Returns the number of contour lines to compute and display.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.DisplayResolutionBuilder NXOpen.GeometricUtilities.DisplayResolutionBuilder@endlink) Resolution
    ##  Returns the tesselation resolution to use for curvature color map and contours.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.DisplayResolutionBuilder
    @property
    def Resolution(self) -> NXOpen.GeometricUtilities.DisplayResolutionBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.DisplayResolutionBuilder NXOpen.GeometricUtilities.DisplayResolutionBuilder@endlink) Resolution
         Returns the tesselation resolution to use for curvature color map and contours.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) ReverseIndividual
    ##  Returns the individual face normal.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObject
    @property
    def ReverseIndividual(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) ReverseIndividual
         Returns the individual face normal.  
             
         
        """
        pass
    
    ## Getter for property: (@link FaceCurvatureAnalysisBuilder.ScaleTypes NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder.ScaleTypes@endlink) ScaleType
    ##  Returns the scaling type of curvature values.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return FaceCurvatureAnalysisBuilder.ScaleTypes
    @property
    def ScaleType(self) -> FaceCurvatureAnalysisBuilder.ScaleTypes:
        """
        Getter for property: (@link FaceCurvatureAnalysisBuilder.ScaleTypes NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder.ScaleTypes@endlink) ScaleType
         Returns the scaling type of curvature values.  
             
         
        """
        pass
    
    ## Setter for property: (@link FaceCurvatureAnalysisBuilder.ScaleTypes NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder.ScaleTypes@endlink) ScaleType

    ##  Returns the scaling type of curvature values.  
    ##      
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ScaleType.setter
    def ScaleType(self, scaleType: FaceCurvatureAnalysisBuilder.ScaleTypes):
        """
        Setter for property: (@link FaceCurvatureAnalysisBuilder.ScaleTypes NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder.ScaleTypes@endlink) ScaleType
         Returns the scaling type of curvature values.  
             
         
        """
        pass
    
    ## Getter for property: (@link FaceCurvatureAnalysisBuilder.DirectionTypes NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder.DirectionTypes@endlink) SectionOption
    ##  Returns whether to use a section plane or maninpulator for sectional curvatures.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return FaceCurvatureAnalysisBuilder.DirectionTypes
    @property
    def SectionOption(self) -> FaceCurvatureAnalysisBuilder.DirectionTypes:
        """
        Getter for property: (@link FaceCurvatureAnalysisBuilder.DirectionTypes NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder.DirectionTypes@endlink) SectionOption
         Returns whether to use a section plane or maninpulator for sectional curvatures.  
             
         
        """
        pass
    
    ## Setter for property: (@link FaceCurvatureAnalysisBuilder.DirectionTypes NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder.DirectionTypes@endlink) SectionOption

    ##  Returns whether to use a section plane or maninpulator for sectional curvatures.  
    ##      
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @SectionOption.setter
    def SectionOption(self, sectionOption: FaceCurvatureAnalysisBuilder.DirectionTypes):
        """
        Setter for property: (@link FaceCurvatureAnalysisBuilder.DirectionTypes NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder.DirectionTypes@endlink) SectionOption
         Returns whether to use a section plane or maninpulator for sectional curvatures.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) SectionOrientation
    ##  Returns the section orientation for sectional curvatures.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Matrix3x3
    @property
    def SectionOrientation(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) SectionOrientation
         Returns the section orientation for sectional curvatures.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) SectionOrientation

    ##  Returns the section orientation for sectional curvatures.  
    ##      
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @SectionOrientation.setter
    def SectionOrientation(self, sectionOrientation: NXOpen.Matrix3x3):
        """
        Setter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) SectionOrientation
         Returns the section orientation for sectional curvatures.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) SectionOrigin
    ##  Returns the section origin for sectional curvatures.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def SectionOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) SectionOrigin
         Returns the section origin for sectional curvatures.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) SectionOrigin

    ##  Returns the section origin for sectional curvatures.  
    ##      
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @SectionOrigin.setter
    def SectionOrigin(self, sectionOrigin: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) SectionOrigin
         Returns the section origin for sectional curvatures.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectObject
    ##  Returns the faces on which to perform curvature analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def SelectObject(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectObject
         Returns the faces on which to perform curvature analysis.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ShowZeroContour
    ##  Returns the option to show zero curvature contour line.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def ShowZeroContour(self) -> bool:
        """
        Getter for property: (bool) ShowZeroContour
         Returns the option to show zero curvature contour line.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ShowZeroContour

    ##  Returns the option to show zero curvature contour line.  
    ##      
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ShowZeroContour.setter
    def ShowZeroContour(self, showZeroContour: bool):
        """
        Setter for property: (bool) ShowZeroContour
         Returns the option to show zero curvature contour line.  
             
         
        """
        pass
    
    ##  Deselects faces 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="faces"> (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink) </param>
    def DeselectFaces(self, faces: List[NXOpen.DisplayableObject]) -> None:
        """
         Deselects faces 
        """
        pass
    
    ##  Reverses all normals. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    def ReverseAllNormals(self) -> None:
        """
         Reverses all normals. 
        """
        pass
    
    ##  Reverses an individual face normal. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="face"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink) </param>
    def ReverseIndividualNormal(self, face: NXOpen.DisplayableObject) -> None:
        """
         Reverses an individual face normal. 
        """
        pass
    
    ##  Updates reverse map. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    def UpdateReverseMap(self) -> None:
        """
         Updates reverse map. 
        """
        pass
    
##  Represents a Face Curvature Analysis builder  <br> To create or edit an instance of this class, use @link NXOpen::GeometricAnalysis::FaceCurvatureAnalysisBuilder  NXOpen::GeometricAnalysis::FaceCurvatureAnalysisBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.0.0  <br> 

class FaceCurvatureAnalysis(AnalysisObject): 
    """ Represents a Face Curvature Analysis builder """
    pass


import NXOpen
##  GapFlushnessBuilder class   <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisObjectCollection::CreateGapFlushnessBuilder  NXOpen::GeometricAnalysis::AnalysisObjectCollection::CreateGapFlushnessBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## SampleNumber </term> <description> 
##  
## 10 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX5.0.0  <br> 

class GapFlushnessBuilder(NXOpen.Builder): 
    """ GapFlushnessBuilder class  """


    ##  This enum represents Label Display Option type  
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## GapOnly</term><description> 
    ##  gap only</description> </item><item><term> 
    ## FlushnessOnly</term><description> 
    ##  flushness only</description> </item><item><term> 
    ## Both</term><description> 
    ##  both </description> </item></list>
    class DisplayOptions(Enum):
        """
        Members Include: <GapOnly> <FlushnessOnly> <Both>
        """
        GapOnly: int
        FlushnessOnly: int
        Both: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> GapFlushnessBuilder.DisplayOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum represents evaluation mode  
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Point</term><description> 
    ##  at point </description> </item><item><term> 
    ## CurveNumber</term><description> 
    ##  along curve and number  </description> </item><item><term> 
    ## Curve</term><description> 
    ##  along curve and distance</description> </item></list>
    class EvaluationModes(Enum):
        """
        Members Include: <Point> <CurveNumber> <Curve>
        """
        Point: int
        CurveNumber: int
        Curve: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> GapFlushnessBuilder.EvaluationModes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum represents the Gap and Flushness Analysis Object evaluation types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Absolute</term><description> 
    ##  absolute </description> </item><item><term> 
    ## Visual</term><description> 
    ##  visual   </description> </item></list>
    class EvaluationTypes(Enum):
        """
        Members Include: <Absolute> <Visual>
        """
        Absolute: int
        Visual: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> GapFlushnessBuilder.EvaluationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum represents panel type  
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Hem</term><description> 
    ##  type hem </description> </item><item><term> 
    ## Flange</term><description> 
    ##  type flange</description> </item><item><term> 
    ## Wall</term><description> 
    ##  type wall </description> </item></list>
    class PanelTypes(Enum):
        """
        Members Include: <Hem> <Flange> <Wall>
        """
        Hem: int
        Flange: int
        Wall: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> GapFlushnessBuilder.PanelTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum represents cross-section alignment type  
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Curve</term><description> 
    ##  curve</description> </item><item><term> 
    ## CurveView</term><description> 
    ##  curve in view</description> </item><item><term> 
    ## SpecifiedDirection</term><description> 
    ##  specified direction </description> </item></list>
    class SectionAlignments(Enum):
        """
        Members Include: <Curve> <CurveView> <SpecifiedDirection>
        """
        Curve: int
        CurveView: int
        SpecifiedDirection: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> GapFlushnessBuilder.SectionAlignments:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum represents Cross Section Curves Options  
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ContactCurve</term><description> 
    ##  use contact curve</description> </item><item><term> 
    ## UserDefined</term><description> 
    ##  use user defined curve </description> </item></list>
    class SectionCurveOptions(Enum):
        """
        Members Include: <ContactCurve> <UserDefined>
        """
        ContactCurve: int
        UserDefined: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> GapFlushnessBuilder.SectionCurveOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BasePanelFaces
    ##  Returns the Base Panel face selection      
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def BasePanelFaces(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BasePanelFaces
         Returns the Base Panel face selection      
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) BasePanelInnerContactCurves
    ##  Returns the Base Panel inner contact section   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def BasePanelInnerContactCurves(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) BasePanelInnerContactCurves
         Returns the Base Panel inner contact section   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) BasePanelOuterContactCurves
    ##  Returns the Base Panel outer contact section    
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def BasePanelOuterContactCurves(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) BasePanelOuterContactCurves
         Returns the Base Panel outer contact section    
            
         
        """
        pass
    
    ## Getter for property: (@link GapFlushnessBuilder.PanelTypes NXOpen.GeometricAnalysis.GapFlushnessBuilder.PanelTypes@endlink) BasePanelType
    ##  Returns the Base Panel type     
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return GapFlushnessBuilder.PanelTypes
    @property
    def BasePanelType(self) -> GapFlushnessBuilder.PanelTypes:
        """
        Getter for property: (@link GapFlushnessBuilder.PanelTypes NXOpen.GeometricAnalysis.GapFlushnessBuilder.PanelTypes@endlink) BasePanelType
         Returns the Base Panel type     
            
         
        """
        pass
    
    ## Setter for property: (@link GapFlushnessBuilder.PanelTypes NXOpen.GeometricAnalysis.GapFlushnessBuilder.PanelTypes@endlink) BasePanelType

    ##  Returns the Base Panel type     
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @BasePanelType.setter
    def BasePanelType(self, panel_type: GapFlushnessBuilder.PanelTypes):
        """
        Setter for property: (@link GapFlushnessBuilder.PanelTypes NXOpen.GeometricAnalysis.GapFlushnessBuilder.PanelTypes@endlink) BasePanelType
         Returns the Base Panel type     
            
         
        """
        pass
    
    ## Getter for property: (@link GapFlushnessBuilder.SectionCurveOptions NXOpen.GeometricAnalysis.GapFlushnessBuilder.SectionCurveOptions@endlink) CrossSectionCurveOption
    ##  Returns the cross section curve option       
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return GapFlushnessBuilder.SectionCurveOptions
    @property
    def CrossSectionCurveOption(self) -> GapFlushnessBuilder.SectionCurveOptions:
        """
        Getter for property: (@link GapFlushnessBuilder.SectionCurveOptions NXOpen.GeometricAnalysis.GapFlushnessBuilder.SectionCurveOptions@endlink) CrossSectionCurveOption
         Returns the cross section curve option       
            
         
        """
        pass
    
    ## Setter for property: (@link GapFlushnessBuilder.SectionCurveOptions NXOpen.GeometricAnalysis.GapFlushnessBuilder.SectionCurveOptions@endlink) CrossSectionCurveOption

    ##  Returns the cross section curve option       
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @CrossSectionCurveOption.setter
    def CrossSectionCurveOption(self, section_curve_option: GapFlushnessBuilder.SectionCurveOptions):
        """
        Setter for property: (@link GapFlushnessBuilder.SectionCurveOptions NXOpen.GeometricAnalysis.GapFlushnessBuilder.SectionCurveOptions@endlink) CrossSectionCurveOption
         Returns the cross section curve option       
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) CrossSectionCurves
    ##  Returns the Cross Section Curves   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def CrossSectionCurves(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) CrossSectionCurves
         Returns the Cross Section Curves   
            
         
        """
        pass
    
    ## Getter for property: (@link GapFlushnessBuilder.EvaluationModes NXOpen.GeometricAnalysis.GapFlushnessBuilder.EvaluationModes@endlink) EvaluationMode
    ##  Returns the evaluation Method      
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return GapFlushnessBuilder.EvaluationModes
    @property
    def EvaluationMode(self) -> GapFlushnessBuilder.EvaluationModes:
        """
        Getter for property: (@link GapFlushnessBuilder.EvaluationModes NXOpen.GeometricAnalysis.GapFlushnessBuilder.EvaluationModes@endlink) EvaluationMode
         Returns the evaluation Method      
            
         
        """
        pass
    
    ## Setter for property: (@link GapFlushnessBuilder.EvaluationModes NXOpen.GeometricAnalysis.GapFlushnessBuilder.EvaluationModes@endlink) EvaluationMode

    ##  Returns the evaluation Method      
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @EvaluationMode.setter
    def EvaluationMode(self, evaluation_mode: GapFlushnessBuilder.EvaluationModes):
        """
        Setter for property: (@link GapFlushnessBuilder.EvaluationModes NXOpen.GeometricAnalysis.GapFlushnessBuilder.EvaluationModes@endlink) EvaluationMode
         Returns the evaluation Method      
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) EvaluationPoint
    ##  Returns the evaluation point       
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def EvaluationPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) EvaluationPoint
         Returns the evaluation point       
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) EvaluationPoint

    ##  Returns the evaluation point       
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @EvaluationPoint.setter
    def EvaluationPoint(self, evaluationPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) EvaluationPoint
         Returns the evaluation point       
            
         
        """
        pass
    
    ## Getter for property: (@link GapFlushnessBuilder.EvaluationTypes NXOpen.GeometricAnalysis.GapFlushnessBuilder.EvaluationTypes@endlink) EvaluationType
    ##  Returns the evaluation type   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return GapFlushnessBuilder.EvaluationTypes
    @property
    def EvaluationType(self) -> GapFlushnessBuilder.EvaluationTypes:
        """
        Getter for property: (@link GapFlushnessBuilder.EvaluationTypes NXOpen.GeometricAnalysis.GapFlushnessBuilder.EvaluationTypes@endlink) EvaluationType
         Returns the evaluation type   
            
         
        """
        pass
    
    ## Setter for property: (@link GapFlushnessBuilder.EvaluationTypes NXOpen.GeometricAnalysis.GapFlushnessBuilder.EvaluationTypes@endlink) EvaluationType

    ##  Returns the evaluation type   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @EvaluationType.setter
    def EvaluationType(self, evaluation_type: GapFlushnessBuilder.EvaluationTypes):
        """
        Setter for property: (@link GapFlushnessBuilder.EvaluationTypes NXOpen.GeometricAnalysis.GapFlushnessBuilder.EvaluationTypes@endlink) EvaluationType
         Returns the evaluation type   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsNegativeToleranceLabelDisplayed
    ##  Returns the Label Display negative tolerance       
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def IsNegativeToleranceLabelDisplayed(self) -> bool:
        """
        Getter for property: (bool) IsNegativeToleranceLabelDisplayed
         Returns the Label Display negative tolerance       
            
         
        """
        pass
    
    ## Setter for property: (bool) IsNegativeToleranceLabelDisplayed

    ##  Returns the Label Display negative tolerance       
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @IsNegativeToleranceLabelDisplayed.setter
    def IsNegativeToleranceLabelDisplayed(self, showlabel_negative: bool):
        """
        Setter for property: (bool) IsNegativeToleranceLabelDisplayed
         Returns the Label Display negative tolerance       
            
         
        """
        pass
    
    ## Getter for property: (bool) IsNominalLabelDisplayed
    ##  Returns the Label Display Nominal       
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def IsNominalLabelDisplayed(self) -> bool:
        """
        Getter for property: (bool) IsNominalLabelDisplayed
         Returns the Label Display Nominal       
            
         
        """
        pass
    
    ## Setter for property: (bool) IsNominalLabelDisplayed

    ##  Returns the Label Display Nominal       
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @IsNominalLabelDisplayed.setter
    def IsNominalLabelDisplayed(self, showlabel_nominal: bool):
        """
        Setter for property: (bool) IsNominalLabelDisplayed
         Returns the Label Display Nominal       
            
         
        """
        pass
    
    ## Getter for property: (bool) IsPositiveToleranceLabelDisplayed
    ##  Returns the Label Display positive tolerance      
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def IsPositiveToleranceLabelDisplayed(self) -> bool:
        """
        Getter for property: (bool) IsPositiveToleranceLabelDisplayed
         Returns the Label Display positive tolerance      
            
         
        """
        pass
    
    ## Setter for property: (bool) IsPositiveToleranceLabelDisplayed

    ##  Returns the Label Display positive tolerance      
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @IsPositiveToleranceLabelDisplayed.setter
    def IsPositiveToleranceLabelDisplayed(self, showlabel_positive: bool):
        """
        Setter for property: (bool) IsPositiveToleranceLabelDisplayed
         Returns the Label Display positive tolerance      
            
         
        """
        pass
    
    ## Getter for property: (@link GapFlushnessBuilder.DisplayOptions NXOpen.GeometricAnalysis.GapFlushnessBuilder.DisplayOptions@endlink) LabelDisplayOption
    ##  Returns the display option type      
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return GapFlushnessBuilder.DisplayOptions
    @property
    def LabelDisplayOption(self) -> GapFlushnessBuilder.DisplayOptions:
        """
        Getter for property: (@link GapFlushnessBuilder.DisplayOptions NXOpen.GeometricAnalysis.GapFlushnessBuilder.DisplayOptions@endlink) LabelDisplayOption
         Returns the display option type      
            
         
        """
        pass
    
    ## Setter for property: (@link GapFlushnessBuilder.DisplayOptions NXOpen.GeometricAnalysis.GapFlushnessBuilder.DisplayOptions@endlink) LabelDisplayOption

    ##  Returns the display option type      
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @LabelDisplayOption.setter
    def LabelDisplayOption(self, display_option: GapFlushnessBuilder.DisplayOptions):
        """
        Setter for property: (@link GapFlushnessBuilder.DisplayOptions NXOpen.GeometricAnalysis.GapFlushnessBuilder.DisplayOptions@endlink) LabelDisplayOption
         Returns the display option type      
            
         
        """
        pass
    
    ## Getter for property: (float) NegativeFlushnessTolerance
    ##  Returns the negative tolerance for flushness        
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def NegativeFlushnessTolerance(self) -> float:
        """
        Getter for property: (float) NegativeFlushnessTolerance
         Returns the negative tolerance for flushness        
            
         
        """
        pass
    
    ## Setter for property: (float) NegativeFlushnessTolerance

    ##  Returns the negative tolerance for flushness        
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @NegativeFlushnessTolerance.setter
    def NegativeFlushnessTolerance(self, negativeTolFlush: float):
        """
        Setter for property: (float) NegativeFlushnessTolerance
         Returns the negative tolerance for flushness        
            
         
        """
        pass
    
    ## Getter for property: (float) NegativeGapTolerance
    ##  Returns the negative tolerance for gap       
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def NegativeGapTolerance(self) -> float:
        """
        Getter for property: (float) NegativeGapTolerance
         Returns the negative tolerance for gap       
            
         
        """
        pass
    
    ## Setter for property: (float) NegativeGapTolerance

    ##  Returns the negative tolerance for gap       
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @NegativeGapTolerance.setter
    def NegativeGapTolerance(self, negativeTolGap: float):
        """
        Setter for property: (float) NegativeGapTolerance
         Returns the negative tolerance for gap       
            
         
        """
        pass
    
    ## Getter for property: (float) NominalFlushness
    ##  Returns the nominal value  for flushness        
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def NominalFlushness(self) -> float:
        """
        Getter for property: (float) NominalFlushness
         Returns the nominal value  for flushness        
            
         
        """
        pass
    
    ## Setter for property: (float) NominalFlushness

    ##  Returns the nominal value  for flushness        
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @NominalFlushness.setter
    def NominalFlushness(self, nominalFlush: float):
        """
        Setter for property: (float) NominalFlushness
         Returns the nominal value  for flushness        
            
         
        """
        pass
    
    ## Getter for property: (float) NominalGap
    ##  Returns the nominal value  for gap         
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def NominalGap(self) -> float:
        """
        Getter for property: (float) NominalGap
         Returns the nominal value  for gap         
            
         
        """
        pass
    
    ## Setter for property: (float) NominalGap

    ##  Returns the nominal value  for gap         
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @NominalGap.setter
    def NominalGap(self, nominalGap: float):
        """
        Setter for property: (float) NominalGap
         Returns the nominal value  for gap         
            
         
        """
        pass
    
    ## Getter for property: (float) PositiveFlushnessTolerance
    ##  Returns the positive tolerance for flushness    
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def PositiveFlushnessTolerance(self) -> float:
        """
        Getter for property: (float) PositiveFlushnessTolerance
         Returns the positive tolerance for flushness    
            
         
        """
        pass
    
    ## Setter for property: (float) PositiveFlushnessTolerance

    ##  Returns the positive tolerance for flushness    
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @PositiveFlushnessTolerance.setter
    def PositiveFlushnessTolerance(self, positiveTolFlush: float):
        """
        Setter for property: (float) PositiveFlushnessTolerance
         Returns the positive tolerance for flushness    
            
         
        """
        pass
    
    ## Getter for property: (float) PositiveGapTolerance
    ##  Returns the positive tolerance for gap        
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def PositiveGapTolerance(self) -> float:
        """
        Getter for property: (float) PositiveGapTolerance
         Returns the positive tolerance for gap        
            
         
        """
        pass
    
    ## Setter for property: (float) PositiveGapTolerance

    ##  Returns the positive tolerance for gap        
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @PositiveGapTolerance.setter
    def PositiveGapTolerance(self, positiveTolGap: float):
        """
        Setter for property: (float) PositiveGapTolerance
         Returns the positive tolerance for gap        
            
         
        """
        pass
    
    ## Getter for property: (bool) PreviewOption
    ##  Returns the preview option   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def PreviewOption(self) -> bool:
        """
        Getter for property: (bool) PreviewOption
         Returns the preview option   
            
         
        """
        pass
    
    ## Setter for property: (bool) PreviewOption

    ##  Returns the preview option   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @PreviewOption.setter
    def PreviewOption(self, previewOption: bool):
        """
        Setter for property: (bool) PreviewOption
         Returns the preview option   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SampleDistance
    ##  Returns the Sample Distance        
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SampleDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SampleDistance
         Returns the Sample Distance        
            
         
        """
        pass
    
    ## Getter for property: (int) SampleNumber
    ##  Returns the sample number   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def SampleNumber(self) -> int:
        """
        Getter for property: (int) SampleNumber
         Returns the sample number   
            
         
        """
        pass
    
    ## Setter for property: (int) SampleNumber

    ##  Returns the sample number   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @SampleNumber.setter
    def SampleNumber(self, sampleNumber: int):
        """
        Setter for property: (int) SampleNumber
         Returns the sample number   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SecondPanelFaces
    ##  Returns the Second Panel face selection        
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def SecondPanelFaces(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SecondPanelFaces
         Returns the Second Panel face selection        
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) SecondPanelInnerContactCurves
    ##  Returns the Second Panel inner contact section    
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def SecondPanelInnerContactCurves(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) SecondPanelInnerContactCurves
         Returns the Second Panel inner contact section    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) SecondPanelOuterContactCurves
    ##  Returns the Second Panel outer contact section   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def SecondPanelOuterContactCurves(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) SecondPanelOuterContactCurves
         Returns the Second Panel outer contact section   
            
         
        """
        pass
    
    ## Getter for property: (@link GapFlushnessBuilder.PanelTypes NXOpen.GeometricAnalysis.GapFlushnessBuilder.PanelTypes@endlink) SecondPanelType
    ##  Returns the Second Panel type     
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return GapFlushnessBuilder.PanelTypes
    @property
    def SecondPanelType(self) -> GapFlushnessBuilder.PanelTypes:
        """
        Getter for property: (@link GapFlushnessBuilder.PanelTypes NXOpen.GeometricAnalysis.GapFlushnessBuilder.PanelTypes@endlink) SecondPanelType
         Returns the Second Panel type     
            
         
        """
        pass
    
    ## Setter for property: (@link GapFlushnessBuilder.PanelTypes NXOpen.GeometricAnalysis.GapFlushnessBuilder.PanelTypes@endlink) SecondPanelType

    ##  Returns the Second Panel type     
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @SecondPanelType.setter
    def SecondPanelType(self, panel_type: GapFlushnessBuilder.PanelTypes):
        """
        Setter for property: (@link GapFlushnessBuilder.PanelTypes NXOpen.GeometricAnalysis.GapFlushnessBuilder.PanelTypes@endlink) SecondPanelType
         Returns the Second Panel type     
            
         
        """
        pass
    
    ## Getter for property: (@link GapFlushnessBuilder.SectionAlignments NXOpen.GeometricAnalysis.GapFlushnessBuilder.SectionAlignments@endlink) SectionAlignment
    ##  Returns the Section Alignment       
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return GapFlushnessBuilder.SectionAlignments
    @property
    def SectionAlignment(self) -> GapFlushnessBuilder.SectionAlignments:
        """
        Getter for property: (@link GapFlushnessBuilder.SectionAlignments NXOpen.GeometricAnalysis.GapFlushnessBuilder.SectionAlignments@endlink) SectionAlignment
         Returns the Section Alignment       
            
         
        """
        pass
    
    ## Setter for property: (@link GapFlushnessBuilder.SectionAlignments NXOpen.GeometricAnalysis.GapFlushnessBuilder.SectionAlignments@endlink) SectionAlignment

    ##  Returns the Section Alignment       
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @SectionAlignment.setter
    def SectionAlignment(self, section_alignment: GapFlushnessBuilder.SectionAlignments):
        """
        Setter for property: (@link GapFlushnessBuilder.SectionAlignments NXOpen.GeometricAnalysis.GapFlushnessBuilder.SectionAlignments@endlink) SectionAlignment
         Returns the Section Alignment       
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SectionAlignmentDirection
    ##  Returns the section alignment vector       
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def SectionAlignmentDirection(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SectionAlignmentDirection
         Returns the section alignment vector       
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SectionAlignmentDirection

    ##  Returns the section alignment vector       
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @SectionAlignmentDirection.setter
    def SectionAlignmentDirection(self, sectionAlignmentDirection: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SectionAlignmentDirection
         Returns the section alignment vector       
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowOutRangeLabels
    ##  Returns the show out of range labels   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def ShowOutRangeLabels(self) -> bool:
        """
        Getter for property: (bool) ShowOutRangeLabels
         Returns the show out of range labels   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowOutRangeLabels

    ##  Returns the show out of range labels   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ShowOutRangeLabels.setter
    def ShowOutRangeLabels(self, showOutRangeLabels: bool):
        """
        Setter for property: (bool) ShowOutRangeLabels
         Returns the show out of range labels   
            
         
        """
        pass
    
##  Gap and Flushness analysis object class  <br> To create or edit an instance of this class, use @link NXOpen::GeometricAnalysis::GapFlushnessBuilder  NXOpen::GeometricAnalysis::GapFlushnessBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class GapFlushness(AnalysisObject): 
    """ Gap and Flushness analysis object class """
    pass


import NXOpen
##  Represents the Geometric Properties class. This class can be used to
##       find local geometric properties of faces, edges, curves, CAE faces, and CAE
##       edges/curves at a given point.
##       <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisManager::CreateGeometricPropertiesObject  NXOpen::GeometricAnalysis::AnalysisManager::CreateGeometricPropertiesObject @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class GeometricProperties(NXOpen.Builder): 
    """ Represents the Geometric Properties class. This class can be used to
      find local geometric properties of faces, edges, curves, CAE faces, and CAE
      edges/curves at a given point.
     """


    ##  Type of input entity for geometric properties. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Face</term><description> 
    ##  Face </description> </item><item><term> 
    ## Edge</term><description> 
    ##  Either a modeling edge or a curve. </description> </item><item><term> 
    ## CaeFace</term><description> 
    ##  CAE Face </description> </item><item><term> 
    ## CaeCurve</term><description> 
    ##  CAE Curve </description> </item></list>
    class Entity(Enum):
        """
        Members Include: <Face> <Edge> <CaeFace> <CaeCurve>
        """
        Face: int
        Edge: int
        CaeFace: int
        CaeCurve: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> GeometricProperties.Entity:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents how to output geometric properties.
    ##              @link GeometricAnalysis::GeometricProperties::OutputTypeDynamic GeometricAnalysis::GeometricProperties::OutputTypeDynamic@endlink 
    ##              displays the properties of an entity under the cursor when NX is
    ##              run interactively. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Dynamic</term><description> 
    ##  Properties of an entity are displayed first on the dialog
    ##                                                               itself on mouse over. These properties are listed on in the
    ##                                                               information window upon selection of a point. </description> </item><item><term> 
    ## Static</term><description> 
    ##  Propeties of the selected entities are displayed in the
    ##                                                             information window. </description> </item></list>
    class OutputType(Enum):
        """
        Members Include: <Dynamic> <Static>
        """
        Dynamic: int
        Static: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> GeometricProperties.OutputType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Status of computing geometric properties. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Success</term><description> 
    ##  Success </description> </item><item><term> 
    ## InvalidInput</term><description> 
    ##  Input specified is not
    ##                                                                valid.</description> </item><item><term> 
    ## Failed</term><description> 
    ##  Failed to find all geometric
    ##                                                          properties</description> </item></list>
    class Status(Enum):
        """
        Members Include: <Success> <InvalidInput> <Failed>
        """
        Success: int
        InvalidInput: int
        Failed: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> GeometricProperties.Status:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  CAE Edge/Curve Geometric Properties 
    ## @link GeometricPropertiesCaeCurve_Struct NXOpen.GeometricAnalysis.GeometricPropertiesCaeCurve_Struct@endlink is an alias for @link GeometricProperties.CaeCurve NXOpen.GeometricAnalysis.GeometricProperties.CaeCurve@endlink.
    class CaeCurve:
        """
         CAE Edge/Curve Geometric Properties 
        @link GeometricPropertiesCaeCurve_Struct NXOpen.GeometricAnalysis.GeometricPropertiesCaeCurve_Struct@endlink is an alias for @link GeometricProperties.CaeCurve NXOpen.GeometricAnalysis.GeometricProperties.CaeCurve@endlink.
        """
        ## Getter for property :(float) ArcLengthParameter
        ## ArcLength parametrization
        ## @return float
        @property
        def ArcLengthParameter(self) -> float:
            """
            Getter for property ArcLengthParameter
            ArcLength parametrization

            """
            pass
        
        ## Setter for property :(float) ArcLengthParameter
        @ArcLengthParameter.setter
        def ArcLengthParameter(self, value: float):
            """
            Getter for property ArcLengthParameter
            ArcLength parametrization
            Setter for property ArcLengthParameter
            ArcLength parametrization

            """
            pass
        
        ## Getter for property :(float) UnitArcLengthParameter
        ## UnitArcLength parametrization
        ## @return float
        @property
        def UnitArcLengthParameter(self) -> float:
            """
            Getter for property UnitArcLengthParameter
            UnitArcLength parametrization

            """
            pass
        
        ## Setter for property :(float) UnitArcLengthParameter
        @UnitArcLengthParameter.setter
        def UnitArcLengthParameter(self, value: float):
            """
            Getter for property UnitArcLengthParameter
            UnitArcLength parametrization
            Setter for property UnitArcLengthParameter
            UnitArcLength parametrization

            """
            pass
        
        ## Getter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) ClosestPointInWcs
        ## closest point on curve in Work Part Coordinates
        ## @return @link NXOpen.Point3d NXOpen.Point3d@endlink
        @property
        def ClosestPointInWcs(self) -> NXOpen.Point3d:
            """
            Getter for property ClosestPointInWcs
            closest point on curve in Work Part Coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) ClosestPointInWcs
        @ClosestPointInWcs.setter
        def ClosestPointInWcs(self, value: NXOpen.Point3d):
            """
            Getter for property ClosestPointInWcs
            closest point on curve in Work Part Coordinates
            Setter for property ClosestPointInWcs
            closest point on curve in Work Part Coordinates

            """
            pass
        
        ## Getter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) NormalInWcs
        ## normal of closest point in Work Part Coordinates
        ## @return @link NXOpen.Vector3d NXOpen.Vector3d@endlink
        @property
        def NormalInWcs(self) -> NXOpen.Vector3d:
            """
            Getter for property NormalInWcs
            normal of closest point in Work Part Coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) NormalInWcs
        @NormalInWcs.setter
        def NormalInWcs(self, value: NXOpen.Vector3d):
            """
            Getter for property NormalInWcs
            normal of closest point in Work Part Coordinates
            Setter for property NormalInWcs
            normal of closest point in Work Part Coordinates

            """
            pass
        
        ## Getter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) TangentInWcs
        ## tangent of closest point in Work Part Coordinates
        ## @return @link NXOpen.Vector3d NXOpen.Vector3d@endlink
        @property
        def TangentInWcs(self) -> NXOpen.Vector3d:
            """
            Getter for property TangentInWcs
            tangent of closest point in Work Part Coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) TangentInWcs
        @TangentInWcs.setter
        def TangentInWcs(self, value: NXOpen.Vector3d):
            """
            Getter for property TangentInWcs
            tangent of closest point in Work Part Coordinates
            Setter for property TangentInWcs
            tangent of closest point in Work Part Coordinates

            """
            pass
        
        ## Getter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) Tangent
        ## tangent of closest point in Root Part Coordinates
        ## @return @link NXOpen.Vector3d NXOpen.Vector3d@endlink
        @property
        def Tangent(self) -> NXOpen.Vector3d:
            """
            Getter for property Tangent
            tangent of closest point in Root Part Coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) Tangent
        @Tangent.setter
        def Tangent(self, value: NXOpen.Vector3d):
            """
            Getter for property Tangent
            tangent of closest point in Root Part Coordinates
            Setter for property Tangent
            tangent of closest point in Root Part Coordinates

            """
            pass
        
        ## Getter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) Normal
        ## normal of closest point in Root Part Coordinates
        ## @return @link NXOpen.Vector3d NXOpen.Vector3d@endlink
        @property
        def Normal(self) -> NXOpen.Vector3d:
            """
            Getter for property Normal
            normal of closest point in Root Part Coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) Normal
        @Normal.setter
        def Normal(self, value: NXOpen.Vector3d):
            """
            Getter for property Normal
            normal of closest point in Root Part Coordinates
            Setter for property Normal
            normal of closest point in Root Part Coordinates

            """
            pass
        
        ## Getter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) ClosestPoint
        ## closest point on curve in Root Part Coordinates
        ## @return @link NXOpen.Point3d NXOpen.Point3d@endlink
        @property
        def ClosestPoint(self) -> NXOpen.Point3d:
            """
            Getter for property ClosestPoint
            closest point on curve in Root Part Coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) ClosestPoint
        @ClosestPoint.setter
        def ClosestPoint(self, value: NXOpen.Point3d):
            """
            Getter for property ClosestPoint
            closest point on curve in Root Part Coordinates
            Setter for property ClosestPoint
            closest point on curve in Root Part Coordinates

            """
            pass
        
    
    
    ##  CAE Face Geometric Properties 
    ## @link GeometricPropertiesCaeFace_Struct NXOpen.GeometricAnalysis.GeometricPropertiesCaeFace_Struct@endlink is an alias for @link GeometricProperties.CaeFace NXOpen.GeometricAnalysis.GeometricProperties.CaeFace@endlink.
    class CaeFace:
        """
         CAE Face Geometric Properties 
        @link GeometricPropertiesCaeFace_Struct NXOpen.GeometricAnalysis.GeometricPropertiesCaeFace_Struct@endlink is an alias for @link GeometricProperties.CaeFace NXOpen.GeometricAnalysis.GeometricProperties.CaeFace@endlink.
        """
        ## Getter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) ClosestPoint
        ## closest point on face in Root Part Coordinates
        ## @return @link NXOpen.Vector3d NXOpen.Vector3d@endlink
        @property
        def ClosestPoint(self) -> NXOpen.Vector3d:
            """
            Getter for property ClosestPoint
            closest point on face in Root Part Coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) ClosestPoint
        @ClosestPoint.setter
        def ClosestPoint(self, value: NXOpen.Vector3d):
            """
            Getter for property ClosestPoint
            closest point on face in Root Part Coordinates
            Setter for property ClosestPoint
            closest point on face in Root Part Coordinates

            """
            pass
        
        ## Getter for property :(float) UParameter
        ## u parameter of the closest point in Root Part Coordinates
        ## @return float
        @property
        def UParameter(self) -> float:
            """
            Getter for property UParameter
            u parameter of the closest point in Root Part Coordinates

            """
            pass
        
        ## Setter for property :(float) UParameter
        @UParameter.setter
        def UParameter(self, value: float):
            """
            Getter for property UParameter
            u parameter of the closest point in Root Part Coordinates
            Setter for property UParameter
            u parameter of the closest point in Root Part Coordinates

            """
            pass
        
        ## Getter for property :(float) VParameter
        ## v parameter of the closest point in Root Part Coordinates
        ## @return float
        @property
        def VParameter(self) -> float:
            """
            Getter for property VParameter
            v parameter of the closest point in Root Part Coordinates

            """
            pass
        
        ## Setter for property :(float) VParameter
        @VParameter.setter
        def VParameter(self, value: float):
            """
            Getter for property VParameter
            v parameter of the closest point in Root Part Coordinates
            Setter for property VParameter
            v parameter of the closest point in Root Part Coordinates

            """
            pass
        
        ## Getter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) Normal
        ## normal at the closest point in Root Part Coordinates
        ## @return @link NXOpen.Vector3d NXOpen.Vector3d@endlink
        @property
        def Normal(self) -> NXOpen.Vector3d:
            """
            Getter for property Normal
            normal at the closest point in Root Part Coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) Normal
        @Normal.setter
        def Normal(self, value: NXOpen.Vector3d):
            """
            Getter for property Normal
            normal at the closest point in Root Part Coordinates
            Setter for property Normal
            normal at the closest point in Root Part Coordinates

            """
            pass
        
        ## Getter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) ClosestPointInWcs
        ## closest point in Work Part Coordinates
        ## @return @link NXOpen.Point3d NXOpen.Point3d@endlink
        @property
        def ClosestPointInWcs(self) -> NXOpen.Point3d:
            """
            Getter for property ClosestPointInWcs
            closest point in Work Part Coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) ClosestPointInWcs
        @ClosestPointInWcs.setter
        def ClosestPointInWcs(self, value: NXOpen.Point3d):
            """
            Getter for property ClosestPointInWcs
            closest point in Work Part Coordinates
            Setter for property ClosestPointInWcs
            closest point in Work Part Coordinates

            """
            pass
        
        ## Getter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) NormalInWcs
        ## normal in Work Part Coordinates
        ## @return @link NXOpen.Vector3d NXOpen.Vector3d@endlink
        @property
        def NormalInWcs(self) -> NXOpen.Vector3d:
            """
            Getter for property NormalInWcs
            normal in Work Part Coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) NormalInWcs
        @NormalInWcs.setter
        def NormalInWcs(self, value: NXOpen.Vector3d):
            """
            Getter for property NormalInWcs
            normal in Work Part Coordinates
            Setter for property NormalInWcs
            normal in Work Part Coordinates

            """
            pass
        
        ## Getter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) UDerivative
        ## Derivative in U, Root Part Coordinates
        ## @return @link NXOpen.Vector3d NXOpen.Vector3d@endlink
        @property
        def UDerivative(self) -> NXOpen.Vector3d:
            """
            Getter for property UDerivative
            Derivative in U, Root Part Coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) UDerivative
        @UDerivative.setter
        def UDerivative(self, value: NXOpen.Vector3d):
            """
            Getter for property UDerivative
            Derivative in U, Root Part Coordinates
            Setter for property UDerivative
            Derivative in U, Root Part Coordinates

            """
            pass
        
        ## Getter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) VDerivative
        ## Derivative in V, Root Part Coordinates
        ## @return @link NXOpen.Vector3d NXOpen.Vector3d@endlink
        @property
        def VDerivative(self) -> NXOpen.Vector3d:
            """
            Getter for property VDerivative
            Derivative in V, Root Part Coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) VDerivative
        @VDerivative.setter
        def VDerivative(self, value: NXOpen.Vector3d):
            """
            Getter for property VDerivative
            Derivative in V, Root Part Coordinates
            Setter for property VDerivative
            Derivative in V, Root Part Coordinates

            """
            pass
        
        ## Getter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) UDerivativeInWcs
        ## Derivative in U in Work Part Coordinates
        ## @return @link NXOpen.Vector3d NXOpen.Vector3d@endlink
        @property
        def UDerivativeInWcs(self) -> NXOpen.Vector3d:
            """
            Getter for property UDerivativeInWcs
            Derivative in U in Work Part Coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) UDerivativeInWcs
        @UDerivativeInWcs.setter
        def UDerivativeInWcs(self, value: NXOpen.Vector3d):
            """
            Getter for property UDerivativeInWcs
            Derivative in U in Work Part Coordinates
            Setter for property UDerivativeInWcs
            Derivative in U in Work Part Coordinates

            """
            pass
        
        ## Getter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) VDerivativeInWcs
        ## Derivative in V in Work Part Coordinates
        ## @return @link NXOpen.Vector3d NXOpen.Vector3d@endlink
        @property
        def VDerivativeInWcs(self) -> NXOpen.Vector3d:
            """
            Getter for property VDerivativeInWcs
            Derivative in V in Work Part Coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) VDerivativeInWcs
        @VDerivativeInWcs.setter
        def VDerivativeInWcs(self, value: NXOpen.Vector3d):
            """
            Getter for property VDerivativeInWcs
            Derivative in V in Work Part Coordinates
            Setter for property VDerivativeInWcs
            Derivative in V in Work Part Coordinates

            """
            pass
        
    
    
    ##  Edge/Curve Geometric Properties 
    ## @link GeometricPropertiesEdge_Struct NXOpen.GeometricAnalysis.GeometricPropertiesEdge_Struct@endlink is an alias for @link GeometricProperties.Edge NXOpen.GeometricAnalysis.GeometricProperties.Edge@endlink.
    class Edge:
        """
         Edge/Curve Geometric Properties 
        @link GeometricPropertiesEdge_Struct NXOpen.GeometricAnalysis.GeometricPropertiesEdge_Struct@endlink is an alias for @link GeometricProperties.Edge NXOpen.GeometricAnalysis.GeometricProperties.Edge@endlink.
        """
        ## Getter for property :(float) ParameterPercentage
        ## Curve Parameter Percentage
        ## @return float
        @property
        def ParameterPercentage(self) -> float:
            """
            Getter for property ParameterPercentage
            Curve Parameter Percentage

            """
            pass
        
        ## Setter for property :(float) ParameterPercentage
        @ParameterPercentage.setter
        def ParameterPercentage(self, value: float):
            """
            Getter for property ParameterPercentage
            Curve Parameter Percentage
            Setter for property ParameterPercentage
            Curve Parameter Percentage

            """
            pass
        
        ## Getter for property :(float) Parameter
        ## Curve Parameter
        ## @return float
        @property
        def Parameter(self) -> float:
            """
            Getter for property Parameter
            Curve Parameter

            """
            pass
        
        ## Setter for property :(float) Parameter
        @Parameter.setter
        def Parameter(self, value: float):
            """
            Getter for property Parameter
            Curve Parameter
            Setter for property Parameter
            Curve Parameter

            """
            pass
        
        ## Getter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) PositionInWcs
        ## XYZ Position in Work Part coordinates
        ## @return @link NXOpen.Point3d NXOpen.Point3d@endlink
        @property
        def PositionInWcs(self) -> NXOpen.Point3d:
            """
            Getter for property PositionInWcs
            XYZ Position in Work Part coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) PositionInWcs
        @PositionInWcs.setter
        def PositionInWcs(self, value: NXOpen.Point3d):
            """
            Getter for property PositionInWcs
            XYZ Position in Work Part coordinates
            Setter for property PositionInWcs
            XYZ Position in Work Part coordinates

            """
            pass
        
        ## Getter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) Position
        ## XYZ Position in Root Part coordinates
        ## @return @link NXOpen.Point3d NXOpen.Point3d@endlink
        @property
        def Position(self) -> NXOpen.Point3d:
            """
            Getter for property Position
            XYZ Position in Root Part coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) Position
        @Position.setter
        def Position(self, value: NXOpen.Point3d):
            """
            Getter for property Position
            XYZ Position in Root Part coordinates
            Setter for property Position
            XYZ Position in Root Part coordinates

            """
            pass
        
        ## Getter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) TangentInWcs
        ## Tangent Vector in Work Part coordinates
        ## @return @link NXOpen.Vector3d NXOpen.Vector3d@endlink
        @property
        def TangentInWcs(self) -> NXOpen.Vector3d:
            """
            Getter for property TangentInWcs
            Tangent Vector in Work Part coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) TangentInWcs
        @TangentInWcs.setter
        def TangentInWcs(self, value: NXOpen.Vector3d):
            """
            Getter for property TangentInWcs
            Tangent Vector in Work Part coordinates
            Setter for property TangentInWcs
            Tangent Vector in Work Part coordinates

            """
            pass
        
        ## Getter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) Tangent
        ## Tangent Vector in Root Part coordinates
        ## @return @link NXOpen.Vector3d NXOpen.Vector3d@endlink
        @property
        def Tangent(self) -> NXOpen.Vector3d:
            """
            Getter for property Tangent
            Tangent Vector in Root Part coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) Tangent
        @Tangent.setter
        def Tangent(self, value: NXOpen.Vector3d):
            """
            Getter for property Tangent
            Tangent Vector in Root Part coordinates
            Setter for property Tangent
            Tangent Vector in Root Part coordinates

            """
            pass
        
        ## Getter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) NormalInWcs
        ## Curve Normal in Work Part coordinates
        ## @return @link NXOpen.Vector3d NXOpen.Vector3d@endlink
        @property
        def NormalInWcs(self) -> NXOpen.Vector3d:
            """
            Getter for property NormalInWcs
            Curve Normal in Work Part coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) NormalInWcs
        @NormalInWcs.setter
        def NormalInWcs(self, value: NXOpen.Vector3d):
            """
            Getter for property NormalInWcs
            Curve Normal in Work Part coordinates
            Setter for property NormalInWcs
            Curve Normal in Work Part coordinates

            """
            pass
        
        ## Getter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) Normal
        ## Curve Normal in Root Part coordinates
        ## @return @link NXOpen.Vector3d NXOpen.Vector3d@endlink
        @property
        def Normal(self) -> NXOpen.Vector3d:
            """
            Getter for property Normal
            Curve Normal in Root Part coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) Normal
        @Normal.setter
        def Normal(self, value: NXOpen.Vector3d):
            """
            Getter for property Normal
            Curve Normal in Root Part coordinates
            Setter for property Normal
            Curve Normal in Root Part coordinates

            """
            pass
        
        ## Getter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) BinormalInWcs
        ## Curve Binormal in Work Part coordinates
        ## @return @link NXOpen.Vector3d NXOpen.Vector3d@endlink
        @property
        def BinormalInWcs(self) -> NXOpen.Vector3d:
            """
            Getter for property BinormalInWcs
            Curve Binormal in Work Part coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) BinormalInWcs
        @BinormalInWcs.setter
        def BinormalInWcs(self, value: NXOpen.Vector3d):
            """
            Getter for property BinormalInWcs
            Curve Binormal in Work Part coordinates
            Setter for property BinormalInWcs
            Curve Binormal in Work Part coordinates

            """
            pass
        
        ## Getter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) Binormal
        ## Curve Binormal in Root Part coordinates
        ## @return @link NXOpen.Vector3d NXOpen.Vector3d@endlink
        @property
        def Binormal(self) -> NXOpen.Vector3d:
            """
            Getter for property Binormal
            Curve Binormal in Root Part coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) Binormal
        @Binormal.setter
        def Binormal(self, value: NXOpen.Vector3d):
            """
            Getter for property Binormal
            Curve Binormal in Root Part coordinates
            Setter for property Binormal
            Curve Binormal in Root Part coordinates

            """
            pass
        
        ## Getter for property :(float) Torsion
        ## Curve Torsion
        ## @return float
        @property
        def Torsion(self) -> float:
            """
            Getter for property Torsion
            Curve Torsion

            """
            pass
        
        ## Setter for property :(float) Torsion
        @Torsion.setter
        def Torsion(self, value: float):
            """
            Getter for property Torsion
            Curve Torsion
            Setter for property Torsion
            Curve Torsion

            """
            pass
        
        ## Getter for property :(float) Curvature
        ## Curvature of the Curve
        ## @return float
        @property
        def Curvature(self) -> float:
            """
            Getter for property Curvature
            Curvature of the Curve

            """
            pass
        
        ## Setter for property :(float) Curvature
        @Curvature.setter
        def Curvature(self, value: float):
            """
            Getter for property Curvature
            Curvature of the Curve
            Setter for property Curvature
            Curvature of the Curve

            """
            pass
        
    
    
    ##  Face Geometric Properties 
    ## @link GeometricPropertiesFace_Struct NXOpen.GeometricAnalysis.GeometricPropertiesFace_Struct@endlink is an alias for @link GeometricProperties.Face NXOpen.GeometricAnalysis.GeometricProperties.Face@endlink.
    class Face:
        """
         Face Geometric Properties 
        @link GeometricPropertiesFace_Struct NXOpen.GeometricAnalysis.GeometricPropertiesFace_Struct@endlink is an alias for @link GeometricProperties.Face NXOpen.GeometricAnalysis.GeometricProperties.Face@endlink.
        """
        ## Getter for property :(float) UParamater
        ## U parameter
        ## @return float
        @property
        def UParamater(self) -> float:
            """
            Getter for property UParamater
            U parameter

            """
            pass
        
        ## Setter for property :(float) UParamater
        @UParamater.setter
        def UParamater(self, value: float):
            """
            Getter for property UParamater
            U parameter
            Setter for property UParamater
            U parameter

            """
            pass
        
        ## Getter for property :(float) VParamater
        ## V parameter
        ## @return float
        @property
        def VParamater(self) -> float:
            """
            Getter for property VParamater
            V parameter

            """
            pass
        
        ## Setter for property :(float) VParamater
        @VParamater.setter
        def VParamater(self, value: float):
            """
            Getter for property VParamater
            V parameter
            Setter for property VParamater
            V parameter

            """
            pass
        
        ## Getter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) PositionInWcs
        ## XYZ Position in Work Part coordinates
        ## @return @link NXOpen.Point3d NXOpen.Point3d@endlink
        @property
        def PositionInWcs(self) -> NXOpen.Point3d:
            """
            Getter for property PositionInWcs
            XYZ Position in Work Part coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) PositionInWcs
        @PositionInWcs.setter
        def PositionInWcs(self, value: NXOpen.Point3d):
            """
            Getter for property PositionInWcs
            XYZ Position in Work Part coordinates
            Setter for property PositionInWcs
            XYZ Position in Work Part coordinates

            """
            pass
        
        ## Getter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) UDerivativeInWcs
        ## Derivative Vector in U direction - Work Part  Coordinates
        ## @return @link NXOpen.Vector3d NXOpen.Vector3d@endlink
        @property
        def UDerivativeInWcs(self) -> NXOpen.Vector3d:
            """
            Getter for property UDerivativeInWcs
            Derivative Vector in U direction - Work Part  Coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) UDerivativeInWcs
        @UDerivativeInWcs.setter
        def UDerivativeInWcs(self, value: NXOpen.Vector3d):
            """
            Getter for property UDerivativeInWcs
            Derivative Vector in U direction - Work Part  Coordinates
            Setter for property UDerivativeInWcs
            Derivative Vector in U direction - Work Part  Coordinates

            """
            pass
        
        ## Getter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) VDerivativeInWcs
        ## Derivative Vector in V direction - Work Part  Coordinates
        ## @return @link NXOpen.Vector3d NXOpen.Vector3d@endlink
        @property
        def VDerivativeInWcs(self) -> NXOpen.Vector3d:
            """
            Getter for property VDerivativeInWcs
            Derivative Vector in V direction - Work Part  Coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) VDerivativeInWcs
        @VDerivativeInWcs.setter
        def VDerivativeInWcs(self, value: NXOpen.Vector3d):
            """
            Getter for property VDerivativeInWcs
            Derivative Vector in V direction - Work Part  Coordinates
            Setter for property VDerivativeInWcs
            Derivative Vector in V direction - Work Part  Coordinates

            """
            pass
        
        ## Getter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) NormalInWcs
        ## Unitized Face Normal - Work Part Coordinates
        ## @return @link NXOpen.Vector3d NXOpen.Vector3d@endlink
        @property
        def NormalInWcs(self) -> NXOpen.Vector3d:
            """
            Getter for property NormalInWcs
            Unitized Face Normal - Work Part Coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) NormalInWcs
        @NormalInWcs.setter
        def NormalInWcs(self, value: NXOpen.Vector3d):
            """
            Getter for property NormalInWcs
            Unitized Face Normal - Work Part Coordinates
            Setter for property NormalInWcs
            Unitized Face Normal - Work Part Coordinates

            """
            pass
        
        ## Getter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) Position
        ## XYZ Position
        ## @return @link NXOpen.Point3d NXOpen.Point3d@endlink
        @property
        def Position(self) -> NXOpen.Point3d:
            """
            Getter for property Position
            XYZ Position

            """
            pass
        
        ## Setter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) Position
        @Position.setter
        def Position(self, value: NXOpen.Point3d):
            """
            Getter for property Position
            XYZ Position
            Setter for property Position
            XYZ Position

            """
            pass
        
        ## Getter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) UDerivative
        ## Derivative Vector in U direction -  Root Part Coordinates
        ## @return @link NXOpen.Vector3d NXOpen.Vector3d@endlink
        @property
        def UDerivative(self) -> NXOpen.Vector3d:
            """
            Getter for property UDerivative
            Derivative Vector in U direction -  Root Part Coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) UDerivative
        @UDerivative.setter
        def UDerivative(self, value: NXOpen.Vector3d):
            """
            Getter for property UDerivative
            Derivative Vector in U direction -  Root Part Coordinates
            Setter for property UDerivative
            Derivative Vector in U direction -  Root Part Coordinates

            """
            pass
        
        ## Getter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) VDerivative
        ## Derivative Vector in V direction - Root Part  Coordinates
        ## @return @link NXOpen.Vector3d NXOpen.Vector3d@endlink
        @property
        def VDerivative(self) -> NXOpen.Vector3d:
            """
            Getter for property VDerivative
            Derivative Vector in V direction - Root Part  Coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) VDerivative
        @VDerivative.setter
        def VDerivative(self, value: NXOpen.Vector3d):
            """
            Getter for property VDerivative
            Derivative Vector in V direction - Root Part  Coordinates
            Setter for property VDerivative
            Derivative Vector in V direction - Root Part  Coordinates

            """
            pass
        
        ## Getter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) Normal
        ## Unitized Face Normal - Root Part Coordinates
        ## @return @link NXOpen.Vector3d NXOpen.Vector3d@endlink
        @property
        def Normal(self) -> NXOpen.Vector3d:
            """
            Getter for property Normal
            Unitized Face Normal - Root Part Coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Vector3d NXOpen.Vector3d@endlink) Normal
        @Normal.setter
        def Normal(self, value: NXOpen.Vector3d):
            """
            Getter for property Normal
            Unitized Face Normal - Root Part Coordinates
            Setter for property Normal
            Unitized Face Normal - Root Part Coordinates

            """
            pass
        
        ## Getter for property :(float) InvOfMinRadiusOfCurvature
        ## Inverse of Minumum  Radius of                                    Curvature, 1/(minimum radius of curvature)
        ## @return float
        @property
        def InvOfMinRadiusOfCurvature(self) -> float:
            """
            Getter for property InvOfMinRadiusOfCurvature
            Inverse of Minumum  Radius of                                    Curvature, 1/(minimum radius of curvature)

            """
            pass
        
        ## Setter for property :(float) InvOfMinRadiusOfCurvature
        @InvOfMinRadiusOfCurvature.setter
        def InvOfMinRadiusOfCurvature(self, value: float):
            """
            Getter for property InvOfMinRadiusOfCurvature
            Inverse of Minumum  Radius of                                    Curvature, 1/(minimum radius of curvature)
            Setter for property InvOfMinRadiusOfCurvature
            Inverse of Minumum  Radius of                                    Curvature, 1/(minimum radius of curvature)

            """
            pass
        
        ## Getter for property :(float) InvOfMaxRadiusOfCurvature
        ## Inverse of Maximum Radius of                                    Curvature,  1/(maximum radius of curvature).
        ## @return float
        @property
        def InvOfMaxRadiusOfCurvature(self) -> float:
            """
            Getter for property InvOfMaxRadiusOfCurvature
            Inverse of Maximum Radius of                                    Curvature,  1/(maximum radius of curvature).

            """
            pass
        
        ## Setter for property :(float) InvOfMaxRadiusOfCurvature
        @InvOfMaxRadiusOfCurvature.setter
        def InvOfMaxRadiusOfCurvature(self, value: float):
            """
            Getter for property InvOfMaxRadiusOfCurvature
            Inverse of Maximum Radius of                                    Curvature,  1/(maximum radius of curvature).
            Setter for property InvOfMaxRadiusOfCurvature
            Inverse of Maximum Radius of                                    Curvature,  1/(maximum radius of curvature).

            """
            pass
        
    
    
    ## Getter for property: (@link NXOpen.SelectObjectList NXOpen.SelectObjectList@endlink) ObjectsForAnalysis
    ##  Returns the Objects for analysis   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.SelectObjectList
    @property
    def ObjectsForAnalysis(self) -> NXOpen.SelectObjectList:
        """
        Getter for property: (@link NXOpen.SelectObjectList NXOpen.SelectObjectList@endlink) ObjectsForAnalysis
         Returns the Objects for analysis   
            
         
        """
        pass
    
    ## Getter for property: (@link GeometricProperties.OutputType NXOpen.GeometricAnalysis.GeometricProperties.OutputType@endlink) OutputMethod
    ##  Returns the output method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return GeometricProperties.OutputType
    @property
    def OutputMethod(self) -> GeometricProperties.OutputType:
        """
        Getter for property: (@link GeometricProperties.OutputType NXOpen.GeometricAnalysis.GeometricProperties.OutputType@endlink) OutputMethod
         Returns the output method   
            
         
        """
        pass
    
    ## Setter for property: (@link GeometricProperties.OutputType NXOpen.GeometricAnalysis.GeometricProperties.OutputType@endlink) OutputMethod

    ##  Returns the output method   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @OutputMethod.setter
    def OutputMethod(self, output_method: GeometricProperties.OutputType):
        """
        Setter for property: (@link GeometricProperties.OutputType NXOpen.GeometricAnalysis.GeometricProperties.OutputType@endlink) OutputMethod
         Returns the output method   
            
         
        """
        pass
    
    ##  Returns CAE curve local properties at the given point 
    ##  @return A tuple consisting of (status, caeCurve). 
    ##  - status is: @link GeometricProperties.Status NXOpen.GeometricAnalysis.GeometricProperties.Status@endlink. Return status .
    ##  - caeCurve is: @link GeometricProperties.CaeCurve NXOpen.GeometricAnalysis.GeometricProperties.CaeCurve@endlink. CAE Edge/Curve Properties .

    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="entityTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  NXObject to
    ##                                                              obtain the properties for </param>
    ## <param name="absPoint"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  Absolute point
    ##                                                             co-ordinates of the reference point 
    ##                                                             to compute the properties </param>
    def GetCaeCurveProperties(self, entityTag: NXOpen.NXObject, absPoint: NXOpen.Point3d) -> Tuple[GeometricProperties.Status, GeometricProperties.CaeCurve]:
        """
         Returns CAE curve local properties at the given point 
         @return A tuple consisting of (status, caeCurve). 
         - status is: @link GeometricProperties.Status NXOpen.GeometricAnalysis.GeometricProperties.Status@endlink. Return status .
         - caeCurve is: @link GeometricProperties.CaeCurve NXOpen.GeometricAnalysis.GeometricProperties.CaeCurve@endlink. CAE Edge/Curve Properties .

        """
        pass
    
    ##  Returns CAE face local properties at the given point 
    ##  @return A tuple consisting of (status, caeFace). 
    ##  - status is: @link GeometricProperties.Status NXOpen.GeometricAnalysis.GeometricProperties.Status@endlink. Return status .
    ##  - caeFace is: @link GeometricProperties.CaeFace NXOpen.GeometricAnalysis.GeometricProperties.CaeFace@endlink. CAE Face Properties .

    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="entityTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  NXObject to
    ##                                                              obtain the properties for </param>
    ## <param name="absPoint"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  Absolute point
    ##                                                             co-ordinates of the reference point 
    ##                                                             to compute the properties </param>
    def GetCaeFaceProperties(self, entityTag: NXOpen.NXObject, absPoint: NXOpen.Point3d) -> Tuple[GeometricProperties.Status, GeometricProperties.CaeFace]:
        """
         Returns CAE face local properties at the given point 
         @return A tuple consisting of (status, caeFace). 
         - status is: @link GeometricProperties.Status NXOpen.GeometricAnalysis.GeometricProperties.Status@endlink. Return status .
         - caeFace is: @link GeometricProperties.CaeFace NXOpen.GeometricAnalysis.GeometricProperties.CaeFace@endlink. CAE Face Properties .

        """
        pass
    
    ##  Returns edge/curve local properties at the given point 
    ##  @return A tuple consisting of (status, edge). 
    ##  - status is: @link GeometricProperties.Status NXOpen.GeometricAnalysis.GeometricProperties.Status@endlink. Return status .
    ##  - edge is: @link GeometricProperties.Edge NXOpen.GeometricAnalysis.GeometricProperties.Edge@endlink. Edge/Curve Properties .

    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="entityTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  NXObject to
    ##                                                              obtain the properties for </param>
    ## <param name="absPoint"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  Absolute point
    ##                                                             co-ordinates of the reference point 
    ##                                                             to compute the properties </param>
    def GetEdgeProperties(self, entityTag: NXOpen.NXObject, absPoint: NXOpen.Point3d) -> Tuple[GeometricProperties.Status, GeometricProperties.Edge]:
        """
         Returns edge/curve local properties at the given point 
         @return A tuple consisting of (status, edge). 
         - status is: @link GeometricProperties.Status NXOpen.GeometricAnalysis.GeometricProperties.Status@endlink. Return status .
         - edge is: @link GeometricProperties.Edge NXOpen.GeometricAnalysis.GeometricProperties.Edge@endlink. Edge/Curve Properties .

        """
        pass
    
    ##  Returns face local properties at the given point 
    ##  @return A tuple consisting of (status, face). 
    ##  - status is: @link GeometricProperties.Status NXOpen.GeometricAnalysis.GeometricProperties.Status@endlink. Return status .
    ##  - face is: @link GeometricProperties.Face NXOpen.GeometricAnalysis.GeometricProperties.Face@endlink. Face Properties .

    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="entityTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  NXObject to
    ##                                                              obtain the properties for </param>
    ## <param name="absPoint"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  Absolute point
    ##                                                             co-ordinates of the reference point 
    ##                                                             to compute the properties </param>
    def GetFaceProperties(self, entityTag: NXOpen.NXObject, absPoint: NXOpen.Point3d) -> Tuple[GeometricProperties.Status, GeometricProperties.Face]:
        """
         Returns face local properties at the given point 
         @return A tuple consisting of (status, face). 
         - status is: @link GeometricProperties.Status NXOpen.GeometricAnalysis.GeometricProperties.Status@endlink. Return status .
         - face is: @link GeometricProperties.Face NXOpen.GeometricAnalysis.GeometricProperties.Face@endlink. Face Properties .

        """
        pass
    
    ##  Displays the local properties of the specified object at the
    ##               given point in the listing window 
    ##  @return status (@link GeometricProperties.Status NXOpen.GeometricAnalysis.GeometricProperties.Status@endlink):  Return status .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="geometricPropertiesBuilder"> (@link GeometricProperties NXOpen.GeometricAnalysis.GeometricProperties@endlink) </param>
    ## <param name="entityTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  NXObject to
    ##                                                              obtain the properties for </param>
    ## <param name="absPoint"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  Absolute point
    ##                                                             co-ordinates of the reference point 
    ##                                                             to compute the properties </param>
    @overload
    def ListProperties(self, entityTag: NXOpen.NXObject, absPoint: NXOpen.Point3d) -> GeometricProperties.Status:
        """
         Displays the local properties of the specified object at the
                      given point in the listing window 
         @return status (@link GeometricProperties.Status NXOpen.GeometricAnalysis.GeometricProperties.Status@endlink):  Return status .
        """
        pass
    
    ##  Displays the local properties of
    ##                @link ObjectsForAnalysis ObjectsForAnalysis@endlink  at the given point in 
    ##                the listing window.  
    ##  @return status (@link GeometricProperties.Status NXOpen.GeometricAnalysis.GeometricProperties.Status@endlink):  Return status .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="geometricPropertiesBuilder"> (@link GeometricProperties NXOpen.GeometricAnalysis.GeometricProperties@endlink) </param>
    ## <param name="absPoint"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  Absolute point
    ##                                                             co-ordinates of the reference point 
    ##                                                             to compute the properties </param>
    @overload
    def ListProperties(self, absPoint: NXOpen.Point3d) -> GeometricProperties.Status:
        """
         Displays the local properties of
                       @link ObjectsForAnalysis ObjectsForAnalysis@endlink  at the given point in 
                       the listing window.  
         @return status (@link GeometricProperties.Status NXOpen.GeometricAnalysis.GeometricProperties.Status@endlink):  Return status .
        """
        pass
    
    ##  Clears all markers showing the local geometric properties in the graphics window 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def Reset(self) -> None:
        """
         Clears all markers showing the local geometric properties in the graphics window 
        """
        pass
    
import NXOpen
## 
##     Represents a
##     @link NXOpen::GeometricAnalysis::HighlightLinesAnalysis NXOpen::GeometricAnalysis::HighlightLinesAnalysis@endlink 
##     builder. Highlight Lines Analysis function can produce both reflection lines and projection
##     lines which are used to evaluate the surface quality and continuity between adjacent surfaces.
##      <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisObjectCollection::CreateHighlightLinesAnalysisBuilder  NXOpen::GeometricAnalysis::AnalysisObjectCollection::CreateHighlightLinesAnalysisBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## EndIsoAngle.Value </term> <description> 
##  
## 90 </description> </item> 
## 
## <item><term> 
##  
## LightNumber </term> <description> 
##  
## 10 </description> </item> 
## 
## <item><term> 
##  
## LightSpacing </term> <description> 
##  
## 50.0 (millimeters part), 2.0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Resolution </term> <description> 
##  
## Fine </description> </item> 
## 
## <item><term> 
##  
## StartIsoAngle.Value </term> <description> 
##  
## -90 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX6.0.0  <br> 

class HighlightLinesAnalysisBuilder(NXOpen.Builder): 
    """
    Represents a
    <ja_class>NXOpen.GeometricAnalysis.HighlightLinesAnalysis</ja_class>
    builder. Highlight Lines Analysis function can produce both reflection lines and projection
    lines which are used to evaluate the surface quality and continuity between adjacent surfaces.
    """


    ##  display methods 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Reflection</term><description> 
    ##  Create reflection lines </description> </item><item><term> 
    ## Projection</term><description> 
    ##  Create projection lines </description> </item></list>
    class DisplayMethods(Enum):
        """
        Members Include: <Reflection> <Projection>
        """
        Reflection: int
        Projection: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> HighlightLinesAnalysisBuilder.DisplayMethods:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  analysis display options 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Polyline</term><description> 
    ##  Polyline </description> </item><item><term> 
    ## ZebraMap</term><description> 
    ##  Zebra Map </description> </item></list>
    class DisplayModes(Enum):
        """
        Members Include: <Polyline> <ZebraMap>
        """
        Polyline: int
        ZebraMap: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> HighlightLinesAnalysisBuilder.DisplayModes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  reference direction options 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Vector</term><description> 
    ##  vector; </description> </item><item><term> 
    ## Orientation</term><description> 
    ##  orientation; </description> </item></list>
    class IsoclineDirection(Enum):
        """
        Members Include: <Vector> <Orientation>
        """
        Vector: int
        Orientation: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> HighlightLinesAnalysisBuilder.IsoclineDirection:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  light placement 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Uniform</term><description> 
    ##  Uniform: Lights are placed uniformly on light plane </description> </item><item><term> 
    ## ThroughPoints</term><description> 
    ##  Through Points: A highlight line is guaranteed to pass through a surface point. </description> </item><item><term> 
    ## BetweenPoints</term><description> 
    ##  Between Points: Two highlight lines are guaranteed to
    ##         pass through two given surface points. More highlight lines
    ##         are created between these two highlight lines when light
    ##         number is more than two. </description> </item></list>
    class LightPlacements(Enum):
        """
        Members Include: <Uniform> <ThroughPoints> <BetweenPoints>
        """
        Uniform: int
        ThroughPoints: int
        BetweenPoints: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> HighlightLinesAnalysisBuilder.LightPlacements:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  light plane options
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## YZ</term><description> 
    ##  Uses YC-ZC plane as light plane </description> </item><item><term> 
    ## ZX</term><description> 
    ##  Uses XC-ZC plane as light plane </description> </item><item><term> 
    ## XY</term><description> 
    ##  Uses XC-YC plane as light plane </description> </item><item><term> 
    ## Arbitrary</term><description> 
    ##  Uses an arbitrary plane as light plane </description> </item></list>
    class LightPlaneOptions(Enum):
        """
        Members Include: <YZ> <ZX> <XY> <Arbitrary>
        """
        YZ: int
        ZX: int
        XY: int
        Arbitrary: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> HighlightLinesAnalysisBuilder.LightPlaneOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  output options 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## AnalysisObject</term><description> 
    ##  Analysis Object </description> </item><item><term> 
    ## HighlightCurves</term><description> 
    ##  Highlight Curves </description> </item><item><term> 
    ## Both</term><description> 
    ##  Both Analysis Object and Highlight Curves </description> </item></list>
    class OutputOption(Enum):
        """
        Members Include: <AnalysisObject> <HighlightCurves> <Both>
        """
        AnalysisObject: int
        HighlightCurves: int
        Both: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> HighlightLinesAnalysisBuilder.OutputOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  resolution options 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Coarse</term><description> 
    ##  Coarse </description> </item><item><term> 
    ## Standard</term><description> 
    ##  Standard </description> </item><item><term> 
    ## Fine</term><description> 
    ##  Fine </description> </item><item><term> 
    ## ExtraFine</term><description> 
    ##  Extra Fine </description> </item><item><term> 
    ## SuperFine</term><description> 
    ##  Super Fine </description> </item><item><term> 
    ## UltraFine</term><description> 
    ##  Ultra Fine </description> </item></list>
    class Resolutions(Enum):
        """
        Members Include: <Coarse> <Standard> <Fine> <ExtraFine> <SuperFine> <UltraFine>
        """
        Coarse: int
        Standard: int
        Fine: int
        ExtraFine: int
        SuperFine: int
        UltraFine: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> HighlightLinesAnalysisBuilder.Resolutions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  three types of light methods 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Uniform</term><description> 
    ##  Uniform: Lights are placed uniformly on light plane </description> </item><item><term> 
    ## ThroughPoints</term><description> 
    ##  Through Points: A highlight line is guaranteed to pass through a surface point. </description> </item><item><term> 
    ## BetweenPoints</term><description> 
    ##  Between Points: Two highlight lines are guaranteed to
    ##         pass through two given surface points. More highlight lines
    ##         are created between these two highlight lines when light
    ##         number is more than two. </description> </item></list>
    class Types(Enum):
        """
        Members Include: <Uniform> <ThroughPoints> <BetweenPoints>
        """
        Uniform: int
        ThroughPoints: int
        BetweenPoints: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> HighlightLinesAnalysisBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  four types of display methods 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Reflection</term><description> 
    ##  Create reflection lines </description> </item><item><term> 
    ## Projection</term><description> 
    ##  Create projection lines </description> </item><item><term> 
    ## Isoclines</term><description> 
    ##  Create isoclines </description> </item><item><term> 
    ## Zebra</term><description> 
    ##  Create zebra contour lines </description> </item></list>
    class Types2(Enum):
        """
        Members Include: <Reflection> <Projection> <Isoclines> <Zebra>
        """
        Reflection: int
        Projection: int
        Isoclines: int
        Zebra: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> HighlightLinesAnalysisBuilder.Types2:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.SelectPointList NXOpen.SelectPointList@endlink) BetweenPoints
    ##  Returns the between points   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SelectPointList
    @property
    def BetweenPoints(self) -> NXOpen.SelectPointList:
        """
        Getter for property: (@link NXOpen.SelectPointList NXOpen.SelectPointList@endlink) BetweenPoints
         Returns the between points   
            
         
        """
        pass
    
    ## Getter for property: (@link HighlightLinesAnalysisBuilder.DisplayMethods NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.DisplayMethods@endlink) DisplayMethod
    ##  Returns the display method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.0.0.  Use @link NXOpen::GeometricAnalysis::HighlightLinesAnalysisBuilder::Type2 NXOpen::GeometricAnalysis::HighlightLinesAnalysisBuilder::Type2@endlink  instead.  <br> 

    ## @return HighlightLinesAnalysisBuilder.DisplayMethods
    @property
    def DisplayMethod(self) -> HighlightLinesAnalysisBuilder.DisplayMethods:
        """
        Getter for property: (@link HighlightLinesAnalysisBuilder.DisplayMethods NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.DisplayMethods@endlink) DisplayMethod
         Returns the display method   
            
         
        """
        pass
    
    ## Setter for property: (@link HighlightLinesAnalysisBuilder.DisplayMethods NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.DisplayMethods@endlink) DisplayMethod

    ##  Returns the display method   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.0.0.  Use @link NXOpen::GeometricAnalysis::HighlightLinesAnalysisBuilder::SetType2 NXOpen::GeometricAnalysis::HighlightLinesAnalysisBuilder::SetType2@endlink  instead.  <br> 

    @DisplayMethod.setter
    def DisplayMethod(self, displayMethod: HighlightLinesAnalysisBuilder.DisplayMethods):
        """
        Setter for property: (@link HighlightLinesAnalysisBuilder.DisplayMethods NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.DisplayMethods@endlink) DisplayMethod
         Returns the display method   
            
         
        """
        pass
    
    ## Getter for property: (@link HighlightLinesAnalysisBuilder.DisplayModes NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.DisplayModes@endlink) DisplayMode
    ##  Returns the analysis display   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return HighlightLinesAnalysisBuilder.DisplayModes
    @property
    def DisplayMode(self) -> HighlightLinesAnalysisBuilder.DisplayModes:
        """
        Getter for property: (@link HighlightLinesAnalysisBuilder.DisplayModes NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.DisplayModes@endlink) DisplayMode
         Returns the analysis display   
            
         
        """
        pass
    
    ## Setter for property: (@link HighlightLinesAnalysisBuilder.DisplayModes NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.DisplayModes@endlink) DisplayMode

    ##  Returns the analysis display   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @DisplayMode.setter
    def DisplayMode(self, display: HighlightLinesAnalysisBuilder.DisplayModes):
        """
        Setter for property: (@link HighlightLinesAnalysisBuilder.DisplayModes NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.DisplayModes@endlink) DisplayMode
         Returns the analysis display   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EndIsoAngle
    ##  Returns the end angle for isoclines (uniform)   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.Expression
    @property
    def EndIsoAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EndIsoAngle
         Returns the end angle for isoclines (uniform)   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Faces
    ##  Returns the face list   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def Faces(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Faces
         Returns the face list   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsReflectionLocked
    ##  Returns the lock reflection.  
    ##    When the lock is on, the reflection lines will be freezed
    ##         while the view is changing. Otherwise, the reflection lines
    ##         will be updated continuously while view is changing.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
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
    
    ## Setter for property: (bool) IsReflectionLocked

    ##  Returns the lock reflection.  
    ##    When the lock is on, the reflection lines will be freezed
    ##         while the view is changing. Otherwise, the reflection lines
    ##         will be updated continuously while view is changing.   
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

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
    
    ## Getter for property: (@link HighlightLinesAnalysisBuilder.IsoclineDirection NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.IsoclineDirection@endlink) IsoclineOption
    ##  Returns the isocline reference direction   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return HighlightLinesAnalysisBuilder.IsoclineDirection
    @property
    def IsoclineOption(self) -> HighlightLinesAnalysisBuilder.IsoclineDirection:
        """
        Getter for property: (@link HighlightLinesAnalysisBuilder.IsoclineDirection NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.IsoclineDirection@endlink) IsoclineOption
         Returns the isocline reference direction   
            
         
        """
        pass
    
    ## Setter for property: (@link HighlightLinesAnalysisBuilder.IsoclineDirection NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.IsoclineDirection@endlink) IsoclineOption

    ##  Returns the isocline reference direction   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @IsoclineOption.setter
    def IsoclineOption(self, option: HighlightLinesAnalysisBuilder.IsoclineDirection):
        """
        Setter for property: (@link HighlightLinesAnalysisBuilder.IsoclineDirection NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.IsoclineDirection@endlink) IsoclineOption
         Returns the isocline reference direction   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) IsoclineOrientation
    ##  Returns the isocline orirentation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.Matrix3x3
    @property
    def IsoclineOrientation(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) IsoclineOrientation
         Returns the isocline orirentation   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) IsoclineOrientation

    ##  Returns the isocline orirentation   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @IsoclineOrientation.setter
    def IsoclineOrientation(self, isoclineOrientation: NXOpen.Matrix3x3):
        """
        Setter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) IsoclineOrientation
         Returns the isocline orirentation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) IsoclineOrigin
    ##  Returns the isocline origin   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def IsoclineOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) IsoclineOrigin
         Returns the isocline origin   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) IsoclineOrigin

    ##  Returns the isocline origin   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @IsoclineOrigin.setter
    def IsoclineOrigin(self, isoclineOrigin: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) IsoclineOrigin
         Returns the isocline origin   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) IsoclineVector
    ##  Returns the vector to define isoclines   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.Direction
    @property
    def IsoclineVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) IsoclineVector
         Returns the vector to define isoclines   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) IsoclineVector

    ##  Returns the vector to define isoclines   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @IsoclineVector.setter
    def IsoclineVector(self, isoclineVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) IsoclineVector
         Returns the vector to define isoclines   
            
         
        """
        pass
    
    ## Getter for property: (float) LightDiffuseness
    ##  Returns the ratio of blended texels to all light texels.  
    ##    It is used by reflection contours   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def LightDiffuseness(self) -> float:
        """
        Getter for property: (float) LightDiffuseness
         Returns the ratio of blended texels to all light texels.  
           It is used by reflection contours   
         
        """
        pass
    
    ## Setter for property: (float) LightDiffuseness

    ##  Returns the ratio of blended texels to all light texels.  
    ##    It is used by reflection contours   
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @LightDiffuseness.setter
    def LightDiffuseness(self, lightDiffuseness: float):
        """
        Setter for property: (float) LightDiffuseness
         Returns the ratio of blended texels to all light texels.  
           It is used by reflection contours   
         
        """
        pass
    
    ## Getter for property: (int) LightNumber
    ##  Returns the number of lights.  
    ##    It's used by Uniform type and Between Points type.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return int
    @property
    def LightNumber(self) -> int:
        """
        Getter for property: (int) LightNumber
         Returns the number of lights.  
           It's used by Uniform type and Between Points type.   
         
        """
        pass
    
    ## Setter for property: (int) LightNumber

    ##  Returns the number of lights.  
    ##    It's used by Uniform type and Between Points type.   
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @LightNumber.setter
    def LightNumber(self, lightNumber: int):
        """
        Setter for property: (int) LightNumber
         Returns the number of lights.  
           It's used by Uniform type and Between Points type.   
         
        """
        pass
    
    ## Getter for property: (@link HighlightLinesAnalysisBuilder.LightPlacements NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.LightPlacements@endlink) LightPlacement
    ##  Returns the light placement   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return HighlightLinesAnalysisBuilder.LightPlacements
    @property
    def LightPlacement(self) -> HighlightLinesAnalysisBuilder.LightPlacements:
        """
        Getter for property: (@link HighlightLinesAnalysisBuilder.LightPlacements NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.LightPlacements@endlink) LightPlacement
         Returns the light placement   
            
         
        """
        pass
    
    ## Setter for property: (@link HighlightLinesAnalysisBuilder.LightPlacements NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.LightPlacements@endlink) LightPlacement

    ##  Returns the light placement   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @LightPlacement.setter
    def LightPlacement(self, placement: HighlightLinesAnalysisBuilder.LightPlacements):
        """
        Setter for property: (@link HighlightLinesAnalysisBuilder.LightPlacements NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.LightPlacements@endlink) LightPlacement
         Returns the light placement   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) LightPlaneOrigin
    ##  Returns the origin of the light plane   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def LightPlaneOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) LightPlaneOrigin
         Returns the origin of the light plane   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) LightPlaneXAxis
    ##  Returns the x-axis of the light plane   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.Vector3d
    @property
    def LightPlaneXAxis(self) -> NXOpen.Vector3d:
        """
        Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) LightPlaneXAxis
         Returns the x-axis of the light plane   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) LightPlaneYAxis
    ##  Returns the y-axis of the light plane   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.Vector3d
    @property
    def LightPlaneYAxis(self) -> NXOpen.Vector3d:
        """
        Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) LightPlaneYAxis
         Returns the y-axis of the light plane   
            
         
        """
        pass
    
    ## Getter for property: (float) LightSpacing
    ##  Returns the light spacing between two adjacent lights.  
    ##    It's used by Uniform type   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return float
    @property
    def LightSpacing(self) -> float:
        """
        Getter for property: (float) LightSpacing
         Returns the light spacing between two adjacent lights.  
           It's used by Uniform type   
         
        """
        pass
    
    ## Setter for property: (float) LightSpacing

    ##  Returns the light spacing between two adjacent lights.  
    ##    It's used by Uniform type   
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @LightSpacing.setter
    def LightSpacing(self, lightSpacing: float):
        """
        Setter for property: (float) LightSpacing
         Returns the light spacing between two adjacent lights.  
           It's used by Uniform type   
         
        """
        pass
    
    ## Getter for property: (float) LightWidth
    ##  Returns the ratio of light size to light spacing.  
    ##    It is used by reflection contours   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return float
    @property
    def LightWidth(self) -> float:
        """
        Getter for property: (float) LightWidth
         Returns the ratio of light size to light spacing.  
           It is used by reflection contours   
         
        """
        pass
    
    ## Setter for property: (float) LightWidth

    ##  Returns the ratio of light size to light spacing.  
    ##    It is used by reflection contours   
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @LightWidth.setter
    def LightWidth(self, lightWidth: float):
        """
        Setter for property: (float) LightWidth
         Returns the ratio of light size to light spacing.  
           It is used by reflection contours   
         
        """
        pass
    
    ## Getter for property: (@link HighlightLinesAnalysisBuilder.OutputOption NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.OutputOption@endlink) Output
    ##  Returns the output   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return HighlightLinesAnalysisBuilder.OutputOption
    @property
    def Output(self) -> HighlightLinesAnalysisBuilder.OutputOption:
        """
        Getter for property: (@link HighlightLinesAnalysisBuilder.OutputOption NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.OutputOption@endlink) Output
         Returns the output   
            
         
        """
        pass
    
    ## Setter for property: (@link HighlightLinesAnalysisBuilder.OutputOption NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.OutputOption@endlink) Output

    ##  Returns the output   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Output.setter
    def Output(self, output: HighlightLinesAnalysisBuilder.OutputOption):
        """
        Setter for property: (@link HighlightLinesAnalysisBuilder.OutputOption NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.OutputOption@endlink) Output
         Returns the output   
            
         
        """
        pass
    
    ## Getter for property: (@link HighlightLinesAnalysisBuilder.Resolutions NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.Resolutions@endlink) Resolution
    ##  Returns the resolution.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return HighlightLinesAnalysisBuilder.Resolutions
    @property
    def Resolution(self) -> HighlightLinesAnalysisBuilder.Resolutions:
        """
        Getter for property: (@link HighlightLinesAnalysisBuilder.Resolutions NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.Resolutions@endlink) Resolution
         Returns the resolution.  
             
         
        """
        pass
    
    ## Setter for property: (@link HighlightLinesAnalysisBuilder.Resolutions NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.Resolutions@endlink) Resolution

    ##  Returns the resolution.  
    ##      
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @Resolution.setter
    def Resolution(self, resolution: HighlightLinesAnalysisBuilder.Resolutions):
        """
        Setter for property: (@link HighlightLinesAnalysisBuilder.Resolutions NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.Resolutions@endlink) Resolution
         Returns the resolution.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StartIsoAngle
    ##  Returns the start angle for isoclines (uniform)   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.Expression
    @property
    def StartIsoAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StartIsoAngle
         Returns the start angle for isoclines (uniform)   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectPointList NXOpen.SelectPointList@endlink) ThroughPoints
    ##  Returns the through points   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SelectPointList
    @property
    def ThroughPoints(self) -> NXOpen.SelectPointList:
        """
        Getter for property: (@link NXOpen.SelectPointList NXOpen.SelectPointList@endlink) ThroughPoints
         Returns the through points   
            
         
        """
        pass
    
    ## Getter for property: (@link HighlightLinesAnalysisBuilder.Types NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.Types@endlink) Type
    ##  Returns the type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.0.0.  Use @link NXOpen::GeometricAnalysis::HighlightLinesAnalysisBuilder::LightPlacement NXOpen::GeometricAnalysis::HighlightLinesAnalysisBuilder::LightPlacement@endlink  instead.  <br> 

    ## @return HighlightLinesAnalysisBuilder.Types
    @property
    def Type(self) -> HighlightLinesAnalysisBuilder.Types:
        """
        Getter for property: (@link HighlightLinesAnalysisBuilder.Types NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.Types@endlink) Type
         Returns the type   
            
         
        """
        pass
    
    ## Setter for property: (@link HighlightLinesAnalysisBuilder.Types NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.Types@endlink) Type

    ##  Returns the type   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.0.0.  Use @link NXOpen::GeometricAnalysis::HighlightLinesAnalysisBuilder::SetLightPlacement NXOpen::GeometricAnalysis::HighlightLinesAnalysisBuilder::SetLightPlacement@endlink  instead.  <br> 

    @Type.setter
    def Type(self, type: HighlightLinesAnalysisBuilder.Types):
        """
        Setter for property: (@link HighlightLinesAnalysisBuilder.Types NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.Types@endlink) Type
         Returns the type   
            
         
        """
        pass
    
    ## Getter for property: (@link HighlightLinesAnalysisBuilder.Types2 NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.Types2@endlink) Type2
    ##  Returns the display type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return HighlightLinesAnalysisBuilder.Types2
    @property
    def Type2(self) -> HighlightLinesAnalysisBuilder.Types2:
        """
        Getter for property: (@link HighlightLinesAnalysisBuilder.Types2 NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.Types2@endlink) Type2
         Returns the display type   
            
         
        """
        pass
    
    ## Setter for property: (@link HighlightLinesAnalysisBuilder.Types2 NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.Types2@endlink) Type2

    ##  Returns the display type   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @Type2.setter
    def Type2(self, type: HighlightLinesAnalysisBuilder.Types2):
        """
        Setter for property: (@link HighlightLinesAnalysisBuilder.Types2 NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.Types2@endlink) Type2
         Returns the display type   
            
         
        """
        pass
    
    ##  Gets the color of the bright (lit) areas of reflection contours 
    ##  @return brightColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    def GetBrightColor(self) -> List[float]:
        """
         Gets the color of the bright (lit) areas of reflection contours 
         @return brightColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    
    ##  Gets the color of the dark (unlit) areas of reflection contours 
    ##  @return darkColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    def GetDarkColor(self) -> List[float]:
        """
         Gets the color of the dark (unlit) areas of reflection contours 
         @return darkColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    
    ##  Reinitialize light plane based on the selected faces. If
    ##         more faces are selected, you may need to change
    ##         light plane, so the light plane could be better centered. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.0.0.  This call currently does not do anything.  Calls to this method can be safely removed.  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    def ReinitializePlane(self) -> None:
        """
         Reinitialize light plane based on the selected faces. If
                more faces are selected, you may need to change
                light plane, so the light plane could be better centered. 
        """
        pass
    
    ##  Sets the color of the bright (lit) areas of reflection contours 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="brightColor"> (List[float])  Array of 3 RGB values, each between 0 and 1 </param>
    def SetBrightColor(self, brightColor: List[float]) -> None:
        """
         Sets the color of the bright (lit) areas of reflection contours 
        """
        pass
    
    ##  Sets the color of the dark (unlit) areas of reflection contours 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="darkColor"> (List[float])  Array of 3 RGB values, each between 0 and 1 </param>
    def SetDarkColor(self, darkColor: List[float]) -> None:
        """
         Sets the color of the dark (unlit) areas of reflection contours 
        """
        pass
    
    ##  Sets the origin of the light plane. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="origin"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  coordinates of origin </param>
    def SetLightPlaneOrigin(self, origin: NXOpen.Point3d) -> None:
        """
         Sets the origin of the light plane. 
        """
        pass
    
    ##  Sets the x-axis of the light plane. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="xAxis"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink)  x-axis vector </param>
    def SetLightPlaneXAxis(self, xAxis: NXOpen.Vector3d) -> None:
        """
         Sets the x-axis of the light plane. 
        """
        pass
    
    ##  Sets the y-axis of the light plane. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ## <param name="yAxis"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink)  y-axis vector </param>
    def SetLightPlaneYAxis(self, yAxis: NXOpen.Vector3d) -> None:
        """
         Sets the y-axis of the light plane. 
        """
        pass
    
##  Represents a Highlight Lines Analysis object. Highlight Lines
##     Analysis function can produce both reflection lines and projection
##     lines which are used to evaluate the surface quality and
##     continuity between adjacent surfaces.  <br> To create or edit an instance of this class, use @link NXOpen::GeometricAnalysis::HighlightLinesAnalysisBuilder  NXOpen::GeometricAnalysis::HighlightLinesAnalysisBuilder @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class HighlightLinesAnalysis(AnalysisObject): 
    """ Represents a Highlight Lines Analysis object. Highlight Lines
    Analysis function can produce both reflection lines and projection
    lines which are used to evaluate the surface quality and
    continuity between adjacent surfaces. """
    pass


import NXOpen
import NXOpen.Features
##  Represents a @link NXOpen::GeometricAnalysis::LocalRadiusAnalysis NXOpen::GeometricAnalysis::LocalRadiusAnalysis@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisObjectCollection::CreateLocalRadiusAnalysisBuilder  NXOpen::GeometricAnalysis::AnalysisObjectCollection::CreateLocalRadiusAnalysisBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## VisibilityCoordinates </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## VisibilityMaxRadius </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## VisibilityMinMaxRadiusTangent </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## VisibilityMinRadius </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## VisibilityRadius </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## VisibilityURadius </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## VisibilityUV </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## VisibilityUVTangent </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## VisibilityVRadius </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX8.5.0  <br> 

class LocalRadiusAnalysisBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.GeometricAnalysis.LocalRadiusAnalysis</ja_class> builder """


    ## Getter for property: (@link NXOpen.Features.GeometricConstraintDataManager NXOpen.Features.GeometricConstraintDataManager@endlink) SelectionPoint
    ##  Returns the selection point   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.Features.GeometricConstraintDataManager
    @property
    def SelectionPoint(self) -> NXOpen.Features.GeometricConstraintDataManager:
        """
        Getter for property: (@link NXOpen.Features.GeometricConstraintDataManager NXOpen.Features.GeometricConstraintDataManager@endlink) SelectionPoint
         Returns the selection point   
            
         
        """
        pass
    
    ## Getter for property: (bool) VisibilityCoordinates
    ##  Returns the toggle coordinates   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def VisibilityCoordinates(self) -> bool:
        """
        Getter for property: (bool) VisibilityCoordinates
         Returns the toggle coordinates   
            
         
        """
        pass
    
    ## Setter for property: (bool) VisibilityCoordinates

    ##  Returns the toggle coordinates   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @VisibilityCoordinates.setter
    def VisibilityCoordinates(self, visibilityCoordinates: bool):
        """
        Setter for property: (bool) VisibilityCoordinates
         Returns the toggle coordinates   
            
         
        """
        pass
    
    ## Getter for property: (bool) VisibilityMaxRadius
    ##  Returns the toggle max radius show   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def VisibilityMaxRadius(self) -> bool:
        """
        Getter for property: (bool) VisibilityMaxRadius
         Returns the toggle max radius show   
            
         
        """
        pass
    
    ## Setter for property: (bool) VisibilityMaxRadius

    ##  Returns the toggle max radius show   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @VisibilityMaxRadius.setter
    def VisibilityMaxRadius(self, visibilityMaxRadius: bool):
        """
        Setter for property: (bool) VisibilityMaxRadius
         Returns the toggle max radius show   
            
         
        """
        pass
    
    ## Getter for property: (bool) VisibilityMinMaxRadiusTangent
    ##  Returns the toggle min radius tangent   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def VisibilityMinMaxRadiusTangent(self) -> bool:
        """
        Getter for property: (bool) VisibilityMinMaxRadiusTangent
         Returns the toggle min radius tangent   
            
         
        """
        pass
    
    ## Setter for property: (bool) VisibilityMinMaxRadiusTangent

    ##  Returns the toggle min radius tangent   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @VisibilityMinMaxRadiusTangent.setter
    def VisibilityMinMaxRadiusTangent(self, visibilityMinMaxRadiusTangent: bool):
        """
        Setter for property: (bool) VisibilityMinMaxRadiusTangent
         Returns the toggle min radius tangent   
            
         
        """
        pass
    
    ## Getter for property: (bool) VisibilityMinRadius
    ##  Returns the toggle min radius show   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def VisibilityMinRadius(self) -> bool:
        """
        Getter for property: (bool) VisibilityMinRadius
         Returns the toggle min radius show   
            
         
        """
        pass
    
    ## Setter for property: (bool) VisibilityMinRadius

    ##  Returns the toggle min radius show   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @VisibilityMinRadius.setter
    def VisibilityMinRadius(self, visibilityMinRadius: bool):
        """
        Setter for property: (bool) VisibilityMinRadius
         Returns the toggle min radius show   
            
         
        """
        pass
    
    ## Getter for property: (bool) VisibilityRadius
    ##  Returns the toggle radius show   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def VisibilityRadius(self) -> bool:
        """
        Getter for property: (bool) VisibilityRadius
         Returns the toggle radius show   
            
         
        """
        pass
    
    ## Setter for property: (bool) VisibilityRadius

    ##  Returns the toggle radius show   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @VisibilityRadius.setter
    def VisibilityRadius(self, visibilityRadius: bool):
        """
        Setter for property: (bool) VisibilityRadius
         Returns the toggle radius show   
            
         
        """
        pass
    
    ## Getter for property: (bool) VisibilityURadius
    ##  Returns the toggle uradius show   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def VisibilityURadius(self) -> bool:
        """
        Getter for property: (bool) VisibilityURadius
         Returns the toggle uradius show   
            
         
        """
        pass
    
    ## Setter for property: (bool) VisibilityURadius

    ##  Returns the toggle uradius show   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @VisibilityURadius.setter
    def VisibilityURadius(self, visibilityURadius: bool):
        """
        Setter for property: (bool) VisibilityURadius
         Returns the toggle uradius show   
            
         
        """
        pass
    
    ## Getter for property: (bool) VisibilityUV
    ##  Returns the toggle uv   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def VisibilityUV(self) -> bool:
        """
        Getter for property: (bool) VisibilityUV
         Returns the toggle uv   
            
         
        """
        pass
    
    ## Setter for property: (bool) VisibilityUV

    ##  Returns the toggle uv   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @VisibilityUV.setter
    def VisibilityUV(self, visibilityUV: bool):
        """
        Setter for property: (bool) VisibilityUV
         Returns the toggle uv   
            
         
        """
        pass
    
    ## Getter for property: (bool) VisibilityUVTangent
    ##  Returns the toggle max radius tangent   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def VisibilityUVTangent(self) -> bool:
        """
        Getter for property: (bool) VisibilityUVTangent
         Returns the toggle max radius tangent   
            
         
        """
        pass
    
    ## Setter for property: (bool) VisibilityUVTangent

    ##  Returns the toggle max radius tangent   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @VisibilityUVTangent.setter
    def VisibilityUVTangent(self, visibilityUVTangent: bool):
        """
        Setter for property: (bool) VisibilityUVTangent
         Returns the toggle max radius tangent   
            
         
        """
        pass
    
    ## Getter for property: (bool) VisibilityVRadius
    ##  Returns the toggle vradius show   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return bool
    @property
    def VisibilityVRadius(self) -> bool:
        """
        Getter for property: (bool) VisibilityVRadius
         Returns the toggle vradius show   
            
         
        """
        pass
    
    ## Setter for property: (bool) VisibilityVRadius

    ##  Returns the toggle vradius show   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @VisibilityVRadius.setter
    def VisibilityVRadius(self, visibilityVRadius: bool):
        """
        Setter for property: (bool) VisibilityVRadius
         Returns the toggle vradius show   
            
         
        """
        pass
    
    ##  TODO: fill in a description for this 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    def ButtonOpenInformationWindow(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    
##  Builder for Local Radius Analysis (formerly Dynamic Radius)  <br> To create or edit an instance of this class, use @link NXOpen::GeometricAnalysis::LocalRadiusAnalysisBuilder  NXOpen::GeometricAnalysis::LocalRadiusAnalysisBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class LocalRadiusAnalysis(AnalysisObject): 
    """ Builder for Local Radius Analysis (formerly Dynamic Radius) """
    pass


import NXOpen
import NXOpen.DesignSimulation
##  Represents a @link NXOpen::GeometricAnalysis::PerformancePredictorBuilder NXOpen::GeometricAnalysis::PerformancePredictorBuilder@endlink   <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisObjectCollectionEx::CreatePerformancePredictorBuilder  NXOpen::GeometricAnalysis::AnalysisObjectCollectionEx::CreatePerformancePredictorBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Study.AnalysisType </term> <description> 
##  
## LinearStatics </description> </item> 
## 
## <item><term> 
##  
## Study.OptimizationObjectiveType </term> <description> 
##  
## MaximumStiffness </description> </item> 
## 
## <item><term> 
##  
## Study.ResolutionVoxelSize.Value </term> <description> 
##  
## 1 (millimeters part), 0.04 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Study.StudyQuality </term> <description> 
##  
## 5 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class PerformancePredictorBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.GeometricAnalysis.PerformancePredictorBuilder</ja_class> """


    ## Getter for property: (@link NXOpen.DesignSimulation.StudyBuilder NXOpen.DesignSimulation.StudyBuilder@endlink) Study
    ##  Returns the study builder  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.DesignSimulation.StudyBuilder
    @property
    def Study(self) -> NXOpen.DesignSimulation.StudyBuilder:
        """
        Getter for property: (@link NXOpen.DesignSimulation.StudyBuilder NXOpen.DesignSimulation.StudyBuilder@endlink) Study
         Returns the study builder  
            
         
        """
        pass
    
import NXOpen
import NXOpen.DesignSimulation
##  Represents a @link NXOpen::GeometricAnalysis::PerformancePredictor NXOpen::GeometricAnalysis::PerformancePredictor@endlink   <br> To create or edit an instance of this class, use @link NXOpen::GeometricAnalysis::PerformancePredictorBuilder  NXOpen::GeometricAnalysis::PerformancePredictorBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class PerformancePredictor(AnalysisObject): 
    """ Represents a <ja_class>NXOpen.GeometricAnalysis.PerformancePredictor</ja_class> """


    ##  Performance Predictor solver option. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Foreground</term><description> 
    ##  Analysis will run in the foreground so that the user needs to wait during processing. </description> </item><item><term> 
    ## Background</term><description> 
    ##  Analysis will run in the background so that the user can proceed working with NX. </description> </item></list>
    class SolveOption(Enum):
        """
        Members Include: <Foreground> <Background>
        """
        Foreground: int
        Background: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PerformancePredictor.SolveOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.DesignSimulation.Study NXOpen.DesignSimulation.Study@endlink) Study
    ##  Returns the active study of Performance Predictor   
    ##     
    ##  
    ## Getter License requirements: nx_perf_predictor (" Performance Predictor")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.DesignSimulation.Study
    @property
    def Study(self) -> NXOpen.DesignSimulation.Study:
        """
        Getter for property: (@link NXOpen.DesignSimulation.Study NXOpen.DesignSimulation.Study@endlink) Study
         Returns the active study of Performance Predictor   
            
         
        """
        pass
    
    ##  Activates Performance Predictor
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_perf_predictor (" Performance Predictor")
    def Activate(self) -> None:
        """
         Activates Performance Predictor
        """
        pass
    
    ##  Solves this @link NXOpen::GeometricAnalysis::PerformancePredictor NXOpen::GeometricAnalysis::PerformancePredictor@endlink  if the analysis is fully setup and ready to solve.
    ## 
    ##         This method will return after pre-processing and launching the analysis process depending on the @link NXOpen::GeometricAnalysis::PerformancePredictor::SolveOption NXOpen::GeometricAnalysis::PerformancePredictor::SolveOption@endlink  passed in this method.
    ##         
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_perf_predictor (" Performance Predictor")
    ## 
    ## <param name="solveOption"> (@link PerformancePredictor.SolveOption NXOpen.GeometricAnalysis.PerformancePredictor.SolveOption@endlink) </param>
    def Analyze(self, solveOption: PerformancePredictor.SolveOption) -> None:
        """
         Solves this @link NXOpen::GeometricAnalysis::PerformancePredictor NXOpen::GeometricAnalysis::PerformancePredictor@endlink  if the analysis is fully setup and ready to solve.
        
                This method will return after pre-processing and launching the analysis process depending on the @link NXOpen::GeometricAnalysis::PerformancePredictor::SolveOption NXOpen::GeometricAnalysis::PerformancePredictor::SolveOption@endlink  passed in this method.
                
        """
        pass
    
    ##  Clones (copies) a @link NXOpen::GeometricAnalysis::PerformancePredictor NXOpen::GeometricAnalysis::PerformancePredictor@endlink  object and returns the cloned (copied) object if successful. 
    ##  @return clonedSolution (@link PerformancePredictor NXOpen.GeometricAnalysis.PerformancePredictor@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_perf_predictor (" Performance Predictor")
    def CloneSimulation(self) -> PerformancePredictor:
        """
         Clones (copies) a @link NXOpen::GeometricAnalysis::PerformancePredictor NXOpen::GeometricAnalysis::PerformancePredictor@endlink  object and returns the cloned (copied) object if successful. 
         @return clonedSolution (@link PerformancePredictor NXOpen.GeometricAnalysis.PerformancePredictor@endlink): .
        """
        pass
    
    ##  Deactivates Performance Predictor
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_perf_predictor (" Performance Predictor")
    def Deactivate(self) -> None:
        """
         Deactivates Performance Predictor
        """
        pass
    
    ##  Finds the @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  with the given identifier.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return study (@link NXOpen.INXObject NXOpen.INXObject@endlink):  An object matching the journal identifier. .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="journalIdentifier"> (str)  Identifier to be found </param>
    def FindObject(self, journalIdentifier: str) -> NXOpen.INXObject:
        """
         Finds the @link NXOpen::DesignSimulation::Study NXOpen::DesignSimulation::Study@endlink  with the given identifier.
                    An exception will be thrown if no object can be found with given name. 
         @return study (@link NXOpen.INXObject NXOpen.INXObject@endlink):  An object matching the journal identifier. .
        """
        pass
    
    ##  Remove results from Performance Predictor
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_perf_predictor (" Performance Predictor")
    def RemoveResults(self) -> None:
        """
         Remove results from Performance Predictor
        """
        pass
    
import NXOpen
import NXOpen.Features
##  Represents a Radius Analysis builder.  <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisObjectCollectionEx::CreateRadiusAnalysisBuilder1  NXOpen::GeometricAnalysis::AnalysisObjectCollectionEx::CreateRadiusAnalysisBuilder1 @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DataRange.IsFixed </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## DataRange.Max </term> <description> 
##  
## 0.01 </description> </item> 
## 
## <item><term> 
##  
## DataRange.Middle </term> <description> 
##  
## 0.00001 </description> </item> 
## 
## <item><term> 
##  
## DataRange.MiddleScale </term> <description> 
##  
## 999999 </description> </item> 
## 
## <item><term> 
##  
## DataRange.Min </term> <description> 
##  
## -0.01 </description> </item> 
## 
## <item><term> 
##  
## DataRange.NumberOfColors </term> <description> 
##  
## Seven </description> </item> 
## 
## <item><term> 
##  
## DataRange.UserDefinedColorScale.NumberOfColors </term> <description> 
##  
## Seven </description> </item> 
## 
## <item><term> 
##  
## DataRange.ZoomScale </term> <description> 
##  
## 8 </description> </item> 
## 
## <item><term> 
##  
## DisplayMode </term> <description> 
##  
## Fringe </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.CanShowFacet </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.ColorLegendOption </term> <description> 
##  
## Blend </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.DisplayResolution.AngleTolerance </term> <description> 
##  
## 15.0 </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.DisplayResolution.EdgeTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.DisplayResolution.FaceTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.DisplayResolution.Resolution </term> <description> 
##  
## Standard </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.DisplayResolution.WidthTolerance </term> <description> 
##  
## 0.3 </description> </item> 
## 
## <item><term> 
##  
## NumberOfContourLines </term> <description> 
##  
## 8 </description> </item> 
## 
## <item><term> 
##  
## SpikeLength </term> <description> 
##  
## 25.4 (millimeters part), 1.0 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2312.0.0  <br> 

class RadiusAnalysisBuilder1(NXOpen.Builder): 
    """ Represents a Radius Analysis builder. """


    ##  The display type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Fringe</term><description> 
    ##  Display in fringe. </description> </item><item><term> 
    ## Hedgehog</term><description> 
    ##  Display in hedgehog. </description> </item><item><term> 
    ## ContourLines</term><description> 
    ##  Display in contour lines. </description> </item></list>
    class DisplayModes(Enum):
        """
        Members Include: <Fringe> <Hedgehog> <ContourLines>
        """
        Fringe: int
        Hedgehog: int
        ContourLines: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RadiusAnalysisBuilder1.DisplayModes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the radius type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Gaussian</term><description> 
    ##  Gaussian radius. </description> </item><item><term> 
    ## Minimum</term><description> 
    ##  Minimum radius. </description> </item><item><term> 
    ## Maximum</term><description> 
    ##  Maximum radius. </description> </item><item><term> 
    ## Mean</term><description> 
    ##  Mean radius. </description> </item><item><term> 
    ## Normal</term><description> 
    ##  Normal radius. </description> </item><item><term> 
    ## Sectional</term><description> 
    ##  Sectional radius. </description> </item><item><term> 
    ## U</term><description> 
    ##  Radius in U direction. </description> </item><item><term> 
    ## V</term><description> 
    ##  Radius in V direction. </description> </item></list>
    class Types(Enum):
        """
        Members Include: <Gaussian> <Minimum> <Maximum> <Mean> <Normal> <Sectional> <U> <V>
        """
        Gaussian: int
        Minimum: int
        Maximum: int
        Mean: int
        Normal: int
        Sectional: int
        U: int
        V: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RadiusAnalysisBuilder1.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link FaceAnalysisDataRangeBuilder NXOpen.GeometricAnalysis.FaceAnalysisDataRangeBuilder@endlink) DataRange
    ##  Returns the radius analysis data range.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return FaceAnalysisDataRangeBuilder
    @property
    def DataRange(self) -> FaceAnalysisDataRangeBuilder:
        """
        Getter for property: (@link FaceAnalysisDataRangeBuilder NXOpen.GeometricAnalysis.FaceAnalysisDataRangeBuilder@endlink) DataRange
         Returns the radius analysis data range.  
             
         
        """
        pass
    
    ## Getter for property: (@link RadiusAnalysisBuilder1.DisplayModes NXOpen.GeometricAnalysis.RadiusAnalysisBuilder1.DisplayModes@endlink) DisplayMode
    ##  Returns the display mode.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return RadiusAnalysisBuilder1.DisplayModes
    @property
    def DisplayMode(self) -> RadiusAnalysisBuilder1.DisplayModes:
        """
        Getter for property: (@link RadiusAnalysisBuilder1.DisplayModes NXOpen.GeometricAnalysis.RadiusAnalysisBuilder1.DisplayModes@endlink) DisplayMode
         Returns the display mode.  
             
         
        """
        pass
    
    ## Setter for property: (@link RadiusAnalysisBuilder1.DisplayModes NXOpen.GeometricAnalysis.RadiusAnalysisBuilder1.DisplayModes@endlink) DisplayMode

    ##  Returns the display mode.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @DisplayMode.setter
    def DisplayMode(self, displayMode: RadiusAnalysisBuilder1.DisplayModes):
        """
        Setter for property: (@link RadiusAnalysisBuilder1.DisplayModes NXOpen.GeometricAnalysis.RadiusAnalysisBuilder1.DisplayModes@endlink) DisplayMode
         Returns the display mode.  
             
         
        """
        pass
    
    ## Getter for property: (@link FaceAnalysisDisplayBuilder NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilder@endlink) DisplaySettings
    ##  Returns the radius analysis display settings.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return FaceAnalysisDisplayBuilder
    @property
    def DisplaySettings(self) -> FaceAnalysisDisplayBuilder:
        """
        Getter for property: (@link FaceAnalysisDisplayBuilder NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilder@endlink) DisplaySettings
         Returns the radius analysis display settings.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Features.GeometricConstraintDataManager NXOpen.Features.GeometricConstraintDataManager@endlink) DynamicLabel
    ##  Returns the dynamic label   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Features.GeometricConstraintDataManager
    @property
    def DynamicLabel(self) -> NXOpen.Features.GeometricConstraintDataManager:
        """
        Getter for property: (@link NXOpen.Features.GeometricConstraintDataManager NXOpen.Features.GeometricConstraintDataManager@endlink) DynamicLabel
         Returns the dynamic label   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Faces
    ##  Returns the face to apply radius analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def Faces(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Faces
         Returns the face to apply radius analysis.  
             
         
        """
        pass
    
    ## Getter for property: (@link FaceAnalysisNormalsBuilder NXOpen.GeometricAnalysis.FaceAnalysisNormalsBuilder@endlink) Normals
    ##  Returns the radius analysis normals.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return FaceAnalysisNormalsBuilder
    @property
    def Normals(self) -> FaceAnalysisNormalsBuilder:
        """
        Getter for property: (@link FaceAnalysisNormalsBuilder NXOpen.GeometricAnalysis.FaceAnalysisNormalsBuilder@endlink) Normals
         Returns the radius analysis normals.  
             
         
        """
        pass
    
    ## Getter for property: (int) NumberOfContourLines
    ##  Returns the number of contour lines.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return int
    @property
    def NumberOfContourLines(self) -> int:
        """
        Getter for property: (int) NumberOfContourLines
         Returns the number of contour lines.  
             
         
        """
        pass
    
    ## Setter for property: (int) NumberOfContourLines

    ##  Returns the number of contour lines.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @NumberOfContourLines.setter
    def NumberOfContourLines(self, numberOfContourLines: int):
        """
        Setter for property: (int) NumberOfContourLines
         Returns the number of contour lines.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane
    ##  Returns the reference plane used for @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1::TypesSectional NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1::TypesSectional@endlink .  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Plane
    @property
    def Plane(self) -> NXOpen.Plane:
        """
        Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane
         Returns the reference plane used for @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1::TypesSectional NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1::TypesSectional@endlink .  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane

    ##  Returns the reference plane used for @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1::TypesSectional NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1::TypesSectional@endlink .  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @Plane.setter
    def Plane(self, plane: NXOpen.Plane):
        """
        Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane
         Returns the reference plane used for @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1::TypesSectional NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1::TypesSectional@endlink .  
             
         
        """
        pass
    
    ## Getter for property: (float) SpikeLength
    ##  Returns the spike length.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def SpikeLength(self) -> float:
        """
        Getter for property: (float) SpikeLength
         Returns the spike length.  
             
         
        """
        pass
    
    ## Setter for property: (float) SpikeLength

    ##  Returns the spike length.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @SpikeLength.setter
    def SpikeLength(self, spikeLength: float):
        """
        Setter for property: (float) SpikeLength
         Returns the spike length.  
             
         
        """
        pass
    
    ## Getter for property: (@link RadiusAnalysisBuilder1.Types NXOpen.GeometricAnalysis.RadiusAnalysisBuilder1.Types@endlink) Type
    ##  Returns the radius type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return RadiusAnalysisBuilder1.Types
    @property
    def Type(self) -> RadiusAnalysisBuilder1.Types:
        """
        Getter for property: (@link RadiusAnalysisBuilder1.Types NXOpen.GeometricAnalysis.RadiusAnalysisBuilder1.Types@endlink) Type
         Returns the radius type.  
             
         
        """
        pass
    
    ## Setter for property: (@link RadiusAnalysisBuilder1.Types NXOpen.GeometricAnalysis.RadiusAnalysisBuilder1.Types@endlink) Type

    ##  Returns the radius type.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @Type.setter
    def Type(self, type: RadiusAnalysisBuilder1.Types):
        """
        Setter for property: (@link RadiusAnalysisBuilder1.Types NXOpen.GeometricAnalysis.RadiusAnalysisBuilder1.Types@endlink) Type
         Returns the radius type.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector
    ##  Returns the reference vector for @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1::TypesNormal NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1::TypesNormal@endlink .  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def Vector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector
         Returns the reference vector for @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1::TypesNormal NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1::TypesNormal@endlink .  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector

    ##  Returns the reference vector for @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1::TypesNormal NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1::TypesNormal@endlink .  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @Vector.setter
    def Vector(self, vector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector
         Returns the reference vector for @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1::TypesNormal NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1::TypesNormal@endlink .  
             
         
        """
        pass
    
    ##  Start radius analysis. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def StartRadiusAnalysis(self) -> None:
        """
         Start radius analysis. 
        """
        pass
    
    ##  Update display after plane changes. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def UpdateDisplayOnPlaneChange(self) -> None:
        """
         Update display after plane changes. 
        """
        pass
    
import NXOpen
import NXOpen.Features
##  Represents a Radius Analysis builder.  <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisObjectCollectionEx::CreateRadiusAnalysisBuilder  NXOpen::GeometricAnalysis::AnalysisObjectCollectionEx::CreateRadiusAnalysisBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DataRange.IsFixed (deprecated) </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## DataRange.Max (deprecated) </term> <description> 
##  
## 0.01 </description> </item> 
## 
## <item><term> 
##  
## DataRange.Middle (deprecated) </term> <description> 
##  
## 0.00001 </description> </item> 
## 
## <item><term> 
##  
## DataRange.MiddleScale (deprecated) </term> <description> 
##  
## 999999 </description> </item> 
## 
## <item><term> 
##  
## DataRange.Min (deprecated) </term> <description> 
##  
## -0.01 </description> </item> 
## 
## <item><term> 
##  
## DataRange.ZoomScale (deprecated) </term> <description> 
##  
## 8 </description> </item> 
## 
## <item><term> 
##  
## DisplayMode (deprecated) </term> <description> 
##  
## Fringe </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.CanShowFacet (deprecated) </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.ColorLegendOption (deprecated) </term> <description> 
##  
## Blend </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.DisplayResolution.AngleTolerance (deprecated) </term> <description> 
##  
## 15.0 </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.DisplayResolution.EdgeTolerance (deprecated) </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.DisplayResolution.FaceTolerance (deprecated) </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.DisplayResolution.Resolution (deprecated) </term> <description> 
##  
## Standard </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.DisplayResolution.WidthTolerance (deprecated) </term> <description> 
##  
## 0.3 </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.NumberOfColors (deprecated) </term> <description> 
##  
## Seven </description> </item> 
## 
## <item><term> 
##  
## NumberOfContourLines (deprecated) </term> <description> 
##  
## 8 </description> </item> 
## 
## <item><term> 
##  
## SpikeLength (deprecated) </term> <description> 
##  
## 25.4 (millimeters part), 1.0 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX11.0.0  <br> 
## 
##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1 NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1@endlink  instead.  <br> 

class RadiusAnalysisBuilder(NXOpen.Builder): 
    """ Represents a Radius Analysis builder. """


    ##  The display type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Fringe</term><description> 
    ##  Display in fringe. </description> </item><item><term> 
    ## Hedgehog</term><description> 
    ##  Display in hedgehog. </description> </item><item><term> 
    ## ContourLines</term><description> 
    ##  Display in contour lines. </description> </item></list>
    class DisplayModes(Enum):
        """
        Members Include: <Fringe> <Hedgehog> <ContourLines>
        """
        Fringe: int
        Hedgehog: int
        ContourLines: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RadiusAnalysisBuilder.DisplayModes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the radius type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Gaussian</term><description> 
    ##  Gaussian radius. </description> </item><item><term> 
    ## Minimum</term><description> 
    ##  Minimum radius. </description> </item><item><term> 
    ## Maximum</term><description> 
    ##  Maximum radius. </description> </item><item><term> 
    ## Mean</term><description> 
    ##  Mean radius. </description> </item><item><term> 
    ## Normal</term><description> 
    ##  Normal radius. </description> </item><item><term> 
    ## Sectional</term><description> 
    ##  Sectional radius. </description> </item><item><term> 
    ## U</term><description> 
    ##  Radius in U direction. </description> </item><item><term> 
    ## V</term><description> 
    ##  Radius in V direction. </description> </item></list>
    class Types(Enum):
        """
        Members Include: <Gaussian> <Minimum> <Maximum> <Mean> <Normal> <Sectional> <U> <V>
        """
        Gaussian: int
        Minimum: int
        Maximum: int
        Mean: int
        Normal: int
        Sectional: int
        U: int
        V: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RadiusAnalysisBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link FaceAnalysisDataRangeBuilder NXOpen.GeometricAnalysis.FaceAnalysisDataRangeBuilder@endlink) DataRange
    ##  Returns the radius analysis data range.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1 NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1@endlink  instead.  <br> 

    ## @return FaceAnalysisDataRangeBuilder
    @property
    def DataRange(self) -> FaceAnalysisDataRangeBuilder:
        """
        Getter for property: (@link FaceAnalysisDataRangeBuilder NXOpen.GeometricAnalysis.FaceAnalysisDataRangeBuilder@endlink) DataRange
         Returns the radius analysis data range.  
             
         
        """
        pass
    
    ## Getter for property: (@link RadiusAnalysisBuilder.DisplayModes NXOpen.GeometricAnalysis.RadiusAnalysisBuilder.DisplayModes@endlink) DisplayMode
    ##  Returns the display mode.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1 NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1@endlink  instead.  <br> 

    ## @return RadiusAnalysisBuilder.DisplayModes
    @property
    def DisplayMode(self) -> RadiusAnalysisBuilder.DisplayModes:
        """
        Getter for property: (@link RadiusAnalysisBuilder.DisplayModes NXOpen.GeometricAnalysis.RadiusAnalysisBuilder.DisplayModes@endlink) DisplayMode
         Returns the display mode.  
             
         
        """
        pass
    
    ## Setter for property: (@link RadiusAnalysisBuilder.DisplayModes NXOpen.GeometricAnalysis.RadiusAnalysisBuilder.DisplayModes@endlink) DisplayMode

    ##  Returns the display mode.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1 NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1@endlink  instead.  <br> 

    @DisplayMode.setter
    def DisplayMode(self, displayMode: RadiusAnalysisBuilder.DisplayModes):
        """
        Setter for property: (@link RadiusAnalysisBuilder.DisplayModes NXOpen.GeometricAnalysis.RadiusAnalysisBuilder.DisplayModes@endlink) DisplayMode
         Returns the display mode.  
             
         
        """
        pass
    
    ## Getter for property: (@link FaceAnalysisDisplayBuilder NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilder@endlink) DisplaySettings
    ##  Returns the radius analysis display settings.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1 NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1@endlink  instead.  <br> 

    ## @return FaceAnalysisDisplayBuilder
    @property
    def DisplaySettings(self) -> FaceAnalysisDisplayBuilder:
        """
        Getter for property: (@link FaceAnalysisDisplayBuilder NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilder@endlink) DisplaySettings
         Returns the radius analysis display settings.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Features.GeometricConstraintDataManager NXOpen.Features.GeometricConstraintDataManager@endlink) DynamicLabel
    ##  Returns the dynamic label   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1 NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1@endlink  instead.  <br> 

    ## @return NXOpen.Features.GeometricConstraintDataManager
    @property
    def DynamicLabel(self) -> NXOpen.Features.GeometricConstraintDataManager:
        """
        Getter for property: (@link NXOpen.Features.GeometricConstraintDataManager NXOpen.Features.GeometricConstraintDataManager@endlink) DynamicLabel
         Returns the dynamic label   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Faces
    ##  Returns the face to apply radius analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1 NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1@endlink  instead.  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def Faces(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Faces
         Returns the face to apply radius analysis.  
             
         
        """
        pass
    
    ## Getter for property: (@link FaceAnalysisNormalsBuilder NXOpen.GeometricAnalysis.FaceAnalysisNormalsBuilder@endlink) Normals
    ##  Returns the radius analysis normals.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1 NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1@endlink  instead.  <br> 

    ## @return FaceAnalysisNormalsBuilder
    @property
    def Normals(self) -> FaceAnalysisNormalsBuilder:
        """
        Getter for property: (@link FaceAnalysisNormalsBuilder NXOpen.GeometricAnalysis.FaceAnalysisNormalsBuilder@endlink) Normals
         Returns the radius analysis normals.  
             
         
        """
        pass
    
    ## Getter for property: (int) NumberOfContourLines
    ##  Returns the number of contour lines.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1 NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1@endlink  instead.  <br> 

    ## @return int
    @property
    def NumberOfContourLines(self) -> int:
        """
        Getter for property: (int) NumberOfContourLines
         Returns the number of contour lines.  
             
         
        """
        pass
    
    ## Setter for property: (int) NumberOfContourLines

    ##  Returns the number of contour lines.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1 NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1@endlink  instead.  <br> 

    @NumberOfContourLines.setter
    def NumberOfContourLines(self, numberOfContourLines: int):
        """
        Setter for property: (int) NumberOfContourLines
         Returns the number of contour lines.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane
    ##  Returns the reference plane used for @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder::TypesSectional NXOpen::GeometricAnalysis::RadiusAnalysisBuilder::TypesSectional@endlink .  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1 NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1@endlink  instead.  <br> 

    ## @return NXOpen.Plane
    @property
    def Plane(self) -> NXOpen.Plane:
        """
        Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane
         Returns the reference plane used for @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder::TypesSectional NXOpen::GeometricAnalysis::RadiusAnalysisBuilder::TypesSectional@endlink .  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane

    ##  Returns the reference plane used for @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder::TypesSectional NXOpen::GeometricAnalysis::RadiusAnalysisBuilder::TypesSectional@endlink .  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1 NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1@endlink  instead.  <br> 

    @Plane.setter
    def Plane(self, plane: NXOpen.Plane):
        """
        Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane
         Returns the reference plane used for @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder::TypesSectional NXOpen::GeometricAnalysis::RadiusAnalysisBuilder::TypesSectional@endlink .  
             
         
        """
        pass
    
    ## Getter for property: (float) SpikeLength
    ##  Returns the spike length.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1 NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1@endlink  instead.  <br> 

    ## @return float
    @property
    def SpikeLength(self) -> float:
        """
        Getter for property: (float) SpikeLength
         Returns the spike length.  
             
         
        """
        pass
    
    ## Setter for property: (float) SpikeLength

    ##  Returns the spike length.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1 NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1@endlink  instead.  <br> 

    @SpikeLength.setter
    def SpikeLength(self, spikeLength: float):
        """
        Setter for property: (float) SpikeLength
         Returns the spike length.  
             
         
        """
        pass
    
    ## Getter for property: (@link RadiusAnalysisBuilder.Types NXOpen.GeometricAnalysis.RadiusAnalysisBuilder.Types@endlink) Type
    ##  Returns the radius type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1 NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1@endlink  instead.  <br> 

    ## @return RadiusAnalysisBuilder.Types
    @property
    def Type(self) -> RadiusAnalysisBuilder.Types:
        """
        Getter for property: (@link RadiusAnalysisBuilder.Types NXOpen.GeometricAnalysis.RadiusAnalysisBuilder.Types@endlink) Type
         Returns the radius type.  
             
         
        """
        pass
    
    ## Setter for property: (@link RadiusAnalysisBuilder.Types NXOpen.GeometricAnalysis.RadiusAnalysisBuilder.Types@endlink) Type

    ##  Returns the radius type.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1 NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1@endlink  instead.  <br> 

    @Type.setter
    def Type(self, type: RadiusAnalysisBuilder.Types):
        """
        Setter for property: (@link RadiusAnalysisBuilder.Types NXOpen.GeometricAnalysis.RadiusAnalysisBuilder.Types@endlink) Type
         Returns the radius type.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector
    ##  Returns the reference vector for @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder::TypesNormal NXOpen::GeometricAnalysis::RadiusAnalysisBuilder::TypesNormal@endlink .  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1 NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1@endlink  instead.  <br> 

    ## @return NXOpen.Direction
    @property
    def Vector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector
         Returns the reference vector for @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder::TypesNormal NXOpen::GeometricAnalysis::RadiusAnalysisBuilder::TypesNormal@endlink .  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector

    ##  Returns the reference vector for @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder::TypesNormal NXOpen::GeometricAnalysis::RadiusAnalysisBuilder::TypesNormal@endlink .  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1 NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1@endlink  instead.  <br> 

    @Vector.setter
    def Vector(self, vector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector
         Returns the reference vector for @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder::TypesNormal NXOpen::GeometricAnalysis::RadiusAnalysisBuilder::TypesNormal@endlink .  
             
         
        """
        pass
    
    ##  Start radius analysis. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1 NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1@endlink  instead.  <br> 

    ## License requirements: None.
    def StartRadiusAnalysis(self) -> None:
        """
         Start radius analysis. 
        """
        pass
    
    ##  Update display after plane changes. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1 NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1@endlink  instead.  <br> 

    ## License requirements: None.
    def UpdateDisplayOnPlaneChange(self) -> None:
        """
         Update display after plane changes. 
        """
        pass
    
##  Represents a Radius analysis   <br> To create or edit an instance of this class, use @link NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1  NXOpen::GeometricAnalysis::RadiusAnalysisBuilder1 @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class RadiusAnalysis(AnalysisObject): 
    """ Represents a Radius analysis  """
    pass


import NXOpen
import NXOpen.GeometricUtilities
##  Represents a Reflection Analysis builder.  <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisObjectCollectionEx::CreateReflectionAnalysisBuilder1  NXOpen::GeometricAnalysis::AnalysisObjectCollectionEx::CreateReflectionAnalysisBuilder1 @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DisplayResolution.AngleTolerance </term> <description> 
##  
## 15.0 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolution.EdgeTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolution.FaceTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolution.Resolution </term> <description> 
##  
## Standard </description> </item> 
## 
## <item><term> 
##  
## DisplayResolution.WidthTolerance </term> <description> 
##  
## 0.3 </description> </item> 
## 
## <item><term> 
##  
## FaceReflectivityScale </term> <description> 
##  
## 100 </description> </item> 
## 
## <item><term> 
##  
## ImagePosition </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## LineNumber </term> <description> 
##  
## ThirtyTwo </description> </item> 
## 
## <item><term> 
##  
## ShowFacetEdge </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2312.0.0  <br> 

class ReflectionAnalysisBuilder1(NXOpen.Builder): 
    """ Represents a Reflection Analysis builder. """


    ##  The type of image movement. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Horizontal</term><description> 
    ##  Move image in horizonal direction. </description> </item><item><term> 
    ## Vertical</term><description> 
    ##  Move image in vertical direction. </description> </item><item><term> 
    ## Rotate</term><description> 
    ##  Rotate image. </description> </item></list>
    class ImageMovementTypes(Enum):
        """
        Members Include: <Horizontal> <Vertical> <Rotate>
        """
        Horizontal: int
        Vertical: int
        Rotate: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder1.ImageMovementTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The reflection image size option. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## KeepCurrent</term><description> 
    ##  Keep current size. </description> </item><item><term> 
    ## ReduceScale</term><description> 
    ##  Reduce scale size. </description> </item></list>
    class ImageSizeOption(Enum):
        """
        Members Include: <KeepCurrent> <ReduceScale>
        """
        KeepCurrent: int
        ReduceScale: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder1.ImageSizeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The line image types. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## BlackLines</term><description> 
    ##  Black lines. </description> </item><item><term> 
    ## BlackandWhiteLines</term><description> 
    ##  Black and lines. </description> </item><item><term> 
    ## ColoredLines</term><description> 
    ##  Colored lines. </description> </item></list>
    class LineImageTypes(Enum):
        """
        Members Include: <BlackLines> <BlackandWhiteLines> <ColoredLines>
        """
        BlackLines: int
        BlackandWhiteLines: int
        ColoredLines: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder1.LineImageTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The reflection line orientation. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Horizontal</term><description> 
    ##  Horizontal. </description> </item><item><term> 
    ## Vertical</term><description> 
    ##  Vertical. </description> </item><item><term> 
    ## Both</term><description> 
    ##  Both horizontal and vertical. </description> </item></list>
    class LineOrientationType(Enum):
        """
        Members Include: <Horizontal> <Vertical> <Both>
        """
        Horizontal: int
        Vertical: int
        Both: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder1.LineOrientationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The reflection line thickness. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Thin</term><description> 
    ##  Thin. </description> </item><item><term> 
    ## Normal</term><description> 
    ##  Normal. </description> </item><item><term> 
    ## Thick</term><description> 
    ##  Thick. </description> </item></list>
    class LineThicknessType(Enum):
        """
        Members Include: <Thin> <Normal> <Thick>
        """
        Thin: int
        Normal: int
        Thick: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder1.LineThicknessType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The number of reflection lines. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## One</term><description> 
    ##  1 reflection line. </description> </item><item><term> 
    ## Two</term><description> 
    ##  2 reflection line. </description> </item><item><term> 
    ## Four</term><description> 
    ##  4 reflection line. </description> </item><item><term> 
    ## Eight</term><description> 
    ##  8 reflection line. </description> </item><item><term> 
    ## Sixteen</term><description> 
    ##  16 reflection line. </description> </item><item><term> 
    ## ThirtyTwo</term><description> 
    ##  32 reflection line. </description> </item><item><term> 
    ## SixtyFour</term><description> 
    ##  64 reflection line. </description> </item><item><term> 
    ## OneTwoEight</term><description> 
    ##  128 reflection line. </description> </item><item><term> 
    ## TwoFiveSix</term><description> 
    ##  256 reflection line. </description> </item></list>
    class NumberOfLinesOptions(Enum):
        """
        Members Include: <One> <Two> <Four> <Eight> <Sixteen> <ThirtyTwo> <SixtyFour> <OneTwoEight> <TwoFiveSix>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder1.NumberOfLinesOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The reflection scene images. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SimulatedHorizon</term><description> 
    ##  Simulated horizon. </description> </item><item><term> 
    ## PhotoHorizon</term><description> 
    ##  Photo horizon. </description> </item><item><term> 
    ## SphericalRoom</term><description> 
    ##  Spherical room. </description> </item><item><term> 
    ## SphericalLightTubesRoom</term><description> 
    ##  Spherical light tubes room. </description> </item><item><term> 
    ## DaytimeHorizon</term><description> 
    ##  Daytime horizon. </description> </item><item><term> 
    ## MagentaSunset</term><description> 
    ##  Magenta sunset. </description> </item><item><term> 
    ## SphericalHorizon</term><description> 
    ##  Spherical horizon. </description> </item><item><term> 
    ## CylindricalRoom</term><description> 
    ##  Cylindrical room. </description> </item><item><term> 
    ## MonochromeHorizon</term><description> 
    ##  Monochrome horizon. </description> </item><item><term> 
    ## SmoothGrayScale</term><description> 
    ##  Smooth gray scale. </description> </item><item><term> 
    ## SharpGrayScale</term><description> 
    ##  Sharp gray scale. </description> </item><item><term> 
    ## SphericalTubes</term><description> 
    ##  Spherical tubes. </description> </item></list>
    class SceneImageType(Enum):
        """
        Members Include: <SimulatedHorizon> <PhotoHorizon> <SphericalRoom> <SphericalLightTubesRoom> <DaytimeHorizon> <MagentaSunset> <SphericalHorizon> <CylindricalRoom> <MonochromeHorizon> <SmoothGrayScale> <SharpGrayScale> <SphericalTubes>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder1.SceneImageType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The types of images. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## LineImages</term><description> 
    ##  Line image. </description> </item><item><term> 
    ## SceneImages</term><description> 
    ##  Scene image. </description> </item><item><term> 
    ## ImageFromFile</term><description> 
    ##  Image from file. </description> </item></list>
    class Types(Enum):
        """
        Members Include: <LineImages> <SceneImages> <ImageFromFile>
        """
        LineImages: int
        SceneImages: int
        ImageFromFile: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder1.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.DisplayResolutionBuilder NXOpen.GeometricUtilities.DisplayResolutionBuilder@endlink) DisplayResolution
    ##  Returns the display resolution.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.DisplayResolutionBuilder
    @property
    def DisplayResolution(self) -> NXOpen.GeometricUtilities.DisplayResolutionBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.DisplayResolutionBuilder NXOpen.GeometricUtilities.DisplayResolutionBuilder@endlink) DisplayResolution
         Returns the display resolution.  
             
         
        """
        pass
    
    ## Getter for property: (int) FaceReflectivityScale
    ##  Returns the face reflectivity scale from 0 to 100.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return int
    @property
    def FaceReflectivityScale(self) -> int:
        """
        Getter for property: (int) FaceReflectivityScale
         Returns the face reflectivity scale from 0 to 100.  
             
         
        """
        pass
    
    ## Setter for property: (int) FaceReflectivityScale

    ##  Returns the face reflectivity scale from 0 to 100.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @FaceReflectivityScale.setter
    def FaceReflectivityScale(self, faceReflectivityScale: int):
        """
        Setter for property: (int) FaceReflectivityScale
         Returns the face reflectivity scale from 0 to 100.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Faces
    ##  Returns the face to apply reflection analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def Faces(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Faces
         Returns the face to apply reflection analysis.  
             
         
        """
        pass
    
    ## Getter for property: (str) FileName
    ##  Returns the file browser.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return str
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
         Returns the file browser.  
             
         
        """
        pass
    
    ## Setter for property: (str) FileName

    ##  Returns the file browser.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @FileName.setter
    def FileName(self, filename: str):
        """
        Setter for property: (str) FileName
         Returns the file browser.  
             
         
        """
        pass
    
    ## Getter for property: (@link ReflectionAnalysisBuilder1.ImageMovementTypes NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.ImageMovementTypes@endlink) ImageMovementType
    ##  Returns the orientation to move reflection lines.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return ReflectionAnalysisBuilder1.ImageMovementTypes
    @property
    def ImageMovementType(self) -> ReflectionAnalysisBuilder1.ImageMovementTypes:
        """
        Getter for property: (@link ReflectionAnalysisBuilder1.ImageMovementTypes NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.ImageMovementTypes@endlink) ImageMovementType
         Returns the orientation to move reflection lines.  
             
         
        """
        pass
    
    ## Setter for property: (@link ReflectionAnalysisBuilder1.ImageMovementTypes NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.ImageMovementTypes@endlink) ImageMovementType

    ##  Returns the orientation to move reflection lines.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @ImageMovementType.setter
    def ImageMovementType(self, imageMovementType: ReflectionAnalysisBuilder1.ImageMovementTypes):
        """
        Setter for property: (@link ReflectionAnalysisBuilder1.ImageMovementTypes NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.ImageMovementTypes@endlink) ImageMovementType
         Returns the orientation to move reflection lines.  
             
         
        """
        pass
    
    ## Getter for property: (int) ImagePosition
    ##  Returns the moving image scale.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return int
    @property
    def ImagePosition(self) -> int:
        """
        Getter for property: (int) ImagePosition
         Returns the moving image scale.  
             
         
        """
        pass
    
    ## Setter for property: (int) ImagePosition

    ##  Returns the moving image scale.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @ImagePosition.setter
    def ImagePosition(self, imagePosition: int):
        """
        Setter for property: (int) ImagePosition
         Returns the moving image scale.  
             
         
        """
        pass
    
    ## Getter for property: (@link ReflectionAnalysisBuilder1.ImageSizeOption NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.ImageSizeOption@endlink) ImageSizeSetting
    ##  Returns the image size setting.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return ReflectionAnalysisBuilder1.ImageSizeOption
    @property
    def ImageSizeSetting(self) -> ReflectionAnalysisBuilder1.ImageSizeOption:
        """
        Getter for property: (@link ReflectionAnalysisBuilder1.ImageSizeOption NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.ImageSizeOption@endlink) ImageSizeSetting
         Returns the image size setting.  
             
         
        """
        pass
    
    ## Setter for property: (@link ReflectionAnalysisBuilder1.ImageSizeOption NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.ImageSizeOption@endlink) ImageSizeSetting

    ##  Returns the image size setting.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @ImageSizeSetting.setter
    def ImageSizeSetting(self, imageSizeSetting: ReflectionAnalysisBuilder1.ImageSizeOption):
        """
        Setter for property: (@link ReflectionAnalysisBuilder1.ImageSizeOption NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.ImageSizeOption@endlink) ImageSizeSetting
         Returns the image size setting.  
             
         
        """
        pass
    
    ## Getter for property: (@link ReflectionAnalysisBuilder1.LineImageTypes NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.LineImageTypes@endlink) LineImageType
    ##  Returns the image type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return ReflectionAnalysisBuilder1.LineImageTypes
    @property
    def LineImageType(self) -> ReflectionAnalysisBuilder1.LineImageTypes:
        """
        Getter for property: (@link ReflectionAnalysisBuilder1.LineImageTypes NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.LineImageTypes@endlink) LineImageType
         Returns the image type.  
             
         
        """
        pass
    
    ## Setter for property: (@link ReflectionAnalysisBuilder1.LineImageTypes NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.LineImageTypes@endlink) LineImageType

    ##  Returns the image type.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @LineImageType.setter
    def LineImageType(self, lineImageType: ReflectionAnalysisBuilder1.LineImageTypes):
        """
        Setter for property: (@link ReflectionAnalysisBuilder1.LineImageTypes NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.LineImageTypes@endlink) LineImageType
         Returns the image type.  
             
         
        """
        pass
    
    ## Getter for property: (@link ReflectionAnalysisBuilder1.NumberOfLinesOptions NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.NumberOfLinesOptions@endlink) LineNumber
    ##  Returns the reflection line number.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return ReflectionAnalysisBuilder1.NumberOfLinesOptions
    @property
    def LineNumber(self) -> ReflectionAnalysisBuilder1.NumberOfLinesOptions:
        """
        Getter for property: (@link ReflectionAnalysisBuilder1.NumberOfLinesOptions NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.NumberOfLinesOptions@endlink) LineNumber
         Returns the reflection line number.  
             
         
        """
        pass
    
    ## Setter for property: (@link ReflectionAnalysisBuilder1.NumberOfLinesOptions NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.NumberOfLinesOptions@endlink) LineNumber

    ##  Returns the reflection line number.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @LineNumber.setter
    def LineNumber(self, lineNumber: ReflectionAnalysisBuilder1.NumberOfLinesOptions):
        """
        Setter for property: (@link ReflectionAnalysisBuilder1.NumberOfLinesOptions NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.NumberOfLinesOptions@endlink) LineNumber
         Returns the reflection line number.  
             
         
        """
        pass
    
    ## Getter for property: (@link ReflectionAnalysisBuilder1.LineOrientationType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.LineOrientationType@endlink) LineOrientation
    ##  Returns the reflection line orientation.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return ReflectionAnalysisBuilder1.LineOrientationType
    @property
    def LineOrientation(self) -> ReflectionAnalysisBuilder1.LineOrientationType:
        """
        Getter for property: (@link ReflectionAnalysisBuilder1.LineOrientationType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.LineOrientationType@endlink) LineOrientation
         Returns the reflection line orientation.  
             
         
        """
        pass
    
    ## Setter for property: (@link ReflectionAnalysisBuilder1.LineOrientationType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.LineOrientationType@endlink) LineOrientation

    ##  Returns the reflection line orientation.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @LineOrientation.setter
    def LineOrientation(self, lineOrientation: ReflectionAnalysisBuilder1.LineOrientationType):
        """
        Setter for property: (@link ReflectionAnalysisBuilder1.LineOrientationType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.LineOrientationType@endlink) LineOrientation
         Returns the reflection line orientation.  
             
         
        """
        pass
    
    ## Getter for property: (@link ReflectionAnalysisBuilder1.LineThicknessType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.LineThicknessType@endlink) LineThickness
    ##  Returns the reflection line thickness.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return ReflectionAnalysisBuilder1.LineThicknessType
    @property
    def LineThickness(self) -> ReflectionAnalysisBuilder1.LineThicknessType:
        """
        Getter for property: (@link ReflectionAnalysisBuilder1.LineThicknessType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.LineThicknessType@endlink) LineThickness
         Returns the reflection line thickness.  
             
         
        """
        pass
    
    ## Setter for property: (@link ReflectionAnalysisBuilder1.LineThicknessType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.LineThicknessType@endlink) LineThickness

    ##  Returns the reflection line thickness.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @LineThickness.setter
    def LineThickness(self, lineThickness: ReflectionAnalysisBuilder1.LineThicknessType):
        """
        Setter for property: (@link ReflectionAnalysisBuilder1.LineThicknessType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.LineThicknessType@endlink) LineThickness
         Returns the reflection line thickness.  
             
         
        """
        pass
    
    ## Getter for property: (@link FaceAnalysisNormalsBuilder NXOpen.GeometricAnalysis.FaceAnalysisNormalsBuilder@endlink) Normals
    ##  Returns the reflection analysis normals.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return FaceAnalysisNormalsBuilder
    @property
    def Normals(self) -> FaceAnalysisNormalsBuilder:
        """
        Getter for property: (@link FaceAnalysisNormalsBuilder NXOpen.GeometricAnalysis.FaceAnalysisNormalsBuilder@endlink) Normals
         Returns the reflection analysis normals.  
             
         
        """
        pass
    
    ## Getter for property: (@link ReflectionAnalysisBuilder1.SceneImageType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.SceneImageType@endlink) SceneImageOption
    ##  Returns the scene image option.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return ReflectionAnalysisBuilder1.SceneImageType
    @property
    def SceneImageOption(self) -> ReflectionAnalysisBuilder1.SceneImageType:
        """
        Getter for property: (@link ReflectionAnalysisBuilder1.SceneImageType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.SceneImageType@endlink) SceneImageOption
         Returns the scene image option.  
             
         
        """
        pass
    
    ## Setter for property: (@link ReflectionAnalysisBuilder1.SceneImageType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.SceneImageType@endlink) SceneImageOption

    ##  Returns the scene image option.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @SceneImageOption.setter
    def SceneImageOption(self, sceneImageOption: ReflectionAnalysisBuilder1.SceneImageType):
        """
        Setter for property: (@link ReflectionAnalysisBuilder1.SceneImageType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.SceneImageType@endlink) SceneImageOption
         Returns the scene image option.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ShowFacetEdge
    ##  Returns the flag indicating if facet edges should be shown.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def ShowFacetEdge(self) -> bool:
        """
        Getter for property: (bool) ShowFacetEdge
         Returns the flag indicating if facet edges should be shown.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ShowFacetEdge

    ##  Returns the flag indicating if facet edges should be shown.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @ShowFacetEdge.setter
    def ShowFacetEdge(self, showFacetEdge: bool):
        """
        Setter for property: (bool) ShowFacetEdge
         Returns the flag indicating if facet edges should be shown.  
             
         
        """
        pass
    
    ## Getter for property: (@link ReflectionAnalysisBuilder1.Types NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.Types@endlink) Type
    ##  Returns the reflection analysis type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return ReflectionAnalysisBuilder1.Types
    @property
    def Type(self) -> ReflectionAnalysisBuilder1.Types:
        """
        Getter for property: (@link ReflectionAnalysisBuilder1.Types NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.Types@endlink) Type
         Returns the reflection analysis type.  
             
         
        """
        pass
    
    ## Setter for property: (@link ReflectionAnalysisBuilder1.Types NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.Types@endlink) Type

    ##  Returns the reflection analysis type.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @Type.setter
    def Type(self, type: ReflectionAnalysisBuilder1.Types):
        """
        Setter for property: (@link ReflectionAnalysisBuilder1.Types NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.Types@endlink) Type
         Returns the reflection analysis type.  
             
         
        """
        pass
    
    ##  Start reflection analysis. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def StartReflectionAnalysis(self) -> None:
        """
         Start reflection analysis. 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a Reflection Analysis builder.  <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisObjectCollectionEx::CreateReflectionAnalysisBuilder  NXOpen::GeometricAnalysis::AnalysisObjectCollectionEx::CreateReflectionAnalysisBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DisplayResolution.AngleTolerance (deprecated) </term> <description> 
##  
## 15.0 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolution.EdgeTolerance (deprecated) </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolution.FaceTolerance (deprecated) </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplayResolution.Resolution (deprecated) </term> <description> 
##  
## Standard </description> </item> 
## 
## <item><term> 
##  
## DisplayResolution.WidthTolerance (deprecated) </term> <description> 
##  
## 0.3 </description> </item> 
## 
## <item><term> 
##  
## FaceReflectivityScale (deprecated) </term> <description> 
##  
## 100 </description> </item> 
## 
## <item><term> 
##  
## ImagePosition (deprecated) </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## LineNumber (deprecated) </term> <description> 
##  
## ThirtyTwo </description> </item> 
## 
## <item><term> 
##  
## ShowFacetEdge (deprecated) </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX11.0.0  <br> 
## 
##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1 NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1@endlink  instead.  <br> 

class ReflectionAnalysisBuilder(NXOpen.Builder): 
    """ Represents a Reflection Analysis builder. """


    ##  The type of image movement. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Horizontal</term><description> 
    ##  Move image in horizonal direction. </description> </item><item><term> 
    ## Vertical</term><description> 
    ##  Move image in vertical direction. </description> </item><item><term> 
    ## Rotate</term><description> 
    ##  Rotate image. </description> </item></list>
    class ImageMovementTypes(Enum):
        """
        Members Include: <Horizontal> <Vertical> <Rotate>
        """
        Horizontal: int
        Vertical: int
        Rotate: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder.ImageMovementTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The reflection image size option. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## KeepCurrent</term><description> 
    ##  Keep current size. </description> </item><item><term> 
    ## ReduceScale</term><description> 
    ##  Reduce scale size. </description> </item></list>
    class ImageSizeOption(Enum):
        """
        Members Include: <KeepCurrent> <ReduceScale>
        """
        KeepCurrent: int
        ReduceScale: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder.ImageSizeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The line image types. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## BlackLines</term><description> 
    ##  Black lines. </description> </item><item><term> 
    ## BlackandWhiteLines</term><description> 
    ##  Black and lines. </description> </item><item><term> 
    ## ColoredLines</term><description> 
    ##  Colored lines. </description> </item></list>
    class LineImageTypes(Enum):
        """
        Members Include: <BlackLines> <BlackandWhiteLines> <ColoredLines>
        """
        BlackLines: int
        BlackandWhiteLines: int
        ColoredLines: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder.LineImageTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The reflection line orientation. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Horizontal</term><description> 
    ##  Horizontal. </description> </item><item><term> 
    ## Vertical</term><description> 
    ##  Vertical. </description> </item><item><term> 
    ## Both</term><description> 
    ##  Both horizontal and vertical. </description> </item></list>
    class LineOrientationType(Enum):
        """
        Members Include: <Horizontal> <Vertical> <Both>
        """
        Horizontal: int
        Vertical: int
        Both: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder.LineOrientationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The reflection line thickness. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Thin</term><description> 
    ##  Thin. </description> </item><item><term> 
    ## Normal</term><description> 
    ##  Normal. </description> </item><item><term> 
    ## Thick</term><description> 
    ##  Thick. </description> </item></list>
    class LineThicknessType(Enum):
        """
        Members Include: <Thin> <Normal> <Thick>
        """
        Thin: int
        Normal: int
        Thick: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder.LineThicknessType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The number of reflection lines. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## One</term><description> 
    ##  1 reflection line. </description> </item><item><term> 
    ## Two</term><description> 
    ##  2 reflection line. </description> </item><item><term> 
    ## Four</term><description> 
    ##  4 reflection line. </description> </item><item><term> 
    ## Eight</term><description> 
    ##  8 reflection line. </description> </item><item><term> 
    ## Sixteen</term><description> 
    ##  16 reflection line. </description> </item><item><term> 
    ## ThirtyTwo</term><description> 
    ##  32 reflection line. </description> </item><item><term> 
    ## SixtyFour</term><description> 
    ##  64 reflection line. </description> </item><item><term> 
    ## OneTwoEight</term><description> 
    ##  128 reflection line. </description> </item><item><term> 
    ## TwoFiveSix</term><description> 
    ##  256 reflection line. </description> </item></list>
    class NumberOfLinesOptions(Enum):
        """
        Members Include: <One> <Two> <Four> <Eight> <Sixteen> <ThirtyTwo> <SixtyFour> <OneTwoEight> <TwoFiveSix>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder.NumberOfLinesOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The reflection scene images. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SimulatedHorizon</term><description> 
    ##  Simulated horizon. </description> </item><item><term> 
    ## PhotoHorizon</term><description> 
    ##  Photo horizon. </description> </item><item><term> 
    ## SphericalRoom</term><description> 
    ##  Spherical room. </description> </item><item><term> 
    ## SphericalLightTubesRoom</term><description> 
    ##  Spherical light tubes room. </description> </item><item><term> 
    ## DaytimeHorizon</term><description> 
    ##  Daytime horizon. </description> </item><item><term> 
    ## MagentaSunset</term><description> 
    ##  Magenta sunset. </description> </item><item><term> 
    ## SphericalHorizon</term><description> 
    ##  Spherical horizon. </description> </item><item><term> 
    ## CylindricalRoom</term><description> 
    ##  Cylindrical room. </description> </item><item><term> 
    ## MonochromeHorizon</term><description> 
    ##  Monochrome horizon. </description> </item><item><term> 
    ## SmoothGrayScale</term><description> 
    ##  Smooth gray scale. </description> </item><item><term> 
    ## SharpGrayScale</term><description> 
    ##  Sharp gray scale. </description> </item><item><term> 
    ## SphericalTubes</term><description> 
    ##  Spherical tubes. </description> </item></list>
    class SceneImageType(Enum):
        """
        Members Include: <SimulatedHorizon> <PhotoHorizon> <SphericalRoom> <SphericalLightTubesRoom> <DaytimeHorizon> <MagentaSunset> <SphericalHorizon> <CylindricalRoom> <MonochromeHorizon> <SmoothGrayScale> <SharpGrayScale> <SphericalTubes>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder.SceneImageType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The types of images. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## LineImages</term><description> 
    ##  Line image. </description> </item><item><term> 
    ## SceneImages</term><description> 
    ##  Scene image. </description> </item><item><term> 
    ## ImageFromFile</term><description> 
    ##  Image from file. </description> </item></list>
    class Types(Enum):
        """
        Members Include: <LineImages> <SceneImages> <ImageFromFile>
        """
        LineImages: int
        SceneImages: int
        ImageFromFile: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ReflectionAnalysisBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.DisplayResolutionBuilder NXOpen.GeometricUtilities.DisplayResolutionBuilder@endlink) DisplayResolution
    ##  Returns the display resolution.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1 NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1@endlink  instead.  <br> 

    ## @return NXOpen.GeometricUtilities.DisplayResolutionBuilder
    @property
    def DisplayResolution(self) -> NXOpen.GeometricUtilities.DisplayResolutionBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.DisplayResolutionBuilder NXOpen.GeometricUtilities.DisplayResolutionBuilder@endlink) DisplayResolution
         Returns the display resolution.  
             
         
        """
        pass
    
    ## Getter for property: (int) FaceReflectivityScale
    ##  Returns the face reflectivity scale from 0 to 100.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1 NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1@endlink  instead.  <br> 

    ## @return int
    @property
    def FaceReflectivityScale(self) -> int:
        """
        Getter for property: (int) FaceReflectivityScale
         Returns the face reflectivity scale from 0 to 100.  
             
         
        """
        pass
    
    ## Setter for property: (int) FaceReflectivityScale

    ##  Returns the face reflectivity scale from 0 to 100.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1 NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1@endlink  instead.  <br> 

    @FaceReflectivityScale.setter
    def FaceReflectivityScale(self, faceReflectivityScale: int):
        """
        Setter for property: (int) FaceReflectivityScale
         Returns the face reflectivity scale from 0 to 100.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Faces
    ##  Returns the face to apply reflection analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1 NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1@endlink  instead.  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def Faces(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Faces
         Returns the face to apply reflection analysis.  
             
         
        """
        pass
    
    ## Getter for property: (str) FileName
    ##  Returns the file browser.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1 NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1@endlink  instead.  <br> 

    ## @return str
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
         Returns the file browser.  
             
         
        """
        pass
    
    ## Setter for property: (str) FileName

    ##  Returns the file browser.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1 NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1@endlink  instead.  <br> 

    @FileName.setter
    def FileName(self, filename: str):
        """
        Setter for property: (str) FileName
         Returns the file browser.  
             
         
        """
        pass
    
    ## Getter for property: (@link ReflectionAnalysisBuilder.ImageMovementTypes NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.ImageMovementTypes@endlink) ImageMovementType
    ##  Returns the orientation to move reflection lines.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1 NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1@endlink  instead.  <br> 

    ## @return ReflectionAnalysisBuilder.ImageMovementTypes
    @property
    def ImageMovementType(self) -> ReflectionAnalysisBuilder.ImageMovementTypes:
        """
        Getter for property: (@link ReflectionAnalysisBuilder.ImageMovementTypes NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.ImageMovementTypes@endlink) ImageMovementType
         Returns the orientation to move reflection lines.  
             
         
        """
        pass
    
    ## Setter for property: (@link ReflectionAnalysisBuilder.ImageMovementTypes NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.ImageMovementTypes@endlink) ImageMovementType

    ##  Returns the orientation to move reflection lines.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1 NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1@endlink  instead.  <br> 

    @ImageMovementType.setter
    def ImageMovementType(self, imageMovementType: ReflectionAnalysisBuilder.ImageMovementTypes):
        """
        Setter for property: (@link ReflectionAnalysisBuilder.ImageMovementTypes NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.ImageMovementTypes@endlink) ImageMovementType
         Returns the orientation to move reflection lines.  
             
         
        """
        pass
    
    ## Getter for property: (int) ImagePosition
    ##  Returns the moving image scale.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1 NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1@endlink  instead.  <br> 

    ## @return int
    @property
    def ImagePosition(self) -> int:
        """
        Getter for property: (int) ImagePosition
         Returns the moving image scale.  
             
         
        """
        pass
    
    ## Setter for property: (int) ImagePosition

    ##  Returns the moving image scale.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1 NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1@endlink  instead.  <br> 

    @ImagePosition.setter
    def ImagePosition(self, imagePosition: int):
        """
        Setter for property: (int) ImagePosition
         Returns the moving image scale.  
             
         
        """
        pass
    
    ## Getter for property: (@link ReflectionAnalysisBuilder.ImageSizeOption NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.ImageSizeOption@endlink) ImageSizeSetting
    ##  Returns the image size setting.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1 NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1@endlink  instead.  <br> 

    ## @return ReflectionAnalysisBuilder.ImageSizeOption
    @property
    def ImageSizeSetting(self) -> ReflectionAnalysisBuilder.ImageSizeOption:
        """
        Getter for property: (@link ReflectionAnalysisBuilder.ImageSizeOption NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.ImageSizeOption@endlink) ImageSizeSetting
         Returns the image size setting.  
             
         
        """
        pass
    
    ## Setter for property: (@link ReflectionAnalysisBuilder.ImageSizeOption NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.ImageSizeOption@endlink) ImageSizeSetting

    ##  Returns the image size setting.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1 NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1@endlink  instead.  <br> 

    @ImageSizeSetting.setter
    def ImageSizeSetting(self, imageSizeSetting: ReflectionAnalysisBuilder.ImageSizeOption):
        """
        Setter for property: (@link ReflectionAnalysisBuilder.ImageSizeOption NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.ImageSizeOption@endlink) ImageSizeSetting
         Returns the image size setting.  
             
         
        """
        pass
    
    ## Getter for property: (@link ReflectionAnalysisBuilder.LineImageTypes NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.LineImageTypes@endlink) LineImageType
    ##  Returns the image type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1 NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1@endlink  instead.  <br> 

    ## @return ReflectionAnalysisBuilder.LineImageTypes
    @property
    def LineImageType(self) -> ReflectionAnalysisBuilder.LineImageTypes:
        """
        Getter for property: (@link ReflectionAnalysisBuilder.LineImageTypes NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.LineImageTypes@endlink) LineImageType
         Returns the image type.  
             
         
        """
        pass
    
    ## Setter for property: (@link ReflectionAnalysisBuilder.LineImageTypes NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.LineImageTypes@endlink) LineImageType

    ##  Returns the image type.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1 NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1@endlink  instead.  <br> 

    @LineImageType.setter
    def LineImageType(self, lineImageType: ReflectionAnalysisBuilder.LineImageTypes):
        """
        Setter for property: (@link ReflectionAnalysisBuilder.LineImageTypes NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.LineImageTypes@endlink) LineImageType
         Returns the image type.  
             
         
        """
        pass
    
    ## Getter for property: (@link ReflectionAnalysisBuilder.NumberOfLinesOptions NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.NumberOfLinesOptions@endlink) LineNumber
    ##  Returns the reflection line number.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1 NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1@endlink  instead.  <br> 

    ## @return ReflectionAnalysisBuilder.NumberOfLinesOptions
    @property
    def LineNumber(self) -> ReflectionAnalysisBuilder.NumberOfLinesOptions:
        """
        Getter for property: (@link ReflectionAnalysisBuilder.NumberOfLinesOptions NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.NumberOfLinesOptions@endlink) LineNumber
         Returns the reflection line number.  
             
         
        """
        pass
    
    ## Setter for property: (@link ReflectionAnalysisBuilder.NumberOfLinesOptions NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.NumberOfLinesOptions@endlink) LineNumber

    ##  Returns the reflection line number.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1 NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1@endlink  instead.  <br> 

    @LineNumber.setter
    def LineNumber(self, lineNumber: ReflectionAnalysisBuilder.NumberOfLinesOptions):
        """
        Setter for property: (@link ReflectionAnalysisBuilder.NumberOfLinesOptions NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.NumberOfLinesOptions@endlink) LineNumber
         Returns the reflection line number.  
             
         
        """
        pass
    
    ## Getter for property: (@link ReflectionAnalysisBuilder.LineOrientationType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.LineOrientationType@endlink) LineOrientation
    ##  Returns the reflection line orientation.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1 NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1@endlink  instead.  <br> 

    ## @return ReflectionAnalysisBuilder.LineOrientationType
    @property
    def LineOrientation(self) -> ReflectionAnalysisBuilder.LineOrientationType:
        """
        Getter for property: (@link ReflectionAnalysisBuilder.LineOrientationType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.LineOrientationType@endlink) LineOrientation
         Returns the reflection line orientation.  
             
         
        """
        pass
    
    ## Setter for property: (@link ReflectionAnalysisBuilder.LineOrientationType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.LineOrientationType@endlink) LineOrientation

    ##  Returns the reflection line orientation.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1 NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1@endlink  instead.  <br> 

    @LineOrientation.setter
    def LineOrientation(self, lineOrientation: ReflectionAnalysisBuilder.LineOrientationType):
        """
        Setter for property: (@link ReflectionAnalysisBuilder.LineOrientationType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.LineOrientationType@endlink) LineOrientation
         Returns the reflection line orientation.  
             
         
        """
        pass
    
    ## Getter for property: (@link ReflectionAnalysisBuilder.LineThicknessType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.LineThicknessType@endlink) LineThickness
    ##  Returns the reflection line thickness.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1 NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1@endlink  instead.  <br> 

    ## @return ReflectionAnalysisBuilder.LineThicknessType
    @property
    def LineThickness(self) -> ReflectionAnalysisBuilder.LineThicknessType:
        """
        Getter for property: (@link ReflectionAnalysisBuilder.LineThicknessType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.LineThicknessType@endlink) LineThickness
         Returns the reflection line thickness.  
             
         
        """
        pass
    
    ## Setter for property: (@link ReflectionAnalysisBuilder.LineThicknessType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.LineThicknessType@endlink) LineThickness

    ##  Returns the reflection line thickness.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1 NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1@endlink  instead.  <br> 

    @LineThickness.setter
    def LineThickness(self, lineThickness: ReflectionAnalysisBuilder.LineThicknessType):
        """
        Setter for property: (@link ReflectionAnalysisBuilder.LineThicknessType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.LineThicknessType@endlink) LineThickness
         Returns the reflection line thickness.  
             
         
        """
        pass
    
    ## Getter for property: (@link FaceAnalysisNormalsBuilder NXOpen.GeometricAnalysis.FaceAnalysisNormalsBuilder@endlink) Normals
    ##  Returns the reflection analysis normals.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1 NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1@endlink  instead.  <br> 

    ## @return FaceAnalysisNormalsBuilder
    @property
    def Normals(self) -> FaceAnalysisNormalsBuilder:
        """
        Getter for property: (@link FaceAnalysisNormalsBuilder NXOpen.GeometricAnalysis.FaceAnalysisNormalsBuilder@endlink) Normals
         Returns the reflection analysis normals.  
             
         
        """
        pass
    
    ## Getter for property: (@link ReflectionAnalysisBuilder.SceneImageType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.SceneImageType@endlink) SceneImageOption
    ##  Returns the scene image option.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1 NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1@endlink  instead.  <br> 

    ## @return ReflectionAnalysisBuilder.SceneImageType
    @property
    def SceneImageOption(self) -> ReflectionAnalysisBuilder.SceneImageType:
        """
        Getter for property: (@link ReflectionAnalysisBuilder.SceneImageType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.SceneImageType@endlink) SceneImageOption
         Returns the scene image option.  
             
         
        """
        pass
    
    ## Setter for property: (@link ReflectionAnalysisBuilder.SceneImageType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.SceneImageType@endlink) SceneImageOption

    ##  Returns the scene image option.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1 NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1@endlink  instead.  <br> 

    @SceneImageOption.setter
    def SceneImageOption(self, sceneImageOption: ReflectionAnalysisBuilder.SceneImageType):
        """
        Setter for property: (@link ReflectionAnalysisBuilder.SceneImageType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.SceneImageType@endlink) SceneImageOption
         Returns the scene image option.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ShowFacetEdge
    ##  Returns the flag indicating if facet edges should be shown.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1 NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1@endlink  instead.  <br> 

    ## @return bool
    @property
    def ShowFacetEdge(self) -> bool:
        """
        Getter for property: (bool) ShowFacetEdge
         Returns the flag indicating if facet edges should be shown.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ShowFacetEdge

    ##  Returns the flag indicating if facet edges should be shown.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1 NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1@endlink  instead.  <br> 

    @ShowFacetEdge.setter
    def ShowFacetEdge(self, showFacetEdge: bool):
        """
        Setter for property: (bool) ShowFacetEdge
         Returns the flag indicating if facet edges should be shown.  
             
         
        """
        pass
    
    ## Getter for property: (@link ReflectionAnalysisBuilder.Types NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.Types@endlink) Type
    ##  Returns the reflection analysis type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1 NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1@endlink  instead.  <br> 

    ## @return ReflectionAnalysisBuilder.Types
    @property
    def Type(self) -> ReflectionAnalysisBuilder.Types:
        """
        Getter for property: (@link ReflectionAnalysisBuilder.Types NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.Types@endlink) Type
         Returns the reflection analysis type.  
             
         
        """
        pass
    
    ## Setter for property: (@link ReflectionAnalysisBuilder.Types NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.Types@endlink) Type

    ##  Returns the reflection analysis type.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1 NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1@endlink  instead.  <br> 

    @Type.setter
    def Type(self, type: ReflectionAnalysisBuilder.Types):
        """
        Setter for property: (@link ReflectionAnalysisBuilder.Types NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.Types@endlink) Type
         Returns the reflection analysis type.  
             
         
        """
        pass
    
    ##  Start reflection analysis. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1 NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1@endlink  instead.  <br> 

    ## License requirements: None.
    def StartReflectionAnalysis(self) -> None:
        """
         Start reflection analysis. 
        """
        pass
    
##  Represents a Reflection analysis   <br> To create or edit an instance of this class, use @link NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1  NXOpen::GeometricAnalysis::ReflectionAnalysisBuilder1 @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class ReflectionAnalysis(AnalysisObject): 
    """ Represents a Reflection analysis  """
    pass


##  Represents a Section Analysis object. Section Analysis
##     generates planar, circular, or isoparametric sections across faces and faceted bodies 
##     to help evaluating sectional curvature flow of faces and surface quality and 
##     characteristics in general. Section Analysis object update dynamically on geometry 
##     changes of the sectioned faces and faceted bodies.  <br> To create or edit an instance of this class, use @link NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder  NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class SectionAnalysisObject(AnalysisObject): 
    """ Represents a Section Analysis object. Section Analysis
    generates planar, circular, or isoparametric sections across faces and faceted bodies 
    to help evaluating sectional curvature flow of faces and surface quality and 
    characteristics in general. Section Analysis object update dynamically on geometry 
    changes of the sectioned faces and faceted bodies. """
    pass


import NXOpen
##  Represents a @link GeometricAnalysis::SheetBoundaryAnalysis GeometricAnalysis::SheetBoundaryAnalysis@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisObjectCollectionEx::CreateSheetBoundaryAnalysisBuilder  NXOpen::GeometricAnalysis::AnalysisObjectCollectionEx::CreateSheetBoundaryAnalysisBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## EmphasisColor </term> <description> 
##  
## 146 </description> </item> 
## 
## <item><term> 
##  
## LineWidth </term> <description> 
##  
## Seven </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1953.0.0  <br> 

class SheetBoundaryAnalysisBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>GeometricAnalysis.SheetBoundaryAnalysis</ja_class> builder """


    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) Bodies
    ##  Returns the input bodies   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def Bodies(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) Bodies
         Returns the input bodies   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) EmphasisColor
    ##  Returns the emphasis color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def EmphasisColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) EmphasisColor
         Returns the emphasis color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) EmphasisColor

    ##  Returns the emphasis color   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @EmphasisColor.setter
    def EmphasisColor(self, emphasisColor: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) EmphasisColor
         Returns the emphasis color   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) LineWidth
    ##  Returns the line width   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.DisplayableObject.ObjectWidth
    @property
    def LineWidth(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) LineWidth
         Returns the line width   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) LineWidth

    ##  Returns the line width   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @LineWidth.setter
    def LineWidth(self, lineWidth: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) LineWidth
         Returns the line width   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowBoundaryVertices
    ##  Returns the option to display boundary vertices   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def ShowBoundaryVertices(self) -> bool:
        """
        Getter for property: (bool) ShowBoundaryVertices
         Returns the option to display boundary vertices   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowBoundaryVertices

    ##  Returns the option to display boundary vertices   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @ShowBoundaryVertices.setter
    def ShowBoundaryVertices(self, showBoundaryVertices: bool):
        """
        Setter for property: (bool) ShowBoundaryVertices
         Returns the option to display boundary vertices   
            
         
        """
        pass
    
## Represents a sheet boundary analysis builder  <br> To create or edit an instance of this class, use @link NXOpen::GeometricAnalysis::SheetBoundaryAnalysisBuilder  NXOpen::GeometricAnalysis::SheetBoundaryAnalysisBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class SheetBoundaryAnalysis(AnalysisObject): 
    """Represents a sheet boundary analysis builder """
    pass


import NXOpen
##  Represents the Simple Interference object. A
##       @link NXOpen::GeometricAnalysis::SimpleInterference NXOpen::GeometricAnalysis::SimpleInterference@endlink  object
##       takes two solid bodies as inputs and the type of interference results to
##       be produced. It can report the first pair of interfering faces between
##       two solids or all pairs of interfering faces. It can also
##       create the interference solid(s) between two bodies.
##       <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisManager::CreateSimpleInterferenceObject  NXOpen::GeometricAnalysis::AnalysisManager::CreateSimpleInterferenceObject @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class SimpleInterference(NXOpen.Builder): 
    """ Represents the Simple Interference object. A
      <ja_class>NXOpen.GeometricAnalysis.SimpleInterference</ja_class> object
      takes two solid bodies as inputs and the type of interference results to
      be produced. It can report the first pair of interfering faces between
      two solids or all pairs of interfering faces. It can also
      create the interference solid(s) between two bodies.
     """


    ##  Specifies to "find only first pair of interfering faces" or "all
    ##              pairs of interfering faces" between the input boides. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## FirstPairOnly</term><description> 
    ##  Find first pair of interfering faces </description> </item><item><term> 
    ## AllPairs</term><description> 
    ##  Find
    ##                                      all pairs of interfering faces. </description> </item></list>
    class FaceInterferenceMethod(Enum):
        """
        Members Include: <FirstPairOnly> <AllPairs>
        """
        FirstPairOnly: int
        AllPairs: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SimpleInterference.FaceInterferenceMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Specifies interference method, i.e., to highlight interfering
    ##              faces or create interference solid 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## InterferingFaces</term><description> 
    ##  Find
    ##                                                          interfering faces. </description> </item><item><term> 
    ## InterferenceSolid</term><description> 
    ##  Create
    ##                                                            interference solid. </description> </item></list>
    class InterferenceMethod(Enum):
        """
        Members Include: <InterferingFaces> <InterferenceSolid>
        """
        InterferingFaces: int
        InterferenceSolid: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SimpleInterference.InterferenceMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Specifies the result of a simple interference check 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NoInterference</term><description> 
    ##  No interference
    ##                                            exists between the input bodies. </description> </item><item><term> 
    ## OnlyEdgesOrFacesInterfere</term><description> 
    ## 
    ##                                            Only faces or edges interfere and no
    ##                                            solid interference exists between
    ##                                            the input bodies. </description> </item><item><term> 
    ## InterferenceExists</term><description> 
    ##  Interference
    ##                                            exists between the input bodies. Use
    ##                                            @link NXOpen::GeometricAnalysis::SimpleInterference::GetInterferenceResults NXOpen::GeometricAnalysis::SimpleInterference::GetInterferenceResults@endlink  to
    ##                                            obtain the pairs of faces interfering
    ##                                            or interference solid(s) created
    ##                                            between the input bodies. </description> </item><item><term> 
    ## CanNotPerformCheck</term><description> 
    ##  An unknown
    ##                                            error has occured while performing
    ##                                            the interference check. Check could 
    ##                                            not be performed between
    ##                                            the input bodies.</description> </item></list>
    class Result(Enum):
        """
        Members Include: <NoInterference> <OnlyEdgesOrFacesInterfere> <InterferenceExists> <CanNotPerformCheck>
        """
        NoInterference: int
        OnlyEdgesOrFacesInterfere: int
        InterferenceExists: int
        CanNotPerformCheck: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SimpleInterference.Result:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link SimpleInterference.FaceInterferenceMethod NXOpen.GeometricAnalysis.SimpleInterference.FaceInterferenceMethod@endlink) FaceInterferenceType
    ##  Returns the FaceInterferenceType.  
    ##   
    ##               <ja_property_both>NXOpen.GeometricAnalysis.SimpleInterference.FaceInterferenceType</ja_property_both> is used when 
    ##               @link NXOpen::GeometricAnalysis::SimpleInterference::SetInterferenceType NXOpen::GeometricAnalysis::SimpleInterference::SetInterferenceType@endlink  is set to
    ##               @link NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferingFaces NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferingFaces@endlink , 
    ##               i.e., create pair(s) of interfering faces between two solids. A
    ##               value of @link NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceMethodFirstPairOnly NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceMethodFirstPairOnly@endlink  
    ##               for <ja_property_both>NXOpen.GeometricAnalysis.SimpleInterference.FaceInterferenceType</ja_property_both> reports only the first
    ##               pair of interfering faces and value of
    ##               @link NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceMethodAllPairs NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceMethodAllPairs@endlink  
    ##               reports all pairs of interfering faces between two bodies.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return SimpleInterference.FaceInterferenceMethod
    @property
    def FaceInterferenceType(self) -> SimpleInterference.FaceInterferenceMethod:
        """
        Getter for property: (@link SimpleInterference.FaceInterferenceMethod NXOpen.GeometricAnalysis.SimpleInterference.FaceInterferenceMethod@endlink) FaceInterferenceType
         Returns the FaceInterferenceType.  
          
                      <ja_property_both>NXOpen.GeometricAnalysis.SimpleInterference.FaceInterferenceType</ja_property_both> is used when 
                      @link NXOpen::GeometricAnalysis::SimpleInterference::SetInterferenceType NXOpen::GeometricAnalysis::SimpleInterference::SetInterferenceType@endlink  is set to
                      @link NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferingFaces NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferingFaces@endlink , 
                      i.e., create pair(s) of interfering faces between two solids. A
                      value of @link NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceMethodFirstPairOnly NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceMethodFirstPairOnly@endlink  
                      for <ja_property_both>NXOpen.GeometricAnalysis.SimpleInterference.FaceInterferenceType</ja_property_both> reports only the first
                      pair of interfering faces and value of
                      @link NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceMethodAllPairs NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceMethodAllPairs@endlink  
                      reports all pairs of interfering faces between two bodies.   
         
        """
        pass
    
    ## Setter for property: (@link SimpleInterference.FaceInterferenceMethod NXOpen.GeometricAnalysis.SimpleInterference.FaceInterferenceMethod@endlink) FaceInterferenceType

    ##  Returns the FaceInterferenceType.  
    ##   
    ##               <ja_property_both>NXOpen.GeometricAnalysis.SimpleInterference.FaceInterferenceType</ja_property_both> is used when 
    ##               @link NXOpen::GeometricAnalysis::SimpleInterference::SetInterferenceType NXOpen::GeometricAnalysis::SimpleInterference::SetInterferenceType@endlink  is set to
    ##               @link NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferingFaces NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferingFaces@endlink , 
    ##               i.e., create pair(s) of interfering faces between two solids. A
    ##               value of @link NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceMethodFirstPairOnly NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceMethodFirstPairOnly@endlink  
    ##               for <ja_property_both>NXOpen.GeometricAnalysis.SimpleInterference.FaceInterferenceType</ja_property_both> reports only the first
    ##               pair of interfering faces and value of
    ##               @link NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceMethodAllPairs NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceMethodAllPairs@endlink  
    ##               reports all pairs of interfering faces between two bodies.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @FaceInterferenceType.setter
    def FaceInterferenceType(self, faceInterferenceType: SimpleInterference.FaceInterferenceMethod):
        """
        Setter for property: (@link SimpleInterference.FaceInterferenceMethod NXOpen.GeometricAnalysis.SimpleInterference.FaceInterferenceMethod@endlink) FaceInterferenceType
         Returns the FaceInterferenceType.  
          
                      <ja_property_both>NXOpen.GeometricAnalysis.SimpleInterference.FaceInterferenceType</ja_property_both> is used when 
                      @link NXOpen::GeometricAnalysis::SimpleInterference::SetInterferenceType NXOpen::GeometricAnalysis::SimpleInterference::SetInterferenceType@endlink  is set to
                      @link NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferingFaces NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferingFaces@endlink , 
                      i.e., create pair(s) of interfering faces between two solids. A
                      value of @link NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceMethodFirstPairOnly NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceMethodFirstPairOnly@endlink  
                      for <ja_property_both>NXOpen.GeometricAnalysis.SimpleInterference.FaceInterferenceType</ja_property_both> reports only the first
                      pair of interfering faces and value of
                      @link NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceMethodAllPairs NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceMethodAllPairs@endlink  
                      reports all pairs of interfering faces between two bodies.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectObject NXOpen.SelectObject@endlink) FirstBody
    ##  Returns the First Body   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.SelectObject
    @property
    def FirstBody(self) -> NXOpen.SelectObject:
        """
        Getter for property: (@link NXOpen.SelectObject NXOpen.SelectObject@endlink) FirstBody
         Returns the First Body   
            
         
        """
        pass
    
    ## Getter for property: (@link SimpleInterference.InterferenceMethod NXOpen.GeometricAnalysis.SimpleInterference.InterferenceMethod@endlink) InterferenceType
    ##  Returns the InterferenceType.  
    ##    A value of
    ##              @link NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferingFaces NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferingFaces@endlink   for
    ##               <ja_property_both>NXOpen.GeometricAnalysis.SimpleInterference.InterferenceType</ja_property_both> reports 
    ##               the pairs of interfering faces between two solids.  You can also
    ##               further specify to report only the first pair of interfering faces or 
    ##               all pairs of interfering faces by 
    ##               @link NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceType NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceType@endlink . A value of
    ##               @link NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferenceSolid NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferenceSolid@endlink  for
    ##               @link NXOpen::GeometricAnalysis::SimpleInterference::SetInterferenceType NXOpen::GeometricAnalysis::SimpleInterference::SetInterferenceType@endlink  creates the 
    ##               interference solid(s) between the two input bodies.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return SimpleInterference.InterferenceMethod
    @property
    def InterferenceType(self) -> SimpleInterference.InterferenceMethod:
        """
        Getter for property: (@link SimpleInterference.InterferenceMethod NXOpen.GeometricAnalysis.SimpleInterference.InterferenceMethod@endlink) InterferenceType
         Returns the InterferenceType.  
           A value of
                     @link NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferingFaces NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferingFaces@endlink   for
                      <ja_property_both>NXOpen.GeometricAnalysis.SimpleInterference.InterferenceType</ja_property_both> reports 
                      the pairs of interfering faces between two solids.  You can also
                      further specify to report only the first pair of interfering faces or 
                      all pairs of interfering faces by 
                      @link NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceType NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceType@endlink . A value of
                      @link NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferenceSolid NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferenceSolid@endlink  for
                      @link NXOpen::GeometricAnalysis::SimpleInterference::SetInterferenceType NXOpen::GeometricAnalysis::SimpleInterference::SetInterferenceType@endlink  creates the 
                      interference solid(s) between the two input bodies.   
         
        """
        pass
    
    ## Setter for property: (@link SimpleInterference.InterferenceMethod NXOpen.GeometricAnalysis.SimpleInterference.InterferenceMethod@endlink) InterferenceType

    ##  Returns the InterferenceType.  
    ##    A value of
    ##              @link NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferingFaces NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferingFaces@endlink   for
    ##               <ja_property_both>NXOpen.GeometricAnalysis.SimpleInterference.InterferenceType</ja_property_both> reports 
    ##               the pairs of interfering faces between two solids.  You can also
    ##               further specify to report only the first pair of interfering faces or 
    ##               all pairs of interfering faces by 
    ##               @link NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceType NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceType@endlink . A value of
    ##               @link NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferenceSolid NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferenceSolid@endlink  for
    ##               @link NXOpen::GeometricAnalysis::SimpleInterference::SetInterferenceType NXOpen::GeometricAnalysis::SimpleInterference::SetInterferenceType@endlink  creates the 
    ##               interference solid(s) between the two input bodies.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @InterferenceType.setter
    def InterferenceType(self, interferenceType: SimpleInterference.InterferenceMethod):
        """
        Setter for property: (@link SimpleInterference.InterferenceMethod NXOpen.GeometricAnalysis.SimpleInterference.InterferenceMethod@endlink) InterferenceType
         Returns the InterferenceType.  
           A value of
                     @link NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferingFaces NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferingFaces@endlink   for
                      <ja_property_both>NXOpen.GeometricAnalysis.SimpleInterference.InterferenceType</ja_property_both> reports 
                      the pairs of interfering faces between two solids.  You can also
                      further specify to report only the first pair of interfering faces or 
                      all pairs of interfering faces by 
                      @link NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceType NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceType@endlink . A value of
                      @link NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferenceSolid NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferenceSolid@endlink  for
                      @link NXOpen::GeometricAnalysis::SimpleInterference::SetInterferenceType NXOpen::GeometricAnalysis::SimpleInterference::SetInterferenceType@endlink  creates the 
                      interference solid(s) between the two input bodies.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectObject NXOpen.SelectObject@endlink) SecondBody
    ##  Returns the Second Body   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.SelectObject
    @property
    def SecondBody(self) -> NXOpen.SelectObject:
        """
        Getter for property: (@link NXOpen.SelectObject NXOpen.SelectObject@endlink) SecondBody
         Returns the Second Body   
            
         
        """
        pass
    
    ##  Returns the pair(s) of interfering faces or solid(s) of interference
    ##               between the input bodies. nObjects will be 0 if there is no face or
    ##               solid interference between the input bodies. If the
    ##               @link NXOpen::GeometricAnalysis::SimpleInterference::InterferenceType NXOpen::GeometricAnalysis::SimpleInterference::InterferenceType@endlink  is
    ##               @link NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferingFaces NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferingFaces@endlink , pair(s) of
    ##               interfering faces are returned. The first two objects represent the first pair of
    ##               interfering faces, and next two objects represent the second pair
    ##               of interering faces and so on. If the
    ##               @link NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceType NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceType@endlink  is
    ##               @link NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceMethodFirstPairOnly NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceMethodFirstPairOnly@endlink ,
    ##               only the first pair of interfering faces are returned.
    ##              
    ##  @return results (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  Results of Simple Interference .
    ## 
    ##   <br>  Created in NX6.0.2  <br> 

    ## License requirements: None.
    def GetInterferenceResults(self) -> List[NXOpen.NXObject]:
        """
         Returns the pair(s) of interfering faces or solid(s) of interference
                      between the input bodies. nObjects will be 0 if there is no face or
                      solid interference between the input bodies. If the
                      @link NXOpen::GeometricAnalysis::SimpleInterference::InterferenceType NXOpen::GeometricAnalysis::SimpleInterference::InterferenceType@endlink  is
                      @link NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferingFaces NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferingFaces@endlink , pair(s) of
                      interfering faces are returned. The first two objects represent the first pair of
                      interfering faces, and next two objects represent the second pair
                      of interering faces and so on. If the
                      @link NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceType NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceType@endlink  is
                      @link NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceMethodFirstPairOnly NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceMethodFirstPairOnly@endlink ,
                      only the first pair of interfering faces are returned.
                     
         @return results (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  Results of Simple Interference .
        """
        pass
    
    ##  Highlights the pairs of interfering faces after a
    ##               @link NXOpen::GeometricAnalysis::SimpleInterference::PerformCheck NXOpen::GeometricAnalysis::SimpleInterference::PerformCheck@endlink . This method is applicable only
    ##               when @link NXOpen::GeometricAnalysis::SimpleInterference::SetInterferenceType NXOpen::GeometricAnalysis::SimpleInterference::SetInterferenceType@endlink  is set to
    ##               @link NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferingFaces NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferingFaces@endlink  and
    ##               @link NXOpen::GeometricAnalysis::SimpleInterference::SetFaceInterferenceType NXOpen::GeometricAnalysis::SimpleInterference::SetFaceInterferenceType@endlink  is set to
    ##               @link NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceMethodAllPairs NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceMethodAllPairs@endlink . When
    ##               highlighting the next pair, current pair of faces is
    ##               unhighlighted. Return value is set to true if there are more
    ##               pairs of faces to be highlighted. If the last pair is reached 
    ##               (i.e., the pair being highlighted in this call is the last pair 
    ##               of faces), return value is set to false.
    ##  @return morePairs (bool):  Indicates if there are
    ##                                                         any more pairs left . .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def HighlightNextPair(self) -> bool:
        """
         Highlights the pairs of interfering faces after a
                      @link NXOpen::GeometricAnalysis::SimpleInterference::PerformCheck NXOpen::GeometricAnalysis::SimpleInterference::PerformCheck@endlink . This method is applicable only
                      when @link NXOpen::GeometricAnalysis::SimpleInterference::SetInterferenceType NXOpen::GeometricAnalysis::SimpleInterference::SetInterferenceType@endlink  is set to
                      @link NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferingFaces NXOpen::GeometricAnalysis::SimpleInterference::InterferenceMethodInterferingFaces@endlink  and
                      @link NXOpen::GeometricAnalysis::SimpleInterference::SetFaceInterferenceType NXOpen::GeometricAnalysis::SimpleInterference::SetFaceInterferenceType@endlink  is set to
                      @link NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceMethodAllPairs NXOpen::GeometricAnalysis::SimpleInterference::FaceInterferenceMethodAllPairs@endlink . When
                      highlighting the next pair, current pair of faces is
                      unhighlighted. Return value is set to true if there are more
                      pairs of faces to be highlighted. If the last pair is reached 
                      (i.e., the pair being highlighted in this call is the last pair 
                      of faces), return value is set to false.
         @return morePairs (bool):  Indicates if there are
                                                                any more pairs left . .
        """
        pass
    
    ##  Perform Interference Check. @link NXOpen::GeometricAnalysis::SimpleInterference::PerformCheck NXOpen::GeometricAnalysis::SimpleInterference::PerformCheck@endlink 
    ##               should be called after specifiying input bodies to be checked, i.e.,
    ##               @link NXOpen::GeometricAnalysis::SimpleInterference::FirstBody NXOpen::GeometricAnalysis::SimpleInterference::FirstBody@endlink 
    ##               and @link NXOpen::GeometricAnalysis::SimpleInterference::SecondBody NXOpen::GeometricAnalysis::SimpleInterference::SecondBody@endlink . 
    ##               The return value @link NXOpen::GeometricAnalysis::SimpleInterference::Result NXOpen::GeometricAnalysis::SimpleInterference::Result@endlink  specifies the type of
    ##               interference existing between the input bodies. Use
    ##               @link NXOpen::GeometricAnalysis::SimpleInterference::GetInterferenceResults NXOpen::GeometricAnalysis::SimpleInterference::GetInterferenceResults@endlink  to obtain the interfering faces
    ##               or solid(s) of interference between the input bodis.
    ##              
    ##  @return result (@link SimpleInterference.Result NXOpen.GeometricAnalysis.SimpleInterference.Result@endlink):  Indicates
    ##                  the type of interference existing between the input bodies. .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def PerformCheck(self) -> SimpleInterference.Result:
        """
         Perform Interference Check. @link NXOpen::GeometricAnalysis::SimpleInterference::PerformCheck NXOpen::GeometricAnalysis::SimpleInterference::PerformCheck@endlink 
                      should be called after specifiying input bodies to be checked, i.e.,
                      @link NXOpen::GeometricAnalysis::SimpleInterference::FirstBody NXOpen::GeometricAnalysis::SimpleInterference::FirstBody@endlink 
                      and @link NXOpen::GeometricAnalysis::SimpleInterference::SecondBody NXOpen::GeometricAnalysis::SimpleInterference::SecondBody@endlink . 
                      The return value @link NXOpen::GeometricAnalysis::SimpleInterference::Result NXOpen::GeometricAnalysis::SimpleInterference::Result@endlink  specifies the type of
                      interference existing between the input bodies. Use
                      @link NXOpen::GeometricAnalysis::SimpleInterference::GetInterferenceResults NXOpen::GeometricAnalysis::SimpleInterference::GetInterferenceResults@endlink  to obtain the interfering faces
                      or solid(s) of interference between the input bodis.
                     
         @return result (@link SimpleInterference.Result NXOpen.GeometricAnalysis.SimpleInterference.Result@endlink):  Indicates
                         the type of interference existing between the input bodies. .
        """
        pass
    
    ##  Frees up resources/results associated with
    ##              @link NXOpen::GeometricAnalysis::SimpleInterference NXOpen::GeometricAnalysis::SimpleInterference@endlink  object after a
    ##              call to @link NXOpen::GeometricAnalysis::SimpleInterference::PerformCheck NXOpen::GeometricAnalysis::SimpleInterference::PerformCheck@endlink .
    ##              @link NXOpen::GeometricAnalysis::SimpleInterference::PerformCheck NXOpen::GeometricAnalysis::SimpleInterference::PerformCheck@endlink  is followed by
    ##              @link NXOpen::GeometricAnalysis::SimpleInterference::GetInterferenceResults NXOpen::GeometricAnalysis::SimpleInterference::GetInterferenceResults@endlink  and the
    ##              @link NXOpen::GeometricAnalysis::SimpleInterference::Reset NXOpen::GeometricAnalysis::SimpleInterference::Reset@endlink . 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def Reset(self) -> None:
        """
         Frees up resources/results associated with
                     @link NXOpen::GeometricAnalysis::SimpleInterference NXOpen::GeometricAnalysis::SimpleInterference@endlink  object after a
                     call to @link NXOpen::GeometricAnalysis::SimpleInterference::PerformCheck NXOpen::GeometricAnalysis::SimpleInterference::PerformCheck@endlink .
                     @link NXOpen::GeometricAnalysis::SimpleInterference::PerformCheck NXOpen::GeometricAnalysis::SimpleInterference::PerformCheck@endlink  is followed by
                     @link NXOpen::GeometricAnalysis::SimpleInterference::GetInterferenceResults NXOpen::GeometricAnalysis::SimpleInterference::GetInterferenceResults@endlink  and the
                     @link NXOpen::GeometricAnalysis::SimpleInterference::Reset NXOpen::GeometricAnalysis::SimpleInterference::Reset@endlink . 
        """
        pass
    
import NXOpen
import NXOpen.Features
##  Represents a Slope Analysis builder.  <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisObjectCollectionEx::CreateSlopeAnalysisBuilder1  NXOpen::GeometricAnalysis::AnalysisObjectCollectionEx::CreateSlopeAnalysisBuilder1 @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DataRange.IsFixed </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## DataRange.Max </term> <description> 
##  
## 0.010000 </description> </item> 
## 
## <item><term> 
##  
## DataRange.Middle </term> <description> 
##  
## 0.000000 </description> </item> 
## 
## <item><term> 
##  
## DataRange.MiddleScale </term> <description> 
##  
## 0.000000 </description> </item> 
## 
## <item><term> 
##  
## DataRange.Min </term> <description> 
##  
## -0.010000 </description> </item> 
## 
## <item><term> 
##  
## DataRange.NumberOfColors </term> <description> 
##  
## Seven </description> </item> 
## 
## <item><term> 
##  
## DataRange.UserDefinedColorScale.NumberOfColors </term> <description> 
##  
## Seven </description> </item> 
## 
## <item><term> 
##  
## DataRange.ZoomScale </term> <description> 
##  
## 8 </description> </item> 
## 
## <item><term> 
##  
## DisplayMode </term> <description> 
##  
## Fringe </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.CanShowFacet </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.ColorLegendOption </term> <description> 
##  
## Blend </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.DisplayResolution.AngleTolerance </term> <description> 
##  
## 15.0 </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.DisplayResolution.EdgeTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.DisplayResolution.FaceTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.DisplayResolution.Resolution </term> <description> 
##  
## Standard </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.DisplayResolution.WidthTolerance </term> <description> 
##  
## 0.3 </description> </item> 
## 
## <item><term> 
##  
## NumberOfContourLines </term> <description> 
##  
## 8 </description> </item> 
## 
## <item><term> 
##  
## SpikeLength </term> <description> 
##  
## 25.4 (millimeters part), 1.0 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2312.0.0  <br> 

class SlopeAnalysisBuilder1(NXOpen.Builder): 
    """ Represents a Slope Analysis builder. """


    ##  The display type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Fringe</term><description> 
    ##  Display in fringe. </description> </item><item><term> 
    ## Hedgehog</term><description> 
    ##  Display in hedgehog. </description> </item><item><term> 
    ## ContourLines</term><description> 
    ##  Display in contour lines. </description> </item></list>
    class DisplayModes(Enum):
        """
        Members Include: <Fringe> <Hedgehog> <ContourLines>
        """
        Fringe: int
        Hedgehog: int
        ContourLines: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SlopeAnalysisBuilder1.DisplayModes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link FaceAnalysisDataRangeBuilder NXOpen.GeometricAnalysis.FaceAnalysisDataRangeBuilder@endlink) DataRange
    ##  Returns the slope analysis data range.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return FaceAnalysisDataRangeBuilder
    @property
    def DataRange(self) -> FaceAnalysisDataRangeBuilder:
        """
        Getter for property: (@link FaceAnalysisDataRangeBuilder NXOpen.GeometricAnalysis.FaceAnalysisDataRangeBuilder@endlink) DataRange
         Returns the slope analysis data range.  
             
         
        """
        pass
    
    ## Getter for property: (@link SlopeAnalysisBuilder1.DisplayModes NXOpen.GeometricAnalysis.SlopeAnalysisBuilder1.DisplayModes@endlink) DisplayMode
    ##  Returns the display mode.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return SlopeAnalysisBuilder1.DisplayModes
    @property
    def DisplayMode(self) -> SlopeAnalysisBuilder1.DisplayModes:
        """
        Getter for property: (@link SlopeAnalysisBuilder1.DisplayModes NXOpen.GeometricAnalysis.SlopeAnalysisBuilder1.DisplayModes@endlink) DisplayMode
         Returns the display mode.  
             
         
        """
        pass
    
    ## Setter for property: (@link SlopeAnalysisBuilder1.DisplayModes NXOpen.GeometricAnalysis.SlopeAnalysisBuilder1.DisplayModes@endlink) DisplayMode

    ##  Returns the display mode.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @DisplayMode.setter
    def DisplayMode(self, displayMode: SlopeAnalysisBuilder1.DisplayModes):
        """
        Setter for property: (@link SlopeAnalysisBuilder1.DisplayModes NXOpen.GeometricAnalysis.SlopeAnalysisBuilder1.DisplayModes@endlink) DisplayMode
         Returns the display mode.  
             
         
        """
        pass
    
    ## Getter for property: (@link FaceAnalysisDisplayBuilder NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilder@endlink) DisplaySettings
    ##  Returns the slope analysis display settings.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return FaceAnalysisDisplayBuilder
    @property
    def DisplaySettings(self) -> FaceAnalysisDisplayBuilder:
        """
        Getter for property: (@link FaceAnalysisDisplayBuilder NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilder@endlink) DisplaySettings
         Returns the slope analysis display settings.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Features.GeometricConstraintDataManager NXOpen.Features.GeometricConstraintDataManager@endlink) DynamicLabel
    ##  Returns the dynamic label   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Features.GeometricConstraintDataManager
    @property
    def DynamicLabel(self) -> NXOpen.Features.GeometricConstraintDataManager:
        """
        Getter for property: (@link NXOpen.Features.GeometricConstraintDataManager NXOpen.Features.GeometricConstraintDataManager@endlink) DynamicLabel
         Returns the dynamic label   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Faces
    ##  Returns the face to apply slope analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def Faces(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Faces
         Returns the face to apply slope analysis.  
             
         
        """
        pass
    
    ## Getter for property: (@link FaceAnalysisNormalsBuilder NXOpen.GeometricAnalysis.FaceAnalysisNormalsBuilder@endlink) Normals
    ##  Returns the slope analysis normals.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return FaceAnalysisNormalsBuilder
    @property
    def Normals(self) -> FaceAnalysisNormalsBuilder:
        """
        Getter for property: (@link FaceAnalysisNormalsBuilder NXOpen.GeometricAnalysis.FaceAnalysisNormalsBuilder@endlink) Normals
         Returns the slope analysis normals.  
             
         
        """
        pass
    
    ## Getter for property: (int) NumberOfContourLines
    ##  Returns the number of contour lines.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return int
    @property
    def NumberOfContourLines(self) -> int:
        """
        Getter for property: (int) NumberOfContourLines
         Returns the number of contour lines.  
             
         
        """
        pass
    
    ## Setter for property: (int) NumberOfContourLines

    ##  Returns the number of contour lines.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @NumberOfContourLines.setter
    def NumberOfContourLines(self, numberOfContourLines: int):
        """
        Setter for property: (int) NumberOfContourLines
         Returns the number of contour lines.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) PmiPoint
    ##  Returns the point to draw labels.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def PmiPoint(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) PmiPoint
         Returns the point to draw labels.  
             
         
        """
        pass
    
    ## Getter for property: (float) SpikeLength
    ##  Returns the spike length.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def SpikeLength(self) -> float:
        """
        Getter for property: (float) SpikeLength
         Returns the spike length.  
             
         
        """
        pass
    
    ## Setter for property: (float) SpikeLength

    ##  Returns the spike length.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @SpikeLength.setter
    def SpikeLength(self, spikeLength: float):
        """
        Setter for property: (float) SpikeLength
         Returns the spike length.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector
    ##  Returns the reference vector used for slope analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def Vector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector
         Returns the reference vector used for slope analysis.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector

    ##  Returns the reference vector used for slope analysis.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @Vector.setter
    def Vector(self, vector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector
         Returns the reference vector used for slope analysis.  
             
         
        """
        pass
    
    ##  Create a PMI label. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="location"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  the loction on the face to create a PMI label. </param>
    ## <param name="face"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink)  the selected face to create a PMI label. </param>
    def CreatePMILabel(self, location: NXOpen.Point3d, face: NXOpen.DisplayableObject) -> None:
        """
         Create a PMI label. 
        """
        pass
    
    ##  Start slope analysis. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def StartSlopeAnalysis(self) -> None:
        """
         Start slope analysis. 
        """
        pass
    
    ##  Update display after vector changes. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def UpdateDisplayOnVectorChange(self) -> None:
        """
         Update display after vector changes. 
        """
        pass
    
import NXOpen
import NXOpen.Features
##  Represents a Slope Analysis builder.  <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisObjectCollectionEx::CreateSlopeAnalysisBuilder  NXOpen::GeometricAnalysis::AnalysisObjectCollectionEx::CreateSlopeAnalysisBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DataRange.IsFixed (deprecated) </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## DataRange.Max (deprecated) </term> <description> 
##  
## 0.010000 </description> </item> 
## 
## <item><term> 
##  
## DataRange.Middle (deprecated) </term> <description> 
##  
## 0.000000 </description> </item> 
## 
## <item><term> 
##  
## DataRange.MiddleScale (deprecated) </term> <description> 
##  
## 0.000000 </description> </item> 
## 
## <item><term> 
##  
## DataRange.Min (deprecated) </term> <description> 
##  
## -0.010000 </description> </item> 
## 
## <item><term> 
##  
## DataRange.ZoomScale (deprecated) </term> <description> 
##  
## 8 </description> </item> 
## 
## <item><term> 
##  
## DisplayMode (deprecated) </term> <description> 
##  
## Fringe </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.CanShowFacet (deprecated) </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.ColorLegendOption (deprecated) </term> <description> 
##  
## Blend </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.DisplayResolution.AngleTolerance (deprecated) </term> <description> 
##  
## 15.0 </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.DisplayResolution.EdgeTolerance (deprecated) </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.DisplayResolution.FaceTolerance (deprecated) </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.DisplayResolution.Resolution (deprecated) </term> <description> 
##  
## Standard </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.DisplayResolution.WidthTolerance (deprecated) </term> <description> 
##  
## 0.3 </description> </item> 
## 
## <item><term> 
##  
## DisplaySettings.NumberOfColors (deprecated) </term> <description> 
##  
## Seven </description> </item> 
## 
## <item><term> 
##  
## NumberOfContourLines (deprecated) </term> <description> 
##  
## 8 </description> </item> 
## 
## <item><term> 
##  
## SpikeLength (deprecated) </term> <description> 
##  
## 25.4 (millimeters part), 1.0 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX11.0.0  <br> 
## 
##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1 NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1@endlink  instead.  <br> 

class SlopeAnalysisBuilder(NXOpen.Builder): 
    """ Represents a Slope Analysis builder. """


    ##  The display type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Fringe</term><description> 
    ## </description> </item><item><term> 
    ## Hedgehog</term><description> 
    ## </description> </item><item><term> 
    ## ContourLines</term><description> 
    ## </description> </item></list>
    class DisplayModes(Enum):
        """
        Members Include: <Fringe> <Hedgehog> <ContourLines>
        """
        Fringe: int
        Hedgehog: int
        ContourLines: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SlopeAnalysisBuilder.DisplayModes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link FaceAnalysisDataRangeBuilder NXOpen.GeometricAnalysis.FaceAnalysisDataRangeBuilder@endlink) DataRange
    ##  Returns the slope analysis data range.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1 NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1@endlink  instead.  <br> 

    ## @return FaceAnalysisDataRangeBuilder
    @property
    def DataRange(self) -> FaceAnalysisDataRangeBuilder:
        """
        Getter for property: (@link FaceAnalysisDataRangeBuilder NXOpen.GeometricAnalysis.FaceAnalysisDataRangeBuilder@endlink) DataRange
         Returns the slope analysis data range.  
             
         
        """
        pass
    
    ## Getter for property: (@link SlopeAnalysisBuilder.DisplayModes NXOpen.GeometricAnalysis.SlopeAnalysisBuilder.DisplayModes@endlink) DisplayMode
    ##  Returns the display mode.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1 NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1@endlink  instead.  <br> 

    ## @return SlopeAnalysisBuilder.DisplayModes
    @property
    def DisplayMode(self) -> SlopeAnalysisBuilder.DisplayModes:
        """
        Getter for property: (@link SlopeAnalysisBuilder.DisplayModes NXOpen.GeometricAnalysis.SlopeAnalysisBuilder.DisplayModes@endlink) DisplayMode
         Returns the display mode.  
             
         
        """
        pass
    
    ## Setter for property: (@link SlopeAnalysisBuilder.DisplayModes NXOpen.GeometricAnalysis.SlopeAnalysisBuilder.DisplayModes@endlink) DisplayMode

    ##  Returns the display mode.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1 NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1@endlink  instead.  <br> 

    @DisplayMode.setter
    def DisplayMode(self, displayMode: SlopeAnalysisBuilder.DisplayModes):
        """
        Setter for property: (@link SlopeAnalysisBuilder.DisplayModes NXOpen.GeometricAnalysis.SlopeAnalysisBuilder.DisplayModes@endlink) DisplayMode
         Returns the display mode.  
             
         
        """
        pass
    
    ## Getter for property: (@link FaceAnalysisDisplayBuilder NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilder@endlink) DisplaySettings
    ##  Returns the slope analysis display settings.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1 NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1@endlink  instead.  <br> 

    ## @return FaceAnalysisDisplayBuilder
    @property
    def DisplaySettings(self) -> FaceAnalysisDisplayBuilder:
        """
        Getter for property: (@link FaceAnalysisDisplayBuilder NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilder@endlink) DisplaySettings
         Returns the slope analysis display settings.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Features.GeometricConstraintDataManager NXOpen.Features.GeometricConstraintDataManager@endlink) DynamicLabel
    ##  Returns the dynamic label   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1 NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1@endlink  instead.  <br> 

    ## @return NXOpen.Features.GeometricConstraintDataManager
    @property
    def DynamicLabel(self) -> NXOpen.Features.GeometricConstraintDataManager:
        """
        Getter for property: (@link NXOpen.Features.GeometricConstraintDataManager NXOpen.Features.GeometricConstraintDataManager@endlink) DynamicLabel
         Returns the dynamic label   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Faces
    ##  Returns the face to apply slope analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1 NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1@endlink  instead.  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def Faces(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Faces
         Returns the face to apply slope analysis.  
             
         
        """
        pass
    
    ## Getter for property: (@link FaceAnalysisNormalsBuilder NXOpen.GeometricAnalysis.FaceAnalysisNormalsBuilder@endlink) Normals
    ##  Returns the slope analysis normals.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1 NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1@endlink  instead.  <br> 

    ## @return FaceAnalysisNormalsBuilder
    @property
    def Normals(self) -> FaceAnalysisNormalsBuilder:
        """
        Getter for property: (@link FaceAnalysisNormalsBuilder NXOpen.GeometricAnalysis.FaceAnalysisNormalsBuilder@endlink) Normals
         Returns the slope analysis normals.  
             
         
        """
        pass
    
    ## Getter for property: (int) NumberOfContourLines
    ##  Returns the number of contour lines.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1 NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1@endlink  instead.  <br> 

    ## @return int
    @property
    def NumberOfContourLines(self) -> int:
        """
        Getter for property: (int) NumberOfContourLines
         Returns the number of contour lines.  
             
         
        """
        pass
    
    ## Setter for property: (int) NumberOfContourLines

    ##  Returns the number of contour lines.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1 NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1@endlink  instead.  <br> 

    @NumberOfContourLines.setter
    def NumberOfContourLines(self, numberOfContourLines: int):
        """
        Setter for property: (int) NumberOfContourLines
         Returns the number of contour lines.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) PmiPoint
    ##  Returns the point to draw labels.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1 NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1@endlink  instead.  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def PmiPoint(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) PmiPoint
         Returns the point to draw labels.  
             
         
        """
        pass
    
    ## Getter for property: (float) SpikeLength
    ##  Returns the spike length.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1 NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1@endlink  instead.  <br> 

    ## @return float
    @property
    def SpikeLength(self) -> float:
        """
        Getter for property: (float) SpikeLength
         Returns the spike length.  
             
         
        """
        pass
    
    ## Setter for property: (float) SpikeLength

    ##  Returns the spike length.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1 NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1@endlink  instead.  <br> 

    @SpikeLength.setter
    def SpikeLength(self, spikeLength: float):
        """
        Setter for property: (float) SpikeLength
         Returns the spike length.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector
    ##  Returns the reference vector used for slope analysis.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1 NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1@endlink  instead.  <br> 

    ## @return NXOpen.Direction
    @property
    def Vector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector
         Returns the reference vector used for slope analysis.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector

    ##  Returns the reference vector used for slope analysis.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1 NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1@endlink  instead.  <br> 

    @Vector.setter
    def Vector(self, vector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector
         Returns the reference vector used for slope analysis.  
             
         
        """
        pass
    
    ##  Create a PMI label. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1 NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1@endlink  instead.  <br> 

    ## License requirements: None.
    ## 
    ## <param name="location"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  the loction on the face to create a PMI label. </param>
    ## <param name="face"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink)  the selected face to create a PMI label. </param>
    def CreatePMILabel(self, location: NXOpen.Point3d, face: NXOpen.DisplayableObject) -> None:
        """
         Create a PMI label. 
        """
        pass
    
    ##  Start slope analysis. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1 NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1@endlink  instead.  <br> 

    ## License requirements: None.
    def StartSlopeAnalysis(self) -> None:
        """
         Start slope analysis. 
        """
        pass
    
##  Represents a Slope analysis   <br> To create or edit an instance of this class, use @link NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1  NXOpen::GeometricAnalysis::SlopeAnalysisBuilder1 @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class SlopeAnalysis(AnalysisObject): 
    """ Represents a Slope analysis  """
    pass


import NXOpen
## 
##       Represents a @link NXOpen::GeometricAnalysis::SolidDensity NXOpen::GeometricAnalysis::SolidDensity@endlink 
##       <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisManager::CreateSolidDensityObject  NXOpen::GeometricAnalysis::AnalysisManager::CreateSolidDensityObject @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class SolidDensity(NXOpen.Builder): 
    """
      Represents a <ja_class>NXOpen.GeometricAnalysis.SolidDensity</ja_class>
     """


    ##  Types of units for solid density 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## PoundsPerCubicInches</term><description> 
    ##  lbm/in^3 </description> </item><item><term> 
    ## PoundsPerCubicFeet</term><description> 
    ##  lbm/ft^3 </description> </item><item><term> 
    ## GramsPerCubicCentimeters</term><description> 
    ##  g/cm^3 </description> </item><item><term> 
    ## KilogramsPerCubicMeters</term><description> 
    ##  kg/m^3 </description> </item></list>
    class UnitsType(Enum):
        """
        Members Include: <PoundsPerCubicInches> <PoundsPerCubicFeet> <GramsPerCubicCentimeters> <KilogramsPerCubicMeters>
        """
        PoundsPerCubicInches: int
        PoundsPerCubicFeet: int
        GramsPerCubicCentimeters: int
        KilogramsPerCubicMeters: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SolidDensity.UnitsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) Density
    ##  Returns the Solid Density.  
    ##    @link NXOpen::GeometricAnalysis::SolidDensity::SetUnits NXOpen::GeometricAnalysis::SolidDensity::SetUnits@endlink  must be specified before
    ##           specifying the density. When @link NXOpen::GeometricAnalysis::SolidDensity::SetUnits NXOpen::GeometricAnalysis::SolidDensity::SetUnits@endlink  is changed, 
    ##           @link NXOpen::GeometricAnalysis::SolidDensity::Density NXOpen::GeometricAnalysis::SolidDensity::Density@endlink  value is recomputed to reflect the change
    ##           in units. Set @link NXOpen::GeometricAnalysis::SolidDensity::SetUnits NXOpen::GeometricAnalysis::SolidDensity::SetUnits@endlink  first, then
    ##           @link NXOpen::GeometricAnalysis::SolidDensity::SetDensity NXOpen::GeometricAnalysis::SolidDensity::SetDensity@endlink  to set specify the density along
    ##           with its units.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def Density(self) -> float:
        """
        Getter for property: (float) Density
         Returns the Solid Density.  
           @link NXOpen::GeometricAnalysis::SolidDensity::SetUnits NXOpen::GeometricAnalysis::SolidDensity::SetUnits@endlink  must be specified before
                  specifying the density. When @link NXOpen::GeometricAnalysis::SolidDensity::SetUnits NXOpen::GeometricAnalysis::SolidDensity::SetUnits@endlink  is changed, 
                  @link NXOpen::GeometricAnalysis::SolidDensity::Density NXOpen::GeometricAnalysis::SolidDensity::Density@endlink  value is recomputed to reflect the change
                  in units. Set @link NXOpen::GeometricAnalysis::SolidDensity::SetUnits NXOpen::GeometricAnalysis::SolidDensity::SetUnits@endlink  first, then
                  @link NXOpen::GeometricAnalysis::SolidDensity::SetDensity NXOpen::GeometricAnalysis::SolidDensity::SetDensity@endlink  to set specify the density along
                  with its units.   
         
        """
        pass
    
    ## Setter for property: (float) Density

    ##  Returns the Solid Density.  
    ##    @link NXOpen::GeometricAnalysis::SolidDensity::SetUnits NXOpen::GeometricAnalysis::SolidDensity::SetUnits@endlink  must be specified before
    ##           specifying the density. When @link NXOpen::GeometricAnalysis::SolidDensity::SetUnits NXOpen::GeometricAnalysis::SolidDensity::SetUnits@endlink  is changed, 
    ##           @link NXOpen::GeometricAnalysis::SolidDensity::Density NXOpen::GeometricAnalysis::SolidDensity::Density@endlink  value is recomputed to reflect the change
    ##           in units. Set @link NXOpen::GeometricAnalysis::SolidDensity::SetUnits NXOpen::GeometricAnalysis::SolidDensity::SetUnits@endlink  first, then
    ##           @link NXOpen::GeometricAnalysis::SolidDensity::SetDensity NXOpen::GeometricAnalysis::SolidDensity::SetDensity@endlink  to set specify the density along
    ##           with its units.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Density.setter
    def Density(self, density: float):
        """
        Setter for property: (float) Density
         Returns the Solid Density.  
           @link NXOpen::GeometricAnalysis::SolidDensity::SetUnits NXOpen::GeometricAnalysis::SolidDensity::SetUnits@endlink  must be specified before
                  specifying the density. When @link NXOpen::GeometricAnalysis::SolidDensity::SetUnits NXOpen::GeometricAnalysis::SolidDensity::SetUnits@endlink  is changed, 
                  @link NXOpen::GeometricAnalysis::SolidDensity::Density NXOpen::GeometricAnalysis::SolidDensity::Density@endlink  value is recomputed to reflect the change
                  in units. Set @link NXOpen::GeometricAnalysis::SolidDensity::SetUnits NXOpen::GeometricAnalysis::SolidDensity::SetUnits@endlink  first, then
                  @link NXOpen::GeometricAnalysis::SolidDensity::SetDensity NXOpen::GeometricAnalysis::SolidDensity::SetDensity@endlink  to set specify the density along
                  with its units.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectObjectList NXOpen.SelectObjectList@endlink) Solids
    ##  Returns the solids to set density for   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.SelectObjectList
    @property
    def Solids(self) -> NXOpen.SelectObjectList:
        """
        Getter for property: (@link NXOpen.SelectObjectList NXOpen.SelectObjectList@endlink) Solids
         Returns the solids to set density for   
            
         
        """
        pass
    
    ## Getter for property: (@link SolidDensity.UnitsType NXOpen.GeometricAnalysis.SolidDensity.UnitsType@endlink) Units
    ##  Returns the density units for @link NXOpen::GeometricAnalysis::SolidDensity NXOpen::GeometricAnalysis::SolidDensity@endlink .  
    ##    
    ##           When @link NXOpen::GeometricAnalysis::SolidDensity::SetUnits NXOpen::GeometricAnalysis::SolidDensity::SetUnits@endlink  is changed, @link NXOpen::GeometricAnalysis::SolidDensity::Density NXOpen::GeometricAnalysis::SolidDensity::Density@endlink 
    ##           value is recomputed to reflect the change in units. Set
    ##           @link NXOpen::GeometricAnalysis::SolidDensity::SetUnits NXOpen::GeometricAnalysis::SolidDensity::SetUnits@endlink  first, then
    ##           @link NXOpen::GeometricAnalysis::SolidDensity::SetDensity NXOpen::GeometricAnalysis::SolidDensity::SetDensity@endlink  to set specify the density with
    ##           units.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return SolidDensity.UnitsType
    @property
    def Units(self) -> SolidDensity.UnitsType:
        """
        Getter for property: (@link SolidDensity.UnitsType NXOpen.GeometricAnalysis.SolidDensity.UnitsType@endlink) Units
         Returns the density units for @link NXOpen::GeometricAnalysis::SolidDensity NXOpen::GeometricAnalysis::SolidDensity@endlink .  
           
                  When @link NXOpen::GeometricAnalysis::SolidDensity::SetUnits NXOpen::GeometricAnalysis::SolidDensity::SetUnits@endlink  is changed, @link NXOpen::GeometricAnalysis::SolidDensity::Density NXOpen::GeometricAnalysis::SolidDensity::Density@endlink 
                  value is recomputed to reflect the change in units. Set
                  @link NXOpen::GeometricAnalysis::SolidDensity::SetUnits NXOpen::GeometricAnalysis::SolidDensity::SetUnits@endlink  first, then
                  @link NXOpen::GeometricAnalysis::SolidDensity::SetDensity NXOpen::GeometricAnalysis::SolidDensity::SetDensity@endlink  to set specify the density with
                  units.   
         
        """
        pass
    
    ## Setter for property: (@link SolidDensity.UnitsType NXOpen.GeometricAnalysis.SolidDensity.UnitsType@endlink) Units

    ##  Returns the density units for @link NXOpen::GeometricAnalysis::SolidDensity NXOpen::GeometricAnalysis::SolidDensity@endlink .  
    ##    
    ##           When @link NXOpen::GeometricAnalysis::SolidDensity::SetUnits NXOpen::GeometricAnalysis::SolidDensity::SetUnits@endlink  is changed, @link NXOpen::GeometricAnalysis::SolidDensity::Density NXOpen::GeometricAnalysis::SolidDensity::Density@endlink 
    ##           value is recomputed to reflect the change in units. Set
    ##           @link NXOpen::GeometricAnalysis::SolidDensity::SetUnits NXOpen::GeometricAnalysis::SolidDensity::SetUnits@endlink  first, then
    ##           @link NXOpen::GeometricAnalysis::SolidDensity::SetDensity NXOpen::GeometricAnalysis::SolidDensity::SetDensity@endlink  to set specify the density with
    ##           units.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Units.setter
    def Units(self, units: SolidDensity.UnitsType):
        """
        Setter for property: (@link SolidDensity.UnitsType NXOpen.GeometricAnalysis.SolidDensity.UnitsType@endlink) Units
         Returns the density units for @link NXOpen::GeometricAnalysis::SolidDensity NXOpen::GeometricAnalysis::SolidDensity@endlink .  
           
                  When @link NXOpen::GeometricAnalysis::SolidDensity::SetUnits NXOpen::GeometricAnalysis::SolidDensity::SetUnits@endlink  is changed, @link NXOpen::GeometricAnalysis::SolidDensity::Density NXOpen::GeometricAnalysis::SolidDensity::Density@endlink 
                  value is recomputed to reflect the change in units. Set
                  @link NXOpen::GeometricAnalysis::SolidDensity::SetUnits NXOpen::GeometricAnalysis::SolidDensity::SetUnits@endlink  first, then
                  @link NXOpen::GeometricAnalysis::SolidDensity::SetDensity NXOpen::GeometricAnalysis::SolidDensity::SetDensity@endlink  to set specify the density with
                  units.   
         
        """
        pass
    
import NXOpen
##  Represents a tool control whether to show a surface's poles and knots  <br> To obtain an instance of this class, refer to @link NXOpen::GeometricAnalysis::AnalysisObjectCollection  NXOpen::GeometricAnalysis::AnalysisObjectCollection @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class SurfaceAnalysisDisplay(NXOpen.Object): 
    """ Represents a tool control whether to show a surface's poles and knots """


    ##  Show flag types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Pole</term><description> 
    ##  show pole   </description> </item><item><term> 
    ## Knot</term><description> 
    ##  show knot   </description> </item></list>
    class ShowFlagType(Enum):
        """
        Members Include: <Pole> <Knot>
        """
        Pole: int
        Knot: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SurfaceAnalysisDisplay.ShowFlagType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Sets show flags 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING")
    ## 
    ## <param name="surface"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink)  surface </param>
    ## <param name="choice"> (@link SurfaceAnalysisDisplay.ShowFlagType NXOpen.GeometricAnalysis.SurfaceAnalysisDisplay.ShowFlagType@endlink)  pole/knot </param>
    ## <param name="on"> (bool)  true/false to show flags </param>
    def SetShowFlag(self, surface: NXOpen.DisplayableObject, choice: SurfaceAnalysisDisplay.ShowFlagType, on: bool) -> None:
        """
         Sets show flags 
        """
        pass
    
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
##  Represents a @link NXOpen::GeometricAnalysis::SurfaceContinuityAnalysis NXOpen::GeometricAnalysis::SurfaceContinuityAnalysis@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisObjectCollection::CreateSurfaceContinuityAnalysisBuilder  NXOpen::GeometricAnalysis::AnalysisObjectCollection::CreateSurfaceContinuityAnalysisBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## CurvatureCheck </term> <description> 
##  
## Sectional </description> </item> 
## 
## <item><term> 
##  
## G0 </term> <description> 
##  
## True </description> </item> 
## 
## <item><term> 
##  
## G1 </term> <description> 
##  
## False </description> </item> 
## 
## <item><term> 
##  
## G2 </term> <description> 
##  
## False </description> </item> 
## 
## <item><term> 
##  
## G3 </term> <description> 
##  
## False </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX6.0.0  <br> 

class SurfaceContinuityAnalysisBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.GeometricAnalysis.SurfaceContinuityAnalysis</ja_class> builder """


    ##  Curvature types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Sectional</term><description> 
    ## </description> </item><item><term> 
    ## Gaussian</term><description> 
    ## </description> </item><item><term> 
    ## Mean</term><description> 
    ## </description> </item><item><term> 
    ## Absolute</term><description> 
    ## </description> </item></list>
    class CurvatureType(Enum):
        """
        Members Include: <Sectional> <Gaussian> <Mean> <Absolute>
        """
        Sectional: int
        Gaussian: int
        Mean: int
        Absolute: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SurfaceContinuityAnalysisBuilder.CurvatureType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Reporting types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Analysis</term><description> 
    ## </description> </item><item><term> 
    ## Pair</term><description> 
    ## </description> </item></list>
    class ReportingType(Enum):
        """
        Members Include: <Analysis> <Pair>
        """
        Analysis: int
        Pair: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SurfaceContinuityAnalysisBuilder.ReportingType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Two possible types for the dialog 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## EdgeToEdge</term><description> 
    ## </description> </item><item><term> 
    ## EdgeToFace</term><description> 
    ## </description> </item><item><term> 
    ## MultiFace</term><description> 
    ## </description> </item></list>
    class Types(Enum):
        """
        Members Include: <EdgeToEdge> <EdgeToFace> <MultiFace>
        """
        EdgeToEdge: int
        EdgeToFace: int
        MultiFace: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SurfaceContinuityAnalysisBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) AngularThreshold
    ##  Returns the angular threshold   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def AngularThreshold(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) AngularThreshold
         Returns the angular threshold   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.CombOptionsBuilder NXOpen.GeometricUtilities.CombOptionsBuilder@endlink) CombOptions
    ##  Returns the comb display block options   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.CombOptionsBuilder
    @property
    def CombOptions(self) -> NXOpen.GeometricUtilities.CombOptionsBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.CombOptionsBuilder NXOpen.GeometricUtilities.CombOptionsBuilder@endlink) CombOptions
         Returns the comb display block options   
            
         
        """
        pass
    
    ## Getter for property: (@link SurfaceContinuityAnalysisBuilder.CurvatureType NXOpen.GeometricAnalysis.SurfaceContinuityAnalysisBuilder.CurvatureType@endlink) CurvatureCheck
    ##  Returns the curvature check   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return SurfaceContinuityAnalysisBuilder.CurvatureType
    @property
    def CurvatureCheck(self) -> SurfaceContinuityAnalysisBuilder.CurvatureType:
        """
        Getter for property: (@link SurfaceContinuityAnalysisBuilder.CurvatureType NXOpen.GeometricAnalysis.SurfaceContinuityAnalysisBuilder.CurvatureType@endlink) CurvatureCheck
         Returns the curvature check   
            
         
        """
        pass
    
    ## Setter for property: (@link SurfaceContinuityAnalysisBuilder.CurvatureType NXOpen.GeometricAnalysis.SurfaceContinuityAnalysisBuilder.CurvatureType@endlink) CurvatureCheck

    ##  Returns the curvature check   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @CurvatureCheck.setter
    def CurvatureCheck(self, curvatureCheck: SurfaceContinuityAnalysisBuilder.CurvatureType):
        """
        Setter for property: (@link SurfaceContinuityAnalysisBuilder.CurvatureType NXOpen.GeometricAnalysis.SurfaceContinuityAnalysisBuilder.CurvatureType@endlink) CurvatureCheck
         Returns the curvature check   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceThreshold
    ##  Returns the distance threshold   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DistanceThreshold(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceThreshold
         Returns the distance threshold   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Features.GeometricConstraintDataManager NXOpen.Features.GeometricConstraintDataManager@endlink) DynamicLabel
    ##  Returns the constraint manager   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Features.GeometricConstraintDataManager
    @property
    def DynamicLabel(self) -> NXOpen.Features.GeometricConstraintDataManager:
        """
        Getter for property: (@link NXOpen.Features.GeometricConstraintDataManager NXOpen.Features.GeometricConstraintDataManager@endlink) DynamicLabel
         Returns the constraint manager   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) Face
    ##  Returns the (second) faces.  
    ##    Used only if the type is EdgeFace   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def Face(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) Face
         Returns the (second) faces.  
           Used only if the type is EdgeFace   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) FirstEdge
    ##  Returns the first edges or faces   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def FirstEdge(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) FirstEdge
         Returns the first edges or faces   
            
         
        """
        pass
    
    ## Getter for property: (bool) G0
    ##  Returns the g0 toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def G0(self) -> bool:
        """
        Getter for property: (bool) G0
         Returns the g0 toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) G0

    ##  Returns the g0 toggle   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @G0.setter
    def G0(self, g0: bool):
        """
        Setter for property: (bool) G0
         Returns the g0 toggle   
            
         
        """
        pass
    
    ## Getter for property: (float) G0Tolerance
    ##  Returns the g0 tolerance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return float
    @property
    def G0Tolerance(self) -> float:
        """
        Getter for property: (float) G0Tolerance
         Returns the g0 tolerance   
            
         
        """
        pass
    
    ## Setter for property: (float) G0Tolerance

    ##  Returns the g0 tolerance   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @G0Tolerance.setter
    def G0Tolerance(self, g0Tolerance: float):
        """
        Setter for property: (float) G0Tolerance
         Returns the g0 tolerance   
            
         
        """
        pass
    
    ## Getter for property: (bool) G1
    ##  Returns the g1 toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def G1(self) -> bool:
        """
        Getter for property: (bool) G1
         Returns the g1 toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) G1

    ##  Returns the g1 toggle   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @G1.setter
    def G1(self, g1: bool):
        """
        Setter for property: (bool) G1
         Returns the g1 toggle   
            
         
        """
        pass
    
    ## Getter for property: (float) G1Tolerance
    ##  Returns the g1 tolerance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return float
    @property
    def G1Tolerance(self) -> float:
        """
        Getter for property: (float) G1Tolerance
         Returns the g1 tolerance   
            
         
        """
        pass
    
    ## Setter for property: (float) G1Tolerance

    ##  Returns the g1 tolerance   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @G1Tolerance.setter
    def G1Tolerance(self, g1Tolerance: float):
        """
        Setter for property: (float) G1Tolerance
         Returns the g1 tolerance   
            
         
        """
        pass
    
    ## Getter for property: (bool) G2
    ##  Returns the g2 toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def G2(self) -> bool:
        """
        Getter for property: (bool) G2
         Returns the g2 toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) G2

    ##  Returns the g2 toggle   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @G2.setter
    def G2(self, g2: bool):
        """
        Setter for property: (bool) G2
         Returns the g2 toggle   
            
         
        """
        pass
    
    ## Getter for property: (float) G2Tolerance
    ##  Returns the g2 tolerance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return float
    @property
    def G2Tolerance(self) -> float:
        """
        Getter for property: (float) G2Tolerance
         Returns the g2 tolerance   
            
         
        """
        pass
    
    ## Setter for property: (float) G2Tolerance

    ##  Returns the g2 tolerance   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @G2Tolerance.setter
    def G2Tolerance(self, g2Tolerance: float):
        """
        Setter for property: (float) G2Tolerance
         Returns the g2 tolerance   
            
         
        """
        pass
    
    ## Getter for property: (bool) G3
    ##  Returns the g3 toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def G3(self) -> bool:
        """
        Getter for property: (bool) G3
         Returns the g3 toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) G3

    ##  Returns the g3 toggle   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @G3.setter
    def G3(self, g3: bool):
        """
        Setter for property: (bool) G3
         Returns the g3 toggle   
            
         
        """
        pass
    
    ## Getter for property: (float) G3Tolerance
    ##  Returns the g3 tolerance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return float
    @property
    def G3Tolerance(self) -> float:
        """
        Getter for property: (float) G3Tolerance
         Returns the g3 tolerance   
            
         
        """
        pass
    
    ## Setter for property: (float) G3Tolerance

    ##  Returns the g3 tolerance   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @G3Tolerance.setter
    def G3Tolerance(self, g3Tolerance: float):
        """
        Setter for property: (float) G3Tolerance
         Returns the g3 tolerance   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) MultiFace
    ##  Returns the objects for multi-face   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def MultiFace(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) MultiFace
         Returns the objects for multi-face   
            
         
        """
        pass
    
    ## Getter for property: (int) ReportPer
    ##  Returns the reporting type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return int
    @property
    def ReportPer(self) -> int:
        """
        Getter for property: (int) ReportPer
         Returns the reporting type   
            
         
        """
        pass
    
    ## Setter for property: (int) ReportPer

    ##  Returns the reporting type   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @ReportPer.setter
    def ReportPer(self, reportPer: int):
        """
        Setter for property: (int) ReportPer
         Returns the reporting type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) SecondEdge
    ##  Returns the second edges or faces.  
    ##    Used only if the type is EdgeEdge   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def SecondEdge(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) SecondEdge
         Returns the second edges or faces.  
           Used only if the type is EdgeEdge   
         
        """
        pass
    
    ## Getter for property: (bool) ShowOutOfTolerance
    ##  Returns the out of tolerance only flag   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def ShowOutOfTolerance(self) -> bool:
        """
        Getter for property: (bool) ShowOutOfTolerance
         Returns the out of tolerance only flag   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowOutOfTolerance

    ##  Returns the out of tolerance only flag   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @ShowOutOfTolerance.setter
    def ShowOutOfTolerance(self, outTolerance: bool):
        """
        Setter for property: (bool) ShowOutOfTolerance
         Returns the out of tolerance only flag   
            
         
        """
        pass
    
    ## Getter for property: (bool) ToleranceMarkup
    ##  Returns the tolerance markup flag   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def ToleranceMarkup(self) -> bool:
        """
        Getter for property: (bool) ToleranceMarkup
         Returns the tolerance markup flag   
            
         
        """
        pass
    
    ## Setter for property: (bool) ToleranceMarkup

    ##  Returns the tolerance markup flag   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @ToleranceMarkup.setter
    def ToleranceMarkup(self, markup: bool):
        """
        Setter for property: (bool) ToleranceMarkup
         Returns the tolerance markup flag   
            
         
        """
        pass
    
    ## Getter for property: (@link SurfaceContinuityAnalysisBuilder.Types NXOpen.GeometricAnalysis.SurfaceContinuityAnalysisBuilder.Types@endlink) Type
    ##  Returns the type of analysis to perform   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return SurfaceContinuityAnalysisBuilder.Types
    @property
    def Type(self) -> SurfaceContinuityAnalysisBuilder.Types:
        """
        Getter for property: (@link SurfaceContinuityAnalysisBuilder.Types NXOpen.GeometricAnalysis.SurfaceContinuityAnalysisBuilder.Types@endlink) Type
         Returns the type of analysis to perform   
            
         
        """
        pass
    
    ## Setter for property: (@link SurfaceContinuityAnalysisBuilder.Types NXOpen.GeometricAnalysis.SurfaceContinuityAnalysisBuilder.Types@endlink) Type

    ##  Returns the type of analysis to perform   
    ##     
    ##  
    ## Setter License requirements: gateway ("UG GATEWAY")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @Type.setter
    def Type(self, type: SurfaceContinuityAnalysisBuilder.Types):
        """
        Setter for property: (@link SurfaceContinuityAnalysisBuilder.Types NXOpen.GeometricAnalysis.SurfaceContinuityAnalysisBuilder.Types@endlink) Type
         Returns the type of analysis to perform   
            
         
        """
        pass
    
    ##  Deselection of first edge or face 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: gateway ("UG GATEWAY")
    ## 
    ## <param name="edge"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink) </param>
    ## <param name="face"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink) </param>
    def DeselectFirstEdgeFace(self, edge: NXOpen.DisplayableObject, face: NXOpen.DisplayableObject) -> None:
        """
         Deselection of first edge or face 
        """
        pass
    
    ##  Deselection of second edge or face 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: gateway ("UG GATEWAY")
    ## 
    ## <param name="edge"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink) </param>
    ## <param name="face"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink) </param>
    def DeselectSecondEdgeFace(self, edge: NXOpen.DisplayableObject, face: NXOpen.DisplayableObject) -> None:
        """
         Deselection of second edge or face 
        """
        pass
    
    ##  Returns the edge1 array not used 
    ##  @return faces (@link NXOpen.Face List[NXOpen.Face]@endlink):  .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def GetFace1Array(self) -> List[NXOpen.Face]:
        """
         Returns the edge1 array not used 
         @return faces (@link NXOpen.Face List[NXOpen.Face]@endlink):  .
        """
        pass
    
    ##  Get G0, G1, G2, or G3 result 
    ##  @return isGxGood (bool): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="continuity"> (int) </param>
    def GetGxResult(self, continuity: int) -> bool:
        """
         Get G0, G1, G2, or G3 result 
         @return isGxGood (bool): .
        """
        pass
    
    ##   Selection of first edge or face 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: gateway ("UG GATEWAY")
    ## 
    ## <param name="edge"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink) </param>
    ## <param name="face"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink) </param>
    def SelectFirstEdgeFace(self, edge: NXOpen.DisplayableObject, face: NXOpen.DisplayableObject) -> None:
        """
          Selection of first edge or face 
        """
        pass
    
    ##   Selection of second edge or face 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: gateway ("UG GATEWAY")
    ## 
    ## <param name="edge"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink) </param>
    ## <param name="face"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink) </param>
    def SelectSecondEdgeFace(self, edge: NXOpen.DisplayableObject, face: NXOpen.DisplayableObject) -> None:
        """
          Selection of second edge or face 
        """
        pass
    
    ##  User selects or deselects face, update builder m_edge2, m_face2 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: gateway ("UG GATEWAY")
    ## 
    ## <param name="face"> (@link NXOpen.Face NXOpen.Face@endlink) </param>
    ## <param name="selection_point"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  </param>
    def UpdateFace(self, face: NXOpen.Face, selection_point: NXOpen.Point3d) -> None:
        """
         User selects or deselects face, update builder m_edge2, m_face2 
        """
        pass
    
    ##  The user selects or deselects first edge or face, update builder m_edge1, m_face1 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: gateway ("UG GATEWAY")
    ## 
    ## <param name="edge_or_face"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink)  the parent of Face or Edge </param>
    ## <param name="selection_point"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  </param>
    def UpdateFirstEdgeFace(self, edge_or_face: NXOpen.DisplayableObject, selection_point: NXOpen.Point3d) -> None:
        """
         The user selects or deselects first edge or face, update builder m_edge1, m_face1 
        """
        pass
    
    ##  User selects or deselects second edge or face, update builder m_edge2, m_face2 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: gateway ("UG GATEWAY")
    ## 
    ## <param name="edge_or_face"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink)  the parent of Face or Edge </param>
    ## <param name="selection_point"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  </param>
    def UpdateSecondEdgeFace(self, edge_or_face: NXOpen.DisplayableObject, selection_point: NXOpen.Point3d) -> None:
        """
         User selects or deselects second edge or face, update builder m_edge2, m_face2 
        """
        pass
    
##  Represents a SurfaceContinuityAnalysis builder  <br> To create or edit an instance of this class, use @link NXOpen::GeometricAnalysis::SurfaceContinuityAnalysisBuilder  NXOpen::GeometricAnalysis::SurfaceContinuityAnalysisBuilder @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class SurfaceContinuityAnalysis(AnalysisObject): 
    """ Represents a SurfaceContinuityAnalysis builder """
    pass


import NXOpen
import NXOpen.GeometricUtilities
##  Represents a @link NXOpen::GeometricAnalysis::SurfaceIntersection NXOpen::GeometricAnalysis::SurfaceIntersection@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisObjectCollection::CreateSurfaceIntersectionBuilder  NXOpen::GeometricAnalysis::AnalysisObjectCollection::CreateSurfaceIntersectionBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## CalculationMethod </term> <description> 
##  
## Curvature </description> </item> 
## 
## <item><term> 
##  
## DynamicProjection </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## NeedleDirection </term> <description> 
##  
## Outside </description> </item> 
## 
## <item><term> 
##  
## ProjectionNormalFace </term> <description> 
##  
## FaceSet1 </description> </item> 
## 
## <item><term> 
##  
## ProjectionOption </term> <description> 
##  
## None </description> </item> 
## 
## <item><term> 
##  
## ProjectionXYZ </term> <description> 
##  
## X </description> </item> 
## 
## <item><term> 
##  
## ScalingMethod </term> <description> 
##  
## Linear </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX7.5.0  <br> 

class SurfaceIntersectionBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.GeometricAnalysis.SurfaceIntersection</ja_class> builder """


    ##  Enumeration for needle calculation method 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Curvature</term><description> 
    ##  needle of curvature value </description> </item><item><term> 
    ## RadiusofCurvature</term><description> 
    ##  needle of radius of curvature value </description> </item></list>
    class CalculationTypes(Enum):
        """
        Members Include: <Curvature> <RadiusofCurvature>
        """
        Curvature: int
        RadiusofCurvature: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SurfaceIntersectionBuilder.CalculationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Enumeration for needle direction type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Inside</term><description> 
    ##  needle pointing inside  </description> </item><item><term> 
    ## Outside</term><description> 
    ##  needle pointing outside </description> </item></list>
    class DirectionTypes(Enum):
        """
        Members Include: <Inside> <Outside>
        """
        Inside: int
        Outside: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SurfaceIntersectionBuilder.DirectionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Enumeration for label computation method 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Curvature</term><description> 
    ##  label showing curvature value </description> </item><item><term> 
    ## RadiusOfCurvature</term><description> 
    ##  label showing radius of curvature value </description> </item></list>
    class LabelValues(Enum):
        """
        Members Include: <Curvature> <RadiusOfCurvature>
        """
        Curvature: int
        RadiusOfCurvature: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SurfaceIntersectionBuilder.LabelValues:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Enumeration for face normal 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## FaceSet1</term><description> 
    ##  linear needle </description> </item><item><term> 
    ## FaceSet2</term><description> 
    ##  logarithmic needle </description> </item></list>
    class NormalTypes(Enum):
        """
        Members Include: <FaceSet1> <FaceSet2>
        """
        FaceSet1: int
        FaceSet2: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SurfaceIntersectionBuilder.NormalTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Projection  types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  no projection  </description> </item><item><term> 
    ## Normal</term><description> 
    ##  face normal </description> </item><item><term> 
    ## Vector</term><description> 
    ##  specify vector </description> </item><item><term> 
    ## View</term><description> 
    ##  view plane     </description> </item><item><term> 
    ## Xyz</term><description> 
    ##  specify x,y,z plane </description> </item></list>
    class ProjectionTypes(Enum):
        """
        Members Include: <NotSet> <Normal> <Vector> <View> <Xyz>
        """
        NotSet: int
        Normal: int
        Vector: int
        View: int
        Xyz: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SurfaceIntersectionBuilder.ProjectionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Enumeration for needle display type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Linear</term><description> 
    ##  linear needle </description> </item><item><term> 
    ## Logarithmic</term><description> 
    ##  logarithmic needle </description> </item></list>
    class ScalingTypes(Enum):
        """
        Members Include: <Linear> <Logarithmic>
        """
        Linear: int
        Logarithmic: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SurfaceIntersectionBuilder.ScalingTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Enumeration for X, Y or Z projection plane 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## X</term><description> 
    ##  x-axis plane </description> </item><item><term> 
    ## Y</term><description> 
    ##  y-axis plane </description> </item><item><term> 
    ## Z</term><description> 
    ##  z-axis plane </description> </item></list>
    class XyzTypes(Enum):
        """
        Members Include: <X> <Y> <Z>
        """
        X: int
        Y: int
        Z: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SurfaceIntersectionBuilder.XyzTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link SurfaceIntersectionBuilder.CalculationTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.CalculationTypes@endlink) CalculationMethod
    ##  Returns the calculation method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return SurfaceIntersectionBuilder.CalculationTypes
    @property
    def CalculationMethod(self) -> SurfaceIntersectionBuilder.CalculationTypes:
        """
        Getter for property: (@link SurfaceIntersectionBuilder.CalculationTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.CalculationTypes@endlink) CalculationMethod
         Returns the calculation method   
            
         
        """
        pass
    
    ## Setter for property: (@link SurfaceIntersectionBuilder.CalculationTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.CalculationTypes@endlink) CalculationMethod

    ##  Returns the calculation method   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @CalculationMethod.setter
    def CalculationMethod(self, calculationMethod: SurfaceIntersectionBuilder.CalculationTypes):
        """
        Setter for property: (@link SurfaceIntersectionBuilder.CalculationTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.CalculationTypes@endlink) CalculationMethod
         Returns the calculation method   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.CombOptionsBuilder NXOpen.GeometricUtilities.CombOptionsBuilder@endlink) CombOptions
    ##  Returns the comb display block options   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.GeometricUtilities.CombOptionsBuilder
    @property
    def CombOptions(self) -> NXOpen.GeometricUtilities.CombOptionsBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.CombOptionsBuilder NXOpen.GeometricUtilities.CombOptionsBuilder@endlink) CombOptions
         Returns the comb display block options   
            
         
        """
        pass
    
    ## Getter for property: (bool) DynamicProjection
    ##  Returns the dynamic projection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def DynamicProjection(self) -> bool:
        """
        Getter for property: (bool) DynamicProjection
         Returns the dynamic projection   
            
         
        """
        pass
    
    ## Setter for property: (bool) DynamicProjection

    ##  Returns the dynamic projection   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @DynamicProjection.setter
    def DynamicProjection(self, dynamicProjection: bool):
        """
        Setter for property: (bool) DynamicProjection
         Returns the dynamic projection   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FirstFaceSet
    ##  Returns the first selected face set   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def FirstFaceSet(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FirstFaceSet
         Returns the first selected face set   
            
         
        """
        pass
    
    ## Getter for property: (@link SurfaceIntersectionBuilder.DirectionTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.DirectionTypes@endlink) NeedleDirection
    ##  Returns the needle direction   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return SurfaceIntersectionBuilder.DirectionTypes
    @property
    def NeedleDirection(self) -> SurfaceIntersectionBuilder.DirectionTypes:
        """
        Getter for property: (@link SurfaceIntersectionBuilder.DirectionTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.DirectionTypes@endlink) NeedleDirection
         Returns the needle direction   
            
         
        """
        pass
    
    ## Setter for property: (@link SurfaceIntersectionBuilder.DirectionTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.DirectionTypes@endlink) NeedleDirection

    ##  Returns the needle direction   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @NeedleDirection.setter
    def NeedleDirection(self, needleDirection: SurfaceIntersectionBuilder.DirectionTypes):
        """
        Setter for property: (@link SurfaceIntersectionBuilder.DirectionTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.DirectionTypes@endlink) NeedleDirection
         Returns the needle direction   
            
         
        """
        pass
    
    ## Getter for property: (@link SurfaceIntersectionBuilder.NormalTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.NormalTypes@endlink) ProjectionNormalFace
    ##  Returns the face normal projection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return SurfaceIntersectionBuilder.NormalTypes
    @property
    def ProjectionNormalFace(self) -> SurfaceIntersectionBuilder.NormalTypes:
        """
        Getter for property: (@link SurfaceIntersectionBuilder.NormalTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.NormalTypes@endlink) ProjectionNormalFace
         Returns the face normal projection   
            
         
        """
        pass
    
    ## Setter for property: (@link SurfaceIntersectionBuilder.NormalTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.NormalTypes@endlink) ProjectionNormalFace

    ##  Returns the face normal projection   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @ProjectionNormalFace.setter
    def ProjectionNormalFace(self, normalFace: SurfaceIntersectionBuilder.NormalTypes):
        """
        Setter for property: (@link SurfaceIntersectionBuilder.NormalTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.NormalTypes@endlink) ProjectionNormalFace
         Returns the face normal projection   
            
         
        """
        pass
    
    ## Getter for property: (@link SurfaceIntersectionBuilder.ProjectionTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.ProjectionTypes@endlink) ProjectionOption
    ##  Returns the projection option  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return SurfaceIntersectionBuilder.ProjectionTypes
    @property
    def ProjectionOption(self) -> SurfaceIntersectionBuilder.ProjectionTypes:
        """
        Getter for property: (@link SurfaceIntersectionBuilder.ProjectionTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.ProjectionTypes@endlink) ProjectionOption
         Returns the projection option  
            
         
        """
        pass
    
    ## Setter for property: (@link SurfaceIntersectionBuilder.ProjectionTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.ProjectionTypes@endlink) ProjectionOption

    ##  Returns the projection option  
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @ProjectionOption.setter
    def ProjectionOption(self, projectionOption: SurfaceIntersectionBuilder.ProjectionTypes):
        """
        Setter for property: (@link SurfaceIntersectionBuilder.ProjectionTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.ProjectionTypes@endlink) ProjectionOption
         Returns the projection option  
            
         
        """
        pass
    
    ## Getter for property: (@link SurfaceIntersectionBuilder.XyzTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.XyzTypes@endlink) ProjectionXYZ
    ##  Returns the xyz projection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return SurfaceIntersectionBuilder.XyzTypes
    @property
    def ProjectionXYZ(self) -> SurfaceIntersectionBuilder.XyzTypes:
        """
        Getter for property: (@link SurfaceIntersectionBuilder.XyzTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.XyzTypes@endlink) ProjectionXYZ
         Returns the xyz projection   
            
         
        """
        pass
    
    ## Setter for property: (@link SurfaceIntersectionBuilder.XyzTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.XyzTypes@endlink) ProjectionXYZ

    ##  Returns the xyz projection   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @ProjectionXYZ.setter
    def ProjectionXYZ(self, projectionXYZ: SurfaceIntersectionBuilder.XyzTypes):
        """
        Setter for property: (@link SurfaceIntersectionBuilder.XyzTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.XyzTypes@endlink) ProjectionXYZ
         Returns the xyz projection   
            
         
        """
        pass
    
    ## Getter for property: (@link SurfaceIntersectionBuilder.ScalingTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.ScalingTypes@endlink) ScalingMethod
    ##  Returns the scaling method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return SurfaceIntersectionBuilder.ScalingTypes
    @property
    def ScalingMethod(self) -> SurfaceIntersectionBuilder.ScalingTypes:
        """
        Getter for property: (@link SurfaceIntersectionBuilder.ScalingTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.ScalingTypes@endlink) ScalingMethod
         Returns the scaling method   
            
         
        """
        pass
    
    ## Setter for property: (@link SurfaceIntersectionBuilder.ScalingTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.ScalingTypes@endlink) ScalingMethod

    ##  Returns the scaling method   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @ScalingMethod.setter
    def ScalingMethod(self, scalingMethod: SurfaceIntersectionBuilder.ScalingTypes):
        """
        Setter for property: (@link SurfaceIntersectionBuilder.ScalingTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.ScalingTypes@endlink) ScalingMethod
         Returns the scaling method   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SecondFaceSet
    ##  Returns the second selected face set   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def SecondFaceSet(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SecondFaceSet
         Returns the second selected face set   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector
    ##  Returns the vector   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Direction
    @property
    def Vector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector
         Returns the vector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector

    ##  Returns the vector   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @Vector.setter
    def Vector(self, vector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector
         Returns the vector   
            
         
        """
        pass
    
    ##  Update work view with a given view matrix 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: studio_analyze ("STUDIO ANALYZE")
    def UpdateWorkView(self) -> None:
        """
         Update work view with a given view matrix 
        """
        pass
    
##  Represents a SurfaceIntersection builder  <br> To create or edit an instance of this class, use @link NXOpen::GeometricAnalysis::SurfaceIntersectionBuilder  NXOpen::GeometricAnalysis::SurfaceIntersectionBuilder @endlink  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class SurfaceIntersection(AnalysisObject): 
    """ Represents a SurfaceIntersection builder """
    pass


## @package NXOpen.GeometricAnalysis
## Classes, Enums and Structs under NXOpen.GeometricAnalysis namespace

##  @link CurveAnalysisDisplayShowFlagType NXOpen.GeometricAnalysis.CurveAnalysisDisplayShowFlagType @endlink is an alias for @link CurveAnalysisDisplay.ShowFlagType NXOpen.GeometricAnalysis.CurveAnalysisDisplay.ShowFlagType@endlink
CurveAnalysisDisplayShowFlagType = CurveAnalysisDisplay.ShowFlagType


##  @link CurveAnalysisRecordDirectionOptionType NXOpen.GeometricAnalysis.CurveAnalysisRecordDirectionOptionType @endlink is an alias for @link CurveAnalysisRecord.DirectionOptionType NXOpen.GeometricAnalysis.CurveAnalysisRecord.DirectionOptionType@endlink
CurveAnalysisRecordDirectionOptionType = CurveAnalysisRecord.DirectionOptionType


##  @link CurveContinuityBuilderType NXOpen.GeometricAnalysis.CurveContinuityBuilderType @endlink is an alias for @link CurveContinuityBuilder.Type NXOpen.GeometricAnalysis.CurveContinuityBuilder.Type@endlink
CurveContinuityBuilderType = CurveContinuityBuilder.Type


##  @link CurveCurvatureAnalysisBuilderCalculationMethod NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilderCalculationMethod @endlink is an alias for @link CurveCurvatureAnalysisBuilder.CalculationMethod NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilder.CalculationMethod@endlink
CurveCurvatureAnalysisBuilderCalculationMethod = CurveCurvatureAnalysisBuilder.CalculationMethod


##  @link CurveCurvatureAnalysisBuilderDisplayStyle NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilderDisplayStyle @endlink is an alias for @link CurveCurvatureAnalysisBuilder.DisplayStyle NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilder.DisplayStyle@endlink
CurveCurvatureAnalysisBuilderDisplayStyle = CurveCurvatureAnalysisBuilder.DisplayStyle


##  @link CurveCurvatureAnalysisBuilderLabelValues NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilderLabelValues @endlink is an alias for @link CurveCurvatureAnalysisBuilder.LabelValues NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilder.LabelValues@endlink
CurveCurvatureAnalysisBuilderLabelValues = CurveCurvatureAnalysisBuilder.LabelValues


##  @link CurveCurvatureAnalysisBuilderNeedleDirection NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilderNeedleDirection @endlink is an alias for @link CurveCurvatureAnalysisBuilder.NeedleDirection NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilder.NeedleDirection@endlink
CurveCurvatureAnalysisBuilderNeedleDirection = CurveCurvatureAnalysisBuilder.NeedleDirection


##  @link CurveCurvatureAnalysisBuilderProjectionTypes NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilderProjectionTypes @endlink is an alias for @link CurveCurvatureAnalysisBuilder.ProjectionTypes NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilder.ProjectionTypes@endlink
CurveCurvatureAnalysisBuilderProjectionTypes = CurveCurvatureAnalysisBuilder.ProjectionTypes


##  @link CurveCurvatureAnalysisBuilderXyzTypes NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilderXyzTypes @endlink is an alias for @link CurveCurvatureAnalysisBuilder.XyzTypes NXOpen.GeometricAnalysis.CurveCurvatureAnalysisBuilder.XyzTypes@endlink
CurveCurvatureAnalysisBuilderXyzTypes = CurveCurvatureAnalysisBuilder.XyzTypes


##  @link DeviationCheckingDeviationOptions NXOpen.GeometricAnalysis.DeviationCheckingDeviationOptions @endlink is an alias for @link DeviationChecking.DeviationOptions NXOpen.GeometricAnalysis.DeviationChecking.DeviationOptions@endlink
DeviationCheckingDeviationOptions = DeviationChecking.DeviationOptions


##  @link DeviationCheckingTypes NXOpen.GeometricAnalysis.DeviationCheckingTypes @endlink is an alias for @link DeviationChecking.Types NXOpen.GeometricAnalysis.DeviationChecking.Types@endlink
DeviationCheckingTypes = DeviationChecking.Types


##  @link DeviationGaugeBuilderAdditionalValuesLabelType NXOpen.GeometricAnalysis.DeviationGaugeBuilderAdditionalValuesLabelType @endlink is an alias for @link DeviationGaugeBuilder.AdditionalValuesLabelType NXOpen.GeometricAnalysis.DeviationGaugeBuilder.AdditionalValuesLabelType@endlink
DeviationGaugeBuilderAdditionalValuesLabelType = DeviationGaugeBuilder.AdditionalValuesLabelType


##  @link DeviationGaugeBuilderColorPlotTypes NXOpen.GeometricAnalysis.DeviationGaugeBuilderColorPlotTypes @endlink is an alias for @link DeviationGaugeBuilder.ColorPlotTypes NXOpen.GeometricAnalysis.DeviationGaugeBuilder.ColorPlotTypes@endlink
DeviationGaugeBuilderColorPlotTypes = DeviationGaugeBuilder.ColorPlotTypes


##  @link DeviationGaugeBuilderMeasurementMethodType NXOpen.GeometricAnalysis.DeviationGaugeBuilderMeasurementMethodType @endlink is an alias for @link DeviationGaugeBuilder.MeasurementMethodType NXOpen.GeometricAnalysis.DeviationGaugeBuilder.MeasurementMethodType@endlink
DeviationGaugeBuilderMeasurementMethodType = DeviationGaugeBuilder.MeasurementMethodType


##  @link DeviationGaugeBuilderMinMaxType NXOpen.GeometricAnalysis.DeviationGaugeBuilderMinMaxType @endlink is an alias for @link DeviationGaugeBuilder.MinMaxType NXOpen.GeometricAnalysis.DeviationGaugeBuilder.MinMaxType@endlink
DeviationGaugeBuilderMinMaxType = DeviationGaugeBuilder.MinMaxType


##  @link DeviationGaugeBuilderReportingPerTypes NXOpen.GeometricAnalysis.DeviationGaugeBuilderReportingPerTypes @endlink is an alias for @link DeviationGaugeBuilder.ReportingPerTypes NXOpen.GeometricAnalysis.DeviationGaugeBuilder.ReportingPerTypes@endlink
DeviationGaugeBuilderReportingPerTypes = DeviationGaugeBuilder.ReportingPerTypes


##  @link DeviationGaugeBuilderXyzDirectionType NXOpen.GeometricAnalysis.DeviationGaugeBuilderXyzDirectionType @endlink is an alias for @link DeviationGaugeBuilder.XyzDirectionType NXOpen.GeometricAnalysis.DeviationGaugeBuilder.XyzDirectionType@endlink
DeviationGaugeBuilderXyzDirectionType = DeviationGaugeBuilder.XyzDirectionType


##  @link DistanceAnalysisBuilder1DisplayModes NXOpen.GeometricAnalysis.DistanceAnalysisBuilder1DisplayModes @endlink is an alias for @link DistanceAnalysisBuilder1.DisplayModes NXOpen.GeometricAnalysis.DistanceAnalysisBuilder1.DisplayModes@endlink
DistanceAnalysisBuilder1DisplayModes = DistanceAnalysisBuilder1.DisplayModes


##  @link DistanceAnalysisBuilderDisplayModes NXOpen.GeometricAnalysis.DistanceAnalysisBuilderDisplayModes @endlink is an alias for @link DistanceAnalysisBuilder.DisplayModes NXOpen.GeometricAnalysis.DistanceAnalysisBuilder.DisplayModes@endlink
DistanceAnalysisBuilderDisplayModes = DistanceAnalysisBuilder.DisplayModes


##  @link DraftAnalysisBuilderDrawDirection NXOpen.GeometricAnalysis.DraftAnalysisBuilderDrawDirection @endlink is an alias for @link DraftAnalysisBuilder.DrawDirection NXOpen.GeometricAnalysis.DraftAnalysisBuilder.DrawDirection@endlink
DraftAnalysisBuilderDrawDirection = DraftAnalysisBuilder.DrawDirection


##  @link DraftAnalysisBuilderSelectOutput NXOpen.GeometricAnalysis.DraftAnalysisBuilderSelectOutput @endlink is an alias for @link DraftAnalysisBuilder.SelectOutput NXOpen.GeometricAnalysis.DraftAnalysisBuilder.SelectOutput@endlink
DraftAnalysisBuilderSelectOutput = DraftAnalysisBuilder.SelectOutput


##  @link ExamineGeometryCheck NXOpen.GeometricAnalysis.ExamineGeometryCheck @endlink is an alias for @link ExamineGeometry.Check NXOpen.GeometricAnalysis.ExamineGeometry.Check@endlink
ExamineGeometryCheck = ExamineGeometry.Check


##  @link FaceAnalysisDataRangeBuilderColorScaleOptions NXOpen.GeometricAnalysis.FaceAnalysisDataRangeBuilderColorScaleOptions @endlink is an alias for @link FaceAnalysisDataRangeBuilder.ColorScaleOptions NXOpen.GeometricAnalysis.FaceAnalysisDataRangeBuilder.ColorScaleOptions@endlink
FaceAnalysisDataRangeBuilderColorScaleOptions = FaceAnalysisDataRangeBuilder.ColorScaleOptions


##  @link FaceAnalysisDataRangeBuilderNumberOfColorsOptions NXOpen.GeometricAnalysis.FaceAnalysisDataRangeBuilderNumberOfColorsOptions @endlink is an alias for @link FaceAnalysisDataRangeBuilder.NumberOfColorsOptions NXOpen.GeometricAnalysis.FaceAnalysisDataRangeBuilder.NumberOfColorsOptions@endlink
FaceAnalysisDataRangeBuilderNumberOfColorsOptions = FaceAnalysisDataRangeBuilder.NumberOfColorsOptions


##  @link FaceAnalysisDisplayBuilderColorLegendOptions NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilderColorLegendOptions @endlink is an alias for @link FaceAnalysisDisplayBuilder.ColorLegendOptions NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilder.ColorLegendOptions@endlink
FaceAnalysisDisplayBuilderColorLegendOptions = FaceAnalysisDisplayBuilder.ColorLegendOptions


##  @link FaceAnalysisDisplayBuilderColorsOptions NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilderColorsOptions @endlink is an alias for @link FaceAnalysisDisplayBuilder.ColorsOptions NXOpen.GeometricAnalysis.FaceAnalysisDisplayBuilder.ColorsOptions@endlink
FaceAnalysisDisplayBuilderColorsOptions = FaceAnalysisDisplayBuilder.ColorsOptions


##  @link FaceCurvatureAnalysisBuilderCurvatureTypes NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilderCurvatureTypes @endlink is an alias for @link FaceCurvatureAnalysisBuilder.CurvatureTypes NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder.CurvatureTypes@endlink
FaceCurvatureAnalysisBuilderCurvatureTypes = FaceCurvatureAnalysisBuilder.CurvatureTypes


##  @link FaceCurvatureAnalysisBuilderDirectionTypes NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilderDirectionTypes @endlink is an alias for @link FaceCurvatureAnalysisBuilder.DirectionTypes NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder.DirectionTypes@endlink
FaceCurvatureAnalysisBuilderDirectionTypes = FaceCurvatureAnalysisBuilder.DirectionTypes


##  @link FaceCurvatureAnalysisBuilderDisplayTypes NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilderDisplayTypes @endlink is an alias for @link FaceCurvatureAnalysisBuilder.DisplayTypes NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder.DisplayTypes@endlink
FaceCurvatureAnalysisBuilderDisplayTypes = FaceCurvatureAnalysisBuilder.DisplayTypes


##  @link FaceCurvatureAnalysisBuilderScaleTypes NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilderScaleTypes @endlink is an alias for @link FaceCurvatureAnalysisBuilder.ScaleTypes NXOpen.GeometricAnalysis.FaceCurvatureAnalysisBuilder.ScaleTypes@endlink
FaceCurvatureAnalysisBuilderScaleTypes = FaceCurvatureAnalysisBuilder.ScaleTypes


##  @link GapFlushnessBuilderDisplayOptions NXOpen.GeometricAnalysis.GapFlushnessBuilderDisplayOptions @endlink is an alias for @link GapFlushnessBuilder.DisplayOptions NXOpen.GeometricAnalysis.GapFlushnessBuilder.DisplayOptions@endlink
GapFlushnessBuilderDisplayOptions = GapFlushnessBuilder.DisplayOptions


##  @link GapFlushnessBuilderEvaluationModes NXOpen.GeometricAnalysis.GapFlushnessBuilderEvaluationModes @endlink is an alias for @link GapFlushnessBuilder.EvaluationModes NXOpen.GeometricAnalysis.GapFlushnessBuilder.EvaluationModes@endlink
GapFlushnessBuilderEvaluationModes = GapFlushnessBuilder.EvaluationModes


##  @link GapFlushnessBuilderEvaluationTypes NXOpen.GeometricAnalysis.GapFlushnessBuilderEvaluationTypes @endlink is an alias for @link GapFlushnessBuilder.EvaluationTypes NXOpen.GeometricAnalysis.GapFlushnessBuilder.EvaluationTypes@endlink
GapFlushnessBuilderEvaluationTypes = GapFlushnessBuilder.EvaluationTypes


##  @link GapFlushnessBuilderPanelTypes NXOpen.GeometricAnalysis.GapFlushnessBuilderPanelTypes @endlink is an alias for @link GapFlushnessBuilder.PanelTypes NXOpen.GeometricAnalysis.GapFlushnessBuilder.PanelTypes@endlink
GapFlushnessBuilderPanelTypes = GapFlushnessBuilder.PanelTypes


##  @link GapFlushnessBuilderSectionAlignments NXOpen.GeometricAnalysis.GapFlushnessBuilderSectionAlignments @endlink is an alias for @link GapFlushnessBuilder.SectionAlignments NXOpen.GeometricAnalysis.GapFlushnessBuilder.SectionAlignments@endlink
GapFlushnessBuilderSectionAlignments = GapFlushnessBuilder.SectionAlignments


##  @link GapFlushnessBuilderSectionCurveOptions NXOpen.GeometricAnalysis.GapFlushnessBuilderSectionCurveOptions @endlink is an alias for @link GapFlushnessBuilder.SectionCurveOptions NXOpen.GeometricAnalysis.GapFlushnessBuilder.SectionCurveOptions@endlink
GapFlushnessBuilderSectionCurveOptions = GapFlushnessBuilder.SectionCurveOptions


## @link GeometricPropertiesCaeCurve_Struct NXOpen.GeometricAnalysis.GeometricPropertiesCaeCurve_Struct@endlink is an alias for @link GeometricProperties.CaeCurve NXOpen.GeometricAnalysis.GeometricProperties.CaeCurve@endlink.
GeometricPropertiesCaeCurve_Struct = GeometricProperties.CaeCurve


## @link GeometricPropertiesCaeFace_Struct NXOpen.GeometricAnalysis.GeometricPropertiesCaeFace_Struct@endlink is an alias for @link GeometricProperties.CaeFace NXOpen.GeometricAnalysis.GeometricProperties.CaeFace@endlink.
GeometricPropertiesCaeFace_Struct = GeometricProperties.CaeFace


## @link GeometricPropertiesEdge_Struct NXOpen.GeometricAnalysis.GeometricPropertiesEdge_Struct@endlink is an alias for @link GeometricProperties.Edge NXOpen.GeometricAnalysis.GeometricProperties.Edge@endlink.
GeometricPropertiesEdge_Struct = GeometricProperties.Edge


##  @link GeometricPropertiesEntity NXOpen.GeometricAnalysis.GeometricPropertiesEntity @endlink is an alias for @link GeometricProperties.Entity NXOpen.GeometricAnalysis.GeometricProperties.Entity@endlink
GeometricPropertiesEntity = GeometricProperties.Entity


## @link GeometricPropertiesFace_Struct NXOpen.GeometricAnalysis.GeometricPropertiesFace_Struct@endlink is an alias for @link GeometricProperties.Face NXOpen.GeometricAnalysis.GeometricProperties.Face@endlink.
GeometricPropertiesFace_Struct = GeometricProperties.Face


##  @link GeometricPropertiesOutputType NXOpen.GeometricAnalysis.GeometricPropertiesOutputType @endlink is an alias for @link GeometricProperties.OutputType NXOpen.GeometricAnalysis.GeometricProperties.OutputType@endlink
GeometricPropertiesOutputType = GeometricProperties.OutputType


##  @link GeometricPropertiesStatus NXOpen.GeometricAnalysis.GeometricPropertiesStatus @endlink is an alias for @link GeometricProperties.Status NXOpen.GeometricAnalysis.GeometricProperties.Status@endlink
GeometricPropertiesStatus = GeometricProperties.Status


##  @link HighlightLinesAnalysisBuilderDisplayMethods NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilderDisplayMethods @endlink is an alias for @link HighlightLinesAnalysisBuilder.DisplayMethods NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.DisplayMethods@endlink
HighlightLinesAnalysisBuilderDisplayMethods = HighlightLinesAnalysisBuilder.DisplayMethods


##  @link HighlightLinesAnalysisBuilderDisplayModes NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilderDisplayModes @endlink is an alias for @link HighlightLinesAnalysisBuilder.DisplayModes NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.DisplayModes@endlink
HighlightLinesAnalysisBuilderDisplayModes = HighlightLinesAnalysisBuilder.DisplayModes


##  @link HighlightLinesAnalysisBuilderIsoclineDirection NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilderIsoclineDirection @endlink is an alias for @link HighlightLinesAnalysisBuilder.IsoclineDirection NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.IsoclineDirection@endlink
HighlightLinesAnalysisBuilderIsoclineDirection = HighlightLinesAnalysisBuilder.IsoclineDirection


##  @link HighlightLinesAnalysisBuilderLightPlacements NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilderLightPlacements @endlink is an alias for @link HighlightLinesAnalysisBuilder.LightPlacements NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.LightPlacements@endlink
HighlightLinesAnalysisBuilderLightPlacements = HighlightLinesAnalysisBuilder.LightPlacements


##  @link HighlightLinesAnalysisBuilderLightPlaneOptions NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilderLightPlaneOptions @endlink is an alias for @link HighlightLinesAnalysisBuilder.LightPlaneOptions NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.LightPlaneOptions@endlink
HighlightLinesAnalysisBuilderLightPlaneOptions = HighlightLinesAnalysisBuilder.LightPlaneOptions


##  @link HighlightLinesAnalysisBuilderOutputOption NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilderOutputOption @endlink is an alias for @link HighlightLinesAnalysisBuilder.OutputOption NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.OutputOption@endlink
HighlightLinesAnalysisBuilderOutputOption = HighlightLinesAnalysisBuilder.OutputOption


##  @link HighlightLinesAnalysisBuilderResolutions NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilderResolutions @endlink is an alias for @link HighlightLinesAnalysisBuilder.Resolutions NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.Resolutions@endlink
HighlightLinesAnalysisBuilderResolutions = HighlightLinesAnalysisBuilder.Resolutions


##  @link HighlightLinesAnalysisBuilderTypes2 NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilderTypes2 @endlink is an alias for @link HighlightLinesAnalysisBuilder.Types2 NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.Types2@endlink
HighlightLinesAnalysisBuilderTypes2 = HighlightLinesAnalysisBuilder.Types2


##  @link HighlightLinesAnalysisBuilderTypes NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilderTypes @endlink is an alias for @link HighlightLinesAnalysisBuilder.Types NXOpen.GeometricAnalysis.HighlightLinesAnalysisBuilder.Types@endlink
HighlightLinesAnalysisBuilderTypes = HighlightLinesAnalysisBuilder.Types


##  @link PerformancePredictorSolveOption NXOpen.GeometricAnalysis.PerformancePredictorSolveOption @endlink is an alias for @link PerformancePredictor.SolveOption NXOpen.GeometricAnalysis.PerformancePredictor.SolveOption@endlink
PerformancePredictorSolveOption = PerformancePredictor.SolveOption


##  @link RadiusAnalysisBuilder1DisplayModes NXOpen.GeometricAnalysis.RadiusAnalysisBuilder1DisplayModes @endlink is an alias for @link RadiusAnalysisBuilder1.DisplayModes NXOpen.GeometricAnalysis.RadiusAnalysisBuilder1.DisplayModes@endlink
RadiusAnalysisBuilder1DisplayModes = RadiusAnalysisBuilder1.DisplayModes


##  @link RadiusAnalysisBuilder1Types NXOpen.GeometricAnalysis.RadiusAnalysisBuilder1Types @endlink is an alias for @link RadiusAnalysisBuilder1.Types NXOpen.GeometricAnalysis.RadiusAnalysisBuilder1.Types@endlink
RadiusAnalysisBuilder1Types = RadiusAnalysisBuilder1.Types


##  @link RadiusAnalysisBuilderDisplayModes NXOpen.GeometricAnalysis.RadiusAnalysisBuilderDisplayModes @endlink is an alias for @link RadiusAnalysisBuilder.DisplayModes NXOpen.GeometricAnalysis.RadiusAnalysisBuilder.DisplayModes@endlink
RadiusAnalysisBuilderDisplayModes = RadiusAnalysisBuilder.DisplayModes


##  @link RadiusAnalysisBuilderTypes NXOpen.GeometricAnalysis.RadiusAnalysisBuilderTypes @endlink is an alias for @link RadiusAnalysisBuilder.Types NXOpen.GeometricAnalysis.RadiusAnalysisBuilder.Types@endlink
RadiusAnalysisBuilderTypes = RadiusAnalysisBuilder.Types


##  @link ReflectionAnalysisBuilder1ImageMovementTypes NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1ImageMovementTypes @endlink is an alias for @link ReflectionAnalysisBuilder1.ImageMovementTypes NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.ImageMovementTypes@endlink
ReflectionAnalysisBuilder1ImageMovementTypes = ReflectionAnalysisBuilder1.ImageMovementTypes


##  @link ReflectionAnalysisBuilder1ImageSizeOption NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1ImageSizeOption @endlink is an alias for @link ReflectionAnalysisBuilder1.ImageSizeOption NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.ImageSizeOption@endlink
ReflectionAnalysisBuilder1ImageSizeOption = ReflectionAnalysisBuilder1.ImageSizeOption


##  @link ReflectionAnalysisBuilder1LineImageTypes NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1LineImageTypes @endlink is an alias for @link ReflectionAnalysisBuilder1.LineImageTypes NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.LineImageTypes@endlink
ReflectionAnalysisBuilder1LineImageTypes = ReflectionAnalysisBuilder1.LineImageTypes


##  @link ReflectionAnalysisBuilder1LineOrientationType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1LineOrientationType @endlink is an alias for @link ReflectionAnalysisBuilder1.LineOrientationType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.LineOrientationType@endlink
ReflectionAnalysisBuilder1LineOrientationType = ReflectionAnalysisBuilder1.LineOrientationType


##  @link ReflectionAnalysisBuilder1LineThicknessType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1LineThicknessType @endlink is an alias for @link ReflectionAnalysisBuilder1.LineThicknessType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.LineThicknessType@endlink
ReflectionAnalysisBuilder1LineThicknessType = ReflectionAnalysisBuilder1.LineThicknessType


##  @link ReflectionAnalysisBuilder1NumberOfLinesOptions NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1NumberOfLinesOptions @endlink is an alias for @link ReflectionAnalysisBuilder1.NumberOfLinesOptions NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.NumberOfLinesOptions@endlink
ReflectionAnalysisBuilder1NumberOfLinesOptions = ReflectionAnalysisBuilder1.NumberOfLinesOptions


##  @link ReflectionAnalysisBuilder1SceneImageType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1SceneImageType @endlink is an alias for @link ReflectionAnalysisBuilder1.SceneImageType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.SceneImageType@endlink
ReflectionAnalysisBuilder1SceneImageType = ReflectionAnalysisBuilder1.SceneImageType


##  @link ReflectionAnalysisBuilder1Types NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1Types @endlink is an alias for @link ReflectionAnalysisBuilder1.Types NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder1.Types@endlink
ReflectionAnalysisBuilder1Types = ReflectionAnalysisBuilder1.Types


##  @link ReflectionAnalysisBuilderImageMovementTypes NXOpen.GeometricAnalysis.ReflectionAnalysisBuilderImageMovementTypes @endlink is an alias for @link ReflectionAnalysisBuilder.ImageMovementTypes NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.ImageMovementTypes@endlink
ReflectionAnalysisBuilderImageMovementTypes = ReflectionAnalysisBuilder.ImageMovementTypes


##  @link ReflectionAnalysisBuilderImageSizeOption NXOpen.GeometricAnalysis.ReflectionAnalysisBuilderImageSizeOption @endlink is an alias for @link ReflectionAnalysisBuilder.ImageSizeOption NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.ImageSizeOption@endlink
ReflectionAnalysisBuilderImageSizeOption = ReflectionAnalysisBuilder.ImageSizeOption


##  @link ReflectionAnalysisBuilderLineImageTypes NXOpen.GeometricAnalysis.ReflectionAnalysisBuilderLineImageTypes @endlink is an alias for @link ReflectionAnalysisBuilder.LineImageTypes NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.LineImageTypes@endlink
ReflectionAnalysisBuilderLineImageTypes = ReflectionAnalysisBuilder.LineImageTypes


##  @link ReflectionAnalysisBuilderLineOrientationType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilderLineOrientationType @endlink is an alias for @link ReflectionAnalysisBuilder.LineOrientationType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.LineOrientationType@endlink
ReflectionAnalysisBuilderLineOrientationType = ReflectionAnalysisBuilder.LineOrientationType


##  @link ReflectionAnalysisBuilderLineThicknessType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilderLineThicknessType @endlink is an alias for @link ReflectionAnalysisBuilder.LineThicknessType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.LineThicknessType@endlink
ReflectionAnalysisBuilderLineThicknessType = ReflectionAnalysisBuilder.LineThicknessType


##  @link ReflectionAnalysisBuilderNumberOfLinesOptions NXOpen.GeometricAnalysis.ReflectionAnalysisBuilderNumberOfLinesOptions @endlink is an alias for @link ReflectionAnalysisBuilder.NumberOfLinesOptions NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.NumberOfLinesOptions@endlink
ReflectionAnalysisBuilderNumberOfLinesOptions = ReflectionAnalysisBuilder.NumberOfLinesOptions


##  @link ReflectionAnalysisBuilderSceneImageType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilderSceneImageType @endlink is an alias for @link ReflectionAnalysisBuilder.SceneImageType NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.SceneImageType@endlink
ReflectionAnalysisBuilderSceneImageType = ReflectionAnalysisBuilder.SceneImageType


##  @link ReflectionAnalysisBuilderTypes NXOpen.GeometricAnalysis.ReflectionAnalysisBuilderTypes @endlink is an alias for @link ReflectionAnalysisBuilder.Types NXOpen.GeometricAnalysis.ReflectionAnalysisBuilder.Types@endlink
ReflectionAnalysisBuilderTypes = ReflectionAnalysisBuilder.Types


##  @link SimpleInterferenceFaceInterferenceMethod NXOpen.GeometricAnalysis.SimpleInterferenceFaceInterferenceMethod @endlink is an alias for @link SimpleInterference.FaceInterferenceMethod NXOpen.GeometricAnalysis.SimpleInterference.FaceInterferenceMethod@endlink
SimpleInterferenceFaceInterferenceMethod = SimpleInterference.FaceInterferenceMethod


##  @link SimpleInterferenceInterferenceMethod NXOpen.GeometricAnalysis.SimpleInterferenceInterferenceMethod @endlink is an alias for @link SimpleInterference.InterferenceMethod NXOpen.GeometricAnalysis.SimpleInterference.InterferenceMethod@endlink
SimpleInterferenceInterferenceMethod = SimpleInterference.InterferenceMethod


##  @link SimpleInterferenceResult NXOpen.GeometricAnalysis.SimpleInterferenceResult @endlink is an alias for @link SimpleInterference.Result NXOpen.GeometricAnalysis.SimpleInterference.Result@endlink
SimpleInterferenceResult = SimpleInterference.Result


##  @link SlopeAnalysisBuilder1DisplayModes NXOpen.GeometricAnalysis.SlopeAnalysisBuilder1DisplayModes @endlink is an alias for @link SlopeAnalysisBuilder1.DisplayModes NXOpen.GeometricAnalysis.SlopeAnalysisBuilder1.DisplayModes@endlink
SlopeAnalysisBuilder1DisplayModes = SlopeAnalysisBuilder1.DisplayModes


##  @link SlopeAnalysisBuilderDisplayModes NXOpen.GeometricAnalysis.SlopeAnalysisBuilderDisplayModes @endlink is an alias for @link SlopeAnalysisBuilder.DisplayModes NXOpen.GeometricAnalysis.SlopeAnalysisBuilder.DisplayModes@endlink
SlopeAnalysisBuilderDisplayModes = SlopeAnalysisBuilder.DisplayModes


##  @link SolidDensityUnitsType NXOpen.GeometricAnalysis.SolidDensityUnitsType @endlink is an alias for @link SolidDensity.UnitsType NXOpen.GeometricAnalysis.SolidDensity.UnitsType@endlink
SolidDensityUnitsType = SolidDensity.UnitsType


##  @link SurfaceAnalysisDisplayShowFlagType NXOpen.GeometricAnalysis.SurfaceAnalysisDisplayShowFlagType @endlink is an alias for @link SurfaceAnalysisDisplay.ShowFlagType NXOpen.GeometricAnalysis.SurfaceAnalysisDisplay.ShowFlagType@endlink
SurfaceAnalysisDisplayShowFlagType = SurfaceAnalysisDisplay.ShowFlagType


##  @link SurfaceContinuityAnalysisBuilderCurvatureType NXOpen.GeometricAnalysis.SurfaceContinuityAnalysisBuilderCurvatureType @endlink is an alias for @link SurfaceContinuityAnalysisBuilder.CurvatureType NXOpen.GeometricAnalysis.SurfaceContinuityAnalysisBuilder.CurvatureType@endlink
SurfaceContinuityAnalysisBuilderCurvatureType = SurfaceContinuityAnalysisBuilder.CurvatureType


##  @link SurfaceContinuityAnalysisBuilderReportingType NXOpen.GeometricAnalysis.SurfaceContinuityAnalysisBuilderReportingType @endlink is an alias for @link SurfaceContinuityAnalysisBuilder.ReportingType NXOpen.GeometricAnalysis.SurfaceContinuityAnalysisBuilder.ReportingType@endlink
SurfaceContinuityAnalysisBuilderReportingType = SurfaceContinuityAnalysisBuilder.ReportingType


##  @link SurfaceContinuityAnalysisBuilderTypes NXOpen.GeometricAnalysis.SurfaceContinuityAnalysisBuilderTypes @endlink is an alias for @link SurfaceContinuityAnalysisBuilder.Types NXOpen.GeometricAnalysis.SurfaceContinuityAnalysisBuilder.Types@endlink
SurfaceContinuityAnalysisBuilderTypes = SurfaceContinuityAnalysisBuilder.Types


##  @link SurfaceIntersectionBuilderCalculationTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilderCalculationTypes @endlink is an alias for @link SurfaceIntersectionBuilder.CalculationTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.CalculationTypes@endlink
SurfaceIntersectionBuilderCalculationTypes = SurfaceIntersectionBuilder.CalculationTypes


##  @link SurfaceIntersectionBuilderDirectionTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilderDirectionTypes @endlink is an alias for @link SurfaceIntersectionBuilder.DirectionTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.DirectionTypes@endlink
SurfaceIntersectionBuilderDirectionTypes = SurfaceIntersectionBuilder.DirectionTypes


##  @link SurfaceIntersectionBuilderLabelValues NXOpen.GeometricAnalysis.SurfaceIntersectionBuilderLabelValues @endlink is an alias for @link SurfaceIntersectionBuilder.LabelValues NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.LabelValues@endlink
SurfaceIntersectionBuilderLabelValues = SurfaceIntersectionBuilder.LabelValues


##  @link SurfaceIntersectionBuilderNormalTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilderNormalTypes @endlink is an alias for @link SurfaceIntersectionBuilder.NormalTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.NormalTypes@endlink
SurfaceIntersectionBuilderNormalTypes = SurfaceIntersectionBuilder.NormalTypes


##  @link SurfaceIntersectionBuilderProjectionTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilderProjectionTypes @endlink is an alias for @link SurfaceIntersectionBuilder.ProjectionTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.ProjectionTypes@endlink
SurfaceIntersectionBuilderProjectionTypes = SurfaceIntersectionBuilder.ProjectionTypes


##  @link SurfaceIntersectionBuilderScalingTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilderScalingTypes @endlink is an alias for @link SurfaceIntersectionBuilder.ScalingTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.ScalingTypes@endlink
SurfaceIntersectionBuilderScalingTypes = SurfaceIntersectionBuilder.ScalingTypes


##  @link SurfaceIntersectionBuilderXyzTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilderXyzTypes @endlink is an alias for @link SurfaceIntersectionBuilder.XyzTypes NXOpen.GeometricAnalysis.SurfaceIntersectionBuilder.XyzTypes@endlink
SurfaceIntersectionBuilderXyzTypes = SurfaceIntersectionBuilder.XyzTypes


