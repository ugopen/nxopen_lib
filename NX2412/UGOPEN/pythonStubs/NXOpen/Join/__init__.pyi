from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class AttachedHardwareBuilder(PointJoinBuilder): 
    """
    Represents a NXOpen.Join.AttachedHardware builder.
    """
    @property
    def MatingFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) MatingFace
         Returns the selected mating face   
            
         
        """
        pass
import NXOpen.Features
class AttachedHardware(NXOpen.Features.Feature): 
    """ Represents a attached hardware feature """
    pass
import NXOpen
class AttachmentHardware(PointJoinHardware): 
    """ Represents a NXOpen.Join.AttachmentHardware.
    """
    @property
    def Alignment(self) -> str:
        """
        Getter for property: (str) Alignment
         Returns the alignment of the attachment hardware part.  
            
         
        """
        pass
    @Alignment.setter
    def Alignment(self, alignment: str):
        """
        Setter for property: (str) Alignment
         Returns the alignment of the attachment hardware part.  
            
         
        """
        pass
    def GetBoltPoint(self) -> List[NXOpen.Point3d]:
        """
         The bolt points of attachment hardware part
         Returns bolts ( NXOpen.Point3d Li): .
        """
        pass
    def GetConnectionPoint(self) -> List[NXOpen.Point3d]:
        """
         The connections points of attachment hardware part
         Returns connections ( NXOpen.Point3d Li): .
        """
        pass
    def SetBoltPoint(self, bolts: List[NXOpen.Point3d]) -> None:
        """
         The bolt points of attachment hardware part
        """
        pass
    def SetConnectionPoint(self, connections: List[NXOpen.Point3d]) -> None:
        """
         The connections points of attachment hardware part
        """
        pass
import NXOpen
import NXOpen.Assemblies
class AutoPointBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Join.AutoPointBuilder builder """
    class InterferenceDetails(Enum):
        """
        Members Include: 
         |NoWeldsNearBodies|  Indicates no existing weld points are in this interference area 
         |Same|  Indicates weld points exist and part name are the same. 
         |Added|  deprecated. 
         |Deleted|  deprecated. 

        """
        NoWeldsNearBodies: int
        Same: int
        Added: int
        Deleted: int
        @staticmethod
        def ValueOf(value: int) -> AutoPointBuilder.InterferenceDetails:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ComponentsToJoin(self) -> NXOpen.Assemblies.SelectComponentList:
        """
        Getter for property: ( NXOpen.Assemblies.SelectComponentList) ComponentsToJoin
         Returns the components that should be joined together.  
           This can be one component, or many.   
         
        """
        pass
    @property
    def ComponentsTreatAsUnit(self) -> NXOpen.Assemblies.SelectComponentList:
        """
        Getter for property: ( NXOpen.Assemblies.SelectComponentList) ComponentsTreatAsUnit
         Returns the components to treat as unit.  
           No features will be created within unit components. Components must be a subset of components to join.   
         
        """
        pass
    @property
    def CreateFeaturesOnOk(self) -> bool:
        """
        Getter for property: (bool) CreateFeaturesOnOk
         Returns the value to indicate if features should be created on ok, or if the Point Join dialog should be launched instead.  
             
         
        """
        pass
    @CreateFeaturesOnOk.setter
    def CreateFeaturesOnOk(self, create_features_on_ok: bool):
        """
        Setter for property: (bool) CreateFeaturesOnOk
         Returns the value to indicate if features should be created on ok, or if the Point Join dialog should be launched instead.  
             
         
        """
        pass
    @property
    def DistanceFromEnds(self) -> float:
        """
        Getter for property: (float) DistanceFromEnds
         Returns the distance from the ends to start creating weld points   
            
         
        """
        pass
    @DistanceFromEnds.setter
    def DistanceFromEnds(self, distanceFromEnds: float):
        """
        Setter for property: (float) DistanceFromEnds
         Returns the distance from the ends to start creating weld points   
            
         
        """
        pass
    @property
    def FaceGapDistance(self) -> float:
        """
        Getter for property: (float) FaceGapDistance
         Returns the face gap distance.  
           This will be used to find interferences between bodies.   
         
        """
        pass
    @FaceGapDistance.setter
    def FaceGapDistance(self, faceGapDistance: float):
        """
        Setter for property: (float) FaceGapDistance
         Returns the face gap distance.  
           This will be used to find interferences between bodies.   
         
        """
        pass
    @property
    def MaximumBendRadius(self) -> float:
        """
        Getter for property: (float) MaximumBendRadius
         Returns the bend radius of a flange.  
            Points will not be put on faces with a 
                    radius smaller than this value.   
         
        """
        pass
    @MaximumBendRadius.setter
    def MaximumBendRadius(self, maximumBendRadius: float):
        """
        Setter for property: (float) MaximumBendRadius
         Returns the bend radius of a flange.  
            Points will not be put on faces with a 
                    radius smaller than this value.   
         
        """
        pass
    @property
    def MaximumCenterlineWidth(self) -> float:
        """
        Getter for property: (float) MaximumCenterlineWidth
         Returns the maximum centerline width.  
           Points will be created using the centerline method
                    if the smallest width is less than this value. If greater, points will be
                    created using the offset from edge method.   
         
        """
        pass
    @MaximumCenterlineWidth.setter
    def MaximumCenterlineWidth(self, maximumCenterlineWidth: float):
        """
        Setter for property: (float) MaximumCenterlineWidth
         Returns the maximum centerline width.  
           Points will be created using the centerline method
                    if the smallest width is less than this value. If greater, points will be
                    created using the offset from edge method.   
         
        """
        pass
    @property
    def MaximumSingleThickness(self) -> float:
        """
        Getter for property: (float) MaximumSingleThickness
         Returns the maximum single metal thickness for all the selected components.  
          
                    If the distance between top faces of two panels (or sheets) is greater
                    than single thickness plus face gap distance, a point will not be created
                    at that location.   
         
        """
        pass
    @MaximumSingleThickness.setter
    def MaximumSingleThickness(self, maximumSingleThickness: float):
        """
        Setter for property: (float) MaximumSingleThickness
         Returns the maximum single metal thickness for all the selected components.  
          
                    If the distance between top faces of two panels (or sheets) is greater
                    than single thickness plus face gap distance, a point will not be created
                    at that location.   
         
        """
        pass
    @property
    def MaximumSpacingBetweenPoints(self) -> float:
        """
        Getter for property: (float) MaximumSpacingBetweenPoints
         Returns the maximum spacing between points   
            
         
        """
        pass
    @MaximumSpacingBetweenPoints.setter
    def MaximumSpacingBetweenPoints(self, maximumSpacingBetweenPoints: float):
        """
        Setter for property: (float) MaximumSpacingBetweenPoints
         Returns the maximum spacing between points   
            
         
        """
        pass
    @property
    def MinimumFlangeWidth(self) -> float:
        """
        Getter for property: (float) MinimumFlangeWidth
         Returns the minimum flange width.  
           If opposite sides of a flange are smaller than
                    minimum flange width, it will be ignored.   
         
        """
        pass
    @MinimumFlangeWidth.setter
    def MinimumFlangeWidth(self, minimumFlangeWidth: float):
        """
        Setter for property: (float) MinimumFlangeWidth
         Returns the minimum flange width.  
           If opposite sides of a flange are smaller than
                    minimum flange width, it will be ignored.   
         
        """
        pass
    @property
    def MinimumNumberPointsOnOverlap(self) -> int:
        """
        Getter for property: (int) MinimumNumberPointsOnOverlap
         Returns the mimimum number points to create on an overlap sheet   
            
         
        """
        pass
    @MinimumNumberPointsOnOverlap.setter
    def MinimumNumberPointsOnOverlap(self, minimumNumberPointsOnOverlap: int):
        """
        Setter for property: (int) MinimumNumberPointsOnOverlap
         Returns the mimimum number points to create on an overlap sheet   
            
         
        """
        pass
    @property
    def MinimumSpacingBetweenPoints(self) -> float:
        """
        Getter for property: (float) MinimumSpacingBetweenPoints
         Returns the minimum spacing between points   
            
         
        """
        pass
    @MinimumSpacingBetweenPoints.setter
    def MinimumSpacingBetweenPoints(self, minimumSpacingBetweenPoints: float):
        """
        Setter for property: (float) MinimumSpacingBetweenPoints
         Returns the minimum spacing between points   
            
         
        """
        pass
    @property
    def MoveReferenceSheetToConstructionLayer(self) -> bool:
        """
        Getter for property: (bool) MoveReferenceSheetToConstructionLayer
         Returns the value to indidate if the output sheet bodies of this feature should be moved to the construction layer.  
           Use  NXOpen::Join::JoinPreferences::SetConstructionLayer  to change the default layer.   
         
        """
        pass
    @MoveReferenceSheetToConstructionLayer.setter
    def MoveReferenceSheetToConstructionLayer(self, moveReferenceSheetToConstructionLayer: bool):
        """
        Setter for property: (bool) MoveReferenceSheetToConstructionLayer
         Returns the value to indidate if the output sheet bodies of this feature should be moved to the construction layer.  
           Use  NXOpen::Join::JoinPreferences::SetConstructionLayer  to change the default layer.   
         
        """
        pass
    @property
    def OffsetDistanceFromEdge(self) -> float:
        """
        Getter for property: (float) OffsetDistanceFromEdge
         Returns the offset distance from edge   
            
         
        """
        pass
    @OffsetDistanceFromEdge.setter
    def OffsetDistanceFromEdge(self, offsetDistanceFromEdge: float):
        """
        Setter for property: (float) OffsetDistanceFromEdge
         Returns the offset distance from edge   
            
         
        """
        pass
    @property
    def Subtype(self) -> str:
        """
        Getter for property: (str) Subtype
         Returns the Subtype   
            
         
        """
        pass
    @Subtype.setter
    def Subtype(self, type: str):
        """
        Setter for property: (str) Subtype
         Returns the Subtype   
            
         
        """
        pass
    @property
    def UniformSpacingTolerance(self) -> float:
        """
        Getter for property: (float) UniformSpacingTolerance
         Returns the distance that maximum spacing can be exceeded to achieve uniform spacing   
            
         
        """
        pass
    @UniformSpacingTolerance.setter
    def UniformSpacingTolerance(self, uniformSpacingTolerance: float):
        """
        Setter for property: (float) UniformSpacingTolerance
         Returns the distance that maximum spacing can be exceeded to achieve uniform spacing   
            
         
        """
        pass
    def AskConnectedBodiesAtPoint(self, refPoint: NXOpen.Point) -> List[NXOpen.Body]:
        """
         Ask the connected bodies at a specific point. The point must be from NXOpen.Join.AutoPointBuilder.GetPoints. 
         Returns bodies ( NXOpen.Body Li): .
        """
        pass
    def CreateFeatureSet(self, interferenceIndex: int) -> NXOpen.NXObject:
        """
         Creates a feature set containing weld points for a given interference. 
         Returns featureSetTag ( NXOpen.NXObject): .
        """
        pass
    def FindNumberOfInterferenceRegions(self) -> int:
        """
         Returns the number of interference areas between the selected components. This
                    method must be invoked or no weld points will be created. The output numInterferences
                    variable can be used to get the status of each interference. 
         Returns numInterferences (int): .
        """
        pass
    def GetInterferenceDetails(self, interferenceIndex: int) -> AutoPointBuilder.InterferenceDetails:
        """
         The status indicating if the interference has existing weld points touching it. The
                    index for this function is described in NXOpen.Join.AutoPointBuilder.FindNumberOfInterferenceRegions. 
         Returns interferenceDetails ( AutoPointBuilder.InterferenceDetails NXOpe): .
        """
        pass
    def GetPoints(self) -> List[NXOpen.Point]:
        """
         Output reference points for which features have not been created. 
         Returns points ( NXOpen.Point Li): .
        """
        pass
    def GetShowSolids(self) -> bool:
        """
         Indicates the display mode. The created feature output can be shown as a solid or point. 
         Returns showSolids (bool): .
        """
        pass
    def GetShowThruState(self) -> bool:
        """
         Indicates whether the output point should show thru on creation 
         Returns showThruState (bool): .
        """
        pass
    def GetVisibleBodies(self) -> List[NXOpen.Body]:
        """
         Visible bodies from the selected components. 
         Returns bodies ( NXOpen.Body Li): .
        """
        pass
    def SetShowSolids(self, showSolids: bool) -> None:
        """
         Indicates the display mode. The created feature output can be shown as a solid or point. 
        """
        pass
    def SetShowThruState(self, showThruState: bool) -> None:
        """
         Indicates whether the output point should show thru on creation 
        """
        pass
