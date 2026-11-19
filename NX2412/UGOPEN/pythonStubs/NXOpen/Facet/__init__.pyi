from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class AdjustMinimumRadiusBuilder(NXOpen.Builder): 
    """
       Represents a NXOpen.Facet.AdjustMinimumRadiusBuilder.
       It smooths the input bodies such that their minimum radius of curvature is larger than the prescribed radius of curvature.
    """
    @property
    def Facets(self) -> NXOpen.FacetCollector:
        """
        Getter for property: ( NXOpen.FacetCollector) Facets
         Returns the input facets.  
           Inputs to this command can be convergent objects.   
         
        """
        pass
    @property
    def IsEditCopy(self) -> bool:
        """
        Getter for property: (bool) IsEditCopy
         Returns the flag indicating if the adjust minimum radius is on the copy of the input facet body.  
             
         
        """
        pass
    @IsEditCopy.setter
    def IsEditCopy(self, isEditCopy: bool):
        """
        Setter for property: (bool) IsEditCopy
         Returns the flag indicating if the adjust minimum radius is on the copy of the input facet body.  
             
         
        """
        pass
    @property
    def MinimumRadius(self) -> float:
        """
        Getter for property: (float) MinimumRadius
         Returns the minimum radius of curvature   
            
         
        """
        pass
    @MinimumRadius.setter
    def MinimumRadius(self, radius: float):
        """
        Setter for property: (float) MinimumRadius
         Returns the minimum radius of curvature   
            
         
        """
        pass
