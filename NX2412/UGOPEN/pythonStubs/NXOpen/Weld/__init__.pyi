from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.Assemblies
import NXOpen.Features
class AutoPointBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Weld.AutoPointBuilder builder """
    class InterferenceDetails(Enum):
        """
        Members Include: 
         |NoWeldsNearBodies|  Indicates no existing weld points are in this interference area 
         |Same|  Indicates weld points exist and part name are the same. 
         |Replaced|  Indicates weld points exist and part names have changed. 
         |Added|  Indicates weld points exist and parts were added. 
         |Deleted|  Indicates weld points exist and parts were removed. 

        """
        NoWeldsNearBodies: int
        Same: int
        Replaced: int
        Added: int
        Deleted: int
        @staticmethod
        def ValueOf(value: int) -> AutoPointBuilder.InterferenceDetails:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OrientationMethodTypes(Enum):
        """
        Members Include: 
         |SurfaceNormal|  Surface Normals. 
         |CoordinateSystem|  Use fixed csys instead of surface normals. 

        """
        SurfaceNormal: int
        CoordinateSystem: int
        @staticmethod
        def ValueOf(value: int) -> AutoPointBuilder.OrientationMethodTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |New|  new points are being created 
         |Move|  move existing points         

        """
        New: int
        Move: int
        @staticmethod
        def ValueOf(value: int) -> AutoPointBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ZDirection(Enum):
        """
        Members Include: 
         |FaceNormal|  along face normal  
         |Opposite|  opposite face normal 

        """
        FaceNormal: int
        Opposite: int
        @staticmethod
        def ValueOf(value: int) -> AutoPointBuilder.ZDirection:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ComponentsToJoin(self) -> NXOpen.Assemblies.SelectComponentList:
        """
        Getter for property: ( NXOpen.Assemblies.SelectComponentList) ComponentsToJoin
         Returns the components that should be welded together.  
           This can be one components, or many.   
         
        """
        pass
    @property
    def ComponentsTreatAsUnit(self) -> NXOpen.Assemblies.SelectComponentList:
        """
        Getter for property: ( NXOpen.Assemblies.SelectComponentList) ComponentsTreatAsUnit
         Returns the components to treat as unit.  
           No interferences will be found within this component.   
         
        """
        pass
    @property
    def DefaultZDirection(self) -> AutoPointBuilder.ZDirection:
        """
        Getter for property: ( AutoPointBuilder.ZDirection NXOpe) DefaultZDirection
         Returns the direction of the Z axis of the coordinate system for the feature.  
             
         
        """
        pass
    @DefaultZDirection.setter
    def DefaultZDirection(self, defaultZDirection: AutoPointBuilder.ZDirection):
        """
        Setter for property: ( AutoPointBuilder.ZDirection NXOpe) DefaultZDirection
         Returns the direction of the Z axis of the coordinate system for the feature.  
             
         
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
    def ManipulatorMatrix(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: ( NXOpen.Matrix3x3) ManipulatorMatrix
         Returns the rotation matrix to use for defining the feature csys.  
             
         
        """
        pass
    @ManipulatorMatrix.setter
    def ManipulatorMatrix(self, manipulatorMatrix: NXOpen.Matrix3x3):
        """
        Setter for property: ( NXOpen.Matrix3x3) ManipulatorMatrix
         Returns the rotation matrix to use for defining the feature csys.  
             
         
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
         Returns the maximum single metal thinkness for all the selected components.  
          
                    If the distance between top faces of two panels (or sheets) is greater
                    than single thickness plus face gap distance, a point will not be created
                    at that location.   
         
        """
        pass
    @MaximumSingleThickness.setter
    def MaximumSingleThickness(self, maximumSingleThickness: float):
        """
        Setter for property: (float) MaximumSingleThickness
         Returns the maximum single metal thinkness for all the selected components.  
          
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
    def MimimumNumberPointsOnOverlap(self) -> int:
        """
        Getter for property: (int) MimimumNumberPointsOnOverlap
         Returns the mimimum number points to create on an overlap sheet   
            
         
        """
        pass
    @MimimumNumberPointsOnOverlap.setter
    def MimimumNumberPointsOnOverlap(self, mimimumNumberPointsOnOverlap: int):
        """
        Setter for property: (int) MimimumNumberPointsOnOverlap
         Returns the mimimum number points to create on an overlap sheet   
            
         
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
    def OrientationMethod(self) -> AutoPointBuilder.OrientationMethodTypes:
        """
        Getter for property: ( AutoPointBuilder.OrientationMethodTypes NXOpe) OrientationMethod
         Returns the orientation method for defining a csys   
            
         
        """
        pass
    @OrientationMethod.setter
    def OrientationMethod(self, orientationMethod: AutoPointBuilder.OrientationMethodTypes):
        """
        Setter for property: ( AutoPointBuilder.OrientationMethodTypes NXOpe) OrientationMethod
         Returns the orientation method for defining a csys   
            
         
        """
        pass
    @property
    def ReuseFeatures(self) -> NXOpen.Features.SelectFeatureList:
        """
        Getter for property: ( NXOpen.Features.SelectFeatureList) ReuseFeatures
         Returns the feature to reuse intead of creating new.  
            These features will be updated instead of creating new.   
         
        """
        pass
    @property
    def ReuseMatchTolerance(self) -> float:
        """
        Getter for property: (float) ReuseMatchTolerance
         Returns the distance used to determine if the location of an existing weld feature is coincident with the 
                    newly calculated location.  
           If the locations are coincident, then the existing weld feature location will be reused.  
         
        """
        pass
    @ReuseMatchTolerance.setter
    def ReuseMatchTolerance(self, reuseMatchTolerance: float):
        """
        Setter for property: (float) ReuseMatchTolerance
         Returns the distance used to determine if the location of an existing weld feature is coincident with the 
                    newly calculated location.  
           If the locations are coincident, then the existing weld feature location will be reused.  
         
        """
        pass
    @property
    def Type(self) -> AutoPointBuilder.Types:
        """
        Getter for property: ( AutoPointBuilder.Types NXOpe) Type
         Returns the type of creation.  
             
         
        """
        pass
    @Type.setter
    def Type(self, type: AutoPointBuilder.Types):
        """
        Setter for property: ( AutoPointBuilder.Types NXOpe) Type
         Returns the type of creation.  
             
         
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
    @property
    def WeldType(self) -> WeldFeatureSetType:
        """
        Getter for property: ( WeldFeatureSetType NXOpe) WeldType
         Returns the weld point type to create   
            
         
        """
        pass
    @WeldType.setter
    def WeldType(self, weldPointType: WeldFeatureSetType):
        """
        Setter for property: ( WeldFeatureSetType NXOpe) WeldType
         Returns the weld point type to create   
            
         
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
         Finds all the interference areas between the selected components. This
                    must be executed or no weld points will be created. The number of regions is 
                    used as an index to get the interference status. The first index is 0. 
         Returns numInterferences (int): .
        """
        pass
    def GetInterferenceDetails(self, interferenceIndex: int) -> AutoPointBuilder.InterferenceDetails:
        """
         The status indicating if the interference has existing weld points touching it. The
                    index for this function is described in the find number of interference regions method. 
         Returns interferenceDetails ( AutoPointBuilder.InterferenceDetails NXOpe): .
        """
        pass
    @overload
    def GetWeldType(self) -> PointMarkBuilder.WeldTypes:
        """
         Gets the weld type references in the customer defaults to create. 
         Returns weldType ( PointMarkBuilder.WeldTypes NXOpe): .
        """
        pass
    def SetDisplayCsys(self, showCsys: bool) -> None:
        """
         Indicates whether the csys should be displayed on creation 
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
    @overload
    def SetWeldType(self, weldType: PointMarkBuilder.WeldTypes) -> None:
        """
         Sets the weld type references in the customer defaults to create. 
        """
        pass
import NXOpen.Features
class AutoPoint(NXOpen.Features.Feature): 
    """ This class will automatically create weld points from selected components """
    pass
import NXOpen
import NXOpen.Drawings
class AutoWeldSymbolsBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Weld.AutoWeldSymbolsBuilder builder """
    @property
    def DraftingViews(self) -> NXOpen.Drawings.SelectDraftingViewList:
        """
        Getter for property: ( NXOpen.Drawings.SelectDraftingViewList) DraftingViews
         Returns the candidate views for weld symbol creation    
            
         
        """
        pass
    @property
    def Welds(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Welds
         Returns the weld objects used to create the weld symbols in the drafting views   
            
         
        """
        pass
import NXOpen
class CharacteristicsBuilder(NXOpen.Builder): 
    """ This builder allows you to define the attribute values to be set on the
    output of the weld feature. """
    class Type(Enum):
        """
        Members Include: 
         |NotSet| 
         |FilletFeature| 
         |GrooveFeature| 
         |ResistanceSpotFeature| 
         |ArcSpotFeature| 
         |ClinchFeature| 
         |DollopFeature| 
         |WeldNutFeature| 
         |WeldStudFeature| 
         |Custom1PointFeature| 
         |Custom2PointFeature| 
         |Custom3PointFeature| 
         |Custom4PointFeature| 
         |Custom5PointFeature| 
         |DatumSurfaceFeature| 
         |DatumPinFeature| 
         |DatumCustom1Feature| 
         |DatumCustom2Feature| 
         |DatumCustom3Feature| 
         |MeasurementSurfaceFeature| 
         |MeasurementHoleFeature| 
         |MeasurementSlotFeature| 
         |MeasurementStudFeature| 
         |MeasurementTrimFeature| 
         |MeasurementHemFeature| 
         |MeasurementCustom1Feature| 
         |MeasurementCustom2Feature| 
         |MeasurementCustom3Feature| 
         |UserDefinedFeature| 
         |SealerFillFeature| 
         |SealerBeadFeature| 
         |JointFeature| 
         |PlugSlotFeature| 
         |ShipHull| 
         |ShipDeck| 
         |ShipTransverseBulkhead| 
         |ShipLongitudinalBulkhead| 
         |ShipGenericPlate| 
         |ShipStiffener| 
         |ShipEdgeReinforcement| 
         |ShipSeam| 
         |DatumSurfaceCustom0| 
         |DatumSurfaceCustom1| 
         |DatumSurfaceCustom2| 
         |DatumSurfaceCustom3| 
         |DatumSurfaceCustom4| 
         |DatumSurfaceCustom5| 
         |DatumSurfaceCustom6| 
         |DatumSurfaceCustom7| 
         |DatumPinCustom0| 
         |DatumPinCustom1| 
         |DatumPinCustom2| 
         |DatumPinCustom3| 
         |DatumPinCustom4| 
         |DatumPinCustom5| 
         |DatumPinCustom6| 
         |DatumPinCustom7| 
         |SurfaceWeld| 
         |ShipProfileCutOut| 
         |JointmarkFeature| 
         |ShipStandardPart| 
         |PointMarkResistanceSpot| 
         |PointMarkArcSpot| 
         |PointMarkDollop| 
         |PointMarkClinch| 
         |PointMarkWeldNut| 
         |PointMarkWeldStud| 
         |PointMarkCustom1| 
         |PointMarkCustom2| 
         |PointMarkCustom3| 
         |PointMarkCustom4| 
         |PointMarkCustom5| 
         |ShipBracket| 
         |ShipCollarPlate| 
         |DatumEdgeFeature| 
         |DatumEdgeCustom0| 
         |DatumEdgeCustom1| 
         |DatumEdgeCustom2| 
         |DatumEdgeCustom3| 
         |DatumEdgeCustom4| 
         |DatumEdgeCustom5| 
         |DatumEdgeCustom6| 
         |DatumEdgeCustom7| 
         |ShipStructuralElement| 

        """
        NotSet: int
        FilletFeature: int
        GrooveFeature: int
        ResistanceSpotFeature: int
        ArcSpotFeature: int
        ClinchFeature: int
        DollopFeature: int
        WeldNutFeature: int
        WeldStudFeature: int
        Custom1PointFeature: int
        Custom2PointFeature: int
        Custom3PointFeature: int
        Custom4PointFeature: int
        Custom5PointFeature: int
        DatumSurfaceFeature: int
        DatumPinFeature: int
        DatumCustom1Feature: int
        DatumCustom2Feature: int
        DatumCustom3Feature: int
        MeasurementSurfaceFeature: int
        MeasurementHoleFeature: int
        MeasurementSlotFeature: int
        MeasurementStudFeature: int
        MeasurementTrimFeature: int
        MeasurementHemFeature: int
        MeasurementCustom1Feature: int
        MeasurementCustom2Feature: int
        MeasurementCustom3Feature: int
        UserDefinedFeature: int
        SealerFillFeature: int
        SealerBeadFeature: int
        JointFeature: int
        PlugSlotFeature: int
        ShipHull: int
        ShipDeck: int
        ShipTransverseBulkhead: int
        ShipLongitudinalBulkhead: int
        ShipGenericPlate: int
        ShipStiffener: int
        ShipEdgeReinforcement: int
        ShipSeam: int
        DatumSurfaceCustom0: int
        DatumSurfaceCustom1: int
        DatumSurfaceCustom2: int
        DatumSurfaceCustom3: int
        DatumSurfaceCustom4: int
        DatumSurfaceCustom5: int
        DatumSurfaceCustom6: int
        DatumSurfaceCustom7: int
        DatumPinCustom0: int
        DatumPinCustom1: int
        DatumPinCustom2: int
        DatumPinCustom3: int
        DatumPinCustom4: int
        DatumPinCustom5: int
        DatumPinCustom6: int
        DatumPinCustom7: int
        SurfaceWeld: int
        ShipProfileCutOut: int
        JointmarkFeature: int
        ShipStandardPart: int
        PointMarkResistanceSpot: int
        PointMarkArcSpot: int
        PointMarkDollop: int
        PointMarkClinch: int
        PointMarkWeldNut: int
        PointMarkWeldStud: int
        PointMarkCustom1: int
        PointMarkCustom2: int
        PointMarkCustom3: int
        PointMarkCustom4: int
        PointMarkCustom5: int
        ShipBracket: int
        ShipCollarPlate: int
        DatumEdgeFeature: int
        DatumEdgeCustom0: int
        DatumEdgeCustom1: int
        DatumEdgeCustom2: int
        DatumEdgeCustom3: int
        DatumEdgeCustom4: int
        DatumEdgeCustom5: int
        DatumEdgeCustom6: int
        DatumEdgeCustom7: int
        ShipStructuralElement: int
        @staticmethod
        def ValueOf(value: int) -> CharacteristicsBuilder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def InheritObject(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) InheritObject
         Returns the selection object containing data that is used to define the attribute values.  
             
         
        """
        pass
    @property
    def Selected(self) -> CharacteristicsValueBuilder:
        """
        Getter for property: ( CharacteristicsValueBuilder NXOpe) Selected
         Returns the selected characteristic value.  
             
         
        """
        pass
    @Selected.setter
    def Selected(self, valueBuilder: CharacteristicsValueBuilder):
        """
        Setter for property: ( CharacteristicsValueBuilder NXOpe) Selected
         Returns the selected characteristic value.  
             
         
        """
        pass
    @property
    def SelectionList(self) -> NXOpen.NXObjectList:
        """
        Getter for property: ( NXOpen.NXObjectList) SelectionList
         Returns the list of potential attributes and objects selected for this weld feature.  
             
         
        """
        pass
    def ApplyAttributes(self, objects: List[NXOpen.NXObject]) -> None:
        """
         Apply the selected attributes to the objects. 
        """
        pass
    def ApplyAttributesToSelected(self) -> None:
        """
         Apply the selected attributes to the objects that were selected. 
        """
        pass
    @overload
    def AreAttributesDefault(self, weldType: int) -> bool:
        """
         Returns true if the characteristics builder contains all attributes with default values. 
         Returns status (bool): .
        """
        pass
    @overload
    def AreAttributesDefault(self, charxType: CharacteristicsBuilder.Type) -> bool:
        """
         Returns true if the characteristics builder contains all attributes with default values. 
         Returns status (bool): .
        """
        pass
    @overload
    def ChangeFeatureType(self, weldType: int) -> None:
        """
         Change the type of feature defining the attributes. 
                    Note after calling this method, the WeldJA::CharacteristicsValueBuilder objects 
                    previously retrieved will be invalid. You need to reaccess them if you want to
                    make any changes to them. 
        """
        pass
    @overload
    def ChangeFeatureType(self, charxType: CharacteristicsBuilder.Type) -> None:
        """
         Change the type of feature defining the attributes. 
                    Note after calling this method, the WeldJA::CharacteristicsValueBuilder objects 
                    previously retrieved will be invalid. You need to reaccess them if you want to
                    make any changes to them. 
        """
        pass
    def CopyAttributesFromObject(self, objectValue: NXOpen.NXObject) -> None:
        """
         Copy the attributes that are on the object to the selection. 
        """
        pass
    def CopyAttributesFromObjectForPaint(self, objectTag: NXOpen.NXObject) -> None:
        """
         Copies the attributes that are on the object to the selection for paint. 
        """
        pass
    def CopyNonActiveAttributesFromObject(self, objectValue: NXOpen.NXObject) -> None:
        """
         Copy the non active attributes that are on the object to the selection. 
        """
        pass
    @overload
    def CreateSelectionSet(self, weldType: int, data: NXOpen.NXObject) -> CharacteristicsSelectionBuilder:
        """
         Create a new selection set and add it to the list. 
         Returns selectionBuilder ( CharacteristicsSelectionBuilder NXOpe): .
        """
        pass
    @overload
    def CreateSelectionSet(self, charxType: CharacteristicsBuilder.Type, data: NXOpen.NXObject) -> CharacteristicsSelectionBuilder:
        """
         Create a new selection set and add it to the list. 
         Returns selectionBuilder ( CharacteristicsSelectionBuilder NXOpe): .
        """
        pass
    def DoesObjectHaveAttributes(self, objectValue: NXOpen.NXObject) -> bool:
        """
         Copy the attributes that are on the object to the selection and returns a flag indicating whether the object actually has attributes. 
         Returns status (bool): .
        """
        pass
    def HasActiveValues(self) -> bool:
        """
         Returns true if the characteristics builder has any active values. 
         Returns status (bool): .
        """
        pass
    def InheritAttributesFromObject(self, objectValue: NXOpen.NXObject) -> None:
        """
         Inherit the attributes that are on the object to the selection. 
        """
        pass
    def RemoveAllAttributes(self, objects: List[NXOpen.NXObject]) -> None:
        """
         Remove all attributes from the objects. 
        """
        pass
    def RemoveInheritedAttributes(self) -> None:
        """
         Remove any attributes that are inherited from other objects (for example, edges).  These will be attributes that are
                    not required and are not in a category. 
        """
        pass
    @overload
    def SetAllAttributesChanged(self) -> None:
        """
         Sets all attributes to be changed. 
        """
        pass
    @overload
    def SetAllAttributesChanged(self, status: bool) -> None:
        """
         Sets all attributes changed value to the status value. 
        """
        pass
import NXOpen
class CharacteristicsSelectionBuilder(NXOpen.NXObject): 
    """ This builder allows you to define the attribute values to be set on the
    output of the weld feature.
    The inheritance option only applies to the NXOpen.Weld.WeldJoint.
     """
    @property
    def AttributeList(self) -> NXOpen.NXObjectList:
        """
        Getter for property: ( NXOpen.NXObjectList) AttributeList
         Returns the list of potential attributes for this weld feature.  
             
         
        """
        pass
    @property
    def SelectObjectList(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SelectObjectList
         Returns the selection object containing data that is to be attributed.  
             
         
        """
        pass
    @overload
    def CreateAttributeListEntry(self, required: bool, onObject: bool, locked: bool, iconName: str, pointMarker: int, color: int, title: str) -> CharacteristicsValueBuilder:
        """
         Create an attribute list entry, that has no value, and add it to the list. 
         Returns listEntry ( CharacteristicsValueBuilder NXOpe): .
        """
        pass
    @overload
    def CreateAttributeListEntry(self, required: bool, onObject: bool, locked: bool, inherited: bool, iconName: str, pointMarker: int, color: int, title: str) -> CharacteristicsValueBuilder:
        """
         Create an attribute list entry, that has no value, and add it to the list. 
         Returns listEntry ( CharacteristicsValueBuilder NXOpe): .
        """
        pass
    @overload
    def CreateDoubleAttributeListEntry(self, required: bool, onObject: bool, locked: bool, iconName: str, pointMarker: int, color: int, title: str, currentValue: float) -> CharacteristicsValueBuilder:
        """
         Create a double attribute list entry and add it to the list. 
         Returns listEntry ( CharacteristicsValueBuilder NXOpe): .
        """
        pass
    @overload
    def CreateDoubleAttributeListEntry(self, required: bool, onObject: bool, locked: bool, inherited: bool, iconName: str, pointMarker: int, color: int, title: str, currentValue: float) -> CharacteristicsValueBuilder:
        """
         Create a double attribute list entry and add it to the list. 
         Returns listEntry ( CharacteristicsValueBuilder NXOpe): .
        """
        pass
    @overload
    def CreateIntegerAttributeListEntry(self, required: bool, onObject: bool, locked: bool, iconName: str, pointMarker: int, color: int, title: str, currentValue: int) -> CharacteristicsValueBuilder:
        """
         Create an integer attribute list entry and add it to the list. 
         Returns listEntry ( CharacteristicsValueBuilder NXOpe): .
        """
        pass
    @overload
    def CreateIntegerAttributeListEntry(self, required: bool, onObject: bool, locked: bool, inherited: bool, iconName: str, pointMarker: int, color: int, title: str, currentValue: int) -> CharacteristicsValueBuilder:
        """
         Create an integer attribute list entry and add it to the list. 
         Returns listEntry ( CharacteristicsValueBuilder NXOpe): .
        """
        pass
    @overload
    def CreateOptionAttributeListEntry(self, required: bool, onObject: bool, locked: bool, iconName: str, pointMarker: int, color: int, title: str, currentValue: str, options: List[str]) -> CharacteristicsValueBuilder:
        """
         Create an option attribute list entry and add it to the list. 
         Returns listEntry ( CharacteristicsValueBuilder NXOpe): .
        """
        pass
    @overload
    def CreateOptionAttributeListEntry(self, required: bool, onObject: bool, locked: bool, inherited: bool, iconName: str, pointMarker: int, color: int, title: str, currentValue: str, options: List[str]) -> CharacteristicsValueBuilder:
        """
         Create an option attribute list entry and add it to the list. 
         Returns listEntry ( CharacteristicsValueBuilder NXOpe): .
        """
        pass
    @overload
    def CreateStringAttributeListEntry(self, required: bool, onObject: bool, locked: bool, iconName: str, pointMarker: int, color: int, title: str, currentValue: str) -> CharacteristicsValueBuilder:
        """
         Create a string attribute list entry and add it to the list. 
         Returns listEntry ( CharacteristicsValueBuilder NXOpe): .
        """
        pass
    @overload
    def CreateStringAttributeListEntry(self, required: bool, onObject: bool, locked: bool, inherited: bool, iconName: str, pointMarker: int, color: int, title: str, currentValue: str) -> CharacteristicsValueBuilder:
        """
         Create a string attribute list entry and add it to the list. 
         Returns listEntry ( CharacteristicsValueBuilder NXOpe): .
        """
        pass
import NXOpen
class CharacteristicsValueBuilder(NXOpen.NXObject): 
    """ The object containing the information about the attribute to be 
    placed on the output of the weld feature.
    The inheritance option only applies to the NXOpen.Weld.WeldJoint.
     """
    class Type(Enum):
        """
        Members Include: 
         |String|  Indicates the attribute value contains a string. 
         |Integer|  Indicates the attribute value contains a integer. 
         |Double|  Indicates the attribute value contains a double. 
         |Option|  Indicates the attribute value contains a pre set list of strings. 
         |NotSet|  Indicates there is no attribute value. 

        """
        String: int
        Integer: int
        Double: int
        Option: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> CharacteristicsValueBuilder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Active(self) -> bool:
        """
        Getter for property: (bool) Active
         Returns the indication if the attribute is to be placed on the output.  
           true indicates
                the attribute will be placed on the output, false indicates the attribute will not
                be placed on the output. Note that if Required is true, then this property cannot be 
                set.   
         
        """
        pass
    @Active.setter
    def Active(self, active: bool):
        """
        Setter for property: (bool) Active
         Returns the indication if the attribute is to be placed on the output.  
           true indicates
                the attribute will be placed on the output, false indicates the attribute will not
                be placed on the output. Note that if Required is true, then this property cannot be 
                set.   
         
        """
        pass
    @property
    def AttributeType(self) -> CharacteristicsValueBuilder.Type:
        """
        Getter for property: ( CharacteristicsValueBuilder.Type NXOpe) AttributeType
         Returns the type of this attribute.  
             
         
        """
        pass
    @property
    def Inherited(self) -> bool:
        """
        Getter for property: (bool) Inherited
         Returns the indication if the attribute value is inherited from the source object.  
             
         
        """
        pass
    @Inherited.setter
    def Inherited(self, inherited: bool):
        """
        Setter for property: (bool) Inherited
         Returns the indication if the attribute value is inherited from the source object.  
             
         
        """
        pass
    @property
    def Required(self) -> bool:
        """
        Getter for property: (bool) Required
         Returns the indication if the attribute is required to be placed on the output.  
           true indicates
                the attribute will always be placed on the output, false indicates the attribute does not 
                have to be placed on the output.   
         
        """
        pass
    @property
    def Title(self) -> str:
        """
        Getter for property: (str) Title
         Returns the title of this attribute.  
             
         
        """
        pass
    @property
    def ValueChanged(self) -> bool:
        """
        Getter for property: (bool) ValueChanged
         Returns the indication if the attribute value has been changed.  
             
         
        """
        pass
    @ValueChanged.setter
    def ValueChanged(self, status: bool):
        """
        Setter for property: (bool) ValueChanged
         Returns the indication if the attribute value has been changed.  
             
         
        """
        pass
    @property
    def ValueDouble(self) -> float:
        """
        Getter for property: (float) ValueDouble
         Returns the value of this attribute when AttributeType is  Weld::CharacteristicsValueBuilder::TypeDouble .  
             
         
        """
        pass
    @ValueDouble.setter
    def ValueDouble(self, valueDouble: float):
        """
        Setter for property: (float) ValueDouble
         Returns the value of this attribute when AttributeType is  Weld::CharacteristicsValueBuilder::TypeDouble .  
             
         
        """
        pass
    @property
    def ValueInteger(self) -> int:
        """
        Getter for property: (int) ValueInteger
         Returns the value of this attribute when AttributeType is  Weld::CharacteristicsValueBuilder::TypeInteger .  
             
         
        """
        pass
    @ValueInteger.setter
    def ValueInteger(self, valueInteger: int):
        """
        Setter for property: (int) ValueInteger
         Returns the value of this attribute when AttributeType is  Weld::CharacteristicsValueBuilder::TypeInteger .  
             
         
        """
        pass
    @property
    def ValueString(self) -> str:
        """
        Getter for property: (str) ValueString
         Returns the value of this attribute when AttributeType is  Weld::CharacteristicsValueBuilder::TypeString  or
                     Weld::CharacteristicsValueBuilder::TypeOption .  
             
         
        """
        pass
    @ValueString.setter
    def ValueString(self, valueString: str):
        """
        Setter for property: (str) ValueString
         Returns the value of this attribute when AttributeType is  Weld::CharacteristicsValueBuilder::TypeString  or
                     Weld::CharacteristicsValueBuilder::TypeOption .  
             
         
        """
        pass
    def GetOptionStrings(self) -> List[str]:
        """
         The list of strings that are available to be set when AttributeType is Weld.CharacteristicsValueBuilder.Type.Option. 
         Returns strings (List[str]):  Strings that are allowed for values. .
        """
        pass
import NXOpen.Features
class CompoundWeldBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a NXOpen.Weld.CompoundWeld builder.
    """
    @property
    def Side1Welds(self) -> NXOpen.Features.SelectFeatureList:
        """
        Getter for property: ( NXOpen.Features.SelectFeatureList) Side1Welds
         Returns the weld features defining side 1 of the compound weld.  
             
         
        """
        pass
    @property
    def Side2Welds(self) -> NXOpen.Features.SelectFeatureList:
        """
        Getter for property: ( NXOpen.Features.SelectFeatureList) Side2Welds
         Returns the weld features defining side 2 of the compound weld.  
             
         
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
class CompoundWeld(NXOpen.Features.Feature): 
    """ Represents a compound weld feature. """
    pass
import NXOpen
class ConnectedFaceFinderBuilder(NXOpen.Builder): 
    """
    Represents a builder to run the Connected Face Finder operation.
    """
    @property
    def ConnectionFinder(self) -> ConnectionFinderBuilder:
        """
        Getter for property: ( ConnectionFinderBuilder NXOpe) ConnectionFinder
         Returns the connection finder object that manages the interaction.  
             
         
        """
        pass
    @property
    def ListFeatureSet(self) -> bool:
        """
        Getter for property: (bool) ListFeatureSet
         Returns the option if set to true will list the search results according to the feature sets that the specified weld point belongs to.  
             
         
        """
        pass
    @ListFeatureSet.setter
    def ListFeatureSet(self, listFeatureSet: bool):
        """
        Setter for property: (bool) ListFeatureSet
         Returns the option if set to true will list the search results according to the feature sets that the specified weld point belongs to.  
             
         
        """
        pass
    @property
    def RetainedWelds(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) RetainedWelds
         Returns the retained weld objects that need to be reconnected.  
             
         
        """
        pass
    def PerformAnalysis(self) -> None:
        """
         Process the selected retained welds and populate the list with appropriate faces to reconnect the weld too.  
        """
        pass
import NXOpen
class ConnectedPart(NXOpen.TransientObject): 
    """ Represents weld connected part to customize the retrieval of connected part information. """
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
            is called, it is illegal to use the object.  In .NET, this method
            is automatically called when the object is deleted by the garbage
            collector. 
        """
        pass
    def GetNumberSets(self) -> int:
        """
         Get the number of connected sets. Use this to limit the number of iterations when calling NXOpen.Weld.ConnectedPart.GetSetInformation. 
         Returns numberOfSets (int): .
        """
        pass
    def GetSetInformation(self, setIndex: int) -> List[NXOpen.NXObject]:
        """
         Get the individual connected set data. 
         Returns eids ( NXOpen.NXObject Li):  Array of connected set information. Should be freed.
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ConnectionFinderBuilder(NXOpen.TaggedObject): 
    """
    Represents a builder to display, manage, delete, and allow the user to
    reparent face information for the weld objects.
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
        def ValueOf(value: int) -> ConnectionFinderBuilder.FilterTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Filter(self) -> ConnectionFinderBuilder.FilterTypes:
        """
        Getter for property: ( ConnectionFinderBuilder.FilterTypes NXOpe) Filter
         Returns the filter values to contol Save All processing.  
             
         
        """
        pass
    @Filter.setter
    def Filter(self, filter: ConnectionFinderBuilder.FilterTypes):
        """
        Setter for property: ( ConnectionFinderBuilder.FilterTypes NXOpe) Filter
         Returns the filter values to contol Save All processing.  
             
         
        """
        pass
    @property
    def IgnoreHoles(self) -> bool:
        """
        Getter for property: (bool) IgnoreHoles
         Returns the option to indicate if holes should be ignored when finding faces.  
             
         
        """
        pass
    @IgnoreHoles.setter
    def IgnoreHoles(self, ignoreHoles: bool):
        """
        Setter for property: (bool) IgnoreHoles
         Returns the option to indicate if holes should be ignored when finding faces.  
             
         
        """
        pass
    @property
    def ListFeatureSet(self) -> bool:
        """
        Getter for property: (bool) ListFeatureSet
         Returns the option to list the search results according to the feature sets that the specified weld point belongs to.  
             
         
        """
        pass
    @ListFeatureSet.setter
    def ListFeatureSet(self, listFeatureSet: bool):
        """
        Setter for property: (bool) ListFeatureSet
         Returns the option to list the search results according to the feature sets that the specified weld point belongs to.  
             
         
        """
        pass
    @property
    def ReassignEdge(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) ReassignEdge
         Returns the edges to use when the reassign button is invoked.  
             
         
        """
        pass
    @property
    def ReassignFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) ReassignFace
         Returns the faces to use when the reassign button is invoked.  
             
         
        """
        pass
    @property
    def UpdateCoordinateSystem(self) -> bool:
        """
        Getter for property: (bool) UpdateCoordinateSystem
         Returns the option to update the coordinate system for the node from the obtained reconnection when saved.  
             
         
        """
        pass
    @UpdateCoordinateSystem.setter
    def UpdateCoordinateSystem(self, updateCoordinateSystem: bool):
        """
        Setter for property: (bool) UpdateCoordinateSystem
         Returns the option to update the coordinate system for the node from the obtained reconnection when saved.  
             
         
        """
        pass
    def CenterNode(self, nodeTag: NXOpen.NXObject) -> None:
        """
         Adjusts the display of the part and fits the selected weld points in the center of the graphics window. 
        """
        pass
    def ClearAllTree(self) -> None:
        """
         Clears the tree list and allows you to perform another search. 
        """
        pass
    def ClearMarking(self, nodeTag: NXOpen.NXObject) -> None:
        """
         Unmarks (removes save or delete mark) the weld feature from processing. 
        """
        pass
    def DeleteNode(self, nodeTag: NXOpen.NXObject) -> None:
        """
         Deletes the connected part information from the results. 
        """
        pass
    def GetEdgeNodeCollector(self, weldObject: NXOpen.NXObject, edgeNodeIndex: int) -> NXOpen.ScCollector:
        """
         Get the edge collector for a specific weld object and index. This is useful when the edge node for the object is empty and you need to populate it. Search will be limited by the list feature set setting. 
         Returns edgeCollector ( NXOpen.ScCollector):  Can return  if not found. .
        """
        pass
    def GetFaceNodeCollector(self, weldObject: NXOpen.NXObject, faceNodeIndex: int) -> NXOpen.ScCollector:
        """
         Get the face collector for a specific weld object and index. This is useful when the face node for the object is empty and you need to populate it. Search will be limited by the list feature set setting. 
         Returns faceCollector ( NXOpen.ScCollector):  Can return  if not found. .
        """
        pass
    def GetFaces(self, weldObject: NXOpen.NXObject) -> List[NXOpen.ScCollector]:
        """
         Get the face collectors for the given feature set or point depending on the NXOpen.Weld.ConnectionFinderBuilder.ListFeatureSet. 
         Returns faceCollectors ( NXOpen.ScCollector Li):  Face Collectors. .
        """
        pass
    def IsEdgeNodeEmpty(self, weldObject: NXOpen.NXObject, edgeNodeIndex: int) -> bool:
        """
         Identify if the edge collector for a specific weld object and index has edges assigned to it. Search will be limited by the list feature set setting. An error will be returned if the edge node cannot be found or the collector is missing. 
         Returns isEmpty (bool): .
        """
        pass
    def IsFaceNodeEmpty(self, weldObject: NXOpen.NXObject, faceNodeIndex: int) -> bool:
        """
         Identify if the face collector for a specific weld object and index has faces assigned to it. Search will be limited by the list feature set setting. An error will be returned if the face node cannot be found or the collector is missing. 
         Returns isEmpty (bool): .
        """
        pass
    def ReassignEdgeNode(self, ownerTag: NXOpen.NXObject, nodeTag: NXOpen.NXObject) -> None:
        """
         Reassign the edges from the Reassign Edge collector to the specified node. 
        """
        pass
    def ReassignFaceNode(self, ownerTag: NXOpen.NXObject, nodeTag: NXOpen.NXObject) -> None:
        """
         Reassign the faces from the Reassign Face collector to the specified node. 
        """
        pass
    def ReorderAfterEdgeNode(self, parentTag: NXOpen.NXObject, edgeSetIndexToMove: int, edgeSetIndexToReoderAfter: int) -> None:
        """
         Reorders a selected edge by putting it after the specified edge. Indices start at 0 for the 1st element. 
        """
        pass
    def ReorderAfterFaceNode(self, parentTag: NXOpen.NXObject, faceSetIndexToMove: int, faceSetIndexToReoderAfter: int) -> None:
        """
         Reorders a selected face by putting it after the specified face. Indices start at 0 for the 1st element. 
        """
        pass
    def ReorderBeforeEdgeNode(self, parentTag: NXOpen.NXObject, edgeSetIndexToMove: int, edgeSetIndexToReoderBefore: int) -> None:
        """
         Reorders a selected edge by putting it before the specified edge. Indices start at 0 for the 1st element. 
        """
        pass
    def ReorderBeforeFaceNode(self, parentTag: NXOpen.NXObject, faceSetIndexToMove: int, faceSetIndexToReoderBefore: int) -> None:
        """
         Reorders a selected face by putting it before the specified face. Indices start at 0 for the 1st element. 
        """
        pass
    def RequiredFaceNode(self, nodeTag: NXOpen.NXObject, isRequired: bool) -> None:
        """
         Identify if the face node is required (true) or optional (false). This is used in the case where a weld point has been identified as having faces from only 1 connected part. 
        """
        pass
    def SaveAllTree(self) -> None:
        """
         Identify all the connected part information as "saved" so the commit will save the information. Dependent on value of NXOpen.Weld.ConnectionFinderBuilder.FilterTypes. Will not mark nodes identified in failure condition. 
        """
        pass
    def SaveNode(self, nodeTag: NXOpen.NXObject) -> None:
        """
         Identify the connected part information as "saved" so commit will save the information. 
        """
        pass
import NXOpen
import NXOpen.Features
class CustomManager(NXOpen.TaggedObjectCollection): 
    """ Represents weld interface to customize the creation of welding joint features.

   
   The "welding joint handler" customization callback is called after the feature is created.
   One can then set edge preparation parameters, change the color of the feature output curve,
   add attributes to the feature, or any additional customization.

   The "variable bevel handler" customization callback is used to define the limits where a welding joint
   should be split at. 
 
  
  """
    class DeleteOption(Enum):
        """
        Members Include: 
         |All|  Delete all design features under design control feature. 
         |InputOnly|  Delete only the input design feature. Only valid if design feature is input. 

        """
        All: int
        InputOnly: int
        @staticmethod
        def ValueOf(value: int) -> CustomManager.DeleteOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PmiSource(Enum):
        """
        Members Include: 
         |Preview|  PMI created for Edit Joint Parameters preview. 
         |FabricationPmi|  PMI created in Fabrication PMI dialog. 

        """
        Preview: int
        FabricationPmi: int
        @staticmethod
        def ValueOf(value: int) -> CustomManager.PmiSource:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    DatumIconHandler = Callable[[DatumIconBuilder], None]
    def AddDatumIconHandler(handler: CustomManager.DatumIconHandler) -> int:
        """
         Registers a user defined method to be notified when the part navigator is updating the surface or pin datum icon. 
         Returns id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    JointPmiCreated = Callable[[CustomManager.PmiSource, List[NXOpen.Annotations.PmiLineWeld], JointExitBuilder], None]
    def AddJointPmiCreated(handler: CustomManager.JointPmiCreated) -> int:
        """
         Registers a user defined method that is called whenever a NXOpen.Annotations.PmiLineWeld is created. 
         Returns id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    ModifyFeatureHandler = Callable[[WeldObjectBuilder], None]
    def AddModifyFeatureHandler(handler: CustomManager.ModifyFeatureHandler) -> int:
        """
         Registers a user defined method to be notified when weld features are created or edited. 
         Returns id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    PipeJointSetType = Callable[[JointItemBuilder], None]
    def AddPipeJointSetType(handler: CustomManager.PipeJointSetType) -> int:
        """
         Registers a user defined method that is called whenever a welding joint is created 
         Returns id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    PointExitHandler = Callable[[WeldPointExitBuilder], None]
    def AddPointExitHandler(handler: CustomManager.PointExitHandler) -> int:
        """
         Registers a user defined method to be notified when weld point features are created. 
         Returns id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    VariableBevelHandler = Callable[[WeldJointBuilder, NXOpen.Curve], None]
    def AddVariableBevelHandler(handler: CustomManager.VariableBevelHandler) -> int:
        """
         Registers a user defined method to define variable bevel angles. The method will be called from the Weld Joint user Interface. 
         Returns id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    WeldJointHandler = Callable[[JointExitBuilder], None]
    def AddWeldJointHandler(handler: CustomManager.WeldJointHandler) -> int:
        """
         Registers a user defined method that is called whenever a welding joint is created or updated 
         Returns id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    def AskConnectedParts(weldTag: NXOpen.NXObject) -> ConnectedPart:
        """
          Find the connected part information for the weld feature, curve, point or body.
          NXOpen.Weld.CustomManager.LocateWelds can be used to retrieve weld data from a part.
          
          The data is stored in NXOpen.Weld.ConnectedPart containing the appropriate
          connected part information. If the weld input is an occurrence then a body or part occurences
          will be returned in the output structures for reading the attributes on the connected parts.
           
         Returns data ( ConnectedPart NXOpe):  Connected parts information.  if none are found. .
        """
        pass
    @overload
    def ConvertLegacy() -> None:
        """
         Method to convert all legacy weld points to the NXOpen.Weld.PointMarkPoint class 
        """
        pass
    def ConvertLegacyJoint(feature: NXOpen.Features.Feature) -> None:
        """
         Converts legacy welding joints to split joints. 
        """
        pass
    @overload
    def ConvertLegacy(fsetFeatures: List[NXOpen.Features.Feature]) -> None:
        """
         Method to convert selected legacy weld point feature sets to the NXOpen.Weld.PointMarkPoint class 
        """
        pass
    @overload
    def ConvertLegacy(fsetFeatures: List[NXOpen.Features.Feature], createSingleFeatures: bool) -> None:
        """
         Method to convert weld point feature sets to the NXOpen.Weld.PointMarkPoint class 
        """
        pass
    def ConvertTransformWeld(selectedObjects: List[NXOpen.Features.Feature]) -> None:
        """
         Method to convert NXOpen.Weld.Transform to their parent type. For example, if a NXOpen.Weld.WeldBead is
              the parent, this function will convert the NXOpen.Weld.Transform to a NXOpen.Weld.WeldBead in the location of the  
              the NXOpen.Weld.Transform. 
        """
        pass
    def CreateFeatureGroupsForCommonConnectedParts(weldFeatures: List[JointmarkElement]) -> None:
        """
         Method to creates Feature Groups to collect individual weld point features that have the same connected part attributes.
          
           Calling with numWeldFeatures equal to zero will cause all NXOpen.Weld.JointmarkElement in the work part to be grouped.
           Connected parts A-B-C and C-B-A will be in the same group.
            
        """
        pass
    def DeleteDesignFeatures(deleteOption: CustomManager.DeleteOption, designObject: NXOpen.TaggedObject) -> None:
        """
         Delete design features (DF) under a design control element (DCE). Function takes either a DCE or DF as input.
              If a DCE is passed in, all DFs under the DCE will be deleted. If a DF is passed in, the deletion will be done according to the 
              setting of NXOpen.Weld.CustomManager.DeleteOption 
          
        """
        pass
    def GetMasterJointCollectorOfSplitFeature(feature: NXOpen.Features.Feature) -> NXOpen.ScCollector:
        """
         Returns  NXOpen.ScCollector  contained in master NXOpen.Weld.WeldJoint. 
         Returns collector ( NXOpen.ScCollector):  A collector in master joint .
        """
        pass
    def HasSourceFacesInWeldPart(weldFeature: NXOpen.Features.Feature) -> List[bool]:
        """
         Method to determine if a NXOpen.Weld.JointmarkElement feature has source faces in the weld part. 
         Returns areSourceFacesInWeldPart (List[bool]):  Indicates if source faces are in the weld part. .
        """
        pass
    def ImpactAnalysisCheck(selectedObjects: List[NXOpen.NXObject]) -> None:
        """
         Method to perform the Weld Impace Analysis command. This will fully load connected parts of the selected objects and generate navigator alert messages if input faces,  or feature specific parameters have changed. 
        """
        pass
    def ImpactAnalysisCheckConnectedParts(selectedObjects: List[NXOpen.NXObject]) -> None:
        """
         Method to perform check if a features connected parts are missing. This will generate navigator alert messages if connected parts are missing. 
        """
        pass
    def ImpactAnalysisConfirm(selectedObjects: List[NXOpen.NXObject]) -> None:
        """
         Method to approve all alerts generated by the Weld Assistant Impact Analysis command. New alert messages are based on the approved objects. 
        """
        pass
    @overload
    def LocateWelds(searchEntireAssembly: bool, wantSolids: bool, wantCurves: bool, wantPoints: bool) -> List[NXOpen.NXObject]:
        """
         Method to search all fully loaded parts for welding objects in an assembly or part file. An array of solids, curves and points can be output 
         Returns foundObjectsArray ( NXOpen.NXObject Li):  Array of objects passing the search criteria specified. .
        """
        pass
    @overload
    def LocateWelds(searchEntireAssembly: bool, excludeInvisibleComponents: bool, wantSolids: bool, wantCurves: bool, wantPoints: bool) -> List[NXOpen.NXObject]:
        """
         Method to search all fully loaded parts for welding objects in an assembly or part file. An array of solids, curves and points can be output 
         Returns foundObjectsArray ( NXOpen.NXObject Li):  Array of objects passing the search criteria specified. .
        """
        pass
    @overload
    def LocateWelds(searchEntireAssembly: bool, excludeInvisibleComponents: bool, wantSolids: bool, wantCurves: bool, wantPoints: bool, wantStructureWelds: bool) -> List[NXOpen.NXObject]:
        """
         Method to search all fully loaded parts for welding objects in an assembly or part file. An array of solids, curves and points can be output. Structure welds can also be included in the search. 
         Returns foundObjectsArray ( NXOpen.NXObject Li):  Array of objects passing the search criteria specified. .
        """
        pass
    def RemoveDatumIconHandler(id: int) -> None:
        """
         Unregisters the datum common icon handler 
        """
        pass
    def RemoveJointPmiCreated(id: int) -> None:
        """
         Unregisters the user defined method that is called whenever a NXOpen.Annotations.PmiLineWeld is created 
        """
        pass
    def RemoveModifyFeatureHandler(id: int) -> None:
        """
         Unregisters the modify feature handler 
        """
        pass
    def RemovePipeJointSetType(id: int) -> None:
        """
         Unregisters the pipe joint set type handler 
        """
        pass
    def RemovePointExitHandler(id: int) -> None:
        """
         Unregisters the point feature handler 
        """
        pass
    def RemoveVariableBevelHandler(id: int) -> None:
        """
         Unregisters the variable bevel handler 
        """
        pass
    def RemoveWeldJointHandler(id: int) -> None:
        """
         Unregisters the welding joint handler 
        """
        pass
    def ShowSolids(showSolids: bool) -> None:
        """
         Method to change display mode of all Weld.PointMarkPoint feature that are fully loaded in an assembly 
        """
        pass
import NXOpen
import NXOpen.Assemblies
class DatumCommonBuilder(NXOpen.Builder): 
    """ Used to create or edit a NXOpen.Weld.DatumSurface  or NXOpen.Weld.DatumPin feature."""
    class ControlMethodTypes(Enum):
        """
        Members Include: 
         |PrincipalAxis|  A principal axis. Absolute X,Y, or Z 
         |UseSectionPlane|  Not a principal axis, use Section Plane 

        """
        PrincipalAxis: int
        UseSectionPlane: int
        @staticmethod
        def ValueOf(value: int) -> DatumCommonBuilder.ControlMethodTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CreationDirectionMethods(Enum):
        """
        Members Include: 
         |Default|  Use the default construction method 
         |Opposite|  Reverse the construction orientation 

        """
        Default: int
        Opposite: int
        @staticmethod
        def ValueOf(value: int) -> DatumCommonBuilder.CreationDirectionMethods:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CustomTypes(Enum):
        """
        Members Include: 
         |Default|  A datum surface or pin specified in the customer defaults by the Default type. 
         |Custom1|  A datum surface or pin specified in the customer defaults by the Custom1 type. 
         |Custom2|  A datum surface or pin specified in the customer defaults by the Custom2 type. 
         |Custom3|  A datum surface or pin specified in the customer defaults by the Custom3 type. 
         |Custom4|  A datum surface or pin specified in the customer defaults by the Custom4 type. 
         |Custom5|  A datum surface or pin specified in the customer defaults by the Custom5 type. 
         |Custom6|  A datum surface or pin specified in the customer defaults by the Custom6 type. 
         |Custom7|  A datum surface or pin specified in the customer defaults by the Custom7 type. 

        """
        Default: int
        Custom1: int
        Custom2: int
        Custom3: int
        Custom4: int
        Custom5: int
        Custom6: int
        Custom7: int
        @staticmethod
        def ValueOf(value: int) -> DatumCommonBuilder.CustomTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PlaneMethodTypes(Enum):
        """
        Members Include: 
         |InferPlanes|  Determine the best XC,YC, or ZC intersection plane. 
         |ParallelXCPlanes|  Datum is on the XC plane. 
         |ParallelYCPlanes|  Datum is on the YC plane. 
         |ParallelZCPlanes|  Datum is on the ZC plane. 
         |SelectPlanes|  Datum is on user selected planes. 
         |Unknown|  Used when plane method is unknown. Used with Connected Face Finder 

        """
        InferPlanes: int
        ParallelXCPlanes: int
        ParallelYCPlanes: int
        ParallelZCPlanes: int
        SelectPlanes: int
        Unknown: int
        @staticmethod
        def ValueOf(value: int) -> DatumCommonBuilder.PlaneMethodTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SizeMethodTypes(Enum):
        """
        Members Include: 
         |Automatic|  The hole or slot size was automatically computed. 
         |Manual|  User manually entered the hole or slot size. 

        """
        Automatic: int
        Manual: int
        @staticmethod
        def ValueOf(value: int) -> DatumCommonBuilder.SizeMethodTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SolidTypes(Enum):
        """
        Members Include: 
         |Sphere|  Datum solid will be a sphere   
         |Cylinder|  Datum solid will be a cylinder 
         |Cone|  Datum solid will be a cone     
         |Cuboid|  Datum solid will be a cuboid for Datum Surface only 
         |Hollow|  Datum solid will be a hollow cylinder for Datum Surface only 
         |Arrow|  Measure solid will be the default solid - an arrow shape 
         |NotSet|  No solid created for either Datum or Measure 
         |Hourglass|  Measure solid will be an hourglass (double cone) shape 

        """
        Sphere: int
        Cylinder: int
        Cone: int
        Cuboid: int
        Hollow: int
        Arrow: int
        NotSet: int
        Hourglass: int
        @staticmethod
        def ValueOf(value: int) -> DatumCommonBuilder.SolidTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AdditionalReferences(self) -> NXOpen.Assemblies.SelectComponentList:
        """
        Getter for property: ( NXOpen.Assemblies.SelectComponentList) AdditionalReferences
         Returns the additional references.  
            Use to define additional parts the datum connects.   
         
        """
        pass
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns the associative flag.  
           Indicates if resulting object should move if an input reference is moved.   
         
        """
        pass
    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
         Returns the associative flag.  
           Indicates if resulting object should move if an input reference is moved.   
         
        """
        pass
    @property
    def Characteristics(self) -> CharacteristicsBuilder:
        """
        Getter for property: ( CharacteristicsBuilder NXOpe) Characteristics
         Returns the characteristics.  
           Used to specify additional attributes.   
         
        """
        pass
    @property
    def ControlMethod(self) -> DatumCommonBuilder.ControlMethodTypes:
        """
        Getter for property: ( DatumCommonBuilder.ControlMethodTypes NXOpe) ControlMethod
         Returns the control method.  
           The method for fixing the datum orientation.   
         
        """
        pass
    @ControlMethod.setter
    def ControlMethod(self, controlMethod: DatumCommonBuilder.ControlMethodTypes):
        """
        Setter for property: ( DatumCommonBuilder.ControlMethodTypes NXOpe) ControlMethod
         Returns the control method.  
           The method for fixing the datum orientation.   
         
        """
        pass
    @property
    def CreateDirectionVector(self) -> bool:
        """
        Getter for property: (bool) CreateDirectionVector
         Returns the option to control if a reference datum axis should be output with this feature.  
             
         
        """
        pass
    @CreateDirectionVector.setter
    def CreateDirectionVector(self, createDirectionVector: bool):
        """
        Setter for property: (bool) CreateDirectionVector
         Returns the option to control if a reference datum axis should be output with this feature.  
             
         
        """
        pass
    @property
    def CreatePlane(self) -> bool:
        """
        Getter for property: (bool) CreatePlane
         Returns the option to control if a reference datum plane should be output with the this feature.  
             
         
        """
        pass
    @CreatePlane.setter
    def CreatePlane(self, createPlane: bool):
        """
        Setter for property: (bool) CreatePlane
         Returns the option to control if a reference datum plane should be output with the this feature.  
             
         
        """
        pass
    @property
    def CreatePoint(self) -> bool:
        """
        Getter for property: (bool) CreatePoint
         Returns the option to control if a reference point should be output with this feature.  
             
         
        """
        pass
    @CreatePoint.setter
    def CreatePoint(self, createPoint: bool):
        """
        Setter for property: (bool) CreatePoint
         Returns the option to control if a reference point should be output with this feature.  
             
         
        """
        pass
    @property
    def CreationDirection(self) -> DatumCommonBuilder.CreationDirectionMethods:
        """
        Getter for property: ( DatumCommonBuilder.CreationDirectionMethods NXOpe) CreationDirection
         Returns the creation direction.  
             
         
        """
        pass
    @CreationDirection.setter
    def CreationDirection(self, creationDirection: DatumCommonBuilder.CreationDirectionMethods):
        """
        Setter for property: ( DatumCommonBuilder.CreationDirectionMethods NXOpe) CreationDirection
         Returns the creation direction.  
             
         
        """
        pass
    @property
    def CustomAboveLength(self) -> float:
        """
        Getter for property: (float) CustomAboveLength
         Returns the length above the datum reference point.  
           This is used if a cylinder, cone, or cuboid (Surface locator only) are created.   
         
        """
        pass
    @CustomAboveLength.setter
    def CustomAboveLength(self, customAboveLength: float):
        """
        Setter for property: (float) CustomAboveLength
         Returns the length above the datum reference point.  
           This is used if a cylinder, cone, or cuboid (Surface locator only) are created.   
         
        """
        pass
    @property
    def CustomRadius(self) -> float:
        """
        Getter for property: (float) CustomRadius
         Returns the radius of the solid sphere, cylinder or cone created.  
               
         
        """
        pass
    @CustomRadius.setter
    def CustomRadius(self, customRadius: float):
        """
        Setter for property: (float) CustomRadius
         Returns the radius of the solid sphere, cylinder or cone created.  
               
         
        """
        pass
    @property
    def CustomTotalLength(self) -> float:
        """
        Getter for property: (float) CustomTotalLength
         Returns the total length of the cylinder, cone, or cuboid (Surface locator only) along the direction axis.  
             
         
        """
        pass
    @CustomTotalLength.setter
    def CustomTotalLength(self, customTotalLength: float):
        """
        Setter for property: (float) CustomTotalLength
         Returns the total length of the cylinder, cone, or cuboid (Surface locator only) along the direction axis.  
             
         
        """
        pass
    @property
    def CustomType(self) -> DatumCommonBuilder.CustomTypes:
        """
        Getter for property: ( DatumCommonBuilder.CustomTypes NXOpe) CustomType
         Returns the custom datum type.  
           This corresponds to an entry in the customer defaults.   
         
        """
        pass
    @CustomType.setter
    def CustomType(self, customType: DatumCommonBuilder.CustomTypes):
        """
        Setter for property: ( DatumCommonBuilder.CustomTypes NXOpe) CustomType
         Returns the custom datum type.  
           This corresponds to an entry in the customer defaults.   
         
        """
        pass
    @property
    def CustomTypeName(self) -> str:
        """
        Getter for property: (str) CustomTypeName
         Returns the custom name used to create the datum.  
              
         
        """
        pass
    @CustomTypeName.setter
    def CustomTypeName(self, customTypeName: str):
        """
        Setter for property: (str) CustomTypeName
         Returns the custom name used to create the datum.  
              
         
        """
        pass
    @property
    def Derived(self) -> bool:
        """
        Getter for property: (bool) Derived
         Returns the indicator if this should be marked as a derived from another datum.  
             
         
        """
        pass
    @Derived.setter
    def Derived(self, derived: bool):
        """
        Setter for property: (bool) Derived
         Returns the indicator if this should be marked as a derived from another datum.  
             
         
        """
        pass
    @property
    def DerivedParentID(self) -> str:
        """
        Getter for property: (str) DerivedParentID
         Returns the derived parent ID for a locator created from a reference locator   
            
         
        """
        pass
    @DerivedParentID.setter
    def DerivedParentID(self, parentDatumID: str):
        """
        Setter for property: (str) DerivedParentID
         Returns the derived parent ID for a locator created from a reference locator   
            
         
        """
        pass
    @property
    def DirectionAxis(self) -> NXOpen.Axis:
        """
        Getter for property: ( NXOpen.Axis) DirectionAxis
         Returns the direction axis.  
            This defines the datum origin and specified axis.   
         
        """
        pass
    @DirectionAxis.setter
    def DirectionAxis(self, directionAxis: NXOpen.Axis):
        """
        Setter for property: ( NXOpen.Axis) DirectionAxis
         Returns the direction axis.  
            This defines the datum origin and specified axis.   
         
        """
        pass
    @property
    def DirectionLength(self) -> float:
        """
        Getter for property: (float) DirectionLength
         Returns the length of the datum axis vector created.  
             
         
        """
        pass
    @DirectionLength.setter
    def DirectionLength(self, directionLength: float):
        """
        Setter for property: (float) DirectionLength
         Returns the length of the datum axis vector created.  
             
         
        """
        pass
    @property
    def HoleDiameter(self) -> float:
        """
        Getter for property: (float) HoleDiameter
         Returns the hole diameter.  
             
         
        """
        pass
    @HoleDiameter.setter
    def HoleDiameter(self, holeDiameter: float):
        """
        Setter for property: (float) HoleDiameter
         Returns the hole diameter.  
             
         
        """
        pass
    @property
    def ModelingTolerance(self) -> float:
        """
        Getter for property: (float) ModelingTolerance
         Returns the modeling distance tolerance.  
             
         
        """
        pass
    @ModelingTolerance.setter
    def ModelingTolerance(self, modelingTolerance: float):
        """
        Setter for property: (float) ModelingTolerance
         Returns the modeling distance tolerance.  
             
         
        """
        pass
    @property
    def PlaneHeight(self) -> float:
        """
        Getter for property: (float) PlaneHeight
         Returns the plane height along the direction axis.  
           Controls the boundary of a datum plane.   
         
        """
        pass
    @PlaneHeight.setter
    def PlaneHeight(self, planeHeight: float):
        """
        Setter for property: (float) PlaneHeight
         Returns the plane height along the direction axis.  
           Controls the boundary of a datum plane.   
         
        """
        pass
    @property
    def PlaneMethod(self) -> DatumCommonBuilder.PlaneMethodTypes:
        """
        Getter for property: ( DatumCommonBuilder.PlaneMethodTypes NXOpe) PlaneMethod
         Returns  the plane method for the datum edge location   
            
         
        """
        pass
    @PlaneMethod.setter
    def PlaneMethod(self, planeMethod: DatumCommonBuilder.PlaneMethodTypes):
        """
        Setter for property: ( DatumCommonBuilder.PlaneMethodTypes NXOpe) PlaneMethod
         Returns  the plane method for the datum edge location   
            
         
        """
        pass
    @property
    def PlaneWidth(self) -> float:
        """
        Getter for property: (float) PlaneWidth
         Returns the plane width perpendicular to the direction axis.  
           Controls the boundary of a datum plane.   
         
        """
        pass
    @PlaneWidth.setter
    def PlaneWidth(self, planeWidth: float):
        """
        Setter for property: (float) PlaneWidth
         Returns the plane width perpendicular to the direction axis.  
           Controls the boundary of a datum plane.   
         
        """
        pass
    @property
    def PrincipalAxisX(self) -> bool:
        """
        Getter for property: (bool) PrincipalAxisX
         Returns the principal axis x.  
           Used to specify datum is controlling the x axis.   
         
        """
        pass
    @PrincipalAxisX.setter
    def PrincipalAxisX(self, principalAxisX: bool):
        """
        Setter for property: (bool) PrincipalAxisX
         Returns the principal axis x.  
           Used to specify datum is controlling the x axis.   
         
        """
        pass
    @property
    def PrincipalAxisY(self) -> bool:
        """
        Getter for property: (bool) PrincipalAxisY
         Returns the principal axis y.  
           Used to specify the datum is controlling the y axis.   
         
        """
        pass
    @PrincipalAxisY.setter
    def PrincipalAxisY(self, principalAxisY: bool):
        """
        Setter for property: (bool) PrincipalAxisY
         Returns the principal axis y.  
           Used to specify the datum is controlling the y axis.   
         
        """
        pass
    @property
    def PrincipalAxisZ(self) -> bool:
        """
        Getter for property: (bool) PrincipalAxisZ
         Returns the principal axis z.  
           Used to specify the datum is controlling the z axis.   
         
        """
        pass
    @PrincipalAxisZ.setter
    def PrincipalAxisZ(self, principalAxisZ: bool):
        """
        Setter for property: (bool) PrincipalAxisZ
         Returns the principal axis z.  
           Used to specify the datum is controlling the z axis.   
         
        """
        pass
    @property
    def ProjectAlongDirection(self) -> bool:
        """
        Getter for property: (bool) ProjectAlongDirection
         Returns the project along direction.  
           Two coordinates can be specified and the third obtained from projection.   
         
        """
        pass
    @ProjectAlongDirection.setter
    def ProjectAlongDirection(self, projectAlongDirection: bool):
        """
        Setter for property: (bool) ProjectAlongDirection
         Returns the project along direction.  
           Two coordinates can be specified and the third obtained from projection.   
         
        """
        pass
    @property
    def RadiusExp(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RadiusExp
         Returns the radius expression used for Datum Pins.  
              
         
        """
        pass
    @property
    def RotationAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RotationAngle
         Returns the rotation angle of the cuboid solid around the normal axis.  
              
         
        """
        pass
    @property
    def SectionPlaneNormal(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) SectionPlaneNormal
         Returns the section plane normal.  
           This is sometimes referred to as the clamping plane.   
         
        """
        pass
    @SectionPlaneNormal.setter
    def SectionPlaneNormal(self, sectionPlaneNormal: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) SectionPlaneNormal
         Returns the section plane normal.  
           This is sometimes referred to as the clamping plane.   
         
        """
        pass
    @property
    def SizeMethodType(self) -> DatumCommonBuilder.SizeMethodTypes:
        """
        Getter for property: ( DatumCommonBuilder.SizeMethodTypes NXOpe) SizeMethodType
         Returns the method used in setting the hole or slot size.  
             
         
        """
        pass
    @SizeMethodType.setter
    def SizeMethodType(self, sizeMethodType: DatumCommonBuilder.SizeMethodTypes):
        """
        Setter for property: ( DatumCommonBuilder.SizeMethodTypes NXOpe) SizeMethodType
         Returns the method used in setting the hole or slot size.  
             
         
        """
        pass
    @property
    def SlotLength(self) -> float:
        """
        Getter for property: (float) SlotLength
         Returns the slot length.  
             
         
        """
        pass
    @SlotLength.setter
    def SlotLength(self, slotLength: float):
        """
        Setter for property: (float) SlotLength
         Returns the slot length.  
             
         
        """
        pass
    @property
    def SlotWidth(self) -> float:
        """
        Getter for property: (float) SlotWidth
         Returns the slot width.  
             
         
        """
        pass
    @SlotWidth.setter
    def SlotWidth(self, slotWidth: float):
        """
        Setter for property: (float) SlotWidth
         Returns the slot width.  
             
         
        """
        pass
    @property
    def SolidType(self) -> DatumCommonBuilder.SolidTypes:
        """
        Getter for property: ( DatumCommonBuilder.SolidTypes NXOpe) SolidType
         Returns the solid body type specified.  
             
         
        """
        pass
    @SolidType.setter
    def SolidType(self, solidType: DatumCommonBuilder.SolidTypes):
        """
        Setter for property: ( DatumCommonBuilder.SolidTypes NXOpe) SolidType
         Returns the solid body type specified.  
             
         
        """
        pass
    @property
    def UserPlane(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) UserPlane
         Returns  the datum edge intersection plane selected by the user   
            
         
        """
        pass
    @property
    def XTolerance(self) -> float:
        """
        Getter for property: (float) XTolerance
         Returns the Measure tolerance for X.  
               
         
        """
        pass
    @XTolerance.setter
    def XTolerance(self, xTolerance: float):
        """
        Setter for property: (float) XTolerance
         Returns the Measure tolerance for X.  
               
         
        """
        pass
    @property
    def YTolerance(self) -> float:
        """
        Getter for property: (float) YTolerance
         Returns the Measure tolerance for Y.  
               
         
        """
        pass
    @YTolerance.setter
    def YTolerance(self, xTolerance: float):
        """
        Setter for property: (float) YTolerance
         Returns the Measure tolerance for Y.  
               
         
        """
        pass
    @property
    def ZTolerance(self) -> float:
        """
        Getter for property: (float) ZTolerance
         Returns the Measure tolerance for Z.  
               
         
        """
        pass
    @ZTolerance.setter
    def ZTolerance(self, xTolerance: float):
        """
        Setter for property: (float) ZTolerance
         Returns the Measure tolerance for Z.  
               
         
        """
        pass
    def UpdateWithDerivedDatum(self) -> None:
        """
         Initialize the builder with the inputs from an existing datum. The builder type and derived datum type must be the same. 
        """
        pass
import NXOpen
class DatumEdgeBuilder(DatumCommonBuilder): 
    """ Used to create or edit a NXOpen.Weld.DatumEdge feature. """
    @property
    def BoundaryCurve(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BoundaryCurve
         Returns the edge curve   
            
         
        """
        pass
    @property
    def CustomCuboidLength(self) -> float:
        """
        Getter for property: (float) CustomCuboidLength
         Returns the length of the solid cuboid created.  
               
         
        """
        pass
    @CustomCuboidLength.setter
    def CustomCuboidLength(self, customCuboidLength: float):
        """
        Setter for property: (float) CustomCuboidLength
         Returns the length of the solid cuboid created.  
               
         
        """
        pass
    @property
    def CustomCuboidWidth(self) -> float:
        """
        Getter for property: (float) CustomCuboidWidth
         Returns the width of the solid cuboid created.  
               
         
        """
        pass
    @CustomCuboidWidth.setter
    def CustomCuboidWidth(self, customCuboidWidth: float):
        """
        Setter for property: (float) CustomCuboidWidth
         Returns the width of the solid cuboid created.  
               
         
        """
        pass
    @property
    def DerivedDatum(self) -> SelectDatumEdge:
        """
        Getter for property: ( SelectDatumEdge NXOpe) DerivedDatum
         Returns the derived datum   
            
         
        """
        pass
    @property
    def GridSnapTolerance(self) -> float:
        """
        Getter for property: (float) GridSnapTolerance
         Returns the grid snap tolerance   
            
         
        """
        pass
    @GridSnapTolerance.setter
    def GridSnapTolerance(self, gridSnapTolerance: float):
        """
        Setter for property: (float) GridSnapTolerance
         Returns the grid snap tolerance   
            
         
        """
        pass
    @property
    def RestingFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) RestingFace
         Returns the reference (resting) face   
            
         
        """
        pass
    @property
    def SnapPointToGrid(self) -> bool:
        """
        Getter for property: (bool) SnapPointToGrid
         Returns the snap point to grid option.  
           Specified locations will be adjusted based on the grid snap tolerance    
         
        """
        pass
    @SnapPointToGrid.setter
    def SnapPointToGrid(self, snapPointToGrid: bool):
        """
        Setter for property: (bool) SnapPointToGrid
         Returns the snap point to grid option.  
           Specified locations will be adjusted based on the grid snap tolerance    
         
        """
        pass
    @property
    def XCoordinate(self) -> float:
        """
        Getter for property: (float) XCoordinate
         Returns the x coordinate position for the edge datum location.  
             
         
        """
        pass
    @XCoordinate.setter
    def XCoordinate(self, xCoordinate: float):
        """
        Setter for property: (float) XCoordinate
         Returns the x coordinate position for the edge datum location.  
             
         
        """
        pass
    @property
    def YCoordinate(self) -> float:
        """
        Getter for property: (float) YCoordinate
         Returns the y coordinate position for the edge datum location   
            
         
        """
        pass
    @YCoordinate.setter
    def YCoordinate(self, yCoordinate: float):
        """
        Setter for property: (float) YCoordinate
         Returns the y coordinate position for the edge datum location   
            
         
        """
        pass
    @property
    def ZCoordinate(self) -> float:
        """
        Getter for property: (float) ZCoordinate
         Returns the z coordinate position for the datum edge location   
            
         
        """
        pass
    @ZCoordinate.setter
    def ZCoordinate(self, zCoordinate: float):
        """
        Setter for property: (float) ZCoordinate
         Returns the z coordinate position for the datum edge location   
            
         
        """
        pass
    def InitializeAxis(self, approximatePoint: NXOpen.Point3d) -> None:
        """
         Update the axis origin to a point specified, and direction to closest principal axis to the pick point. 
        """
        pass
    def MoveMinimumDistance(self) -> None:
        """
         Moves a point to the nearest location on the edge 
        """
        pass
    def UpdateAxisData(self) -> None:
        """
         Updates data related to the axis. The origin will be adjusted based on grid snapping and projection direction. In addition the control direction information will be updated.  
        """
        pass
import NXOpen.Features
class DatumEdge(NXOpen.Features.Feature): 
    """ Represents a Weld Datum Edge feature """
    pass
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
class DatumIconBuilder(NXOpen.TaggedObject): 
    """ Represents a NXOpen.Weld.DatumIconBuilder class used to control the part navigator icon for Datum Pin and Surface Locators. This class is used to set the Datum Surface or Datum Pin
        icon, but never both at the same time. If the icon is not being set for a feature, that feature will be set to .
        See example in DatumIconCallback.cxx in ugweldsamples kit. """
    @property
    def CustomType(self) -> DatumCommonBuilder.CustomTypes:
        """
        Getter for property: ( DatumCommonBuilder.CustomTypes NXOpe) CustomType
         Returns the custom datum type from the customer defaults that was used.  
             
         
        """
        pass
    @property
    def DatumPin(self) -> DatumPin:
        """
        Getter for property: ( DatumPin NXOpe) DatumPin
         Returns the DatumPin feature.  
           This will be NULL if setting the icon for a different feature.   
         
        """
        pass
    @property
    def DatumSurface(self) -> DatumSurface:
        """
        Getter for property: ( DatumSurface NXOpe) DatumSurface
         Returns the DatumSurface feature.  
           This will be NULL if setting the icon for a different feature.   
         
        """
        pass
    @property
    def Derived(self) -> bool:
        """
        Getter for property: (bool) Derived
         Returns the indicator if this datum was derived from another datum.  
             
         
        """
        pass
    @property
    def IconName(self) -> str:
        """
        Getter for property: (str) IconName
         Returns the bit map name for the icon to be used.  
           If the bit map cannot be found a default one will be used.   
         
        """
        pass
    @IconName.setter
    def IconName(self, iconName: str):
        """
        Setter for property: (str) IconName
         Returns the bit map name for the icon to be used.  
           If the bit map cannot be found a default one will be used.   
         
        """
        pass
    @property
    def MeasureHem(self) -> NXOpen.Features.Feature:
        """
        Getter for property: ( NXOpen.Features.Feature) MeasureHem
         Returns the Measure Hem feature.  
           This will be NULL if setting the icon for a different feature.   
         
        """
        pass
    @property
    def MeasureHole(self) -> NXOpen.Features.Feature:
        """
        Getter for property: ( NXOpen.Features.Feature) MeasureHole
         Returns the Measure Hole feature.  
           This will be NULL if setting the icon for a different feature.   
         
        """
        pass
    @property
    def MeasureSlot(self) -> NXOpen.Features.Feature:
        """
        Getter for property: ( NXOpen.Features.Feature) MeasureSlot
         Returns the Measure Slot feature.  
           This will be NULL if setting the icon for a different feature.   
         
        """
        pass
    @property
    def MeasureSurface(self) -> MeasureSurface:
        """
        Getter for property: ( MeasureSurface NXOpe) MeasureSurface
         Returns the Measure Surface feature.  
           This will be NULL if setting the icon for a different feature.   
         
        """
        pass
    @property
    def MeasureTrim(self) -> NXOpen.Features.Feature:
        """
        Getter for property: ( NXOpen.Features.Feature) MeasureTrim
         Returns the Measure Trim feature.  
           This will be NULL if setting the icon for a different feature.   
         
        """
        pass
import NXOpen
class DatumPinBuilder(DatumCommonBuilder): 
    """ Used to create or edit a NXOpen.Weld.DatumPin feature. """
    @property
    def BoundaryCurve(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BoundaryCurve
         Returns the boundary curves   
            
         
        """
        pass
    @property
    def CreatePunchVector(self) -> bool:
        """
        Getter for property: (bool) CreatePunchVector
         Returns the flag that indicates if a datum vector should be created for the punch direction.  
             
         
        """
        pass
    @CreatePunchVector.setter
    def CreatePunchVector(self, createPunchVector: bool):
        """
        Setter for property: (bool) CreatePunchVector
         Returns the flag that indicates if a datum vector should be created for the punch direction.  
             
         
        """
        pass
    @property
    def DerivedDatum(self) -> SelectDatumPin:
        """
        Getter for property: ( SelectDatumPin NXOpe) DerivedDatum
         Returns the derived datum   
            
         
        """
        pass
    @property
    def PunchDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) PunchDirection
         Returns the punch direction vector object.  
             
         
        """
        pass
    @PunchDirection.setter
    def PunchDirection(self, punchDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) PunchDirection
         Returns the punch direction vector object.  
             
         
        """
        pass
    @property
    def PunchDirectionLength(self) -> float:
        """
        Getter for property: (float) PunchDirectionLength
         Returns the length of the punch direction vector created.  
             
         
        """
        pass
    @PunchDirectionLength.setter
    def PunchDirectionLength(self, punchDirectionLength: float):
        """
        Setter for property: (float) PunchDirectionLength
         Returns the length of the punch direction vector created.  
             
         
        """
        pass
    def InitializeAxis(self) -> None:
        """
         Update the axis origin to the center of the slot or circle, and direction to the normal of the boundary.  If the boundary is not planar an approximate direction will be computed from boundary bounding box. 
        """
        pass
    def MoveToCenter(self) -> None:
        """
         Moves a point to the center of a circle or slot boundary 
        """
        pass
    def UpdateAxisData(self) -> None:
        """
         Updates data related to the axis. The origin will be adjusted based on grid snapping, and projection direction.   In addition the control direction information will be updated.  
        """
        pass
import NXOpen.Features
class DatumPin(NXOpen.Features.Feature): 
    """ Represents a Weld Datum Pin feature """
    pass
import NXOpen
class DatumSurfaceBuilder(DatumCommonBuilder): 
    """ Used to create or edit a NXOpen.Weld.DatumSurface feature. """
    class Types(Enum):
        """
        Members Include: 
         |Direct|  direct location 
         |Mirror|  mirror location 

        """
        Direct: int
        Mirror: int
        @staticmethod
        def ValueOf(value: int) -> DatumSurfaceBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BoundaryCurve(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BoundaryCurve
         Returns the boundary curves   
            
         
        """
        pass
    @property
    def CustomCuboidLength(self) -> float:
        """
        Getter for property: (float) CustomCuboidLength
         Returns the length of the solid cuboid created.  
               
         
        """
        pass
    @CustomCuboidLength.setter
    def CustomCuboidLength(self, customCuboidLength: float):
        """
        Setter for property: (float) CustomCuboidLength
         Returns the length of the solid cuboid created.  
               
         
        """
        pass
    @property
    def CustomCuboidWidth(self) -> float:
        """
        Getter for property: (float) CustomCuboidWidth
         Returns the width of the solid cuboid created.  
               
         
        """
        pass
    @CustomCuboidWidth.setter
    def CustomCuboidWidth(self, customCuboidWidth: float):
        """
        Setter for property: (float) CustomCuboidWidth
         Returns the width of the solid cuboid created.  
               
         
        """
        pass
    @property
    def CustomHollowLength(self) -> float:
        """
        Getter for property: (float) CustomHollowLength
         Returns the inner length of the racetrack (extended hollow cylinder) solid created.  
               
         
        """
        pass
    @CustomHollowLength.setter
    def CustomHollowLength(self, customHollowLength: float):
        """
        Setter for property: (float) CustomHollowLength
         Returns the inner length of the racetrack (extended hollow cylinder) solid created.  
               
         
        """
        pass
    @property
    def CustomHollowRadius(self) -> float:
        """
        Getter for property: (float) CustomHollowRadius
         Returns the inner radius of the hollow cylinder solid created.  
               
         
        """
        pass
    @CustomHollowRadius.setter
    def CustomHollowRadius(self, customHollowRadius: float):
        """
        Setter for property: (float) CustomHollowRadius
         Returns the inner radius of the hollow cylinder solid created.  
               
         
        """
        pass
    @property
    def DerivedDatum(self) -> SelectDatumSurface:
        """
        Getter for property: ( SelectDatumSurface NXOpe) DerivedDatum
         Returns the derived datum   
            
         
        """
        pass
    @property
    def GridSnapTolerance(self) -> float:
        """
        Getter for property: (float) GridSnapTolerance
         Returns the grid snap tolerance   
            
         
        """
        pass
    @GridSnapTolerance.setter
    def GridSnapTolerance(self, gridSnapTolerance: float):
        """
        Setter for property: (float) GridSnapTolerance
         Returns the grid snap tolerance   
            
         
        """
        pass
    @property
    def MirrorPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) MirrorPlane
         Returns the plane used for mirroring a reference surface locator.  
             
         
        """
        pass
    @MirrorPlane.setter
    def MirrorPlane(self, mirrorPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) MirrorPlane
         Returns the plane used for mirroring a reference surface locator.  
             
         
        """
        pass
    @property
    def RestingFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) RestingFace
         Returns the resting face   
            
         
        """
        pass
    @property
    def SnapPointToGrid(self) -> bool:
        """
        Getter for property: (bool) SnapPointToGrid
         Returns the snap point to grid option.  
           Specified locations will be adjusted based on the grid snap tolerance    
         
        """
        pass
    @SnapPointToGrid.setter
    def SnapPointToGrid(self, snapPointToGrid: bool):
        """
        Setter for property: (bool) SnapPointToGrid
         Returns the snap point to grid option.  
           Specified locations will be adjusted based on the grid snap tolerance    
         
        """
        pass
    @property
    def Type(self) -> DatumSurfaceBuilder.Types:
        """
        Getter for property: ( DatumSurfaceBuilder.Types NXOpe) Type
         Returns the construction type used to create the datum surface.  
             
         
        """
        pass
    @Type.setter
    def Type(self, type: DatumSurfaceBuilder.Types):
        """
        Setter for property: ( DatumSurfaceBuilder.Types NXOpe) Type
         Returns the construction type used to create the datum surface.  
             
         
        """
        pass
    @property
    def XCoordinate(self) -> float:
        """
        Getter for property: (float) XCoordinate
         Returns the x coordinate position for the surface datum location.  
             
         
        """
        pass
    @XCoordinate.setter
    def XCoordinate(self, xCoordinate: float):
        """
        Setter for property: (float) XCoordinate
         Returns the x coordinate position for the surface datum location.  
             
         
        """
        pass
    @property
    def YCoordinate(self) -> float:
        """
        Getter for property: (float) YCoordinate
         Returns the y coordinate position for the surface datum location   
            
         
        """
        pass
    @YCoordinate.setter
    def YCoordinate(self, yCoordinate: float):
        """
        Setter for property: (float) YCoordinate
         Returns the y coordinate position for the surface datum location   
            
         
        """
        pass
    @property
    def ZCoordinate(self) -> float:
        """
        Getter for property: (float) ZCoordinate
         Returns the z coordinate position for the datum surface location   
            
         
        """
        pass
    @ZCoordinate.setter
    def ZCoordinate(self, zCoordinate: float):
        """
        Setter for property: (float) ZCoordinate
         Returns the z coordinate position for the datum surface location   
            
         
        """
        pass
    def InitializeAxis(self, approximatePoint: NXOpen.Point3d) -> None:
        """
         Update the axis origin to a point specified, and direction to closest principal axis to face normal.  The point will be adjusted by snapping to a grid. 
        """
        pass
    def MoveMinimumDistance(self) -> None:
        """
         Moves a point to the nearest location on the resting face 
        """
        pass
    def UpdateAxisData(self) -> None:
        """
         Updates data related to the axis. The origin will be adjusted based on grid snapping, and projection direction.   In addition the control direction information will be updated.  
        """
        pass
    def UpdateWithReferenceDatum(self) -> None:
        """
         Initialize the builder with the inputs from an existing datum surface locator. 
        """
        pass
import NXOpen.Features
class DatumSurface(NXOpen.Features.Feature): 
    """ Represents a Weld Datum Surface feature """
    pass
import NXOpen
class EasyPatternBuilder(NXOpen.Builder): 
    """ Represents the easy pattern builder. This is used to create hem, trim and surface measurement
        points at various plane locations. """
    class HemMethodTypes(Enum):
        """
        Members Include: 
         |MidPoint|  Use the mid point of a section cut. 
         |NormalToBody|  Use Normal to Body Method. 

        """
        MidPoint: int
        NormalToBody: int
        @staticmethod
        def ValueOf(value: int) -> EasyPatternBuilder.HemMethodTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PlaneMethodTypes(Enum):
        """
        Members Include: 
         |InferPlanes|  Determine the best XC,YC, or ZC plane. 
         |ParallelXCPlanes|  Patterns are on the XC plane. 
         |ParallelYCPlanes|  Patterns are on the YC plane. 
         |ParallelZCPlanes|  Patterns are on the ZC plane. 
         |SelectPlanes|  Patterns are on user selected planes. 

        """
        InferPlanes: int
        ParallelXCPlanes: int
        ParallelYCPlanes: int
        ParallelZCPlanes: int
        SelectPlanes: int
        @staticmethod
        def ValueOf(value: int) -> EasyPatternBuilder.PlaneMethodTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SpacingMethodTypes(Enum):
        """
        Members Include: 
         |Grid|  Use Grid spacing to cut sections. 
         |SinglePlane|  Use a single plane to cut a sections. 

        """
        Grid: int
        SinglePlane: int
        @staticmethod
        def ValueOf(value: int) -> EasyPatternBuilder.SpacingMethodTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SurfaceVectorCount(Enum):
        """
        Members Include: 
         |One|  Create one surface vector. 
         |Two|  Creates two surface vectors. 

        """
        One: int
        Two: int
        @staticmethod
        def ValueOf(value: int) -> EasyPatternBuilder.SurfaceVectorCount:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |TrimAndSurface|  Trim vector and surface vectors. 
         |HemAndSurface|  Hem vector and surface vectors.  
         |Surface|  Surface vector. 
         |Trim|  Trim vector. 
         |Hem|  Hem vector.  
         |SurfacePoints|  Surface vectors from existing points 

        """
        TrimAndSurface: int
        HemAndSurface: int
        Surface: int
        Trim: int
        Hem: int
        SurfacePoints: int
        @staticmethod
        def ValueOf(value: int) -> EasyPatternBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BackEdgeOffset(self) -> float:
        """
        Getter for property: (float) BackEdgeOffset
         Returns the back edge offset.  
           This offset distance is measured from the end of the section cut curve. The start of the curve is at path curve specified.    
         
        """
        pass
    @BackEdgeOffset.setter
    def BackEdgeOffset(self, backEdgeOffset: float):
        """
        Setter for property: (float) BackEdgeOffset
         Returns the back edge offset.  
           This offset distance is measured from the end of the section cut curve. The start of the curve is at path curve specified.    
         
        """
        pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance.  
             
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, tolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance.  
             
         
        """
        pass
    @property
    def GridAngleTolerance(self) -> float:
        """
        Getter for property: (float) GridAngleTolerance
         Returns the grid angle tolerance.  
           This is used for the inferred grid spacing method.    
         
        """
        pass
    @GridAngleTolerance.setter
    def GridAngleTolerance(self, gridAngleTolerance: float):
        """
        Setter for property: (float) GridAngleTolerance
         Returns the grid angle tolerance.  
           This is used for the inferred grid spacing method.    
         
        """
        pass
    @property
    def GridIncrement(self) -> float:
        """
        Getter for property: (float) GridIncrement
         Returns the grid increment.  
           The grid spacing value use to generate planes.   
         
        """
        pass
    @GridIncrement.setter
    def GridIncrement(self, gridIncrement: float):
        """
        Setter for property: (float) GridIncrement
         Returns the grid increment.  
           The grid spacing value use to generate planes.   
         
        """
        pass
    @property
    def Height(self) -> float:
        """
        Getter for property: (float) Height
         Returns the height of the measurement solid to create.  
             
         
        """
        pass
    @Height.setter
    def Height(self, height: float):
        """
        Setter for property: (float) Height
         Returns the height of the measurement solid to create.  
             
         
        """
        pass
    @property
    def HemMethod(self) -> EasyPatternBuilder.HemMethodTypes:
        """
        Getter for property: ( EasyPatternBuilder.HemMethodTypes NXOpe) HemMethod
         Returns the hem method.  
           This controls the method used for determining the hem point location and vector direction.   
         
        """
        pass
    @HemMethod.setter
    def HemMethod(self, hemMethod: EasyPatternBuilder.HemMethodTypes):
        """
        Setter for property: ( EasyPatternBuilder.HemMethodTypes NXOpe) HemMethod
         Returns the hem method.  
           This controls the method used for determining the hem point location and vector direction.   
         
        """
        pass
    @property
    def LengthAndWidth(self) -> float:
        """
        Getter for property: (float) LengthAndWidth
         Returns the length and width of the measurement solid to create.  
             
         
        """
        pass
    @LengthAndWidth.setter
    def LengthAndWidth(self, lengthAndWidth: float):
        """
        Setter for property: (float) LengthAndWidth
         Returns the length and width of the measurement solid to create.  
             
         
        """
        pass
    @property
    def MaximumSpacing(self) -> float:
        """
        Getter for property: (float) MaximumSpacing
         Returns the maximum spacing between the trim edge offset and the back edge offset.  
             
         
        """
        pass
    @MaximumSpacing.setter
    def MaximumSpacing(self, maximumSpacing: float):
        """
        Setter for property: (float) MaximumSpacing
         Returns the maximum spacing between the trim edge offset and the back edge offset.  
             
         
        """
        pass
    @property
    def MinimumFlangeWidth(self) -> float:
        """
        Getter for property: (float) MinimumFlangeWidth
         Returns the value used to control when only one surface measurement vector will be created.  
              
         
        """
        pass
    @MinimumFlangeWidth.setter
    def MinimumFlangeWidth(self, minimumFlangeWidth: float):
        """
        Setter for property: (float) MinimumFlangeWidth
         Returns the value used to control when only one surface measurement vector will be created.  
              
         
        """
        pass
    @property
    def NumberSurfaceVectors(self) -> int:
        """
        Getter for property: (int) NumberSurfaceVectors
         Returns the number surface vectors to create for each pattern.  
             
         
        """
        pass
    @NumberSurfaceVectors.setter
    def NumberSurfaceVectors(self, numberSurfaceVectors: int):
        """
        Setter for property: (int) NumberSurfaceVectors
         Returns the number surface vectors to create for each pattern.  
             
         
        """
        pass
    @property
    def OtherCharacteristics(self) -> CharacteristicsBuilder:
        """
        Getter for property: ( CharacteristicsBuilder NXOpe) OtherCharacteristics
         Returns the trim or hem characteristics.  
           Used to specify additional attributes.   
         
        """
        pass
    @property
    def PatternPath(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) PatternPath
         Returns the pattern path.  
           This path is used to determine the pattern spacing.   
         
        """
        pass
    @property
    def PatternSelPoints(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) PatternSelPoints
         Returns the selected points for the pattern   
            
         
        """
        pass
    @property
    def PlaneLocation(self) -> float:
        """
        Getter for property: (float) PlaneLocation
         Returns the plane location.  
           The single plane location to create a pattern.   
         
        """
        pass
    @PlaneLocation.setter
    def PlaneLocation(self, planeLocation: float):
        """
        Setter for property: (float) PlaneLocation
         Returns the plane location.  
           The single plane location to create a pattern.   
         
        """
        pass
    @property
    def PlaneMethod(self) -> EasyPatternBuilder.PlaneMethodTypes:
        """
        Getter for property: ( EasyPatternBuilder.PlaneMethodTypes NXOpe) PlaneMethod
         Returns the plane method.  
           This is used to control plane orientations for the measurement points.   
         
        """
        pass
    @PlaneMethod.setter
    def PlaneMethod(self, planeMethod: EasyPatternBuilder.PlaneMethodTypes):
        """
        Setter for property: ( EasyPatternBuilder.PlaneMethodTypes NXOpe) PlaneMethod
         Returns the plane method.  
           This is used to control plane orientations for the measurement points.   
         
        """
        pass
    @property
    def PrimaryCharacteristics(self) -> CharacteristicsBuilder:
        """
        Getter for property: ( CharacteristicsBuilder NXOpe) PrimaryCharacteristics
         Returns the surface characteristics.  
           Used to specify additional attributes.   
         
        """
        pass
    @property
    def ProjectAlongDirection(self) -> bool:
        """
        Getter for property: (bool) ProjectAlongDirection
         Returns the project along direction flag.  
           This will project any off-surface points to the surface based on the direction toggle.   
         
        """
        pass
    @ProjectAlongDirection.setter
    def ProjectAlongDirection(self, projectToSurface: bool):
        """
        Setter for property: (bool) ProjectAlongDirection
         Returns the project along direction flag.  
           This will project any off-surface points to the surface based on the direction toggle.   
         
        """
        pass
    @property
    def ReverseDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseDirection
         Returns the reverse direction.  
           This will reverse direction of all measurement points created.   
         
        """
        pass
    @ReverseDirection.setter
    def ReverseDirection(self, reverseDirection: bool):
        """
        Setter for property: (bool) ReverseDirection
         Returns the reverse direction.  
           This will reverse direction of all measurement points created.   
         
        """
        pass
    @property
    def SpacingMethod(self) -> EasyPatternBuilder.SpacingMethodTypes:
        """
        Getter for property: ( EasyPatternBuilder.SpacingMethodTypes NXOpe) SpacingMethod
         Returns the spacing method.  
           This method controls whether multiple patterns are created or a single pattern.   
         
        """
        pass
    @SpacingMethod.setter
    def SpacingMethod(self, spacingMethod: EasyPatternBuilder.SpacingMethodTypes):
        """
        Setter for property: ( EasyPatternBuilder.SpacingMethodTypes NXOpe) SpacingMethod
         Returns the spacing method.  
           This method controls whether multiple patterns are created or a single pattern.   
         
        """
        pass
    @property
    def SurfaceVectorFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SurfaceVectorFace
         Returns the surface vector face.  
           This is the face surface vectors will be created on.   
         
        """
        pass
    @property
    def TrimEdgeOffset(self) -> float:
        """
        Getter for property: (float) TrimEdgeOffset
         Returns the trim edge offset distance.  
           This is the offset distance from the path specified.   
         
        """
        pass
    @TrimEdgeOffset.setter
    def TrimEdgeOffset(self, trimEdgeOffset: float):
        """
        Setter for property: (float) TrimEdgeOffset
         Returns the trim edge offset distance.  
           This is the offset distance from the path specified.   
         
        """
        pass
    @property
    def Type(self) -> EasyPatternBuilder.Types:
        """
        Getter for property: ( EasyPatternBuilder.Types NXOpe) Type
         Returns the type of pattern to created.  
             
         
        """
        pass
    @Type.setter
    def Type(self, type: EasyPatternBuilder.Types):
        """
        Setter for property: ( EasyPatternBuilder.Types NXOpe) Type
         Returns the type of pattern to created.  
             
         
        """
        pass
    @property
    def UserPlanes(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) UserPlanes
         Returns the selected planes for the pattern   
            
         
        """
        pass
import NXOpen
class EdgePrepBuilder(NXOpen.Builder): 
    """ A builder used to create or edit a NXOpen.Weld.EdgePrep feature. """
    @property
    def ErrorCode(self) -> int:
        """
        Getter for property: (int) ErrorCode
         Returns the error code for the first welding joint curve that could not be processed.  
             
         
        """
        pass
    @property
    def WeldObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) WeldObjects
         Returns the welding joints to drive edge preparation   
            
         
        """
        pass
    def GetNoResultsInfo(self) -> List[NXOpen.Curve]:
        """
         Returns the curves that weld preparation was attempted on, but could not be performed. 
         Returns curves ( NXOpen.Curve Li):  The welding joint curves that weld preparation failed on. .
        """
        pass
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
class EdgePrepValuesBuilder(NXOpen.Builder): 
    """ Used to view or edit the values used to define the welding joint and edge preparation. """
    class Apply(Enum):
        """
        Members Include: 
         |ToAllValues|  Update all values of each selected joint. 
         |ToChangedValuesOnly|  Update only the changed values to each selected joint. 

        """
        ToAllValues: int
        ToChangedValuesOnly: int
        @staticmethod
        def ValueOf(value: int) -> EdgePrepValuesBuilder.Apply:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Option(Enum):
        """
        Members Include: 
         |Entered|  Use the values entered as edge prep values. 
         |Computed|  Use the computed values as edge prep values. 

        """
        Entered: int
        Computed: int
        @staticmethod
        def ValueOf(value: int) -> EdgePrepValuesBuilder.Option:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EdgesPrepared(self) -> bool:
        """
        Getter for property: (bool) EdgesPrepared
         Returns the indication that the edges are prepared for welding   
            
         
        """
        pass
    @EdgesPrepared.setter
    def EdgesPrepared(self, prepared: bool):
        """
        Setter for property: (bool) EdgesPrepared
         Returns the indication that the edges are prepared for welding   
            
         
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
         Returns the welding joint curves.  
             
         
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
    def ValueSegment(self) -> NXOpen.SelectCurve:
        """
        Getter for property: ( NXOpen.SelectCurve) ValueSegment
         Returns the selected segment.  
             
         
        """
        pass
    @property
    def ValuesApplyOption(self) -> EdgePrepValuesBuilder.Apply:
        """
        Getter for property: ( EdgePrepValuesBuilder.Apply NXOpe) ValuesApplyOption
         Returns the apply values option which indicates whether the all the values of each selected joint should be updated or just the values that were changed in the  NXOpen::Weld::JointExitBuilder .  
             
         
        """
        pass
    @ValuesApplyOption.setter
    def ValuesApplyOption(self, option: EdgePrepValuesBuilder.Apply):
        """
        Setter for property: ( EdgePrepValuesBuilder.Apply NXOpe) ValuesApplyOption
         Returns the apply values option which indicates whether the all the values of each selected joint should be updated or just the values that were changed in the  NXOpen::Weld::JointExitBuilder .  
             
         
        """
        pass
    @property
    def ValuesOption(self) -> EdgePrepValuesBuilder.Option:
        """
        Getter for property: ( EdgePrepValuesBuilder.Option NXOpe) ValuesOption
         Returns the values option which indicates whether the entered or computed values should be used.  
             
         
        """
        pass
    @ValuesOption.setter
    def ValuesOption(self, option: EdgePrepValuesBuilder.Option):
        """
        Setter for property: ( EdgePrepValuesBuilder.Option NXOpe) ValuesOption
         Returns the values option which indicates whether the entered or computed values should be used.  
             
         
        """
        pass
    def CreatePathCurvesForLeaveLoose(self) -> Tuple[NXOpen.Curve, NXOpen.Curve]:
        """
         Creates the path curves to be used for NXOpen.Weld.EdgePrepValuesBuilder.LeaveLooseStartValue and NXOpen.Weld.EdgePrepValuesBuilder.LeaveLooseEndValue. 
         Returns A tuple consisting of (path, reversedPath). 
         - path is:  NXOpen.Curve. Path curve for NXOpen.Weld.EdgePrepValuesBuilder.LeaveLooseStartValue. .
         - reversedPath is:  NXOpen.Curve. Reversed Path Curve for NXOpen.Weld.EdgePrepValuesBuilder.LeaveLooseEndValue. .

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
    def ReadEdgePrepValues(self, feature: NXOpen.Features.Feature) -> None:
        """
         Reads the edge prep values from the feature. 
        """
        pass
    def ReadEdgePrepValuesFromCurve(self, curve: NXOpen.Curve) -> None:
        """
         Reads the edge prep values from joint curve. 
        """
        pass
    def RecreateCurves(self) -> None:
        """
         Recreates the curves after changes to edge prep values. 
        """
        pass
import NXOpen.Features
class EdgePrep(NXOpen.Features.BodyFeature): 
    """ Represents a Weld Edge Prep feature """
    pass
import NXOpen
class ExportDpvBuilder(NXOpen.Builder): 
    """ Represents a ExportDpvBuilder class """
    @property
    def DpvFileName(self) -> str:
        """
        Getter for property: (str) DpvFileName
         Returns the DPV file name   
            
         
        """
        pass
    @DpvFileName.setter
    def DpvFileName(self, dpvFileName: str):
        """
        Setter for property: (str) DpvFileName
         Returns the DPV file name   
            
         
        """
        pass
    @property
    def WeldPoints(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) WeldPoints
         Returns the weld points to be exported to DPV file   
            
         
        """
        pass
import NXOpen
class ExportWeldBuilder(NXOpen.Builder): 
    """ Represents a ExportWeldBuilder class """
    class AttributeOriginType(Enum):
        """
        Members Include: 
         |Object| 
         |Df| 

        """
        Object: int
        Df: int
        @staticmethod
        def ValueOf(value: int) -> ExportWeldBuilder.AttributeOriginType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OutputType(Enum):
        """
        Members Include: 
         |IntermediateFile| 
         |InformationWindow| 

        """
        IntermediateFile: int
        InformationWindow: int
        @staticmethod
        def ValueOf(value: int) -> ExportWeldBuilder.OutputType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AttributeOrigin(self) -> ExportWeldBuilder.AttributeOriginType:
        """
        Getter for property: ( ExportWeldBuilder.AttributeOriginType NXOpe) AttributeOrigin
         Returns the option indicating where the attributes are read from, welding object or corresponding Design Feature.  
            
         
        """
        pass
    @AttributeOrigin.setter
    def AttributeOrigin(self, attributeOrigin: ExportWeldBuilder.AttributeOriginType):
        """
        Setter for property: ( ExportWeldBuilder.AttributeOriginType NXOpe) AttributeOrigin
         Returns the option indicating where the attributes are read from, welding object or corresponding Design Feature.  
            
         
        """
        pass
    @property
    def ConnectedPartAttrToggle(self) -> bool:
        """
        Getter for property: (bool) ConnectedPartAttrToggle
         Returns the connected part attribute toggle to control if read connected part attributes from weld points   
            
         
        """
        pass
    @ConnectedPartAttrToggle.setter
    def ConnectedPartAttrToggle(self, connectedPartAttrToggle: bool):
        """
        Setter for property: (bool) ConnectedPartAttrToggle
         Returns the connected part attribute toggle to control if read connected part attributes from weld points   
            
         
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
    def Output(self) -> ExportWeldBuilder.OutputType:
        """
        Getter for property: ( ExportWeldBuilder.OutputType NXOpe) Output
         Returns the option defining where to write the output data.  
           Data will be written to either a comma separated value file or the output window.   
         
        """
        pass
    @Output.setter
    def Output(self, outputType: ExportWeldBuilder.OutputType):
        """
        Setter for property: ( ExportWeldBuilder.OutputType NXOpe) Output
         Returns the option defining where to write the output data.  
           Data will be written to either a comma separated value file or the output window.   
         
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
    def WeldPoints(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) WeldPoints
         Returns the weld points to be exported to CSV file   
            
         
        """
        pass
    def GetConnectedPartAttributes(self) -> List[str]:
        """
         Get the connected part attributes of weld points 
         Returns connectedPartAttributes (List[str]):  Connected part attributes string .
        """
        pass
    def GetExportedAttributes(self) -> List[str]:
        """
         Get the attributes of weld points to be exported to CSV file 
         Returns exportedAttributes (List[str]):  Exported attributes string .
        """
        pass
    def OpenFromFile(self) -> None:
        """
         Open a template file to update exported attributes. Before use it, you must set template file name. 
        """
        pass
    def ReadAttributesFromWelds(self) -> None:
        """
         Read attributes from selected welds and save to exported attributes and connected part attributes 
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
         Set the connected part attributes of weld points 
        """
        pass
    def SetExportedAttributes(self, exportedAttributes: List[str]) -> None:
        """
         Set the attributes of weld points to be exported to CSV file 
        """
        pass
import NXOpen
class ExportWeldJointBuilder(ExportWeldBuilder): 
    """ Represents exporting weld joints. """
    class OutputFaceInfoTypes(Enum):
        """
        Members Include: 
         |NotSet|  No face normals output 
         |ForFilletsOnly|  Will output face normals at each point along the joint curve if leg lengths are defined. Will also output a separate record if leg lengths are defined for the opposite side 
         |All|  Will output face normals at each point along the joint curve. Will also output a separate record for the opposite side 

        """
        NotSet: int
        ForFilletsOnly: int
        All: int
        @staticmethod
        def ValueOf(value: int) -> ExportWeldJointBuilder.OutputFaceInfoTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ChordalTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ChordalTolerance
         Returns the minimum chordal length used to create a discrete version of the weld path, points along it will be output into 
                    xml file to represent the weld path   
            
         
        """
        pass
    @property
    def IncludeAttributesFromMAG(self) -> bool:
        """
        Getter for property: (bool) IncludeAttributesFromMAG
         Returns the indication to include attributes from the managed attribute associated to a design feature, if present.  
             
         
        """
        pass
    @IncludeAttributesFromMAG.setter
    def IncludeAttributesFromMAG(self, status: bool):
        """
        Setter for property: (bool) IncludeAttributesFromMAG
         Returns the indication to include attributes from the managed attribute associated to a design feature, if present.  
             
         
        """
        pass
    @property
    def OutputFaceInfo(self) -> ExportWeldJointBuilder.OutputFaceInfoTypes:
        """
        Getter for property: ( ExportWeldJointBuilder.OutputFaceInfoTypes NXOpe) OutputFaceInfo
         Returns the indication to output face normals at each point of the welding joint and opposite side   
            
         
        """
        pass
    @OutputFaceInfo.setter
    def OutputFaceInfo(self, outputType: ExportWeldJointBuilder.OutputFaceInfoTypes):
        """
        Setter for property: ( ExportWeldJointBuilder.OutputFaceInfoTypes NXOpe) OutputFaceInfo
         Returns the indication to output face normals at each point of the welding joint and opposite side   
            
         
        """
        pass
    @property
    def OutputFilletFaceInfo(self) -> bool:
        """
        Getter for property: (bool) OutputFilletFaceInfo
         Returns the indication to output face normals at each point if leg lengths are defined.  
           Will also output a separate record if leg lengths are defined for the opposite side   
         
        """
        pass
    @OutputFilletFaceInfo.setter
    def OutputFilletFaceInfo(self, status: bool):
        """
        Setter for property: (bool) OutputFilletFaceInfo
         Returns the indication to output face normals at each point if leg lengths are defined.  
           Will also output a separate record if leg lengths are defined for the opposite side   
         
        """
        pass
    @property
    def ProjectToTarget(self) -> bool:
        """
        Getter for property: (bool) ProjectToTarget
         Returns the indication to project opposite side points onto target faces if the point is not located on the target face.  
             
         
        """
        pass
    @ProjectToTarget.setter
    def ProjectToTarget(self, projectStatus: bool):
        """
        Setter for property: (bool) ProjectToTarget
         Returns the indication to project opposite side points onto target faces if the point is not located on the target face.  
             
         
        """
        pass
    @property
    def WorkCoordinateSystem(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) WorkCoordinateSystem
         Returns the local coordinate system used to calculate the output points on welding joint.  
           
                    If no coordinate system is provided, the points will be calculated in terms of the global coordinate system.   
         
        """
        pass
    @WorkCoordinateSystem.setter
    def WorkCoordinateSystem(self, coordSystem: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) WorkCoordinateSystem
         Returns the local coordinate system used to calculate the output points on welding joint.  
           
                    If no coordinate system is provided, the points will be calculated in terms of the global coordinate system.   
         
        """
        pass
import NXOpen.Features
class Extract(NXOpen.Features.Feature): 
    """ Represents a Linked Feature created in the Weld Assistant. """
    def CompressFace(self) -> None:
        """
         Compresses the size of weld linked face objects. This will reduce file size when the
              object is stored. On edit these faces will be automatically recreated. 
        """
        pass
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
class FilletBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a NXOpen.Weld.Fillet builder. """
    class EnumConstructionMethod(Enum):
        """
        Members Include: 
         |Default| 
         |RollAround| 

        """
        Default: int
        RollAround: int
        @staticmethod
        def ValueOf(value: int) -> FilletBuilder.EnumConstructionMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EnumContour(Enum):
        """
        Members Include: 
         |NotSet| 
         |Convex| 
         |Flush| 
         |Concave| 

        """
        NotSet: int
        Convex: int
        Flush: int
        Concave: int
        @staticmethod
        def ValueOf(value: int) -> FilletBuilder.EnumContour:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EnumExtendEdges(Enum):
        """
        Members Include: 
         |Manual| 
         |Automatic| 

        """
        Manual: int
        Automatic: int
        @staticmethod
        def ValueOf(value: int) -> FilletBuilder.EnumExtendEdges:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EnumExtensionMethod(Enum):
        """
        Members Include: 
         |Automatic| 
         |ByValue| 

        """
        Automatic: int
        ByValue: int
        @staticmethod
        def ValueOf(value: int) -> FilletBuilder.EnumExtensionMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EnumFillFaceHolesType(Enum):
        """
        Members Include: 
         |NotSet| 
         |Set1| 
         |Set2| 
         |Both| 

        """
        NotSet: int
        Set1: int
        Set2: int
        Both: int
        @staticmethod
        def ValueOf(value: int) -> FilletBuilder.EnumFillFaceHolesType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EnumSkipWeldMethod(Enum):
        """
        Members Include: 
         |NumberLength| 
         |NumberSpacing| 
         |SpacingLength| 

        """
        NumberLength: int
        NumberSpacing: int
        SpacingLength: int
        @staticmethod
        def ValueOf(value: int) -> FilletBuilder.EnumSkipWeldMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EnumWeldingType(Enum):
        """
        Members Include: 
         |T| 
         |Lap| 
         |Corner| 

        """
        T: int
        Lap: int
        Corner: int
        @staticmethod
        def ValueOf(value: int) -> FilletBuilder.EnumWeldingType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AddCosmeticEnd(self) -> bool:
        """
        Getter for property: (bool) AddCosmeticEnd
         Returns the value identify if a cosmtic end should be added to each end of the fillet.  
             
         
        """
        pass
    @AddCosmeticEnd.setter
    def AddCosmeticEnd(self, addCosmeticEnd: bool):
        """
        Setter for property: (bool) AddCosmeticEnd
         Returns the value identify if a cosmtic end should be added to each end of the fillet.  
             
         
        """
        pass
    @property
    def AllowBroken(self) -> bool:
        """
        Getter for property: (bool) AllowBroken
         Returns the toggle to allow broken link.  
             
         
        """
        pass
    @AllowBroken.setter
    def AllowBroken(self, allowBroken: bool):
        """
        Setter for property: (bool) AllowBroken
         Returns the toggle to allow broken link.  
             
         
        """
        pass
    @property
    def AssignWeldPMI(self) -> bool:
        """
        Getter for property: (bool) AssignWeldPMI
         Returns the toggle to assign weld pmi.  
             
         
        """
        pass
    @AssignWeldPMI.setter
    def AssignWeldPMI(self, assignWeldPMI: bool):
        """
        Setter for property: (bool) AssignWeldPMI
         Returns the toggle to assign weld pmi.  
             
         
        """
        pass
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns the value identify if WAVE links should remain unbroken.  
             
         
        """
        pass
    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
         Returns the value identify if WAVE links should remain unbroken.  
             
         
        """
        pass
    @property
    def ConstructionMethod(self) -> FilletBuilder.EnumConstructionMethod:
        """
        Getter for property: ( FilletBuilder.EnumConstructionMethod NXOpe) ConstructionMethod
         Returns the value for determining the construction method.  
           Default method should be used for all conditions, unless you know the situation if for the roll around condition.   
         
        """
        pass
    @ConstructionMethod.setter
    def ConstructionMethod(self, constructionMethod: FilletBuilder.EnumConstructionMethod):
        """
        Setter for property: ( FilletBuilder.EnumConstructionMethod NXOpe) ConstructionMethod
         Returns the value for determining the construction method.  
           Default method should be used for all conditions, unless you know the situation if for the roll around condition.   
         
        """
        pass
    @property
    def ContourHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ContourHeight
         Returns the linear dimension contour height.  
             
         
        """
        pass
    @property
    def ContourType(self) -> FilletBuilder.EnumContour:
        """
        Getter for property: ( FilletBuilder.EnumContour NXOpe) ContourType
         Returns the contour.  
             
         
        """
        pass
    @ContourType.setter
    def ContourType(self, contour: FilletBuilder.EnumContour):
        """
        Setter for property: ( FilletBuilder.EnumContour NXOpe) ContourType
         Returns the contour.  
             
         
        """
        pass
    @property
    def DirectToggle(self) -> bool:
        """
        Getter for property: (bool) DirectToggle
         Returns the toggle to change direction.  
             
         
        """
        pass
    @DirectToggle.setter
    def DirectToggle(self, directToggle: bool):
        """
        Setter for property: (bool) DirectToggle
         Returns the toggle to change direction.  
             
         
        """
        pass
    @property
    def DirectionVector1(self) -> bool:
        """
        Getter for property: (bool) DirectionVector1
         Returns the face normal direction.  
             
         
        """
        pass
    @DirectionVector1.setter
    def DirectionVector1(self, directionVector1: bool):
        """
        Setter for property: (bool) DirectionVector1
         Returns the face normal direction.  
             
         
        """
        pass
    @property
    def DirectionVector2(self) -> bool:
        """
        Getter for property: (bool) DirectionVector2
         Returns the face normal direction for the second face.  
             
         
        """
        pass
    @DirectionVector2.setter
    def DirectionVector2(self, directionVector2: bool):
        """
        Setter for property: (bool) DirectionVector2
         Returns the face normal direction for the second face.  
             
         
        """
        pass
    @property
    def DistTolerance(self) -> float:
        """
        Getter for property: (float) DistTolerance
         Returns the distance tolerance.  
             
         
        """
        pass
    @DistTolerance.setter
    def DistTolerance(self, distTolerance: float):
        """
        Setter for property: (float) DistTolerance
         Returns the distance tolerance.  
             
         
        """
        pass
    @property
    def EdgeSet1(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) EdgeSet1
         Returns the edge set1.  
             
         
        """
        pass
    @property
    def EdgeSet2(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) EdgeSet2
         Returns the edge set2.  
             
         
        """
        pass
    @property
    def EndDist(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) EndDist
         Returns the on path dimension end distance.  
             
         
        """
        pass
    @property
    def EndVector(self) -> bool:
        """
        Getter for property: (bool) EndVector
         Returns the end direction reversed or not.  
             
         
        """
        pass
    @EndVector.setter
    def EndVector(self, endVector: bool):
        """
        Setter for property: (bool) EndVector
         Returns the end direction reversed or not.  
             
         
        """
        pass
    @property
    def EnumMethod(self) -> FilletBuilder.EnumSkipWeldMethod:
        """
        Getter for property: ( FilletBuilder.EnumSkipWeldMethod NXOpe) EnumMethod
         Returns the enum method for skip welds.  
             
         
        """
        pass
    @EnumMethod.setter
    def EnumMethod(self, enumMethod: FilletBuilder.EnumSkipWeldMethod):
        """
        Setter for property: ( FilletBuilder.EnumSkipWeldMethod NXOpe) EnumMethod
         Returns the enum method for skip welds.  
             
         
        """
        pass
    @property
    def ExtendEdges(self) -> FilletBuilder.EnumExtendEdges:
        """
        Getter for property: ( FilletBuilder.EnumExtendEdges NXOpe) ExtendEdges
         Returns the value for how to populate the edge sets.  
             
         
        """
        pass
    @ExtendEdges.setter
    def ExtendEdges(self, extendEdges: FilletBuilder.EnumExtendEdges):
        """
        Setter for property: ( FilletBuilder.EnumExtendEdges NXOpe) ExtendEdges
         Returns the value for how to populate the edge sets.  
             
         
        """
        pass
    @property
    def ExtensionDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ExtensionDistance
         Returns the linear dimension extension distance.  
             
         
        """
        pass
    @property
    def ExtensionMethod(self) -> FilletBuilder.EnumExtensionMethod:
        """
        Getter for property: ( FilletBuilder.EnumExtensionMethod NXOpe) ExtensionMethod
         Returns the extension method.  
             
         
        """
        pass
    @ExtensionMethod.setter
    def ExtensionMethod(self, extensionMethod: FilletBuilder.EnumExtensionMethod):
        """
        Setter for property: ( FilletBuilder.EnumExtensionMethod NXOpe) ExtensionMethod
         Returns the extension method.  
             
         
        """
        pass
    @property
    def FaceFillGapDistance(self) -> float:
        """
        Getter for property: (float) FaceFillGapDistance
         Returns the distance the fillet will span when there are gaps in the sheet definition.  
             
         
        """
        pass
    @FaceFillGapDistance.setter
    def FaceFillGapDistance(self, faceFillGapDistance: float):
        """
        Setter for property: (float) FaceFillGapDistance
         Returns the distance the fillet will span when there are gaps in the sheet definition.  
             
         
        """
        pass
    @property
    def FaceSet1(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FaceSet1
         Returns the face set1.  
             
         
        """
        pass
    @property
    def FaceSet2(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FaceSet2
         Returns the face set2.  
             
         
        """
        pass
    @property
    def FieldWeld(self) -> bool:
        """
        Getter for property: (bool) FieldWeld
         Returns the field weld.  
             
         
        """
        pass
    @FieldWeld.setter
    def FieldWeld(self, fieldWeld: bool):
        """
        Setter for property: (bool) FieldWeld
         Returns the field weld.  
             
         
        """
        pass
    @property
    def FillFaceHoles(self) -> FilletBuilder.EnumFillFaceHolesType:
        """
        Getter for property: ( FilletBuilder.EnumFillFaceHolesType NXOpe) FillFaceHoles
         Returns the value to identify if the face set should be filled during construction.  
           Only holes fully bounded by a single face will be filled.   
         
        """
        pass
    @FillFaceHoles.setter
    def FillFaceHoles(self, fillFaceHolestype: FilletBuilder.EnumFillFaceHolesType):
        """
        Setter for property: ( FilletBuilder.EnumFillFaceHolesType NXOpe) FillFaceHoles
         Returns the value to identify if the face set should be filled during construction.  
           Only holes fully bounded by a single face will be filled.   
         
        """
        pass
    @property
    def FilletType(self) -> FilletBuilder.EnumWeldingType:
        """
        Getter for property: ( FilletBuilder.EnumWeldingType NXOpe) FilletType
         Returns the fillet type.  
             
         
        """
        pass
    @FilletType.setter
    def FilletType(self, filletType: FilletBuilder.EnumWeldingType):
        """
        Setter for property: ( FilletBuilder.EnumWeldingType NXOpe) FilletType
         Returns the fillet type.  
             
         
        """
        pass
    @property
    def FirstLeg(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FirstLeg
         Returns the linear dimension first leg.  
             
         
        """
        pass
    @property
    def NumberOfWelds(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NumberOfWelds
         Returns the expression number indicates number of welds in skip welds.  
             
         
        """
        pass
    @property
    def Pmi(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) Pmi
         Returns the pmi symbol.  
             
         
        """
        pass
    @Pmi.setter
    def Pmi(self, pmi: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) Pmi
         Returns the pmi symbol.  
             
         
        """
        pass
    @property
    def SecondLeg(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SecondLeg
         Returns the linear dimension second leg.  
             
         
        """
        pass
    @property
    def SeedFace1(self) -> NXOpen.Face:
        """
        Getter for property: ( NXOpen.Face) SeedFace1
         Returns the first seed face.  
             
         
        """
        pass
    @SeedFace1.setter
    def SeedFace1(self, seedFace1: NXOpen.Face):
        """
        Setter for property: ( NXOpen.Face) SeedFace1
         Returns the first seed face.  
             
         
        """
        pass
    @property
    def SeedFace2(self) -> NXOpen.Face:
        """
        Getter for property: ( NXOpen.Face) SeedFace2
         Returns the second seed face.  
             
         
        """
        pass
    @SeedFace2.setter
    def SeedFace2(self, seedFace2: NXOpen.Face):
        """
        Setter for property: ( NXOpen.Face) SeedFace2
         Returns the second seed face.  
             
         
        """
        pass
    @property
    def SeedPoint1(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) SeedPoint1
         Returns the point on the first face.  
             
         
        """
        pass
    @SeedPoint1.setter
    def SeedPoint1(self, seedPoint1: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) SeedPoint1
         Returns the point on the first face.  
             
         
        """
        pass
    @property
    def SeedPoint2(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) SeedPoint2
         Returns the point on the second face.  
             
         
        """
        pass
    @SeedPoint2.setter
    def SeedPoint2(self, seedPoint1: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) SeedPoint2
         Returns the point on the second face.  
             
         
        """
        pass
    @property
    def SegmentLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SegmentLength
         Returns the linear dimension length indicates segment length for each weld.  
             
         
        """
        pass
    @property
    def Spacing(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Spacing
         Returns the linear dimension spacing indicates distance between each weld.  
             
         
        """
        pass
    @property
    def StartDist(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) StartDist
         Returns the on path dimension start distance.  
             
         
        """
        pass
    @property
    def StartVector(self) -> bool:
        """
        Getter for property: (bool) StartVector
         Returns the start direction reversed or not.  
             
         
        """
        pass
    @StartVector.setter
    def StartVector(self, startVector: bool):
        """
        Setter for property: (bool) StartVector
         Returns the start direction reversed or not.  
             
         
        """
        pass
    @property
    def ThroatThickToggle(self) -> bool:
        """
        Getter for property: (bool) ThroatThickToggle
         Returns the toggle throat thickness.  
             
         
        """
        pass
    @ThroatThickToggle.setter
    def ThroatThickToggle(self, throatThickToggle: bool):
        """
        Setter for property: (bool) ThroatThickToggle
         Returns the toggle throat thickness.  
             
         
        """
        pass
    @property
    def ToggleCreateSkipWelds(self) -> bool:
        """
        Getter for property: (bool) ToggleCreateSkipWelds
         Returns the toggle to create skip welds.  
             
         
        """
        pass
    @ToggleCreateSkipWelds.setter
    def ToggleCreateSkipWelds(self, toggleCreateSkipWelds: bool):
        """
        Setter for property: (bool) ToggleCreateSkipWelds
         Returns the toggle to create skip welds.  
             
         
        """
        pass
    @property
    def ToggleRecreateDeletedWelds(self) -> bool:
        """
        Getter for property: (bool) ToggleRecreateDeletedWelds
         Returns the toggle to recreate deleted welds.  
             
         
        """
        pass
    @ToggleRecreateDeletedWelds.setter
    def ToggleRecreateDeletedWelds(self, toggleRecreateDeletedWelds: bool):
        """
        Setter for property: (bool) ToggleRecreateDeletedWelds
         Returns the toggle to recreate deleted welds.  
             
         
        """
        pass
    @property
    def Uparameter1(self) -> float:
        """
        Getter for property: (float) Uparameter1
         Returns the u parameter for first face.  
             
         
        """
        pass
    @Uparameter1.setter
    def Uparameter1(self, u1: float):
        """
        Setter for property: (float) Uparameter1
         Returns the u parameter for first face.  
             
         
        """
        pass
    @property
    def Uparameter2(self) -> float:
        """
        Getter for property: (float) Uparameter2
         Returns the u parameter for second face.  
             
         
        """
        pass
    @Uparameter2.setter
    def Uparameter2(self, u2: float):
        """
        Setter for property: (float) Uparameter2
         Returns the u parameter for second face.  
             
         
        """
        pass
    @property
    def Vparameter1(self) -> float:
        """
        Getter for property: (float) Vparameter1
         Returns the v parameter for first face.  
             
         
        """
        pass
    @Vparameter1.setter
    def Vparameter1(self, v1: float):
        """
        Setter for property: (float) Vparameter1
         Returns the v parameter for first face.  
             
         
        """
        pass
    @property
    def Vparameter2(self) -> float:
        """
        Getter for property: (float) Vparameter2
         Returns the v parameter for second face.  
             
         
        """
        pass
    @Vparameter2.setter
    def Vparameter2(self, v2: float):
        """
        Setter for property: (float) Vparameter2
         Returns the v parameter for second face.  
             
         
        """
        pass
    @property
    def WeldingCharacteristics(self) -> CharacteristicsBuilder:
        """
        Getter for property: ( CharacteristicsBuilder NXOpe) WeldingCharacteristics
         Returns the welding characteristics.  
             
         
        """
        pass
import NXOpen.Features
class Fillet(NXOpen.Features.BodyFeature): 
    """ Represents a Weld Fillet Feature. This is the new Fillet Dialog introduced in 8.0 """
    pass
import NXOpen.Features
class Fill(NXOpen.Features.BodyFeature): 
    """ Represents a Weld Fill feature """
    pass
import NXOpen
import NXOpen.Features
class GrooveBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Groove Weld feature """
    @property
    def BottomExtension(self) -> WeldGrooveExtension:
        """
        Getter for property: ( WeldGrooveExtension NXOpe) BottomExtension
         Returns the extension method for the bottom edges   
            
         
        """
        pass
    @BottomExtension.setter
    def BottomExtension(self, extension_type: WeldGrooveExtension):
        """
        Setter for property: ( WeldGrooveExtension NXOpe) BottomExtension
         Returns the extension method for the bottom edges   
            
         
        """
        pass
    @property
    def ContourShape(self) -> WeldContourShape:
        """
        Getter for property: ( WeldContourShape NXOpe) ContourShape
         Returns the contour contour shape.  
           This is the shape on the top of the groove weld   
         
        """
        pass
    @ContourShape.setter
    def ContourShape(self, contour_shape: WeldContourShape):
        """
        Setter for property: ( WeldContourShape NXOpe) ContourShape
         Returns the contour contour shape.  
           This is the shape on the top of the groove weld   
         
        """
        pass
    @property
    def DistanceFromEnd(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DistanceFromEnd
         Returns the distance from the end of the faces to build the groove weld   
            
         
        """
        pass
    @property
    def DistanceFromStart(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DistanceFromStart
         Returns the distance from the start of the faces to build the groove weld   
            
         
        """
        pass
    @property
    def FirstFaceset(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FirstFaceset
         Returns the first set of faces   
            
         
        """
        pass
    @FirstFaceset.setter
    def FirstFaceset(self, face_collector: NXOpen.ScCollector):
        """
        Setter for property: ( NXOpen.ScCollector) FirstFaceset
         Returns the first set of faces   
            
         
        """
        pass
    @property
    def FirstFacesetBottomEdges(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) FirstFacesetBottomEdges
         Returns the first set bottom edges to extend   
            
         
        """
        pass
    @FirstFacesetBottomEdges.setter
    def FirstFacesetBottomEdges(self, section: NXOpen.Section):
        """
        Setter for property: ( NXOpen.Section) FirstFacesetBottomEdges
         Returns the first set bottom edges to extend   
            
         
        """
        pass
    @property
    def FirstFacesetHelpPoint(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) FirstFacesetHelpPoint
         Returns the first set help point.  
           If multiple solutions exist, the desired solution 
                used will be the one closest to this point   
         
        """
        pass
    @FirstFacesetHelpPoint.setter
    def FirstFacesetHelpPoint(self, help_point: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) FirstFacesetHelpPoint
         Returns the first set help point.  
           If multiple solutions exist, the desired solution 
                used will be the one closest to this point   
         
        """
        pass
    @property
    def FirstFacesetTopEdges(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) FirstFacesetTopEdges
         Returns the first set top edges to extend   
            
         
        """
        pass
    @FirstFacesetTopEdges.setter
    def FirstFacesetTopEdges(self, section: NXOpen.Section):
        """
        Setter for property: ( NXOpen.Section) FirstFacesetTopEdges
         Returns the first set top edges to extend   
            
         
        """
        pass
    @property
    def GrooveShape(self) -> WeldGrooveShape:
        """
        Getter for property: ( WeldGrooveShape NXOpe) GrooveShape
         Returns the shape of the groove weld to create   
            
         
        """
        pass
    @GrooveShape.setter
    def GrooveShape(self, groove_shape: WeldGrooveShape):
        """
        Setter for property: ( WeldGrooveShape NXOpe) GrooveShape
         Returns the shape of the groove weld to create   
            
         
        """
        pass
    @property
    def GrooveType(self) -> WeldGrooveType:
        """
        Getter for property: ( WeldGrooveType NXOpe) GrooveType
         Returns the groove creation type   
            
         
        """
        pass
    @GrooveType.setter
    def GrooveType(self, groove_type: WeldGrooveType):
        """
        Setter for property: ( WeldGrooveType NXOpe) GrooveType
         Returns the groove creation type   
            
         
        """
        pass
    @property
    def IsFieldWeld(self) -> bool:
        """
        Getter for property: (bool) IsFieldWeld
         Returns the field weld status.  
           If true then this is a field weld,
                if false it is not.   
         
        """
        pass
    @IsFieldWeld.setter
    def IsFieldWeld(self, field_weld: bool):
        """
        Setter for property: (bool) IsFieldWeld
         Returns the field weld status.  
           If true then this is a field weld,
                if false it is not.   
         
        """
        pass
    @property
    def IsFirstFacesetNormalReversed(self) -> bool:
        """
        Getter for property: (bool) IsFirstFacesetNormalReversed
         Returns the side of the faceset to build the groove feature.  
           The feature will
                be built opposite the face closest to the help point 
                  
         
        """
        pass
    @IsFirstFacesetNormalReversed.setter
    def IsFirstFacesetNormalReversed(self, reversedd: bool):
        """
        Setter for property: (bool) IsFirstFacesetNormalReversed
         Returns the side of the faceset to build the groove feature.  
           The feature will
                be built opposite the face closest to the help point 
                  
         
        """
        pass
    @property
    def IsNumberOfSegments(self) -> bool:
        """
        Getter for property: (bool) IsNumberOfSegments
         Returns the is number of segments option.  
           This is used when creating skip welds to
               compute the spacing between them.   
         
        """
        pass
    @IsNumberOfSegments.setter
    def IsNumberOfSegments(self, is_number_of_segments: bool):
        """
        Setter for property: (bool) IsNumberOfSegments
         Returns the is number of segments option.  
           This is used when creating skip welds to
               compute the spacing between them.   
         
        """
        pass
    @property
    def IsSecondFacesetNormalReversed(self) -> bool:
        """
        Getter for property: (bool) IsSecondFacesetNormalReversed
         Returns the side of the faceset to build the groove feature.  
           The feature will
                be built opposite the face closest to the help point 
                  
         
        """
        pass
    @IsSecondFacesetNormalReversed.setter
    def IsSecondFacesetNormalReversed(self, reversed: bool):
        """
        Setter for property: (bool) IsSecondFacesetNormalReversed
         Returns the side of the faceset to build the groove feature.  
           The feature will
                be built opposite the face closest to the help point 
                  
         
        """
        pass
    @property
    def IsSegmentLength(self) -> bool:
        """
        Getter for property: (bool) IsSegmentLength
         Returns the is segment length option.  
           This is used when creating skip welds to
               compute the spacing between them.   
         
        """
        pass
    @IsSegmentLength.setter
    def IsSegmentLength(self, is_segment_length: bool):
        """
        Setter for property: (bool) IsSegmentLength
         Returns the is segment length option.  
           This is used when creating skip welds to
               compute the spacing between them.   
         
        """
        pass
    @property
    def IsSpacing(self) -> bool:
        """
        Getter for property: (bool) IsSpacing
         Returns the is spacing option.  
           This is used when creating skip welds to 
                compute the spacing between them.   
         
        """
        pass
    @IsSpacing.setter
    def IsSpacing(self, is_spacing: bool):
        """
        Setter for property: (bool) IsSpacing
         Returns the is spacing option.  
           This is used when creating skip welds to 
                compute the spacing between them.   
         
        """
        pass
    @property
    def Method(self) -> WeldArcMethod:
        """
        Getter for property: ( WeldArcMethod NXOpe) Method
         Returns the method   
            
         
        """
        pass
    @Method.setter
    def Method(self, method: WeldArcMethod):
        """
        Setter for property: ( WeldArcMethod NXOpe) Method
         Returns the method   
            
         
        """
        pass
    @property
    def NumberOfSegments(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NumberOfSegments
         Returns the number of weld welds for a skip weld.  
              
         
        """
        pass
    @property
    def NumberRequiredFaceSets(self) -> int:
        """
        Getter for property: (int) NumberRequiredFaceSets
         Returns the number of connected parts.  
           Either one for two.   
         
        """
        pass
    @NumberRequiredFaceSets.setter
    def NumberRequiredFaceSets(self, number_required_face_sets: int):
        """
        Setter for property: (int) NumberRequiredFaceSets
         Returns the number of connected parts.  
           Either one for two.   
         
        """
        pass
    @property
    def OutputGeometryType(self) -> WeldFeatureOutput:
        """
        Getter for property: ( WeldFeatureOutput NXOpe) OutputGeometryType
         Returns the output geometry type   
            
         
        """
        pass
    @OutputGeometryType.setter
    def OutputGeometryType(self, output_geometry_type: WeldFeatureOutput):
        """
        Setter for property: ( WeldFeatureOutput NXOpe) OutputGeometryType
         Returns the output geometry type   
            
         
        """
        pass
    @property
    def OutputType(self) -> OutputType:
        """
        Getter for property: ( OutputType NXOpe) OutputType
         Returns the output type.  
             
         
        """
        pass
    @OutputType.setter
    def OutputType(self, output_type: OutputType):
        """
        Setter for property: ( OutputType NXOpe) OutputType
         Returns the output type.  
             
         
        """
        pass
    @property
    def PrepareEdges(self) -> WeldPrepareEdges:
        """
        Getter for property: ( WeldPrepareEdges NXOpe) PrepareEdges
         Returns the apply edge preportion indicator.  
             
         
        """
        pass
    @PrepareEdges.setter
    def PrepareEdges(self, prepare_edges: WeldPrepareEdges):
        """
        Setter for property: ( WeldPrepareEdges NXOpe) PrepareEdges
         Returns the apply edge preportion indicator.  
             
         
        """
        pass
    @property
    def RootUpdate(self) -> WeldRootUpdate:
        """
        Getter for property: ( WeldRootUpdate NXOpe) RootUpdate
         Returns the process type   
            
         
        """
        pass
    @RootUpdate.setter
    def RootUpdate(self, root_update: WeldRootUpdate):
        """
        Setter for property: ( WeldRootUpdate NXOpe) RootUpdate
         Returns the process type   
            
         
        """
        pass
    @property
    def SecondFaceset(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SecondFaceset
         Returns the second set of faces   
            
         
        """
        pass
    @SecondFaceset.setter
    def SecondFaceset(self, face_collector: NXOpen.ScCollector):
        """
        Setter for property: ( NXOpen.ScCollector) SecondFaceset
         Returns the second set of faces   
            
         
        """
        pass
    @property
    def SecondFacesetBottomEdges(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) SecondFacesetBottomEdges
         Returns the second set bottom edges to extend   
            
         
        """
        pass
    @SecondFacesetBottomEdges.setter
    def SecondFacesetBottomEdges(self, edge_collector: NXOpen.Section):
        """
        Setter for property: ( NXOpen.Section) SecondFacesetBottomEdges
         Returns the second set bottom edges to extend   
            
         
        """
        pass
    @property
    def SecondFacesetHelpPoint(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) SecondFacesetHelpPoint
         Returns the second set help point.  
           If multiple solutions exist, the desired solution 
                used will be the one closest to this point   
         
        """
        pass
    @SecondFacesetHelpPoint.setter
    def SecondFacesetHelpPoint(self, help_point: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) SecondFacesetHelpPoint
         Returns the second set help point.  
           If multiple solutions exist, the desired solution 
                used will be the one closest to this point   
         
        """
        pass
    @property
    def SecondFacesetTopEdges(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) SecondFacesetTopEdges
         Returns the second set top edges to extend   
            
         
        """
        pass
    @SecondFacesetTopEdges.setter
    def SecondFacesetTopEdges(self, edge_collector: NXOpen.Section):
        """
        Setter for property: ( NXOpen.Section) SecondFacesetTopEdges
         Returns the second set top edges to extend   
            
         
        """
        pass
    @property
    def SegmentLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SegmentLength
         Returns the segment length for a skip weld.  
              
         
        """
        pass
    @property
    def SequenceNumber(self) -> int:
        """
        Getter for property: (int) SequenceNumber
         Returns the sequence number for the groove feature.  
           Each groove feature contains a solid.
                If multiple groove wels are to be created, you must specify the sequence of the groove weld you want.
                For example if you are expecting 3 welds to be created. You must create 3 groove weld features.
                The features will have sequence numbers 0,1 and 2.    
         
        """
        pass
    @SequenceNumber.setter
    def SequenceNumber(self, sequence_number: int):
        """
        Setter for property: (int) SequenceNumber
         Returns the sequence number for the groove feature.  
           Each groove feature contains a solid.
                If multiple groove wels are to be created, you must specify the sequence of the groove weld you want.
                For example if you are expecting 3 welds to be created. You must create 3 groove weld features.
                The features will have sequence numbers 0,1 and 2.    
         
        """
        pass
    @property
    def SpacingDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SpacingDistance
         Returns the desired spacing between skip welds.  
             
         
        """
        pass
    @property
    def TaperAtEnd(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TaperAtEnd
         Returns the taper angle at the end.  
           A positive number will taper towards
                the inside of the weld.   
         
        """
        pass
    @property
    def TaperAtStart(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TaperAtStart
         Returns the taper angle at the start.  
           A positive number will taper towards
                the inside of the weld.   
         
        """
        pass
    @property
    def TaperMethod(self) -> WeldTaperMethod:
        """
        Getter for property: ( WeldTaperMethod NXOpe) TaperMethod
         Returns the taper method to use if tapering is specified.  
             
         
        """
        pass
    @TaperMethod.setter
    def TaperMethod(self, taper_method: WeldTaperMethod):
        """
        Setter for property: ( WeldTaperMethod NXOpe) TaperMethod
         Returns the taper method to use if tapering is specified.  
             
         
        """
        pass
    @property
    def TopExtension(self) -> WeldGrooveExtension:
        """
        Getter for property: ( WeldGrooveExtension NXOpe) TopExtension
         Returns the the extension method for the top edges   
            
         
        """
        pass
    @TopExtension.setter
    def TopExtension(self, extension_type: WeldGrooveExtension):
        """
        Setter for property: ( WeldGrooveExtension NXOpe) TopExtension
         Returns the the extension method for the top edges   
            
         
        """
        pass
    def GetContourHeight(self) -> NXOpen.Expression:
        """
         Gets the contour height needed to describe groove weld shape 
         Returns contour_height ( NXOpen.Expression):  expression .
        """
        pass
    def GetFirstFacesetEndAdjacentFaces(self) -> List[NXOpen.Face]:
        """
         Gets the adjacent faces of the target solid. These faces are used to
                trim the groove weld solid with. 
         Returns objects ( NXOpen.Face Li):  the adjacent face reference objects .
        """
        pass
    def GetFirstFacesetStartAdjacentFaces(self) -> List[NXOpen.Face]:
        """
         Gets the adjacent faces of the target solid. These faces are used to
                trim the groove weld solid with. 
         Returns objects ( NXOpen.Face Li):  the adjacent face reference objects .
        """
        pass
    def GetGrooveAngle(self) -> NXOpen.Expression:
        """
         Gets the groove angle needed to describe groove weld 
         Returns groove_angle ( NXOpen.Expression):  expression .
        """
        pass
    def GetGrooveRadius(self) -> NXOpen.Expression:
        """
         Gets the groove radius needed to describe groove weld 
         Returns groove_angle ( NXOpen.Expression):  expression .
        """
        pass
    def GetPenetrationDepth(self) -> NXOpen.Expression:
        """
         Gets the penetration depth needed to describe groove weld 
         Returns penetration_depth ( NXOpen.Expression):  expression .
        """
        pass
    def GetRootOpening(self) -> NXOpen.Expression:
        """
         Gets the root opening height needed to describe groove weld 
         Returns root_opening ( NXOpen.Expression):  expression .
        """
        pass
    def GetRootPenetration(self) -> NXOpen.Expression:
        """
         Gets the root penetration needed to describe groove weld 
         Returns root_penetration ( NXOpen.Expression):  expression .
        """
        pass
    def GetSecondFacesetEndAdjacentFaces(self) -> List[NXOpen.Face]:
        """
         Gets the adjacent faces of the target solid. These faces are used to
                trim the groove weld solid with. 
         Returns objects ( NXOpen.Face Li):  the adjacent face reference objects .
        """
        pass
    def GetSecondFacesetStartAdjacentFaces(self) -> List[NXOpen.Face]:
        """
         Gets the adjacent faces of the target solid. These faces are used to
                trim the groove weld solid with. 
         Returns objects ( NXOpen.Face Li):  the adjacent face reference objects .
        """
        pass
    def GetSecondPenetrationDepth(self) -> NXOpen.Expression:
        """
         Gets the second penetration depth needed to describe groove weld. This is only needed if face heights are different. 
         Returns second_penetration_depth ( NXOpen.Expression):  expression .
        """
        pass
    def SetContourHeight(self, contour_height: str) -> None:
        """
         Sets the contour height needed to describe groove weld 
        """
        pass
    def SetDistanceFromEnd(self, end_distance: str) -> None:
        """
         Sets the distance from the end of the faces to build the groove weld 
        """
        pass
    def SetDistanceFromStart(self, start_distance: str) -> None:
        """
         Set the distance from the start of the faces to build the groove weld 
        """
        pass
    def SetFirstFacesetEndAdjacentFaces(self, objects: List[NXOpen.Face]) -> None:
        """
         Sets the adjacent faces of the target solid. These faces are used to
                trim the groove weld solid with. 
        """
        pass
    def SetFirstFacesetStartAdjacentFaces(self, objects: List[NXOpen.Face]) -> None:
        """
         Sets the adjacent faces of the target solid. These faces are used to
                trim the groove weld solid with. 
        """
        pass
    def SetGrooveAngle(self, groove_angle: str) -> None:
        """
         Sets the groove angle needed to describe groove weld 
        """
        pass
    def SetGrooveRadius(self, groove_angle: str) -> None:
        """
         Sets the groove radius needed to describe groove weld 
        """
        pass
    def SetNumberOfSegments(self, num_segments: str) -> None:
        """
         Sets the desired number of segments for the groove weld. 
        """
        pass
    def SetPenetrationDepth(self, penetration_depth: str) -> None:
        """
         Sets the penetration depth needed to describe groove weld 
        """
        pass
    def SetRootOpening(self, root_opening: str) -> None:
        """
         Sets the root opening height needed to describe groove weld 
        """
        pass
    def SetRootPenetration(self, root_penetration: str) -> None:
        """
         Sets the root penetration needed to describe groove weld 
        """
        pass
    def SetSecondFacesetEndAdjacentFaces(self, objects: List[NXOpen.Face]) -> None:
        """
         Sets the adjacent faces of the target solid. These faces are used to
                trim the groove weld solid with. 
        """
        pass
    def SetSecondFacesetStartAdjacentFaces(self, objects: List[NXOpen.Face]) -> None:
        """
         Sets the adjacent faces of the target solid. These faces are used to
                trim the groove weld solid with. 
        """
        pass
    def SetSecondPenetrationDepth(self, second_penetration_depth: str) -> None:
        """
         Sets the penetration depth needed to describe groove weld 
        """
        pass
    def SetSegmentLength(self, segment_length: str) -> None:
        """
         Sets the desired segment lengh for the skip weld. 
        """
        pass
    def SetSpacingDistance(self, spacing_distance: str) -> None:
        """
         Sets the desired spacing between skip welds. 
        """
        pass
    def SetTaperAtEnd(self, end_taper: str) -> None:
        """
         Sets the taper angle at the end. A positive number will taper towards
                the inside of the weld. 
        """
        pass
    def SetTaperAtStart(self, start_taper: str) -> None:
        """
         Sets the taper angle at the start. A positive number will taper towards
                the inside of the weld. 
        """
        pass
import NXOpen.Features
class Groove(NXOpen.Features.Feature): 
    """ Represents a WeldGroove feature. """
    pass
import NXOpen
class IFeature(NXOpen.INXObject): 
    """ Represents a Weld Assistant or Structure Welding created feature """
    @abstractmethod
    def GetFeatureDiagnostics(self) -> List[int]:
        """
         Returns the feature diagnostic information, warning, or error codes. 
         Returns diagnosticCodes (List[int]):  the information, warning, or error codes for this feature. .
        """
        pass
    @abstractmethod
    def GetFeatureIconName(self) -> str:
        """
         Gets the feature icon name. 
         Returns iconName (str): .
        """
        pass
    @abstractmethod
    def GetFeatureLayer(self) -> int:
        """
         Gets the feature layer. 
         Returns layer (int): .
        """
        pass
    @abstractmethod
    def GetFeatureObjectColor(self) -> int:
        """
         Gets the feature color. 
         Returns color (int): .
        """
        pass
    @abstractmethod
    def GetFeatureReferenceSetStrings(self) -> List[str]:
        """
         Gets all the reference sets that this feature is a member of. 
         Returns refSet (List[str]): .
        """
        pass
    @abstractmethod
    def GetFeatureReferenceSets(self) -> List[NXOpen.ReferenceSet]:
        """
         Gets all the reference sets that this feature is a member of. 
         Returns refSet ( NXOpen.ReferenceSet Li): .
        """
        pass
import NXOpen
class InformationBuilder(NXOpen.Builder): 
    """
        This class is used by "Fabrication Information" to output fabrication objects information.
        When commit is called, attributes and total weld length and volume of selected objects 
        will be output into a list window. No objects are returned when Commit is called.
    """
    class AttributeOriginType(Enum):
        """
        Members Include: 
         |Object| 
         |Df| 

        """
        Object: int
        Df: int
        @staticmethod
        def ValueOf(value: int) -> InformationBuilder.AttributeOriginType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AttributeOrigin(self) -> InformationBuilder.AttributeOriginType:
        """
        Getter for property: ( InformationBuilder.AttributeOriginType NXOpe) AttributeOrigin
         Returns the option indicating where the attributes are read from, welding object or corresponding Design Feature.  
            
         
        """
        pass
    @AttributeOrigin.setter
    def AttributeOrigin(self, attributeOrigin: InformationBuilder.AttributeOriginType):
        """
        Setter for property: ( InformationBuilder.AttributeOriginType NXOpe) AttributeOrigin
         Returns the option indicating where the attributes are read from, welding object or corresponding Design Feature.  
            
         
        """
        pass
    @property
    def ConnectedToInformation(self) -> bool:
        """
        Getter for property: (bool) ConnectedToInformation
         Returns the option to specify if the connected to information should be displayed in the output.  
             
         
        """
        pass
    @ConnectedToInformation.setter
    def ConnectedToInformation(self, connectedToInformation: bool):
        """
        Setter for property: (bool) ConnectedToInformation
         Returns the option to specify if the connected to information should be displayed in the output.  
             
         
        """
        pass
    @property
    def FabricationObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) FabricationObjects
         Returns the list of weld fabrication objects to create the output.  
             
         
        """
        pass
    @property
    def OutputAttributes(self) -> bool:
        """
        Getter for property: (bool) OutputAttributes
         Returns the option to specify if the weld attributes should be included in the output.  
             
         
        """
        pass
    @OutputAttributes.setter
    def OutputAttributes(self, outputAttributes: bool):
        """
        Setter for property: (bool) OutputAttributes
         Returns the option to specify if the weld attributes should be included in the output.  
             
         
        """
        pass
    @property
    def OutputLengthAndVolume(self) -> bool:
        """
        Getter for property: (bool) OutputLengthAndVolume
         Returns the option to specify if the weld length and volume should be calculated for the output.  
             
         
        """
        pass
    @OutputLengthAndVolume.setter
    def OutputLengthAndVolume(self, outputLengthAndVolume: bool):
        """
        Setter for property: (bool) OutputLengthAndVolume
         Returns the option to specify if the weld length and volume should be calculated for the output.  
             
         
        """
        pass
    def GetTotalLength(self) -> float:
        """
         Get the total length of the selection weld objects. 
                    This function may be time intensive and should be used after all weld data has been defined. 
         Returns totalLength (float): .
        """
        pass
    def GetTotalVolume(self) -> float:
        """
         Get the total volume of the selection weld objects. 
                    This function may be time intensive and should be used after all weld data has been defined. 
         Returns totalVolume (float): .
        """
        pass
import NXOpen
import NXOpen.Annotations
class JointExitBuilder(WeldJointBuilder): 
    """ Used to set custom edge preparation parameters of a NXOpen.Weld.WeldJoint feature. """
    class BodySide(Enum):
        """
        Members Include: 
         |First|  the first side. For fillet welds only this needs to be specified. 
         |Second|  the other side. This is only used for butt welds. 

        """
        First: int
        Second: int
        @staticmethod
        def ValueOf(value: int) -> JointExitBuilder.BodySide:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Positions(Enum):
        """
        Members Include: 
         |UpperChamfer|  the upper chamfer position 
         |Upper|  the upper position 
         |Middle|  the middle position 
         |Lower|  the lower position 
         |LowerChamfer|  the lower chamfer position 

        """
        UpperChamfer: int
        Upper: int
        Middle: int
        Lower: int
        LowerChamfer: int
        @staticmethod
        def ValueOf(value: int) -> JointExitBuilder.Positions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FilletSizes:
        """
         The structure for defining fillet weld lengths. 
         JointExitBuilderFilletSizes_Struct NXOpe is an alias for  JointExitBuilder.FilletSizes NXOpe.
        """
        @property
        def ThroatThickness(self) -> float:
            """
            Getter for property ThroatThickness
            The fillet weld throat thickness

            """
            pass
        @ThroatThickness.setter
        def ThroatThickness(self, value: float):
            """
            Getter for property ThroatThickness
            The fillet weld throat thickness
            Setter for property ThroatThickness
            The fillet weld throat thickness

            """
            pass
        @property
        def LegLength1(self) -> float:
            """
            Getter for property LegLength1
            The fillet weld first length.

            """
            pass
        @LegLength1.setter
        def LegLength1(self, value: float):
            """
            Getter for property LegLength1
            The fillet weld first length.
            Setter for property LegLength1
            The fillet weld first length.

            """
            pass
        @property
        def LegLength2(self) -> float:
            """
            Getter for property LegLength2
            The fillet weld second length.

            """
            pass
        @LegLength2.setter
        def LegLength2(self, value: float):
            """
            Getter for property LegLength2
            The fillet weld second length.
            Setter for property LegLength2
            The fillet weld second length.

            """
            pass
    @property
    def FinishMethod(self) -> NXOpen.Annotations.FinishMethod:
        """
        Getter for property: ( NXOpen.Annotations.FinishMethod) FinishMethod
         Returns the weld finish method   
            
         
        """
        pass
    @FinishMethod.setter
    def FinishMethod(self, method: NXOpen.Annotations.FinishMethod):
        """
        Setter for property: ( NXOpen.Annotations.FinishMethod) FinishMethod
         Returns the weld finish method   
            
         
        """
        pass
    @property
    def LeaveLooseEndValue(self) -> float:
        """
        Getter for property: (float) LeaveLooseEndValue
         Returns the leave loose value at the end of the joint curve   
            
         
        """
        pass
    @LeaveLooseEndValue.setter
    def LeaveLooseEndValue(self, endValue: float):
        """
        Setter for property: (float) LeaveLooseEndValue
         Returns the leave loose value at the end of the joint curve   
            
         
        """
        pass
    @property
    def LeaveLooseStartValue(self) -> float:
        """
        Getter for property: (float) LeaveLooseStartValue
         Returns the leave loose value at the start of the joint curve   
            
         
        """
        pass
    @LeaveLooseStartValue.setter
    def LeaveLooseStartValue(self, startValue: float):
        """
        Setter for property: (float) LeaveLooseStartValue
         Returns the leave loose value at the start of the joint curve   
            
         
        """
        pass
    @property
    def OtherSideSymbol(self) -> NXOpen.Annotations.Symbol:
        """
        Getter for property: ( NXOpen.Annotations.Symbol) OtherSideSymbol
         Returns the symbol for welding other side when it is not being prepared   
            
         
        """
        pass
    @OtherSideSymbol.setter
    def OtherSideSymbol(self, symbol: NXOpen.Annotations.Symbol):
        """
        Setter for property: ( NXOpen.Annotations.Symbol) OtherSideSymbol
         Returns the symbol for welding other side when it is not being prepared   
            
         
        """
        pass
    @property
    def RootOpening(self) -> float:
        """
        Getter for property: (float) RootOpening
         Returns the desired gap between bodies being welded   
            
         
        """
        pass
    @RootOpening.setter
    def RootOpening(self, rootOpening: float):
        """
        Setter for property: (float) RootOpening
         Returns the desired gap between bodies being welded   
            
         
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
    def Side(self) -> JointExitBuilder.BodySide:
        """
        Getter for property: ( JointExitBuilder.BodySide NXOpe) Side
         Returns the side edge preparation values will be applied to   
            
         
        """
        pass
    @Side.setter
    def Side(self, side: JointExitBuilder.BodySide):
        """
        Setter for property: ( JointExitBuilder.BodySide NXOpe) Side
         Returns the side edge preparation values will be applied to   
            
         
        """
        pass
    @property
    def SymbolType(self) -> NXOpen.Annotations.Symbol:
        """
        Getter for property: ( NXOpen.Annotations.Symbol) SymbolType
         Returns the symbol to override the symbol computed from the joint parameters, if  NXOpen::Annotations::Symbol  is not   NXOpen::Annotations::SymbolNone  .  
            
                  Currently only   NXOpen::Annotations::SymbolJButt   and   NXOpen::Annotations::SymbolUButt   are implemented. All other values
                  will be treated as   NXOpen::Annotations::SymbolNone  
                
         
        """
        pass
    @SymbolType.setter
    def SymbolType(self, symbol: NXOpen.Annotations.Symbol):
        """
        Setter for property: ( NXOpen.Annotations.Symbol) SymbolType
         Returns the symbol to override the symbol computed from the joint parameters, if  NXOpen::Annotations::Symbol  is not   NXOpen::Annotations::SymbolNone  .  
            
                  Currently only   NXOpen::Annotations::SymbolJButt   and   NXOpen::Annotations::SymbolUButt   are implemented. All other values
                  will be treated as   NXOpen::Annotations::SymbolNone  
                
         
        """
        pass
    def CreateEdgePrepCurves(self, areEdgesPrepared: bool, segmentAttributeTitle: str, primaryThickness: float, secondaryThickness: float) -> List[NXOpen.Curve]:
        """
         Creates sketch curves from joint parameters. 
         Returns newCurves ( NXOpen.Curve Li):  .
        """
        pass
    def CreateFilletCurves(self, oldCurves: List[NXOpen.Curve], primaryThickness: float, secondaryThickness: float) -> List[NXOpen.Curve]:
        """
         Creates fillet curves from joint parameters. 
         Returns newCurves ( NXOpen.Curve Li):  Includes oldCurves plus newly created fillet curves .
        """
        pass
    def GetAndClearErrorMessages(self) -> List[str]:
        """
         Gets error messages logged by callback and clears them 
         Returns messages (List[str]):  error messages logged by callback .
        """
        pass
    def GetAngleBetweenTag(self) -> float:
        """
         Get the angle between faces (primarysecondary or placementtarget 
         Returns rootOpening (float): .
        """
        pass
    def GetCallbackMessage(self) -> str:
        """
         Gets a message to display after callback processing ends 
         Returns message (str):  Message to display to user .
        """
        pass
    def GetCurveForLeader(self) -> NXOpen.Curve:
        """
         Get the curve used for weld symbol leader. 
         Returns leaderCurve ( NXOpen.Curve):  .
        """
        pass
    def GetEdgePrepValueAngle(self, position: JointExitBuilder.Positions) -> float:
        """
         Gets the angle for the desired weld position 
         Returns angle (float):  The angle of edge preporation for this position. .
        """
        pass
    def GetEdgePrepValueThickness(self, position: JointExitBuilder.Positions) -> float:
        """
         Gets the thickness for the desired weld position 
         Returns thickness (float):  The thickness depth for this position. .
        """
        pass
    def GetEdgePrepValues(self, position: JointExitBuilder.Positions) -> Tuple[float, float]:
        """
         Gets the thickness and angle combination to set for the desired weld position 
         Returns A tuple consisting of (thickness, angle). 
         - thickness is: float. The thickness depth for this position. .
         - angle is: float. The angle of edge preporation for this position. .

        """
        pass
    def GetEdgesPrepared(self) -> bool:
        """
         Indicates whether edges are prepared. 
         Returns areEdgesPrepared (bool):   .
        """
        pass
    def GetEdgesPreparedTag(self) -> bool:
        """
         Indicates whether edges are prepared. 
         Returns areEdgesPrepared (bool):   .
        """
        pass
    def GetFilletLengths(self) -> JointExitBuilder.FilletSizes:
        """
         Gets the fillet weld values for the side of the welding joint. 
         Returns sizes ( JointExitBuilder.FilletSizes NXOpe):  The fillet sizes for the side of the welding joint .
        """
        pass
    def GetFilletLengthsTag(self) -> JointExitBuilder.FilletSizes:
        """
         Gets the fillet weld values for the side of the welding joint. 
         Returns sizes ( JointExitBuilder.FilletSizes NXOpe):  The fillet sizes for the side of the welding joint .
        """
        pass
    def GetIsLongPointTag(self) -> bool:
        """
         Indicates long point scenario. 
         Returns isLongPoint (bool):   .
        """
        pass
    def GetMasterEdgeTag(self) -> NXOpen.ScCollector:
        """
         Get the master edges 
         Returns collector ( NXOpen.ScCollector): .
        """
        pass
    def GetOppositeFilletLengths(self) -> JointExitBuilder.FilletSizes:
        """
         Gets the fillet weld values for the opposite side of the welding joint. 
         Returns oppositeSizes ( JointExitBuilder.FilletSizes NXOpe):  The fillet sizes for the opposite side of the welding joint .
        """
        pass
    def GetOppositeFilletLengthsTag(self) -> JointExitBuilder.FilletSizes:
        """
         Gets the fillet weld values for the opposite side of the welding joint. 
         Returns oppositeSizes ( JointExitBuilder.FilletSizes NXOpe):  The fillet sizes for the opposite side of the welding joint .
        """
        pass
    def GetPlacementFaceTag(self) -> NXOpen.ScCollector:
        """
         Get the placement faces 
         Returns collector ( NXOpen.ScCollector): .
        """
        pass
    def GetPrimaryEdgeTag(self) -> NXOpen.ScCollector:
        """
         Get the primary edges 
         Returns collector ( NXOpen.ScCollector): .
        """
        pass
    def GetPrimaryFaceTag(self) -> NXOpen.ScCollector:
        """
         Get the primary faces 
         Returns collector ( NXOpen.ScCollector): .
        """
        pass
    def GetPrimaryThicknessTag(self) -> float:
        """
         Get the primary thickness 
         Returns thickness (float): .
        """
        pass
    def GetRootOpeningTag(self) -> float:
        """
         Get the desired gap between bodies being welded 
         Returns rootOpening (float): .
        """
        pass
    def GetSecondaryEdgeTag(self) -> NXOpen.ScCollector:
        """
         Get the secondary edges 
         Returns collector ( NXOpen.ScCollector): .
        """
        pass
    def GetSecondaryFaceTag(self) -> NXOpen.ScCollector:
        """
         Get the secondary faces 
         Returns collector ( NXOpen.ScCollector): .
        """
        pass
    def GetSecondaryThicknessTag(self) -> float:
        """
         Get the secondary thickness 
         Returns thickness (float): .
        """
        pass
    def GetTargetFaceTag(self) -> NXOpen.ScCollector:
        """
         Get the target faces 
         Returns collector ( NXOpen.ScCollector): .
        """
        pass
    def GetUseCallbackValues(self) -> bool:
        """
         Get flag if joint is to use callback values. 
         Returns useCallbackValues (bool):   .
        """
        pass
    def GetWeldTypeTag(self) -> WeldJointBuilder.WeldTypes:
        """
         Get the weld type 
         Returns type ( WeldJointBuilder.WeldTypes NXOpe): .
        """
        pass
    def IsCornerOpenTag(self) -> bool:
        """
         Returns true if corner joint is an open case which means the placement face only touches the target face at the master edge. 
         Returns status (bool): .
        """
        pass
    def RecreateSketchCurvesOnly(self, areEdgesPrepared: bool, oldCurves: List[NXOpen.Curve], segmentAttributeTitle: str, primaryThickness: float, secondaryThickness: float) -> List[NXOpen.Curve]:
        """
         Recreates sketch curves from joint parameters. 
         Returns newCurves ( NXOpen.Curve Li):  .
        """
        pass
    def SetBothFilletLengths(self, sizes: JointExitBuilder.FilletSizes) -> None:
        """
         Sets the symmetric fillet weld values for a welding joint. 
        """
        pass
    def SetCallbackFile(self, file: str) -> None:
        """
         Sets the callback file that was used for rules based join table 
        """
        pass
    def SetCallbackMessageTag(self, message: str) -> None:
        """
         Sets a message to display after callback processing ends 
        """
        pass
    def SetEdgePrepValues(self, position: JointExitBuilder.Positions, thickness: float, angle: float) -> None:
        """
         This method should be called multiple times.  First set the BodySide then call this method for each Position.
                  For Butt welds this function should be used to set each side. After the primary side is set, change
                  the BodySide and call this method for the secondary side. For Fillet welds, only the primary side needs to be set.
                
        """
        pass
    def SetEdgePrepValuesTag(self, position: JointExitBuilder.Positions, thickness: float, angle: float) -> None:
        """
         This method should be called multiple times.  First set the BodySide then call this method for each Position.
                  For Butt welds this function should be used to set each side. After the primary side is set, change
                  the BodySide and call this method for the secondary side. For Fillet welds, only the primary side needs to be set.
                
        """
        pass
    def SetFilletLengths(self, sizes: JointExitBuilder.FilletSizes) -> None:
        """
         Sets the fillet weld values for the side of the welding joint. 
        """
        pass
    def SetFilletLengthsTag(self, sizes: JointExitBuilder.FilletSizes) -> None:
        """
         Sets the fillet weld values for the side of the welding joint. 
        """
        pass
    def SetOppositeFilletLengths(self, sizes: JointExitBuilder.FilletSizes) -> None:
        """
         Sets the fillet weld values for the opposite side of the welding joint. 
        """
        pass
    def SetOppositeFilletLengthsTag(self, sizes: JointExitBuilder.FilletSizes) -> None:
        """
         Sets the fillet weld values for the opposite side of the welding joint. 
        """
        pass
    def SetRootOpeningTag(self, rootOpening: float) -> None:
        """
         Set the desired gap between bodies being welded 
        """
        pass
    def SetSideTag(self, side: JointExitBuilder.BodySide) -> None:
        """
         Set the side edge preparation values will be applied to 
        """
        pass
    def SetUseCallbackValues(self, useCallbackValues: bool) -> None:
        """
         Set flag if joint is to use callback values. 
        """
        pass
import NXOpen
class JointItemBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[JointItemBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: JointItemBuilder) -> None:
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
    def Erase(self, obj: JointItemBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: JointItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: JointItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> JointItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( JointItemBuilder NXOpe):  object found at input index .
        """
        pass
    def GetContents(self) -> List[JointItemBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( JointItemBuilder List[NXO):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: JointItemBuilder) -> None:
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
    def SetContents(self, objects: List[JointItemBuilder]) -> None:
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
    def Swap(self, object1: JointItemBuilder, object2: JointItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.Die
import NXOpen.GeometricUtilities
import NXOpen.Routing
class JointItemBuilder(NXOpen.TaggedObject): 
    """ Used to create or edit a Weld.WeldJoint feature. """
    @property
    def BackingFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BackingFace
         Returns the backing face.  
             
         
        """
        pass
    @property
    def Curve(self) -> NXOpen.Curve:
        """
        Getter for property: ( NXOpen.Curve) Curve
         Returns the joint curve   
            
         
        """
        pass
    @property
    def Limits(self) -> NXOpen.Die.DieLimitsBuilder:
        """
        Getter for property: ( NXOpen.Die.DieLimitsBuilder) Limits
         Returns the limits of the joint curve span.  
             
         
        """
        pass
    @property
    def MasterEdge(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) MasterEdge
         Returns the master edge of a T-joint weld.  
             
         
        """
        pass
    @property
    def PlacementFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) PlacementFace
         Returns the placement face of a T-joint weld.  
           For example, on a profile it is the face that touches the plate.   
         
        """
        pass
    @property
    def PrimaryEdge(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) PrimaryEdge
         Returns the primary edge of a butt weld.  
             
         
        """
        pass
    @property
    def PrimaryFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) PrimaryFace
         Returns the primary face of a butt weld.  
             
         
        """
        pass
    @property
    def RoutingObject(self) -> NXOpen.Routing.SelectPort:
        """
        Getter for property: ( NXOpen.Routing.SelectPort) RoutingObject
         Returns the routing port.  
             
         
        """
        pass
    @property
    def SecondaryEdge(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SecondaryEdge
         Returns the secondary edge of a butt weld.  
             
         
        """
        pass
    @property
    def SecondaryFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SecondaryFace
         Returns the secondary face of a butt weld.  
             
         
        """
        pass
    @property
    def TargetFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) TargetFace
         Returns the target face of a T-joint weld.  
            For example, the plate face that the profile lies on.   
         
        """
        pass
    @property
    def UseCallbackValues(self) -> bool:
        """
        Getter for property: (bool) UseCallbackValues
         Returns the indication to use the values of the callback to define the joint   
            
         
        """
        pass
    @UseCallbackValues.setter
    def UseCallbackValues(self, status: bool):
        """
        Setter for property: (bool) UseCallbackValues
         Returns the indication to use the values of the callback to define the joint   
            
         
        """
        pass
    @property
    def WeldType(self) -> int:
        """
        Getter for property: (int) WeldType
         Returns the weld type   
            
         
        """
        pass
    @WeldType.setter
    def WeldType(self, type: int):
        """
        Setter for property: (int) WeldType
         Returns the weld type   
            
         
        """
        pass
    @property
    def WeldingCharacteristics(self) -> CharacteristicsBuilder:
        """
        Getter for property: ( CharacteristicsBuilder NXOpe) WeldingCharacteristics
         Returns the collection of welding characteristics defined by attributes.  
             
         
        """
        pass
    def DeleteCurve(self) -> None:
        """
         Deletes the joint curve from the builder. 
        """
        pass
    def GetPortEngagement(self) -> float:
        """
         Returns the engagement distance of the parent port of the pipe joint 
         Returns engagement (float):  Engagement distance .
        """
        pass
    def ReadEdgePrepValues(self) -> EdgePrepValuesBuilder:
        """
         Read edge prep values set by the user plugin function. 
         Returns valuesBuilder ( EdgePrepValuesBuilder NXOpe): .
        """
        pass
    def SaveEdgePrepValues(self, valuesBuilder: EdgePrepValuesBuilder) -> None:
        """
         Save edge prep values to the Welding Joint. 
        """
        pass
    def SetCallbackMessage(self, message: str) -> None:
        """
         Sets a message to display after callback processing ends 
        """
        pass
import NXOpen
import NXOpen.Features
class JointmarkBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a NXOpen.Weld.Jointmark builder """
    class ConnectPartTypes(Enum):
        """
        Members Include: 
         |AllUniqueParts|  All unique parts 
         |OnlyOnePart|  Only one part    
         |IgnoreFiltering|  Ignore Filtering 

        """
        AllUniqueParts: int
        OnlyOnePart: int
        IgnoreFiltering: int
        @staticmethod
        def ValueOf(value: int) -> JointmarkBuilder.ConnectPartTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ConnectedPanelTypes(Enum):
        """
        Members Include: 
         |Two| 
         |Three| 
         |Four| 

        """
        Two: int
        Three: int
        Four: int
        @staticmethod
        def ValueOf(value: int) -> JointmarkBuilder.ConnectedPanelTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Method(Enum):
        """
        Members Include: 
         |GuideCurve|  Guide Curve 
         |Mirror|  Mirror      
         |Points|  Points      
         |Translate|  Translate   
         |ExistingPoints|  Existing Points. Only allowed for NXOpen.Weld.PointMark class. 

        """
        GuideCurve: int
        Mirror: int
        Points: int
        Translate: int
        ExistingPoints: int
        @staticmethod
        def ValueOf(value: int) -> JointmarkBuilder.Method:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OrientationMethodTypes(Enum):
        """
        Members Include: 
         |SurfaceNormal|  Surface Normals. 
         |CoordinateSystem|  Use fixed csys instead of surface normals. 

        """
        SurfaceNormal: int
        CoordinateSystem: int
        @staticmethod
        def ValueOf(value: int) -> JointmarkBuilder.OrientationMethodTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ProjectionDirectionOptions(Enum):
        """
        Members Include: 
         |NotSet| 
         |AlongFaceNormal| 
         |PricipalAxis| 
         |X| 
         |Y| 
         |Z| 

        """
        NotSet: int
        AlongFaceNormal: int
        PricipalAxis: int
        X: int
        Y: int
        Z: int
        @staticmethod
        def ValueOf(value: int) -> JointmarkBuilder.ProjectionDirectionOptions:
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
        def ValueOf(value: int) -> JointmarkBuilder.ReferenceSheetTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ReuseMethod(Enum):
        """
        Members Include: 
         |SameConnectingParts| 
         |AnyConnectingParts| 

        """
        SameConnectingParts: int
        AnyConnectingParts: int
        @staticmethod
        def ValueOf(value: int) -> JointmarkBuilder.ReuseMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Associativity(self) -> bool:
        """
        Getter for property: (bool) Associativity
         Returns the automatic update option also known as associativity.  
           If true, the curve representing the Jointmark feature will change its location if the guide curve is updated  
         
        """
        pass
    @Associativity.setter
    def Associativity(self, associativity: bool):
        """
        Setter for property: (bool) Associativity
         Returns the automatic update option also known as associativity.  
           If true, the curve representing the Jointmark feature will change its location if the guide curve is updated  
         
        """
        pass
    @property
    def Characteristics(self) -> CharacteristicsBuilder:
        """
        Getter for property: ( CharacteristicsBuilder NXOpe) Characteristics
         Returns the characteristics   
            
         
        """
        pass
    @property
    def ConnectPart(self) -> bool:
        """
        Getter for property: (bool) ConnectPart
         Returns the option of connecting only one part.  
           If true, Jointmark feature is created on a single component.    
         
        """
        pass
    @ConnectPart.setter
    def ConnectPart(self, connectPart: bool):
        """
        Setter for property: (bool) ConnectPart
         Returns the option of connecting only one part.  
           If true, Jointmark feature is created on a single component.    
         
        """
        pass
    @property
    def ConnectPartType(self) -> JointmarkBuilder.ConnectPartTypes:
        """
        Getter for property: ( JointmarkBuilder.ConnectPartTypes NXOpe) ConnectPartType
         Returns the option of connecting only one part.  
           If true, Jointmark feature is created on a single component.    
         
        """
        pass
    @ConnectPartType.setter
    def ConnectPartType(self, connectPart: JointmarkBuilder.ConnectPartTypes):
        """
        Setter for property: ( JointmarkBuilder.ConnectPartTypes NXOpe) ConnectPartType
         Returns the option of connecting only one part.  
           If true, Jointmark feature is created on a single component.    
         
        """
        pass
    @property
    def ConnectedPanelType(self) -> JointmarkBuilder.ConnectedPanelTypes:
        """
        Getter for property: ( JointmarkBuilder.ConnectedPanelTypes NXOpe) ConnectedPanelType
         Returns the number of connected panels at a point.  
           This is used when the construction method is Existing Points   
         
        """
        pass
    @ConnectedPanelType.setter
    def ConnectedPanelType(self, method: JointmarkBuilder.ConnectedPanelTypes):
        """
        Setter for property: ( JointmarkBuilder.ConnectedPanelTypes NXOpe) ConnectedPanelType
         Returns the number of connected panels at a point.  
           This is used when the construction method is Existing Points   
         
        """
        pass
    @property
    def ConstructionMethod(self) -> JointmarkBuilder.Method:
        """
        Getter for property: ( JointmarkBuilder.Method NXOpe) ConstructionMethod
         Returns the construction method for creating Jointmark   
            
         
        """
        pass
    @ConstructionMethod.setter
    def ConstructionMethod(self, method: JointmarkBuilder.Method):
        """
        Setter for property: ( JointmarkBuilder.Method NXOpe) ConstructionMethod
         Returns the construction method for creating Jointmark   
            
         
        """
        pass
    @property
    def CreateSingleFeatures(self) -> bool:
        """
        Getter for property: (bool) CreateSingleFeatures
         Returns the control option to determine if individual features should be created.  
           Only allowed for  NXOpen::Weld::PointMark  class.   
         
        """
        pass
    @CreateSingleFeatures.setter
    def CreateSingleFeatures(self, createSingleFeatures: bool):
        """
        Setter for property: (bool) CreateSingleFeatures
         Returns the control option to determine if individual features should be created.  
           Only allowed for  NXOpen::Weld::PointMark  class.   
         
        """
        pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance   
            
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance   
            
         
        """
        pass
    @property
    def FaceSetsList(self) -> JointmarkFaceSetsBuilderList:
        """
        Getter for property: ( JointmarkFaceSetsBuilderList NXOpe) FaceSetsList
         Returns the list of face sets    
            
         
        """
        pass
    @property
    def FixedCsys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) FixedCsys
         Returns the fixed csys that overrides the default Csys orientation.  
             
         
        """
        pass
    @FixedCsys.setter
    def FixedCsys(self, fixedCsys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) FixedCsys
         Returns the fixed csys that overrides the default Csys orientation.  
             
         
        """
        pass
    @property
    def GuideCurvesList(self) -> JointmarkGuideBuilderList:
        """
        Getter for property: ( JointmarkGuideBuilderList NXOpe) GuideCurvesList
         Returns the list of guide curves   
            
         
        """
        pass
    @property
    def NotifyIfParentPointMoved(self) -> bool:
        """
        Getter for property: (bool) NotifyIfParentPointMoved
         Returns the option to indicate if an alert should be issued when the parent point moves.  
            Valid when using  NXOpen::Weld::JointmarkBuilder::MethodExistingPoints  and associativity is off.   
         
        """
        pass
    @NotifyIfParentPointMoved.setter
    def NotifyIfParentPointMoved(self, notifyIfParentPointMoved: bool):
        """
        Setter for property: (bool) NotifyIfParentPointMoved
         Returns the option to indicate if an alert should be issued when the parent point moves.  
            Valid when using  NXOpen::Weld::JointmarkBuilder::MethodExistingPoints  and associativity is off.   
         
        """
        pass
    @property
    def OrientationMethod(self) -> JointmarkBuilder.OrientationMethodTypes:
        """
        Getter for property: ( JointmarkBuilder.OrientationMethodTypes NXOpe) OrientationMethod
         Returns the orientation method for defining a csys   
            
         
        """
        pass
    @OrientationMethod.setter
    def OrientationMethod(self, orientationMethod: JointmarkBuilder.OrientationMethodTypes):
        """
        Setter for property: ( JointmarkBuilder.OrientationMethodTypes NXOpe) OrientationMethod
         Returns the orientation method for defining a csys   
            
         
        """
        pass
    @property
    def Plane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) Plane
         Returns the plane used for mirror  
            
         
        """
        pass
    @Plane.setter
    def Plane(self, plane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) Plane
         Returns the plane used for mirror  
            
         
        """
        pass
    @property
    def PointList(self) -> JointmarkPointsBuilderList:
        """
        Getter for property: ( JointmarkPointsBuilderList NXOpe) PointList
         Returns the list of points  
            
         
        """
        pass
    @property
    def ProjectionDirectionOption(self) -> JointmarkBuilder.ProjectionDirectionOptions:
        """
        Getter for property: ( JointmarkBuilder.ProjectionDirectionOptions NXOpe) ProjectionDirectionOption
         Returns the projection direction option used to project  NXOpen::Weld::JointmarkBuilder::SelectPointsObject  onto the  NXOpen::Weld::JointmarkBuilder::GetReferenceSheet .  
             
         
        """
        pass
    @ProjectionDirectionOption.setter
    def ProjectionDirectionOption(self, projectionOption: JointmarkBuilder.ProjectionDirectionOptions):
        """
        Setter for property: ( JointmarkBuilder.ProjectionDirectionOptions NXOpe) ProjectionDirectionOption
         Returns the projection direction option used to project  NXOpen::Weld::JointmarkBuilder::SelectPointsObject  onto the  NXOpen::Weld::JointmarkBuilder::GetReferenceSheet .  
             
         
        """
        pass
    @property
    def ReferenceSheetType(self) -> JointmarkBuilder.ReferenceSheetTypes:
        """
        Getter for property: ( JointmarkBuilder.ReferenceSheetTypes NXOpe) ReferenceSheetType
         Returns the type of reference sheet  
            
         
        """
        pass
    @ReferenceSheetType.setter
    def ReferenceSheetType(self, refSheet: JointmarkBuilder.ReferenceSheetTypes):
        """
        Setter for property: ( JointmarkBuilder.ReferenceSheetTypes NXOpe) ReferenceSheetType
         Returns the type of reference sheet  
            
         
        """
        pass
    @property
    def ReuseFeatures(self) -> NXOpen.Features.SelectFeatureList:
        """
        Getter for property: ( NXOpen.Features.SelectFeatureList) ReuseFeatures
         Returns the selected reuse features   
            
         
        """
        pass
    @property
    def ReuseFeaturesMethod(self) -> JointmarkBuilder.ReuseMethod:
        """
        Getter for property: ( JointmarkBuilder.ReuseMethod NXOpe) ReuseFeaturesMethod
         Returns the method used to infer feature parameters if all connected parts are the same, or skip inferring due to connected parts being different.  
             
         
        """
        pass
    @ReuseFeaturesMethod.setter
    def ReuseFeaturesMethod(self, reuseMethod: JointmarkBuilder.ReuseMethod):
        """
        Setter for property: ( JointmarkBuilder.ReuseMethod NXOpe) ReuseFeaturesMethod
         Returns the method used to infer feature parameters if all connected parts are the same, or skip inferring due to connected parts being different.  
             
         
        """
        pass
    @property
    def SelectMirrorObject(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) SelectMirrorObject
         Returns the selected objects for mirror.  
           These objects can be features or curves representing Jointmark   
         
        """
        pass
    @property
    def SelectPointsObject(self) -> NXOpen.SelectPointList:
        """
        Getter for property: ( NXOpen.SelectPointList) SelectPointsObject
         Returns the selected objects for Points   
            
         
        """
        pass
    @property
    def SelectTranslateObject(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) SelectTranslateObject
         Returns the selected objects to translate.  
           These objects can be features or curves representing Jointmark   
         
        """
        pass
    @property
    def ShowWorkCsys(self) -> bool:
        """
        Getter for property: (bool) ShowWorkCsys
         Returns the option to control if the work coordinate system should be showing.  
             
         
        """
        pass
    @ShowWorkCsys.setter
    def ShowWorkCsys(self, showWorkCsys: bool):
        """
        Setter for property: (bool) ShowWorkCsys
         Returns the option to control if the work coordinate system should be showing.  
             
         
        """
        pass
    @property
    def TranslateCsys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) TranslateCsys
         Returns the coordinate system that defines the translate offset directions.  
           If not specified the absolute csys will be used.  
         
        """
        pass
    @TranslateCsys.setter
    def TranslateCsys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) TranslateCsys
         Returns the coordinate system that defines the translate offset directions.  
           If not specified the absolute csys will be used.  
         
        """
        pass
    @property
    def TranslateX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TranslateX
         Returns the expression containing the value of the x translation distance.  
             
         
        """
        pass
    @property
    def TranslateY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TranslateY
         Returns the expression containing the value of the y translation distance.  
             
         
        """
        pass
    @property
    def TranslateZ(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TranslateZ
         Returns the expression containing the value of the z translation distance.  
             
         
        """
        pass
    @property
    def Vector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) Vector
         Returns the vector which points to Y axis   
            
         
        """
        pass
    @Vector.setter
    def Vector(self, vector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) Vector
         Returns the vector which points to Y axis   
            
         
        """
        pass
    def AppendPoints(self, mode: bool, curve: NXOpen.Curve) -> None:
        """
         Creates a list of points on the overlap sheet. In addition, a curve selected by the user will be placed at these points. 
        """
        pass
    def AskConnectedFaces(self) -> ConnectedPart:
        """
                Find the connected face information. 
                
                The data is stored in NXOpen.Weld.ConnectedPart containing the appropriate
                connected part face occurrence information. 
                 
         Returns data ( ConnectedPart NXOpe):  Connected face information.  if none are found. .
        """
        pass
    def CreateReferenceData(self) -> None:
        """
         Create a temporary overlap or top sheet and guide curve. Use with independent NXOpen.Weld.PointMarkPoint features. 
        """
        pass
    def CreateSymbolCurve(self, path: str, name: str) -> NXOpen.Curve:
        """
         Create curve From PMI symbol 
         Returns curve ( NXOpen.Curve):  Curve from symbol .
        """
        pass
    def DeleteReferenceData(self) -> None:
        """
         Delete temporary overlap or top sheet feature. Use with independent NXOpen.Weld.PointMarkPoint features. 
        """
        pass
    def FromReuseFeatures(self) -> Tuple[bool, bool, bool]:
        """
         Initializes face sets, guide curve, and points builders from reuse features.  
         Returns A tuple consisting of (faceSetsUpdated, guideCurvesUpdated, pointSelectionUpdated). 
         - faceSetsUpdated is: bool. Indicates if the face set list was updated. .
         - guideCurvesUpdated is: bool. Indicates if the guide curve list was updated. .
         - pointSelectionUpdated is: bool. Indicates if point selection object was updated. .

        """
        pass
    def GetCreateReferenceDataMessages(self) -> List[str]:
        """
         Get all the messages created by NXOpen.Weld.JointmarkBuilder.CreateReferenceData. 
         Returns messages (List[str]):  The array of messages generated during the process of discovering the reference data. .
        """
        pass
    def GetReferenceSheet(self) -> NXOpen.Features.Feature:
        """
         Returns the Reference Sheet feature
         Returns sheet ( NXOpen.Features.Feature): .
        """
        pass
    def GetSelectedReferences(self) -> List[NXOpen.NXObject]:
        """
         Gets the selected points, or point features, references. Does not apply to the guide curves method. 
         Returns references ( NXOpen.NXObject Li): The array of references. These may be points or point features. .
        """
        pass
    def GetSheetEdges(self) -> List[NXOpen.Edge]:
        """
         Edges of created sheet 
         Returns edges ( NXOpen.Edge Li): .
        """
        pass
    def MapFeaturesToPoints(self) -> None:
        """
         Maps the selected reuse features to the new preview point locations. 
        """
        pass
    def MoveReferenceSheet(self) -> None:
        """
         Move the Reference Sheet to work layer, and unlink from grouping feature. 
        """
        pass
    def NewFaceSets(self) -> JointmarkFaceSetsBuilder:
        """
         Creates a NXOpen.Weld.JointmarkFaceSetsBuilder object. 
         Returns newfaceSetsBuilder ( JointmarkFaceSetsBuilder NXOpe): .
        """
        pass
    def NewGuide(self) -> JointmarkGuideBuilder:
        """
         Creates a NXOpen.Weld.JointmarkGuideBuilder object. 
         Returns newGuideBuilder ( JointmarkGuideBuilder NXOpe): .
        """
        pass
    def NewPoints(self) -> JointmarkPointsBuilder:
        """
         Creates a NXOpen.Weld.JointmarkPointsBuilder object. 
         Returns newPointsBuilder ( JointmarkPointsBuilder NXOpe): .
        """
        pass
    def RediscoverFaces(self) -> None:
        """
         Use the Weld Assistant Connected Face Finder command to rediscover faces based on the current feature point positions. 
        """
        pass
    def SetDisplayCsys(self, status: bool) -> None:
        """
         Indicates whether the csys should be displayed on creation 
        """
        pass
    def SetShowThruState(self, status: bool) -> None:
        """
         Indicates whether the output objects should show thru on creation 
        """
        pass
    def UpdateFeatures(self) -> None:
        """
         Updates all the items on the points list based on the construction method and related inputs. 
        """
        pass
    def UpdatePoint(self) -> None:
        """
         Updates the selected point by projecting it to the guide curve. 
        """
        pass
    def UpdateReferenceSheet(self, facesModified: bool) -> NXOpen.Features.Feature:
        """
         Prepares a Reference Sheet for placing Jointmark features. If the sheet is suppressed, it will be unsuppressed. 
         Returns sheet ( NXOpen.Features.Feature): .
        """
        pass
import NXOpen.Features
class JointmarkElement(NXOpen.Features.Feature): 
    """ Represents a Weld.JointmarkElement Feature. """
    pass
import NXOpen
class JointmarkFaceSetsBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[JointmarkFaceSetsBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: JointmarkFaceSetsBuilder) -> None:
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
    def Erase(self, obj: JointmarkFaceSetsBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: JointmarkFaceSetsBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: JointmarkFaceSetsBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> JointmarkFaceSetsBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( JointmarkFaceSetsBuilder NXOpe):  object found at input index .
        """
        pass
    def GetContents(self) -> List[JointmarkFaceSetsBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( JointmarkFaceSetsBuilder List[NXO):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: JointmarkFaceSetsBuilder) -> None:
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
    def SetContents(self, objects: List[JointmarkFaceSetsBuilder]) -> None:
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
    def Swap(self, object1: JointmarkFaceSetsBuilder, object2: JointmarkFaceSetsBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class JointmarkFaceSetsBuilder(NXOpen.TaggedObject): 
    """ Used to create or edit a set of faces for Jointmark """
    @property
    def FaceSelect(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FaceSelect
         Returns the selected face collector   
            
         
        """
        pass
import NXOpen
class JointmarkGuideBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[JointmarkGuideBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: JointmarkGuideBuilder) -> None:
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
    def Erase(self, obj: JointmarkGuideBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: JointmarkGuideBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: JointmarkGuideBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> JointmarkGuideBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( JointmarkGuideBuilder NXOpe):  object found at input index .
        """
        pass
    def GetContents(self) -> List[JointmarkGuideBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( JointmarkGuideBuilder List[NXO):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: JointmarkGuideBuilder) -> None:
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
    def SetContents(self, objects: List[JointmarkGuideBuilder]) -> None:
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
    def Swap(self, object1: JointmarkGuideBuilder, object2: JointmarkGuideBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class JointmarkGuideBuilder(NXOpen.TaggedObject): 
    """ Used to create or edit a guide curve for Jointmark. """
    class Location(Enum):
        """
        Members Include: 
         |CenterLine|  Centerline 
         |OffsetFromEdge|  Offset from Edge 
         |ExistingCurve|  Existing Curve 

        """
        CenterLine: int
        OffsetFromEdge: int
        ExistingCurve: int
        @staticmethod
        def ValueOf(value: int) -> JointmarkGuideBuilder.Location:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
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
        def ValueOf(value: int) -> JointmarkGuideBuilder.SpaceMethod:
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
        def ValueOf(value: int) -> JointmarkGuideBuilder.SpaceOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
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
    def ExtendOffset(self) -> bool:
        """
        Getter for property: (bool) ExtendOffset
         Returns the extend offset.  
             
         
        """
        pass
    @ExtendOffset.setter
    def ExtendOffset(self, extendOffset: bool):
        """
        Setter for property: (bool) ExtendOffset
         Returns the extend offset.  
             
         
        """
        pass
    @property
    def GuideCurve(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) GuideCurve
         Returns the guide curve.  
             
         
        """
        pass
    @GuideCurve.setter
    def GuideCurve(self, guide: NXOpen.Section):
        """
        Setter for property: ( NXOpen.Section) GuideCurve
         Returns the guide curve.  
             
         
        """
        pass
    @property
    def LocationOption(self) -> JointmarkGuideBuilder.Location:
        """
        Getter for property: ( JointmarkGuideBuilder.Location NXOpe) LocationOption
         Returns the location option.  
             
         
        """
        pass
    @LocationOption.setter
    def LocationOption(self, locationOption: JointmarkGuideBuilder.Location):
        """
        Setter for property: ( JointmarkGuideBuilder.Location NXOpe) LocationOption
         Returns the location option.  
             
         
        """
        pass
    @property
    def NumberOfPoints(self) -> int:
        """
        Getter for property: (int) NumberOfPoints
         Returns the number to determine the points along the guide curve.  
             
         
        """
        pass
    @NumberOfPoints.setter
    def NumberOfPoints(self, number: int):
        """
        Setter for property: (int) NumberOfPoints
         Returns the number to determine the points along the guide curve.  
             
         
        """
        pass
    @property
    def OffsetDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OffsetDistance
         Returns the offset distance.  
             
         
        """
        pass
    @property
    def RespacePoints(self) -> bool:
        """
        Getter for property: (bool) RespacePoints
         Returns the option to control whether new points should be added when the feature is edited.  
            If true new points can to be added, otherwise no new points will be added.   
         
        """
        pass
    @RespacePoints.setter
    def RespacePoints(self, respacePoints: bool):
        """
        Setter for property: (bool) RespacePoints
         Returns the option to control whether new points should be added when the feature is edited.  
            If true new points can to be added, otherwise no new points will be added.   
         
        """
        pass
    @property
    def ReverseDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseDirection
         Returns the reversal status of Guide Curve direction.  
             
         
        """
        pass
    @ReverseDirection.setter
    def ReverseDirection(self, reverse: bool):
        """
        Setter for property: (bool) ReverseDirection
         Returns the reversal status of Guide Curve direction.  
             
         
        """
        pass
    @property
    def Section1(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Section1
         Returns the first section used in Centerline.  
             
         
        """
        pass
    @property
    def Section2(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Section2
         Returns the second section used in Centerline.  
             
         
        """
        pass
    @property
    def Section3(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Section3
         Returns the third section used in Offset from Edge.  
             
         
        """
        pass
    @property
    def Section4(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Section4
         Returns the fourth section used in Existing Curve.  
             
         
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
    def SpacingMethod(self) -> JointmarkGuideBuilder.SpaceMethod:
        """
        Getter for property: ( JointmarkGuideBuilder.SpaceMethod NXOpe) SpacingMethod
         Returns the spacing method.  
             
         
        """
        pass
    @SpacingMethod.setter
    def SpacingMethod(self, spacingMethod: JointmarkGuideBuilder.SpaceMethod):
        """
        Setter for property: ( JointmarkGuideBuilder.SpaceMethod NXOpe) SpacingMethod
         Returns the spacing method.  
             
         
        """
        pass
    @property
    def SpacingOption(self) -> JointmarkGuideBuilder.SpaceOption:
        """
        Getter for property: ( JointmarkGuideBuilder.SpaceOption NXOpe) SpacingOption
         Returns the spacing option.  
             
         
        """
        pass
    @SpacingOption.setter
    def SpacingOption(self, spacingOption: JointmarkGuideBuilder.SpaceOption):
        """
        Setter for property: ( JointmarkGuideBuilder.SpaceOption NXOpe) SpacingOption
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
    def CreateGuideCurves(self) -> None:
        """
         Creates the guide curves. 
        """
        pass
    def GetGuideCurves(self) -> Tuple[List[NXOpen.ICurve], List[NXOpen.NXObject]]:
        """
         Gets the created curves curves. The guide curves need to exist before calling this, or nothing will be returned. 
         Returns A tuple consisting of (guideCurves, instanceGuideCurves). 
         - guideCurves is:  NXOpen.ICurve Li.The array of curves.
         - instanceGuideCurves is:  NXOpen.NXObject Li.The array of component curve instances. If there is not an assembly, then this will match the prototype curve. .

        """
        pass
    def RediscoverGuideEnds(self) -> None:
        """
         Use the specified reuse features to set the start and end distance for the guide curve. 
        """
        pass
import NXOpen
class JointmarkPointsBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[JointmarkPointsBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: JointmarkPointsBuilder) -> None:
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
    def Erase(self, obj: JointmarkPointsBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: JointmarkPointsBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: JointmarkPointsBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> JointmarkPointsBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( JointmarkPointsBuilder NXOpe):  object found at input index .
        """
        pass
    def GetContents(self) -> List[JointmarkPointsBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( JointmarkPointsBuilder List[NXO):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: JointmarkPointsBuilder) -> None:
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
    def SetContents(self, objects: List[JointmarkPointsBuilder]) -> None:
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
    def Swap(self, object1: JointmarkPointsBuilder, object2: JointmarkPointsBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
class JointmarkPointsBuilder(NXOpen.TaggedObject): 
    """ Used to create or edit a point in the list of points for Jointmark """
    class PointPosition(Enum):
        """
        Members Include: 
         |NotSet|  None specifed. 
         |MovedAlongGuide|  User moved point from default location along the guide curve 
         |MovedOffGuide|  User moved point from default location off the guide curve 

        """
        NotSet: int
        MovedAlongGuide: int
        MovedOffGuide: int
        @staticmethod
        def ValueOf(value: int) -> JointmarkPointsBuilder.PointPosition:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Angle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Angle
         Returns  the angle through which X and Y axis to rotate   
            
         
        """
        pass
    @property
    def FlipDirection(self) -> bool:
        """
        Getter for property: (bool) FlipDirection
         Returns the flip of  Z axis.  
           Z axis representing the normal can be flipped   
         
        """
        pass
    @FlipDirection.setter
    def FlipDirection(self, flip: bool):
        """
        Setter for property: (bool) FlipDirection
         Returns the flip of  Z axis.  
           Z axis representing the normal can be flipped   
         
        """
        pass
    @property
    def MappingFeature(self) -> NXOpen.Features.SelectFeature:
        """
        Getter for property: ( NXOpen.Features.SelectFeature) MappingFeature
         Returns the selected feature to move to the location specified.  
             
         
        """
        pass
    @property
    def Point(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Point
         Returns the point  at which the feature is created   
            
         
        """
        pass
    @Point.setter
    def Point(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Point
         Returns the point  at which the feature is created   
            
         
        """
        pass
    def UpdateCsys(self, matrix: NXOpen.Matrix3x3) -> None:
        """
         Update the csys using a new matrix. 
        """
        pass
import NXOpen.Features
class Jointmark(NXOpen.Features.Feature): 
    """ Represents a Weld Jointmark Feature. """
    pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Features
class LocatorReferenceBuilder(NXOpen.Builder): 
    """
        This class is used by "Locator Reference" to add the additional component for a weld datum DF.
        When commit is called, the selected additional components will be added to weld datum parms.
    """
    @property
    def AdditionalReferences(self) -> NXOpen.Assemblies.SelectComponentList:
        """
        Getter for property: ( NXOpen.Assemblies.SelectComponentList) AdditionalReferences
         Returns the additional references   
            
         
        """
        pass
    @property
    def SelectLocator(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SelectLocator
         Returns the selecte locator   
            
         
        """
        pass
    def SetAdditionalReferenceFromFeature(self, additionalReference: NXOpen.Features.Feature) -> None:
        """
         Set additional references.  Use to set additional references from feature. 
        """
        pass
class LogInfo:
    """
     Represents entity and its log message 
    """
    @property
    def Entity(self) -> NXOpen.TaggedObject:
        """
        Getter for property Entity
        weld object

        """
        pass
    @Entity.setter
    def Entity(self, value: NXOpen.TaggedObject):
        """
        Getter for property Entity
        weld object
        Setter for property Entity
        weld object

        """
        pass
    @property
    def LogMessage(self) -> str:
        """
        Getter for property LogMessage
        log message

        """
        pass
    @LogMessage.setter
    def LogMessage(self, value: str):
        """
        Getter for property LogMessage
        log message
        Setter for property LogMessage
        log message

        """
        pass
class MeasureHemBuilder(MeasureTrimBuilder): 
    """ Used to create or edit a NXOpen.Weld.MeasureHem feature. """
    class HemMethodTypes(Enum):
        """
        Members Include: 
         |MidPoint|  Use the mid point of a section cut. 
         |NormalToBody|  Use Normal to Body Method. 

        """
        MidPoint: int
        NormalToBody: int
        @staticmethod
        def ValueOf(value: int) -> MeasureHemBuilder.HemMethodTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def HemMethod(self) -> MeasureHemBuilder.HemMethodTypes:
        """
        Getter for property: ( MeasureHemBuilder.HemMethodTypes NXOpe) HemMethod
         Returns the method for calculating the Hem location.  
               
         
        """
        pass
    @HemMethod.setter
    def HemMethod(self, hemMethod: MeasureHemBuilder.HemMethodTypes):
        """
        Setter for property: ( MeasureHemBuilder.HemMethodTypes NXOpe) HemMethod
         Returns the method for calculating the Hem location.  
               
         
        """
        pass
import NXOpen.Features
class MeasureHem(NXOpen.Features.Feature): 
    """ Represents a Weld Measure Hem feature """
    pass
class MeasureHoleBuilder(DatumPinBuilder): 
    """ Used to create or edit a NXOpen.Weld.MeasureHole feature. """
    pass
import NXOpen.Features
class MeasureHole(NXOpen.Features.Feature): 
    """ Represents a Weld Measure Hole feature """
    pass
class MeasureSurfaceBuilder(DatumSurfaceBuilder): 
    """ Used to create or edit a NXOpen.Weld.MeasureSurface feature. """
    @property
    def CustomArrowLength(self) -> float:
        """
        Getter for property: (float) CustomArrowLength
         Returns the length of the solid arrow staff.  
               
         
        """
        pass
    @CustomArrowLength.setter
    def CustomArrowLength(self, customArrowLength: float):
        """
        Setter for property: (float) CustomArrowLength
         Returns the length of the solid arrow staff.  
               
         
        """
        pass
    @property
    def CustomArrowWidth(self) -> float:
        """
        Getter for property: (float) CustomArrowWidth
         Returns the width of the solid arrowhead.  
               
         
        """
        pass
    @CustomArrowWidth.setter
    def CustomArrowWidth(self, customArrowWidth: float):
        """
        Setter for property: (float) CustomArrowWidth
         Returns the width of the solid arrowhead.  
               
         
        """
        pass
import NXOpen.Features
class MeasureSurface(NXOpen.Features.Feature): 
    """ Represents a Weld Measure Surface feature """
    pass
class MeasureTrimBuilder(DatumEdgeBuilder): 
    """ Used to create or edit a NXOpen.Weld.MeasureTrim feature. """
    pass
import NXOpen.Features
class MeasureTrim(NXOpen.Features.Feature): 
    """ Represents a Weld Measure Trim feature """
    pass
class OutputType(Enum):
    """
    Members Include: 
     |Associative|  output data will be associated to inputs. If inputs change the outputs will change also 
     |Fixed|  output data will not change if inputs change  

    """
    Associative: int
    Fixed: int
    @staticmethod
    def ValueOf(value: int) -> OutputType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.Features
class PlugSlotBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a NXOpen.Weld.PlugSlot builder """
    class ArcProcessEnum(Enum):
        """
        Members Include: 
         |Gmaw| 
         |Gtaw| 
         |Gtac| 
         |Smaw| 
         |Paw| 

        """
        Gmaw: int
        Gtaw: int
        Gtac: int
        Smaw: int
        Paw: int
        @staticmethod
        def ValueOf(value: int) -> PlugSlotBuilder.ArcProcessEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EnumContour(Enum):
        """
        Members Include: 
         |NotSet| 
         |Convex| 
         |Flush| 
         |Concave| 

        """
        NotSet: int
        Convex: int
        Flush: int
        Concave: int
        @staticmethod
        def ValueOf(value: int) -> PlugSlotBuilder.EnumContour:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AssignWeldPMI(self) -> bool:
        """
        Getter for property: (bool) AssignWeldPMI
         Returns the assign weld pmi   
            
         
        """
        pass
    @AssignWeldPMI.setter
    def AssignWeldPMI(self, assignWeldPMI: bool):
        """
        Setter for property: (bool) AssignWeldPMI
         Returns the assign weld pmi   
            
         
        """
        pass
    @property
    def Characteristics(self) -> CharacteristicsBuilder:
        """
        Getter for property: ( CharacteristicsBuilder NXOpe) Characteristics
         Returns the characteristics   
            
         
        """
        pass
    @property
    def ContourDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ContourDepth
         Returns the contour depth   
            
         
        """
        pass
    @property
    def ContourHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ContourHeight
         Returns the contour height needed for cap  
            
         
        """
        pass
    @property
    def ContourType(self) -> PlugSlotBuilder.EnumContour:
        """
        Getter for property: ( PlugSlotBuilder.EnumContour NXOpe) ContourType
         Returns the contour type   
            
         
        """
        pass
    @ContourType.setter
    def ContourType(self, contourType: PlugSlotBuilder.EnumContour):
        """
        Setter for property: ( PlugSlotBuilder.EnumContour NXOpe) ContourType
         Returns the contour type   
            
         
        """
        pass
    @property
    def Edge1(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Edge1
         Returns the edge of the hole or slot on face1   
            
         
        """
        pass
    @property
    def Face1(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Face1
         Returns the face1   
            
         
        """
        pass
    @property
    def Face2(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Face2
         Returns the face2   
            
         
        """
        pass
    @property
    def FieldWeld(self) -> bool:
        """
        Getter for property: (bool) FieldWeld
         Returns the field weld   
            
         
        """
        pass
    @FieldWeld.setter
    def FieldWeld(self, fieldWeld: bool):
        """
        Setter for property: (bool) FieldWeld
         Returns the field weld   
            
         
        """
        pass
    @property
    def SeedFace1(self) -> NXOpen.Face:
        """
        Getter for property: ( NXOpen.Face) SeedFace1
         Returns the top face on face1  
            
         
        """
        pass
    @SeedFace1.setter
    def SeedFace1(self, seedFace1: NXOpen.Face):
        """
        Setter for property: ( NXOpen.Face) SeedFace1
         Returns the top face on face1  
            
         
        """
        pass
    @property
    def SeedFace2(self) -> NXOpen.Face:
        """
        Getter for property: ( NXOpen.Face) SeedFace2
         Returns the bottom face from which the weld will be extruded towards the top  
            
         
        """
        pass
    @SeedFace2.setter
    def SeedFace2(self, seedFace2: NXOpen.Face):
        """
        Setter for property: ( NXOpen.Face) SeedFace2
         Returns the bottom face from which the weld will be extruded towards the top  
            
         
        """
        pass
import NXOpen.Features
class PlugSlot(NXOpen.Features.BodyFeature): 
    """ create a PlugSlot feature for Weld """
    pass
class PointMarkBuilder(JointmarkBuilder): 
    """ Used to create or edit a NXOpen.Weld.PointMark feature. """
    class WeldTypes(Enum):
        """
        Members Include: 
         |ResistanceSpot|  Resistance Spot 
         |ArcSpot|  Arc Spot 
         |Clinch|  Clinch 
         |Dollop|  Dollop 
         |WeldNut|  Weld Nut
         |WeldStud|  Weld Stud 
         |Custom1|  Custom 1 as defined in customer defaults 
         |Custom2|  Custom 2 as defined in customer defaults 
         |Custom3|  Custom 3 as defined in customer defaults 
         |Custom4|  Custom 4 as defined in customer defaults 
         |Custom5|  Custom 5 as defined in customer defaults 

        """
        ResistanceSpot: int
        ArcSpot: int
        Clinch: int
        Dollop: int
        WeldNut: int
        WeldStud: int
        Custom1: int
        Custom2: int
        Custom3: int
        Custom4: int
        Custom5: int
        @staticmethod
        def ValueOf(value: int) -> PointMarkBuilder.WeldTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ShowSolids(self) -> bool:
        """
        Getter for property: (bool) ShowSolids
         Returns the display mode.  
           This is only used on create. On edit the display mode will be that of the latest state of the edited features.   
         
        """
        pass
    @ShowSolids.setter
    def ShowSolids(self, showSolids: bool):
        """
        Setter for property: (bool) ShowSolids
         Returns the display mode.  
           This is only used on create. On edit the display mode will be that of the latest state of the edited features.   
         
        """
        pass
    @property
    def WeldType(self) -> PointMarkBuilder.WeldTypes:
        """
        Getter for property: ( PointMarkBuilder.WeldTypes NXOpe) WeldType
         Returns the weld type references in the customer defaults to create.  
             
         
        """
        pass
    @WeldType.setter
    def WeldType(self, weldType: PointMarkBuilder.WeldTypes):
        """
        Setter for property: ( PointMarkBuilder.WeldTypes NXOpe) WeldType
         Returns the weld type references in the customer defaults to create.  
             
         
        """
        pass
    def AppendPointsOverride(self, create: bool) -> None:
        """
         Creates a list of points on the overlap sheet. In addition, a curve selected by the user will be placed at these points. 
        """
        pass
    def NewPointsOverride(self) -> PointMarkPointBuilder:
        """
         Creates a NXOpen.Weld.PointMarkPointBuilder object. 
         Returns newPointBuilder ( PointMarkPointBuilder NXOpe): .
        """
        pass
class PointMarkPointBuilder(JointmarkPointsBuilder): 
    """ Used to create or edit a point in the list of points for Jointmark """
    pass
import NXOpen.Features
class PointMarkPoint(NXOpen.Features.BodyFeature): 
    """ Represents a Weld.PointMarkPoint Feature. """
    def GetPointMarker(self) -> int:
        """
         Gets the Symbol(Point Marker) information 
         Returns pointMark (int): .
        """
        pass
import NXOpen.Features
class PointMark(NXOpen.Features.Feature): 
    """ Represents a Weld PointMark Feature. """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectDatumEdge(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""
    @property
    def Value(self) -> DatumEdge:
        """
        Getter for property: ( DatumEdge NXOpe) Value
         Returns the object being selected
              
            
         
        """
        pass
    @Value.setter
    def Value(self, selection: DatumEdge):
        """
        Setter for property: ( DatumEdge NXOpe) Value
         Returns the object being selected
              
            
         
        """
        pass
    @overload
    def GetValue(self) -> Tuple[DatumEdge, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         Returns A tuple consisting of (selection, view, point). 
         - selection is:  DatumEdge NXOpe. selected object .
         - view is:  NXOpen.View. selected object view.
         - point is:  NXOpen.Point3d. selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, DatumEdge, NXOpen.View, NXOpen.Point3d, DatumEdge, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         Returns A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is:  NXOpen.InferSnapType.SnapType.  snap point type.
         - selection1 is:  DatumEdge NXOpe. first selected object .
         - view1 is:  NXOpen.View. first selected object view.
         - point1 is:  NXOpen.Point3d. first selected object point.
         - selection2 is:  DatumEdge NXOpe. second selected object .
         - view2 is:  NXOpen.View. second selected object view.
         - point2 is:  NXOpen.Point3d. second selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[DatumEdge, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         Returns A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is:  DatumEdge NXOpe. selected object .
         - cae_sub_type is:  NXOpen.CaeObjectType.CaeSubType. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    @overload
    def SetValue(self, selection: DatumEdge, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: DatumEdge, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: DatumEdge, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
    @overload
    def SetValue(self, selection: DatumEdge, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectDatumPin(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""
    @property
    def Value(self) -> DatumPin:
        """
        Getter for property: ( DatumPin NXOpe) Value
         Returns the object being selected
              
            
         
        """
        pass
    @Value.setter
    def Value(self, selection: DatumPin):
        """
        Setter for property: ( DatumPin NXOpe) Value
         Returns the object being selected
              
            
         
        """
        pass
    @overload
    def GetValue(self) -> Tuple[DatumPin, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         Returns A tuple consisting of (selection, view, point). 
         - selection is:  DatumPin NXOpe. selected object .
         - view is:  NXOpen.View. selected object view.
         - point is:  NXOpen.Point3d. selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, DatumPin, NXOpen.View, NXOpen.Point3d, DatumPin, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         Returns A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is:  NXOpen.InferSnapType.SnapType.  snap point type.
         - selection1 is:  DatumPin NXOpe. first selected object .
         - view1 is:  NXOpen.View. first selected object view.
         - point1 is:  NXOpen.Point3d. first selected object point.
         - selection2 is:  DatumPin NXOpe. second selected object .
         - view2 is:  NXOpen.View. second selected object view.
         - point2 is:  NXOpen.Point3d. second selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[DatumPin, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         Returns A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is:  DatumPin NXOpe. selected object .
         - cae_sub_type is:  NXOpen.CaeObjectType.CaeSubType. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    @overload
    def SetValue(self, selection: DatumPin, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: DatumPin, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: DatumPin, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
    @overload
    def SetValue(self, selection: DatumPin, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectDatumSurface(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""
    @property
    def Value(self) -> DatumSurface:
        """
        Getter for property: ( DatumSurface NXOpe) Value
         Returns the object being selected
              
            
         
        """
        pass
    @Value.setter
    def Value(self, selection: DatumSurface):
        """
        Setter for property: ( DatumSurface NXOpe) Value
         Returns the object being selected
              
            
         
        """
        pass
    @overload
    def GetValue(self) -> Tuple[DatumSurface, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         Returns A tuple consisting of (selection, view, point). 
         - selection is:  DatumSurface NXOpe. selected object .
         - view is:  NXOpen.View. selected object view.
         - point is:  NXOpen.Point3d. selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, DatumSurface, NXOpen.View, NXOpen.Point3d, DatumSurface, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         Returns A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is:  NXOpen.InferSnapType.SnapType.  snap point type.
         - selection1 is:  DatumSurface NXOpe. first selected object .
         - view1 is:  NXOpen.View. first selected object view.
         - point1 is:  NXOpen.Point3d. first selected object point.
         - selection2 is:  DatumSurface NXOpe. second selected object .
         - view2 is:  NXOpen.View. second selected object view.
         - point2 is:  NXOpen.Point3d. second selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[DatumSurface, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         Returns A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is:  DatumSurface NXOpe. selected object .
         - cae_sub_type is:  NXOpen.CaeObjectType.CaeSubType. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    @overload
    def SetValue(self, selection: DatumSurface, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: DatumSurface, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: DatumSurface, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
    @overload
    def SetValue(self, selection: DatumSurface, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
import NXOpen
import NXOpen.Assemblies
class StructureWeldBuilder(NXOpen.Builder): 
    """ This class is used to create or edit the information shared among all Structure Weld builders. """
    def GetCommittedComponents(self) -> List[NXOpen.Assemblies.Component]:
        """
         This method returns the component parts that are created by  Builder.Commit.
                
         Returns objects ( NXOpen.Assemblies.Component Li):  The components created by Commit .
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SurfaceWeldBuilder(StructureWeldBuilder): 
    """
    Use to create or edit a NXOpen.Weld.SurfaceWeld feature.
    """
    class DestinationTypes(Enum):
        """
        Members Include: 
         |WorkPart| 
         |NewComponent| 

        """
        WorkPart: int
        NewComponent: int
        @staticmethod
        def ValueOf(value: int) -> SurfaceWeldBuilder.DestinationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Boundary(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Boundary
         Returns the section defining all the boundaries to use for creating the surface weld.  
           The largest boundary will be treated as the primary exterior boundary.   
         
        """
        pass
    @property
    def Characteristics(self) -> CharacteristicsBuilder:
        """
        Getter for property: ( CharacteristicsBuilder NXOpe) Characteristics
         Returns the characteristics to assign to the object created.  
             
         
        """
        pass
    @property
    def Destination(self) -> SurfaceWeldBuilder.DestinationTypes:
        """
        Getter for property: ( SurfaceWeldBuilder.DestinationTypes NXOpe) Destination
         Returns the option specifying the destination for this surface weld feature.  
           Only applicable during create.   
         
        """
        pass
    @Destination.setter
    def Destination(self, destination: SurfaceWeldBuilder.DestinationTypes):
        """
        Setter for property: ( SurfaceWeldBuilder.DestinationTypes NXOpe) Destination
         Returns the option specifying the destination for this surface weld feature.  
           Only applicable during create.   
         
        """
        pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance for constructing the surface weld.  
           Uses the modeling tolerance during creation.   
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance for constructing the surface weld.  
           Uses the modeling tolerance during creation.   
         
        """
        pass
    @property
    def LineColorFontWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) LineColorFontWidth
         Returns the color, font, and width of the surface weld output curve.  
            
         
        """
        pass
    @property
    def NamePrefix(self) -> str:
        """
        Getter for property: (str) NamePrefix
         Returns the prefix used for the surface weld Design Feature name in Fourth Generation Design mode.  
           Only applicable during create.   
         
        """
        pass
    @NamePrefix.setter
    def NamePrefix(self, prefix: str):
        """
        Setter for property: (str) NamePrefix
         Returns the prefix used for the surface weld Design Feature name in Fourth Generation Design mode.  
           Only applicable during create.   
         
        """
        pass
    @property
    def Panel(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Panel
         Returns the collector containing the faces to create the surface weld on.  
             
         
        """
        pass
    @property
    def ProjectionDirection(self) -> NXOpen.GeometricUtilities.ProjectionOptions:
        """
        Getter for property: ( NXOpen.GeometricUtilities.ProjectionOptions) ProjectionDirection
         Returns the project direction, which is used to project the boundary curves to the plate mold face.  
             
         
        """
        pass
    @property
    def Thickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Thickness
         Returns the expression containing the value of the thickness of the surface weld.  
             
         
        """
        pass
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Width
         Returns the expression containing the value of the width of the surface weld if only the centerline is specified.  
             
         
        """
        pass
import NXOpen.Features
class SurfaceWeld(NXOpen.Features.CurveFeature): 
    """ Represents a surface weld feature """
    pass
import NXOpen
import NXOpen.Features
class TransformBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a NXOpen.Weld.TransformBuilder builder """
    class ConnectedPartMethods(Enum):
        """
        Members Include: 
         |TransformBody|  Use the location of the transform body to help find connected parts 
         |ParentFaces|  Use transformed parent faces to find connected parts 

        """
        TransformBody: int
        ParentFaces: int
        @staticmethod
        def ValueOf(value: int) -> TransformBuilder.ConnectedPartMethods:
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
    def Characteristics(self) -> CharacteristicsBuilder:
        """
        Getter for property: ( CharacteristicsBuilder NXOpe) Characteristics
         Returns the collection of welding characteristics defined by attributes.  
             
         
        """
        pass
    @property
    def ConnectedPartMethod(self) -> TransformBuilder.ConnectedPartMethods:
        """
        Getter for property: ( TransformBuilder.ConnectedPartMethods NXOpe) ConnectedPartMethod
         Returns the method used to find connected parts   
            
         
        """
        pass
    @ConnectedPartMethod.setter
    def ConnectedPartMethod(self, method: TransformBuilder.ConnectedPartMethods):
        """
        Setter for property: ( TransformBuilder.ConnectedPartMethods NXOpe) ConnectedPartMethod
         Returns the method used to find connected parts   
            
         
        """
        pass
    @property
    def ConnectedPartTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ConnectedPartTolerance
         Returns the expression containing the value of the connected part tolerance.  
           This is used to find connected part information for the transformed weld.   
         
        """
        pass
    @property
    def DerivedDatum(self) -> bool:
        """
        Getter for property: (bool) DerivedDatum
         Returns the indication to create a datum feature as derived from the parent   
            
         
        """
        pass
    @DerivedDatum.setter
    def DerivedDatum(self, associative: bool):
        """
        Setter for property: (bool) DerivedDatum
         Returns the indication to create a datum feature as derived from the parent   
            
         
        """
        pass
    @property
    def Features(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Features
         Returns the weld features to transform   
            
         
        """
        pass
    @property
    def MirrorPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) MirrorPlane
         Returns the mirror plane, used when  NXOpen::Weld::TransformBuilder::TransformationTypes  is set to   NXOpen::Weld::TransformBuilder::TransformationTypesMirror     
            
         
        """
        pass
    @MirrorPlane.setter
    def MirrorPlane(self, mirrorPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) MirrorPlane
         Returns the mirror plane, used when  NXOpen::Weld::TransformBuilder::TransformationTypes  is set to   NXOpen::Weld::TransformBuilder::TransformationTypesMirror     
            
         
        """
        pass
    @property
    def TranslateCsys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) TranslateCsys
         Returns the coordinate system that defines the translate offset directions.  
           If not specified the absolute coordinate system will be used.
                    Used when  NXOpen::Weld::TransformBuilder::TransformationTypes  is set to   NXOpen::Weld::TransformBuilder::TransformationTypesTranslate     
         
        """
        pass
    @TranslateCsys.setter
    def TranslateCsys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) TranslateCsys
         Returns the coordinate system that defines the translate offset directions.  
           If not specified the absolute coordinate system will be used.
                    Used when  NXOpen::Weld::TransformBuilder::TransformationTypes  is set to   NXOpen::Weld::TransformBuilder::TransformationTypesTranslate     
         
        """
        pass
    @property
    def TranslateX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TranslateX
         Returns the expression containing the value of the x translation distance.  
           
                    Used when  NXOpen::Weld::TransformBuilder::TransformationTypes  is set to   NXOpen::Weld::TransformBuilder::TransformationTypesTranslate     
         
        """
        pass
    @property
    def TranslateY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TranslateY
         Returns the expression containing the value of the y translation distance.  
             
         
        """
        pass
    @property
    def TranslateZ(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TranslateZ
         Returns the expression containing the value of the z translation distance.  
             
         
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
import NXOpen.Features
class Transform(NXOpen.Features.BodyFeature): 
    """ Represents a Weld Transform Feature. """
    pass
import NXOpen
class UserDefinedWeldBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Weld.UserDefinedWeldBuilder builder. """
    class WeldTypes(Enum):
        """
        Members Include: 
         |Groove|  Groove Weld type. 
         |Fillet|  Fillet Weld type. 
         |PlugSlot|  Plug Slot Weld type. 
         |Bead|  Bead Weld type. 
         |Fill|  Fill Weld type. 

        """
        Groove: int
        Fillet: int
        PlugSlot: int
        Bead: int
        Fill: int
        @staticmethod
        def ValueOf(value: int) -> UserDefinedWeldBuilder.WeldTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AssignWeldPMI(self) -> bool:
        """
        Getter for property: (bool) AssignWeldPMI
         Returns the assign weld pmi.  
             
         
        """
        pass
    @AssignWeldPMI.setter
    def AssignWeldPMI(self, assignWeldPMI: bool):
        """
        Setter for property: (bool) AssignWeldPMI
         Returns the assign weld pmi.  
             
         
        """
        pass
    @property
    def Characteristics(self) -> CharacteristicsBuilder:
        """
        Getter for property: ( CharacteristicsBuilder NXOpe) Characteristics
         Returns the characteristics.  
             
         
        """
        pass
    @property
    def Class4gd(self) -> UserDefinedWeldBuilder.WeldTypes:
        """
        Getter for property: ( UserDefinedWeldBuilder.WeldTypes NXOpe) Class4gd
         Returns the 4GD class option.  
             
         
        """
        pass
    @Class4gd.setter
    def Class4gd(self, assignWeldPMI: UserDefinedWeldBuilder.WeldTypes):
        """
        Setter for property: ( UserDefinedWeldBuilder.WeldTypes NXOpe) Class4gd
         Returns the 4GD class option.  
             
         
        """
        pass
    @property
    def SelectBody(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) SelectBody
         Returns the select body.  
             
         
        """
        pass
    @property
    def SelectConnectParts(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SelectConnectParts
         Returns the select connect parts.  
             
         
        """
        pass
    @property
    def SelectEdge(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) SelectEdge
         Returns the select edge.  
             
         
        """
        pass
import NXOpen.Features
class UserDefinedWeld(NXOpen.Features.BodyFeature): 
    """ Represents a User Defined Weld feature. """
    pass
import NXOpen
class WeldAdvisorBuilder(NXOpen.Builder): 
    """ Represents a weld advisor test """
    def DeleteFeaturesFromResult(self, objects: List[NXOpen.TaggedObject]) -> None:
        """
         Delete the features from the check result 
        """
        pass
    def GetCheckZoneRadius(self, type: WeldAdvisorCustomerDefault) -> float:
        """
         The weld advisor parameter Check Zone Radius 
         Returns face_radius (float):  The weld advisor parameter Check Zone Radius .
        """
        pass
    def GetCheckers(self) -> List[WeldAdvisorCheckerType]:
        """
         Gets the checkers be executed  
         Returns checkers ( WeldAdvisorCheckerType List[NXO):  Checkers to be executed.
        """
        pass
    def GetFailedObjects(self, checker: WeldAdvisorCheckerType) -> Tuple[List[str], List[LogInfo]]:
        """
         The failed results 
         Returns A tuple consisting of (weld_id, weld_objects). 
         - weld_id is: List[str]. weld id.
         - weld_objects is:  LogInfo List[NXO. failed objects.

        """
        pass
    def GetFlangeCheckHeight(self, type: WeldAdvisorCustomerDefault) -> float:
        """
         The weld advisor parameter Flange Check Height 
         Returns flange_height (float):  The weld advisor parameter Flange Check Height .
        """
        pass
    def GetFlangeCheckRadius(self, type: WeldAdvisorCustomerDefault) -> float:
        """
         The weld advisor parameter Flange Check Radius 
         Returns flange_radius (float):  The weld advisor parameter Flange Check Radius .
        """
        pass
    def GetIncludeSealer(self) -> bool:
        """
         The sealer included or not 
         Returns include_sealer (bool):  include sealer .
        """
        pass
    def GetMaximumCsysFaceNormalAngle(self, type: WeldAdvisorCustomerDefault) -> float:
        """
         The weld advisor parameter Maximum CSYS Face Normal Angle 
         Returns csys_face_nml_angle (float):  The weld advisor parameter Maximum CSYS Face Normal Angle .
        """
        pass
    def GetMaximumNumberLoosePanels(self, type: WeldAdvisorCustomerDefault) -> int:
        """
         The weld advisor parameter Maximum Number of Loose Panels 
         Returns max_num_of_loose_panels (int):  The weld advisor parameter Maximum Number of Loose Panels .
        """
        pass
    def GetMaximumPointFaceDistance(self, type: WeldAdvisorCustomerDefault) -> float:
        """
         The weld advisor parameter Maximum Point Face Distance 
         Returns point_face_dist (float):  The weld advisor parameter Maximum Point Face Distance .
        """
        pass
    def GetMaximumStackUpGap(self, type: WeldAdvisorCustomerDefault) -> float:
        """
         The weld advisor parameter Maximum Stack Up Gap 
         Returns max_face_dist (float):  The weld advisor parameter Maximum Stack Up Gap .
        """
        pass
    def GetMaximumTotalMetalThickness(self, type: WeldAdvisorCustomerDefault) -> float:
        """
         The weld advisor parameter Maximum Total Metal Thickness 
         Returns total_metal_thickness (float):  The weld advisor parameter Maximum Total Metal Thickness .
        """
        pass
    def GetMinimumClosedAngle(self, type: WeldAdvisorCustomerDefault) -> float:
        """
         The weld advisor parameter Minimum Closed Angle 
         Returns min_closed_angle (float):  The weld advisor parameter Minimum Closed Angle .
        """
        pass
    def GetMinimumEdgeDistance(self, type: WeldAdvisorCustomerDefault) -> float:
        """
         The weld advisor parameter Minimum Edge Distance 
         Returns min_edge_dist (float):  The weld advisor parameter Minimum Edge Distance .
        """
        pass
    def GetMinimumEdgeDistanceWithSealer(self, type: WeldAdvisorCustomerDefault) -> float:
        """
         The weld advisor parameter Minimum Edge Distance With Sealer 
         Returns min_edge_dist_with_sealer (float):  The weld advisor parameter Minimum Edge Distance With Sealer .
        """
        pass
    def GetMinimumPointDistance(self, type: WeldAdvisorCustomerDefault) -> float:
        """
         The weld advisor parameter Minimum Spacing 
         Returns min_point_dist (float):  The weld advisor parameter Minimum Spacing .
        """
        pass
    def GetObjects(self) -> List[NXOpen.TaggedObject]:
        """
         Gets the objects to be checked 
         Returns objects ( NXOpen.TaggedObject Li):  Objects to be checked.
        """
        pass
    def GetParallelismTolerance(self, type: WeldAdvisorCustomerDefault) -> float:
        """
         The weld advisor parameter Parallelism Tolerance 
         Returns face_parallelism_tolerance (float):  The weld advisor parameter Parallelism Tolerance .
        """
        pass
    def GetPlanarityTolerance(self, type: WeldAdvisorCustomerDefault) -> float:
        """
         The weld advisor parameter Planarity Tolerance 
         Returns face_planarity_tolerance (float):  The weld advisor parameter Planarity Tolerance .
        """
        pass
    def GetReferenceObjects(self, weld_object: NXOpen.TaggedObject, checker: WeldAdvisorCheckerType) -> List[LogInfo]:
        """
         The objects that failed weld objects referenced 
         Returns weld_objects ( LogInfo List[NXO): reference objects.
        """
        pass
    def GetSealerCheckZoneRadius(self, type: WeldAdvisorCustomerDefault) -> float:
        """
         The weld advisor parameter Sealer Check Zone Radius 
         Returns face_radius_with_sealer (float):  The weld advisor parameter Sealer Check Zone Radius .
        """
        pass
    def GetThicknessOuterRatio(self, type: WeldAdvisorCustomerDefault) -> float:
        """
         The weld advisor parameter Thickness Outer Ratio 
         Returns thickness_outer_ratio (float):  The weld advisor parameter Thickness Outer Ratio .
        """
        pass
    def GetThicknessRatio(self, type: WeldAdvisorCustomerDefault) -> float:
        """
         The weld advisor parameter Thickness Ratio 
         Returns thickness_ratio (float):  The weld advisor parameter Thickness Ratio .
        """
        pass
    def InitializeSettings(self) -> None:
        """
         The initialization for settings 
        """
        pass
    def ReportResult(self, file_path: str) -> None:
        """
         The report results to xml file  
        """
        pass
    def SaveResult(self) -> None:
        """
         The save all to part  
        """
        pass
    def SetCheckZoneRadius(self, type: WeldAdvisorCustomerDefault, face_radius: float) -> None:
        """
         The weld advisor parameter Check Zone Radius 
        """
        pass
    def SetCheckers(self, checkers: List[WeldAdvisorCheckerType]) -> None:
        """
         Sets the checkers be executed  
        """
        pass
    def SetFlangeCheckHeight(self, type: WeldAdvisorCustomerDefault, flange_height: float) -> None:
        """
         The weld advisor parameter Flange Check Height 
        """
        pass
    def SetFlangeCheckRadius(self, type: WeldAdvisorCustomerDefault, flange_radius: float) -> None:
        """
         The weld advisor parameter Flange Check Radius 
        """
        pass
    def SetIncludeSealer(self, include_sealer: bool) -> None:
        """
         The sealer included or not 
        """
        pass
    def SetMaximumCsysFaceNormalAngle(self, type: WeldAdvisorCustomerDefault, csys_face_nml_angle: float) -> None:
        """
         The weld advisor parameter Maximum CSYS Face Normal Angle 
        """
        pass
    def SetMaximumNumberLoosePanels(self, type: WeldAdvisorCustomerDefault, max_num_of_loose_panels: int) -> None:
        """
         The weld advisor parameter Maximum Number of Loose Panels 
        """
        pass
    def SetMaximumPointFaceDistance(self, type: WeldAdvisorCustomerDefault, point_face_dist: float) -> None:
        """
         The weld advisor parameter Maximum Point Face Distance 
        """
        pass
    def SetMaximumStackUpGap(self, type: WeldAdvisorCustomerDefault, max_face_dist: float) -> None:
        """
         The weld advisor parameter Maximum Stack Up Gap 
        """
        pass
    def SetMaximumTotalMetalThickness(self, type: WeldAdvisorCustomerDefault, total_metal_thickness: float) -> None:
        """
         The weld advisor parameter Maximum Total Metal Thickness 
        """
        pass
    def SetMinimumClosedAngle(self, type: WeldAdvisorCustomerDefault, min_closed_angle: float) -> None:
        """
         The weld advisor parameter Minimum Closed Angle 
        """
        pass
    def SetMinimumEdgeDistance(self, type: WeldAdvisorCustomerDefault, min_edge_dist: float) -> None:
        """
         The weld advisor parameter Minimum Edge Distance 
        """
        pass
    def SetMinimumEdgeDistanceWithSealer(self, type: WeldAdvisorCustomerDefault, min_edge_dist_with_sealer: float) -> None:
        """
         The weld advisor parameter Minimum Edge Distance With Sealer 
        """
        pass
    def SetMinimumPointDistance(self, type: WeldAdvisorCustomerDefault, min_point_dist: float) -> None:
        """
         The weld advisor parameter Minimum Spacing 
        """
        pass
    def SetObjects(self, objects: List[NXOpen.TaggedObject]) -> None:
        """
         Sets the objects to be checked 
        """
        pass
    def SetParallelismTolerance(self, type: WeldAdvisorCustomerDefault, face_parallelism_tolerance: float) -> None:
        """
         The weld advisor parameter Parallelism Tolerance 
        """
        pass
    def SetPlanarityTolerance(self, type: WeldAdvisorCustomerDefault, face_planarity_tolerance: float) -> None:
        """
         The weld advisor parameter Planarity Tolerance 
        """
        pass
    def SetSealerCheckZoneRadius(self, type: WeldAdvisorCustomerDefault, face_radius_with_sealer: float) -> None:
        """
         The weld advisor parameter Sealer Check Zone Radius 
        """
        pass
    def SetThicknessOuterRatio(self, type: WeldAdvisorCustomerDefault, thickness_outer_ratio: float) -> None:
        """
         The weld advisor parameter Thickness Outer Ratio 
        """
        pass
    def SetThicknessRatio(self, type: WeldAdvisorCustomerDefault, thickness_ratio: float) -> None:
        """
         The weld advisor parameter Thickness Ratio 
        """
        pass
class WeldAdvisorCheckerType(Enum):
    """
    Members Include: 
     |CoincidentPoint|  Mimimum Distance 
     |MinimumPointDistance|  minimum point distance 
     |MinimumEdgeDistance|  minimum edge distance 
     |StackUpGap|  stack up gap 
     |FacePlanarity|  face planarity 
     |FaceParallelism|  face parallelism 
     |PointFaceDistance|  point face distance 
     |CsysFaceNormalAngle|  csys face normal angle 
     |MetalStackUp|  metal stack up 
     |MetalMinimumPointDatumDistance|  minimum point datum distance 
     |MetalMinimumPointMeasurementDistance|  minimum point measurement distance 
     |SpacingPerPanelCombination|  spacing per panel combination 
     |WeldFlange|  weld flange 
     |Bead|  sealer bead
     |Number|  number of checkers 

    """
    CoincidentPoint: int
    MinimumPointDistance: int
    MinimumEdgeDistance: int
    StackUpGap: int
    FacePlanarity: int
    FaceParallelism: int
    PointFaceDistance: int
    CsysFaceNormalAngle: int
    MetalStackUp: int
    MetalMinimumPointDatumDistance: int
    MetalMinimumPointMeasurementDistance: int
    SpacingPerPanelCombination: int
    WeldFlange: int
    Bead: int
    Number: int
    @staticmethod
    def ValueOf(value: int) -> WeldAdvisorCheckerType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class WeldAdvisorCustomerDefault(Enum):
    """
    Members Include: 
     |ResistanceSpot|  Resistance Spot 
     |ArcSpot|  Arc Spot        
     |Clinch|  Clinch          
     |Dollop|  Dollop          
     |WeldNut|  Weld Nut        
     |WeldStud|  Weld Stud       
     |Custom1Point|  Custom1 Point   
     |Custom2Point|  Custom2 Point   
     |Custom3Point|  Custom3 Point   
     |Custom4Point|  Custom4 Point   
     |Custom5Point|  Custom5 Point   
     |Datum|  datum, used for implementing weld advisor parameters 
     |Measurement|  measurement, used for implementing weld advisor parameters 
     |Num|  number of types

    """
    ResistanceSpot: int
    ArcSpot: int
    Clinch: int
    Dollop: int
    WeldNut: int
    WeldStud: int
    Custom1Point: int
    Custom2Point: int
    Custom3Point: int
    Custom4Point: int
    Custom5Point: int
    Datum: int
    Measurement: int
    Num: int
    @staticmethod
    def ValueOf(value: int) -> WeldAdvisorCustomerDefault:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class WeldArcMethod(Enum):
    """
    Members Include: 
     |Continuous|  creates a single solid 
     |Skip|  creates multiple solids 

    """
    Continuous: int
    Skip: int
    @staticmethod
    def ValueOf(value: int) -> WeldArcMethod:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class WeldAttribType(Enum):
    """
    Members Include: 
     |Integer|  integer 
     |Real|  real    
     |Null|  null    
     |String|  stringt 

    """
    Integer: int
    Real: int
    Null: int
    String: int
    @staticmethod
    def ValueOf(value: int) -> WeldAttribType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class WeldBeadBuilder(NXOpen.Builder): 
    """ Used to create or edit a NXOpen.Weld.WeldBead feature. """
    class BeadLocationMethod(Enum):
        """
        Members Include: 
         |SecondaryParts|  on the secondary parts    
         |PrimaryParts|  on the primary parts      
         |InSpace|  in space. No on any parts 

        """
        SecondaryParts: int
        PrimaryParts: int
        InSpace: int
        @staticmethod
        def ValueOf(value: int) -> WeldBeadBuilder.BeadLocationMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FaceInferMethodType(Enum):
        """
        Members Include: 
         |TangentFaces|  use faces tangent to selected faces to create the bead path curve 
         |NotSet|  only use selected faces to create the bead path curve 

        """
        TangentFaces: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> WeldBeadBuilder.FaceInferMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OutputTypes(Enum):
        """
        Members Include: 
         |Fixed|  Bead does not recreate itself on update.    
         |Associative|  Bead follows normal update behaviour. 

        """
        Fixed: int
        Associative: int
        @staticmethod
        def ValueOf(value: int) -> WeldBeadBuilder.OutputTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |Ellipse|  ellipse shape 
         |Tube|  tube shape    
         |Sketch|  sketch shape  
         |Triangle|  triangle shape  
         |Rectangle|  rectangle shape  

        """
        Ellipse: int
        Tube: int
        Sketch: int
        Triangle: int
        Rectangle: int
        @staticmethod
        def ValueOf(value: int) -> WeldBeadBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BeadLocation(self) -> WeldBeadBuilder.BeadLocationMethod:
        """
        Getter for property: ( WeldBeadBuilder.BeadLocationMethod NXOpe) BeadLocation
         Returns the desired bead location.  
             
         
        """
        pass
    @BeadLocation.setter
    def BeadLocation(self, beadLocation: WeldBeadBuilder.BeadLocationMethod):
        """
        Setter for property: ( WeldBeadBuilder.BeadLocationMethod NXOpe) BeadLocation
         Returns the desired bead location.  
             
         
        """
        pass
    @property
    def Characteristics(self) -> CharacteristicsBuilder:
        """
        Getter for property: ( CharacteristicsBuilder NXOpe) Characteristics
         Returns the characteristics to assign to the object created.  
             
         
        """
        pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance for constructing the bead.  
             
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance for constructing the bead.  
             
         
        """
        pass
    @property
    def ExtendToBoundary(self) -> bool:
        """
        Getter for property: (bool) ExtendToBoundary
         Returns the option to control if the bead guide curve should extend to the nearest face boundary.  
              
         
        """
        pass
    @ExtendToBoundary.setter
    def ExtendToBoundary(self, extendToBoundary: bool):
        """
        Setter for property: (bool) ExtendToBoundary
         Returns the option to control if the bead guide curve should extend to the nearest face boundary.  
              
         
        """
        pass
    @property
    def FaceInferMethod(self) -> WeldBeadBuilder.FaceInferMethodType:
        """
        Getter for property: ( WeldBeadBuilder.FaceInferMethodType NXOpe) FaceInferMethod
         Returns the method to use when inferring faces to create the bead guide curve path.  
             
         
        """
        pass
    @FaceInferMethod.setter
    def FaceInferMethod(self, faceInferMethod: WeldBeadBuilder.FaceInferMethodType):
        """
        Setter for property: ( WeldBeadBuilder.FaceInferMethodType NXOpe) FaceInferMethod
         Returns the method to use when inferring faces to create the bead guide curve path.  
             
         
        """
        pass
    @property
    def OutputType(self) -> WeldBeadBuilder.OutputTypes:
        """
        Getter for property: ( WeldBeadBuilder.OutputTypes NXOpe) OutputType
         Returns the output type which controls the update behaviour of the bead feature.  
             
         
        """
        pass
    @OutputType.setter
    def OutputType(self, type: WeldBeadBuilder.OutputTypes):
        """
        Setter for property: ( WeldBeadBuilder.OutputTypes NXOpe) OutputType
         Returns the output type which controls the update behaviour of the bead feature.  
             
         
        """
        pass
    @property
    def PathList(self) -> WeldBeadPathBuilderList:
        """
        Getter for property: ( WeldBeadPathBuilderList NXOpe) PathList
         Returns the list containing the defined path segments.  
             
         
        """
        pass
    @property
    def SelectBottomParts(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SelectBottomParts
         Returns the collector containing the secondary bodies the bead is attached to.  
             
         
        """
        pass
    @property
    def SelectTopParts(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SelectTopParts
         Returns the collector containing the primary bodies the bead is attached to.  
             
         
        """
        pass
    @property
    def SizeList(self) -> WeldBeadSizeBuilderList:
        """
        Getter for property: ( WeldBeadSizeBuilderList NXOpe) SizeList
         Returns the list containing the sizes used to create the bead.  
            
         
        """
        pass
    @property
    def TangentAngle(self) -> float:
        """
        Getter for property: (float) TangentAngle
         Returns the tangent angle used to find faces tangent to the seed face specified.  
             
         
        """
        pass
    @TangentAngle.setter
    def TangentAngle(self, tangentAngle: float):
        """
        Setter for property: (float) TangentAngle
         Returns the tangent angle used to find faces tangent to the seed face specified.  
             
         
        """
        pass
    @property
    def TransformSketchToBeadCenterline(self) -> bool:
        """
        Getter for property: (bool) TransformSketchToBeadCenterline
         Returns the indication whether Sketch On Path is defined in relation to the bead centerline or if it needs to be transformed to be in proper position.  
             
         
        """
        pass
    @TransformSketchToBeadCenterline.setter
    def TransformSketchToBeadCenterline(self, transformSketchToBeadCenterline: bool):
        """
        Setter for property: (bool) TransformSketchToBeadCenterline
         Returns the indication whether Sketch On Path is defined in relation to the bead centerline or if it needs to be transformed to be in proper position.  
             
         
        """
        pass
    @property
    def Type(self) -> WeldBeadBuilder.Types:
        """
        Getter for property: ( WeldBeadBuilder.Types NXOpe) Type
         Returns the shape of the bead to create.  
             
         
        """
        pass
    @Type.setter
    def Type(self, type: WeldBeadBuilder.Types):
        """
        Setter for property: ( WeldBeadBuilder.Types NXOpe) Type
         Returns the shape of the bead to create.  
             
         
        """
        pass
    def CreatePreviewPath(self) -> NXOpen.Spline:
        """
         Creates a preview curve that will be used to create the bead solid.
         Returns previewPathCurve ( NXOpen.Spline):  The preview curve. .
        """
        pass
    def GetPreviewPath(self) -> NXOpen.Spline:
        """
         The preview curve that will be used to create the bead solid.
         Returns previewPathCurve ( NXOpen.Spline):  The preview curve. .
        """
        pass
    def NewPath(self) -> WeldBeadPathBuilder:
        """
         Creates a NXOpen.Weld.WeldBeadPathBuilder object. 
         Returns newPathBuilder ( WeldBeadPathBuilder NXOpe): .
        """
        pass
    def NewSize(self) -> WeldBeadSizeBuilder:
        """
         Creates a NXOpen.Weld.WeldBeadSizeBuilder object. 
         Returns newSizeBuilder ( WeldBeadSizeBuilder NXOpe): .
        """
        pass
import NXOpen
class WeldBeadPathBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[WeldBeadPathBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: WeldBeadPathBuilder) -> None:
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
    def Erase(self, obj: WeldBeadPathBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: WeldBeadPathBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: WeldBeadPathBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> WeldBeadPathBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( WeldBeadPathBuilder NXOpe):  object found at input index .
        """
        pass
    def GetContents(self) -> List[WeldBeadPathBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( WeldBeadPathBuilder List[NXO):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: WeldBeadPathBuilder) -> None:
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
    def SetContents(self, objects: List[WeldBeadPathBuilder]) -> None:
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
    def Swap(self, object1: WeldBeadPathBuilder, object2: WeldBeadPathBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class WeldBeadPathBuilder(NXOpen.TaggedObject): 
    """ Represents the path the bead shape will be swept along. """
    class OffsetMethodType(Enum):
        """
        Members Include: 
         |InFace|  offset in selected primary faces 
         |Centerline|  centerline of overlapping sheets 

        """
        InFace: int
        Centerline: int
        @staticmethod
        def ValueOf(value: int) -> WeldBeadPathBuilder.OffsetMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CreateEndToStart(self) -> bool:
        """
        Getter for property: (bool) CreateEndToStart
         Returns the indication if the sweep should be created from the edge location to the start location.  
           True
                    indicates the sweep will be created from the end to the start location of the path, false
                    indicates the sweep will be from the start to the end location of the path. This option is
                    only used if the path section is closed.    
         
        """
        pass
    @CreateEndToStart.setter
    def CreateEndToStart(self, createEndToStart: bool):
        """
        Setter for property: (bool) CreateEndToStart
         Returns the indication if the sweep should be created from the edge location to the start location.  
           True
                    indicates the sweep will be created from the end to the start location of the path, false
                    indicates the sweep will be from the start to the end location of the path. This option is
                    only used if the path section is closed.    
         
        """
        pass
    @property
    def EndPath(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) EndPath
         Returns the location at which to end the sweep of the bead shape.  
             
         
        """
        pass
    @property
    def OffsetAlongNormal(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OffsetAlongNormal
         Returns the offset along normal   
            
         
        """
        pass
    @property
    def OffsetInFace(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OffsetInFace
         Returns the expression containing the distance to offset the path normal to the face.  
             
         
        """
        pass
    @property
    def OffsetMethod(self) -> WeldBeadPathBuilder.OffsetMethodType:
        """
        Getter for property: ( WeldBeadPathBuilder.OffsetMethodType NXOpe) OffsetMethod
         Returns the desired path offset method.  
             
         
        """
        pass
    @OffsetMethod.setter
    def OffsetMethod(self, offsetMethod: WeldBeadPathBuilder.OffsetMethodType):
        """
        Setter for property: ( WeldBeadPathBuilder.OffsetMethodType NXOpe) OffsetMethod
         Returns the desired path offset method.  
             
         
        """
        pass
    @property
    def PathSection(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) PathSection
         Returns the section defining the path.  
             
         
        """
        pass
    @property
    def ReverseOffsetDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseOffsetDirection
         Returns the reverse the direction to offset the path section.  
           The update path method 
                    provides the information for the default directions.   
         
        """
        pass
    @ReverseOffsetDirection.setter
    def ReverseOffsetDirection(self, reverseOffsetDirection: bool):
        """
        Setter for property: (bool) ReverseOffsetDirection
         Returns the reverse the direction to offset the path section.  
           The update path method 
                    provides the information for the default directions.   
         
        """
        pass
    @property
    def StartPath(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) StartPath
         Returns the location at which to start the sweep of the bead shape.  
             
         
        """
        pass
    def GetSweepPath(self) -> NXOpen.Spline:
        """
         The portion of the preview curve that can be used to adjust the start or end limits. 
         Returns sweepPathCurve ( NXOpen.Spline):  The sweep path curve used for setting limits. .
        """
        pass
    def UpdatePath(self) -> Tuple[bool, NXOpen.Point3d, NXOpen.Vector3d, NXOpen.Vector3d, NXOpen.Vector3d]:
        """
         Computes the preview path, and evaluation information for indicating desired face side of the preview path. 
         Returns A tuple consisting of (pointFound, evaluationPoint, pathTangent, faceNormalWithFin, faceNormalOppositeFin). 
         - pointFound is: bool. Point and evaluation results are valid .
         - evaluationPoint is:  NXOpen.Point3d. Point that reference vectors are computed at.
         - pathTangent is:  NXOpen.Vector3d. Tangent to path at evaluationPoint .
         - faceNormalWithFin is:  NXOpen.Vector3d. Normal if path is in direction of parasolid fin .
         - faceNormalOppositeFin is:  NXOpen.Vector3d. Normal if path is opposite direction of parasolid fin.

        """
        pass
import NXOpen
class WeldBeadSizeBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[WeldBeadSizeBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: WeldBeadSizeBuilder) -> None:
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
    def Erase(self, obj: WeldBeadSizeBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: WeldBeadSizeBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: WeldBeadSizeBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> WeldBeadSizeBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( WeldBeadSizeBuilder NXOpe):  object found at input index .
        """
        pass
    def GetContents(self) -> List[WeldBeadSizeBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( WeldBeadSizeBuilder List[NXO):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: WeldBeadSizeBuilder) -> None:
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
    def SetContents(self, objects: List[WeldBeadSizeBuilder]) -> None:
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
    def Swap(self, object1: WeldBeadSizeBuilder, object2: WeldBeadSizeBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class WeldBeadSizeBuilder(NXOpen.TaggedObject): 
    """ This builder is used to define the bead shape. """
    class Size(Enum):
        """
        Members Include: 
         |Default1|  Default1 from the customer defaults 
         |Default2|  Default2 from the customer defaults 
         |Default3|  Default3 from the customer defaults 
         |Default4|  Default4 from the customer defaults 
         |Default5|  Default5 from the customer defaults 
         |Custom|  Manually keyin value.               

        """
        Default1: int
        Default2: int
        Default3: int
        Default4: int
        Default5: int
        Custom: int
        @staticmethod
        def ValueOf(value: int) -> WeldBeadSizeBuilder.Size:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TriangleMethodType(Enum):
        """
        Members Include: 
         |LegLength|  Triangle defined by leg lengths 
         |ThroatThickness|  Trangle defined by throat thickness               

        """
        LegLength: int
        ThroatThickness: int
        @staticmethod
        def ValueOf(value: int) -> WeldBeadSizeBuilder.TriangleMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TriangleTypes(Enum):
        """
        Members Include: 
         |OneSided|  Basically a right triangle 
         |TwoSided|  Basically an isosceles triangle 

        """
        OneSided: int
        TwoSided: int
        @staticmethod
        def ValueOf(value: int) -> WeldBeadSizeBuilder.TriangleTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CustomSection(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) CustomSection
         Returns  the section containing the custom bead shape.  
             
         
        """
        pass
    @property
    def PathLocation(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) PathLocation
         Returns the location on the path to place the bead shape.  
             
         
        """
        pass
    @property
    def RectangleBase(self) -> float:
        """
        Getter for property: (float) RectangleBase
         Returns the base length of a rectangle shaped bead.  
            
         
        """
        pass
    @RectangleBase.setter
    def RectangleBase(self, length: float):
        """
        Setter for property: (float) RectangleBase
         Returns the base length of a rectangle shaped bead.  
            
         
        """
        pass
    @property
    def RectangleHeight(self) -> float:
        """
        Getter for property: (float) RectangleHeight
         Returns the height of a rectangle shaped bead.  
            
         
        """
        pass
    @RectangleHeight.setter
    def RectangleHeight(self, height: float):
        """
        Setter for property: (float) RectangleHeight
         Returns the height of a rectangle shaped bead.  
            
         
        """
        pass
    @property
    def SemiMajor(self) -> float:
        """
        Getter for property: (float) SemiMajor
         Returns the semi the semi major size of an ellipse shaped bead.  
              
         
        """
        pass
    @SemiMajor.setter
    def SemiMajor(self, semiMajor: float):
        """
        Setter for property: (float) SemiMajor
         Returns the semi the semi major size of an ellipse shaped bead.  
              
         
        """
        pass
    @property
    def SemiMinor(self) -> float:
        """
        Getter for property: (float) SemiMinor
         Returns the semi minor size of an ellipse shaped bead.  
            
         
        """
        pass
    @SemiMinor.setter
    def SemiMinor(self, semiMinor: float):
        """
        Setter for property: (float) SemiMinor
         Returns the semi minor size of an ellipse shaped bead.  
            
         
        """
        pass
    @property
    def SizeString(self) -> WeldBeadSizeBuilder.Size:
        """
        Getter for property: ( WeldBeadSizeBuilder.Size NXOpe) SizeString
         Returns the standard size setting.  
             
         
        """
        pass
    @SizeString.setter
    def SizeString(self, sizeString: WeldBeadSizeBuilder.Size):
        """
        Setter for property: ( WeldBeadSizeBuilder.Size NXOpe) SizeString
         Returns the standard size setting.  
             
         
        """
        pass
    @property
    def ThroatThickness(self) -> float:
        """
        Getter for property: (float) ThroatThickness
         Returns the throat thickness of a triangular shaped bead.  
            
         
        """
        pass
    @ThroatThickness.setter
    def ThroatThickness(self, throatThickness: float):
        """
        Setter for property: (float) ThroatThickness
         Returns the throat thickness of a triangular shaped bead.  
            
         
        """
        pass
    @property
    def TriangleBase(self) -> float:
        """
        Getter for property: (float) TriangleBase
         Returns the horizontal leg length of a triangular shaped bead.  
            
         
        """
        pass
    @TriangleBase.setter
    def TriangleBase(self, length: float):
        """
        Setter for property: (float) TriangleBase
         Returns the horizontal leg length of a triangular shaped bead.  
            
         
        """
        pass
    @property
    def TriangleHeight(self) -> float:
        """
        Getter for property: (float) TriangleHeight
         Returns the vertical leg length of a triangular shaped bead.  
            
         
        """
        pass
    @TriangleHeight.setter
    def TriangleHeight(self, length: float):
        """
        Setter for property: (float) TriangleHeight
         Returns the vertical leg length of a triangular shaped bead.  
            
         
        """
        pass
    @property
    def TriangleMethod(self) -> WeldBeadSizeBuilder.TriangleMethodType:
        """
        Getter for property: ( WeldBeadSizeBuilder.TriangleMethodType NXOpe) TriangleMethod
         Returns the method used to construct the triangle shape.  
             
         
        """
        pass
    @TriangleMethod.setter
    def TriangleMethod(self, method: WeldBeadSizeBuilder.TriangleMethodType):
        """
        Setter for property: ( WeldBeadSizeBuilder.TriangleMethodType NXOpe) TriangleMethod
         Returns the method used to construct the triangle shape.  
             
         
        """
        pass
    @property
    def TriangleType(self) -> WeldBeadSizeBuilder.TriangleTypes:
        """
        Getter for property: ( WeldBeadSizeBuilder.TriangleTypes NXOpe) TriangleType
         Returns the method used to indicate the type of triangle to create.  
             
         
        """
        pass
    @TriangleType.setter
    def TriangleType(self, method: WeldBeadSizeBuilder.TriangleTypes):
        """
        Setter for property: ( WeldBeadSizeBuilder.TriangleTypes NXOpe) TriangleType
         Returns the method used to indicate the type of triangle to create.  
             
         
        """
        pass
    @property
    def TubeDiameter(self) -> float:
        """
        Getter for property: (float) TubeDiameter
         Returns the diameter size of the tube shape.  
             
         
        """
        pass
    @TubeDiameter.setter
    def TubeDiameter(self, tubeDiameter: float):
        """
        Setter for property: (float) TubeDiameter
         Returns the diameter size of the tube shape.  
             
         
        """
        pass
import NXOpen.Features
class WeldBead(NXOpen.Features.BodyFeature): 
    """ Represents a Weld Bead feature """
    pass
class WeldContourShape(Enum):
    """
    Members Include: 
     |NotSet|  No shape                  
     |Convex|  Convex shape              
     |Flush|  Flush shape               
     |Concave|  Concave shape             

    """
    NotSet: int
    Convex: int
    Flush: int
    Concave: int
    @staticmethod
    def ValueOf(value: int) -> WeldContourShape:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class WeldCpdUtils(NXOpen.Object): 
    """
    Provides methods for access a WeldCpdUtils class object in NX.
    """
    def GetDesignFeatureFromWeldFeature(featureTag: NXOpen.NXObject) -> List[NXOpen.NXObject]:
        """
         
                Return Design Features of a given welding joint or surface weld feature.
                
         Returns designFeatures ( NXOpen.NXObject Li):  design features .
        """
        pass
    def GetJointCurvesFromWeldFeature(featureTag: NXOpen.NXObject) -> List[NXOpen.Curve]:
        """
         
                Return joint curves of a given welding joint feature.
                
         Returns jointCurves ( NXOpen.Curve Li):  joint curves .
        """
        pass
class WeldCreationDirection(Enum):
    """
    Members Include: 
     |Default|  Default construction direction 
     |Opposite|  Opposite construction direction 

    """
    Default: int
    Opposite: int
    @staticmethod
    def ValueOf(value: int) -> WeldCreationDirection:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class WeldCustom(Enum):
    """
    Members Include: 
     |SolidNone|  creates only a point 
     |SolidSphere|  creates a sphere 
     |SolidCylinder|  creates a cylinder 
     |SolidCone|  creates a cone 
     |SolidDefault|  creates a default solid 

    """
    SolidNone: int
    SolidSphere: int
    SolidCylinder: int
    SolidCone: int
    SolidDefault: int
    @staticmethod
    def ValueOf(value: int) -> WeldCustom:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class WeldDatumControlDirection(Enum):
    """
    Members Include: 
     |Invalid|  Invalid direction 
     |X|  X direction 
     |Y|  Y direction 
     |Z|  Z direction 

    """
    Invalid: int
    X: int
    Y: int
    Z: int
    @staticmethod
    def ValueOf(value: int) -> WeldDatumControlDirection:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class WeldFacesetIndex(Enum):
    """
    Members Include: 
     |First|  first face set 
     |Second|  second face set 
     |Third|  third face set 
     |Forth|  forth face set 

    """
    First: int
    Second: int
    Third: int
    Forth: int
    @staticmethod
    def ValueOf(value: int) -> WeldFacesetIndex:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class WeldFeatureOutput(Enum):
    """
    Members Include: 
     |Curves|  Output only curves 
     |Solid|  Output only solids 
     |Both|  Output both curves and solids 

    """
    Curves: int
    Solid: int
    Both: int
    @staticmethod
    def ValueOf(value: int) -> WeldFeatureOutput:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class WeldFeatureSetType(Enum):
    """
    Members Include: 
     |FilletWeld|  Fillet Weld     
     |GrooveWeld|  Groove Weld     
     |ResistanceSpot|  Resistance Spot 
     |ArcSpot|  Arc Spot        
     |Clinch|  Clinch          
     |Dollop|  Dollop          
     |WeldNut|  Weld Nut        
     |WeldStud|  Weld Stud       
     |Custom1Point|  Custom1 Point   
     |Custom2Point|  Custom2 Point   
     |Custom3Point|  Custom3 Point   
     |Custom4Point|  Custom4 Point   
     |Custom5Point|  Custom5 Point   
     |BiwDatumSurface|  Datum Surface   
     |BiwDatumPin|  Datum Pin       
     |BiwDatumCustomer1|  Datum Customer1 
     |BiwDatumCustomer2|  Datum Customer2 
     |BiwDatumCustomer3|  Datum Customer3 
     |BiwMeasurementSurface|  Measurement Surface 
     |BiwMeasurementHole|  Measurement Hole    
     |BiwMeasurementSlot|  Measurement Slot    
     |BiwMeasurementStud|  Measurement Stud    
     |BiwMeasurementTrim|  Measurement Trim    
     |BiwMeasurementHem|  Measurement Hem     
     |BiwMeasurementCustomer1|  Measurement Customer1 
     |BiwMeasurementCustomer2|  Measurement Customer2 
     |BiwMeasurementCustomer3|  Measurement Customer3 

    """
    FilletWeld: int
    GrooveWeld: int
    ResistanceSpot: int
    ArcSpot: int
    Clinch: int
    Dollop: int
    WeldNut: int
    WeldStud: int
    Custom1Point: int
    Custom2Point: int
    Custom3Point: int
    Custom4Point: int
    Custom5Point: int
    BiwDatumSurface: int
    BiwDatumPin: int
    BiwDatumCustomer1: int
    BiwDatumCustomer2: int
    BiwDatumCustomer3: int
    BiwMeasurementSurface: int
    BiwMeasurementHole: int
    BiwMeasurementSlot: int
    BiwMeasurementStud: int
    BiwMeasurementTrim: int
    BiwMeasurementHem: int
    BiwMeasurementCustomer1: int
    BiwMeasurementCustomer2: int
    BiwMeasurementCustomer3: int
    @staticmethod
    def ValueOf(value: int) -> WeldFeatureSetType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class WeldFillBuilder(NXOpen.Builder): 
    """ A builder used to create or edit a NXOpen.Weld.Fill feature. """
    class BoundaryMethodType(Enum):
        """
        Members Include: 
         |Rectangle|  Boundary defined by a two point rectangle. 
         |Curve|  Boundary defined by a curve. 

        """
        Rectangle: int
        Curve: int
        @staticmethod
        def ValueOf(value: int) -> WeldFillBuilder.BoundaryMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class WidthAlongType(Enum):
        """
        Members Include: 
         |Xc|  The length is aligned along the current WCS X direction. 
         |Yc|  The length is aligned along the current WCS Y direction. 

        """
        Xc: int
        Yc: int
        @staticmethod
        def ValueOf(value: int) -> WeldFillBuilder.WidthAlongType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Boundary(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Boundary
         Returns the section defining the boundary if the 
                     NXOpen::Weld::WeldFillBuilder::BoundaryMethodTypeCurve  
                    option is specified for the boundary type.  
             
         
        """
        pass
    @property
    def BoundaryMethod(self) -> WeldFillBuilder.BoundaryMethodType:
        """
        Getter for property: ( WeldFillBuilder.BoundaryMethodType NXOpe) BoundaryMethod
         Returns the type of boundary to create the fill from.  
             
         
        """
        pass
    @BoundaryMethod.setter
    def BoundaryMethod(self, boundaryMethod: WeldFillBuilder.BoundaryMethodType):
        """
        Setter for property: ( WeldFillBuilder.BoundaryMethodType NXOpe) BoundaryMethod
         Returns the type of boundary to create the fill from.  
             
         
        """
        pass
    @property
    def ChangeViewOrientation(self) -> bool:
        """
        Getter for property: (bool) ChangeViewOrientation
         Returns the indication if the view orientation should be changed automatically (true)
                    upon initial creation of rectangles, or not (false)   
            
         
        """
        pass
    @ChangeViewOrientation.setter
    def ChangeViewOrientation(self, changeViewOrientation: bool):
        """
        Setter for property: (bool) ChangeViewOrientation
         Returns the indication if the view orientation should be changed automatically (true)
                    upon initial creation of rectangles, or not (false)   
            
         
        """
        pass
    @property
    def Characteristics(self) -> CharacteristicsBuilder:
        """
        Getter for property: ( CharacteristicsBuilder NXOpe) Characteristics
         Returns the characteristics information.  
             
         
        """
        pass
    @property
    def Corner1(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Corner1
         Returns the first corner of the boundary if the 
                     NXOpen::Weld::WeldFillBuilder::BoundaryMethodTypeRectangle  
                    option is specified for the boundary type.  
             
         
        """
        pass
    @Corner1.setter
    def Corner1(self, corner1: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Corner1
         Returns the first corner of the boundary if the 
                     NXOpen::Weld::WeldFillBuilder::BoundaryMethodTypeRectangle  
                    option is specified for the boundary type.  
             
         
        """
        pass
    @property
    def Corner2(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Corner2
         Returns the second corner of the boundary if the 
                     NXOpen::Weld::WeldFillBuilder::BoundaryMethodTypeRectangle  
                    option is specified for the boundary type.  
             
         
        """
        pass
    @Corner2.setter
    def Corner2(self, corner2: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Corner2
         Returns the second corner of the boundary if the 
                     NXOpen::Weld::WeldFillBuilder::BoundaryMethodTypeRectangle  
                    option is specified for the boundary type.  
             
         
        """
        pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance used in processing to determine if two points are coincident.  
             
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance used in processing to determine if two points are coincident.  
             
         
        """
        pass
    @property
    def ExtendDistance(self) -> float:
        """
        Getter for property: (float) ExtendDistance
         Returns the distance to extend a strip.  
             
         
        """
        pass
    @ExtendDistance.setter
    def ExtendDistance(self, distance: float):
        """
        Setter for property: (float) ExtendDistance
         Returns the distance to extend a strip.  
             
         
        """
        pass
    @property
    def ExtrudeHeight(self) -> float:
        """
        Getter for property: (float) ExtrudeHeight
         Returns the height of the extrusions representing the fill.  
             
         
        """
        pass
    @ExtrudeHeight.setter
    def ExtrudeHeight(self, extrudeHeight: float):
        """
        Setter for property: (float) ExtrudeHeight
         Returns the height of the extrusions representing the fill.  
             
         
        """
        pass
    @property
    def FillStripList(self) -> WeldFillStripBuilderList:
        """
        Getter for property: ( WeldFillStripBuilderList NXOpe) FillStripList
         Returns the fill strip list.  
             
         
        """
        pass
    @property
    def InnerBoundary(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) InnerBoundary
         Returns the section containing edges of interior openings which indicate that these openings should be filled over.  
             
         
        """
        pass
    @property
    def Orientation(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) Orientation
         Returns the coordinate system that defines the alignment of the strips and rectangle.  
             
         
        """
        pass
    @Orientation.setter
    def Orientation(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) Orientation
         Returns the coordinate system that defines the alignment of the strips and rectangle.  
             
         
        """
        pass
    @property
    def PlacementFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) PlacementFace
         Returns the collector containing the faces to build the fill on.  
           Note that during processing
                    additional faces will be obtained by getting adjacent tangent faces (within 45 degrees) so that
                    the boundary of the area is covered. At least one face inside of every boundary must be selected.   
         
        """
        pass
    @property
    def SubdivideRegion(self) -> bool:
        """
        Getter for property: (bool) SubdivideRegion
         Returns the indication if the fill is to be a collection of rectangles (true), or
                    simply the enclosed boundary area (false).  
             
         
        """
        pass
    @SubdivideRegion.setter
    def SubdivideRegion(self, subdivideRegion: bool):
        """
        Setter for property: (bool) SubdivideRegion
         Returns the indication if the fill is to be a collection of rectangles (true), or
                    simply the enclosed boundary area (false).  
             
         
        """
        pass
    @property
    def UseSeedFace(self) -> bool:
        """
        Getter for property: (bool) UseSeedFace
         Returns the indication if the selected faces should be used as seed faces.  
             
         
        """
        pass
    @UseSeedFace.setter
    def UseSeedFace(self, useSeedFace: bool):
        """
        Setter for property: (bool) UseSeedFace
         Returns the indication if the selected faces should be used as seed faces.  
             
         
        """
        pass
    @property
    def Width(self) -> float:
        """
        Getter for property: (float) Width
         Returns the width of the rectangles.  
           Only used if SubdivideRegion is true.   
         
        """
        pass
    @Width.setter
    def Width(self, width: float):
        """
        Setter for property: (float) Width
         Returns the width of the rectangles.  
           Only used if SubdivideRegion is true.   
         
        """
        pass
    @property
    def WidthAlong(self) -> WeldFillBuilder.WidthAlongType:
        """
        Getter for property: ( WeldFillBuilder.WidthAlongType NXOpe) WidthAlong
         Returns the width of the rectangles will be measured along this direction.  
              
         
        """
        pass
    @WidthAlong.setter
    def WidthAlong(self, widthAlong: WeldFillBuilder.WidthAlongType):
        """
        Setter for property: ( WeldFillBuilder.WidthAlongType NXOpe) WidthAlong
         Returns the width of the rectangles will be measured along this direction.  
              
         
        """
        pass
    def DeleteFillStrip(self, fillStrip: WeldFillStripBuilder) -> None:
        """
         Delete a fill strip. 
        """
        pass
    def NewFillStrip(self, center: NXOpen.Point3d, length: float) -> WeldFillStripBuilder:
        """
         Create a new fill strip. 
         Returns newFillStrip ( WeldFillStripBuilder NXOpe): .
        """
        pass
import NXOpen
class WeldFillStripBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[WeldFillStripBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: WeldFillStripBuilder) -> None:
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
    def Erase(self, obj: WeldFillStripBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: WeldFillStripBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: WeldFillStripBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> WeldFillStripBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( WeldFillStripBuilder NXOpe):  object found at input index .
        """
        pass
    def GetContents(self) -> List[WeldFillStripBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( WeldFillStripBuilder List[NXO):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: WeldFillStripBuilder) -> None:
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
    def SetContents(self, objects: List[WeldFillStripBuilder]) -> None:
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
    def Swap(self, object1: WeldFillStripBuilder, object2: WeldFillStripBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class WeldFillStripBuilder(NXOpen.Builder): 
    """ A builder used to create or edit a single strip of the NXOpen.Weld.WeldFillBuilder. """
    @property
    def Center(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) Center
         Returns the center of the fill strip.  
             
         
        """
        pass
    @property
    def Length(self) -> float:
        """
        Getter for property: (float) Length
         Returns the length of the fill strip.  
             
         
        """
        pass
    @Length.setter
    def Length(self, length: float):
        """
        Setter for property: (float) Length
         Returns the length of the fill strip.  
             
         
        """
        pass
    @property
    def ToBeDeleted(self) -> bool:
        """
        Getter for property: (bool) ToBeDeleted
         Returns the flag indicating that the strip should be deleted.  
             
         
        """
        pass
    @ToBeDeleted.setter
    def ToBeDeleted(self, flag: bool):
        """
        Setter for property: (bool) ToBeDeleted
         Returns the flag indicating that the strip should be deleted.  
             
         
        """
        pass
    def AlignNegative(self, alignStrip: WeldFillStripBuilder) -> None:
        """
         Aligns the end of the fill strip, opposite of the length direction from center, to the
                    same end of the input fill strip. 
        """
        pass
    def AlignPositive(self, alignStrip: WeldFillStripBuilder) -> None:
        """
         Aligns the end of the fill strip, along the length direction from center, to the
                    same end of the input fill strip. 
        """
        pass
    def JoinNegative(self, joinStrip: WeldFillStripBuilder) -> None:
        """
         Joins the end of the fill strip, opposite of the length direction from center, to the
                    other fill strip input. Note the caller must delete the joinStrip if desired. 
        """
        pass
    def JoinPositive(self, joinStrip: WeldFillStripBuilder) -> None:
        """
         Joins the end of the fill strip, along the length direction from center, to the
                    other fill strip input. Note the caller must delete the joinStrip if desired. 
        """
        pass
    def MoveDelta(self, lengthDelta: float, widthDelta: float) -> None:
        """
         Moves the fill strip the input length and width values. 
        """
        pass
    def MoveToPoint(self, newCenter: NXOpen.Point3d) -> None:
        """
         Moves the fill strip to the input center. 
        """
        pass
    def Split(self) -> WeldFillStripBuilder:
        """
         Splits the fill strip at the center and creates a new strip. 
         Returns newFillStrip ( WeldFillStripBuilder NXOpe): .
        """
        pass
    def StretchNegative(self, lengthDelta: float) -> None:
        """
         Stretches the fill strip the input length opposite of the length direction. 
        """
        pass
    def StretchPositive(self, lengthDelta: float) -> None:
        """
         Stretches the fill strip the input length in the length direction. 
        """
        pass
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
class WeldGrooveBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a NXOpen.Weld.WeldGroove builder """
    class Contour(Enum):
        """
        Members Include: 
         |NotSet|  None   
         |Convex|  Convex 
         |Flush|  Flush  
         |Concave| 

        """
        NotSet: int
        Convex: int
        Flush: int
        Concave: int
        @staticmethod
        def ValueOf(value: int) -> WeldGrooveBuilder.Contour:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Edge(Enum):
        """
        Members Include: 
         |NotPrepared|  Not Prepared 
         |Prepared|  Prepared 

        """
        NotPrepared: int
        Prepared: int
        @staticmethod
        def ValueOf(value: int) -> WeldGrooveBuilder.Edge:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Prepare(Enum):
        """
        Members Include: 
         |NotSet|  None 
         |EntireLength|  Entire Length 
         |WeldLimits|  Weld Limits 
         |Complex|  Complex 

        """
        NotSet: int
        EntireLength: int
        WeldLimits: int
        Complex: int
        @staticmethod
        def ValueOf(value: int) -> WeldGrooveBuilder.Prepare:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SkipWeldMethod(Enum):
        """
        Members Include: 
         |NumberLength|  Number and Length  
         |NumberSpacing|  Number and Spacing 
         |SpacingLength|  Spacing and Length 

        """
        NumberLength: int
        NumberSpacing: int
        SpacingLength: int
        @staticmethod
        def ValueOf(value: int) -> WeldGrooveBuilder.SkipWeldMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Taper(Enum):
        """
        Members Include: 
         |FromEndFace|  From End Face 
         |FromTopFace|  From Top Face 

        """
        FromEndFace: int
        FromTopFace: int
        @staticmethod
        def ValueOf(value: int) -> WeldGrooveBuilder.Taper:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |SquareButt|  Square Butt              
         |VGroove|  V Groove                 
         |BevelGroove|  Bevel Groove             
         |UGroove|  U Groove                 
         |JGroove|  J Groove                 
         |FlaredVGroove|  Flared V Groove          
         |FlaredBevelGroove|  Flared Bevel Groove      
         |FillinFlaredVGroove| 
         |FillinFlaredBevelGroove|  Fillin Flared Bevel Groove

        """
        SquareButt: int
        VGroove: int
        BevelGroove: int
        UGroove: int
        JGroove: int
        FlaredVGroove: int
        FlaredBevelGroove: int
        FillinFlaredVGroove: int
        FillinFlaredBevelGroove: int
        @staticmethod
        def ValueOf(value: int) -> WeldGrooveBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AssignWeldPMI(self) -> bool:
        """
        Getter for property: (bool) AssignWeldPMI
         Returns a value indicating whether the assign weld pmi is true    
            
         
        """
        pass
    @AssignWeldPMI.setter
    def AssignWeldPMI(self, assignWeldPMI: bool):
        """
        Setter for property: (bool) AssignWeldPMI
         Returns a value indicating whether the assign weld pmi is true    
            
         
        """
        pass
    @property
    def Characteristics(self) -> CharacteristicsBuilder:
        """
        Getter for property: ( CharacteristicsBuilder NXOpe) Characteristics
         Returns the characteristics   
            
         
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
    def ContourType(self) -> WeldGrooveBuilder.Contour:
        """
        Getter for property: ( WeldGrooveBuilder.Contour NXOpe) ContourType
         Returns the contour type   
            
         
        """
        pass
    @ContourType.setter
    def ContourType(self, contour: WeldGrooveBuilder.Contour):
        """
        Setter for property: ( WeldGrooveBuilder.Contour NXOpe) ContourType
         Returns the contour type   
            
         
        """
        pass
    @property
    def CreateSkipWelds(self) -> bool:
        """
        Getter for property: (bool) CreateSkipWelds
         Returns a value indicating whether to create skip welds     
            
         
        """
        pass
    @CreateSkipWelds.setter
    def CreateSkipWelds(self, createSkipWelds: bool):
        """
        Setter for property: (bool) CreateSkipWelds
         Returns a value indicating whether to create skip welds     
            
         
        """
        pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance   
            
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance   
            
         
        """
        pass
    @property
    def EdgeSet1(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) EdgeSet1
         Returns the first edge set   
            
         
        """
        pass
    @property
    def EdgeSet2(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) EdgeSet2
         Returns the second edge set   
            
         
        """
        pass
    @property
    def EdgeType(self) -> WeldGrooveBuilder.Edge:
        """
        Getter for property: ( WeldGrooveBuilder.Edge NXOpe) EdgeType
         Returns the edge type   
            
         
        """
        pass
    @EdgeType.setter
    def EdgeType(self, edgeType: WeldGrooveBuilder.Edge):
        """
        Setter for property: ( WeldGrooveBuilder.Edge NXOpe) EdgeType
         Returns the edge type   
            
         
        """
        pass
    @property
    def EndAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndAngle
         Returns the taper angle at the end of the weld   
            
         
        """
        pass
    @property
    def EndDistance(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) EndDistance
         Returns the end limit as defined by the distance along the edge    
            
         
        """
        pass
    @property
    def FaceSet1(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FaceSet1
         Returns the face set1   
            
         
        """
        pass
    @property
    def FaceSet2(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FaceSet2
         Returns the face set2   
            
         
        """
        pass
    @property
    def GrooveAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) GrooveAngle
         Returns the groove angle   
            
         
        """
        pass
    @property
    def GrooveRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) GrooveRadius
         Returns the groove radius   
            
         
        """
        pass
    @property
    def IsRootOpening(self) -> bool:
        """
        Getter for property: (bool) IsRootOpening
         Returns a value indicating whether root opening is true    
            
         
        """
        pass
    @IsRootOpening.setter
    def IsRootOpening(self, isRootOpening: bool):
        """
        Setter for property: (bool) IsRootOpening
         Returns a value indicating whether root opening is true    
            
         
        """
        pass
    @property
    def IsRootPenetration(self) -> bool:
        """
        Getter for property: (bool) IsRootPenetration
         Returns a value indicating whether root depth is true    
            
         
        """
        pass
    @IsRootPenetration.setter
    def IsRootPenetration(self, isRootPenetration: bool):
        """
        Setter for property: (bool) IsRootPenetration
         Returns a value indicating whether root depth is true    
            
         
        """
        pass
    @property
    def Method(self) -> WeldGrooveBuilder.SkipWeldMethod:
        """
        Getter for property: ( WeldGrooveBuilder.SkipWeldMethod NXOpe) Method
         Returns the method for creating skip welds   
            
         
        """
        pass
    @Method.setter
    def Method(self, method: WeldGrooveBuilder.SkipWeldMethod):
        """
        Setter for property: ( WeldGrooveBuilder.SkipWeldMethod NXOpe) Method
         Returns the method for creating skip welds   
            
         
        """
        pass
    @property
    def NumberOfWelds(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NumberOfWelds
         Returns the number of welds   
            
         
        """
        pass
    @property
    def PenetrationDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PenetrationDepth
         Returns the penetration depth   
            
         
        """
        pass
    @property
    def PrepareEdges(self) -> WeldGrooveBuilder.Prepare:
        """
        Getter for property: ( WeldGrooveBuilder.Prepare NXOpe) PrepareEdges
         Returns the type of edges to prepare   
            
         
        """
        pass
    @PrepareEdges.setter
    def PrepareEdges(self, prepareEdges: WeldGrooveBuilder.Prepare):
        """
        Setter for property: ( WeldGrooveBuilder.Prepare NXOpe) PrepareEdges
         Returns the type of edges to prepare   
            
         
        """
        pass
    @property
    def RecreateDeletedWelds(self) -> bool:
        """
        Getter for property: (bool) RecreateDeletedWelds
         Returns a value indicating whether to recreate deleted welds    
            
         
        """
        pass
    @RecreateDeletedWelds.setter
    def RecreateDeletedWelds(self, recreateDeletedWelds: bool):
        """
        Setter for property: (bool) RecreateDeletedWelds
         Returns a value indicating whether to recreate deleted welds    
            
         
        """
        pass
    @property
    def RemoveHoles(self) -> bool:
        """
        Getter for property: (bool) RemoveHoles
         Returns a value indicating whether holes should be ignored when creating the groove weld.  
             
         
        """
        pass
    @RemoveHoles.setter
    def RemoveHoles(self, removeHoles: bool):
        """
        Setter for property: (bool) RemoveHoles
         Returns a value indicating whether holes should be ignored when creating the groove weld.  
             
         
        """
        pass
    @property
    def RootOpening(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RootOpening
         Returns the root opening   
            
         
        """
        pass
    @property
    def RootPenetration(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RootPenetration
         Returns the root penetration   
            
         
        """
        pass
    @property
    def SecondPenetrationDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SecondPenetrationDepth
         Returns the second penetration depth   
            
         
        """
        pass
    @property
    def SeedFace1(self) -> NXOpen.Face:
        """
        Getter for property: ( NXOpen.Face) SeedFace1
         Returns the first seed face   
            
         
        """
        pass
    @SeedFace1.setter
    def SeedFace1(self, seedFace1: NXOpen.Face):
        """
        Setter for property: ( NXOpen.Face) SeedFace1
         Returns the first seed face   
            
         
        """
        pass
    @property
    def SeedFace2(self) -> NXOpen.Face:
        """
        Getter for property: ( NXOpen.Face) SeedFace2
         Returns the second seed face   
            
         
        """
        pass
    @SeedFace2.setter
    def SeedFace2(self, seedFace2: NXOpen.Face):
        """
        Setter for property: ( NXOpen.Face) SeedFace2
         Returns the second seed face   
            
         
        """
        pass
    @property
    def SeedPoint1(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) SeedPoint1
         Returns the point on the first face   
            
         
        """
        pass
    @SeedPoint1.setter
    def SeedPoint1(self, seedPoint1: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) SeedPoint1
         Returns the point on the first face   
            
         
        """
        pass
    @property
    def SeedPoint2(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) SeedPoint2
         Returns the point on the second face   
            
         
        """
        pass
    @SeedPoint2.setter
    def SeedPoint2(self, seedPoint1: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) SeedPoint2
         Returns the point on the second face   
            
         
        """
        pass
    @property
    def SegmentLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SegmentLength
         Returns the length of weld   
            
         
        """
        pass
    @property
    def SingleFaceSet(self) -> bool:
        """
        Getter for property: (bool) SingleFaceSet
         Returns a value indicating whether the single face set is true    
            
         
        """
        pass
    @SingleFaceSet.setter
    def SingleFaceSet(self, singleFaceSet: bool):
        """
        Setter for property: (bool) SingleFaceSet
         Returns a value indicating whether the single face set is true    
            
         
        """
        pass
    @property
    def Spacing(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Spacing
         Returns the spacing between welds   
            
         
        """
        pass
    @property
    def StartAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartAngle
         Returns the taper angle at the start of the weld   
            
         
        """
        pass
    @property
    def StartDistance(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) StartDistance
         Returns the start limit as defined by the distance along the edge    
            
         
        """
        pass
    @property
    def TaperMethod(self) -> WeldGrooveBuilder.Taper:
        """
        Getter for property: ( WeldGrooveBuilder.Taper NXOpe) TaperMethod
         Returns the taper method   
            
         
        """
        pass
    @TaperMethod.setter
    def TaperMethod(self, taperMethod: WeldGrooveBuilder.Taper):
        """
        Setter for property: ( WeldGrooveBuilder.Taper NXOpe) TaperMethod
         Returns the taper method   
            
         
        """
        pass
    @property
    def Type(self) -> WeldGrooveBuilder.Types:
        """
        Getter for property: ( WeldGrooveBuilder.Types NXOpe) Type
         Returns the type of the groove   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: WeldGrooveBuilder.Types):
        """
        Setter for property: ( WeldGrooveBuilder.Types NXOpe) Type
         Returns the type of the groove   
            
         
        """
        pass
    @property
    def Uparameter1(self) -> float:
        """
        Getter for property: (float) Uparameter1
         Returns the u parameter for first face   
            
         
        """
        pass
    @Uparameter1.setter
    def Uparameter1(self, u1: float):
        """
        Setter for property: (float) Uparameter1
         Returns the u parameter for first face   
            
         
        """
        pass
    @property
    def Uparameter2(self) -> float:
        """
        Getter for property: (float) Uparameter2
         Returns the u parameter for second face   
            
         
        """
        pass
    @Uparameter2.setter
    def Uparameter2(self, u2: float):
        """
        Setter for property: (float) Uparameter2
         Returns the u parameter for second face   
            
         
        """
        pass
    @property
    def UseFillin(self) -> bool:
        """
        Getter for property: (bool) UseFillin
         Returns a value indicating whether to use fillin   
            
         
        """
        pass
    @UseFillin.setter
    def UseFillin(self, useFillin: bool):
        """
        Setter for property: (bool) UseFillin
         Returns a value indicating whether to use fillin   
            
         
        """
        pass
    @property
    def Vparameter1(self) -> float:
        """
        Getter for property: (float) Vparameter1
         Returns the v parameter for first face   
            
         
        """
        pass
    @Vparameter1.setter
    def Vparameter1(self, v1: float):
        """
        Setter for property: (float) Vparameter1
         Returns the v parameter for first face   
            
         
        """
        pass
    @property
    def Vparameter2(self) -> float:
        """
        Getter for property: (float) Vparameter2
         Returns the v parameter for second face   
            
         
        """
        pass
    @Vparameter2.setter
    def Vparameter2(self, v2: float):
        """
        Setter for property: (float) Vparameter2
         Returns the v parameter for second face   
            
         
        """
        pass
    @property
    def WeldSymmetric(self) -> bool:
        """
        Getter for property: (bool) WeldSymmetric
         Returns a value indicating whether the second depth is the same as the first depth    
            
         
        """
        pass
    @WeldSymmetric.setter
    def WeldSymmetric(self, weldSymmetric: bool):
        """
        Setter for property: (bool) WeldSymmetric
         Returns a value indicating whether the second depth is the same as the first depth    
            
         
        """
        pass
class WeldGrooveExtension(Enum):
    """
    Members Include: 
     |Tangent|  Extend selected edges to form an intersection. 
     |Project|  Project selected edges to opposite face set. 
     |ReverseProject|  Project selected edges to oppsoite face set using
                                                          normals from selected edges. 

    """
    Tangent: int
    Project: int
    ReverseProject: int
    @staticmethod
    def ValueOf(value: int) -> WeldGrooveExtension:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class WeldGrooveShape(Enum):
    """
    Members Include: 
     |SquareButt|  Square butt shape  
     |VGroove|  V groove shape     
     |Bevel|  Bevel shape        
     |UGroove|  U groove shape     
     |JGroove|  J groove shape     
     |FlaredV|  Flared V shape     
     |FlaredBevel|  Flared bevel shape 
     |FillinFlaredV|  Fillin Flared V shape 
     |FillinFlaredBevel|  Fillin Flared Bevel shape 

    """
    SquareButt: int
    VGroove: int
    Bevel: int
    UGroove: int
    JGroove: int
    FlaredV: int
    FlaredBevel: int
    FillinFlaredV: int
    FillinFlaredBevel: int
    @staticmethod
    def ValueOf(value: int) -> WeldGrooveShape:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class WeldGrooveType(Enum):
    """
    Members Include: 
     |EdgesNotPrepared|  Edges are not prepared 
     |EdgesPrepared|  Edges are prepared  

    """
    EdgesNotPrepared: int
    EdgesPrepared: int
    @staticmethod
    def ValueOf(value: int) -> WeldGrooveType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen.Features
class WeldGroove(NXOpen.Features.BodyFeature): 
    """ Represents a Weld Groove Feature """
    pass
class WeldGroupIdColor(Enum):
    """
    Members Include: 
     |NotSet|  None group id color 
     |First|  First Group Id Color Index 
     |Second|  Second Group Id Color Index 
     |Third|  Third Group Id Color Index 
     |Fourth|  Fourth Group Id Color Index 
     |Fifth|  Fifth Group Id Color Index 
     |Sixth|  Sixth Group Id Color Index 
     |Seventh|  Seventh Group Id Color Index 
     |Eighth|  Eighth Group Id Color Index 
     |Ninth|  Ninth Group Id Color Index 
     |Tenth|  Tenth Group Id Color Index 
     |Eleventh|  Eleventh Group Id Color Index 
     |Twelfth|  Twelvth Group Id Color Index 
     |Thirteenth|  Thirteenth Group Id Color Index 
     |Fourteenth|  Fourteenth Group Id Color Index 

    """
    NotSet: int
    First: int
    Second: int
    Third: int
    Fourth: int
    Fifth: int
    Sixth: int
    Seventh: int
    Eighth: int
    Ninth: int
    Tenth: int
    Eleventh: int
    Twelfth: int
    Thirteenth: int
    Fourteenth: int
    @staticmethod
    def ValueOf(value: int) -> WeldGroupIdColor:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class WeldImportBuilder(NXOpen.Builder): 
    """ Creates Weld features by reading a csv file """
    @property
    def ConfirmWarningMessages(self) -> bool:
        """
        Getter for property: (bool) ConfirmWarningMessages
         Returns the option to indicate if warning messages need to be confirmed.  
           If false setting, all warnings will be accepted.   
         
        """
        pass
    @ConfirmWarningMessages.setter
    def ConfirmWarningMessages(self, option: bool):
        """
        Setter for property: (bool) ConfirmWarningMessages
         Returns the option to indicate if warning messages need to be confirmed.  
           If false setting, all warnings will be accepted.   
         
        """
        pass
    @property
    def CreateFeatureGroups(self) -> bool:
        """
        Getter for property: (bool) CreateFeatureGroups
         Returns the option to create Feature Group features to collect Weld Point features that have the same connected part combinations.  
           Connected parts A-B-C and C-B-A will be in the same group.   
         
        """
        pass
    @CreateFeatureGroups.setter
    def CreateFeatureGroups(self, createFeatureGroups: bool):
        """
        Setter for property: (bool) CreateFeatureGroups
         Returns the option to create Feature Group features to collect Weld Point features that have the same connected part combinations.  
           Connected parts A-B-C and C-B-A will be in the same group.   
         
        """
        pass
    @property
    def InputFile(self) -> str:
        """
        Getter for property: (str) InputFile
         Returns the input csv file   
            
         
        """
        pass
    @InputFile.setter
    def InputFile(self, filename: str):
        """
        Setter for property: (str) InputFile
         Returns the input csv file   
            
         
        """
        pass
    @property
    def TemplateFile(self) -> str:
        """
        Getter for property: (str) TemplateFile
         Returns the template file indicating attribute mapping.  
             
         
        """
        pass
    @TemplateFile.setter
    def TemplateFile(self, filename: str):
        """
        Setter for property: (str) TemplateFile
         Returns the template file indicating attribute mapping.  
             
         
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Die
import NXOpen.Routing
class WeldJointBuilder(StructureWeldBuilder): 
    """ Used to create or edit a NXOpen.Weld.WeldJoint feature. """
    class Application(Enum):
        """
        Members Include: 
         |StructureWelding|  Structure Welding Application.   
         |Routing|  Routing Application. 
         |StructureDesign|  Structure Design Application. 

        """
        StructureWelding: int
        Routing: int
        StructureDesign: int
        @staticmethod
        def ValueOf(value: int) -> WeldJointBuilder.Application:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CoordinateSystem(Enum):
        """
        Members Include: 
         |Absolute|  Desired points and vectors should be in absolute coordinates.   
         |Ship|  Desired points and vectors should be in ship coordinate system. 

        """
        Absolute: int
        Ship: int
        @staticmethod
        def ValueOf(value: int) -> WeldJointBuilder.CoordinateSystem:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DestinationTypes(Enum):
        """
        Members Include: 
         |WorkPart|  Create new joints in work part. 
         |NewComponent|  Create a new componenent for each joint under the work part. 

        """
        WorkPart: int
        NewComponent: int
        @staticmethod
        def ValueOf(value: int) -> WeldJointBuilder.DestinationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SplitTypes(Enum):
        """
        Members Include: 
         |EqualSegments|  Specified number of equal segments. 
         |Limits|  At limits defined by NXOpen.Weld.WeldJointBuilder.LimitList. 
         |Angle|  At specifed angle. 
         |ComputedAngle|  At angle computed from geometry and tables. 
         |Length|  At equal arc length. 
         |NotSet|  No split. 
         |Skip|  Skip joint, defined by segment length and spacing length. 
         |SkipNumberLength|  Skip joint, defined by number of skips and segment length. 
         |SkipLengthPitch|  Skip joint, defined by segment length and minimum ptich. 

        """
        EqualSegments: int
        Limits: int
        Angle: int
        ComputedAngle: int
        Length: int
        NotSet: int
        Skip: int
        SkipNumberLength: int
        SkipLengthPitch: int
        @staticmethod
        def ValueOf(value: int) -> WeldJointBuilder.SplitTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |CreateAutomatic|  Automatic weld joint creation. 
         |CreateManual|  Manual weld joint creation. 
         |CreateMultiple|  Create multiple weld joints from manual input. 
         |CreateAttributes|  Create weld joints from attributed ship structures data. 
         |CreateSingleSided|  Create multiple single sided weld joints from manual input. 

        """
        CreateAutomatic: int
        CreateManual: int
        CreateMultiple: int
        CreateAttributes: int
        CreateSingleSided: int
        @staticmethod
        def ValueOf(value: int) -> WeldJointBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class WeldTypes(Enum):
        """
        Members Include: 
         |Any|  Any Joint type. 
         |Groove|  Groove joint. 
         |Fillet|  T-Joint. 
         |Corner|  Corner joint. 
         |Lap|  Lap joint. 
         |Socket|  Socket joint for pipe welding. 
         |Mechanical|  Mechanical joint for pipe welding. 
         |Sleeve|  Sleeve joint for pipe welding. 
         |Boss|  Boss joint for pipe welding. 

        """
        Any: int
        Groove: int
        Fillet: int
        Corner: int
        Lap: int
        Socket: int
        Mechanical: int
        Sleeve: int
        Boss: int
        @staticmethod
        def ValueOf(value: int) -> WeldJointBuilder.WeldTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class JointMidPointData:
        """
         Joint evaluation information at the mid point. Results are returned in absolute and ship coordinates 
         WeldJointBuilderJointMidPointData_Struct NXOpe is an alias for  WeldJointBuilder.JointMidPointData NXOpe.
        """
        @property
        def JointMidPoint(self) -> NXOpen.Point3d:
            """
            Getter for property JointMidPoint
            The mid point of the joint in absolute coordinates.

            """
            pass
        @JointMidPoint.setter
        def JointMidPoint(self, value: NXOpen.Point3d):
            """
            Getter for property JointMidPoint
            The mid point of the joint in absolute coordinates.
            Setter for property JointMidPoint
            The mid point of the joint in absolute coordinates.

            """
            pass
        @property
        def JointTangent(self) -> NXOpen.Vector3d:
            """
            Getter for property JointTangent
            The tangent at the joint mid point in absolute coordinates.

            """
            pass
        @JointTangent.setter
        def JointTangent(self, value: NXOpen.Vector3d):
            """
            Getter for property JointTangent
            The tangent at the joint mid point in absolute coordinates.
            Setter for property JointTangent
            The tangent at the joint mid point in absolute coordinates.

            """
            pass
        @property
        def PrimaryFaceNormal(self) -> NXOpen.Vector3d:
            """
            Getter for property PrimaryFaceNormal
            The primary body face normal in absolute coordinates at the joint mid point.

            """
            pass
        @PrimaryFaceNormal.setter
        def PrimaryFaceNormal(self, value: NXOpen.Vector3d):
            """
            Getter for property PrimaryFaceNormal
            The primary body face normal in absolute coordinates at the joint mid point.
            Setter for property PrimaryFaceNormal
            The primary body face normal in absolute coordinates at the joint mid point.

            """
            pass
        @property
        def SecondaryFaceNormal(self) -> NXOpen.Vector3d:
            """
            Getter for property SecondaryFaceNormal
            The secondary body face normal in absolute coordinates at the joint mid point.

            """
            pass
        @SecondaryFaceNormal.setter
        def SecondaryFaceNormal(self, value: NXOpen.Vector3d):
            """
            Getter for property SecondaryFaceNormal
            The secondary body face normal in absolute coordinates at the joint mid point.
            Setter for property SecondaryFaceNormal
            The secondary body face normal in absolute coordinates at the joint mid point.

            """
            pass
        @property
        def GroovePrimaryDirection(self) -> NXOpen.Vector3d:
            """
            Getter for property GroovePrimaryDirection
            The direction in absolute coordinates towards the primary faces, and way from secondary faces.

            """
            pass
        @GroovePrimaryDirection.setter
        def GroovePrimaryDirection(self, value: NXOpen.Vector3d):
            """
            Getter for property GroovePrimaryDirection
            The direction in absolute coordinates towards the primary faces, and way from secondary faces.
            Setter for property GroovePrimaryDirection
            The direction in absolute coordinates towards the primary faces, and way from secondary faces.

            """
            pass
        @property
        def GrooveAlignedWithPrimary(self) -> bool:
            """
            Getter for property GrooveAlignedWithPrimary
            Indicates if the primary faces for the groove are farthest along a positive principal axis.

            """
            pass
        @GrooveAlignedWithPrimary.setter
        def GrooveAlignedWithPrimary(self, value: bool):
            """
            Getter for property GrooveAlignedWithPrimary
            Indicates if the primary faces for the groove are farthest along a positive principal axis.
            Setter for property GrooveAlignedWithPrimary
            Indicates if the primary faces for the groove are farthest along a positive principal axis.

            """
            pass
    @property
    def AssociativeSplit(self) -> bool:
        """
        Getter for property: (bool) AssociativeSplit
         Returns whether split joints should be associative   
            
         
        """
        pass
    @AssociativeSplit.setter
    def AssociativeSplit(self, status: bool):
        """
        Setter for property: (bool) AssociativeSplit
         Returns whether split joints should be associative   
            
         
        """
        pass
    @property
    def BackingFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BackingFace
         Returns the backing face.  
           
                    This should only be used when creating a  NXOpen::Weld::WeldJoint  feature.  
                    When editing a feature the  NXOpen::Weld::JointItemBuilder::BackingFace  of the  NXOpen::Weld::JointItemBuilder  should be used
                    to access the data.  
         
        """
        pass
    @property
    def BossColorFontWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) BossColorFontWidth
         Returns the color, font, and width of the boss joint curves.  
            
         
        """
        pass
    @property
    def ButtColorFontWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) ButtColorFontWidth
         Returns the color, font, and width of the butt joint curves.  
            
         
        """
        pass
    @property
    def CombineConnectedJoints(self) -> bool:
        """
        Getter for property: (bool) CombineConnectedJoints
         Returns the indication to combine connected joints if they belong to the same body   
            
         
        """
        pass
    @CombineConnectedJoints.setter
    def CombineConnectedJoints(self, status: bool):
        """
        Setter for property: (bool) CombineConnectedJoints
         Returns the indication to combine connected joints if they belong to the same body   
            
         
        """
        pass
    @property
    def CornerColorFontWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) CornerColorFontWidth
         Returns the color, font, and width of the corner joint curves.  
            
         
        """
        pass
    @property
    def CreateMethod(self) -> WeldJointBuilder.Types:
        """
        Getter for property: ( WeldJointBuilder.Types NXOpe) CreateMethod
         Returns the creation method   
            
         
        """
        pass
    @CreateMethod.setter
    def CreateMethod(self, type: WeldJointBuilder.Types):
        """
        Setter for property: ( WeldJointBuilder.Types NXOpe) CreateMethod
         Returns the creation method   
            
         
        """
        pass
    @property
    def CreatedApplication(self) -> WeldJointBuilder.Application:
        """
        Getter for property: ( WeldJointBuilder.Application NXOpe) CreatedApplication
         Returns the application where joint is created   
            
         
        """
        pass
    @CreatedApplication.setter
    def CreatedApplication(self, application: WeldJointBuilder.Application):
        """
        Setter for property: ( WeldJointBuilder.Application NXOpe) CreatedApplication
         Returns the application where joint is created   
            
         
        """
        pass
    @property
    def Destination(self) -> WeldJointBuilder.DestinationTypes:
        """
        Getter for property: ( WeldJointBuilder.DestinationTypes NXOpe) Destination
         Returns the destination to create new joints   
            
         
        """
        pass
    @Destination.setter
    def Destination(self, type: WeldJointBuilder.DestinationTypes):
        """
        Setter for property: ( WeldJointBuilder.DestinationTypes NXOpe) Destination
         Returns the destination to create new joints   
            
         
        """
        pass
    @property
    def DuplicateCheck(self) -> bool:
        """
        Getter for property: (bool) DuplicateCheck
         Returns the indication to not allow new joints to be created if they are duplicates of exising joints   
            
         
        """
        pass
    @DuplicateCheck.setter
    def DuplicateCheck(self, status: bool):
        """
        Setter for property: (bool) DuplicateCheck
         Returns the indication to not allow new joints to be created if they are duplicates of exising joints   
            
         
        """
        pass
    @property
    def Joint(self) -> NXOpen.SelectCurveList:
        """
        Getter for property: ( NXOpen.SelectCurveList) Joint
         Returns the welding joint curves.  
             
         
        """
        pass
    @property
    def JointList(self) -> JointItemBuilderList:
        """
        Getter for property: ( JointItemBuilderList NXOpe) JointList
         Returns the list of  NXOpen::Weld::JointItemBuilder  objects.  
           
                    When editing a  NXOpen::Weld::WeldJoint  the  NXOpen::Weld::WeldJointBuilder::Joint  should be used
                    to access the output curves of the feature.   NXOpen::Weld::WeldJointBuilder::GetSingleJoint  is then used to access the 
                     NXOpen::Weld::JointItemBuilder  from the curve.    
         
        """
        pass
    @property
    def JointPrefix(self) -> str:
        """
        Getter for property: (str) JointPrefix
         Returns the prefix for the weld ID attribute, and the prefix for the name of the component if  NXOpen::Weld::WeldJointBuilder::DestinationTypes  is   NXOpen::Weld::WeldJointBuilder::DestinationTypesNewComponent      
            
         
        """
        pass
    @JointPrefix.setter
    def JointPrefix(self, prefix: str):
        """
        Setter for property: (str) JointPrefix
         Returns the prefix for the weld ID attribute, and the prefix for the name of the component if  NXOpen::Weld::WeldJointBuilder::DestinationTypes  is   NXOpen::Weld::WeldJointBuilder::DestinationTypesNewComponent      
            
         
        """
        pass
    @property
    def LapColorFontWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) LapColorFontWidth
         Returns the color, font, and width of the lap joint curves.  
            
         
        """
        pass
    @property
    def LimitList(self) -> NXOpen.Die.DieLimitsBuilderList:
        """
        Getter for property: ( NXOpen.Die.DieLimitsBuilderList) LimitList
         Returns the list of limit builders.  
             
         
        """
        pass
    @property
    def Limits(self) -> NXOpen.Die.DieLimitsBuilder:
        """
        Getter for property: ( NXOpen.Die.DieLimitsBuilder) Limits
         Returns the limits of the joint curve span.  
             
         
        """
        pass
    @property
    def MasterEdge(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) MasterEdge
         Returns the master edge of a fillet weld.  
           This should only be used when creating a  NXOpen::Weld::WeldJoint  feature.  
                    When editing a feature the  NXOpen::Weld::JointItemBuilder::MasterEdge  of the  NXOpen::Weld::JointItemBuilder  should be used
                    to access the data.  
         
        """
        pass
    @property
    def MaximumFaceGap(self) -> float:
        """
        Getter for property: (float) MaximumFaceGap
         Returns the maximum face gap used when determining if two bodies intersect.  
             
         
        """
        pass
    @MaximumFaceGap.setter
    def MaximumFaceGap(self, gapValue: float):
        """
        Setter for property: (float) MaximumFaceGap
         Returns the maximum face gap used when determining if two bodies intersect.  
             
         
        """
        pass
    @property
    def MechanicalColorFontWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) MechanicalColorFontWidth
         Returns the color, font, and width of the mechanical joint curves.  
            
         
        """
        pass
    @property
    def NamePrefix(self) -> str:
        """
        Getter for property: (str) NamePrefix
         Returns the prefix used for the welding joint Design Feature name in Collaborative Product Development mode    
            
         
        """
        pass
    @NamePrefix.setter
    def NamePrefix(self, prefix: str):
        """
        Setter for property: (str) NamePrefix
         Returns the prefix used for the welding joint Design Feature name in Collaborative Product Development mode    
            
         
        """
        pass
    @property
    def NumberSegments(self) -> int:
        """
        Getter for property: (int) NumberSegments
         Returns the number of segments to divide a joint when using   NXOpen::Weld::WeldJointBuilder::SplitTypesEqualSegments   or
                      NXOpen::Weld::WeldJointBuilder::SplitTypesSkipNumberLength  .  
             
         
        """
        pass
    @NumberSegments.setter
    def NumberSegments(self, numberSegments: int):
        """
        Setter for property: (int) NumberSegments
         Returns the number of segments to divide a joint when using   NXOpen::Weld::WeldJointBuilder::SplitTypesEqualSegments   or
                      NXOpen::Weld::WeldJointBuilder::SplitTypesSkipNumberLength  .  
             
         
        """
        pass
    @property
    def PlacementFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) PlacementFace
         Returns the placement face of a fillet weld.  
           For example, on a profile it is the face that touches the plate. 
                    This should only be used when creating a  NXOpen::Weld::WeldJoint  feature.  
                    When editing a feature the  NXOpen::Weld::JointItemBuilder::PlacementFace  of the  NXOpen::Weld::JointItemBuilder  should be used
                    to access the data.  
         
        """
        pass
    @property
    def PrimaryEdge(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) PrimaryEdge
         Returns the primary edge of a butt weld.  
           
                    This should only be used when creating a  NXOpen::Weld::WeldJoint  feature.  
                    When editing a feature the  NXOpen::Weld::JointItemBuilder::PrimaryEdge  of the  NXOpen::Weld::JointItemBuilder  should be used
                    to access the data.  
         
        """
        pass
    @property
    def PrimaryFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) PrimaryFace
         Returns the primary face of a butt weld.  
           
                    This should only be used when creating a  NXOpen::Weld::WeldJoint  feature.  
                    When editing a feature the  NXOpen::Weld::JointItemBuilder::PrimaryFace  of the  NXOpen::Weld::JointItemBuilder  should be used
                    to access the data.  
         
        """
        pass
    @property
    def SecondaryEdge(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SecondaryEdge
         Returns the secondary edge of a butt weld.  
           
                    This should only be used when creating a  NXOpen::Weld::WeldJoint  feature.  
                    When editing a feature the  NXOpen::Weld::JointItemBuilder::SecondaryEdge  of the  NXOpen::Weld::JointItemBuilder  should be used
                    to access the data.  
         
        """
        pass
    @property
    def SecondaryFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SecondaryFace
         Returns the secondary face of a butt weld.  
           
                    This should only be used when creating a  NXOpen::Weld::WeldJoint  feature.  
                    When editing a feature the  NXOpen::Weld::JointItemBuilder::SecondaryFace  of the  NXOpen::Weld::JointItemBuilder  should be used
                    to access the data.  
         
        """
        pass
    @property
    def ShipComponent(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) ShipComponent
         Returns the components on which the welding joints will be created.  
           Used when  NXOpen::Weld::WeldJointBuilder::Types .
                    is set to   NXOpen::Weld::WeldJointBuilder::TypesCreateAutomatic   or 
                      NXOpen::Weld::WeldJointBuilder::TypesCreateAttributes  
                    After setting the components,  NXOpen::Weld::WeldJointBuilder::ShowJoints  should be called to create the welding joints.   
         
        """
        pass
    @property
    def SleeveColorFontWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) SleeveColorFontWidth
         Returns the color, font, and width of the sleeve joint curves.  
            
         
        """
        pass
    @property
    def SocketColorFontWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) SocketColorFontWidth
         Returns the color, font, and width of the socket joint curves.  
            
         
        """
        pass
    @property
    def SpacingLength(self) -> float:
        """
        Getter for property: (float) SpacingLength
         Returns the spacing length when using   NXOpen::Weld::WeldJointBuilder::SplitTypesSkip   or
                    the minium pitch when using   NXOpen::Weld::WeldJointBuilder::SplitTypesSkipNumberLength  
                    or   NXOpen::Weld::WeldJointBuilder::SplitTypesSkipLengthPitch  .  
            
         
        """
        pass
    @SpacingLength.setter
    def SpacingLength(self, length: float):
        """
        Setter for property: (float) SpacingLength
         Returns the spacing length when using   NXOpen::Weld::WeldJointBuilder::SplitTypesSkip   or
                    the minium pitch when using   NXOpen::Weld::WeldJointBuilder::SplitTypesSkipNumberLength  
                    or   NXOpen::Weld::WeldJointBuilder::SplitTypesSkipLengthPitch  .  
            
         
        """
        pass
    @property
    def SplitAngle(self) -> float:
        """
        Getter for property: (float) SplitAngle
         Returns the split angle to divide a joint when using   NXOpen::Weld::WeldJointBuilder::SplitTypesAngle  .  
            
         
        """
        pass
    @SplitAngle.setter
    def SplitAngle(self, angle: float):
        """
        Setter for property: (float) SplitAngle
         Returns the split angle to divide a joint when using   NXOpen::Weld::WeldJointBuilder::SplitTypesAngle  .  
            
         
        """
        pass
    @property
    def SplitLength(self) -> float:
        """
        Getter for property: (float) SplitLength
         Returns the segment length when using   NXOpen::Weld::WeldJointBuilder::SplitTypesSkip  .  
            
         
        """
        pass
    @SplitLength.setter
    def SplitLength(self, length: float):
        """
        Setter for property: (float) SplitLength
         Returns the segment length when using   NXOpen::Weld::WeldJointBuilder::SplitTypesSkip  .  
            
         
        """
        pass
    @property
    def SplitOption(self) -> WeldJointBuilder.SplitTypes:
        """
        Getter for property: ( WeldJointBuilder.SplitTypes NXOpe) SplitOption
         Returns the method used to split the joint   
            
         
        """
        pass
    @SplitOption.setter
    def SplitOption(self, option: WeldJointBuilder.SplitTypes):
        """
        Setter for property: ( WeldJointBuilder.SplitTypes NXOpe) SplitOption
         Returns the method used to split the joint   
            
         
        """
        pass
    @property
    def SubsetPart(self) -> NXOpen.Part:
        """
        Getter for property: ( NXOpen.Part) SubsetPart
         Returns the subset part where Design Control Elements are to be created   
            
         
        """
        pass
    @SubsetPart.setter
    def SubsetPart(self, part: NXOpen.Part):
        """
        Setter for property: ( NXOpen.Part) SubsetPart
         Returns the subset part where Design Control Elements are to be created   
            
         
        """
        pass
    @property
    def TJointColorFontWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) TJointColorFontWidth
         Returns the color, font, and width of the T-joint curves.  
            
         
        """
        pass
    @property
    def TargetFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) TargetFace
         Returns the target face of a fillet weld.  
            For example, the plate face that the profile lies on. 
                    This should only be used when creating a  NXOpen::Weld::WeldJoint  feature.  
                    When editing a feature the  NXOpen::Weld::JointItemBuilder::TargetFace  of the  NXOpen::Weld::JointItemBuilder  should be used
                    to access the data.  
         
        """
        pass
    @property
    def Type(self) -> WeldJointBuilder.Types:
        """
        Getter for property: ( WeldJointBuilder.Types NXOpe) Type
         Returns the creation type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: WeldJointBuilder.Types):
        """
        Setter for property: ( WeldJointBuilder.Types NXOpe) Type
         Returns the creation type   
            
         
        """
        pass
    @property
    def WeldType(self) -> WeldJointBuilder.WeldTypes:
        """
        Getter for property: ( WeldJointBuilder.WeldTypes NXOpe) WeldType
         Returns the weld type   
            
         
        """
        pass
    @WeldType.setter
    def WeldType(self, type: WeldJointBuilder.WeldTypes):
        """
        Setter for property: ( WeldJointBuilder.WeldTypes NXOpe) WeldType
         Returns the weld type   
            
         
        """
        pass
    @property
    def WeldingCharacteristics(self) -> CharacteristicsBuilder:
        """
        Getter for property: ( CharacteristicsBuilder NXOpe) WeldingCharacteristics
         Returns the collection of welding characteristics defined by attributes.  
             
         
        """
        pass
    @property
    def WorkPart(self) -> NXOpen.Part:
        """
        Getter for property: ( NXOpen.Part) WorkPart
         Returns the saved work part   
            
         
        """
        pass
    @WorkPart.setter
    def WorkPart(self, part: NXOpen.Part):
        """
        Setter for property: ( NXOpen.Part) WorkPart
         Returns the saved work part   
            
         
        """
        pass
    def AddCharacteristicsInheritaceInformation(self) -> None:
        """
         Add welding characteristics inheritance information.  
        """
        pass
    def CopyLimits(self, limits: NXOpen.Die.DieLimitsBuilder) -> None:
        """
         Copy input limits to builder limits 
        """
        pass
    def CreateLimitsPath(self, jointCurve: NXOpen.Curve) -> NXOpen.Curve:
        """
         Creates the path to be used for the limits. 
         Returns path ( NXOpen.Curve):  Resulting path. .
        """
        pass
    def CreateSingleJointFromFeature(self, featureCurve: NXOpen.Curve, updateBuilder: bool) -> None:
        """
         Creates a joint from a feature. 
        """
        pass
    def Delete(self) -> None:
        """
         Deletes all joints set by NXOpen.Weld.WeldJointBuilder.Joint. 
        """
        pass
    def DeleteAllUnMarkedJoints(self) -> None:
        """
         Deletes any joints that were not marked with a call to NXOpen.Weld.WeldJointBuilder.MarkJointsToKeep.  
        """
        pass
    def DeleteCharacteristicsInheritaceInformation(self) -> None:
        """
         Delete welding characteristics inheritance information.  
        """
        pass
    def FindPortsInParts(self, parts: List[NXOpen.Assemblies.Component]) -> List[NXOpen.Routing.Port]:
        """
         Gets ports from the parts. 
         Returns ports ( NXOpen.Routing.Port Li):  the collection of ports in the parts .
        """
        pass
    def GetAngleBetween(self) -> float:
        """
         Gets the angle between the fillet weld mold faces, and the target faces, or butt weld primary and secondary faces. 
         Returns angleBetween (float): .
        """
        pass
    def GetConnectedParts(self) -> List[NXOpen.Assemblies.Component]:
        """
         Gets connected parts for joint. Only connected parts that are partially or fully loaded will be returned. Any components that are unloaded will not be returned. 
         Returns parts ( NXOpen.Assemblies.Component Li):  .
        """
        pass
    def GetIsLongPoint(self) -> bool:
        """
         Gets the long point status. A long point indicates only trimming and no extension is needed to to meeting the body being welded to. 
         Returns isLongPoint (bool): .
        """
        pass
    def GetJointChanged(self, curve: NXOpen.Curve) -> bool:
        """
         Indicates whether joint was changed. 
         Returns changed (bool): .
        """
        pass
    def GetJointLimits(self, curve: NXOpen.Curve) -> NXOpen.Die.DieLimitsBuilder:
        """
         Get the limits of an individual joint. 
         Returns limits ( NXOpen.Die.DieLimitsBuilder): .
        """
        pass
    def GetMidPointInformation(self, desiredCoordinateSystem: WeldJointBuilder.CoordinateSystem) -> Tuple[bool, WeldJointBuilder.JointMidPointData]:
        """
         Gets the joint curve mid point, tangent, and face normals at the mid point from the primary and secondary bodies. 
         Returns A tuple consisting of (success, jointMidPointData). 
         - success is: bool. Equals true if data was returned. .
         - jointMidPointData is:  WeldJointBuilder.JointMidPointData NXOpe. The joint mid point, tangent and face normals. .

        """
        pass
    def GetNewlyCreatedJoints(self) -> Tuple[List[NXOpen.Curve], List[JointItemBuilder]]:
        """
        Gets the NXOpen.Weld.JointItemBuilder objects and curves which were just created by NXOpen.Weld.WeldJointBuilder.ShowJoints.
         Returns A tuple consisting of (curves, newItemBuilder). 
         - curves is:  NXOpen.Curve Li. .
         - newItemBuilder is:  JointItemBuilder List[NXO. .

        """
        pass
    def GetPrimaryThickness(self, curve: NXOpen.Curve) -> float:
        """
         Gets the primary thickness for a specified joint 
         Returns primaryThickness (float): .
        """
        pass
    def GetSecondaryThickness(self, curve: NXOpen.Curve) -> float:
        """
         Gets the primary secondary for a specified joint 
         Returns secondaryThickness (float): .
        """
        pass
    def GetSingleJoint(self, curve: NXOpen.Curve) -> JointItemBuilder:
        """
         Gets the NXOpen.Weld.JointItemBuilder object associated to the input curve. 
         Returns singleJoint ( JointItemBuilder NXOpe): .
        """
        pass
    def GetVariableBevelAngles(self) -> List[float]:
        """
         Gets variable bevel angles.  This method is for use with the variable bevel callback. 
         Returns variableAngles (List[float]):  .
        """
        pass
    def IsCornerOpen(self) -> bool:
        """
         Returns status value of true if corner joint is an open case which means the placement face only touches the target face at the master edge. 
         Returns status (bool): .
        """
        pass
    def IsPipeJoint(self) -> bool:
        """
         Returns status value of true if this is a pipe welding joint. 
         Returns status (bool): .
        """
        pass
    def MarkJointsToKeep(self) -> None:
        """
         Marks all currently created welding joints so they do not get deleted when NXOpen.Weld.WeldJointBuilder.DeleteAllUnMarkedJoints is called from the dialog.  
        """
        pass
    def NewItem(self) -> JointItemBuilder:
        """
         Creates a NXOpen.Weld.JointItemBuilder object. 
         Returns newItemBuilder ( JointItemBuilder NXOpe): .
        """
        pass
    def ProcessCreatedJoints(self) -> None:
        """
         Creates NXOpen.Die.DieLimitsBuilder for all newly created NXOpen.Weld.JointItemBuilder. 
        """
        pass
    def SetCallbackMessage(self, message: str) -> None:
        """
         Sets a message to display after callback processing ends 
        """
        pass
    def SetErrorMessage(self, message: str) -> None:
        """
         Sets an error message to display 
        """
        pass
    def SetJointChanged(self, curve: NXOpen.Curve, changed: bool) -> None:
        """
         Indicate that joint was changed. 
        """
        pass
    def SetVariableBevelAngles(self, variableAngles: List[float]) -> None:
        """
         This method is for use with the variable bevel callback. 
        """
        pass
    def ShowJoints(self) -> None:
        """
         Show joints will create joints using the method set by  NXOpen.Weld.WeldJointBuilder.Types .
                    For  NXOpen.Weld.WeldJointBuilder.Types.CreateAutomatic  and  NXOpen.Weld.WeldJointBuilder.Types.CreateAttributes 
                    components need to be set using NXOpen.Weld.WeldJointBuilder.ShipComponent.  For  NXOpen.Weld.WeldJointBuilder.Types.CreateManual ,
                    the following need to be set:
                    When NXOpen.Weld.WeldJointBuilder.WeldTypes is  NXOpen.Weld.WeldJointBuilder.WeldTypes.Fillet , the following 
                    methods need to be called to set the input data: NXOpen.Weld.WeldJointBuilder.MasterEdge, NXOpen.Weld.WeldJointBuilder.PlacementFace,
                     NXOpen.Weld.WeldJointBuilder.TargetFace .  
                    When NXOpen.Weld.WeldJointBuilder.WeldTypes is  NXOpen.Weld.WeldJointBuilder.WeldTypes.Groove , the following 
                    methods need to be called to set the input data: NXOpen.Weld.WeldJointBuilder.PrimaryFace, NXOpen.Weld.WeldJointBuilder.PrimaryEdge,
                     NXOpen.Weld.WeldJointBuilder.SecondaryFace ,  NXOpen.Weld.WeldJointBuilder.SecondaryEdge . 
        """
        pass
    def Split(self) -> None:
        """
         Splits all joints set by NXOpen.Weld.WeldJointBuilder.Joint defined by  NXOpen.Weld.WeldJointBuilder.SplitTypes .  
        """
        pass
    def UpdateCollectors(self, jointCurve: NXOpen.Curve) -> None:
        """
         Updates the main collectors by copying data from Joint. 
        """
        pass
    @overload
    def UpdateJointAfterLimitsChange(self) -> None:
        """
         Updates the joint curve after the limits change. 
        """
        pass
    @overload
    def UpdateJointAfterLimitsChange(self, limits: NXOpen.Die.DieLimitsBuilder) -> None:
        """
         Updates the joint curve after the limits change. 
        """
        pass
    def UpdateJointType(self, type: WeldJointBuilder.WeldTypes) -> None:
        """
         Updates all joints set by NXOpen.Weld.WeldJointBuilder.Joint to have the given type.  
        """
        pass
import NXOpen.Features
class WeldJoint(NXOpen.Features.BodyFeature): 
    """ Represents a weld joint feature """
    pass
import NXOpen
import NXOpen.Annotations
class WeldLabelBuilder(NXOpen.Builder): 
    """ Create weld labels for multiple welds and BIW locators, this builder's Commit can produce more than one object, 
        the GetCommittedObjects can be used to get the objects and the order of GetCommittedObject's output array is stable. """
    class OrientationPlaneType(Enum):
        """
        Members Include: 
         |XYPlane| 
         |XZPlane| 
         |YZPlane| 
         |ModelView| 
         |LastUserDefined| 
         |UserDefined| 

        """
        XYPlane: int
        XZPlane: int
        YZPlane: int
        ModelView: int
        LastUserDefined: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> WeldLabelBuilder.OrientationPlaneType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
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
    def Leader(self) -> NXOpen.Annotations.LeaderBuilder:
        """
        Getter for property: ( NXOpen.Annotations.LeaderBuilder) Leader
         Returns the  NXOpen::Annotations::LeaderBuilder  for the annotation   
            
         
        """
        pass
    @property
    def Objects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Objects
         Returns the objects that are used to create labels.  
             
         
        """
        pass
    @property
    def Origin(self) -> NXOpen.Annotations.OriginBuilder:
        """
        Getter for property: ( NXOpen.Annotations.OriginBuilder) Origin
         Returns the  NXOpen::Annotations::OriginBuilder  for the annotation   
            
         
        """
        pass
    @property
    def PlaneType(self) -> WeldLabelBuilder.OrientationPlaneType:
        """
        Getter for property: ( WeldLabelBuilder.OrientationPlaneType NXOpe) PlaneType
         Returns the plane type.  
             
         
        """
        pass
    @PlaneType.setter
    def PlaneType(self, planeType: WeldLabelBuilder.OrientationPlaneType):
        """
        Setter for property: ( WeldLabelBuilder.OrientationPlaneType NXOpe) PlaneType
         Returns the plane type.  
             
         
        """
        pass
    @property
    def Style(self) -> NXOpen.Annotations.StyleBuilder:
        """
        Getter for property: ( NXOpen.Annotations.StyleBuilder) Style
         Returns the  NXOpen::Annotations::StyleBuilder  for the annotation   
            
         
        """
        pass
    @property
    def Text(self) -> NXOpen.Annotations.TextWithEditControlsBuilder:
        """
        Getter for property: ( NXOpen.Annotations.TextWithEditControlsBuilder) Text
         Returns the  NXOpen::Annotations::TextWithEditControlsBuilder  for the annotation   
            
         
        """
        pass
    @property
    def UserCsys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) UserCsys
         Returns the user specified coordinate system.  
             
         
        """
        pass
    @UserCsys.setter
    def UserCsys(self, userCsys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) UserCsys
         Returns the user specified coordinate system.  
             
         
        """
        pass
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
class WeldManager(NXOpen.TaggedObjectCollection): 
    """ Manages weld features and assistant tools. """
    class SearchOption(Enum):
        """
        Members Include: 
         |DesignFeatureAndDesignControlElement|  search design feature and design control element 
         |DesignFeature|  search design feature only 
         |DesignControlElement|  search design control element only 

        """
        DesignFeatureAndDesignControlElement: int
        DesignFeature: int
        DesignControlElement: int
        @staticmethod
        def ValueOf(value: int) -> WeldManager.SearchOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def CreateAutoPointBuilder(self, unused: NXOpen.Features.Feature) -> AutoPointBuilder:
        """
         Creates a NXOpen.Weld.AutoPointBuilder object. 
         Returns builder ( AutoPointBuilder NXOpe):  AutoPoint assistant builder.
        """
        pass
    def CreateAutoWeldSymbolsBuilder(self) -> AutoWeldSymbolsBuilder:
        """
         Creates a NXOpen.Weld.AutoWeldSymbolsBuilder object. 
         Returns builder ( AutoWeldSymbolsBuilder NXOpe):  Auto Weld Symbol assistant builder.
        """
        pass
    def CreateBeadDesignFeature(self) -> None:
        """
         Create a Weld Bead Design Feature part and make it the session work part.
               The design feature will be created in the active subset work part. 
        """
        pass
    @overload
    def CreateCharacteristicsBuilder(self, objectValue: NXOpen.NXObject, weldType: int) -> CharacteristicsBuilder:
        """
         Creates a NXOpen.Weld.CharacteristicsBuilder, used to specify
               welding characteristics for any welding feature. 
         Returns builder ( CharacteristicsBuilder NXOpe): .
        """
        pass
    @overload
    def CreateCharacteristicsBuilder(self, objectValue: NXOpen.NXObject, charxType: CharacteristicsBuilder.Type) -> CharacteristicsBuilder:
        """
         Creates a NXOpen.Weld.CharacteristicsBuilder, used to specify
               welding characteristics for any welding feature. 
         Returns builder ( CharacteristicsBuilder NXOpe): .
        """
        pass
    def CreateCompoundWeldBuilder(self, compound_weld: CompoundWeld) -> CompoundWeldBuilder:
        """
         Creates a NXOpen.Weld.CompoundWeldBuilder 
         Returns builder ( CompoundWeldBuilder NXOpe):  .
        """
        pass
    def CreateConnectedFaceFinderBuilder(self, weldFeatures: List[NXOpen.Features.Feature]) -> ConnectedFaceFinderBuilder:
        """
         Creates a builder for running the Connected Face Finder utility.
            Only used internally for Mirror or Transform on the fly. 
         Returns builder ( ConnectedFaceFinderBuilder NXOpe):  .
        """
        pass
    def CreateConnectedFaceFinderBuilder2(self, ignoreHoles: bool, weldFeatures: List[NXOpen.Features.Feature]) -> ConnectedFaceFinderBuilder:
        """
         Creates a builder for running the Connected Face Finder utility.
               Used internally for From Existing Points, Mirror or Transform on the fly. 
         Returns builder ( ConnectedFaceFinderBuilder NXOpe):  .
        """
        pass
    def CreateConnectedFaceFinderOperation(self) -> ConnectedFaceFinderBuilder:
        """
         Creates a builder for running the Connected Face Finder utility. 
         Returns builder ( ConnectedFaceFinderBuilder NXOpe):  .
        """
        pass
    def CreateDatumEdgeBuilder(self, feature: DatumEdge) -> DatumEdgeBuilder:
        """
         Creates a NXOpen.Weld.DatumEdgeBuilder object. 
         Returns builder ( DatumEdgeBuilder NXOpe): .
        """
        pass
    def CreateDatumPinBuilder(self, feature: DatumPin) -> DatumPinBuilder:
        """
         Creates a NXOpen.Weld.DatumPinBuilder object. 
         Returns builder ( DatumPinBuilder NXOpe): .
        """
        pass
    def CreateDatumSurfaceBuilder(self, feature: DatumSurface) -> DatumSurfaceBuilder:
        """
         Creates a NXOpen.Weld.DatumSurfaceBuilder object. 
         Returns builder ( DatumSurfaceBuilder NXOpe): .
        """
        pass
    def CreateEasyPatternBuilder(self, pattern_feature_set: NXOpen.Features.Feature) -> EasyPatternBuilder:
        """
         Creates a NXOpen.Weld.EasyPatternBuilder object. 
         Returns builder ( EasyPatternBuilder NXOpe):  EasyPattern assistant builder.
        """
        pass
    def CreateEdgePrepBuilder(self, edge_prep_feature: EdgePrep) -> EdgePrepBuilder:
        """
         Creates a NXOpen.Weld.EdgePrepBuilder object. 
         Returns builder ( EdgePrepBuilder NXOpe): .
        """
        pass
    def CreateEdgePrepValuesBuilder(self) -> EdgePrepValuesBuilder:
        """
         Creates a NXOpen.Weld.EdgePrepValuesBuilder object. 
         Returns builder ( EdgePrepValuesBuilder NXOpe):  Edge Prep Values builder.
        """
        pass
    def CreateExportDpvBuilder(self) -> ExportDpvBuilder:
        """
         Creates a NXOpen.Weld.ExportDpvBuilder object. 
         Returns builder ( ExportDpvBuilder NXOpe):  ExportWeld assistant builder.
        """
        pass
    def CreateExportWeldBuilder(self) -> ExportWeldBuilder:
        """
         Creates a NXOpen.Weld.ExportWeldBuilder object. 
         Returns builder ( ExportWeldBuilder NXOpe):  ExportWeld assistant builder.
        """
        pass
    def CreateExportWeldJointBuilder(self) -> ExportWeldJointBuilder:
        """
         Creates a NXOpen.Weld.ExportWeldJointBuilder object. 
         Returns builder ( ExportWeldJointBuilder NXOpe):  Export Weld Joint builder.
        """
        pass
    def CreateFillBuilder(self, fillFeature: Fill) -> WeldFillBuilder:
        """
         Creates a NXOpen.Weld.WeldFillBuilder, used to create or edit
            a NXOpen.Weld.Fill feature. 
         Returns builder ( WeldFillBuilder NXOpe): .
        """
        pass
    def CreateFilletBuilder(self, feature: NXOpen.Features.Feature) -> FilletBuilder:
        """
         Creates a NXOpen.Weld.FilletBuilder object. 
         Returns builder ( FilletBuilder NXOpe): .
        """
        pass
    def CreateImportBuilder(self) -> WeldImportBuilder:
        """
         Creates a NXOpen.Weld.WeldImportBuilder object. 
         Returns builder ( WeldImportBuilder NXOpe):  Import weld builder .
        """
        pass
    def CreateInformationBuilder(self) -> InformationBuilder:
        """
         Creates a NXOpen.Weld.InformationBuilder 
         Returns builderTag ( InformationBuilder NXOpe): .
        """
        pass
    def CreateJointBuilder(self, weld_joint: WeldJoint) -> WeldJointBuilder:
        """
         Creates a NXOpen.Weld.WeldJointBuilder 
         Returns builder ( WeldJointBuilder NXOpe):  .
        """
        pass
    def CreateJointExitBuilder(self, weld_joint: WeldJoint) -> JointExitBuilder:
        """
         Creates a NXOpen.Weld.JointExitBuilder 
         Returns builder ( JointExitBuilder NXOpe):  .
        """
        pass
    def CreateJointExitBuilderCurve(self, curve: NXOpen.Curve) -> JointExitBuilder:
        """
         Creates a NXOpen.Weld.JointExitBuilder using the curve of a NXOpen.Weld.WeldJoint 
         Returns builder ( JointExitBuilder NXOpe):  .
        """
        pass
    def CreateJointmarkBuilder(self, jointmark_feature: Jointmark) -> JointmarkBuilder:
        """
         Creates a NXOpen.Weld.JointmarkBuilder object. 
         Returns builder ( JointmarkBuilder NXOpe): .
        """
        pass
    def CreateLocatorReferenceBuilder(self) -> LocatorReferenceBuilder:
        """
         Creates a NXOpen.Weld.LocatorReferenceBuilder 
         Returns builderTag ( LocatorReferenceBuilder NXOpe): .
        """
        pass
    def CreateMeasureHemBuilder(self, feature: MeasureHem) -> MeasureHemBuilder:
        """
         Creates a NXOpen.Weld.MeasureHemBuilder object. 
         Returns builder ( MeasureHemBuilder NXOpe): .
        """
        pass
    def CreateMeasureHoleBuilder(self, feature: MeasureHole) -> MeasureHoleBuilder:
        """
         Creates a NXOpen.Weld.MeasureHoleBuilder object. 
         Returns builder ( MeasureHoleBuilder NXOpe): .
        """
        pass
    def CreateMeasureSurfaceBuilder(self, measureSurface: MeasureSurface) -> MeasureSurfaceBuilder:
        """
         Creates a NXOpen.Weld.MeasureSurfaceBuilder object. 
         Returns builder ( MeasureSurfaceBuilder NXOpe): .
        """
        pass
    def CreateMeasureTrimBuilder(self, feature: MeasureTrim) -> MeasureTrimBuilder:
        """
         Creates a NXOpen.Weld.MeasureTrimBuilder object. 
         Returns builder ( MeasureTrimBuilder NXOpe): .
        """
        pass
    def CreatePlugSlotBuilder(self, feature: NXOpen.Features.Feature) -> PlugSlotBuilder:
        """
         Creates a NXOpen.Weld.PlugSlotBuilder object. 
         Returns builder ( PlugSlotBuilder NXOpe): .
        """
        pass
    def CreatePointMarkBuilder(self, pointMarkFeature: PointMark) -> PointMarkBuilder:
        """
         Creates a NXOpen.Weld.PointMarkBuilder object. 
         Returns builder ( PointMarkBuilder NXOpe): .
        """
        pass
    def CreatePreferenceBuilder(self) -> WeldPreferenceBuilder:
        """
         Creates a NXOpen.Weld.WeldPreferenceBuilder object. 
         Returns builder ( WeldPreferenceBuilder NXOpe):  WeldPref assistant builder.
        """
        pass
    def CreateSurfaceWeldBuilder(self, surface_weld: SurfaceWeld) -> SurfaceWeldBuilder:
        """
         Creates a NXOpen.Weld.SurfaceWeldBuilder 
         Returns builder ( SurfaceWeldBuilder NXOpe):  .
        """
        pass
    def CreateTransformBuilder(self, feature: Transform) -> TransformBuilder:
        """
         Creates a NXOpen.Weld.TransformBuilder object. 
         Returns builder ( TransformBuilder NXOpe): .
        """
        pass
    def CreateUserDefinedWeldBuilder(self, feature_set: NXOpen.Features.Feature) -> UserDefinedWeldBuilder:
        """
         Creates a NXOpen.Weld.UserDefinedWeldBuilder 
         Returns builder ( UserDefinedWeldBuilder NXOpe): .
        """
        pass
    def CreateWeldAdvisorBuilder(self) -> WeldAdvisorBuilder:
        """
         Creates a NXOpen.Weld.WeldAdvisorBuilder object. 
         Returns builder ( WeldAdvisorBuilder NXOpe):  Weld Advisor builder.
        """
        pass
    def CreateWeldBeadBuilder(self, bead_feature: NXOpen.Features.Feature) -> WeldBeadBuilder:
        """
         Creates a NXOpen.Weld.WeldBeadBuilder object. 
         Returns builder ( WeldBeadBuilder NXOpe): .
        """
        pass
    def CreateWeldGroove1Builder(self, groove_feature: NXOpen.Features.Feature) -> WeldGrooveBuilder:
        """
         Creates a NXOpen.Weld.WeldGrooveBuilder object. 
         Returns builder ( WeldGrooveBuilder NXOpe):      .
        """
        pass
    def CreateWeldGrooveBuilder(self, weld_groove: NXOpen.Features.Feature) -> GrooveBuilder:
        """
         Creates a NXOpen.Weld.GrooveBuilder object. 
         Returns builder ( GrooveBuilder NXOpe):  WeldGroove feature builder.
        """
        pass
    def CreateWeldLabelBuilder(self, annotation: NXOpen.Annotations.Annotation) -> WeldLabelBuilder:
        """
         The welding annotation to edit, otherwise if , then create a new one 
         Returns builder ( WeldLabelBuilder NXOpe):  weld label builder.
        """
        pass
    def CreateWeldObjectBuilder(self) -> WeldObjectBuilder:
        """
         Creates a NXOpen.Weld.WeldObjectBuilder object. 
         Returns builder ( WeldObjectBuilder NXOpe): .
        """
        pass
    def CreateWeldPmiBuilder(self) -> WeldPmiBuilder:
        """
         Creates a NXOpen.Weld.WeldPmiBuilder object.
         Returns builder ( WeldPmiBuilder NXOpe):  weld PMI builder.
        """
        pass
    def CreateWeldPointBuilder(self, weld_point: NXOpen.Features.Feature) -> WeldPointBuilder:
        """
         Creates a NXOpen.Weld.WeldPointBuilder object. 
         Returns builder ( WeldPointBuilder NXOpe):  WeldPoint feature builder.
        """
        pass
    def CreateWeldPointExitBuilder(self) -> WeldPointExitBuilder:
        """
         Creates a NXOpen.Weld.WeldPointExitBuilder object. 
         Returns builder ( WeldPointExitBuilder NXOpe): .
        """
        pass
    def EditSingleJointmarkFeature(self, element_feature: NXOpen.Features.Feature) -> JointmarkBuilder:
        """
         Creates a NXOpen.Weld.JointmarkBuilder object from a single element feature. 
         Returns builder ( JointmarkBuilder NXOpe): .
        """
        pass
    def EditSinglePointMarkFeature(self, elementFeature: PointMarkPoint) -> PointMarkBuilder:
        """
         Creates a NXOpen.Weld.PointMarkBuilder object from a single element feature. 
         Returns builder ( PointMarkBuilder NXOpe): .
        """
        pass
    def IsEntityAWeldObject(self) -> bool:
        """
         Checks if object is a weld object. 
         Returns status (bool): .
        """
        pass
    def IsEntityFromDesignFeatureOrDesignControlElementPart(self, searchOption: WeldManager.SearchOption) -> bool:
        """
         Checks if object is from a design feature or design control element. 
         Returns status (bool): .
        """
        pass
class WeldMeasurementSizeMethod(Enum):
    """
    Members Include: 
     |Invalid|  Invalid size method 
     |Auto|  auto size method 
     |Manual|  manual size method 

    """
    Invalid: int
    Auto: int
    Manual: int
    @staticmethod
    def ValueOf(value: int) -> WeldMeasurementSizeMethod:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class WeldObjectBuilder(NXOpen.TaggedObject): 
    """ Represents a NXOpen.Weld.WeldObjectBuilder class used to collect welding objects created or edited from a command. """
    class CommandName(Enum):
        """
        Members Include: 
         |NotSet|  No command. Used to initialize value. 
         |Groove|  Groove Weld command 
         |Fillet|  Fillet Weld command 
         |UserDefined|  User Defined Weld command 
         |WeldPoint|  Weld Point command 
         |Bead|  Bead command 
         |Fill|  Fill command 
         |ImportCsv|  Import CSV command 
         |EasySpot|  Easy Spot command 
         |DatumLocator|  Datum Locator command  
         |MeasurementLocator|  Measurement Locator command   
         |EasyMeasurementPattern|  Easy Measurement Pattern command 
         |PlugSlot|  Plug Slot command 
         |Joint|  Welding Joint command 
         |DatumSurface|  Datum Surface command 
         |DatumEdge|  Datum Edge command 
         |SurfaceWeld|  Surface Weld command 
         |Compound|  Compound Weld command 
         |WeldAttribute|  Edit Weld Attribute 
         |JointDefinition|  Edit Joint Definition Parameters 
         |Jointmark|  Joint Mark command 
         |WeldPointWizard|  Weld Point Wizard command 
         |Transform|  Weld Transform command 
         |DatumPin|  Datum Pin command 

        """
        NotSet: int
        Groove: int
        Fillet: int
        UserDefined: int
        WeldPoint: int
        Bead: int
        Fill: int
        ImportCsv: int
        EasySpot: int
        DatumLocator: int
        MeasurementLocator: int
        EasyMeasurementPattern: int
        PlugSlot: int
        Joint: int
        DatumSurface: int
        DatumEdge: int
        SurfaceWeld: int
        Compound: int
        WeldAttribute: int
        JointDefinition: int
        Jointmark: int
        WeldPointWizard: int
        Transform: int
        DatumPin: int
        @staticmethod
        def ValueOf(value: int) -> WeldObjectBuilder.CommandName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FeatureInfo:
        """
            Structure used to identify if each feature is newly created or edited.  
          
         WeldObjectBuilderFeatureInfo_Struct NXOpe is an alias for  WeldObjectBuilder.FeatureInfo NXOpe.
        """
        @property
        def Feature(self) -> NXOpen.Features.Feature:
            """
            Getter for property Feature
            the newly created or edited feature

            """
            pass
        @Feature.setter
        def Feature(self, value: NXOpen.Features.Feature):
            """
            Getter for property Feature
            the newly created or edited feature
            Setter for property Feature
            the newly created or edited feature

            """
            pass
        @property
        def IsNewlyCreated(self) -> bool:
            """
            Getter for property IsNewlyCreated
            true if a new feature, false if an existing feature was edited.

            """
            pass
        @IsNewlyCreated.setter
        def IsNewlyCreated(self, value: bool):
            """
            Getter for property IsNewlyCreated
            true if a new feature, false if an existing feature was edited.
            Setter for property IsNewlyCreated
            true if a new feature, false if an existing feature was edited.

            """
            pass
    @property
    def CommandUsed(self) -> WeldObjectBuilder.CommandName:
        """
        Getter for property: ( WeldObjectBuilder.CommandName NXOpe) CommandUsed
         Returns the command name that was last used to create or modify features   
            
         
        """
        pass
    def GetFeatureInformation(self) -> List[WeldObjectBuilder.FeatureInfo]:
        """
         Gets the created and modifed features 
         Returns features ( WeldObjectBuilder.FeatureInfo List[NXO):  features created or edited .
        """
        pass
class WeldOverlapStatus(Enum):
    """
    Members Include: 
     |Invalid|  invalid status 
     |Creation|  create overlap 
     |NonCreation|  don't create overlap 

    """
    Invalid: int
    Creation: int
    NonCreation: int
    @staticmethod
    def ValueOf(value: int) -> WeldOverlapStatus:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class WeldParasetLocation(Enum):
    """
    Members Include: 
     |Length|  arc length 
     |Percent|  percent arc length 
     |ThroughPoint|  through point 

    """
    Length: int
    Percent: int
    ThroughPoint: int
    @staticmethod
    def ValueOf(value: int) -> WeldParasetLocation:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.Annotations
class WeldPmiBuilder(NXOpen.Builder): 
    """ Create PMI symbols for multiple structure welds, this builder's Commit can produce more than one object, 
        the GetCommittedObjects can be used to get the objects and the order of GetCommittedObject's output array is stable. """
    class GroupWeldSymbolsType(Enum):
        """
        Members Include: 
         |NotSet|  No grouping of weld symbols 
         |All|  Group weld symbols of all selected objects 
         |ByStructureDesignerObjects|  Group like weld symbols according to objects created by same structure designer objects 

        """
        NotSet: int
        All: int
        ByStructureDesignerObjects: int
        @staticmethod
        def ValueOf(value: int) -> WeldPmiBuilder.GroupWeldSymbolsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OrientationPlaneType(Enum):
        """
        Members Include: 
         |XYPlane| 
         |XZPlane| 
         |YZPlane| 
         |ModelView| 
         |LastUserDefined| 
         |UserDefined| 

        """
        XYPlane: int
        XZPlane: int
        YZPlane: int
        ModelView: int
        LastUserDefined: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> WeldPmiBuilder.OrientationPlaneType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def GroupWeldSymbols(self) -> WeldPmiBuilder.GroupWeldSymbolsType:
        """
        Getter for property: ( WeldPmiBuilder.GroupWeldSymbolsType NXOpe) GroupWeldSymbols
         Returns the indication whether to combine identical weld symbols.  
             
         
        """
        pass
    @GroupWeldSymbols.setter
    def GroupWeldSymbols(self, groupWeldSymbols: WeldPmiBuilder.GroupWeldSymbolsType):
        """
        Setter for property: ( WeldPmiBuilder.GroupWeldSymbolsType NXOpe) GroupWeldSymbols
         Returns the indication whether to combine identical weld symbols.  
             
         
        """
        pass
    @property
    def Objects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Objects
         Returns the objects (either features or curves) that are used to create PMI symbols.  
             
         
        """
        pass
    @property
    def PlaneType(self) -> WeldPmiBuilder.OrientationPlaneType:
        """
        Getter for property: ( WeldPmiBuilder.OrientationPlaneType NXOpe) PlaneType
         Returns the plane type.  
             
         
        """
        pass
    @PlaneType.setter
    def PlaneType(self, planeType: WeldPmiBuilder.OrientationPlaneType):
        """
        Setter for property: ( WeldPmiBuilder.OrientationPlaneType NXOpe) PlaneType
         Returns the plane type.  
             
         
        """
        pass
    @property
    def SpaceFactor(self) -> float:
        """
        Getter for property: (float) SpaceFactor
         Returns the space factor.  
           The value is greater than zero.   
         
        """
        pass
    @SpaceFactor.setter
    def SpaceFactor(self, spaceFactor: float):
        """
        Setter for property: (float) SpaceFactor
         Returns the space factor.  
           The value is greater than zero.   
         
        """
        pass
    @property
    def Style(self) -> NXOpen.Annotations.StyleBuilder:
        """
        Getter for property: ( NXOpen.Annotations.StyleBuilder) Style
         Returns the  Annotations::StyleBuilder  for the annotation.  
             
         
        """
        pass
    @property
    def UserCoordinateSystem(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) UserCoordinateSystem
         Returns the user specified coordinate system.  
             
         
        """
        pass
    @UserCoordinateSystem.setter
    def UserCoordinateSystem(self, userCsys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) UserCoordinateSystem
         Returns the user specified coordinate system.  
             
         
        """
        pass
import NXOpen
import NXOpen.Features
class WeldPointBuilder(NXOpen.Builder): 
    """ Represents a Spot Weld feature """
    @property
    def ConnectingOnlyOnePart(self) -> bool:
        """
        Getter for property: (bool) ConnectingOnlyOnePart
         Returns   
            
         
        """
        pass
    @ConnectingOnlyOnePart.setter
    def ConnectingOnlyOnePart(self, connecting_only_one_part: bool):
        """
        Setter for property: (bool) ConnectingOnlyOnePart
         Returns   
            
         
        """
        pass
    @property
    def CreationDirection(self) -> WeldCreationDirection:
        """
        Getter for property: ( WeldCreationDirection NXOpe) CreationDirection
         Returns the creation direction type.  
             
         
        """
        pass
    @CreationDirection.setter
    def CreationDirection(self, creation_direction: WeldCreationDirection):
        """
        Setter for property: ( WeldCreationDirection NXOpe) CreationDirection
         Returns the creation direction type.  
             
         
        """
        pass
    @property
    def CsysAssemblyState(self) -> bool:
        """
        Getter for property: (bool) CsysAssemblyState
         Returns the assy coordinate system state   
            
         
        """
        pass
    @CsysAssemblyState.setter
    def CsysAssemblyState(self, assy_csys_state: bool):
        """
        Setter for property: (bool) CsysAssemblyState
         Returns the assy coordinate system state   
            
         
        """
        pass
    @property
    def CsysWorkPartState(self) -> bool:
        """
        Getter for property: (bool) CsysWorkPartState
         Returns the work coordinate systemstate   
            
         
        """
        pass
    @CsysWorkPartState.setter
    def CsysWorkPartState(self, workCsysState: bool):
        """
        Setter for property: (bool) CsysWorkPartState
         Returns the work coordinate systemstate   
            
         
        """
        pass
    @property
    def CustomCylinderAbove(self) -> float:
        """
        Getter for property: (float) CustomCylinderAbove
         Returns the distance the custom cylinder should be created above the
                weld point   
            
         
        """
        pass
    @CustomCylinderAbove.setter
    def CustomCylinderAbove(self, custom_cylinder_above: float):
        """
        Setter for property: (float) CustomCylinderAbove
         Returns the distance the custom cylinder should be created above the
                weld point   
            
         
        """
        pass
    @property
    def CustomRadius(self) -> float:
        """
        Getter for property: (float) CustomRadius
         Returns the radius to create the sphere, cylinder, or cone with   
            
         
        """
        pass
    @CustomRadius.setter
    def CustomRadius(self, custom_radius: float):
        """
        Setter for property: (float) CustomRadius
         Returns the radius to create the sphere, cylinder, or cone with   
            
         
        """
        pass
    @property
    def CustomTotalCylinderLength(self) -> float:
        """
        Getter for property: (float) CustomTotalCylinderLength
         Returns the total length of the cylinder to be created.  
             
         
        """
        pass
    @CustomTotalCylinderLength.setter
    def CustomTotalCylinderLength(self, total_cylinder_length: float):
        """
        Setter for property: (float) CustomTotalCylinderLength
         Returns the total length of the cylinder to be created.  
             
         
        """
        pass
    @property
    def DatumFirstReferenceDirection(self) -> WeldDatumControlDirection:
        """
        Getter for property: ( WeldDatumControlDirection NXOpe) DatumFirstReferenceDirection
         Returns the datum reference direction type.  
             
         
        """
        pass
    @DatumFirstReferenceDirection.setter
    def DatumFirstReferenceDirection(self, datum_ref_dir: WeldDatumControlDirection):
        """
        Setter for property: ( WeldDatumControlDirection NXOpe) DatumFirstReferenceDirection
         Returns the datum reference direction type.  
             
         
        """
        pass
    @property
    def DatumMajorDirection(self) -> WeldDatumControlDirection:
        """
        Getter for property: ( WeldDatumControlDirection NXOpe) DatumMajorDirection
         Returns the datum major direction type.  
             
         
        """
        pass
    @DatumMajorDirection.setter
    def DatumMajorDirection(self, datum_major_dir: WeldDatumControlDirection):
        """
        Setter for property: ( WeldDatumControlDirection NXOpe) DatumMajorDirection
         Returns the datum major direction type.  
             
         
        """
        pass
    @property
    def DatumSecondReferenceDirection(self) -> WeldDatumControlDirection:
        """
        Getter for property: ( WeldDatumControlDirection NXOpe) DatumSecondReferenceDirection
         Returns the datum reference direction type.  
             
         
        """
        pass
    @DatumSecondReferenceDirection.setter
    def DatumSecondReferenceDirection(self, datum_ref_dir: WeldDatumControlDirection):
        """
        Setter for property: ( WeldDatumControlDirection NXOpe) DatumSecondReferenceDirection
         Returns the datum reference direction type.  
             
         
        """
        pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance for the weld point   
            
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distance_tolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance for the weld point   
            
         
        """
        pass
    @property
    def EndDistance(self) -> str:
        """
        Getter for property: (str) EndDistance
         Returns the end dist   
            
         
        """
        pass
    @EndDistance.setter
    def EndDistance(self, end_dist_str: str):
        """
        Setter for property: (str) EndDistance
         Returns the end dist   
            
         
        """
        pass
    @property
    def EndDistanceLocation(self) -> WeldParasetLocation:
        """
        Getter for property: ( WeldParasetLocation NXOpe) EndDistanceLocation
         Returns the end dist location   
            
         
        """
        pass
    @EndDistanceLocation.setter
    def EndDistanceLocation(self, end_dist_location: WeldParasetLocation):
        """
        Setter for property: ( WeldParasetLocation NXOpe) EndDistanceLocation
         Returns the end dist location   
            
         
        """
        pass
    @property
    def ExtendMethod(self) -> WeldPointExtendMethod:
        """
        Getter for property: ( WeldPointExtendMethod NXOpe) ExtendMethod
         Returns the offset curve extend method.  
             
         
        """
        pass
    @ExtendMethod.setter
    def ExtendMethod(self, extend_method: WeldPointExtendMethod):
        """
        Setter for property: ( WeldPointExtendMethod NXOpe) ExtendMethod
         Returns the offset curve extend method.  
             
         
        """
        pass
    @property
    def Location(self) -> WeldPointLocation:
        """
        Getter for property: ( WeldPointLocation NXOpe) Location
         Returns the processing method to use for generating weld points along reference section(s)   
            
         
        """
        pass
    @Location.setter
    def Location(self, location: WeldPointLocation):
        """
        Setter for property: ( WeldPointLocation NXOpe) Location
         Returns the processing method to use for generating weld points along reference section(s)   
            
         
        """
        pass
    @property
    def MeasurementDefaultHeight(self) -> float:
        """
        Getter for property: (float) MeasurementDefaultHeight
         Returns the default height of the object for measurement to be created.  
             
         
        """
        pass
    @MeasurementDefaultHeight.setter
    def MeasurementDefaultHeight(self, measurement_default_height: float):
        """
        Setter for property: (float) MeasurementDefaultHeight
         Returns the default height of the object for measurement to be created.  
             
         
        """
        pass
    @property
    def MeasurementDefaultWidth(self) -> float:
        """
        Getter for property: (float) MeasurementDefaultWidth
         Returns the default width of the object for measurement to be created.  
             
         
        """
        pass
    @MeasurementDefaultWidth.setter
    def MeasurementDefaultWidth(self, measurement_default_width: float):
        """
        Setter for property: (float) MeasurementDefaultWidth
         Returns the default width of the object for measurement to be created.  
             
         
        """
        pass
    @property
    def MeasurementHoleSize(self) -> float:
        """
        Getter for property: (float) MeasurementHoleSize
         Returns the hole_size of the object for measurement to be created.  
             
         
        """
        pass
    @MeasurementHoleSize.setter
    def MeasurementHoleSize(self, hole_size: float):
        """
        Setter for property: (float) MeasurementHoleSize
         Returns the hole_size of the object for measurement to be created.  
             
         
        """
        pass
    @property
    def MeasurementSlotLength(self) -> float:
        """
        Getter for property: (float) MeasurementSlotLength
         Returns the slot height of the object for measurement to be created.  
             
         
        """
        pass
    @MeasurementSlotLength.setter
    def MeasurementSlotLength(self, slot_length: float):
        """
        Setter for property: (float) MeasurementSlotLength
         Returns the slot height of the object for measurement to be created.  
             
         
        """
        pass
    @property
    def MeasurementSlotWidth(self) -> float:
        """
        Getter for property: (float) MeasurementSlotWidth
         Returns the slot width of the object for measurement to be created.  
             
         
        """
        pass
    @MeasurementSlotWidth.setter
    def MeasurementSlotWidth(self, slot_width: float):
        """
        Setter for property: (float) MeasurementSlotWidth
         Returns the slot width of the object for measurement to be created.  
             
         
        """
        pass
    @property
    def MeasurementStudSize(self) -> float:
        """
        Getter for property: (float) MeasurementStudSize
         Returns the stud size of the object for measurement to be created.  
             
         
        """
        pass
    @MeasurementStudSize.setter
    def MeasurementStudSize(self, stud_size: float):
        """
        Setter for property: (float) MeasurementStudSize
         Returns the stud size of the object for measurement to be created.  
             
         
        """
        pass
    @property
    def MirrorByType(self) -> bool:
        """
        Getter for property: (bool) MirrorByType
         Returns the mirror by type   
            
         
        """
        pass
    @MirrorByType.setter
    def MirrorByType(self, mirror_by_type: bool):
        """
        Setter for property: (bool) MirrorByType
         Returns the mirror by type   
            
         
        """
        pass
    @property
    def MirrorPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) MirrorPlane
         Returns the plane that a point is to be mirrored about.  
             
         
        """
        pass
    @MirrorPlane.setter
    def MirrorPlane(self, mirror_plane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) MirrorPlane
         Returns the plane that a point is to be mirrored about.  
             
         
        """
        pass
    @property
    def NumberConnectedPanels(self) -> int:
        """
        Getter for property: (int) NumberConnectedPanels
         Returns the num connected panels.  
             
         
        """
        pass
    @NumberConnectedPanels.setter
    def NumberConnectedPanels(self, num_connected_panels: int):
        """
        Setter for property: (int) NumberConnectedPanels
         Returns the num connected panels.  
             
         
        """
        pass
    @property
    def OffsetDistance(self) -> str:
        """
        Getter for property: (str) OffsetDistance
         Returns the offset distance from edges in guide_collector1 to place weld points    
            
         
        """
        pass
    @OffsetDistance.setter
    def OffsetDistance(self, offset_distance_str: str):
        """
        Setter for property: (str) OffsetDistance
         Returns the offset distance from edges in guide_collector1 to place weld points    
            
         
        """
        pass
    @property
    def OutputType(self) -> OutputType:
        """
        Getter for property: ( OutputType NXOpe) OutputType
         Returns the output type.  
             
         
        """
        pass
    @OutputType.setter
    def OutputType(self, output_type: OutputType):
        """
        Setter for property: ( OutputType NXOpe) OutputType
         Returns the output type.  
             
         
        """
        pass
    @property
    def PointMethod(self) -> WeldPointMethod:
        """
        Getter for property: ( WeldPointMethod NXOpe) PointMethod
         Returns  the method for creating weld points.  
            Weld points can be created using guide
                 entities or  Point  objects.   
         
        """
        pass
    @PointMethod.setter
    def PointMethod(self, pt_method: WeldPointMethod):
        """
        Setter for property: ( WeldPointMethod NXOpe) PointMethod
         Returns  the method for creating weld points.  
            Weld points can be created using guide
                 entities or  Point  objects.   
         
        """
        pass
    @property
    def PointsGuideDistance(self) -> float:
        """
        Getter for property: (float) PointsGuideDistance
         Returns the distance percentage from the start of the curve where the
                weld point should be.  
           0.0 is the start of the curve
                100.0 is the end of the curve.   
         
        """
        pass
    @PointsGuideDistance.setter
    def PointsGuideDistance(self, points_guide_dist: float):
        """
        Setter for property: (float) PointsGuideDistance
         Returns the distance percentage from the start of the curve where the
                weld point should be.  
           0.0 is the start of the curve
                100.0 is the end of the curve.   
         
        """
        pass
    @property
    def ProjectDirection(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) ProjectDirection
         Returns the project direction   
            
         
        """
        pass
    @ProjectDirection.setter
    def ProjectDirection(self, direction: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) ProjectDirection
         Returns the project direction   
            
         
        """
        pass
    @property
    def ProjectDirectionObject(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ProjectDirectionObject
         Returns the project direction NXOpen object   
            
         
        """
        pass
    @ProjectDirectionObject.setter
    def ProjectDirectionObject(self, direction: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ProjectDirectionObject
         Returns the project direction NXOpen object   
            
         
        """
        pass
    @property
    def ProjectionMethod(self) -> WeldProjectionMethod:
        """
        Getter for property: ( WeldProjectionMethod NXOpe) ProjectionMethod
         Returns the project method type.  
             
         
        """
        pass
    @ProjectionMethod.setter
    def ProjectionMethod(self, proj_method: WeldProjectionMethod):
        """
        Setter for property: ( WeldProjectionMethod NXOpe) ProjectionMethod
         Returns the project method type.  
             
         
        """
        pass
    @property
    def ReferenceSheetSpacingMethod(self) -> WeldPointSpacingMethod:
        """
        Getter for property: ( WeldPointSpacingMethod NXOpe) ReferenceSheetSpacingMethod
         Returns the refsheet spacing method   
            
         
        """
        pass
    @ReferenceSheetSpacingMethod.setter
    def ReferenceSheetSpacingMethod(self, spacing_method: WeldPointSpacingMethod):
        """
        Setter for property: ( WeldPointSpacingMethod NXOpe) ReferenceSheetSpacingMethod
         Returns the refsheet spacing method   
            
         
        """
        pass
    @property
    def ReferenceSheetType(self) -> WeldPointReferenceSheetType:
        """
        Getter for property: ( WeldPointReferenceSheetType NXOpe) ReferenceSheetType
         Returns  the type of sheet to create to place weld points on.  
             
         
        """
        pass
    @ReferenceSheetType.setter
    def ReferenceSheetType(self, ref_sheet_type: WeldPointReferenceSheetType):
        """
        Setter for property: ( WeldPointReferenceSheetType NXOpe) ReferenceSheetType
         Returns  the type of sheet to create to place weld points on.  
             
         
        """
        pass
    @property
    def SectionPlaneEntity(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) SectionPlaneEntity
         Returns   
            
         
        """
        pass
    @SectionPlaneEntity.setter
    def SectionPlaneEntity(self, plane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) SectionPlaneEntity
         Returns   
            
         
        """
        pass
    @property
    def SequenceNumber(self) -> int:
        """
        Getter for property: (int) SequenceNumber
         Returns the sequence number for the weld point feature.  
           Each Weld point feature contains a single point.
                If multiple Weld points are to be created, you must specify the sequence of the point you want.
                For example if you are expecting 3 points to be created. You must create 3 weld point features.
                The features will have sequence numbers 0,1 and 2.    
         
        """
        pass
    @SequenceNumber.setter
    def SequenceNumber(self, sequence_number: int):
        """
        Setter for property: (int) SequenceNumber
         Returns the sequence number for the weld point feature.  
           Each Weld point feature contains a single point.
                If multiple Weld points are to be created, you must specify the sequence of the point you want.
                For example if you are expecting 3 points to be created. You must create 3 weld point features.
                The features will have sequence numbers 0,1 and 2.    
         
        """
        pass
    @property
    def ShowThroughAssemblyState(self) -> bool:
        """
        Getter for property: (bool) ShowThroughAssemblyState
         Returns the through assy coordinate system state   
            
         
        """
        pass
    @ShowThroughAssemblyState.setter
    def ShowThroughAssemblyState(self, thru_assy_state: bool):
        """
        Setter for property: (bool) ShowThroughAssemblyState
         Returns the through assy coordinate system state   
            
         
        """
        pass
    @property
    def ShowThroughWorkPartState(self) -> bool:
        """
        Getter for property: (bool) ShowThroughWorkPartState
         Returns the through work coordinate system state   
            
         
        """
        pass
    @ShowThroughWorkPartState.setter
    def ShowThroughWorkPartState(self, thru_work_state: bool):
        """
        Setter for property: (bool) ShowThroughWorkPartState
         Returns the through work coordinate system state   
            
         
        """
        pass
    @property
    def SizeMethod(self) -> WeldMeasurementSizeMethod:
        """
        Getter for property: ( WeldMeasurementSizeMethod NXOpe) SizeMethod
         Returns the measurement size method.  
             
         
        """
        pass
    @SizeMethod.setter
    def SizeMethod(self, size_method: WeldMeasurementSizeMethod):
        """
        Setter for property: ( WeldMeasurementSizeMethod NXOpe) SizeMethod
         Returns the measurement size method.  
             
         
        """
        pass
    @property
    def SolidType(self) -> WeldCustom:
        """
        Getter for property: ( WeldCustom NXOpe) SolidType
         Returns the output solid type.  
             
         
        """
        pass
    @SolidType.setter
    def SolidType(self, solid_type: WeldCustom):
        """
        Setter for property: ( WeldCustom NXOpe) SolidType
         Returns the output solid type.  
             
         
        """
        pass
    @property
    def SpacingCalculateMethod(self) -> WeldSpacingCalcMethod:
        """
        Getter for property: ( WeldSpacingCalcMethod NXOpe) SpacingCalculateMethod
         Returns the project method type.  
             
         
        """
        pass
    @SpacingCalculateMethod.setter
    def SpacingCalculateMethod(self, spacing_calc_method: WeldSpacingCalcMethod):
        """
        Setter for property: ( WeldSpacingCalcMethod NXOpe) SpacingCalculateMethod
         Returns the project method type.  
             
         
        """
        pass
    @property
    def SpacingNumber(self) -> str:
        """
        Getter for property: (str) SpacingNumber
         Returns the spacing number   
            
         
        """
        pass
    @SpacingNumber.setter
    def SpacingNumber(self, spacing_or_number_str: str):
        """
        Setter for property: (str) SpacingNumber
         Returns the spacing number   
            
         
        """
        pass
    @property
    def StartDistance(self) -> str:
        """
        Getter for property: (str) StartDistance
         Returns the start dist  
            
         
        """
        pass
    @StartDistance.setter
    def StartDistance(self, start_dist_str: str):
        """
        Setter for property: (str) StartDistance
         Returns the start dist  
            
         
        """
        pass
    @property
    def StartDistanceLocation(self) -> WeldParasetLocation:
        """
        Getter for property: ( WeldParasetLocation NXOpe) StartDistanceLocation
         Returns the start dist location   
            
         
        """
        pass
    @StartDistanceLocation.setter
    def StartDistanceLocation(self, start_dist_location: WeldParasetLocation):
        """
        Setter for property: ( WeldParasetLocation NXOpe) StartDistanceLocation
         Returns the start dist location   
            
         
        """
        pass
    @property
    def TranslateCsys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) TranslateCsys
         Returns the coordinate system that a point is to be translated about.  
             
         
        """
        pass
    @TranslateCsys.setter
    def TranslateCsys(self, translate_csys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) TranslateCsys
         Returns the coordinate system that a point is to be translated about.  
             
         
        """
        pass
    @property
    def TranslateXDistance(self) -> str:
        """
        Getter for property: (str) TranslateXDistance
         Returnsthe tran x dist   
            
         
        """
        pass
    @TranslateXDistance.setter
    def TranslateXDistance(self, trans_x_dist_str: str):
        """
        Setter for property: (str) TranslateXDistance
         Returnsthe tran x dist   
            
         
        """
        pass
    @property
    def TranslateYDistance(self) -> str:
        """
        Getter for property: (str) TranslateYDistance
         Returnsthe trans y dist   
            
         
        """
        pass
    @TranslateYDistance.setter
    def TranslateYDistance(self, trans_y_dist_str: str):
        """
        Setter for property: (str) TranslateYDistance
         Returnsthe trans y dist   
            
         
        """
        pass
    @property
    def TranslateZDistance(self) -> str:
        """
        Getter for property: (str) TranslateZDistance
         Returns the translate distance for weld points in z axis direction.  
              
         
        """
        pass
    @TranslateZDistance.setter
    def TranslateZDistance(self, trans_z_dist_str: str):
        """
        Setter for property: (str) TranslateZDistance
         Returns the translate distance for weld points in z axis direction.  
              
         
        """
        pass
    @property
    def WeldType(self) -> WeldFeatureSetType:
        """
        Getter for property: ( WeldFeatureSetType NXOpe) WeldType
         Returns the weld type.  
             
         
        """
        pass
    @WeldType.setter
    def WeldType(self, cur_weld_type: WeldFeatureSetType):
        """
        Setter for property: ( WeldFeatureSetType NXOpe) WeldType
         Returns the weld type.  
             
         
        """
        pass
    def CalculateDatumMeasurementDefaultDirection(self) -> None:
        """
         Calculate location and default direction of datum and measurement, need to set the current point prior to calling this method 
        """
        pass
    def CalculateWeldPoints(self) -> List[NXOpen.Point3d]:
        """
        To calculate all weld points
         Returns points ( NXOpen.Point3d Li):  weld points .
        """
        pass
    def ClearFaceSets(self) -> None:
        """
         The clear for all existed facesets 
        """
        pass
    def CommitFaceSets(self) -> None:
        """
         
        """
        pass
    def CommitReferenceSheets(self, create_status: WeldOverlapStatus) -> None:
        """
         The commit for reference sheets 
        """
        pass
    def CommitSection(self, path: NXOpen.Section) -> None:
        """
        Commit created section
        """
        pass
    def CreateCenterLine(self) -> NXOpen.Section:
        """
         To create center line
         Returns centerline ( NXOpen.Section): .
        """
        pass
    def CreateOffsetCurve(self) -> NXOpen.Section:
        """
        Create offset curve 
         Returns offset_curve ( NXOpen.Section): .
        """
        pass
    def CreateSectionPlaneCurves(self) -> NXOpen.Section:
        """
         Create section curve
         Returns section_curves ( NXOpen.Section):  section curve.
        """
        pass
    def CreateSingleWeldPoint(self, point_coord: NXOpen.Point3d) -> None:
        """
        The creation for single weld point
        """
        pass
    def FlipZAxis(self) -> None:
        """
         Flip the z axis 
        """
        pass
    def GetCsys(self) -> Tuple[NXOpen.Point3d, NXOpen.Matrix3x3]:
        """
        Get coordinate system for point
         Returns A tuple consisting of (origin, matrix). 
         - origin is:  NXOpen.Point3d. origin point .
         - matrix is:  NXOpen.Matrix3x3. rotate matrix .

        """
        pass
    def GetCurrentReferenceSheet(self) -> int:
        """
         The current refsheet 
         Returns currentRefSheet (int): .
        """
        pass
    def GetFaceSet(self, faceset_index: int) -> Tuple[List[NXOpen.DisplayableObject], List[NXOpen.Features.Feature]]:
        """
         Gets the user selected faces for the indicated face set 
         Returns A tuple consisting of (objects, frecs). 
         - objects is:  NXOpen.DisplayableObject Li. the face set reference objects .
         - frecs is:  NXOpen.Features.Feature Li. the face set wave linked frecs .

        """
        pass
    def GetFirstSection(self) -> NXOpen.Section:
        """
         Get the first section. For guide curves method, this section contains curves that used to create weld path, 
              For centerline method, this section contians the first group of curves used to create centerline 
         Returns section ( NXOpen.Section): the section .
        """
        pass
    def GetMirrorTranslateReferenceObjects(self) -> List[NXOpen.DisplayableObject]:
        """
         Get mirror translate reference objects
         Returns objects ( NXOpen.DisplayableObject Li):  the mirror translate reference objects.
        """
        pass
    def GetNumFaceSets(self) -> int:
        """
        Get the amount of face sets  
         Returns numFaceets (int):  total amount of face sets .
        """
        pass
    def GetReferenceSheets(self) -> NXOpen.Features.Feature:
        """
         The refernence sheet feature 
         Returns refSheet ( NXOpen.Features.Feature):  the reference sheet.
        """
        pass
    def GetSecondSection(self) -> NXOpen.Section:
        """
         Get the second section. this method for centerline method weld only, this section contains 
             the second group of curves used to create centerline 
         Returns section ( NXOpen.Section): the section .
        """
        pass
    def GetSectionCurves(self, section: NXOpen.Section) -> List[NXOpen.Curve]:
        """
         Gets the curves contained in the input section 
         Returns curves ( NXOpen.Curve Li):  the curves of the section .
        """
        pass
    def MovePoint(self, origin: NXOpen.Point3d) -> None:
        """
        Move selected points
        """
        pass
    def ProjectPoints(self) -> None:
        """
         Project selected points along the specified vector to reference sheets
        """
        pass
    def RemoveCharacteristics(self, attr_title: str, attr_type: WeldAttribType, attr_value: str) -> None:
        """
        Remove characteristics for selected points, need to set the current point prior to calling this method  
        """
        pass
    def RemoveWeldPoint(self) -> None:
        """
        Remove the current selected point, need to set the current point prior to calling this method  
        """
        pass
    def SetCharacteristics(self, attr_title: str, attr_type: WeldAttribType, attr_value: str) -> None:
        """
        Set or edit characteristics for selected points 
        """
        pass
    def SetCurrentReferenceSheet(self, currentRefSheet: int) -> None:
        """
         Set current refsheet
        """
        pass
    def SetFaceSet(self, faceset_index: WeldFacesetIndex, objects: List[NXOpen.DisplayableObject]) -> None:
        """
         Sets the user selected faces for the indicated face set 
        """
        pass
    def SetFirstSection(self, section: NXOpen.Section) -> None:
        """
        The commit for first section 
        """
        pass
    def SetMirrorTranslateReferenceObjects(self, refs: List[NXOpen.TaggedObject]) -> None:
        """
         Add or remove mirror translate reference objects
        """
        pass
    def SetPoint(self, index: int) -> None:
        """
        Set the selected point 
        """
        pass
    def SetSecondSection(self, section: NXOpen.Section) -> None:
        """
        Create second section 
        """
        pass
    def SetSelectionType(self, selection_type: WeldSelectionType) -> None:
        """
        Set the selection type 
        """
        pass
    def UpdateCsys(self, origin: NXOpen.Point3d, matrix: NXOpen.Matrix3x3) -> None:
        """
        Update coordinate system for selected points
        """
        pass
    def UpdateFirstSection(self, total_section: NXOpen.Section) -> None:
        """
        Update first section 
        """
        pass
    def UpdateSecondSection(self, total_section: NXOpen.Section) -> None:
        """
        Update second section 
        """
        pass
class WeldPointDirection(Enum):
    """
    Members Include: 
     |StartToEnd|  Direction is from start to end
     |EndToStart|  Direction is from end to start 

    """
    StartToEnd: int
    EndToStart: int
    @staticmethod
    def ValueOf(value: int) -> WeldPointDirection:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class WeldPointExitBuilder(NXOpen.TaggedObject): 
    """ Represents a NXOpen.Weld.WeldPointExitBuilder class used to pass welding object from the Weld Point command to a user callback. This object is not used on edit. """
    class CommandName(Enum):
        """
        Members Include: 
         |NotSet|  No command. Used to initialize value. 
         |WeldPoint|  Weld Point command 
         |DatumLocator|  Datum Locator command  
         |MeasurementLocator|  Measurement Locator command   
         |Jointmark|  Joint Mark command   
         |WeldPointWizard|  Weld Point Wizard command 
         |EasySpot|  Easy Spot. User selected OK. Features exist to process. 
         |EasySpotSelected|  Easy Spot. User selected Create Features From Selection. 
         |EasySpotApply|  Easy Spot. User selected Apply 
         |EasySpotEnded|  Easy Spot. User selected OK or Cancel. No new features created. 

        """
        NotSet: int
        WeldPoint: int
        DatumLocator: int
        MeasurementLocator: int
        Jointmark: int
        WeldPointWizard: int
        EasySpot: int
        EasySpotSelected: int
        EasySpotApply: int
        EasySpotEnded: int
        @staticmethod
        def ValueOf(value: int) -> WeldPointExitBuilder.CommandName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FeatureStatus(Enum):
        """
        Members Include: 
         |Modified|  An existing feature was modified. 
         |NewlyCreated|  A new feature was created.        
         |NotUsed|  A feature to move was specified, but changes to spacing options caused this feature not to be used. 

        """
        Modified: int
        NewlyCreated: int
        NotUsed: int
        @staticmethod
        def ValueOf(value: int) -> WeldPointExitBuilder.FeatureStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MethodUsed(Enum):
        """
        Members Include: 
         |NotSet|  No method specified. Used to initialize value. 
         |Mirror|  Feature was created using the mirror method. 
         |Translate|  Feature was created using the translate method. 
         |GuideCurve|  Feature was created using the guide curves method. 
         |Points|  Feature was created using the points method. 
         |GuideCurveMovedOff|  Feature was created using the guide curves method, but user moved it off. 

        """
        NotSet: int
        Mirror: int
        Translate: int
        GuideCurve: int
        Points: int
        GuideCurveMovedOff: int
        @staticmethod
        def ValueOf(value: int) -> WeldPointExitBuilder.MethodUsed:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FeatureDetails:
        """
            Structure used to identify newly created, edited, and unused features.  
          
         WeldPointExitBuilderFeatureDetails_Struct NXOpe is an alias for  WeldPointExitBuilder.FeatureDetails NXOpe.
        """
        @property
        def Feature(self) -> NXOpen.Features.Feature:
            """
            Getter for property Feature
            the newly created, edited, or unused feature

            """
            pass
        @Feature.setter
        def Feature(self, value: NXOpen.Features.Feature):
            """
            Getter for property Feature
            the newly created, edited, or unused feature
            Setter for property Feature
            the newly created, edited, or unused feature

            """
            pass
        @property
        def MethodUsed(self) -> WeldPointExitBuilder.MethodUsed:
            """
            Getter for property MethodUsed
            the method used to create the feature

            """
            pass
        @MethodUsed.setter
        def MethodUsed(self, value: WeldPointExitBuilder.MethodUsed):
            """
            Getter for property MethodUsed
            the method used to create the feature
            Setter for property MethodUsed
            the method used to create the feature

            """
            pass
        @property
        def Parent(self) -> NXOpen.Features.Feature:
            """
            Getter for property Parent
            the parent if method used was mirror or translate

            """
            pass
        @Parent.setter
        def Parent(self, value: NXOpen.Features.Feature):
            """
            Getter for property Parent
            the parent if method used was mirror or translate
            Setter for property Parent
            the parent if method used was mirror or translate

            """
            pass
        @property
        def IsNewlyCreated(self) -> WeldPointExitBuilder.FeatureStatus:
            """
            Getter for property IsNewlyCreated
            Indicates if the feature was modified, newly created, or unused.

            """
            pass
        @IsNewlyCreated.setter
        def IsNewlyCreated(self, value: WeldPointExitBuilder.FeatureStatus):
            """
            Getter for property IsNewlyCreated
            Indicates if the feature was modified, newly created, or unused.
            Setter for property IsNewlyCreated
            Indicates if the feature was modified, newly created, or unused.

            """
            pass
    class FeatureInfo:
        """
            Structure used to identify newly created features.  
          
         WeldPointExitBuilderFeatureInfo_Struct NXOpe is an alias for  WeldPointExitBuilder.FeatureInfo NXOpe.
        """
        @property
        def Feature(self) -> NXOpen.Features.Feature:
            """
            Getter for property Feature
            the newly created or edited feature

            """
            pass
        @Feature.setter
        def Feature(self, value: NXOpen.Features.Feature):
            """
            Getter for property Feature
            the newly created or edited feature
            Setter for property Feature
            the newly created or edited feature

            """
            pass
        @property
        def MethodUsed(self) -> WeldPointExitBuilder.MethodUsed:
            """
            Getter for property MethodUsed
            the method used to create the feature

            """
            pass
        @MethodUsed.setter
        def MethodUsed(self, value: WeldPointExitBuilder.MethodUsed):
            """
            Getter for property MethodUsed
            the method used to create the feature
            Setter for property MethodUsed
            the method used to create the feature

            """
            pass
        @property
        def Parent(self) -> NXOpen.Features.Feature:
            """
            Getter for property Parent
            the parent if method used was mirror or translate

            """
            pass
        @Parent.setter
        def Parent(self, value: NXOpen.Features.Feature):
            """
            Getter for property Parent
            the parent if method used was mirror or translate
            Setter for property Parent
            the parent if method used was mirror or translate

            """
            pass
        @property
        def IsNewlyCreated(self) -> bool:
            """
            Getter for property IsNewlyCreated
            true if a new feature, false if an existing feature was edited.

            """
            pass
        @IsNewlyCreated.setter
        def IsNewlyCreated(self, value: bool):
            """
            Getter for property IsNewlyCreated
            true if a new feature, false if an existing feature was edited.
            Setter for property IsNewlyCreated
            true if a new feature, false if an existing feature was edited.

            """
            pass
    @property
    def CommandUsed(self) -> WeldPointExitBuilder.CommandName:
        """
        Getter for property: ( WeldPointExitBuilder.CommandName NXOpe) CommandUsed
         Returns the command name that was last used to create features.  
           This callback is not called on edit.   
         
        """
        pass
    def GetFeatureDetails(self) -> List[WeldPointExitBuilder.FeatureDetails]:
        """
         Gets the information for the newly created, edited or unused features. 
         Returns features ( WeldPointExitBuilder.FeatureDetails List[NXO):  features created .
        """
        pass
    def GetFeatureInformation(self) -> List[WeldPointExitBuilder.FeatureInfo]:
        """
         Gets the information for the newly created, or edited features. 
         Returns features ( WeldPointExitBuilder.FeatureInfo List[NXO):  features created .
        """
        pass
class WeldPointExtendMethod(Enum):
    """
    Members Include: 
     |NotSet|  Do not extend offset curves. 
     |Boundary|  Extend offset curves to the faces boundary. 

    """
    NotSet: int
    Boundary: int
    @staticmethod
    def ValueOf(value: int) -> WeldPointExtendMethod:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class WeldPointLocation(Enum):
    """
    Members Include: 
     |AlongGuideCurve|  Place spot welds along guide curves 
     |AlongGuideEdge|  Place spot welds by offsetting from an edge(s). 
     |AlongCenterLine|  To sections are needed for this method.     
     |SectionPlane|  Place spot welds along a section curve      

    """
    AlongGuideCurve: int
    AlongGuideEdge: int
    AlongCenterLine: int
    SectionPlane: int
    @staticmethod
    def ValueOf(value: int) -> WeldPointLocation:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class WeldPointMethod(Enum):
    """
    Members Include: 
     |Multiple|  use guide curve(s) or edge(s) to generate spot weld points 
     |Single|  use point constructor to generate spot weld points  
     |Mirror|  mirror existing points 
     |Translate|  translate existing points 
     |FromPoints|  create fixsinglenone points using existing points 

    """
    Multiple: int
    Single: int
    Mirror: int
    Translate: int
    FromPoints: int
    @staticmethod
    def ValueOf(value: int) -> WeldPointMethod:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class WeldPointReferenceSheetType(Enum):
    """
    Members Include: 
     |Overlap|  spot welds are based on the intersection of face sets 
     |Top|  spot welds are based on the first face set 
     |NotSet|  spot welds are points in 3d space          

    """
    Overlap: int
    Top: int
    NotSet: int
    @staticmethod
    def ValueOf(value: int) -> WeldPointReferenceSheetType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class WeldPointSpacingMethod(Enum):
    """
    Members Include: 
     |Distance|  Place multiple spot welds based on distance 
     |NumPoints|  Place multiple spot welds based on number of points 

    """
    Distance: int
    NumPoints: int
    @staticmethod
    def ValueOf(value: int) -> WeldPointSpacingMethod:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen.Features
class WeldPoint(NXOpen.Features.Feature): 
    """ Represents a WeldPoint feature. """
    pass
import NXOpen
class WeldPreferenceBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Weld.WeldPreferenceBuilder builder """
    @property
    def CurrentGroupIDColorIndex(self) -> WeldGroupIdColor:
        """
        Getter for property: ( WeldGroupIdColor NXOpe) CurrentGroupIDColorIndex
         Returns the group idcolor assigned   
            
         
        """
        pass
    @CurrentGroupIDColorIndex.setter
    def CurrentGroupIDColorIndex(self, currentGroupIDColorIndex: WeldGroupIdColor):
        """
        Setter for property: ( WeldGroupIdColor NXOpe) CurrentGroupIDColorIndex
         Returns the group idcolor assigned   
            
         
        """
        pass
    @property
    def DatumIdLowerRange(self) -> int:
        """
        Getter for property: (int) DatumIdLowerRange
         Returns the datum id lower range   
            
         
        """
        pass
    @DatumIdLowerRange.setter
    def DatumIdLowerRange(self, datumIdLowerRange: int):
        """
        Setter for property: (int) DatumIdLowerRange
         Returns the datum id lower range   
            
         
        """
        pass
    @property
    def DatumIdUpperRange(self) -> int:
        """
        Getter for property: (int) DatumIdUpperRange
         Returns the datum id upper range   
            
         
        """
        pass
    @DatumIdUpperRange.setter
    def DatumIdUpperRange(self, datumIdUpperRange: int):
        """
        Setter for property: (int) DatumIdUpperRange
         Returns the datum id upper range   
            
         
        """
        pass
    @property
    def DatumNamePrefix(self) -> str:
        """
        Getter for property: (str) DatumNamePrefix
         Returns the datum name prefix   
            
         
        """
        pass
    @DatumNamePrefix.setter
    def DatumNamePrefix(self, datumNamePrefix: str):
        """
        Setter for property: (str) DatumNamePrefix
         Returns the datum name prefix   
            
         
        """
        pass
    @property
    def DatumObjectColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) DatumObjectColor
         Returns the datum object color   
            
         
        """
        pass
    @DatumObjectColor.setter
    def DatumObjectColor(self, datumObjectColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) DatumObjectColor
         Returns the datum object color   
            
         
        """
        pass
    @property
    def DatumObjectLayer(self) -> int:
        """
        Getter for property: (int) DatumObjectLayer
         Returns the datum object layer   
            
         
        """
        pass
    @DatumObjectLayer.setter
    def DatumObjectLayer(self, datumObjectLayer: int):
        """
        Setter for property: (int) DatumObjectLayer
         Returns the datum object layer   
            
         
        """
        pass
    @property
    def DatumPartNumber(self) -> str:
        """
        Getter for property: (str) DatumPartNumber
         Returns the datum part number   
            
         
        """
        pass
    @DatumPartNumber.setter
    def DatumPartNumber(self, datumPartNumber: str):
        """
        Setter for property: (str) DatumPartNumber
         Returns the datum part number   
            
         
        """
        pass
    @property
    def MeasurementIdLowerRange(self) -> int:
        """
        Getter for property: (int) MeasurementIdLowerRange
         Returns the measurement id lower range   
            
         
        """
        pass
    @MeasurementIdLowerRange.setter
    def MeasurementIdLowerRange(self, measurementIdLowerRange: int):
        """
        Setter for property: (int) MeasurementIdLowerRange
         Returns the measurement id lower range   
            
         
        """
        pass
    @property
    def MeasurementIdUpperRange(self) -> int:
        """
        Getter for property: (int) MeasurementIdUpperRange
         Returns the measurement id upper range   
            
         
        """
        pass
    @MeasurementIdUpperRange.setter
    def MeasurementIdUpperRange(self, measurementIdUpperRange: int):
        """
        Setter for property: (int) MeasurementIdUpperRange
         Returns the measurement id upper range   
            
         
        """
        pass
    @property
    def MeasurementNamePrefix(self) -> str:
        """
        Getter for property: (str) MeasurementNamePrefix
         Returns the measurement name prefix   
            
         
        """
        pass
    @MeasurementNamePrefix.setter
    def MeasurementNamePrefix(self, measurementNamePrefix: str):
        """
        Setter for property: (str) MeasurementNamePrefix
         Returns the measurement name prefix   
            
         
        """
        pass
    @property
    def MeasurementObjectColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) MeasurementObjectColor
         Returns the measurement object color   
            
         
        """
        pass
    @MeasurementObjectColor.setter
    def MeasurementObjectColor(self, measurementObjectColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) MeasurementObjectColor
         Returns the measurement object color   
            
         
        """
        pass
    @property
    def MeasurementObjectLayer(self) -> int:
        """
        Getter for property: (int) MeasurementObjectLayer
         Returns the measurement object layer   
            
         
        """
        pass
    @MeasurementObjectLayer.setter
    def MeasurementObjectLayer(self, measurementObjectLayer: int):
        """
        Setter for property: (int) MeasurementObjectLayer
         Returns the measurement object layer   
            
         
        """
        pass
    @property
    def MeasurementPartNumber(self) -> str:
        """
        Getter for property: (str) MeasurementPartNumber
         Returns the measurement part number   
            
         
        """
        pass
    @MeasurementPartNumber.setter
    def MeasurementPartNumber(self, measurementPartNumber: str):
        """
        Setter for property: (str) MeasurementPartNumber
         Returns the measurement part number   
            
         
        """
        pass
    @property
    def WeldArcGridLineEndCapDisp(self) -> float:
        """
        Getter for property: (float) WeldArcGridLineEndCapDisp
         Returns the weld arc grid line end cap disp   
            
         
        """
        pass
    @WeldArcGridLineEndCapDisp.setter
    def WeldArcGridLineEndCapDisp(self, weldArcGridLineEndCapDisp: float):
        """
        Setter for property: (float) WeldArcGridLineEndCapDisp
         Returns the weld arc grid line end cap disp   
            
         
        """
        pass
    @property
    def WeldArcGridLineTopDisp(self) -> float:
        """
        Getter for property: (float) WeldArcGridLineTopDisp
         Returns the weld arc grid line top disp   
            
         
        """
        pass
    @WeldArcGridLineTopDisp.setter
    def WeldArcGridLineTopDisp(self, weldArcGridLineTopDisp: float):
        """
        Setter for property: (float) WeldArcGridLineTopDisp
         Returns the weld arc grid line top disp   
            
         
        """
        pass
    @property
    def WeldAssoColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) WeldAssoColor
         Returns the weld asso color   
            
         
        """
        pass
    @WeldAssoColor.setter
    def WeldAssoColor(self, weldAssoColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) WeldAssoColor
         Returns the weld asso color   
            
         
        """
        pass
    @property
    def WeldConstLayer(self) -> int:
        """
        Getter for property: (int) WeldConstLayer
         Returns the weld const layer   
            
         
        """
        pass
    @WeldConstLayer.setter
    def WeldConstLayer(self, weldConstLayer: int):
        """
        Setter for property: (int) WeldConstLayer
         Returns the weld const layer   
            
         
        """
        pass
    @property
    def WeldFixedColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) WeldFixedColor
         Returns the weld fixed color   
            
         
        """
        pass
    @WeldFixedColor.setter
    def WeldFixedColor(self, weldFixedColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) WeldFixedColor
         Returns the weld fixed color   
            
         
        """
        pass
    @property
    def WeldGroupIdLowerRange(self) -> str:
        """
        Getter for property: (str) WeldGroupIdLowerRange
         Returns the weld group id lower range   
            
         
        """
        pass
    @WeldGroupIdLowerRange.setter
    def WeldGroupIdLowerRange(self, weldGroupIdLowerRange: str):
        """
        Setter for property: (str) WeldGroupIdLowerRange
         Returns the weld group id lower range   
            
         
        """
        pass
    @property
    def WeldGroupIdUpperRange(self) -> str:
        """
        Getter for property: (str) WeldGroupIdUpperRange
         Returns the weld group id upper range   
            
         
        """
        pass
    @WeldGroupIdUpperRange.setter
    def WeldGroupIdUpperRange(self, weldGroupIdUpperRange: str):
        """
        Setter for property: (str) WeldGroupIdUpperRange
         Returns the weld group id upper range   
            
         
        """
        pass
    @property
    def WeldIdLowerRange(self) -> int:
        """
        Getter for property: (int) WeldIdLowerRange
         Returns the weld id lower range   
            
         
        """
        pass
    @WeldIdLowerRange.setter
    def WeldIdLowerRange(self, weldIdLowerRange: int):
        """
        Setter for property: (int) WeldIdLowerRange
         Returns the weld id lower range   
            
         
        """
        pass
    @property
    def WeldIdUpperRange(self) -> int:
        """
        Getter for property: (int) WeldIdUpperRange
         Returns the weld id upper range   
            
         
        """
        pass
    @WeldIdUpperRange.setter
    def WeldIdUpperRange(self, weldIdUpperRange: int):
        """
        Setter for property: (int) WeldIdUpperRange
         Returns the weld id upper range   
            
         
        """
        pass
    @property
    def WeldNamePrefix(self) -> str:
        """
        Getter for property: (str) WeldNamePrefix
         Returns the weld name prefix   
            
         
        """
        pass
    @WeldNamePrefix.setter
    def WeldNamePrefix(self, weldNamePrefix: str):
        """
        Setter for property: (str) WeldNamePrefix
         Returns the weld name prefix   
            
         
        """
        pass
    @property
    def WeldObjectLayer(self) -> int:
        """
        Getter for property: (int) WeldObjectLayer
         Returns the weld object layer   
            
         
        """
        pass
    @WeldObjectLayer.setter
    def WeldObjectLayer(self, weldObjectLayer: int):
        """
        Setter for property: (int) WeldObjectLayer
         Returns the weld object layer   
            
         
        """
        pass
    @property
    def WeldPartNumber(self) -> str:
        """
        Getter for property: (str) WeldPartNumber
         Returns the weld part number   
            
         
        """
        pass
    @WeldPartNumber.setter
    def WeldPartNumber(self, weldPartNumber: str):
        """
        Setter for property: (str) WeldPartNumber
         Returns the weld part number   
            
         
        """
        pass
    @property
    def WeldRetainedColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) WeldRetainedColor
         Returns the weld retained color   
            
         
        """
        pass
    @WeldRetainedColor.setter
    def WeldRetainedColor(self, weldRetainedColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) WeldRetainedColor
         Returns the weld retained color   
            
         
        """
        pass
    @property
    def WeldSymbolDecimalPlaces(self) -> int:
        """
        Getter for property: (int) WeldSymbolDecimalPlaces
         Returns the weld sym dec places   
            
         
        """
        pass
    @WeldSymbolDecimalPlaces.setter
    def WeldSymbolDecimalPlaces(self, weldSymbolDecimalPlaces: int):
        """
        Setter for property: (int) WeldSymbolDecimalPlaces
         Returns the weld sym dec places   
            
         
        """
        pass
    def GetDatumSelectedPrefix(self) -> List[str]:
        """
         The datum selected prefix 
         Returns datumSelectedPrefix (List[str]):  Selected datum prefix .
        """
        pass
    def GetDatumSelectedSuffix(self) -> List[str]:
        """
         The datum selected suffix 
         Returns datumSelectedSuffix (List[str]):  Selected datum suffix .
        """
        pass
    def GetMeasurementSelectedPrefix(self) -> List[str]:
        """
         The measurement selected prefix 
         Returns measurementSelectedPrefix (List[str]):  Selected measurement prefix .
        """
        pass
    def GetMeasurementSelectedSuffix(self) -> List[str]:
        """
         The measurement selected suffix 
         Returns measurementSelectedSuffix (List[str]):  Selected measurement suffix .
        """
        pass
    def SetDatumSelectedPrefix(self, datumSelectedPrefix: List[str]) -> None:
        """
         The datum selected prefix 
        """
        pass
    def SetDatumSelectedSuffix(self, datumSelectedSuffix: List[str]) -> None:
        """
         Selected datum suffix 
        """
        pass
    def SetMeasurementSelectedPrefix(self, measurementSelectedPrefix: List[str]) -> None:
        """
         The measurement selected prefix 
        """
        pass
    def SetMeasurementSelectedSuffix(self, measurementSelectedSuffix: List[str]) -> None:
        """
         Selected measurement suffix 
        """
        pass
class WeldPrepareEdges(Enum):
    """
    Members Include: 
     |NotSet|  Output edges will not be prepared 
     |EntireEdge|  Output edges will be prepared for entire edge length 
     |WeldLimits|  Output edges will be prepared for the weld length only 
     |Complex|  Same as entire edge, but use if a portion of target body is below the desired weld 

    """
    NotSet: int
    EntireEdge: int
    WeldLimits: int
    Complex: int
    @staticmethod
    def ValueOf(value: int) -> WeldPrepareEdges:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class WeldProjectionMethod(Enum):
    """
    Members Include: 
     |NotSet|  creates only a point 
     |FaceNormal|  creates a sphere 
     |AlongVector|  creates a cylinder 

    """
    NotSet: int
    FaceNormal: int
    AlongVector: int
    @staticmethod
    def ValueOf(value: int) -> WeldProjectionMethod:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class WeldRootUpdate(Enum):
    """
    Members Include: 
     |Automatic|  Automatically compute the root opening 
     |NotSet|  Use user specified root opening 

    """
    Automatic: int
    NotSet: int
    @staticmethod
    def ValueOf(value: int) -> WeldRootUpdate:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class WeldSelectionType(Enum):
    """
    Members Include: 
     |General|  general type 
     |Surface|  surface 
     |Curve|  curve 

    """
    General: int
    Surface: int
    Curve: int
    @staticmethod
    def ValueOf(value: int) -> WeldSelectionType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class WeldSpacingCalcMethod(Enum):
    """
    Members Include: 
     |Arclength|  spaces based on arc length 
     |ParallelXPlane|  spaces based on parallel x planes 
     |ParallelYPlane|  spaces based on parallel y planes 
     |ParallelZPlane|  spaces based on parallel z planes 
     |MiddleOfCurve|  spaces based on middle of curve 
     |NormalToBody|  spaces based on normal to body 

    """
    Arclength: int
    ParallelXPlane: int
    ParallelYPlane: int
    ParallelZPlane: int
    MiddleOfCurve: int
    NormalToBody: int
    @staticmethod
    def ValueOf(value: int) -> WeldSpacingCalcMethod:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class WeldTaperMethod(Enum):
    """
    Members Include: 
     |FromEndFace|  Taper will be measured from groove end caps 
     |FromSideFace|  Taper will be measured from groove side face 

    """
    FromEndFace: int
    FromSideFace: int
    @staticmethod
    def ValueOf(value: int) -> WeldTaperMethod:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