import NXOpen.Features
class CompoundJoinWeldBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a NXOpen.Join.CompoundJoinWeld builder.
    """
    @property
    def ArrowSideJoinWelds(self) -> NXOpen.Features.SelectFeatureList:
        """
        Getter for property: ( NXOpen.Features.SelectFeatureList) ArrowSideJoinWelds
         Returns the join weld features defining the arrow side of the compound join weld.  
             
         
        """
        pass
    @property
    def OtherSideJoinWelds(self) -> NXOpen.Features.SelectFeatureList:
        """
        Getter for property: ( NXOpen.Features.SelectFeatureList) OtherSideJoinWelds
         Returns the join weld features defining the other side of the compound join weld.  
             
         
        """
        pass
    @property
    def Staggered(self) -> bool:
        """
        Getter for property: (bool) Staggered
         Returns the value to control if the weld symbol created from this compound weld should have the staggered indication.  
             
         
        """
        pass
    @Staggered.setter
    def Staggered(self, bStaggered: bool):
        """
        Setter for property: (bool) Staggered
         Returns the value to control if the weld symbol created from this compound weld should have the staggered indication.  
             
         
        """
        pass
import NXOpen.Features
class CompoundJoinWeld(NXOpen.Features.Feature): 
    """ Represents a compound join weld feature. """
    def GetArrowSideWelds(self) -> List[NXOpen.Features.Feature]:
        """
         Get the join feature tags, if any, from the arrow side of a compound join weld feature.
         Returns arrowSideWelds ( NXOpen.Features.Feature Li): .
        """
        pass
    def GetOtherSideWelds(self) -> List[NXOpen.Features.Feature]:
        """
         Get the weld feature tags, if any, from the Other Side of a weld feature. 
         Returns otherSideWelds ( NXOpen.Features.Feature Li): .
        """
        pass
    def GetOwningCompoundWelds(self) -> List[CompoundJoinWeld]:
        """
         Get a list of NXOpen.Join.CompoundJoinWeld from a compound join weld feature.
         Returns compoundJoinWeldFeatures ( CompoundJoinWeld List[NXO): .
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class CurveJoinBuilder(JoinBuilder): 
    """
    Represents a NXOpen.Join.CurveJoin builder.
    """
    class BodyType(Enum):
        """
        Members Include: 
         |NotSet|  Do not output a body. 
         |Solid|  Output solid body. 
         |Sheet|  Output sheet body. 

        """
        NotSet: int
        Solid: int
        Sheet: int
        @staticmethod
        def ValueOf(value: int) -> CurveJoinBuilder.BodyType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CatTailLengthOptions(Enum):
        """
        Members Include: 
         |ScaleFactor|  Factor applied to leg length of original weld extent. 
         |Value|  Length option to provide cat tail length in actual value. 

        """
        ScaleFactor: int
        Value: int
        @staticmethod
        def ValueOf(value: int) -> CurveJoinBuilder.CatTailLengthOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CatTailLocationTypes(Enum):
        """
        Members Include: 
         |StartAndEnd| 
         |Start| 
         |End| 

        """
        StartAndEnd: int
        Start: int
        End: int
        @staticmethod
        def ValueOf(value: int) -> CurveJoinBuilder.CatTailLocationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ConnectedPartsType(Enum):
        """
        Members Include: 
         |Two|  Two connected parts were used to define the plug weld. 
         |Three|  Three connected parts were used to define the plug weld. 

        """
        Two: int
        Three: int
        @staticmethod
        def ValueOf(value: int) -> CurveJoinBuilder.ConnectedPartsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ContourType(Enum):
        """
        Members Include: 
         |NotSet|  straight line 
         |Flush|  straight line 
         |Concave|  concave corner shape 
         |Convex|  convex corner shape 

        """
        NotSet: int
        Flush: int
        Concave: int
        Convex: int
        @staticmethod
        def ValueOf(value: int) -> CurveJoinBuilder.ContourType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EdgePrepType(Enum):
        """
        Members Include: 
         |EntireLength|  Entire length of solid will be modified. 
         |Limits|  Only portion of solid within the specified limits will be modified. 

        """
        EntireLength: int
        Limits: int
        @staticmethod
        def ValueOf(value: int) -> CurveJoinBuilder.EdgePrepType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FillFaceSlotsOnSetType(Enum):
        """
        Members Include: 
         |NotSet|  No filling of face slots is requested. 
         |Set1|  Slots should be filled only on Face Set 1 faces. 
         |Set2|  Slots should be filled only on Face Set 2 faces. 
         |Both|  Slots should be filled on both Face Sets' faces. 

        """
        NotSet: int
        Set1: int
        Set2: int
        Both: int
        @staticmethod
        def ValueOf(value: int) -> CurveJoinBuilder.FillFaceSlotsOnSetType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LapFilletLocationOption(Enum):
        """
        Members Include: 
         |Both|  Fillets will be created on both sides of lap solids. 
         |PlacementEdge|  Fillet will be created along the placement edges only. 

        """
        Both: int
        PlacementEdge: int
        @staticmethod
        def ValueOf(value: int) -> CurveJoinBuilder.LapFilletLocationOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ShapeType(Enum):
        """
        Members Include: 
         |Sketch|  Use sketch to define profile shape. 
         |Tube|  Create tube along the path.         
         |Ellipse|  Create ellipse along the path.      
         |Rectangle|  Create rectangle along the path.    
         |FillCorner|  Fill corner between face sets.      
         |SquareButt|  Square Butt Groove profile shape.   
         |VGroove|  V Groove profile shape.             
         |BevelGroove|  Bevel Groove profile shape.         
         |UGroove|  U Groove profile shape.             
         |JGroove|  J Groove profile shape.             
         |FlareVGroove|  Flare V Groove profile shape.       
         |FlareBevelGroove|  Flare Bevel Groove profile shape.   
         |ButtJoint|  Butt joint defintion.               
         |Plug|  Plug shape to fill a hole.          
         |TJoint|  T-joint definition.                 
         |CornerJoint|  Corner joint definition.            
         |LapJoint|  Lap joint definition.               

        """
        Sketch: int
        Tube: int
        Ellipse: int
        Rectangle: int
        FillCorner: int
        SquareButt: int
        VGroove: int
        BevelGroove: int
        UGroove: int
        JGroove: int
        FlareVGroove: int
        FlareBevelGroove: int
        ButtJoint: int
        Plug: int
        TJoint: int
        CornerJoint: int
        LapJoint: int
        @staticmethod
        def ValueOf(value: int) -> CurveJoinBuilder.ShapeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SkipFeatureType(Enum):
        """
        Members Include: 
         |NumberLength| 
         |PitchLength| 

        """
        NumberLength: int
        PitchLength: int
        @staticmethod
        def ValueOf(value: int) -> CurveJoinBuilder.SkipFeatureType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TaperType(Enum):
        """
        Members Include: 
         |FromTop|  Taper will be measured from groove side face 
         |FromEnd|  Taper will be measured from groove end caps  

        """
        FromTop: int
        FromEnd: int
        @staticmethod
        def ValueOf(value: int) -> CurveJoinBuilder.TaperType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AlignFilletToPartEdge(self) -> bool:
        """
        Getter for property: (bool) AlignFilletToPartEdge
         Returns the flush creation flag for fillet.  
           If true, fillet solid will be aligned with the part edge.   
         
        """
        pass
    @AlignFilletToPartEdge.setter
    def AlignFilletToPartEdge(self, status: bool):
        """
        Setter for property: (bool) AlignFilletToPartEdge
         Returns the flush creation flag for fillet.  
           If true, fillet solid will be aligned with the part edge.   
         
        """
        pass
    @property
    def AlignGrooveToPartEdge(self) -> bool:
        """
        Getter for property: (bool) AlignGrooveToPartEdge
         Returns the flush creation flag.  
           If true, groove solid will be extended to the part edge and then trimmed.   
         
        """
        pass
    @AlignGrooveToPartEdge.setter
    def AlignGrooveToPartEdge(self, status: bool):
        """
        Setter for property: (bool) AlignGrooveToPartEdge
         Returns the flush creation flag.  
           If true, groove solid will be extended to the part edge and then trimmed.   
         
        """
        pass
    @property
    def AltOriginPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) AltOriginPoint
         Returns the alternative origin for generated closed extent curve   
            
         
        """
        pass
    @AltOriginPoint.setter
    def AltOriginPoint(self, originPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) AltOriginPoint
         Returns the alternative origin for generated closed extent curve   
            
         
        """
        pass
    @property
    def BodyColor(self) -> int:
        """
        Getter for property: (int) BodyColor
         Returns the path body color value   
            
         
        """
        pass
    @BodyColor.setter
    def BodyColor(self, bodyColor: int):
        """
        Setter for property: (int) BodyColor
         Returns the path body color value   
            
         
        """
        pass
    @property
    def CalculatedPitch(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CalculatedPitch
         Returns the computed pitch when when  NXOpen::Join::CurveJoinBuilder::SkipFeatureType  is   NXOpen::Join::CurveJoinBuilder::SkipFeatureTypePitchLength     
            
         
        """
        pass
    @property
    def CatTailEndAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CatTailEndAngle
         Returns the end angle of cat tail   
            
         
        """
        pass
    @property
    def CatTailEndLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CatTailEndLength
         Returns the end length of cat tail   
            
         
        """
        pass
    @property
    def CatTailEndLengthType(self) -> CurveJoinBuilder.CatTailLengthOptions:
        """
        Getter for property: ( CurveJoinBuilder.CatTailLengthOptions NXOpe) CatTailEndLengthType
         Returns the cat tail end length type  
            
         
        """
        pass
    @CatTailEndLengthType.setter
    def CatTailEndLengthType(self, catTailEndLengthType: CurveJoinBuilder.CatTailLengthOptions):
        """
        Setter for property: ( CurveJoinBuilder.CatTailLengthOptions NXOpe) CatTailEndLengthType
         Returns the cat tail end length type  
            
         
        """
        pass
    @property
    def CatTailEndScaleFactor(self) -> float:
        """
        Getter for property: (float) CatTailEndScaleFactor
         Returns the cat tail end scale factor.  
             
         
        """
        pass
    @CatTailEndScaleFactor.setter
    def CatTailEndScaleFactor(self, catTailEndScaleFactor: float):
        """
        Setter for property: (float) CatTailEndScaleFactor
         Returns the cat tail end scale factor.  
             
         
        """
        pass
    @property
    def CatTailLocation(self) -> CurveJoinBuilder.CatTailLocationTypes:
        """
        Getter for property: ( CurveJoinBuilder.CatTailLocationTypes NXOpe) CatTailLocation
         Returns the cat tail location   
            
         
        """
        pass
    @CatTailLocation.setter
    def CatTailLocation(self, catTailLocation: CurveJoinBuilder.CatTailLocationTypes):
        """
        Setter for property: ( CurveJoinBuilder.CatTailLocationTypes NXOpe) CatTailLocation
         Returns the cat tail location   
            
         
        """
        pass
    @property
    def CatTailStartAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CatTailStartAngle
         Returns the start angle of cat tail   
            
         
        """
        pass
    @property
    def CatTailStartLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CatTailStartLength
         Returns the start length of cat tail   
            
         
        """
        pass
    @property
    def CatTailStartLengthType(self) -> CurveJoinBuilder.CatTailLengthOptions:
        """
        Getter for property: ( CurveJoinBuilder.CatTailLengthOptions NXOpe) CatTailStartLengthType
         Returns the cat tail start length type  
            
         
        """
        pass
    @CatTailStartLengthType.setter
    def CatTailStartLengthType(self, catTailStartLengthType: CurveJoinBuilder.CatTailLengthOptions):
        """
        Setter for property: ( CurveJoinBuilder.CatTailLengthOptions NXOpe) CatTailStartLengthType
         Returns the cat tail start length type  
            
         
        """
        pass
    @property
    def CatTailStartScaleFactor(self) -> float:
        """
        Getter for property: (float) CatTailStartScaleFactor
         Returns the cat tail start scale factor.  
             
         
        """
        pass
    @CatTailStartScaleFactor.setter
    def CatTailStartScaleFactor(self, catTailStartScaleFactor: float):
        """
        Setter for property: (float) CatTailStartScaleFactor
         Returns the cat tail start scale factor.  
             
         
        """
        pass
    @property
    def ConnectionType(self) -> CurveJoinBuilder.ConnectedPartsType:
        """
        Getter for property: ( CurveJoinBuilder.ConnectedPartsType NXOpe) ConnectionType
         Returns the plug weld connection value   
            
         
        """
        pass
    @ConnectionType.setter
    def ConnectionType(self, connectedPartsType: CurveJoinBuilder.ConnectedPartsType):
        """
        Setter for property: ( CurveJoinBuilder.ConnectedPartsType NXOpe) ConnectionType
         Returns the plug weld connection value   
            
         
        """
        pass
    @property
    def ContourHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ContourHeight
         Returns the contour height   
            
         
        """
        pass
    @property
    def CreateCatTails(self) -> bool:
        """
        Getter for property: (bool) CreateCatTails
         Returns the flag to indicate if cat tails should be created.  
             
         
        """
        pass
    @CreateCatTails.setter
    def CreateCatTails(self, createCatTails: bool):
        """
        Setter for property: (bool) CreateCatTails
         Returns the flag to indicate if cat tails should be created.  
             
         
        """
        pass
    @property
    def CreateSkipFeatures(self) -> bool:
        """
        Getter for property: (bool) CreateSkipFeatures
         Returns the flag to indicate if skip features should be created.  
             
         
        """
        pass
    @CreateSkipFeatures.setter
    def CreateSkipFeatures(self, createSkipFeatures: bool):
        """
        Setter for property: (bool) CreateSkipFeatures
         Returns the flag to indicate if skip features should be created.  
             
         
        """
        pass
    @property
    def CreateSolid(self) -> bool:
        """
        Getter for property: (bool) CreateSolid
         Returns the solid creation status.  
           If true, soild should be created in connected bodies. If false, no solid would be generated.   
         
        """
        pass
    @CreateSolid.setter
    def CreateSolid(self, status: bool):
        """
        Setter for property: (bool) CreateSolid
         Returns the solid creation status.  
           If true, soild should be created in connected bodies. If false, no solid would be generated.   
         
        """
        pass
    @property
    def CurveSelSection(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) CurveSelSection
         Returns the selected curve section   
            
         
        """
        pass
    @property
    def EdgePrepMethod(self) -> CurveJoinBuilder.EdgePrepType:
        """
        Getter for property: ( CurveJoinBuilder.EdgePrepType NXOpe) EdgePrepMethod
         Returns the edge preparation method value   
            
         
        """
        pass
    @EdgePrepMethod.setter
    def EdgePrepMethod(self, edgePrepMethod: CurveJoinBuilder.EdgePrepType):
        """
        Setter for property: ( CurveJoinBuilder.EdgePrepType NXOpe) EdgePrepMethod
         Returns the edge preparation method value   
            
         
        """
        pass
    @property
    def EdgeSection1(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) EdgeSection1
         Returns the primary selected edges   
            
         
        """
        pass
    @property
    def EdgeSection2(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) EdgeSection2
         Returns the secondary selected edges   
            
         
        """
        pass
    @property
    def EllipseSemiMajorAxis(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EllipseSemiMajorAxis
         Returns the ellipse semi-major axis   
            
         
        """
        pass
    @property
    def EllipseSemiMinorAxis(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EllipseSemiMinorAxis
         Returns the ellipse semi-minor axis   
            
         
        """
        pass
    @property
    def EndDistance(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) EndDistance
         Returns the end distance used to limit the length of the output curve  
            
         
        """
        pass
    @property
    def EndTaperAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndTaperAngle
         Returns the groove end taper angle   
            
         
        """
        pass
    @property
    def ExtensionDistance1(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ExtensionDistance1
         Returns the primary extension distance   
            
         
        """
        pass
    @property
    def ExtensionDistance2(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ExtensionDistance2
         Returns the secondary extension distance   
            
         
        """
        pass
    @property
    def FaceCollector1(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FaceCollector1
         Returns the primary selected faces   
            
         
        """
        pass
    @property
    def FaceCollector2(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FaceCollector2
         Returns the secondary selected faces   
            
         
        """
        pass
    @property
    def FaceCollector3(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FaceCollector3
         Returns the third selected faces   
            
         
        """
        pass
    @property
    def FillFaceHoles(self) -> bool:
        """
        Getter for property: (bool) FillFaceHoles
         Returns the face hole fill status.  
           If true, holes in faces should be filled. If false, then no hole filling will happen.   
         
        """
        pass
    @FillFaceHoles.setter
    def FillFaceHoles(self, status: bool):
        """
        Setter for property: (bool) FillFaceHoles
         Returns the face hole fill status.  
           If true, holes in faces should be filled. If false, then no hole filling will happen.   
         
        """
        pass
    @property
    def FillFaceSlotsGap(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FillFaceSlotsGap
         Returns the fillet weld fill face slot gap value   
            
         
        """
        pass
    @property
    def FillFaceSlotsOnSet(self) -> CurveJoinBuilder.FillFaceSlotsOnSetType:
        """
        Getter for property: ( CurveJoinBuilder.FillFaceSlotsOnSetType NXOpe) FillFaceSlotsOnSet
         Returns the fillet weld fill face slots value   
            
         
        """
        pass
    @FillFaceSlotsOnSet.setter
    def FillFaceSlotsOnSet(self, fillFaceSlotsOnSetType: CurveJoinBuilder.FillFaceSlotsOnSetType):
        """
        Setter for property: ( CurveJoinBuilder.FillFaceSlotsOnSetType NXOpe) FillFaceSlotsOnSet
         Returns the fillet weld fill face slots value   
            
         
        """
        pass
    @property
    def GrooveAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) GrooveAngle
         Returns the angle of groove   
            
         
        """
        pass
    @property
    def GrooveDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) GrooveDepth
         Returns the depth for groove   
            
         
        """
        pass
    @property
    def GrooveRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) GrooveRadius
         Returns the radius of groove   
            
         
        """
        pass
    @property
    def InferFaceInfoFromSelection(self) -> bool:
        """
        Getter for property: (bool) InferFaceInfoFromSelection
         Returns the flag to indicate if face related fields should be populated based on curve selection.  
             
         
        """
        pass
    @InferFaceInfoFromSelection.setter
    def InferFaceInfoFromSelection(self, inferFaceInfoFromSelection: bool):
        """
        Setter for property: (bool) InferFaceInfoFromSelection
         Returns the flag to indicate if face related fields should be populated based on curve selection.  
             
         
        """
        pass
    @property
    def JointMarkFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) JointMarkFace
         Returns the face for joint mark placement   
            
         
        """
        pass
    @property
    def JointMarkSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) JointMarkSize
         Returns the joint mark size   
            
         
        """
        pass
    @property
    def LapFilletLocation(self) -> CurveJoinBuilder.LapFilletLocationOption:
        """
        Getter for property: ( CurveJoinBuilder.LapFilletLocationOption NXOpe) LapFilletLocation
         Returns the lap fillet location   
            
         
        """
        pass
    @LapFilletLocation.setter
    def LapFilletLocation(self, location: CurveJoinBuilder.LapFilletLocationOption):
        """
        Setter for property: ( CurveJoinBuilder.LapFilletLocationOption NXOpe) LapFilletLocation
         Returns the lap fillet location   
            
         
        """
        pass
    @property
    def MinimumPitch(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumPitch
         Returns the minimum desired pitch between skip features.  
           Only used when  NXOpen::Join::CurveJoinBuilder::SkipFeatureType  is   NXOpen::Join::CurveJoinBuilder::SkipFeatureTypePitchLength     
         
        """
        pass
    @property
    def NumberOfSkips(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NumberOfSkips
         Returns the number of skip features to create.  
             
         
        """
        pass
    @property
    def PathSolidBodyType(self) -> CurveJoinBuilder.BodyType:
        """
        Getter for property: ( CurveJoinBuilder.BodyType NXOpe) PathSolidBodyType
         Returns the path solid body type to output   
            
         
        """
        pass
    @PathSolidBodyType.setter
    def PathSolidBodyType(self, bodyType: CurveJoinBuilder.BodyType):
        """
        Setter for property: ( CurveJoinBuilder.BodyType NXOpe) PathSolidBodyType
         Returns the path solid body type to output   
            
         
        """
        pass
    @property
    def PickFace1(self) -> NXOpen.Face:
        """
        Getter for property: ( NXOpen.Face) PickFace1
         Returns the pick face associated with  NXOpen::Join::CurveJoinBuilder::FaceCollector1    
            
         
        """
        pass
    @PickFace1.setter
    def PickFace1(self, pickFace1: NXOpen.Face):
        """
        Setter for property: ( NXOpen.Face) PickFace1
         Returns the pick face associated with  NXOpen::Join::CurveJoinBuilder::FaceCollector1    
            
         
        """
        pass
    @property
    def PickFace2(self) -> NXOpen.Face:
        """
        Getter for property: ( NXOpen.Face) PickFace2
         Returns the pick face associated with  NXOpen::Join::CurveJoinBuilder::FaceCollector2    
            
         
        """
        pass
    @PickFace2.setter
    def PickFace2(self, pickFace2: NXOpen.Face):
        """
        Setter for property: ( NXOpen.Face) PickFace2
         Returns the pick face associated with  NXOpen::Join::CurveJoinBuilder::FaceCollector2    
            
         
        """
        pass
    @property
    def PickPoint1(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) PickPoint1
         Returns the pick point associated with  NXOpen::Join::CurveJoinBuilder::FaceCollector1    
            
         
        """
        pass
    @PickPoint1.setter
    def PickPoint1(self, pickPoint1: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) PickPoint1
         Returns the pick point associated with  NXOpen::Join::CurveJoinBuilder::FaceCollector1    
            
         
        """
        pass
    @property
    def PickPoint2(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) PickPoint2
         Returns the pick point associated with  NXOpen::Join::CurveJoinBuilder::FaceCollector2    
            
         
        """
        pass
    @PickPoint2.setter
    def PickPoint2(self, pickPoint2: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) PickPoint2
         Returns the pick point associated with  NXOpen::Join::CurveJoinBuilder::FaceCollector2    
            
         
        """
        pass
    @property
    def ProfileContourType(self) -> CurveJoinBuilder.ContourType:
        """
        Getter for property: ( CurveJoinBuilder.ContourType NXOpe) ProfileContourType
         Returns the profile contour type value   
            
         
        """
        pass
    @ProfileContourType.setter
    def ProfileContourType(self, contourType: CurveJoinBuilder.ContourType):
        """
        Setter for property: ( CurveJoinBuilder.ContourType NXOpe) ProfileContourType
         Returns the profile contour type value   
            
         
        """
        pass
    @property
    def ProfileDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ProfileDiameter
         Returns the profile diameter   
            
         
        """
        pass
    @property
    def ProfileDimension1(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ProfileDimension1
         Returns the profile first dimension   
            
         
        """
        pass
    @property
    def ProfileDimension2(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ProfileDimension2
         Returns the profile second dimension   
            
         
        """
        pass
    @property
    def ProfileType(self) -> CurveJoinBuilder.ShapeType:
        """
        Getter for property: ( CurveJoinBuilder.ShapeType NXOpe) ProfileType
         Returns the profile type value   
            
         
        """
        pass
    @ProfileType.setter
    def ProfileType(self, profileType: CurveJoinBuilder.ShapeType):
        """
        Setter for property: ( CurveJoinBuilder.ShapeType NXOpe) ProfileType
         Returns the profile type value   
            
         
        """
        pass
    @property
    def RectangleBase(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RectangleBase
         Returns the rectangle base   
            
         
        """
        pass
    @property
    def RectangleHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RectangleHeight
         Returns the rectangle height   
            
         
        """
        pass
    @property
    def RootDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RootDepth
         Returns the root depth for groove   
            
         
        """
        pass
    @property
    def RootOpening(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RootOpening
         Returns the root opening for groove   
            
         
        """
        pass
    @property
    def SegmentLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SegmentLength
         Returns the segment length for each skip feature.  
             
         
        """
        pass
    @property
    def SketchSection(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) SketchSection
         Returns the sketch profile's section   
            
         
        """
        pass
    @property
    def SkipFeatureMethod(self) -> CurveJoinBuilder.SkipFeatureType:
        """
        Getter for property: ( CurveJoinBuilder.SkipFeatureType NXOpe) SkipFeatureMethod
         Returns the skip feature spacing method   
            
         
        """
        pass
    @SkipFeatureMethod.setter
    def SkipFeatureMethod(self, skipFeatureMethod: CurveJoinBuilder.SkipFeatureType):
        """
        Setter for property: ( CurveJoinBuilder.SkipFeatureType NXOpe) SkipFeatureMethod
         Returns the skip feature spacing method   
            
         
        """
        pass
    @property
    def StartDistance(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) StartDistance
         Returns the start distance used to limit the length of the output curve  
            
         
        """
        pass
    @property
    def StartTaperAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartTaperAngle
         Returns the groove start taper angle   
            
         
        """
        pass
    @property
    def TaperMethod(self) -> CurveJoinBuilder.TaperType:
        """
        Getter for property: ( CurveJoinBuilder.TaperType NXOpe) TaperMethod
         Returns the groove taper method value   
            
         
        """
        pass
    @TaperMethod.setter
    def TaperMethod(self, taperMethod: CurveJoinBuilder.TaperType):
        """
        Setter for property: ( CurveJoinBuilder.TaperType NXOpe) TaperMethod
         Returns the groove taper method value   
            
         
        """
        pass
    @property
    def ThroatThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ThroatThickness
         Returns the throat thickness   
            
         
        """
        pass
    @property
    def UseFaceSet1ForProjection(self) -> bool:
        """
        Getter for property: (bool) UseFaceSet1ForProjection
         Returns the flag to indicate if selected curves should be projected onto face set 1.  
             
         
        """
        pass
    @UseFaceSet1ForProjection.setter
    def UseFaceSet1ForProjection(self, useFaceSet1ForProjection: bool):
        """
        Setter for property: (bool) UseFaceSet1ForProjection
         Returns the flag to indicate if selected curves should be projected onto face set 1.  
             
         
        """
        pass
    @property
    def UseThroatThickness(self) -> bool:
        """
        Getter for property: (bool) UseThroatThickness
         Returns the flag to indicate whether throat thickness should be used to calculate profile dimensions.  
             
         
        """
        pass
    @UseThroatThickness.setter
    def UseThroatThickness(self, status: bool):
        """
        Setter for property: (bool) UseThroatThickness
         Returns the flag to indicate whether throat thickness should be used to calculate profile dimensions.  
             
         
        """
        pass
    @property
    def UserDefinedSolid(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: ( NXOpen.SelectBodyList) UserDefinedSolid
         Returns the selected user-defined solid   
            
         
        """
        pass
    @property
    def VisFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) VisFace
         Returns the face for visualization geometry placement   
            
         
        """
        pass
    @property
    def VisSolidType(self) -> int:
        """
        Getter for property: (int) VisSolidType
         Returns the visualization solid type value   
            
         
        """
        pass
    @VisSolidType.setter
    def VisSolidType(self, visSolidType: int):
        """
        Setter for property: (int) VisSolidType
         Returns the visualization solid type value   
            
         
        """
        pass
    @property
    def VisTubeDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) VisTubeDiameter
         Returns the visualization solid tube diameter   
            
         
        """
        pass
    @property
    def VisualizationColor(self) -> int:
        """
        Getter for property: (int) VisualizationColor
         Returns the visualization color value   
            
         
        """
        pass
    @VisualizationColor.setter
    def VisualizationColor(self, visualizationColor: int):
        """
        Setter for property: (int) VisualizationColor
         Returns the visualization color value   
            
         
        """
        pass
    @property
    def WeldSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) WeldSize
         Returns the weld size for flare groove   
            
         
        """
        pass
    def ChangeGeneratedExtentCurveOrigin(self, point: NXOpen.Point) -> None:
        """
         Changes origin of generated extent curve 
        """
        pass
    def GenerateExtentCurve(self) -> None:
        """
         Generates extent curve 
        """
        pass
import NXOpen.Features
class CurveJoin(NXOpen.Features.BodyFeature): 
    """ Represents a curve based join feature """
    pass
import NXOpen
class CurveSelectBuilder(NXOpen.Builder): 
    """ Represents a CurveSelectBuilder class """
    @property
    def CurveSelect(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) CurveSelect
         Returns the selected curve   
            
         
        """
        pass
import NXOpen
import NXOpen.Features
class EdgePrepBuilder(NXOpen.Features.FeatureBuilder): 
    """ A builder used to create or edit a NXOpen.Join.EdgePrep feature. """
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance for constructing the edge prep feature.  
             
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance for constructing the edge prep feature.  
             
         
        """
        pass
    @property
    def ErrorCode(self) -> int:
        """
        Getter for property: (int) ErrorCode
         Returns the error code for the first curve join that could not be processed.  
             
         
        """
        pass
    @property
    def JoinObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) JoinObjects
         Returns the curve joins to drive edge preparation   
            
         
        """
        pass
    def GetNoResultsInfo(self) -> List[NXOpen.Features.Feature]:
        """
         Returns the curves that edge preparation was attempted on, but could not be performed. 
         Returns curveJoinFeatures ( NXOpen.Features.Feature Li):  The curve join features that edge preparation failed on. .
        """
        pass
import NXOpen.Features
class EdgePrep(NXOpen.Features.BodyFeature): 
    """ Represents a Join Edge Prep feature """
    pass
import NXOpen
class EditCurveJoinDefinitionBuilder(NXOpen.Builder): 
    """ Represents a EditCurveJoinDefinitionBuilder class """
    @property
    def CurveJoin(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) CurveJoin
         Returns the  Join::CurveJoin  to be edited   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class EditCurveJoinParametersBuilder(NXOpen.Builder): 
    """ Used to view or edit the values used to define the joint and edge preparation. """
    class Option(Enum):
        """
        Members Include: 
         |Entered|  Use the values entered as edge prep values. 
         |Computed|  Use the computed values as edge prep values. 

        """
        Entered: int
        Computed: int
        @staticmethod
        def ValueOf(value: int) -> EditCurveJoinParametersBuilder.Option:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EdgesPrepared(self) -> bool:
        """
        Getter for property: (bool) EdgesPrepared
         Returns the indication that the edges are prepared   
            
         
        """
        pass
    @EdgesPrepared.setter
    def EdgesPrepared(self, prepared: bool):
        """
        Setter for property: (bool) EdgesPrepared
         Returns the indication that the edges are prepared   
            
         
        """
        pass
    @property
    def EditingManagedAttributeGroup(self) -> bool:
        """
        Getter for property: (bool) EditingManagedAttributeGroup
         Returns the indication that the modifications will be applied to a Managed Attribute Group, not the feature   
            
         
        """
        pass
    @EditingManagedAttributeGroup.setter
    def EditingManagedAttributeGroup(self, editingManagedAttributeGroup: bool):
        """
        Setter for property: (bool) EditingManagedAttributeGroup
         Returns the indication that the modifications will be applied to a Managed Attribute Group, not the feature   
            
         
        """
        pass
    @property
    def Joint(self) -> NXOpen.SelectCurveList:
        """
        Getter for property: ( NXOpen.SelectCurveList) Joint
         Returns the joint curves.  
             
         
        """
        pass
    @property
    def JointExitBuilder(self) -> JointExitBuilder:
        """
        Getter for property: ( JointExitBuilder NXOpe) JointExitBuilder
         Returns the  NXOpen::Weld::JointExitBuilder .  
             
         
        """
        pass
    @property
    def LeaveLooseEndValue(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) LeaveLooseEndValue
         Returns the distance from the end of the joint to not weld (i.  
          e., leave loose).   
         
        """
        pass
    @property
    def LeaveLooseStartValue(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) LeaveLooseStartValue
         Returns the distance from the start of the joint to not weld (i.  
          e., leave loose).   
         
        """
        pass
    @property
    def PrimaryThicknessUser(self) -> float:
        """
        Getter for property: (float) PrimaryThicknessUser
         Returns the user defined value for primary thickness   
            
         
        """
        pass
    @PrimaryThicknessUser.setter
    def PrimaryThicknessUser(self, thickness: float):
        """
        Setter for property: (float) PrimaryThicknessUser
         Returns the user defined value for primary thickness   
            
         
        """
        pass
    @property
    def RootOpening(self) -> float:
        """
        Getter for property: (float) RootOpening
         Returns the root opening   
            
         
        """
        pass
    @RootOpening.setter
    def RootOpening(self, rootOpening: float):
        """
        Setter for property: (float) RootOpening
         Returns the root opening   
            
         
        """
        pass
    @property
    def SecondaryThicknessUser(self) -> float:
        """
        Getter for property: (float) SecondaryThicknessUser
         Returns the user defined value for secondary thickness   
            
         
        """
        pass
    @SecondaryThicknessUser.setter
    def SecondaryThicknessUser(self, thickness: float):
        """
        Setter for property: (float) SecondaryThicknessUser
         Returns the user defined value for secondary thickness   
            
         
        """
        pass
    @property
    def Segment2Radius(self) -> float:
        """
        Getter for property: (float) Segment2Radius
         Returns the segment 2 blend radius value   
            
         
        """
        pass
    @Segment2Radius.setter
    def Segment2Radius(self, radius: float):
        """
        Setter for property: (float) Segment2Radius
         Returns the segment 2 blend radius value   
            
         
        """
        pass
    @property
    def Segment4Radius(self) -> float:
        """
        Getter for property: (float) Segment4Radius
         Returns the segment 4 blend radius value   
            
         
        """
        pass
    @Segment4Radius.setter
    def Segment4Radius(self, radius: float):
        """
        Setter for property: (float) Segment4Radius
         Returns the segment 4 blend radius value   
            
         
        """
        pass
    @property
    def ValueSegment(self) -> NXOpen.SelectCurve:
        """
        Getter for property: ( NXOpen.SelectCurve) ValueSegment
         Returns the selected segment.  
             
         
        """
        pass
    @property
    def ValuesOption(self) -> EditCurveJoinParametersBuilder.Option:
        """
        Getter for property: ( EditCurveJoinParametersBuilder.Option NXOpe) ValuesOption
         Returns the values option which indicates whether the entered or computed values should be used.  
             
         
        """
        pass
    @ValuesOption.setter
    def ValuesOption(self, option: EditCurveJoinParametersBuilder.Option):
        """
        Setter for property: ( EditCurveJoinParametersBuilder.Option NXOpe) ValuesOption
         Returns the values option which indicates whether the entered or computed values should be used.  
             
         
        """
        pass
    def CreatePathCurvesForLeaveLoose(self) -> Tuple[NXOpen.Curve, NXOpen.Curve]:
        """
         Creates the path curves to be used for NXOpen.Join.EditCurveJoinParametersBuilder.LeaveLooseStartValue and NXOpen.Join.EditCurveJoinParametersBuilder.LeaveLooseEndValue. 
         Returns A tuple consisting of (path, reversedPath). 
         - path is:  NXOpen.Curve. Path curve for NXOpen.Join.EditCurveJoinParametersBuilder.LeaveLooseStartValue. .
         - reversedPath is:  NXOpen.Curve. Reversed Path Curve for NXOpen.Join.EditCurveJoinParametersBuilder.LeaveLooseEndValue. .

        """
        pass
    def DeleteExitBuilder(self) -> None:
        """
         Deletes the NXOpen.Weld.JointExitBuilder. 
        """
        pass
    def GetSegmentFromIndex(self, value: int) -> NXOpen.Curve:
        """
         Creates the path to be used for the limits. 
         Returns segment ( NXOpen.Curve):  Segment. .
        """
        pass
    def ReadEdgePrepValuesFromCurve(self, curve: NXOpen.Curve) -> None:
        """
         Reads the edge prep values from joint curve. 
        """
        pass
    def RecreateCurves(self) -> None:
        """
         Recreate sketch curves for dialog preview. 
        """
        pass
import NXOpen
class ExportJoinBuilder(NXOpen.Builder): 
    """ Represents a ExportJoinBuilder class """
    class OutputType(Enum):
        """
        Members Include: 
         |IntermediateFile| 
         |XMLFile| 

        """
        IntermediateFile: int
        XMLFile: int
        @staticmethod
        def ValueOf(value: int) -> ExportJoinBuilder.OutputType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ConnectedPartAttrToggle(self) -> bool:
        """
        Getter for property: (bool) ConnectedPartAttrToggle
         Returns the connected part attribute toggle to control if read connected part attributes from join points   
            
         
        """
        pass
    @ConnectedPartAttrToggle.setter
    def ConnectedPartAttrToggle(self, connectedPartAttrToggle: bool):
        """
        Setter for property: (bool) ConnectedPartAttrToggle
         Returns the connected part attribute toggle to control if read connected part attributes from join points   
            
         
        """
        pass
    @property
    def CsvFileName(self) -> str:
        """
        Getter for property: (str) CsvFileName
         Returns the CSV file name   
            
         
        """
        pass
    @CsvFileName.setter
    def CsvFileName(self, csvFileName: str):
        """
        Setter for property: (str) CsvFileName
         Returns the CSV file name   
            
         
        """
        pass
    @property
    def JoinPoints(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) JoinPoints
         Returns the join points to be exported to CSV file   
            
         
        """
        pass
    @property
    def Output(self) -> ExportJoinBuilder.OutputType:
        """
        Getter for property: ( ExportJoinBuilder.OutputType NXOpe) Output
         Returns the option defining where to write the output data.  
           Data will initally be written to a comma separated value file.  Later options will be added.   
         
        """
        pass
    @Output.setter
    def Output(self, outputType: ExportJoinBuilder.OutputType):
        """
        Setter for property: ( ExportJoinBuilder.OutputType NXOpe) Output
         Returns the option defining where to write the output data.  
           Data will initally be written to a comma separated value file.  Later options will be added.   
         
        """
        pass
    @property
    def ReferenceCsys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) ReferenceCsys
         Returns the reference CSYS for exported data.  
                
         
        """
        pass
    @ReferenceCsys.setter
    def ReferenceCsys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) ReferenceCsys
         Returns the reference CSYS for exported data.  
                
         
        """
        pass
    @property
    def TemplateFileName(self) -> str:
        """
        Getter for property: (str) TemplateFileName
         Returns the template file name   
            
         
        """
        pass
    @TemplateFileName.setter
    def TemplateFileName(self, templateFileName: str):
        """
        Setter for property: (str) TemplateFileName
         Returns the template file name   
            
         
        """
        pass
    @property
    def UseSelectedCsys(self) -> bool:
        """
        Getter for property: (bool) UseSelectedCsys
         Returns the option to use the CSYS associated with  NXOpen::Join::ExportJoinBuilder::ReferenceCsys     
            
         
        """
        pass
    @UseSelectedCsys.setter
    def UseSelectedCsys(self, csysToggle: bool):
        """
        Setter for property: (bool) UseSelectedCsys
         Returns the option to use the CSYS associated with  NXOpen::Join::ExportJoinBuilder::ReferenceCsys     
            
         
        """
        pass
    @property
    def XmlFileName(self) -> str:
        """
        Getter for property: (str) XmlFileName
         Returns the XML file name   
            
         
        """
        pass
    @XmlFileName.setter
    def XmlFileName(self, xmlFileName: str):
        """
        Setter for property: (str) XmlFileName
         Returns the XML file name   
            
         
        """
        pass
    def GetConnectedPartAttributes(self) -> List[str]:
        """
         Get the connected part attributes of join points 
         Returns connectedPartAttributes (List[str]):  Connected part attributes string .
        """
        pass
    def GetExportedAttributes(self) -> List[str]:
        """
         Get the attributes of join points to be exported to CSV file 
         Returns exportedAttributes (List[str]):  Exported attributes string .
        """
        pass
    def OpenFromFile(self) -> None:
        """
         Open a template file to update exported attributes. Before use it, you must set template file name. 
        """
        pass
    def ReadAttributesFromJoins(self) -> None:
        """
         Read attributes from selected joins and save to exported attributes and connected part attributes 
        """
        pass
    def RestoreDefault(self) -> None:
        """
         Restore default template to update exported attributes. Before use it, you must set template file name. 
        """
        pass
    def SaveAsDefault(self) -> None:
        """
         Save exported attributes as default template. Before use it, you must set template file name. 
        """
        pass
    def SaveToFile(self) -> None:
        """
         Save exported attributes to a template file. Before use it, you must set template file name. 
        """
        pass
    def SetConnectedPartAttributes(self, connectedPartAttributes: List[str]) -> None:
        """
         Set the connected part attributes of join points 
        """
        pass
    def SetExportedAttributes(self, exportedAttributes: List[str]) -> None:
        """
         Set the attributes of join points to be exported to CSV file 
        """
        pass
import NXOpen
class FaceIntersectionBuilder(NXOpen.Builder): 
    """ Represents a FaceIntersectionBuilder class """
    @property
    def EdgeSection1(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) EdgeSection1
         Returns the primary selected edges   
            
         
        """
        pass
    @property
    def EdgeSection2(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) EdgeSection2
         Returns the secondary selected edges   
            
         
        """
        pass
    @property
    def ExtensionDistance1(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ExtensionDistance1
         Returns the primary extension distance   
            
         
        """
        pass
    @property
    def ExtensionDistance2(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ExtensionDistance2
         Returns the secondary extension distance   
            
         
        """
        pass
    @property
    def FaceCollector1(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FaceCollector1
         Returns the primary selected faces   
            
         
        """
        pass
    @property
    def FaceCollector2(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FaceCollector2
         Returns the secondary selected faces   
            
         
        """
        pass
import NXOpen.Features
class FaceIntersection(NXOpen.Features.BodyFeature): 
    """ Represents a join face intersection feature """
    pass
import NXOpen
class FaceJoinBuilder(JoinBuilder): 
    """
    Represents a NXOpen.Join.FaceJoin builder.
    """
    class BoundaryMethodType(Enum):
        """
        Members Include: 
         |Automatic| 
         |Rectangle| 
         |Curve| 

        """
        Automatic: int
        Rectangle: int
        Curve: int
        @staticmethod
        def ValueOf(value: int) -> FaceJoinBuilder.BoundaryMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class HolesCoverageType(Enum):
        """
        Members Include: 
         |CoverTop| 
         |FillInside| 
         |DoNotCover| 

        """
        CoverTop: int
        FillInside: int
        DoNotCover: int
        @staticmethod
        def ValueOf(value: int) -> FaceJoinBuilder.HolesCoverageType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OrientationTypes(Enum):
        """
        Members Include: 
         |NormalSelectedFace| 
         |AlongVector| 

        """
        NormalSelectedFace: int
        AlongVector: int
        @staticmethod
        def ValueOf(value: int) -> FaceJoinBuilder.OrientationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class VisualizationBodyType(Enum):
        """
        Members Include: 
         |NotSet| 
         |SolidBody| 
         |SheetBody| 

        """
        NotSet: int
        SolidBody: int
        SheetBody: int
        @staticmethod
        def ValueOf(value: int) -> FaceJoinBuilder.VisualizationBodyType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class VisualizationLocationType(Enum):
        """
        Members Include: 
         |AboveFace| 
         |BelowFace| 
         |AboveBelowFace| 

        """
        AboveFace: int
        BelowFace: int
        AboveBelowFace: int
        @staticmethod
        def ValueOf(value: int) -> FaceJoinBuilder.VisualizationLocationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BoundaryMethod(self) -> FaceJoinBuilder.BoundaryMethodType:
        """
        Getter for property: ( FaceJoinBuilder.BoundaryMethodType NXOpe) BoundaryMethod
         Returns the boundary method   
            
         
        """
        pass
    @BoundaryMethod.setter
    def BoundaryMethod(self, boundaryMethod: FaceJoinBuilder.BoundaryMethodType):
        """
        Setter for property: ( FaceJoinBuilder.BoundaryMethodType NXOpe) BoundaryMethod
         Returns the boundary method   
            
         
        """
        pass
    @property
    def Corner1(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Corner1
         Returns the first corner of rectangle   
            
         
        """
        pass
    @Corner1.setter
    def Corner1(self, corner1: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Corner1
         Returns the first corner of rectangle   
            
         
        """
        pass
    @property
    def Corner2(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Corner2
         Returns the second corner of rectangle   
            
         
        """
        pass
    @Corner2.setter
    def Corner2(self, corner2: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Corner2
         Returns the second corner of rectangle   
            
         
        """
        pass
    @property
    def FaceCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FaceCollector
         Returns the selected faces   
            
         
        """
        pass
    @property
    def HolesCoverage(self) -> FaceJoinBuilder.HolesCoverageType:
        """
        Getter for property: ( FaceJoinBuilder.HolesCoverageType NXOpe) HolesCoverage
         Returns the holes coverage value   
            
         
        """
        pass
    @HolesCoverage.setter
    def HolesCoverage(self, holesCoverage: FaceJoinBuilder.HolesCoverageType):
        """
        Setter for property: ( FaceJoinBuilder.HolesCoverageType NXOpe) HolesCoverage
         Returns the holes coverage value   
            
         
        """
        pass
    @property
    def InnerBoundary(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) InnerBoundary
         Returns the section defining the inner boundary curve   
            
         
        """
        pass
    @property
    def OrientationType(self) -> FaceJoinBuilder.OrientationTypes:
        """
        Getter for property: ( FaceJoinBuilder.OrientationTypes NXOpe) OrientationType
         Returns the orientation type value   
            
         
        """
        pass
    @OrientationType.setter
    def OrientationType(self, orientationType: FaceJoinBuilder.OrientationTypes):
        """
        Setter for property: ( FaceJoinBuilder.OrientationTypes NXOpe) OrientationType
         Returns the orientation type value   
            
         
        """
        pass
    @property
    def OrientationVector(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) OrientationVector
         Returns the orientation vector   
            
         
        """
        pass
    @OrientationVector.setter
    def OrientationVector(self, orientationVector: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) OrientationVector
         Returns the orientation vector   
            
         
        """
        pass
    @property
    def OuterBoundary(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) OuterBoundary
         Returns the section defining the outer boundary curve when boundary method is 
                  NXOpen::Join::FaceJoinBuilder::BoundaryMethodTypeCurve     
            
         
        """
        pass
    @property
    def VisualizationColor(self) -> int:
        """
        Getter for property: (int) VisualizationColor
         Returns the visualization color value   
            
         
        """
        pass
    @VisualizationColor.setter
    def VisualizationColor(self, visualizationColor: int):
        """
        Setter for property: (int) VisualizationColor
         Returns the visualization color value   
            
         
        """
        pass
    @property
    def VisualizationLocation(self) -> FaceJoinBuilder.VisualizationLocationType:
        """
        Getter for property: ( FaceJoinBuilder.VisualizationLocationType NXOpe) VisualizationLocation
         Returns the visualization location method   
            
         
        """
        pass
    @VisualizationLocation.setter
    def VisualizationLocation(self, visualizationLocation: FaceJoinBuilder.VisualizationLocationType):
        """
        Setter for property: ( FaceJoinBuilder.VisualizationLocationType NXOpe) VisualizationLocation
         Returns the visualization location method   
            
         
        """
        pass
    @property
    def VisualizationThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) VisualizationThickness
         Returns the visualization thickness   
            
         
        """
        pass
    @property
    def VisualizationType(self) -> FaceJoinBuilder.VisualizationBodyType:
        """
        Getter for property: ( FaceJoinBuilder.VisualizationBodyType NXOpe) VisualizationType
         Returns the visualization type method   
            
         
        """
        pass
    @VisualizationType.setter
    def VisualizationType(self, visualizationType: FaceJoinBuilder.VisualizationBodyType):
        """
        Setter for property: ( FaceJoinBuilder.VisualizationBodyType NXOpe) VisualizationType
         Returns the visualization type method   
            
         
        """
        pass
import NXOpen.Features
class FaceJoin(NXOpen.Features.BodyFeature): 
    """ Represents a face based join feature """
    pass
import NXOpen
class FaceSelectBuilder(NXOpen.Builder): 
    """ Represents a FaceSelectBuilder class """
    @property
    def FaceSelect(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FaceSelect
         Returns the selected face   
            
         
        """
        pass
import NXOpen
class GroupJoinsBuilder(NXOpen.Builder): 
    """ Represents a join grouping utility builder. """
    class GroupingMethod(Enum):
        """
        Members Include: 
         |Standard|  A standard one, which uses different default criterias of grouping. 
         |Custom|  A custom method type uses a pre-registered callback for join grouping. 

        """
        Standard: int
        Custom: int
        @staticmethod
        def ValueOf(value: int) -> GroupJoinsBuilder.GroupingMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CustomAttributes(self) -> bool:
        """
        Getter for property: (bool) CustomAttributes
         Returns the value of custom attributes criteria.  
             
         
        """
        pass
    @CustomAttributes.setter
    def CustomAttributes(self, customAttributes: bool):
        """
        Setter for property: (bool) CustomAttributes
         Returns the value of custom attributes criteria.  
             
         
        """
        pass
    @property
    def GroupingMethodType(self) -> GroupJoinsBuilder.GroupingMethod:
        """
        Getter for property: ( GroupJoinsBuilder.GroupingMethod NXOpe) GroupingMethodType
         Returns the value of grouping type.  
             
         
        """
        pass
    @GroupingMethodType.setter
    def GroupingMethodType(self, groupingMethod: GroupJoinsBuilder.GroupingMethod):
        """
        Setter for property: ( GroupJoinsBuilder.GroupingMethod NXOpe) GroupingMethodType
         Returns the value of grouping type.  
             
         
        """
        pass
    @property
    def Hardware(self) -> bool:
        """
        Getter for property: (bool) Hardware
         Returns the value of hardware criteria.  
             
         
        """
        pass
    @Hardware.setter
    def Hardware(self, hardware: bool):
        """
        Setter for property: (bool) Hardware
         Returns the value of hardware criteria.  
             
         
        """
        pass
    @property
    def HoleRequirements(self) -> bool:
        """
        Getter for property: (bool) HoleRequirements
         Returns the value of hole requirement criteria.  
             
         
        """
        pass
    @HoleRequirements.setter
    def HoleRequirements(self, holeRequirements: bool):
        """
        Setter for property: (bool) HoleRequirements
         Returns the value of hole requirement criteria.  
             
         
        """
        pass
    @property
    def UseCustomNamingScheme(self) -> bool:
        """
        Getter for property: (bool) UseCustomNamingScheme
         Returns the value of use custom naming scheme.  
             
         
        """
        pass
    @UseCustomNamingScheme.setter
    def UseCustomNamingScheme(self, useCustomNamingScheme: bool):
        """
        Setter for property: (bool) UseCustomNamingScheme
         Returns the value of use custom naming scheme.  
             
         
        """
        pass
import NXOpen
class ImportJoinBuilder(NXOpen.Builder): 
    """ Represents a ImportJoinBuilder class """
    class OutputType(Enum):
        """
        Members Include: 
         |IntermediateFile| 

        """
        IntermediateFile: int
        @staticmethod
        def ValueOf(value: int) -> ImportJoinBuilder.OutputType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def InputFileName(self) -> str:
        """
        Getter for property: (str) InputFileName
         Returns the input file name   
            
         
        """
        pass
    @InputFileName.setter
    def InputFileName(self, inputFileName: str):
        """
        Setter for property: (str) InputFileName
         Returns the input file name   
            
         
        """
        pass
    @property
    def TemplateFileName(self) -> str:
        """
        Getter for property: (str) TemplateFileName
         Returns the template file name   
            
         
        """
        pass
    @TemplateFileName.setter
    def TemplateFileName(self, templateFileName: str):
        """
        Setter for property: (str) TemplateFileName
         Returns the template file name   
            
         
        """
        pass
import NXOpen
import NXOpen.Annotations
import NXOpen.Assemblies
import NXOpen.Features
import NXOpen.Routing
class JoinBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Base class for all NXOpen.Join builders.
    """
    class DestinationTypes(Enum):
        """
        Members Include: 
         |WorkPart|  Create new NXOpen.Join in work part. 
         |NewComponent|  Create a new componenent for each NXOpen.Join under the work part. 

        """
        WorkPart: int
        NewComponent: int
        @staticmethod
        def ValueOf(value: int) -> JoinBuilder.DestinationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MaterialAssignmentPolicyType(Enum):
        """
        Members Include: 
         |NoneAssigned| 
         |ExternallyAssigned| 
         |JoinFeatureAssigned| 

        """
        NoneAssigned: int
        ExternallyAssigned: int
        JoinFeatureAssigned: int
        @staticmethod
        def ValueOf(value: int) -> JoinBuilder.MaterialAssignmentPolicyType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RoutingCreateModeTypes(Enum):
        """
        Members Include: 
         |SingleFeature|  Create one NXOpen.Join. 
         |MultipleFeatures|  Create multiple NXOpen.Join. 

        """
        SingleFeature: int
        MultipleFeatures: int
        @staticmethod
        def ValueOf(value: int) -> JoinBuilder.RoutingCreateModeTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns the associative option for join creation   
            
         
        """
        pass
    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
         Returns the associative option for join creation   
            
         
        """
        pass
    @property
    def ConnectedBodies(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: ( NXOpen.SelectBodyList) ConnectedBodies
         Returns the Connected Bodies   
            
         
        """
        pass
    @property
    def CustomAttributesHolder(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) CustomAttributesHolder
         Returns a custom attribute holder object that holds the attributes temporarily.  
          
                The custom attributes for the  NXOpen::Features::BodyFeature  could be set on this object. 
                If the attributes match the attributes' description in the join feature description, the custom attributes are created on the feature. Otherwise, ignored.
                Do not delete this object, deletion results in undefined behavior.   
         
        """
        pass
    @property
    def DelayUpdate(self) -> bool:
        """
        Getter for property: (bool) DelayUpdate
         Returns a delayed feature update.  
           A logical true delays updating the join feature 
                when the dependency geometries change. False updates the join feature normally.   
         
        """
        pass
    @DelayUpdate.setter
    def DelayUpdate(self, delayUpdate: bool):
        """
        Setter for property: (bool) DelayUpdate
         Returns a delayed feature update.  
           A logical true delays updating the join feature 
                when the dependency geometries change. False updates the join feature normally.   
         
        """
        pass
    @property
    def Destination(self) -> JoinBuilder.DestinationTypes:
        """
        Getter for property: ( JoinBuilder.DestinationTypes NXOpe) Destination
         Returns the part destination to create new  NXOpen::Join    
            
         
        """
        pass
    @Destination.setter
    def Destination(self, type: JoinBuilder.DestinationTypes):
        """
        Setter for property: ( JoinBuilder.DestinationTypes NXOpe) Destination
         Returns the part destination to create new  NXOpen::Join    
            
         
        """
        pass
    @property
    def DistanceTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DistanceTolerance
         Returns the distance tolerance   
            
         
        """
        pass
    @property
    def Material(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) Material
         Returns the material of the join   
            
         
        """
        pass
    @Material.setter
    def Material(self, material: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) Material
         Returns the material of the join   
            
         
        """
        pass
    @property
    def MaterialActualThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaterialActualThickness
         Returns the material actual thickness   
            
         
        """
        pass
    @property
    def MaterialAssignmentPolicy(self) -> JoinBuilder.MaterialAssignmentPolicyType:
        """
        Getter for property: ( JoinBuilder.MaterialAssignmentPolicyType NXOpe) MaterialAssignmentPolicy
         Returns the material assignment policy of the join   
            
         
        """
        pass
    @MaterialAssignmentPolicy.setter
    def MaterialAssignmentPolicy(self, materialPolicy: JoinBuilder.MaterialAssignmentPolicyType):
        """
        Setter for property: ( JoinBuilder.MaterialAssignmentPolicyType NXOpe) MaterialAssignmentPolicy
         Returns the material assignment policy of the join   
            
         
        """
        pass
    @property
    def MaterialDispensedWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaterialDispensedWidth
         Returns the material dispensed width   
            
         
        """
        pass
    @property
    def NuggetDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NuggetDiameter
         Returns the nugget diameter   
            
         
        """
        pass
    @property
    def PortSelect(self) -> NXOpen.Routing.SelectPortList:
        """
        Getter for property: ( NXOpen.Routing.SelectPortList) PortSelect
         Returns the  NXOpen::Routing::Port    
            
         
        """
        pass
    @property
    def PreventDuplicates(self) -> bool:
        """
        Getter for property: (bool) PreventDuplicates
         Returns the indication to not create features if they would overlay existing join features.  
           
                    This setting will only be used during  Builder::Commit  when  NXOpen::Join::JoinBuilder::RoutingCreateModeTypes  
                    is  NXOpen::Join::JoinBuilder::RoutingCreateModeTypesMultipleFeatures  or
                    when  Builder::Commit  is called by  NXOpen::Join::RulesBasedJoinBulkCreateBuilder    
         
        """
        pass
    @PreventDuplicates.setter
    def PreventDuplicates(self, status: bool):
        """
        Setter for property: (bool) PreventDuplicates
         Returns the indication to not create features if they would overlay existing join features.  
           
                    This setting will only be used during  Builder::Commit  when  NXOpen::Join::JoinBuilder::RoutingCreateModeTypes  
                    is  NXOpen::Join::JoinBuilder::RoutingCreateModeTypesMultipleFeatures  or
                    when  Builder::Commit  is called by  NXOpen::Join::RulesBasedJoinBulkCreateBuilder    
         
        """
        pass
    @property
    def RoutingComponents(self) -> NXOpen.Assemblies.SelectComponentList:
        """
        Getter for property: ( NXOpen.Assemblies.SelectComponentList) RoutingComponents
         Returns the list of routing  NXOpen::Assemblies::Component  used to create a Pipe Join   
            
         
        """
        pass
    @property
    def RoutingCreateMode(self) -> JoinBuilder.RoutingCreateModeTypes:
        """
        Getter for property: ( JoinBuilder.RoutingCreateModeTypes NXOpe) RoutingCreateMode
         Returns the routing creation mode.  
             
         
        """
        pass
    @RoutingCreateMode.setter
    def RoutingCreateMode(self, type: JoinBuilder.RoutingCreateModeTypes):
        """
        Setter for property: ( JoinBuilder.RoutingCreateModeTypes NXOpe) RoutingCreateMode
         Returns the routing creation mode.  
             
         
        """
        pass
    @property
    def ShowConnectedBodies(self) -> bool:
        """
        Getter for property: (bool) ShowConnectedBodies
         Returns an indication of which connected bodies to include.  
             
         
        """
        pass
    @ShowConnectedBodies.setter
    def ShowConnectedBodies(self, showConnectedBodies: bool):
        """
        Setter for property: (bool) ShowConnectedBodies
         Returns an indication of which connected bodies to include.  
             
         
        """
        pass
    @property
    def Subtype(self) -> str:
        """
        Getter for property: (str) Subtype
         Returns the Subtype   
            
         
        """
        pass
    @Subtype.setter
    def Subtype(self, type: str):
        """
        Setter for property: (str) Subtype
         Returns the Subtype   
            
         
        """
        pass
    @property
    def TwoPointWeld(self) -> bool:
        """
        Getter for property: (bool) TwoPointWeld
         Returns an indication of whether to create a two point weld.  
             
         
        """
        pass
    @TwoPointWeld.setter
    def TwoPointWeld(self, status: bool):
        """
        Setter for property: (bool) TwoPointWeld
         Returns an indication of whether to create a two point weld.  
             
         
        """
        pass
    @property
    def WeldFinishMethod(self) -> NXOpen.Annotations.FinishMethod:
        """
        Getter for property: ( NXOpen.Annotations.FinishMethod) WeldFinishMethod
         Returns the weld finish method   
            
         
        """
        pass
    @WeldFinishMethod.setter
    def WeldFinishMethod(self, method: NXOpen.Annotations.FinishMethod):
        """
        Setter for property: ( NXOpen.Annotations.FinishMethod) WeldFinishMethod
         Returns the weld finish method   
            
         
        """
        pass
    def AddNewlyCreatedWaveLink(self, waveLink: NXOpen.NXObject) -> None:
        """
         Used to collect newly created wave links on the fly. 
        """
        pass
    def EvaluateFormula(self, formula: str) -> float:
        """
         Evaluates the formula string and returns the value 
         Returns formulaResult (float): .
        """
        pass
    def GetCustomAttributeType(self, title: str) -> NXOpen.NXObject.AttributeType:
        """
         Gets the attribute type from the attribute title 
         Returns type ( NXOpen.NXObject.AttributeType): .
        """
        pass
    def GetJoinBodies(self) -> List[NXOpen.Body]:
        """
         Gets visualization bodies created by NXOpen.Join of the builder. 
         Returns joinBodies ( NXOpen.Body Li):  .
        """
        pass
    def GetPortComponents(self) -> List[NXOpen.Part]:
        """
         Gets part components attached to NXOpen.Routing.Port 
         Returns parts ( NXOpen.Part Li): .
        """
        pass
    def SetCallbackFile(self, file: str) -> None:
        """
         Sets the callback file that was used for pipe join table 
        """
        pass
    def SetHideSolid(self, hideSolid: bool) -> None:
        """
         Indicates whether the output should be hidden on creation 
        """
        pass
    def SetShowThroughState(self, status: bool) -> None:
        """
         Indicates whether the output objects should show through on creation 
        """
        pass
import NXOpen
class JoinCheckMateUtils(NXOpen.Object): 
    """ Represents a utility for Join Check-Mate checkers. """
    def AreConnectedPartsFullyLoaded(pointJoin: PointJoin) -> bool:
        """
         Check whether all of the connected parts of Join.PointJoin are in fully loaded state or not.
         Returns fullyLoaded (bool): .
        """
        pass
    def GetHoleDiameter(pointJoin: PointJoin) -> float:
        """
         Gets simple hole diameter of a Join.PointJoin.
         Returns holeDiameter (float): .
        """
        pass
    def GetPointJoinStackupFirstEntryPoint(pointJoin: PointJoin) -> NXOpen.Point3d:
        """
         Gets first stackup entry point of a Join.PointJoin.
         Returns firstEntryPoint ( NXOpen.Point3d): .
        """
        pass
    def GetStackupInfo(pointJoin: PointJoin) -> PointJoinStackupInfo:
        """
         Gets stackup information of a Join.PointJoin.
         Returns stackupInfo ( PointJoinStackupInfo NXOpe): .
        """
        pass
    def LoadConnectedParts(pointJoin: PointJoin) -> None:
        """
         Load connected parts of Join.PointJoin.
        """
        pass
import NXOpen
import NXOpen.Features
class JoinedFaceFinderBuilder(NXOpen.Builder): 
    """
    Represents a builder to run the Analyze Connections command.
    """
    @property
    def ConnectionFinder(self) -> JoinedFinderBuilder:
        """
        Getter for property: ( JoinedFinderBuilder NXOpe) ConnectionFinder
         Returns the connection finder object that manages the interaction.  
             
         
        """
        pass
    @property
    def Features(self) -> NXOpen.Features.SelectFeatureList:
        """
        Getter for property: ( NXOpen.Features.SelectFeatureList) Features
         Returns the join features used to analyze connections.  
             
         
        """
        pass
    def GetResultNodes(self) -> List[NXOpen.NXObject]:
        """
         Gets all the result nodes. Each node will either be a Group entity, or feature if it cannot be grouped. 
         Returns objects ( NXOpen.NXObject Li): The array group objects, or features. .
        """
        pass
    def PerformAnalysis(self) -> None:
        """
         Process the selected join features by finding the new connected parts for each feature. 
        """
        pass
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
class JoinedFinderBuilder(NXOpen.TaggedObject): 
    """
    Represents a builder to display, manage, delete, and allow the user to
    edit Point Join features.
    """
    class FilterTypes(Enum):
        """
        Members Include: 
         |All| 
         |Passed| 
         |Warning| 
         |Failed| 
         |Saved| 
         |NotSaved| 
         |Deleted| 

        """
        All: int
        Passed: int
        Warning: int
        Failed: int
        Saved: int
        NotSaved: int
        Deleted: int
        @staticmethod
        def ValueOf(value: int) -> JoinedFinderBuilder.FilterTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Filter(self) -> JoinedFinderBuilder.FilterTypes:
        """
        Getter for property: ( JoinedFinderBuilder.FilterTypes NXOpe) Filter
         Returns the filter value to control which nodes are shown.  
             
         
        """
        pass
    @Filter.setter
    def Filter(self, filter: JoinedFinderBuilder.FilterTypes):
        """
        Setter for property: ( JoinedFinderBuilder.FilterTypes NXOpe) Filter
         Returns the filter value to control which nodes are shown.  
             
         
        """
        pass
    @property
    def GroupResults(self) -> bool:
        """
        Getter for property: (bool) GroupResults
         Returns the option to list the results grouped by feature type, and common connected parts.  
             
         
        """
        pass
    @GroupResults.setter
    def GroupResults(self, groupResults: bool):
        """
        Setter for property: (bool) GroupResults
         Returns the option to list the results grouped by feature type, and common connected parts.  
             
         
        """
        pass
    @property
    def ReassignBody(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: ( NXOpen.SelectTaggedObject) ReassignBody
         Returns the object to use when changing a connected body.  
             
         
        """
        pass
    def CenterNode(self, nodeTag: NXOpen.NXObject) -> None:
        """
         Adjusts the display of the part and fits the selected join features in the center of the graphics window. 
        """
        pass
    def ClearAllTree(self) -> None:
        """
         Clears the tree list and allows you to perform another search. 
        """
        pass
    def DeleteNode(self, nodeTag: NXOpen.NXObject) -> None:
        """
         Marks the join feature to be delete. 
        """
        pass
    def FeatureSelectObjects(self, joinFeatureTag: NXOpen.NXObject) -> List[NXOpen.TaggedObject]:
        """
         From the feature, or group entity, get an array the SelectObject entities. This list can be used to change the body in the SelectObject entity. 
         Returns selectObjects ( NXOpen.TaggedObject Li):  Array of SelectObject entities for the connected bodies. .
        """
        pass
    def GetBodies(self, joinFeature: NXOpen.Features.Feature) -> List[NXOpen.ScCollector]:
        """
         Get the body collectors for the given feature.  
         Returns bodyCollectors ( NXOpen.ScCollector Li):  Body Collectors. .
        """
        pass
    def MarkFeatureModified(self, joinFeatureTag: NXOpen.NXObject, isModified: bool) -> None:
        """
         Mark the feature or group node as modifiedunmodified. 
        """
        pass
    def ReassignBodyNode(self, ownerTag: NXOpen.NXObject, nodeTag: NXOpen.TaggedObject) -> None:
        """
         Reassign the bodies for a specified node. 
        """
        pass
    def RemoveBodyNode(self, selectObjectTag: NXOpen.TaggedObject) -> None:
        """
         Removes a connected body for a single feature, or multiple features if results are grouped. 
        """
        pass
    def SaveAllTree(self) -> None:
        """
         Identify all the connected part information as "accepted" so Builder.Commit will save the information. 
        """
        pass
import NXOpen
import NXOpen.Features
class JoinHoleBuilder(NXOpen.Builder): 
    """ Represents a Join.JoinHoleBuilder builder. """
    @property
    def PointJoins(self) -> NXOpen.Features.SelectFeatureList:
        """
        Getter for property: ( NXOpen.Features.SelectFeatureList) PointJoins
         Returns the selected point joins   
            
         
        """
        pass
import NXOpen.Features
class JoinHole(NXOpen.Features.Feature): 
    """ Represents a point join hole feature """
    pass
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
class JoinManager(NXOpen.Object): 
    """ Represents a manager of join feature builders. """
    class BuilderCallbackReason(Enum):
        """
        Members Include: 
         |Unknown|  Used only for validation. 
         |RoutingPort|  Called on routing port to determine attributes. 
         |RoutingPortMechanical|  Called for routing mechnical pipe joins to determine attributes. 
         |Count|  The number of callback reasons. 

        """
        Unknown: int
        RoutingPort: int
        RoutingPortMechanical: int
        Count: int
        @staticmethod
        def ValueOf(value: int) -> JoinManager.BuilderCallbackReason:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CallbackReason(Enum):
        """
        Members Include: 
         |Unknown|  Used only for validation. 
         |PostCommit|  Called in dialog apply processing after Join builder commit has been executed. Result of Builder.GetCommittedObjects is passed to NXOpen.Join.JoinManager.ExecuteCallback. 
         |GroupJoinsCustomMethod|  Called on apply of group joins utility. 
         |EasyJoinPoints|  Called from Easy Join to override creation of Point Join features. 
         |JointParameters|  Called to set parameters on rbsw type curve joins. 
         |TransformPostCommit|  Called in transform dialog apply processing after builder commit has been executed. Result of Builder.GetCommittedObjects is passed to NXOpen.Join.JoinManager.ExecuteCallback. 
         |PreDialogLaunch|  Called in dialog initialization processing before dialog is launched. NXOpen.Join.JoinBuilder is passed to NXOpen.Join.JoinManager.ExecuteCallback. 
         |Count|  The number of callback reasons. 

        """
        Unknown: int
        PostCommit: int
        GroupJoinsCustomMethod: int
        EasyJoinPoints: int
        JointParameters: int
        TransformPostCommit: int
        PreDialogLaunch: int
        Count: int
        @staticmethod
        def ValueOf(value: int) -> JoinManager.CallbackReason:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RoutingJoinFunction(Enum):
        """
        Members Include: 
         |PipeJoin|  Pipe Join function. 
         |Mechanical|  Mechanical function. 
         |BulkPipeJoin|  Bulk Create Pipe Join function. 
         |CreatePMI|  Join Note function. 
         |ExportJoin|  Export Join function. 

        """
        PipeJoin: int
        Mechanical: int
        BulkPipeJoin: int
        CreatePMI: int
        ExportJoin: int
        @staticmethod
        def ValueOf(value: int) -> JoinManager.RoutingJoinFunction:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RoutingJoinType(Enum):
        """
        Members Include: 
         |PipeJoin|  Pipe Join. 
         |Mechanical|  Mechanical Join. 

        """
        PipeJoin: int
        Mechanical: int
        @staticmethod
        def ValueOf(value: int) -> JoinManager.RoutingJoinType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    BuilderCallback = Callable[[JoinBuilder], None]
    def AddBuilderCallback(reason: JoinManager.BuilderCallbackReason, callbackMethod: JoinManager.BuilderCallback) -> int:
        """
         Adds the builder callback with the given reason.
                    NOTE: You can register more than one callback with the same reason. 
         Returns callbackMethodId (int):  A unique identifier for your callback. .
        """
        pass
    Callback = Callable[[List[NXOpen.NXObject]], None]
    def AddCallback(reason: JoinManager.CallbackReason, callbackMethod: JoinManager.Callback) -> int:
        """
         Adds the callback with the given reason.
                    NOTE: You can register more than one callback with the same reason. 
         Returns callbackMethodId (int):  A unique identifier for your callback. .
        """
        pass
    def AreConnectedPartsFullyLoaded(pointJoin: PointJoin) -> bool:
        """
         Check whether all of the connected parts of Join.PointJoin are in fully loaded state or not.
         Returns fullyLoaded (bool): .
        """
        pass
    def CreateAttachedHardwareBuilder(part: NXOpen.Part, attachedHardware: AttachedHardware) -> AttachedHardwareBuilder:
        """
         Creates a Join.AttachedHardwareBuilder 
         Returns builder ( AttachedHardwareBuilder NXOpe): .
        """
        pass
    def CreateAutoPointBuilder(part: NXOpen.Part) -> AutoPointBuilder:
        """
         Creates a Join.AutoPointBuilder 
         Returns builder ( AutoPointBuilder NXOpe): .
        """
        pass
    def CreateCompoundJoinWeldBuilder(part: NXOpen.Part, compoundJoinWeld: CompoundJoinWeld) -> CompoundJoinWeldBuilder:
        """
         Creates a NXOpen.Join.CompoundJoinWeldBuilder object 
         Returns builder ( CompoundJoinWeldBuilder NXOpe):  .
        """
        pass
    def CreateConnectedFaceFinderBuilder(part: NXOpen.Part, features: List[NXOpen.Features.Feature]) -> JoinedFaceFinderBuilder:
        """
         Creates a builder for running the Connected Face Finder utility. 
         Returns builder ( JoinedFaceFinderBuilder NXOpe):  .
        """
        pass
    def CreateConnectedFaceFinderOperation(part: NXOpen.Part) -> JoinedFaceFinderBuilder:
        """
         Creates a builder for running the Connected Face Finder utility. 
         Returns builder ( JoinedFaceFinderBuilder NXOpe):  .
        """
        pass
    def CreateCurveJoinBuilder(part: NXOpen.Part, curveJoin: CurveJoin) -> CurveJoinBuilder:
        """
         Creates a Join.CurveJoinBuilder 
         Returns builder ( CurveJoinBuilder NXOpe): .
        """
        pass
    def CreateCurveSelectBuilder(part: NXOpen.Part) -> CurveSelectBuilder:
        """
         Creates a NXOpen.Join.CurveSelectBuilder object. 
         Returns builder ( CurveSelectBuilder NXOpe):  CurveSelectBuilder builder.
        """
        pass
    def CreateEdgePrepBuilder(part: NXOpen.Part, edgePrepFeature: EdgePrep) -> EdgePrepBuilder:
        """
         Creates a NXOpen.Weld.EdgePrepBuilder object. 
         Returns builder ( EdgePrepBuilder NXOpe): .
        """
        pass
    def CreateEditCurveJoinDefinitionBuilder(part: NXOpen.Part) -> EditCurveJoinDefinitionBuilder:
        """
         Creates a NXOpen.Join.EditCurveJoinDefinitionBuilder object. 
         Returns builder ( EditCurveJoinDefinitionBuilder NXOpe):  EditCurveJoinDefinitionBuilder builder.
        """
        pass
    def CreateEditCurveJoinParametersBuilder(part: NXOpen.Part, parentBuilder: EditCurveJoinDefinitionBuilder) -> EditCurveJoinParametersBuilder:
        """
         Creates a NXOpen.Join.EditCurveJoinParametersBuilder object. 
         Returns builder ( EditCurveJoinParametersBuilder NXOpe):  EditCurveJoinParametersBuilder builder.
        """
        pass
    def CreateExportJoinBuilder(part: NXOpen.Part) -> ExportJoinBuilder:
        """
         Creates a NXOpen.Join.ExportJoinBuilder object. 
         Returns builder ( ExportJoinBuilder NXOpe):  ExportJoin builder.
        """
        pass
    def CreateFaceIntersectionBuilder(part: NXOpen.Part, faceIntersection: FaceIntersection) -> FaceIntersectionBuilder:
        """
         Creates a Join.FaceIntersectionBuilder 
         Returns builder ( FaceIntersectionBuilder NXOpe): .
        """
        pass
    def CreateFaceJoinBuilder(part: NXOpen.Part, faceJoin: FaceJoin) -> FaceJoinBuilder:
        """
         Creates a Join.FaceJoinBuilder 
         Returns builder ( FaceJoinBuilder NXOpe): .
        """
        pass
    def CreateFaceSelectBuilder(part: NXOpen.Part) -> FaceSelectBuilder:
        """
         Creates a NXOpen.Join.FaceSelectBuilder object. 
         Returns builder ( FaceSelectBuilder NXOpe):  FaceSelectBuilder builder.
        """
        pass
    def CreateGroupJoinsBuilder(part: NXOpen.Part) -> GroupJoinsBuilder:
        """
         Creates a Join.GroupJoinsBuilder 
         Returns builder ( GroupJoinsBuilder NXOpe): .
        """
        pass
    def CreateImportJoinBuilder(part: NXOpen.Part) -> ImportJoinBuilder:
        """
         Creates a NXOpen.Join.ImportJoinBuilder object. 
         Returns builder ( ImportJoinBuilder NXOpe):  ImportJoin builder.
        """
        pass
    def CreateJoinHoleBuilder(part: NXOpen.Part, joinHole: JoinHole) -> JoinHoleBuilder:
        """
         Creates a NXOpen.Join.JoinHoleBuilder 
         Returns builder ( JoinHoleBuilder NXOpe):  NXOpen.Join.JoinHoleBuilder to be returned .
        """
        pass
    def CreateJoinNoteBuilder(part: NXOpen.Part, annotation: NXOpen.Annotations.Annotation) -> JoinNoteBuilder:
        """
         Creates a NXOpen.Join.JoinNoteBuilder object. 
         Returns builder ( JoinNoteBuilder NXOpe):  Join Note builder.
        """
        pass
    def CreateMultiEditCurveJoinParametersBuilder(part: NXOpen.Part, parentBuilder: EditCurveJoinDefinitionBuilder) -> MultiEditCurveJoinParametersBuilder:
        """
         Creates a NXOpen.Join.MultiEditCurveJoinParametersBuilder object. 
         Returns builder ( MultiEditCurveJoinParametersBuilder NXOpe):  MultiEditCurveJoinParametersBuilder builder.
        """
        pass
    def CreateMultiEditPointJoinBuilder(part: NXOpen.Part) -> MultiEditPointJoinBuilder:
        """
         Creates a NXOpen.Join.MultiEditPointJoinBuilder object. 
         Returns builder ( MultiEditPointJoinBuilder NXOpe):  MultiEditPointJoinBuilder builder.
        """
        pass
    def CreateMultiEditPointJoinParametersBuilder(part: NXOpen.Part, parentBuilder: MultiEditPointJoinBuilder) -> MultiEditPointJoinParametersBuilder:
        """
         Creates a NXOpen.Join.MultiEditPointJoinParametersBuilder object. 
         Returns builder ( MultiEditPointJoinParametersBuilder NXOpe):  MultiEditPointJoinBuilder builder.
        """
        pass
    def CreateOverlapBuilder(part: NXOpen.Part, overlapFeature: Overlap) -> OverlapBuilder:
        """
         Creates an Join.OverlapBuilder 
         Returns builder ( OverlapBuilder NXOpe): .
        """
        pass
    def CreatePointJoinBuilder(part: NXOpen.Part, pointJoin: PointJoin) -> PointJoinBuilder:
        """
         Creates a Join.PointJoinBuilder 
         Returns builder ( PointJoinBuilder NXOpe): .
        """
        pass
    def CreatePointLayoutBuilder(part: NXOpen.Part, pointLayoutFeature: PointLayout) -> PointLayoutBuilder:
        """
         Creates an Join.PointLayoutBuilder 
         Returns builder ( PointLayoutBuilder NXOpe): .
        """
        pass
    def CreatePreferencesBuilder(part: NXOpen.Part, joinPrefs: JoinPreferences) -> PreferencesBuilder:
        """
         Creates a NXOpen.Join.PreferencesBuilder object. 
         Returns builder ( PreferencesBuilder NXOpe): .
        """
        pass
    def CreateRulesBasedJoinBulkCreateBuilder(part: NXOpen.Part) -> RulesBasedJoinBulkCreateBuilder:
        """
         Creates a NXOpen.Join.RulesBasedJoinBulkCreateBuilder object. 
         Returns builder ( RulesBasedJoinBulkCreateBuilder NXOpe):  RulesBasedJoinBulkCreateBuilder builder.
        """
        pass
    def CreateTransformBuilder(part: NXOpen.Part, feature: NXOpen.Features.Feature) -> TransformBuilder:
        """
         Creates a NXOpen.Weld.TransformBuilder object. 
         Returns builder ( TransformBuilder NXOpe):  TransformBuilder builder.
        """
        pass
    def CreateWeldSymbolBuilder(part: NXOpen.Part) -> WeldSymbolBuilder:
        """
         Creates a NXOpen.Join.WeldSymbolBuilder object. 
         Returns builder ( WeldSymbolBuilder NXOpe):  weld symbol builder.
        """
        pass
    def ExecuteBuilderCallback(reason: JoinManager.BuilderCallbackReason, builder: JoinBuilder) -> None:
        """
         Executes the Join builder callback. 
        """
        pass
    def ExecuteCallback(reason: JoinManager.CallbackReason, nxObjects: List[NXOpen.NXObject]) -> None:
        """
         Executes the Join callback. 
        """
        pass
    def GetAllNonJoinBodiesInAssembly() -> List[NXOpen.Body]:
        """
         Gets all bodies from assembly, except the visualization bodies of point joins present.
         Returns bodies ( NXOpen.Body Li): .
        """
        pass
    def GetJointCurveFromCurveJoin(joinCurveFeature: CurveJoin) -> NXOpen.Curve:
        """
         Get curve of NXOpen.Weld.WeldJoint from Join.CurveJoin. 
         Returns jointCurve ( NXOpen.Curve): .
        """
        pass
    def HideSolids(joinFeatures: List[NXOpen.NXObject], hideSolids: bool) -> None:
        """
         Method to show or hide the solid body associated with a Join.PointJoin feature in the work part. 
        """
        pass
    def IsRoutingJoinOfType(pointJoin: PointJoin, routingJoinType: JoinManager.RoutingJoinType) -> bool:
        """
         Check whether input Join.PointJoin is of mechanical pipe join type or not.
         Returns isOfTypeResult (bool): .
        """
        pass
    def LoadConnectedParts(pointJoin: PointJoin) -> None:
        """
         Load connected parts of Join.PointJoin.
        """
        pass
    def PrepareRoutingForJoinFunction(joinFunction: JoinManager.RoutingJoinFunction) -> None:
        """
         Prepares routing application for specified join function.
        """
        pass
    def RemoveAllBuilderCallbacks() -> None:
        """
         Removes all the registered builder callbacks, except those configured in the Application View (APV) file. 
        """
        pass
    def RemoveAllBuilderCallbacksForReason(reason: JoinManager.BuilderCallbackReason) -> None:
        """
         Removes all the builder callbacks registered for a particular reason. 
        """
        pass
    def RemoveAllCallbacks() -> None:
        """
         Removes all the registered callbacks, except those configured in the Application View (APV) file. 
        """
        pass
    def RemoveAllCallbacksForReason(reason: JoinManager.CallbackReason) -> None:
        """
         Removes all the callbacks registered for a particular reason. 
        """
        pass
    def RemoveBuilderCallback(callbackMethodId: int) -> None:
        """
         Removes the registered builder callback. 
        """
        pass
    def RemoveCallback(callbackMethodId: int) -> None:
        """
         Removes the registered callback. 
        """
        pass
    def RenewAllPreNX2312PointJoins(part: NXOpen.Part) -> None:
        """
         Renews all of the pre-NX2312 Join.PointJoin features to NX2312 version.
        """
        pass
    def ShowThrough(joinFeatures: List[NXOpen.NXObject], showThrough: bool) -> None:
        """
         Method to turn on or off the show through state for Join.PointJoin features in the work part. 
        """
        pass
    def UpdateStackup(joinFeatures: List[NXOpen.NXObject]) -> None:
        """
         Method to recompute the stackup for the Point Joint Feature. The method creates a build for each feature, commits it, and runs update for all changed features. 
        """
        pass
import NXOpen
import NXOpen.Annotations
class JoinNoteBuilder(NXOpen.Builder): 
    """ Create Join Annotation for multiple Join features. This builder's Commit can produce more than one object so 
        the GetCommittedObjects can be used to get the objects and the order of GetCommittedObject's output array is stable. """
    class AttrPrecision(Enum):
        """
        Members Include: 
         |Zero|  Numeric attribute will have 0 digits after the decimal. 
         |One|  Numeric attribute will have 1 digit after the decimal. 
         |Two|  Numeric attribute will have 2 digits after the decimal. 
         |Three|  Numeric attribute will have 3 digits after the decimal. 
         |Four|  Numeric attribute will have 4 digits after the decimal. 
         |Five|  Numeric attribute will have 5 digits after the decimal. 
         |Six|  Numeric attribute will have 6 digits after the decimal. 

        """
        Zero: int
        One: int
        Two: int
        Three: int
        Four: int
        Five: int
        Six: int
        @staticmethod
        def ValueOf(value: int) -> JoinNoteBuilder.AttrPrecision:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AssociatedObjects(self) -> NXOpen.Annotations.AssociatedObjectsBuilder:
        """
        Getter for property: ( NXOpen.Annotations.AssociatedObjectsBuilder) AssociatedObjects
         Returns the  NXOpen::Annotations::AssociatedObjectsBuilder  for the annotation   
            
         
        """
        pass
    @property
    def IncludeLeader(self) -> bool:
        """
        Getter for property: (bool) IncludeLeader
         Returns the leader option, indicates whether to create a leader   
            
         
        """
        pass
    @IncludeLeader.setter
    def IncludeLeader(self, leader: bool):
        """
        Setter for property: (bool) IncludeLeader
         Returns the leader option, indicates whether to create a leader   
            
         
        """
        pass
    @property
    def Joins(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Joins
         Returns the join objects to be annotated.  
             
         
        """
        pass
    @property
    def Leader(self) -> NXOpen.Annotations.LeaderBuilder:
        """
        Getter for property: ( NXOpen.Annotations.LeaderBuilder) Leader
         Returns the  NXOpen::Annotations::LeaderBuilder  for the annotation   
            
         
        """
        pass
    @property
    def Origin(self) -> NXOpen.Annotations.OriginBuilder:
        """
        Getter for property: ( NXOpen.Annotations.OriginBuilder) Origin
         Returns the origin   
            
         
        """
        pass
    @property
    def Plane(self) -> NXOpen.Annotations.PlaneBuilder:
        """
        Getter for property: ( NXOpen.Annotations.PlaneBuilder) Plane
         Returns the plane builder   
            
         
        """
        pass
    @property
    def Precision(self) -> JoinNoteBuilder.AttrPrecision:
        """
        Getter for property: ( JoinNoteBuilder.AttrPrecision NXOpe) Precision
         Returns the numeric precision used for numbers in PMI   
            
         
        """
        pass
    @Precision.setter
    def Precision(self, leader: JoinNoteBuilder.AttrPrecision):
        """
        Setter for property: ( JoinNoteBuilder.AttrPrecision NXOpe) Precision
         Returns the numeric precision used for numbers in PMI   
            
         
        """
        pass
    @property
    def Style(self) -> NXOpen.Annotations.StyleBuilder:
        """
        Getter for property: ( NXOpen.Annotations.StyleBuilder) Style
         Returns the style builder   
            
         
        """
        pass
    @property
    def Text(self) -> NXOpen.Annotations.TextWithEditControlsBuilder:
        """
        Getter for property: ( NXOpen.Annotations.TextWithEditControlsBuilder) Text
         Returns the text   
            
         
        """
        pass
import NXOpen
class JoinPreferences(NXOpen.NXObject): 
    """ Represents a NXOpen.Join.JoinPreferences """
    def GetConstructionLayer(self) -> int:
        """
        Gets a construction layer preference
         Returns constructionLayer (int): .
        """
        pass
    def GetFixTimestamp(self) -> bool:
        """
        Gets a fix time stamp preference
         Returns fixTimestamp (bool): .
        """
        pass
    def GetGroupIdSeedValue(self) -> str:
        """
        Gets a join group ID seed value preference
         Returns groupIdSeedValue (str): .
        """
        pass
    def GetOutputGeometryLayer(self) -> int:
        """
        Gets an output geometry layer preference
         Returns outputGeomLayer (int): .
        """
        pass
    def SetConstructionLayer(self, constructionLayer: int) -> None:
        """
        Sets a construction layer preference
        """
        pass
    def SetFixTimestamp(self, fixTimestamp: bool) -> None:
        """
        Sets a fix time stamp preference
        """
        pass
    def SetGroupIdSeedValue(self, groupIdSeedValue: str) -> None:
        """
        Sets a join group ID seed value preference
        """
        pass
    def SetOutputGeometryLayer(self, outputGeomLayer: int) -> None:
        """
        Sets an output geometry layer preference
        """
        pass
import NXOpen
class MultiEditCurveJoinParametersBuilder(NXOpen.Builder): 
    """ Represents a MultiEditCurveJoinParametersBuilder class """
    def GetJointExitBuilder(self, row: int) -> JointExitBuilder:
        """
         Get the NXOpen.Weld.JointExitBuilder. 
         Returns exitBuilder ( JointExitBuilder NXOpe): .
        """
        pass
    def ResetToCallbackValues(self, exitBuilder: JointExitBuilder) -> None:
        """
         Reset the values of NXOpen.Weld.JointExitBuilder to the callback values. 
        """
        pass
import NXOpen
class MultiEditPointJoinBuilder(NXOpen.Builder): 
    """ Represents a MultiEditPointJoinBuilder class """
    @property
    def JoinPoints(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) JoinPoints
         Returns the join points to be edited   
            
         
        """
        pass
import NXOpen
import NXOpen.Features
class MultiEditPointJoinParametersBuilder(NXOpen.Builder): 
    """ Represents a MultiEditPointJoinParametersBuilder class """
    def AddToDeleteList(self, objectTag: NXOpen.TaggedObject) -> None:
        """
         Adds object to be deleted on builder destroy 
        """
        pass
    def CreateLinkedCurve(self, objectValue: NXOpen.ICurve, feature: NXOpen.Features.Feature) -> NXOpen.ICurve:
        """
         Creates linked curve feature in work part. Linked curve feature is reorded before input feature 
         Returns linkedCurve ( NXOpen.ICurve):  newly created linked curve .
        """
        pass
    def CreateLinkedFace(self, face: NXOpen.Face, feature: NXOpen.Features.Feature) -> NXOpen.Face:
        """
         Creates linked face feature in work part. Linked face feature is reorded before input feature 
         Returns linkedFace ( NXOpen.Face):  newly created linked face .
        """
        pass
    def LoadHardware(self, row: int) -> None:
        """
         Loadupdate hardware for feature corresponding to table row. 
        """
        pass
    def SetAttachmentHardware(self, row: int, column: int, pinName: str, pinPath: str, pinFamilyInstanceName: str, pinTcClassId: str, pinTcClassInstanceId: str) -> None:
        """
         Set attachment hardware value for the table cell (row, colummn) 
        """
        pass
    def SetBooleanValue(self, row: int, column: int, value: bool) -> None:
        """
         Set a boolean value for the table cell (row, colummn) 
        """
        pass
    def SetDoubleValue(self, row: int, column: int, value: float) -> None:
        """
         Set a double value for the table cell (row, colummn) 
        """
        pass
    def SetExpressionValue(self, row: int, column: int, expTag: NXOpen.Expression) -> None:
        """
         Set a expression value for the table cell (row, colummn) 
        """
        pass
    def SetHardwareOrientationCurve(self, row: int, collector: NXOpen.ScCollector) -> None:
        """
         Sets collector containing curves to define alignment direction 
        """
        pass
    def SetHardwarePin(self, row: int, column: int, pinName: str, pinPath: str, pinFamilyInstanceName: str, pinTcClassId: str, pinTcClassInstanceId: str) -> None:
        """
         Set a hardware pin value for the table cell (row, colummn) 
        """
        pass
    def SetHardwarePinSpecification(self, row: int, pinSpecificationName: str, pinSpecificationDescriptiveName: str) -> None:
        """
         Set a hardware pin specification value for the table row 
        """
        pass
    def SetHeadSideParts(self, row: int, column: int, headNames: List[str], headPaths: List[str], headFamilyInstanceNames: List[str], headTcClassIds: List[str], headTcClassInstanceIds: List[str]) -> None:
        """
         Set a hardware head side parts value for the table cell (row, colummn) 
        """
        pass
    def SetIntegerValue(self, row: int, column: int, value: int) -> None:
        """
         Set an integer value for the table cell (row, colummn) 
        """
        pass
    def SetMaterial(self, row: int, column: int, material: NXOpen.PhysicalMaterial) -> None:
        """
         Sets the material in the table cell (row, colummn) 
        """
        pass
    def SetMatingFace(self, row: int, collector: NXOpen.ScCollector) -> None:
        """
         Sets collector containing faces for attachment hardware 
        """
        pass
    def SetStackupNormalSurface(self, row: int, collector: NXOpen.ScCollector) -> None:
        """
         Sets collector containing faces to define alignment direction 
        """
        pass
    def SetTailSideParts(self, row: int, column: int, tailNames: List[str], tailPaths: List[str], tailFamilyInstanceNames: List[str], tailTcClassIds: List[str], tailTcClassInstanceIds: List[str]) -> None:
        """
         Set a hardware tail side parts value for the table cell (row, colummn) 
        """
        pass
    def SetVectorTagValue(self, row: int, column: int, vector: NXOpen.Direction) -> None:
        """
         Makes a fixed vector copy of the input vector tag and sets in the table cell (row, colummn) 
        """
        pass
    def UnloadHardware(self, row: int) -> None:
        """
         Unload hardware for feature corresponding to table row. 
        """
        pass
import NXOpen
class OnPathDimension(NXOpen.TaggedObject): 
    """ Represents a NXOpen.Join.OnPathDimension.
    """
    pass
import NXOpen
import NXOpen.Features
class OverlapBuilder(NXOpen.Features.FeatureBuilder): 
    """ Used to create or edit a NXOpen.Join.Overlap feature. """
    class ConnectPartTypes(Enum):
        """
        Members Include: 
         |AllUniqueParts|  All connected parts must unique. 
         |OnlyOnePart|  All connected parts must be the same.   
         |RepeatedParts|  Connected parts do not need to be unique.  

        """
        AllUniqueParts: int
        OnlyOnePart: int
        RepeatedParts: int
        @staticmethod
        def ValueOf(value: int) -> OverlapBuilder.ConnectPartTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class GuideCurveCreationTypes(Enum):
        """
        Members Include: 
         |Manual|  User must manually specify the edges on the reference sheet. 
         |Automatic|  Automatically determine edges needed to create a centerline or offset curves on a reference sheet. 

        """
        Manual: int
        Automatic: int
        @staticmethod
        def ValueOf(value: int) -> OverlapBuilder.GuideCurveCreationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class InputDataTypes(Enum):
        """
        Members Include: 
         |Faces|  Construct the overlap sheet from faces. 
         |Bodies|  Construct the overlap sheet from bodies. 

        """
        Faces: int
        Bodies: int
        @staticmethod
        def ValueOf(value: int) -> OverlapBuilder.InputDataTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ReferenceSheetOptionTypes(Enum):
        """
        Members Include: 
         |TopTarget|  Join Reference Sheet feature is created on the top of the target body. 
         |BetweenBodies|  Join Reference Sheet feature is created between the target and tool bodies. 

        """
        TopTarget: int
        BetweenBodies: int
        @staticmethod
        def ValueOf(value: int) -> OverlapBuilder.ReferenceSheetOptionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ReferenceSheetTypes(Enum):
        """
        Members Include: 
         |Overlap|  Overlap 
         |Top|  Top     

        """
        Overlap: int
        Top: int
        @staticmethod
        def ValueOf(value: int) -> OverlapBuilder.ReferenceSheetTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ConnectPart(self) -> OverlapBuilder.ConnectPartTypes:
        """
        Getter for property: ( OverlapBuilder.ConnectPartTypes NXOpe) ConnectPart
         Returns the option of connecting only one part.  
           If true, only one face set is required.   
         
        """
        pass
    @ConnectPart.setter
    def ConnectPart(self, connectPart: OverlapBuilder.ConnectPartTypes):
        """
        Setter for property: ( OverlapBuilder.ConnectPartTypes NXOpe) ConnectPart
         Returns the option of connecting only one part.  
           If true, only one face set is required.   
         
        """
        pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance for constructing the feature.  
              
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance for constructing the feature.  
              
         
        """
        pass
    @property
    def FaceSetsList(self) -> OverlapFaceSetsBuilderList:
        """
        Getter for property: ( OverlapFaceSetsBuilderList NXOpe) FaceSetsList
         Returns the list of face sets    
            
         
        """
        pass
    @property
    def GuideCurveCreationType(self) -> OverlapBuilder.GuideCurveCreationTypes:
        """
        Getter for property: ( OverlapBuilder.GuideCurveCreationTypes NXOpe) GuideCurveCreationType
         Returns the option if sheet edges should be automatically selected.  
             
         
        """
        pass
    @GuideCurveCreationType.setter
    def GuideCurveCreationType(self, guideCurveCreationType: OverlapBuilder.GuideCurveCreationTypes):
        """
        Setter for property: ( OverlapBuilder.GuideCurveCreationTypes NXOpe) GuideCurveCreationType
         Returns the option if sheet edges should be automatically selected.  
             
         
        """
        pass
    @property
    def GuideCurvesList(self) -> OverlapGuideBuilderList:
        """
        Getter for property: ( OverlapGuideBuilderList NXOpe) GuideCurvesList
         Returns the list of guide curves   
            
         
        """
        pass
    @property
    def MaximumBendRadius(self) -> float:
        """
        Getter for property: (float) MaximumBendRadius
         Returns the radius value for which faces will be excluded from the reference sheet construction.  
           Processing time will increase when smaller values are used.   
         
        """
        pass
    @MaximumBendRadius.setter
    def MaximumBendRadius(self, maximumBendRadius: float):
        """
        Setter for property: (float) MaximumBendRadius
         Returns the radius value for which faces will be excluded from the reference sheet construction.  
           Processing time will increase when smaller values are used.   
         
        """
        pass
    @property
    def MaximumCenterlineWidth(self) -> float:
        """
        Getter for property: (float) MaximumCenterlineWidth
         Returns the maximum centerline width.  
           Points will be created using the centerline method
                if the smallest width is less than this value. If greater, points will be
                created using the offset from edge method.   
         
        """
        pass
    @MaximumCenterlineWidth.setter
    def MaximumCenterlineWidth(self, maximumCenterlineWidth: float):
        """
        Setter for property: (float) MaximumCenterlineWidth
         Returns the maximum centerline width.  
           Points will be created using the centerline method
                if the smallest width is less than this value. If greater, points will be
                created using the offset from edge method.   
         
        """
        pass
    @property
    def MaximumGapBetweenBodies(self) -> float:
        """
        Getter for property: (float) MaximumGapBetweenBodies
         Returns the maximum gap expected when joining bodies.  
           This value should not be bigger than expected gaps between bodies.   
         
        """
        pass
    @MaximumGapBetweenBodies.setter
    def MaximumGapBetweenBodies(self, maximumGapBetweenBodies: float):
        """
        Setter for property: (float) MaximumGapBetweenBodies
         Returns the maximum gap expected when joining bodies.  
           This value should not be bigger than expected gaps between bodies.   
         
        """
        pass
    @property
    def MinimumFlangeWidth(self) -> float:
        """
        Getter for property: (float) MinimumFlangeWidth
         Returns the radius value for which faces will be excluded from the reference sheet construction.  
           Processing time will increase when smaller values are used.   
         
        """
        pass
    @MinimumFlangeWidth.setter
    def MinimumFlangeWidth(self, minimumFlangeWidth: float):
        """
        Setter for property: (float) MinimumFlangeWidth
         Returns the radius value for which faces will be excluded from the reference sheet construction.  
           Processing time will increase when smaller values are used.   
         
        """
        pass
    @property
    def MoveReferenceSheetToConstructionLayer(self) -> bool:
        """
        Getter for property: (bool) MoveReferenceSheetToConstructionLayer
         Returns the value to indidate if the output sheet bodies of this feature should be moved to the construction layer.  
             
         
        """
        pass
    @MoveReferenceSheetToConstructionLayer.setter
    def MoveReferenceSheetToConstructionLayer(self, moveReferenceSheetToConstructionLayer: bool):
        """
        Setter for property: (bool) MoveReferenceSheetToConstructionLayer
         Returns the value to indidate if the output sheet bodies of this feature should be moved to the construction layer.  
             
         
        """
        pass
    @property
    def OffsetFromEdgeDistance(self) -> float:
        """
        Getter for property: (float) OffsetFromEdgeDistance
         Returns the offset distance from edge   
            
         
        """
        pass
    @OffsetFromEdgeDistance.setter
    def OffsetFromEdgeDistance(self, offsetFromEdgeDistance: float):
        """
        Setter for property: (float) OffsetFromEdgeDistance
         Returns the offset distance from edge   
            
         
        """
        pass
    @property
    def OtherBodies(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: ( NXOpen.SelectBodyList) OtherBodies
         Returns the other bodies that are connected tot he top body.  
             
         
        """
        pass
    @property
    def ReferenceSheetOption(self) -> OverlapBuilder.ReferenceSheetOptionTypes:
        """
        Getter for property: ( OverlapBuilder.ReferenceSheetOptionTypes NXOpe) ReferenceSheetOption
         Returns the option to control where the overlap sheet will be created.  
             
         
        """
        pass
    @ReferenceSheetOption.setter
    def ReferenceSheetOption(self, sheetLocation: OverlapBuilder.ReferenceSheetOptionTypes):
        """
        Setter for property: ( OverlapBuilder.ReferenceSheetOptionTypes NXOpe) ReferenceSheetOption
         Returns the option to control where the overlap sheet will be created.  
             
         
        """
        pass
    @property
    def ReferenceSheetType(self) -> OverlapBuilder.ReferenceSheetTypes:
        """
        Getter for property: ( OverlapBuilder.ReferenceSheetTypes NXOpe) ReferenceSheetType
         Returns the type of reference sheet  
            
         
        """
        pass
    @ReferenceSheetType.setter
    def ReferenceSheetType(self, refSheet: OverlapBuilder.ReferenceSheetTypes):
        """
        Setter for property: ( OverlapBuilder.ReferenceSheetTypes NXOpe) ReferenceSheetType
         Returns the type of reference sheet  
            
         
        """
        pass
    @property
    def TopBodies(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: ( NXOpen.SelectBodyList) TopBodies
         Returns the top body that other bodies will be connected to.  
            Reference sheet faces will be on the outside of this body.   
         
        """
        pass
    @property
    def Type(self) -> OverlapBuilder.InputDataTypes:
        """
        Getter for property: ( OverlapBuilder.InputDataTypes NXOpe) Type
         Returns the input data type represented by  NXOpen::Join::OverlapBuilder::InputDataTypes  to create the reference sheet.  
             
         
        """
        pass
    @Type.setter
    def Type(self, type: OverlapBuilder.InputDataTypes):
        """
        Setter for property: ( OverlapBuilder.InputDataTypes NXOpe) Type
         Returns the input data type represented by  NXOpen::Join::OverlapBuilder::InputDataTypes  to create the reference sheet.  
             
         
        """
        pass
    def MoveReferenceSheet(self) -> None:
        """
         Move the Reference Sheet to work layer, and unlink from grouping feature. 
        """
        pass
    def NewFaceSets(self) -> OverlapFaceSetsBuilder:
        """
         Creates a NXOpen.Join.OverlapFaceSetsBuilder object. 
         Returns newfaceSetsBuilder ( OverlapFaceSetsBuilder NXOpe): .
        """
        pass
    def NewGuide(self) -> OverlapGuideBuilder:
        """
         Creates a NXOpen.Join.OverlapGuideBuilder object. 
         Returns newGuideBuilder ( OverlapGuideBuilder NXOpe): .
        """
        pass
import NXOpen
class OverlapFaceSetsBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[OverlapFaceSetsBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: OverlapFaceSetsBuilder) -> None:
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
    def Erase(self, obj: OverlapFaceSetsBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: OverlapFaceSetsBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: OverlapFaceSetsBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> OverlapFaceSetsBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( OverlapFaceSetsBuilder NXOpe):  object found at input index .
        """
        pass
    def GetContents(self) -> List[OverlapFaceSetsBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( OverlapFaceSetsBuilder List[NXO):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: OverlapFaceSetsBuilder) -> None:
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
    def SetContents(self, objects: List[OverlapFaceSetsBuilder]) -> None:
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
    def Swap(self, object1: OverlapFaceSetsBuilder, object2: OverlapFaceSetsBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class OverlapFaceSetsBuilder(NXOpen.TaggedObject): 
    """ Used to define the faces to create create that will be used to create a NXOpen.Join.Overlap feature. """
    @property
    def FaceSelect(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FaceSelect
         Returns the selected face collector   
            
         
        """
        pass
import NXOpen
class OverlapGuideBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[OverlapGuideBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: OverlapGuideBuilder) -> None:
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
    def Erase(self, obj: OverlapGuideBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: OverlapGuideBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: OverlapGuideBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> OverlapGuideBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( OverlapGuideBuilder NXOpe):  object found at input index .
        """
        pass
    def GetContents(self) -> List[OverlapGuideBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( OverlapGuideBuilder List[NXO):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: OverlapGuideBuilder) -> None:
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
    def SetContents(self, objects: List[OverlapGuideBuilder]) -> None:
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
    def Swap(self, object1: OverlapGuideBuilder, object2: OverlapGuideBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class OverlapGuideBuilder(NXOpen.TaggedObject): 
    """ Used to create or edit a guide curve in the NXOpen.Join.Overlap feature.  """
    class Method(Enum):
        """
        Members Include: 
         |CenterLine|  Centerline 
         |OffsetFromEdge|  Offset from Edge 
         |ExistingCurve|  Existing Curve 
         |NominalDiameter|  Nominal diameter. Uses Diameter, Multiplier, and Allowance to define the offset distance. 

        """
        CenterLine: int
        OffsetFromEdge: int
        ExistingCurve: int
        NominalDiameter: int
        @staticmethod
        def ValueOf(value: int) -> OverlapGuideBuilder.Method:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Allowance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Allowance
         Returns the design allowance.  
           Used with  OverlapGuideBuilder::MethodNominalDiameter . See  Diameter  expression.   
         
        """
        pass
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Diameter
         Returns the nominal diameter.  
            Used with  OverlapGuideBuilder::MethodNominalDiameter .  This value times  Multiplier  plus  Allowance  defines the offset distance.   
         
        """
        pass
    @property
    def ExtendOffset(self) -> bool:
        """
        Getter for property: (bool) ExtendOffset
         Returns the flag indicating if the guide curve should be extened to the nearest face boundary.  
           Used with Offset From Edge, and Nominal Diameter.   
         
        """
        pass
    @ExtendOffset.setter
    def ExtendOffset(self, extendOffset: bool):
        """
        Setter for property: (bool) ExtendOffset
         Returns the flag indicating if the guide curve should be extened to the nearest face boundary.  
           Used with Offset From Edge, and Nominal Diameter.   
         
        """
        pass
    @property
    def GuideCurve(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) GuideCurve
         Returns the guide curves created from the specified inputs.  
             
         
        """
        pass
    @GuideCurve.setter
    def GuideCurve(self, guide: NXOpen.Section):
        """
        Setter for property: ( NXOpen.Section) GuideCurve
         Returns the guide curves created from the specified inputs.  
             
         
        """
        pass
    @property
    def MethodOption(self) -> OverlapGuideBuilder.Method:
        """
        Getter for property: ( OverlapGuideBuilder.Method NXOpe) MethodOption
         Returns the method option is used to define how the guide curves will be created.  
             
         
        """
        pass
    @MethodOption.setter
    def MethodOption(self, methodOption: OverlapGuideBuilder.Method):
        """
        Setter for property: ( OverlapGuideBuilder.Method NXOpe) MethodOption
         Returns the method option is used to define how the guide curves will be created.  
             
         
        """
        pass
    @property
    def Multiplier(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Multiplier
         Returns the diameter multiplier.  
           Used with  OverlapGuideBuilder::MethodNominalDiameter . See  Diameter .   
         
        """
        pass
    @property
    def OffsetDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OffsetDistance
         Returns the offset distance used with the  OverlapGuideBuilder::MethodOffsetFromEdge     
            
         
        """
        pass
    @property
    def Section1(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Section1
         Returns the first section used to create a centerline with.  
           Used with  OverlapGuideBuilder::MethodCenterLine .   
         
        """
        pass
    @property
    def Section2(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Section2
         Returns the second section used to create a centerline with.  
           Used with  OverlapGuideBuilder::MethodCenterLine .   
         
        """
        pass
    @property
    def Section3(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Section3
         Returns the section used specify the edges on the reference sheet to offset from.  
           Used with  OverlapGuideBuilder::MethodOffsetFromEdge  and  OverlapGuideBuilder::MethodNominalDiameter .   
         
        """
        pass
    @property
    def Section4(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Section4
         Returns the section used to specify curves to project to the reference sheet.  
            Used with  OverlapGuideBuilder::MethodExistingCurve .    
         
        """
        pass
    def CreateGuideCurves(self) -> None:
        """
         Creates the guide curves defined by the method and sections. 
        """
        pass
    def GetGuideCurves(self) -> Tuple[List[NXOpen.ICurve], List[NXOpen.NXObject]]:
        """
         Gets the created curves. The guide curves must exist before calling this method. 
         Returns A tuple consisting of (guideCurves, instanceGuideCurves). 
         - guideCurves is:  NXOpen.ICurve Li.The array of curves.
         - instanceGuideCurves is:  NXOpen.NXObject Li.The array of component curve instances. If there is not an assembly, then this will match the prototype curve. .

        """
        pass
    def GetOffsetDirection(self) -> Tuple[NXOpen.Point3d, NXOpen.Vector3d]:
        """
         Gets the mid point of the section used for creating the offset curves, and a vector indicating the offset direction. 
         Returns A tuple consisting of (midPoint, direction). 
         - midPoint is:  NXOpen.Point3d. The mid point of the section used for offsetting the curve. .
         - direction is:  NXOpen.Vector3d. The vector direction that points to the interior of the reference sheet. .

        """
        pass
import NXOpen.Features
class Overlap(NXOpen.Features.Feature): 
    """ Represents a Join.Overlap Feature. """
    def GetReferenceSheet(self) -> NXOpen.Features.Feature:
        """
         Retrieves a Reference Sheet from a Join.Overlap Feature. 
         Returns sheetFrec ( NXOpen.Features.Feature): .
        """
        pass
import NXOpen
class PointJoinBuilder(JoinBuilder): 
    """
    Represents a NXOpen.Join.PointJoin builder.
    """
    class HoleTypes(Enum):
        """
        Members Include: 
         |Simple| 
         |Counterbored| 
         |Countersunk| 

        """
        Simple: int
        Counterbored: int
        Countersunk: int
        @staticmethod
        def ValueOf(value: int) -> PointJoinBuilder.HoleTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StackupAlignmentTypes(Enum):
        """
        Members Include: 
         |NormalClosestFace| 
         |NormalSelectedFace| 
         |AlongVector| 

        """
        NormalClosestFace: int
        NormalSelectedFace: int
        AlongVector: int
        @staticmethod
        def ValueOf(value: int) -> PointJoinBuilder.StackupAlignmentTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StackupMethodType(Enum):
        """
        Members Include: 
         |Automatic| 
         |Manual| 

        """
        Automatic: int
        Manual: int
        @staticmethod
        def ValueOf(value: int) -> PointJoinBuilder.StackupMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class VisualizationGeometryType(Enum):
        """
        Members Include: 
         |Sphere| 
         |Cylinder| 
         |Cone| 
         |Prism| 

        """
        Sphere: int
        Cylinder: int
        Cone: int
        Prism: int
        @staticmethod
        def ValueOf(value: int) -> PointJoinBuilder.VisualizationGeometryType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CreateCsys(self) -> bool:
        """
        Getter for property: (bool) CreateCsys
         Returns the indication to create a  NXOpen::CoordinateSystem    
            
         
        """
        pass
    @CreateCsys.setter
    def CreateCsys(self, createCsys: bool):
        """
        Setter for property: (bool) CreateCsys
         Returns the indication to create a  NXOpen::CoordinateSystem    
            
         
        """
        pass
    @property
    def CsysYDirection(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) CsysYDirection
         Returns  the indication to specify the y direction of the  NXOpen::CoordinateSystem     
            
         
        """
        pass
    @CsysYDirection.setter
    def CsysYDirection(self, csysYDirection: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) CsysYDirection
         Returns  the indication to specify the y direction of the  NXOpen::CoordinateSystem     
            
         
        """
        pass
    @property
    def FlipCsysDirection(self) -> bool:
        """
        Getter for property: (bool) FlipCsysDirection
         Returns the indication to reverse the z direction of the  NXOpen::CoordinateSystem     
            
         
        """
        pass
    @FlipCsysDirection.setter
    def FlipCsysDirection(self, flipCsysDirection: bool):
        """
        Setter for property: (bool) FlipCsysDirection
         Returns the indication to reverse the z direction of the  NXOpen::CoordinateSystem     
            
         
        """
        pass
    @property
    def HardwareAlignmentAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) HardwareAlignmentAngle
         Returns the alignment angle for rotation of hardware   
            
         
        """
        pass
    @property
    def HardwareAsNGC(self) -> bool:
        """
        Getter for property: (bool) HardwareAsNGC
         Returns the hardware as non geometric component flag.  
           If true, hardware components will get marked as non geometric components.   
         
        """
        pass
    @HardwareAsNGC.setter
    def HardwareAsNGC(self, status: bool):
        """
        Setter for property: (bool) HardwareAsNGC
         Returns the hardware as non geometric component flag.  
           If true, hardware components will get marked as non geometric components.   
         
        """
        pass
    @property
    def HardwareLoad(self) -> bool:
        """
        Getter for property: (bool) HardwareLoad
         Returns the load hardware flag.  
           If true, hardware should be loaded into assembly.   
         
        """
        pass
    @HardwareLoad.setter
    def HardwareLoad(self, status: bool):
        """
        Setter for property: (bool) HardwareLoad
         Returns the load hardware flag.  
           If true, hardware should be loaded into assembly.   
         
        """
        pass
    @property
    def HardwareOrientationCurve(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) HardwareOrientationCurve
         Returns the orientation curves along which the hardware can be oriented   
            
         
        """
        pass
    @property
    def HardwareQuantity(self) -> int:
        """
        Getter for property: (int) HardwareQuantity
         Returns the hardware quantity.  
           Specified value will get used to add number of components of hardware parts.  
         
        """
        pass
    @HardwareQuantity.setter
    def HardwareQuantity(self, hardwareQuantity: int):
        """
        Setter for property: (int) HardwareQuantity
         Returns the hardware quantity.  
           Specified value will get used to add number of components of hardware parts.  
         
        """
        pass
    @property
    def HoleCounterBoreDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) HoleCounterBoreDepth
         Returns the Counterbore depth   
            
         
        """
        pass
    @property
    def HoleCounterBoreDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) HoleCounterBoreDiameter
         Returns the Counterbore diameter   
            
         
        """
        pass
    @property
    def HoleCounterSinkAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) HoleCounterSinkAngle
         Returns the Countersink angle   
            
         
        """
        pass
    @property
    def HoleCounterSinkDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) HoleCounterSinkDiameter
         Returns the Countersink diameter   
            
         
        """
        pass
    @property
    def HoleCounterSinkSubflush(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) HoleCounterSinkSubflush
         Returns the Countersink sub-flush depth value   
            
         
        """
        pass
    @property
    def HoleCreate(self) -> bool:
        """
        Getter for property: (bool) HoleCreate
         Returns the hole creation status.  
           If true, holes should be created in connected bodies. If false, holes should be removed (or not created) from connected bodies   
         
        """
        pass
    @HoleCreate.setter
    def HoleCreate(self, status: bool):
        """
        Setter for property: (bool) HoleCreate
         Returns the hole creation status.  
           If true, holes should be created in connected bodies. If false, holes should be removed (or not created) from connected bodies   
         
        """
        pass
    @property
    def HoleDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) HoleDiameter
         Returns the hole diameter   
            
         
        """
        pass
    @property
    def HoleType(self) -> PointJoinBuilder.HoleTypes:
        """
        Getter for property: ( PointJoinBuilder.HoleTypes NXOpe) HoleType
         Returns the hole type value   
            
         
        """
        pass
    @HoleType.setter
    def HoleType(self, holeType: PointJoinBuilder.HoleTypes):
        """
        Setter for property: ( PointJoinBuilder.HoleTypes NXOpe) HoleType
         Returns the hole type value   
            
         
        """
        pass
    @property
    def JointMarkAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) JointMarkAngle
         Returns the joint mark angle   
            
         
        """
        pass
    @property
    def JointMarkFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) JointMarkFace
         Returns the face for the joint mark placement   
            
         
        """
        pass
    @property
    def JointMarkGuideCurve(self) -> NXOpen.SelectCurveList:
        """
        Getter for property: ( NXOpen.SelectCurveList) JointMarkGuideCurve
         Returns the curve along which the joint mark symbol is placed   
            
         
        """
        pass
    @property
    def JointMarkSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) JointMarkSize
         Returns the joint mark size   
            
         
        """
        pass
    @property
    def ManualStackupEndPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) ManualStackupEndPoint
         Returns the selected end point for manual stackup  
            
         
        """
        pass
    @ManualStackupEndPoint.setter
    def ManualStackupEndPoint(self, manualStackupEndPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) ManualStackupEndPoint
         Returns the selected end point for manual stackup  
            
         
        """
        pass
    @property
    def MatedWithNutplate(self) -> bool:
        """
        Getter for property: (bool) MatedWithNutplate
         Returns the flag when ON indicates only nutplate points from attached hardware utility are selectable    
            
         
        """
        pass
    @MatedWithNutplate.setter
    def MatedWithNutplate(self, matedWithNutplate: bool):
        """
        Setter for property: (bool) MatedWithNutplate
         Returns the flag when ON indicates only nutplate points from attached hardware utility are selectable    
            
         
        """
        pass
    @property
    def PointSelPoints(self) -> NXOpen.SelectPointList:
        """
        Getter for property: ( NXOpen.SelectPointList) PointSelPoints
         Returns the selected points   
            
         
        """
        pass
    @property
    def PreviewCsys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) PreviewCsys
         Returns  the  NXOpen::CoordinateSystem  during preview  
            
         
        """
        pass
    @PreviewCsys.setter
    def PreviewCsys(self, previewCsys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) PreviewCsys
         Returns  the  NXOpen::CoordinateSystem  during preview  
            
         
        """
        pass
    @property
    def StackupAlignment(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) StackupAlignment
         Returns the stackup alignment   
            
         
        """
        pass
    @StackupAlignment.setter
    def StackupAlignment(self, stackupAlignment: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) StackupAlignment
         Returns the stackup alignment   
            
         
        """
        pass
    @property
    def StackupAlignmentType(self) -> PointJoinBuilder.StackupAlignmentTypes:
        """
        Getter for property: ( PointJoinBuilder.StackupAlignmentTypes NXOpe) StackupAlignmentType
         Returns the stackup alignment type value   
            
         
        """
        pass
    @StackupAlignmentType.setter
    def StackupAlignmentType(self, stackupAlignmentType: PointJoinBuilder.StackupAlignmentTypes):
        """
        Setter for property: ( PointJoinBuilder.StackupAlignmentTypes NXOpe) StackupAlignmentType
         Returns the stackup alignment type value   
            
         
        """
        pass
    @property
    def StackupGapLimit(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StackupGapLimit
         Returns the gap limit   
            
         
        """
        pass
    @property
    def StackupGapTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StackupGapTolerance
         Returns the gap tolerance   
            
         
        """
        pass
    @property
    def StackupMaxHolePerimeter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StackupMaxHolePerimeter
         Returns the maximum hole perimeter.  
           Stackup will include bodies with holes or other openings with a loop perimeter smaller than specified here.
                Bodies with larger openings will be excluded from the stackup.   
         
        """
        pass
    @property
    def StackupMethod(self) -> PointJoinBuilder.StackupMethodType:
        """
        Getter for property: ( PointJoinBuilder.StackupMethodType NXOpe) StackupMethod
         Returns the stackup method   
            
         
        """
        pass
    @StackupMethod.setter
    def StackupMethod(self, stackupMethod: PointJoinBuilder.StackupMethodType):
        """
        Setter for property: ( PointJoinBuilder.StackupMethodType NXOpe) StackupMethod
         Returns the stackup method   
            
         
        """
        pass
    @property
    def StackupNormalSurface(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) StackupNormalSurface
         Returns the selected normal surface   
            
         
        """
        pass
    @property
    def StackupOnSurfaceTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StackupOnSurfaceTolerance
         Returns the stackup on surface tolerance   
            
         
        """
        pass
    @property
    def StackupOverlapTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StackupOverlapTolerance
         Returns the overlap tolerance   
            
         
        """
        pass
    @property
    def StackupReverseDirection(self) -> bool:
        """
        Getter for property: (bool) StackupReverseDirection
         Returns the reverse stackup direction flag   
            
         
        """
        pass
    @StackupReverseDirection.setter
    def StackupReverseDirection(self, isReversed: bool):
        """
        Setter for property: (bool) StackupReverseDirection
         Returns the reverse stackup direction flag   
            
         
        """
        pass
    @property
    def SynchronizeLocation(self) -> bool:
        """
        Getter for property: (bool) SynchronizeLocation
         Returns the indication of whether to update a point join's location to match its linked point.  
             
         
        """
        pass
    @SynchronizeLocation.setter
    def SynchronizeLocation(self, synchronizeLocation: bool):
        """
        Setter for property: (bool) SynchronizeLocation
         Returns the indication of whether to update a point join's location to match its linked point.  
             
         
        """
        pass
    @property
    def VisualizationColor(self) -> int:
        """
        Getter for property: (int) VisualizationColor
         Returns the visualization color value   
            
         
        """
        pass
    @VisualizationColor.setter
    def VisualizationColor(self, visualizationColor: int):
        """
        Setter for property: (int) VisualizationColor
         Returns the visualization color value   
            
         
        """
        pass
    @property
    def VisualizationCreateSolid(self) -> bool:
        """
        Getter for property: (bool) VisualizationCreateSolid
         Returns  the indication that the point join should be represented by a solid body    
            
         
        """
        pass
    @VisualizationCreateSolid.setter
    def VisualizationCreateSolid(self, visualizationCreateSolid: bool):
        """
        Setter for property: (bool) VisualizationCreateSolid
         Returns  the indication that the point join should be represented by a solid body    
            
         
        """
        pass
    @property
    def VisualizationDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) VisualizationDiameter
         Returns the visualization diameter   
            
         
        """
        pass
    @property
    def VisualizationGeometry(self) -> PointJoinBuilder.VisualizationGeometryType:
        """
        Getter for property: ( PointJoinBuilder.VisualizationGeometryType NXOpe) VisualizationGeometry
         Returns the visualization geometry type value   
            
         
        """
        pass
    @VisualizationGeometry.setter
    def VisualizationGeometry(self, visualizationGeometry: PointJoinBuilder.VisualizationGeometryType):
        """
        Setter for property: ( PointJoinBuilder.VisualizationGeometryType NXOpe) VisualizationGeometry
         Returns the visualization geometry type value   
            
         
        """
        pass
    @property
    def VisualizationHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) VisualizationHeight
         Returns the visualization height   
            
         
        """
        pass
    @property
    def VisualizationPointMarker(self) -> int:
        """
        Getter for property: (int) VisualizationPointMarker
         Returns the point marker   
            
         
        """
        pass
    @VisualizationPointMarker.setter
    def VisualizationPointMarker(self, visualizationPointMarker: int):
        """
        Setter for property: (int) VisualizationPointMarker
         Returns the point marker   
            
         
        """
        pass
    def ClearAttachmentHardware(self) -> None:
        """
         Clears the attachment Hardware. 
        """
        pass
    def ClearHardwarePin(self) -> None:
        """
         Clears the hardware pin. 
        """
        pass
    def CreateAttachmentHardware(self) -> None:
        """
         Creates a new attachment Hardware. 
        """
        pass
    def CreateHardwarePin(self) -> None:
        """
         Creates a new hardware pin. 
        """
        pass
    def GetAttachmentHardware(self) -> AttachmentHardware:
        """
         Gets the attachment hardware. 
         Returns attachmentHardware ( AttachmentHardware NXOpe): .
        """
        pass
    def GetHardwarePin(self) -> PointJoinHardware:
        """
         Gets the hardware pin. 
         Returns pin ( PointJoinHardware NXOpe): .
        """
        pass
    def GetNthHeadSidePart(self, headsidePartIndex: int) -> PointJoinHardware:
        """
         Gets the headside hardware part by index 
         Returns headsidePart ( PointJoinHardware NXOpe): .
        """
        pass
    def GetNthTailSidePart(self, tailsidePartIndex: int) -> PointJoinHardware:
        """
         Gets the tailside hardware part by index 
         Returns tailsidePart ( PointJoinHardware NXOpe): .
        """
        pass
    def GetNumberOfHeadSideParts(self) -> int:
        """
         Gets number of headside hardware parts 
         Returns numberofHeadsideParts (int): .
        """
        pass
    def GetNumberOfTailSideParts(self) -> int:
        """
         Gets number of tailside hardware parts 
         Returns numberofTailsideParts (int): .
        """
        pass
    def GetStackupDirectionForPoint(self, point: NXOpen.Point) -> bool:
        """
         This method adds a point that the stackup direction should be reversed for. 
         Returns reverseStackupDirection (bool):  Indicates if the stackup direction should be reversed for this point. .
        """
        pass
    def GetStackupEntryPoint(self) -> NXOpen.Point3d:
        """
         This method gets stackup entry point of Pointjoin 
         Returns entryPoint ( NXOpen.Point3d): .
        """
        pass
    def LoadHardware(self) -> bool:
        """
         Loads hardware parts into assembly. 
         Returns status (bool): .
        """
        pass
    def ProcessWasherInfoForStackup(self) -> None:
        """
         The washer information is addedupdated on stackup 
        """
        pass
    def SetHardwarePin(self, pinName: str, pinPath: str) -> None:
        """
         Set hardware pin information from name. 
                If reuse library is the hardware data source, pinName is the descriptive name of the part
                and pinPath is the path of the part in the reuse library.
                If an XML database is used, pinName is the look up name and pinPath may be null. 
                
        """
        pass
    def SetHeadSideParts(self, headNames: List[str], headPaths: List[str]) -> None:
        """
         Set hardware for head side parts.
                If reuse library is the hardware data source, headNames are the descriptive names of the parts
                and headPaths are the paths of the parts in the reuse library.
                If an XML database is used, headNames are the look up names and headPaths may be empty strings. 
        """
        pass
    def SetNumberOfHeadSideParts(self, numberOfHeadsideParts: int) -> None:
        """
         Sets the number of headside hardware parts.
                Existing head side hardware objects are deleted and new head side hardware objects are created.
                The number of newly created head side hardware objects equals numberOfHeadsideParts.
                
        """
        pass
    def SetNumberOfTailSideParts(self, numberOfTailsideParts: int) -> None:
        """
         Sets the number of tailside hardware parts.
                Existing tail side hardware objects are deleted and new tail side hardware objects are created.
                The number of newly created tail side hardware objects equals numberOfTailsideParts.
                
        """
        pass
    def SetStackupDirectionForPoint(self, point: NXOpen.Point, reverseStackupDirection: bool) -> None:
        """
         This method gets the stackup direction for a specific point. 
        """
        pass
    def SetTailSideParts(self, tailNames: List[str], tailPaths: List[str]) -> None:
        """
         Set hardware for tail side parts. 
                If reuse library is the hardware data source, tailNames are the descriptive names of the parts
                and tailPaths are the paths of the parts in the reuse library.
                If an XML database is used, tailNames are the look up names and tailPaths may be empty strings. 
        """
        pass
    def UnloadHardware(self) -> bool:
        """
         Unloads hardware parts from assembly. 
         Returns status (bool): .
        """
        pass
import NXOpen
class PointJoinHardware(NXOpen.TaggedObject): 
    """ Represents a NXOpen.Join.PointJoinHardware.
    """
    class AttributeDataSourceType(Enum):
        """
        Members Include: 
         |Undefined| 
         |XmlDatabase| 
         |ReuseLibraryExcel| 
         |TeamcenterClassification| 
         |XmlDatabaseSpecification| 
         |ReuseLibrarySpecification| 

        """
        Undefined: int
        XmlDatabase: int
        ReuseLibraryExcel: int
        TeamcenterClassification: int
        XmlDatabaseSpecification: int
        ReuseLibrarySpecification: int
        @staticmethod
        def ValueOf(value: int) -> PointJoinHardware.AttributeDataSourceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AttributeDataSource(self) -> PointJoinHardware.AttributeDataSourceType:
        """
        Getter for property: ( PointJoinHardware.AttributeDataSourceType NXOpe) AttributeDataSource
         Returns the attribute data source of the point join hardware part.  
            
         
        """
        pass
    @AttributeDataSource.setter
    def AttributeDataSource(self, attributeDataSource: PointJoinHardware.AttributeDataSourceType):
        """
        Setter for property: ( PointJoinHardware.AttributeDataSourceType NXOpe) AttributeDataSource
         Returns the attribute data source of the point join hardware part.  
            
         
        """
        pass
    @property
    def ClassificationClassId(self) -> str:
        """
        Getter for property: (str) ClassificationClassId
         Returns the Teamcenter Classification Object Class Id of the point join hardware part.  
             
         
        """
        pass
    @ClassificationClassId.setter
    def ClassificationClassId(self, classId: str):
        """
        Setter for property: (str) ClassificationClassId
         Returns the Teamcenter Classification Object Class Id of the point join hardware part.  
             
         
        """
        pass
    @property
    def ClassificationInstanceId(self) -> str:
        """
        Getter for property: (str) ClassificationInstanceId
         Returns the Teamcenter Classification Object Instance Id of the point join hardware part.  
             
         
        """
        pass
    @ClassificationInstanceId.setter
    def ClassificationInstanceId(self, instanceId: str):
        """
        Setter for property: (str) ClassificationInstanceId
         Returns the Teamcenter Classification Object Instance Id of the point join hardware part.  
             
         
        """
        pass
    @property
    def FamilyInstance(self) -> str:
        """
        Getter for property: (str) FamilyInstance
         Returns the Family Instance Name of the point join hardware part in its family table.  
          
                It is the cell value of either the DB_PART_NO or OS_PART_NAME column of the instance's row in the part family table.
                The cell value maybe prefixed with "DB_PART_NO:" or "OS_PART_NAME:" for a precise lookup for instance's values.
                When not prefixed, both columns are checked for a match.
                  
         
        """
        pass
    @FamilyInstance.setter
    def FamilyInstance(self, familyInstance: str):
        """
        Setter for property: (str) FamilyInstance
         Returns the Family Instance Name of the point join hardware part in its family table.  
          
                It is the cell value of either the DB_PART_NO or OS_PART_NAME column of the instance's row in the part family table.
                The cell value maybe prefixed with "DB_PART_NO:" or "OS_PART_NAME:" for a precise lookup for instance's values.
                When not prefixed, both columns are checked for a match.
                  
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of the point join hardware.  
          
                If the attribute data source is  NXOpen::Join::PointJoinHardware::AttributeDataSourceTypeXmlDatabase ,
                name is used to look up the attributes from the XML database and the available PointJoinHardware attributes
                are auto populated.
                  
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name of the point join hardware.  
          
                If the attribute data source is  NXOpen::Join::PointJoinHardware::AttributeDataSourceTypeXmlDatabase ,
                name is used to look up the attributes from the XML database and the available PointJoinHardware attributes
                are auto populated.
                  
         
        """
        pass
    @property
    def Orientation(self) -> str:
        """
        Getter for property: (str) Orientation
         Returns the orientation of the point join hardware part.  
            
         
        """
        pass
    @Orientation.setter
    def Orientation(self, orientation: str):
        """
        Setter for property: (str) Orientation
         Returns the orientation of the point join hardware part.  
            
         
        """
        pass
    @property
    def Path(self) -> str:
        """
        Getter for property: (str) Path
         Returns the path of the point join hardware part.  
          
                If the attribute data source is  NXOpen::Join::PointJoinHardware::AttributeDataSourceTypeReuseLibraryExcel ,
                path is used to look up the attributes from the EXCEL database and the available PointJoinHardware attributes
                are auto populated.
                  
         
        """
        pass
    @Path.setter
    def Path(self, path: str):
        """
        Setter for property: (str) Path
         Returns the path of the point join hardware part.  
          
                If the attribute data source is  NXOpen::Join::PointJoinHardware::AttributeDataSourceTypeReuseLibraryExcel ,
                path is used to look up the attributes from the EXCEL database and the available PointJoinHardware attributes
                are auto populated.
                  
         
        """
        pass
    @property
    def Specification(self) -> str:
        """
        Getter for property: (str) Specification
         Returns the specification of the point join hardware.  
             
         
        """
        pass
    @Specification.setter
    def Specification(self, spec: str):
        """
        Setter for property: (str) Specification
         Returns the specification of the point join hardware.  
             
         
        """
        pass
    @property
    def SpecificationDescriptiveName(self) -> str:
        """
        Getter for property: (str) SpecificationDescriptiveName
         Returns the Descriptive Name of the hardware specification in Reuse Library.  
            
         
        """
        pass
    @SpecificationDescriptiveName.setter
    def SpecificationDescriptiveName(self, specDescName: str):
        """
        Setter for property: (str) SpecificationDescriptiveName
         Returns the Descriptive Name of the hardware specification in Reuse Library.  
            
         
        """
        pass
    @property
    def Thickness(self) -> float:
        """
        Getter for property: (float) Thickness
         Returns the thickness of the point join hardware part.  
            
         
        """
        pass
    @Thickness.setter
    def Thickness(self, thickness: float):
        """
        Setter for property: (float) Thickness
         Returns the thickness of the point join hardware part.  
            
         
        """
        pass
    @property
    def ThreadPitch(self) -> float:
        """
        Getter for property: (float) ThreadPitch
         Returns the thread pitch of the point join hardware part.  
            
         
        """
        pass
    @ThreadPitch.setter
    def ThreadPitch(self, threadPitch: float):
        """
        Setter for property: (float) ThreadPitch
         Returns the thread pitch of the point join hardware part.  
            
         
        """
        pass
    @property
    def ThreadedLength(self) -> float:
        """
        Getter for property: (float) ThreadedLength
         Returns the threaded length of the point join hardware part.  
            
         
        """
        pass
    @ThreadedLength.setter
    def ThreadedLength(self, threadedLength: float):
        """
        Setter for property: (float) ThreadedLength
         Returns the threaded length of the point join hardware part.  
            
         
        """
        pass
    @property
    def Type(self) -> str:
        """
        Getter for property: (str) Type
         Returns the type of the point join hardware part.  
            
         
        """
        pass
    @Type.setter
    def Type(self, type: str):
        """
        Setter for property: (str) Type
         Returns the type of the point join hardware part.  
            
         
        """
        pass
class PointJoinStackupInfoOptions:
    """
     Indicates the required stackup info from a  Join::PointJoin . 
    """
    @property
    def ConnectedBodies(self) -> bool:
        """
        Getter for property ConnectedBodies
        connected bodies.

        """
        pass
    @ConnectedBodies.setter
    def ConnectedBodies(self, value: bool):
        """
        Getter for property ConnectedBodies
        connected bodies.
        Setter for property ConnectedBodies
        connected bodies.

        """
        pass
    @property
    def EntryExitPoints(self) -> bool:
        """
        Getter for property EntryExitPoints
        entryexit points.

        """
        pass
    @EntryExitPoints.setter
    def EntryExitPoints(self, value: bool):
        """
        Getter for property EntryExitPoints
        entryexit points.
        Setter for property EntryExitPoints
        entryexit points.

        """
        pass
    @property
    def EntryExitFaces(self) -> bool:
        """
        Getter for property EntryExitFaces
        entryexit faces.

        """
        pass
    @EntryExitFaces.setter
    def EntryExitFaces(self, value: bool):
        """
        Getter for property EntryExitFaces
        entryexit faces.
        Setter for property EntryExitFaces
        entryexit faces.

        """
        pass
    @property
    def HoleEdges(self) -> bool:
        """
        Getter for property HoleEdges
        hole edges

        """
        pass
    @HoleEdges.setter
    def HoleEdges(self, value: bool):
        """
        Getter for property HoleEdges
        hole edges
        Setter for property HoleEdges
        hole edges

        """
        pass
import NXOpen
class PointJoinStackupInfo(NXOpen.TransientObject): 
    """ Represents a manager of point join stackup info objects. """
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                is called, it is illegal to use the object. In .NET, this method
                is automatically called when the object is deleted by the garbage
                collector. 
        """
        pass
    def GetConnectedBodies(self) -> List[NXOpen.Body]:
        """
         Gets connected bodies of point join. 
         Returns bodies ( NXOpen.Body Li):  .
        """
        pass
    def GetConnectedBody(self, i: int) -> NXOpen.Body:
        """
         Gets connected body of point join. 
         Returns body ( NXOpen.Body): .
        """
        pass
    def GetCount(self) -> int:
        """
         Gets total number of stackup entries. 
         Returns stackupCount (int): .
        """
        pass
    def GetEntryFaces(self, i: int) -> List[NXOpen.Face]:
        """
         Gets entry faces of point join. Maximum index can be found using NXOpen.Join.PointJoinStackupInfo.GetCount. 
         Returns faces ( NXOpen.Face Li):  .
        """
        pass
    def GetEntryPoint(self, i: int) -> NXOpen.Point3d:
        """
         Gets entry co-ordinates of point join. 
         Returns coordinates ( NXOpen.Point3d): .
        """
        pass
    def GetEntryPoints(self) -> List[NXOpen.Point3d]:
        """
         Gets all entry points of point join. 
         Returns points ( NXOpen.Point3d Li):  .
        """
        pass
    def GetExitFaces(self, i: int) -> List[NXOpen.Face]:
        """
         Gets exit faces of point join. Maximum index can be found using NXOpen.Join.PointJoinStackupInfo.GetCount. 
         Returns faces ( NXOpen.Face Li):  .
        """
        pass
    def GetExitPoint(self, i: int) -> NXOpen.Point3d:
        """
         Gets exit co-ordinates of point join. 
         Returns coordinates ( NXOpen.Point3d): .
        """
        pass
    def GetExitPoints(self) -> List[NXOpen.Point3d]:
        """
         Gets all exit points of point join. 
         Returns points ( NXOpen.Point3d Li):  .
        """
        pass
    def GetHoleEdges(self) -> List[NXOpen.Edge]:
        """
         Gets hole edges of Point Join. 
         Returns edges ( NXOpen.Edge Li):  .
        """
        pass
    def GetStackupDirection(self) -> NXOpen.Vector3d:
        """
         Gets stackup direction. 
         Returns stackupDirection ( NXOpen.Vector3d): .
        """
        pass
import NXOpen
import NXOpen.Features
class PointJoin(NXOpen.Features.BodyFeature): 
    """ Represents a point based join feature """
    def AreConnectedPartsFullyLoaded(self) -> bool:
        """
         Checks whether all of the connected parts of a point join are fully loaded or not.
         Returns fullyLoaded (bool): .
        """
        pass
    def GetHoleDiameter(self) -> float:
        """
         Gets simple hole diameter of a point join.
         Returns holeDiameter (float): .
        """
        pass
    def GetPointJoinStackupFirstEntryPoint(self) -> NXOpen.Point3d:
        """
         Gets first stackup entry point of a point join.
         Returns firstEntryPoint ( NXOpen.Point3d): .
        """
        pass
    def GetStackupInfo(self, stackupInfoOptions: PointJoinStackupInfoOptions) -> PointJoinStackupInfo:
        """
         Gets stackup information of a point join.
         Returns stackupInfo ( PointJoinStackupInfo NXOpe): .
        """
        pass
    def GetStackupMethod(self) -> PointJoinBuilder.StackupMethodType:
        """
         Gets stackup method of a point join.
         Returns stackupMethod ( PointJoinBuilder.StackupMethodType NXOpe): .
        """
        pass
    def LoadConnectedParts(self) -> None:
        """
         Loads connected parts of a point join.
        """
        pass
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
class PointLayoutBuilder(NXOpen.Features.FeatureBuilder): 
    """ Used to create points on a guide curve. """
    class SpaceMethod(Enum):
        """
        Members Include: 
         |ArcLength|  Arc Length 
         |ParallelXPlane|  Parallel X Plane 
         |ParallelYPlane|  Parallel Y Plane 
         |ParallelZPlane|  Parallel Z Plane 

        """
        ArcLength: int
        ParallelXPlane: int
        ParallelYPlane: int
        ParallelZPlane: int
        @staticmethod
        def ValueOf(value: int) -> PointLayoutBuilder.SpaceMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SpaceOption(Enum):
        """
        Members Include: 
         |Distance|  Space points by a fixed distance. Spacing at last point may not be uniform.
         |Number|  Uniformly space a number of points. 
         |MinimumDistance|  Uniformly space points using a minimum distance value. 

        """
        Distance: int
        Number: int
        MinimumDistance: int
        @staticmethod
        def ValueOf(value: int) -> PointLayoutBuilder.SpaceOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SpacingTypes(Enum):
        """
        Members Include: 
         |Manual|  Fixed parameters are used to space points. 
         |Automatic|  Points are spaced using a minimum spacing distance and maximum spacing distance variables. 

        """
        Manual: int
        Automatic: int
        @staticmethod
        def ValueOf(value: int) -> PointLayoutBuilder.SpacingTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DistanceFromEnds(self) -> float:
        """
        Getter for property: (float) DistanceFromEnds
         Returns the distance from the ends to start creating weld points at   
            
         
        """
        pass
    @DistanceFromEnds.setter
    def DistanceFromEnds(self, distanceFromEnds: float):
        """
        Setter for property: (float) DistanceFromEnds
         Returns the distance from the ends to start creating weld points at   
            
         
        """
        pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance for constructing the feature.  
              
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance for constructing the feature.  
              
         
        """
        pass
    @property
    def EndDistance(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) EndDistance
         Returns the end distance.  
             
         
        """
        pass
    @property
    def GuidePath(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) GuidePath
         Returns the selected section used to place point along.  
             
         
        """
        pass
    @property
    def MaximumSpacingBetweenPoints(self) -> float:
        """
        Getter for property: (float) MaximumSpacingBetweenPoints
         Returns the maximum spacing between points   
            
         
        """
        pass
    @MaximumSpacingBetweenPoints.setter
    def MaximumSpacingBetweenPoints(self, maximumSpacingBetweenPoints: float):
        """
        Setter for property: (float) MaximumSpacingBetweenPoints
         Returns the maximum spacing between points   
            
         
        """
        pass
    @property
    def MinimumNumberPoints(self) -> int:
        """
        Getter for property: (int) MinimumNumberPoints
         Returns the minimum number points to create on an overlap sheet   
            
         
        """
        pass
    @MinimumNumberPoints.setter
    def MinimumNumberPoints(self, minimumNumberPointsOnOverlap: int):
        """
        Setter for property: (int) MinimumNumberPoints
         Returns the minimum number points to create on an overlap sheet   
            
         
        """
        pass
    @property
    def MinimumSpacingBetweenPoints(self) -> float:
        """
        Getter for property: (float) MinimumSpacingBetweenPoints
         Returns the minimum spacing between points   
            
         
        """
        pass
    @MinimumSpacingBetweenPoints.setter
    def MinimumSpacingBetweenPoints(self, minimumSpacingBetweenPoints: float):
        """
        Setter for property: (float) MinimumSpacingBetweenPoints
         Returns the minimum spacing between points   
            
         
        """
        pass
    @property
    def NumberOfPoints(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NumberOfPoints
         Returns the number to determine the points along the guide curve.  
             
         
        """
        pass
    @property
    def PointList(self) -> PointLayoutPointBuilderList:
        """
        Getter for property: ( PointLayoutPointBuilderList NXOpe) PointList
         Returns the list of points  
            
         
        """
        pass
    @property
    def Spacing(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Spacing
         Returns the spacing to determine the points along the guide curve.  
             
         
        """
        pass
    @property
    def SpacingMethod(self) -> PointLayoutBuilder.SpaceMethod:
        """
        Getter for property: ( PointLayoutBuilder.SpaceMethod NXOpe) SpacingMethod
         Returns the spacing method.  
             
         
        """
        pass
    @SpacingMethod.setter
    def SpacingMethod(self, spacingMethod: PointLayoutBuilder.SpaceMethod):
        """
        Setter for property: ( PointLayoutBuilder.SpaceMethod NXOpe) SpacingMethod
         Returns the spacing method.  
             
         
        """
        pass
    @property
    def SpacingOption(self) -> PointLayoutBuilder.SpaceOption:
        """
        Getter for property: ( PointLayoutBuilder.SpaceOption NXOpe) SpacingOption
         Returns the spacing option.  
             
         
        """
        pass
    @SpacingOption.setter
    def SpacingOption(self, spacingOption: PointLayoutBuilder.SpaceOption):
        """
        Setter for property: ( PointLayoutBuilder.SpaceOption NXOpe) SpacingOption
         Returns the spacing option.  
             
         
        """
        pass
    @property
    def StartDistance(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) StartDistance
         Returns the start distance.  
             
         
        """
        pass
    @property
    def Type(self) -> PointLayoutBuilder.SpacingTypes:
        """
        Getter for property: ( PointLayoutBuilder.SpacingTypes NXOpe) Type
         Returns the point spacing method represented by  NXOpen::Join::PointLayoutBuilder::SpacingTypes .  
            
         
        """
        pass
    @Type.setter
    def Type(self, type: PointLayoutBuilder.SpacingTypes):
        """
        Setter for property: ( PointLayoutBuilder.SpacingTypes NXOpe) Type
         Returns the point spacing method represented by  NXOpen::Join::PointLayoutBuilder::SpacingTypes .  
            
         
        """
        pass
    @property
    def UniformSpacingTolerance(self) -> float:
        """
        Getter for property: (float) UniformSpacingTolerance
         Returns the distance that maximum spacing can be exceeded to achieve uniform spacing   
            
         
        """
        pass
    @UniformSpacingTolerance.setter
    def UniformSpacingTolerance(self, uniformSpacingTolerance: float):
        """
        Setter for property: (float) UniformSpacingTolerance
         Returns the distance that maximum spacing can be exceeded to achieve uniform spacing   
            
         
        """
        pass
    def AppendPoints(self) -> None:
        """
         Creates a list of points on the overlap sheet. In addition, a curve selected by the user will be placed at these points. 
        """
        pass
    def NewPoints(self) -> PointLayoutPointBuilder:
        """
         Creates a NXOpen.Join.PointLayoutPointBuilder object. 
         Returns newPointBuilder ( PointLayoutPointBuilder NXOpe): .
        """
        pass
import NXOpen
class PointLayoutPointBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[PointLayoutPointBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: PointLayoutPointBuilder) -> None:
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
    def Erase(self, obj: PointLayoutPointBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: PointLayoutPointBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: PointLayoutPointBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> PointLayoutPointBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( PointLayoutPointBuilder NXOpe):  object found at input index .
        """
        pass
    def GetContents(self) -> List[PointLayoutPointBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( PointLayoutPointBuilder List[NXO):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: PointLayoutPointBuilder) -> None:
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
    def SetContents(self, objects: List[PointLayoutPointBuilder]) -> None:
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
    def Swap(self, object1: PointLayoutPointBuilder, object2: PointLayoutPointBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class PointLayoutPointBuilder(NXOpen.TaggedObject): 
    """ Used to create or edit a point in the list of points for PointLayoutBuilder """
    class PointPosition(Enum):
        """
        Members Include: 
         |NotSet|  None specifed. 
         |MovedAlongGuide|  User moved point from default location along the guide curve 

        """
        NotSet: int
        MovedAlongGuide: int
        @staticmethod
        def ValueOf(value: int) -> PointLayoutPointBuilder.PointPosition:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Point(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Point
         Returns the point at which the feature is created   
            
         
        """
        pass
    @Point.setter
    def Point(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Point
         Returns the point at which the feature is created   
            
         
        """
        pass
import NXOpen
import NXOpen.Features
class PointLayout(NXOpen.Features.Feature): 
    """ Represents a Join.Overlap Feature. """
    def GetPoints(self) -> List[NXOpen.Point3d]:
        """
         Retrieves the point locations represented by the Join.PointLayout Feature. 
         Returns points ( NXOpen.Point3d Li):  .
        """
        pass
import NXOpen
class PreferencesBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Join.PreferencesBuilder builder """
    @property
    def ConstructionLayer(self) -> int:
        """
        Getter for property: (int) ConstructionLayer
         Returns the construction layer preference.  
           This option specifies the layer on which the construction geometry should be placed.  
         
        """
        pass
    @ConstructionLayer.setter
    def ConstructionLayer(self, constructionLayer: int):
        """
        Setter for property: (int) ConstructionLayer
         Returns the construction layer preference.  
           This option specifies the layer on which the construction geometry should be placed.  
         
        """
        pass
    @property
    def FixTimestamp(self) -> bool:
        """
        Getter for property: (bool) FixTimestamp
         Returns the fix at timestamp preference.  
           When WAVE Links are created by the Join commands including Curve utilities and Join Creation, linked geometry will be fixed at Current Timestamp allowing users to create holes where applicable.  
         
        """
        pass
    @FixTimestamp.setter
    def FixTimestamp(self, fixTimestamp: bool):
        """
        Setter for property: (bool) FixTimestamp
         Returns the fix at timestamp preference.  
           When WAVE Links are created by the Join commands including Curve utilities and Join Creation, linked geometry will be fixed at Current Timestamp allowing users to create holes where applicable.  
         
        """
        pass
    @property
    def GroupIdSeedValue(self) -> str:
        """
        Getter for property: (str) GroupIdSeedValue
         Returns a join group ID seed value preference.  
          
                  
         
        """
        pass
    @GroupIdSeedValue.setter
    def GroupIdSeedValue(self, groupIdSeedValue: str):
        """
        Setter for property: (str) GroupIdSeedValue
         Returns a join group ID seed value preference.  
          
                  
         
        """
        pass
    @property
    def NamingLowerLimit(self) -> int:
        """
        Getter for property: (int) NamingLowerLimit
         Returns the naming lower limit preference.  
           This option specifies the lower limit used to name the join features.  
         
        """
        pass
    @NamingLowerLimit.setter
    def NamingLowerLimit(self, namingLowerLimit: int):
        """
        Setter for property: (int) NamingLowerLimit
         Returns the naming lower limit preference.  
           This option specifies the lower limit used to name the join features.  
         
        """
        pass
    @property
    def NamingUpperLimit(self) -> int:
        """
        Getter for property: (int) NamingUpperLimit
         Returns the naming upper limit preference.  
           This option specifies the upper limit used to name the join features.  
         
        """
        pass
    @NamingUpperLimit.setter
    def NamingUpperLimit(self, namingUpperLimit: int):
        """
        Setter for property: (int) NamingUpperLimit
         Returns the naming upper limit preference.  
           This option specifies the upper limit used to name the join features.  
         
        """
        pass
    @property
    def OutputGeometryLayer(self) -> int:
        """
        Getter for property: (int) OutputGeometryLayer
         Returns the output geometry layer preference.  
           This option specifies the layer on which the output geometry should be placed.  
         
        """
        pass
    @OutputGeometryLayer.setter
    def OutputGeometryLayer(self, outputGeomLayer: int):
        """
        Setter for property: (int) OutputGeometryLayer
         Returns the output geometry layer preference.  
           This option specifies the layer on which the output geometry should be placed.  
         
        """
        pass
import NXOpen
class RulesBasedJoinBulkCreateBuilder(CurveJoinBuilder): 
    """ Represents a RulesBasedJoinBulkCreateBuilder class """
    @property
    def BodySelection(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: ( NXOpen.SelectBodyList) BodySelection
         Returns the body selection   
            
         
        """
        pass
    @property
    def CombineWelds(self) -> bool:
        """
        Getter for property: (bool) CombineWelds
         Returns the indication to combine welds if tool faces are from same body.  
             
         
        """
        pass
    @CombineWelds.setter
    def CombineWelds(self, status: bool):
        """
        Setter for property: (bool) CombineWelds
         Returns the indication to combine welds if tool faces are from same body.  
             
         
        """
        pass
    @property
    def DuplicateCheck(self) -> bool:
        """
        Getter for property: (bool) DuplicateCheck
         Returns the indication to not create features if they would overlay existing curve join features.  
             
         
        """
        pass
    @DuplicateCheck.setter
    def DuplicateCheck(self, status: bool):
        """
        Setter for property: (bool) DuplicateCheck
         Returns the indication to not create features if they would overlay existing curve join features.  
             
         
        """
        pass
    @property
    def MaximumBodyGap(self) -> float:
        """
        Getter for property: (float) MaximumBodyGap
         Returns the maximum distance used when determining if two bodies are coincident.  
             
         
        """
        pass
    @MaximumBodyGap.setter
    def MaximumBodyGap(self, gapValue: float):
        """
        Setter for property: (float) MaximumBodyGap
         Returns the maximum distance used when determining if two bodies are coincident.  
             
         
        """
        pass
    @property
    def SubtypeId(self) -> str:
        """
        Getter for property: (str) SubtypeId
         Returns the Subtype   
            
         
        """
        pass
    @SubtypeId.setter
    def SubtypeId(self, type: str):
        """
        Setter for property: (str) SubtypeId
         Returns the Subtype   
            
         
        """
        pass
import NXOpen
class SubtypeAuthorAddNewAttributesBuilder(NXOpen.Builder): 
    """ Represents a SubtypeAuthorAddNewAttributesBuilder class """
    class DataTypes(Enum):
        """
        Members Include: 
         |Boolean| 
         |Integer| 
         |Double| 
         |String| 

        """
        Boolean: int
        Integer: int
        Double: int
        String: int
        @staticmethod
        def ValueOf(value: int) -> SubtypeAuthorAddNewAttributesBuilder.DataTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DataType(self) -> SubtypeAuthorAddNewAttributesBuilder.DataTypes:
        """
        Getter for property: ( SubtypeAuthorAddNewAttributesBuilder.DataTypes NXOpe) DataType
         Returns the data type   
            
         
        """
        pass
    @DataType.setter
    def DataType(self, dataType: SubtypeAuthorAddNewAttributesBuilder.DataTypes):
        """
        Setter for property: ( SubtypeAuthorAddNewAttributesBuilder.DataTypes NXOpe) DataType
         Returns the data type   
            
         
        """
        pass
    @property
    def StringValue(self) -> str:
        """
        Getter for property: (str) StringValue
         Returns the string value   
            
         
        """
        pass
    @StringValue.setter
    def StringValue(self, stringValue: str):
        """
        Setter for property: (str) StringValue
         Returns the string value   
            
         
        """
        pass
import NXOpen
class SubtypeAuthorValidValuesBuilder(NXOpen.Builder): 
    """ Represents a SubtypeAuthorValidValuesBuilder class """
    class ConstraintTypes(Enum):
        """
        Members Include: 
         |Equals| 
         |Min| 
         |Max| 
         |MinInclusive| 
         |MaxInclusive| 
         |NotEquals| 
         |Contains| 
         |DoesNotContain| 
         |BeginsWith| 
         |EndsWith| 

        """
        Equals: int
        Min: int
        Max: int
        MinInclusive: int
        MaxInclusive: int
        NotEquals: int
        Contains: int
        DoesNotContain: int
        BeginsWith: int
        EndsWith: int
        @staticmethod
        def ValueOf(value: int) -> SubtypeAuthorValidValuesBuilder.ConstraintTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ConstraintType(self) -> SubtypeAuthorValidValuesBuilder.ConstraintTypes:
        """
        Getter for property: ( SubtypeAuthorValidValuesBuilder.ConstraintTypes NXOpe) ConstraintType
         Returns the constraint   
            
         
        """
        pass
    @ConstraintType.setter
    def ConstraintType(self, constraint: SubtypeAuthorValidValuesBuilder.ConstraintTypes):
        """
        Setter for property: ( SubtypeAuthorValidValuesBuilder.ConstraintTypes NXOpe) ConstraintType
         Returns the constraint   
            
         
        """
        pass
    @property
    def DoubleValue(self) -> float:
        """
        Getter for property: (float) DoubleValue
         Returns the double value   
            
         
        """
        pass
    @DoubleValue.setter
    def DoubleValue(self, doubleValue: float):
        """
        Setter for property: (float) DoubleValue
         Returns the double value   
            
         
        """
        pass
    @property
    def IntValue(self) -> int:
        """
        Getter for property: (int) IntValue
         Returns the int value   
            
         
        """
        pass
    @IntValue.setter
    def IntValue(self, intValue: int):
        """
        Setter for property: (int) IntValue
         Returns the int value   
            
         
        """
        pass
    @property
    def StringValue(self) -> str:
        """
        Getter for property: (str) StringValue
         Returns the string value   
            
         
        """
        pass
    @StringValue.setter
    def StringValue(self, stringValue: str):
        """
        Setter for property: (str) StringValue
         Returns the string value   
            
         
        """
        pass
import NXOpen
import NXOpen.Features
class TransformBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a NXOpen.Join.TransformBuilder builder """
    class AssociativityTypes(Enum):
        """
        Members Include: 
         |SourceJoin|  Associative to source join. 
         |DestinationGeometry|  Associative to Destination geometry. 

        """
        SourceJoin: int
        DestinationGeometry: int
        @staticmethod
        def ValueOf(value: int) -> TransformBuilder.AssociativityTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TransformationTypes(Enum):
        """
        Members Include: 
         |Mirror|  Mirror 
         |Translate|  Translate 

        """
        Mirror: int
        Translate: int
        @staticmethod
        def ValueOf(value: int) -> TransformBuilder.TransformationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns the indication to create associative feature   
            
         
        """
        pass
    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
         Returns the indication to create associative feature   
            
         
        """
        pass
    @property
    def AssociativityType(self) -> TransformBuilder.AssociativityTypes:
        """
        Getter for property: ( TransformBuilder.AssociativityTypes NXOpe) AssociativityType
         Returns the associativity type   
            
         
        """
        pass
    @AssociativityType.setter
    def AssociativityType(self, associativityType: TransformBuilder.AssociativityTypes):
        """
        Setter for property: ( TransformBuilder.AssociativityTypes NXOpe) AssociativityType
         Returns the associativity type   
            
         
        """
        pass
    @property
    def ConnectedPartTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ConnectedPartTolerance
         Returns the expression containing the value of the connected part tolerance.  
             
         
        """
        pass
    @property
    def CreateHole(self) -> bool:
        """
        Getter for property: (bool) CreateHole
         Returns the hole creation status.  
           If true, holes should be created in connected bodies. If false, holes should be removed (or not created) from connected bodies   
         
        """
        pass
    @CreateHole.setter
    def CreateHole(self, status: bool):
        """
        Setter for property: (bool) CreateHole
         Returns the hole creation status.  
           If true, holes should be created in connected bodies. If false, holes should be removed (or not created) from connected bodies   
         
        """
        pass
    @property
    def EditSettingsOnly(self) -> bool:
        """
        Getter for property: (bool) EditSettingsOnly
         Returns the indication to only edit items in the settings group.  
           Mainly  NXOpen::Join::TransformBuilder::Associative , 
                     NXOpen::Join::TransformBuilder::LoadHardware , and  NXOpen::Join::TransformBuilder::CreateHole .
                    All other parameters will be left unchanged.   
         
        """
        pass
    @EditSettingsOnly.setter
    def EditSettingsOnly(self, status: bool):
        """
        Setter for property: (bool) EditSettingsOnly
         Returns the indication to only edit items in the settings group.  
           Mainly  NXOpen::Join::TransformBuilder::Associative , 
                     NXOpen::Join::TransformBuilder::LoadHardware , and  NXOpen::Join::TransformBuilder::CreateHole .
                    All other parameters will be left unchanged.   
         
        """
        pass
    @property
    def Features(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Features
         Returns the join features to transform   
            
         
        """
        pass
    @property
    def LoadHardware(self) -> bool:
        """
        Getter for property: (bool) LoadHardware
         Returns the hardware load status.  
           If true, loads hardware parts into assembly. If false, removes hardware parts.   
         
        """
        pass
    @LoadHardware.setter
    def LoadHardware(self, status: bool):
        """
        Setter for property: (bool) LoadHardware
         Returns the hardware load status.  
           If true, loads hardware parts into assembly. If false, removes hardware parts.   
         
        """
        pass
    @property
    def MirrorPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) MirrorPlane
         Returns the mirror plane, used when  NXOpen::Join::TransformBuilder::TransformationTypes  is set to   NXOpen::Join::TransformBuilder::TransformationTypesMirror     
            
         
        """
        pass
    @MirrorPlane.setter
    def MirrorPlane(self, mirrorPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) MirrorPlane
         Returns the mirror plane, used when  NXOpen::Join::TransformBuilder::TransformationTypes  is set to   NXOpen::Join::TransformBuilder::TransformationTypesMirror     
            
         
        """
        pass
    @property
    def TranslateCsys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) TranslateCsys
         Returns the coordinate system that defines the translate offset directions.  
           If not specified the absolute coordinate system will be used.
                    Used when  NXOpen::Join::TransformBuilder::TransformationTypes  is set to   NXOpen::Join::TransformBuilder::TransformationTypesTranslate     
         
        """
        pass
    @TranslateCsys.setter
    def TranslateCsys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) TranslateCsys
         Returns the coordinate system that defines the translate offset directions.  
           If not specified the absolute coordinate system will be used.
                    Used when  NXOpen::Join::TransformBuilder::TransformationTypes  is set to   NXOpen::Join::TransformBuilder::TransformationTypesTranslate     
         
        """
        pass
    @property
    def TranslateX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TranslateX
         Returns the expression containing the value of the x translation distance.  
           
                    Used when  NXOpen::Join::TransformBuilder::TransformationTypes  is set to   NXOpen::Join::TransformBuilder::TransformationTypesTranslate     
         
        """
        pass
    @property
    def TranslateY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TranslateY
         Returns the expression containing the value of the y translation distance.  
           
                    Used when  NXOpen::Join::TransformBuilder::TransformationTypes  is set to   NXOpen::Join::TransformBuilder::TransformationTypesTranslate     
         
        """
        pass
    @property
    def TranslateZ(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TranslateZ
         Returns the expression containing the value of the z translation distance.  
           
                    Used when  NXOpen::Join::TransformBuilder::TransformationTypes  is set to   NXOpen::Join::TransformBuilder::TransformationTypesTranslate     
         
        """
        pass
    @property
    def Type(self) -> TransformBuilder.TransformationTypes:
        """
        Getter for property: ( TransformBuilder.TransformationTypes NXOpe) Type
         Returns the transformation type   
            
         
        """
        pass
    @Type.setter
    def Type(self, transType: TransformBuilder.TransformationTypes):
        """
        Setter for property: ( TransformBuilder.TransformationTypes NXOpe) Type
         Returns the transformation type   
            
         
        """
        pass
import NXOpen
import NXOpen.Annotations
class WeldSymbolBuilder(NXOpen.Builder): 
    """ the Builder.Commit can produce more than one object. """
    @property
    def Objects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Objects
         Returns the objects (features) that are used to create Weld symbols.  
             
         
        """
        pass
    @property
    def Plane(self) -> NXOpen.Annotations.PlaneBuilder:
        """
        Getter for property: ( NXOpen.Annotations.PlaneBuilder) Plane
         Returns the  Annotations::PlaneBuilder  for the annotation.  
             
         
        """
        pass
    @property
    def Style(self) -> NXOpen.Annotations.StyleBuilder:
        """
        Getter for property: ( NXOpen.Annotations.StyleBuilder) Style
         Returns the  Annotations::StyleBuilder  for the annotation.  
             
         
        """
        pass
