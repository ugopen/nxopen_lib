from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.Features
class AlignmentMethodBuilder1(NXOpen.TaggedObject): 
    """ Represents a NXOpen.GeometricUtilities.AlignmentMethodBuilder1 """
    class FillerSurfaceType(Enum):
        """
        Members Include: 
         |NoFiller|  No end filler surface 
         |GeneralizedCone|  Generalized conical developable surface 
         |GeneralizedCylinder|  Generalized cylindrical developable surface 
         |ExtrapolateAndTrim| 

        """
        NoFiller: int
        GeneralizedCone: int
        GeneralizedCylinder: int
        ExtrapolateAndTrim: int
        @staticmethod
        def ValueOf(value: int) -> AlignmentMethodBuilder1.FillerSurfaceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Type(Enum):
        """
        Members Include: 
         |Parameter|  
         |ArcLength|  
         |ByPoints|  
         |Distance|  
         |Angle|  
         |SpineCurve|  
         |BySegments|  
         |Developable| 

        """
        Parameter: int
        ArcLength: int
        ByPoints: int
        Distance: int
        Angle: int
        SpineCurve: int
        BySegments: int
        Developable: int
        @staticmethod
        def ValueOf(value: int) -> AlignmentMethodBuilder1.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AlignAxis(self) -> NXOpen.Axis:
        """
        Getter for property: ( NXOpen.Axis) AlignAxis
         Returns the alignment axis   
            
         
        """
        pass
    @AlignAxis.setter
    def AlignAxis(self, alignAxis: NXOpen.Axis):
        """
        Setter for property: ( NXOpen.Axis) AlignAxis
         Returns the alignment axis   
            
         
        """
        pass
    @property
    def AlignCurve(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) AlignCurve
         Returns the align curve   
            
         
        """
        pass
    @property
    def AlignType(self) -> AlignmentMethodBuilder1.Type:
        """
        Getter for property: ( AlignmentMethodBuilder1.Type NXOpen.Geome) AlignType
         Returns the alignment type   
            
         
        """
        pass
    @AlignType.setter
    def AlignType(self, alignType: AlignmentMethodBuilder1.Type):
        """
        Setter for property: ( AlignmentMethodBuilder1.Type NXOpen.Geome) AlignType
         Returns the alignment type   
            
         
        """
        pass
    @property
    def AlignVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) AlignVector
         Returns the alignment vector   
            
         
        """
        pass
    @AlignVector.setter
    def AlignVector(self, alignVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) AlignVector
         Returns the alignment vector   
            
         
        """
        pass
    @property
    def EndAlignFillerSurfaceOption(self) -> AlignmentMethodBuilder1.FillerSurfaceType:
        """
        Getter for property: ( AlignmentMethodBuilder1.FillerSurfaceType NXOpen.Geome) EndAlignFillerSurfaceOption
         Returns the end align filler surface option   
            
         
        """
        pass
    @EndAlignFillerSurfaceOption.setter
    def EndAlignFillerSurfaceOption(self, endAlignFillerSurfaceOption: AlignmentMethodBuilder1.FillerSurfaceType):
        """
        Setter for property: ( AlignmentMethodBuilder1.FillerSurfaceType NXOpen.Geome) EndAlignFillerSurfaceOption
         Returns the end align filler surface option   
            
         
        """
        pass
    @property
    def Points(self) -> NXOpen.Features.GeometricConstraintDataManager:
        """
        Getter for property: ( NXOpen.Features.GeometricConstraintDataManager) Points
         Returns the points   
            
         
        """
        pass
    @property
    def StartAlignFillerSurfaceOption(self) -> AlignmentMethodBuilder1.FillerSurfaceType:
        """
        Getter for property: ( AlignmentMethodBuilder1.FillerSurfaceType NXOpen.Geome) StartAlignFillerSurfaceOption
         Returns the start align filler surface option   
            
         
        """
        pass
    @StartAlignFillerSurfaceOption.setter
    def StartAlignFillerSurfaceOption(self, startAlignFillerSurfaceOption: AlignmentMethodBuilder1.FillerSurfaceType):
        """
        Setter for property: ( AlignmentMethodBuilder1.FillerSurfaceType NXOpen.Geome) StartAlignFillerSurfaceOption
         Returns the start align filler surface option   
            
         
        """
        pass
    def DeleteAllPoints(self) -> None:
        """
         Deletes all alignment points on all sections 
        """
        pass
    def DeletePoint(self, point: NXOpen.Point) -> None:
        """
         Deletes an alignment point and corresponding alignment points on all sections 
        """
        pass
    def InsertPoint(self, point: NXOpen.Point) -> None:
        """
         Insert alignment point and create alignment points on all sections 
        """
        pass
    def MovePointByPercentParameter(self, point: NXOpen.Point, percentParameterOfSection: float) -> None:
        """
         Moves alignment point based on percentage parameter value of section on which it resides. 
        """
        pass
    def PostPointEdit(self, point: NXOpen.Point) -> None:
        """
         Updates internal data based on edited point. Call this method after a point is edited. 
        """
        pass
    def ResetAllPoints(self) -> None:
        """
         Reset Points. 
        """
        pass
import NXOpen
class AlignmentMethodBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.GeometricUtilities.AlignmentMethodBuilder
    """
    class AlignFillerSurfaceType(Enum):
        """
        Members Include: 
         |NoFiller|  No end filler surface 
         |Cone| Generalized conical developable surface.
         |Cylinder| Generalized cylindrical developable surface.
         |Trimmed| Trimmed developable surface.

        """
        NoFiller: int
        Cone: int
        Cylinder: int
        Trimmed: int
        @staticmethod
        def ValueOf(value: int) -> AlignmentMethodBuilder.AlignFillerSurfaceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Type(Enum):
        """
        Members Include: 
         |Parameter|  
         |ArcLength|  
         |Points|  
         |Distance|  
         |Angle|  
         |SpineCurve|  
         |SplinePoints|  
         |Segments|  
         |Developable|  

        """
        Parameter: int
        ArcLength: int
        Points: int
        Distance: int
        Angle: int
        SpineCurve: int
        SplinePoints: int
        Segments: int
        Developable: int
        @staticmethod
        def ValueOf(value: int) -> AlignmentMethodBuilder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AlignAxis(self) -> NXOpen.Axis:
        """
        Getter for property: ( NXOpen.Axis) AlignAxis
         Returns the alignment axis   
            
         
        """
        pass
    @AlignAxis.setter
    def AlignAxis(self, alignAxis: NXOpen.Axis):
        """
        Setter for property: ( NXOpen.Axis) AlignAxis
         Returns the alignment axis   
            
         
        """
        pass
    @property
    def AlignCurve(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) AlignCurve
         Returns the align curve   
            
         
        """
        pass
    @property
    def AlignType(self) -> AlignmentMethodBuilder.Type:
        """
        Getter for property: ( AlignmentMethodBuilder.Type NXOpen.Geome) AlignType
         Returns the alignment type   
            
         
        """
        pass
    @AlignType.setter
    def AlignType(self, alignType: AlignmentMethodBuilder.Type):
        """
        Setter for property: ( AlignmentMethodBuilder.Type NXOpen.Geome) AlignType
         Returns the alignment type   
            
         
        """
        pass
    @property
    def AlignVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) AlignVector
         Returns the alignment vector   
            
         
        """
        pass
    @AlignVector.setter
    def AlignVector(self, alignVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) AlignVector
         Returns the alignment vector   
            
         
        """
        pass
    @property
    def EndAlignFillerSurfaceOption(self) -> AlignmentMethodBuilder.AlignFillerSurfaceType:
        """
        Getter for property: ( AlignmentMethodBuilder.AlignFillerSurfaceType NXOpen.Geome) EndAlignFillerSurfaceOption
         Returns the end align filler surface option   
            
         
        """
        pass
    @EndAlignFillerSurfaceOption.setter
    def EndAlignFillerSurfaceOption(self, fillerSurfaceType: AlignmentMethodBuilder.AlignFillerSurfaceType):
        """
        Setter for property: ( AlignmentMethodBuilder.AlignFillerSurfaceType NXOpen.Geome) EndAlignFillerSurfaceOption
         Returns the end align filler surface option   
            
         
        """
        pass
    @property
    def NumberOfPointsPerSection(self) -> int:
        """
        Getter for property: (int) NumberOfPointsPerSection
         Returns the number of alignment points in each section.  
           All the sections always have same number of alignment points    
         
        """
        pass
    @property
    def NumberOfSections(self) -> int:
        """
        Getter for property: (int) NumberOfSections
         Returns the number of section in the alignment point block   
            
         
        """
        pass
    @property
    def StartAlignFillerSurfaceOption(self) -> AlignmentMethodBuilder.AlignFillerSurfaceType:
        """
        Getter for property: ( AlignmentMethodBuilder.AlignFillerSurfaceType NXOpen.Geome) StartAlignFillerSurfaceOption
         Returns the start align filler surface option   
            
         
        """
        pass
    @StartAlignFillerSurfaceOption.setter
    def StartAlignFillerSurfaceOption(self, fillerSurfaceType: AlignmentMethodBuilder.AlignFillerSurfaceType):
        """
        Setter for property: ( AlignmentMethodBuilder.AlignFillerSurfaceType NXOpen.Geome) StartAlignFillerSurfaceOption
         Returns the start align filler surface option   
            
         
        """
        pass
    def AddPoint(self, alignPoint: OnPathDimensionBuilder) -> int:
        """
         Insert a given point, and create corresponding points on other sections.  The points on other sections
                    are computed based on existing alignment points 
         Returns alignmentRowIndex (int):  Index of the newly added point on each section .
        """
        pass
    def AddSection(self, sectionIndex: int, sec: NXOpen.Section) -> None:
        """
         Add a section at the given index among existing sections.  Computes points for other sections 
        """
        pass
    def ComputeDefaultPoints(self) -> None:
        """
         Calculate default alignment points on existing sections.  Pre-existing alignment points destroyed 
        """
        pass
    def CreateOnPathDimBuilder(self, sec: NXOpen.Section, pnt: NXOpen.Point3d) -> OnPathDimensionBuilder:
        """
         Set the sections.  Does not compute default alignment 
         Returns alignPoint ( OnPathDimensionBuilder NXOpen.Geome):  The generated onPathDim.
        """
        pass
    def GetAllPoints(self) -> Tuple[List[OnPathDimensionBuilder], int]:
        """
         Get all of the alignment points, returns as a single dimension array 
         Returns A tuple consisting of (alignPoints, numSection). 
         - alignPoints is:  OnPathDimensionBuilder List[NXOpen.Geo. Gets all the points, numPoints is total number of points, not points per section .
         - numSection is: int. Number of sections returned.

        """
        pass
    def GetPoint(self, sectionIndex: int, pointIndex: int) -> OnPathDimensionBuilder:
        """
         Gets an alignment point for a section 
         Returns alignPoint ( OnPathDimensionBuilder NXOpen.Geome):  .
        """
        pass
    def RemoveAllPoints(self) -> None:
        """
         Remove all alignment points.   Keeps the sections 
        """
        pass
    def RemovePoint(self, alignPoint: OnPathDimensionBuilder) -> None:
        """
         Remove given point, also remove corresponding points on other sections 
        """
        pass
    def RemoveSection(self, sec: NXOpen.Section) -> None:
        """
         Find and delete the section 
        """
        pass
    def RemoveSectionAtIndex(self, secIndex: int) -> None:
        """
         Remove section at given index 
        """
        pass
    def SetAlignPoints(self, alignPoints: List[OnPathDimensionBuilder]) -> None:
        """
         Set the Alignment Points when sections have been set up.
                    The incoming points are organized section by section.  The points
                    parent section match the pre-existing sections held by this object 
        """
        pass
    def SetSections(self, sections: List[NXOpen.Section]) -> None:
        """
         Set the sections.  Does not compute default alignment 
        """
        pass
    def UnloadSections(self) -> None:
        """
         Unload sections held by the builder 
        """
        pass
    def UpdateSectionAtIndex(self, secIndex: int) -> None:
        """
         Update section at given index 
        """
        pass
import NXOpen
class AlongPathPattern(NXOpen.TaggedObject): 
    """ the AlongPath pattern definition.  Allows specification along
        two section pathes. """
    class PathOptions(Enum):
        """
        Members Include: 
         |Rigid|  path is the selected section. 
         |Offset|  path is an offset from the selected path. 
         |Translate|  path is a translation from the selected path. 

        """
        Rigid: int
        Offset: int
        Translate: int
        @staticmethod
        def ValueOf(value: int) -> AlongPathPattern.PathOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class YDirectionOptions(Enum):
        """
        Members Include: 
         |Vector|  y direction is a vector. 
         |Section|  y direction is a section. 

        """
        Vector: int
        Section: int
        @staticmethod
        def ValueOf(value: int) -> AlongPathPattern.YDirectionOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def UseYDirectionToggle(self) -> bool:
        """
        Getter for property: (bool) UseYDirectionToggle
         Returns the UseYDirection toggle attribute.  
           This function gets the UseYDirection toggle value   
         
        """
        pass
    @UseYDirectionToggle.setter
    def UseYDirectionToggle(self, toggle: bool):
        """
        Setter for property: (bool) UseYDirectionToggle
         Returns the UseYDirection toggle attribute.  
           This function gets the UseYDirection toggle value   
         
        """
        pass
    @property
    def XOnPathSpacing(self) -> OnPathDistancePatternSpacing:
        """
        Getter for property: ( OnPathDistancePatternSpacing NXOpen.Geome) XOnPathSpacing
         Returns the on path instance spacing along the x path   
            
         
        """
        pass
    @property
    def XPath(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) XPath
         Returns the x path   
            
         
        """
        pass
    @XPath.setter
    def XPath(self, xPath: NXOpen.Section):
        """
        Setter for property: ( NXOpen.Section) XPath
         Returns the x path   
            
         
        """
        pass
    @property
    def XPathOption(self) -> AlongPathPattern.PathOptions:
        """
        Getter for property: ( AlongPathPattern.PathOptions NXOpen.Geome) XPathOption
         Returns the x path options   
            
         
        """
        pass
    @XPathOption.setter
    def XPathOption(self, xPathOption: AlongPathPattern.PathOptions):
        """
        Setter for property: ( AlongPathPattern.PathOptions NXOpen.Geome) XPathOption
         Returns the x path options   
            
         
        """
        pass
    @property
    def YDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) YDirection
         Returns the y axis, which can be any vector not parallel to the x axis   
            
         
        """
        pass
    @YDirection.setter
    def YDirection(self, yDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) YDirection
         Returns the y axis, which can be any vector not parallel to the x axis   
            
         
        """
        pass
    @property
    def YDirectionOption(self) -> AlongPathPattern.YDirectionOptions:
        """
        Getter for property: ( AlongPathPattern.YDirectionOptions NXOpen.Geome) YDirectionOption
         Returns the y direction options   
            
         
        """
        pass
    @YDirectionOption.setter
    def YDirectionOption(self, yDirectionOption: AlongPathPattern.YDirectionOptions):
        """
        Setter for property: ( AlongPathPattern.YDirectionOptions NXOpen.Geome) YDirectionOption
         Returns the y direction options   
            
         
        """
        pass
    @property
    def YOnPathSpacing(self) -> OnPathDistancePatternSpacing:
        """
        Getter for property: ( OnPathDistancePatternSpacing NXOpen.Geome) YOnPathSpacing
         Returns the on path instance spacing along the y path   
            
         
        """
        pass
    @property
    def YPath(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) YPath
         Returns the y path, which can be any continuous section   
            
         
        """
        pass
    @YPath.setter
    def YPath(self, yPath: NXOpen.Section):
        """
        Setter for property: ( NXOpen.Section) YPath
         Returns the y path, which can be any continuous section   
            
         
        """
        pass
    @property
    def YPathOption(self) -> AlongPathPattern.PathOptions:
        """
        Getter for property: ( AlongPathPattern.PathOptions NXOpen.Geome) YPathOption
         Returns the y path options   
            
         
        """
        pass
    @YPathOption.setter
    def YPathOption(self, yPathOption: AlongPathPattern.PathOptions):
        """
        Setter for property: ( AlongPathPattern.PathOptions NXOpen.Geome) YPathOption
         Returns the y path options   
            
         
        """
        pass
    @property
    def YSpacing(self) -> DistancePatternSpacing:
        """
        Getter for property: ( DistancePatternSpacing NXOpen.Geome) YSpacing
         Returns the instance spacing along the y axis   
            
         
        """
        pass
import NXOpen
class AlongSpineBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.GeometricUtilities.AlongSpineBuilder
    """
    class RetainSpineOption(Enum):
        """
        Members Include: 
         |KeepOriginal|  Keeps the original profile as it is during edit of pre NX3 parms 
         |Replace|  Deletes the old profile, so that user has to select new one during edit of pre NX3 parms 

        """
        KeepOriginal: int
        Replace: int
        @staticmethod
        def ValueOf(value: int) -> AlongSpineBuilder.RetainSpineOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FeatureSpine(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) FeatureSpine
         Returns the Spine set by the owning feature of the law   
            
         
        """
        pass
    @property
    def Spine(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Spine
         Returns the Spine   
            
         
        """
        pass
    @property
    def SpineOption(self) -> AlongSpineBuilder.RetainSpineOption:
        """
        Getter for property: ( AlongSpineBuilder.RetainSpineOption NXOpen.Geome) SpineOption
         Returns the spine option of the legacy features.  
            This will be used only during the edit of Pre NX3 feature Parms   
         
        """
        pass
    @SpineOption.setter
    def SpineOption(self, spine_option: AlongSpineBuilder.RetainSpineOption):
        """
        Setter for property: ( AlongSpineBuilder.RetainSpineOption NXOpen.Geome) SpineOption
         Returns the spine option of the legacy features.  
            This will be used only during the edit of Pre NX3 feature Parms   
         
        """
        pass
    @property
    def SpinePointList(self) -> NXOpen.ObjectList:
        """
        Getter for property: ( NXOpen.ObjectList) SpinePointList
         Returns the list of spine points.  
             
         
        """
        pass
    def CreateSpinePoint(self) -> OnPathDimWithValueBuilder:
        """
         Creates a new spine point 
         Returns dimWithValueBuilder ( OnPathDimWithValueBuilder NXOpen.Geome):  OnPathDimWithValueBuilder Object .
        """
        pass
    def GetSpinePoints(self) -> List[OnPathDimWithValueBuilder]:
        """
         Returns the all SpinePointData objects 
         Returns sp_points ( OnPathDimWithValueBuilder List[NXOpen.Geo):  Array of SpinePointData Objects .
        """
        pass
    def ResetSpine(self) -> None:
        """
         Reset the spine  
        """
        pass
    def SetFeatureSpine(self, featureSpine: NXOpen.Section) -> None:
        """
         Set the spine sent by the owning feature dynamically into builder 
        """
        pass
import NXOpen
class AnchorLocatorBuilder(NXOpen.TaggedObject): 
    """ Represents a NXOpen.GeometricUtilities.AnchorLocatorBuilder """
    @property
    def Origin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) Origin
         Returns the origin of the plane   
            
         
        """
        pass
    @Origin.setter
    def Origin(self, origin: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) Origin
         Returns the origin of the plane   
            
         
        """
        pass
    @property
    def XAxis(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) XAxis
         Returns the x-axis of the plane   
            
         
        """
        pass
    @XAxis.setter
    def XAxis(self, xAxis: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) XAxis
         Returns the x-axis of the plane   
            
         
        """
        pass
    @property
    def YAxis(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) YAxis
         Returns the y-axis of the plane   
            
         
        """
        pass
    @YAxis.setter
    def YAxis(self, yAxis: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) YAxis
         Returns the y-axis of the plane   
            
         
        """
        pass
class AngularLimits(Limits): 
    """ Represents a angular limts data. 
    """
    @property
    def Distance(self) -> float:
        """
        Getter for property: (float) Distance
         Returns a computed distance  
            
         
        """
        pass
import NXOpen
class AngularPatternSpacing(PatternSpacing): 
    """ defines the various ways pattern instances can be 
        spaced within the pattern, particularly in the context of the
        PatternDefinition class. """
    class UsePitchOptions(Enum):
        """
        Members Include: 
         |Angle|  angle is pitch value 
         |Distance|  distance is pitch value. 

        """
        Angle: int
        Distance: int
        @staticmethod
        def ValueOf(value: int) -> AngularPatternSpacing.UsePitchOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def PitchAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PitchAngle
         Returns the angle for the spacing of the pattern from one instance to the next.  
            
         
        """
        pass
    @property
    def PitchDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PitchDistance
         Returns the circumfrential distance for the spacing of the pattern from one instance to the next.  
            
         
        """
        pass
    @property
    def SpanAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SpanAngle
         Returns the angle for the spacing of the pattern for the entire pattern.  
             
         
        """
        pass
    @property
    def UsePitchOption(self) -> AngularPatternSpacing.UsePitchOptions:
        """
        Getter for property: ( AngularPatternSpacing.UsePitchOptions NXOpen.Geome) UsePitchOption
         Returns the switch to use Pitch Distance or Pitch Angle.  
             
         
        """
        pass
    @UsePitchOption.setter
    def UsePitchOption(self, usePitchOption: AngularPatternSpacing.UsePitchOptions):
        """
        Setter for property: ( AngularPatternSpacing.UsePitchOptions NXOpen.Geome) UsePitchOption
         Returns the switch to use Pitch Distance or Pitch Angle.  
             
         
        """
        pass
import NXOpen
class BetweenLocationsData(NXOpen.TaggedObject): 
    """ Represents a NXOpen.GeometricUtilities.BetweenLocationsData
    """
    @property
    def FromLocation(self) -> GeometryLocationData:
        """
        Getter for property: ( GeometryLocationData NXOpen.Geome) FromLocation
         Returns the from location   
            
         
        """
        pass
    @property
    def ToLocationList(self) -> NXOpen.TaggedObjectList:
        """
        Getter for property: ( NXOpen.TaggedObjectList) ToLocationList
         Returns the to location list   
            
         
        """
        pass
import NXOpen
class BlendLimitsData(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.GeometricUtilities.BlendLimitsData
    """
    @property
    def CapsList(self) -> NXOpen.TaggedObjectList:
        """
        Getter for property: ( NXOpen.TaggedObjectList) CapsList
         Returns the caps list   
            
         
        """
        pass
    @property
    def UserSelectedObjects(self) -> bool:
        """
        Getter for property: (bool) UserSelectedObjects
         Returns the use plane cap blend   
            
         
        """
        pass
    @UserSelectedObjects.setter
    def UserSelectedObjects(self, useSelectedObject: bool):
        """
        Setter for property: (bool) UserSelectedObjects
         Returns the use plane cap blend   
            
         
        """
        pass
import NXOpen
class BlendSetbackBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[BlendSetbackBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: BlendSetbackBuilder) -> None:
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
    def Erase(self, obj: BlendSetbackBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: BlendSetbackBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: BlendSetbackBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> BlendSetbackBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( BlendSetbackBuilder NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[BlendSetbackBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( BlendSetbackBuilder List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: BlendSetbackBuilder) -> None:
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
    def SetContents(self, objects: List[BlendSetbackBuilder]) -> None:
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
    def Swap(self, object1: BlendSetbackBuilder, object2: BlendSetbackBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class BlendSetbackBuilder(NXOpen.TaggedObject): 
    """
        This class provides ability to define a setback curve on a blend face.
    """
    class Directions(Enum):
        """
        Members Include: 
         |U|  setback curve is an iso-u parameter curve 
         |V|  setback curve is an iso-v parameter curve 
         |Plane|  setback curve is the intersection curve between a plane and faces 

        """
        U: int
        V: int
        Plane: int
        @staticmethod
        def ValueOf(value: int) -> BlendSetbackBuilder.Directions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Direction(self) -> BlendSetbackBuilder.Directions:
        """
        Getter for property: ( BlendSetbackBuilder.Directions NXOpen.Geome) Direction
         Returns the direction type   
            
         
        """
        pass
    @Direction.setter
    def Direction(self, direction: BlendSetbackBuilder.Directions):
        """
        Setter for property: ( BlendSetbackBuilder.Directions NXOpen.Geome) Direction
         Returns the direction type   
            
         
        """
        pass
    @property
    def Face(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Face
         Returns the blend face collector.  
           The collector can include faces from different blends.   
         
        """
        pass
    @property
    def HandlePoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) HandlePoint
         Returns the handle point for uv direction.  
           The setback curve will pass through the handle point.   
         
        """
        pass
    @HandlePoint.setter
    def HandlePoint(self, handlekPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) HandlePoint
         Returns the handle point for uv direction.  
           The setback curve will pass through the handle point.   
         
        """
        pass
    @property
    def IsDirectionFlipped(self) -> bool:
        """
        Getter for property: (bool) IsDirectionFlipped
         Returns the flag indicating if the setback curve direction is flipped.  
             
         
        """
        pass
    @IsDirectionFlipped.setter
    def IsDirectionFlipped(self, flipDirection: bool):
        """
        Setter for property: (bool) IsDirectionFlipped
         Returns the flag indicating if the setback curve direction is flipped.  
             
         
        """
        pass
    @property
    def Plane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) Plane
         Returns the setback plane.  
           The setback curve will be the intersection curve between plane and face collector.   
         
        """
        pass
    @Plane.setter
    def Plane(self, plane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) Plane
         Returns the setback plane.  
           The setback curve will be the intersection curve between plane and face collector.   
         
        """
        pass
    @property
    def SetbackPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) SetbackPoint
         Returns the setback point for uv direction.  
           This point is optional. 
                    If specified, it will replace the handle point and establish the associativity 
                    between the point and the setback curve. 
                    Once the handle point is changed through dragging, the associativity will be lost.   
         
        """
        pass
    @SetbackPoint.setter
    def SetbackPoint(self, setbackPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) SetbackPoint
         Returns the setback point for uv direction.  
           This point is optional. 
                    If specified, it will replace the handle point and establish the associativity 
                    between the point and the setback curve. 
                    Once the handle point is changed through dragging, the associativity will be lost.   
         
        """
        pass
import NXOpen
class BlendStopshortBuilderCollection(NXOpen.TaggedObjectCollection): 
    """ This class contains the factory methods for creating an BlendStopshortBuilder. """
    def Create(self, m_choice: BlendStopshortBuilder.Choices, m_on_path_exp: NXOpen.Expression, m_path: NXOpen.Edge, m_is_flipped: bool, m_thru_point: NXOpen.Point) -> BlendStopshortBuilder:
        """
         Creates an BlendStopshortBuilder. 
         Returns ss_builder ( BlendStopshortBuilder NXOpen.Geome): .
        """
        pass
import NXOpen
class BlendStopshortBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.GeometricUtilities.BlendStopshortBuilder
    """
    class Choices(Enum):
        """
        Members Include: 
         |AtDistance|  Distance 
         |AtIntersection|  Intersection 

        """
        AtDistance: int
        AtIntersection: int
        @staticmethod
        def ValueOf(value: int) -> BlendStopshortBuilder.Choices:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Choice(self) -> BlendStopshortBuilder.Choices:
        """
        Getter for property: ( BlendStopshortBuilder.Choices NXOpen.Geome) Choice
         Returns the Stopshort option choice.  
           Choose from 'At Distance' or 'At Intersection'.   
         
        """
        pass
    @Choice.setter
    def Choice(self, mChoice: BlendStopshortBuilder.Choices):
        """
        Setter for property: ( BlendStopshortBuilder.Choices NXOpen.Geome) Choice
         Returns the Stopshort option choice.  
           Choose from 'At Distance' or 'At Intersection'.   
         
        """
        pass
    @property
    def OnPath(self) -> OnPathDimensionBuilder:
        """
        Getter for property: ( OnPathDimensionBuilder NXOpen.Geome) OnPath
         Returns the  NXOpen::GeometricUtilities::BlendStopshortBuilder  subobject.  
             
         
        """
        pass
    def Destroy(self) -> None:
        """
         Destructor for NXOpen.GeometricUtilities.BlendStopshortBuilder 
        """
        pass
    def FlipPath(self) -> None:
        """
         Flip the builder path for NXOpen.GeometricUtilities.BlendStopshortBuilder 
        """
        pass
import NXOpen
class BooleanOperation(NXOpen.TaggedObject): 
    """ Represents a boolean operation .  
    """
    class BooleanType(Enum):
        """
        Members Include: 
         |Create|  Create 
         |Unite|  Unite 
         |Subtract|  Subtract 
         |Intersect|  Intersect 
         |Sew|  Sew 

        """
        Create: int
        Unite: int
        Subtract: int
        Intersect: int
        Sew: int
        @staticmethod
        def ValueOf(value: int) -> BooleanOperation.BooleanType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Type(self) -> BooleanOperation.BooleanType:
        """
        Getter for property: ( BooleanOperation.BooleanType NXOpen.Geome) Type
         Returns  the boolean operation type
                  
            
         
        """
        pass
    @Type.setter
    def Type(self, type: BooleanOperation.BooleanType):
        """
        Setter for property: ( BooleanOperation.BooleanType NXOpen.Geome) Type
         Returns  the boolean operation type
                  
            
         
        """
        pass
    def GetBooleanOperationAndBody(self) -> Tuple[BooleanOperation.BooleanType, NXOpen.Body]:
        """
          Get the Boolean operation type and target body
                
         Returns A tuple consisting of (type, target_body). 
         - type is:  BooleanOperation.BooleanType NXOpen.Geome. boolean type .
         - target_body is:  NXOpen.Body. target body .

        """
        pass
    def GetTargetBodies(self) -> List[NXOpen.Body]:
        """
          Get the target bodies 
                
         Returns target_bodies ( NXOpen.Body Li):  target bodies of boolean .
        """
        pass
    def GetTargetBodiesCollector(self) -> NXOpen.ScCollector:
        """
          Get the target bodies collector
                
         Returns targetBodiesCollector ( NXOpen.ScCollector):  target bodies collector of boolean .
        """
        pass
    def SetBooleanOperationAndBody(self, type: BooleanOperation.BooleanType, target_body: NXOpen.Body) -> None:
        """
          Set the Boolean operation type and target body
                
        """
        pass
    def SetTargetBodies(self, target_bodies: List[NXOpen.Body]) -> None:
        """
          Set the target bodies 
                
        """
        pass
import NXOpen
class BooleanRegionSelect(NXOpen.TaggedObject): 
    """ a class which defines boolean region select. 
      """
    class KeepRemoveOption(Enum):
        """
        Members Include: 
         |Keep|  Selected region will be kept. Default set. 
         |Remove|  Selected reg
        ion will be removed. 

        """
        Keep: int
        Remove: int
        @staticmethod
        def ValueOf(value: int) -> BooleanRegionSelect.KeepRemoveOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SelectOption(Enum):
        """
        Members Include: 
         |NotSet|  No regions to pick 
         |KeepOrRemove|  Keep or remove regions 
         |KeepAndRemove|  Keep and remove regions 

        """
        NotSet: int
        KeepOrRemove: int
        KeepAndRemove: int
        @staticmethod
        def ValueOf(value: int) -> BooleanRegionSelect.SelectOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FindAutomaticRegions(self) -> bool:
        """
        Getter for property: (bool) FindAutomaticRegions
         Returns the boolean region option to find the automaticdefault regions from the input sheet bodies   
            
         
        """
        pass
    @FindAutomaticRegions.setter
    def FindAutomaticRegions(self, findAutomaticRegions: bool):
        """
        Setter for property: (bool) FindAutomaticRegions
         Returns the boolean region option to find the automaticdefault regions from the input sheet bodies   
            
         
        """
        pass
    @property
    def KeepRemoveTargetMethod(self) -> BooleanRegionSelect.KeepRemoveOption:
        """
        Getter for property: ( BooleanRegionSelect.KeepRemoveOption NXOpen.Geome) KeepRemoveTargetMethod
         Returns the boolean region to keepremove method   
            
         
        """
        pass
    @KeepRemoveTargetMethod.setter
    def KeepRemoveTargetMethod(self, targetMethod: BooleanRegionSelect.KeepRemoveOption):
        """
        Setter for property: ( BooleanRegionSelect.KeepRemoveOption NXOpen.Geome) KeepRemoveTargetMethod
         Returns the boolean region to keepremove method   
            
         
        """
        pass
    @property
    def KeepRemoveToolMethod(self) -> BooleanRegionSelect.KeepRemoveOption:
        """
        Getter for property: ( BooleanRegionSelect.KeepRemoveOption NXOpen.Geome) KeepRemoveToolMethod
         Returns the boolean region to keepremove method   
            
         
        """
        pass
    @KeepRemoveToolMethod.setter
    def KeepRemoveToolMethod(self, toolMethod: BooleanRegionSelect.KeepRemoveOption):
        """
        Setter for property: ( BooleanRegionSelect.KeepRemoveOption NXOpen.Geome) KeepRemoveToolMethod
         Returns the boolean region to keepremove method   
            
         
        """
        pass
    @property
    def SelectMethod(self) -> BooleanRegionSelect.SelectOption:
        """
        Getter for property: ( BooleanRegionSelect.SelectOption NXOpen.Geome) SelectMethod
         Returns the boolean region selection method method   
            
         
        """
        pass
    @SelectMethod.setter
    def SelectMethod(self, selectOption: BooleanRegionSelect.SelectOption):
        """
        Setter for property: ( BooleanRegionSelect.SelectOption NXOpen.Geome) SelectMethod
         Returns the boolean region selection method method   
            
         
        """
        pass
    def AppendOneRegionTracker(self) -> RegionTracker:
        """
         Create empty region tracker object and register it on the boolean region select builder 
         Returns regionTracker ( RegionTracker NXOpen.Geome): .
        """
        pass
    def AssignTargets(self, targets: List[NXOpen.TaggedObject]) -> None:
        """
         Assigns the targets to be used for region selection 
        """
        pass
    def ClearAllRegionTrackers(self) -> None:
        """
         Clears all region trackers currently registered on the feature 
        """
        pass
    def ClearRegions(self) -> None:
        """
         Clears all preview regions and the current region trackers 
        """
        pass
    def NotifyBodiesHaveChanged(self, bodySelectionList: NXOpen.ScCollector) -> None:
        """
         Notify that the bodies have changed 
        """
        pass
    def RemoveOneRegionTracker(self, regionTracker: RegionTracker) -> None:
        """
         Remove one specific region tracker object and un-register it on the boolean region select builder 
        """
        pass
import NXOpen
class BooleanToolBuilder(NXOpen.TaggedObject): 
    """ a class which defines boolean tool builder. It provides four types of
       tool creation methods viz. a set of existing faces or datum planes, a new plane
       created on the fly (FacePlaneToolBuilder), extrude or revolve sheet bodies created on the fly by
       a given section and direction (ExtrudeRevolveToolBuilder).
      """
    class BooleanToolType(Enum):
        """
        Members Include: 
         |FaceOrPlane|  Tool consists of sets of faces or datum planes 
         |NewPlane|  Tool consists of plane created on the fly 
         |Extrude|  Tool consists of extrude created on the fly 
         |Revolve|  Tool consists of revolve created on the fly 

        """
        FaceOrPlane: int
        NewPlane: int
        Extrude: int
        Revolve: int
        @staticmethod
        def ValueOf(value: int) -> BooleanToolBuilder.BooleanToolType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ExtrudeRevolveTool(self) -> ExtrudeRevolveToolBuilder:
        """
        Getter for property: ( ExtrudeRevolveToolBuilder NXOpen.Geome) ExtrudeRevolveTool
         Returns the ExtrudeRevolveTool builder.  
           Through this tool, the extrude 
                   or revolve created on the fly can be queried   
         
        """
        pass
    @property
    def FacePlaneTool(self) -> FacePlaneToolBuilder:
        """
        Getter for property: ( FacePlaneToolBuilder NXOpen.Geome) FacePlaneTool
         Returns the FacePlaneTool Builder.  
           Through this tool, the sets of tool facesdatum planes or
                   new plane created on the fly can be queried   
         
        """
        pass
    @property
    def ReverseDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseDirection
         Returns the boolean tool reverse direction option   
            
         
        """
        pass
    @ReverseDirection.setter
    def ReverseDirection(self, reverseDirection: bool):
        """
        Setter for property: (bool) ReverseDirection
         Returns the boolean tool reverse direction option   
            
         
        """
        pass
    @property
    def ToolOption(self) -> BooleanToolBuilder.BooleanToolType:
        """
        Getter for property: ( BooleanToolBuilder.BooleanToolType NXOpen.Geome) ToolOption
         Returns the boolean tool option   
            
         
        """
        pass
    @ToolOption.setter
    def ToolOption(self, toolOption: BooleanToolBuilder.BooleanToolType):
        """
        Setter for property: ( BooleanToolBuilder.BooleanToolType NXOpen.Geome) ToolOption
         Returns the boolean tool option   
            
         
        """
        pass
import NXOpen
class BoundaryDefinitionBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[BoundaryDefinitionBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: BoundaryDefinitionBuilder) -> None:
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
    def Erase(self, obj: BoundaryDefinitionBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: BoundaryDefinitionBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: BoundaryDefinitionBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> BoundaryDefinitionBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( BoundaryDefinitionBuilder NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[BoundaryDefinitionBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( BoundaryDefinitionBuilder List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: BoundaryDefinitionBuilder) -> None:
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
    def SetContents(self, objects: List[BoundaryDefinitionBuilder]) -> None:
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
    def Swap(self, object1: BoundaryDefinitionBuilder, object2: BoundaryDefinitionBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class BoundaryDefinitionBuilder(NXOpen.TaggedObject): 
    """ Represents a NXOpen.GeometricUtilities.BoundaryDefinitionBuilder.
        A boundary definition is a collection of ordered points which can be imagined to be
        connected by a polyline indicating a boundary. Any point in the collection can be 
        marked as a key point. Marking some points as key points helps to delete part of the 
        boundary efficiently. All the points in a boundary definition are co-planar. 
        A depth value can be specified to define a 3D boundary equivalent to an extrusion. """
    @property
    def Depth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Depth
         Returns the region depth   
            
         
        """
        pass
    def AppendPoint(self, point: NXOpen.Point3d, isKeyPoint: bool) -> None:
        """
         Appends a point to the boundary definition 
        """
        pass
    def Close(self) -> bool:
        """
         Closes the boundary by appending start point at the end of boundary definition 
         Returns isClosed (bool):  .
        """
        pass
    def DeleteAll(self) -> None:
        """
         Deletes all the points in the boundary definition 
        """
        pass
    def DeleteLastKeyPoint(self) -> None:
        """
         Deletes last key point and all the points from last key point up to and excluding its previous key point 
        """
        pass
    def GetPoints(self) -> List[NXOpen.Point3d]:
        """
         Queries all the boundary definition points 
         Returns points ( NXOpen.Point3d Li):  .
        """
        pass
    def SetPlaneNormal(self, direction: NXOpen.Vector3d) -> None:
        """
         Sets normal of the plane in which boundary is defined 
        """
        pass
    def Translate(self, vector: NXOpen.Vector3d) -> None:
        """
         Translates the boundary from its current position using the direction and the magnitude of a vector. 
        """
        pass
import NXOpen
class BoundingObjectBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[BoundingObjectBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: BoundingObjectBuilder) -> None:
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
    def Erase(self, obj: BoundingObjectBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: BoundingObjectBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: BoundingObjectBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> BoundingObjectBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( BoundingObjectBuilder NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[BoundingObjectBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( BoundingObjectBuilder List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: BoundingObjectBuilder) -> None:
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
    def SetContents(self, objects: List[BoundingObjectBuilder]) -> None:
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
    def Swap(self, object1: BoundingObjectBuilder, object2: BoundingObjectBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class BoundingObjectBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.GeometricUtilities.BoundingObjectBuilder
    """
    class Method(Enum):
        """
        Members Include: 
         |ExistingCurve|  Existing Curve 
         |ProjectPoint|  Project Point 
         |LineBy2Points|  Line by 2 Points 
         |PointAndVector|  Point and Vector 
         |ByPlane|  By Plane 

        """
        ExistingCurve: int
        ProjectPoint: int
        LineBy2Points: int
        PointAndVector: int
        ByPlane: int
        @staticmethod
        def ValueOf(value: int) -> BoundingObjectBuilder.Method:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BoundingCurve(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: ( NXOpen.SelectDisplayableObject) BoundingCurve
         Returns the existing bounding curve.  
           This is applicable for   NXOpen::GeometricUtilities::BoundingObjectBuilder::MethodExistingCurve    
         
        """
        pass
    @property
    def BoundingObjectMethod(self) -> BoundingObjectBuilder.Method:
        """
        Getter for property: ( BoundingObjectBuilder.Method NXOpen.Geome) BoundingObjectMethod
         Returns the bounding object method   
            
         
        """
        pass
    @BoundingObjectMethod.setter
    def BoundingObjectMethod(self, boundingObjectMethod: BoundingObjectBuilder.Method):
        """
        Setter for property: ( BoundingObjectBuilder.Method NXOpen.Geome) BoundingObjectMethod
         Returns the bounding object method   
            
         
        """
        pass
    @property
    def BoundingPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) BoundingPlane
         Returns the bounding plane.  
           This is applicable for   NXOpen::GeometricUtilities::BoundingObjectBuilder::MethodByPlane    
         
        """
        pass
    @BoundingPlane.setter
    def BoundingPlane(self, plane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) BoundingPlane
         Returns the bounding plane.  
           This is applicable for   NXOpen::GeometricUtilities::BoundingObjectBuilder::MethodByPlane    
         
        """
        pass
    @property
    def BoundingPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) BoundingPoint
         Returns the bounding point.  
           This is applicable for   NXOpen::GeometricUtilities::BoundingObjectBuilder::MethodPointAndVector    
         
        """
        pass
    @BoundingPoint.setter
    def BoundingPoint(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) BoundingPoint
         Returns the bounding point.  
           This is applicable for   NXOpen::GeometricUtilities::BoundingObjectBuilder::MethodPointAndVector    
         
        """
        pass
    @property
    def BoundingPoint1(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) BoundingPoint1
         Returns the bounding point1.  
           This represents first bounding point. This is applicable for   NXOpen::GeometricUtilities::BoundingObjectBuilder::MethodLineBy2Points    
         
        """
        pass
    @BoundingPoint1.setter
    def BoundingPoint1(self, point1: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) BoundingPoint1
         Returns the bounding point1.  
           This represents first bounding point. This is applicable for   NXOpen::GeometricUtilities::BoundingObjectBuilder::MethodLineBy2Points    
         
        """
        pass
    @property
    def BoundingPoint2(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) BoundingPoint2
         Returns the bounding point2.  
           This represents second bounding point. This is applicable for   NXOpen::GeometricUtilities::BoundingObjectBuilder::MethodLineBy2Points    
         
        """
        pass
    @BoundingPoint2.setter
    def BoundingPoint2(self, point2: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) BoundingPoint2
         Returns the bounding point2.  
           This represents second bounding point. This is applicable for   NXOpen::GeometricUtilities::BoundingObjectBuilder::MethodLineBy2Points    
         
        """
        pass
    @property
    def BoundingProjectPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) BoundingProjectPoint
         Returns the bounding project point.  
           This is applicable for   NXOpen::GeometricUtilities::BoundingObjectBuilder::MethodProjectPoint    
         
        """
        pass
    @BoundingProjectPoint.setter
    def BoundingProjectPoint(self, projectPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) BoundingProjectPoint
         Returns the bounding project point.  
           This is applicable for   NXOpen::GeometricUtilities::BoundingObjectBuilder::MethodProjectPoint    
         
        """
        pass
    @property
    def BoundingVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) BoundingVector
         Returns the bounding vector.  
           This is applicable for   NXOpen::GeometricUtilities::BoundingObjectBuilder::MethodPointAndVector    
         
        """
        pass
    @BoundingVector.setter
    def BoundingVector(self, vector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) BoundingVector
         Returns the bounding vector.  
           This is applicable for   NXOpen::GeometricUtilities::BoundingObjectBuilder::MethodPointAndVector    
         
        """
        pass
    @property
    def IntersectionReference(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) IntersectionReference
         Returns the intersection reference   
            
         
        """
        pass
    @IntersectionReference.setter
    def IntersectionReference(self, intersectionReference: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) IntersectionReference
         Returns the intersection reference   
            
         
        """
        pass
import NXOpen
class BridgeCurveConnectivity(NXOpen.TaggedObject): 
    """ Data offering connectivity controls for NXOpen.Features.BridgeCurveBuilderEx.
        Use NXOpen.GeometricUtilities.BridgeCurveConnectivity to define continuity level,
        position and tangency, curvature or flow at the end of a bridge curve. For more details see 
        the NX documentation for Bridge Curves.
    """
    class CurveDirectionOptions(Enum):
        """
        Members Include: 
         |Tangent|  Tangent to section 
         |Perpendicular|  Perpendicular to section using a reference face 

        """
        Tangent: int
        Perpendicular: int
        @staticmethod
        def ValueOf(value: int) -> BridgeCurveConnectivity.CurveDirectionOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FaceDirectionOptions(Enum):
        """
        Members Include: 
         |Sectional|  Sectional direction 
         |IsoU|  Along U iso-parameter 
         |IsoV|  Along V iso-parameter 

        """
        Sectional: int
        IsoU: int
        IsoV: int
        @staticmethod
        def ValueOf(value: int) -> BridgeCurveConnectivity.FaceDirectionOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CanReverseDirection(self) -> bool:
        """
        Getter for property: (bool) CanReverseDirection
         Returns the flag indicating if tangent direction is to be reversed   
            
         
        """
        pass
    @CanReverseDirection.setter
    def CanReverseDirection(self, reverseDirection: bool):
        """
        Setter for property: (bool) CanReverseDirection
         Returns the flag indicating if tangent direction is to be reversed   
            
         
        """
        pass
    @property
    def Continuity(self) -> Continuity:
        """
        Getter for property: ( Continuity NXOpen.Geome) Continuity
         Returns the continuity level   
            
         
        """
        pass
    @property
    def CurveDirectionOption(self) -> BridgeCurveConnectivity.CurveDirectionOptions:
        """
        Getter for property: ( BridgeCurveConnectivity.CurveDirectionOptions NXOpen.Geome) CurveDirectionOption
         Returns the curve direction option   
            
         
        """
        pass
    @CurveDirectionOption.setter
    def CurveDirectionOption(self, curveDirectionOption: BridgeCurveConnectivity.CurveDirectionOptions):
        """
        Setter for property: ( BridgeCurveConnectivity.CurveDirectionOptions NXOpen.Geome) CurveDirectionOption
         Returns the curve direction option   
            
         
        """
        pass
    @property
    def DirectionAtPoint(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) DirectionAtPoint
         Returns the direction at point   
            
         
        """
        pass
    @DirectionAtPoint.setter
    def DirectionAtPoint(self, direction: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) DirectionAtPoint
         Returns the direction at point   
            
         
        """
        pass
    @property
    def FaceDirectionOption(self) -> BridgeCurveConnectivity.FaceDirectionOptions:
        """
        Getter for property: ( BridgeCurveConnectivity.FaceDirectionOptions NXOpen.Geome) FaceDirectionOption
         Returns the face direction option   
            
         
        """
        pass
    @FaceDirectionOption.setter
    def FaceDirectionOption(self, faceDirectionOption: BridgeCurveConnectivity.FaceDirectionOptions):
        """
        Setter for property: ( BridgeCurveConnectivity.FaceDirectionOptions NXOpen.Geome) FaceDirectionOption
         Returns the face direction option   
            
         
        """
        pass
    @property
    def LocationOnSection(self) -> OnPathDimensionBuilder:
        """
        Getter for property: ( OnPathDimensionBuilder NXOpen.Geome) LocationOnSection
         Returns the location on section   
            
         
        """
        pass
    @property
    def PerpendicularFace(self) -> NXOpen.SelectFace:
        """
        Getter for property: ( NXOpen.SelectFace) PerpendicularFace
         Returns the perpendicular face   
            
         
        """
        pass
    @property
    def SectionAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SectionAngle
         Returns the section angle.  
           Positive U direction is used as reference to measure the angle in tangent plane.   
         
        """
        pass
    @property
    def UPercentage(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) UPercentage
         Returns the U coordinate percentage indicating location on the face where bridge curve is connected   
            
         
        """
        pass
    @property
    def VPercentage(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) VPercentage
         Returns the V coordinate percentage indicating location on the face where bridge curve is connected   
            
         
        """
        pass
    def EditUVPercentage(self, uPercent: float, vPercent: float) -> None:
        """
         Edits parameter percentage of a representative point on face 
        """
        pass
    def UpdateBasedOnLocationOnSection(self) -> None:
        """
         Updates the data based on NXOpen.GeometricUtilities.BridgeCurveConnectivity.LocationOnSection 
        """
        pass
    def UpdateOnDirectionAtPointReversal(self) -> None:
        """
         Updates the data based on  BridgeCurveConnectivity.DirectionAtPoint  sense 
        """
        pass
import NXOpen
class CAMDataPrepManager(NXOpen.Object): 
    """ Contains the create functions for builders. """
    def CreateMatchSurfaceBuilder(self) -> MatchSurfaceBuilder:
        """
         Creates a  NXOpen.GeometricUtilities.MatchSurfaceBuilder  
         Returns builder ( MatchSurfaceBuilder NXOpen.Geome): .
        """
        pass
    def CreateReduceSurfaceRadiusBuilder(self) -> ReduceSurfaceRadiusBuilder:
        """
         Creates a  NXOpen.GeometricUtilities.ReduceSurfaceRadiusBuilder  
         Returns builder ( ReduceSurfaceRadiusBuilder NXOpen.Geome): .
        """
        pass
    def CreateReduceSurfaceRadiusFaceGroupBuilder(self) -> ReduceSurfaceRadiusFaceGroupBuilder:
        """
         Creates a  NXOpen.GeometricUtilities.ReduceSurfaceRadiusFaceGroupBuilder  
         Returns builder ( ReduceSurfaceRadiusFaceGroupBuilder NXOpen.Geome): .
        """
        pass
    def CreateSnipIntoPatchesBuilder(self) -> SnipIntoPatchesBuilder:
        """
         Creates a  NXOpen.GeometricUtilities.SnipIntoPatchesBuilder  
         Returns builder ( SnipIntoPatchesBuilder NXOpen.Geome): .
        """
        pass
import NXOpen
class ChamferEdgeChainSetBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[ChamferEdgeChainSetBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: ChamferEdgeChainSetBuilder) -> None:
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
    def Erase(self, obj: ChamferEdgeChainSetBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: ChamferEdgeChainSetBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: ChamferEdgeChainSetBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> ChamferEdgeChainSetBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( ChamferEdgeChainSetBuilder NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[ChamferEdgeChainSetBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( ChamferEdgeChainSetBuilder List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: ChamferEdgeChainSetBuilder) -> None:
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
    def SetContents(self, objects: List[ChamferEdgeChainSetBuilder]) -> None:
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
    def Swap(self, object1: ChamferEdgeChainSetBuilder, object2: ChamferEdgeChainSetBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class ChamferEdgeChainSetBuilder(NXOpen.Builder): 
    """
    a class which defines the list item in ChamferEdgeManager
    """
    class CrossSectionType(Enum):
        """
        Members Include: 
         |Symmetric| 
         |Asymmetric| 
         |OffsetandAngle| 

        """
        Symmetric: int
        Asymmetric: int
        OffsetandAngle: int
        @staticmethod
        def ValueOf(value: int) -> ChamferEdgeChainSetBuilder.CrossSectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Angular(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Angular
         Returns the chamfer angle   
            
         
        """
        pass
    @property
    def CrossSectionOptions(self) -> ChamferEdgeChainSetBuilder.CrossSectionType:
        """
        Getter for property: ( ChamferEdgeChainSetBuilder.CrossSectionType NXOpen.Geome) CrossSectionOptions
         Returns the Chamfer cross section type   
            
         
        """
        pass
    @CrossSectionOptions.setter
    def CrossSectionOptions(self, crossSectionOptions: ChamferEdgeChainSetBuilder.CrossSectionType):
        """
        Setter for property: ( ChamferEdgeChainSetBuilder.CrossSectionType NXOpen.Geome) CrossSectionOptions
         Returns the Chamfer cross section type   
            
         
        """
        pass
    @property
    def Distance1(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Distance1
         Returns the first distance for symmetricasymmetric offset   
            
         
        """
        pass
    @property
    def Distance2(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Distance2
         Returns the second distance for asymmetric offset   
            
         
        """
        pass
    @property
    def Edges(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Edges
         Returns the edge collector of the edge set to do chamfer   
            
         
        """
        pass
    @Edges.setter
    def Edges(self, edges: NXOpen.ScCollector):
        """
        Setter for property: ( NXOpen.ScCollector) Edges
         Returns the edge collector of the edge set to do chamfer   
            
         
        """
        pass
    @property
    def ReverseDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseDirection
         Returns the offset reverse status   
            
         
        """
        pass
    @ReverseDirection.setter
    def ReverseDirection(self, reverseDirection: bool):
        """
        Setter for property: (bool) ReverseDirection
         Returns the offset reverse status   
            
         
        """
        pass
import NXOpen
class ChamferEdgeManager(NXOpen.TaggedObject): 
    """
     a class which defines edge manager for Apex Range Chamfer
    """
    @property
    def EdgeChainSetList(self) -> ChamferEdgeChainSetBuilderList:
        """
        Getter for property: ( ChamferEdgeChainSetBuilderList NXOpen.Geome) EdgeChainSetList
         Returns the list of edge chain set data to do chamfer  
            
         
        """
        pass
    def CreateChamferEdgeChainSetBuilder(self) -> ChamferEdgeChainSetBuilder:
        """
         Creates a Apex Range Chamfer Edge Chain Set builder
         Returns builder ( ChamferEdgeChainSetBuilder NXOpen.Geome): ChamferEdgeChainSetBuilder object .
        """
        pass
import NXOpen
class CircularCrossSection(NXOpen.TaggedObject): 
    """ Represents a circular section data for face blend. 
    """
    @property
    def LawControl(self) -> LawBuilder:
        """
        Getter for property: ( LawBuilder NXOpen.Geome) LawControl
         Returns the Law builder   
            
         
        """
        pass
    @property
    def Radius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Radius
         Returns the radius for the circular section with face blend
                  
            
         
        """
        pass
    @property
    def RadiusOption(self) -> RadiusMethod:
        """
        Getter for property: ( RadiusMethod NXOpen.Geome) RadiusOption
         Returns the radius option for the circular section with face blend
                  
            
         
        """
        pass
    @RadiusOption.setter
    def RadiusOption(self, method: RadiusMethod):
        """
        Setter for property: ( RadiusMethod NXOpen.Geome) RadiusOption
         Returns the radius option for the circular section with face blend
                  
            
         
        """
        pass
    def SetLawControlConstantRadius(self, radius: str) -> None:
        """
         Sets a constant radius for the law control of the circular section with face blend.
                
        """
        pass
    def SetLawControlEndRadius(self, radius: str) -> None:
        """
         Sets a end radius for the law control of the circular section with face blend.
                
        """
        pass
    def SetLawControlStartRadius(self, radius: str) -> None:
        """
         Sets a start radius for the law control of the circular section with face blend.
                
        """
        pass
    def SetRadius(self, radius: str) -> None:
        """
         Sets a radius for the circular section with face blend.
                
        """
        pass
class CircularFrameBuilder(ShapeFrameBuilder): 
    """
    Represents a NXOpen.GeometricUtilities.CircularFrameBuilder
    """
    class Subtypes(Enum):
        """
        Members Include: 
         |Arbitrary|  Arbitrary circle 
         |Half|  Half circle 
         |Quarter|  Quarter circle 
         |Full|  Full circle 

        """
        Arbitrary: int
        Half: int
        Quarter: int
        Full: int
        @staticmethod
        def ValueOf(value: int) -> CircularFrameBuilder.Subtypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Subtype(self) -> CircularFrameBuilder.Subtypes:
        """
        Getter for property: ( CircularFrameBuilder.Subtypes NXOpen.Geome) Subtype
         Returns the subtype   
            
         
        """
        pass
    @Subtype.setter
    def Subtype(self, subtype: CircularFrameBuilder.Subtypes):
        """
        Setter for property: ( CircularFrameBuilder.Subtypes NXOpen.Geome) Subtype
         Returns the subtype   
            
         
        """
        pass
    def GetAngle(self, index: int) -> float:
        """
         Gets the i-th angle of the circular frame 
         Returns angle (float):  angle .
        """
        pass
    def GetRadius(self, index: int) -> float:
        """
         Gets the i-th radius of the circular frame 
         Returns radius (float):  radius .
        """
        pass
    def SetAngle(self, index: int, angle: float) -> None:
        """
         Sets the i-th angle of the circular frame 
        """
        pass
    def SetRadius(self, index: int, radius: float) -> None:
        """
         Sets the i-th radius of the circular frame 
        """
        pass
import NXOpen
class CircularPattern(NXOpen.TaggedObject): 
    """ the circular pattern definition.  Allows specification along
        both the angular and radial directions. """
    class StaggerOptions(Enum):
        """
        Members Include: 
         |NotSet|  No stagger applied 
         |Row|  Stagger row 

        """
        NotSet: int
        Row: int
        @staticmethod
        def ValueOf(value: int) -> CircularPattern.StaggerOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngularSpacing(self) -> AngularPatternSpacing:
        """
        Getter for property: ( AngularPatternSpacing NXOpen.Geome) AngularSpacing
         Returns the angular spacing of the instances of the pattern  
            
         
        """
        pass
    @property
    def CenterPoint(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) CenterPoint
         Returns the center point object for 2D mode.  
           This function gets center point object of the 2D pattern   
         
        """
        pass
    @property
    def CreateLastStaggered(self) -> bool:
        """
        Getter for property: (bool) CreateLastStaggered
         Returns the option to generate the last item in a staggered row.  
            If 'true' the pattern will be
                    narrower on rows that have been staggered.   
         
        """
        pass
    @CreateLastStaggered.setter
    def CreateLastStaggered(self, create: bool):
        """
        Setter for property: (bool) CreateLastStaggered
         Returns the option to generate the last item in a staggered row.  
            If 'true' the pattern will be
                    narrower on rows that have been staggered.   
         
        """
        pass
    @property
    def Flip(self) -> bool:
        """
        Getter for property: (bool) Flip
         Returns the flip object for 2D mode.  
            This function gets the flip attribute of the 2D pattern.   
         
        """
        pass
    @Flip.setter
    def Flip(self, enabled: bool):
        """
        Setter for property: (bool) Flip
         Returns the flip object for 2D mode.  
            This function gets the flip attribute of the 2D pattern.   
         
        """
        pass
    @property
    def HorizontalRef(self) -> HorizontalReference:
        """
        Getter for property: ( HorizontalReference NXOpen.Geome) HorizontalRef
         Returns the horizontal reference   
            
         
        """
        pass
    @property
    def IncludeSeedToggle(self) -> bool:
        """
        Getter for property: (bool) IncludeSeedToggle
         Returns the IncludeSeed toggle attribute.  
           This function gets the IncludeSeed toggle value   
         
        """
        pass
    @IncludeSeedToggle.setter
    def IncludeSeedToggle(self, toggle: bool):
        """
        Setter for property: (bool) IncludeSeedToggle
         Returns the IncludeSeed toggle attribute.  
           This function gets the IncludeSeed toggle value   
         
        """
        pass
    @property
    def RadialSpacing(self) -> DistancePatternSpacing:
        """
        Getter for property: ( DistancePatternSpacing NXOpen.Geome) RadialSpacing
         Returns the radial spacing of the instances of the pattern   
            
         
        """
        pass
    @property
    def RotationAxis(self) -> NXOpen.Axis:
        """
        Getter for property: ( NXOpen.Axis) RotationAxis
         Returns the rotation axis for the pattern.  
             
         
        """
        pass
    @RotationAxis.setter
    def RotationAxis(self, rotationAxis: NXOpen.Axis):
        """
        Setter for property: ( NXOpen.Axis) RotationAxis
         Returns the rotation axis for the pattern.  
             
         
        """
        pass
    @property
    def RotationCenter(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) RotationCenter
         Returns the rotation center for the 2d pattern.  
             
         
        """
        pass
    @RotationCenter.setter
    def RotationCenter(self, rotationCenter: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) RotationCenter
         Returns the rotation center for the 2d pattern.  
             
         
        """
        pass
    @property
    def StaggerType(self) -> CircularPattern.StaggerOptions:
        """
        Getter for property: ( CircularPattern.StaggerOptions NXOpen.Geome) StaggerType
         Returns the type of stagger to be used by the pattern   
            
         
        """
        pass
    @StaggerType.setter
    def StaggerType(self, staggerType: CircularPattern.StaggerOptions):
        """
        Setter for property: ( CircularPattern.StaggerOptions NXOpen.Geome) StaggerType
         Returns the type of stagger to be used by the pattern   
            
         
        """
        pass
    @property
    def UseRadialDirectionToggle(self) -> bool:
        """
        Getter for property: (bool) UseRadialDirectionToggle
         Returns the UseRadialDirection toggle attribute.  
           This function gets the UseRadialDirection toggle value   
         
        """
        pass
    @UseRadialDirectionToggle.setter
    def UseRadialDirectionToggle(self, toggle: bool):
        """
        Setter for property: (bool) UseRadialDirectionToggle
         Returns the UseRadialDirection toggle attribute.  
           This function gets the UseRadialDirection toggle value   
         
        """
        pass
import NXOpen
class CollectorPairBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[CollectorPairBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: CollectorPairBuilder) -> None:
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
    def Erase(self, obj: CollectorPairBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: CollectorPairBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: CollectorPairBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> CollectorPairBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( CollectorPairBuilder NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[CollectorPairBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( CollectorPairBuilder List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: CollectorPairBuilder) -> None:
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
    def SetContents(self, objects: List[CollectorPairBuilder]) -> None:
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
    def Swap(self, object1: CollectorPairBuilder, object2: CollectorPairBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class CollectorPairBuilder(NXOpen.TaggedObject): 
    """
    Represents a Pair
    """
    @property
    def AutoPopulateSideTwoOption(self) -> bool:
        """
        Getter for property: (bool) AutoPopulateSideTwoOption
         Returns the auto populate side two faces option   
            
         
        """
        pass
    @AutoPopulateSideTwoOption.setter
    def AutoPopulateSideTwoOption(self, autoPopulateSideTwoOption: bool):
        """
        Setter for property: (bool) AutoPopulateSideTwoOption
         Returns the auto populate side two faces option   
            
         
        """
        pass
    @property
    def AutomaticPair(self) -> bool:
        """
        Getter for property: (bool) AutomaticPair
         Returns the auto populate side two faces option   
            
         
        """
        pass
    @AutomaticPair.setter
    def AutomaticPair(self, isAutomaticPair: bool):
        """
        Setter for property: (bool) AutomaticPair
         Returns the auto populate side two faces option   
            
         
        """
        pass
    @property
    def First(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) First
         Returns the side one faces for manual pair   
            
         
        """
        pass
    @property
    def OffsetOnlyOption(self) -> bool:
        """
        Getter for property: (bool) OffsetOnlyOption
         Returns the toggle used to determine neutral sheet creation mode   
            
         
        """
        pass
    @OffsetOnlyOption.setter
    def OffsetOnlyOption(self, offsetOnlyOption: bool):
        """
        Setter for property: (bool) OffsetOnlyOption
         Returns the toggle used to determine neutral sheet creation mode   
            
         
        """
        pass
    @property
    def SearchDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SearchDistance
         Returns the search distance to be used when searching for side 2 faces   
            
         
        """
        pass
    @property
    def Second(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Second
         Returns the side two faces for manual pair   
            
         
        """
        pass
    @property
    def TrimOption(self) -> bool:
        """
        Getter for property: (bool) TrimOption
         Returns the toggle used to determine whether or not to trim neutral sheets   
            
         
        """
        pass
    @TrimOption.setter
    def TrimOption(self, trimOption: bool):
        """
        Setter for property: (bool) TrimOption
         Returns the toggle used to determine whether or not to trim neutral sheets   
            
         
        """
        pass
    @property
    def UserDefinedMidSurfaceSelection(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) UserDefinedMidSurfaceSelection
         Returns the replacement sheet body, face or datum plane   
            
         
        """
        pass
    def Destroy(self) -> None:
        """
         Deletes a SI_collectorpair 
        """
        pass
    def PopulateSide2FacesFromSide1(self) -> None:
        """
         Search the side 2 faces from side 1 using the search distance and create or update side 2 faces collector 
        """
        pass
    def ReverseFacePair(self) -> None:
        """
         Button used to determine whether or not to swap face pairs 
        """
        pass
import NXOpen
class CollectorPairListBuilder(NXOpen.TaggedObject): 
    """ Represents a list of NXOpen.GeometricUtilities.CollectorPairBuilder objects. """
    @property
    def CollectorPairList(self) -> CollectorPairBuilderList:
        """
        Getter for property: ( CollectorPairBuilderList NXOpen.Geome) CollectorPairList
         Returns the list of pairs   
            
         
        """
        pass
    @property
    def ShowAutomaticPairs(self) -> bool:
        """
        Getter for property: (bool) ShowAutomaticPairs
         Returns the toggle used to show the automatically found face pairs from the solid to the list  
            
         
        """
        pass
    @ShowAutomaticPairs.setter
    def ShowAutomaticPairs(self, showAutomaticPairs: bool):
        """
        Setter for property: (bool) ShowAutomaticPairs
         Returns the toggle used to show the automatically found face pairs from the solid to the list  
            
         
        """
        pass
    def CreateCollectorPairBuilder(self) -> CollectorPairBuilder:
        """
         Creates one item of type NXOpen.GeometricUtilities.CollectorPairBuilder and append it to the list 
         Returns builder ( CollectorPairBuilder NXOpen.Geome): .
        """
        pass
import NXOpen
import NXOpen.Facet
class ColorCodedRegionBuilder(NXOpen.TaggedObject): 
    """ Represents a NXOpen.GeometricUtilities.ColorCodedRegionBuilder.
        The Color Coded Region block allows the user to select color coded regions of facet bodies ."""
    @property
    def AllSameColor(self) -> bool:
        """
        Getter for property: (bool) AllSameColor
         Returns the option to select all regions of the same color   
            
         
        """
        pass
    @AllSameColor.setter
    def AllSameColor(self, allSameColor: bool):
        """
        Setter for property: (bool) AllSameColor
         Returns the option to select all regions of the same color   
            
         
        """
        pass
    def BuildBodyColoredRegion(self, body: NXOpen.DisplayableObject, facetId: int, localVertexId: int) -> None:
        """
         Build Colored Region. Inputs to this command can be convergent objects. 
        """
        pass
    def BuildColoredRegion(self, facetBody: NXOpen.Facet.FacetedBody, facetId: int, localVertexId: int) -> None:
        """
         Build Colored Region. 
        """
        pass
    def DeselectColoredRegion(self, objIndex: int) -> None:
        """
         Deselect Colored Region 
        """
        pass
import NXOpen
class CombOptionsBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.GeometricUtilities.CombOptionsBuilder
    """
    class AnalysisTypes(Enum):
        """
        Members Include: 
         |NotSet|  None 
         |Curvature|  Curvature 
         |Radius|  Radius 

        """
        NotSet: int
        Curvature: int
        Radius: int
        @staticmethod
        def ValueOf(value: int) -> CombOptionsBuilder.AnalysisTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LabelTypes(Enum):
        """
        Members Include: 
         |NotSet|  None 
         |Minimum|  Minimum 
         |Maximum|  Maximum 
         |MinimumMaximum|  Minimum and Maximum 

        """
        NotSet: int
        Minimum: int
        Maximum: int
        MinimumMaximum: int
        @staticmethod
        def ValueOf(value: int) -> CombOptionsBuilder.LabelTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AnalysisType(self) -> CombOptionsBuilder.AnalysisTypes:
        """
        Getter for property: ( CombOptionsBuilder.AnalysisTypes NXOpen.Geome) AnalysisType
         Returns the analysis type   
            
         
        """
        pass
    @AnalysisType.setter
    def AnalysisType(self, analysis: CombOptionsBuilder.AnalysisTypes):
        """
        Setter for property: ( CombOptionsBuilder.AnalysisTypes NXOpen.Geome) AnalysisType
         Returns the analysis type   
            
         
        """
        pass
    @property
    def AutoScale(self) -> bool:
        """
        Getter for property: (bool) AutoScale
         Returns the auto scale flag   
            
         
        """
        pass
    @AutoScale.setter
    def AutoScale(self, hasAutoScale: bool):
        """
        Setter for property: (bool) AutoScale
         Returns the auto scale flag   
            
         
        """
        pass
    @property
    def Density(self) -> int:
        """
        Getter for property: (int) Density
         Returns the density   
            
         
        """
        pass
    @Density.setter
    def Density(self, density: int):
        """
        Setter for property: (int) Density
         Returns the density   
            
         
        """
        pass
    @property
    def HasMaxNeedleLength(self) -> bool:
        """
        Getter for property: (bool) HasMaxNeedleLength
         Returns the maximum needle flag   
            
         
        """
        pass
    @HasMaxNeedleLength.setter
    def HasMaxNeedleLength(self, hasMaxNeedleLength: bool):
        """
        Setter for property: (bool) HasMaxNeedleLength
         Returns the maximum needle flag   
            
         
        """
        pass
    @property
    def IntermediateDensity(self) -> int:
        """
        Getter for property: (int) IntermediateDensity
         Returns the intermediate density   
            
         
        """
        pass
    @IntermediateDensity.setter
    def IntermediateDensity(self, intermediateDensity: int):
        """
        Setter for property: (int) IntermediateDensity
         Returns the intermediate density   
            
         
        """
        pass
    @property
    def IsMaximumLabelEnabled(self) -> bool:
        """
        Getter for property: (bool) IsMaximumLabelEnabled
         Returns the value indicating if the maximum label is enabled   
            
         
        """
        pass
    @IsMaximumLabelEnabled.setter
    def IsMaximumLabelEnabled(self, isMaximumLabelEnabled: bool):
        """
        Setter for property: (bool) IsMaximumLabelEnabled
         Returns the value indicating if the maximum label is enabled   
            
         
        """
        pass
    @property
    def IsMinimumLabelEnabled(self) -> bool:
        """
        Getter for property: (bool) IsMinimumLabelEnabled
         Returns the value indicating if the minimum label is enabled   
            
         
        """
        pass
    @IsMinimumLabelEnabled.setter
    def IsMinimumLabelEnabled(self, isMinimumLabelEnabled: bool):
        """
        Setter for property: (bool) IsMinimumLabelEnabled
         Returns the value indicating if the minimum label is enabled   
            
         
        """
        pass
    @property
    def IsNormalToGridPlane(self) -> bool:
        """
        Getter for property: (bool) IsNormalToGridPlane
         Returns the normal to grid plane flag   
            
         
        """
        pass
    @IsNormalToGridPlane.setter
    def IsNormalToGridPlane(self, isNormalToGridPlane: bool):
        """
        Setter for property: (bool) IsNormalToGridPlane
         Returns the normal to grid plane flag   
            
         
        """
        pass
    @property
    def MaxNeedleLength(self) -> float:
        """
        Getter for property: (float) MaxNeedleLength
         Returns the maximum needle length   
            
         
        """
        pass
    @MaxNeedleLength.setter
    def MaxNeedleLength(self, maxNeedleLength: float):
        """
        Setter for property: (float) MaxNeedleLength
         Returns the maximum needle length   
            
         
        """
        pass
    @property
    def ReverseNeedles(self) -> bool:
        """
        Getter for property: (bool) ReverseNeedles
         Returns the reverse needles flag   
            
         
        """
        pass
    @ReverseNeedles.setter
    def ReverseNeedles(self, reverseNeedles: bool):
        """
        Setter for property: (bool) ReverseNeedles
         Returns the reverse needles flag   
            
         
        """
        pass
    @property
    def SampleDistance(self) -> float:
        """
        Getter for property: (float) SampleDistance
         Returns the sample distance   
            
         
        """
        pass
    @SampleDistance.setter
    def SampleDistance(self, sampleDistance: float):
        """
        Setter for property: (float) SampleDistance
         Returns the sample distance   
            
         
        """
        pass
    @property
    def ScaleFactor(self) -> float:
        """
        Getter for property: (float) ScaleFactor
         Returns the scale factor   
            
         
        """
        pass
    @ScaleFactor.setter
    def ScaleFactor(self, scaleFactor: float):
        """
        Setter for property: (float) ScaleFactor
         Returns the scale factor   
            
         
        """
        pass
    @property
    def ShowNeedles(self) -> bool:
        """
        Getter for property: (bool) ShowNeedles
         Returns the show needles flag   
            
         
        """
        pass
    @ShowNeedles.setter
    def ShowNeedles(self, showNeedles: bool):
        """
        Setter for property: (bool) ShowNeedles
         Returns the show needles flag   
            
         
        """
        pass
import NXOpen
class ConicCrossSection(NXOpen.TaggedObject): 
    """ Represents a conic section data for face blend. 
    """
    class DefineMethod(Enum):
        """
        Members Include: 
         |BoundaryPlusCenter|  conic shape controlled by boundary and center values 
         |BoundaryPlusRho|  conic shape controlled by boundary and rho values 
         |CenterPlusRho|  conic shape controlled by center and rho values 

        """
        BoundaryPlusCenter: int
        BoundaryPlusRho: int
        CenterPlusRho: int
        @staticmethod
        def ValueOf(value: int) -> ConicCrossSection.DefineMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DepthMethod(Enum):
        """
        Members Include: 
         |Constant|  Constant 
         |Law|  Control by law 

        """
        Constant: int
        Law: int
        @staticmethod
        def ValueOf(value: int) -> ConicCrossSection.DepthMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OffsetMethod(Enum):
        """
        Members Include: 
         |Constant|  Constant 
         |Law|  Control by law 

        """
        Constant: int
        Law: int
        @staticmethod
        def ValueOf(value: int) -> ConicCrossSection.OffsetMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RhoMethod(Enum):
        """
        Members Include: 
         |Constant|  Constant 
         |Law|  Control by law 
         |AutoEllipse|  Automatic Ellipse 

        """
        Constant: int
        Law: int
        AutoEllipse: int
        @staticmethod
        def ValueOf(value: int) -> ConicCrossSection.RhoMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ShapeSkewMethod(Enum):
        """
        Members Include: 
         |Constant|  Constant 
         |Law|  Control by law 

        """
        Constant: int
        Law: int
        @staticmethod
        def ValueOf(value: int) -> ConicCrossSection.ShapeSkewMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ConicMethod(self) -> ConicCrossSection.DefineMethod:
        """
        Getter for property: ( ConicCrossSection.DefineMethod NXOpen.Geome) ConicMethod
         Returns the conic method for the advanced symmetric conic section with face blend
                  
            
         
        """
        pass
    @ConicMethod.setter
    def ConicMethod(self, method: ConicCrossSection.DefineMethod):
        """
        Setter for property: ( ConicCrossSection.DefineMethod NXOpen.Geome) ConicMethod
         Returns the conic method for the advanced symmetric conic section with face blend
                  
            
         
        """
        pass
    @property
    def Depth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Depth
         Returns the depth expression for the conic section with face blend
                  
            
         
        """
        pass
    @property
    def DepthLawControl(self) -> LawBuilder:
        """
        Getter for property: ( LawBuilder NXOpen.Geome) DepthLawControl
         Returns the Depth Law builder   
            
         
        """
        pass
    @property
    def DepthOption(self) -> ConicCrossSection.DepthMethod:
        """
        Getter for property: ( ConicCrossSection.DepthMethod NXOpen.Geome) DepthOption
         Returns the depth option for the conic section with face blend
                  
            
         
        """
        pass
    @DepthOption.setter
    def DepthOption(self, method: ConicCrossSection.DepthMethod):
        """
        Setter for property: ( ConicCrossSection.DepthMethod NXOpen.Geome) DepthOption
         Returns the depth option for the conic section with face blend
                  
            
         
        """
        pass
    @property
    def FirstConstraintCurveCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FirstConstraintCurveCollector
         Returns the first constraint curve collector
                   
            
         
        """
        pass
    @FirstConstraintCurveCollector.setter
    def FirstConstraintCurveCollector(self, collector: NXOpen.ScCollector):
        """
        Setter for property: ( NXOpen.ScCollector) FirstConstraintCurveCollector
         Returns the first constraint curve collector
                   
            
         
        """
        pass
    @property
    def FirstLawControl(self) -> LawBuilder:
        """
        Getter for property: ( LawBuilder NXOpen.Geome) FirstLawControl
         Returns the First Offset Law builder   
            
         
        """
        pass
    @property
    def FirstOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FirstOffset
         Returns the first offset for the conic section with face blend
                  
            
         
        """
        pass
    @property
    def FirstOffsetOption(self) -> ConicCrossSection.OffsetMethod:
        """
        Getter for property: ( ConicCrossSection.OffsetMethod NXOpen.Geome) FirstOffsetOption
         Returns the first offset option for the conic section with face blend
                  
            
         
        """
        pass
    @FirstOffsetOption.setter
    def FirstOffsetOption(self, method: ConicCrossSection.OffsetMethod):
        """
        Setter for property: ( ConicCrossSection.OffsetMethod NXOpen.Geome) FirstOffsetOption
         Returns the first offset option for the conic section with face blend
                  
            
         
        """
        pass
    @property
    def OffsetSkewRatio(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OffsetSkewRatio
         Returns the offset skew ratio expression for the conic section with face blend
                  
            
         
        """
        pass
    @property
    def Rho(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Rho
         Returns the rho expression for the conic section with face blend
                  
            
         
        """
        pass
    @property
    def RhoLawControl(self) -> LawBuilder:
        """
        Getter for property: ( LawBuilder NXOpen.Geome) RhoLawControl
         Returns the Rho Law builder   
            
         
        """
        pass
    @property
    def RhoOption(self) -> ConicCrossSection.RhoMethod:
        """
        Getter for property: ( ConicCrossSection.RhoMethod NXOpen.Geome) RhoOption
         Returns the rho option for the conic section with face blend
                  
            
         
        """
        pass
    @RhoOption.setter
    def RhoOption(self, method: ConicCrossSection.RhoMethod):
        """
        Setter for property: ( ConicCrossSection.RhoMethod NXOpen.Geome) RhoOption
         Returns the rho option for the conic section with face blend
                  
            
         
        """
        pass
    @property
    def SecondConstraintCurveCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SecondConstraintCurveCollector
         Returns the second constraint curve collector
                   
            
         
        """
        pass
    @SecondConstraintCurveCollector.setter
    def SecondConstraintCurveCollector(self, collector: NXOpen.ScCollector):
        """
        Setter for property: ( NXOpen.ScCollector) SecondConstraintCurveCollector
         Returns the second constraint curve collector
                   
            
         
        """
        pass
    @property
    def SecondLawControl(self) -> LawBuilder:
        """
        Getter for property: ( LawBuilder NXOpen.Geome) SecondLawControl
         Returns the Second Offset Law builder   
            
         
        """
        pass
    @property
    def SecondOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SecondOffset
         Returns the second offset for the conic section with face blend
                  
            
         
        """
        pass
    @property
    def SecondOffsetOption(self) -> ConicCrossSection.OffsetMethod:
        """
        Getter for property: ( ConicCrossSection.OffsetMethod NXOpen.Geome) SecondOffsetOption
         Returns the second offset option for the conic section with face blend
                  
            
         
        """
        pass
    @SecondOffsetOption.setter
    def SecondOffsetOption(self, method: ConicCrossSection.OffsetMethod):
        """
        Setter for property: ( ConicCrossSection.OffsetMethod NXOpen.Geome) SecondOffsetOption
         Returns the second offset option for the conic section with face blend
                  
            
         
        """
        pass
    @property
    def ShapeSkew(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ShapeSkew
         Returns the shape skew expression for the conic section with face blend
                  
            
         
        """
        pass
    @property
    def ShapeSkewLawControl(self) -> LawBuilder:
        """
        Getter for property: ( LawBuilder NXOpen.Geome) ShapeSkewLawControl
         Returns the Shape Skew Law builder   
            
         
        """
        pass
    @property
    def ShapeSkewOption(self) -> ConicCrossSection.ShapeSkewMethod:
        """
        Getter for property: ( ConicCrossSection.ShapeSkewMethod NXOpen.Geome) ShapeSkewOption
         Returns the shape skew option for the conic section with face blend
                  
            
         
        """
        pass
    @ShapeSkewOption.setter
    def ShapeSkewOption(self, method: ConicCrossSection.ShapeSkewMethod):
        """
        Setter for property: ( ConicCrossSection.ShapeSkewMethod NXOpen.Geome) ShapeSkewOption
         Returns the shape skew option for the conic section with face blend
                  
            
         
        """
        pass
    @property
    def TransitionLinkFlag(self) -> bool:
        """
        Getter for property: (bool) TransitionLinkFlag
         Returns the flag to link multi-transition law types
                  
            
         
        """
        pass
    @TransitionLinkFlag.setter
    def TransitionLinkFlag(self, transition_link_flag: bool):
        """
        Setter for property: (bool) TransitionLinkFlag
         Returns the flag to link multi-transition law types
                  
            
         
        """
        pass
    def SetFirstOffset(self, offset: str) -> None:
        """
         Sets the first offset for the conic section with face blend.
                
        """
        pass
    def SetLawControlConstantDepth(self, radius: str) -> None:
        """
         Sets a constant radius for the depth law control of the conic section with face blend.
                
        """
        pass
    def SetLawControlConstantFirstOffset(self, radius: str) -> None:
        """
         Sets a constant radius for the first law control of the conic section with face blend.
                
        """
        pass
    def SetLawControlConstantRho(self, radius: str) -> None:
        """
         Sets a constant radius for the rho law control of the conic section with face blend.
                
        """
        pass
    def SetLawControlConstantSecondOffset(self, radius: str) -> None:
        """
         Sets a constant radius for the second law control of the conic section with face blend.
                
        """
        pass
    def SetLawControlConstantShapeSkew(self, radius: str) -> None:
        """
         Sets a constant radius for the shape skew law control of the conic section with face blend.
                
        """
        pass
    def SetLawControlDepthEndRadius(self, radius: str) -> None:
        """
         Sets a end radius for the depth law control of the conic section with face blend.
                
        """
        pass
    def SetLawControlDepthStartRadius(self, radius: str) -> None:
        """
         Sets a start radius for the depth law control of the conic section with face blend.
                
        """
        pass
    def SetLawControlFirstOffsetEndRadius(self, radius: str) -> None:
        """
         Sets a end radius for the first law control of the conic section with face blend.
                
        """
        pass
    def SetLawControlFirstOffsetStartRadius(self, radius: str) -> None:
        """
         Sets a start radius for the first law control of the conic section with face blend.
                
        """
        pass
    def SetLawControlRhoEndRadius(self, radius: str) -> None:
        """
         Sets a end radius for the rho law control of the conic section with face blend.
                
        """
        pass
    def SetLawControlRhoStartRadius(self, radius: str) -> None:
        """
         Sets a start radius for the rho law control of the conic section with face blend.
                
        """
        pass
    def SetLawControlSecondOffsetEndRadius(self, radius: str) -> None:
        """
         Sets a end radius for the second law control of the conic section with face blend.
                
        """
        pass
    def SetLawControlSecondOffsetStartRadius(self, radius: str) -> None:
        """
         Sets a start radius for the second law control of the conic section with face blend.
                
        """
        pass
    def SetLawControlShapeSkewEndRadius(self, radius: str) -> None:
        """
         Sets a end radius for the shape skew law control of the conic section with face blend.
                
        """
        pass
    def SetLawControlShapeSkewStartRadius(self, radius: str) -> None:
        """
         Sets a start radius for the shape skew law control of the conic section with face blend.
                
        """
        pass
    def SetRho(self, rho: str) -> None:
        """
         Sets a rho expression for the conic section with face blend.
                
        """
        pass
    def SetSecondOffset(self, offset: str) -> None:
        """
         Sets the second offset for the conic section with face blend.
                
        """
        pass
import NXOpen
class Continuity(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.GeometricUtilities.Continuity
    Allows user to specify continuity constraint surface construction.
    """
    class ContinuityTypes(Enum):
        """
        Members Include: 
         |G0|  G0 continuity 
         |G1|  G1 continuity 
         |G2|  G2 continuity 
         |G3|  G3 continuity
         |Free|  Free continuity 

        """
        G0: int
        G1: int
        G2: int
        G3: int
        Free: int
        @staticmethod
        def ValueOf(value: int) -> Continuity.ContinuityTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ConstraintFaces(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) ConstraintFaces
         Returns the constraint face collector.  
          
                  
         
        """
        pass
    @property
    def ContinuityType(self) -> Continuity.ContinuityTypes:
        """
        Getter for property: ( Continuity.ContinuityTypes NXOpen.Geome) ContinuityType
         Returns the continuity type.  
           If continuity = G0, then constraint face selector is disabled.
                  
         
        """
        pass
    @ContinuityType.setter
    def ContinuityType(self, continuityType: Continuity.ContinuityTypes):
        """
        Setter for property: ( Continuity.ContinuityTypes NXOpen.Geome) ContinuityType
         Returns the continuity type.  
           If continuity = G0, then constraint face selector is disabled.
                  
         
        """
        pass
    @property
    def IsFixed(self) -> bool:
        """
        Getter for property: (bool) IsFixed
         Returns the value indicating if a continuity constraint is of fixed type.  
          
                    This flag is valid for 
                     NXOpen::GeometricUtilities::Continuity::ContinuityTypesG1 ,
                     NXOpen::GeometricUtilities::Continuity::ContinuityTypesG2 ,
                     NXOpen::GeometricUtilities::Continuity::ContinuityTypesG3 
                    types only.   
         
        """
        pass
    @IsFixed.setter
    def IsFixed(self, isFixed: bool):
        """
        Setter for property: (bool) IsFixed
         Returns the value indicating if a continuity constraint is of fixed type.  
          
                    This flag is valid for 
                     NXOpen::GeometricUtilities::Continuity::ContinuityTypesG1 ,
                     NXOpen::GeometricUtilities::Continuity::ContinuityTypesG2 ,
                     NXOpen::GeometricUtilities::Continuity::ContinuityTypesG3 
                    types only.   
         
        """
        pass
import NXOpen
class ControlPoleManagerData(NXOpen.TaggedObject): 
    """
       This class manages the control poles for a set of surfaces or curves.
    """
    def CreatePolesGroup(self) -> int:
        """
         Creates a new poles group 
         Returns groupIndex (int):  New group index for newly created poles group. .
        """
        pass
    def DeletePolesGroup(self, groupIndex: int) -> None:
        """
         Deletes a group of poles 
        """
        pass
    def DeselectPoles(self, groupIndex: int, polesIndex: List[int], poles: List[NXOpen.Point]) -> None:
        """
         Removes selected pole 
        """
        pass
    def GetIsUPeriodic(self, groupIndex: int) -> bool:
        """
         Queries periodicity in U direction of a group of poles 
         Returns uPeriodicity (bool):  U Periodicity .
        """
        pass
    def GetIsVPeriodic(self, groupIndex: int) -> bool:
        """
         Queries periodicity in V direction of a group of poles 
         Returns vPeriodicity (bool):  V Periodicity .
        """
        pass
    def GetPoles(self, groupIndex: int) -> Tuple[List[int], List[NXOpen.Point]]:
        """
         Gets poles of an entity 
         Returns A tuple consisting of (polesIndex, poles). 
         - polesIndex is: List[int]. Poles index .
         - poles is:  NXOpen.Point Li. Poles .

        """
        pass
    def GetSelectedPoles(self, groupIndex: int) -> Tuple[List[int], List[NXOpen.Point]]:
        """
         Gets selected poles 
         Returns A tuple consisting of (polesIndex, poles). 
         - polesIndex is: List[int]. Poles index .
         - poles is:  NXOpen.Point Li. Poles .

        """
        pass
    def GetUDimension(self, groupIndex: int) -> int:
        """
         Queries dimension in U direction of a group of poles 
         Returns uDimension (int):  U Dimension .
        """
        pass
    def GetVDimension(self, groupIndex: int) -> int:
        """
         Queries dimension in V direction of a group of poles 
         Returns vDimension (int):  V Dimension .
        """
        pass
    def SelectPoles(self, groupIndex: int, polesIndex: List[int], poles: List[NXOpen.Point]) -> None:
        """
         Adds new selected pole 
        """
        pass
    def SetIsUPeriodic(self, groupIndex: int, uPeriodicity: bool) -> None:
        """
         Sets periodicity in U direction of a group of poles 
        """
        pass
    def SetIsVPeriodic(self, groupIndex: int, vPeriodicity: bool) -> None:
        """
         Sets periodicity in V direction of a group of poles 
        """
        pass
    @overload
    def SetPoleGroupEntity(self, groupIndex: int, face: NXOpen.Face) -> None:
        """
         Sets face to control poles group 
        """
        pass
    @overload
    def SetPoleGroupEntity(self, groupIndex: int, curve: NXOpen.Curve) -> None:
        """
         Sets curve to control poles group 
        """
        pass
    def SetPoles(self, groupIndex: int, polesIndex: List[int], poles: List[NXOpen.Point]) -> None:
        """
         Sets new group poles 
        """
        pass
    def SetUDimension(self, groupIndex: int, uDimension: int) -> None:
        """
         Sets dimension in U direction of a group of poles 
        """
        pass
    def SetVDimension(self, groupIndex: int, vDimension: int) -> None:
        """
         Sets dimension in V direction of a group of poles 
        """
        pass
    def UpdatePolePositions(self, groupIndex: int, poleIndex: List[int], newPosition: List[NXOpen.Point3d]) -> None:
        """
         Updates pole positions 
        """
        pass
import NXOpen
import NXOpen.Features
class ConvertFeatureGroupsToModulesBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.GeometricUtilities.ConvertFeatureGroupsToModulesBuilder builder """
    def AddAll(self) -> None:
        """
         Add all feature groups into convertible set 
        """
        pass
    def AddFeatureGroupIntoConvertibleSet(self, featureGroups: List[NXOpen.Features.FeatureGroup]) -> None:
        """
         Add feature group into convertible set 
        """
        pass
    def RemoveAll(self) -> None:
        """
         Remove all feature groups from convertible set 
        """
        pass
    def RemoveFeatureGroupFromConvertibleSet(self, featureGroups: List[NXOpen.Features.FeatureGroup]) -> None:
        """
         Remove feature group from convertible set 
        """
        pass
import NXOpen
import NXOpen.Display
class CrayonSelectionData(NXOpen.TaggedObject): 
    """ Represents a NXOpen.GeometricUtilities.CrayonSelectionData.
        A crayon is a trail of cursor in view plane selecting the entities underneath. """
    class EntityData:
        """
         Structure representing selected entity data. 
         CrayonSelectionDataEntityData_Struct NXOpen.Geome is an alias for  CrayonSelectionData.EntityData NXOpen.Geome.
        """
        @property
        def Entity(self) -> NXOpen.NXObject:
            """
            Getter for property Entity
            Entity in root part

            """
            pass
        @Entity.setter
        def Entity(self, value: NXOpen.NXObject):
            """
            Getter for property Entity
            Entity in root part
            Setter for property Entity
            Entity in root part

            """
            pass
        @property
        def PickPoint(self) -> NXOpen.Point3d:
            """
            Getter for property PickPoint
            Pick point on entity in root part

            """
            pass
        @PickPoint.setter
        def PickPoint(self, value: NXOpen.Point3d):
            """
            Getter for property PickPoint
            Pick point on entity in root part
            Setter for property PickPoint
            Pick point on entity in root part

            """
            pass
        @property
        def View(self) -> NXOpen.Display.NXOpen.View:
            """
            Getter for property View
            Selection view

            """
            pass
        @View.setter
        def View(self, value: NXOpen.Display.NXOpen.View):
            """
            Getter for property View
            Selection view
            Setter for property View
            Selection view

            """
            pass
    def Clear(self) -> None:
        """
         Clears all the selected entities 
        """
        pass
    def GetEntities(self) -> List[CrayonSelectionData.EntityData]:
        """
         Queries all the selected entities. Note that the returned array may contain repeated entries for
                    an entity as user may have selected it multiple times using crayon dragging. 
         Returns entities ( CrayonSelectionData.EntityData List[NXOpen.Geo):  .
        """
        pass
    def SelectEntities(self, entities: List[CrayonSelectionData.EntityData]) -> None:
        """
         Selects an array of entities and appends to currently selected entities. 
        """
        pass
    def SelectEntity(self, entity: CrayonSelectionData.EntityData) -> None:
        """
         Selects an entity and appends to currently selected array of entities. 
        """
        pass
import NXOpen
class CurveAlignedItemBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[CurveAlignedItemBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: CurveAlignedItemBuilder) -> None:
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
    def Erase(self, obj: CurveAlignedItemBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: CurveAlignedItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: CurveAlignedItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> CurveAlignedItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( CurveAlignedItemBuilder NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[CurveAlignedItemBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( CurveAlignedItemBuilder List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: CurveAlignedItemBuilder) -> None:
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
    def SetContents(self, objects: List[CurveAlignedItemBuilder]) -> None:
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
    def Swap(self, object1: CurveAlignedItemBuilder, object2: CurveAlignedItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class CurveAlignedItemBuilder(NXOpen.Builder): 
    """ Represents a single item in the Curve Aligned List. """
    class CurveControlTypes(Enum):
        """
        Members Include: 
         |U| 
         |V| 

        """
        U: int
        V: int
        @staticmethod
        def ValueOf(value: int) -> CurveAlignedItemBuilder.CurveControlTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CurveAlignedSelection(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) CurveAlignedSelection
         Returns   the sc section which contains curves.  
            
           
         
        """
        pass
    @property
    def CurveControl(self) -> CurveAlignedItemBuilder.CurveControlTypes:
        """
        Getter for property: ( CurveAlignedItemBuilder.CurveControlTypes NXOpen.Geome) CurveControl
         Returns   the curve controls  
          
          
           
         
        """
        pass
    @CurveControl.setter
    def CurveControl(self, curveControls: CurveAlignedItemBuilder.CurveControlTypes):
        """
        Setter for property: ( CurveAlignedItemBuilder.CurveControlTypes NXOpen.Geome) CurveControl
         Returns   the curve controls  
          
          
           
         
        """
        pass
import NXOpen
class CurveAlignedListBuilder(NXOpen.TaggedObject): 
    """ the builder for a list of GeometricUtilities.CurveAlignedItemBuilder objects """
    @property
    def List(self) -> CurveAlignedItemBuilderList:
        """
        Getter for property: ( CurveAlignedItemBuilderList NXOpen.Geome) List
         Returns a list of  GeometricUtilities::CurveAlignedItemBuilder  objects   
            
         
        """
        pass
    def CreateCurveAlignedItemBuilder(self) -> CurveAlignedItemBuilder:
        """
         Creates a GeometricUtilities.CurveAlignedItemBuilder 
         Returns builder ( CurveAlignedItemBuilder NXOpen.Geome): .
        """
        pass
import NXOpen
class CurveExtendData(NXOpen.TaggedObject): 
    """ Represents a NXOpen.GeometricUtilities.CurveExtendData """
    class LimitOptions(Enum):
        """
        Members Include: 
         |Value|  Value 
         |AtPoint|  At Point 
         |UntilSelected|  Until Selected 

        """
        Value: int
        AtPoint: int
        UntilSelected: int
        @staticmethod
        def ValueOf(value: int) -> CurveExtendData.LimitOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Distance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Distance
         Returns the distance   
            
         
        """
        pass
    @property
    def LimitOption(self) -> CurveExtendData.LimitOptions:
        """
        Getter for property: ( CurveExtendData.LimitOptions NXOpen.Geome) LimitOption
         Returns the limit option   
            
         
        """
        pass
    @LimitOption.setter
    def LimitOption(self, limitOption: CurveExtendData.LimitOptions):
        """
        Setter for property: ( CurveExtendData.LimitOptions NXOpen.Geome) LimitOption
         Returns the limit option   
            
         
        """
        pass
    @property
    def UntilSelectedObject(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: ( NXOpen.SelectDisplayableObject) UntilSelectedObject
         Returns the until selected object   
            
         
        """
        pass
import NXOpen
class CurveExtensionBuilder(NXOpen.TaggedObject): 
    """ Spline extension builder class. This class allows natural extension or trimming of a b-spline cuve. """
    class ExtensionOption(Enum):
        """
        Members Include: 
         |NotSet|  No extension 
         |ByValue|  Extend by value 
         |ByPoint|  Extend up to a point 

        """
        NotSet: int
        ByValue: int
        ByPoint: int
        @staticmethod
        def ValueOf(value: int) -> CurveExtensionBuilder.ExtensionOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EndExtensionOption(self) -> CurveExtensionBuilder.ExtensionOption:
        """
        Getter for property: ( CurveExtensionBuilder.ExtensionOption NXOpen.Geome) EndExtensionOption
         Returns the extension options   
            
         
        """
        pass
    @EndExtensionOption.setter
    def EndExtensionOption(self, extensionOption: CurveExtensionBuilder.ExtensionOption):
        """
        Setter for property: ( CurveExtensionBuilder.ExtensionOption NXOpen.Geome) EndExtensionOption
         Returns the extension options   
            
         
        """
        pass
    @property
    def EndPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) EndPoint
         Returns the point up to which end is extended   
            
         
        """
        pass
    @EndPoint.setter
    def EndPoint(self, endPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) EndPoint
         Returns the point up to which end is extended   
            
         
        """
        pass
    @property
    def EndValue(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndValue
         Returns the end value   
            
         
        """
        pass
    @property
    def IsSymmetric(self) -> bool:
        """
        Getter for property: (bool) IsSymmetric
         Returns the flag indicating if extension is symmetry.  
           Symmetric extension follows start extension values   
         
        """
        pass
    @IsSymmetric.setter
    def IsSymmetric(self, isSymmetric: bool):
        """
        Setter for property: (bool) IsSymmetric
         Returns the flag indicating if extension is symmetry.  
           Symmetric extension follows start extension values   
         
        """
        pass
    @property
    def StartExtensionOption(self) -> CurveExtensionBuilder.ExtensionOption:
        """
        Getter for property: ( CurveExtensionBuilder.ExtensionOption NXOpen.Geome) StartExtensionOption
         Returns the extension options   
            
         
        """
        pass
    @StartExtensionOption.setter
    def StartExtensionOption(self, extensionOption: CurveExtensionBuilder.ExtensionOption):
        """
        Setter for property: ( CurveExtensionBuilder.ExtensionOption NXOpen.Geome) StartExtensionOption
         Returns the extension options   
            
         
        """
        pass
    @property
    def StartPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) StartPoint
         Returns the point up to which start is extended   
            
         
        """
        pass
    @StartPoint.setter
    def StartPoint(self, startPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) StartPoint
         Returns the point up to which start is extended   
            
         
        """
        pass
    @property
    def StartValue(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartValue
         Returns the start value   
            
         
        """
        pass
import NXOpen
class CurveFitData(NXOpen.TaggedObject): 
    """ Represents the curve fitting methods options.
    """
    class Join(Enum):
        """
        Members Include: 
         |No|  No 
         |Cubic|  Cubic 
         |General|  General 
         |Quintic|  Quintic 

        """
        No: int
        Cubic: int
        General: int
        Quintic: int
        @staticmethod
        def ValueOf(value: int) -> CurveFitData.Join:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Method(Enum):
        """
        Members Include: 
         |DegreeAndSegments|  Degree and Segments 
         |DegreeAndTolerance|  Degree and Tolerance 
         |KeepParameterization|  Keep Parameterization 
         |AutoFit|  Auto Fit 

        """
        DegreeAndSegments: int
        DegreeAndTolerance: int
        KeepParameterization: int
        AutoFit: int
        @staticmethod
        def ValueOf(value: int) -> CurveFitData.Method:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngleTolerance(self) -> float:
        """
        Getter for property: (float) AngleTolerance
         Returns the angle tolerance   
            
         
        """
        pass
    @AngleTolerance.setter
    def AngleTolerance(self, angleTolerance: float):
        """
        Setter for property: (float) AngleTolerance
         Returns the angle tolerance   
            
         
        """
        pass
    @property
    def CurveJoinMethod(self) -> CurveFitData.Join:
        """
        Getter for property: ( CurveFitData.Join NXOpen.Geome) CurveJoinMethod
         Returns the curve join method   
            
         
        """
        pass
    @CurveJoinMethod.setter
    def CurveJoinMethod(self, curveJoinMethod: CurveFitData.Join):
        """
        Setter for property: ( CurveFitData.Join NXOpen.Geome) CurveJoinMethod
         Returns the curve join method   
            
         
        """
        pass
    @property
    def Degree(self) -> int:
        """
        Getter for property: (int) Degree
         Returns the fitting degree   
            
         
        """
        pass
    @Degree.setter
    def Degree(self, degree: int):
        """
        Setter for property: (int) Degree
         Returns the fitting degree   
            
         
        """
        pass
    @property
    def FitMethod(self) -> CurveFitData.Method:
        """
        Getter for property: ( CurveFitData.Method NXOpen.Geome) FitMethod
         Returns the fitting method   
            
         
        """
        pass
    @FitMethod.setter
    def FitMethod(self, fitMethod: CurveFitData.Method):
        """
        Setter for property: ( CurveFitData.Method NXOpen.Geome) FitMethod
         Returns the fitting method   
            
         
        """
        pass
    @property
    def IsAdvancedFit(self) -> bool:
        """
        Getter for property: (bool) IsAdvancedFit
         Returns the advanced fitting option   
            
         
        """
        pass
    @IsAdvancedFit.setter
    def IsAdvancedFit(self, isAdvancedFit: bool):
        """
        Setter for property: (bool) IsAdvancedFit
         Returns the advanced fitting option   
            
         
        """
        pass
    @property
    def IsAlignShape(self) -> bool:
        """
        Getter for property: (bool) IsAlignShape
         Returns the align shape option   
            
         
        """
        pass
    @IsAlignShape.setter
    def IsAlignShape(self, isAlignShape: bool):
        """
        Setter for property: (bool) IsAlignShape
         Returns the align shape option   
            
         
        """
        pass
    @property
    def MaximumDegree(self) -> int:
        """
        Getter for property: (int) MaximumDegree
         Returns the maximum degree   
            
         
        """
        pass
    @MaximumDegree.setter
    def MaximumDegree(self, maximumDegree: int):
        """
        Setter for property: (int) MaximumDegree
         Returns the maximum degree   
            
         
        """
        pass
    @property
    def MaximumSegments(self) -> int:
        """
        Getter for property: (int) MaximumSegments
         Returns the maximum segments   
            
         
        """
        pass
    @MaximumSegments.setter
    def MaximumSegments(self, maximumSegments: int):
        """
        Setter for property: (int) MaximumSegments
         Returns the maximum segments   
            
         
        """
        pass
    @property
    def MinimumDegree(self) -> int:
        """
        Getter for property: (int) MinimumDegree
         Returns the minimum degree   
            
         
        """
        pass
    @MinimumDegree.setter
    def MinimumDegree(self, minimumDegree: int):
        """
        Setter for property: (int) MinimumDegree
         Returns the minimum degree   
            
         
        """
        pass
    @property
    def Segments(self) -> int:
        """
        Getter for property: (int) Segments
         Returns the fitting segments   
            
         
        """
        pass
    @Segments.setter
    def Segments(self, segments: int):
        """
        Setter for property: (int) Segments
         Returns the fitting segments   
            
         
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
import NXOpen
class CurveFitJoin(NXOpen.TaggedObject): 
    """ Represents the curve fit join data 
    """
    class JoinMethod(Enum):
        """
        Members Include: 
         |No|  No 
         |Cubic|  Cubic 
         |Genernal|  General 
         |Quintic|  Quintic 

        """
        No: int
        Cubic: int
        Genernal: int
        Quintic: int
        @staticmethod
        def ValueOf(value: int) -> CurveFitJoin.JoinMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CurveFitOptions(self) -> CurveFitOptions:
        """
        Getter for property: ( CurveFitOptions NXOpen.Geome) CurveFitOptions
         Returns the curve fit options   
            
         
        """
        pass
    @property
    def CurveJoinMethod(self) -> CurveFitJoin.JoinMethod:
        """
        Getter for property: ( CurveFitJoin.JoinMethod NXOpen.Geome) CurveJoinMethod
         Returns the curve join method 
                 
            
         
        """
        pass
    @CurveJoinMethod.setter
    def CurveJoinMethod(self, curveJoinMethod: CurveFitJoin.JoinMethod):
        """
        Setter for property: ( CurveFitJoin.JoinMethod NXOpen.Geome) CurveJoinMethod
         Returns the curve join method 
                 
            
         
        """
        pass
import NXOpen
class CurveFitOptions(NXOpen.TaggedObject): 
    """ Represents the curve fit data 
    """
    class FitMethod(Enum):
        """
        Members Include: 
         |Cubic|  Cubic 
         |Quintic|  Quintic 
         |Advanced|  Advanced 

        """
        Cubic: int
        Quintic: int
        Advanced: int
        @staticmethod
        def ValueOf(value: int) -> CurveFitOptions.FitMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FitOption(self) -> CurveFitOptions.FitMethod:
        """
        Getter for property: ( CurveFitOptions.FitMethod NXOpen.Geome) FitOption
         Returns the curve fit method    
            
         
        """
        pass
    @FitOption.setter
    def FitOption(self, curveFitMethod: CurveFitOptions.FitMethod):
        """
        Setter for property: ( CurveFitOptions.FitMethod NXOpen.Geome) FitOption
         Returns the curve fit method    
            
         
        """
        pass
    @property
    def MaximumDegree(self) -> int:
        """
        Getter for property: (int) MaximumDegree
         Returns the maximum degree method 
                 
            
         
        """
        pass
    @MaximumDegree.setter
    def MaximumDegree(self, maximum_degree: int):
        """
        Setter for property: (int) MaximumDegree
         Returns the maximum degree method 
                 
            
         
        """
        pass
    @property
    def MaximumSegments(self) -> int:
        """
        Getter for property: (int) MaximumSegments
         Returns the maximum segments method 
                 
            
         
        """
        pass
    @MaximumSegments.setter
    def MaximumSegments(self, maximum_segments: int):
        """
        Setter for property: (int) MaximumSegments
         Returns the maximum segments method 
                 
            
         
        """
        pass
import NXOpen
class CurveLengthBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.GeometricUtilities.CurveLengthBuilder builder
    """
    class EndObjectType(Enum):
        """
        Members Include: 
         |Value| 
         |FromSelected| 

        """
        Value: int
        FromSelected: int
        @staticmethod
        def ValueOf(value: int) -> CurveLengthBuilder.EndObjectType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EndOffset0(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndOffset0
         Returns the end 1 length   
            
         
        """
        pass
    @property
    def EndOffset1(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndOffset1
         Returns the end 2 length   
            
         
        """
        pass
    @property
    def EndSelection0(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) EndSelection0
         Returns the select object for end 1   
            
         
        """
        pass
    @property
    def EndSelection1(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) EndSelection1
         Returnsthe select object for end 2  
            
         
        """
        pass
    @property
    def EndType0(self) -> CurveLengthBuilder.EndObjectType:
        """
        Getter for property: ( CurveLengthBuilder.EndObjectType NXOpen.Geome) EndType0
         Returns the end 1 type   
            
         
        """
        pass
    @EndType0.setter
    def EndType0(self, endType0: CurveLengthBuilder.EndObjectType):
        """
        Setter for property: ( CurveLengthBuilder.EndObjectType NXOpen.Geome) EndType0
         Returns the end 1 type   
            
         
        """
        pass
    @property
    def EndType1(self) -> CurveLengthBuilder.EndObjectType:
        """
        Getter for property: ( CurveLengthBuilder.EndObjectType NXOpen.Geome) EndType1
         Returns the end 2 type   
            
         
        """
        pass
    @EndType1.setter
    def EndType1(self, endType1: CurveLengthBuilder.EndObjectType):
        """
        Setter for property: ( CurveLengthBuilder.EndObjectType NXOpen.Geome) EndType1
         Returns the end 2 type   
            
         
        """
        pass
    @property
    def ReverseEndOffset0Direction(self) -> bool:
        """
        Getter for property: (bool) ReverseEndOffset0Direction
         Returns the reverse endOffset0 direction flag.  
           Indicates whether the endOffset0 direction has been flipped from its initial inferred direction   
         
        """
        pass
    @ReverseEndOffset0Direction.setter
    def ReverseEndOffset0Direction(self, reverseEndOffset0Direction: bool):
        """
        Setter for property: (bool) ReverseEndOffset0Direction
         Returns the reverse endOffset0 direction flag.  
           Indicates whether the endOffset0 direction has been flipped from its initial inferred direction   
         
        """
        pass
    @property
    def ReverseEndOffset1Direction(self) -> bool:
        """
        Getter for property: (bool) ReverseEndOffset1Direction
         Returns the reverse endOffset1 direction flag.  
           Indicates whether the endOffset1 direction has been flipped from its initial inferred direction   
         
        """
        pass
    @ReverseEndOffset1Direction.setter
    def ReverseEndOffset1Direction(self, reverseEndOffset1Direction: bool):
        """
        Setter for property: (bool) ReverseEndOffset1Direction
         Returns the reverse endOffset1 direction flag.  
           Indicates whether the endOffset1 direction has been flipped from its initial inferred direction   
         
        """
        pass
    @property
    def ReverseGuideCurveLoopDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseGuideCurveLoopDirection
         Returns the reverse guide curve direction flag.  
           Indicates whether the guide curve loop direction has been flipped from its initial inferred direction   
         
        """
        pass
    @ReverseGuideCurveLoopDirection.setter
    def ReverseGuideCurveLoopDirection(self, reverseGuideCurveLoopDirection: bool):
        """
        Setter for property: (bool) ReverseGuideCurveLoopDirection
         Returns the reverse guide curve direction flag.  
           Indicates whether the guide curve loop direction has been flipped from its initial inferred direction   
         
        """
        pass
import NXOpen
class CurveLengthData(NXOpen.TaggedObject): 
    """ Represents an CurveLength data. 
    """
    @property
    def EndDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndDistance
         Returns the end distance 
                  
            
         
        """
        pass
    @property
    def ExtensionDirection(self) -> ExtensionDirection:
        """
        Getter for property: ( ExtensionDirection NXOpen.Geome) ExtensionDirection
         Returns the extension direction
                 
            
         
        """
        pass
    @ExtensionDirection.setter
    def ExtensionDirection(self, extension_direction: ExtensionDirection):
        """
        Setter for property: ( ExtensionDirection NXOpen.Geome) ExtensionDirection
         Returns the extension direction
                 
            
         
        """
        pass
    @property
    def ExtensionMethod(self) -> ExtensionMethod:
        """
        Getter for property: ( ExtensionMethod NXOpen.Geome) ExtensionMethod
         Returns the total or incremental extension method 
                  
            
         
        """
        pass
    @ExtensionMethod.setter
    def ExtensionMethod(self, extension_method: ExtensionMethod):
        """
        Setter for property: ( ExtensionMethod NXOpen.Geome) ExtensionMethod
         Returns the total or incremental extension method 
                  
            
         
        """
        pass
    @property
    def ExtensionSide(self) -> ExtensionSide:
        """
        Getter for property: ( ExtensionSide NXOpen.Geome) ExtensionSide
         Returns the extension side option 
                 
            
         
        """
        pass
    @ExtensionSide.setter
    def ExtensionSide(self, extension_side: ExtensionSide):
        """
        Setter for property: ( ExtensionSide NXOpen.Geome) ExtensionSide
         Returns the extension side option 
                 
            
         
        """
        pass
    @property
    def StartDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartDistance
         Returns the start distance 
                  
            
         
        """
        pass
    @property
    def TotalLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TotalLength
         Returns the total length
                  
            
         
        """
        pass
    def SetEndDistance(self, end_distance: str) -> None:
        """
         Set end distance 
                
        """
        pass
    def SetStartDistance(self, start_distance: str) -> None:
        """
         Set start distance 
                
        """
        pass
    def SetTotalLength(self, total_length: str) -> None:
        """
         Set total length
                
        """
        pass
import NXOpen
class CurveLimitsData(NXOpen.TaggedObject): 
    """ Represents a NXOpen.GeometricUtilities.CurveLimitsData """
    @property
    def EndLimit(self) -> CurveExtendData:
        """
        Getter for property: ( CurveExtendData NXOpen.Geome) EndLimit
         Returns the end limit   
            
         
        """
        pass
    @property
    def FullCircle(self) -> bool:
        """
        Getter for property: (bool) FullCircle
         Returns the full circle   
            
         
        """
        pass
    @FullCircle.setter
    def FullCircle(self, fullCircle: bool):
        """
        Setter for property: (bool) FullCircle
         Returns the full circle   
            
         
        """
        pass
    @property
    def StartLimit(self) -> CurveExtendData:
        """
        Getter for property: ( CurveExtendData NXOpen.Geome) StartLimit
         Returns the start limit   
            
         
        """
        pass
    def ComplementArc(self) -> None:
        """
         Complements the arc 
        """
        pass
class CurveLocationType(Enum):
    """
    Members Include: 
     |Start|  Start point 
     |End|  End point 
     |Center|  Center point of arcs 
     |Mid|   Mid point of analytic types 

    """
    Start: int
    End: int
    Center: int
    Mid: int
    @staticmethod
    def ValueOf(value: int) -> CurveLocationType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class CurveLocation:
    @property
    def Type(self) -> CurveLocationType:
        """
        Getter for property Type
        the type of location relative to the edgecurve

        """
        pass
    @Type.setter
    def Type(self, value: CurveLocationType):
        """
        Getter for property Type
        the type of location relative to the edgecurve
        Setter for property Type
        the type of location relative to the edgecurve

        """
        pass
    @property
    def Location(self) -> NXOpen.Point3d:
        """
        Getter for property Location
        the location in the edgecurve's part space

        """
        pass
    @Location.setter
    def Location(self, value: NXOpen.Point3d):
        """
        Getter for property Location
        the location in the edgecurve's part space
        Setter for property Location
        the location in the edgecurve's part space

        """
        pass
import NXOpen
class CurveOptions(NXOpen.TaggedObject): 
    """ Represents the curve options data
    """
    class InputCurve(Enum):
        """
        Members Include: 
         |Retain|  Retains the original input curve and creates the new output curve 
         |Blank|  Blanks the original input curve and creates the new output curve 
         |Delete|  Deletes the original input curve and creates the new output curve 
         |Replace|  Replaces the original input curve with the new output curve 

        """
        Retain: int
        Blank: int
        Delete: int
        Replace: int
        @staticmethod
        def ValueOf(value: int) -> CurveOptions.InputCurve:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns the associativity option 
                 
            
         
        """
        pass
    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
         Returns the associativity option 
                 
            
         
        """
        pass
    @property
    def InputCurveOption(self) -> CurveOptions.InputCurve:
        """
        Getter for property: ( CurveOptions.InputCurve NXOpen.Geome) InputCurveOption
         Returns the curve options 
                 
            
         
        """
        pass
    @InputCurveOption.setter
    def InputCurveOption(self, input_curve_option: CurveOptions.InputCurve):
        """
        Setter for property: ( CurveOptions.InputCurve NXOpen.Geome) InputCurveOption
         Returns the curve options 
                 
            
         
        """
        pass
import NXOpen
class CurveRangeBuilder(NXOpen.TaggedObject): 
    """ Represents the curve range and anchor builder """
    class AnchorPositionType(Enum):
        """
        Members Include: 
         |Start|  Anchor at the start of the curve 
         |Center|  Anchor at the center of the curve 
         |End|  Anchor at the end of the curve 

        """
        Start: int
        Center: int
        End: int
        @staticmethod
        def ValueOf(value: int) -> CurveRangeBuilder.AnchorPositionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AnchorPosition(self) -> CurveRangeBuilder.AnchorPositionType:
        """
        Getter for property: ( CurveRangeBuilder.AnchorPositionType NXOpen.Geome) AnchorPosition
         Returns the anchor position   
            
         
        """
        pass
    @AnchorPosition.setter
    def AnchorPosition(self, anchorPosition: CurveRangeBuilder.AnchorPositionType):
        """
        Setter for property: ( CurveRangeBuilder.AnchorPositionType NXOpen.Geome) AnchorPosition
         Returns the anchor position   
            
         
        """
        pass
    @property
    def Center(self) -> OnPathDimensionBuilder:
        """
        Getter for property: ( OnPathDimensionBuilder NXOpen.Geome) Center
         Returns the center   
            
         
        """
        pass
    @property
    def End(self) -> OnPathDimensionBuilder:
        """
        Getter for property: ( OnPathDimensionBuilder NXOpen.Geome) End
         Returns the end   
            
         
        """
        pass
    @property
    def Start(self) -> OnPathDimensionBuilder:
        """
        Getter for property: ( OnPathDimensionBuilder NXOpen.Geome) Start
         Returns the start   
            
         
        """
        pass
import NXOpen
class CurveSettings(NXOpen.TaggedObject): 
    """ Represents the curve settings data
    """
    @property
    def CurveFitData(self) -> CurveFitData:
        """
        Getter for property: ( CurveFitData NXOpen.Geome) CurveFitData
         Returns the curve fit data   
            
         
        """
        pass
    @property
    def InputCurvesOption(self) -> CurveOptions:
        """
        Getter for property: ( CurveOptions NXOpen.Geome) InputCurvesOption
         Returns the input curves option   
            
         
        """
        pass
import NXOpen
import NXOpen.Features
class CurveShapingBuilder(NXOpen.TaggedObject): 
    """ Represents a NXOpen.GeometricUtilities.CurveShapingBuilder.
        This class allows shaping of curves by identifying key points on them and modifying the
        location of those points. It also allows constraining curve ends.  """
    class InsertionMethodOptions(Enum):
        """
        Members Include: 
         |Uniform|  Insert points uniformly 
         |ThroughPoints|  Insert points through points 
         |BetweenPoints|  Insert points between points 

        """
        Uniform: int
        ThroughPoints: int
        BetweenPoints: int
        @staticmethod
        def ValueOf(value: int) -> CurveShapingBuilder.InsertionMethodOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MovementMethodType(Enum):
        """
        Members Include: 
         |WCS|  Movement along WCS principal axis or plane 
         |View|  Movement in view plane 
         |Vector|  Movement along arbitrary direction 
         |Plane|  Movement in arbitrary plane 
         |Normal|  Movement along a face normal 

        """
        WCS: int
        View: int
        Vector: int
        Plane: int
        Normal: int
        @staticmethod
        def ValueOf(value: int) -> CurveShapingBuilder.MovementMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class WCSOptionType(Enum):
        """
        Members Include: 
         |X|  Along X axis 
         |Y|  Along Y axis 
         |Z|  Along Z axis 
         |YZ|  In YZ plane 
         |XZ|  In XZ plane 
         |XY|  In XY plane 

        """
        X: int
        Y: int
        Z: int
        YZ: int
        XZ: int
        XY: int
        @staticmethod
        def ValueOf(value: int) -> CurveShapingBuilder.WCSOptionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CanMoveAlongCurve(self) -> bool:
        """
        Getter for property: (bool) CanMoveAlongCurve
         Returns the value indicating if point should be moved along curve.  
           A key point is moved along the curve
                    in order to change its parametric location without affecting curve shape.    
         
        """
        pass
    @CanMoveAlongCurve.setter
    def CanMoveAlongCurve(self, canMoveAlongCurve: bool):
        """
        Setter for property: (bool) CanMoveAlongCurve
         Returns the value indicating if point should be moved along curve.  
           A key point is moved along the curve
                    in order to change its parametric location without affecting curve shape.    
         
        """
        pass
    @property
    def ConstraintManager(self) -> NXOpen.Features.GeometricConstraintDataManager:
        """
        Getter for property: ( NXOpen.Features.GeometricConstraintDataManager) ConstraintManager
         Returns the constraint manager.  
           Allows definition of key points to be used to shape the curve.   
         
        """
        pass
    @property
    def EndContinuity(self) -> Continuity.ContinuityTypes:
        """
        Getter for property: ( Continuity.ContinuityTypes NXOpen.Geome) EndContinuity
         Returns the continuity at end of the curve   
            
         
        """
        pass
    @EndContinuity.setter
    def EndContinuity(self, endContinuity: Continuity.ContinuityTypes):
        """
        Setter for property: ( Continuity.ContinuityTypes NXOpen.Geome) EndContinuity
         Returns the continuity at end of the curve   
            
         
        """
        pass
    @property
    def HasLinearTransition(self) -> bool:
        """
        Getter for property: (bool) HasLinearTransition
         Returns the value indicating if transition type is linear   
            
         
        """
        pass
    @HasLinearTransition.setter
    def HasLinearTransition(self, hasLinear: bool):
        """
        Setter for property: (bool) HasLinearTransition
         Returns the value indicating if transition type is linear   
            
         
        """
        pass
    @property
    def InsertionMethod(self) -> CurveShapingBuilder.InsertionMethodOptions:
        """
        Getter for property: ( CurveShapingBuilder.InsertionMethodOptions NXOpen.Geome) InsertionMethod
         Returns the point insertion method   
            
         
        """
        pass
    @InsertionMethod.setter
    def InsertionMethod(self, insertionMethod: CurveShapingBuilder.InsertionMethodOptions):
        """
        Setter for property: ( CurveShapingBuilder.InsertionMethodOptions NXOpen.Geome) InsertionMethod
         Returns the point insertion method   
            
         
        """
        pass
    @property
    def MovementMethod(self) -> CurveShapingBuilder.MovementMethodType:
        """
        Getter for property: ( CurveShapingBuilder.MovementMethodType NXOpen.Geome) MovementMethod
         Returns the movement method   
            
         
        """
        pass
    @MovementMethod.setter
    def MovementMethod(self, movementMethod: CurveShapingBuilder.MovementMethodType):
        """
        Setter for property: ( CurveShapingBuilder.MovementMethodType NXOpen.Geome) MovementMethod
         Returns the movement method   
            
         
        """
        pass
    @property
    def MovementPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) MovementPlane
         Returns the movement plane   
            
         
        """
        pass
    @MovementPlane.setter
    def MovementPlane(self, movementPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) MovementPlane
         Returns the movement plane   
            
         
        """
        pass
    @property
    def MovementVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) MovementVector
         Returns the movement vector   
            
         
        """
        pass
    @MovementVector.setter
    def MovementVector(self, movementVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) MovementVector
         Returns the movement vector   
            
         
        """
        pass
    @property
    def Number(self) -> int:
        """
        Getter for property: (int) Number
         Returns the number of points to be inserted   
            
         
        """
        pass
    @Number.setter
    def Number(self, number: int):
        """
        Setter for property: (int) Number
         Returns the number of points to be inserted   
            
         
        """
        pass
    @property
    def OrientExpress(self) -> OrientXpressBuilder:
        """
        Getter for property: ( OrientXpressBuilder NXOpen.Geome) OrientExpress
         Returns the orient express object   
            
         
        """
        pass
    @property
    def SelectCurves(self) -> NXOpen.SelectSplineList:
        """
        Getter for property: ( NXOpen.SelectSplineList) SelectCurves
         Returns the curve selection for point insertion   
            
         
        """
        pass
    @property
    def SpecifyPoints(self) -> NXOpen.SelectPointList:
        """
        Getter for property: ( NXOpen.SelectPointList) SpecifyPoints
         Returns the specified points to define insertion point locations   
            
         
        """
        pass
    @property
    def StartContinuity(self) -> Continuity.ContinuityTypes:
        """
        Getter for property: ( Continuity.ContinuityTypes NXOpen.Geome) StartContinuity
         Returns the continuity at start of the curve   
            
         
        """
        pass
    @StartContinuity.setter
    def StartContinuity(self, startContinuity: Continuity.ContinuityTypes):
        """
        Setter for property: ( Continuity.ContinuityTypes NXOpen.Geome) StartContinuity
         Returns the continuity at start of the curve   
            
         
        """
        pass
    @property
    def WCSOption(self) -> CurveShapingBuilder.WCSOptionType:
        """
        Getter for property: ( CurveShapingBuilder.WCSOptionType NXOpen.Geome) WCSOption
         Returns the WCS option   
            
         
        """
        pass
    @WCSOption.setter
    def WCSOption(self, wcsOption: CurveShapingBuilder.WCSOptionType):
        """
        Setter for property: ( CurveShapingBuilder.WCSOptionType NXOpen.Geome) WCSOption
         Returns the WCS option   
            
         
        """
        pass
    def AddCurve(self, curve: NXOpen.Curve) -> None:
        """
         Adds a curve for shaping 
        """
        pass
    def ApplyParameterValue(self, sourcePoint: NXOpen.Point, destinationPoints: List[NXOpen.Point]) -> None:
        """
         Applies parameter value from a key point to a group of key points without affecting curve shape 
        """
        pass
    def Deform(self) -> None:
        """
         Deforms curves based on active points 
        """
        pass
    def DeleteAllPoints(self, curve: NXOpen.Spline) -> None:
        """
         Deletes all points on a curve. If no curve is specified, deletes all points on all curves. 
        """
        pass
    def RemoveCurve(self, curve: NXOpen.Curve) -> None:
        """
         Removes a curve 
        """
        pass
    def SetActivePoints(self, points: List[NXOpen.Point], masterPoint: NXOpen.Point) -> None:
        """
         Sets key points that are selected or will be moved 
        """
        pass
import NXOpen
import NXOpen.Assemblies
class DegreesAndSegmentsOrPatchesBuilder(NXOpen.TaggedObject): 
    """ the DegreesAndSegmentsOrPatches builder """
    @property
    def Degree(self) -> int:
        """
        Getter for property: (int) Degree
         Returns the degree   
            
         
        """
        pass
    @Degree.setter
    def Degree(self, degree: int):
        """
        Setter for property: (int) Degree
         Returns the degree   
            
         
        """
        pass
    @property
    def IsOccurrence(self) -> bool:
        """
        Getter for property: (bool) IsOccurrence
         Returns whether this object is an occurrence or not.  
             
         
        """
        pass
    @property
    def JournalIdentifier(self) -> str:
        """
        Getter for property: (str) JournalIdentifier
         Returns the identifier that would be recorded in a journal for this object.  
           
            This may not be the same across different releases of the software.   
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the custom name of the object.  
              
         
        """
        pass
    @property
    def OwningComponent(self) -> NXOpen.Assemblies.Component:
        """
        Getter for property: ( NXOpen.Assemblies.Component) OwningComponent
         Returns the owning component, if this object is an occurrence.  
             
         
        """
        pass
    @property
    def OwningPart(self) -> NXOpen.BasePart:
        """
        Getter for property: ( NXOpen.BasePart) OwningPart
         Returns the owning part of this object   
            
         
        """
        pass
    @property
    def Prototype(self) -> NXOpen.INXObject:
        """
        Getter for property: ( NXOpen.INXObject) Prototype
         Returns the prototype of this object if it is an occurrence.  
             
         
        """
        pass
    @property
    def SegmentsOrPatches(self) -> int:
        """
        Getter for property: (int) SegmentsOrPatches
         Returns the patches   
            
         
        """
        pass
    @SegmentsOrPatches.setter
    def SegmentsOrPatches(self, segmentsOrPatches: int):
        """
        Setter for property: (int) SegmentsOrPatches
         Returns the patches   
            
         
        """
        pass
    @property
    def UDegree(self) -> int:
        """
        Getter for property: (int) UDegree
         Returns the u degree   
            
         
        """
        pass
    @UDegree.setter
    def UDegree(self, uDegree: int):
        """
        Setter for property: (int) UDegree
         Returns the u degree   
            
         
        """
        pass
    @property
    def UPatches(self) -> int:
        """
        Getter for property: (int) UPatches
         Returns the u patches   
            
         
        """
        pass
    @UPatches.setter
    def UPatches(self, uPatches: int):
        """
        Setter for property: (int) UPatches
         Returns the u patches   
            
         
        """
        pass
    @property
    def VDegree(self) -> int:
        """
        Getter for property: (int) VDegree
         Returns the v degree   
            
         
        """
        pass
    @VDegree.setter
    def VDegree(self, vDegree: int):
        """
        Setter for property: (int) VDegree
         Returns the v degree   
            
         
        """
        pass
    @property
    def VPatches(self) -> int:
        """
        Getter for property: (int) VPatches
         Returns the v patches   
            
         
        """
        pass
    @VPatches.setter
    def VPatches(self, vPatches: int):
        """
        Setter for property: (int) VPatches
         Returns the v patches   
            
         
        """
        pass
import NXOpen
class DepthSkewBuilder(NXOpen.TaggedObject): 
    """
        This class provides ability to specify a depth and a skew value.
    """
    @property
    def Depth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Depth
         Returns the depth   
            
         
        """
        pass
    @property
    def Skew(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Skew
         Returns the skew   
            
         
        """
        pass
import NXOpen
class DesignMeshBody(NXOpen.DisplayableObject): 
    """ Represents a faceted mesh. """
    def GetEdges(self) -> List[DesignMeshEdge]:
        """
         Returns the edges in the mesh. 
         Returns edges ( DesignMeshEdge List[NXOpen.Geo):  .
        """
        pass
    def GetFaces(self) -> List[DesignMeshFace]:
        """
         Returns the faces in the mesh. 
         Returns faces ( DesignMeshFace List[NXOpen.Geo):  .
        """
        pass
    def GetVertices(self) -> List[DesignMeshVertex]:
        """
         Returns the vertexes in the mesh. 
         Returns vertices ( DesignMeshVertex List[NXOpen.Geo):  .
        """
        pass
import NXOpen
class DesignMeshEdge(NXOpen.DisplayableObject): 
    """ Represents a facet mesh edge. """
    def GetBody(self) -> DesignMeshBody:
        """
         Returns the mesh owning this edge. 
         Returns body ( DesignMeshBody NXOpen.Geome):  .
        """
        pass
    def GetFaces(self) -> Tuple[DesignMeshFace, DesignMeshFace]:
        """
         Returns the faces connected to the edge. 
         Returns A tuple consisting of (face1, face2). 
         - face1 is:  DesignMeshFace NXOpen.Geome. First face of the edge .
         - face2 is:  DesignMeshFace NXOpen.Geome. Second face of the edge, could null in case of boundary edge. .

        """
        pass
    def GetVertices(self) -> Tuple[DesignMeshVertex, DesignMeshVertex]:
        """
         Returns the vertexes of the edge. 
         Returns A tuple consisting of (vertex1, vertex2). 
         - vertex1 is:  DesignMeshVertex NXOpen.Geome. First vertex in the edge .
         - vertex2 is:  DesignMeshVertex NXOpen.Geome. Second vertex in the edge .

        """
        pass
import NXOpen
class DesignMeshFace(NXOpen.DisplayableObject): 
    """ Represents a facet mesh face. """
    def GetBody(self) -> DesignMeshBody:
        """
         Returns the mesh owning this face. 
         Returns body ( DesignMeshBody NXOpen.Geome):  .
        """
        pass
    def GetEdges(self) -> List[DesignMeshEdge]:
        """
         Returns the edges of the face. 
         Returns edges ( DesignMeshEdge List[NXOpen.Geo):  .
        """
        pass
    def GetVertices(self) -> List[DesignMeshVertex]:
        """
         Returns the vertexes of the face. 
         Returns vertices ( DesignMeshVertex List[NXOpen.Geo):  .
        """
        pass
import NXOpen
class DesignMeshVertex(NXOpen.DisplayableObject): 
    """ Represents a facet mesh vertex. """
    def GetBody(self) -> DesignMeshBody:
        """
         Returns the mesh owning this vertex. 
         Returns body ( DesignMeshBody NXOpen.Geome):  .
        """
        pass
    def GetCoordinates(self) -> NXOpen.Point3d:
        """
         Returns the position of the vertex. 
         Returns position ( NXOpen.Point3d):  .
        """
        pass
    def GetEdges(self) -> List[DesignMeshEdge]:
        """
         Returns the edges connected to the vertex. 
         Returns edges ( DesignMeshEdge List[NXOpen.Geo):  .
        """
        pass
    def GetFaces(self) -> List[DesignMeshFace]:
        """
         Returns the faces connected to the vertex. 
         Returns faces ( DesignMeshFace List[NXOpen.Geo):  .
        """
        pass
import NXOpen
import NXOpen.Preferences
class DisplayResolutionBuilder(NXOpen.TaggedObject): 
    """ Represents a NXOpen.GeometricUtilities.DisplayResolutionBuilder.
        The display resolution block defines the parameters for faceting."""
    @property
    def AngleTolerance(self) -> float:
        """
        Getter for property: (float) AngleTolerance
         Returns the angle tolerance   
            
         
        """
        pass
    @AngleTolerance.setter
    def AngleTolerance(self, angleTolerance: float):
        """
        Setter for property: (float) AngleTolerance
         Returns the angle tolerance   
            
         
        """
        pass
    @property
    def EdgeTolerance(self) -> float:
        """
        Getter for property: (float) EdgeTolerance
         Returns the edge tolerance   
            
         
        """
        pass
    @EdgeTolerance.setter
    def EdgeTolerance(self, edgeTolerance: float):
        """
        Setter for property: (float) EdgeTolerance
         Returns the edge tolerance   
            
         
        """
        pass
    @property
    def FaceTolerance(self) -> float:
        """
        Getter for property: (float) FaceTolerance
         Returns the face tolerance   
            
         
        """
        pass
    @FaceTolerance.setter
    def FaceTolerance(self, faceTolerance: float):
        """
        Setter for property: (float) FaceTolerance
         Returns the face tolerance   
            
         
        """
        pass
    @property
    def Resolution(self) -> NXOpen.Preferences.PartVisualizationShade.AdvViewToleranceType:
        """
        Getter for property: ( NXOpen.Preferences.PartVisualizationShade.AdvViewToleranceType) Resolution
         Returns the resolution   
            
         
        """
        pass
    @Resolution.setter
    def Resolution(self, resolution: NXOpen.Preferences.PartVisualizationShade.AdvViewToleranceType):
        """
        Setter for property: ( NXOpen.Preferences.PartVisualizationShade.AdvViewToleranceType) Resolution
         Returns the resolution   
            
         
        """
        pass
    @property
    def WidthTolerance(self) -> float:
        """
        Getter for property: (float) WidthTolerance
         Returns the width tolerance   
            
         
        """
        pass
    @WidthTolerance.setter
    def WidthTolerance(self, widthTolerance: float):
        """
        Setter for property: (float) WidthTolerance
         Returns the width tolerance   
            
         
        """
        pass
import NXOpen
class DistancePatternSpacing(PatternSpacing): 
    """ defines the various ways pattern instances can be 
        spaced within the pattern, particularly in the context of the
        PatternDefinition class. """
    @property
    def PitchDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PitchDistance
         Returns the distance for the spacing of the pattern from one instance to the next.  
            
         
        """
        pass
    @property
    def SpanDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SpanDistance
         Returns the distance for the spacing of the pattern for the entire pattern.  
             
         
        """
        pass
import NXOpen
class DraftPointData(NXOpen.TaggedObject): 
    """ Represents a draft point data object
    """
    @property
    def Parameter(self) -> float:
        """
        Getter for property: (float) Parameter
         Returns the point coordinates
                   
            
         
        """
        pass
    @Parameter.setter
    def Parameter(self, parameter: float):
        """
        Setter for property: (float) Parameter
         Returns the point coordinates
                   
            
         
        """
        pass
    def GetAngle(self) -> NXOpen.Expression:
        """
         Returns the Angle value
                 
         Returns angle ( NXOpen.Expression):  Angle Expression Object .
        """
        pass
    def SetAngle(self, angle: str) -> None:
        """
         Sets the Angle value
                 
        """
        pass
import NXOpen
class DraftVariableAngleData(NXOpen.TaggedObject): 
    """ Represents data containing variable angle draft point data objects
    """
    def AddDraftPoints(self, points: List[DraftPointData]) -> None:
        """
         Adds NXOpen.GeometricUtilities.DraftPointData objects    
                 
        """
        pass
    def GetDraftPoints(self) -> List[DraftPointData]:
        """
         Returns NXOpen.GeometricUtilities.DraftPointData objects
                 
         Returns points ( DraftPointData List[NXOpen.Geo):  Array of DraftPointData Objects .
        """
        pass
    def GetNumberOfDraftPoints(self) -> int:
        """
         Returns number of NXOpen.GeometricUtilities.DraftPointData objects
                 
         Returns num_points (int):  Number of DraftPointData Objects .
        """
        pass
    def RemoveDraftPoints(self, points: List[DraftPointData]) -> None:
        """
         Removes NXOpen.GeometricUtilities.DraftPointData objects
                 
        """
        pass
class Dummy(Enum):
    """
    Members Include: 
     |Line| 

    """
    Line: int
    @staticmethod
    def ValueOf(value: int) -> Dummy:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class EndHoleData(NXOpen.TaggedObject): 
    """ Represents a NXOpen.GeometricUtilities.EndHoleData """
    class FormOptions(Enum):
        """
        Members Include: 
         |ScrewClearance|  Screw clearance 
         |Threaded|  Threaded hole 
         |Through|  Through hole - This option should not be used in NX6 and later versions. Instead of this
                                                                         screw_clearance option should be used 

        """
        ScrewClearance: int
        Threaded: int
        Through: int
        @staticmethod
        def ValueOf(value: int) -> EndHoleData.FormOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class HoleDepthLimitOptions(Enum):
        """
        Members Include: 
         |Value|  Value limit options 
         |UntilSelected|  Until selected limit options 
         |UntilNext|  Until next limit options 
         |ThroughBody|  Through body limit options 

        """
        Value: int
        UntilSelected: int
        UntilNext: int
        ThroughBody: int
        @staticmethod
        def ValueOf(value: int) -> EndHoleData.HoleDepthLimitOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class HoleDepthOptions(Enum):
        """
        Members Include: 
         |ToCylinderBottom| 
         |ToConeTip| 

        """
        ToCylinderBottom: int
        ToConeTip: int
        @staticmethod
        def ValueOf(value: int) -> EndHoleData.HoleDepthOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ThreadLengthOptions(Enum):
        """
        Members Include: 
         |Diameterx1|  1    (tap drill diameter) 
         |Diameterx15|  1.5  (tap drill diameter) 
         |Diameterx20|  2    (tap drill diameter) 
         |Diameterx25|  2.5  (tap drill diameter) 
         |Diameterx30|  3    (tap drill diameter) 
         |Standard|  Length is standard 
         |Custom|  Length is custom 
         |Full|  Length is full hole depth 

        """
        Diameterx1: int
        Diameterx15: int
        Diameterx20: int
        Diameterx25: int
        Diameterx30: int
        Standard: int
        Custom: int
        Full: int
        @staticmethod
        def ValueOf(value: int) -> EndHoleData.ThreadLengthOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ThreadRotationOptions(Enum):
        """
        Members Include: 
         |Right|  Right rotation 
         |Left|  Left rotation 

        """
        Right: int
        Left: int
        @staticmethod
        def ValueOf(value: int) -> EndHoleData.ThreadRotationOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BooleanOperation(self) -> BooleanOperation:
        """
        Getter for property: ( BooleanOperation NXOpen.Geome) BooleanOperation
         Returns the boolean operation   
            
         
        """
        pass
    @property
    def DepthOption(self) -> EndHoleData.HoleDepthOptions:
        """
        Getter for property: ( EndHoleData.HoleDepthOptions NXOpen.Geome) DepthOption
         Returns the hole depth option   
            
         
        """
        pass
    @DepthOption.setter
    def DepthOption(self, depthOption: EndHoleData.HoleDepthOptions):
        """
        Setter for property: ( EndHoleData.HoleDepthOptions NXOpen.Geome) DepthOption
         Returns the hole depth option   
            
         
        """
        pass
    @property
    def FitOption(self) -> str:
        """
        Getter for property: (str) FitOption
         Returns the fit option   
            
         
        """
        pass
    @FitOption.setter
    def FitOption(self, fitOption: str):
        """
        Setter for property: (str) FitOption
         Returns the fit option   
            
         
        """
        pass
    @property
    def FormOption(self) -> EndHoleData.FormOptions:
        """
        Getter for property: ( EndHoleData.FormOptions NXOpen.Geome) FormOption
         Returns the form option   
            
         
        """
        pass
    @FormOption.setter
    def FormOption(self, formOption: EndHoleData.FormOptions):
        """
        Setter for property: ( EndHoleData.FormOptions NXOpen.Geome) FormOption
         Returns the form option   
            
         
        """
        pass
    @property
    def HoleDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) HoleDepth
         Returns the hole depth   
            
         
        """
        pass
    @property
    def HoleDepthLimitOption(self) -> EndHoleData.HoleDepthLimitOptions:
        """
        Getter for property: ( EndHoleData.HoleDepthLimitOptions NXOpen.Geome) HoleDepthLimitOption
         Returns the hole depth limit   
            
         
        """
        pass
    @HoleDepthLimitOption.setter
    def HoleDepthLimitOption(self, holeDepthLimitOption: EndHoleData.HoleDepthLimitOptions):
        """
        Setter for property: ( EndHoleData.HoleDepthLimitOptions NXOpen.Geome) HoleDepthLimitOption
         Returns the hole depth limit   
            
         
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
    def MatchDimOfStartHole(self) -> bool:
        """
        Getter for property: (bool) MatchDimOfStartHole
         Returns the match dim of start hole   
            
         
        """
        pass
    @MatchDimOfStartHole.setter
    def MatchDimOfStartHole(self, matchDimOfStartHole: bool):
        """
        Setter for property: (bool) MatchDimOfStartHole
         Returns the match dim of start hole   
            
         
        """
        pass
    @property
    def RadialEngageOption(self) -> str:
        """
        Getter for property: (str) RadialEngageOption
         Returns the radial engage option   
            
         
        """
        pass
    @RadialEngageOption.setter
    def RadialEngageOption(self, radialEngageOption: str):
        """
        Setter for property: (str) RadialEngageOption
         Returns the radial engage option   
            
         
        """
        pass
    @property
    def ReliefChamferEnabled(self) -> bool:
        """
        Getter for property: (bool) ReliefChamferEnabled
         Returns the threaded relief chamfer enabled - this is applicable for threaded hole type   
            
         
        """
        pass
    @ReliefChamferEnabled.setter
    def ReliefChamferEnabled(self, reliefChamferEnabled: bool):
        """
        Setter for property: (bool) ReliefChamferEnabled
         Returns the threaded relief chamfer enabled - this is applicable for threaded hole type   
            
         
        """
        pass
    @property
    def ScrewClearanceEndChamferAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ScrewClearanceEndChamferAngle
         Returns the screw clearance end chamfer angle   
            
         
        """
        pass
    @property
    def ScrewClearanceEndChamferEnabled(self) -> bool:
        """
        Getter for property: (bool) ScrewClearanceEndChamferEnabled
         Returns the screw clearance end chamfer enabled   
            
         
        """
        pass
    @ScrewClearanceEndChamferEnabled.setter
    def ScrewClearanceEndChamferEnabled(self, screwClearanceEndChamferEnabled: bool):
        """
        Setter for property: (bool) ScrewClearanceEndChamferEnabled
         Returns the screw clearance end chamfer enabled   
            
         
        """
        pass
    @property
    def ScrewClearanceEndChamferOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ScrewClearanceEndChamferOffset
         Returns the screw clearance end chamfer offset   
            
         
        """
        pass
    @property
    def ScrewClearanceStartChamferAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ScrewClearanceStartChamferAngle
         Returns the screw clearance start chamfer angle   
            
         
        """
        pass
    @property
    def ScrewClearanceStartChamferEnabled(self) -> bool:
        """
        Getter for property: (bool) ScrewClearanceStartChamferEnabled
         Returns the screw clearance start chamfer enabled   
            
         
        """
        pass
    @ScrewClearanceStartChamferEnabled.setter
    def ScrewClearanceStartChamferEnabled(self, screwClearenceStartChamferEnabled: bool):
        """
        Setter for property: (bool) ScrewClearanceStartChamferEnabled
         Returns the screw clearance start chamfer enabled   
            
         
        """
        pass
    @property
    def ScrewClearanceStartChamferOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ScrewClearanceStartChamferOffset
         Returns the screw clearance start chamfer offset   
            
         
        """
        pass
    @property
    def TapDrillDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TapDrillDiameter
         Returns the tap drill diameter   
            
         
        """
        pass
    @property
    def ThreadDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ThreadDepth
         Returns the thread depth   
            
         
        """
        pass
    @property
    def ThreadLengthOption(self) -> EndHoleData.ThreadLengthOptions:
        """
        Getter for property: ( EndHoleData.ThreadLengthOptions NXOpen.Geome) ThreadLengthOption
         Returns the thread length option   
            
         
        """
        pass
    @ThreadLengthOption.setter
    def ThreadLengthOption(self, threadLengthOption: EndHoleData.ThreadLengthOptions):
        """
        Setter for property: ( EndHoleData.ThreadLengthOptions NXOpen.Geome) ThreadLengthOption
         Returns the thread length option   
            
         
        """
        pass
    @property
    def ThreadRotation(self) -> EndHoleData.ThreadRotationOptions:
        """
        Getter for property: ( EndHoleData.ThreadRotationOptions NXOpen.Geome) ThreadRotation
         Returns the thread rotation   
            
         
        """
        pass
    @ThreadRotation.setter
    def ThreadRotation(self, threadRotation: EndHoleData.ThreadRotationOptions):
        """
        Setter for property: ( EndHoleData.ThreadRotationOptions NXOpen.Geome) ThreadRotation
         Returns the thread rotation   
            
         
        """
        pass
    @property
    def ThreadSize(self) -> str:
        """
        Getter for property: (str) ThreadSize
         Returns the thread size   
            
         
        """
        pass
    @ThreadSize.setter
    def ThreadSize(self, threadSize: str):
        """
        Setter for property: (str) ThreadSize
         Returns the thread size   
            
         
        """
        pass
    @property
    def ThreadedEndChamferAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ThreadedEndChamferAngle
         Returns the threaded end chamfer angle   
            
         
        """
        pass
    @property
    def ThreadedEndChamferDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ThreadedEndChamferDiameter
         Returns the threaded end chamfer offset   
            
         
        """
        pass
    @property
    def ThreadedEndChamferEnabled(self) -> bool:
        """
        Getter for property: (bool) ThreadedEndChamferEnabled
         Returns the threaded end chamfer enabled   
            
         
        """
        pass
    @ThreadedEndChamferEnabled.setter
    def ThreadedEndChamferEnabled(self, threadedEndChamferEnabled: bool):
        """
        Setter for property: (bool) ThreadedEndChamferEnabled
         Returns the threaded end chamfer enabled   
            
         
        """
        pass
    @property
    def ThreadedReliefAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ThreadedReliefAngle
         Returns the relief angle - this is applicable for threaded hole type   
            
         
        """
        pass
    @property
    def ThreadedReliefChamferAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ThreadedReliefChamferAngle
         Returns the threaded relief chamfer angle - this is applicable for threaded hole type   
            
         
        """
        pass
    @property
    def ThreadedReliefChamferOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ThreadedReliefChamferOffset
         Returns the threaded relief chamfer offset - this is applicable for threaded hole type   
            
         
        """
        pass
    @property
    def ThreadedReliefDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ThreadedReliefDepth
         Returns the threaded relief depth - this is applicable for threaded hole type   
            
         
        """
        pass
    @property
    def ThreadedReliefDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ThreadedReliefDiameter
         Returns the relief diameter - this is applicable for threaded hole type   
            
         
        """
        pass
    @property
    def ThreadedReliefEnabled(self) -> bool:
        """
        Getter for property: (bool) ThreadedReliefEnabled
         Returns the threaded relief enabled - this is applicable for threaded hole type   
            
         
        """
        pass
    @ThreadedReliefEnabled.setter
    def ThreadedReliefEnabled(self, threadedReliefEnabled: bool):
        """
        Setter for property: (bool) ThreadedReliefEnabled
         Returns the threaded relief enabled - this is applicable for threaded hole type   
            
         
        """
        pass
    @property
    def ThreadedStartChamferAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ThreadedStartChamferAngle
         Returns the threaded start chamfer angle   
            
         
        """
        pass
    @property
    def ThreadedStartChamferDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ThreadedStartChamferDiameter
         Returns the threaded start chamfer offset   
            
         
        """
        pass
    @property
    def ThreadedStartChamferEnabled(self) -> bool:
        """
        Getter for property: (bool) ThreadedStartChamferEnabled
         Returns the threaded start chamfer enabled   
            
         
        """
        pass
    @ThreadedStartChamferEnabled.setter
    def ThreadedStartChamferEnabled(self, threadedStartChamferEnabled: bool):
        """
        Setter for property: (bool) ThreadedStartChamferEnabled
         Returns the threaded start chamfer enabled   
            
         
        """
        pass
    @property
    def TipAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TipAngle
         Returns the tip angle   
            
         
        """
        pass
    @property
    def UntilSelectedTarget(self) -> NXOpen.SelectFace:
        """
        Getter for property: ( NXOpen.SelectFace) UntilSelectedTarget
         Returns the until selected target - this is applicable for general hole and threaded hole type   
            
         
        """
        pass
import NXOpen
class EntityUsageInfoList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[EntityUsageInfo]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: EntityUsageInfo) -> None:
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
    def Erase(self, obj: EntityUsageInfo) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: EntityUsageInfo, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: EntityUsageInfo) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> EntityUsageInfo:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( EntityUsageInfo NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[EntityUsageInfo]:
        """
         Gets the contents of the entire list 
         Returns objects ( EntityUsageInfo List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: EntityUsageInfo) -> None:
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
    def SetContents(self, objects: List[EntityUsageInfo]) -> None:
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
    def Swap(self, object1: EntityUsageInfo, object2: EntityUsageInfo) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.Features
class EntityUsageInfo(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.GeometricUtilities.EntityUsageInfo. An object of this class provides the
    dependency information for a single reparentable entity (edge or face). The creation of NXOpen.GeometricUtilities.EntityUsageInfo
    is restricted for internal use (see NXOpen.GeometricUtilities.ReplAsstBuilder).
    """
    class Status(Enum):
        """
        Members Include: 
         |Unused|  unused 
         |IntraPart|  used in same part 
         |InterPart|  used interpart 

        """
        Unused: int
        IntraPart: int
        InterPart: int
        @staticmethod
        def ValueOf(value: int) -> EntityUsageInfo.Status:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Entity(self) -> NXOpen.DisplayableObject:
        """
        Getter for property: ( NXOpen.DisplayableObject) Entity
         Returns the important entity.  
             
         
        """
        pass
    @property
    def UsageStatus(self) -> EntityUsageInfo.Status:
        """
        Getter for property: ( EntityUsageInfo.Status NXOpen.Geome) UsageStatus
         Returns the usage status of the corresponding entity   
            
         
        """
        pass
    def GetDependentFeatures(self, typeOfUsage: EntityUsageInfo.Status) -> Tuple[List[NXOpen.Features.Feature], List[str]]:
        """
         Query the dependent features of this entity. Use 'typeOfUsage' to restrict the query to
                    intra-part features or to include interpart features too. 
         Returns A tuple consisting of (dependentFeatures, detailedUsageInfo). 
         - dependentFeatures is:  NXOpen.Features.Feature Li. dependent features .
         - detailedUsageInfo is: List[str]. detailed usage information for each dependent feature .

        """
        pass
    def GetOtherDependents(self, typeOfUsage: EntityUsageInfo.Status) -> Tuple[List[NXOpen.NXObject], List[str]]:
        """
         Query other dependents of this entity. Use 'typeOfUsage' to restrict the query to
                    intra-part dependents or to include interpart usage too. 
         Returns A tuple consisting of (otherDependents, detailedUsageInfo). 
         - otherDependents is:  NXOpen.NXObject Li. dependent objects .
         - detailedUsageInfo is: List[str]. detailed usage information for each dependent object .

        """
        pass
import NXOpen
class Extend(NXOpen.TaggedObject): 
    """ Represents an extend data. Inputs to this class can be convergent objects.
    """
    class ExtendType(Enum):
        """
        Members Include: 
         |Value|  
         |ValueFromStartLimit| 
         |UntilNext|  
         |UntilSelected|  
         |UntilExtended|  
         |OffsetFromSelected|  
         |ThroughAll|  
         |Symmetric|  
         |Percent|  
         |ArcLength|  
         |ThruPoint|  

        """
        Value: int
        ValueFromStartLimit: int
        UntilNext: int
        UntilSelected: int
        UntilExtended: int
        OffsetFromSelected: int
        ThroughAll: int
        Symmetric: int
        Percent: int
        ArcLength: int
        ThruPoint: int
        @staticmethod
        def ValueOf(value: int) -> Extend.ExtendType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Target(self) -> NXOpen.DisplayableObject:
        """
        Getter for property: ( NXOpen.DisplayableObject) Target
         Returns the extend target for the following types
                     NXOpen::GeometricUtilities::Extend::ExtendTypeUntilSelected .  
            
                     NXOpen::GeometricUtilities::Extend::ExtendTypeUntilExtended .  
                  
         
        """
        pass
    @Target.setter
    def Target(self, selected_object: NXOpen.DisplayableObject):
        """
        Setter for property: ( NXOpen.DisplayableObject) Target
         Returns the extend target for the following types
                     NXOpen::GeometricUtilities::Extend::ExtendTypeUntilSelected .  
            
                     NXOpen::GeometricUtilities::Extend::ExtendTypeUntilExtended .  
                  
         
        """
        pass
    @property
    def TrimType(self) -> Extend.ExtendType:
        """
        Getter for property: ( Extend.ExtendType NXOpen.Geome) TrimType
         Returns the extend type 
                     NXOpen::GeometricUtilities::Extend::ExtendType .  
          
                  
         
        """
        pass
    @TrimType.setter
    def TrimType(self, extend_type: Extend.ExtendType):
        """
        Setter for property: ( Extend.ExtendType NXOpen.Geome) TrimType
         Returns the extend type 
                     NXOpen::GeometricUtilities::Extend::ExtendType .  
          
                  
         
        """
        pass
    @property
    def Value(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Value
         Returns the extend value for the following type
                     NXOpen::GeometricUtilities::Extend::ExtendTypeValue .  
          
                  
         
        """
        pass
    def SetValue(self, value_expression: str) -> None:
        """
         Set extend value for the following type
                    NXOpen.GeometricUtilities.Extend.ExtendType.Value.
                
        """
        pass
class ExtensionDirection(Enum):
    """
    Members Include: 
     |Natural|  Extension Direction Natural 
     |Linear|  Extension Direction Circular 
     |Circular|  Extension Direction Linear 

    """
    Natural: int
    Linear: int
    Circular: int
    @staticmethod
    def ValueOf(value: int) -> ExtensionDirection:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class ExtensionMethod(Enum):
    """
    Members Include: 
     |Incremental|  Extension Method Incremental 
     |Total|  Extension Method Total 

    """
    Incremental: int
    Total: int
    @staticmethod
    def ValueOf(value: int) -> ExtensionMethod:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class ExtensionSide(Enum):
    """
    Members Include: 
     |StartEnd|  Extension Side StartEnd 
     |Start|  Extension Side Start 
     |End|  Extension Side End 
     |Symmetric|  Extension Side Symmetric 

    """
    StartEnd: int
    Start: int
    End: int
    Symmetric: int
    @staticmethod
    def ValueOf(value: int) -> ExtensionSide:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class ExtrudeRevolveToolBuilder(NXOpen.TaggedObject): 
    """ a class which is a sub-component of BooleanTool. It provides other two basic tools
       creation methods by creating extrude or revolve bodies on the fly. Given a
       super section with non-intersecting loops and a certain direction,
       it will create a revolve tool or an extrude tool to do the boolean operation.
      """
    @property
    def ToolAxis(self) -> NXOpen.Axis:
        """
        Getter for property: ( NXOpen.Axis) ToolAxis
         Returns the tool axis used for doing revolve  
            
         
        """
        pass
    @ToolAxis.setter
    def ToolAxis(self, toolAxis: NXOpen.Axis):
        """
        Setter for property: ( NXOpen.Axis) ToolAxis
         Returns the tool axis used for doing revolve  
            
         
        """
        pass
    @property
    def ToolDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ToolDirection
         Returns the tool direction used for doing extrude   
            
         
        """
        pass
    @ToolDirection.setter
    def ToolDirection(self, toolDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ToolDirection
         Returns the tool direction used for doing extrude   
            
         
        """
        pass
    @property
    def ToolSection(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) ToolSection
         Returns the tool super section   
            
         
        """
        pass
import NXOpen
class FaceChangeOverflowBehavior(NXOpen.TaggedObject): 
    """   
    Represents a NXOpen.GeometricUtilities.FaceChangeOverflowBehavior
    It provides several face change options for controlling behavior when a change face overflows an incident face.
    """
    class Option(Enum):
        """
        Members Include: 
         |Automatic|  Automatic 
         |ExtendChangeFace|  Extend Change Face 
         |ExtendIncidentFace|  Extend Incident Face 
         |ExtendCapFace|  Extend Cap Face 

        """
        Automatic: int
        ExtendChangeFace: int
        ExtendIncidentFace: int
        ExtendCapFace: int
        @staticmethod
        def ValueOf(value: int) -> FaceChangeOverflowBehavior.Option:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FaceChangeOption(self) -> FaceChangeOverflowBehavior.Option:
        """
        Getter for property: ( FaceChangeOverflowBehavior.Option NXOpen.Geome) FaceChangeOption
         Returns the face change option.  
          
                  
         
        """
        pass
    @FaceChangeOption.setter
    def FaceChangeOption(self, faceChangeOption: FaceChangeOverflowBehavior.Option):
        """
        Setter for property: ( FaceChangeOverflowBehavior.Option NXOpen.Geome) FaceChangeOption
         Returns the face change option.  
          
                  
         
        """
        pass
import NXOpen
class FacePairingBuilder(NXOpen.TaggedObject): 
    """ a class which defines face pairing builder. 
      """
    class PairingStrategyType(Enum):
        """
        Members Include: 
         |Progressive| Automatic Pairing; Progressive thickness is used
         |Thickness| Automatic Pairing: Find all faces within search distance 
         |NotSet| Automatic pairing process is off 

        """
        Progressive: int
        Thickness: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> FacePairingBuilder.PairingStrategyType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AutomaticOffsetOnlyOption(self) -> bool:
        """
        Getter for property: (bool) AutomaticOffsetOnlyOption
         Returns the option to force the creation the mid-surface using the offset method for all automatic face pairs   
            
         
        """
        pass
    @AutomaticOffsetOnlyOption.setter
    def AutomaticOffsetOnlyOption(self, automaticOffsetOnlyOption: bool):
        """
        Setter for property: (bool) AutomaticOffsetOnlyOption
         Returns the option to force the creation the mid-surface using the offset method for all automatic face pairs   
            
         
        """
        pass
    @property
    def AutomaticTrimOption(self) -> bool:
        """
        Getter for property: (bool) AutomaticTrimOption
         Returns the option to trim all automatic face pairs   
            
         
        """
        pass
    @AutomaticTrimOption.setter
    def AutomaticTrimOption(self, automaticTrimOption: bool):
        """
        Setter for property: (bool) AutomaticTrimOption
         Returns the option to trim all automatic face pairs   
            
         
        """
        pass
    @property
    def CollectorPairList(self) -> CollectorPairListBuilder:
        """
        Getter for property: ( CollectorPairListBuilder NXOpen.Geome) CollectorPairList
         Returns the  GeometricUtilities::CollectorPairListBuilder  for manual pairing   
            
         
        """
        pass
    @property
    def InputSolidBodies(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) InputSolidBodies
         Returns the input solid bodies used to find the default face pairs   
            
         
        """
        pass
    @property
    def MergeAngleTolerance(self) -> float:
        """
        Getter for property: (float) MergeAngleTolerance
         Returns the merge angle tolerance   
            
         
        """
        pass
    @MergeAngleTolerance.setter
    def MergeAngleTolerance(self, mergeAngleTolerance: float):
        """
        Setter for property: (float) MergeAngleTolerance
         Returns the merge angle tolerance   
            
         
        """
        pass
    @property
    def PairingStrategy(self) -> FacePairingBuilder.PairingStrategyType:
        """
        Getter for property: ( FacePairingBuilder.PairingStrategyType NXOpen.Geome) PairingStrategy
         Returns the pairing strategy used by automatic pairs   
            
         
        """
        pass
    @PairingStrategy.setter
    def PairingStrategy(self, pairingStrategy: FacePairingBuilder.PairingStrategyType):
        """
        Setter for property: ( FacePairingBuilder.PairingStrategyType NXOpen.Geome) PairingStrategy
         Returns the pairing strategy used by automatic pairs   
            
         
        """
        pass
    @property
    def ThicknessRatio(self) -> float:
        """
        Getter for property: (float) ThicknessRatio
         Returns the thickness to solid diagonal length ratio used by the automatic face pair search   
            
         
        """
        pass
    @ThicknessRatio.setter
    def ThicknessRatio(self, thicknessRatio: float):
        """
        Setter for property: (float) ThicknessRatio
         Returns the thickness to solid diagonal length ratio used by the automatic face pair search   
            
         
        """
        pass
    @property
    def ThicknessValue(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ThicknessValue
         Returns the thickness value when pairing strategy is set to Thickness   
            
         
        """
        pass
    def ExcludeFace(self, face: NXOpen.Face) -> None:
        """
         Face that is explicitly selected by the user to be excluded in the search of possible face pairs 
        """
        pass
    def IncludeFace(self, face: NXOpen.Face) -> bool:
        """
         Face that is explicitly selected by the user to be included in the search of possible face pairs 
         Returns isFacePairExcluded (bool):  If true, an excluded automatic face pair was removed and is now included. .
        """
        pass
import NXOpen
class FacePlaneSelectionBuilderCollection(NXOpen.TaggedObjectCollection): 
    """ This class contains the factory methods for creating an FacePlaneSelectionBuilder. """
    def Create(self) -> FacePlaneSelectionBuilder:
        """
         Creates an FacePlaneSelectionBuilder. 
         Returns entityBuilderData ( FacePlaneSelectionBuilder NXOpen.Geome): .
        """
        pass
    def Destroy(self, entityBuilderData: FacePlaneSelectionBuilder) -> None:
        """
         Destroys an FacePlaneSelectionBuilder. 
        """
        pass
import NXOpen
class FacePlaneSelectionBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.GeometricUtilities.FacePlaneSelectionBuilder
    """
    class TrimObjectType(Enum):
        """
        Members Include: 
         |Plane|  plane end cap
         |Face|  face end cap
         |Edge|  edge limit cap 

        """
        Plane: int
        Face: int
        Edge: int
        @staticmethod
        def ValueOf(value: int) -> FacePlaneSelectionBuilder.TrimObjectType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def IsOk(self) -> bool:
        """
        Getter for property: (bool) IsOk
         Returnsthe data OK flag   
            
         
        """
        pass
    @IsOk.setter
    def IsOk(self, isOk: bool):
        """
        Setter for property: (bool) IsOk
         Returnsthe data OK flag   
            
         
        """
        pass
    @property
    def LimitTopolSwitchFinFlag(self) -> bool:
        """
        Getter for property: (bool) LimitTopolSwitchFinFlag
         Returns the limit edge switch fin flag   
            
         
        """
        pass
    @LimitTopolSwitchFinFlag.setter
    def LimitTopolSwitchFinFlag(self, switchFlag: bool):
        """
        Setter for property: (bool) LimitTopolSwitchFinFlag
         Returns the limit edge switch fin flag   
            
         
        """
        pass
    @property
    def PlaneHelpPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) PlaneHelpPoint
         Returnsthe user plane cap help point   
            
         
        """
        pass
    @PlaneHelpPoint.setter
    def PlaneHelpPoint(self, helpPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) PlaneHelpPoint
         Returnsthe user plane cap help point   
            
         
        """
        pass
    @property
    def SelectEdge(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SelectEdge
         Returns the select limit edge   
            
         
        """
        pass
    @property
    def SelectFace(self) -> FaceSetData:
        """
        Getter for property: ( FaceSetData NXOpen.Geome) SelectFace
         Returns the select face   
            
         
        """
        pass
    @property
    def SelectPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) SelectPlane
         Returns the select plane   
            
         
        """
        pass
    @SelectPlane.setter
    def SelectPlane(self, selectPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) SelectPlane
         Returns the select plane   
            
         
        """
        pass
    @property
    def TrimObject(self) -> FacePlaneSelectionBuilder.TrimObjectType:
        """
        Getter for property: ( FacePlaneSelectionBuilder.TrimObjectType NXOpen.Geome) TrimObject
         Returns the trim object   
            
         
        """
        pass
    @TrimObject.setter
    def TrimObject(self, trimObject: FacePlaneSelectionBuilder.TrimObjectType):
        """
        Setter for property: ( FacePlaneSelectionBuilder.TrimObjectType NXOpen.Geome) TrimObject
         Returns the trim object   
            
         
        """
        pass
    @property
    def UseFaceCapBlend(self) -> bool:
        """
        Getter for property: (bool) UseFaceCapBlend
         Returns the use face cap blend flag   
            
         
        """
        pass
    @UseFaceCapBlend.setter
    def UseFaceCapBlend(self, useFaceCapBlend: bool):
        """
        Setter for property: (bool) UseFaceCapBlend
         Returns the use face cap blend flag   
            
         
        """
        pass
    @property
    def UsePlaneCapBlend(self) -> bool:
        """
        Getter for property: (bool) UsePlaneCapBlend
         Returns the use plane cap blend   
            
         
        """
        pass
    @UsePlaneCapBlend.setter
    def UsePlaneCapBlend(self, usePlaneCapBlend: bool):
        """
        Setter for property: (bool) UsePlaneCapBlend
         Returns the use plane cap blend   
            
         
        """
        pass
import NXOpen
class FacePlaneToolBuilder(NXOpen.TaggedObject): 
    """ a sub-component of BooleanToolBuilder. It provides two basic tools
       creation methods i.e. collector sets of facesdatum planes, or a new plane 
       created on the fly. 
      """
    @property
    def ToolFaces(self) -> FaceSetData:
        """
        Getter for property: ( FaceSetData NXOpen.Geome) ToolFaces
         Returns the sets of tool faces or datum planes   
            
         
        """
        pass
    @property
    def ToolPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) ToolPlane
         Returns the new plane created on the fly.  
           Note: only one plane is getset   
         
        """
        pass
    @ToolPlane.setter
    def ToolPlane(self, toolPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) ToolPlane
         Returns the new plane created on the fly.  
           Note: only one plane is getset   
         
        """
        pass
import NXOpen
class FaceSetDataCollection(NXOpen.TaggedObjectCollection): 
    """ This class contains the factory methods for creating an FaceSetData. """
    def Create(self, m_face_collector: NXOpen.ScCollector, m_reverse_normal_flag: bool) -> FaceSetData:
        """
         Creates an FaceSetData. 
         Returns faceSetData ( FaceSetData NXOpen.Geome): .
        """
        pass
import NXOpen
class FaceSetData(NXOpen.NXObject): 
    """
    Represents a NXOpen.GeometricUtilities.FaceSetData
    """
    @property
    def FaceCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FaceCollector
         Returns the face set collector   
            
         
        """
        pass
    @property
    def ReverseNormalFlag(self) -> bool:
        """
        Getter for property: (bool) ReverseNormalFlag
         Returns the face set reverse direction flag   
            
         
        """
        pass
    @ReverseNormalFlag.setter
    def ReverseNormalFlag(self, mReverseNormalFlag: bool):
        """
        Setter for property: (bool) ReverseNormalFlag
         Returns the face set reverse direction flag   
            
         
        """
        pass
import NXOpen
class FaceSetOffsetCollection(NXOpen.TaggedObjectCollection): 
    """ This class contains the factory methods for creating an face set offset. """
    def CreateEmptyFaceSet(self) -> FaceSetOffset:
        """
         Creates an empty offset face set, with all parameters set to 0 or  
         Returns face_set ( FaceSetOffset NXOpen.Geome):  Resultant offset face set .
        """
        pass
    def CreateFaceSet(self, offset: str, face_collector: NXOpen.ScCollector, flip_value: bool, index: int) -> FaceSetOffset:
        """
         Creates an offset face set. 
         Returns face_set ( FaceSetOffset NXOpen.Geome):  Resultant offset face set .
        """
        pass
import NXOpen
class FaceSetOffsetList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[FaceSetOffset]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: FaceSetOffset) -> None:
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
    def Erase(self, obj: FaceSetOffset) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: FaceSetOffset, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: FaceSetOffset) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> FaceSetOffset:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( FaceSetOffset NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[FaceSetOffset]:
        """
         Gets the contents of the entire list 
         Returns objects ( FaceSetOffset List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: FaceSetOffset) -> None:
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
    def SetContents(self, objects: List[FaceSetOffset]) -> None:
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
    def Swap(self, object1: FaceSetOffset, object2: FaceSetOffset) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class FaceSetOffset(NXOpen.ExpressionCollectorSet): 
    """ This class represents a face set (collector) offset data. As the name indicates, it is a
       combination of a face collector and an offset distance.
     """
    @property
    def FaceCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FaceCollector
         Returns the face collector
                   
            
         
        """
        pass
    @FaceCollector.setter
    def FaceCollector(self, face_collector: NXOpen.ScCollector):
        """
        Setter for property: ( NXOpen.ScCollector) FaceCollector
         Returns the face collector
                   
            
         
        """
        pass
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Offset
         Returns the offset distance
                   
            
         
        """
        pass
    def FlipDirection(self) -> None:
        """
         Flip offset direction. This API flips the direction of offset keeping the offset distance same.
                 
        """
        pass
    def SetOffset(self, offset_value: str) -> None:
        """
         Sets the offset distance
                 
        """
        pass
import NXOpen
class FeatureOffset(NXOpen.TaggedObject): 
    """ Represents a Offset .
    """
    @property
    def EndOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndOffset
         Returns the End Offset
                  
            
         
        """
        pass
    @property
    def Option(self) -> Type:
        """
        Getter for property: ( Type NXOpen.Geome) Option
         Returns the Offset option
                  
            
         
        """
        pass
    @Option.setter
    def Option(self, offset_type: Type):
        """
        Setter for property: ( Type NXOpen.Geome) Option
         Returns the Offset option
                  
            
         
        """
        pass
    @property
    def StartOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartOffset
         Returns the Start Offset
                  
            
         
        """
        pass
    def SetEndOffset(self, value_expression: str) -> None:
        """
         The End Offset
                
        """
        pass
    def SetStartOffset(self, value_expression: str) -> None:
        """
         The Start Offset
                
        """
        pass
import NXOpen
class FeatureOptions(NXOpen.TaggedObject): 
    """ Represents various options supported on features. 
    """
    class BodyStyle(Enum):
        """
        Members Include: 
         |Solid|  Solid Body 
         |Sheet|  Sheet Body 

        """
        Solid: int
        Sheet: int
        @staticmethod
        def ValueOf(value: int) -> FeatureOptions.BodyStyle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BodyType(self) -> FeatureOptions.BodyStyle:
        """
        Getter for property: ( FeatureOptions.BodyStyle NXOpen.Geome) BodyType
         Returns the body type 
                  
            
         
        """
        pass
    @BodyType.setter
    def BodyType(self, type: FeatureOptions.BodyStyle):
        """
        Setter for property: ( FeatureOptions.BodyStyle NXOpen.Geome) BodyType
         Returns the body type 
                  
            
         
        """
        pass
import NXOpen
class FlowDirection(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.GeometricUtilities.FlowDirection
    Allows user to specify different flow direction to control output surface shape.
    """
    class Type(Enum):
        """
        Members Include: 
         |NotSpecified|  Not Specified 
         |Isoparametric|  Iso Parametric 
         |IsoCurveU|  Iso Curve U 
         |IsoCurveV|  Iso Curve V 
         |Perpendicular|  Perpendicular 
         |AdjacentEdges|  Adjacent Edges 

        """
        NotSpecified: int
        Isoparametric: int
        IsoCurveU: int
        IsoCurveV: int
        Perpendicular: int
        AdjacentEdges: int
        @staticmethod
        def ValueOf(value: int) -> FlowDirection.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FlowDirectionType(self) -> FlowDirection.Type:
        """
        Getter for property: ( FlowDirection.Type NXOpen.Geome) FlowDirectionType
         Returns the flow direction type.  
          
                  
         
        """
        pass
    @FlowDirectionType.setter
    def FlowDirectionType(self, flowDirectionType: FlowDirection.Type):
        """
        Setter for property: ( FlowDirection.Type NXOpen.Geome) FlowDirectionType
         Returns the flow direction type.  
          
                  
         
        """
        pass
import NXOpen
class FrameOnPathBuilder(NXOpen.TaggedObject): 
    """ Frame on path builder """
    class AnchorLocationType(Enum):
        """
        Members Include: 
         |Center|  Center position 
         |Right|  Right position 
         |Left|  Left position 

        """
        Center: int
        Right: int
        Left: int
        @staticmethod
        def ValueOf(value: int) -> FrameOnPathBuilder.AnchorLocationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AnchorLocation(self) -> FrameOnPathBuilder.AnchorLocationType:
        """
        Getter for property: ( FrameOnPathBuilder.AnchorLocationType NXOpen.Geome) AnchorLocation
         Returns the anchor location   
            
         
        """
        pass
    @AnchorLocation.setter
    def AnchorLocation(self, anchorLocation: FrameOnPathBuilder.AnchorLocationType):
        """
        Setter for property: ( FrameOnPathBuilder.AnchorLocationType NXOpen.Geome) AnchorLocation
         Returns the anchor location   
            
         
        """
        pass
    @property
    def AnchorPosition(self) -> OnPathDimensionBuilder:
        """
        Getter for property: ( OnPathDimensionBuilder NXOpen.Geome) AnchorPosition
         Returns the anchor position   
            
         
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
    def IsApexReversed(self) -> bool:
        """
        Getter for property: (bool) IsApexReversed
         Returns the value indicating if apex point is reversed   
            
         
        """
        pass
    @IsApexReversed.setter
    def IsApexReversed(self, isReversed: bool):
        """
        Setter for property: (bool) IsApexReversed
         Returns the value indicating if apex point is reversed   
            
         
        """
        pass
    @property
    def Length(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Length
         Returns the length   
            
         
        """
        pass
    @property
    def LockAspectRatio(self) -> bool:
        """
        Getter for property: (bool) LockAspectRatio
         Returns a flag indicating if aspect ratio is locked   
            
         
        """
        pass
    @LockAspectRatio.setter
    def LockAspectRatio(self, lockAspectRatio: bool):
        """
        Setter for property: (bool) LockAspectRatio
         Returns a flag indicating if aspect ratio is locked   
            
         
        """
        pass
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Offset
         Returns the offset   
            
         
        """
        pass
    @property
    def WScale(self) -> float:
        """
        Getter for property: (float) WScale
         Returns the width scale   
            
         
        """
        pass
    @WScale.setter
    def WScale(self, wScale: float):
        """
        Setter for property: (float) WScale
         Returns the width scale   
            
         
        """
        pass
import NXOpen
class FtmFixedCurvesBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[FtmFixedCurvesBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: FtmFixedCurvesBuilder) -> None:
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
    def Erase(self, obj: FtmFixedCurvesBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: FtmFixedCurvesBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: FtmFixedCurvesBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> FtmFixedCurvesBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( FtmFixedCurvesBuilder NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[FtmFixedCurvesBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( FtmFixedCurvesBuilder List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: FtmFixedCurvesBuilder) -> None:
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
    def SetContents(self, objects: List[FtmFixedCurvesBuilder]) -> None:
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
    def Swap(self, object1: FtmFixedCurvesBuilder, object2: FtmFixedCurvesBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class FtmFixedCurvesBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.GeometricUtilities.FtmFixedCurvesBuilder builder
    """
    class FixedCurvesContinuityType(Enum):
        """
        Members Include: 
         |G0|  G0 position 
         |G1|  G1 Tangent 
         |G2|  G2 Curvature 
         |G3|  G3 Continuity 
         |G4|  G4 Continuity 

        """
        G0: int
        G1: int
        G2: int
        G3: int
        G4: int
        @staticmethod
        def ValueOf(value: int) -> FtmFixedCurvesBuilder.FixedCurvesContinuityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FixedCurves(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) FixedCurves
         Returns the fixed curves that define the fixed constraints on the product shape   
            
         
        """
        pass
    @property
    def FixedCurvesContinuity(self) -> FtmFixedCurvesBuilder.FixedCurvesContinuityType:
        """
        Getter for property: ( FtmFixedCurvesBuilder.FixedCurvesContinuityType NXOpen.Geome) FixedCurvesContinuity
         Returns the continuity option for the fixed curves used in the transformation or morphing calculations    
            
         
        """
        pass
    @FixedCurvesContinuity.setter
    def FixedCurvesContinuity(self, fixedCurvesContinuity: FtmFixedCurvesBuilder.FixedCurvesContinuityType):
        """
        Setter for property: ( FtmFixedCurvesBuilder.FixedCurvesContinuityType NXOpen.Geome) FixedCurvesContinuity
         Returns the continuity option for the fixed curves used in the transformation or morphing calculations    
            
         
        """
        pass
    def UpdateContinuityOnClassAChange(self, classAOption: bool) -> None:
        """
         Update continuity when Class A option changes  
        """
        pass
import NXOpen
class FtmTransformCurvesBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[FtmTransformCurvesBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: FtmTransformCurvesBuilder) -> None:
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
    def Erase(self, obj: FtmTransformCurvesBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: FtmTransformCurvesBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: FtmTransformCurvesBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> FtmTransformCurvesBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( FtmTransformCurvesBuilder NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[FtmTransformCurvesBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( FtmTransformCurvesBuilder List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: FtmTransformCurvesBuilder) -> None:
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
    def SetContents(self, objects: List[FtmTransformCurvesBuilder]) -> None:
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
    def Swap(self, object1: FtmTransformCurvesBuilder, object2: FtmTransformCurvesBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class FtmTransformCurvesBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.GeometricUtilities.FtmTransformCurvesBuilder builder
    """
    class TransformCurvesContinuityType(Enum):
        """
        Members Include: 
         |G0| 
         |G1| 
         |G2| 

        """
        G0: int
        G1: int
        G2: int
        @staticmethod
        def ValueOf(value: int) -> FtmTransformCurvesBuilder.TransformCurvesContinuityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AlignBreakPoints(self) -> bool:
        """
        Getter for property: (bool) AlignBreakPoints
         Returns the option for aligning break points used in the transformation or morphing calculations   
            
         
        """
        pass
    @AlignBreakPoints.setter
    def AlignBreakPoints(self, alignBreakPoints: bool):
        """
        Setter for property: (bool) AlignBreakPoints
         Returns the option for aligning break points used in the transformation or morphing calculations   
            
         
        """
        pass
    @property
    def OppositeSense(self) -> bool:
        """
        Getter for property: (bool) OppositeSense
         Returns the option to reverse the OmniCAD pre-determined direction for the transformation start and end curves   
            
         
        """
        pass
    @OppositeSense.setter
    def OppositeSense(self, oppositeSense: bool):
        """
        Setter for property: (bool) OppositeSense
         Returns the option to reverse the OmniCAD pre-determined direction for the transformation start and end curves   
            
         
        """
        pass
    @property
    def OppositeSide(self) -> bool:
        """
        Getter for property: (bool) OppositeSide
         Returns the option to change the displacements to the opposite side of the transformation   
            
         
        """
        pass
    @OppositeSide.setter
    def OppositeSide(self, oppositeSide: bool):
        """
        Setter for property: (bool) OppositeSide
         Returns the option to change the displacements to the opposite side of the transformation   
            
         
        """
        pass
    @property
    def TransformCurvesContinuity(self) -> FtmTransformCurvesBuilder.TransformCurvesContinuityType:
        """
        Getter for property: ( FtmTransformCurvesBuilder.TransformCurvesContinuityType NXOpen.Geome) TransformCurvesContinuity
         Returns the continuity option for the transformation start and end curves used in the transformation or morphing calculations   
            
         
        """
        pass
    @TransformCurvesContinuity.setter
    def TransformCurvesContinuity(self, transformCurvesContinuity: FtmTransformCurvesBuilder.TransformCurvesContinuityType):
        """
        Setter for property: ( FtmTransformCurvesBuilder.TransformCurvesContinuityType NXOpen.Geome) TransformCurvesContinuity
         Returns the continuity option for the transformation start and end curves used in the transformation or morphing calculations   
            
         
        """
        pass
    @property
    def TransformCurvesMagnitude(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TransformCurvesMagnitude
         Returns the magnitude controlled by continuity for the transformation curves   
            
         
        """
        pass
    @property
    def TransformEndCurves(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) TransformEndCurves
         Returns the end or target constraint for the product shape in the form of curves used in the transformation or morphing calculations   
            
         
        """
        pass
    @property
    def TransformStartCurves(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) TransformStartCurves
         Returns the starting constraint for the product shape in the form of curves used in the transformation or morphing calculations   
            
         
        """
        pass
import NXOpen
class FtmTransformPointsBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[FtmTransformPointsBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: FtmTransformPointsBuilder) -> None:
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
    def Erase(self, obj: FtmTransformPointsBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: FtmTransformPointsBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: FtmTransformPointsBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> FtmTransformPointsBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( FtmTransformPointsBuilder NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[FtmTransformPointsBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( FtmTransformPointsBuilder List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: FtmTransformPointsBuilder) -> None:
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
    def SetContents(self, objects: List[FtmTransformPointsBuilder]) -> None:
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
    def Swap(self, object1: FtmTransformPointsBuilder, object2: FtmTransformPointsBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class FtmTransformPointsBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.GeometricUtilities.FtmTransformPointsBuilder builder
    """
    @property
    def TransformEndPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) TransformEndPoint
         Returns the end point that defines the end or target point constraint on the product shape   
            
         
        """
        pass
    @TransformEndPoint.setter
    def TransformEndPoint(self, transformEndPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) TransformEndPoint
         Returns the end point that defines the end or target point constraint on the product shape   
            
         
        """
        pass
    @property
    def TransformStartPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) TransformStartPoint
         Returns the start point that defines the starting point constraint on the product shape   
            
         
        """
        pass
    @TransformStartPoint.setter
    def TransformStartPoint(self, transformStartPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) TransformStartPoint
         Returns the start point that defines the starting point constraint on the product shape   
            
         
        """
        pass
import NXOpen
class GeneralPattern(NXOpen.TaggedObject): 
    """ the General pattern definition.  """
    class FromLocationOptions(Enum):
        """
        Members Include: 
         |Point|  point 
         |Csys|  csys 

        """
        Point: int
        Csys: int
        @staticmethod
        def ValueOf(value: int) -> GeneralPattern.FromLocationOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FromLocationCsys2d(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) FromLocationCsys2d
         Returns the from location 2d csys   
            
         
        """
        pass
    @property
    def FromLocationCsys3d(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) FromLocationCsys3d
         Returns the from location 3d csys   
            
         
        """
        pass
    @FromLocationCsys3d.setter
    def FromLocationCsys3d(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) FromLocationCsys3d
         Returns the from location 3d csys   
            
         
        """
        pass
    @property
    def FromLocationPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) FromLocationPoint
         Returns the from location point   
            
         
        """
        pass
    @FromLocationPoint.setter
    def FromLocationPoint(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) FromLocationPoint
         Returns the from location point   
            
         
        """
        pass
    @property
    def FromLocationType(self) -> GeneralPattern.FromLocationOptions:
        """
        Getter for property: ( GeneralPattern.FromLocationOptions NXOpen.Geome) FromLocationType
         Returns the from location type   
            
         
        """
        pass
    @FromLocationType.setter
    def FromLocationType(self, fromLocationType: GeneralPattern.FromLocationOptions):
        """
        Setter for property: ( GeneralPattern.FromLocationOptions NXOpen.Geome) FromLocationType
         Returns the from location type   
            
         
        """
        pass
    @property
    def ToCsysList(self) -> NXOpen.SelectCoordinateSystemList:
        """
        Getter for property: ( NXOpen.SelectCoordinateSystemList) ToCsysList
         Returns the to csys list    
            
         
        """
        pass
    @property
    def ToPoints(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) ToPoints
         Returns the to points    
            
         
        """
        pass
import NXOpen
class GeometryLocationDataCollection(NXOpen.TaggedObjectCollection): 
    """ This class contains the factory methods for creating GeometryLocationData. """
    def CreateGeometryLocationData(self) -> GeometryLocationData:
        """
         Creates geometry location data. 
         Returns newGeometryLocationData ( GeometryLocationData NXOpen.Geome):  Resultant geometry location data .
        """
        pass
import NXOpen
class GeometryLocationData(NXOpen.TaggedObject): 
    """ Represents a NXOpen.GeometricUtilities.GeometryLocationData
    """
    class EntityTypes(Enum):
        """
        Members Include: 
         |Point| 
         |Csys| 

        """
        Point: int
        Csys: int
        @staticmethod
        def ValueOf(value: int) -> GeometryLocationData.EntityTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Csys(self) -> NXOpen.SelectObject:
        """
        Getter for property: ( NXOpen.SelectObject) Csys
         Returns the csys   
            
         
        """
        pass
    @property
    def EntityType(self) -> GeometryLocationData.EntityTypes:
        """
        Getter for property: ( GeometryLocationData.EntityTypes NXOpen.Geome) EntityType
         Returns the type   
            
         
        """
        pass
    @EntityType.setter
    def EntityType(self, entityType: GeometryLocationData.EntityTypes):
        """
        Setter for property: ( GeometryLocationData.EntityTypes NXOpen.Geome) EntityType
         Returns the type   
            
         
        """
        pass
    @property
    def Point(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Point
         Returns the point   
            
         
        """
        pass
    @Point.setter
    def Point(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Point
         Returns the point   
            
         
        """
        pass
import NXOpen
class HelixPattern(NXOpen.TaggedObject): 
    """ the Helix pattern definition.  Allows specification along
        both the angular and radial directions. """
    class DirectionTypes(Enum):
        """
        Members Include: 
         |Righthand|  Right hand orientation. 
         |Lefthand|  Left hand orientation. 

        """
        Righthand: int
        Lefthand: int
        @staticmethod
        def ValueOf(value: int) -> HelixPattern.DirectionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SizeOptions(Enum):
        """
        Members Include: 
         |CountAngleDistance|  use Count, Angle, Distance to define a Helix 
         |CountHelixPitchAndTurns|  use Count, Helix Pitch, Turns to define a Helix 
         |CountHelixPitchAndSpan|  use Count, Helix Pitch, Span to define a Helix 
         |AngleHelixPitchAndTurns|  use Angle, Helix Pitch, Turns to define a Helix 
         |AngleHelixPitchAndSpan|  use Angle, Helix Pitch, Span to define a Helix 

        """
        CountAngleDistance: int
        CountHelixPitchAndTurns: int
        CountHelixPitchAndSpan: int
        AngleHelixPitchAndTurns: int
        AngleHelixPitchAndSpan: int
        @staticmethod
        def ValueOf(value: int) -> HelixPattern.SizeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AnglePitch(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) AnglePitch
         Returns the angle pitch expression for the Helix type pattern   
            
         
        """
        pass
    @property
    def CountOfInstances(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CountOfInstances
         Returns the count of instances for the Helix type pattern   
            
         
        """
        pass
    @property
    def DirectionType(self) -> HelixPattern.DirectionTypes:
        """
        Getter for property: ( HelixPattern.DirectionTypes NXOpen.Geome) DirectionType
         Returns the type of helix direction method   
            
         
        """
        pass
    @DirectionType.setter
    def DirectionType(self, directionType: HelixPattern.DirectionTypes):
        """
        Setter for property: ( HelixPattern.DirectionTypes NXOpen.Geome) DirectionType
         Returns the type of helix direction method   
            
         
        """
        pass
    @property
    def DistancePitch(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DistancePitch
         Returns the distance pitch expression for the Helix type pattern   
            
         
        """
        pass
    @property
    def HelixPitch(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) HelixPitch
         Returns the helix pitch expression for the Helix type pattern   
            
         
        """
        pass
    @property
    def HelixSpan(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) HelixSpan
         Returns the helix span expression for the Helix type pattern   
            
         
        """
        pass
    @property
    def NumberOfTurns(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NumberOfTurns
         Returns the number of turns for the Helix type pattern   
            
         
        """
        pass
    @property
    def RotationAxis(self) -> NXOpen.Axis:
        """
        Getter for property: ( NXOpen.Axis) RotationAxis
         Returns the rotation axis for the pattern.  
             
         
        """
        pass
    @RotationAxis.setter
    def RotationAxis(self, rotationAxis: NXOpen.Axis):
        """
        Setter for property: ( NXOpen.Axis) RotationAxis
         Returns the rotation axis for the pattern.  
             
         
        """
        pass
    @property
    def SizeOption(self) -> HelixPattern.SizeOptions:
        """
        Getter for property: ( HelixPattern.SizeOptions NXOpen.Geome) SizeOption
         Returns the Helix size option   
            
         
        """
        pass
    @SizeOption.setter
    def SizeOption(self, option: HelixPattern.SizeOptions):
        """
        Setter for property: ( HelixPattern.SizeOptions NXOpen.Geome) SizeOption
         Returns the Helix size option   
            
         
        """
        pass
import NXOpen
class HorizontalReference(NXOpen.TaggedObject): 
    """ the horizontal reference vector definition.  """
    @property
    def Flip(self) -> bool:
        """
        Getter for property: (bool) Flip
         Returns the 2D Selection flip attribute.  
           This function flips the selection object of the 2D pattern   
         
        """
        pass
    @Flip.setter
    def Flip(self, flip: bool):
        """
        Setter for property: (bool) Flip
         Returns the 2D Selection flip attribute.  
           This function flips the selection object of the 2D pattern   
         
        """
        pass
    @property
    def HorizontalRefObject(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) HorizontalRefObject
         Returns the direction object.  
           This function gets reference vector of the 2D pattern. This call will result in an Exception if not called in 2D mode.   
         
        """
        pass
    @property
    def HorizontalRefVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) HorizontalRefVector
         Returns the horizontal reference vector   
            
         
        """
        pass
    @HorizontalRefVector.setter
    def HorizontalRefVector(self, horizontalRefVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) HorizontalRefVector
         Returns the horizontal reference vector   
            
         
        """
        pass
    @property
    def RotationAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RotationAngle
         Returns the rotation angle wrt horizontal reference direction   
            
         
        """
        pass
import NXOpen
class IComponentBuilder(NXOpen.Object): 
    """ Represents a component contained in a builder
    """
    @abstractmethod
    def Validate(self) -> bool:
        """
         Validate whether the inputs to the component are sufficient for 
                    commit to be called.  If the component is not in a state to commit
                    then an exception is thrown.  For example, if the component requires
                    you to set some property, this method will throw an exception if
                    you haven't set it.  This method throws a not yet implemented
                    NXException for some components.
                
         Returns result (bool):  Was self validation successful .
        """
        pass
import NXOpen
class InstanceEditedExpressionItemList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[InstanceEditedExpressionItem]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: InstanceEditedExpressionItem) -> None:
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
    def Erase(self, obj: InstanceEditedExpressionItem) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: InstanceEditedExpressionItem, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: InstanceEditedExpressionItem) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> InstanceEditedExpressionItem:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( InstanceEditedExpressionItem NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[InstanceEditedExpressionItem]:
        """
         Gets the contents of the entire list 
         Returns objects ( InstanceEditedExpressionItem List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: InstanceEditedExpressionItem) -> None:
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
    def SetContents(self, objects: List[InstanceEditedExpressionItem]) -> None:
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
    def Swap(self, object1: InstanceEditedExpressionItem, object2: InstanceEditedExpressionItem) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class InstanceEditedExpressionItem(NXOpen.TaggedObject): 
    """ edited value of one master expression of the input object(s) being patterned. """
    @property
    def MasterExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MasterExpression
         Returns the master expression   
            
         
        """
        pass
    @property
    def ValueExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ValueExpression
         Returns the edited value expression for the master expression   
            
         
        """
        pass
import NXOpen
class InstanceEditedExpressionsList(NXOpen.TaggedObject): 
    """ list of NXOpen.GeometricUtilities.InstanceEditedExpressionItem objects. """
    @property
    def List(self) -> InstanceEditedExpressionItemList:
        """
        Getter for property: ( InstanceEditedExpressionItemList NXOpen.Geome) List
         Returns the list of  NXOpen::GeometricUtilities::InstanceEditedExpressionItem  objects.  
             
         
        """
        pass
    @overload
    def EditInstanceExpression(self) -> InstanceEditedExpressionItem:
        """
         This is the default creator for NXOpen.GeometricUtilities.InstanceEditedExpressionItem. 
         Returns editedExpItem ( InstanceEditedExpressionItem NXOpen.Geome): .
        """
        pass
    @overload
    def EditInstanceExpression(self, masterExpression: NXOpen.Expression, instanceExpression: NXOpen.Expression) -> InstanceEditedExpressionItem:
        """
         This is the creator for NXOpen.GeometricUtilities.InstanceEditedExpressionItem which should be used. 
         Returns editedExpItem ( InstanceEditedExpressionItem NXOpen.Geome): .
        """
        pass
import NXOpen
class InteractiveSectionBuilder(NXOpen.TaggedObject): 
    """ Represents a NXOpen.GeometricUtilities.InteractiveSectionBuilder.
        The interactive section block uses 2 points to draw a line or a section."""
    def AppendPlane(self, point1: NXOpen.Point3d, point2: NXOpen.Point3d, origin: NXOpen.Point3d, normal: NXOpen.Vector3d) -> None:
        """
         Appends a plane 
        """
        pass
    def DeleteLast(self) -> None:
        """
         Deletes last point or the plane created
        """
        pass
    def GetNthPlane(self, index: int) -> SectionPlaneData:
        """
         Get the Nth plane 
         Returns plane ( SectionPlaneData NXOpen.Geome):  plane found at index.
        """
        pass
    def GetNumPlanes(self) -> int:
        """
         Get the number of planes 
         Returns num (int):  number of planes .
        """
        pass
import NXOpen
class LatticeItemBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[LatticeItemBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: LatticeItemBuilder) -> None:
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
    def Erase(self, obj: LatticeItemBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: LatticeItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: LatticeItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> LatticeItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( LatticeItemBuilder NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[LatticeItemBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( LatticeItemBuilder List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: LatticeItemBuilder) -> None:
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
    def SetContents(self, objects: List[LatticeItemBuilder]) -> None:
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
    def Swap(self, object1: LatticeItemBuilder, object2: LatticeItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class LatticeItemBuilder(NXOpen.TaggedObject): 
    """ This object contains each 3MF export option within the LatticeItemList. """
    class ClippingModeTypes(Enum):
        """
        Members Include: 
         |NotSet| 
         |Inside| 
         |Outside| 

        """
        NotSet: int
        Inside: int
        Outside: int
        @staticmethod
        def ValueOf(value: int) -> LatticeItemBuilder.ClippingModeTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ExportTypes(Enum):
        """
        Members Include: 
         |GraphOnly| 
         |GraphandBody| 

        """
        GraphOnly: int
        GraphandBody: int
        @staticmethod
        def ValueOf(value: int) -> LatticeItemBuilder.ExportTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ClippingBody(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: ( NXOpen.SelectBodyList) ClippingBody
         Returns   The body being clipped with 3MF Export.  
            
            
         
        """
        pass
    @property
    def ClippingMode(self) -> LatticeItemBuilder.ClippingModeTypes:
        """
        Getter for property: ( LatticeItemBuilder.ClippingModeTypes NXOpen.Geome) ClippingMode
         Returns   The clipping mode option for the lattice body in 3MF export.  
           Can be none, inside or outside.  
           
         
        """
        pass
    @ClippingMode.setter
    def ClippingMode(self, clippingMode: LatticeItemBuilder.ClippingModeTypes):
        """
        Setter for property: ( LatticeItemBuilder.ClippingModeTypes NXOpen.Geome) ClippingMode
         Returns   The clipping mode option for the lattice body in 3MF export.  
           Can be none, inside or outside.  
           
         
        """
        pass
    @property
    def ExportMode(self) -> LatticeItemBuilder.ExportTypes:
        """
        Getter for property: ( LatticeItemBuilder.ExportTypes NXOpen.Geome) ExportMode
         Returns    The export mode for the lattice body in 3MF export.  
           Can be graph or graph and body.  
            
         
        """
        pass
    @ExportMode.setter
    def ExportMode(self, exportMode: LatticeItemBuilder.ExportTypes):
        """
        Setter for property: ( LatticeItemBuilder.ExportTypes NXOpen.Geome) ExportMode
         Returns    The export mode for the lattice body in 3MF export.  
           Can be graph or graph and body.  
            
         
        """
        pass
    @property
    def LatticeBodies(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: ( NXOpen.SelectBodyList) LatticeBodies
         Returns   This object contains the lattice bodies within the list  
          
          
            
         
        """
        pass
    def Destroy(self) -> None:
        """
         Destroys this GeometricUtilities.LatticeItemBuilder 
        """
        pass
import NXOpen
class LatticeItemListBuilder(NXOpen.TaggedObject): 
    """ Represents a LatticeItemList """
    @property
    def LatticeItemList(self) -> LatticeItemBuilderList:
        """
        Getter for property: ( LatticeItemBuilderList NXOpen.Geome) LatticeItemList
         Returns the section defining the lattice body options.  
             
         
        """
        pass
    def CreateLatticeItemBuilder(self) -> LatticeItemBuilder:
        """
         Creates a GeometricUtilities.LatticeItemBuilder 
         Returns builder ( LatticeItemBuilder NXOpen.Geome): .
        """
        pass
import NXOpen
class LawBuilder(NXOpen.TaggedObject): 
    """ Represents a LawBuilder """
    class RetainLawCurveOption(Enum):
        """
        Members Include: 
         |KeepOriginal|  Keeps the original profile as it is during edit pre NX3 parms 
         |Replace|  Deletes the old profile, so that user has to select new one during edit pre NX3 parms 

        """
        KeepOriginal: int
        Replace: int
        @staticmethod
        def ValueOf(value: int) -> LawBuilder.RetainLawCurveOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Type(Enum):
        """
        Members Include: 
         |Constant|  constant law type
         |Linear|  linear law type 
         |Cubic|  cubic law type  
         |LinearAlongSpine|  linear along spine law type  
         |CubicAlongSpine|  cubic along spine law type  
         |ByEquation|  by equation law type  
         |ByLawCurve|  by law curve law type  
         |MultiTransition|  multi-transition law type 
         |NonInflecting|  non-inflecting law type 
         |SShaped|  S-shaped law type 

        """
        Constant: int
        Linear: int
        Cubic: int
        LinearAlongSpine: int
        CubicAlongSpine: int
        ByEquation: int
        ByLawCurve: int
        MultiTransition: int
        NonInflecting: int
        SShaped: int
        @staticmethod
        def ValueOf(value: int) -> LawBuilder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AlongSpineData(self) -> AlongSpineBuilder:
        """
        Getter for property: ( AlongSpineBuilder NXOpen.Geome) AlongSpineData
         Returns the linear or cubic along spine law.  
           This will be used only when the law type is linear along spinecubic along spine   
         
        """
        pass
    @property
    def BaseLine(self) -> NXOpen.SelectLine:
        """
        Getter for property: ( NXOpen.SelectLine) BaseLine
         Returns the base line.  
           This will be used only when the law type is by law curve   
         
        """
        pass
    @property
    def EndValue(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndValue
         Returns the end value.  
           This will be used only when the law type is linearcubic   
         
        """
        pass
    @property
    def Function(self) -> str:
        """
        Getter for property: (str) Function
         Returns the function.  
           This will be used only when the law type is by equation. 
                Make sure that the expression should be created before setting it in to the builder   
         
        """
        pass
    @Function.setter
    def Function(self, function: str):
        """
        Setter for property: (str) Function
         Returns the function.  
           This will be used only when the law type is by equation. 
                Make sure that the expression should be created before setting it in to the builder   
         
        """
        pass
    @property
    def IsSimpleCubicAlongSpine(self) -> bool:
        """
        Getter for property: (bool) IsSimpleCubicAlongSpine
         Returns a value indicating if  NXOpen::GeometricUtilities::LawBuilder::TypeCubicAlongSpine  is using simple cubic interpolation.  
          
                    Simple cubic interpolation minimizes enforcement of automatic tangent constraints at the defining points. This option is valid only
                    when  NXOpen::GeometricUtilities::LawBuilder::Type  is  NXOpen::GeometricUtilities::LawBuilder::TypeCubicAlongSpine    
         
        """
        pass
    @IsSimpleCubicAlongSpine.setter
    def IsSimpleCubicAlongSpine(self, isSimpleCubic: bool):
        """
        Setter for property: (bool) IsSimpleCubicAlongSpine
         Returns a value indicating if  NXOpen::GeometricUtilities::LawBuilder::TypeCubicAlongSpine  is using simple cubic interpolation.  
          
                    Simple cubic interpolation minimizes enforcement of automatic tangent constraints at the defining points. This option is valid only
                    when  NXOpen::GeometricUtilities::LawBuilder::Type  is  NXOpen::GeometricUtilities::LawBuilder::TypeCubicAlongSpine    
         
        """
        pass
    @property
    def LawCurve(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) LawCurve
         Returns the law curve.  
           This will be used only when the law type is by law curve   
         
        """
        pass
    @property
    def LawCurveOption(self) -> LawBuilder.RetainLawCurveOption:
        """
        Getter for property: ( LawBuilder.RetainLawCurveOption NXOpen.Geome) LawCurveOption
         Returns the option to retain law curve.  
            This will be used only during the edit of Pre NX3 feature Parms   
         
        """
        pass
    @LawCurveOption.setter
    def LawCurveOption(self, lawCurveOption: LawBuilder.RetainLawCurveOption):
        """
        Setter for property: ( LawBuilder.RetainLawCurveOption NXOpen.Geome) LawCurveOption
         Returns the option to retain law curve.  
            This will be used only during the edit of Pre NX3 feature Parms   
         
        """
        pass
    @property
    def LawType(self) -> LawBuilder.Type:
        """
        Getter for property: ( LawBuilder.Type NXOpen.Geome) LawType
         Returns the law type   
            
         
        """
        pass
    @LawType.setter
    def LawType(self, lawType: LawBuilder.Type):
        """
        Setter for property: ( LawBuilder.Type NXOpen.Geome) LawType
         Returns the law type   
            
         
        """
        pass
    @property
    def MultiTransitionLaw(self) -> MultiTransitionLawBuilder:
        """
        Getter for property: ( MultiTransitionLawBuilder NXOpen.Geome) MultiTransitionLaw
         Returns the multi transition law.  
           This will be used only when the law type is multi transition law   
         
        """
        pass
    @property
    def NonInflectingLaw(self) -> NonInflectingLawBuilder:
        """
        Getter for property: ( NonInflectingLawBuilder NXOpen.Geome) NonInflectingLaw
         Returns the non inflecting law.  
           This will be used only when the law type is non inflecting law   
         
        """
        pass
    @property
    def Parameter(self) -> str:
        """
        Getter for property: (str) Parameter
         Returns the parameter.  
           This will be used only when the law type is by equation. 
                Make sure that the expression should be created before setting it in to the builder   
         
        """
        pass
    @Parameter.setter
    def Parameter(self, parameter: str):
        """
        Setter for property: (str) Parameter
         Returns the parameter.  
           This will be used only when the law type is by equation. 
                Make sure that the expression should be created before setting it in to the builder   
         
        """
        pass
    @property
    def ReverseDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseDirection
         Returns the reverse direction.  
           This will be used only when the law type is by law curve   
         
        """
        pass
    @ReverseDirection.setter
    def ReverseDirection(self, reverseDirection: bool):
        """
        Setter for property: (bool) ReverseDirection
         Returns the reverse direction.  
           This will be used only when the law type is by law curve   
         
        """
        pass
    @property
    def SShapedLaw(self) -> SShapedLawBuilder:
        """
        Getter for property: ( SShapedLawBuilder NXOpen.Geome) SShapedLaw
         Returns the s-shaped law.  
           This will be used only when the law type is s-shaped law   
         
        """
        pass
    @property
    def StartValue(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartValue
         Returns the start value.  
           This will be used only when the law type is linearcubic   
         
        """
        pass
    @property
    def Value(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Value
         Returns the constant value.  
           This will be used only when the law type is constant   
         
        """
        pass
    def SetSpineIntoBuilder(self, spine: NXOpen.Section) -> None:
        """
         Sets the spine dynamically into builder 
        """
        pass
import NXOpen
class LengthLimitPointBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.GeometricUtilities.LengthLimitPointBuilder
    """
    @property
    def OnPathDim(self) -> OnPathDimensionBuilder:
        """
        Getter for property: ( OnPathDimensionBuilder NXOpen.Geome) OnPathDim
         Returns the  NXOpen::GeometricUtilities::LengthLimitPointBuilder  subobject.  
             
         
        """
        pass
    def Destroy(self) -> None:
        """
         Destructor for NXOpen.GeometricUtilities.LengthLimitPointBuilder 
        """
        pass
    def FlipPath(self, isStartOfEdge: bool) -> None:
        """
         Flip the builder path for NXOpen.GeometricUtilities.LengthLimitPointBuilder 
        """
        pass
import NXOpen
class LengthLimitsListBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.GeometricUtilities.LengthLimitsListBuilder
    """
    @property
    def CapsList(self) -> PointFacePlaneSelectionBuilderList:
        """
        Getter for property: ( PointFacePlaneSelectionBuilderList NXOpen.Geome) CapsList
         Returns the list of lenght limit data objects  
            
         
        """
        pass
    def CreatePointFacePlaneSelectionBuilder(self, seed: NXOpen.TaggedObject) -> PointFacePlaneSelectionBuilder:
        """
         Creates a FacePlaneSelectionBuilder
         Returns builder ( PointFacePlaneSelectionBuilder NXOpen.Geome): PointFacePlaneSelectionBuilder object .
        """
        pass
    def DestroyPointFacePlaneSelectionBuilder(self, entityBuilderData: PointFacePlaneSelectionBuilder) -> None:
        """
         Destroys a FacePlaneSelectionBuilder
        """
        pass
import NXOpen
class Limits(NXOpen.TaggedObject): 
    """ Represents a limits data. Inputs to this class can be convergent objects.
    """
    @property
    def EndExtend(self) -> Extend:
        """
        Getter for property: ( Extend NXOpen.Geome) EndExtend
         Returns the end extend builder 
                  
            
         
        """
        pass
    @property
    def StartExtend(self) -> Extend:
        """
        Getter for property: ( Extend NXOpen.Geome) StartExtend
         Returns the start extend builder 
                  
            
         
        """
        pass
    @property
    def SymmetricOption(self) -> bool:
        """
        Getter for property: (bool) SymmetricOption
         Returns the symmetric option
                  
            
         
        """
        pass
    @SymmetricOption.setter
    def SymmetricOption(self, symmetric_option: bool):
        """
        Setter for property: (bool) SymmetricOption
         Returns the symmetric option
                  
            
         
        """
        pass
class LinearLimits(Limits): 
    """ Represents a limits data. 
    """
    pass
import NXOpen
import NXOpen.Features
class LocalUntrimBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.GeometricUtilities.LocalUntrimBuilder builder. This builder is used to untrim and extend a sheet. """
    @property
    def EdgeCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) EdgeCollector
         Returns the edges on the face to delete.  
            
         
        """
        pass
    @property
    def EditCopy(self) -> bool:
        """
        Getter for property: (bool) EditCopy
         Returns the flag to indicate whether to edit a copied face or not.  
            
         
        """
        pass
    @EditCopy.setter
    def EditCopy(self, editCopy: bool):
        """
        Setter for property: (bool) EditCopy
         Returns the flag to indicate whether to edit a copied face or not.  
            
         
        """
        pass
    @property
    def Face(self) -> NXOpen.SelectFace:
        """
        Getter for property: ( NXOpen.SelectFace) Face
         Returns the tool object to split the target body.  
             
         
        """
        pass
    @property
    def RemoveBoundary(self) -> bool:
        """
        Getter for property: (bool) RemoveBoundary
         Returns the flag to indicate whether to remove the face boundary or not.  
            
         
        """
        pass
    @RemoveBoundary.setter
    def RemoveBoundary(self, removeBoundary: bool):
        """
        Setter for property: (bool) RemoveBoundary
         Returns the flag to indicate whether to remove the face boundary or not.  
            
         
        """
        pass
    @property
    def UEndDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) UEndDistance
         Returns the U end distance.  
             
         
        """
        pass
    @property
    def UEndLimit(self) -> OnPathDimensionBuilder:
        """
        Getter for property: ( OnPathDimensionBuilder NXOpen.Geome) UEndLimit
         Returns the region limit of U end.  
             
         
        """
        pass
    @property
    def UStartDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) UStartDistance
         Returns the U start distance.  
             
         
        """
        pass
    @property
    def UStartLimit(self) -> OnPathDimensionBuilder:
        """
        Getter for property: ( OnPathDimensionBuilder NXOpen.Geome) UStartLimit
         Returns the region limit of U start.  
             
         
        """
        pass
    @property
    def VEndDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) VEndDistance
         Returns the V end distance.  
             
         
        """
        pass
    @property
    def VEndLimit(self) -> OnPathDimensionBuilder:
        """
        Getter for property: ( OnPathDimensionBuilder NXOpen.Geome) VEndLimit
         Returns the region limit of V end.  
             
         
        """
        pass
    @property
    def VStartDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) VStartDistance
         Returns the V start distance.  
             
         
        """
        pass
    @property
    def VStartLimit(self) -> OnPathDimensionBuilder:
        """
        Getter for property: ( OnPathDimensionBuilder NXOpen.Geome) VStartLimit
         Returns the region limit of V start.  
             
         
        """
        pass
    def CleanUpFeaturesCreated(self) -> None:
        """
         Cleans up the features created by the selecting face call back.
        """
        pass
    def CreateCopyFace(self) -> None:
        """
         Creates the extracted face when the flag of Edit a Copy is turned on or a solid body face is selected.
        """
        pass
    def CreateProductBoundingBox(self) -> None:
        """
         Creates the product initial bounding box.
        """
        pass
    def SetCurrentFeature(self, objectValue: NXOpen.Features.Feature) -> None:
        """
         Records the current feature before constructing the dialog.
        """
        pass
    def SetInitialDistanceValue(self, distanceValues: List[float]) -> None:
        """
         Sets the initial distance value. 
        """
        pass
    def SetLimitChangeValue(self, limitType: int) -> None:
        """
         Sets the limit boundary handle type. 
        """
        pass
    def SetOriginalFace(self, originalFace: NXOpen.Face) -> None:
        """
         Sets the originally selected face. 
        """
        pass
    def UpdateBoundingBox(self) -> None:
        """
        Updates the bounding box when changing the distance value. 
        """
        pass
import NXOpen
class LocalUntrimManager(NXOpen.Object): 
    """ Provides create builder methods for LocalUntrimBuilder """
    def CreateBuilder(self) -> LocalUntrimBuilder:
        """
         Creates local untrim and extend builder. 
         Returns builder ( LocalUntrimBuilder NXOpen.Geome):  LocalUntrimBuilder  object object .
        """
        pass
import NXOpen
class MatchSurfaceBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.GeometricUtilities.MatchSurfaceBuilder builder.This builder's Commit can create a b-surface """
    class MatchConstaint(Enum):
        """
        Members Include: 
         |Position| 
         |Tangent| 

        """
        Position: int
        Tangent: int
        @staticmethod
        def ValueOf(value: int) -> MatchSurfaceBuilder.MatchConstaint:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngleTolerance(self) -> float:
        """
        Getter for property: (float) AngleTolerance
         Returns the angle tolerance   
            
         
        """
        pass
    @AngleTolerance.setter
    def AngleTolerance(self, angleTolerance: float):
        """
        Setter for property: (float) AngleTolerance
         Returns the angle tolerance   
            
         
        """
        pass
    @property
    def Constraint(self) -> MatchSurfaceBuilder.MatchConstaint:
        """
        Getter for property: ( MatchSurfaceBuilder.MatchConstaint NXOpen.Geome) Constraint
         Returns the continuity type for matching   
            
         
        """
        pass
    @Constraint.setter
    def Constraint(self, constraint: MatchSurfaceBuilder.MatchConstaint):
        """
        Setter for property: ( MatchSurfaceBuilder.MatchConstaint NXOpen.Geome) Constraint
         Returns the continuity type for matching   
            
         
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
    def DistanceTolerance(self, distTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance   
            
         
        """
        pass
    @property
    def EditEdge(self) -> NXOpen.SelectEdge:
        """
        Getter for property: ( NXOpen.SelectEdge) EditEdge
         Returns the selected edge for matching   
            
         
        """
        pass
    @property
    def EndToEnd(self) -> bool:
        """
        Getter for property: (bool) EndToEnd
         Returns the option to match end-to-end, between the end of edit edge and the reference egde or curve   
            
         
        """
        pass
    @EndToEnd.setter
    def EndToEnd(self, endToEnd: bool):
        """
        Setter for property: (bool) EndToEnd
         Returns the option to match end-to-end, between the end of edit edge and the reference egde or curve   
            
         
        """
        pass
    @property
    def KeepSheet(self) -> bool:
        """
        Getter for property: (bool) KeepSheet
         Returns the option to keep original sheet   
            
         
        """
        pass
    @KeepSheet.setter
    def KeepSheet(self, keepSheet: bool):
        """
        Setter for property: (bool) KeepSheet
         Returns the option to keep original sheet   
            
         
        """
        pass
    @property
    def MatchExact(self) -> bool:
        """
        Getter for property: (bool) MatchExact
         Returns the option to match exact, between the end of edit edge and the reference egde or curve   
            
         
        """
        pass
    @MatchExact.setter
    def MatchExact(self, matchExact: bool):
        """
        Setter for property: (bool) MatchExact
         Returns the option to match exact, between the end of edit edge and the reference egde or curve   
            
         
        """
        pass
    @property
    def Reference(self) -> NXOpen.SelectEdge:
        """
        Getter for property: ( NXOpen.SelectEdge) Reference
         Returns the selected reference edge or curve    
            
         
        """
        pass
    @property
    def ReferenceFace(self) -> NXOpen.SelectFace:
        """
        Getter for property: ( NXOpen.SelectFace) ReferenceFace
         Returns the selected face for reference curve    
            
         
        """
        pass
    @property
    def RegionLimit(self) -> OnPathDimensionBuilder:
        """
        Getter for property: ( OnPathDimensionBuilder NXOpen.Geome) RegionLimit
         Returns the distance limit of deformation region   
            
         
        """
        pass
import NXOpen
class MiddleHoleData(NXOpen.TaggedObject): 
    """ Represents a NXOpen.GeometricUtilities.MiddleHoleData """
    @property
    def BooleanOperation(self) -> BooleanOperation:
        """
        Getter for property: ( BooleanOperation NXOpen.Geome) BooleanOperation
         Returns the boolean operation   
            
         
        """
        pass
    @property
    def EndChamferAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndChamferAngle
         Returns the end chamfer angle   
            
         
        """
        pass
    @property
    def EndChamferEnabled(self) -> bool:
        """
        Getter for property: (bool) EndChamferEnabled
         Returns the end chamfer enabled   
            
         
        """
        pass
    @EndChamferEnabled.setter
    def EndChamferEnabled(self, endChamferEnabled: bool):
        """
        Setter for property: (bool) EndChamferEnabled
         Returns the end chamfer enabled   
            
         
        """
        pass
    @property
    def EndChamferOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndChamferOffset
         Returns the end chamfer offset   
            
         
        """
        pass
    @property
    def FitOption(self) -> str:
        """
        Getter for property: (str) FitOption
         Returns the fit option  
            
         
        """
        pass
    @FitOption.setter
    def FitOption(self, fitOption: str):
        """
        Setter for property: (str) FitOption
         Returns the fit option  
            
         
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
    def MatchDimOfStartHole(self) -> bool:
        """
        Getter for property: (bool) MatchDimOfStartHole
         Returns the match dim of start hole   
            
         
        """
        pass
    @MatchDimOfStartHole.setter
    def MatchDimOfStartHole(self, matchDimOfStartHole: bool):
        """
        Setter for property: (bool) MatchDimOfStartHole
         Returns the match dim of start hole   
            
         
        """
        pass
    @property
    def StartChamferAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartChamferAngle
         Returns the start chamfer angle   
            
         
        """
        pass
    @property
    def StartChamferEnabled(self) -> bool:
        """
        Getter for property: (bool) StartChamferEnabled
         Returns the start chamfer enabled   
            
         
        """
        pass
    @StartChamferEnabled.setter
    def StartChamferEnabled(self, startChamferEnabled: bool):
        """
        Setter for property: (bool) StartChamferEnabled
         Returns the start chamfer enabled   
            
         
        """
        pass
    @property
    def StartChamferOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartChamferOffset
         Returns the start chamfer offset   
            
         
        """
        pass
import NXOpen
class MirrorPattern(NXOpen.TaggedObject): 
    """ the Mirror pattern definition.  """
    class PlaneOptions(Enum):
        """
        Members Include: 
         |Existing|  existing plane
         |New|  new plane 

        """
        Existing: int
        New: int
        @staticmethod
        def ValueOf(value: int) -> MirrorPattern.PlaneOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ExistingPlane(self) -> NXOpen.SelectISurface:
        """
        Getter for property: ( NXOpen.SelectISurface) ExistingPlane
         Returns the Existing Mirror Plane   
            
         
        """
        pass
    @property
    def NewPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) NewPlane
         Returns the new plane    
            
         
        """
        pass
    @NewPlane.setter
    def NewPlane(self, newPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) NewPlane
         Returns the new plane    
            
         
        """
        pass
    @property
    def PlaneOption(self) -> MirrorPattern.PlaneOptions:
        """
        Getter for property: ( MirrorPattern.PlaneOptions NXOpen.Geome) PlaneOption
         Returns the plane option   
            
         
        """
        pass
    @PlaneOption.setter
    def PlaneOption(self, plane_options: MirrorPattern.PlaneOptions):
        """
        Setter for property: ( MirrorPattern.PlaneOptions NXOpen.Geome) PlaneOption
         Returns the plane option   
            
         
        """
        pass
import NXOpen
class ModlAlongCurveAngle(NXOpen.TaggedObject): 
    """ This class NXOpen.GeometricUtilities.ModlAlongCurveAngle represents motion type in ModlMotion """
    @property
    def AlongCurve(self) -> OnPathDimensionBuilder:
        """
        Getter for property: ( OnPathDimensionBuilder NXOpen.Geome) AlongCurve
         Returns the value of transform.  
             
         
        """
        pass
    @property
    def AlongCurveAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) AlongCurveAngle
         Returns the value of angular transform.  
             
         
        """
        pass
    @property
    def Curve(self) -> NXOpen.SelectCurve:
        """
        Getter for property: ( NXOpen.SelectCurve) Curve
         Returns the curve on which doing the transform.  
             
         
        """
        pass
    @property
    def ReverseCurveDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseCurveDirection
         Returns whether the direction of the curve to determine the transform should be reversed or not.  
             
         
        """
        pass
    @ReverseCurveDirection.setter
    def ReverseCurveDirection(self, reverseCurveDirection: bool):
        """
        Setter for property: (bool) ReverseCurveDirection
         Returns whether the direction of the curve to determine the transform should be reversed or not.  
             
         
        """
        pass
import NXOpen
class ModlDistanceAngle(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.GeometricUtilities.ModlDistanceAngle
    """
    @property
    def Angle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Angle
         Returns the value of angular transform.  
             
         
        """
        pass
    @property
    def AngularDirection(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) AngularDirection
         Returns the direction of angular dimensions.  
             
         
        """
        pass
    @AngularDirection.setter
    def AngularDirection(self, angularDirection: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) AngularDirection
         Returns the direction of angular dimensions.  
             
         
        """
        pass
    @property
    def Distance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Distance
         Returns the distance of linear transform.  
             
         
        """
        pass
    @property
    def LinearAxis(self) -> NXOpen.Axis:
        """
        Getter for property: ( NXOpen.Axis) LinearAxis
         Returns the linear axis of distance.  
             
         
        """
        pass
    @LinearAxis.setter
    def LinearAxis(self, linearAxis: NXOpen.Axis):
        """
        Setter for property: ( NXOpen.Axis) LinearAxis
         Returns the linear axis of distance.  
             
         
        """
        pass
    @property
    def OrientXpress(self) -> OrientXpressBuilder:
        """
        Getter for property: ( OrientXpressBuilder NXOpen.Geome) OrientXpress
         Returns the orientXpress.  
          
                OrientXpress used as overlay in Motion.   
         
        """
        pass
import NXOpen
class ModlMotion(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.GeometricUtilities.ModlMotion
    """
    class Delta(Enum):
        """
        Members Include: 
         |ReferenceAcsWorkPart|  Reference CSYS is absolute coordinate system in the work part 
         |ReferenceAcsDisplayPart|  Reference CSYS is absolute coordinate system in the display part 
         |ReferenceWcsWorkPart|  Reference CSYS is work coordinate system in the work part 
         |ReferenceWcsDisplayPart|  Reference CSYS is work coordinate system in the display part 
         |ReferenceDrawing|  Reference CSYS is drawing sheet coordinate system in drafting 

        """
        ReferenceAcsWorkPart: int
        ReferenceAcsDisplayPart: int
        ReferenceWcsWorkPart: int
        ReferenceWcsDisplayPart: int
        ReferenceDrawing: int
        @staticmethod
        def ValueOf(value: int) -> ModlMotion.Delta:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Options(Enum):
        """
        Members Include: 
         |AlongCurveAngle|  Move by AlongCurve-Angle 
         |DistanceAngle|  Move by Distance-Angle 
         |Distance|  Move by Distance 
         |Angle|  Move by Angle 
         |DistanceBetweenPoints|  Move by Distance between Points 
         |RadialDistance|  Move by Radial Distance 
         |PointToPoint|  Move by Point to Point 
         |RotateByThreePoints|  Move by Rotate by Three Points 
         |AlignAxisVector|  Move by Align Axis to Vector 
         |CsysToCsys|  Move by CSYS to CSYS 
         |Dynamic|  Move by Dynamic 
         |DeltaXyz|  Move by delta XYZ 
         |NotSet|  No move 

        """
        AlongCurveAngle: int
        DistanceAngle: int
        Distance: int
        Angle: int
        DistanceBetweenPoints: int
        RadialDistance: int
        PointToPoint: int
        RotateByThreePoints: int
        AlignAxisVector: int
        CsysToCsys: int
        Dynamic: int
        DeltaXyz: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> ModlMotion.Options:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AlignVector(self) -> NXOpen.Axis:
        """
        Getter for property: ( NXOpen.Axis) AlignVector
         Returns the axis of  NXOpen::GeometricUtilities::ModlMotion::OptionsAlignAxisVector 
                 motion option.  
             
         
        """
        pass
    @AlignVector.setter
    def AlignVector(self, alignVector: NXOpen.Axis):
        """
        Setter for property: ( NXOpen.Axis) AlignVector
         Returns the axis of  NXOpen::GeometricUtilities::ModlMotion::OptionsAlignAxisVector 
                 motion option.  
             
         
        """
        pass
    @property
    def AlongCurveAngle(self) -> ModlAlongCurveAngle:
        """
        Getter for property: ( ModlAlongCurveAngle NXOpen.Geome) AlongCurveAngle
         Returns the alongCurveAngle of   NXOpen::GeometricUtilities::ModlMotion::OptionsAlongCurveAngle  
                 motion option.  
             
         
        """
        pass
    @property
    def Angle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Angle
         Returns the angle of   NXOpen::GeometricUtilities::ModlMotion::OptionsAngle  
                 motion option.  
             
         
        """
        pass
    @property
    def AngularAxis(self) -> NXOpen.Axis:
        """
        Getter for property: ( NXOpen.Axis) AngularAxis
         Returns the angular axis of   NXOpen::GeometricUtilities::ModlMotion::OptionsAngle  
                 motion option.  
             
         
        """
        pass
    @AngularAxis.setter
    def AngularAxis(self, angularAxis: NXOpen.Axis):
        """
        Setter for property: ( NXOpen.Axis) AngularAxis
         Returns the angular axis of   NXOpen::GeometricUtilities::ModlMotion::OptionsAngle  
                 motion option.  
             
         
        """
        pass
    @property
    def DeltaEnum(self) -> ModlMotion.Delta:
        """
        Getter for property: ( ModlMotion.Delta NXOpen.Geome) DeltaEnum
         Returns the delta enum   
            
         
        """
        pass
    @DeltaEnum.setter
    def DeltaEnum(self, deltaEnum: ModlMotion.Delta):
        """
        Setter for property: ( ModlMotion.Delta NXOpen.Geome) DeltaEnum
         Returns the delta enum   
            
         
        """
        pass
    @property
    def DeltaX(self) -> float:
        """
        Getter for property: (float) DeltaX
         Returns the delta x   
            
         
        """
        pass
    @DeltaX.setter
    def DeltaX(self, deltaX: float):
        """
        Setter for property: (float) DeltaX
         Returns the delta x   
            
         
        """
        pass
    @property
    def DeltaXc(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DeltaXc
         Returns the delta xc   
            
         
        """
        pass
    @property
    def DeltaY(self) -> float:
        """
        Getter for property: (float) DeltaY
         Returns the delta y   
            
         
        """
        pass
    @DeltaY.setter
    def DeltaY(self, deltaY: float):
        """
        Setter for property: (float) DeltaY
         Returns the delta y   
            
         
        """
        pass
    @property
    def DeltaYc(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DeltaYc
         Returns the delta yc   
            
         
        """
        pass
    @property
    def DeltaZ(self) -> float:
        """
        Getter for property: (float) DeltaZ
         Returns the delta z   
            
         
        """
        pass
    @DeltaZ.setter
    def DeltaZ(self, deltaZ: float):
        """
        Setter for property: (float) DeltaZ
         Returns the delta z   
            
         
        """
        pass
    @property
    def DeltaZc(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DeltaZc
         Returns the delta zc   
            
         
        """
        pass
    @property
    def DistanceAngle(self) -> ModlDistanceAngle:
        """
        Getter for property: ( ModlDistanceAngle NXOpen.Geome) DistanceAngle
         Returns the distance-angle of   NXOpen::GeometricUtilities::ModlMotion::OptionsDistanceAngle  
                 motion option.  
             
         
        """
        pass
    @property
    def DistanceBetweenPointsDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DistanceBetweenPointsDistance
         Returns the distance of   NXOpen::GeometricUtilities::ModlMotion::OptionsDistanceBetweenPoints  
                 motion option.  
             
         
        """
        pass
    @property
    def DistanceBetweenPointsMeasurePoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) DistanceBetweenPointsMeasurePoint
         Returns the measure point of   NXOpen::GeometricUtilities::ModlMotion::OptionsDistanceBetweenPoints  
                 motion option.  
             
         
        """
        pass
    @DistanceBetweenPointsMeasurePoint.setter
    def DistanceBetweenPointsMeasurePoint(self, measurePoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) DistanceBetweenPointsMeasurePoint
         Returns the measure point of   NXOpen::GeometricUtilities::ModlMotion::OptionsDistanceBetweenPoints  
                 motion option.  
             
         
        """
        pass
    @property
    def DistanceBetweenPointsOriginDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DistanceBetweenPointsOriginDistance
         Returns the distance between origin point and face of   NXOpen::GeometricUtilities::ModlMotion::OptionsDistanceBetweenPoints  
                 motion option.  
             
         
        """
        pass
    @property
    def DistanceBetweenPointsOriginPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) DistanceBetweenPointsOriginPoint
         Returnsthe origin point of   NXOpen::GeometricUtilities::ModlMotion::OptionsDistanceBetweenPoints  
                motion option.  
             
         
        """
        pass
    @DistanceBetweenPointsOriginPoint.setter
    def DistanceBetweenPointsOriginPoint(self, originPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) DistanceBetweenPointsOriginPoint
         Returnsthe origin point of   NXOpen::GeometricUtilities::ModlMotion::OptionsDistanceBetweenPoints  
                motion option.  
             
         
        """
        pass
    @property
    def DistanceBetweenPointsVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) DistanceBetweenPointsVector
         Returns the direction of   NXOpen::GeometricUtilities::ModlMotion::OptionsDistanceBetweenPoints  
                 motion option.  
             
         
        """
        pass
    @DistanceBetweenPointsVector.setter
    def DistanceBetweenPointsVector(self, vector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) DistanceBetweenPointsVector
         Returns the direction of   NXOpen::GeometricUtilities::ModlMotion::OptionsDistanceBetweenPoints  
                 motion option.  
             
         
        """
        pass
    @property
    def DistanceValue(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DistanceValue
         Returnsthe distance value of   NXOpen::GeometricUtilities::ModlMotion::OptionsDistance   
                motion option.  
             
         
        """
        pass
    @property
    def DistanceVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) DistanceVector
         Returnsthe direction of   NXOpen::GeometricUtilities::ModlMotion::OptionsDistance   
                motion option.  
             
         
        """
        pass
    @DistanceVector.setter
    def DistanceVector(self, distanceVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) DistanceVector
         Returnsthe direction of   NXOpen::GeometricUtilities::ModlMotion::OptionsDistance   
                motion option.  
             
         
        """
        pass
    @property
    def EndPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) EndPoint
         Returns the end point of  NXOpen::GeometricUtilities::ModlMotion::OptionsRotateByThreePoints 
                 motion option.  
             
         
        """
        pass
    @EndPoint.setter
    def EndPoint(self, endPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) EndPoint
         Returns the end point of  NXOpen::GeometricUtilities::ModlMotion::OptionsRotateByThreePoints 
                 motion option.  
             
         
        """
        pass
    @property
    def FromCsys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) FromCsys
         Returns the "from csys" of   NXOpen::GeometricUtilities::ModlMotion::OptionsCsysToCsys  
                 motion option .  
             
         
        """
        pass
    @FromCsys.setter
    def FromCsys(self, fromcsys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) FromCsys
         Returns the "from csys" of   NXOpen::GeometricUtilities::ModlMotion::OptionsCsysToCsys  
                 motion option .  
             
         
        """
        pass
    @property
    def FromPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) FromPoint
         Returns the "from point" of   NXOpen::GeometricUtilities::ModlMotion::OptionsPointToPoint  
                 motion option.  
             
         
        """
        pass
    @FromPoint.setter
    def FromPoint(self, fromPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) FromPoint
         Returns the "from point" of   NXOpen::GeometricUtilities::ModlMotion::OptionsPointToPoint  
                 motion option.  
             
         
        """
        pass
    @property
    def ManipulatorMatrix(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: ( NXOpen.Matrix3x3) ManipulatorMatrix
         Returns the matrix of manipulator for  NXOpen::GeometricUtilities::ModlMotion::OptionsDynamic 
                 motion option.  
             
         
        """
        pass
    @ManipulatorMatrix.setter
    def ManipulatorMatrix(self, manipulatorMatrix: NXOpen.Matrix3x3):
        """
        Setter for property: ( NXOpen.Matrix3x3) ManipulatorMatrix
         Returns the matrix of manipulator for  NXOpen::GeometricUtilities::ModlMotion::OptionsDynamic 
                 motion option.  
             
         
        """
        pass
    @property
    def ManipulatorOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) ManipulatorOrigin
         Returns the origin point of manipulator for  NXOpen::GeometricUtilities::ModlMotion::OptionsDynamic 
                 motion option.  
             
         
        """
        pass
    @ManipulatorOrigin.setter
    def ManipulatorOrigin(self, manipulatorOrigin: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) ManipulatorOrigin
         Returns the origin point of manipulator for  NXOpen::GeometricUtilities::ModlMotion::OptionsDynamic 
                 motion option.  
             
         
        """
        pass
    @property
    def MoveHandle(self) -> bool:
        """
        Getter for property: (bool) MoveHandle
         Returns the move handle toggle of  NXOpen::GeometricUtilities::ModlMotion::OptionsDynamic 
                 motion option.  
          If true,moves only manipulator handle. If false, moves both manipulator handle and object.  
         
        """
        pass
    @MoveHandle.setter
    def MoveHandle(self, moveHandle: bool):
        """
        Setter for property: (bool) MoveHandle
         Returns the move handle toggle of  NXOpen::GeometricUtilities::ModlMotion::OptionsDynamic 
                 motion option.  
          If true,moves only manipulator handle. If false, moves both manipulator handle and object.  
         
        """
        pass
    @property
    def Option(self) -> ModlMotion.Options:
        """
        Getter for property: ( ModlMotion.Options NXOpen.Geome) Option
         Returns the options.  
          
                Control the Motion methods.   
         
        """
        pass
    @Option.setter
    def Option(self, type: ModlMotion.Options):
        """
        Setter for property: ( ModlMotion.Options NXOpen.Geome) Option
         Returns the options.  
          
                Control the Motion methods.   
         
        """
        pass
    @property
    def OrientXpress(self) -> OrientXpressBuilder:
        """
        Getter for property: ( OrientXpressBuilder NXOpen.Geome) OrientXpress
         Returns the orientXpress.  
          
                OrientXpress used as overlay in Motion.   
         
        """
        pass
    @property
    def RadialAxis(self) -> NXOpen.Axis:
        """
        Getter for property: ( NXOpen.Axis) RadialAxis
         Returns the axis of   NXOpen::GeometricUtilities::ModlMotion::OptionsRadialDistance  
                 motion option.  
             
         
        """
        pass
    @RadialAxis.setter
    def RadialAxis(self, radialAxis: NXOpen.Axis):
        """
        Setter for property: ( NXOpen.Axis) RadialAxis
         Returns the axis of   NXOpen::GeometricUtilities::ModlMotion::OptionsRadialDistance  
                 motion option.  
             
         
        """
        pass
    @property
    def RadialDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RadialDistance
         Returns the distance value of   NXOpen::GeometricUtilities::ModlMotion::OptionsRadialDistance  
                 motion option.  
             
         
        """
        pass
    @property
    def RadialMeasurePoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) RadialMeasurePoint
         Returns the measure point of   NXOpen::GeometricUtilities::ModlMotion::OptionsRadialDistance  
                 motion option.  
             
         
        """
        pass
    @RadialMeasurePoint.setter
    def RadialMeasurePoint(self, radialMeasuPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) RadialMeasurePoint
         Returns the measure point of   NXOpen::GeometricUtilities::ModlMotion::OptionsRadialDistance  
                 motion option.  
             
         
        """
        pass
    @property
    def RadialOriginDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RadialOriginDistance
         Returns the distance between axis point and face of   NXOpen::GeometricUtilities::ModlMotion::OptionsRadialDistance  
                 motion option.  
             
         
        """
        pass
    @property
    def RotateVector(self) -> NXOpen.Axis:
        """
        Getter for property: ( NXOpen.Axis) RotateVector
         Returns the direction of   NXOpen::GeometricUtilities::ModlMotion::OptionsRotateByThreePoints  
                 motion option.  
             
         
        """
        pass
    @RotateVector.setter
    def RotateVector(self, rotateVector: NXOpen.Axis):
        """
        Setter for property: ( NXOpen.Axis) RotateVector
         Returns the direction of   NXOpen::GeometricUtilities::ModlMotion::OptionsRotateByThreePoints  
                 motion option.  
             
         
        """
        pass
    @property
    def StartPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) StartPoint
         Returns the start point of   NXOpen::GeometricUtilities::ModlMotion::OptionsRotateByThreePoints  
                 motion option.  
             
         
        """
        pass
    @StartPoint.setter
    def StartPoint(self, startPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) StartPoint
         Returns the start point of   NXOpen::GeometricUtilities::ModlMotion::OptionsRotateByThreePoints  
                 motion option.  
             
         
        """
        pass
    @property
    def TempManipulatorOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) TempManipulatorOrigin
         Returns the temporary origin point of manipulator for  NXOpen::GeometricUtilities::ModlMotion::OptionsDynamic 
                    motion option.  
             
         
        """
        pass
    @TempManipulatorOrigin.setter
    def TempManipulatorOrigin(self, manipulatorOrigin: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) TempManipulatorOrigin
         Returns the temporary origin point of manipulator for  NXOpen::GeometricUtilities::ModlMotion::OptionsDynamic 
                    motion option.  
             
         
        """
        pass
    @property
    def ToCsys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) ToCsys
         Returns the "to csys" where object is moved for motion option 
                  NXOpen::GeometricUtilities::ModlMotion::OptionsCsysToCsys  .  
             
         
        """
        pass
    @ToCsys.setter
    def ToCsys(self, tocsys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) ToCsys
         Returns the "to csys" where object is moved for motion option 
                  NXOpen::GeometricUtilities::ModlMotion::OptionsCsysToCsys  .  
             
         
        """
        pass
    @property
    def ToPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) ToPoint
         Returns the point where object is moved for motion option 
                  NXOpen::GeometricUtilities::ModlMotion::OptionsPointToPoint     
            
         
        """
        pass
    @ToPoint.setter
    def ToPoint(self, toPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) ToPoint
         Returns the point where object is moved for motion option 
                  NXOpen::GeometricUtilities::ModlMotion::OptionsPointToPoint     
            
         
        """
        pass
    @property
    def ToVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ToVector
         Returns the vector of  NXOpen::GeometricUtilities::ModlMotion::OptionsAlignAxisVector 
                 motion option.  
             
         
        """
        pass
    @ToVector.setter
    def ToVector(self, toVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ToVector
         Returns the vector of  NXOpen::GeometricUtilities::ModlMotion::OptionsAlignAxisVector 
                 motion option.  
             
         
        """
        pass
    def GetTransformation(self) -> List[float]:
        """
         The 4x4 transformation matrix 
         Returns transformation (List[float]): .
        """
        pass
    def ResetMotionToThreeDimensions(self) -> None:
        """
         Reset motion to three dimensions 
        """
        pass
    def SetDependentView(self, view: NXOpen.View) -> None:
        """
         Set the view for view dependent drafting objects 
        """
        pass
    def SetFromPointSelectionObjects(self, selectedObjects: List[NXOpen.TaggedObject]) -> None:
        """
         Selected entities for extracting fromPoint 
        """
        pass
    def SetMotionToTwoDimensions(self, plane: NXOpen.Plane) -> None:
        """
         Set motion to two dimensions along the given plane 
        """
        pass
    def SetToPointSelectionObjects(self, selectedObjects: List[NXOpen.TaggedObject]) -> None:
        """
         Selected entities for extracting toPoint 
        """
        pass
    def SetUpdateOption(self, option: NXOpen.SmartObject.UpdateOption) -> None:
        """
         Set the update option for defining the update behavior for the object.
                    As an example, in modeling application, the update option should be 
                    "WithinModeling" and in drafting application it should be "AfterModeling".
        """
        pass
import NXOpen
class MovePoleBuilder(NXOpen.TaggedObject): 
    """
       This class manages the control poles movements for a surface or curve.
    """
    class MoveMethodType(Enum):
        """
        Members Include: 
         |Wcs| 
         |View| 
         |Vector| 
         |Plane| 
         |Normal| 
         |Polygon| 

        """
        Wcs: int
        View: int
        Vector: int
        Plane: int
        Normal: int
        Polygon: int
        @staticmethod
        def ValueOf(value: int) -> MovePoleBuilder.MoveMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class WCSDirectionType(Enum):
        """
        Members Include: 
         |X| 
         |Y| 
         |Z| 
         |YZ| 
         |XZ| 
         |XY| 

        """
        X: int
        Y: int
        Z: int
        YZ: int
        XZ: int
        XY: int
        @staticmethod
        def ValueOf(value: int) -> MovePoleBuilder.WCSDirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ControlPoleManager(self) -> ControlPoleManagerData:
        """
        Getter for property: ( ControlPoleManagerData NXOpen.Geome) ControlPoleManager
         Returns the control pole manager   
            
         
        """
        pass
    @property
    def DegreesAndPatches(self) -> DegreesAndSegmentsOrPatchesBuilder:
        """
        Getter for property: ( DegreesAndSegmentsOrPatchesBuilder NXOpen.Geome) DegreesAndPatches
         Returns the degrees and patches   
            
         
        """
        pass
    @property
    def Entity(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) Entity
         Returns the entity   
            
         
        """
        pass
    @Entity.setter
    def Entity(self, entity: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) Entity
         Returns the entity   
            
         
        """
        pass
    @property
    def MoveMethod(self) -> MovePoleBuilder.MoveMethodType:
        """
        Getter for property: ( MovePoleBuilder.MoveMethodType NXOpen.Geome) MoveMethod
         Returns the control pole move method   
            
         
        """
        pass
    @MoveMethod.setter
    def MoveMethod(self, moveMethod: MovePoleBuilder.MoveMethodType):
        """
        Setter for property: ( MovePoleBuilder.MoveMethodType NXOpen.Geome) MoveMethod
         Returns the control pole move method   
            
         
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
    def WCSDirection(self) -> MovePoleBuilder.WCSDirectionType:
        """
        Getter for property: ( MovePoleBuilder.WCSDirectionType NXOpen.Geome) WCSDirection
         Returns the fixed direction   
            
         
        """
        pass
    @WCSDirection.setter
    def WCSDirection(self, wcsDirection: MovePoleBuilder.WCSDirectionType):
        """
        Setter for property: ( MovePoleBuilder.WCSDirectionType NXOpen.Geome) WCSDirection
         Returns the fixed direction   
            
         
        """
        pass
import NXOpen
import NXOpen.Features
class MultiDraft(SimpleDraft): 
    """ Represents a multi-draft. 
    """
    class AngleOption(Enum):
        """
        Members Include: 
         |Single| Sigle draft
         |Multiple| Multi draft

        """
        Single: int
        Multiple: int
        @staticmethod
        def ValueOf(value: int) -> MultiDraft.AngleOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BackDraftAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BackDraftAngle
         Returns the back draft angle.  
           This function is used only when the angle type is  GeometricUtilities::MultiDraft::AngleOptionSingle .
                   
         
        """
        pass
    @property
    def DraftOption(self) -> SimpleDraft.SimpleDraftType:
        """
        Getter for property: ( SimpleDraft.SimpleDraftType NXOpen.Geome) DraftOption
         Returns  the draft type
                  
            
         
        """
        pass
    @DraftOption.setter
    def DraftOption(self, type: SimpleDraft.SimpleDraftType):
        """
        Setter for property: ( SimpleDraft.SimpleDraftType NXOpen.Geome) DraftOption
         Returns  the draft type
                  
            
         
        """
        pass
    @property
    def FrontDraftAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FrontDraftAngle
         Returns the front draft angle.  
           This function is used only when the angle type is  GeometricUtilities::MultiDraft::AngleOptionSingle .
                  
         
        """
        pass
    def GetAngleOption(self) -> MultiDraft.AngleOption:
        """
        Returns the draft angle option
                 
         Returns type ( MultiDraft.AngleOption NXOpen.Geome): .
        """
        pass
    def GetDrafts(self, section: NXOpen.Section) -> List[NXOpen.Features.EmbossTaper]:
        """
         Return all the drafts
                 
         Returns drafts ( NXOpen.Features.EmbossTaper Li):  Array of draft objects .
        """
        pass
    def SetAngleOption(self, type: MultiDraft.AngleOption) -> None:
        """
        Sets the draft angle option
                 
        """
        pass
import NXOpen
class MultiTransitionLawBuilder(NXOpen.TaggedObject): 
    """
        Represents multiple transition law.
        
        This class represents NXOpen.GeometricUtilities.LawBuilder.Type.MultiTransition type
        of law in NXOpen.GeometricUtilities.LawBuilder.
        Objects of class NXOpen.GeometricUtilities.TransitionLawNodeBuilder are used
        as law nodes in NXOpen.GeometricUtilities.MultiTransitionLawBuilder. Spine
        definition in this class is mandatory. You can specify any number of law nodes on the spine.
        Minimum two law nodes are necessary to define the multi transition law along the spine.
        The law nodes must be specified in the parametrically increasing order in the spine direction.
        

        
        
        Depending on the law node position on the spine following transition types are supported -
        
        
        
        Start node - All options in NXOpen.GeometricUtilities.TransitionLawNodeBuilder.TransitionType except
        NXOpen.GeometricUtilities.TransitionLawNodeBuilder.TransitionType.Unknown
        
        
        
        End node - NXOpen.GeometricUtilities.TransitionLawNodeBuilder.TransitionType.Blend and
        NXOpen.GeometricUtilities.TransitionLawNodeBuilder.TransitionType.Minmax only
        
        
        
        End node - All options in NXOpen.GeometricUtilities.TransitionLawNodeBuilder.TransitionType may be supported.
        Consult the referencing class documentation to see when
        NXOpen.GeometricUtilities.TransitionLawNodeBuilder.TransitionType.Unknown is not supported
        at a law node.
        
        
        
    """
    @property
    def NodeList(self) -> TransitionLawNodeBuilderList:
        """
        Getter for property: ( TransitionLawNodeBuilderList NXOpen.Geome) NodeList
         Returns the list of law nodes.  
             
         
        """
        pass
    @property
    def Spine(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Spine
         Returns the spine   
            
         
        """
        pass
    def CreateNode(self) -> TransitionLawNodeBuilder:
        """
         Creates a new law node 
         Returns lawNode ( TransitionLawNodeBuilder NXOpen.Geome):  Law node .
        """
        pass
    def UpdateSpine(self) -> None:
        """
         Update the builder based on current spine 
        """
        pass
import NXOpen
import NXOpen.Features
class NestModuleBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.GeometricUtilities.NestModuleBuilder 
    
    Note that this class is now deprecated. Please use the 
    NXOpen.Features.FeatureCollection instead.
    
    """
    @property
    def DestinationModule(self) -> NXOpen.Features.SelectFeature:
        """
        Getter for property: ( NXOpen.Features.SelectFeature) DestinationModule
         Returns the destination module 
                  
                This API is now deprecated.  
          
                Please use  NXOpen::Features::FeatureCollection::ReorganizeFeature  instead.
                  
                  
         
        """
        pass
    @property
    def ModuleToNest(self) -> NXOpen.Features.SelectFeature:
        """
        Getter for property: ( NXOpen.Features.SelectFeature) ModuleToNest
         Returns the module to nest 
                  
                This API is now deprecated.  
          
                Please use  NXOpen::Features::FeatureCollection::ReorganizeFeature  instead.
                  
                  
         
        """
        pass
import NXOpen
class NonInflectingLawBuilder(NXOpen.TaggedObject): 
    """
        Represents a non-inflecting law.
        
        This class represents NXOpen.GeometricUtilities.LawBuilder.Type.NonInflecting type
        of law in NXOpen.GeometricUtilities.LawBuilder.
        Objects of class NXOpen.GeometricUtilities.OnPathDimWithValueBuilder are used
        as law nodes in NXOpen.GeometricUtilities.NonInflectingLawBuilder. Spine
        definition in this class is mandatory. The law nodes at start and end of the spine are fixed.
        Middle node can be located any where between start and end nodes.
    """
    @property
    def EndNode(self) -> OnPathDimWithValueBuilder:
        """
        Getter for property: ( OnPathDimWithValueBuilder NXOpen.Geome) EndNode
         Returns the end node   
            
         
        """
        pass
    @property
    def MiddleNode(self) -> OnPathDimWithValueBuilder:
        """
        Getter for property: ( OnPathDimWithValueBuilder NXOpen.Geome) MiddleNode
         Returns the middle node   
            
         
        """
        pass
    @property
    def Spine(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Spine
         Returns the Spine   
            
         
        """
        pass
    @property
    def StartNode(self) -> OnPathDimWithValueBuilder:
        """
        Getter for property: ( OnPathDimWithValueBuilder NXOpen.Geome) StartNode
         Returns the start node   
            
         
        """
        pass
    def UpdateSpine(self) -> None:
        """
         Update the builder based on current spine 
        """
        pass
import NXOpen
class OmnicadManager(NXOpen.Object): 
    """ Represents a manager for creating builder objects for OmniCAD Free Transformer """
    def CreateFtmFixedCurvesBuilder(self) -> FtmFixedCurvesBuilder:
        """
         Creates Free Transformer fixed curves builder. 
         Returns builder ( FtmFixedCurvesBuilder NXOpen.Geome):  FtmFixedCurvesBuilder  object object .
        """
        pass
    def CreateFtmTransformCurvesBuilder(self) -> FtmTransformCurvesBuilder:
        """
         Creates Free Transformer transform curves builder. 
         Returns builder ( FtmTransformCurvesBuilder NXOpen.Geome):  FtmTransformCurvesBuilder  object object .
        """
        pass
    def CreateFtmTransformPointsBuilder(self) -> FtmTransformPointsBuilder:
        """
         Creates Free Transformer transform points builder. 
         Returns builder ( FtmTransformPointsBuilder NXOpen.Geome):  FtmTransformPointsBuilder  object object .
        """
        pass
import NXOpen
class OnPathDimensionBuilder(NXOpen.TaggedObject): 
    """ Builds an on-path dimension """
    class UpdateReason(Enum):
        """
        Members Include: 
         |Path|  Update because of the path may have changed 
         |ThroughPoint|  Update because the through point location may have changed 
         |All|  Update because either path or through point location may have changed 

        """
        Path: int
        ThroughPoint: int
        All: int
        @staticmethod
        def ValueOf(value: int) -> OnPathDimensionBuilder.UpdateReason:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Expression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Expression
         Returns the expression for the value of the dimension   
            
         
        """
        pass
    @property
    def IsFlipped(self) -> bool:
        """
        Getter for property: (bool) IsFlipped
         Returns a flag indicating whether the length along the path is evaluated
                    starting from the end point of path instead of the start point of the path   
            
         
        """
        pass
    @IsFlipped.setter
    def IsFlipped(self, flipped: bool):
        """
        Setter for property: (bool) IsFlipped
         Returns a flag indicating whether the length along the path is evaluated
                    starting from the end point of path instead of the start point of the path   
            
         
        """
        pass
    @property
    def IsParameterUsed(self) -> bool:
        """
        Getter for property: (bool) IsParameterUsed
         Returns a flag indicating whether the expression is in terms of the mathematical
                    parameter of the path (is_parameter_used = true) or in terms of its 
                    arclength (is_parameter_used = false).  
            When value is true, the value
                    will always be expressed in terms of percentage (between 0 and 100) regardless
                    of is_percent_used's setting.  This property must be used with care.  Most 
                    referencing classes will only accept arclength values, and setting this property 
                    to true for those classes will result in a run time error.  Consult the referencing
                    class documentation to see if this value can be true for that particular operation.   
         
        """
        pass
    @IsParameterUsed.setter
    def IsParameterUsed(self, use_parameter: bool):
        """
        Setter for property: (bool) IsParameterUsed
         Returns a flag indicating whether the expression is in terms of the mathematical
                    parameter of the path (is_parameter_used = true) or in terms of its 
                    arclength (is_parameter_used = false).  
            When value is true, the value
                    will always be expressed in terms of percentage (between 0 and 100) regardless
                    of is_percent_used's setting.  This property must be used with care.  Most 
                    referencing classes will only accept arclength values, and setting this property 
                    to true for those classes will result in a run time error.  Consult the referencing
                    class documentation to see if this value can be true for that particular operation.   
         
        """
        pass
    @property
    def IsPercentUsed(self) -> bool:
        """
        Getter for property: (bool) IsPercentUsed
         Returns a flag indicating whether the expression represents the percentage along
                    the path.  
            If false, the expression represents the length along the path   
         
        """
        pass
    @IsPercentUsed.setter
    def IsPercentUsed(self, use_percent: bool):
        """
        Setter for property: (bool) IsPercentUsed
         Returns a flag indicating whether the expression represents the percentage along
                    the path.  
            If false, the expression represents the length along the path   
         
        """
        pass
    @property
    def Path(self) -> NXOpen.SelectObject:
        """
        Getter for property: ( NXOpen.SelectObject) Path
         Returns the path that the dimension is evaluated on.  
            Note: in some cases, the
                    builder will not permit you to change the path   
         
        """
        pass
    @property
    def ThroughPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) ThroughPoint
         Returns the through point   
            
         
        """
        pass
    @ThroughPoint.setter
    def ThroughPoint(self, throughPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) ThroughPoint
         Returns the through point   
            
         
        """
        pass
    def Update(self, updateReason: OnPathDimensionBuilder.UpdateReason) -> None:
        """
         Updates this object if the path or through point location has changed.  
                Call this function if the path is a section
                and you have added or removed curves from the section, or if there
                is a through point and the coordinates of the through point have changed. 
        """
        pass
import NXOpen
import NXOpen.Assemblies
class OnPathDimWithValueBuilder(NXOpen.TaggedObject): 
    """
    Represents a  NXOpen.GeometricUtilities.OnPathDimWithValueBuilder 
    """
    @property
    def IsOccurrence(self) -> bool:
        """
        Getter for property: (bool) IsOccurrence
         Returns whether this object is an occurrence or not.  
             
         
        """
        pass
    @property
    def JournalIdentifier(self) -> str:
        """
        Getter for property: (str) JournalIdentifier
         Returns the identifier that would be recorded in a journal for this object.  
           
            This may not be the same across different releases of the software.   
         
        """
        pass
    @property
    def Location(self) -> OnPathDimensionBuilder:
        """
        Getter for property: ( OnPathDimensionBuilder NXOpen.Geome) Location
         Returns the location on path   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the custom name of the object.  
              
         
        """
        pass
    @property
    def OwningComponent(self) -> NXOpen.Assemblies.Component:
        """
        Getter for property: ( NXOpen.Assemblies.Component) OwningComponent
         Returns the owning component, if this object is an occurrence.  
             
         
        """
        pass
    @property
    def OwningPart(self) -> NXOpen.BasePart:
        """
        Getter for property: ( NXOpen.BasePart) OwningPart
         Returns the owning part of this object   
            
         
        """
        pass
    @property
    def Prototype(self) -> NXOpen.INXObject:
        """
        Getter for property: ( NXOpen.INXObject) Prototype
         Returns the prototype of this object if it is an occurrence.  
             
         
        """
        pass
    @property
    def Value(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Value
         Returns the value expression   
            
         
        """
        pass
    def InheritLocation(self, sourceBuilder: OnPathDimWithValueBuilder) -> None:
        """
         Inherits location data of a NXOpen.GeometricUtilities.OnPathDimWithValueBuilder object 
        """
        pass
    def InheritValue(self, sourceBuilder: OnPathDimWithValueBuilder) -> None:
        """
         Inherits value of a NXOpen.GeometricUtilities.OnPathDimWithValueBuilder object 
        """
        pass
class OnPathDistancePatternSpacing(PatternSpacing): 
    """ defines the various ways pattern instances can be 
        spaced within the pattern, particularly in the context of the
        PatternDefinition class. """
    @property
    def OnPathPitchDistance(self) -> OnPathDimensionBuilder:
        """
        Getter for property: ( OnPathDimensionBuilder NXOpen.Geome) OnPathPitchDistance
         Returns the distance for the spacing of the pattern from one instance to the next.  
            
         
        """
        pass
    @property
    def OnPathSpanDistance(self) -> OnPathDimensionBuilder:
        """
        Getter for property: ( OnPathDimensionBuilder NXOpen.Geome) OnPathSpanDistance
         Returns the distance for the spacing of the pattern for the entire pattern.  
             
         
        """
        pass
import NXOpen
class OrientationMethodBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.GeometricUtilities.OrientationMethodBuilder
    """
    class OrientationOptions(Enum):
        """
        Members Include: 
         |Fixed|  Fixed 
         |ByFaceNormals|  Face Normals 
         |ByVectorDirection|  Vector Direction 
         |ByAnotherCurve|  Another Curve 
         |ByAPoint|  A Point 
         |ByAngularLaw|  Angular Law 
         |ByForcedDirection|  Forced Direction 

        """
        Fixed: int
        ByFaceNormals: int
        ByVectorDirection: int
        ByAnotherCurve: int
        ByAPoint: int
        ByAngularLaw: int
        ByForcedDirection: int
        @staticmethod
        def ValueOf(value: int) -> OrientationMethodBuilder.OrientationOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngularLaw(self) -> LawBuilder:
        """
        Getter for property: ( LawBuilder NXOpen.Geome) AngularLaw
         Returns the angular law.  
           For orientation by an Angular Law, the section rotation along the guide curve is governed by the input law.   
         
        """
        pass
    @property
    def Faces(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Faces
         Returns the faces that provide normal direction for alignment of second axis of local coordinate system.  
             
         
        """
        pass
    @property
    def NormalFaceList(self) -> NXOpen.SelectFaceList:
        """
        Getter for property: ( NXOpen.SelectFaceList) NormalFaceList
         Returns the normal face list.  
           For orientation by Face Normals, the second axis of the local coordinate system is aligned with the resultant 
                    of normals of the input faces.   
         
        """
        pass
    @property
    def OrientationCurve(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) OrientationCurve
         Returns the orientation curve.  
           For orientation by Another Curve, the second axis of the local coordinate system is obtained by joining
                    corresponding points on the guide and the input section.   
         
        """
        pass
    @property
    def OrientationOption(self) -> OrientationMethodBuilder.OrientationOptions:
        """
        Getter for property: ( OrientationMethodBuilder.OrientationOptions NXOpen.Geome) OrientationOption
         Returns the orientation option.  
           Except for Fixed orientation method, additional parameters andor inputs are required.   
         
        """
        pass
    @OrientationOption.setter
    def OrientationOption(self, orientationOption: OrientationMethodBuilder.OrientationOptions):
        """
        Setter for property: ( OrientationMethodBuilder.OrientationOptions NXOpen.Geome) OrientationOption
         Returns the orientation option.  
           Except for Fixed orientation method, additional parameters andor inputs are required.   
         
        """
        pass
    @property
    def OrientationPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) OrientationPoint
         Returns the orientation point.  
           For orientation by a Point, the second axis is obtained with the equivalent of a three-sided ruled 
                    sheet between the guide string and the input point.   
         
        """
        pass
    @OrientationPoint.setter
    def OrientationPoint(self, orientationPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) OrientationPoint
         Returns the orientation point.  
           For orientation by a Point, the second axis is obtained with the equivalent of a three-sided ruled 
                    sheet between the guide string and the input point.   
         
        """
        pass
    @property
    def OrientationVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) OrientationVector
         Returns the orientation vector.  
           For orientation by Vector, the second axis of the local coordinate system is aligned with the input vector.   
         
        """
        pass
    @OrientationVector.setter
    def OrientationVector(self, orientationVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) OrientationVector
         Returns the orientation vector.  
           For orientation by Vector, the second axis of the local coordinate system is aligned with the input vector.   
         
        """
        pass
import NXOpen
class OrientXpressBuilder(NXOpen.TaggedObject): 
    """ Represent the OrientXpress block """
    class Axis(Enum):
        """
        Members Include: 
         |X|  Active axis in x-axis direction 
         |Y|  Active axis in y-axis direction 
         |Z|  Active axis in z-axis direction 
         |Passive|  Passive axis input mode 

        """
        X: int
        Y: int
        Z: int
        Passive: int
        @staticmethod
        def ValueOf(value: int) -> OrientXpressBuilder.Axis:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Plane(Enum):
        """
        Members Include: 
         |Yz|  Active plane is parallel to yz-plane 
         |Xz|  Active plane is parallel to xz-plane 
         |Xy|  Active plane is parallel to xy-plane 
         |Passive|  Passive plane input mode 

        """
        Yz: int
        Xz: int
        Xy: int
        Passive: int
        @staticmethod
        def ValueOf(value: int) -> OrientXpressBuilder.Plane:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Reference(Enum):
        """
        Members Include: 
         |AcsWorkPart|  Reference CSYS is absolute coordinate system in the work part 
         |AcsDisplayPart|  Reference CSYS is absolute coordinate system in the display part 
         |WcsWorkPart|  Reference CSYS is work coordinate system in the work part 
         |WcsDisplayPart|  Reference CSYS is work coordinate system in the display part 
         |Csys|  Reference CSYS is user specified coordinate system 
         |Fixed|  Reference CSYS is user defined coordinate system 
         |ProgramDefined|  Reference CSYS is application defined 
         |PathOrientation|  Reference CSYS is based off the path orientation 

        """
        AcsWorkPart: int
        AcsDisplayPart: int
        WcsWorkPart: int
        WcsDisplayPart: int
        Csys: int
        Fixed: int
        ProgramDefined: int
        PathOrientation: int
        @staticmethod
        def ValueOf(value: int) -> OrientXpressBuilder.Reference:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AxisOption(self) -> OrientXpressBuilder.Axis:
        """
        Getter for property: ( OrientXpressBuilder.Axis NXOpen.Geome) AxisOption
         Returns the orientXpress active axis option   
            
         
        """
        pass
    @AxisOption.setter
    def AxisOption(self, orientXpressAxisOption: OrientXpressBuilder.Axis):
        """
        Setter for property: ( OrientXpressBuilder.Axis NXOpen.Geome) AxisOption
         Returns the orientXpress active axis option   
            
         
        """
        pass
    @property
    def Csys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) Csys
         Returns the orientXpress reference csys when reference option is set to csys   
            
         
        """
        pass
    @Csys.setter
    def Csys(self, orientXpressCSYS: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) Csys
         Returns the orientXpress reference csys when reference option is set to csys   
            
         
        """
        pass
    @property
    def FixedCsys(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) FixedCsys
         Returns the orientXpress fixed csys when reference option is set to fixed csys   
            
         
        """
        pass
    @FixedCsys.setter
    def FixedCsys(self, orientXpressFixedCSYS: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) FixedCsys
         Returns the orientXpress fixed csys when reference option is set to fixed csys   
            
         
        """
        pass
    @property
    def PlaneOption(self) -> OrientXpressBuilder.Plane:
        """
        Getter for property: ( OrientXpressBuilder.Plane NXOpen.Geome) PlaneOption
         Returns the orientXpress active plane option   
            
         
        """
        pass
    @PlaneOption.setter
    def PlaneOption(self, orientXpressPlaneOption: OrientXpressBuilder.Plane):
        """
        Setter for property: ( OrientXpressBuilder.Plane NXOpen.Geome) PlaneOption
         Returns the orientXpress active plane option   
            
         
        """
        pass
    @property
    def ProgramDefinedCsys(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) ProgramDefinedCsys
         Returns the orientXpress program defined csys when reference option is set to program defined csys   
            
         
        """
        pass
    @ProgramDefinedCsys.setter
    def ProgramDefinedCsys(self, orientXpressProgramDefinedCSYS: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) ProgramDefinedCsys
         Returns the orientXpress program defined csys when reference option is set to program defined csys   
            
         
        """
        pass
    @property
    def ReferenceOption(self) -> OrientXpressBuilder.Reference:
        """
        Getter for property: ( OrientXpressBuilder.Reference NXOpen.Geome) ReferenceOption
         Returns the orientXpress reference coordinate system   
            
         
        """
        pass
    @ReferenceOption.setter
    def ReferenceOption(self, orientXpressReferenceOption: OrientXpressBuilder.Reference):
        """
        Setter for property: ( OrientXpressBuilder.Reference NXOpen.Geome) ReferenceOption
         Returns the orientXpress reference coordinate system   
            
         
        """
        pass
import NXOpen
class ParentEquivalencyMapList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[ParentEquivalencyMap]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: ParentEquivalencyMap) -> None:
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
    def Erase(self, obj: ParentEquivalencyMap) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: ParentEquivalencyMap, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: ParentEquivalencyMap) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> ParentEquivalencyMap:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( ParentEquivalencyMap NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[ParentEquivalencyMap]:
        """
         Gets the contents of the entire list 
         Returns objects ( ParentEquivalencyMap List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: ParentEquivalencyMap) -> None:
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
    def SetContents(self, objects: List[ParentEquivalencyMap]) -> None:
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
    def Swap(self, object1: ParentEquivalencyMap, object2: ParentEquivalencyMap) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class ParentEquivalencyMap(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.GeometricUtilities.ParentEquivalencyMap. An object of this class represents
    a correspondence between entities of the current object (Linked  Extract feature being edited) and entities
    of the replacement object (faces  body).
    """
    class Status(Enum):
        """
        Members Include: 
         |Incomplete|  incomplete 
         |Tentative|  tentative 
         |Accepted|  accepted 

        """
        Incomplete: int
        Tentative: int
        Accepted: int
        @staticmethod
        def ValueOf(value: int) -> ParentEquivalencyMap.Status:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Type(Enum):
        """
        Members Include: 
         |Undefined|  undefined 
         |UserDefined|  user defined or manual 
         |NameBased|  mapped by name 
         |Geometric|  mapped by geometric comparison 
         |Inferred|  inferred from accepted 
         |Internal|  internal ID reuse 
         |Inherited|  inherited from other part or operation 
         |Mixed|  combination of multiple methods 

        """
        Undefined: int
        UserDefined: int
        NameBased: int
        Geometric: int
        Inferred: int
        Internal: int
        Inherited: int
        Mixed: int
        @staticmethod
        def ValueOf(value: int) -> ParentEquivalencyMap.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def MapStatus(self) -> ParentEquivalencyMap.Status:
        """
        Getter for property: ( ParentEquivalencyMap.Status NXOpen.Geome) MapStatus
         Returns the map status   
            
         
        """
        pass
    @MapStatus.setter
    def MapStatus(self, mapStatus: ParentEquivalencyMap.Status):
        """
        Setter for property: ( ParentEquivalencyMap.Status NXOpen.Geome) MapStatus
         Returns the map status   
            
         
        """
        pass
    @property
    def MapType(self) -> ParentEquivalencyMap.Type:
        """
        Getter for property: ( ParentEquivalencyMap.Type NXOpen.Geome) MapType
         Returns the map type   
            
         
        """
        pass
    @MapType.setter
    def MapType(self, mapType: ParentEquivalencyMap.Type):
        """
        Setter for property: ( ParentEquivalencyMap.Type NXOpen.Geome) MapType
         Returns the map type   
            
         
        """
        pass
    def GetEntitiesFromCurrentObject(self) -> List[NXOpen.DisplayableObject]:
        """
         Get the mapped entities from the current object. 
         Returns entitiesFromCurrentObject ( NXOpen.DisplayableObject Li):  entities from the current object .
        """
        pass
    def GetEntitiesFromReplacementObject(self) -> List[NXOpen.DisplayableObject]:
        """
         Get the mapped entities from the replacement object 
         Returns entitiesFromReplacementObject ( NXOpen.DisplayableObject Li):  entities from the replacement object .
        """
        pass
    def SetMappedEntities(self, oldEntities: List[NXOpen.DisplayableObject], newEntities: List[NXOpen.DisplayableObject]) -> None:
        """
         Set externally mapped entities 
        """
        pass
import NXOpen
import NXOpen.Features
class PartModuleInputBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.GeometricUtilities.PartModuleInputBuilder """
    class ModifiableGeometryOptions(Enum):
        """
        Members Include: 
         |WholeBody|  the whole shared body will be allowed for selection inside part module
         |Selected|  the facesedges on shared body that are allowed for selection inside part module

        """
        WholeBody: int
        Selected: int
        @staticmethod
        def ValueOf(value: int) -> PartModuleInputBuilder.ModifiableGeometryOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DefineSharedBodyInput(self) -> bool:
        """
        Getter for property: (bool) DefineSharedBodyInput
         Returns the shared body inputs option.  
           If true, user will be able to provide shared body inputs.   
         
        """
        pass
    @DefineSharedBodyInput.setter
    def DefineSharedBodyInput(self, defineSharedBodyInput: bool):
        """
        Setter for property: (bool) DefineSharedBodyInput
         Returns the shared body inputs option.  
           If true, user will be able to provide shared body inputs.   
         
        """
        pass
    @property
    def InputReferences(self) -> NXOpen.Features.PartGeometryCopyBuilder:
        """
        Getter for property: ( NXOpen.Features.PartGeometryCopyBuilder) InputReferences
         Returns the part module input data   
            
         
        """
        pass
    @property
    def ModifiableGeometry(self) -> NXOpen.ScCollectorList:
        """
        Getter for property: ( NXOpen.ScCollectorList) ModifiableGeometry
         Returns the facesedges specified as modifiable geometry   
            
         
        """
        pass
    @property
    def ModifiableGeometryOption(self) -> PartModuleInputBuilder.ModifiableGeometryOptions:
        """
        Getter for property: ( PartModuleInputBuilder.ModifiableGeometryOptions NXOpen.Geome) ModifiableGeometryOption
         Returns the Modifiable Geometry option   
            
         
        """
        pass
    @ModifiableGeometryOption.setter
    def ModifiableGeometryOption(self, modifiableGeometryOption: PartModuleInputBuilder.ModifiableGeometryOptions):
        """
        Setter for property: ( PartModuleInputBuilder.ModifiableGeometryOptions NXOpen.Geome) ModifiableGeometryOption
         Returns the Modifiable Geometry option   
            
         
        """
        pass
    @property
    def SharedBodyInput(self) -> NXOpen.Features.PartGeometryCopyBuilder:
        """
        Getter for property: ( NXOpen.Features.PartGeometryCopyBuilder) SharedBodyInput
         Returns the bodies for part module shared body   
            
         
        """
        pass
import NXOpen
import NXOpen.Features
class PartModuleOutputBuilder1(NXOpen.Builder): 
    """ Represents a NXOpen.GeometricUtilities.PartModuleOutputBuilder1 """
    @property
    def OutputReferences1(self) -> NXOpen.Features.PartGeometryCopyBuilder:
        """
        Getter for property: ( NXOpen.Features.PartGeometryCopyBuilder) OutputReferences1
         Returns the new part module output data   
            
         
        """
        pass
import NXOpen
class PartModuleOutputBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.GeometricUtilities.PartModuleOutputBuilder """
    @property
    def Activate(self) -> bool:
        """
        Getter for property: (bool) Activate
         Returns the option indicating whether the part module is to be activated.  
           If true, the part module will be activated, else, no action is taken
                   
                 This API is now deprecated.
                 Please use  NXOpen::Features::PartModule::Activate  instead.
                   
                  
         
        """
        pass
    @Activate.setter
    def Activate(self, activate: bool):
        """
        Setter for property: (bool) Activate
         Returns the option indicating whether the part module is to be activated.  
           If true, the part module will be activated, else, no action is taken
                   
                 This API is now deprecated.
                 Please use  NXOpen::Features::PartModule::Activate  instead.
                   
                  
         
        """
        pass
    @property
    def Deactivate(self) -> bool:
        """
        Getter for property: (bool) Deactivate
         Returns the option indicating whether the part module is to be deactivated.  
           If true, the part module will be deactivated, else, no action is taken
                   
                 This API is now deprecated.
                 Please use  NXOpen::Features::PartModule::Activate  instead.
                   
                  
         
        """
        pass
    @Deactivate.setter
    def Deactivate(self, deactivate: bool):
        """
        Setter for property: (bool) Deactivate
         Returns the option indicating whether the part module is to be deactivated.  
           If true, the part module will be deactivated, else, no action is taken
                   
                 This API is now deprecated.
                 Please use  NXOpen::Features::PartModule::Activate  instead.
                   
                  
         
        """
        pass
    @property
    def OutputReferences(self) -> PartModuleReferencesBuilder:
        """
        Getter for property: ( PartModuleReferencesBuilder NXOpen.Geome) OutputReferences
         Returns the part module output data 
                   
                 This API is now deprecated.  
          
                 Please use  NXOpen::GeometricUtilities::PartModuleOutputBuilder1::OutputReferences1  instead.
                   
                  
         
        """
        pass
import NXOpen
class PartModuleReferencesBuilder(NXOpen.TaggedObject): 
    """ Represents a NXOpen.GeometricUtilities.PartModuleReferencesBuilder """
    @property
    def ExpressionList(self) -> NXOpen.SelectExpressionList:
        """
        Getter for property: ( NXOpen.SelectExpressionList) ExpressionList
         Returns the expressions for part module inputoutput   
            
         
        """
        pass
    @property
    def GeometryList(self) -> SelectionListList:
        """
        Getter for property: ( SelectionListList NXOpen.Geome) GeometryList
         Returns the geometric references for part module inputoutput   
            
         
        """
        pass
import NXOpen
import NXOpen.Features
class PartModuleRelationshipBuilder(NXOpen.Builder): 
    """ Represents a Features.PartModule builder """
    @property
    def LinkedPartModule(self) -> NXOpen.Features.SelectPartModule:
        """
        Getter for property: ( NXOpen.Features.SelectPartModule) LinkedPartModule
         Returns the linked part module in separate part to which relationship needs to be established   
            
         
        """
        pass
    @property
    def PartModule(self) -> NXOpen.Features.SelectPartModule:
        """
        Getter for property: ( NXOpen.Features.SelectPartModule) PartModule
         Returns the part module in owining part to establish the relationship   
            
         
        """
        pass
class PathLimits(Limits): 
    """ Represents a path limits data. 
    """
    pass
import NXOpen
class PatternClockingBuilder(NXOpen.Builder): 
    """  enables the ability to apply delta transforms on individual instances of a pattern within the pattern feature """
    class ClockingType(Enum):
        """
        Members Include: 
         |WithinPatternDefinitionLinear|  
         |WithinPatternDefinitionCircular|  
         |UserDefined|  
         |WithinPatternDefinitionAxial|  

        """
        WithinPatternDefinitionLinear: int
        WithinPatternDefinitionCircular: int
        UserDefined: int
        WithinPatternDefinitionAxial: int
        @staticmethod
        def ValueOf(value: int) -> PatternClockingBuilder.ClockingType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngularDelta(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) AngularDelta
         Returns the angular delta for circular clocking   
            
         
        """
        pass
    @property
    def ClockType(self) -> PatternClockingBuilder.ClockingType:
        """
        Getter for property: ( PatternClockingBuilder.ClockingType NXOpen.Geome) ClockType
         Returns the clocking enum to determine if linear or angular clocking   
            
         
        """
        pass
    @ClockType.setter
    def ClockType(self, clockType: PatternClockingBuilder.ClockingType):
        """
        Setter for property: ( PatternClockingBuilder.ClockingType NXOpen.Geome) ClockType
         Returns the clocking enum to determine if linear or angular clocking   
            
         
        """
        pass
    @property
    def Direction1Delta(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Direction1Delta
         Returns the x direction delta for linear clocking   
            
         
        """
        pass
    @property
    def Direction2Delta(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Direction2Delta
         Returns the y direction delta for linear clocking   
            
         
        """
        pass
    @property
    def Motion(self) -> ModlMotion:
        """
        Getter for property: ( ModlMotion NXOpen.Geome) Motion
         Returns the user defined transform motion   
            
         
        """
        pass
    @property
    def RadialDelta(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RadialDelta
         Returns the radial delta for circular clocking   
            
         
        """
        pass
    def AddInstance(self, index1: int, index2: int) -> None:
        """
         Adds an instance that will get this clocking 
        """
        pass
    def RemoveInstance(self, index1: int, index2: int) -> None:
        """
         Removes an instance from this clocking 
        """
        pass
import NXOpen
class PatternClocking(NXOpen.TaggedObject): 
    """  enables the ability to apply delta transforms on individual instances of a pattern """
    class ClockingType(Enum):
        """
        Members Include: 
         |WithinPatternDefinitionLinear|  
         |WithinPatternDefinitionCircular|  
         |WithinPatternDefinitionAxial|  

        """
        WithinPatternDefinitionLinear: int
        WithinPatternDefinitionCircular: int
        WithinPatternDefinitionAxial: int
        @staticmethod
        def ValueOf(value: int) -> PatternClocking.ClockingType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngularDelta(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) AngularDelta
         Returns the angular delta for circular clocking   
            
         
        """
        pass
    @property
    def ClockType(self) -> PatternClocking.ClockingType:
        """
        Getter for property: ( PatternClocking.ClockingType NXOpen.Geome) ClockType
         Returns the clocking enum to determine if linear or angular clocking   
            
         
        """
        pass
    @property
    def Direction1Delta(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Direction1Delta
         Returns the x direction delta for linear clocking   
            
         
        """
        pass
    @property
    def Direction2Delta(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Direction2Delta
         Returns the y direction delta for linear clocking   
            
         
        """
        pass
    @property
    def RadialDelta(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RadialDelta
         Returns the radial delta for circular clocking   
            
         
        """
        pass
    def SetAngularDelta(self, angularDeltaExp: str) -> None:
        """
         Sets a angular delta for circular clocking 
        """
        pass
    def SetRadialDelta(self, radialDelta: str) -> None:
        """
         Sets a radial delta for circular clocking 
        """
        pass
    def SetXDirectionDelta(self, direction1Exp: str) -> None:
        """
         Sets an x direction delta for linear clocking 
        """
        pass
    def SetYDirectionDelta(self, direction2Exp: str) -> None:
        """
         Sets a y direction delta for linear clocking 
        """
        pass
import NXOpen
class PatternDefinition(NXOpen.TaggedObject): 
    """ pattern spacing for several pattern based commands.  See PatternEnum definition
        below for a listing of the various pattern definitions available. """
    class PatternEnum(Enum):
        """
        Members Include: 
         |Linear|  pattern along single linear direction. 
         |Circular|  pattern in angular and radial directions. 
         |Polygon|  polygon pattern. 
         |Spiral|  spiral pattern. 
         |AlongPath|  pattern along a section path. 
         |General|  general pattern. 
         |Reference|  reference pattern. 
         |Mirror|  mirror pattern. 
         |Helix|  helix pattern. 
         |Axial|  pattern in angular and axial directions. 

        """
        Linear: int
        Circular: int
        Polygon: int
        Spiral: int
        AlongPath: int
        General: int
        Reference: int
        Mirror: int
        Helix: int
        Axial: int
        @staticmethod
        def ValueOf(value: int) -> PatternDefinition.PatternEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AlongPathDefinition(self) -> AlongPathPattern:
        """
        Getter for property: ( AlongPathPattern NXOpen.Geome) AlongPathDefinition
         Returns the along path definition.  
            See AlongPathPattern for details.   
         
        """
        pass
    @property
    def CircularDefinition(self) -> CircularPattern:
        """
        Getter for property: ( CircularPattern NXOpen.Geome) CircularDefinition
         Returns the circular definition.  
            See CircularPattern for details.   
         
        """
        pass
    @property
    def FrameOnlyToggle(self) -> bool:
        """
        Getter for property: (bool) FrameOnlyToggle
         Returns the frameOnlyToggle, a logical flag to indicate if the we need only instances on the boundary.  
             
         
        """
        pass
    @FrameOnlyToggle.setter
    def FrameOnlyToggle(self, frameOnlyToggle: bool):
        """
        Setter for property: (bool) FrameOnlyToggle
         Returns the frameOnlyToggle, a logical flag to indicate if the we need only instances on the boundary.  
             
         
        """
        pass
    @property
    def GeneralDefinition(self) -> GeneralPattern:
        """
        Getter for property: ( GeneralPattern NXOpen.Geome) GeneralDefinition
         Returns the general definition.  
            See GeneralPattern for details.   
         
        """
        pass
    @property
    def HelixDefinition(self) -> HelixPattern:
        """
        Getter for property: ( HelixPattern NXOpen.Geome) HelixDefinition
         Returns the helix definition.  
            See HelixPattern for details.   
         
        """
        pass
    @property
    def MirrorDefinition(self) -> MirrorPattern:
        """
        Getter for property: ( MirrorPattern NXOpen.Geome) MirrorDefinition
         Returns the mirror definition.  
            See MirrorPattern for details.   
         
        """
        pass
    @property
    def PatternFill(self) -> PatternFill:
        """
        Getter for property: ( PatternFill NXOpen.Geome) PatternFill
         Returns the pattern fill definition.  
            See PatternFill for details.   
         
        """
        pass
    @property
    def PatternIncrementsBuilder(self) -> PatternIncrementsBuilder:
        """
        Getter for property: ( PatternIncrementsBuilder NXOpen.Geome) PatternIncrementsBuilder
         Returns the pattern increments definition.  
            See  NXOpen::GeometricUtilities::PatternIncrementsBuilder  for details.   
         
        """
        pass
    @property
    def PatternOrientation(self) -> PatternOrientation:
        """
        Getter for property: ( PatternOrientation NXOpen.Geome) PatternOrientation
         Returns the pattern orientation definition.  
            See PatternOrientation for details.   
         
        """
        pass
    @property
    def PatternType(self) -> PatternDefinition.PatternEnum:
        """
        Getter for property: ( PatternDefinition.PatternEnum NXOpen.Geome) PatternType
         Returns the pattern type   
            
         
        """
        pass
    @PatternType.setter
    def PatternType(self, patternType: PatternDefinition.PatternEnum):
        """
        Setter for property: ( PatternDefinition.PatternEnum NXOpen.Geome) PatternType
         Returns the pattern type   
            
         
        """
        pass
    @property
    def PolygonDefinition(self) -> PolygonPattern:
        """
        Getter for property: ( PolygonPattern NXOpen.Geome) PolygonDefinition
         Returns the polygon definition.  
            See PolygonPattern for details.   
         
        """
        pass
    @property
    def RectangularDefinition(self) -> RectangularPattern:
        """
        Getter for property: ( RectangularPattern NXOpen.Geome) RectangularDefinition
         Returns the linear definition.  
            See LinearPattern for details.   
         
        """
        pass
    @property
    def ReferenceDefinition(self) -> ReferencePattern:
        """
        Getter for property: ( ReferencePattern NXOpen.Geome) ReferenceDefinition
         Returns the reference definition.  
            See ReferencePattern for details.   
         
        """
        pass
    @property
    def SeedOnlyToggle(self) -> bool:
        """
        Getter for property: (bool) SeedOnlyToggle
         Returns the seedOnlyToggle, a logical flag to indicate if the we need only instances for the seed along the second direction.  
             
         
        """
        pass
    @SeedOnlyToggle.setter
    def SeedOnlyToggle(self, seedOnlyToggle: bool):
        """
        Setter for property: (bool) SeedOnlyToggle
         Returns the seedOnlyToggle, a logical flag to indicate if the we need only instances for the seed along the second direction.  
             
         
        """
        pass
    @property
    def SpiralDefinition(self) -> SpiralPattern:
        """
        Getter for property: ( SpiralPattern NXOpen.Geome) SpiralDefinition
         Returns the spiral definition.  
            See SpiralPattern for details.   
         
        """
        pass
    def CreateClockingBuilder(self, ix: int, iy: int) -> PatternClockingBuilder:
        """
         Creates a pattern clocking object 
         Returns clockingBuilder ( PatternClockingBuilder NXOpen.Geome): .
        """
        pass
    def CreatePatternInstanceEditBuilder(self) -> PatternInstanceEditBuilder:
        """
         This is the default creator for NXOpen.GeometricUtilities.PatternInstanceEditBuilder. 
         Returns editBuilder ( PatternInstanceEditBuilder NXOpen.Geome): .
        """
        pass
    def GetClocking(self, index1: int, index2: int) -> PatternClocking:
        """
         Returns the clocking data for a NXOpen.GeometricUtilities.PatternDefinition instance 
         Returns clockingBuilder ( PatternClocking NXOpen.Geome): .
        """
        pass
    def GetDeleteState(self, index1: int, index2: int) -> bool:
        """
         Gets the delete state for the instance at the specified indicies. 
         Returns deleteState (bool): .
        """
        pass
    def GetSuppressState(self, index1: int, index2: int) -> bool:
        """
         Gets the suppress state for the instance at the specified indicies. 
         Returns suppressState (bool): .
        """
        pass
    def RemoveClocking(self, index1: int, index2: int) -> None:
        """
         Removes clocking from pattern definition instance 
        """
        pass
    def RemoveVariance(self, index1: int, index2: int) -> None:
        """
         Removes variance from pattern definition instance 
        """
        pass
    def SetDeleteState(self, index1: int, index2: int, deleteState: bool) -> None:
        """
         Sets the delete state for the instance at the specified indicies. 
        """
        pass
    def SetSpreadsheetData(self, spreadsheetTableArray: List[float], locationTableArray: List[float], defaultTableArray: List[bool]) -> None:
        """
         Sets the spreadsheet data 
        """
        pass
    def SetSuppressState(self, index1: int, index2: int, suppressState: bool) -> None:
        """
         Sets the suppress state for the instance at the specified indicies. 
        """
        pass
import NXOpen
class PatternFill(NXOpen.TaggedObject): 
    """ the pattern fill definition.  Allows to speicify a section boundary with an offset margin. """
    class PatternFillOptions(Enum):
        """
        Members Include: 
         |NotSet|  no section is defined 
         |FillbyFace|  section is face-based, and for fill area. 
         |FillbyBoundary|  section is for fill area.  
         |ExcludeAreaOnly|  section is for exclude area only 

        """
        NotSet: int
        FillbyFace: int
        FillbyBoundary: int
        ExcludeAreaOnly: int
        @staticmethod
        def ValueOf(value: int) -> PatternFill.PatternFillOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ApplyMarginToInnerBoundToggle(self) -> bool:
        """
        Getter for property: (bool) ApplyMarginToInnerBoundToggle
         Returns the applyMarginToInnerBoundToggle, a logical flag to indicate if we need to apply the margin value to internal bounday.  
             
         
        """
        pass
    @ApplyMarginToInnerBoundToggle.setter
    def ApplyMarginToInnerBoundToggle(self, applyMarginToInnerBoundToggle: bool):
        """
        Setter for property: (bool) ApplyMarginToInnerBoundToggle
         Returns the applyMarginToInnerBoundToggle, a logical flag to indicate if we need to apply the margin value to internal bounday.  
             
         
        """
        pass
    @property
    def FaceBoundary(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) FaceBoundary
         Returns the face boundary   
            
         
        """
        pass
    @property
    def FillBoundary(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) FillBoundary
         Returns the fill boundary   
            
         
        """
        pass
    @property
    def FillMargin(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FillMargin
         Returns the fill margin   
            
         
        """
        pass
    @property
    def FillOptions(self) -> PatternFill.PatternFillOptions:
        """
        Getter for property: ( PatternFill.PatternFillOptions NXOpen.Geome) FillOptions
         Returns the fill options   
            
         
        """
        pass
    @FillOptions.setter
    def FillOptions(self, fillOptions: PatternFill.PatternFillOptions):
        """
        Setter for property: ( PatternFill.PatternFillOptions NXOpen.Geome) FillOptions
         Returns the fill options   
            
         
        """
        pass
    @property
    def InternalBoundary(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) InternalBoundary
         Returns the fill boundary   
            
         
        """
        pass
    @property
    def SimplifiedBoundaryToggle(self) -> bool:
        """
        Getter for property: (bool) SimplifiedBoundaryToggle
         Returns the simplifiedBoundaryToggle, a logical flag to indicate a special case for Linear, Circular, Spiral, or Polygon.  
             
         
        """
        pass
    @SimplifiedBoundaryToggle.setter
    def SimplifiedBoundaryToggle(self, simplifiedBoundaryToggle: bool):
        """
        Setter for property: (bool) SimplifiedBoundaryToggle
         Returns the simplifiedBoundaryToggle, a logical flag to indicate a special case for Linear, Circular, Spiral, or Polygon.  
             
         
        """
        pass
import NXOpen
class PatternIncrementItemList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[PatternIncrementItem]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: PatternIncrementItem) -> None:
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
    def Erase(self, obj: PatternIncrementItem) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: PatternIncrementItem, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: PatternIncrementItem) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> PatternIncrementItem:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( PatternIncrementItem NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[PatternIncrementItem]:
        """
         Gets the contents of the entire list 
         Returns objects ( PatternIncrementItem List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: PatternIncrementItem) -> None:
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
    def SetContents(self, objects: List[PatternIncrementItem]) -> None:
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
    def Swap(self, object1: PatternIncrementItem, object2: PatternIncrementItem) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class PatternIncrementItem(NXOpen.TaggedObject): 
    """ variational for one master expression of the input object(s) being patterned. """
    class OperationEnum(Enum):
        """
        Members Include: 
         |Add|  add the increment to the master value. 
         |Multiply|  multiply the increment to the master value. 

        """
        Add: int
        Multiply: int
        @staticmethod
        def ValueOf(value: int) -> PatternIncrementItem.OperationEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def IncrementExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) IncrementExpression
         Returns the increment or variation to be applied to master expression   
            
         
        """
        pass
    @property
    def MasterExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MasterExpression
         Returns the master expression   
            
         
        """
        pass
    @property
    def Operation(self) -> PatternIncrementItem.OperationEnum:
        """
        Getter for property: ( PatternIncrementItem.OperationEnum NXOpen.Geome) Operation
         Returns the increment operation   
            
         
        """
        pass
    @Operation.setter
    def Operation(self, operation: PatternIncrementItem.OperationEnum):
        """
        Setter for property: ( PatternIncrementItem.OperationEnum NXOpen.Geome) Operation
         Returns the increment operation   
            
         
        """
        pass
import NXOpen
class PatternIncrementsBuilder(NXOpen.TaggedObject): 
    """ pattern increments builder """
    @property
    def IncrementsListInDirection1(self) -> PatternIncrementsList:
        """
        Getter for property: ( PatternIncrementsList NXOpen.Geome) IncrementsListInDirection1
         Returns the increments  NXOpen::GeometricUtilities::PatternIncrementsList  in Direction1.  
             
         
        """
        pass
    @property
    def IncrementsListInDirection2(self) -> PatternIncrementsList:
        """
        Getter for property: ( PatternIncrementsList NXOpen.Geome) IncrementsListInDirection2
         Returns the increments  NXOpen::GeometricUtilities::PatternIncrementsList  in Direction2.  
             
         
        """
        pass
import NXOpen
class PatternIncrementsList(NXOpen.TaggedObject): 
    """ list of NXOpen.GeometricUtilities.PatternIncrementItem objects. """
    @property
    def List(self) -> PatternIncrementItemList:
        """
        Getter for property: ( PatternIncrementItemList NXOpen.Geome) List
         Returns the list of  NXOpen::GeometricUtilities::PatternIncrementItem  objects.  
             
         
        """
        pass
    @overload
    def CreatePatternIncrementItem(self) -> PatternIncrementItem:
        """
         This is the default creator for NXOpen.GeometricUtilities.PatternIncrementItem.
                    Caution: This should never be called! 
         Returns varItem ( PatternIncrementItem NXOpen.Geome): .
        """
        pass
    @overload
    def CreatePatternIncrementItem(self, masterExpression: NXOpen.Expression) -> PatternIncrementItem:
        """
         This is the actual creator for NXOpen.GeometricUtilities.PatternIncrementItem. 
         Returns varItem ( PatternIncrementItem NXOpen.Geome): .
        """
        pass
import NXOpen
class PatternInstanceEditBuilder(NXOpen.Builder): 
    """ pattern instance edit builder """
    @property
    def EditedExpressionsList(self) -> InstanceEditedExpressionsList:
        """
        Getter for property: ( InstanceEditedExpressionsList NXOpen.Geome) EditedExpressionsList
         Returns the edited expressions list  NXOpen::GeometricUtilities::InstanceEditedExpressionsList .  
             
         
        """
        pass
    def SetSelectedInstances(self, firstIndexOfSelectedInstances: List[int], secondIndexOfSelectedInstances: List[int]) -> None:
        """
         Sets the indices of the selected Pattern Instances whose expressions are to be edited with
                    the expressions provided in the NXOpen.GeometricUtilities.InstanceEditedExpressionsList. 
        """
        pass
import NXOpen
class PatternOrientation(NXOpen.TaggedObject): 
    """ the pattern orientation definition.  Allows to specify an orientation option and corresponding entities. """
    class Enum(Enum):
        """
        Members Include: 
         |Fixed|  same orientation as the seed. 
         |NormalToPath|  normal to path orientation for Along Type first direction. 
         |NormalToVector|  normal to vector orientation for Along Type first direction.  
         |ParallelToVector|  parallel to vector orientation for Along Type first direction.  
         |ThroughAxis|  through axis orientation for Along Type first direction.  
         |FollowPattern|  follow pattern orientation, for example, circular, Axial pattern type.  
         |FollowCSYS|  follow CSYS orientation, for general pattern type, when fromto is CSYS.  
         |CSYStoCSYS|  a relative orientation defined by two CSYSs to transform the seed to an instance location.  

        """
        Fixed: int
        NormalToPath: int
        NormalToVector: int
        ParallelToVector: int
        ThroughAxis: int
        FollowPattern: int
        FollowCSYS: int
        CSYStoCSYS: int
        @staticmethod
        def ValueOf(value: int) -> PatternOrientation.Enum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ProjDirEnum(Enum):
        """
        Members Include: 
         |PatternPlaneNormal|  use pattern plane normal as project direction. 
         |NormalToFace|  project along face normal. 
         |RadialDir|  project along radial direction. This is specific for Circular pattern type.  
         |UserDefinedVector|  project along user defined vector.  
         |AxialDir|  project along axial direction. This is specific for Axial pattern type.  

        """
        PatternPlaneNormal: int
        NormalToFace: int
        RadialDir: int
        UserDefinedVector: int
        AxialDir: int
        @staticmethod
        def ValueOf(value: int) -> PatternOrientation.ProjDirEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AlongOrientationOption(self) -> PatternOrientation.Enum:
        """
        Getter for property: ( PatternOrientation.Enum NXOpen.Geome) AlongOrientationOption
         Returns the orientationOption for Along pattern type   
            
         
        """
        pass
    @AlongOrientationOption.setter
    def AlongOrientationOption(self, alongOrientationOption: PatternOrientation.Enum):
        """
        Setter for property: ( PatternOrientation.Enum NXOpen.Geome) AlongOrientationOption
         Returns the orientationOption for Along pattern type   
            
         
        """
        pass
    @property
    def AlongPathRotationAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) AlongPathRotationAngle
         Returns the along path rotation angle for the Along type pattern Normal to Path option.  
             
         
        """
        pass
    @property
    def CircularOrientationOption(self) -> PatternOrientation.Enum:
        """
        Getter for property: ( PatternOrientation.Enum NXOpen.Geome) CircularOrientationOption
         Returns the orientationOption for Circular pattern type   
            
         
        """
        pass
    @CircularOrientationOption.setter
    def CircularOrientationOption(self, circularOrientationOption: PatternOrientation.Enum):
        """
        Setter for property: ( PatternOrientation.Enum NXOpen.Geome) CircularOrientationOption
         Returns the orientationOption for Circular pattern type   
            
         
        """
        pass
    @property
    def FollowFaceProjDirOption(self) -> PatternOrientation.ProjDirEnum:
        """
        Getter for property: ( PatternOrientation.ProjDirEnum NXOpen.Geome) FollowFaceProjDirOption
         Returns the followFaceProjDirOption, an enum for follow face project direction.  
             
         
        """
        pass
    @FollowFaceProjDirOption.setter
    def FollowFaceProjDirOption(self, followFaceProjDirOption: PatternOrientation.ProjDirEnum):
        """
        Setter for property: ( PatternOrientation.ProjDirEnum NXOpen.Geome) FollowFaceProjDirOption
         Returns the followFaceProjDirOption, an enum for follow face project direction.  
             
         
        """
        pass
    @property
    def FollowFaceSelection(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FollowFaceSelection
         Returns the followFaceSelection, a sc collector to store selected faces.  
             
         
        """
        pass
    @property
    def FollowFaceToggle(self) -> bool:
        """
        Getter for property: (bool) FollowFaceToggle
         Returns the followFaceToggle, a logical flag to indicate if the we need to modify the orientation to follow selected faces.  
             
         
        """
        pass
    @FollowFaceToggle.setter
    def FollowFaceToggle(self, followFaceToggle: bool):
        """
        Setter for property: (bool) FollowFaceToggle
         Returns the followFaceToggle, a logical flag to indicate if the we need to modify the orientation to follow selected faces.  
             
         
        """
        pass
    @property
    def FromCSYS(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) FromCSYS
         Returns the fromCSYS, a CSYS for certain pattern type orientation need.  
             
         
        """
        pass
    @FromCSYS.setter
    def FromCSYS(self, fromCSYS: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) FromCSYS
         Returns the fromCSYS, a CSYS for certain pattern type orientation need.  
             
         
        """
        pass
    @property
    def GeneralOrientationOption(self) -> PatternOrientation.Enum:
        """
        Getter for property: ( PatternOrientation.Enum NXOpen.Geome) GeneralOrientationOption
         Returns the orientationOption for General pattern type   
            
         
        """
        pass
    @GeneralOrientationOption.setter
    def GeneralOrientationOption(self, generalOrientationOption: PatternOrientation.Enum):
        """
        Setter for property: ( PatternOrientation.Enum NXOpen.Geome) GeneralOrientationOption
         Returns the orientationOption for General pattern type   
            
         
        """
        pass
    @property
    def HelixOrientationOption(self) -> PatternOrientation.Enum:
        """
        Getter for property: ( PatternOrientation.Enum NXOpen.Geome) HelixOrientationOption
         Returns the orientationOption for Helix pattern type   
            
         
        """
        pass
    @HelixOrientationOption.setter
    def HelixOrientationOption(self, helixOrientationOption: PatternOrientation.Enum):
        """
        Setter for property: ( PatternOrientation.Enum NXOpen.Geome) HelixOrientationOption
         Returns the orientationOption for Helix pattern type   
            
         
        """
        pass
    @property
    def LinearOrientationOption(self) -> PatternOrientation.Enum:
        """
        Getter for property: ( PatternOrientation.Enum NXOpen.Geome) LinearOrientationOption
         Returns the orientationOption for Linear pattern type   
            
         
        """
        pass
    @LinearOrientationOption.setter
    def LinearOrientationOption(self, linearOrientationOption: PatternOrientation.Enum):
        """
        Setter for property: ( PatternOrientation.Enum NXOpen.Geome) LinearOrientationOption
         Returns the orientationOption for Linear pattern type   
            
         
        """
        pass
    @property
    def MirrorOrientationOption(self) -> PatternOrientation.Enum:
        """
        Getter for property: ( PatternOrientation.Enum NXOpen.Geome) MirrorOrientationOption
         Returns the orientationOption for Mirror pattern type   
            
         
        """
        pass
    @MirrorOrientationOption.setter
    def MirrorOrientationOption(self, mirrorOrientationOption: PatternOrientation.Enum):
        """
        Setter for property: ( PatternOrientation.Enum NXOpen.Geome) MirrorOrientationOption
         Returns the orientationOption for Mirror pattern type   
            
         
        """
        pass
    @property
    def OrientationOption(self) -> PatternOrientation.Enum:
        """
        Getter for property: ( PatternOrientation.Enum NXOpen.Geome) OrientationOption
         Returns the orientationOption for rectangular pattern type
                 Note: this one does not have a straight forward replacement;
                    Replacement based on pattern type:       
                     GeometricUtilities::PatternOrientation::LinearOrientationOption 
                     GeometricUtilities::PatternOrientation::CircularOrientationOption 
                     GeometricUtilities::PatternOrientation::AlongOrientationOption 
                     GeometricUtilities::PatternOrientation::PolygonOrientationOption 
                     GeometricUtilities::PatternOrientation::SpiralOrientationOption 
                     GeometricUtilities::PatternOrientation::GeneralOrientationOption 
                     GeometricUtilities::PatternOrientation::MirrorOrientationOption  
                     GeometricUtilities::PatternOrientation::HelixOrientationOption  
                     GeometricUtilities::PatternOrientation::AxialOrientationOption   
            
         
        """
        pass
    @OrientationOption.setter
    def OrientationOption(self, orientationOption: PatternOrientation.Enum):
        """
        Setter for property: ( PatternOrientation.Enum NXOpen.Geome) OrientationOption
         Returns the orientationOption for rectangular pattern type
                 Note: this one does not have a straight forward replacement;
                    Replacement based on pattern type:       
                     GeometricUtilities::PatternOrientation::LinearOrientationOption 
                     GeometricUtilities::PatternOrientation::CircularOrientationOption 
                     GeometricUtilities::PatternOrientation::AlongOrientationOption 
                     GeometricUtilities::PatternOrientation::PolygonOrientationOption 
                     GeometricUtilities::PatternOrientation::SpiralOrientationOption 
                     GeometricUtilities::PatternOrientation::GeneralOrientationOption 
                     GeometricUtilities::PatternOrientation::MirrorOrientationOption  
                     GeometricUtilities::PatternOrientation::HelixOrientationOption  
                     GeometricUtilities::PatternOrientation::AxialOrientationOption   
            
         
        """
        pass
    @property
    def PolygonOrientationOption(self) -> PatternOrientation.Enum:
        """
        Getter for property: ( PatternOrientation.Enum NXOpen.Geome) PolygonOrientationOption
         Returns the orientationOption for Polygon pattern type   
            
         
        """
        pass
    @PolygonOrientationOption.setter
    def PolygonOrientationOption(self, polygonOrientationOption: PatternOrientation.Enum):
        """
        Setter for property: ( PatternOrientation.Enum NXOpen.Geome) PolygonOrientationOption
         Returns the orientationOption for Polygon pattern type   
            
         
        """
        pass
    @property
    def RepeatTransformSetting(self) -> bool:
        """
        Getter for property: (bool) RepeatTransformSetting
         Returns the repeatTransformSetting, a logical flag to indicate if the we need to repeatedly apply the transform.  
             
         
        """
        pass
    @RepeatTransformSetting.setter
    def RepeatTransformSetting(self, repeatTransformSetting: bool):
        """
        Setter for property: (bool) RepeatTransformSetting
         Returns the repeatTransformSetting, a logical flag to indicate if the we need to repeatedly apply the transform.  
             
         
        """
        pass
    @property
    def SpiralOrientationOption(self) -> PatternOrientation.Enum:
        """
        Getter for property: ( PatternOrientation.Enum NXOpen.Geome) SpiralOrientationOption
         Returns the orientationOption for Spiral pattern type   
            
         
        """
        pass
    @SpiralOrientationOption.setter
    def SpiralOrientationOption(self, spiralOrientationOption: PatternOrientation.Enum):
        """
        Setter for property: ( PatternOrientation.Enum NXOpen.Geome) SpiralOrientationOption
         Returns the orientationOption for Spiral pattern type   
            
         
        """
        pass
    @property
    def ToCSYS(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) ToCSYS
         Returns the toCSYS, a CSYS for certain pattern type orientation need.  
             
         
        """
        pass
    @ToCSYS.setter
    def ToCSYS(self, toCSYS: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) ToCSYS
         Returns the toCSYS, a CSYS for certain pattern type orientation need.  
             
         
        """
        pass
    @property
    def UserDefinedProjDir(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) UserDefinedProjDir
         Returns the userDefinedProjDir, a vector for user defined follow face project direction.  
             
         
        """
        pass
    @UserDefinedProjDir.setter
    def UserDefinedProjDir(self, userDefinedProjDir: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) UserDefinedProjDir
         Returns the userDefinedProjDir, a vector for user defined follow face project direction.  
             
         
        """
        pass
    @property
    def VectorForAlong(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) VectorForAlong
         Returns the vectorForAlong, a vector for Along type orientation need.  
             
         
        """
        pass
    @VectorForAlong.setter
    def VectorForAlong(self, vectorForAlong: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) VectorForAlong
         Returns the vectorForAlong, a vector for Along type orientation need.  
             
         
        """
        pass
import NXOpen
class PatternReferencePointServiceBuilder(NXOpen.TaggedObject): 
    """ Pattern Reference Point is a service which enables the employing client to compute the reference point for pattern instance locations. 
     The reference point can be inferred or user-selected """
    @property
    def IsReferencePointInferred(self) -> bool:
        """
        Getter for property: (bool) IsReferencePointInferred
         Returns the reference point inferred flag.  
          
                    This flag states whether the reference point is inferred from selected entites or not.
                    If 'true', the reference point will be inferred every time the selected entities get modified or updated.
                    If 'false', the reference point provided by the user will be independent of the selected entities
                    but will be associative to the rule by which it was created (e.g. End of Line, Center of Arc).   
         
        """
        pass
    @IsReferencePointInferred.setter
    def IsReferencePointInferred(self, isReferencePointInferred: bool):
        """
        Setter for property: (bool) IsReferencePointInferred
         Returns the reference point inferred flag.  
          
                    This flag states whether the reference point is inferred from selected entites or not.
                    If 'true', the reference point will be inferred every time the selected entities get modified or updated.
                    If 'false', the reference point provided by the user will be independent of the selected entities
                    but will be associative to the rule by which it was created (e.g. End of Line, Center of Arc).   
         
        """
        pass
    @property
    def Point(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Point
         Returns the reference point   
            
         
        """
        pass
    @Point.setter
    def Point(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Point
         Returns the reference point   
            
         
        """
        pass
import NXOpen
class PatternSpacingsListItemList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[PatternSpacingsListItem]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: PatternSpacingsListItem) -> None:
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
    def Erase(self, obj: PatternSpacingsListItem) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: PatternSpacingsListItem, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: PatternSpacingsListItem) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> PatternSpacingsListItem:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( PatternSpacingsListItem NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[PatternSpacingsListItem]:
        """
         Gets the contents of the entire list 
         Returns objects ( PatternSpacingsListItem List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: PatternSpacingsListItem) -> None:
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
    def SetContents(self, objects: List[PatternSpacingsListItem]) -> None:
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
    def Swap(self, object1: PatternSpacingsListItem, object2: PatternSpacingsListItem) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class PatternSpacingsListItem(NXOpen.TaggedObject): 
    """ one pattern spacing in the spacings list """
    @property
    def SpacingExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SpacingExpression
         Returns the spacing expression   
            
         
        """
        pass
    @property
    def SpacingOnPath(self) -> OnPathDimensionBuilder:
        """
        Getter for property: ( OnPathDimensionBuilder NXOpen.Geome) SpacingOnPath
         Returns the spacing  NXOpen::GeometricUtilities::OnPathDimensionBuilder    
            
         
        """
        pass
import NXOpen
class PatternSpacingsList(NXOpen.TaggedObject): 
    """ list of NXOpen.GeometricUtilities.PatternSpacingsListItem objects. """
    @property
    def List(self) -> PatternSpacingsListItemList:
        """
        Getter for property: ( PatternSpacingsListItemList NXOpen.Geome) List
         Returns the list of  NXOpen::GeometricUtilities::PatternSpacingsListItem  objects.  
             
         
        """
        pass
    def CreatePatternSpacingsListItem(self) -> PatternSpacingsListItem:
        """
         This is the default creator for NXOpen.GeometricUtilities.PatternSpacingsListItem. 
         Returns varItem ( PatternSpacingsListItem NXOpen.Geome): .
        """
        pass
import NXOpen
class PatternSpacing(NXOpen.TaggedObject): 
    """ defines the various ways pattern instances can be 
        spaced within the pattern, particularly in the context of the
        PatternDefinition class. """
    class SpacingType(Enum):
        """
        Members Include: 
         |Offset|  Specify distance from the origin of one instance to the origin of the next instance. 
         |Span|  Specify a distance for which all instances should occupy. 
         |PitchAndSpan|  Specify distance between instances and distance for all instances, number of copies is calculated. 
         |Pitch|  This is for pattern fill case. Count is calculated based on the pitch and fill boundary box. 
         |List|  Specify offsets with a list. 
         |PolygonCountPerSide|  This is for Polygon type. Specify number of count per side. 
         |PolygonPitchAlongSide|  This is for Polygon type. Specify a pitch distance along one side. 
         |Points|  Specify offsets by point(s). Points are projected onto the direction or along path. One instance per point. 

        """
        Offset: int
        Span: int
        PitchAndSpan: int
        Pitch: int
        List: int
        PolygonCountPerSide: int
        PolygonPitchAlongSide: int
        Points: int
        @staticmethod
        def ValueOf(value: int) -> PatternSpacing.SpacingType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def NCopies(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NCopies
         Returns the number of copies the pattern will generated in this direction   
            
         
        """
        pass
    @property
    def Points(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Points
         Returns the section with points to be used in this direction   
            
         
        """
        pass
    @property
    def SpaceType(self) -> PatternSpacing.SpacingType:
        """
        Getter for property: ( PatternSpacing.SpacingType NXOpen.Geome) SpaceType
         Returns the type of spacing to be used by the pattern   
            
         
        """
        pass
    @SpaceType.setter
    def SpaceType(self, spaceType: PatternSpacing.SpacingType):
        """
        Setter for property: ( PatternSpacing.SpacingType NXOpen.Geome) SpaceType
         Returns the type of spacing to be used by the pattern   
            
         
        """
        pass
    @property
    def SpacingsList(self) -> PatternSpacingsList:
        """
        Getter for property: ( PatternSpacingsList NXOpen.Geome) SpacingsList
         Returns the list of spacings (Expression or OnPathDimBuilder) to be used in this direction   
            
         
        """
        pass
import NXOpen
class PlayButtonsBuilder(NXOpen.TaggedObject): 
    """ VCR buttons for any dialog that needs them """
    class PlayModeValues(Enum):
        """
        Members Include: 
         |PlayOnce| 
         |LoopOver| 
         |Retrace| 

        """
        PlayOnce: int
        LoopOver: int
        Retrace: int
        @staticmethod
        def ValueOf(value: int) -> PlayButtonsBuilder.PlayModeValues:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CurrentStep(self) -> int:
        """
        Getter for property: (int) CurrentStep
         Returns the step   
            
         
        """
        pass
    @CurrentStep.setter
    def CurrentStep(self, currentStep: int):
        """
        Setter for property: (int) CurrentStep
         Returns the step   
            
         
        """
        pass
    @property
    def PlayModes(self) -> PlayButtonsBuilder.PlayModeValues:
        """
        Getter for property: ( PlayButtonsBuilder.PlayModeValues NXOpen.Geome) PlayModes
         Returns the play modes   
            
         
        """
        pass
    @PlayModes.setter
    def PlayModes(self, playModes: PlayButtonsBuilder.PlayModeValues):
        """
        Setter for property: ( PlayButtonsBuilder.PlayModeValues NXOpen.Geome) PlayModes
         Returns the play modes   
            
         
        """
        pass
    @property
    def ScaleSpeed(self) -> float:
        """
        Getter for property: (float) ScaleSpeed
         Returns the scale speed   
            
         
        """
        pass
    @ScaleSpeed.setter
    def ScaleSpeed(self, scaleSpeed: float):
        """
        Setter for property: (float) ScaleSpeed
         Returns the scale speed   
            
         
        """
        pass
    @property
    def ScaleStep(self) -> float:
        """
        Getter for property: (float) ScaleStep
         Returns the scale step   
            
         
        """
        pass
    @ScaleStep.setter
    def ScaleStep(self, scaleStep: float):
        """
        Setter for property: (float) ScaleStep
         Returns the scale step   
            
         
        """
        pass
    @property
    def Speed(self) -> float:
        """
        Getter for property: (float) Speed
         Returns the speed   
            
         
        """
        pass
    @Speed.setter
    def Speed(self, speed: float):
        """
        Setter for property: (float) Speed
         Returns the speed   
            
         
        """
        pass
    def ForwardToEnd(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    def PlayBackward(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    def PlayForward(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    def RewindToStart(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    def StepBackward(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    def StepForward(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    def Stop(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
import NXOpen
class PointFacePlaneSelectionBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[PointFacePlaneSelectionBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: PointFacePlaneSelectionBuilder) -> None:
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
    def Erase(self, obj: PointFacePlaneSelectionBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: PointFacePlaneSelectionBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: PointFacePlaneSelectionBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> PointFacePlaneSelectionBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( PointFacePlaneSelectionBuilder NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[PointFacePlaneSelectionBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( PointFacePlaneSelectionBuilder List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: PointFacePlaneSelectionBuilder) -> None:
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
    def SetContents(self, objects: List[PointFacePlaneSelectionBuilder]) -> None:
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
    def Swap(self, object1: PointFacePlaneSelectionBuilder, object2: PointFacePlaneSelectionBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class PointFacePlaneSelectionBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.GeometricUtilities.PointFacePlaneSelectionBuilder
    """
    class TrimObjectType(Enum):
        """
        Members Include: 
         |Point|  length limit point 
         |Plane|  plane end cap
         |Face|  face end cap
         |Edge|  edge limit cap 

        """
        Point: int
        Plane: int
        Face: int
        Edge: int
        @staticmethod
        def ValueOf(value: int) -> PointFacePlaneSelectionBuilder.TrimObjectType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def IsOk(self) -> bool:
        """
        Getter for property: (bool) IsOk
         Returnsthe length limit object data OK flag   
            
         
        """
        pass
    @IsOk.setter
    def IsOk(self, isOk: bool):
        """
        Setter for property: (bool) IsOk
         Returnsthe length limit object data OK flag   
            
         
        """
        pass
    @property
    def LengthLimitPoint(self) -> LengthLimitPointBuilder:
        """
        Getter for property: ( LengthLimitPointBuilder NXOpen.Geome) LengthLimitPoint
         Returnsthe select point as length limit object  
            
         
        """
        pass
    @property
    def LimitTopolSwitchFinFlag(self) -> bool:
        """
        Getter for property: (bool) LimitTopolSwitchFinFlag
         Returns the limit edge switch fin flag   
            
         
        """
        pass
    @LimitTopolSwitchFinFlag.setter
    def LimitTopolSwitchFinFlag(self, switchFlag: bool):
        """
        Setter for property: (bool) LimitTopolSwitchFinFlag
         Returns the limit edge switch fin flag   
            
         
        """
        pass
    @property
    def PlaneHelpPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) PlaneHelpPoint
         Returnsthe user plane cap help point   
            
         
        """
        pass
    @PlaneHelpPoint.setter
    def PlaneHelpPoint(self, helpPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) PlaneHelpPoint
         Returnsthe user plane cap help point   
            
         
        """
        pass
    @property
    def SelectEdge(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SelectEdge
         Returnsthe select edge as length limit object  
            
         
        """
        pass
    @property
    def SelectFace(self) -> FaceSetData:
        """
        Getter for property: ( FaceSetData NXOpen.Geome) SelectFace
         Returns the select face as length limit object  
            
         
        """
        pass
    @property
    def SelectPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) SelectPlane
         Returns the select plane as length limit object  
            
         
        """
        pass
    @SelectPlane.setter
    def SelectPlane(self, selectPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) SelectPlane
         Returns the select plane as length limit object  
            
         
        """
        pass
    @property
    def TrimObject(self) -> PointFacePlaneSelectionBuilder.TrimObjectType:
        """
        Getter for property: ( PointFacePlaneSelectionBuilder.TrimObjectType NXOpen.Geome) TrimObject
         Returns the object type for length limit object   
            
         
        """
        pass
    @TrimObject.setter
    def TrimObject(self, trimObject: PointFacePlaneSelectionBuilder.TrimObjectType):
        """
        Setter for property: ( PointFacePlaneSelectionBuilder.TrimObjectType NXOpen.Geome) TrimObject
         Returns the object type for length limit object   
            
         
        """
        pass
    @property
    def UseFaceCapBlend(self) -> bool:
        """
        Getter for property: (bool) UseFaceCapBlend
         Returns the use face cap blend flag   
            
         
        """
        pass
    @UseFaceCapBlend.setter
    def UseFaceCapBlend(self, useFaceCapBlend: bool):
        """
        Setter for property: (bool) UseFaceCapBlend
         Returns the use face cap blend flag   
            
         
        """
        pass
    @property
    def UsePlaneCapBlend(self) -> bool:
        """
        Getter for property: (bool) UsePlaneCapBlend
         Returns the use plane cap blend   
            
         
        """
        pass
    @UsePlaneCapBlend.setter
    def UsePlaneCapBlend(self, usePlaneCapBlend: bool):
        """
        Setter for property: (bool) UsePlaneCapBlend
         Returns the use plane cap blend   
            
         
        """
        pass
    def CreateLengthLimitPointBuilder(self, mOnPathExp: NXOpen.Expression, mOnPath: OnPathDimensionBuilder, mIsFlipped: bool, mThruPoint: NXOpen.Point) -> LengthLimitPointBuilder:
        """
         Creates a FacePlaneSelectionBuilder
         Returns lengthLimitPointBuilder ( LengthLimitPointBuilder NXOpen.Geome): LengthLimitPointBuilder object .
        """
        pass
import NXOpen
class PointSetAlignmentBuilder(NXOpen.Builder): 
    """ This class performs a point set to point set alignment """
    class ConstraintOptions(Enum):
        """
        Members Include: 
         |NotSet|  No constraint 
         |X|  X axis 
         |Y|  Y axis 
         |Z|  Z axis 

        """
        NotSet: int
        X: int
        Y: int
        Z: int
        @staticmethod
        def ValueOf(value: int) -> PointSetAlignmentBuilder.ConstraintOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Constraint(self) -> PointSetAlignmentBuilder.ConstraintOptions:
        """
        Getter for property: ( PointSetAlignmentBuilder.ConstraintOptions NXOpen.Geome) Constraint
         Returns the constraint   
            
         
        """
        pass
    @Constraint.setter
    def Constraint(self, constraint: PointSetAlignmentBuilder.ConstraintOptions):
        """
        Setter for property: ( PointSetAlignmentBuilder.ConstraintOptions NXOpen.Geome) Constraint
         Returns the constraint   
            
         
        """
        pass
    @property
    def FromPointSet(self) -> NXOpen.SelectPointList:
        """
        Getter for property: ( NXOpen.SelectPointList) FromPointSet
         Returns the "from" point set   
            
         
        """
        pass
    @property
    def ObjectsToMove(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) ObjectsToMove
         Returns the objects to move   
            
         
        """
        pass
    @property
    def ToPointSet(self) -> NXOpen.SelectPointList:
        """
        Getter for property: ( NXOpen.SelectPointList) ToPointSet
         Returns the "to" point set   
            
         
        """
        pass
import NXOpen
class PointsFromFileBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.GeometricUtilities.PointsFromFileBuilder builder
    read points from a text file with format .asc, .txt, .dat, .pts
    """
    class Options(Enum):
        """
        Members Include: 
         |Absolute|  Absolute coordinates
         |Wcs|  Work coordinates 

        """
        Absolute: int
        Wcs: int
        @staticmethod
        def ValueOf(value: int) -> PointsFromFileBuilder.Options:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CoordinateOption(self) -> PointsFromFileBuilder.Options:
        """
        Getter for property: ( PointsFromFileBuilder.Options NXOpen.Geome) CoordinateOption
         Returns the option indicating type of point coordinates   
            
         
        """
        pass
    @CoordinateOption.setter
    def CoordinateOption(self, option: PointsFromFileBuilder.Options):
        """
        Setter for property: ( PointsFromFileBuilder.Options NXOpen.Geome) CoordinateOption
         Returns the option indicating type of point coordinates   
            
         
        """
        pass
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
         Returns the file name of the point data file   
            
         
        """
        pass
    @FileName.setter
    def FileName(self, filename: str):
        """
        Setter for property: (str) FileName
         Returns the file name of the point data file   
            
         
        """
        pass
    @property
    def PathName(self) -> str:
        """
        Getter for property: (str) PathName
         Returns the path name of the point data file   
            
         
        """
        pass
    @PathName.setter
    def PathName(self, pathname: str):
        """
        Setter for property: (str) PathName
         Returns the path name of the point data file   
            
         
        """
        pass
import NXOpen
class PolygonPatternSpacing(PatternSpacing): 
    """ defines the various ways pattern instances can be 
        spaced within the pattern, particularly in the context of the
        PatternDefinition class. """
    @property
    def PitchDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PitchDistance
         Returns the pitch distance along one side for the spacing of the pattern from one instance to the next.  
            
         
        """
        pass
    @property
    def SpanAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SpanAngle
         Returns the angle for the spacing of the pattern for the entire pattern.  
             
         
        """
        pass
import NXOpen
class PolygonPattern(NXOpen.TaggedObject): 
    """ the polygon pattern definition.  Allows specification along
        both the angular and radial directions. """
    class SizeOptions(Enum):
        """
        Members Include: 
         |Inscribed|  use inscribed circle to define a polygon 
         |Circumscribed|  use circumscribed circle to define a polygon 

        """
        Inscribed: int
        Circumscribed: int
        @staticmethod
        def ValueOf(value: int) -> PolygonPattern.SizeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Flip(self) -> bool:
        """
        Getter for property: (bool) Flip
         Returns the flip object for 2D mode.  
            This function gets the flip attribute of the 2D pattern.   
         
        """
        pass
    @Flip.setter
    def Flip(self, enabled: bool):
        """
        Setter for property: (bool) Flip
         Returns the flip object for 2D mode.  
            This function gets the flip attribute of the 2D pattern.   
         
        """
        pass
    @property
    def HorizontalRef(self) -> HorizontalReference:
        """
        Getter for property: ( HorizontalReference NXOpen.Geome) HorizontalRef
         Returns the horizontal reference   
            
         
        """
        pass
    @property
    def NumberOfSides(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NumberOfSides
         Returns the number of sides for the polygon type pattern will generated in this direction   
            
         
        """
        pass
    @property
    def PolygonSizeOption(self) -> PolygonPattern.SizeOptions:
        """
        Getter for property: ( PolygonPattern.SizeOptions NXOpen.Geome) PolygonSizeOption
         Returns the polygon size option   
            
         
        """
        pass
    @PolygonSizeOption.setter
    def PolygonSizeOption(self, option: PolygonPattern.SizeOptions):
        """
        Setter for property: ( PolygonPattern.SizeOptions NXOpen.Geome) PolygonSizeOption
         Returns the polygon size option   
            
         
        """
        pass
    @property
    def PolygonSpacing(self) -> PolygonPatternSpacing:
        """
        Getter for property: ( PolygonPatternSpacing NXOpen.Geome) PolygonSpacing
         Returns the polygon spacing of the instances of the pattern  
            
         
        """
        pass
    @property
    def RadialSpacing(self) -> DistancePatternSpacing:
        """
        Getter for property: ( DistancePatternSpacing NXOpen.Geome) RadialSpacing
         Returns the radial spacing of the instances of the pattern   
            
         
        """
        pass
    @property
    def RotationAxis(self) -> NXOpen.Axis:
        """
        Getter for property: ( NXOpen.Axis) RotationAxis
         Returns the rotation axis for the pattern.  
             
         
        """
        pass
    @RotationAxis.setter
    def RotationAxis(self, rotationAxis: NXOpen.Axis):
        """
        Setter for property: ( NXOpen.Axis) RotationAxis
         Returns the rotation axis for the pattern.  
             
         
        """
        pass
    @property
    def RotationCenter(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) RotationCenter
         Returns the rotation center for the 2d pattern.  
             
         
        """
        pass
    @RotationCenter.setter
    def RotationCenter(self, rotationCenter: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) RotationCenter
         Returns the rotation center for the 2d pattern.  
             
         
        """
        pass
    @property
    def UseRadialDirectionToggle(self) -> bool:
        """
        Getter for property: (bool) UseRadialDirectionToggle
         Returns the UseRadialDirection toggle attribute.  
           This function gets the UseRadialDirection toggle value   
         
        """
        pass
    @UseRadialDirectionToggle.setter
    def UseRadialDirectionToggle(self, toggle: bool):
        """
        Setter for property: (bool) UseRadialDirectionToggle
         Returns the UseRadialDirection toggle attribute.  
           This function gets the UseRadialDirection toggle value   
         
        """
        pass
import NXOpen
class ProjectionOptions(NXOpen.TaggedObject): 
    """ Represents a ProjectionOptions """
    class DirectionType(Enum):
        """
        Members Include: 
         |FaceNormal|  Face Normal 
         |CrvPlaneNormal|  Curve plane Normal 
         |Vector|  Vector Constructor 

        """
        FaceNormal: int
        CrvPlaneNormal: int
        Vector: int
        @staticmethod
        def ValueOf(value: int) -> ProjectionOptions.DirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ProjectDirectionMethod(self) -> ProjectionOptions.DirectionType:
        """
        Getter for property: ( ProjectionOptions.DirectionType NXOpen.Geome) ProjectDirectionMethod
         Returns  the Projection direction method   
            
         
        """
        pass
    @ProjectDirectionMethod.setter
    def ProjectDirectionMethod(self, project_direction_method: ProjectionOptions.DirectionType):
        """
        Setter for property: ( ProjectionOptions.DirectionType NXOpen.Geome) ProjectDirectionMethod
         Returns  the Projection direction method   
            
         
        """
        pass
    @property
    def ProjectVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ProjectVector
         Returns the Projection vector   
            
         
        """
        pass
    @ProjectVector.setter
    def ProjectVector(self, project_direction: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ProjectVector
         Returns the Projection vector   
            
         
        """
        pass
class QuadrilateralFrameBuilder(ShapeFrameBuilder): 
    """ Represents a NXOpen.GeometricUtilities.QuadrilateralFrameBuilder """
    class Subtypes(Enum):
        """
        Members Include: 
         |Arbitrary|  Arbitrary quadrilateral 
         |Parallelogram|  Parallelogram 
         |Rectangle|  Rectangle 
         |Square|  Square 

        """
        Arbitrary: int
        Parallelogram: int
        Rectangle: int
        Square: int
        @staticmethod
        def ValueOf(value: int) -> QuadrilateralFrameBuilder.Subtypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Subtype(self) -> QuadrilateralFrameBuilder.Subtypes:
        """
        Getter for property: ( QuadrilateralFrameBuilder.Subtypes NXOpen.Geome) Subtype
         Returns the subtype   
            
         
        """
        pass
    @Subtype.setter
    def Subtype(self, subtype: QuadrilateralFrameBuilder.Subtypes):
        """
        Setter for property: ( QuadrilateralFrameBuilder.Subtypes NXOpen.Geome) Subtype
         Returns the subtype   
            
         
        """
        pass
class RadiusMethod(Enum):
    """
    Members Include: 
     |Constant|  Constant 
     |Law|  Control by law 
     |Tangency|  Control by tangency 

    """
    Constant: int
    Law: int
    Tangency: int
    @staticmethod
    def ValueOf(value: int) -> RadiusMethod:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class Rebuild(NXOpen.TaggedObject): 
    """ Represents a NXOpen.GeometricUtilities.Rebuild.
    The Rebuild block provides control over the method in which a surface is rebuilt (None, Manual,
    Advanced). Rebuild can be used for both uni-directional and bi-directional rebuild functions. 
    Uni-directional functions require one instance of the rebuild block while bi-directional functions 
    require two instances of the Rebuild block.
    """
    class DegreeTypes(Enum):
        """
        Members Include: 
         |Cubic|  The rebuild degree is cubic. 
         |Quintic|  The rebuild degree is quintic 

        """
        Cubic: int
        Quintic: int
        @staticmethod
        def ValueOf(value: int) -> Rebuild.DegreeTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RebuildTypes(Enum):
        """
        Members Include: 
         |NotSet|  No degree entry or simple integerenumerable value used to specify the rebuild degree.
         |Manual|  Specify the rebuild degree manually. 
         |Advanced|  Specify the maximum degree and maximum segments to rebuild.
         |KeepParameterization|  Keep the parameterization 

        """
        NotSet: int
        Manual: int
        Advanced: int
        KeepParameterization: int
        @staticmethod
        def ValueOf(value: int) -> Rebuild.RebuildTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Degree(self) -> int:
        """
        Getter for property: (int) Degree
         Returns the degree when rebuild type is none.  
          
                    In general, the degree is limited from 1 to 24. However,degree = 1 will only be used for 
                    Through Curve case to replace the current V-degree option, which can start from 1. 
                    Otherwise the minimum degree should be 2.
                    
         
        """
        pass
    @Degree.setter
    def Degree(self, degree: int):
        """
        Setter for property: (int) Degree
         Returns the degree when rebuild type is none.  
          
                    In general, the degree is limited from 1 to 24. However,degree = 1 will only be used for 
                    Through Curve case to replace the current V-degree option, which can start from 1. 
                    Otherwise the minimum degree should be 2.
                    
         
        """
        pass
    @property
    def DegreeType(self) -> Rebuild.DegreeTypes:
        """
        Getter for property: ( Rebuild.DegreeTypes NXOpen.Geome) DegreeType
         Returns the degree type when rebuild type is none.  
           
                  
         
        """
        pass
    @DegreeType.setter
    def DegreeType(self, degreeType: Rebuild.DegreeTypes):
        """
        Setter for property: ( Rebuild.DegreeTypes NXOpen.Geome) DegreeType
         Returns the degree type when rebuild type is none.  
           
                  
         
        """
        pass
    @property
    def ManualDegree(self) -> int:
        """
        Getter for property: (int) ManualDegree
         Returns the degree when rebuild type is manual.  
          
                    The degree value is limited from 2 to 24.
                  
         
        """
        pass
    @ManualDegree.setter
    def ManualDegree(self, manualDegree: int):
        """
        Setter for property: (int) ManualDegree
         Returns the degree when rebuild type is manual.  
          
                    The degree value is limited from 2 to 24.
                  
         
        """
        pass
    @property
    def MaximumDegree(self) -> int:
        """
        Getter for property: (int) MaximumDegree
         Returns the maximum degree when rebuild type is advanced.  
           
                    The maximum degree value is limited from 2 to 24.
                  
         
        """
        pass
    @MaximumDegree.setter
    def MaximumDegree(self, maximumDegree: int):
        """
        Setter for property: (int) MaximumDegree
         Returns the maximum degree when rebuild type is advanced.  
           
                    The maximum degree value is limited from 2 to 24.
                  
         
        """
        pass
    @property
    def MaximumSegments(self) -> int:
        """
        Getter for property: (int) MaximumSegments
         Returns the maximum segments when rebuild type is advanced.  
           
                    The maximum segments value is limited from 1 to 1000.
                  
         
        """
        pass
    @MaximumSegments.setter
    def MaximumSegments(self, maximumSegments: int):
        """
        Setter for property: (int) MaximumSegments
         Returns the maximum segments when rebuild type is advanced.  
           
                    The maximum segments value is limited from 1 to 1000.
                  
         
        """
        pass
    @property
    def RebuildType(self) -> Rebuild.RebuildTypes:
        """
        Getter for property: ( Rebuild.RebuildTypes NXOpen.Geome) RebuildType
         Returns the rebuild type.  
          
                  
         
        """
        pass
    @RebuildType.setter
    def RebuildType(self, rebuildType: Rebuild.RebuildTypes):
        """
        Setter for property: ( Rebuild.RebuildTypes NXOpen.Geome) RebuildType
         Returns the rebuild type.  
          
                  
         
        """
        pass
import NXOpen
class RectangularFrameBuilder(NXOpen.TaggedObject): 
    """ Rectangular frame builder """
    class AnchorLocationType(Enum):
        """
        Members Include: 
         |TopLeft|  Top left position 
         |TopCenter|  Top center position 
         |TopRight|  Top right position 
         |MiddleLeft|  Middle left position 
         |MiddleCenter|  Middle center position 
         |MiddleRight|  Middle right position 
         |BottomLeft|  Bottom left position 
         |BottomCenter|  Bottom center position 
         |BottomRight|  Bottom right position 

        """
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
        def ValueOf(value: int) -> RectangularFrameBuilder.AnchorLocationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AnchorLocation(self) -> RectangularFrameBuilder.AnchorLocationType:
        """
        Getter for property: ( RectangularFrameBuilder.AnchorLocationType NXOpen.Geome) AnchorLocation
         Returns the anchor location   
            
         
        """
        pass
    @AnchorLocation.setter
    def AnchorLocation(self, anchorLocation: RectangularFrameBuilder.AnchorLocationType):
        """
        Setter for property: ( RectangularFrameBuilder.AnchorLocationType NXOpen.Geome) AnchorLocation
         Returns the anchor location   
            
         
        """
        pass
    @property
    def AnchorLocator(self) -> NXOpen.SelectSmartObject:
        """
        Getter for property: ( NXOpen.SelectSmartObject) AnchorLocator
         Returns the point or coordinate system to define initial location and orientation of the frame   
            
         
        """
        pass
    @property
    def CoordinateSystem(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) CoordinateSystem
         Returns the coordinate system   
            
         
        """
        pass
    @CoordinateSystem.setter
    def CoordinateSystem(self, coordinateSystem: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) CoordinateSystem
         Returns the coordinate system   
            
         
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
    def Length(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Length
         Returns the length   
            
         
        """
        pass
    @property
    def LockAspectRatio(self) -> bool:
        """
        Getter for property: (bool) LockAspectRatio
         Returns a flag indicating if aspect ratio is locked   
            
         
        """
        pass
    @LockAspectRatio.setter
    def LockAspectRatio(self, lockAspectRatio: bool):
        """
        Setter for property: (bool) LockAspectRatio
         Returns a flag indicating if aspect ratio is locked   
            
         
        """
        pass
    @property
    def Shear(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Shear
         Returns the shear   
            
         
        """
        pass
    @property
    def WScale(self) -> float:
        """
        Getter for property: (float) WScale
         Returns the width scale   
            
         
        """
        pass
    @WScale.setter
    def WScale(self, wScale: float):
        """
        Setter for property: (float) WScale
         Returns the width scale   
            
         
        """
        pass
    def EditCoordinateSystem(self, origin: NXOpen.Point, csys: NXOpen.Matrix3x3) -> None:
        """
         Edits current coordinate system. 
        """
        pass
    def UpdateOnCoordinateSystem(self) -> None:
        """
         Updates the frame based on coordinate system. 
        """
        pass
import NXOpen
class RectangularPattern(NXOpen.TaggedObject): 
    """ the rectangular pattern definition.  Allows specification along
        two linear axes, which may or may not be orthogonal. """
    class SimplifiedLayoutTypes(Enum):
        """
        Members Include: 
         |Square|  Square Layout 
         |Triangle|  Triangle Layout 
         |Diamond|  Diamond Layout 

        """
        Square: int
        Triangle: int
        Diamond: int
        @staticmethod
        def ValueOf(value: int) -> RectangularPattern.SimplifiedLayoutTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StaggerOptions(Enum):
        """
        Members Include: 
         |NotSet|  No stagger applied 
         |Row|  Stagger row 
         |Column|  Stagger column 

        """
        NotSet: int
        Row: int
        Column: int
        @staticmethod
        def ValueOf(value: int) -> RectangularPattern.StaggerOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CreateLastStaggered(self) -> bool:
        """
        Getter for property: (bool) CreateLastStaggered
         Returns the option to generate the last item in a staggered row.  
            If 'true' the pattern will be
                    narrower on rows that have been staggered.   
         
        """
        pass
    @CreateLastStaggered.setter
    def CreateLastStaggered(self, create: bool):
        """
        Setter for property: (bool) CreateLastStaggered
         Returns the option to generate the last item in a staggered row.  
            If 'true' the pattern will be
                    narrower on rows that have been staggered.   
         
        """
        pass
    @property
    def HorizontalRef(self) -> HorizontalReference:
        """
        Getter for property: ( HorizontalReference NXOpen.Geome) HorizontalRef
         Returns the horizontal reference   
            
         
        """
        pass
    @property
    def SimplifiedLayoutType(self) -> RectangularPattern.SimplifiedLayoutTypes:
        """
        Getter for property: ( RectangularPattern.SimplifiedLayoutTypes NXOpen.Geome) SimplifiedLayoutType
         Returns the simplified layout type to be used by the pattern   
            
         
        """
        pass
    @SimplifiedLayoutType.setter
    def SimplifiedLayoutType(self, type: RectangularPattern.SimplifiedLayoutTypes):
        """
        Setter for property: ( RectangularPattern.SimplifiedLayoutTypes NXOpen.Geome) SimplifiedLayoutType
         Returns the simplified layout type to be used by the pattern   
            
         
        """
        pass
    @property
    def StaggerType(self) -> RectangularPattern.StaggerOptions:
        """
        Getter for property: ( RectangularPattern.StaggerOptions NXOpen.Geome) StaggerType
         Returns the type of stagger to be used by the pattern   
            
         
        """
        pass
    @StaggerType.setter
    def StaggerType(self, staggerType: RectangularPattern.StaggerOptions):
        """
        Setter for property: ( RectangularPattern.StaggerOptions NXOpen.Geome) StaggerType
         Returns the type of stagger to be used by the pattern   
            
         
        """
        pass
    @property
    def UseYDirectionToggle(self) -> bool:
        """
        Getter for property: (bool) UseYDirectionToggle
         Returns the UseYDirection toggle attribute.  
           This function gets the UseYDirection toggle value   
         
        """
        pass
    @UseYDirectionToggle.setter
    def UseYDirectionToggle(self, toggle: bool):
        """
        Setter for property: (bool) UseYDirectionToggle
         Returns the UseYDirection toggle attribute.  
           This function gets the UseYDirection toggle value   
         
        """
        pass
    @property
    def XDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) XDirection
         Returns the x axis   
            
         
        """
        pass
    @XDirection.setter
    def XDirection(self, xDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) XDirection
         Returns the x axis   
            
         
        """
        pass
    @property
    def XFlip(self) -> bool:
        """
        Getter for property: (bool) XFlip
         Returns the XSelection flip attribute.  
           This function flips X selection object of the 2D pattern   
         
        """
        pass
    @XFlip.setter
    def XFlip(self, xFlip: bool):
        """
        Setter for property: (bool) XFlip
         Returns the XSelection flip attribute.  
           This function flips X selection object of the 2D pattern   
         
        """
        pass
    @property
    def XSelection(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) XSelection
         Returns the direction object.  
           This function gets X direction object of the 2D pattern. This call will result in an Exception if not called in 2D mode.   
         
        """
        pass
    @property
    def XSpacing(self) -> DistancePatternSpacing:
        """
        Getter for property: ( DistancePatternSpacing NXOpen.Geome) XSpacing
         Returns the instance spacing along the x axis   
            
         
        """
        pass
    @property
    def XSymmetryToggle(self) -> bool:
        """
        Getter for property: (bool) XSymmetryToggle
         Returns the XSymmetry toggle attribute.  
           This function gets the x Symmetry toggle value   
         
        """
        pass
    @XSymmetryToggle.setter
    def XSymmetryToggle(self, toggle: bool):
        """
        Setter for property: (bool) XSymmetryToggle
         Returns the XSymmetry toggle attribute.  
           This function gets the x Symmetry toggle value   
         
        """
        pass
    @property
    def YDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) YDirection
         Returns the y axis, which can be any vector not parallel to the x axis   
            
         
        """
        pass
    @YDirection.setter
    def YDirection(self, yDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) YDirection
         Returns the y axis, which can be any vector not parallel to the x axis   
            
         
        """
        pass
    @property
    def YFlip(self) -> bool:
        """
        Getter for property: (bool) YFlip
         Returns the YSelection flip attribute.  
           This function flips Y selection object of the 2D pattern   
         
        """
        pass
    @YFlip.setter
    def YFlip(self, xFlip: bool):
        """
        Setter for property: (bool) YFlip
         Returns the YSelection flip attribute.  
           This function flips Y selection object of the 2D pattern   
         
        """
        pass
    @property
    def YSelection(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) YSelection
         Returns the direction object.  
           This function gets Y direction object of the 2D pattern. This call will result in an Exception if not called in 2D mode.   
         
        """
        pass
    @property
    def YSpacing(self) -> DistancePatternSpacing:
        """
        Getter for property: ( DistancePatternSpacing NXOpen.Geome) YSpacing
         Returns the instance spacing along the y axis   
            
         
        """
        pass
    @property
    def YSymmetryToggle(self) -> bool:
        """
        Getter for property: (bool) YSymmetryToggle
         Returns the YSymmetry toggle attribute.  
           This function gets the y Symmetry toggle value   
         
        """
        pass
    @YSymmetryToggle.setter
    def YSymmetryToggle(self, toggle: bool):
        """
        Setter for property: (bool) YSymmetryToggle
         Returns the YSymmetry toggle attribute.  
           This function gets the y Symmetry toggle value   
         
        """
        pass
import NXOpen
class ReduceSurfaceRadiusBuilder(NXOpen.Builder): 
    """ Reduce Surface Radius Builder of Geometric Utilities. This builder's Commit can produce more than one object, 
        the GetCommittedObjects can be used to get the objects. """
    class FaceSelectionSpecification(Enum):
        """
        Members Include: 
         |Radius| 
         |Chain| 
         |Select| 

        """
        Radius: int
        Chain: int
        Select: int
        @staticmethod
        def ValueOf(value: int) -> ReduceSurfaceRadiusBuilder.FaceSelectionSpecification:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ReduceValueTypeSpecification(Enum):
        """
        Members Include: 
         |Percentage| 
         |Value| 
         |Delta| 

        """
        Percentage: int
        Value: int
        Delta: int
        @staticmethod
        def ValueOf(value: int) -> ReduceSurfaceRadiusBuilder.ReduceValueTypeSpecification:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ReducedFaceTypeSpecification(Enum):
        """
        Members Include: 
         |FaceGroup|  Preview all items in face group list when using "Select Faces by Radius" to select input objects. 
         |SingleChainInGroup|  Preview single item in face group list when using "Select Faces by Radius" to select input objects. 
         |SingleChain|  Preview single chain when using "Select Faces by Chain" and "Single Selection" to select input objects. 

        """
        FaceGroup: int
        SingleChainInGroup: int
        SingleChain: int
        @staticmethod
        def ValueOf(value: int) -> ReduceSurfaceRadiusBuilder.ReducedFaceTypeSpecification:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Direction(self) -> bool:
        """
        Getter for property: (bool) Direction
         Returns the direction which specifies concave face respect to the body face normal   
            
         
        """
        pass
    @Direction.setter
    def Direction(self, direction: bool):
        """
        Setter for property: (bool) Direction
         Returns the direction which specifies concave face respect to the body face normal   
            
         
        """
        pass
    @property
    def FaceGroupList(self) -> ReduceSurfaceRadiusFaceGroupBuilderList:
        """
        Getter for property: ( ReduceSurfaceRadiusFaceGroupBuilderList NXOpen.Geome) FaceGroupList
         Returns the list containing the face chains as input objects used to do reduction.  
            
         
        """
        pass
    @property
    def HighRadius(self) -> float:
        """
        Getter for property: (float) HighRadius
         Returns the high radius which specifies lower limit to filter out all qualified faces   
            
         
        """
        pass
    @HighRadius.setter
    def HighRadius(self, highRadius: float):
        """
        Setter for property: (float) HighRadius
         Returns the high radius which specifies lower limit to filter out all qualified faces   
            
         
        """
        pass
    @property
    def IndexListItem(self) -> int:
        """
        Getter for property: (int) IndexListItem
         Returns the index of list item   
            
         
        """
        pass
    @IndexListItem.setter
    def IndexListItem(self, index: int):
        """
        Setter for property: (int) IndexListItem
         Returns the index of list item   
            
         
        """
        pass
    @property
    def LowRadius(self) -> float:
        """
        Getter for property: (float) LowRadius
         Returns the low radius which specifies lower limit to filter out all qualified faces   
            
         
        """
        pass
    @LowRadius.setter
    def LowRadius(self, lowRadius: float):
        """
        Setter for property: (float) LowRadius
         Returns the low radius which specifies lower limit to filter out all qualified faces   
            
         
        """
        pass
    @property
    def OnPathDimEnd(self) -> OnPathDimensionBuilder:
        """
        Getter for property: ( OnPathDimensionBuilder NXOpen.Geome) OnPathDimEnd
         Returns the end position of reduced sheet body   
            
         
        """
        pass
    @property
    def OnPathDimStart(self) -> OnPathDimensionBuilder:
        """
        Getter for property: ( OnPathDimensionBuilder NXOpen.Geome) OnPathDimStart
         Returns the start position of reduced sheet body   
            
         
        """
        pass
    @property
    def PercentReduction(self) -> float:
        """
        Getter for property: (float) PercentReduction
         Returns the value of percentage reduction method   
            
         
        """
        pass
    @PercentReduction.setter
    def PercentReduction(self, percentReduction: float):
        """
        Setter for property: (float) PercentReduction
         Returns the value of percentage reduction method   
            
         
        """
        pass
    @property
    def PositionTolerance(self) -> float:
        """
        Getter for property: (float) PositionTolerance
         Returns the position tolerance between two faces connection   
            
         
        """
        pass
    @PositionTolerance.setter
    def PositionTolerance(self, positionTolerance: float):
        """
        Setter for property: (float) PositionTolerance
         Returns the position tolerance between two faces connection   
            
         
        """
        pass
    @property
    def ReduceValueType(self) -> ReduceSurfaceRadiusBuilder.ReduceValueTypeSpecification:
        """
        Getter for property: ( ReduceSurfaceRadiusBuilder.ReduceValueTypeSpecification NXOpen.Geome) ReduceValueType
         Returns the type of reduced value which results surface shape   
            
         
        """
        pass
    @ReduceValueType.setter
    def ReduceValueType(self, reduceValueType: ReduceSurfaceRadiusBuilder.ReduceValueTypeSpecification):
        """
        Setter for property: ( ReduceSurfaceRadiusBuilder.ReduceValueTypeSpecification NXOpen.Geome) ReduceValueType
         Returns the type of reduced value which results surface shape   
            
         
        """
        pass
    @property
    def ReducedFaceType(self) -> ReduceSurfaceRadiusBuilder.ReducedFaceTypeSpecification:
        """
        Getter for property: ( ReduceSurfaceRadiusBuilder.ReducedFaceTypeSpecification NXOpen.Geome) ReducedFaceType
         Returns the type of performing the radius reduction preview   
            
         
        """
        pass
    @ReducedFaceType.setter
    def ReducedFaceType(self, reducedFaceType: ReduceSurfaceRadiusBuilder.ReducedFaceTypeSpecification):
        """
        Setter for property: ( ReduceSurfaceRadiusBuilder.ReducedFaceTypeSpecification NXOpen.Geome) ReducedFaceType
         Returns the type of performing the radius reduction preview   
            
         
        """
        pass
    @property
    def SelectChain(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SelectChain
         Returns the selected entities for performing the radius reduction operation, which selected by "Select Faces by Chain" and "Single Selection"   
            
         
        """
        pass
    @property
    def SelectFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SelectFace
         Returns the selected entities for performing the radius reduction operation, which selected by "Select Faces by Radius"   
            
         
        """
        pass
    @property
    def TangentTolerance(self) -> float:
        """
        Getter for property: (float) TangentTolerance
         Returns the tangent tolerance between two faces connection   
            
         
        """
        pass
    @TangentTolerance.setter
    def TangentTolerance(self, tangentTolerance: float):
        """
        Setter for property: (float) TangentTolerance
         Returns the tangent tolerance between two faces connection   
            
         
        """
        pass
    @property
    def TargetReduction(self) -> float:
        """
        Getter for property: (float) TargetReduction
         Returns the target value method   
            
         
        """
        pass
    @TargetReduction.setter
    def TargetReduction(self, targetReduction: float):
        """
        Setter for property: (float) TargetReduction
         Returns the target value method   
            
         
        """
        pass
    @property
    def ValueReduction(self) -> float:
        """
        Getter for property: (float) ValueReduction
         Returns the value of reduction value method   
            
         
        """
        pass
    @ValueReduction.setter
    def ValueReduction(self, valueReduction: float):
        """
        Setter for property: (float) ValueReduction
         Returns the value of reduction value method   
            
         
        """
        pass
import NXOpen
class ReduceSurfaceRadiusFaceGroupBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[ReduceSurfaceRadiusFaceGroupBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: ReduceSurfaceRadiusFaceGroupBuilder) -> None:
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
    def Erase(self, obj: ReduceSurfaceRadiusFaceGroupBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: ReduceSurfaceRadiusFaceGroupBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: ReduceSurfaceRadiusFaceGroupBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> ReduceSurfaceRadiusFaceGroupBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( ReduceSurfaceRadiusFaceGroupBuilder NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[ReduceSurfaceRadiusFaceGroupBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( ReduceSurfaceRadiusFaceGroupBuilder List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: ReduceSurfaceRadiusFaceGroupBuilder) -> None:
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
    def SetContents(self, objects: List[ReduceSurfaceRadiusFaceGroupBuilder]) -> None:
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
    def Swap(self, object1: ReduceSurfaceRadiusFaceGroupBuilder, object2: ReduceSurfaceRadiusFaceGroupBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class ReduceSurfaceRadiusFaceGroupBuilder(NXOpen.Builder): 
    """ Reduce Surface Radius Face Group Builder of Geometric Utilities. No object is returned by this builder. """
    @property
    def EndLimit(self) -> OnPathDimensionBuilder:
        """
        Getter for property: ( OnPathDimensionBuilder NXOpen.Geome) EndLimit
         Returns the end position of reduced sheet body   
            
         
        """
        pass
    @property
    def SelectFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SelectFace
         Returns the selected entities of single chain for performing radius reduction   
            
         
        """
        pass
    @property
    def StartLimit(self) -> OnPathDimensionBuilder:
        """
        Getter for property: ( OnPathDimensionBuilder NXOpen.Geome) StartLimit
         Returns the start position of reduced sheet body   
            
         
        """
        pass
import NXOpen
class ReferencePattern(NXOpen.TaggedObject): 
    """ the reference pattern definition. """
    @property
    def ReferencedPattern(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) ReferencedPattern
         Returns the referenced pattern object.  
            
         
        """
        pass
    def ResetBaseInstance(self) -> None:
        """
         Reset the base instance indices to an "undefined" state. The base instance will be reset
                    so that the indices do not correspond to indices from any instance of the referenced 
                    pattern selected. The base instance indices must be set after this call before commit. 
        """
        pass
    def SetBaseInstance(self, firstIndex: int, secondIndex: int) -> None:
        """
         Set the base instance 
        """
        pass
import NXOpen
class RefitControlBuilder(NXOpen.TaggedObject): 
    """ This class is used to specify the parameter set to refit faces """
    class RefitControlDirection(Enum):
        """
        Members Include: 
         |UV|  u and v 
         |U|  u  
         |V|  v  

        """
        UV: int
        U: int
        V: int
        @staticmethod
        def ValueOf(value: int) -> RefitControlBuilder.RefitControlDirection:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RefitControlMethod(Enum):
        """
        Members Include: 
         |KeepParameterization|  Keep parameterization 
         |DegreePatches|  Degree and patches  
         |DegreeTolerance|  Degree and tolerance  
         |PatchTolerance|  Patch and tolerance  

        """
        KeepParameterization: int
        DegreePatches: int
        DegreeTolerance: int
        PatchTolerance: int
        @staticmethod
        def ValueOf(value: int) -> RefitControlBuilder.RefitControlMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DegreesAndSegmentsOrPatches(self) -> DegreesAndSegmentsOrPatchesBuilder:
        """
        Getter for property: ( DegreesAndSegmentsOrPatchesBuilder NXOpen.Geome) DegreesAndSegmentsOrPatches
         Returns the refit degrees and  segments or patches       
            
         
        """
        pass
    @property
    def RefitDirection(self) -> RefitControlBuilder.RefitControlDirection:
        """
        Getter for property: ( RefitControlBuilder.RefitControlDirection NXOpen.Geome) RefitDirection
         Returns the refit direction   
            
         
        """
        pass
    @RefitDirection.setter
    def RefitDirection(self, refitDirection: RefitControlBuilder.RefitControlDirection):
        """
        Setter for property: ( RefitControlBuilder.RefitControlDirection NXOpen.Geome) RefitDirection
         Returns the refit direction   
            
         
        """
        pass
    @property
    def RefitMethod(self) -> RefitControlBuilder.RefitControlMethod:
        """
        Getter for property: ( RefitControlBuilder.RefitControlMethod NXOpen.Geome) RefitMethod
         Returns the refit method   
            
         
        """
        pass
    @RefitMethod.setter
    def RefitMethod(self, refitMethod: RefitControlBuilder.RefitControlMethod):
        """
        Setter for property: ( RefitControlBuilder.RefitControlMethod NXOpen.Geome) RefitMethod
         Returns the refit method   
            
         
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
import NXOpen
class RegionTracker(NXOpen.TaggedObject): 
    """ a class which collects all the geometric entities used to identify a region of faces during a boolean feature. 
      """
    class ExtremityType(Enum):
        """
        Members Include: 
         |Start|  start 
         |End|  end   

        """
        Start: int
        End: int
        @staticmethod
        def ValueOf(value: int) -> RegionTracker.ExtremityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Added(self) -> bool:
        """
        Getter for property: (bool) Added
         Returns a flag indicating if the region is addedselected by the user   
            
         
        """
        pass
    @Added.setter
    def Added(self, isAdded: bool):
        """
        Setter for property: (bool) Added
         Returns a flag indicating if the region is addedselected by the user   
            
         
        """
        pass
    @property
    def OnTool(self) -> bool:
        """
        Getter for property: (bool) OnTool
         Returns a flag indicating if the region belongs to the tool (true) or to the target (false)   
            
         
        """
        pass
    @OnTool.setter
    def OnTool(self, isOnTool: bool):
        """
        Setter for property: (bool) OnTool
         Returns a flag indicating if the region belongs to the tool (true) or to the target (false)   
            
         
        """
        pass
    @property
    def Removed(self) -> bool:
        """
        Getter for property: (bool) Removed
         Returns a flag indicating if the region is removeddeselected by the user   
            
         
        """
        pass
    @Removed.setter
    def Removed(self, isRemoved: bool):
        """
        Setter for property: (bool) Removed
         Returns a flag indicating if the region is removeddeselected by the user   
            
         
        """
        pass
    def AppendOneBoundaryBody(self, boundaryBodyEid: NXOpen.Body, sideness: bool) -> None:
        """
         Append one new region boundary body to the region tracker 
        """
        pass
    def GetEdgeSelectors(self) -> List[NXOpen.Face]:
        """
         The input target or tool edges used to identify the region 
         Returns entities ( NXOpen.Face Li):  Entities to use as selector .
        """
        pass
    def GetFaceSelectors(self) -> List[NXOpen.Face]:
        """
         The input target or tool faces used to identify the region 
         Returns entities ( NXOpen.Face Li):  Entities to use as selector .
        """
        pass
    def GetOwningBody(self) -> NXOpen.Body:
        """
         The owning body where the region is located onto 
         Returns owningBodyEid ( NXOpen.Body):  region owning entity .
        """
        pass
    def GetVertexSelectors(self) -> Tuple[List[NXOpen.Edge], List[RegionTracker.ExtremityType]]:
        """
         The input target or tool vertices (edge extremities) used to identify the region 
         Returns A tuple consisting of (entities, extremities). 
         - entities is:  NXOpen.Edge Li. Edges associated with the vertex .
         - extremities is:  RegionTracker.ExtremityType List[NXOpen.Geo. Extremity (false : start, true : end) of the edge corresponding to vertex .

        """
        pass
    def SetEdgeSelectors(self, entities: List[NXOpen.Edge]) -> None:
        """
         The input target or tool edges used to identify the region 
        """
        pass
    def SetFaceSelectors(self, entities: List[NXOpen.Face]) -> None:
        """
         The input target or tool faces used to identify the region 
        """
        pass
    def SetOneEdgeSelector(self, entity: NXOpen.Edge) -> None:
        """
         An input target or tool edge used to identify the region 
        """
        pass
    def SetOneFaceSelector(self, entity: NXOpen.Face) -> None:
        """
         An input target or tool face used to identify the region 
        """
        pass
    def SetOnePointSelector(self, location: NXOpen.Point3d) -> None:
        """
         The input point location (x,y,z) used to identify the region 
        """
        pass
    def SetOneVertexSelector(self, entity: NXOpen.Edge, extremity: RegionTracker.ExtremityType) -> None:
        """
         One input target or tool vertex (edge extremity) used to identify the region 
        """
        pass
    def SetOwningBody(self, owningBodyEid: NXOpen.Body) -> None:
        """
         The owning body where the region is located onto 
        """
        pass
    def SetVertexSelectors(self, entities: List[NXOpen.Edge], extremities: List[RegionTracker.ExtremityType]) -> None:
        """
         The input target or tool vertices (edge extremities) used to identify the region 
        """
        pass
import NXOpen
class RenameLinkedPartModulePartBuilder(NXOpen.Builder): 
    """ Represents a Features.PartModule builder """
    def GetAllAssociatedLinkedPartModulePartTags(self, mainPartTag: NXOpen.Part) -> List[NXOpen.Part]:
        """
         Get all linked part module part tags associated with given main part.
                    This function will also load linked parts if they are not loaded. 
         Returns linkedPartTags ( NXOpen.Part Li):  all associated linked part module parts.
        """
        pass
    @overload
    def GetLinkedPartNameToBeSavedAs(self, linkedPartTag: NXOpen.Part) -> str:
        """
         Retrieve new name of linked part module part added earlier for "Save As". 
         Returns fileName (str):  new linked part file name.
        """
        pass
    @overload
    def GetLinkedPartNameToBeSavedAs(self) -> List[str]:
        """
         Retrieve all linked part module parts and their associated new names. 
         Returns fileName (List[str]):  new linked part file name.
        """
        pass
    @overload
    def SetLinkedPartNameToBeSavedAs(self, linkedPartTag: NXOpen.Part, fileName: str) -> None:
        """
         Add linked part module part tag and its new name to perform "Save As" along with its main part. 
        """
        pass
    @overload
    def SetLinkedPartNameToBeSavedAs(self, linkedPartTag: List[NXOpen.Part], fileName: List[str]) -> None:
        """
         Add multiple linked part module part tags and their new names to perform "Save As" along with its main part. 
        """
        pass
import NXOpen
import NXOpen.Features
class RenewFeatureBuilder(NXOpen.Builder): 
    """ Represents a RenewFeatureBuilder object."""
    @property
    def FeatureList(self) -> NXOpen.Features.FeatureList:
        """
        Getter for property: ( NXOpen.Features.FeatureList) FeatureList
         Returns the renew feature list   
            
         
        """
        pass
    @property
    def MakeRenewedFeatureCurrent(self) -> bool:
        """
        Getter for property: (bool) MakeRenewedFeatureCurrent
         Returns the option to make the renewed feature current   
            
         
        """
        pass
    @MakeRenewedFeatureCurrent.setter
    def MakeRenewedFeatureCurrent(self, makeRenewedFeatureCurrent: bool):
        """
        Setter for property: (bool) MakeRenewedFeatureCurrent
         Returns the option to make the renewed feature current   
            
         
        """
        pass
import NXOpen
class ReplaceManager(NXOpen.Object): 
    """ Represents the Replace Manager class."""
    def CreateReplaceManualMatchBuilder(part: NXOpen.Part) -> ReplaceManualMatchBuilder:
        """
         Creates a GeometricUtilities.ReplaceManualMatchBuilder 
         Returns replMatchBuilder ( ReplaceManualMatchBuilder NXOpen.Geome): .
        """
        pass
import NXOpen
class ReplaceManualMatchBuilder(NXOpen.Builder): 
    """ a light-weight builder to keep track of the entities that need manual mapping. 
    The data is stored in form of NXOpen.GeometricUtilities.ReplaceMatchListItem objects """
    @property
    def ReplaceMatchList(self) -> ReplaceMatchListItemList:
        """
        Getter for property: ( ReplaceMatchListItemList NXOpen.Geome) ReplaceMatchList
         Returns the list of all match list objects used in the manual mapping dialog used in stagemodel_replaceDesignPart command  
            
         
        """
        pass
    def CreateReplaceMatchListItem(self, parentEntity: NXOpen.TaggedObject, depName: str, depPartName: str) -> ReplaceMatchListItem:
        """
        Creates a Replace Match Ref builder for manual mapping used in stagemodel_replaceDesignPart command
         Returns replaceMatchListItem ( ReplaceMatchListItem NXOpen.Geome): .
        """
        pass
import NXOpen
class ReplaceMatchListItemList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[ReplaceMatchListItem]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: ReplaceMatchListItem) -> None:
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
    def Erase(self, obj: ReplaceMatchListItem) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: ReplaceMatchListItem, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: ReplaceMatchListItem) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> ReplaceMatchListItem:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( ReplaceMatchListItem NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[ReplaceMatchListItem]:
        """
         Gets the contents of the entire list 
         Returns objects ( ReplaceMatchListItem List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: ReplaceMatchListItem) -> None:
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
    def SetContents(self, objects: List[ReplaceMatchListItem]) -> None:
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
    def Swap(self, object1: ReplaceMatchListItem, object2: ReplaceMatchListItem) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class ReplaceMatchListItem(NXOpen.Builder): 
    """Used to select matches for Replace Design Part Manual Match Dialog """
    pass
import NXOpen
class ReplAsstBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.GeometricUtilities.ReplAsstBuilder. This is the primary data container
    for Replacement Assistant mapping environment available on editing Linked Body, Linked Face, Extract Body, 
    Extract Face and Mirror Body features. Execute Enter() before invoking any match creation or automatic matching APIs.
    Call Exit() to exit the mapping environment.
    """
    @property
    def Allowance(self) -> float:
        """
        Getter for property: (float) Allowance
         Returns the deviation allowance for geometric matching   
            
         
        """
        pass
    @Allowance.setter
    def Allowance(self, allowance: float):
        """
        Setter for property: (float) Allowance
         Returns the deviation allowance for geometric matching   
            
         
        """
        pass
    @property
    def MatchList(self) -> ParentEquivalencyMapList:
        """
        Getter for property: ( ParentEquivalencyMapList NXOpen.Geome) MatchList
         Returns the list of all Parent Equivalency Map objects   
            
         
        """
        pass
    @property
    def MatchObjectsWithDependentsOnly(self) -> bool:
        """
        Getter for property: (bool) MatchObjectsWithDependentsOnly
         Returns the automatic matching preference to match objects with dependents only (if already searched separately)   
            
         
        """
        pass
    @MatchObjectsWithDependentsOnly.setter
    def MatchObjectsWithDependentsOnly(self, matchObjectsWithDependentsOnly: bool):
        """
        Setter for property: (bool) MatchObjectsWithDependentsOnly
         Returns the automatic matching preference to match objects with dependents only (if already searched separately)   
            
         
        """
        pass
    @property
    def MatchSheetBoundariesOnly(self) -> bool:
        """
        Getter for property: (bool) MatchSheetBoundariesOnly
         Returns the automatic matching preference to match sheet boundaries only   
            
         
        """
        pass
    @MatchSheetBoundariesOnly.setter
    def MatchSheetBoundariesOnly(self, sheetBoundariesOnly: bool):
        """
        Setter for property: (bool) MatchSheetBoundariesOnly
         Returns the automatic matching preference to match sheet boundaries only   
            
         
        """
        pass
    @property
    def OneToOne(self) -> bool:
        """
        Getter for property: (bool) OneToOne
         Returns the one to one auto matching preference   
            
         
        """
        pass
    @OneToOne.setter
    def OneToOne(self, oneToOne: bool):
        """
        Setter for property: (bool) OneToOne
         Returns the one to one auto matching preference   
            
         
        """
        pass
    @property
    def UsageInfoList(self) -> EntityUsageInfoList:
        """
        Getter for property: ( EntityUsageInfoList NXOpen.Geome) UsageInfoList
         Returns the list of all Entity Usage Info objects   
            
         
        """
        pass
    def CreateEmptyMatch(self) -> ParentEquivalencyMap:
        """
         This is the default creator for a parent equivalency map. 
         Returns pem ( ParentEquivalencyMap NXOpen.Geome): .
        """
        pass
    def CreateGeometricMaps(self) -> List[ParentEquivalencyMap]:
        """
         Perform geometric matching. 
         Returns maps ( ParentEquivalencyMap List[NXOpen.Geo):  new maps created by geometric matching .
        """
        pass
    def CreateInferredMaps(self) -> List[ParentEquivalencyMap]:
        """
         Infer more matches from matches already 'Accepted'. Add [array_order_guaranteed] annotation for output array when API wrap allows the same.
         Returns maps ( ParentEquivalencyMap List[NXOpen.Geo):  new maps created by inferring .
        """
        pass
    def CreateNameBasedMaps(self) -> List[ParentEquivalencyMap]:
        """
         Perform automatic matching based on user-defined object names. 
         Returns maps ( ParentEquivalencyMap List[NXOpen.Geo):  new maps created by name-based matching .
        """
        pass
    def Enter(self) -> None:
        """
         Entry and re-entry to the Replacement Assistant mapping environment. 
                    This function needs to be executed before invoking any match creation or automatic matching APIs.
                    The matches inferred internally (internal identifier reuse, inherited from parent and siblings)
                    will be populated when this function is executed for the first time after selecting a
                    replacement entity. 
        """
        pass
    def Exit(self) -> None:
        """
         Exit the Replacement Assistant mapping environment. 
                    Any match creation or automatic matchping API cannot be executed after this function is called.
                    
        """
        pass
    def QueryFeatureOutputUsage(self) -> int:
        """
         Query the downstream usage of the current feature's output entities and populate the usageInfoList.
                    This API need be called only ONCE per feature being reparented. 
         Returns nImportantEntititesFound (int): .
        """
        pass
    def SetNewParents(self, replacementObjects: List[NXOpen.DisplayableObject]) -> None:
        """
         Set the source entities for the Replacement Assistant. If there are matches already
                created and the body is changed, the matches will be deleted. 
        """
        pass
    def SetProdInt(self, prodInt: NXOpen.TaggedObject) -> None:
        """
         Set the product interface tag for the Replacement Assistant.  
        """
        pass
import NXOpen
class RodItemBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[RodItemBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: RodItemBuilder) -> None:
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
    def Erase(self, obj: RodItemBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: RodItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: RodItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> RodItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( RodItemBuilder NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[RodItemBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( RodItemBuilder List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: RodItemBuilder) -> None:
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
    def SetContents(self, objects: List[RodItemBuilder]) -> None:
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
    def Swap(self, object1: RodItemBuilder, object2: RodItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class RodItemBuilder(NXOpen.TaggedObject): 
    """ Represents a RodItem """
    class CurveCreateType(Enum):
        """
        Members Include: 
         |ByPoints|  Create by points 
         |ExistingCurves|  Create by existing curves 

        """
        ByPoints: int
        ExistingCurves: int
        @staticmethod
        def ValueOf(value: int) -> RodItemBuilder.CurveCreateType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EndPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) EndPoint
         Returns the end point   
            
         
        """
        pass
    @EndPoint.setter
    def EndPoint(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) EndPoint
         Returns the end point   
            
         
        """
        pass
    @property
    def GraphEdge(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) GraphEdge
         Returns the section defining the unit cell graph.  
           It can contain curves or edges. It is used only if the method is set to existing curves   
         
        """
        pass
    @property
    def Method(self) -> RodItemBuilder.CurveCreateType:
        """
        Getter for property: ( RodItemBuilder.CurveCreateType NXOpen.Geome) Method
         Returnsthe rod creation method.  
           The 2 choices are a rod defined by 2 selected points or a section defined by existing curves.   
         
        """
        pass
    @Method.setter
    def Method(self, method: RodItemBuilder.CurveCreateType):
        """
        Setter for property: ( RodItemBuilder.CurveCreateType NXOpen.Geome) Method
         Returnsthe rod creation method.  
           The 2 choices are a rod defined by 2 selected points or a section defined by existing curves.   
         
        """
        pass
    @property
    def NumberOfSegments(self) -> int:
        """
        Getter for property: (int) NumberOfSegments
         Returns the number of segments of the non-linear curve devided into a polyline   
            
         
        """
        pass
    @NumberOfSegments.setter
    def NumberOfSegments(self, numberOfSegments: int):
        """
        Setter for property: (int) NumberOfSegments
         Returns the number of segments of the non-linear curve devided into a polyline   
            
         
        """
        pass
    @property
    def StartPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) StartPoint
         Returnsthe start point of the rod.  
           Used only if the rod creation method is set to by points.   
         
        """
        pass
    @StartPoint.setter
    def StartPoint(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) StartPoint
         Returnsthe start point of the rod.  
           Used only if the rod creation method is set to by points.   
         
        """
        pass
    def Destroy(self) -> None:
        """
         Deletes a Features.RodItemBuilder 
        """
        pass
import NXOpen
class RodItemListBuilder(NXOpen.TaggedObject): 
    """ Represents a RodItemList """
    @property
    def RodItemList(self) -> RodItemBuilderList:
        """
        Getter for property: ( RodItemBuilderList NXOpen.Geome) RodItemList
         Returns the section defining the unit cell graph.  
           It can contain curves or edges   
         
        """
        pass
    def CreateRodItemBuilder(self) -> RodItemBuilder:
        """
         Creates a Features.RodItemBuilder 
         Returns builder ( RodItemBuilder NXOpen.Geome): .
        """
        pass
import NXOpen
class RotationSetBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[RotationSetBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: RotationSetBuilder) -> None:
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
    def Erase(self, obj: RotationSetBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: RotationSetBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: RotationSetBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> RotationSetBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( RotationSetBuilder NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[RotationSetBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( RotationSetBuilder List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: RotationSetBuilder) -> None:
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
    def SetContents(self, objects: List[RotationSetBuilder]) -> None:
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
    def Swap(self, object1: RotationSetBuilder, object2: RotationSetBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.Assemblies
class RotationSetBuilder(NXOpen.TaggedObject): 
    """
    Represents a  NXOpen.GeometricUtilities.RotationSetBuilder 
    """
    @property
    def IsOccurrence(self) -> bool:
        """
        Getter for property: (bool) IsOccurrence
         Returns whether this object is an occurrence or not.  
             
         
        """
        pass
    @property
    def JournalIdentifier(self) -> str:
        """
        Getter for property: (str) JournalIdentifier
         Returns the identifier that would be recorded in a journal for this object.  
           
            This may not be the same across different releases of the software.   
         
        """
        pass
    @property
    def Location(self) -> OnPathDimensionBuilder:
        """
        Getter for property: ( OnPathDimensionBuilder NXOpen.Geome) Location
         Returns the location on path   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the custom name of the object.  
              
         
        """
        pass
    @property
    def OwningComponent(self) -> NXOpen.Assemblies.Component:
        """
        Getter for property: ( NXOpen.Assemblies.Component) OwningComponent
         Returns the owning component, if this object is an occurrence.  
             
         
        """
        pass
    @property
    def OwningPart(self) -> NXOpen.BasePart:
        """
        Getter for property: ( NXOpen.BasePart) OwningPart
         Returns the owning part of this object   
            
         
        """
        pass
    @property
    def Prototype(self) -> NXOpen.INXObject:
        """
        Getter for property: ( NXOpen.INXObject) Prototype
         Returns the prototype of this object if it is an occurrence.  
             
         
        """
        pass
    @property
    def Value(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Value
         Returns the value expression   
            
         
        """
        pass
    def ResetExtraData(self) -> None:
        """
         Resets rotation extra data. 
                For legacy reason, Rotation has to contain some extra data.
                When you try to reset the rotation, you not only need to reset the angular dimension 
                but also need to simultaneously call this API to reset the extra data. 
        """
        pass
import NXOpen
class SaveConstraintsBuilder(NXOpen.TaggedObject): 
    """
    Represents a builder for a Save Constraints.
    """
    @property
    def SaveConstraints(self) -> bool:
        """
        Getter for property: (bool) SaveConstraints
         Returns the flag indicating whether to save the constraints or not   
            
         
        """
        pass
    @SaveConstraints.setter
    def SaveConstraints(self, is_save_constraints: bool):
        """
        Setter for property: (bool) SaveConstraints
         Returns the flag indicating whether to save the constraints or not   
            
         
        """
        pass
import NXOpen
class ScalingMethodBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.GeometricUtilities.ScalingMethodBuilder
    """
    class BlendingFunctionTypes(Enum):
        """
        Members Include: 
         |Linear|  Linear 
         |Cubic|  Cubic 

        """
        Linear: int
        Cubic: int
        @staticmethod
        def ValueOf(value: int) -> ScalingMethodBuilder.BlendingFunctionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ScalingOptions(Enum):
        """
        Members Include: 
         |Constant|  Constant 
         |ByBlendingFunction|  Blending Function 
         |ByAnotherCurve|  Another Curve 
         |ByAPoint|  A Point 
         |ByAreaLaw|  Area Law 
         |ByPerimeterLaw|  Perimeter Law 
         |Uniform|  Uniform, available only if 2 guides are selected 
         |Lateral|  Lateral, available only if 2 guides are selected 

        """
        Constant: int
        ByBlendingFunction: int
        ByAnotherCurve: int
        ByAPoint: int
        ByAreaLaw: int
        ByPerimeterLaw: int
        Uniform: int
        Lateral: int
        @staticmethod
        def ValueOf(value: int) -> ScalingMethodBuilder.ScalingOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AreaLaw(self) -> LawBuilder:
        """
        Getter for property: ( LawBuilder NXOpen.Geome) AreaLaw
         Returns the area law.  
           For scaling by Area Law, the input law governs the cross sectional area at the start and end of the guide curve.   
         
        """
        pass
    @property
    def BlendingFunctionType(self) -> ScalingMethodBuilder.BlendingFunctionTypes:
        """
        Getter for property: ( ScalingMethodBuilder.BlendingFunctionTypes NXOpen.Geome) BlendingFunctionType
         Returns the blending function.  
           Allows linear or cubic scaling between specified starting and ending scale factors, which 
                    correspond to the start and end of the guide string.   
         
        """
        pass
    @BlendingFunctionType.setter
    def BlendingFunctionType(self, blendingFunctionType: ScalingMethodBuilder.BlendingFunctionTypes):
        """
        Setter for property: ( ScalingMethodBuilder.BlendingFunctionTypes NXOpen.Geome) BlendingFunctionType
         Returns the blending function.  
           Allows linear or cubic scaling between specified starting and ending scale factors, which 
                    correspond to the start and end of the guide string.   
         
        """
        pass
    @property
    def EndBlendScaleFactor(self) -> float:
        """
        Getter for property: (float) EndBlendScaleFactor
         Returns the end blend scale factor.  
           For scaling by Blending Function, the end scale factor will be applied at the
                    end point of the guide curve.   
         
        """
        pass
    @EndBlendScaleFactor.setter
    def EndBlendScaleFactor(self, endBlendScaleFactor: float):
        """
        Setter for property: (float) EndBlendScaleFactor
         Returns the end blend scale factor.  
           For scaling by Blending Function, the end scale factor will be applied at the
                    end point of the guide curve.   
         
        """
        pass
    @property
    def PerimeterLaw(self) -> LawBuilder:
        """
        Getter for property: ( LawBuilder NXOpen.Geome) PerimeterLaw
         Returns the perimeter law.  
           For scaling by Perimeter Law, the input law governs the perimeter of the sections at the start and end of the guide curve.   
         
        """
        pass
    @property
    def ScaleFactor(self) -> float:
        """
        Getter for property: (float) ScaleFactor
         Returns the scale factor.  
           For Constant scaling method, the scale factor will be applied to all sections along the guide.   
         
        """
        pass
    @ScaleFactor.setter
    def ScaleFactor(self, scaleFactor: float):
        """
        Setter for property: (float) ScaleFactor
         Returns the scale factor.  
           For Constant scaling method, the scale factor will be applied to all sections along the guide.   
         
        """
        pass
    @property
    def ScalingCurve(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) ScalingCurve
         Returns the scaling curve.  
           For scaling by Another Curve, the scale at any given point is based on the length of the 
                    ruling between the guide string and the input scaling curve.   
         
        """
        pass
    @property
    def ScalingOption(self) -> ScalingMethodBuilder.ScalingOptions:
        """
        Getter for property: ( ScalingMethodBuilder.ScalingOptions NXOpen.Geome) ScalingOption
         Returns the scaling method option.  
           Except for Uniform and Lateral scaling methods, additional parameters andor inputs are required.   
         
        """
        pass
    @ScalingOption.setter
    def ScalingOption(self, scalingOption: ScalingMethodBuilder.ScalingOptions):
        """
        Setter for property: ( ScalingMethodBuilder.ScalingOptions NXOpen.Geome) ScalingOption
         Returns the scaling method option.  
           Except for Uniform and Lateral scaling methods, additional parameters andor inputs are required.   
         
        """
        pass
    @property
    def ScalingPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) ScalingPoint
         Returns the scaling point.  
           For scaling by a Point, the scale at any given point is based on the length of the 
                    ruling between the guide string and the input point.   
         
        """
        pass
    @ScalingPoint.setter
    def ScalingPoint(self, scalingPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) ScalingPoint
         Returns the scaling point.  
           For scaling by a Point, the scale at any given point is based on the length of the 
                    ruling between the guide string and the input point.   
         
        """
        pass
    @property
    def StartBlendScaleFactor(self) -> float:
        """
        Getter for property: (float) StartBlendScaleFactor
         Returns the start blend scale factor.  
           For scaling by Blending Function, the start scale factor will be applied at the
                    starting of the guide curve.   
         
        """
        pass
    @StartBlendScaleFactor.setter
    def StartBlendScaleFactor(self, startBlendScaleFactor: float):
        """
        Setter for property: (float) StartBlendScaleFactor
         Returns the start blend scale factor.  
           For scaling by Blending Function, the start scale factor will be applied at the
                    starting of the guide curve.   
         
        """
        pass
import NXOpen
class ScalingSetBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[ScalingSetBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: ScalingSetBuilder) -> None:
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
    def Erase(self, obj: ScalingSetBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: ScalingSetBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: ScalingSetBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> ScalingSetBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( ScalingSetBuilder NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[ScalingSetBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( ScalingSetBuilder List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: ScalingSetBuilder) -> None:
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
    def SetContents(self, objects: List[ScalingSetBuilder]) -> None:
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
    def Swap(self, object1: ScalingSetBuilder, object2: ScalingSetBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class ScalingSetBuilder(OnPathDimWithValueBuilder): 
    """
    Represents a  NXOpen.GeometricUtilities.ScalingSetBuilder 
    """
    @property
    def ScalingValue(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ScalingValue
         Returns the scaling value expression   
            
         
        """
        pass
import NXOpen
class SecondarySectionData(NXOpen.NXObject): 
    """
    Represents a NXOpen.GeometricUtilities.SecondarySectionData
    """
    @property
    def IsEndSection(self) -> bool:
        """
        Getter for property: (bool) IsEndSection
         Returns the End Section    
            
         
        """
        pass
    @IsEndSection.setter
    def IsEndSection(self, endSection: bool):
        """
        Setter for property: (bool) IsEndSection
         Returns the End Section    
            
         
        """
        pass
    @property
    def IsStartSection(self) -> bool:
        """
        Getter for property: (bool) IsStartSection
         Returns the Start Section    
            
         
        """
        pass
    @IsStartSection.setter
    def IsStartSection(self, startSection: bool):
        """
        Setter for property: (bool) IsStartSection
         Returns the Start Section    
            
         
        """
        pass
    @property
    def OnPathDimData(self) -> Extend:
        """
        Getter for property: ( Extend NXOpen.Geome) OnPathDimData
         Returns the on path dim   
            
         
        """
        pass
    def CreateSketch(self, pathLocation: float) -> None:
        """
         Copy the master sketch to create the secondary section sketch
                
        """
        pass
    def DeleteSketch(self) -> None:
        """
         Delete secondary section sketch
                
        """
        pass
    def Destroy(self) -> None:
        """
         Delete the secondary section object.
                  
        """
        pass
    def GetMasterExpressionValues(self) -> List[NXOpen.Expression]:
        """
         Get the Master Sketch Expression Values
         Returns expressions ( NXOpen.Expression Li):  All the expressions in the sketch .
        """
        pass
    def GetSecondarySectionValues(self) -> List[str]:
        """
         Get the Secondary Sketch Expression Values
         Returns expressions (List[str]):  Dim Expressions .
        """
        pass
    def SetMasterExpressionValues(self, expressions: List[NXOpen.Expression]) -> None:
        """
         Set the Master Sketch Expression Values. 
                  
        """
        pass
    def SetMasterSection(self, masterSection: NXOpen.Section) -> None:
        """
         Mutator to register the master section. This is needed only if method CreateSketch is called.
                
        """
        pass
    def SetPathLocation(self, pathLocationPercent: float) -> None:
        """
         Path Location  
        """
        pass
    def SetSecondarySectionValues(self, expressions: List[str]) -> None:
        """
         Set the Secondary Sketch Expression Values. 
                    These values should be in the same sequence as the master sketch.
                    You can call NXOpen.Sketch.GetAllExpressions to get the exact
                    sequence of expression values.
                  
        """
        pass
import NXOpen
class SectionPlaneData(NXOpen.TaggedObject): 
    """ Represents a Section Plane Data class
        This class acts like a container to hold the data needed to create a plane. It provides the ability to define two points on a plane """
    @property
    def PlaneNormal(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) PlaneNormal
         Returnsthe normal of the plane   
            
         
        """
        pass
    @PlaneNormal.setter
    def PlaneNormal(self, point: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) PlaneNormal
         Returnsthe normal of the plane   
            
         
        """
        pass
    @property
    def PlaneOrigin(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) PlaneOrigin
         Returnsthe origin of the plane   
            
         
        """
        pass
    @PlaneOrigin.setter
    def PlaneOrigin(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) PlaneOrigin
         Returnsthe origin of the plane   
            
         
        """
        pass
    @property
    def PlanePoint1(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) PlanePoint1
         Returnsthe first point of the plane   
            
         
        """
        pass
    @PlanePoint1.setter
    def PlanePoint1(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) PlanePoint1
         Returnsthe first point of the plane   
            
         
        """
        pass
    @property
    def PlanePoint2(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) PlanePoint2
         Returnsthe second point of the plane   
            
         
        """
        pass
    @PlanePoint2.setter
    def PlanePoint2(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) PlanePoint2
         Returnsthe second point of the plane   
            
         
        """
        pass
import NXOpen
import NXOpen.Features
class SelectDividingObjectBuilder(NXOpen.TaggedObject): 
    """ Represents the dividing tool block for dividing face"""
    class IsoparametricDirectionType(Enum):
        """
        Members Include: 
         |U| 
         |V| 

        """
        U: int
        V: int
        @staticmethod
        def ValueOf(value: int) -> SelectDividingObjectBuilder.IsoparametricDirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ToolType(Enum):
        """
        Members Include: 
         |Object| 
         |LineByTwoPoints| 
         |OffsetCurveInFace| 
         |IsoparametricCurve| 

        """
        Object: int
        LineByTwoPoints: int
        OffsetCurveInFace: int
        IsoparametricCurve: int
        @staticmethod
        def ValueOf(value: int) -> SelectDividingObjectBuilder.ToolType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ConstraintManager(self) -> NXOpen.Features.GeometricConstraintDataManager:
        """
        Getter for property: ( NXOpen.Features.GeometricConstraintDataManager) ConstraintManager
         Returns the iso parameter point   
            
         
        """
        pass
    @property
    def CurvesToOffset(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) CurvesToOffset
         Returns the curves to offset   
            
         
        """
        pass
    @property
    def DividingObjectsList(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) DividingObjectsList
         Returns the dividing objects list   
            
         
        """
        pass
    @property
    def EndPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) EndPoint
         Returns the end point   
            
         
        """
        pass
    @EndPoint.setter
    def EndPoint(self, endPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) EndPoint
         Returns the end point   
            
         
        """
        pass
    @property
    def IsoparametricDirection(self) -> SelectDividingObjectBuilder.IsoparametricDirectionType:
        """
        Getter for property: ( SelectDividingObjectBuilder.IsoparametricDirectionType NXOpen.Geome) IsoparametricDirection
         Returns the isoparametric direction    
            
         
        """
        pass
    @IsoparametricDirection.setter
    def IsoparametricDirection(self, isoprametricDirection: SelectDividingObjectBuilder.IsoparametricDirectionType):
        """
        Setter for property: ( SelectDividingObjectBuilder.IsoparametricDirectionType NXOpen.Geome) IsoparametricDirection
         Returns the isoparametric direction    
            
         
        """
        pass
    @property
    def OffsetDirection(self) -> bool:
        """
        Getter for property: (bool) OffsetDirection
         Returns the offset direction   
            
         
        """
        pass
    @OffsetDirection.setter
    def OffsetDirection(self, offsetDirection: bool):
        """
        Setter for property: (bool) OffsetDirection
         Returns the offset direction   
            
         
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
    def StartPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) StartPoint
         Returns the start point   
            
         
        """
        pass
    @StartPoint.setter
    def StartPoint(self, startPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) StartPoint
         Returns the start point   
            
         
        """
        pass
    @property
    def ToolOption(self) -> SelectDividingObjectBuilder.ToolType:
        """
        Getter for property: ( SelectDividingObjectBuilder.ToolType NXOpen.Geome) ToolOption
         Returns the tool option   
            
         
        """
        pass
    @ToolOption.setter
    def ToolOption(self, toolOption: SelectDividingObjectBuilder.ToolType):
        """
        Setter for property: ( SelectDividingObjectBuilder.ToolType NXOpen.Geome) ToolOption
         Returns the tool option   
            
         
        """
        pass
import NXOpen
class SelectionListList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[SelectionList]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: SelectionList) -> None:
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
    def Erase(self, obj: SelectionList) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: SelectionList, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: SelectionList) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> SelectionList:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( SelectionList NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[SelectionList]:
        """
         Gets the contents of the entire list 
         Returns objects ( SelectionList List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: SelectionList) -> None:
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
    def SetContents(self, objects: List[SelectionList]) -> None:
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
    def Swap(self, object1: SelectionList, object2: SelectionList) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class SelectionList(NXOpen.NXObject): 
    """ Represents a NXOpen.GeometricUtilities.SelectionList """
    @property
    def SelectObjectList(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) SelectObjectList
         Returns the list of geometries    
            
         
        """
        pass
import NXOpen
class ShapeFrameBuilder(NXOpen.TaggedObject): 
    """ Represents a NXOpen.GeometricUtilities.ShapeFrameBuilder """
    class AnchorAttachmentType(Enum):
        """
        Members Include: 
         |NotSet|  Anchor is not attached to the frame 
         |Center|  Anchor is attached to the center of the frame 
         |Vertex1|  Anchor is attached to the first vertex of the frame 
         |Vertex2|  Anchor is attached to the second vertex of the frame 
         |Vertex3|  Anchor is attached to the third vertex of the frame 
         |Vertex4|  Anchor is attached to the fourth vertex of the frame 

        """
        NotSet: int
        Center: int
        Vertex1: int
        Vertex2: int
        Vertex3: int
        Vertex4: int
        @staticmethod
        def ValueOf(value: int) -> ShapeFrameBuilder.AnchorAttachmentType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Anchor(self) -> AnchorLocatorBuilder:
        """
        Getter for property: ( AnchorLocatorBuilder NXOpen.Geome) Anchor
         Returns the anchor of the frame   
            
         
        """
        pass
    @property
    def AnchorAttachment(self) -> ShapeFrameBuilder.AnchorAttachmentType:
        """
        Getter for property: ( ShapeFrameBuilder.AnchorAttachmentType NXOpen.Geome) AnchorAttachment
         Returns the anchor attachment   
            
         
        """
        pass
    @AnchorAttachment.setter
    def AnchorAttachment(self, anchorAttachment: ShapeFrameBuilder.AnchorAttachmentType):
        """
        Setter for property: ( ShapeFrameBuilder.AnchorAttachmentType NXOpen.Geome) AnchorAttachment
         Returns the anchor attachment   
            
         
        """
        pass
    @property
    def NumberVertices(self) -> int:
        """
        Getter for property: (int) NumberVertices
         Returns the number of vertices of the frame   
            
         
        """
        pass
    def GetMidpointCoords(self, index: int) -> NXOpen.Point2d:
        """
         Gets the coordinates of the i-th midpoint of the frame with respect to the plane 
         Returns coords ( NXOpen.Point2d):  coordinates of midpoint relative with respect to plane .
        """
        pass
    def GetVertexCoords(self, index: int) -> NXOpen.Point2d:
        """
         Gets the coordinates of the i-th vertex of the frame with respect to the plane 
         Returns coords ( NXOpen.Point2d):  coordinates of vertex relative with respect to plane .
        """
        pass
    def SetMidpointCoords(self, index: int, coords: NXOpen.Point2d) -> None:
        """
         Sets the coordinates of the i-th midpoint of the frame with respect to the plane 
        """
        pass
    def SetVertexCoords(self, index: int, coords: NXOpen.Point2d) -> None:
        """
         Sets the coordinates of the i-th vertex of the frame with respect to the plane 
        """
        pass
import NXOpen
class SimpleDraft(NXOpen.TaggedObject): 
    """ Represents an Offset . 
    """
    class SimpleDraftType(Enum):
        """
        Members Include: 
         |NoDraft|  No draft 
         |SimpleFromStart|  Draft using the start limit as the reference 
         |SimpleFromProfile|  Draft using the profile as the reference 
         |Symmetric|  Draft on both sides of the profile using the same angle 
         |MatchedEnds|  Draft on both sides of the profile such that the end profiles match in areas 
         |Asymmetric|  Draft on both sides of the profile using the not same angle 

        """
        NoDraft: int
        SimpleFromStart: int
        SimpleFromProfile: int
        Symmetric: int
        MatchedEnds: int
        Asymmetric: int
        @staticmethod
        def ValueOf(value: int) -> SimpleDraft.SimpleDraftType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DraftAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DraftAngle
         Returns the draft angle
                  
            
         
        """
        pass
    @property
    def DraftType(self) -> SimpleDraft.SimpleDraftType:
        """
        Getter for property: ( SimpleDraft.SimpleDraftType NXOpen.Geome) DraftType
         Returns  the simple draft type
                  
            
         
        """
        pass
    @DraftType.setter
    def DraftType(self, type: SimpleDraft.SimpleDraftType):
        """
        Setter for property: ( SimpleDraft.SimpleDraftType NXOpen.Geome) DraftType
         Returns  the simple draft type
                  
            
         
        """
        pass
    def SetDraftAngle(self, draft_angle: str) -> None:
        """
         Sets the draft angle 
        """
        pass
import NXOpen
class SmartVolumeProfileBuilder(NXOpen.TaggedObject): 
    """ This class contains the options for automatically closing the profile to surrounding model geometry.
        It is instantiated in section based sweep operators like extrude and revolve.
    """
    class CloseProfileRuleType(Enum):
        """
        Members Include: 
         |Fci|  Extends the open profile to form 
                                                     the first complete intersection with the target. 
         |Lci|  Extends the open profile to form
                                                     the last complete intersection with the target. 
         |Cci|  For subtract boolean operation,
                                                     extends the open profile to form the last complete intersection 
                                                     if the profile lies outside the target excluding the coincident portion.
                                                     Otherwise, use the first complete intersection. 

        """
        Fci: int
        Lci: int
        Cci: int
        @staticmethod
        def ValueOf(value: int) -> SmartVolumeProfileBuilder.CloseProfileRuleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CloseProfileRule(self) -> SmartVolumeProfileBuilder.CloseProfileRuleType:
        """
        Getter for property: ( SmartVolumeProfileBuilder.CloseProfileRuleType NXOpen.Geome) CloseProfileRule
         Returns the option defines how to extend the open profile to form a proper intersection with the target body.  
           
                  
         
        """
        pass
    @CloseProfileRule.setter
    def CloseProfileRule(self, closeProfileRule: SmartVolumeProfileBuilder.CloseProfileRuleType):
        """
        Setter for property: ( SmartVolumeProfileBuilder.CloseProfileRuleType NXOpen.Geome) CloseProfileRule
         Returns the option defines how to extend the open profile to form a proper intersection with the target body.  
           
                  
         
        """
        pass
    @property
    def OpenProfileSmartVolumeOption(self) -> bool:
        """
        Getter for property: (bool) OpenProfileSmartVolumeOption
         Returns the option for enabling open profile smart volume.  
           
                    When this option is enabled, extends the tool volume along open end points of the profile to find
                    closure with the target body.
                  
         
        """
        pass
    @OpenProfileSmartVolumeOption.setter
    def OpenProfileSmartVolumeOption(self, openProfileSmartVolumeOption: bool):
        """
        Setter for property: (bool) OpenProfileSmartVolumeOption
         Returns the option for enabling open profile smart volume.  
           
                    When this option is enabled, extends the tool volume along open end points of the profile to find
                    closure with the target body.
                  
         
        """
        pass
import NXOpen
class SnipIntoPatchesBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.GeometricUtilities.SnipIntoPatchesBuilder builder. No object is returned by this builder."""
    @property
    def Face(self) -> NXOpen.SelectFace:
        """
        Getter for property: ( NXOpen.SelectFace) Face
         Returns the face to snip into patches   
            
         
        """
        pass
    @property
    def HideOriginal(self) -> bool:
        """
        Getter for property: (bool) HideOriginal
         Returns the option indicating to hide or show the original.  
           If True it is hidden,else it is shown   
         
        """
        pass
    @HideOriginal.setter
    def HideOriginal(self, hideOriginal: bool):
        """
        Setter for property: (bool) HideOriginal
         Returns the option indicating to hide or show the original.  
           If True it is hidden,else it is shown   
         
        """
        pass
    @property
    def Region(self) -> NXOpen.RegionPointList:
        """
        Getter for property: ( NXOpen.RegionPointList) Region
         Returns the region to delete from the surface   
            
         
        """
        pass
    def CreateRegionsPreview(self, targetFace: NXOpen.Face, allCurves: List[NXOpen.Curve]) -> None:
        """
         Create region preview 
        """
        pass
    def DeleteExtractFace(self, extractFace: NXOpen.Face) -> None:
        """
         Delete the extracted face 
        """
        pass
    def DeleteInternalPatch(self, targetFace: NXOpen.Face, allCurves: List[NXOpen.Curve]) -> None:
        """
         Delete internal patch from the selected surface 
        """
        pass
    def DeleteIsoCurve(self, allCurves: List[NXOpen.Curve]) -> None:
        """
         Delete the isoparametric curve generated on the selected surface 
        """
        pass
    def GetExtractFace(self) -> NXOpen.Face:
        """
         Get extracted face 
         Returns extractFace ( NXOpen.Face): .
        """
        pass
    def GetIsoCurves(self, targetFace: NXOpen.Face) -> List[NXOpen.Curve]:
        """
         Get the generated isoparametric curves on the selected surface 
         Returns allCurves ( NXOpen.Curve Li): .
        """
        pass
    def SnipSurfaceIntoPatches(self, targetFace: NXOpen.Face) -> None:
        """
         Snip the selected surface into patches 
        """
        pass
import NXOpen
class SpineDefinitionBuilder(NXOpen.TaggedObject): 
    """ Provides a spine definition for modeling operations """
    class MethodOptions(Enum):
        """
        Members Include: 
         |NotSet|  No spine 
         |Curve|  Spine by curve or a profile
         |Vector|  Spine by a vector 

        """
        NotSet: int
        Curve: int
        Vector: int
        @staticmethod
        def ValueOf(value: int) -> SpineDefinitionBuilder.MethodOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Method(self) -> SpineDefinitionBuilder.MethodOptions:
        """
        Getter for property: ( SpineDefinitionBuilder.MethodOptions NXOpen.Geome) Method
         Returns the method   
            
         
        """
        pass
    @Method.setter
    def Method(self, method: SpineDefinitionBuilder.MethodOptions):
        """
        Setter for property: ( SpineDefinitionBuilder.MethodOptions NXOpen.Geome) Method
         Returns the method   
            
         
        """
        pass
    @property
    def Section(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Section
         Returns the section   
            
         
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
import NXOpen
class SpinePlaneBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[SpinePlaneBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: SpinePlaneBuilder) -> None:
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
    def Erase(self, obj: SpinePlaneBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: SpinePlaneBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: SpinePlaneBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> SpinePlaneBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( SpinePlaneBuilder NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[SpinePlaneBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( SpinePlaneBuilder List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: SpinePlaneBuilder) -> None:
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
    def SetContents(self, objects: List[SpinePlaneBuilder]) -> None:
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
    def Swap(self, object1: SpinePlaneBuilder, object2: SpinePlaneBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class SpinePlaneBuilder(NXOpen.TaggedObject): 
    """ Represents a NXOpen.GeometricUtilities.SpinePlaneBuilder. """
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
    def AlternateSolution(self) -> None:
        """
         Creates the longer arc between the current and previous plane. Shorter arc is constructed by default. 
        """
        pass
import NXOpen
class SpinePointDataCollection(NXOpen.TaggedObjectCollection): 
    """ This class contains the factory methods for creating a SpinePointData object. """
    @overload
    def CreateSpinePointData(self, law_value: float, parameter: float, parent: NXOpen.Section) -> SpinePointData:
        """
         Creates a SpinePointData object. 
         Returns spine_point_data ( SpinePointData NXOpen.Geome):  SpinePointData Object .
        """
        pass
    @overload
    def CreateSpinePointData(self, law_value_expression: NXOpen.Expression, parameter: float, parent: NXOpen.Section) -> SpinePointData:
        """
         Creates a SpinePointData object with expression. 
         Returns spine_point_data ( SpinePointData NXOpen.Geome):  SpinePointData Object .
        """
        pass
import NXOpen
class SpinePointData(NXOpen.TaggedObject): 
    """ Represents a spine point def object
    """
    class ParameterType(Enum):
        """
        Members Include: 
         |Normal| 
         |Percent|  Parameter expressed as percent arc length
         |Length|  Parameter expressed as arc length 

        """
        Normal: int
        Percent: int
        Length: int
        @staticmethod
        def ValueOf(value: int) -> SpinePointData.ParameterType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ParameterLength(self) -> float:
        """
        Getter for property: (float) ParameterLength
         Returns the parameter in arc length   
            
         
        """
        pass
    @ParameterLength.setter
    def ParameterLength(self, length_parameter: float):
        """
        Setter for property: (float) ParameterLength
         Returns the parameter in arc length   
            
         
        """
        pass
    @property
    def ParameterPercent(self) -> float:
        """
        Getter for property: (float) ParameterPercent
         Returns the parameter in percent arc length   
            
         
        """
        pass
    @ParameterPercent.setter
    def ParameterPercent(self, percent_parameter: float):
        """
        Setter for property: (float) ParameterPercent
         Returns the parameter in percent arc length   
            
         
        """
        pass
    def GetLawValueAtPoint(self) -> NXOpen.Expression:
        """
         Returns the law value at the specified point 
         Returns lawValueAtPoint ( NXOpen.Expression):  Law value Expression Object .
        """
        pass
    def GetParentSpine(self) -> NXOpen.Section:
        """
         Returns the parent spine on which spine point is defined    
         Returns parentSpine ( NXOpen.Section):  section object.
        """
        pass
    def SetLawValueAtPoint(self, val_string: str) -> None:
        """
         Sets the law value at the specified point 
        """
        pass
    def SetParentSpine(self, parent: NXOpen.Section) -> None:
        """
         Sets the parent spine on which spine point is defined    
        """
        pass
import NXOpen
class SpiralPattern(NXOpen.TaggedObject): 
    """ the Spiral pattern definition.  """
    class OrientType(Enum):
        """
        Members Include: 
         |Lefthand|  Left hand orientation. 
         |Righthand|  Right hand orientation. 

        """
        Lefthand: int
        Righthand: int
        @staticmethod
        def ValueOf(value: int) -> SpiralPattern.OrientType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SpiralDefineSize(Enum):
        """
        Members Include: 
         |NumberOfTurns|  using number of turns to define size of spiral 
         |TotalAngle|  using total angle to define size of spiral 

        """
        NumberOfTurns: int
        TotalAngle: int
        @staticmethod
        def ValueOf(value: int) -> SpiralPattern.SpiralDefineSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DirectionType(self) -> SpiralPattern.OrientType:
        """
        Getter for property: ( SpiralPattern.OrientType NXOpen.Geome) DirectionType
         Returns the type of spiral direction method   
            
         
        """
        pass
    @DirectionType.setter
    def DirectionType(self, directionType: SpiralPattern.OrientType):
        """
        Setter for property: ( SpiralPattern.OrientType NXOpen.Geome) DirectionType
         Returns the type of spiral direction method   
            
         
        """
        pass
    @property
    def HorizontalRef(self) -> HorizontalReference:
        """
        Getter for property: ( HorizontalReference NXOpen.Geome) HorizontalRef
         Returns the horizontal reference   
            
         
        """
        pass
    @property
    def NumberOfTurns(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NumberOfTurns
         Returns the number of turns of spiral   
            
         
        """
        pass
    @property
    def PitchAlongSpiral(self) -> OnPathDistancePatternSpacing:
        """
        Getter for property: ( OnPathDistancePatternSpacing NXOpen.Geome) PitchAlongSpiral
         Returns the pitch along spiral curve   
            
         
        """
        pass
    @property
    def RadialPitch(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RadialPitch
         Returns the radial pitch of spiral   
            
         
        """
        pass
    @property
    def SizeSpiralType(self) -> SpiralPattern.SpiralDefineSize:
        """
        Getter for property: ( SpiralPattern.SpiralDefineSize NXOpen.Geome) SizeSpiralType
         Returns the size spiral type   
            
         
        """
        pass
    @SizeSpiralType.setter
    def SizeSpiralType(self, sizeSpiralType: SpiralPattern.SpiralDefineSize):
        """
        Setter for property: ( SpiralPattern.SpiralDefineSize NXOpen.Geome) SizeSpiralType
         Returns the size spiral type   
            
         
        """
        pass
    @property
    def SpiralNormal(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) SpiralNormal
         Returns the spiral normal vector   
            
         
        """
        pass
    @SpiralNormal.setter
    def SpiralNormal(self, spiralNormal: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) SpiralNormal
         Returns the spiral normal vector   
            
         
        """
        pass
    @property
    def TotalAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TotalAngle
         Returns the total angle of spiral   
            
         
        """
        pass
import NXOpen
class SplineExtensionBuilder(NXOpen.TaggedObject): 
    """ Spline extension builder class. This class allows natural extension or trimming of a b-spline cuve. """
    class ExtensionOption(Enum):
        """
        Members Include: 
         |NotSet|  No extension 
         |ByValue|  Extend by value 
         |ByPoint|  Extend up to a point 

        """
        NotSet: int
        ByValue: int
        ByPoint: int
        @staticmethod
        def ValueOf(value: int) -> SplineExtensionBuilder.ExtensionOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EndExtensionOption(self) -> SplineExtensionBuilder.ExtensionOption:
        """
        Getter for property: ( SplineExtensionBuilder.ExtensionOption NXOpen.Geome) EndExtensionOption
         Returns the extension options   
            
         
        """
        pass
    @EndExtensionOption.setter
    def EndExtensionOption(self, extensionOption: SplineExtensionBuilder.ExtensionOption):
        """
        Setter for property: ( SplineExtensionBuilder.ExtensionOption NXOpen.Geome) EndExtensionOption
         Returns the extension options   
            
         
        """
        pass
    @property
    def EndPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) EndPoint
         Returns the point up to which end is extended   
            
         
        """
        pass
    @EndPoint.setter
    def EndPoint(self, endPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) EndPoint
         Returns the point up to which end is extended   
            
         
        """
        pass
    @property
    def EndValue(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndValue
         Returns the end value   
            
         
        """
        pass
    @property
    def IsSymmetric(self) -> bool:
        """
        Getter for property: (bool) IsSymmetric
         Returns the flag indicating if extension is symmetry.  
           Symmetric extension follows start extension values   
         
        """
        pass
    @IsSymmetric.setter
    def IsSymmetric(self, isSymmetric: bool):
        """
        Setter for property: (bool) IsSymmetric
         Returns the flag indicating if extension is symmetry.  
           Symmetric extension follows start extension values   
         
        """
        pass
    @property
    def StartExtensionOption(self) -> SplineExtensionBuilder.ExtensionOption:
        """
        Getter for property: ( SplineExtensionBuilder.ExtensionOption NXOpen.Geome) StartExtensionOption
         Returns the extension options   
            
         
        """
        pass
    @StartExtensionOption.setter
    def StartExtensionOption(self, extensionOption: SplineExtensionBuilder.ExtensionOption):
        """
        Setter for property: ( SplineExtensionBuilder.ExtensionOption NXOpen.Geome) StartExtensionOption
         Returns the extension options   
            
         
        """
        pass
    @property
    def StartPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) StartPoint
         Returns the point up to which start is extended   
            
         
        """
        pass
    @StartPoint.setter
    def StartPoint(self, startPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) StartPoint
         Returns the point up to which start is extended   
            
         
        """
        pass
    @property
    def StartValue(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartValue
         Returns the start value   
            
         
        """
        pass
import NXOpen
class SShapedLawBuilder(NXOpen.TaggedObject): 
    """
        Represents a s-shaped law.
        
        This class represents NXOpen.GeometricUtilities.LawBuilder.Type.SShaped type
        of law in NXOpen.GeometricUtilities.LawBuilder.
        Objects of class NXOpen.GeometricUtilities.OnPathDimWithValueBuilder are used
        as law nodes in NXOpen.GeometricUtilities.SShapedLawBuilder. Spine
        definition in this class is mandatory. The law nodes at start and end of the spine are fixed.
    """
    @property
    def EndNode(self) -> OnPathDimWithValueBuilder:
        """
        Getter for property: ( OnPathDimWithValueBuilder NXOpen.Geome) EndNode
         Returns the end node   
            
         
        """
        pass
    @property
    def SlopeNode(self) -> OnPathDimWithValueBuilder:
        """
        Getter for property: ( OnPathDimWithValueBuilder NXOpen.Geome) SlopeNode
         Returns the slope node   
            
         
        """
        pass
    @property
    def Spine(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Spine
         Returns the Spine   
            
         
        """
        pass
    @property
    def StartNode(self) -> OnPathDimWithValueBuilder:
        """
        Getter for property: ( OnPathDimWithValueBuilder NXOpen.Geome) StartNode
         Returns the start node   
            
         
        """
        pass
    def UpdateSpine(self) -> None:
        """
         Update the builder based on current spine 
        """
        pass
import NXOpen
class StartHoleData(NXOpen.TaggedObject): 
    """ Represents a NXOpen.GeometricUtilities.StartHoleData """
    class HoleForms(Enum):
        """
        Members Include: 
         |Simple|  Simple hole form 
         |Counterbored|  Counterbored hole form 
         |Countersink|  Countersink hole form 

        """
        Simple: int
        Counterbored: int
        Countersink: int
        @staticmethod
        def ValueOf(value: int) -> StartHoleData.HoleForms:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BooleanOperation(self) -> BooleanOperation:
        """
        Getter for property: ( BooleanOperation NXOpen.Geome) BooleanOperation
         Returns the boolean operation   
            
         
        """
        pass
    @property
    def CounterboreDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CounterboreDepth
         Returns the counterbore depth   
            
         
        """
        pass
    @property
    def CounterboreDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CounterboreDiameter
         Returns the counterbore diameter   
            
         
        """
        pass
    @property
    def CountersinkAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CountersinkAngle
         Returns the countersink angle   
            
         
        """
        pass
    @property
    def CountersinkDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CountersinkDiameter
         Returns the countersink diameter   
            
         
        """
        pass
    @property
    def EndChamferAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndChamferAngle
         Returns the end chamfer angle   
            
         
        """
        pass
    @property
    def EndChamferEnabled(self) -> bool:
        """
        Getter for property: (bool) EndChamferEnabled
         Returns the end chamfer enabled   
            
         
        """
        pass
    @EndChamferEnabled.setter
    def EndChamferEnabled(self, endChamferEnabled: bool):
        """
        Setter for property: (bool) EndChamferEnabled
         Returns the end chamfer enabled   
            
         
        """
        pass
    @property
    def EndChamferOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndChamferOffset
         Returns the end chamfer offset   
            
         
        """
        pass
    @property
    def FitOption(self) -> str:
        """
        Getter for property: (str) FitOption
         Returns the fit option   
            
         
        """
        pass
    @FitOption.setter
    def FitOption(self, fitOption: str):
        """
        Setter for property: (str) FitOption
         Returns the fit option   
            
         
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
    def HoleForm(self) -> StartHoleData.HoleForms:
        """
        Getter for property: ( StartHoleData.HoleForms NXOpen.Geome) HoleForm
         Returns the hole form   
            
         
        """
        pass
    @HoleForm.setter
    def HoleForm(self, holeForm: StartHoleData.HoleForms):
        """
        Setter for property: ( StartHoleData.HoleForms NXOpen.Geome) HoleForm
         Returns the hole form   
            
         
        """
        pass
    @property
    def NeckChamferAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NeckChamferAngle
         Returns the neck chamfer angle   
            
         
        """
        pass
    @property
    def NeckChamferEnabled(self) -> bool:
        """
        Getter for property: (bool) NeckChamferEnabled
         Returns the neck chamfer enabled   
            
         
        """
        pass
    @NeckChamferEnabled.setter
    def NeckChamferEnabled(self, neckChamferEnabled: bool):
        """
        Setter for property: (bool) NeckChamferEnabled
         Returns the neck chamfer enabled   
            
         
        """
        pass
    @property
    def NeckChamferOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NeckChamferOffset
         Returns the neck chamfer offset   
            
         
        """
        pass
    @property
    def ReliefDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ReliefDepth
         Returns the relief depth   
            
         
        """
        pass
    @property
    def ReliefEnabled(self) -> bool:
        """
        Getter for property: (bool) ReliefEnabled
         Returns the  relief  enabled   
            
         
        """
        pass
    @ReliefEnabled.setter
    def ReliefEnabled(self, reliefEnabled: bool):
        """
        Setter for property: (bool) ReliefEnabled
         Returns the  relief  enabled   
            
         
        """
        pass
    @property
    def ScrewSize(self) -> str:
        """
        Getter for property: (str) ScrewSize
         Returns the screw size   
            
         
        """
        pass
    @ScrewSize.setter
    def ScrewSize(self, screwSize: str):
        """
        Setter for property: (str) ScrewSize
         Returns the screw size   
            
         
        """
        pass
    @property
    def ScrewType(self) -> str:
        """
        Getter for property: (str) ScrewType
         Returns the screw type   
            
         
        """
        pass
    @ScrewType.setter
    def ScrewType(self, screwType: str):
        """
        Setter for property: (str) ScrewType
         Returns the screw type   
            
         
        """
        pass
    @property
    def StartChamferAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartChamferAngle
         Returns the start chamfer angle   
            
         
        """
        pass
    @property
    def StartChamferEnabled(self) -> bool:
        """
        Getter for property: (bool) StartChamferEnabled
         Returns the start chamfer enabled   
            
         
        """
        pass
    @StartChamferEnabled.setter
    def StartChamferEnabled(self, startChamferEnabled: bool):
        """
        Setter for property: (bool) StartChamferEnabled
         Returns the start chamfer enabled   
            
         
        """
        pass
    @property
    def StartChamferOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartChamferOffset
         Returns the start chamfer offset   
            
         
        """
        pass
import NXOpen
class StepOptionBehavior(NXOpen.TaggedObject): 
    """   
    Represents a NXOpen.GeometricUtilities.StepOptionBehavior
    It provides several step options for controlling behavior when 
    move face and so on.
    """
    class StepOptionType(Enum):
        """
        Members Include: 
         |NotSet|  Does not add step faces.
         |ExtendNeighborsatSmoothEdge|  Extends faces neighboring a smooth edge of the motion face.

        """
        NotSet: int
        ExtendNeighborsatSmoothEdge: int
        @staticmethod
        def ValueOf(value: int) -> StepOptionBehavior.StepOptionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def StepOption(self) -> StepOptionBehavior.StepOptionType:
        """
        Getter for property: ( StepOptionBehavior.StepOptionType NXOpen.Geome) StepOption
         Returns the step option   
            
         
        """
        pass
    @StepOption.setter
    def StepOption(self, stepOption: StepOptionBehavior.StepOptionType):
        """
        Setter for property: ( StepOptionBehavior.StepOptionType NXOpen.Geome) StepOption
         Returns the step option   
            
         
        """
        pass
import NXOpen
class StrokeGestureData(NXOpen.TaggedObject): 
    """ Represents a NXOpen.GeometricUtilities.StrokeGestureData.
        A stroke is an ordered list of points. """
    class Point:
        """
         Structure representing stroke point in absolute space. 
         StrokeGestureDataPoint_Struct NXOpen.Geome is an alias for  StrokeGestureData.Point NXOpen.Geome.
        """
        @property
        def Position(self) -> NXOpen.Point3d:
            """
            Getter for property Position
            The point

            """
            pass
        @Position.setter
        def Position(self, value: NXOpen.Point3d):
            """
            Getter for property Position
            The point
            Setter for property Position
            The point

            """
            pass
        @property
        def Speed(self) -> float:
            """
            Getter for property Speed
            The speed

            """
            pass
        @Speed.setter
        def Speed(self, value: float):
            """
            Getter for property Speed
            The speed
            Setter for property Speed
            The speed

            """
            pass
    @property
    def DrawingScale(self) -> float:
        """
        Getter for property: (float) DrawingScale
         Returns the drawing scale.  
           The view scale at which stroke is drawn.   
         
        """
        pass
    @DrawingScale.setter
    def DrawingScale(self, scale: float):
        """
        Setter for property: (float) DrawingScale
         Returns the drawing scale.  
           The view scale at which stroke is drawn.   
         
        """
        pass
    def AddPoint(self, point: StrokeGestureData.Point) -> None:
        """
         Appends a point to the stroke 
        """
        pass
    def Clear(self) -> None:
        """
         Deletes all the points 
        """
        pass
    def GetPoints(self) -> List[StrokeGestureData.Point]:
        """
         Queries all the points 
         Returns points ( StrokeGestureData.Point List[NXOpen.Geo):  .
        """
        pass
    def SetDrawingPlane(self, matrix: NXOpen.Matrix3x3) -> None:
        """
         Defines the plane in which stroke gesture is executed. 
        """
        pass
import NXOpen
class StyledSweepDoubleOnPathDimBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[StyledSweepDoubleOnPathDimBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: StyledSweepDoubleOnPathDimBuilder) -> None:
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
    def Erase(self, obj: StyledSweepDoubleOnPathDimBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: StyledSweepDoubleOnPathDimBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: StyledSweepDoubleOnPathDimBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> StyledSweepDoubleOnPathDimBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( StyledSweepDoubleOnPathDimBuilder NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[StyledSweepDoubleOnPathDimBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( StyledSweepDoubleOnPathDimBuilder List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: StyledSweepDoubleOnPathDimBuilder) -> None:
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
    def SetContents(self, objects: List[StyledSweepDoubleOnPathDimBuilder]) -> None:
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
    def Swap(self, object1: StyledSweepDoubleOnPathDimBuilder, object2: StyledSweepDoubleOnPathDimBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class StyledSweepDoubleOnPathDimBuilder(NXOpen.NXObject): 
    """
    Represents a  NXOpen.GeometricUtilities.StyledSweepDoubleOnPathDimBuilder 
    """
    @property
    def FirstLocation(self) -> OnPathDimensionBuilder:
        """
        Getter for property: ( OnPathDimensionBuilder NXOpen.Geome) FirstLocation
         Returns the first location   
            
         
        """
        pass
    @property
    def SecondLocation(self) -> OnPathDimensionBuilder:
        """
        Getter for property: ( OnPathDimensionBuilder NXOpen.Geome) SecondLocation
         Returns the second location   
            
         
        """
        pass
    def ResetExtraData(self) -> None:
        """
         Reset pivot position extra data. 
                For legacy reason, pivot position has to contain some extra data.
                When you try to reset the pivot position, you not only need to reset the two on path dimensions 
                but also need to simultaneously call this API to reset the extra data. 
        """
        pass
import NXOpen
class StyledSweepReferenceMethodBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.GeometricUtilities.StyledSweepReferenceMethodBuilder
    """
    class ReferenceOptions(Enum):
        """
        Members Include: 
         |ToGuide|  Guide 
         |ToCurve|  Curve 
         |ToVector|  Vector Direction 

        """
        ToGuide: int
        ToCurve: int
        ToVector: int
        @staticmethod
        def ValueOf(value: int) -> StyledSweepReferenceMethodBuilder.ReferenceOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def HasHingeVector(self) -> bool:
        """
        Getter for property: (bool) HasHingeVector
         Returns a value indicating whether there is a hinge vector   
            
         
        """
        pass
    @HasHingeVector.setter
    def HasHingeVector(self, hasHingeVector: bool):
        """
        Setter for property: (bool) HasHingeVector
         Returns a value indicating whether there is a hinge vector   
            
         
        """
        pass
    @property
    def ReferenceCurve(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) ReferenceCurve
         Returns the section orientation reference curve.  
             
         
        """
        pass
    @property
    def ReferenceOption(self) -> StyledSweepReferenceMethodBuilder.ReferenceOptions:
        """
        Getter for property: ( StyledSweepReferenceMethodBuilder.ReferenceOptions NXOpen.Geome) ReferenceOption
         Returns the section orientation reference option.  
             
         
        """
        pass
    @ReferenceOption.setter
    def ReferenceOption(self, referenceOption: StyledSweepReferenceMethodBuilder.ReferenceOptions):
        """
        Setter for property: ( StyledSweepReferenceMethodBuilder.ReferenceOptions NXOpen.Geome) ReferenceOption
         Returns the section orientation reference option.  
             
         
        """
        pass
    @property
    def ReferenceVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ReferenceVector
         Returns the section orientation reference vector.  
             
         
        """
        pass
    @ReferenceVector.setter
    def ReferenceVector(self, referenceVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ReferenceVector
         Returns the section orientation reference vector.  
             
         
        """
        pass
    def UpdateOnReferenceVectorReversal(self) -> None:
        """
         Updates the builder based on reference vector sense 
        """
        pass
import NXOpen
class SupportPlaneData(NXOpen.TaggedObject): 
    """ Represents a NXOpen.GeometricUtilities.SupportPlaneData """
    class LockPlaneStatus(Enum):
        """
        Members Include: 
         |No|  No Lock 
         |AfterFirstConstraint|  Lock after first constraint 
         |AfterSecondConstraint|  Lock after second constraint 
         |AfterThirdConstraint|  Lock after third constraint 
         |AfterFirstAndSecondConstraint|  Lock after first and second constraint 
         |AfterFirstAndThirdConstraint|  Lock after first and third constraint 
         |AfterSecondAndThirdConstraint|  Lock after second and third constraint 
         |AfterAllConstraint|  Lock after all constraint 
         |LockExistingPlane|  Lock support plane using existing face or datum 
         |CenterPointDirection|  Lock support plane using center point and direction, this option should be used for Center Radius Arc only 

        """
        No: int
        AfterFirstConstraint: int
        AfterSecondConstraint: int
        AfterThirdConstraint: int
        AfterFirstAndSecondConstraint: int
        AfterFirstAndThirdConstraint: int
        AfterSecondAndThirdConstraint: int
        AfterAllConstraint: int
        LockExistingPlane: int
        CenterPointDirection: int
        @staticmethod
        def ValueOf(value: int) -> SupportPlaneData.LockPlaneStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ExistingPlane(self) -> NXOpen.DisplayableObject:
        """
        Getter for property: ( NXOpen.DisplayableObject) ExistingPlane
         Returns the existing face or plane  
            
         
        """
        pass
    @ExistingPlane.setter
    def ExistingPlane(self, existingPlane: NXOpen.DisplayableObject):
        """
        Setter for property: ( NXOpen.DisplayableObject) ExistingPlane
         Returns the existing face or plane  
            
         
        """
        pass
    @property
    def SupportPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) SupportPlane
         Returns the support plane  
            
         
        """
        pass
    @SupportPlane.setter
    def SupportPlane(self, supportPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) SupportPlane
         Returns the support plane  
            
         
        """
        pass
    @property
    def SupportPlaneLockStatus(self) -> SupportPlaneData.LockPlaneStatus:
        """
        Getter for property: ( SupportPlaneData.LockPlaneStatus NXOpen.Geome) SupportPlaneLockStatus
         Returns the support plane lock status   
            
         
        """
        pass
    @SupportPlaneLockStatus.setter
    def SupportPlaneLockStatus(self, lock_plane_status: SupportPlaneData.LockPlaneStatus):
        """
        Setter for property: ( SupportPlaneData.LockPlaneStatus NXOpen.Geome) SupportPlaneLockStatus
         Returns the support plane lock status   
            
         
        """
        pass
    @property
    def WorkView(self) -> NXOpen.View:
        """
        Getter for property: ( NXOpen.View) WorkView
         Returns the work view required when lock plane status is  NXOpen::GeometricUtilities::SupportPlaneData::LockPlaneStatusAfterFirstConstraint    
            
         
        """
        pass
    @WorkView.setter
    def WorkView(self, work_view: NXOpen.View):
        """
        Setter for property: ( NXOpen.View) WorkView
         Returns the work view required when lock plane status is  NXOpen::GeometricUtilities::SupportPlaneData::LockPlaneStatusAfterFirstConstraint    
            
         
        """
        pass
import NXOpen
class SurfaceRangeBuilder(NXOpen.TaggedObject): 
    """ Represents the surface range and anchor builder """
    class AnchorPositionType(Enum):
        """
        Members Include: 
         |Center|  Anchor at the center of the surface 
         |Vertex1|  Anchor at the first corner of the surface 
         |Vertex2|  Anchor at the second corner of the surface 
         |Vertex3|  Anchor at the third corner of the surface 
         |Vertex4|  Anchor at the fourth corner of the surface 

        """
        Center: int
        Vertex1: int
        Vertex2: int
        Vertex3: int
        Vertex4: int
        @staticmethod
        def ValueOf(value: int) -> SurfaceRangeBuilder.AnchorPositionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AnchorPosition(self) -> SurfaceRangeBuilder.AnchorPositionType:
        """
        Getter for property: ( SurfaceRangeBuilder.AnchorPositionType NXOpen.Geome) AnchorPosition
         Returns the anchor position   
            
         
        """
        pass
    @AnchorPosition.setter
    def AnchorPosition(self, anchorPosition: SurfaceRangeBuilder.AnchorPositionType):
        """
        Setter for property: ( SurfaceRangeBuilder.AnchorPositionType NXOpen.Geome) AnchorPosition
         Returns the anchor position   
            
         
        """
        pass
    @property
    def UEnd(self) -> OnPathDimensionBuilder:
        """
        Getter for property: ( OnPathDimensionBuilder NXOpen.Geome) UEnd
         Returns the u end   
            
         
        """
        pass
    @property
    def UStart(self) -> OnPathDimensionBuilder:
        """
        Getter for property: ( OnPathDimensionBuilder NXOpen.Geome) UStart
         Returns the u start   
            
         
        """
        pass
    @property
    def VEnd(self) -> OnPathDimensionBuilder:
        """
        Getter for property: ( OnPathDimensionBuilder NXOpen.Geome) VEnd
         Returns the v end   
            
         
        """
        pass
    @property
    def VStart(self) -> OnPathDimensionBuilder:
        """
        Getter for property: ( OnPathDimensionBuilder NXOpen.Geome) VStart
         Returns the v start   
            
         
        """
        pass
import NXOpen
class TangentMagnitudeBuilder(NXOpen.TaggedObject): 
    """
        This class provides ability to specify the start and end
        tangent magnitude values.
    """
    @property
    def EndTangentMagnitude(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndTangentMagnitude
         Returns the end tangent magnitude   
            
         
        """
        pass
    @property
    def StartTangentMagnitude(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartTangentMagnitude
         Returns the start tangent magnitude   
            
         
        """
        pass
import NXOpen
class TransformerData(NXOpen.TaggedObject): 
    """ Transformation and orientation tool.
    """
    class ObjectType(Enum):
        """
        Members Include: 
         |NotSet|   
         |Origin|   
         |TranslationX|   
         |TranslationY|   
         |TranslationZ|   
         |RotationXY|   
         |RotationYZ|   
         |RotationXZ|   
         |ScaleX|   
         |ScaleY|   
         |ScaleZ|   
         |DirectionX|   
         |DirectionY|   
         |DirectionZ|   
         |PlaneXY|   
         |PlaneYZ|   
         |PlaneXZ|   
         |ArcXY|   
         |ArcYZ|   
         |ArcXZ|   
         |ShearX|  Not used yet 
         |ShearY|  Not used yet 
         |ShearZ|  Not used yet 
         |HotSpot1|  Not used yet 
         |HotSpot2|  Not used yet 
         |HotSpot3|  Not used yet 

        """
        NotSet: int
        Origin: int
        TranslationX: int
        TranslationY: int
        TranslationZ: int
        RotationXY: int
        RotationYZ: int
        RotationXZ: int
        ScaleX: int
        ScaleY: int
        ScaleZ: int
        DirectionX: int
        DirectionY: int
        DirectionZ: int
        PlaneXY: int
        PlaneYZ: int
        PlaneXZ: int
        ArcXY: int
        ArcYZ: int
        ArcXZ: int
        ShearX: int
        ShearY: int
        ShearZ: int
        HotSpot1: int
        HotSpot2: int
        HotSpot3: int
        @staticmethod
        def ValueOf(value: int) -> TransformerData.ObjectType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def Activate(self, objectType: TransformerData.ObjectType) -> None:
        """
         Sets a component of the tool to be active. 
        """
        pass
    def AlignToAbsoluteCoordinateSystem(self) -> None:
        """
         Reorient the tool by aligning it to absolute coordinate system 
        """
        pass
    def AlignToWorkCoordinateSystem(self) -> None:
        """
         Reorient the tool by aligning it to work coordinate system 
        """
        pass
    def ReorientByCoordinateSystem(self, matrix: NXOpen.Matrix3x3) -> None:
        """
         Reorient the tool by aligning it to a coordinate system. 
        """
        pass
    def ReorientByDirection(self, objectType: TransformerData.ObjectType, direction: NXOpen.Vector3d) -> None:
        """
         Reorient the tool by changing its axis direction. 
        """
        pass
    def Reposition(self, origin: NXOpen.Point3d, matrix: NXOpen.Matrix3x3) -> None:
        """
         Repositions the tool at a coordinate system. 
        """
        pass
    def RepositionByOrigin(self, origin: NXOpen.Point3d) -> None:
        """
         Repositions the tool by changing its origin. 
        """
        pass
    def RepositionByPlane(self, objectType: TransformerData.ObjectType, planeOrigin: NXOpen.Point3d, planeNormal: NXOpen.Vector3d) -> None:
        """
         Repositions the tool by changing its plane. 
        """
        pass
    def Reverse(self, axisType: TransformerData.ObjectType) -> None:
        """
         Reverses the axis. 
        """
        pass
    def Rotate(self, axisType: TransformerData.ObjectType, angle: float) -> None:
        """
         Rotates the tool. 
        """
        pass
    def Scale(self, axisType: TransformerData.ObjectType, factor: float) -> None:
        """
         Sets the scale factor. 
        """
        pass
    def SetTransformationObject(self, objectType: TransformerData.ObjectType) -> None:
        """
         Sets a component of the tool using which transformation is started. It is possible
                    that user starts transformation without activating a tool component. 
        """
        pass
    def StartTransformation(self) -> None:
        """
         Sets current coordinate system as reference coordinate system for
                    the transformation. 
        """
        pass
    def Translate(self, axisType: TransformerData.ObjectType, distance: float) -> None:
        """
         Translates the tool. 
        """
        pass
    def UpdateOnOriginMove(self) -> None:
        """
         Updates tool upon movement of the point representing origin. 
        """
        pass
import NXOpen
class TransitionCurveBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[TransitionCurveBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: TransitionCurveBuilder) -> None:
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
    def Erase(self, obj: TransitionCurveBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: TransitionCurveBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: TransitionCurveBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> TransitionCurveBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( TransitionCurveBuilder NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[TransitionCurveBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( TransitionCurveBuilder List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: TransitionCurveBuilder) -> None:
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
    def SetContents(self, objects: List[TransitionCurveBuilder]) -> None:
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
    def Swap(self, object1: TransitionCurveBuilder, object2: TransitionCurveBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class TransitionCurveBuilder(NXOpen.TaggedObject): 
    """ 
        This class provides ability to create a transition(bridge) curve between two adjacent setback curves.
    """
    class TangentDirections(Enum):
        """
        Members Include: 
         |Rail|  transition curve will be tangent to the blend rail curve 
         |Limit|  transition curve will be tangent to the limit curve 

        """
        Rail: int
        Limit: int
        @staticmethod
        def ValueOf(value: int) -> TransitionCurveBuilder.TangentDirections:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EndTangentDirection(self) -> TransitionCurveBuilder.TangentDirections:
        """
        Getter for property: ( TransitionCurveBuilder.TangentDirections NXOpen.Geome) EndTangentDirection
         Returns the end tangent direction   
            
         
        """
        pass
    @EndTangentDirection.setter
    def EndTangentDirection(self, direction: TransitionCurveBuilder.TangentDirections):
        """
        Setter for property: ( TransitionCurveBuilder.TangentDirections NXOpen.Geome) EndTangentDirection
         Returns the end tangent direction   
            
         
        """
        pass
    @property
    def EndTangentMagnitude(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndTangentMagnitude
         Returns the end tangent magnitude   
            
         
        """
        pass
    @property
    def StartTangentDirection(self) -> TransitionCurveBuilder.TangentDirections:
        """
        Getter for property: ( TransitionCurveBuilder.TangentDirections NXOpen.Geome) StartTangentDirection
         Returns the start tangent direction   
            
         
        """
        pass
    @StartTangentDirection.setter
    def StartTangentDirection(self, direction: TransitionCurveBuilder.TangentDirections):
        """
        Setter for property: ( TransitionCurveBuilder.TangentDirections NXOpen.Geome) StartTangentDirection
         Returns the start tangent direction   
            
         
        """
        pass
    @property
    def StartTangentMagnitude(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartTangentMagnitude
         Returns the start tangent magnitude   
            
         
        """
        pass
import NXOpen
class TransitionLawNodeBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[TransitionLawNodeBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: TransitionLawNodeBuilder) -> None:
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
    def Erase(self, obj: TransitionLawNodeBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: TransitionLawNodeBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: TransitionLawNodeBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> TransitionLawNodeBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( TransitionLawNodeBuilder NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[TransitionLawNodeBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( TransitionLawNodeBuilder List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: TransitionLawNodeBuilder) -> None:
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
    def SetContents(self, objects: List[TransitionLawNodeBuilder]) -> None:
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
    def Swap(self, object1: TransitionLawNodeBuilder, object2: TransitionLawNodeBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
class TransitionLawNodeBuilder(OnPathDimWithValueBuilder): 
    """
        Represents a law node with transition type.
        
        This class extends NXOpen.GeometricUtilities.OnPathDimWithValueBuilder such
        that apart from specifying a value at a location on spine, it allows specification of transition type.
        This class represents a law node in NXOpen.GeometricUtilities.MultiTransitionLawBuilder
    """
    class TransitionType(Enum):
        """
        Members Include: 
         |Unknown|  No interpolation type 
         |Constant|  Constant transition 
         |Linear|  Linear transition 
         |Blend|  Smooth blended transition 
         |Minmax|  Minimum-Maximum type transition 

        """
        Unknown: int
        Constant: int
        Linear: int
        Blend: int
        Minmax: int
        @staticmethod
        def ValueOf(value: int) -> TransitionLawNodeBuilder.TransitionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Transition(self) -> TransitionLawNodeBuilder.TransitionType:
        """
        Getter for property: ( TransitionLawNodeBuilder.TransitionType NXOpen.Geome) Transition
         Returns the transition type   
            
         
        """
        pass
    @Transition.setter
    def Transition(self, transition: TransitionLawNodeBuilder.TransitionType):
        """
        Setter for property: ( TransitionLawNodeBuilder.TransitionType NXOpen.Geome) Transition
         Returns the transition type   
            
         
        """
        pass
class TriangularFrameBuilder(ShapeFrameBuilder): 
    """
    Represents a NXOpen.GeometricUtilities.TriangularFrameBuilder
    """
    class Subtypes(Enum):
        """
        Members Include: 
         |Arbitrary|  Arbitrary triangle 
         |Isosceles|  Isosceles triangle 
         |Equilateral|  Equilateral triangle 
         |Rightangle|  Right angle triangle 

        """
        Arbitrary: int
        Isosceles: int
        Equilateral: int
        Rightangle: int
        @staticmethod
        def ValueOf(value: int) -> TriangularFrameBuilder.Subtypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Subtype(self) -> TriangularFrameBuilder.Subtypes:
        """
        Getter for property: ( TriangularFrameBuilder.Subtypes NXOpen.Geome) Subtype
         Returns the subtype   
            
         
        """
        pass
    @Subtype.setter
    def Subtype(self, subtype: TriangularFrameBuilder.Subtypes):
        """
        Setter for property: ( TriangularFrameBuilder.Subtypes NXOpen.Geome) Subtype
         Returns the subtype   
            
         
        """
        pass
import NXOpen
class TrimCurveBoundingObjectBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[TrimCurveBoundingObjectBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: TrimCurveBoundingObjectBuilder) -> None:
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
    def Erase(self, obj: TrimCurveBoundingObjectBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: TrimCurveBoundingObjectBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: TrimCurveBoundingObjectBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> TrimCurveBoundingObjectBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( TrimCurveBoundingObjectBuilder NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[TrimCurveBoundingObjectBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( TrimCurveBoundingObjectBuilder List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: TrimCurveBoundingObjectBuilder) -> None:
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
    def SetContents(self, objects: List[TrimCurveBoundingObjectBuilder]) -> None:
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
    def Swap(self, object1: TrimCurveBoundingObjectBuilder, object2: TrimCurveBoundingObjectBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class TrimCurveBoundingObjectBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.GeometricUtilities.TrimCurveBoundingObjectBuilder
    """
    class Method(Enum):
        """
        Members Include: 
         |SelectObject| 
         |SelectPlane| 

        """
        SelectObject: int
        SelectPlane: int
        @staticmethod
        def ValueOf(value: int) -> TrimCurveBoundingObjectBuilder.Method:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BoundingObject(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: ( NXOpen.SelectDisplayableObject) BoundingObject
         Returns the  bounding object   
            
         
        """
        pass
    @property
    def BoundingObjectList(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) BoundingObjectList
         Returns the bounding object list
                
                Only one object is allowed in this list.  
           In the case of multiple objects, only first object will be considered for the operation.
                  
         
        """
        pass
    @property
    def BoundingObjectMethodType(self) -> TrimCurveBoundingObjectBuilder.Method:
        """
        Getter for property: ( TrimCurveBoundingObjectBuilder.Method NXOpen.Geome) BoundingObjectMethodType
         Returns the bounding object enum type   
            
         
        """
        pass
    @BoundingObjectMethodType.setter
    def BoundingObjectMethodType(self, boundingObjectMethod: TrimCurveBoundingObjectBuilder.Method):
        """
        Setter for property: ( TrimCurveBoundingObjectBuilder.Method NXOpen.Geome) BoundingObjectMethodType
         Returns the bounding object enum type   
            
         
        """
        pass
    @property
    def BoundingPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) BoundingPlane
         Returns the bounding plane   
            
         
        """
        pass
    @BoundingPlane.setter
    def BoundingPlane(self, plane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) BoundingPlane
         Returns the bounding plane   
            
         
        """
        pass
import NXOpen
class TwoExpressionsCollectorSetList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[TwoExpressionsCollectorSet]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: TwoExpressionsCollectorSet) -> None:
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
    def Erase(self, obj: TwoExpressionsCollectorSet) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: TwoExpressionsCollectorSet, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: TwoExpressionsCollectorSet) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> TwoExpressionsCollectorSet:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( TwoExpressionsCollectorSet NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[TwoExpressionsCollectorSet]:
        """
         Gets the contents of the entire list 
         Returns objects ( TwoExpressionsCollectorSet List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: TwoExpressionsCollectorSet) -> None:
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
    def SetContents(self, objects: List[TwoExpressionsCollectorSet]) -> None:
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
    def Swap(self, object1: TwoExpressionsCollectorSet, object2: TwoExpressionsCollectorSet) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class TwoExpressionsCollectorSet(NXOpen.ExpressionCollectorSet): 
    """
    Represents a two dimension list item builder
    """
    @property
    def ItemValueTwo(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ItemValueTwo
         Returns the second expression
                  
            
         
        """
        pass
import NXOpen
class TwoExpressionsSectionSetList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[TwoExpressionsSectionSet]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: TwoExpressionsSectionSet) -> None:
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
    def Erase(self, obj: TwoExpressionsSectionSet) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: TwoExpressionsSectionSet, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: TwoExpressionsSectionSet) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> TwoExpressionsSectionSet:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( TwoExpressionsSectionSet NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[TwoExpressionsSectionSet]:
        """
         Gets the contents of the entire list 
         Returns objects ( TwoExpressionsSectionSet List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: TwoExpressionsSectionSet) -> None:
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
    def SetContents(self, objects: List[TwoExpressionsSectionSet]) -> None:
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
    def Swap(self, object1: TwoExpressionsSectionSet, object2: TwoExpressionsSectionSet) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class TwoExpressionsSectionSet(NXOpen.ExpressionSectionSet): 
    """
    Represents a two dimension list section item builder
    """
    @property
    def ItemValueTwo(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ItemValueTwo
         Returns the second expression
                  
            
         
        """
        pass
class Type(Enum):
    """
    Members Include: 
     |NoOffset|  No offset 
     |NonsymmetricOffset|  Offset with two different distances 
     |SymmetricOffset|  Offset with same distance in both directions 
     |SingleOffset|  Offset with single distance in one direction 

    """
    NoOffset: int
    NonsymmetricOffset: int
    SymmetricOffset: int
    SingleOffset: int
    @staticmethod
    def ValueOf(value: int) -> Type:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class UnitCellBuilder(NXOpen.TaggedObject): 
    """Represents a GeometricUtilities.UnitCellBuilder"""
    class UnitCellType(Enum):
        """
        Members Include: 
         |BiTriangle| 
         |TriDiametral| 
         |TriDiametralChevron| 
         |QuadDiametral| 
         |QuadDiametralLine| 
         |QuadDiametralCross| 
         |Dodecahedron| 
         |Star| 
         |HexStar| 
         |PseudoSierpinski| 
         |HexVase| 
         |HexVaseMod| 
         |Cubeplex| 
         |Octapeak| 
         |Octahedroid| 
         |FromFile| 
         |FromPart| 

        """
        BiTriangle: int
        TriDiametral: int
        TriDiametralChevron: int
        QuadDiametral: int
        QuadDiametralLine: int
        QuadDiametralCross: int
        Dodecahedron: int
        Star: int
        HexStar: int
        PseudoSierpinski: int
        HexVase: int
        HexVaseMod: int
        Cubeplex: int
        Octapeak: int
        Octahedroid: int
        FromFile: int
        FromPart: int
        @staticmethod
        def ValueOf(value: int) -> UnitCellBuilder.UnitCellType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ApproximateSourceHexMeshSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ApproximateSourceHexMeshSize
         Returns the approximate size of hexaherdal mesh element  
            
         
        """
        pass
    @property
    def CellType(self) -> UnitCellBuilder.UnitCellType:
        """
        Getter for property: ( UnitCellBuilder.UnitCellType NXOpen.Geome) CellType
         Returns the unit cell type  
            
         
        """
        pass
    @CellType.setter
    def CellType(self, cellType: UnitCellBuilder.UnitCellType):
        """
        Setter for property: ( UnitCellBuilder.UnitCellType NXOpen.Geome) CellType
         Returns the unit cell type  
            
         
        """
        pass
    @property
    def CellTypeName(self) -> str:
        """
        Getter for property: (str) CellTypeName
         Returns  the name of the unit cell type.  
           
          
                   
                   Currently there are 15 valid unit cells that are 
                   supported in NX. Their name strings are: 
                   
                   BiTriangle 
                   Cubeplex
                   Dodecahedron
                   HexStar
                   HexVase
                   HexVaseMod
                   Octapeak 
                   Octahedroid 
                   PseudoSierpinski
                   QuadDiametral
                   QuadDiametralCross
                   QuadDiametralLine
                   Star 
                   TriDiametral
                   TriDiametralChevron
                   
                     
         
        """
        pass
    @CellTypeName.setter
    def CellTypeName(self, cellTypeName: str):
        """
        Setter for property: (str) CellTypeName
         Returns  the name of the unit cell type.  
           
          
                   
                   Currently there are 15 valid unit cells that are 
                   supported in NX. Their name strings are: 
                   
                   BiTriangle 
                   Cubeplex
                   Dodecahedron
                   HexStar
                   HexVase
                   HexVaseMod
                   Octapeak 
                   Octahedroid 
                   PseudoSierpinski
                   QuadDiametral
                   QuadDiametralCross
                   QuadDiametralLine
                   Star 
                   TriDiametral
                   TriDiametralChevron
                   
                     
         
        """
        pass
    @property
    def CustomUnitCellFile(self) -> str:
        """
        Getter for property: (str) CustomUnitCellFile
         Returns the native file browser0   
            
         
        """
        pass
    @CustomUnitCellFile.setter
    def CustomUnitCellFile(self, filename: str):
        """
        Setter for property: (str) CustomUnitCellFile
         Returns the native file browser0   
            
         
        """
        pass
    @property
    def EdgeLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EdgeLength
         Returns the edge length of the unit cell bounding box, 
                     and effective only when the bounding box is a uniform cube  
            
         
        """
        pass
    @property
    def IsUniformCube(self) -> bool:
        """
        Getter for property: (bool) IsUniformCube
         Returnswhether the unit cell bounding box is a uniform cube  
            
         
        """
        pass
    @IsUniformCube.setter
    def IsUniformCube(self, uniformCube: bool):
        """
        Setter for property: (bool) IsUniformCube
         Returnswhether the unit cell bounding box is a uniform cube  
            
         
        """
        pass
    @property
    def SizeX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SizeX
         Returnsthe size of the unit cell bounding box in x axis, 
                     and effective only when the bounding box is not a uniform cube  
            
         
        """
        pass
    @property
    def SizeY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SizeY
         Returnsthe size of the unit cell bounding box in y axis, 
                     and effective only when the bounding box is not a uniform cube  
            
         
        """
        pass
    @property
    def SizeZ(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SizeZ
         Returns the size of the unit cell bounding box in z axis, 
                     and effective only when the bounding box is not a uniform cube  
            
         
        """
        pass
    @property
    def UnitCellBody(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) UnitCellBody
         Returnsthe sheet or solid body that define the seed body for body lattice type.  
            
         
        """
        pass
import NXOpen
import NXOpen.Features
class UnnestModuleBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.GeometricUtilities.UnnestModuleBuilder
     
     Note that this class is now deprecated. Please use the 
     NXOpen.Features.FeatureCollection instead.
     
     """
    @property
    def ModuleToUnnest(self) -> NXOpen.Features.SelectFeature:
        """
        Getter for property: ( NXOpen.Features.SelectFeature) ModuleToUnnest
         Returns the module to unnest 
                  
                This API is now deprecated.  
          
                Please use  NXOpen::Features::FeatureCollection::ReorganizeFeature  instead.
                  
                  
         
        """
        pass
import NXOpen
class UserDefinedColorScaleData(NXOpen.TaggedObject): 
    """ Represents color scale functions used by Face Analysis. """
    class NumberOfColorsOptions(Enum):
        """
        Members Include: 
         |Two|  2  colors. 
         |Three|  3  colors. 
         |Four|  4  colors. 
         |Five|  5  colors. 
         |Six|  6  colors. 
         |Seven|  7  colors. 
         |Eight|  8  colors. 
         |Nine|  9  colors. 
         |Ten|  10 colors. 
         |Eleven|  11 colors. 
         |Twelve|  12 colors. 

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
        def ValueOf(value: int) -> UserDefinedColorScaleData.NumberOfColorsOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Limit1(self) -> float:
        """
        Getter for property: (float) Limit1
         Returns the 1st limit.  
             
         
        """
        pass
    @Limit1.setter
    def Limit1(self, limit1: float):
        """
        Setter for property: (float) Limit1
         Returns the 1st limit.  
             
         
        """
        pass
    @property
    def Limit10(self) -> float:
        """
        Getter for property: (float) Limit10
         Returns the 10th limit.  
             
         
        """
        pass
    @Limit10.setter
    def Limit10(self, limit10: float):
        """
        Setter for property: (float) Limit10
         Returns the 10th limit.  
             
         
        """
        pass
    @property
    def Limit11(self) -> float:
        """
        Getter for property: (float) Limit11
         Returns the 11th limit.  
             
         
        """
        pass
    @Limit11.setter
    def Limit11(self, limit11: float):
        """
        Setter for property: (float) Limit11
         Returns the 11th limit.  
             
         
        """
        pass
    @property
    def Limit12(self) -> float:
        """
        Getter for property: (float) Limit12
         Returns the 12th limit.  
             
         
        """
        pass
    @Limit12.setter
    def Limit12(self, limit12: float):
        """
        Setter for property: (float) Limit12
         Returns the 12th limit.  
             
         
        """
        pass
    @property
    def Limit13(self) -> float:
        """
        Getter for property: (float) Limit13
         Returns the 13th limit.  
             
         
        """
        pass
    @Limit13.setter
    def Limit13(self, limit13: float):
        """
        Setter for property: (float) Limit13
         Returns the 13th limit.  
             
         
        """
        pass
    @property
    def Limit2(self) -> float:
        """
        Getter for property: (float) Limit2
         Returns the 2nd limit.  
             
         
        """
        pass
    @Limit2.setter
    def Limit2(self, limit2: float):
        """
        Setter for property: (float) Limit2
         Returns the 2nd limit.  
             
         
        """
        pass
    @property
    def Limit3(self) -> float:
        """
        Getter for property: (float) Limit3
         Returns the 3rd limit.  
             
         
        """
        pass
    @Limit3.setter
    def Limit3(self, limit1: float):
        """
        Setter for property: (float) Limit3
         Returns the 3rd limit.  
             
         
        """
        pass
    @property
    def Limit4(self) -> float:
        """
        Getter for property: (float) Limit4
         Returns the 4th limit.  
             
         
        """
        pass
    @Limit4.setter
    def Limit4(self, limit4: float):
        """
        Setter for property: (float) Limit4
         Returns the 4th limit.  
             
         
        """
        pass
    @property
    def Limit5(self) -> float:
        """
        Getter for property: (float) Limit5
         Returns the 5th limit.  
             
         
        """
        pass
    @Limit5.setter
    def Limit5(self, limit5: float):
        """
        Setter for property: (float) Limit5
         Returns the 5th limit.  
             
         
        """
        pass
    @property
    def Limit6(self) -> float:
        """
        Getter for property: (float) Limit6
         Returns the 6th limit.  
             
         
        """
        pass
    @Limit6.setter
    def Limit6(self, limit6: float):
        """
        Setter for property: (float) Limit6
         Returns the 6th limit.  
             
         
        """
        pass
    @property
    def Limit7(self) -> float:
        """
        Getter for property: (float) Limit7
         Returns the 7th limit.  
             
         
        """
        pass
    @Limit7.setter
    def Limit7(self, limit7: float):
        """
        Setter for property: (float) Limit7
         Returns the 7th limit.  
             
         
        """
        pass
    @property
    def Limit8(self) -> float:
        """
        Getter for property: (float) Limit8
         Returns the 8th limit.  
             
         
        """
        pass
    @Limit8.setter
    def Limit8(self, limit8: float):
        """
        Setter for property: (float) Limit8
         Returns the 8th limit.  
             
         
        """
        pass
    @property
    def Limit9(self) -> float:
        """
        Getter for property: (float) Limit9
         Returns the 9th limit.  
             
         
        """
        pass
    @Limit9.setter
    def Limit9(self, limit9: float):
        """
        Setter for property: (float) Limit9
         Returns the 9th limit.  
             
         
        """
        pass
    @property
    def NumberOfColors(self) -> UserDefinedColorScaleData.NumberOfColorsOptions:
        """
        Getter for property: ( UserDefinedColorScaleData.NumberOfColorsOptions NXOpen.Geome) NumberOfColors
         Returns the number of colors option.  
             
         
        """
        pass
    @NumberOfColors.setter
    def NumberOfColors(self, colorNumber: UserDefinedColorScaleData.NumberOfColorsOptions):
        """
        Setter for property: ( UserDefinedColorScaleData.NumberOfColorsOptions NXOpen.Geome) NumberOfColors
         Returns the number of colors option.  
             
         
        """
        pass
    def AdaptRange(self) -> None:
        """
         Adapt to actual range. 
        """
        pass
    def ExportFile(self, fileName: str) -> None:
        """
         Export to file. 
        """
        pass
    def GetColor1(self) -> List[float]:
        """
         Returns color1 
         Returns color (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def GetColor10(self) -> List[float]:
        """
         Returns color10 
         Returns color (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def GetColor11(self) -> List[float]:
        """
         Returns color11 
         Returns color (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def GetColor12(self) -> List[float]:
        """
         Returns color12 
         Returns color (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def GetColor2(self) -> List[float]:
        """
         Returns color2 
         Returns color (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def GetColor3(self) -> List[float]:
        """
         Returns color3 
         Returns color (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def GetColor4(self) -> List[float]:
        """
         Returns color4 
         Returns color (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def GetColor5(self) -> List[float]:
        """
         Returns color5 
         Returns color (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def GetColor6(self) -> List[float]:
        """
         Returns color6 
         Returns color (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def GetColor7(self) -> List[float]:
        """
         Returns color7 
         Returns color (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def GetColor8(self) -> List[float]:
        """
         Returns color8 
         Returns color (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def GetColor9(self) -> List[float]:
        """
         Returns color9 
         Returns color (List[float]):  Array of 3 RGB values, each between 0 and 1 .
        """
        pass
    def ImportFile(self, fileName: str) -> None:
        """
         Import from file. 
        """
        pass
    def InvertColors(self) -> None:
        """
         Invert color scale. 
        """
        pass
    def MakeEquidistant(self) -> None:
        """
         Make limits equidistant. 
        """
        pass
    def MakeLogarithmic(self) -> None:
        """
         Make limits logarithmic. 
        """
        pass
    def SetColor1(self, color: List[float]) -> None:
        """
         Sets color1 
        """
        pass
    def SetColor10(self, color: List[float]) -> None:
        """
         Sets color10 
        """
        pass
    def SetColor11(self, color: List[float]) -> None:
        """
         Sets color11 
        """
        pass
    def SetColor12(self, color: List[float]) -> None:
        """
         Sets color12 
        """
        pass
    def SetColor2(self, color: List[float]) -> None:
        """
         Sets color2 
        """
        pass
    def SetColor3(self, color: List[float]) -> None:
        """
         Sets color3 
        """
        pass
    def SetColor4(self, color: List[float]) -> None:
        """
         Sets color4 
        """
        pass
    def SetColor5(self, color: List[float]) -> None:
        """
         Sets color5 
        """
        pass
    def SetColor6(self, color: List[float]) -> None:
        """
         Sets color6 
        """
        pass
    def SetColor7(self, color: List[float]) -> None:
        """
         Sets color7 
        """
        pass
    def SetColor8(self, color: List[float]) -> None:
        """
         Sets color8 
        """
        pass
    def SetColor9(self, color: List[float]) -> None:
        """
         Sets color9 
        """
        pass
import NXOpen
class VoronoiItemBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[VoronoiItemBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: VoronoiItemBuilder) -> None:
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
    def Erase(self, obj: VoronoiItemBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: VoronoiItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: VoronoiItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> VoronoiItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( VoronoiItemBuilder NXOpen.Geome):  object found at input index .
        """
        pass
    def GetContents(self) -> List[VoronoiItemBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( VoronoiItemBuilder List[NXOpen.Geo):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: VoronoiItemBuilder) -> None:
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
    def SetContents(self, objects: List[VoronoiItemBuilder]) -> None:
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
    def Swap(self, object1: VoronoiItemBuilder, object2: VoronoiItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class VoronoiItemBuilder(NXOpen.Builder): 
    """ Represents a local specification of pore size and rod diameter for a Voronoi lattice """
    @property
    def PoreSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PoreSize
         Returns the pore size for the given item in the list   
            
         
        """
        pass
    @property
    def RodDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RodDiameter
         Returns the rod diameter for the given iteem in the list  
            
         
        """
        pass
    @property
    def Selection(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) Selection
         Returns the select object list which contains faces or points   
            
         
        """
        pass
import NXOpen
class VoronoiItemListBuilder(NXOpen.TaggedObject): 
    """ the builder for a list of GeometricUtilities.VoronoiItemBuilder objects """
    @property
    def List(self) -> VoronoiItemBuilderList:
        """
        Getter for property: ( VoronoiItemBuilderList NXOpen.Geome) List
         Returns a list of  GeometricUtilities::VoronoiItemBuilder  objects   
            
         
        """
        pass
    def CreateVoronoiItemBuilder(self) -> VoronoiItemBuilder:
        """
         Creates a GeometricUtilities.VoronoiItemBuilder 
         Returns builder ( VoronoiItemBuilder NXOpen.Geome): .
        """
        pass
import NXOpen
import NXOpen.Features
class WaveLinkRepository(NXOpen.NXObject): 
    """
    Represents a  NXOpen.GeometricUtilities.WaveLinkRepository.
    This object performs the task of embedding the link features created by 
    the command. It also cleans up unused links.
    """
    def Destroy(self) -> None:
        """
         Destroy the link repository 
        """
        pass
    def SetBuilder(self, builder: NXOpen.Builder) -> None:
        """
         Set the builder of the active command.If the builder is feat builder, 
                 then the feature from the builder will be queried and used as master feature. 
                 This master feature is needed to populate the repository with existing slave links on the feature.
        """
        pass
    def SetLink(self, linkFeature: NXOpen.Features.Feature) -> None:
        """
         Set the link created by interpart selection 
        """
        pass
    def SetNonFeatureApplication(self, flag: bool) -> None:
        """
         Specify if the client is non-feature based application or not. This flag
                 is used by the repository to properly clean up unused links. 
        """
        pass