import NXOpen
class BestFitAlignBuilder(NXOpen.Builder): 
    """ This class performs the best fit alignment between objects """
    class ConstraintOptions(Enum):
        """
        Members Include: 
         |Free|  No constraint 
         |OnlyTranslation|  Only translation 
         |TranslationInPlane|  Translation in the plane 
         |TranslationAlongDirection|  Translation along direction 
         |OnlyRotation|  Only rotation 
         |RotationAroundPoint|  Rotation around specific point 
         |RotationAroundLine|  Rotation around specific line 
         |HoldToPlane|  Moving in the plane 
         |HoldToLine|  Moving along the line 

        """
        Free: int
        OnlyTranslation: int
        TranslationInPlane: int
        TranslationAlongDirection: int
        OnlyRotation: int
        RotationAroundPoint: int
        RotationAroundLine: int
        HoldToPlane: int
        HoldToLine: int
        @staticmethod
        def ValueOf(value: int) -> BestFitAlignBuilder.ConstraintOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DestinationObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) DestinationObjects
         Returns the destination objects   
            
         
        """
        pass
    @property
    def Direction(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) Direction
         Returns the plane or line direction   
            
         
        """
        pass
    @Direction.setter
    def Direction(self, direction: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) Direction
         Returns the plane or line direction   
            
         
        """
        pass
    @property
    def FitConstraints(self) -> BestFitAlignBuilder.ConstraintOptions:
        """
        Getter for property: ( BestFitAlignBuilder.ConstraintOptions NXOpe) FitConstraints
         Returns the fit constraint   
            
         
        """
        pass
    @FitConstraints.setter
    def FitConstraints(self, fitConstraints: BestFitAlignBuilder.ConstraintOptions):
        """
        Setter for property: ( BestFitAlignBuilder.ConstraintOptions NXOpe) FitConstraints
         Returns the fit constraint   
            
         
        """
        pass
    @property
    def GlobalSearch(self) -> bool:
        """
        Getter for property: (bool) GlobalSearch
         Returns a value indicating whether to do a global search   
            
         
        """
        pass
    @GlobalSearch.setter
    def GlobalSearch(self, globalSearch: bool):
        """
        Setter for property: (bool) GlobalSearch
         Returns a value indicating whether to do a global search   
            
         
        """
        pass
    @property
    def MobileObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) MobileObjects
         Returns the mobile objects   
            
         
        """
        pass
    @property
    def RotateCenter(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) RotateCenter
         Returns the rotation center   
            
         
        """
        pass
    @RotateCenter.setter
    def RotateCenter(self, rotateCenter: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) RotateCenter
         Returns the rotation center   
            
         
        """
        pass
    @property
    def SourceObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SourceObjects
         Returns the source objects   
            
         
        """
        pass
import NXOpen
class BridgeFacetBodyBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Facet.BridgeFacetBodyBuilder
    It bridges two disjoint NX facet bodies. User need to specify the range for each input facet body.
    It returns a new megered NX facet Body. The two input bodies can be kept, deleted or hidden.
    """
    class Input(Enum):
        """
        Members Include: 
         |Keep|  Keep the input facet body after builder committing 
         |Delete|  Delete the input facet body after builder committing 
         |Hide|  Hide the input facet body after builder committing 

        """
        Keep: int
        Delete: int
        Hide: int
        @staticmethod
        def ValueOf(value: int) -> BridgeFacetBodyBuilder.Input:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SmoothTypes(Enum):
        """
        Members Include: 
         |Linear|  Insert new facets with linear smoothness 
         |TangentBased|  Insert new facets with tangent smoothness 

        """
        Linear: int
        TangentBased: int
        @staticmethod
        def ValueOf(value: int) -> BridgeFacetBodyBuilder.SmoothTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance used in the bridge facet body feature   
            
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance used in the bridge facet body feature   
            
         
        """
        pass
    @property
    def FacetBodyOne(self) -> SelectFacetedBody:
        """
        Getter for property: ( SelectFacetedBody NXOpe) FacetBodyOne
         Returns the first NX facet body to be bridged   
            
         
        """
        pass
    @property
    def FacetBodyTwo(self) -> SelectFacetedBody:
        """
        Getter for property: ( SelectFacetedBody NXOpe) FacetBodyTwo
         Returns the second NX facet body to be bridged   
            
         
        """
        pass
    @property
    def InputStatus(self) -> BridgeFacetBodyBuilder.Input:
        """
        Getter for property: ( BridgeFacetBodyBuilder.Input NXOpe) InputStatus
         Returns the option to specify how to deal with the input two facet bodies: keep, delete or hide   
            
         
        """
        pass
    @InputStatus.setter
    def InputStatus(self, inputStatus: BridgeFacetBodyBuilder.Input):
        """
        Setter for property: ( BridgeFacetBodyBuilder.Input NXOpe) InputStatus
         Returns the option to specify how to deal with the input two facet bodies: keep, delete or hide   
            
         
        """
        pass
    @property
    def Smoothness(self) -> BridgeFacetBodyBuilder.SmoothTypes:
        """
        Getter for property: ( BridgeFacetBodyBuilder.SmoothTypes NXOpe) Smoothness
         Returns the inserted facet smooth type   
            
         
        """
        pass
    @Smoothness.setter
    def Smoothness(self, smoothType: BridgeFacetBodyBuilder.SmoothTypes):
        """
        Setter for property: ( BridgeFacetBodyBuilder.SmoothTypes NXOpe) Smoothness
         Returns the inserted facet smooth type   
            
         
        """
        pass
    @property
    def Vertex1Range1(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Vertex1Range1
         Returns the first vertex used to define the range on the the first facet body   
            
         
        """
        pass
    @Vertex1Range1.setter
    def Vertex1Range1(self, vertex1Range1: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Vertex1Range1
         Returns the first vertex used to define the range on the the first facet body   
            
         
        """
        pass
    @property
    def Vertex1Range2(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Vertex1Range2
         Returns the first vertex used to defind the range on the second facet body   
            
         
        """
        pass
    @Vertex1Range2.setter
    def Vertex1Range2(self, vertex1Range2: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Vertex1Range2
         Returns the first vertex used to defind the range on the second facet body   
            
         
        """
        pass
    @property
    def Vertex2Range1(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Vertex2Range1
         Returns the second vertex used to define the range on the first facet body   
            
         
        """
        pass
    @Vertex2Range1.setter
    def Vertex2Range1(self, vertex2Range1: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Vertex2Range1
         Returns the second vertex used to define the range on the first facet body   
            
         
        """
        pass
    @property
    def Vertex2Range2(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Vertex2Range2
         Returns the second vertex used to defind the range on the second facet body   
            
         
        """
        pass
    @Vertex2Range2.setter
    def Vertex2Range2(self, vertex2Range2: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Vertex2Range2
         Returns the second vertex used to defind the range on the second facet body   
            
         
        """
        pass
    def FlipRange1(self) -> None:
        """
         Flip the range between the first and second vertex on the first facet body 
        """
        pass
    def FlipRange2(self) -> None:
        """
         Flip the range between the first and second vertex on the second facet body 
        """
        pass
import NXOpen
class CleanupFacetBodyBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Facet.CleanupFacetBodyBuilder builder. 
    It removes defects that are present in the surfaces of the bodies selected. 
    """
    class CleanupOptions(Enum):
        """
        Members Include: 
         |NotSet|  Don't perform Analysis or Repair 
         |Analyze|  Perform Analysis 
         |Repair|  Perform Repair 

        """
        NotSet: int
        Analyze: int
        Repair: int
        @staticmethod
        def ValueOf(value: int) -> CleanupFacetBodyBuilder.CleanupOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OriginalBodyOptions(Enum):
        """
        Members Include: 
         |Keep|  Keep original body 
         |Hide|  Hide original body 
         |Delete|  Delete original body 

        """
        Keep: int
        Hide: int
        Delete: int
        @staticmethod
        def ValueOf(value: int) -> CleanupFacetBodyBuilder.OriginalBodyOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the tolerance value use to detect the faults in facet body and fix the same.  
          
                  
                This API is now deprecated.
                Please use  ToleranceFactor  and  DistanceTolerance  instead.
                  
                  
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, disTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the tolerance value use to detect the faults in facet body and fix the same.  
          
                  
                This API is now deprecated.
                Please use  ToleranceFactor  and  DistanceTolerance  instead.
                  
                  
         
        """
        pass
    @property
    def FoldedEdges(self) -> CleanupFacetBodyBuilder.CleanupOptions:
        """
        Getter for property: ( CleanupFacetBodyBuilder.CleanupOptions NXOpe) FoldedEdges
         Returns the option to identify or repair facets having an angle with adjacent facets less than a specified minimum value   
            
         
        """
        pass
    @FoldedEdges.setter
    def FoldedEdges(self, foldedEdges: CleanupFacetBodyBuilder.CleanupOptions):
        """
        Setter for property: ( CleanupFacetBodyBuilder.CleanupOptions NXOpe) FoldedEdges
         Returns the option to identify or repair facets having an angle with adjacent facets less than a specified minimum value   
            
         
        """
        pass
    @property
    def InconsistentNormals(self) -> CleanupFacetBodyBuilder.CleanupOptions:
        """
        Getter for property: ( CleanupFacetBodyBuilder.CleanupOptions NXOpe) InconsistentNormals
         Returns the option to identify or repair normals of neighboring facets or vertices that do not have the right orientation   
            
         
        """
        pass
    @InconsistentNormals.setter
    def InconsistentNormals(self, inconsistentNormals: CleanupFacetBodyBuilder.CleanupOptions):
        """
        Setter for property: ( CleanupFacetBodyBuilder.CleanupOptions NXOpe) InconsistentNormals
         Returns the option to identify or repair normals of neighboring facets or vertices that do not have the right orientation   
            
         
        """
        pass
    @property
    def InputBodies(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) InputBodies
         Returns the input facet bodies to be analyzed or repaired   
            
         
        """
        pass
    @property
    def LaminarSlits(self) -> CleanupFacetBodyBuilder.CleanupOptions:
        """
        Getter for property: ( CleanupFacetBodyBuilder.CleanupOptions NXOpe) LaminarSlits
         Returns the option to identify or repair thin holes or slits in the mesh caused by facets not being aligned   
            
         
        """
        pass
    @LaminarSlits.setter
    def LaminarSlits(self, laminarSlits: CleanupFacetBodyBuilder.CleanupOptions):
        """
        Setter for property: ( CleanupFacetBodyBuilder.CleanupOptions NXOpe) LaminarSlits
         Returns the option to identify or repair thin holes or slits in the mesh caused by facets not being aligned   
            
         
        """
        pass
    @property
    def LongFacets(self) -> CleanupFacetBodyBuilder.CleanupOptions:
        """
        Getter for property: ( CleanupFacetBodyBuilder.CleanupOptions NXOpe) LongFacets
         Returns the option to identify or repair facets with a ratio of longest to shortest side exceeding a specified value   
            
         
        """
        pass
    @LongFacets.setter
    def LongFacets(self, longFacets: CleanupFacetBodyBuilder.CleanupOptions):
        """
        Setter for property: ( CleanupFacetBodyBuilder.CleanupOptions NXOpe) LongFacets
         Returns the option to identify or repair facets with a ratio of longest to shortest side exceeding a specified value   
            
         
        """
        pass
    @property
    def MaxRatioLongFacets(self) -> float:
        """
        Getter for property: (float) MaxRatioLongFacets
         Returns the specified value used to define long facets   
            
         
        """
        pass
    @MaxRatioLongFacets.setter
    def MaxRatioLongFacets(self, maxRatioLongFacets: float):
        """
        Setter for property: (float) MaxRatioLongFacets
         Returns the specified value used to define long facets   
            
         
        """
        pass
    @property
    def MinAngleFoldedFacets(self) -> float:
        """
        Getter for property: (float) MinAngleFoldedFacets
         Returns the minimum angle between adjacent facets to define folded facets   
            
         
        """
        pass
    @MinAngleFoldedFacets.setter
    def MinAngleFoldedFacets(self, minAngleFoldedFacets: float):
        """
        Setter for property: (float) MinAngleFoldedFacets
         Returns the minimum angle between adjacent facets to define folded facets   
            
         
        """
        pass
    @property
    def MinFacetNumberPerBody(self) -> int:
        """
        Getter for property: (int) MinFacetNumberPerBody
         Returns the minimum number of facets per mesh   
            
         
        """
        pass
    @MinFacetNumberPerBody.setter
    def MinFacetNumberPerBody(self, minFacetNumber: int):
        """
        Setter for property: (int) MinFacetNumberPerBody
         Returns the minimum number of facets per mesh   
            
         
        """
        pass
    @property
    def OriginalBodyOption(self) -> CleanupFacetBodyBuilder.OriginalBodyOptions:
        """
        Getter for property: ( CleanupFacetBodyBuilder.OriginalBodyOptions NXOpe) OriginalBodyOption
         Returns the option for handling the input facet bodies   
            
         
        """
        pass
    @OriginalBodyOption.setter
    def OriginalBodyOption(self, enumOriginalBodyOption: CleanupFacetBodyBuilder.OriginalBodyOptions):
        """
        Setter for property: ( CleanupFacetBodyBuilder.OriginalBodyOptions NXOpe) OriginalBodyOption
         Returns the option for handling the input facet bodies   
            
         
        """
        pass
    @property
    def SelfIntersections(self) -> CleanupFacetBodyBuilder.CleanupOptions:
        """
        Getter for property: ( CleanupFacetBodyBuilder.CleanupOptions NXOpe) SelfIntersections
         Returns the option to identify or repair facets of the same mesh intersecting each other   
            
         
        """
        pass
    @SelfIntersections.setter
    def SelfIntersections(self, selfIntersections: CleanupFacetBodyBuilder.CleanupOptions):
        """
        Setter for property: ( CleanupFacetBodyBuilder.CleanupOptions NXOpe) SelfIntersections
         Returns the option to identify or repair facets of the same mesh intersecting each other   
            
         
        """
        pass
    @property
    def ShowInfo(self) -> bool:
        """
        Getter for property: (bool) ShowInfo
         Returns 
                the option to display numbers of various type of defects identified or repaired in the   NXOpen::ListingWindow  .  
          
                If this option is true, but the program is running externally without UI, display would go to
                a standard output devicethe.  The listing window output can be sent to the Information window or to a 
                file, or to both. See   NXOpen::ListingWindow::SelectDevice  
                for more information.
                  
         
        """
        pass
    @ShowInfo.setter
    def ShowInfo(self, showInfo: bool):
        """
        Setter for property: (bool) ShowInfo
         Returns 
                the option to display numbers of various type of defects identified or repaired in the   NXOpen::ListingWindow  .  
          
                If this option is true, but the program is running externally without UI, display would go to
                a standard output devicethe.  The listing window output can be sent to the Information window or to a 
                file, or to both. See   NXOpen::ListingWindow::SelectDevice  
                for more information.
                  
         
        """
        pass
    @property
    def ThinFacets(self) -> CleanupFacetBodyBuilder.CleanupOptions:
        """
        Getter for property: ( CleanupFacetBodyBuilder.CleanupOptions NXOpe) ThinFacets
         Returns the option to identify or repair facets with with one long edge and two edges with more or the less the same length and a ratio of length to width exceeding a specified value   
            
         
        """
        pass
    @ThinFacets.setter
    def ThinFacets(self, thinFacets: CleanupFacetBodyBuilder.CleanupOptions):
        """
        Setter for property: ( CleanupFacetBodyBuilder.CleanupOptions NXOpe) ThinFacets
         Returns the option to identify or repair facets with with one long edge and two edges with more or the less the same length and a ratio of length to width exceeding a specified value   
            
         
        """
        pass
    @property
    def ToleranceFactor(self) -> float:
        """
        Getter for property: (float) ToleranceFactor
         Returns the tolerance factor use to detect the faults in facet body and fix the same   
            
         
        """
        pass
    @ToleranceFactor.setter
    def ToleranceFactor(self, tolFactor: float):
        """
        Setter for property: (float) ToleranceFactor
         Returns the tolerance factor use to detect the faults in facet body and fix the same   
            
         
        """
        pass
    def DisplayCleanupReportInListWindow(self) -> None:
        """
         
                Displays the  NXOpen.ListingWindow  with numbers of various type of defects identified or repaired.
                If we call this method externally without UI, it displays 
                the information on standard output device. The listing 
                window output can be sent to the Information window or to a 
                file, or to both. See  NXOpen.ListingWindow.SelectDevice 
                for more information.
                
        """
        pass
    def SetAllOptionsToAnalyze(self) -> None:
        """
         Sets all cleanup options to Facet.CleanupFacetBodyBuilder.CleanupOptions.Analyze, which means to identify the defects only for the input bodies 
        """
        pass
    def SetAllOptionsToNone(self) -> None:
        """
         Sets all cleanup options to Facet.CleanupFacetBodyBuilder.CleanupOptions.None, which means to do nothing 
        """
        pass
    def SetAllOptionsToRepair(self) -> None:
        """
         Sets all cleanup options to Facet.CleanupFacetBodyBuilder.CleanupOptions.Repair, which means to identify as well as repair the defects for the input bodies 
        """
        pass
import NXOpen
class CleanupFacetBodyWizardBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Facet.CleanupFacetBodyWizardBuilder builder. 
    It removes defects that are present in the surfaces of the bodies selected. 
    """
    class FillType(Enum):
        """
        Members Include: 
         |NotSet| 
         |Linear| 
         |Refined| 
         |TangentBased| 
         |CurvatureBased| 

        """
        NotSet: int
        Linear: int
        Refined: int
        TangentBased: int
        CurvatureBased: int
        @staticmethod
        def ValueOf(value: int) -> CleanupFacetBodyWizardBuilder.FillType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class JaCleanupFacetBodyBuilderRegionremoveoption(Enum):
        """
        Members Include: 
         |ByRegion| 
         |ByDefectMarkup| 

        """
        ByRegion: int
        ByDefectMarkup: int
        @staticmethod
        def ValueOf(value: int) -> CleanupFacetBodyWizardBuilder.JaCleanupFacetBodyBuilderRegionremoveoption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AutomaticFillType(self) -> CleanupFacetBodyWizardBuilder.FillType:
        """
        Getter for property: ( CleanupFacetBodyWizardBuilder.FillType NXOpe) AutomaticFillType
         Returns the automatic fill type   
            
         
        """
        pass
    @AutomaticFillType.setter
    def AutomaticFillType(self, automaticFillType: CleanupFacetBodyWizardBuilder.FillType):
        """
        Setter for property: ( CleanupFacetBodyWizardBuilder.FillType NXOpe) AutomaticFillType
         Returns the automatic fill type   
            
         
        """
        pass
    @property
    def CircumferenceRings(self) -> int:
        """
        Getter for property: (int) CircumferenceRings
         Returns the circumference rings   
            
         
        """
        pass
    @CircumferenceRings.setter
    def CircumferenceRings(self, circumferenceRings: int):
        """
        Setter for property: (int) CircumferenceRings
         Returns the circumference rings   
            
         
        """
        pass
    @property
    def CleanupFacetBodyBuilder(self) -> CleanupFacetBodyBuilder:
        """
        Getter for property: ( CleanupFacetBodyBuilder NXOpe) CleanupFacetBodyBuilder
         Returns the cleanup Facet   
            
         
        """
        pass
    @property
    def FacetCollector(self) -> NXOpen.FacetCollector:
        """
        Getter for property: ( NXOpen.FacetCollector) FacetCollector
         Returns the collector of facets to be remove.  
            
         
        """
        pass
    @FacetCollector.setter
    def FacetCollector(self, collector: NXOpen.FacetCollector):
        """
        Setter for property: ( NXOpen.FacetCollector) FacetCollector
         Returns the collector of facets to be remove.  
            
         
        """
        pass
    @property
    def FillMesh(self) -> FillMeshBuilder:
        """
        Getter for property: ( FillMeshBuilder NXOpe) FillMesh
         Returns the Fill Mesh   
            
         
        """
        pass
    @property
    def FoldedEdges(self) -> bool:
        """
        Getter for property: (bool) FoldedEdges
         Returns the folded edges   
            
         
        """
        pass
    @FoldedEdges.setter
    def FoldedEdges(self, foldedEdges: bool):
        """
        Setter for property: (bool) FoldedEdges
         Returns the folded edges   
            
         
        """
        pass
    @property
    def InconsistentNormals(self) -> bool:
        """
        Getter for property: (bool) InconsistentNormals
         Returns the inconsistent normals   
            
         
        """
        pass
    @InconsistentNormals.setter
    def InconsistentNormals(self, inconsistentNormals: bool):
        """
        Setter for property: (bool) InconsistentNormals
         Returns the inconsistent normals   
            
         
        """
        pass
    @property
    def InputBodies(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) InputBodies
         Returns the input bodies.  
           For convergent bodies having associative feature can not be edited. Use CreateCopiesToEdit API to create copies   
         
        """
        pass
    @property
    def LaminarSlits(self) -> bool:
        """
        Getter for property: (bool) LaminarSlits
         Returns the laminar slits   
            
         
        """
        pass
    @LaminarSlits.setter
    def LaminarSlits(self, laminarSlits: bool):
        """
        Setter for property: (bool) LaminarSlits
         Returns the laminar slits   
            
         
        """
        pass
    @property
    def MinAngleFoldedFacets(self) -> float:
        """
        Getter for property: (float) MinAngleFoldedFacets
         Returns the min angle folded facets   
            
         
        """
        pass
    @MinAngleFoldedFacets.setter
    def MinAngleFoldedFacets(self, minAngleFoldedFacets: float):
        """
        Setter for property: (float) MinAngleFoldedFacets
         Returns the min angle folded facets   
            
         
        """
        pass
    @property
    def MinFacetNumberPerBody(self) -> int:
        """
        Getter for property: (int) MinFacetNumberPerBody
         Returns the min facet number per body   
            
         
        """
        pass
    @MinFacetNumberPerBody.setter
    def MinFacetNumberPerBody(self, minFacetNumberPerBody: int):
        """
        Setter for property: (int) MinFacetNumberPerBody
         Returns the min facet number per body   
            
         
        """
        pass
    @property
    def QualityIndex(self) -> bool:
        """
        Getter for property: (bool) QualityIndex
         Returns the quality index   
            
         
        """
        pass
    @QualityIndex.setter
    def QualityIndex(self, qualityIndex: bool):
        """
        Setter for property: (bool) QualityIndex
         Returns the quality index   
            
         
        """
        pass
    @property
    def RegionRemoveOption(self) -> CleanupFacetBodyWizardBuilder.JaCleanupFacetBodyBuilderRegionremoveoption:
        """
        Getter for property: ( CleanupFacetBodyWizardBuilder.JaCleanupFacetBodyBuilderRegionremoveoption NXOpe) RegionRemoveOption
         Returns the region remove option   
            
         
        """
        pass
    @RegionRemoveOption.setter
    def RegionRemoveOption(self, regionRemoveOption: CleanupFacetBodyWizardBuilder.JaCleanupFacetBodyBuilderRegionremoveoption):
        """
        Setter for property: ( CleanupFacetBodyWizardBuilder.JaCleanupFacetBodyBuilderRegionremoveoption NXOpe) RegionRemoveOption
         Returns the region remove option   
            
         
        """
        pass
    @property
    def SelfIntersections(self) -> bool:
        """
        Getter for property: (bool) SelfIntersections
         Returns the self intersections   
            
         
        """
        pass
    @SelfIntersections.setter
    def SelfIntersections(self, selfIntersections: bool):
        """
        Setter for property: (bool) SelfIntersections
         Returns the self intersections   
            
         
        """
        pass
    @property
    def SnipFacetBodyBuilder(self) -> SnipFacetBodyBuilder:
        """
        Getter for property: ( SnipFacetBodyBuilder NXOpe) SnipFacetBodyBuilder
         Returns the snip Facet  
            
         
        """
        pass
    @property
    def ThinFacets(self) -> bool:
        """
        Getter for property: (bool) ThinFacets
         Returns the thin facets   
            
         
        """
        pass
    @ThinFacets.setter
    def ThinFacets(self, thinFacets: bool):
        """
        Setter for property: (bool) ThinFacets
         Returns the thin facets   
            
         
        """
        pass
    @property
    def ToleranceFactor(self) -> float:
        """
        Getter for property: (float) ToleranceFactor
         Returns the tolerance factor   
            
         
        """
        pass
    @ToleranceFactor.setter
    def ToleranceFactor(self, toleranceFactor: float):
        """
        Setter for property: (float) ToleranceFactor
         Returns the tolerance factor   
            
         
        """
        pass
    def Analyze(self) -> None:
        """
         The analyze 
        """
        pass
    def CreateCopiesToEdit(self) -> None:
        """
         Create copies of Associative convergent bodies. Return 1 if copies created 
        """
        pass
    def FillHole(self) -> None:
        """
         The Fill hole button 
        """
        pass
    def RemoveFacets(self) -> None:
        """
         Remove facet 
        """
        pass
    def Repair(self) -> None:
        """
         The repair 
        """
        pass
import NXOpen
class CombineFacetBodiesBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Facet.CombineFacetBodiesBuilder
        Merges multiple convergent bodies by averaging the meshes in the overlapping zones. """
    class InputBodiesOption(Enum):
        """
        Members Include: 
         |Delete| 
         |Keep| 
         |Hide| 

        """
        Delete: int
        Keep: int
        Hide: int
        @staticmethod
        def ValueOf(value: int) -> CombineFacetBodiesBuilder.InputBodiesOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AnalyzeMeshQuality(self) -> bool:
        """
        Getter for property: (bool) AnalyzeMeshQuality
         Returns the value used to determine if analyzing the quality of the mesh or not.  
             
         
        """
        pass
    @AnalyzeMeshQuality.setter
    def AnalyzeMeshQuality(self, analyzeMeshQuality: bool):
        """
        Setter for property: (bool) AnalyzeMeshQuality
         Returns the value used to determine if analyzing the quality of the mesh or not.  
             
         
        """
        pass
    @property
    def AverageFacetSize(self) -> float:
        """
        Getter for property: (float) AverageFacetSize
         Returns the parameter used to control the average size of the output triangulation.  
          
                    The value is also used as a threshold to determine overlapping of the two bodies.   
         
        """
        pass
    @AverageFacetSize.setter
    def AverageFacetSize(self, averageFacetSize: float):
        """
        Setter for property: (float) AverageFacetSize
         Returns the parameter used to control the average size of the output triangulation.  
          
                    The value is also used as a threshold to determine overlapping of the two bodies.   
         
        """
        pass
    @property
    def InputBodiesOptions(self) -> CombineFacetBodiesBuilder.InputBodiesOption:
        """
        Getter for property: ( CombineFacetBodiesBuilder.InputBodiesOption NXOpe) InputBodiesOptions
         Returns the option indicating action to be taken for input bodies after combine operation is performed.  
          
                the builder is committed.  
         
        """
        pass
    @InputBodiesOptions.setter
    def InputBodiesOptions(self, inputBodiesOptions: CombineFacetBodiesBuilder.InputBodiesOption):
        """
        Setter for property: ( CombineFacetBodiesBuilder.InputBodiesOption NXOpe) InputBodiesOptions
         Returns the option indicating action to be taken for input bodies after combine operation is performed.  
          
                the builder is committed.  
         
        """
        pass
    @property
    def InputFacetBodies(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) InputFacetBodies
         Returns the input facet bodies.  
             
         
        """
        pass
import NXOpen
class CombineFacetBodyBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Facet.CombineFacetBodyBuilder builder. 
    It combines the facet bodies to one facet body. The original inputs are deleted.
    """
    @property
    def FacetedBodiesToCombine(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) FacetedBodiesToCombine
         Returns the faceted bodies to combine   
            
         
        """
        pass
import NXOpen
class ConvertFacetBodyBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Facet.ConvertFacetBodyBuilder builder. 
    It converts the selected NX facet bodies to Convergent bodies or JT bodies, and converts JT facet bodies 
    to Convergent bodies or NX facets bodies. The original inputs can be deleted, kept, or hidden.
    """
    class OriginalBodyOptions(Enum):
        """
        Members Include: 
         |Keep|  Keep original body 
         |Hide|  Hide original body 
         |Delete|  Delete original body 

        """
        Keep: int
        Hide: int
        Delete: int
        @staticmethod
        def ValueOf(value: int) -> ConvertFacetBodyBuilder.OriginalBodyOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OutputTypes(Enum):
        """
        Members Include: 
         |ConvergentBody|  Convert To Convergent bodies 
         |NXFacetBody|  Convert to NX Facet bodies 
         |JTFacetBody|  Convert To JT Facet bodies 

        """
        ConvergentBody: int
        NXFacetBody: int
        JTFacetBody: int
        @staticmethod
        def ValueOf(value: int) -> ConvertFacetBodyBuilder.OutputTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CleanUp(self) -> bool:
        """
        Getter for property: (bool) CleanUp
         Returns an option for automatically repairing the converted PSM mesh   
            
         
        """
        pass
    @CleanUp.setter
    def CleanUp(self, cleanUp: bool):
        """
        Setter for property: (bool) CleanUp
         Returns an option for automatically repairing the converted PSM mesh   
            
         
        """
        pass
    @property
    def FacetedBodiesToConvert(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) FacetedBodiesToConvert
         Returns the input facet bodies to convert   
            
         
        """
        pass
    @property
    def MinimumAngleFoldedFacets(self) -> float:
        """
        Getter for property: (float) MinimumAngleFoldedFacets
         Returns the minimum angle between adjacent facets to define folded facets.  
             
         
        """
        pass
    @MinimumAngleFoldedFacets.setter
    def MinimumAngleFoldedFacets(self, minimumAngleFoldedFacets: float):
        """
        Setter for property: (float) MinimumAngleFoldedFacets
         Returns the minimum angle between adjacent facets to define folded facets.  
             
         
        """
        pass
    @property
    def MinimumFacetNumber(self) -> int:
        """
        Getter for property: (int) MinimumFacetNumber
         Returns the minimum number of facets to create output body.  
             
         
        """
        pass
    @MinimumFacetNumber.setter
    def MinimumFacetNumber(self, minimumFacetNumber: int):
        """
        Setter for property: (int) MinimumFacetNumber
         Returns the minimum number of facets to create output body.  
             
         
        """
        pass
    @property
    def OriginalBodyOption(self) -> ConvertFacetBodyBuilder.OriginalBodyOptions:
        """
        Getter for property: ( ConvertFacetBodyBuilder.OriginalBodyOptions NXOpe) OriginalBodyOption
         Returns the option for handling the input facet bodies   
            
         
        """
        pass
    @OriginalBodyOption.setter
    def OriginalBodyOption(self, enumOriginalBodyOption: ConvertFacetBodyBuilder.OriginalBodyOptions):
        """
        Setter for property: ( ConvertFacetBodyBuilder.OriginalBodyOptions NXOpe) OriginalBodyOption
         Returns the option for handling the input facet bodies   
            
         
        """
        pass
    @property
    def OutputType(self) -> ConvertFacetBodyBuilder.OutputTypes:
        """
        Getter for property: ( ConvertFacetBodyBuilder.OutputTypes NXOpe) OutputType
         Returns the output type of converted facet body   
            
         
        """
        pass
    @OutputType.setter
    def OutputType(self, enumOutputType: ConvertFacetBodyBuilder.OutputTypes):
        """
        Setter for property: ( ConvertFacetBodyBuilder.OutputTypes NXOpe) OutputType
         Returns the output type of converted facet body   
            
         
        """
        pass
import NXOpen
import NXOpen.Features
class CreateTransitionBuilder(NXOpen.Builder): 
    """
       Represents a NXOpen.Facet.CreateTransitionBuilder builder. 
       This class creates the blendchamfer of a facet body.
    """
    class Types(Enum):
        """
        Members Include: 
         |Round| 
         |Flat| 

        """
        Round: int
        Flat: int
        @staticmethod
        def ValueOf(value: int) -> CreateTransitionBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Distance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Distance
         Returns the distance.  
           This value is for chamfer operation.   
         
        """
        pass
    @property
    def IsClosed(self) -> bool:
        """
        Getter for property: (bool) IsClosed
         Returns the is closed.  
           The flag indicate if the edge is closed or not.   
         
        """
        pass
    @IsClosed.setter
    def IsClosed(self, isClosed: bool):
        """
        Setter for property: (bool) IsClosed
         Returns the is closed.  
           The flag indicate if the edge is closed or not.   
         
        """
        pass
    @property
    def IsEditCopy(self) -> bool:
        """
        Getter for property: (bool) IsEditCopy
         Returns the flag indicating if the transition is created on the copy of the input facet body.  
             
         
        """
        pass
    @IsEditCopy.setter
    def IsEditCopy(self, isEditCopy: bool):
        """
        Setter for property: (bool) IsEditCopy
         Returns the flag indicating if the transition is created on the copy of the input facet body.  
             
         
        """
        pass
    @property
    def Radius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Radius
         Returns the radius.  
           This value is for blend operation.   
         
        """
        pass
    @property
    def SelectedBody(self) -> NXOpen.DisplayableObject:
        """
        Getter for property: ( NXOpen.DisplayableObject) SelectedBody
         Returns the selected facet body.  
           It could be a convergent object.   
         
        """
        pass
    @SelectedBody.setter
    def SelectedBody(self, selectedBody: NXOpen.DisplayableObject):
        """
        Setter for property: ( NXOpen.DisplayableObject) SelectedBody
         Returns the selected facet body.  
           It could be a convergent object.   
         
        """
        pass
    @property
    def SelectedPoints(self) -> NXOpen.Features.GeometricConstraintDataManager:
        """
        Getter for property: ( NXOpen.Features.GeometricConstraintDataManager) SelectedPoints
         Returns the selected points.  
           The points will define the edge which needs blendchamfer.   
         
        """
        pass
    @property
    def Type(self) -> CreateTransitionBuilder.Types:
        """
        Getter for property: ( CreateTransitionBuilder.Types NXOpe) Type
         Returns the type.  
           This value defines the transition type.   
         
        """
        pass
    @Type.setter
    def Type(self, type: CreateTransitionBuilder.Types):
        """
        Setter for property: ( CreateTransitionBuilder.Types NXOpe) Type
         Returns the type.  
           This value defines the transition type.   
         
        """
        pass
import NXOpen
class CurvatureBuilder(NXOpen.Builder): 
    """
       Represents a NXOpen.Facet.CurvatureBuilder.
       It calculates the maximum absolute principal curvature on facet
       bodies and creates a color map of these values.
    """
    @property
    def Bodies(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) Bodies
         Returns the input facet body list.  
           Inputs to this command can be convergent objects.   
         
        """
        pass
    @property
    def ConcaveRadius(self) -> float:
        """
        Getter for property: (float) ConcaveRadius
         Returns the concave radius threshold   
            
         
        """
        pass
    @ConcaveRadius.setter
    def ConcaveRadius(self, concave_radius: float):
        """
        Setter for property: (float) ConcaveRadius
         Returns the concave radius threshold   
            
         
        """
        pass
    @property
    def ConvexRadius(self) -> float:
        """
        Getter for property: (float) ConvexRadius
         Returns the convex radius threshold   
            
         
        """
        pass
    @ConvexRadius.setter
    def ConvexRadius(self, convex_radius: float):
        """
        Setter for property: (float) ConvexRadius
         Returns the convex radius threshold   
            
         
        """
        pass
    @property
    def FacetBodies(self) -> SelectFacetedBodyList:
        """
        Getter for property: ( SelectFacetedBodyList NXOpe) FacetBodies
         Returns the input facet body list   
            
         
        """
        pass
    @property
    def IsDirectionReversed(self) -> bool:
        """
        Getter for property: (bool) IsDirectionReversed
         Returns the reverse direction option   
            
         
        """
        pass
    @IsDirectionReversed.setter
    def IsDirectionReversed(self, direction_reversed: bool):
        """
        Setter for property: (bool) IsDirectionReversed
         Returns the reverse direction option   
            
         
        """
        pass
    @property
    def SmoothingFactor(self) -> float:
        """
        Getter for property: (float) SmoothingFactor
         Returns the smoothing factor   
            
         
        """
        pass
    @SmoothingFactor.setter
    def SmoothingFactor(self, smoothing_factor: float):
        """
        Setter for property: (float) SmoothingFactor
         Returns the smoothing factor   
            
         
        """
        pass
    def DeleteCurvature(self) -> None:
        """
         Deletes the curvature data associated with the input facet bodies.
                    Call this method in order to save memory if the curvature data are not needed any more.
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class DecimateFacetBodyBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Facet.DecimateFacetBodyBuilder.
    Decimate Body Builder is a function to facilitate the reduction of data by reducing the density of facets while keeping the general shape in tact.
    Three different methods are provided to reduce the data. """
    class DecimateMethodType(Enum):
        """
        Members Include: 
         |ChordalDeviation|  Chordal deviation reduces the number of facets by removing facets which do not effect the overall accuracy of the mesh.
         |SmallestFacet|  Smallest facet removes all facets smaller than the defined area, thus removing facets deemed to be redundant by the designer.
         |Percentage|  Percentage option allows the user to reduce the facet count by overall percentage.

        """
        ChordalDeviation: int
        SmallestFacet: int
        Percentage: int
        @staticmethod
        def ValueOf(value: int) -> DecimateFacetBodyBuilder.DecimateMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngleThreshold(self) -> float:
        """
        Getter for property: (float) AngleThreshold
         Returns the value indicating maximum angle, where any facets with a larger relative angle are not reduced.  
          
                    This allows sharp edges to be retained.   
         
        """
        pass
    @AngleThreshold.setter
    def AngleThreshold(self, angleThreshold: float):
        """
        Setter for property: (float) AngleThreshold
         Returns the value indicating maximum angle, where any facets with a larger relative angle are not reduced.  
          
                    This allows sharp edges to be retained.   
         
        """
        pass
    @property
    def Bodies(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) Bodies
         Returns the facet bodies to be decimated.  
           Inputs to this command can be convergent objects.  
         
        """
        pass
    @property
    def DecimateMethod(self) -> DecimateFacetBodyBuilder.DecimateMethodType:
        """
        Getter for property: ( DecimateFacetBodyBuilder.DecimateMethodType NXOpe) DecimateMethod
         Returns the decimation method   
            
         
        """
        pass
    @DecimateMethod.setter
    def DecimateMethod(self, decimateMethod: DecimateFacetBodyBuilder.DecimateMethodType):
        """
        Setter for property: ( DecimateFacetBodyBuilder.DecimateMethodType NXOpe) DecimateMethod
         Returns the decimation method   
            
         
        """
        pass
    @property
    def FacetBodies(self) -> SelectFacetedBodyList:
        """
        Getter for property: ( SelectFacetedBodyList NXOpe) FacetBodies
         Returns the facet bodies to be decimated   
            
         
        """
        pass
    @property
    def FacetCollector(self) -> NXOpen.FacetCollector:
        """
        Getter for property: ( NXOpen.FacetCollector) FacetCollector
         Returns a collector of facets on the facet bodies to be decimated.  
            
         
        """
        pass
    @FacetCollector.setter
    def FacetCollector(self, collector: NXOpen.FacetCollector):
        """
        Setter for property: ( NXOpen.FacetCollector) FacetCollector
         Returns a collector of facets on the facet bodies to be decimated.  
            
         
        """
        pass
    @property
    def IsEditCopy(self) -> bool:
        """
        Getter for property: (bool) IsEditCopy
         Returns the value indicating if a copy of the facet body to be decimated without altering the original   
            
         
        """
        pass
    @IsEditCopy.setter
    def IsEditCopy(self, isEditCopy: bool):
        """
        Setter for property: (bool) IsEditCopy
         Returns the value indicating if a copy of the facet body to be decimated without altering the original   
            
         
        """
        pass
    @property
    def IsLockBoundary(self) -> bool:
        """
        Getter for property: (bool) IsLockBoundary
         Returns the value indicating if the open edges of inner and outer loops in the facet bodies are to be kept intact   
            
         
        """
        pass
    @IsLockBoundary.setter
    def IsLockBoundary(self, isLockBoundary: bool):
        """
        Setter for property: (bool) IsLockBoundary
         Returns the value indicating if the open edges of inner and outer loops in the facet bodies are to be kept intact   
            
         
        """
        pass
    @property
    def MinimumArea(self) -> float:
        """
        Getter for property: (float) MinimumArea
         Returns the value indicating area of the smallest facet that is to be retained.  
           All the facets
                    smaller than the minimum area are removed. This value is used when
                     NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodType  is
                     NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodTypeSmallestFacet .   
         
        """
        pass
    @MinimumArea.setter
    def MinimumArea(self, minimumArea: float):
        """
        Setter for property: (float) MinimumArea
         Returns the value indicating area of the smallest facet that is to be retained.  
           All the facets
                    smaller than the minimum area are removed. This value is used when
                     NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodType  is
                     NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodTypeSmallestFacet .   
         
        """
        pass
    @property
    def Percentage(self) -> float:
        """
        Getter for property: (float) Percentage
         Returns the value indicating percentage by which facet count is to be reduced.  
           This value is used when
                     NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodType  is
                     NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodTypePercentage .   
         
        """
        pass
    @Percentage.setter
    def Percentage(self, percentage: float):
        """
        Setter for property: (float) Percentage
         Returns the value indicating percentage by which facet count is to be reduced.  
           This value is used when
                     NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodType  is
                     NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodTypePercentage .   
         
        """
        pass
    @property
    def RegionList(self) -> NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList:
        """
        Getter for property: ( NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList) RegionList
         Returns an optional list of regions on the facet bodies to be decimated.  
             
         
        """
        pass
    @property
    def Tolerance(self) -> float:
        """
        Getter for property: (float) Tolerance
         Returns the value indicating maximum chordal deviation from the original facet body.  
           The value is used
                    when  NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodType  is
                     NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodTypeChordalDeviation .   
         
        """
        pass
    @Tolerance.setter
    def Tolerance(self, tolerance: float):
        """
        Setter for property: (float) Tolerance
         Returns the value indicating maximum chordal deviation from the original facet body.  
           The value is used
                    when  NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodType  is
                     NXOpen::Facet::DecimateFacetBodyBuilder::DecimateMethodTypeChordalDeviation .   
         
        """
        pass
import NXOpen
class DetectPrimitivesBuilder(NXOpen.Builder): 
    """
       This class manages the primitive shape detection for a facet body.
    """
    @property
    def BlendFactor(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BlendFactor
         Returns the blend factor   
            
         
        """
        pass
    @property
    def CurvatureSensitivity(self) -> int:
        """
        Getter for property: (int) CurvatureSensitivity
         Returns the curvature sensitivity   
            
         
        """
        pass
    @CurvatureSensitivity.setter
    def CurvatureSensitivity(self, curvatureSensitivity: int):
        """
        Setter for property: (int) CurvatureSensitivity
         Returns the curvature sensitivity   
            
         
        """
        pass
    @property
    def FacetSelection(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) FacetSelection
         Returns the facet selection.  
           Inputs to this command can be convergent objects.  
         
        """
        pass
    def AdjustShapeBoundary(self) -> None:
        """
         Adjust shape detection result with selectivity angle 
        """
        pass
    def GetBlendColor(self) -> List[float]:
        """
         Returns the blend color 
         Returns blendColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def GetConeColor(self) -> List[float]:
        """
         Returns the cone color 
         Returns coneColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def GetCylinderColor(self) -> List[float]:
        """
         Returns the cylinder color 
         Returns cylinderColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def GetOtherColor(self) -> List[float]:
        """
         Returns Other type of color. All non-primitive shapes are classfied as Other type 
         Returns otherColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def GetPlaneColor(self) -> List[float]:
        """
         Returns the plane color 
         Returns planeColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def GetSphereColor(self) -> List[float]:
        """
         Returns the sphere color 
         Returns sphereColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def SetBlendColor(self, blendColor: List[float]) -> None:
        """
         Sets the blend color 
        """
        pass
    def SetConeColor(self, coneColor: List[float]) -> None:
        """
         Sets the cone color 
        """
        pass
    def SetCylinderColor(self, cylinderColor: List[float]) -> None:
        """
         Sets the cylinder color 
        """
        pass
    def SetOtherColor(self, otherColor: List[float]) -> None:
        """
         Sets the other color 
        """
        pass
    def SetPlaneColor(self, planeColor: List[float]) -> None:
        """
         Sets the plane color 
        """
        pass
    def SetSphereColor(self, sphereColor: List[float]) -> None:
        """
         Sets the sphere color 
        """
        pass
import NXOpen
class DivideFacetFaceBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Facet.DivideFacetFaceBuilder.
    Divide Facet Face Builder is a function to facilitate dividing of selected facet out of original facet face. """
    class DivideFacetTypes(Enum):
        """
        Members Include: 
         |ByColor|  Divide Facet face based on colored facets 
         |ByRegion|  Divide Facet face based on selected regional facets 
         |ByCurves|  Divide Facet face based on split curves 

        """
        ByColor: int
        ByRegion: int
        ByCurves: int
        @staticmethod
        def ValueOf(value: int) -> DivideFacetFaceBuilder.DivideFacetTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Degree(self) -> int:
        """
        Getter for property: (int) Degree
         Returns the polynomial degree (one unit less than the order).  
            
         
        """
        pass
    @Degree.setter
    def Degree(self, degree: int):
        """
        Setter for property: (int) Degree
         Returns the polynomial degree (one unit less than the order).  
            
         
        """
        pass
    @property
    def FacetBodyCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FacetBodyCollector
         Returns the collector for specifying facet bodies to be divided based on colored regions.  
            
         
        """
        pass
    @property
    def FacetCollector(self) -> NXOpen.FacetCollector:
        """
        Getter for property: ( NXOpen.FacetCollector) FacetCollector
         Returns the collector for specifying facet regions  
            
         
        """
        pass
    @property
    def IsEditCopy(self) -> bool:
        """
        Getter for property: (bool) IsEditCopy
         Returns the value indicating if a copy of the facet body to be used for Divide facet face without altering the original   
            
         
        """
        pass
    @IsEditCopy.setter
    def IsEditCopy(self, isEditCopy: bool):
        """
        Setter for property: (bool) IsEditCopy
         Returns the value indicating if a copy of the facet body to be used for Divide facet face without altering the original   
            
         
        """
        pass
    @property
    def IsSmoothEdge(self) -> bool:
        """
        Getter for property: (bool) IsSmoothEdge
         Returns the option to add smoothing to the edge of the divided region    
            
         
        """
        pass
    @IsSmoothEdge.setter
    def IsSmoothEdge(self, isSmoothEdge: bool):
        """
        Setter for property: (bool) IsSmoothEdge
         Returns the option to add smoothing to the edge of the divided region    
            
         
        """
        pass
    @property
    def Segments(self) -> int:
        """
        Getter for property: (int) Segments
         Returnsthe number of segments used for advanced fitting  
            
         
        """
        pass
    @Segments.setter
    def Segments(self, segments: int):
        """
        Setter for property: (int) Segments
         Returnsthe number of segments used for advanced fitting  
            
         
        """
        pass
    @property
    def SplitCurveMethodListDataManager(self) -> SplitCurveMethodListDataManager:
        """
        Getter for property: ( SplitCurveMethodListDataManager NXOpe) SplitCurveMethodListDataManager
         Returns the split curve method list data manager   
            
         
        """
        pass
    @property
    def Type(self) -> DivideFacetFaceBuilder.DivideFacetTypes:
        """
        Getter for property: ( DivideFacetFaceBuilder.DivideFacetTypes NXOpe) Type
         Returns the type of enum which decides method for dividing facet faces  
            
         
        """
        pass
    @Type.setter
    def Type(self, type: DivideFacetFaceBuilder.DivideFacetTypes):
        """
        Setter for property: ( DivideFacetFaceBuilder.DivideFacetTypes NXOpe) Type
         Returns the type of enum which decides method for dividing facet faces  
            
         
        """
        pass
import NXOpen
class ExtrudeFacetBodyBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Facet.ExtrudeFacetBodyBuilder
    It extrudes a NX Facet Body. The limit of extrusion can be specified by direction and distance
    or plane object. It returns the extruded NX Facet Body.
    """
    class LimitType(Enum):
        """
        Members Include: 
         |Distance|  Specify the limit by direction and distance. Direction and Distance need to be specified. 
         |ToPlane|  Specify the limit by plane object. Plane needes to be specified. 

        """
        Distance: int
        ToPlane: int
        @staticmethod
        def ValueOf(value: int) -> ExtrudeFacetBodyBuilder.LimitType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Direction(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) Direction
         Returns the direction used when limit type is  NXOpen::Facet::ExtrudeFacetBodyBuilder::LimitTypeDistance    
            
         
        """
        pass
    @Direction.setter
    def Direction(self, direction: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) Direction
         Returns the direction used when limit type is  NXOpen::Facet::ExtrudeFacetBodyBuilder::LimitTypeDistance    
            
         
        """
        pass
    @property
    def Distance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Distance
         Returns the distance used when limit type is  NXOpen::Facet::ExtrudeFacetBodyBuilder::LimitTypeDistance    
            
         
        """
        pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance used in the extrude facet body feature   
            
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance used in the extrude facet body feature   
            
         
        """
        pass
    @property
    def FacetBody(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) FacetBody
         Returns the facetsheet bodies to be extruded   
            
         
        """
        pass
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Offset
         Returns the offset value used to offset the extruded body   
            
         
        """
        pass
    @property
    def Plane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) Plane
         Returns the plane used when limit type is  NXOpen::Facet::ExtrudeFacetBodyBuilder::LimitTypeToPlane    
            
         
        """
        pass
    @Plane.setter
    def Plane(self, plane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) Plane
         Returns the plane used when limit type is  NXOpen::Facet::ExtrudeFacetBodyBuilder::LimitTypeToPlane    
            
         
        """
        pass
    @property
    def Type(self) -> ExtrudeFacetBodyBuilder.LimitType:
        """
        Getter for property: ( ExtrudeFacetBodyBuilder.LimitType NXOpe) Type
         Returns the limit type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: ExtrudeFacetBodyBuilder.LimitType):
        """
        Setter for property: ( ExtrudeFacetBodyBuilder.LimitType NXOpe) Type
         Returns the limit type   
            
         
        """
        pass
import NXOpen
class ExtrudeProfileBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Facet.ExtrudeProfileBuilder
    It extrudes 3D closed profile between planes. The two planes are defined 
    by direction and distance. It returns the extruded NX Facet Body.
    """
    @property
    def Direction(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) Direction
         Returns the extrude direction   
            
         
        """
        pass
    @Direction.setter
    def Direction(self, direction: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) Direction
         Returns the extrude direction   
            
         
        """
        pass
    @property
    def FirstDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FirstDistance
         Returns the first distance to extrude   
            
         
        """
        pass
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Offset
         Returns the offset used to offset the extruded body   
            
         
        """
        pass
    @property
    def Profile(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Profile
         Returns the 3D profile to be extruded   
            
         
        """
        pass
    @property
    def SecondDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SecondDistance
         Returns the second distance to extrude   
            
         
        """
        pass
    @property
    def Tolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Tolerance
         Returns the tolerance used to create the polyline   
            
         
        """
        pass
import NXOpen
class FacetBodyFromBodyBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Facet.FacetBodyFromBodyBuilder builder. 
    It converts the selected analytic bodies to NX convergent bodies bodies. 
    The original inputs are deleted.
    """
    class OriginalBodyOptions(Enum):
        """
        Members Include: 
         |Keep|  Keep original body 
         |Hide|  Hide original body 
         |Delete|  Delete original body 

        """
        Keep: int
        Hide: int
        Delete: int
        @staticmethod
        def ValueOf(value: int) -> FacetBodyFromBodyBuilder.OriginalBodyOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OutputTypes(Enum):
        """
        Members Include: 
         |ConvergentBody|  Convert To Convergent bodies 
         |NXFacetBody|  Convert to NX Facet Bodies 
         |JTFacetBody|  Convert To JT Facet bodies 

        """
        ConvergentBody: int
        NXFacetBody: int
        JTFacetBody: int
        @staticmethod
        def ValueOf(value: int) -> FacetBodyFromBodyBuilder.OutputTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns the option that specifies whether the facet body from body operation is associative   
            
         
        """
        pass
    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
         Returns the option that specifies whether the facet body from body operation is associative   
            
         
        """
        pass
    @property
    def MaximumDeviation(self) -> float:
        """
        Getter for property: (float) MaximumDeviation
         Returns the maximum deviation   
            
         
        """
        pass
    @MaximumDeviation.setter
    def MaximumDeviation(self, maximumDeviation: float):
        """
        Setter for property: (float) MaximumDeviation
         Returns the maximum deviation   
            
         
        """
        pass
    @property
    def NonFacetedBodiesToConvert(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) NonFacetedBodiesToConvert
         Returns the input non-faceted bodies to convert   
            
         
        """
        pass
    @property
    def OriginalBodyOption(self) -> FacetBodyFromBodyBuilder.OriginalBodyOptions:
        """
        Getter for property: ( FacetBodyFromBodyBuilder.OriginalBodyOptions NXOpe) OriginalBodyOption
         Returns the original body option of enum   
            
         
        """
        pass
    @OriginalBodyOption.setter
    def OriginalBodyOption(self, enumOriginalBodyOption: FacetBodyFromBodyBuilder.OriginalBodyOptions):
        """
        Setter for property: ( FacetBodyFromBodyBuilder.OriginalBodyOptions NXOpe) OriginalBodyOption
         Returns the original body option of enum   
            
         
        """
        pass
    @property
    def OutputType(self) -> FacetBodyFromBodyBuilder.OutputTypes:
        """
        Getter for property: ( FacetBodyFromBodyBuilder.OutputTypes NXOpe) OutputType
         Returns the output of the type of enum   
            
         
        """
        pass
    @OutputType.setter
    def OutputType(self, enumOutputType: FacetBodyFromBodyBuilder.OutputTypes):
        """
        Setter for property: ( FacetBodyFromBodyBuilder.OutputTypes NXOpe) OutputType
         Returns the output of the type of enum   
            
         
        """
        pass
import NXOpen
class FacetedBodyCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of faceted bodies in a part """
    class Type(Enum):
        """
        Members Include: 
         |Nx|  NX facet 
         |Jt|  JT facet 

        """
        Nx: int
        Jt: int
        @staticmethod
        def ValueOf(value: int) -> FacetedBodyCollection.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FacetModelingCollection() -> FacetModelingCollection:
        """
         Returns the FacetModelingCollection instance belonging to this part 
        """
        pass
    def Convert(self, fromBody: FacetedBody, toFacetType: FacetedBodyCollection.Type) -> None:
        """
         Converts the internal representation of this faceted body to the specified type. This does not create a new body 
        """
        pass
    def Copy(self, fromBody: FacetedBody, toPart: NXOpen.Part, toFacetType: FacetedBodyCollection.Type) -> FacetedBody:
        """
         Copies a faceted body and optionally changes the internal representation to the given type
                     (This is only valid for JT to NX copy) 
                 
         Returns copy ( FacetedBody NXOpe):  New body .
        """
        pass
    def CreateBestFitAlignBuilder(self) -> BestFitAlignBuilder:
        """
         Creates a NXOpen.Facet.BestFitAlignBuilder 
         Returns builder ( BestFitAlignBuilder NXOpe): .
        """
        pass
    def CreateBridgeFacetBodyBuilder(self) -> BridgeFacetBodyBuilder:
        """
         Creates a NXOpen.Facet.BridgeFacetBodyBuilder 
         Returns builder ( BridgeFacetBodyBuilder NXOpe): .
        """
        pass
    def CreateDecimateFacetBodyBuilder(self) -> DecimateFacetBodyBuilder:
        """
         Creates a NXOpen.Facet.DecimateFacetBodyBuilder 
         Returns builder ( DecimateFacetBodyBuilder NXOpe): .
        """
        pass
    def CreateExtrudeFacetBodyBuilder(self) -> ExtrudeFacetBodyBuilder:
        """
         Creates a NXOpen.Facet.ExtrudeFacetBodyBuilder 
         Returns builder ( ExtrudeFacetBodyBuilder NXOpe): .
        """
        pass
    def CreateExtrudeProfileBuilder(self) -> ExtrudeProfileBuilder:
        """
         Creates a NXOpen.Facet.ExtrudeProfileBuilder 
         Returns builder ( ExtrudeProfileBuilder NXOpe): .
        """
        pass
    def CreateFacetBody(self, solidBodies: List[NXOpen.Body]) -> Tuple[List[FacetedBody], List[int]]:
        """
         Creates a JT NXOpen.Facet.FacetedBody using the default faceting tolerances. 
                    The output facetBodies and errorTable arrays are the same size as the input nSolidBodies. 
                    The errorTable array provides information about any errors encountered when faceting bodies. 
                    Note that it is possible that faceted bodies with 0 facets are created (and returned in the facetBodies parameter). 
                    For this case, the errorTable will contain the UF_FACET_err_zero_facets_produced error. 
                    If there is an existing facet body it will get refaceted with the previous tolerance used to tessellate it .
                    See NXOpen.Body.GetFacetedBody for ways to check for this situation.
                
         Returns A tuple consisting of (facetBodies, errorTable). 
         - facetBodies is:  FacetedBody List[NXO.
         - errorTable is: List[int].

        """
        pass
    def CreateFacetBodyFromFaces(self, solidFaces: List[NXOpen.Face]) -> Tuple[List[FacetedBody], List[int]]:
        """
         Creates a JT NXOpen.Facet.FacetedBody using the default faceting tolerances. 
                    The output facetBodies and errorTable arrays are the same size as the input nSolidFaces. 
                    The errorTable array provides information about any errors encountered when faceting bodies. 
                    Note that it is possible that faceted bodies with 0 facets are created (and returned in the facetBodies parameter). 
                    For this case, the errorTable will contain the UF_FACET_err_zero_facets_produced error. 
                    If there is an existing facet body it will get refaceted with the previous tolerance used to tessellate it .
                    See NXOpen.Body.GetFacetedBody for ways to check for this situation.
                
         Returns A tuple consisting of (facetBodies, errorTable). 
         - facetBodies is:  FacetedBody List[NXO.
         - errorTable is: List[int].

        """
        pass
    def CreateFacetCurvatureBuilder(self) -> CurvatureBuilder:
        """
         Create a NXOpen.Facet.CurvatureBuilder object. 
         Returns builder ( CurvatureBuilder NXOpe): .
        """
        pass
    def CreateFacetFeatureExtractionBuilder(self) -> FeatureExtractionBuilder:
        """
         Create a NXOpen.Facet.FeatureExtractionBuilder object. 
         Returns builder ( FeatureExtractionBuilder NXOpe): .
        """
        pass
    def CreateFillHoleBuilder(self) -> FillHoleBuilder:
        """
         Creates a NXOpen.Facet.FillHoleBuilder 
         Returns builder ( FillHoleBuilder NXOpe): .
        """
        pass
    def CreateMergeFacetBodyBuilder(self) -> MergeFacetBodyBuilder:
        """
         Creates a NXOpen.Facet.MergeFacetBodyBuilder 
         Returns builder ( MergeFacetBodyBuilder NXOpe): .
        """
        pass
    def CreateMultiPatchAlignmentBuilder(self) -> MultiPatchAlignmentBuilder:
        """
         Creates a NXOpen.Facet.MultiPatchAlignmentBuilder 
         Returns builder ( MultiPatchAlignmentBuilder NXOpe): .
        """
        pass
    def CreateSTLImportBuilder(self) -> STLImportBuilder:
        """
         Creates a NXOpen.Facet.STLImportBuilder 
         Returns builder ( STLImportBuilder NXOpe): .
        """
        pass
    def CreateSewFacetBodyBuilder(self) -> SewFacetBodyBuilder:
        """
         Creates a NXOpen.Facet.SewFacetBodyBuilder 
         Returns builder ( SewFacetBodyBuilder NXOpe): .
        """
        pass
    def CreateSmoothFacetBodyBuilder(self) -> SmoothFacetBodyBuilder:
        """
         Creates a NXOpen.Facet.SmoothFacetBodyBuilder 
         Returns builder ( SmoothFacetBodyBuilder NXOpe): .
        """
        pass
    def CreateSnipFacetBodyBuilder(self) -> SnipFacetBodyBuilder:
        """
         Creates a NXOpen.Facet.SnipFacetBodyBuilder 
         Returns builder ( SnipFacetBodyBuilder NXOpe): .
        """
        pass
    def CreateSubdivideFacetBodyBuilder(self) -> SubdivideFacetBodyBuilder:
        """
         Creates a NXOpen.Facet.SubdivideFacetBodyBuilder 
         Returns builder ( SubdivideFacetBodyBuilder NXOpe): .
        """
        pass
    def DeleteTemporaryFacesAndEdges(self) -> None:
        """
         Delete any temporary faces and edges on faceted bodies that may have been created 
                    in the specified part.  Please note that this call will invoke an Update operation.
                
        """
        pass
    def FindObject(self, journal_identifier: str) -> FacetedBody:
        """
         Finds the  NXOpen.Facet.FacetedBody  with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.
                    An exception will be thrown if no object can be found with the given journal identifier. 
         Returns found ( FacetedBody NXOpe):  Faceted body with this identifier .
        """
        pass
    def GetAssociatedFacetedBodies(self, solidBody: NXOpen.Body) -> Tuple[List[FacetedBody], int]:
        """
         Returns the loaded solid bodies associated with the argument faceted body.
                    Also returns the number of unloaded associated faceted bodies.
                
         Returns A tuple consisting of (associatedFacetedBodies, numberOfUnloadedFacetedBodies). 
         - associatedFacetedBodies is:  FacetedBody List[NXO. Array of loaded associated faceted bodies .
         - numberOfUnloadedFacetedBodies is: int. The number of unloaded associated faceted bodies for this solids body .

        """
        pass
import NXOpen
class FacetedBody(NXOpen.DisplayableObject): 
    """ 
    Represents a faceted body. Instances of this class cannot be created directly by the user, but can
    be created using the methods of FacetedBodyCollection.
    """
    class FacetedbodyType(Enum):
        """
        Members Include: 
         |Undefined|  Undefined body type 
         |SolidBody| 
         |SheetBody| 

        """
        Undefined: int
        SolidBody: int
        SheetBody: int
        @staticmethod
        def ValueOf(value: int) -> FacetedBody.FacetedbodyType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AssociatedBody(self) -> NXOpen.Body:
        """
        Getter for property: ( NXOpen.Body) AssociatedBody
         Returns
                    the solid body associated with this facet body.  
          
                  
         
        """
        pass
    @property
    def BodyType(self) -> FacetedBody.FacetedbodyType:
        """
        Getter for property: ( FacetedBody.FacetedbodyType NXOpe) BodyType
         Returns the type of the body.  
          
                    This only works for JT Facets.
                  
         
        """
        pass
    @property
    def IsAssemblyLevel(self) -> bool:
        """
        Getter for property: (bool) IsAssemblyLevel
         Returns
                    a flag indicating this is an assembly level representation.  
           That is
                    this facet body is associated with an occurrence of a solid body. 
                  
         
        """
        pass
    @property
    def IsAssociatedBodyLoaded(self) -> bool:
        """
        Getter for property: (bool) IsAssociatedBodyLoaded
         Returns
                    the load state of the solid body associated with this facet body.  
          
                    False if there is no associated body.
                  
         
        """
        pass
    @property
    def IsSheetBody(self) -> bool:
        """
        Getter for property: (bool) IsSheetBody
         Returns true if the body is a sheet body   
            
         
        """
        pass
    @property
    def IsSolidBody(self) -> bool:
        """
        Getter for property: (bool) IsSolidBody
         Returns true if the body is a solid body   
            
         
        """
        pass
    @property
    def NumberOfFaces(self) -> int:
        """
        Getter for property: (int) NumberOfFaces
         Returns
                    the number of faces in this faceted body in the highest level of detail.  
          
                    Typically only useful if the model has been derived from a solid model. 
                    For models constructed directly, the output will be number of facetstriangles, since there would be no faces. 
                  
         
        """
        pass
    @property
    def NumberOfLevelsOfDetail(self) -> int:
        """
        Getter for property: (int) NumberOfLevelsOfDetail
         Returns
                    the number of levels of detail in this faceted body.  
          
                  
         
        """
        pass
    @property
    def SurfaceArea(self) -> float:
        """
        Getter for property: (float) SurfaceArea
         Returns
                    the surface area of the faceted body in part units for its
                    highest level of detail.  
          
                  
         
        """
        pass
    @property
    def Volume(self) -> float:
        """
        Getter for property: (float) Volume
         Returns
                    the volume of the faceted body in part units for its
                    highest level of detail.  
          
                  
         
        """
        pass
    def DestroyOwnedFacets(self) -> None:
        """
                    Destroys all IFacet objects owned by this body.
                     
                    Please note that this method does not geometrically delete a facet from its surface mesh leaving a hole. 
                    It only deletes the tagged object created to represent the individual facet.
                    
                
        """
        pass
    def GetEdges(self) -> List[FacetedEdge]:
        """
         Returns the edges in the faceted body.
                    This only works for JT Facets.
                
         Returns edges ( FacetedEdge List[NXO):  .
        """
        pass
    def GetFaces(self) -> List[FacetedFace]:
        """
         Returns the faces in the faceted body.
                    This only works for JT Facets.
                
         Returns faceted_face ( FacetedFace List[NXO): .
        """
        pass
    def GetNumberOfEdges(self) -> int:
        """
         Returns the number of edges in the faceted body.
                    This only works for JT Facets.
                
         Returns number_of_edges (int): .
        """
        pass
    def GetNumberOfFacets(self, level_of_detail: int) -> int:
        """
                    Get the number of facets in the given level of detail.
                
         Returns count (int): .
        """
        pass
    def GetParameters(self) -> FacetingParameters:
        """
         
                    Get the faceted body parameters
                
         Returns parameters ( FacetingParameters NXOpe):  faceting parameters for this body .
        """
        pass
    def HasLightWeightAnalytics(self) -> bool:
        """
         Returns whether the FACET has analytical information.
                    This only works for JT Facets.
                
         Returns has_lightweight_analytics (bool): .
        """
        pass
    def HasTopologyInformation(self) -> bool:
        """
         Returns whether the FACET has topology information.
                    This only works for JT Facets.
                
         Returns has_topology_information (bool): .
        """
        pass
    def SetParameters(self, parameters: FacetingParameters) -> None:
        """
         
                    Set the faceted body parameters, it will retessellate the body with the new parameters
                
        """
        pass
import NXOpen
class FacetedEdge(NXOpen.DisplayableObject): 
    """ Represents a faceted edge. Instances of this class may be
        generated when recording a journal, but they cannot be created
        directly. 
    """
    class FacetededgeType(Enum):
        """
        Members Include: 
         |Undefined| 
         |Linear|  Linear edge 
         |Circular|  Circular edge 
         |Elliptical|  Elliptical edge 
         |Intersection|  Intersection edge 
         |Spline|  Spline edge 

        """
        Undefined: int
        Linear: int
        Circular: int
        Elliptical: int
        Intersection: int
        Spline: int
        @staticmethod
        def ValueOf(value: int) -> FacetedEdge.FacetededgeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EdgeType(self) -> FacetedEdge.FacetededgeType:
        """
        Getter for property: ( FacetedEdge.FacetededgeType NXOpe) EdgeType
         Returns the type of the facet edge   
            
         
        """
        pass
    @property
    def IsReference(self) -> bool:
        """
        Getter for property: (bool) IsReference
         Returns the reference state of a curve   
            
         
        """
        pass
    def GetBody(self) -> FacetedBody:
        """
         Returns the body containing this edge 
         Returns faceted_body ( FacetedBody NXOpe):  .
        """
        pass
    def GetCurveData(self) -> Tuple[NXOpen.Point3d, NXOpen.Point3d, NXOpen.Point3d, float, float]:
        """
         Returns the curve information for the facet edge
                   Parameter description
                   faceted_edge           : The input edge tag for which curve information is required.
                   PNT3_p_t position      : Line: Position on Line 
                                            CircleEllipse: Center Point
                                            SplineIntersection-Curve: Start Point of Curve.
                   PNT3_p_t dir_or_end_pt : Line : Direction of the Line
                                            Circle: Normal to Plane Axis.
                                            Ellipse: Major Axis
                                            SplineIntersection-Curve: End Point.
                   PNT3_p_t x_axis         : Circle: Axis from Center to Start Point,
                                            Ellipse: Minor Axis
                                            Not valid for other types.
               
                   double radius         : Circle: Radius
                                            Ellipse: Major Radius
                                            Not valid for other types.
                   double minor_radius   : Ellipse: Minor Radius
                                            Not valid for other types.
                
         Returns A tuple consisting of (position, dir_or_end_pt, x_axis, radius, minor_radius). 
         - position is:  NXOpen.Point3d.
         - dir_or_end_pt is:  NXOpen.Point3d.
         - x_axis is:  NXOpen.Point3d.
         - radius is: float.
         - minor_radius is: float.

        """
        pass
    def GetFaces(self) -> List[FacetedFace]:
        """
         Returns the faces connected to the edge 
         Returns faces ( FacetedFace List[NXO): .
        """
        pass
    def GetVertices(self) -> Tuple[NXOpen.Point3d, NXOpen.Point3d]:
        """
         Returns the vertices of the edge. If the edge is closed, the second vertex is the same as the first. 
         Returns A tuple consisting of (vertex1, vertex2). 
         - vertex1 is:  NXOpen.Point3d. First vertex in the edge .
         - vertex2 is:  NXOpen.Point3d. Second vertex in the edge .

        """
        pass
import NXOpen
class FacetedFace(NXOpen.DisplayableObject): 
    """ Represents a faceted face. Instances of this class may be
        generated when recording a journal, but they cannot be created
        directly. 
    """
    class FacetedfaceType(Enum):
        """
        Members Include: 
         |Undefined|  Undefined body type 
         |Planar|  Planar face 
         |Cylindrical|  Cylindrical face 
         |Conical|  Conical face 
         |Spherical|  Spherical face 
         |Toroidal|  Face from toroid 
         |Parametric|  Parametric face 

        """
        Undefined: int
        Planar: int
        Cylindrical: int
        Conical: int
        Spherical: int
        Toroidal: int
        Parametric: int
        @staticmethod
        def ValueOf(value: int) -> FacetedFace.FacetedfaceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FaceType(self) -> FacetedFace.FacetedfaceType:
        """
        Getter for property: ( FacetedFace.FacetedfaceType NXOpe) FaceType
         Returns the type of the face   
            
         
        """
        pass
    def GetBody(self) -> FacetedBody:
        """
         Returns the facet body containing this facet face 
         Returns faceted_body ( FacetedBody NXOpe): .
        """
        pass
    def GetEdges(self) -> List[FacetedEdge]:
        """
         Returns the edges connected to the face 
         Returns faceted_edges ( FacetedEdge List[NXO): .
        """
        pass
    def GetNumberOfEdges(self) -> int:
        """
         Returns the number of edges in the faceted face 
         Returns number_of_edges (int): .
        """
        pass
    def GetSurfaceData(self) -> Tuple[NXOpen.Point3d, NXOpen.Point3d, float, float, bool]:
        """
         Returns the surface information for this face 
               
                    tag_t    faceted_face     : The input edge tag for which face information is required.
                    PNT3_p_t position         : Plane: Position on Plane
                                                Origin for other
                    PNT3_p_t dir              : Plane: Normal direction
                                                Axis for others.
                    double   radius          : Not applicable for planes
                                                Cylinder: Radius of Cylinder, 
                                                Sphere: Radius of Sphere
                                                Cone: Radius of Circle on the cone and in the plane passing through the position.
                    double   radius_or_angle : Cone: Half Angle. 
                    logical  sense           : Indicates the sense of normal
                
         Returns A tuple consisting of (position, dir, radius, radius_or_angle, sense). 
         - position is:  NXOpen.Point3d.
         - dir is:  NXOpen.Point3d.
         - radius is: float.
         - radius_or_angle is: float.
         - sense is: bool.

        """
        pass
class FacetingParameters:
    """
     The structure of JA faceting parameters 
    """
    @property
    def MaximumFacetEdges(self) -> int:
        """
        Getter for property MaximumFacetEdges
        The maximum number of edges allowed                                               in the facets that are to be generated                                                (this does not apply to JT).

        """
        pass
    @MaximumFacetEdges.setter
    def MaximumFacetEdges(self, value: int):
        """
        Getter for property MaximumFacetEdges
        The maximum number of edges allowed                                               in the facets that are to be generated                                                (this does not apply to JT).
        Setter for property MaximumFacetEdges
        The maximum number of edges allowed                                               in the facets that are to be generated                                                (this does not apply to JT).

        """
        pass
    @property
    def SpecifySurfaceTolerance(self) -> bool:
        """
        Getter for property SpecifySurfaceTolerance
        If this value is true, then                                               values must be specified for                                               surfaceDistanceTolerance                                               and surfaceAngularTolerance.

        """
        pass
    @SpecifySurfaceTolerance.setter
    def SpecifySurfaceTolerance(self, value: bool):
        """
        Getter for property SpecifySurfaceTolerance
        If this value is true, then                                               values must be specified for                                               surfaceDistanceTolerance                                               and surfaceAngularTolerance.
        Setter for property SpecifySurfaceTolerance
        If this value is true, then                                               values must be specified for                                               surfaceDistanceTolerance                                               and surfaceAngularTolerance.

        """
        pass
    @property
    def SurfaceDistanceTolerance(self) -> float:
        """
        Getter for property SurfaceDistanceTolerance
        This is the maximum distance from                                               the surface to the facet.

        """
        pass
    @SurfaceDistanceTolerance.setter
    def SurfaceDistanceTolerance(self, value: float):
        """
        Getter for property SurfaceDistanceTolerance
        This is the maximum distance from                                               the surface to the facet.
        Setter for property SurfaceDistanceTolerance
        This is the maximum distance from                                               the surface to the facet.

        """
        pass
    @property
    def SurfaceAngularTolerance(self) -> float:
        """
        Getter for property SurfaceAngularTolerance
        This is the maximum angular variation                                               in radians of the surface normal                                               over the facet.

        """
        pass
    @SurfaceAngularTolerance.setter
    def SurfaceAngularTolerance(self, value: float):
        """
        Getter for property SurfaceAngularTolerance
        This is the maximum angular variation                                               in radians of the surface normal                                               over the facet.
        Setter for property SurfaceAngularTolerance
        This is the maximum angular variation                                               in radians of the surface normal                                               over the facet.

        """
        pass
    @property
    def SpecifyCurveTolerance(self) -> bool:
        """
        Getter for property SpecifyCurveTolerance
        This indicates that values are to be                                               specified for curveDistanceTolerance                                               and curveAngularTolerance and                                               curve_max_length.

        """
        pass
    @SpecifyCurveTolerance.setter
    def SpecifyCurveTolerance(self, value: bool):
        """
        Getter for property SpecifyCurveTolerance
        This indicates that values are to be                                               specified for curveDistanceTolerance                                               and curveAngularTolerance and                                               curve_max_length.
        Setter for property SpecifyCurveTolerance
        This indicates that values are to be                                               specified for curveDistanceTolerance                                               and curveAngularTolerance and                                               curve_max_length.

        """
        pass
    @property
    def CurveDistanceTolerance(self) -> float:
        """
        Getter for property CurveDistanceTolerance
        This is the maximum distance between                                               the facet edge and the curve segment                                               represented by the facet edge.

        """
        pass
    @CurveDistanceTolerance.setter
    def CurveDistanceTolerance(self, value: float):
        """
        Getter for property CurveDistanceTolerance
        This is the maximum distance between                                               the facet edge and the curve segment                                               represented by the facet edge.
        Setter for property CurveDistanceTolerance
        This is the maximum distance between                                               the facet edge and the curve segment                                               represented by the facet edge.

        """
        pass
    @property
    def CurveAngularTolerance(self) -> float:
        """
        Getter for property CurveAngularTolerance
        This is the maximum angular variation                                               in radians of the curve tangent along                                               the curve segment represented by the                                               facet edge.

        """
        pass
    @CurveAngularTolerance.setter
    def CurveAngularTolerance(self, value: float):
        """
        Getter for property CurveAngularTolerance
        This is the maximum angular variation                                               in radians of the curve tangent along                                               the curve segment represented by the                                               facet edge.
        Setter for property CurveAngularTolerance
        This is the maximum angular variation                                               in radians of the curve tangent along                                               the curve segment represented by the                                               facet edge.

        """
        pass
    @property
    def CurveMaximumLength(self) -> float:
        """
        Getter for property CurveMaximumLength
        The maximum length of a curve, default is 1000.

        """
        pass
    @CurveMaximumLength.setter
    def CurveMaximumLength(self, value: float):
        """
        Getter for property CurveMaximumLength
        The maximum length of a curve, default is 1000.
        Setter for property CurveMaximumLength
        The maximum length of a curve, default is 1000.

        """
        pass
    @property
    def SpecifyConvexFacets(self) -> bool:
        """
        Getter for property SpecifyConvexFacets
        This indicates that the facets                                               generated by the faceter should all be                                               convex (this does not apply to JT).

        """
        pass
    @SpecifyConvexFacets.setter
    def SpecifyConvexFacets(self, value: bool):
        """
        Getter for property SpecifyConvexFacets
        This indicates that the facets                                               generated by the faceter should all be                                               convex (this does not apply to JT).
        Setter for property SpecifyConvexFacets
        This indicates that the facets                                               generated by the faceter should all be                                               convex (this does not apply to JT).

        """
        pass
    @property
    def SpecifyMaximumFacetSize(self) -> bool:
        """
        Getter for property SpecifyMaximumFacetSize
        This indicates that a maximum width of                                               facet is to be specified using                                               maximumFacetSize.

        """
        pass
    @SpecifyMaximumFacetSize.setter
    def SpecifyMaximumFacetSize(self, value: bool):
        """
        Getter for property SpecifyMaximumFacetSize
        This indicates that a maximum width of                                               facet is to be specified using                                               maximumFacetSize.
        Setter for property SpecifyMaximumFacetSize
        This indicates that a maximum width of                                               facet is to be specified using                                               maximumFacetSize.

        """
        pass
    @property
    def MaximumFacetSize(self) -> float:
        """
        Getter for property MaximumFacetSize
        This is the maximum width of a facet.

        """
        pass
    @MaximumFacetSize.setter
    def MaximumFacetSize(self, value: float):
        """
        Getter for property MaximumFacetSize
        This is the maximum width of a facet.
        Setter for property MaximumFacetSize
        This is the maximum width of a facet.

        """
        pass
    @property
    def SpecifyParameters(self) -> bool:
        """
        Getter for property SpecifyParameters
        This indicates that the model will be                                               created with the parametric information                                               for each vertex.

        """
        pass
    @SpecifyParameters.setter
    def SpecifyParameters(self, value: bool):
        """
        Getter for property SpecifyParameters
        This indicates that the model will be                                               created with the parametric information                                               for each vertex.
        Setter for property SpecifyParameters
        This indicates that the model will be                                               created with the parametric information                                               for each vertex.

        """
        pass
    @property
    def NumberStorageType(self) -> int:
        """
        Getter for property NumberStorageType
        This indicates whether the real                                               numbers for facet vertices and facet                                               normals should be stored as floats                                               (UF_FACET_TYPE_FLOAT) or as doubles                                               (UF_FACET_TYPE_DOUBLE).

        """
        pass
    @NumberStorageType.setter
    def NumberStorageType(self, value: int):
        """
        Getter for property NumberStorageType
        This indicates whether the real                                               numbers for facet vertices and facet                                               normals should be stored as floats                                               (UF_FACET_TYPE_FLOAT) or as doubles                                               (UF_FACET_TYPE_DOUBLE).
        Setter for property NumberStorageType
        This indicates whether the real                                               numbers for facet vertices and facet                                               normals should be stored as floats                                               (UF_FACET_TYPE_FLOAT) or as doubles                                               (UF_FACET_TYPE_DOUBLE).

        """
        pass
    @property
    def SpecifyViewDirection(self) -> bool:
        """
        Getter for property SpecifyViewDirection
        Should we use a viewing direction                                               for denser faceting around                                               silhouettes.

        """
        pass
    @SpecifyViewDirection.setter
    def SpecifyViewDirection(self, value: bool):
        """
        Getter for property SpecifyViewDirection
        Should we use a viewing direction                                               for denser faceting around                                               silhouettes.
        Setter for property SpecifyViewDirection
        Should we use a viewing direction                                               for denser faceting around                                               silhouettes.

        """
        pass
    @property
    def SilhouetteViewDirection(self) -> NXOpen.Vector3d:
        """
        Getter for property SilhouetteViewDirection
        If specifyViewDirection is specified,                                               then this is the view direction to use                                               (this does not apply to JT).

        """
        pass
    @SilhouetteViewDirection.setter
    def SilhouetteViewDirection(self, value: NXOpen.Vector3d):
        """
        Getter for property SilhouetteViewDirection
        If specifyViewDirection is specified,                                               then this is the view direction to use                                               (this does not apply to JT).
        Setter for property SilhouetteViewDirection
        If specifyViewDirection is specified,                                               then this is the view direction to use                                               (this does not apply to JT).

        """
        pass
    @property
    def SilhouetteChordTolerance(self) -> float:
        """
        Getter for property SilhouetteChordTolerance
        If specifyViewDirection is specified                                               then this is the tolerance which will be                                               used as a tighter surface tolerance                                               in the silhouette area specified                                               by the view direction (this does not apply to JT).

        """
        pass
    @SilhouetteChordTolerance.setter
    def SilhouetteChordTolerance(self, value: float):
        """
        Getter for property SilhouetteChordTolerance
        If specifyViewDirection is specified                                               then this is the tolerance which will be                                               used as a tighter surface tolerance                                               in the silhouette area specified                                               by the view direction (this does not apply to JT).
        Setter for property SilhouetteChordTolerance
        If specifyViewDirection is specified                                               then this is the tolerance which will be                                               used as a tighter surface tolerance                                               in the silhouette area specified                                               by the view direction (this does not apply to JT).

        """
        pass
    @property
    def StoreFaceTag(self) -> bool:
        """
        Getter for property StoreFaceTag
        Should this FACET body record face tags or not                                                (this does not apply to JT).

        """
        pass
    @StoreFaceTag.setter
    def StoreFaceTag(self, value: bool):
        """
        Getter for property StoreFaceTag
        Should this FACET body record face tags or not                                                (this does not apply to JT).
        Setter for property StoreFaceTag
        Should this FACET body record face tags or not                                                (this does not apply to JT).

        """
        pass
    @property
    def WithLODS(self) -> bool:
        """
        Getter for property WithLODS
        When creating a JT facet body whether to create LODs or not                                                (this does not apply to NX).

        """
        pass
    @WithLODS.setter
    def WithLODS(self, value: bool):
        """
        Getter for property WithLODS
        When creating a JT facet body whether to create LODs or not                                                (this does not apply to NX).
        Setter for property WithLODS
        When creating a JT facet body whether to create LODs or not                                                (this does not apply to NX).

        """
        pass
import NXOpen
import NXOpen.Features
class FacetModelingCollection(NXOpen.Object): 
    """ Collection of freeform facet operations. """
    def CreateCleanupFacetBodyBuilder(self) -> CleanupFacetBodyBuilder:
        """
         Creates a NXOpen.Facet.CleanupFacetBodyBuilder 
         Returns builder ( CleanupFacetBodyBuilder NXOpe): .
        """
        pass
    def CreateCleanupFacetBodyWizardBuilder(self) -> CleanupFacetBodyWizardBuilder:
        """
         Creates a NXOpen.Facet.CleanupFacetBodyWizardBuilder 
         Returns builder ( CleanupFacetBodyWizardBuilder NXOpe): .
        """
        pass
    def CreateCombineFacetBodiesBuilder(self) -> CombineFacetBodiesBuilder:
        """
         Creates a NXOpen.Facet.CombineFacetBodiesBuilder 
         Returns builder ( CombineFacetBodiesBuilder NXOpe): .
        """
        pass
    def CreateCombineFacetBodyBuilder(self) -> CombineFacetBodyBuilder:
        """
         Creates a NXOpen.Facet.CombineFacetBodyBuilder 
         Returns builder ( CombineFacetBodyBuilder NXOpe): .
        """
        pass
    def CreateConvertFacetBodyBuilder(self) -> ConvertFacetBodyBuilder:
        """
         Creates a NXOpen.Facet.ConvertFacetBodyBuilder 
         Returns builder ( ConvertFacetBodyBuilder NXOpe): .
        """
        pass
    def CreateCreateTransitionBuilder(self) -> CreateTransitionBuilder:
        """
         Creates a NXOpen.Facet.CreateTransitionBuilder object 
         Returns builder ( CreateTransitionBuilder NXOpe): .
        """
        pass
    def CreateDetectPrimitivesBuilder(self) -> DetectPrimitivesBuilder:
        """
         Creates a NXOpen.Facet.DetectPrimitivesBuilder object. 
         Returns builder ( DetectPrimitivesBuilder NXOpe): .
        """
        pass
    def CreateDivideFacetFaceBuilder(self) -> DivideFacetFaceBuilder:
        """
         Creates a NXOpen.Facet.DivideFacetFaceBuilder 
         Returns builder ( DivideFacetFaceBuilder NXOpe): .
        """
        pass
    def CreateFacetAdjustMinimumRadiusBuilder(self) -> AdjustMinimumRadiusBuilder:
        """
         Create a NXOpen.Facet.AdjustMinimumRadiusBuilder object. 
         Returns builder ( AdjustMinimumRadiusBuilder NXOpe): .
        """
        pass
    def CreateFacetBodyFromBodyBuilder(self) -> FacetBodyFromBodyBuilder:
        """
         Creates a NXOpen.Facet.FacetBodyFromBodyBuilder 
         Returns builder ( FacetBodyFromBodyBuilder NXOpe): .
        """
        pass
    def CreateFillMeshBuilder(self) -> FillMeshBuilder:
        """
         Creates a NXOpen.Facet.FillMeshBuilder 
         Returns builder ( FillMeshBuilder NXOpe): .
        """
        pass
    def CreateLocalOffsetBuilder(self) -> LocalOffsetBuilder:
        """
         Creates a Facet.LocalOffsetBuilder 
         Returns builder ( LocalOffsetBuilder NXOpe): .
        """
        pass
    def CreateMergeFacetFacesBuilder(self) -> MergeFacetFacesBuilder:
        """
         Creates a NXOpen.Facet.MergeFacetFacesBuilder 
         Returns builder ( MergeFacetFacesBuilder NXOpe): .
        """
        pass
    def CreateMeshFromCloudBuilder(self) -> MeshFromCloudBuilder:
        """
         Creates a NXOpen.Facet.MeshFromCloudBuilder 
         Returns builder ( MeshFromCloudBuilder NXOpe): .
        """
        pass
    def CreatePaintBrushBuilder(self) -> PaintBrushBuilder:
        """
         Creates a NXOpen.Facet.PaintBrushBuilder object. 
         Returns builder ( PaintBrushBuilder NXOpe): .
        """
        pass
    def CreatePaintFacetBodyBuilder(self) -> PaintFacetBodyBuilder:
        """
         Creates a NXOpen.Facet.PaintFacetBodyBuilder object. 
         Returns builder ( PaintFacetBodyBuilder NXOpe): .
        """
        pass
    def CreatePlugLeakageBuilder(self) -> PlugLeakageBuilder:
        """
         Creates a NXOpen.Facet.PlugLeakageBuilder 
         Returns builder ( PlugLeakageBuilder NXOpe): .
        """
        pass
    def CreatePolygonModelingBuilder(self) -> PolygonModelingBuilder:
        """
         Creates a NXOpen.Facet.PolygonModelingBuilder 
         Returns builder ( PolygonModelingBuilder NXOpe): .
        """
        pass
    def CreateRemeshFacetBodyBuilder(self) -> RemeshFacetBodyBuilder:
        """
         Creates a Facet.RemeshFacetBodyBuilder 
         Returns builder ( RemeshFacetBodyBuilder NXOpe): .
        """
        pass
    def CreateReplaceMeshWithFaceBuilder(self) -> ReplaceMeshWithFaceBuilder:
        """
         Creates a Facet.ReplaceMeshWithFaceBuilder 
         Returns builder ( ReplaceMeshWithFaceBuilder NXOpe): .
        """
        pass
    def CreateSculptMeshBuilder(self) -> SculptMeshBuilder:
        """
         Creates a NXOpen.Facet.SculptMeshBuilder 
         Returns builder ( SculptMeshBuilder NXOpe): .
        """
        pass
    def CreateSplitCurveMethodBuilder(self) -> SplitCurveMethodBuilder:
        """
         Creates a NXOpen.Facet.SplitCurveMethodBuilder 
         Returns builder ( SplitCurveMethodBuilder NXOpe): .
        """
        pass
    def CreateSplitCurveMethodListDataManager(self) -> SplitCurveMethodListDataManager:
        """
         Creates a NXOpen.Facet.SplitCurveMethodListDataManager 
         Returns dataManager ( SplitCurveMethodListDataManager NXOpe): .
        """
        pass
    def CreateTubeLatticeBuilder(self, tube_lattice: NXOpen.Features.TubeLattice) -> NXOpen.Features.TubeLatticeBuilder:
        """
         Creates a Features.TubeLatticeBuilder 
         Returns builder ( NXOpen.Features.TubeLatticeBuilder):  .
        """
        pass
    def CreateWrapMeshBuilder(self) -> WrapMeshBuilder:
        """
         Creates a NXOpen.Facet.WrapMeshBuilder 
         Returns builder ( WrapMeshBuilder NXOpe): .
        """
        pass
import NXOpen
class FeatureExtractionBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Facet.FeatureExtractionBuilder
    It extracts feature lines or separates regions of different curvature
    from a facet body based on the curvature map.
    For facet body curvature, please see NXOpen.Facet.CurvatureBuilder.
    """
    class InputActions(Enum):
        """
        Members Include: 
         |Blank|  Blank the input facet bodies 
         |Retain|  Retain the input facet bodies 
         |Delete|  Delete the input facet bodies 

        """
        Blank: int
        Retain: int
        Delete: int
        @staticmethod
        def ValueOf(value: int) -> FeatureExtractionBuilder.InputActions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AreBordersEnabled(self) -> bool:
        """
        Getter for property: (bool) AreBordersEnabled
         Returns the extracting borders option   
            
         
        """
        pass
    @AreBordersEnabled.setter
    def AreBordersEnabled(self, bordersEnabled: bool):
        """
        Setter for property: (bool) AreBordersEnabled
         Returns the extracting borders option   
            
         
        """
        pass
    @property
    def AreRegionsEnabled(self) -> bool:
        """
        Getter for property: (bool) AreRegionsEnabled
         Returns  the extracting regions option   
            
         
        """
        pass
    @AreRegionsEnabled.setter
    def AreRegionsEnabled(self, regionsEnabled: bool):
        """
        Setter for property: (bool) AreRegionsEnabled
         Returns  the extracting regions option   
            
         
        """
        pass
    @property
    def FacetBodies(self) -> SelectFacetedBodyList:
        """
        Getter for property: ( SelectFacetedBodyList NXOpe) FacetBodies
         Returns the input facet body selection list   
            
         
        """
        pass
    @property
    def InputAction(self) -> FeatureExtractionBuilder.InputActions:
        """
        Getter for property: ( FeatureExtractionBuilder.InputActions NXOpe) InputAction
         Returns the input facet body action   
            
         
        """
        pass
    @InputAction.setter
    def InputAction(self, inputAction: FeatureExtractionBuilder.InputActions):
        """
        Setter for property: ( FeatureExtractionBuilder.InputActions NXOpe) InputAction
         Returns the input facet body action   
            
         
        """
        pass
    @property
    def IsSmoothingEnabled(self) -> bool:
        """
        Getter for property: (bool) IsSmoothingEnabled
         Returns the smoothing option   
            
         
        """
        pass
    @IsSmoothingEnabled.setter
    def IsSmoothingEnabled(self, smoothingEnabled: bool):
        """
        Setter for property: (bool) IsSmoothingEnabled
         Returns the smoothing option   
            
         
        """
        pass
    @property
    def MinimumBorderLength(self) -> float:
        """
        Getter for property: (float) MinimumBorderLength
         Returns the minimum border length   
            
         
        """
        pass
    @MinimumBorderLength.setter
    def MinimumBorderLength(self, minimumBorderLength: float):
        """
        Setter for property: (float) MinimumBorderLength
         Returns the minimum border length   
            
         
        """
        pass
    @property
    def SmoothingFactor(self) -> float:
        """
        Getter for property: (float) SmoothingFactor
         Returns the smoothing factor   
            
         
        """
        pass
    @SmoothingFactor.setter
    def SmoothingFactor(self, smoothingFactor: float):
        """
        Setter for property: (float) SmoothingFactor
         Returns the smoothing factor   
            
         
        """
        pass
    def GetExtractedBorders(self) -> List[NXOpen.Spline]:
        """
         Gets the extracted curves. Call Builder.Commit before calling this method. 
         Returns borders ( NXOpen.Spline Li):  The extracted curves.
        """
        pass
    def GetExtractedRegions(self) -> List[FacetedBody]:
        """
         Gets the extracted facet bodies. Call Builder.Commit before calling this method. 
         Returns regions ( FacetedBody List[NXO):  The extracted facet bodies .
        """
        pass
import NXOpen
class FillHoleBuilder(NXOpen.Builder): 
    """ This class finds and fills holes to a prescribed boundary smoothness condition.
        Inputs to this class can be convergent objects. """
    class SmoothTypes(Enum):
        """
        Members Include: 
         |Linear|  Linear (triangulated) fill. 
         |Refined|  Smooth internal fill. 
         |TangentBased|  Smooth fill, boundary is based on facet body tangent. 
         |CurvatureBased|  Smooth fill, boundary is based on facet body curvature. 

        """
        Linear: int
        Refined: int
        TangentBased: int
        CurvatureBased: int
        @staticmethod
        def ValueOf(value: int) -> FillHoleBuilder.SmoothTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TargetTypes(Enum):
        """
        Members Include: 
         |UserDefined|  Fills user-defined target holes. 
         |ByNumberOfEdges|  Automatically target holes based on number of edges. 

        """
        UserDefined: int
        ByNumberOfEdges: int
        @staticmethod
        def ValueOf(value: int) -> FillHoleBuilder.TargetTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |FillHole|  Fills individual hole(s). 
         |FillIsland|  Fills a hole defined by inner island and outer facet body. 
         |BridgeGap|  Bridges some open boundary edges with a linear fill. 

        """
        FillHole: int
        FillIsland: int
        BridgeGap: int
        @staticmethod
        def ValueOf(value: int) -> FillHoleBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BridgeEdges1(self) -> NXOpen.SelectICurveList:
        """
        Getter for property: ( NXOpen.SelectICurveList) BridgeEdges1
         Returns the first list of edges when bridging holes.  
             
         
        """
        pass
    @property
    def BridgeEdges2(self) -> NXOpen.SelectICurveList:
        """
        Getter for property: ( NXOpen.SelectICurveList) BridgeEdges2
         Returns the second list of edges when bridging holes.  
             
         
        """
        pass
    @property
    def InnerHole(self) -> NXOpen.SelectICurveList:
        """
        Getter for property: ( NXOpen.SelectICurveList) InnerHole
         Returns the Inner Hole in island filling.  
             
         
        """
        pass
    @property
    def IsEditCopy(self) -> bool:
        """
        Getter for property: (bool) IsEditCopy
         Returns the flag indicating if the hole filling is on the copy of the input facet body.  
             
         
        """
        pass
    @IsEditCopy.setter
    def IsEditCopy(self, isEditCopy: bool):
        """
        Setter for property: (bool) IsEditCopy
         Returns the flag indicating if the hole filling is on the copy of the input facet body.  
             
         
        """
        pass
    @property
    def MaxEdges(self) -> int:
        """
        Getter for property: (int) MaxEdges
         Returns the maximum number of edges that a targeted hole can have.  
             
         
        """
        pass
    @MaxEdges.setter
    def MaxEdges(self, max_edges: int):
        """
        Setter for property: (int) MaxEdges
         Returns the maximum number of edges that a targeted hole can have.  
             
         
        """
        pass
    @property
    def OuterHole(self) -> NXOpen.SelectICurveList:
        """
        Getter for property: ( NXOpen.SelectICurveList) OuterHole
         Returns the Outer Hole in island filling.  
             
         
        """
        pass
    @property
    def SmoothType(self) -> FillHoleBuilder.SmoothTypes:
        """
        Getter for property: ( FillHoleBuilder.SmoothTypes NXOpe) SmoothType
         Returns the boundary smoothness.  
             
         
        """
        pass
    @SmoothType.setter
    def SmoothType(self, smooth_type: FillHoleBuilder.SmoothTypes):
        """
        Setter for property: ( FillHoleBuilder.SmoothTypes NXOpe) SmoothType
         Returns the boundary smoothness.  
             
         
        """
        pass
    @property
    def TargetBody(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: ( NXOpen.SelectDisplayableObject) TargetBody
         Returns the facet body we will be filling.  
             
         
        """
        pass
    @property
    def TargetFacetBody(self) -> SelectFacetedBody:
        """
        Getter for property: ( SelectFacetedBody NXOpe) TargetFacetBody
         Returns the facet body we will be filling.  
             
         
        """
        pass
    @property
    def TargetHole(self) -> NXOpen.SelectICurveList:
        """
        Getter for property: ( NXOpen.SelectICurveList) TargetHole
         Returns the hole curves using Fill Hole, User Defined.  
             
         
        """
        pass
    @property
    def TargetType(self) -> FillHoleBuilder.TargetTypes:
        """
        Getter for property: ( FillHoleBuilder.TargetTypes NXOpe) TargetType
         Returns the hole target type when filling holes.  
             
         
        """
        pass
    @TargetType.setter
    def TargetType(self, target_type: FillHoleBuilder.TargetTypes):
        """
        Setter for property: ( FillHoleBuilder.TargetTypes NXOpe) TargetType
         Returns the hole target type when filling holes.  
             
         
        """
        pass
    @property
    def Type(self) -> FillHoleBuilder.Types:
        """
        Getter for property: ( FillHoleBuilder.Types NXOpe) Type
         Returns the hole filling type.  
             
         
        """
        pass
    @Type.setter
    def Type(self, type: FillHoleBuilder.Types):
        """
        Setter for property: ( FillHoleBuilder.Types NXOpe) Type
         Returns the hole filling type.  
             
         
        """
        pass
    def ClearHoleFills(self) -> None:
        """
         Cleans up local meshes associated with each fill. 
        """
        pass
    def ClearHoles(self) -> None:
        """
         Removes all holes, deletes associated hole polylines. 
        """
        pass
    def FillHoles(self, globalUpdate: bool) -> NXOpen.DisplayableObject:
        """
         Fills targeted holes. 
         Returns newFacetBody ( NXOpen.DisplayableObject):  updated input facet body .
        """
        pass
    def FindHoles(self) -> None:
        """
         Locates holes in the mesh and creates polylines around them. 
        """
        pass
    def GetAllHoles(self) -> List[NXOpen.DisplayableObject]:
        """
         Gets a list of all holes (represented by polylines). 
         Returns holeCurveTags ( NXOpen.DisplayableObject Li):  Hole polylines. .
        """
        pass
    def GetHoleByIndex(self, index: int) -> NXOpen.ICurve:
        """
         Gets a hole given an index into the list of holes. 
         Returns holeAtIndex ( NXOpen.ICurve):  Equals  if not found .
        """
        pass
    def GetHoleFillsOnly(self) -> NXOpen.DisplayableObject:
        """
         Builds a facet body that contains only the facets of the filled holes.
         Returns facetBodyResult ( NXOpen.DisplayableObject):  the fill facet body .
        """
        pass
    def GetNumberOfHoles(self) -> int:
        """
         Gets the number of holes in the target facet body. 
         Returns numberOfHoles (int): .
        """
        pass
    def GetTargetHolesByEdgeNumber(self, numMaxEdges: int) -> List[NXOpen.DisplayableObject]:
        """
         Gets a list of targeted holes (represented by polylines) based on number of edges. 
         Returns holeCurveTags ( NXOpen.DisplayableObject Li):  Hole polylines. .
        """
        pass
    def SwitchHoleFillType(self) -> None:
        """
         Switches boundary edge mapping based on the filling type (holes, island, bridge)
                    When filling holes or islands, each hole is defined by a polyline.  When bridging holes,
                    each individual open edge has its own polyline.
                
        """
        pass
import NXOpen
class FillMeshBuilder(NXOpen.Builder): 
    """ This function fills one or more holes in the selected facet bodies to make convergent bodies solid  """
    class EdgeOptionMenu(Enum):
        """
        Members Include: 
         |All| 
         |UserSelected| 
         |ByNumberofEdges| 

        """
        All: int
        UserSelected: int
        ByNumberofEdges: int
        @staticmethod
        def ValueOf(value: int) -> FillMeshBuilder.EdgeOptionMenu:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SmoothnessOptionMenu(Enum):
        """
        Members Include: 
         |Linear| 
         |Refined| 
         |TangentBased| 
         |CurvatureBased| 

        """
        Linear: int
        Refined: int
        TangentBased: int
        CurvatureBased: int
        @staticmethod
        def ValueOf(value: int) -> FillMeshBuilder.SmoothnessOptionMenu:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |FillHole| 
         |CloseNotch| 
         |FillIsland| 
         |ConnectHoles| 
         |BridgeGap| 

        """
        FillHole: int
        CloseNotch: int
        FillIsland: int
        ConnectHoles: int
        BridgeGap: int
        @staticmethod
        def ValueOf(value: int) -> FillMeshBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FacetVertexData:
        """
         Contains facet vertex information. 
         FillMeshBuilderFacetVertexData_Struct NXOpe is an alias for  FillMeshBuilder.FacetVertexData NXOpe.
        """
        @property
        def Face(self) -> NXOpen.NXObject:
            """
            Getter for property Face
            The face that facet belongs to.

            """
            pass
        @Face.setter
        def Face(self, value: NXOpen.NXObject):
            """
            Getter for property Face
            The face that facet belongs to.
            Setter for property Face
            The face that facet belongs to.

            """
            pass
        @property
        def NxFacetIndex(self) -> int:
            """
            Getter for property NxFacetIndex
            The facet index for NX facet body.

            """
            pass
        @NxFacetIndex.setter
        def NxFacetIndex(self, value: int):
            """
            Getter for property NxFacetIndex
            The facet index for NX facet body.
            Setter for property NxFacetIndex
            The facet index for NX facet body.

            """
            pass
        @property
        def PointCoord(self) -> NXOpen.Point3d:
            """
            Getter for property PointCoord
            The 3d point location on the facet body.

            """
            pass
        @PointCoord.setter
        def PointCoord(self, value: NXOpen.Point3d):
            """
            Getter for property PointCoord
            The 3d point location on the facet body.
            Setter for property PointCoord
            The 3d point location on the facet body.

            """
            pass
    @property
    def EdgeHole(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) EdgeHole
         Returns the edge hole   
            
         
        """
        pass
    @property
    def EdgeSelectionMethod(self) -> FillMeshBuilder.EdgeOptionMenu:
        """
        Getter for property: ( FillMeshBuilder.EdgeOptionMenu NXOpe) EdgeSelectionMethod
         Returns the edge selection method   
            
         
        """
        pass
    @EdgeSelectionMethod.setter
    def EdgeSelectionMethod(self, edgeSelectionMethod: FillMeshBuilder.EdgeOptionMenu):
        """
        Setter for property: ( FillMeshBuilder.EdgeOptionMenu NXOpe) EdgeSelectionMethod
         Returns the edge selection method   
            
         
        """
        pass
    @property
    def EditCopy(self) -> bool:
        """
        Getter for property: (bool) EditCopy
         Returns the edit copy   
            
         
        """
        pass
    @EditCopy.setter
    def EditCopy(self, editCopy: bool):
        """
        Setter for property: (bool) EditCopy
         Returns the edit copy   
            
         
        """
        pass
    @property
    def EndEdgeVertex1(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) EndEdgeVertex1
         Returns the end edge vertex1   
            
         
        """
        pass
    @EndEdgeVertex1.setter
    def EndEdgeVertex1(self, endEdgeVertex1: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) EndEdgeVertex1
         Returns the end edge vertex1   
            
         
        """
        pass
    @property
    def EndEdgeVertex2(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) EndEdgeVertex2
         Returns the end edge vertex2   
            
         
        """
        pass
    @EndEdgeVertex2.setter
    def EndEdgeVertex2(self, endEdgeVertex2: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) EndEdgeVertex2
         Returns the end edge vertex2   
            
         
        """
        pass
    @property
    def EndHole(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) EndHole
         Returns the end hole   
            
         
        """
        pass
    @property
    def FacetBodies(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) FacetBodies
         Returns the facet body   
            
         
        """
        pass
    @property
    def InnerHole(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) InnerHole
         Returns the inner hole   
            
         
        """
        pass
    @property
    def MaxEdges(self) -> int:
        """
        Getter for property: (int) MaxEdges
         Returns the max edges   
            
         
        """
        pass
    @MaxEdges.setter
    def MaxEdges(self, maxEdges: int):
        """
        Setter for property: (int) MaxEdges
         Returns the max edges   
            
         
        """
        pass
    @property
    def OuterHole(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) OuterHole
         Returns the outer hole   
            
         
        """
        pass
    @property
    def SmoothnessOption(self) -> FillMeshBuilder.SmoothnessOptionMenu:
        """
        Getter for property: ( FillMeshBuilder.SmoothnessOptionMenu NXOpe) SmoothnessOption
         Returns the smoothness option   
            
         
        """
        pass
    @SmoothnessOption.setter
    def SmoothnessOption(self, smoothnessOption: FillMeshBuilder.SmoothnessOptionMenu):
        """
        Setter for property: ( FillMeshBuilder.SmoothnessOptionMenu NXOpe) SmoothnessOption
         Returns the smoothness option   
            
         
        """
        pass
    @property
    def StartEdgeVertex1(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) StartEdgeVertex1
         Returns the start edge vertex1   
            
         
        """
        pass
    @StartEdgeVertex1.setter
    def StartEdgeVertex1(self, startEdgeVertex1: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) StartEdgeVertex1
         Returns the start edge vertex1   
            
         
        """
        pass
    @property
    def StartEdgeVertex2(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) StartEdgeVertex2
         Returns the start edge vertex2   
            
         
        """
        pass
    @StartEdgeVertex2.setter
    def StartEdgeVertex2(self, startEdgeVertex2: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) StartEdgeVertex2
         Returns the start edge vertex2   
            
         
        """
        pass
    @property
    def StartHole(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) StartHole
         Returns the start hole   
            
         
        """
        pass
    @property
    def Type(self) -> FillMeshBuilder.Types:
        """
        Getter for property: ( FillMeshBuilder.Types NXOpe) Type
         Returns the type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: FillMeshBuilder.Types):
        """
        Setter for property: ( FillMeshBuilder.Types NXOpe) Type
         Returns the type   
            
         
        """
        pass
    @property
    def TypeOfHole(self) -> FillMeshBuilder.Types:
        """
        Getter for property: ( FillMeshBuilder.Types NXOpe) TypeOfHole
         Returns the type of Hole   
            
         
        """
        pass
    @TypeOfHole.setter
    def TypeOfHole(self, type: FillMeshBuilder.Types):
        """
        Setter for property: ( FillMeshBuilder.Types NXOpe) TypeOfHole
         Returns the type of Hole   
            
         
        """
        pass
    @property
    def Vertex1(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Vertex1
         Returns the vertex1   
            
         
        """
        pass
    @Vertex1.setter
    def Vertex1(self, vertex1: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Vertex1
         Returns the vertex1   
            
         
        """
        pass
    @property
    def Vertex2(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Vertex2
         Returns the vertex2   
            
         
        """
        pass
    @Vertex2.setter
    def Vertex2(self, vertex2: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Vertex2
         Returns the vertex2   
            
         
        """
        pass
    def FlipRangeEnd(self) -> None:
        """
         Flips the end edge range 
        """
        pass
    def FlipRangeStart(self) -> None:
        """
         Flips the start edge range 
        """
        pass
    def SetBridgeGapEndEdgeVertex1(self, facetVertexData: FillMeshBuilder.FacetVertexData) -> None:
        """
         Sets first end edge vertex to bridge the gap. 
        """
        pass
    def SetBridgeGapEndEdgeVertex2(self, facetVertexData: FillMeshBuilder.FacetVertexData) -> None:
        """
         Sets second end edge vertex to bridge the gap. 
        """
        pass
    def SetBridgeGapStartEdgeVertex1(self, facetVertexData: FillMeshBuilder.FacetVertexData) -> None:
        """
         Sets first start edge vertex to bridge the gap. 
        """
        pass
    def SetBridgeGapStartEdgeVertex2(self, facetVertexData: FillMeshBuilder.FacetVertexData) -> None:
        """
         Sets second start edge vertex to bridge the gap. 
        """
        pass
    def SetCloseNotchVertex1(self, facetVertexData: FillMeshBuilder.FacetVertexData) -> None:
        """
         Sets first vertex to close the notch. 
        """
        pass
    def SetCloseNotchVertex2(self, facetVertexData: FillMeshBuilder.FacetVertexData) -> None:
        """
         Sets second vertex to close the notch. 
        """
        pass
    def UpdateHoles(self) -> None:
        """
         Update all the holes of the selected facet bodies. 
        """
        pass
import NXOpen
class LocalOffsetBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Facet.LocalOffsetBuilder.
        This class adds or removes material on facet bodies by creating local offsets."""
    class ShapeMethodType(Enum):
        """
        Members Include: 
         |Sharp|  Sharp specifies a transition region without smoothing.
         |Smooth|  Smooth specifies a transition region with smoothing.

        """
        Sharp: int
        Smooth: int
        @staticmethod
        def ValueOf(value: int) -> LocalOffsetBuilder.ShapeMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TransitionMethodType(Enum):
        """
        Members Include: 
         |NotSet|  None creates an offset without a transition region.
         |ByConstantOffset|  Constant offset creates a transition region of constant distance.
         |ByRegionSelection|  Region selection allows the user to select transtion regions.

        """
        NotSet: int
        ByConstantOffset: int
        ByRegionSelection: int
        @staticmethod
        def ValueOf(value: int) -> LocalOffsetBuilder.TransitionMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FacetRegion(self) -> NXOpen.FacetCollector:
        """
        Getter for property: ( NXOpen.FacetCollector) FacetRegion
         Returns the facets to be offset   
            
         
        """
        pass
    @property
    def FacetTransitionRegions(self) -> NXOpen.FacetCollector:
        """
        Getter for property: ( NXOpen.FacetCollector) FacetTransitionRegions
         Returns the user-selected transition regions   
            
         
        """
        pass
    @property
    def IsEditCopy(self) -> bool:
        """
        Getter for property: (bool) IsEditCopy
         Returns the option to create a non-associative copy of the selected body and edit that copy   
            
         
        """
        pass
    @IsEditCopy.setter
    def IsEditCopy(self, isEditCopy: bool):
        """
        Setter for property: (bool) IsEditCopy
         Returns the option to create a non-associative copy of the selected body and edit that copy   
            
         
        """
        pass
    @property
    def IsRegenerateOffsetMesh(self) -> bool:
        """
        Getter for property: (bool) IsRegenerateOffsetMesh
         Returns the option to rebuild the mesh structure of the offset output   
            
         
        """
        pass
    @IsRegenerateOffsetMesh.setter
    def IsRegenerateOffsetMesh(self, isRegenerateOffsetMesh: bool):
        """
        Setter for property: (bool) IsRegenerateOffsetMesh
         Returns the option to rebuild the mesh structure of the offset output   
            
         
        """
        pass
    @property
    def IsReverseDirection(self) -> bool:
        """
        Getter for property: (bool) IsReverseDirection
         Returns the method to reverse the direction of the offset.  
             
         
        """
        pass
    @IsReverseDirection.setter
    def IsReverseDirection(self, isReverseDirection: bool):
        """
        Setter for property: (bool) IsReverseDirection
         Returns the method to reverse the direction of the offset.  
             
         
        """
        pass
    @property
    def IsSmoothEdge(self) -> bool:
        """
        Getter for property: (bool) IsSmoothEdge
         Returns the option to add smoothing to the edge of the offset region   
            
         
        """
        pass
    @IsSmoothEdge.setter
    def IsSmoothEdge(self, isSmoothEdge: bool):
        """
        Setter for property: (bool) IsSmoothEdge
         Returns the option to add smoothing to the edge of the offset region   
            
         
        """
        pass
    @property
    def OffsetDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OffsetDistance
         Returns the linear distance of the created local offset, which may be a positive or negative distance   
            
         
        """
        pass
    @property
    def RegionDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RegionDistance
         Returns the distance of the transition region with the constant offset option   
            
         
        """
        pass
    @property
    def ShapeMethod(self) -> LocalOffsetBuilder.ShapeMethodType:
        """
        Getter for property: ( LocalOffsetBuilder.ShapeMethodType NXOpe) ShapeMethod
         Returns the method to define the shape of the transition region   
            
         
        """
        pass
    @ShapeMethod.setter
    def ShapeMethod(self, shapeMethod: LocalOffsetBuilder.ShapeMethodType):
        """
        Setter for property: ( LocalOffsetBuilder.ShapeMethodType NXOpe) ShapeMethod
         Returns the method to define the shape of the transition region   
            
         
        """
        pass
    @property
    def TransitionMethod(self) -> LocalOffsetBuilder.TransitionMethodType:
        """
        Getter for property: ( LocalOffsetBuilder.TransitionMethodType NXOpe) TransitionMethod
         Returns the type of transition region   
            
         
        """
        pass
    @TransitionMethod.setter
    def TransitionMethod(self, transitionMethod: LocalOffsetBuilder.TransitionMethodType):
        """
        Setter for property: ( LocalOffsetBuilder.TransitionMethodType NXOpe) TransitionMethod
         Returns the type of transition region   
            
         
        """
        pass
import NXOpen
class MergeFacetBodyBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Facet.MergeFacetBodyBuilder
    It merges two overlapping NX facet bodies. It returns a new mergered NX facet body. The two input bodies
    can be kept, deleted or hidden.
    """
    class Input(Enum):
        """
        Members Include: 
         |Keep|  Keep the input facet body after builder committing 
         |Delete|  Delete the input facet body after builder committing 
         |Hide|  Hide the input facet body after builder committing 

        """
        Keep: int
        Delete: int
        Hide: int
        @staticmethod
        def ValueOf(value: int) -> MergeFacetBodyBuilder.Input:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngleTolerance(self) -> float:
        """
        Getter for property: (float) AngleTolerance
         Returns the angle tolerance used in the merge facet body feature   
            
         
        """
        pass
    @AngleTolerance.setter
    def AngleTolerance(self, angleTolerance: float):
        """
        Setter for property: (float) AngleTolerance
         Returns the angle tolerance used in the merge facet body feature   
            
         
        """
        pass
    @property
    def ChordHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ChordHeight
         Returns the chord height to control the size of new facets   
            
         
        """
        pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance used in the merge facet body feature   
            
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance used in the merge facet body feature   
            
         
        """
        pass
    @property
    def EdgeLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EdgeLength
         Returns the edge length to control the size of new facets   
            
         
        """
        pass
    @property
    def FacetBodyOne(self) -> SelectFacetedBody:
        """
        Getter for property: ( SelectFacetedBody NXOpe) FacetBodyOne
         Returns the first NX facet body to be merged   
            
         
        """
        pass
    @property
    def FacetBodyTwo(self) -> SelectFacetedBody:
        """
        Getter for property: ( SelectFacetedBody NXOpe) FacetBodyTwo
         Returns the second NX facet body to be merged   
            
         
        """
        pass
    @property
    def InputStatus(self) -> MergeFacetBodyBuilder.Input:
        """
        Getter for property: ( MergeFacetBodyBuilder.Input NXOpe) InputStatus
         Returns the option to specify how to deal with the input two facet bodies: keep, delete or hide   
            
         
        """
        pass
    @InputStatus.setter
    def InputStatus(self, inputStatus: MergeFacetBodyBuilder.Input):
        """
        Setter for property: ( MergeFacetBodyBuilder.Input NXOpe) InputStatus
         Returns the option to specify how to deal with the input two facet bodies: keep, delete or hide   
            
         
        """
        pass
import NXOpen
class MergeFacetFacesBuilder(NXOpen.Builder): 
    """
    Represents a Facet.MergeFacetFacesBuilder builder
    """
    @property
    def FaceCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FaceCollector
         Returns the face collector   
            
         
        """
        pass
    @property
    def IsEditCopy(self) -> bool:
        """
        Getter for property: (bool) IsEditCopy
         Returns the value indicating if a copy of the facet body to be used for Merge facet faces without altering the original   
            
         
        """
        pass
    @IsEditCopy.setter
    def IsEditCopy(self, isEditCopy: bool):
        """
        Setter for property: (bool) IsEditCopy
         Returns the value indicating if a copy of the facet body to be used for Merge facet faces without altering the original   
            
         
        """
        pass
import NXOpen
class MeshFromCloudBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Facet.MeshFromCloudBuilder
    Creates a convergent body from point clouds. The point cloud data source
    can be either a file or existing points within the part file.
    """
    class ModeOption(Enum):
        """
        Members Include: 
         |UniformDensity|  Uniform vertex density. 
         |VariableDensity|  uniform vertex density in planar areas with increased density in curvy areas. 
         |KeepAllPoints|  Preserve input points to create corresponding vertices. 

        """
        UniformDensity: int
        VariableDensity: int
        KeepAllPoints: int
        @staticmethod
        def ValueOf(value: int) -> MeshFromCloudBuilder.ModeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SourceOption(Enum):
        """
        Members Include: 
         |FromFile| 
         |ExistingPoints| 

        """
        FromFile: int
        ExistingPoints: int
        @staticmethod
        def ValueOf(value: int) -> MeshFromCloudBuilder.SourceOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AnalyzeMeshQuality(self) -> bool:
        """
        Getter for property: (bool) AnalyzeMeshQuality
         Returns the value used to determine if analyzing the quality of the mesh or not.  
             
         
        """
        pass
    @AnalyzeMeshQuality.setter
    def AnalyzeMeshQuality(self, analyzeMeshQuality: bool):
        """
        Setter for property: (bool) AnalyzeMeshQuality
         Returns the value used to determine if analyzing the quality of the mesh or not.  
             
         
        """
        pass
    @property
    def ModeOptions(self) -> MeshFromCloudBuilder.ModeOption:
        """
        Getter for property: ( MeshFromCloudBuilder.ModeOption NXOpe) ModeOptions
         Returns the option controlling distribution of vertices in the output convergent body.  
             
         
        """
        pass
    @ModeOptions.setter
    def ModeOptions(self, modeOptions: MeshFromCloudBuilder.ModeOption):
        """
        Setter for property: ( MeshFromCloudBuilder.ModeOption NXOpe) ModeOptions
         Returns the option controlling distribution of vertices in the output convergent body.  
             
         
        """
        pass
    @property
    def NeighborhoodSize(self) -> float:
        """
        Getter for property: (float) NeighborhoodSize
         Returns the value used to determine neighboring points when creating a body.  
             
         
        """
        pass
    @NeighborhoodSize.setter
    def NeighborhoodSize(self, neighborhoodSize: float):
        """
        Setter for property: (float) NeighborhoodSize
         Returns the value used to determine neighboring points when creating a body.  
             
         
        """
        pass
    @property
    def PointFile(self) -> str:
        """
        Getter for property: (str) PointFile
         Returns the point cloud file.  
             
         
        """
        pass
    @PointFile.setter
    def PointFile(self, filename: str):
        """
        Setter for property: (str) PointFile
         Returns the point cloud file.  
             
         
        """
        pass
    @property
    def SelectPoints(self) -> NXOpen.SelectPointList:
        """
        Getter for property: ( NXOpen.SelectPointList) SelectPoints
         Returns the point cloud.  
             
         
        """
        pass
    @property
    def SmoothingFactor(self) -> int:
        """
        Getter for property: (int) SmoothingFactor
         Returns the value indicating smoothing factor.  
           The value can be between 0 and 100, with high value indicating higher smoothing.   
         
        """
        pass
    @SmoothingFactor.setter
    def SmoothingFactor(self, smoothingFactor: int):
        """
        Setter for property: (int) SmoothingFactor
         Returns the value indicating smoothing factor.  
           The value can be between 0 and 100, with high value indicating higher smoothing.   
         
        """
        pass
    @property
    def SourceOptions(self) -> MeshFromCloudBuilder.SourceOption:
        """
        Getter for property: ( MeshFromCloudBuilder.SourceOption NXOpe) SourceOptions
         Returns the option indicating the source of point cloud.  
             
         
        """
        pass
    @SourceOptions.setter
    def SourceOptions(self, sourceOptions: MeshFromCloudBuilder.SourceOption):
        """
        Setter for property: ( MeshFromCloudBuilder.SourceOption NXOpe) SourceOptions
         Returns the option indicating the source of point cloud.  
             
         
        """
        pass
    @property
    def TargetVertexNumber(self) -> int:
        """
        Getter for property: (int) TargetVertexNumber
         Returns the value indicating the desired number of vertices in the output body.  
             
         
        """
        pass
    @TargetVertexNumber.setter
    def TargetVertexNumber(self, targetVertexNumber: int):
        """
        Setter for property: (int) TargetVertexNumber
         Returns the value indicating the desired number of vertices in the output body.  
             
         
        """
        pass
    @property
    def TessellationPercentage(self) -> float:
        """
        Getter for property: (float) TessellationPercentage
         Returns the value as a percentage ratio of number of output vertices to the number of input points.  
             
         
        """
        pass
    @TessellationPercentage.setter
    def TessellationPercentage(self, tessellationPercentage: float):
        """
        Setter for property: (float) TessellationPercentage
         Returns the value as a percentage ratio of number of output vertices to the number of input points.  
             
         
        """
        pass
    def SuggestNeighborhoodSize(self) -> None:
        """
         Determines NXOpen.Facet.MeshFromCloudBuilder.NeighborhoodSize for a given point cloud data. 
        """
        pass
import NXOpen
class MultiPatchAlignmentBuilder(NXOpen.Builder): 
    """ Aligns multiple facet bodies to one another without using reference points. """
    class ResolutionType(Enum):
        """
        Members Include: 
         |High|  Uses a high number of facets for the alignment. 
         |Medium|  Uses a medium number of facets for the alignment. 
         |Low|  Uses a low number of facets for the alignment. 

        """
        High: int
        Medium: int
        Low: int
        @staticmethod
        def ValueOf(value: int) -> MultiPatchAlignmentBuilder.ResolutionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AlignFacetPatches(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) AlignFacetPatches
         Returns the facet bodies to be aligned.  
           Inputs to this command can be convergent objects.   
         
        """
        pass
    @property
    def AlignmentBodies(self) -> SelectFacetedBodyList:
        """
        Getter for property: ( SelectFacetedBodyList NXOpe) AlignmentBodies
         Returns the facet bodies to be aligned.  
             
         
        """
        pass
    @property
    def Iteration(self) -> int:
        """
        Getter for property: (int) Iteration
         Returns the value indicating the number of times the alignment algorithm is applied.  
           
                    Many iterations improve alignment accuracy but take longer.   
         
        """
        pass
    @Iteration.setter
    def Iteration(self, iteration: int):
        """
        Setter for property: (int) Iteration
         Returns the value indicating the number of times the alignment algorithm is applied.  
           
                    Many iterations improve alignment accuracy but take longer.   
         
        """
        pass
    @property
    def MaximumCheckingDistance(self) -> float:
        """
        Getter for property: (float) MaximumCheckingDistance
         Returns the distance facets may be from one another in order to be used 
                    in the alignment.  
           Larger numbers slow the alignment process.   
         
        """
        pass
    @MaximumCheckingDistance.setter
    def MaximumCheckingDistance(self, maximumCheckingDistance: float):
        """
        Setter for property: (float) MaximumCheckingDistance
         Returns the distance facets may be from one another in order to be used 
                    in the alignment.  
           Larger numbers slow the alignment process.   
         
        """
        pass
    @property
    def ReferenceFacetPatches(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) ReferenceFacetPatches
         Returns an optional reference facet body.  
           Inputs to this command can be convergent objects.   
         
        """
        pass
    @property
    def ReferencePatches(self) -> SelectFacetedBodyList:
        """
        Getter for property: ( SelectFacetedBodyList NXOpe) ReferencePatches
         Returns an optional reference facet body with a location and orientation that will 
                    remain fixed, causing all of the other selected facet bodies to align with 
                    it.  
           If you do not select a reference body, all of the selected facet bodies 
                    will align to each other, without a fixed location.   
         
        """
        pass
    @property
    def Resolution(self) -> MultiPatchAlignmentBuilder.ResolutionType:
        """
        Getter for property: ( MultiPatchAlignmentBuilder.ResolutionType NXOpe) Resolution
         Returns the type indicating number of facets to be used  in the alignment.  
             
         
        """
        pass
    @Resolution.setter
    def Resolution(self, resolution: MultiPatchAlignmentBuilder.ResolutionType):
        """
        Setter for property: ( MultiPatchAlignmentBuilder.ResolutionType NXOpe) Resolution
         Returns the type indicating number of facets to be used  in the alignment.  
             
         
        """
        pass
    @property
    def Tolerance(self) -> float:
        """
        Getter for property: (float) Tolerance
         Returns the precision of the alignment.  
          
                    Alignment will complete when tolerance is met or the number of iterations has been reached.   
         
        """
        pass
    @Tolerance.setter
    def Tolerance(self, tolerance: float):
        """
        Setter for property: (float) Tolerance
         Returns the precision of the alignment.  
          
                    Alignment will complete when tolerance is met or the number of iterations has been reached.   
         
        """
        pass
import NXOpen
class PaintBrushBuilder(NXOpen.Builder): 
    """
       This class manages the paint brush utility for a facet body.
    """
    def ClearThePaintPath(self) -> None:
        """
         Clears the paint path 
        """
        pass
    def GetPaintBrushColor(self) -> List[float]:
        """
         Returns the paint brush color 
         Returns paintBrushColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def PaintVertexColor(self, position: NXOpen.Point3d) -> None:
        """
         Paints facet body vertex color 
        """
        pass
    def SetBodyBeingPainted(self, body: NXOpen.DisplayableObject) -> None:
        """
         Sets facet body being painted. Inputs to this command can be convergent objects. 
        """
        pass
    def SetFacetBeingPainted(self, facet: FacetedBody) -> None:
        """
         Sets facet body being painted. 
        """
        pass
    def SetPaintBrushColor(self, paintBrushColor: List[float]) -> None:
        """
         Sets the paint brush color 
        """
        pass
    def SetTemporaryFacetDisplay(self, tempDisplay: bool) -> None:
        """
         Flag to use temporary facet display 
        """
        pass
    def SetupPaintFacetBody(self) -> None:
        """
         Setup the paint facet body 
        """
        pass
import NXOpen
class PaintFacetBodyBuilder(NXOpen.Builder): 
    """
       This class manages the color painting on a facet body.
    """
    @property
    def FacetCollector(self) -> NXOpen.FacetCollector:
        """
        Getter for property: ( NXOpen.FacetCollector) FacetCollector
         Returns a collector of facets on the facet bodies to be to be tested.  
             
         
        """
        pass
    @property
    def InheritBodyColorPick(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: ( NXOpen.SelectDisplayableObject) InheritBodyColorPick
         Returns the inherit color pick.  
           Inputs to this command can be convergent objects.   
         
        """
        pass
    @property
    def InheritColorPick(self) -> SelectFacetedBody:
        """
        Getter for property: ( SelectFacetedBody NXOpe) InheritColorPick
         Returns the inherit color pick   
            
         
        """
        pass
    @property
    def PaintBrush(self) -> PaintBrushBuilder:
        """
        Getter for property: ( PaintBrushBuilder NXOpe) PaintBrush
         Returns the paint brush   
            
         
        """
        pass
    @property
    def PaintBrushSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PaintBrushSize
         Returns the paint brush size   
            
         
        """
        pass
    def GetPaintBrushColor(self) -> List[float]:
        """
         Returns the paint brush color 
         Returns paintBrushColor (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def PaintBodiesBackgroundColor(self, bodies: List[NXOpen.DisplayableObject]) -> None:
        """
         Paints facets background color. Inputs to this command can be convergent objects.
        """
        pass
    def PaintFacetsBackGroundColor(self, facets: List[FacetedBody]) -> None:
        """
         Paints facets background color 
        """
        pass
    def PaintSelectedFacets(self) -> None:
        """
         Paints selected facets. 
        """
        pass
    def SetPaintBrushColor(self, paintBrushColor: List[float]) -> None:
        """
         Sets the paint brush color 
        """
        pass
    def SetupBodyColorData(self, bodies: List[NXOpen.DisplayableObject]) -> None:
        """
         Setup color data. Inputs to this command can be convergent objects. 
        """
        pass
    def SetupColorData(self, facets: List[FacetedBody]) -> None:
        """
         Setup color data 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class PlugLeakageBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Facet.PlugLeakageBuilder
        that identifies holes in facet bodies and covers the holes with newly created facet bodies."""
    @property
    def HoleMinimumSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) HoleMinimumSize
         Returns the minimum size of hole to be detected  
            
         
        """
        pass
    @property
    def InnerPoint(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) InnerPoint
         Returnsthe inner point   
            
         
        """
        pass
    @InnerPoint.setter
    def InnerPoint(self, innerPoint: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) InnerPoint
         Returnsthe inner point   
            
         
        """
        pass
    @property
    def InputBodyCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) InputBodyCollector
         Returns the input body collector  
            
         
        """
        pass
    @property
    def OuterPoint(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) OuterPoint
         Returnsthe outer point  
            
         
        """
        pass
    @OuterPoint.setter
    def OuterPoint(self, outerPoint: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) OuterPoint
         Returnsthe outer point  
            
         
        """
        pass
    @property
    def RegionList(self) -> NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList:
        """
        Getter for property: ( NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList) RegionList
         Returnsthe boundaries that are defined to patch the holes.  
            
         
        """
        pass
    def CreatePatch(self) -> None:
        """
        Creates a patch defined by the boundary.
        """
        pass
    def FindPath(self) -> None:
        """
         Finds the path that goes through the holes, starting from 
                NXOpen.Facet.PlugLeakageBuilder.InnerPoint and ending at 
                NXOpen.Facet.PlugLeakageBuilder.OuterPoint.
        """
        pass
import NXOpen
class PolygonModelingBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Facet.PolygonModelingBuilder builder. 
    """
    class ConvertTypes(Enum):
        """
        Members Include: 
         |Convergent| 
         |Facet| 

        """
        Convergent: int
        Facet: int
        @staticmethod
        def ValueOf(value: int) -> PolygonModelingBuilder.ConvertTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ConvertType(self) -> PolygonModelingBuilder.ConvertTypes:
        """
        Getter for property: ( PolygonModelingBuilder.ConvertTypes NXOpe) ConvertType
         Returns the convert type   
            
         
        """
        pass
    @ConvertType.setter
    def ConvertType(self, convertType: PolygonModelingBuilder.ConvertTypes):
        """
        Setter for property: ( PolygonModelingBuilder.ConvertTypes NXOpe) ConvertType
         Returns the convert type   
            
         
        """
        pass
    @property
    def EditCopy(self) -> bool:
        """
        Getter for property: (bool) EditCopy
         Returns the option to create a non-associative copy of the selected body and edit that copy   
            
         
        """
        pass
    @EditCopy.setter
    def EditCopy(self, isEditCopy: bool):
        """
        Setter for property: (bool) EditCopy
         Returns the option to create a non-associative copy of the selected body and edit that copy   
            
         
        """
        pass
    @property
    def SelectFacetBodies(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SelectFacetBodies
         Returns the selected bodies   
            
         
        """
        pass
    def MergeAllFaces(self, bodyTag: NXOpen.Body) -> None:
        """
         Merges all faces of the input body
        """
        pass
    def RemoveParameterOfBody(self, bodyTag: NXOpen.Body) -> None:
        """
         Removes the parameters of the input body
        """
        pass
import NXOpen
class RemeshFacetBodyBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Facet.RemeshFacetBodyBuilder.
        This class remeshes selected facet regions to specified density."""
    class RemeshModeType(Enum):
        """
        Members Include: 
         |Constant| 
         |Variable| 

        """
        Constant: int
        Variable: int
        @staticmethod
        def ValueOf(value: int) -> RemeshFacetBodyBuilder.RemeshModeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SharpEdgesLockType(Enum):
        """
        Members Include: 
         |NoLock| 
         |SoftLock| 
         |HardLock| 

        """
        NoLock: int
        SoftLock: int
        HardLock: int
        @staticmethod
        def ValueOf(value: int) -> RemeshFacetBodyBuilder.SharpEdgesLockType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngularThreshold(self) -> float:
        """
        Getter for property: (float) AngularThreshold
         Returns the AngularThreshold for remesh  
            
         
        """
        pass
    @AngularThreshold.setter
    def AngularThreshold(self, angularThreshold: float):
        """
        Setter for property: (float) AngularThreshold
         Returns the AngularThreshold for remesh  
            
         
        """
        pass
    @property
    def AverageSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) AverageSize
         Returns the AverageSize for remesh  
            
         
        """
        pass
    @property
    def ChordalTolerance(self) -> float:
        """
        Getter for property: (float) ChordalTolerance
         Returns the ChordalTolerance for remesh  
            
         
        """
        pass
    @ChordalTolerance.setter
    def ChordalTolerance(self, chordalTolerance: float):
        """
        Setter for property: (float) ChordalTolerance
         Returns the ChordalTolerance for remesh  
            
         
        """
        pass
    @property
    def FacetRegion(self) -> NXOpen.FacetCollector:
        """
        Getter for property: ( NXOpen.FacetCollector) FacetRegion
         Returns the facets to be remeshed   
            
         
        """
        pass
    @property
    def IsEditCopy(self) -> bool:
        """
        Getter for property: (bool) IsEditCopy
         Returns the option to create a non-associative copy of the selected body and edit that copy   
            
         
        """
        pass
    @IsEditCopy.setter
    def IsEditCopy(self, isEditCopy: bool):
        """
        Setter for property: (bool) IsEditCopy
         Returns the option to create a non-associative copy of the selected body and edit that copy   
            
         
        """
        pass
    @property
    def IsLockBoundary(self) -> bool:
        """
        Getter for property: (bool) IsLockBoundary
         Returns the option to lock boundary of remesh regions   
            
         
        """
        pass
    @IsLockBoundary.setter
    def IsLockBoundary(self, isLockBoundary: bool):
        """
        Setter for property: (bool) IsLockBoundary
         Returns the option to lock boundary of remesh regions   
            
         
        """
        pass
    @property
    def IsShowDeviationPlot(self) -> bool:
        """
        Getter for property: (bool) IsShowDeviationPlot
         Returns the option to show deviation plot   
            
         
        """
        pass
    @IsShowDeviationPlot.setter
    def IsShowDeviationPlot(self, isShowDeviationPlot: bool):
        """
        Setter for property: (bool) IsShowDeviationPlot
         Returns the option to show deviation plot   
            
         
        """
        pass
    @property
    def MaximumSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumSize
         Returns the MaximumSize for remesh  
            
         
        """
        pass
    @property
    def RemeshMode(self) -> RemeshFacetBodyBuilder.RemeshModeType:
        """
        Getter for property: ( RemeshFacetBodyBuilder.RemeshModeType NXOpe) RemeshMode
         Returns the Mode for remesh  
            
         
        """
        pass
    @RemeshMode.setter
    def RemeshMode(self, remeshMode: RemeshFacetBodyBuilder.RemeshModeType):
        """
        Setter for property: ( RemeshFacetBodyBuilder.RemeshModeType NXOpe) RemeshMode
         Returns the Mode for remesh  
            
         
        """
        pass
    @property
    def SharpEdgesLockOption(self) -> RemeshFacetBodyBuilder.SharpEdgesLockType:
        """
        Getter for property: ( RemeshFacetBodyBuilder.SharpEdgesLockType NXOpe) SharpEdgesLockOption
         Returns the Option for sharp edges lock type  
            
         
        """
        pass
    @SharpEdgesLockOption.setter
    def SharpEdgesLockOption(self, sharpEdgesLockType: RemeshFacetBodyBuilder.SharpEdgesLockType):
        """
        Setter for property: ( RemeshFacetBodyBuilder.SharpEdgesLockType NXOpe) SharpEdgesLockOption
         Returns the Option for sharp edges lock type  
            
         
        """
        pass
import NXOpen
class ReplaceMeshWithFaceBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Facet.ReplaceMeshWithFaceBuilder.
    Replace Mesh With Face Builder is a function to facilitate the creation of prismatic faces 
    through selected facet regions and replace that facet region with the analytic face. """
    class ConeConstraint(Enum):
        """
        Members Include: 
         |NotSet|  None constraint for cone 
         |Parallel|  Parallel constraint for cone 
         |Colinear|  Colinear constraint for cone 
         |AverageParallel|  AverageParallel constraint for cone 
         |AverageColinear|  AverageColinear constraint for cone 

        """
        NotSet: int
        Parallel: int
        Colinear: int
        AverageParallel: int
        AverageColinear: int
        @staticmethod
        def ValueOf(value: int) -> ReplaceMeshWithFaceBuilder.ConeConstraint:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CylinderConstraint(Enum):
        """
        Members Include: 
         |NotSet|  None constraint for cylinder 
         |Parallel|  Parallel constraint for cylinder 
         |Colinear|  Colinear constraint for cylinder 
         |AverageParallel|  AverageParallel constraint for cylinder 
         |AverageColinear|  AverageColinear constraint for cylinder 

        """
        NotSet: int
        Parallel: int
        Colinear: int
        AverageParallel: int
        AverageColinear: int
        @staticmethod
        def ValueOf(value: int) -> ReplaceMeshWithFaceBuilder.CylinderConstraint:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PlaneConstraint(Enum):
        """
        Members Include: 
         |NotSet|  None constraint for plane 
         |Orthogonal|  Orthogonal constraint for plane 
         |Parallel|  Parallel constraint for plane 
         |Coplanar|  Coplanar constraint for plane 
         |AverageParallel|  AverageParallel constraint for plane 
         |AverageCoplanar|  AverageCoplanar constraint for plane 

        """
        NotSet: int
        Orthogonal: int
        Parallel: int
        Coplanar: int
        AverageParallel: int
        AverageCoplanar: int
        @staticmethod
        def ValueOf(value: int) -> ReplaceMeshWithFaceBuilder.PlaneConstraint:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ReplaceMeshOnOption(Enum):
        """
        Members Include: 
         |OriginalBody|  Replace mesh on original body
         |NewBody|  Replace mesh on new body 

        """
        OriginalBody: int
        NewBody: int
        @staticmethod
        def ValueOf(value: int) -> ReplaceMeshWithFaceBuilder.ReplaceMeshOnOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SphereConstraint(Enum):
        """
        Members Include: 
         |NotSet|  None constraint for sphere 
         |Concentric|  Concentric constraint for sphere 
         |AverageConcentric|  AverageConcentric constraint for sphere 

        """
        NotSet: int
        Concentric: int
        AverageConcentric: int
        @staticmethod
        def ValueOf(value: int) -> ReplaceMeshWithFaceBuilder.SphereConstraint:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |Plane|  Divide facet face to fit the plane 
         |Cylinder|  Divide facet face to fit the cylinder 
         |Cone|  Divide facet face to fit the cone 
         |Sphere|  Divide facet face to fit the sphere 

        """
        Plane: int
        Cylinder: int
        Cone: int
        Sphere: int
        @staticmethod
        def ValueOf(value: int) -> ReplaceMeshWithFaceBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ConeAverageConstrainToDirectionToggle(self) -> bool:
        """
        Getter for property: (bool) ConeAverageConstrainToDirectionToggle
         Returns the cone average constrain to direction toggle   
            
         
        """
        pass
    @ConeAverageConstrainToDirectionToggle.setter
    def ConeAverageConstrainToDirectionToggle(self, coneAverageConstrainToDirectionToggle: bool):
        """
        Setter for property: (bool) ConeAverageConstrainToDirectionToggle
         Returns the cone average constrain to direction toggle   
            
         
        """
        pass
    @property
    def ConeAverageConstrainToDirectionVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ConeAverageConstrainToDirectionVector
         Returns the cone average constrain to direction vector   
            
         
        """
        pass
    @ConeAverageConstrainToDirectionVector.setter
    def ConeAverageConstrainToDirectionVector(self, coneAverageConstrainToDirectionVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ConeAverageConstrainToDirectionVector
         Returns the cone average constrain to direction vector   
            
         
        """
        pass
    @property
    def ConeColinearConstraintAxis(self) -> NXOpen.Axis:
        """
        Getter for property: ( NXOpen.Axis) ConeColinearConstraintAxis
         Returns the cone colinear constraint axis   
            
         
        """
        pass
    @ConeColinearConstraintAxis.setter
    def ConeColinearConstraintAxis(self, coneColinearConstraintAxis: NXOpen.Axis):
        """
        Setter for property: ( NXOpen.Axis) ConeColinearConstraintAxis
         Returns the cone colinear constraint axis   
            
         
        """
        pass
    @property
    def ConeConstraintTypes(self) -> ReplaceMeshWithFaceBuilder.ConeConstraint:
        """
        Getter for property: ( ReplaceMeshWithFaceBuilder.ConeConstraint NXOpe) ConeConstraintTypes
         Returns the cone constraint types   
            
         
        """
        pass
    @ConeConstraintTypes.setter
    def ConeConstraintTypes(self, coneConstraintTypes: ReplaceMeshWithFaceBuilder.ConeConstraint):
        """
        Setter for property: ( ReplaceMeshWithFaceBuilder.ConeConstraint NXOpe) ConeConstraintTypes
         Returns the cone constraint types   
            
         
        """
        pass
    @property
    def ConeHalfAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ConeHalfAngle
         Returns the cone half angle   
            
         
        """
        pass
    @property
    def ConeParallelConstraintVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ConeParallelConstraintVector
         Returns the cone parallel constraint vector   
            
         
        """
        pass
    @ConeParallelConstraintVector.setter
    def ConeParallelConstraintVector(self, coneParallelConstraintVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ConeParallelConstraintVector
         Returns the cone parallel constraint vector   
            
         
        """
        pass
    @property
    def CylinderAverageConstrainToDirectionToggle(self) -> bool:
        """
        Getter for property: (bool) CylinderAverageConstrainToDirectionToggle
         Returns the cylinder average constrain to direction toggle   
            
         
        """
        pass
    @CylinderAverageConstrainToDirectionToggle.setter
    def CylinderAverageConstrainToDirectionToggle(self, cylinderAverageConstrainToDirectionToggle: bool):
        """
        Setter for property: (bool) CylinderAverageConstrainToDirectionToggle
         Returns the cylinder average constrain to direction toggle   
            
         
        """
        pass
    @property
    def CylinderAverageConstrainToDirectionVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) CylinderAverageConstrainToDirectionVector
         Returns the cylinder average constrain to direction vector   
            
         
        """
        pass
    @CylinderAverageConstrainToDirectionVector.setter
    def CylinderAverageConstrainToDirectionVector(self, cylinderAverageConstrainToDirectionVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) CylinderAverageConstrainToDirectionVector
         Returns the cylinder average constrain to direction vector   
            
         
        """
        pass
    @property
    def CylinderColinearConstraintAxis(self) -> NXOpen.Axis:
        """
        Getter for property: ( NXOpen.Axis) CylinderColinearConstraintAxis
         Returns the cylinder colinear constraint axis   
            
         
        """
        pass
    @CylinderColinearConstraintAxis.setter
    def CylinderColinearConstraintAxis(self, cylinderColinearConstraintAxis: NXOpen.Axis):
        """
        Setter for property: ( NXOpen.Axis) CylinderColinearConstraintAxis
         Returns the cylinder colinear constraint axis   
            
         
        """
        pass
    @property
    def CylinderConstraintTypes(self) -> ReplaceMeshWithFaceBuilder.CylinderConstraint:
        """
        Getter for property: ( ReplaceMeshWithFaceBuilder.CylinderConstraint NXOpe) CylinderConstraintTypes
         Returns the cylinder constraint types   
            
         
        """
        pass
    @CylinderConstraintTypes.setter
    def CylinderConstraintTypes(self, cylinderConstraintTypes: ReplaceMeshWithFaceBuilder.CylinderConstraint):
        """
        Setter for property: ( ReplaceMeshWithFaceBuilder.CylinderConstraint NXOpe) CylinderConstraintTypes
         Returns the cylinder constraint types   
            
         
        """
        pass
    @property
    def CylinderOrSphereRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CylinderOrSphereRadius
         Returns the cylinder or sphere radius   
            
         
        """
        pass
    @property
    def CylinderParallelConstraintVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) CylinderParallelConstraintVector
         Returns the cylinder parallel constraint vector   
            
         
        """
        pass
    @CylinderParallelConstraintVector.setter
    def CylinderParallelConstraintVector(self, cylinderParallelConstraintVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) CylinderParallelConstraintVector
         Returns the cylinder parallel constraint vector   
            
         
        """
        pass
    @property
    def FacetCollector(self) -> NXOpen.FacetCollector:
        """
        Getter for property: ( NXOpen.FacetCollector) FacetCollector
         Returns the face collector   
            
         
        """
        pass
    @property
    def HalfAngleToggle(self) -> bool:
        """
        Getter for property: (bool) HalfAngleToggle
         Returns the half angle toggle   
            
         
        """
        pass
    @HalfAngleToggle.setter
    def HalfAngleToggle(self, halfAngleToggle: bool):
        """
        Setter for property: (bool) HalfAngleToggle
         Returns the half angle toggle   
            
         
        """
        pass
    @property
    def MaxDeviation(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxDeviation
         Returns the max deviation   
            
         
        """
        pass
    @property
    def MinimumFacetNumber(self) -> int:
        """
        Getter for property: (int) MinimumFacetNumber
         Returns the minimum facet number   
            
         
        """
        pass
    @MinimumFacetNumber.setter
    def MinimumFacetNumber(self, minimumFacetNumber: int):
        """
        Setter for property: (int) MinimumFacetNumber
         Returns the minimum facet number   
            
         
        """
        pass
    @property
    def OrthogonalOrCoplanarConstraintPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) OrthogonalOrCoplanarConstraintPlane
         Returns the orthogonal or coplanar constraint plane   
            
         
        """
        pass
    @OrthogonalOrCoplanarConstraintPlane.setter
    def OrthogonalOrCoplanarConstraintPlane(self, orthogonalOrCoplanarConstraintPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) OrthogonalOrCoplanarConstraintPlane
         Returns the orthogonal or coplanar constraint plane   
            
         
        """
        pass
    @property
    def PlaneAverageConstrainToNormalToggle(self) -> bool:
        """
        Getter for property: (bool) PlaneAverageConstrainToNormalToggle
         Returns the plane average constrain to normal toggle   
            
         
        """
        pass
    @PlaneAverageConstrainToNormalToggle.setter
    def PlaneAverageConstrainToNormalToggle(self, planeAverageConstrainToNormalToggle: bool):
        """
        Setter for property: (bool) PlaneAverageConstrainToNormalToggle
         Returns the plane average constrain to normal toggle   
            
         
        """
        pass
    @property
    def PlaneAverageConstrainToNormalVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) PlaneAverageConstrainToNormalVector
         Returns the plane average constrain to normal vector   
            
         
        """
        pass
    @PlaneAverageConstrainToNormalVector.setter
    def PlaneAverageConstrainToNormalVector(self, planeAverageConstrainToNormalVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) PlaneAverageConstrainToNormalVector
         Returns the plane average constrain to normal vector   
            
         
        """
        pass
    @property
    def PlaneConstraintTypes(self) -> ReplaceMeshWithFaceBuilder.PlaneConstraint:
        """
        Getter for property: ( ReplaceMeshWithFaceBuilder.PlaneConstraint NXOpe) PlaneConstraintTypes
         Returns the plane constraint types   
            
         
        """
        pass
    @PlaneConstraintTypes.setter
    def PlaneConstraintTypes(self, planeConstraintTypes: ReplaceMeshWithFaceBuilder.PlaneConstraint):
        """
        Setter for property: ( ReplaceMeshWithFaceBuilder.PlaneConstraint NXOpe) PlaneConstraintTypes
         Returns the plane constraint types   
            
         
        """
        pass
    @property
    def PlaneParallelConstraintNormal(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) PlaneParallelConstraintNormal
         Returns the plane parallel constraint normal   
            
         
        """
        pass
    @PlaneParallelConstraintNormal.setter
    def PlaneParallelConstraintNormal(self, planeParallelConstraintNormal: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) PlaneParallelConstraintNormal
         Returns the plane parallel constraint normal   
            
         
        """
        pass
    @property
    def RadiusToggle(self) -> bool:
        """
        Getter for property: (bool) RadiusToggle
         Returns the radius toggle   
            
         
        """
        pass
    @RadiusToggle.setter
    def RadiusToggle(self, radiusToggle: bool):
        """
        Setter for property: (bool) RadiusToggle
         Returns the radius toggle   
            
         
        """
        pass
    @property
    def ReplaceMeshOn(self) -> ReplaceMeshWithFaceBuilder.ReplaceMeshOnOption:
        """
        Getter for property: ( ReplaceMeshWithFaceBuilder.ReplaceMeshOnOption NXOpe) ReplaceMeshOn
         Returns the replace mesh on enum   
            
         
        """
        pass
    @ReplaceMeshOn.setter
    def ReplaceMeshOn(self, replaceMeshOn: ReplaceMeshWithFaceBuilder.ReplaceMeshOnOption):
        """
        Setter for property: ( ReplaceMeshWithFaceBuilder.ReplaceMeshOnOption NXOpe) ReplaceMeshOn
         Returns the replace mesh on enum   
            
         
        """
        pass
    @property
    def SphereConcentricConstraintPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) SphereConcentricConstraintPoint
         Returns the sphere concentric constraint point   
            
         
        """
        pass
    @SphereConcentricConstraintPoint.setter
    def SphereConcentricConstraintPoint(self, sphereConcentricConstraintPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) SphereConcentricConstraintPoint
         Returns the sphere concentric constraint point   
            
         
        """
        pass
    @property
    def SphereConstraintTypes(self) -> ReplaceMeshWithFaceBuilder.SphereConstraint:
        """
        Getter for property: ( ReplaceMeshWithFaceBuilder.SphereConstraint NXOpe) SphereConstraintTypes
         Returns the sphere constraint types   
            
         
        """
        pass
    @SphereConstraintTypes.setter
    def SphereConstraintTypes(self, sphereConstraintTypes: ReplaceMeshWithFaceBuilder.SphereConstraint):
        """
        Setter for property: ( ReplaceMeshWithFaceBuilder.SphereConstraint NXOpe) SphereConstraintTypes
         Returns the sphere constraint types   
            
         
        """
        pass
    @property
    def Type(self) -> ReplaceMeshWithFaceBuilder.Types:
        """
        Getter for property: ( ReplaceMeshWithFaceBuilder.Types NXOpe) Type
         Returns the type of enum which decides method for dividing facet faces  
            
         
        """
        pass
    @Type.setter
    def Type(self, type: ReplaceMeshWithFaceBuilder.Types):
        """
        Setter for property: ( ReplaceMeshWithFaceBuilder.Types NXOpe) Type
         Returns the type of enum which decides method for dividing facet faces  
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SculptMeshBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Facet.SculptMeshBuilder.
        This class provides the ability to sculpt the shape of a facet body by pushing or pulling facets within a locally defined area."""
    @property
    def EditCopy(self) -> bool:
        """
        Getter for property: (bool) EditCopy
         Returns the edit copy   
            
         
        """
        pass
    @EditCopy.setter
    def EditCopy(self, editCopy: bool):
        """
        Setter for property: (bool) EditCopy
         Returns the edit copy   
            
         
        """
        pass
    @property
    def FallOffFactor(self) -> float:
        """
        Getter for property: (float) FallOffFactor
         Returns the falloff factor   
            
         
        """
        pass
    @FallOffFactor.setter
    def FallOffFactor(self, fallOffFactor: float):
        """
        Setter for property: (float) FallOffFactor
         Returns the falloff factor   
            
         
        """
        pass
    @property
    def MaximumOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumOffset
         Returns the maximum offset   
            
         
        """
        pass
    @property
    def TargetFacetBody(self) -> SelectFacetedBodyList:
        """
        Getter for property: ( SelectFacetedBodyList NXOpe) TargetFacetBody
         Returns the target body   
            
         
        """
        pass
    @property
    def Tool(self) -> NXOpen.GeometricUtilities.StrokeGestureData:
        """
        Getter for property: ( NXOpen.GeometricUtilities.StrokeGestureData) Tool
         Returns the sculpting tool   
            
         
        """
        pass
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Width
         Returns the width   
            
         
        """
        pass
    def ResetToMedium(self) -> None:
        """
         Reset falloff factor to medium 
        """
        pass
    def SculptMesh(self) -> None:
        """
          Sculpts the mesh based on the sculpting tool parameters and trajectory. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectFacetedBodyList(NXOpen.TaggedObject): 
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
    def Add(self, objectValue: FacetedBody) -> bool:
        """
         Adds an object to the list
            
         Returns added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    def AddWithViews(self, objects: List[FacetedBody], views: List[NXOpen.View]) -> bool:
        """
         Adds a set of objects with views to the list
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, objects: List[FacetedBody]) -> bool:
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
    def Add(self, selection: FacetedBody, view: NXOpen.View, point: NXOpen.Point3d) -> bool:
        """
         Adds the object with the objects view and objects point
            
         Returns added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: FacetedBody, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: FacetedBody, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
         The object being selected with the objects view and objects point and snap information.
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, selection: FacetedBody, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> bool:
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
    def Contains(self, objectValue: FacetedBody) -> bool:
        """
         Returns whether the specified object is already in the list or not.
            
         Returns list_contains (bool):  true if object is in the list, false otherwise .
        """
        pass
    def GetArray(self) -> List[FacetedBody]:
        """
         Returns the list of objects in the selection list.
            
         Returns objects ( FacetedBody List[NXO):  items in list .
        """
        pass
    def GetSelectObjectArray(self) -> List[NXOpen.SelectObject]:
        """
         Returns the list of SelectObjects in the selection list.
            
         Returns objects ( NXOpen.SelectObject Li):  items in list .
        """
        pass
    @overload
    def Remove(self, objectValue: FacetedBody) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    def RemoveArray(self, objects: List[FacetedBody]) -> bool:
        """
         Remove specified objects from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    @overload
    def Remove(self, objectValue: FacetedBody, view: NXOpen.View) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object  view was not a member of the list .
        """
        pass
    @overload
    def Remove(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: FacetedBody, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: FacetedBody, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
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
    def SetArray(self, objects: List[FacetedBody]) -> None:
        """
         Sets the list of objects in the selection list. This will clear any existing
            items in the list.
            
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectFacetedBody(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""
    @property
    def Value(self) -> FacetedBody:
        """
        Getter for property: ( FacetedBody NXOpe) Value
         Returns the object being selected
              
            
         
        """
        pass
    @Value.setter
    def Value(self, selection: FacetedBody):
        """
        Setter for property: ( FacetedBody NXOpe) Value
         Returns the object being selected
              
            
         
        """
        pass
    @overload
    def GetValue(self) -> Tuple[FacetedBody, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         Returns A tuple consisting of (selection, view, point). 
         - selection is:  FacetedBody NXOpe. selected object .
         - view is:  NXOpen.View. selected object view.
         - point is:  NXOpen.Point3d. selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, FacetedBody, NXOpen.View, NXOpen.Point3d, FacetedBody, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         Returns A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is:  NXOpen.InferSnapType.SnapType.  snap point type.
         - selection1 is:  FacetedBody NXOpe. first selected object .
         - view1 is:  NXOpen.View. first selected object view.
         - point1 is:  NXOpen.Point3d. first selected object point.
         - selection2 is:  FacetedBody NXOpe. second selected object .
         - view2 is:  NXOpen.View. second selected object view.
         - point2 is:  NXOpen.Point3d. second selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[FacetedBody, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         Returns A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is:  FacetedBody NXOpe. selected object .
         - cae_sub_type is:  NXOpen.CaeObjectType.CaeSubType. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    @overload
    def SetValue(self, selection: FacetedBody, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: FacetedBody, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: FacetedBody, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
    @overload
    def SetValue(self, selection: FacetedBody, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
import NXOpen
class SewFacetBodyBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Facet.SewFacetBodyBuilder
    It sews two touching NX facet bodies. User need to specify the range on one of input body.
    The range on the other body is calculated automatically by choosing the closest vertex.
    It retruns a new mergered NX facet body. The two input bodies can be kept, deleted or hidden.
    """
    class Input(Enum):
        """
        Members Include: 
         |Keep|  Keep the input facet body after builder committing 
         |Delete|  Delete the input facet body after builder committing 
         |Hide|  Hide the input facet body after builder committing 

        """
        Keep: int
        Delete: int
        Hide: int
        @staticmethod
        def ValueOf(value: int) -> SewFacetBodyBuilder.Input:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class VertexIndex(Enum):
        """
        Members Include: 
         |First|  Index of the first vertex 
         |Second|  Index of the second vertex 

        """
        First: int
        Second: int
        @staticmethod
        def ValueOf(value: int) -> SewFacetBodyBuilder.VertexIndex:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DeformBody(self) -> SelectFacetedBody:
        """
        Getter for property: ( SelectFacetedBody NXOpe) DeformBody
         Returns the deform body to be sewed   
            
         
        """
        pass
    @property
    def DeformDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DeformDistance
         Returns the distance to control the deform area on the deform body   
            
         
        """
        pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance used in the merge touching facet body feature   
            
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance used in the merge touching facet body feature   
            
         
        """
        pass
    @property
    def InputStatus(self) -> SewFacetBodyBuilder.Input:
        """
        Getter for property: ( SewFacetBodyBuilder.Input NXOpe) InputStatus
         Returns the option to specify how to deal with the input two facet bodies: keep, delete or hide   
            
         
        """
        pass
    @InputStatus.setter
    def InputStatus(self, inputStatus: SewFacetBodyBuilder.Input):
        """
        Setter for property: ( SewFacetBodyBuilder.Input NXOpe) InputStatus
         Returns the option to specify how to deal with the input two facet bodies: keep, delete or hide   
            
         
        """
        pass
    @property
    def TargetBody(self) -> SelectFacetedBody:
        """
        Getter for property: ( SelectFacetedBody NXOpe) TargetBody
         Returns the target body to be sewed   
            
         
        """
        pass
    @property
    def Vertex1(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Vertex1
         Returns the first vertex used to define the range   
            
         
        """
        pass
    @Vertex1.setter
    def Vertex1(self, vertexPoint1: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Vertex1
         Returns the first vertex used to define the range   
            
         
        """
        pass
    @property
    def Vertex2(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Vertex2
         Returns the second vertex used to define the range   
            
         
        """
        pass
    @Vertex2.setter
    def Vertex2(self, vertexPoint2: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Vertex2
         Returns the second vertex used to define the range   
            
         
        """
        pass
    def FlipRange(self) -> None:
        """
         Flip the range between the first and second vertex 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SmoothFacetBodyBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Facet.SmoothFacetBodyBuilder.
    Smooth Facet Body Builder is a function to facilitate the removal of noise from facet bodies while keeping the general shape in tact. """
    class Types(Enum):
        """
        Members Include: 
         |Mesh| 
         |Edge| 

        """
        Mesh: int
        Edge: int
        @staticmethod
        def ValueOf(value: int) -> SmoothFacetBodyBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Bodies(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) Bodies
         Returns the facet bodies to be smoothed.  
           Inputs to this command can be convergent objects.   
         
        """
        pass
    @property
    def FaceEdge(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) FaceEdge
         Returns the option indicating if a copy of the facet body will be smoothed without altering the original   
            
         
        """
        pass
    @property
    def FacetBodies(self) -> SelectFacetedBodyList:
        """
        Getter for property: ( SelectFacetedBodyList NXOpe) FacetBodies
         Returns the facet bodies to be smoothed   
            
         
        """
        pass
    @property
    def FacetCollector(self) -> NXOpen.FacetCollector:
        """
        Getter for property: ( NXOpen.FacetCollector) FacetCollector
         Returns a collector of facets on the facet bodies to be to be smoothed.  
             
         
        """
        pass
    @FacetCollector.setter
    def FacetCollector(self, collector: NXOpen.FacetCollector):
        """
        Setter for property: ( NXOpen.FacetCollector) FacetCollector
         Returns a collector of facets on the facet bodies to be to be smoothed.  
             
         
        """
        pass
    @property
    def IsEditCopy(self) -> bool:
        """
        Getter for property: (bool) IsEditCopy
         Returns the option indicating if a copy of the facet body will be smoothed without altering the original   
            
         
        """
        pass
    @IsEditCopy.setter
    def IsEditCopy(self, isEditCopy: bool):
        """
        Setter for property: (bool) IsEditCopy
         Returns the option indicating if a copy of the facet body will be smoothed without altering the original   
            
         
        """
        pass
    @property
    def IsLockBoundary(self) -> bool:
        """
        Getter for property: (bool) IsLockBoundary
         Returns the option indicating if the open edges of inner and outer loops in the facet bodies are to be kept intact   
            
         
        """
        pass
    @IsLockBoundary.setter
    def IsLockBoundary(self, isLockBoundary: bool):
        """
        Setter for property: (bool) IsLockBoundary
         Returns the option indicating if the open edges of inner and outer loops in the facet bodies are to be kept intact   
            
         
        """
        pass
    @property
    def IsSmoothOverEdges(self) -> bool:
        """
        Getter for property: (bool) IsSmoothOverEdges
         Returns an option to apply the smooth operator across face edges   
            
         
        """
        pass
    @IsSmoothOverEdges.setter
    def IsSmoothOverEdges(self, isSmoothOverEdges: bool):
        """
        Setter for property: (bool) IsSmoothOverEdges
         Returns an option to apply the smooth operator across face edges   
            
         
        """
        pass
    @property
    def ModifyPercent(self) -> int:
        """
        Getter for property: (int) ModifyPercent
         Returns the modification percentage   
            
         
        """
        pass
    @ModifyPercent.setter
    def ModifyPercent(self, modifyPercent: int):
        """
        Setter for property: (int) ModifyPercent
         Returns the modification percentage   
            
         
        """
        pass
    @property
    def NumberOfIterations(self) -> int:
        """
        Getter for property: (int) NumberOfIterations
         Returns the number of iterations   
            
         
        """
        pass
    @NumberOfIterations.setter
    def NumberOfIterations(self, numberOfIterations: int):
        """
        Setter for property: (int) NumberOfIterations
         Returns the number of iterations   
            
         
        """
        pass
    @property
    def RegionList(self) -> NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList:
        """
        Getter for property: ( NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList) RegionList
         Returns an optional list of regions on the facet bodies to be smoothed   
            
         
        """
        pass
    @property
    def SmoothFactor(self) -> int:
        """
        Getter for property: (int) SmoothFactor
         Returns the smoothing factor   
            
         
        """
        pass
    @SmoothFactor.setter
    def SmoothFactor(self, smoothFactor: int):
        """
        Setter for property: (int) SmoothFactor
         Returns the smoothing factor   
            
         
        """
        pass
    @property
    def Type(self) -> SmoothFacetBodyBuilder.Types:
        """
        Getter for property: ( SmoothFacetBodyBuilder.Types NXOpe) Type
         Returns the type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: SmoothFacetBodyBuilder.Types):
        """
        Setter for property: ( SmoothFacetBodyBuilder.Types NXOpe) Type
         Returns the type   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SnipFacetBodyBuilder(NXOpen.Builder): 
    """ Represents a SnipFacetBody builder """
    class AutomaticFillTypes(Enum):
        """
        Members Include: 
         |NotSet|  None (do not fill) 
         |Linear|  Linear (triangulated) fill. 
         |Refined|  Smooth internal fill. 
         |TangentBased|  Smooth fill, boundary is based on facet body tangent. 
         |CurvatureBased|  Smooth fill, boundary is based on facet body curvature. 

        """
        NotSet: int
        Linear: int
        Refined: int
        TangentBased: int
        CurvatureBased: int
        @staticmethod
        def ValueOf(value: int) -> SnipFacetBodyBuilder.AutomaticFillTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class BoundaryFacetTreatmentMethod(Enum):
        """
        Members Include: 
         |SnipFacets|  Snip scarred facets by the border 
         |RemoveFacets|  Remove scarred facets 

        """
        SnipFacets: int
        RemoveFacets: int
        @staticmethod
        def ValueOf(value: int) -> SnipFacetBodyBuilder.BoundaryFacetTreatmentMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DirectionType(Enum):
        """
        Members Include: 
         |ViewDirection|  Snip along view direction 
         |FacetNormal|  Snip along facet normal 
         |AlongVector|  Snip along specified vector 

        """
        ViewDirection: int
        FacetNormal: int
        AlongVector: int
        @staticmethod
        def ValueOf(value: int) -> SnipFacetBodyBuilder.DirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RegionsOptionType(Enum):
        """
        Members Include: 
         |RemoveSelected|  Remove Selected 
         |KeepSelected|  Keep Selected 
         |Divide|  Divide 

        """
        RemoveSelected: int
        KeepSelected: int
        Divide: int
        @staticmethod
        def ValueOf(value: int) -> SnipFacetBodyBuilder.RegionsOptionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |SnipByBoundary|  Snip by boundary 
         |SnipByRegion|  Snip by region 
         |SnipWithCurves|  Snip with curves 
         |SnipAtPlane|  Snip at plane 

        """
        SnipByBoundary: int
        SnipByRegion: int
        SnipWithCurves: int
        SnipAtPlane: int
        @staticmethod
        def ValueOf(value: int) -> SnipFacetBodyBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AlongDirection(self) -> SnipFacetBodyBuilder.DirectionType:
        """
        Getter for property: ( SnipFacetBodyBuilder.DirectionType NXOpe) AlongDirection
         Returns the direction in which snipping profiles are projected on the facet bodies    
            
         
        """
        pass
    @AlongDirection.setter
    def AlongDirection(self, alongDirection: SnipFacetBodyBuilder.DirectionType):
        """
        Setter for property: ( SnipFacetBodyBuilder.DirectionType NXOpe) AlongDirection
         Returns the direction in which snipping profiles are projected on the facet bodies    
            
         
        """
        pass
    @property
    def AutomaticFillType(self) -> SnipFacetBodyBuilder.AutomaticFillTypes:
        """
        Getter for property: ( SnipFacetBodyBuilder.AutomaticFillTypes NXOpe) AutomaticFillType
         Returns the boundary smoothness   
            
         
        """
        pass
    @AutomaticFillType.setter
    def AutomaticFillType(self, smooth_type: SnipFacetBodyBuilder.AutomaticFillTypes):
        """
        Setter for property: ( SnipFacetBodyBuilder.AutomaticFillTypes NXOpe) AutomaticFillType
         Returns the boundary smoothness   
            
         
        """
        pass
    @property
    def Bodies(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) Bodies
         Returns the facet bodies to snip.  
           Inputs to this command can be convergent objects.   
         
        """
        pass
    @property
    def BoundaryFacetTreatmentType(self) -> SnipFacetBodyBuilder.BoundaryFacetTreatmentMethod:
        """
        Getter for property: ( SnipFacetBodyBuilder.BoundaryFacetTreatmentMethod NXOpe) BoundaryFacetTreatmentType
         Returns the boundary facet treatment type   
            
         
        """
        pass
    @BoundaryFacetTreatmentType.setter
    def BoundaryFacetTreatmentType(self, boundaryFacetTreatmentType: SnipFacetBodyBuilder.BoundaryFacetTreatmentMethod):
        """
        Setter for property: ( SnipFacetBodyBuilder.BoundaryFacetTreatmentMethod NXOpe) BoundaryFacetTreatmentType
         Returns the boundary facet treatment type   
            
         
        """
        pass
    @property
    def CanDivide(self) -> bool:
        """
        Getter for property: (bool) CanDivide
         Returns the value indicating if facet body is to be divided   
            
         
        """
        pass
    @CanDivide.setter
    def CanDivide(self, canDivide: bool):
        """
        Setter for property: (bool) CanDivide
         Returns the value indicating if facet body is to be divided   
            
         
        """
        pass
    @property
    def FacetBodies(self) -> SelectFacetedBodyList:
        """
        Getter for property: ( SelectFacetedBodyList NXOpe) FacetBodies
         Returns the facet bodies to snip   
            
         
        """
        pass
    @property
    def FacetCollector(self) -> NXOpen.FacetCollector:
        """
        Getter for property: ( NXOpen.FacetCollector) FacetCollector
         Returns the collector of facets to be snipped.  
            
         
        """
        pass
    @FacetCollector.setter
    def FacetCollector(self, collector: NXOpen.FacetCollector):
        """
        Setter for property: ( NXOpen.FacetCollector) FacetCollector
         Returns the collector of facets to be snipped.  
            
         
        """
        pass
    @property
    def IsEditCopy(self) -> bool:
        """
        Getter for property: (bool) IsEditCopy
         Returns the value indicating if a copy of the facet body to be snipped without altering the original   
            
         
        """
        pass
    @IsEditCopy.setter
    def IsEditCopy(self, isEditCopy: bool):
        """
        Setter for property: (bool) IsEditCopy
         Returns the value indicating if a copy of the facet body to be snipped without altering the original   
            
         
        """
        pass
    @property
    def IsSnipNearFacets(self) -> bool:
        """
        Getter for property: (bool) IsSnipNearFacets
         Returns the value indicating if only facets near to the viewer to be snipped   
            
         
        """
        pass
    @IsSnipNearFacets.setter
    def IsSnipNearFacets(self, isSnipNearFacets: bool):
        """
        Setter for property: (bool) IsSnipNearFacets
         Returns the value indicating if only facets near to the viewer to be snipped   
            
         
        """
        pass
    @property
    def Plane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) Plane
         Returns the snipping plane   
            
         
        """
        pass
    @Plane.setter
    def Plane(self, plane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) Plane
         Returns the snipping plane   
            
         
        """
        pass
    @property
    def ProfileList(self) -> NXOpen.SectionList:
        """
        Getter for property: ( NXOpen.SectionList) ProfileList
         Returns the list of snipping profiles   
            
         
        """
        pass
    @property
    def ProjectBothSides(self) -> bool:
        """
        Getter for property: (bool) ProjectBothSides
         Returns the value indicating if project both sides in snip with curves along specified vector.  
             
         
        """
        pass
    @ProjectBothSides.setter
    def ProjectBothSides(self, projectBothSides: bool):
        """
        Setter for property: (bool) ProjectBothSides
         Returns the value indicating if project both sides in snip with curves along specified vector.  
             
         
        """
        pass
    @property
    def ProjectionVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ProjectionVector
         Returns the projection vector   
            
         
        """
        pass
    @ProjectionVector.setter
    def ProjectionVector(self, projectionVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ProjectionVector
         Returns the projection vector   
            
         
        """
        pass
    @property
    def RegionList(self) -> NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList:
        """
        Getter for property: ( NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList) RegionList
         Returns the list of regions to snip   
            
         
        """
        pass
    @property
    def RegionPoint(self) -> NXOpen.SelectPointList:
        """
        Getter for property: ( NXOpen.SelectPointList) RegionPoint
         Returns the point indicating the portion of the facet body with respect to specified region to be snipped.  
             
         
        """
        pass
    @property
    def RegionsOption(self) -> SnipFacetBodyBuilder.RegionsOptionType:
        """
        Getter for property: ( SnipFacetBodyBuilder.RegionsOptionType NXOpe) RegionsOption
         Returns the regions option of enum   
            
         
        """
        pass
    @RegionsOption.setter
    def RegionsOption(self, regionsOption: SnipFacetBodyBuilder.RegionsOptionType):
        """
        Setter for property: ( SnipFacetBodyBuilder.RegionsOptionType NXOpe) RegionsOption
         Returns the regions option of enum   
            
         
        """
        pass
    @property
    def Type(self) -> SnipFacetBodyBuilder.Types:
        """
        Getter for property: ( SnipFacetBodyBuilder.Types NXOpe) Type
         Returns the snipping method accessor  
            
         
        """
        pass
    @Type.setter
    def Type(self, type: SnipFacetBodyBuilder.Types):
        """
        Setter for property: ( SnipFacetBodyBuilder.Types NXOpe) Type
         Returns the snipping method accessor  
            
         
        """
        pass
    @property
    def ViewDirection(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) ViewDirection
         Returns the view direction   
            
         
        """
        pass
    @ViewDirection.setter
    def ViewDirection(self, viewDirection: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) ViewDirection
         Returns the view direction   
            
         
        """
        pass
    def SwitchRegion(self) -> None:
        """
         Switch the region to be snipped indicated by the region point. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SplitCurveMethodBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Facet.SplitCurveMethodBuilder.
   Split Curve Method Builder is a class to provide a curve to divide the facet faces. """
    class ProjectOption(Enum):
        """
        Members Include: 
         |NormalToFace|  project normal to face 
         |AlongVector|  project along vector 

        """
        NormalToFace: int
        AlongVector: int
        @staticmethod
        def ValueOf(value: int) -> SplitCurveMethodBuilder.ProjectOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ExistingCurves(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) ExistingCurves
         Returns the existing curves to be used to divide facet body  
            
         
        """
        pass
    @property
    def ProjectDirection(self) -> NXOpen.GeometricUtilities.ProjectionOptions:
        """
        Getter for property: ( NXOpen.GeometricUtilities.ProjectionOptions) ProjectDirection
         Returns the projection direction   
            
         
        """
        pass
    def AddCurveOnBodies(self, bodyArray: List[NXOpen.Body]) -> None:
        """
         Set the list of curves on bodies 
        """
        pass
    def CreateSplitCurveWithUseExisting(self) -> List[NXOpen.Spline]:
        """
         Create split curve with use existing method
         Returns curves ( NXOpen.Spline Li): .
        """
        pass
import NXOpen
class SplitCurveMethodListDataManager(NXOpen.TaggedObject): 
    """ Represents a NXOpen.Facet.SplitCurveMethodListDataManager.
    Split Curve Method List Data Manager is a class to provide list of split curve methods used in facet body. """
    @property
    def SplitCurveMethodList(self) -> NXOpen.TaggedObjectList:
        """
        Getter for property: ( NXOpen.TaggedObjectList) SplitCurveMethodList
         Returns the split curve list   
            
         
        """
        pass
import NXOpen
class STLImportBuilder(NXOpen.Builder): 
    """ The STL file import builder. Inputs to this class can be convergent objects."""
    class AngularToleranceTypes(Enum):
        """
        Members Include: 
         |Coarse|  
         |Medium|  
         |Fine|  

        """
        Coarse: int
        Medium: int
        Fine: int
        @staticmethod
        def ValueOf(value: int) -> STLImportBuilder.AngularToleranceTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FacetBodyTypes(Enum):
        """
        Members Include: 
         |Psm|  Import to Facet Brep format
         |Nx|  Import To NX Facet Format 
         |Jt|  Import to JT format

        """
        Psm: int
        Nx: int
        Jt: int
        @staticmethod
        def ValueOf(value: int) -> STLImportBuilder.FacetBodyTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class STLFileUnitsTypes(Enum):
        """
        Members Include: 
         |Meters|  
         |Millimeters|  
         |Inches|  

        """
        Meters: int
        Millimeters: int
        Inches: int
        @staticmethod
        def ValueOf(value: int) -> STLImportBuilder.STLFileUnitsTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngularTolerance(self) -> STLImportBuilder.AngularToleranceTypes:
        """
        Getter for property: ( STLImportBuilder.AngularToleranceTypes NXOpe) AngularTolerance
         Returns the angular tolerance   
            
         
        """
        pass
    @AngularTolerance.setter
    def AngularTolerance(self, angularTolerance: STLImportBuilder.AngularToleranceTypes):
        """
        Setter for property: ( STLImportBuilder.AngularToleranceTypes NXOpe) AngularTolerance
         Returns the angular tolerance   
            
         
        """
        pass
    @property
    def CleanUp(self) -> bool:
        """
        Getter for property: (bool) CleanUp
         Returns the option to clean up all mesh defects on import   
            
         
        """
        pass
    @CleanUp.setter
    def CleanUp(self, cleanUp: bool):
        """
        Setter for property: (bool) CleanUp
         Returns the option to clean up all mesh defects on import   
            
         
        """
        pass
    @property
    def FacetBodyType(self) -> STLImportBuilder.FacetBodyTypes:
        """
        Getter for property: ( STLImportBuilder.FacetBodyTypes NXOpe) FacetBodyType
         Returns the facet body type   
            
         
        """
        pass
    @FacetBodyType.setter
    def FacetBodyType(self, facetBodyType: STLImportBuilder.FacetBodyTypes):
        """
        Setter for property: ( STLImportBuilder.FacetBodyTypes NXOpe) FacetBodyType
         Returns the facet body type   
            
         
        """
        pass
    @property
    def File(self) -> str:
        """
        Getter for property: (str) File
         Returns the STL file    
            
         
        """
        pass
    @File.setter
    def File(self, filename: str):
        """
        Setter for property: (str) File
         Returns the STL file    
            
         
        """
        pass
    @property
    def HideSmoothEdges(self) -> bool:
        """
        Getter for property: (bool) HideSmoothEdges
         Returns the indicator for whether to hide smooth edges   
            
         
        """
        pass
    @HideSmoothEdges.setter
    def HideSmoothEdges(self, hideSmoothEdges: bool):
        """
        Setter for property: (bool) HideSmoothEdges
         Returns the indicator for whether to hide smooth edges   
            
         
        """
        pass
    @property
    def MinimumAngleFoldedFacets(self) -> float:
        """
        Getter for property: (float) MinimumAngleFoldedFacets
         Returns the value for minimum angle between adjacent facets to define folded facets.  
             
         
        """
        pass
    @MinimumAngleFoldedFacets.setter
    def MinimumAngleFoldedFacets(self, minimumAngleFoldedFacets: float):
        """
        Setter for property: (float) MinimumAngleFoldedFacets
         Returns the value for minimum angle between adjacent facets to define folded facets.  
             
         
        """
        pass
    @property
    def MinimumFacetNumber(self) -> int:
        """
        Getter for property: (int) MinimumFacetNumber
         Returns the value for minimum number of facets for a STL file to be imported   
            
         
        """
        pass
    @MinimumFacetNumber.setter
    def MinimumFacetNumber(self, minimumFacetNumber: int):
        """
        Setter for property: (int) MinimumFacetNumber
         Returns the value for minimum number of facets for a STL file to be imported   
            
         
        """
        pass
    @property
    def STLFileUnits(self) -> STLImportBuilder.STLFileUnitsTypes:
        """
        Getter for property: ( STLImportBuilder.STLFileUnitsTypes NXOpe) STLFileUnits
         Returns the STL file units   
            
         
        """
        pass
    @STLFileUnits.setter
    def STLFileUnits(self, stlFileUnits: STLImportBuilder.STLFileUnitsTypes):
        """
        Setter for property: ( STLImportBuilder.STLFileUnitsTypes NXOpe) STLFileUnits
         Returns the STL file units   
            
         
        """
        pass
    @property
    def ShowInformationWindow(self) -> bool:
        """
        Getter for property: (bool) ShowInformationWindow
         Returns the indicator for whether to show information window   
            
         
        """
        pass
    @ShowInformationWindow.setter
    def ShowInformationWindow(self, showInformationWindow: bool):
        """
        Setter for property: (bool) ShowInformationWindow
         Returns the indicator for whether to show information window   
            
         
        """
        pass
    def GetTopology(self) -> List[NXOpen.Part]:
        """
          The imported bodies after STL file import 
         Returns topology ( NXOpen.Part Li): .
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SubdivideFacetBodyBuilder(NXOpen.Builder): 
    """ This class provides functionality to subdivide the polygons to increase the density of the facet bodies.
    Subdividing Polygons creates a smoother representation."""
    class InterpolationMethodType(Enum):
        """
        Members Include: 
         |Linear|  In the linear option the sub-triangles are coplanar to the original triangle. Shape resolution remains untouched. 
         |Cubic|  In the cubic option the sub-triangles are fitted cubic to the surrounding triangles. Shape resolution increases. 

        """
        Linear: int
        Cubic: int
        @staticmethod
        def ValueOf(value: int) -> SubdivideFacetBodyBuilder.InterpolationMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SubdivisionMethodType(Enum):
        """
        Members Include: 
         |SubdivideIntoFour|  Subdivides the polygons into four sub triangles. The original mesh structure remains.
         |SubdividebyEdgeLength|  Subdivides the polygons to a specified edge length. The original mesh structure disappears. 

        """
        SubdivideIntoFour: int
        SubdividebyEdgeLength: int
        @staticmethod
        def ValueOf(value: int) -> SubdivideFacetBodyBuilder.SubdivisionMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngleThreshold(self) -> float:
        """
        Getter for property: (float) AngleThreshold
         Returns the angular tolerance to detect sharp edges to be kept.  
           Cubic interpolation can not interpolate over an edge of two triangles whose normals differ more than the specified value. Same applies to re-meshing.   
         
        """
        pass
    @AngleThreshold.setter
    def AngleThreshold(self, angleThreshold: float):
        """
        Setter for property: (float) AngleThreshold
         Returns the angular tolerance to detect sharp edges to be kept.  
           Cubic interpolation can not interpolate over an edge of two triangles whose normals differ more than the specified value. Same applies to re-meshing.   
         
        """
        pass
    @property
    def Bodies(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) Bodies
         Returns the facet bodies to be subdivided.  
           Inputs to this command can be convergent objects.   
         
        """
        pass
    @property
    def EdgeLength(self) -> float:
        """
        Getter for property: (float) EdgeLength
         Returns the value indicating length of the edge of the polygons to be subdivided.  
            
         
        """
        pass
    @EdgeLength.setter
    def EdgeLength(self, edgeLength: float):
        """
        Setter for property: (float) EdgeLength
         Returns the value indicating length of the edge of the polygons to be subdivided.  
            
         
        """
        pass
    @property
    def FacetBodies(self) -> SelectFacetedBodyList:
        """
        Getter for property: ( SelectFacetedBodyList NXOpe) FacetBodies
         Returns the facet bodies to be subdivided  
            
         
        """
        pass
    @property
    def FacetCollector(self) -> NXOpen.FacetCollector:
        """
        Getter for property: ( NXOpen.FacetCollector) FacetCollector
         Returns a collector of facets on the facet bodies to be subdivided.  
             
         
        """
        pass
    @FacetCollector.setter
    def FacetCollector(self, collector: NXOpen.FacetCollector):
        """
        Setter for property: ( NXOpen.FacetCollector) FacetCollector
         Returns a collector of facets on the facet bodies to be subdivided.  
             
         
        """
        pass
    @property
    def InterpolationMethod(self) -> SubdivideFacetBodyBuilder.InterpolationMethodType:
        """
        Getter for property: ( SubdivideFacetBodyBuilder.InterpolationMethodType NXOpe) InterpolationMethod
         Returns the interpolation method   
            
         
        """
        pass
    @InterpolationMethod.setter
    def InterpolationMethod(self, interpolationMethod: SubdivideFacetBodyBuilder.InterpolationMethodType):
        """
        Setter for property: ( SubdivideFacetBodyBuilder.InterpolationMethodType NXOpe) InterpolationMethod
         Returns the interpolation method   
            
         
        """
        pass
    @property
    def IsEditCopy(self) -> bool:
        """
        Getter for property: (bool) IsEditCopy
         Returns the value indicating if a copy of the facet body to be subdivided without altering the original.  
             
         
        """
        pass
    @IsEditCopy.setter
    def IsEditCopy(self, isEditCopy: bool):
        """
        Setter for property: (bool) IsEditCopy
         Returns the value indicating if a copy of the facet body to be subdivided without altering the original.  
             
         
        """
        pass
    @property
    def IsOptimize(self) -> bool:
        """
        Getter for property: (bool) IsOptimize
         Returns the value indicating whether to perform a decimation step after the subdivision.  
            
         
        """
        pass
    @IsOptimize.setter
    def IsOptimize(self, isOptimize: bool):
        """
        Setter for property: (bool) IsOptimize
         Returns the value indicating whether to perform a decimation step after the subdivision.  
            
         
        """
        pass
    @property
    def RegionList(self) -> NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList:
        """
        Getter for property: ( NXOpen.GeometricUtilities.BoundaryDefinitionBuilderList) RegionList
         Returns an optional list of regions on the facet bodies to be subdivided.  
             
         
        """
        pass
    @property
    def SubdivisionMethod(self) -> SubdivideFacetBodyBuilder.SubdivisionMethodType:
        """
        Getter for property: ( SubdivideFacetBodyBuilder.SubdivisionMethodType NXOpe) SubdivisionMethod
         Returns the subdivision method   
            
         
        """
        pass
    @SubdivisionMethod.setter
    def SubdivisionMethod(self, subdivisionMethod: SubdivideFacetBodyBuilder.SubdivisionMethodType):
        """
        Setter for property: ( SubdivideFacetBodyBuilder.SubdivisionMethodType NXOpe) SubdivisionMethod
         Returns the subdivision method   
            
         
        """
        pass
import NXOpen
class WrapMeshBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Facet.WrapMeshBuilder.
        This class wraps a facet body around one or more bodies."""
    class KeepInputBodyType(Enum):
        """
        Members Include: 
         |Keep| 
         |Hide| 

        """
        Keep: int
        Hide: int
        @staticmethod
        def ValueOf(value: int) -> WrapMeshBuilder.KeepInputBodyType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MethodType(Enum):
        """
        Members Include: 
         |External| 
         |LargestInternal| 
         |InternalBySeedPoint| 

        """
        External: int
        LargestInternal: int
        InternalBySeedPoint: int
        @staticmethod
        def ValueOf(value: int) -> WrapMeshBuilder.MethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class WrapMeshModeType(Enum):
        """
        Members Include: 
         |Constant| 
         |Variable| 

        """
        Constant: int
        Variable: int
        @staticmethod
        def ValueOf(value: int) -> WrapMeshBuilder.WrapMeshModeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngleThreshold(self) -> float:
        """
        Getter for property: (float) AngleThreshold
         Returns the angle threshold  
            
         
        """
        pass
    @AngleThreshold.setter
    def AngleThreshold(self, angleThreshold: float):
        """
        Setter for property: (float) AngleThreshold
         Returns the angle threshold  
            
         
        """
        pass
    @property
    def AverageSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) AverageSize
         Returns the average size for wrap mesh  
            
         
        """
        pass
    @property
    def ChordalTolerance(self) -> float:
        """
        Getter for property: (float) ChordalTolerance
         Returns the chordal tolerance for wrap mesh  
            
         
        """
        pass
    @ChordalTolerance.setter
    def ChordalTolerance(self, chordalTolerance: float):
        """
        Setter for property: (float) ChordalTolerance
         Returns the chordal tolerance for wrap mesh  
            
         
        """
        pass
    @property
    def FacetsInGap(self) -> int:
        """
        Getter for property: (int) FacetsInGap
         Returns the facets in gap   
            
         
        """
        pass
    @FacetsInGap.setter
    def FacetsInGap(self, facetsInGap: int):
        """
        Setter for property: (int) FacetsInGap
         Returns the facets in gap   
            
         
        """
        pass
    @property
    def GapFaces(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) GapFaces
         Returns the select gap faces  
            
         
        """
        pass
    @property
    def InputBodyCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) InputBodyCollector
         Returns the input body collector   
            
         
        """
        pass
    @property
    def InputBodyOption(self) -> WrapMeshBuilder.KeepInputBodyType:
        """
        Getter for property: ( WrapMeshBuilder.KeepInputBodyType NXOpe) InputBodyOption
         Returns the input body visibility option.  
             
         
        """
        pass
    @InputBodyOption.setter
    def InputBodyOption(self, inputBodyOption: WrapMeshBuilder.KeepInputBodyType):
        """
        Setter for property: ( WrapMeshBuilder.KeepInputBodyType NXOpe) InputBodyOption
         Returns the input body visibility option.  
             
         
        """
        pass
    @property
    def IntendedGapSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) IntendedGapSize
         Returns the intended gap size  
            
         
        """
        pass
    @property
    def KeepSharpEdges(self) -> bool:
        """
        Getter for property: (bool) KeepSharpEdges
         Returns the flag indicating if sharp edges should be kept.  
             
         
        """
        pass
    @KeepSharpEdges.setter
    def KeepSharpEdges(self, keepSharpEdges: bool):
        """
        Setter for property: (bool) KeepSharpEdges
         Returns the flag indicating if sharp edges should be kept.  
             
         
        """
        pass
    @property
    def MaxGapSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxGapSize
         Returns the maximum gap size  
            
         
        """
        pass
    @property
    def MaximumSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumSize
         Returns the maximum size for wrap mesh  
            
         
        """
        pass
    @property
    def Method(self) -> WrapMeshBuilder.MethodType:
        """
        Getter for property: ( WrapMeshBuilder.MethodType NXOpe) Method
         Returns the method for selected volume  
            
         
        """
        pass
    @Method.setter
    def Method(self, method: WrapMeshBuilder.MethodType):
        """
        Setter for property: ( WrapMeshBuilder.MethodType NXOpe) Method
         Returns the method for selected volume  
            
         
        """
        pass
    @property
    def ProximityRefinement(self) -> bool:
        """
        Getter for property: (bool) ProximityRefinement
         Returns the proximity refinement   
            
         
        """
        pass
    @ProximityRefinement.setter
    def ProximityRefinement(self, proximityRefinement: bool):
        """
        Setter for property: (bool) ProximityRefinement
         Returns the proximity refinement   
            
         
        """
        pass
    @property
    def SearchDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SearchDistance
         Returns the search distance   
            
         
        """
        pass
    @property
    def SeedPoint(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) SeedPoint
         Returns the seed point   
            
         
        """
        pass
    @property
    def WrapMeshMode(self) -> WrapMeshBuilder.WrapMeshModeType:
        """
        Getter for property: ( WrapMeshBuilder.WrapMeshModeType NXOpe) WrapMeshMode
         Returns the mode for wrap mesh  
            
         
        """
        pass
    @WrapMeshMode.setter
    def WrapMeshMode(self, wrapMeshMode: WrapMeshBuilder.WrapMeshModeType):
        """
        Setter for property: ( WrapMeshBuilder.WrapMeshModeType NXOpe) WrapMeshMode
         Returns the mode for wrap mesh  
            
         
        """
        pass
