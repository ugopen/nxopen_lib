from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
class AddendumSectionBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a NXOpen.Die.AddendumSectionBuilder which is used to create or edit an addendum section.
    """
    class SectionLocationType(Enum):
        """
        Members Include: 
         |AtPoint|  Create section at a point. 
         |AtPlane|  Create section at a plane. 
         |WithCurve|  Create section by approximating curves. 

        """
        AtPoint: int
        AtPlane: int
        WithCurve: int
        @staticmethod
        def ValueOf(value: int) -> AddendumSectionBuilder.SectionLocationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SectionOrientationType(Enum):
        """
        Members Include: 
         |Default|  Orient perpendicular to tangency curve. 
         |ThreeDPerpendicular|  Orient 3D perpendicular to tangency curve 
         |Conjugate|  Use conjugate orientation. 
         |Isoparametric|  Orient along isoparametric line of closest face. 
         |IncidentEdge|  Orient from incident edge. 
         |Blank|  No orientation. 

        """
        Default: int
        ThreeDPerpendicular: int
        Conjugate: int
        Isoparametric: int
        IncidentEdge: int
        Blank: int
        @staticmethod
        def ValueOf(value: int) -> AddendumSectionBuilder.SectionOrientationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SectionShapeType(Enum):
        """
        Members Include: 
         |Basic|  Section consists of all segments in a step like shape. 
         |DrawBar|  Section consists of all segments in a draw bar shape. 
         |Simple|  Section consists of trim ledge, punch radius, and second stretch wall segments. 
         |Channel|  Section consists of all segments in a channel shape. 
         |Blend|  Section consists of a single radius type segment to define the blend shape. 
         |Extension|  Section consists of a plus segment only. 
         |System|  Section shape determined by blending neighboring sections. 
         |UserDefined|  Section shape is user defined. 
         |Reuse|  Section shape is read from reuse library. 
         |Blank|  No section shape. 

        """
        Basic: int
        DrawBar: int
        Simple: int
        Channel: int
        Blend: int
        Extension: int
        System: int
        UserDefined: int
        Reuse: int
        Blank: int
        @staticmethod
        def ValueOf(value: int) -> AddendumSectionBuilder.SectionShapeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SegmentParameterType(Enum):
        """
        Members Include: 
         |Length|  The length parameter of a straight segment. 
         |Angle|  The angle parameter of a straight segment. 
         |Radius|  The radius parameter of an arc segment. 
         |ArcLength|  The arc length parameter of an arc segment. 

        """
        Length: int
        Angle: int
        Radius: int
        ArcLength: int
        @staticmethod
        def ValueOf(value: int) -> AddendumSectionBuilder.SegmentParameterType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SegmentType(Enum):
        """
        Members Include: 
         |Plus|  Update plus segment. 
         |Punch|  Update punch segment. 
         |FirstStretchWall|  Update first stretch wall segment. 
         |Reverse|  Update reverse segment. 
         |TrimLedge|  Update trim ledge segment. 
         |DiePunch|  Update die punch segment. 
         |SecondStretchWall|  Update second stretch wall segment. 
         |DieReverse|  Update die reverse segment. 
         |FlatToBead|  Update flat to bead segment. 

        """
        Plus: int
        Punch: int
        FirstStretchWall: int
        Reverse: int
        TrimLedge: int
        DiePunch: int
        SecondStretchWall: int
        DieReverse: int
        FlatToBead: int
        @staticmethod
        def ValueOf(value: int) -> AddendumSectionBuilder.SegmentType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SurfaceBuildType(Enum):
        """
        Members Include: 
         |NoSurface|  Do not create a surface. 
         |Sectional|  Create sectional sweep surface. 
         |CurveMesh|  Create curve mesh surface. 
         |ChannelTunnelCap|  Create channel tunnel cap surface. 
         |MultipleFaceBlend|  Create multiple face blend surface. 
         |WallsOnly|  Create walls only surface. 
         |DiskFaceBlend|  Create disc blend surface. 
         |SphereFaceBlend|  Create spherical blend surface. 

        """
        NoSurface: int
        Sectional: int
        CurveMesh: int
        ChannelTunnelCap: int
        MultipleFaceBlend: int
        WallsOnly: int
        DiskFaceBlend: int
        SphereFaceBlend: int
        @staticmethod
        def ValueOf(value: int) -> AddendumSectionBuilder.SurfaceBuildType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngleTolerance(self) -> float:
        """
        Getter for property: (float) AngleTolerance
         Returns the angle tolerance.  
             
         
        """
        pass
    @AngleTolerance.setter
    def AngleTolerance(self, angleTolerance: float):
        """
        Setter for property: (float) AngleTolerance
         Returns the angle tolerance.  
             
         
        """
        pass
    @property
    def Attributes(self) -> DieAttributesBuilder:
        """
        Getter for property: ( DieAttributesBuilder NXOp) Attributes
         Returns the color and string attributes of the section.  
             
         
        """
        pass
    @property
    def ByCurves(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) ByCurves
         Returns the curves used to approximate an addendum section.  
             
         
        """
        pass
    @property
    def ConstraintCurve(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) ConstraintCurve
         Returns the constraint curve.  
             
         
        """
        pass
    @property
    def ConstraintCurveToEdit(self) -> NXOpen.Curve:
        """
        Getter for property: ( NXOpen.Curve) ConstraintCurveToEdit
         Returns the constraint curve to edit.  
            This function will read the objects using  NXOpen::Die::AddendumSectionBuilder::ConstraintCurve .
                    and if needed create a non-associative curve to be used by the edit curve functions.  The only case where it will
                    not create a curve is if there is only one non-associative spline on the selection.             
                  
         
        """
        pass
    @property
    def ConstraintFaces(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) ConstraintFaces
         Returns the constraint faces.  
             
         
        """
        pass
    @property
    def CurveToExtend(self) -> NXOpen.Curve:
        """
        Getter for property: ( NXOpen.Curve) CurveToExtend
         Returns the constraint curve to extend.  
             
         
        """
        pass
    @CurveToExtend.setter
    def CurveToExtend(self, curve: NXOpen.Curve):
        """
        Setter for property: ( NXOpen.Curve) CurveToExtend
         Returns the constraint curve to extend.  
             
         
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
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance.  
             
         
        """
        pass
    @property
    def DrawDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) DrawDirection
         Returns the draw direction.  
             
         
        """
        pass
    @DrawDirection.setter
    def DrawDirection(self, drawDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) DrawDirection
         Returns the draw direction.  
             
         
        """
        pass
    @property
    def EditedConstraintCurve(self) -> NXOpen.Curve:
        """
        Getter for property: ( NXOpen.Curve) EditedConstraintCurve
         Returns the edited constraint curve.  
             
         
        """
        pass
    @EditedConstraintCurve.setter
    def EditedConstraintCurve(self, curve: NXOpen.Curve):
        """
        Setter for property: ( NXOpen.Curve) EditedConstraintCurve
         Returns the edited constraint curve.  
             
         
        """
        pass
    @property
    def ExtendData(self) -> NXOpen.GeometricUtilities.CurveLengthData:
        """
        Getter for property: ( NXOpen.GeometricUtilities.CurveLengthData) ExtendData
         Returns the object used to extend the constraint curve which is accessed via  NXOpen::Die::AddendumSectionBuilder::ConstraintCurve .  
           
                    Need to call function  NXOpen::Die::AddendumSectionBuilder::CreateExtendSection  before calling this function.
                  
         
        """
        pass
    @property
    def ExtendEndDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ExtendEndDistance
         Returns the distance to extend the end of the constraint curve.  
             
         
        """
        pass
    @property
    def ExtendStartDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ExtendStartDistance
         Returns the distance to extend the start of the constraint curve.  
             
         
        """
        pass
    @property
    def FacetDensity(self) -> float:
        """
        Getter for property: (float) FacetDensity
         Returns the facet density.  
             
         
        """
        pass
    @FacetDensity.setter
    def FacetDensity(self, facetDensity: float):
        """
        Setter for property: (float) FacetDensity
         Returns the facet density.  
             
         
        """
        pass
    @property
    def Limits(self) -> DieLimitsBuilder:
        """
        Getter for property: ( DieLimitsBuilder NXOp) Limits
         Returns the limits to control the span of the preview surface   
            
         
        """
        pass
    @property
    def LocationType(self) -> AddendumSectionBuilder.SectionLocationType:
        """
        Getter for property: ( AddendumSectionBuilder.SectionLocationType NXOp) LocationType
         Returns the location where the section will be created.  
             
         
        """
        pass
    @LocationType.setter
    def LocationType(self, locationType: AddendumSectionBuilder.SectionLocationType):
        """
        Setter for property: ( AddendumSectionBuilder.SectionLocationType NXOp) LocationType
         Returns the location where the section will be created.  
             
         
        """
        pass
    @property
    def MaximumPositive(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumPositive
         Returns the maximum positive trim angle.  
             
         
        """
        pass
    @property
    def MinimumDraftAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumDraftAngle
         Returns the minimum draft angle.  
             
         
        """
        pass
    @property
    def MinimumNegative(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumNegative
         Returns the minimum negative trim angle.  
             
         
        """
        pass
    @property
    def MinimumRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumRadius
         Returns the minimum radius.  
             
         
        """
        pass
    @property
    def MinimumTrimLedge(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumTrimLedge
         Returns the minimum trim ledge.  
             
         
        """
        pass
    @property
    def MirrorPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) MirrorPlane
         Returns the mirror plane.  
             
         
        """
        pass
    @MirrorPlane.setter
    def MirrorPlane(self, mirrorPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) MirrorPlane
         Returns the mirror plane.  
             
         
        """
        pass
    @property
    def NeutralCurve(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) NeutralCurve
         Returns the neutral curve.  
             
         
        """
        pass
    @property
    def PlusLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PlusLength
         Returns the minimum plus length.  
             
         
        """
        pass
    @property
    def Product(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Product
         Returns the product faces.  
             
         
        """
        pass
    @property
    def SectionOrientation(self) -> AddendumSectionBuilder.SectionOrientationType:
        """
        Getter for property: ( AddendumSectionBuilder.SectionOrientationType NXOp) SectionOrientation
         Returns the section orientation.  
             
         
        """
        pass
    @SectionOrientation.setter
    def SectionOrientation(self, sectionOrientation: AddendumSectionBuilder.SectionOrientationType):
        """
        Setter for property: ( AddendumSectionBuilder.SectionOrientationType NXOp) SectionOrientation
         Returns the section orientation.  
             
         
        """
        pass
    @property
    def SectionPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) SectionPlane
         Returns the section plane.  
             
         
        """
        pass
    @SectionPlane.setter
    def SectionPlane(self, sectionPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) SectionPlane
         Returns the section plane.  
             
         
        """
        pass
    @property
    def SectionPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) SectionPoint
         Returns the origin point where the section will be located.  
             
         
        """
        pass
    @SectionPoint.setter
    def SectionPoint(self, sectionPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) SectionPoint
         Returns the origin point where the section will be located.  
             
         
        """
        pass
    @property
    def SectionShape(self) -> AddendumSectionBuilder.SectionShapeType:
        """
        Getter for property: ( AddendumSectionBuilder.SectionShapeType NXOp) SectionShape
         Returns the section shape.  
             
         
        """
        pass
    @SectionShape.setter
    def SectionShape(self, sectionShape: AddendumSectionBuilder.SectionShapeType):
        """
        Setter for property: ( AddendumSectionBuilder.SectionShapeType NXOp) SectionShape
         Returns the section shape.  
             
         
        """
        pass
    @property
    def Sections(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) Sections
         Returns the addendum sections to edit.  
             
         
        """
        pass
    @property
    def SmoothRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SmoothRadius
         Returns the smoothing radius for the constraint curve used by  NXOpen::Die::AddendumSectionBuilder::SmoothCurve .  
             
         
        """
        pass
    @property
    def SurfaceBuildMethod(self) -> AddendumSectionBuilder.SurfaceBuildType:
        """
        Getter for property: ( AddendumSectionBuilder.SurfaceBuildType NXOp) SurfaceBuildMethod
         Returns the addendum surface build method.  
             
         
        """
        pass
    @SurfaceBuildMethod.setter
    def SurfaceBuildMethod(self, surfaceBuildMethod: AddendumSectionBuilder.SurfaceBuildType):
        """
        Setter for property: ( AddendumSectionBuilder.SurfaceBuildType NXOp) SurfaceBuildMethod
         Returns the addendum surface build method.  
             
         
        """
        pass
    @property
    def TranslateDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TranslateDistance
         Returns the translate distance used by  NXOpen::Die::AddendumSectionBuilder::TranslateWall .  
             
         
        """
        pass
    def ChangeSectionPlane(self, section: NXOpen.Curve, plane: NXOpen.Direction) -> None:
        """
         Changes the section orientation. 
        """
        pass
    def CopySection(self, section: NXOpen.Curve, copyPlaneData: bool) -> None:
        """
         Copies addendum section in order to be pasted at another location. 
        """
        pass
    def CreateExtendSection(self) -> NXOpen.Section:
        """
         Creates a NXOpen.Section object containing the extended constraint curve. 
         Returns section ( NXOpen.Section): .
        """
        pass
    def CreateSection(self) -> None:
        """
         Create addendum section using previously supplied parameters. 
        """
        pass
    def CreateSectionFromReuse(self, file_name: str) -> None:
        """
         Creates a section using the information stored in the reuse library. 
                
        """
        pass
    def CutSection(self, section: NXOpen.Curve, copyPlaneData: bool) -> None:
        """
         Cuts section in order to be pasted at another location. 
        """
        pass
    def DefaultDraw(self) -> None:
        """
         Create default draw vector based upon the input product faces. 
        """
        pass
    def DeleteExtendSection(self) -> NXOpen.Section:
        """
         Deletes the NXOpen.Section used for extended constraint curve. 
         Returns section ( NXOpen.Section):  NXOpen.Section to delete. .
        """
        pass
    def DeleteSections(self) -> None:
        """
         Delete addendum sections from NXOpen.Die.AddendumSectionBuilder.Sections. 
        """
        pass
    def EditBlendSection(self, section: NXOpen.Curve, radius: float) -> None:
        """
         Edit radius value of blend section. 
        """
        pass
    def InitializeEditParameters(self, section: NXOpen.Curve) -> None:
        """
         Initializes environment to start editing parameters of a section.  
        """
        pass
    def LockSegment(self, section: NXOpen.Curve, segment: AddendumSectionBuilder.SegmentType, type: AddendumSectionBuilder.SegmentParameterType) -> None:
        """
         Lock a segment parameter value. 
        """
        pass
    def MirrorSections(self) -> None:
        """
         Mirror sections using plane from NXOpen.Die.AddendumSectionBuilder.MirrorPlane. 
        """
        pass
    def MoveSectionOrigin(self, section: NXOpen.Curve, newOrigin: NXOpen.Point3d, useSectionPlane: int) -> None:
        """
         Moves addendum section to a new location. 
        """
        pass
    def PasteSection(self) -> None:
        """
         Paste section. 
        """
        pass
    def PasteSectionFromCurve(self, curve: NXOpen.Curve) -> None:
        """
         Creates a section by reading the section parameters from the input curve and pasting at 
                    the location specified by NXOpen.Die.AddendumSectionBuilder.SectionPoint
                
        """
        pass
    def RecreateSections(self) -> None:
        """
         Re-create all existing sections because of a change in the draw direction or product faces. 
        """
        pass
    def Reinitialize(self) -> None:
        """
         Reinitialize the environment after changes to input data such as draw vector or product faces 
        """
        pass
    def ReplaceConstraintCurve(self, editedCurve: NXOpen.Curve) -> None:
        """
         Replaces the constraint curve with an edited curve. 
        """
        pass
    def ReplaceSectionCurve(self, section: NXOpen.Curve) -> None:
        """
         Replaces the current section with the edited one. 
        """
        pass
    def ResetSection(self, section: NXOpen.Curve) -> None:
        """
         Resets the section to the last saved state. 
        """
        pass
    def SmoothCurve(self) -> None:
        """
         Smooth the constraint curve using the radius supplied by NXOpen.Die.AddendumSectionBuilder.SmoothRadius. 
        """
        pass
    def TerminateEditParameters(self, section: NXOpen.Curve) -> None:
        """
         Cleans up environment after editing parameters of a section.  
        """
        pass
    def TranslateWall(self) -> None:
        """
         Translate the constraint curve in the direction of the last wall segment of the addendum section using the 
                    distance supplied by NXOpen.Die.AddendumSectionBuilder.TranslateDistance.
                 
        """
        pass
    def TrimExtendConstraintCurve(self, constraintCurve: NXOpen.Section) -> None:
        """
         Trims or extends constraint curve. 
        """
        pass
    def UnlockSegment(self, section: NXOpen.Curve, segment: AddendumSectionBuilder.SegmentType, type: AddendumSectionBuilder.SegmentParameterType) -> None:
        """
         Unlock a segment parameter value. 
        """
        pass
    def UpdateSection(self, section: NXOpen.Curve) -> None:
        """
         Updates section after editing segments via NXOpen.Die.AddendumSectionBuilder.UpdateSegment. 
                    This makes permanent the temporary changes so that any future calls to NXOpen.Die.AddendumSectionBuilder.ResetSection
                    will reset the section to this state.
                
        """
        pass
    def UpdateSectionAttributes(self, section: NXOpen.Curve) -> None:
        """
         Updates the section attributes. You must call NXOpen.Die.AddendumSectionBuilder.Attributes 
                    first in order to set the attributes to be updated.
                
        """
        pass
    def UpdateSectionsAfterConstraintChange(self) -> None:
        """
         Called to update the section when constraint curve or constraint surface is changed. 
        """
        pass
    def UpdateSegment(self, temporary: bool, section: NXOpen.Curve, segment: AddendumSectionBuilder.SegmentType, lengthRadius: float, angle: float) -> float:
        """
         Updates length or angle value of a segment. 
         Returns flangeLength (float):  Computed flange length value. .
        """
        pass
import NXOpen
class AddendumSectionUserDefinedBuilder(NXOpen.Builder): 
    """ 
     Represents a NXOpen.Die.AddendumSectionUserDefinedBuilder builder used to select a previously
     defined section or a string of objects to define the section shape.
    """
    @property
    def ReverseAnchorPoint(self) -> bool:
        """
        Getter for property: (bool) ReverseAnchorPoint
         Returns the indicator to reverse the anchor point.  
            The anchor point is initially the first point of the joined string of
                    selected objects.  This is used as the starting point for the section when it is placed on the tangency curve.
                    It can be reversed to use the other end of the string as the starting point. 
                   
         
        """
        pass
    @ReverseAnchorPoint.setter
    def ReverseAnchorPoint(self, reverseAnchorPoint: bool):
        """
        Setter for property: (bool) ReverseAnchorPoint
         Returns the indicator to reverse the anchor point.  
            The anchor point is initially the first point of the joined string of
                    selected objects.  This is used as the starting point for the section when it is placed on the tangency curve.
                    It can be reversed to use the other end of the string as the starting point. 
                   
         
        """
        pass
    @property
    def Section(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Section
         Returns the objects defining the section, either a previously defined section or a string of objects defining the section shape.  
             
         
        """
        pass
    def CreateUserDefinedSection(self) -> NXOpen.Curve:
        """
         Creates user defined addendum section based upon input to NXOpen.Die.AddendumSectionUserDefinedBuilder.Section. 
         Returns outputCurve ( NXOpen.Curve):  user defined section curve .
        """
        pass
import NXOpen
import NXOpen.Features
class AddSurfBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a NXOpen.Die.AddSurfBuilder builder
    """
    class Methods(Enum):
        """
        Members Include: 
         |Sectional|  Sweep section around tangency curve. 
         |CurveMesh|  Modeling curve mesh. 
         |ChannelTunnelCap|  To close an end cap. 
         |MultiFaceBlend|  Face blend between sets of walls. 
         |WallsOnly|  Produces just the walls, no blend. 
         |DiskFaceBlend|  Disk type face blend. 
         |SphereFaceBlend|  Spherical type face blend. 

        """
        Sectional: int
        CurveMesh: int
        ChannelTunnelCap: int
        MultiFaceBlend: int
        WallsOnly: int
        DiskFaceBlend: int
        SphereFaceBlend: int
        @staticmethod
        def ValueOf(value: int) -> AddSurfBuilder.Methods:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns the flag that indicates during creation if a feature is to be created or just the sheet body,
                    true indicates a feature will be created.  
             
         
        """
        pass
    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
         Returns the flag that indicates during creation if a feature is to be created or just the sheet body,
                    true indicates a feature will be created.  
             
         
        """
        pass
    @property
    def ConcaveCornerRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ConcaveCornerRadius
         Returns the concave corner radius value   
            
         
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
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance.  
             
         
        """
        pass
    @property
    def Limits(self) -> DieLimitsBuilder:
        """
        Getter for property: ( DieLimitsBuilder NXOp) Limits
         Returns the limits to control the span of the addendum   
            
         
        """
        pass
    @property
    def Method(self) -> AddSurfBuilder.Methods:
        """
        Getter for property: ( AddSurfBuilder.Methods NXOp) Method
         Returns the addendum surface output method.  
             
         
        """
        pass
    @Method.setter
    def Method(self, type: AddSurfBuilder.Methods):
        """
        Setter for property: ( AddSurfBuilder.Methods NXOp) Method
         Returns the addendum surface output method.  
             
         
        """
        pass
    @property
    def RefPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) RefPoint
         Returns the keep point for trimming.  
             
         
        """
        pass
    @RefPoint.setter
    def RefPoint(self, point0: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) RefPoint
         Returns the keep point for trimming.  
             
         
        """
        pass
    @property
    def SelectSection(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SelectSection
         Returns the addendum section feature to define the shape of the addendum surface.  
             
         
        """
        pass
    @property
    def Sewn(self) -> bool:
        """
        Getter for property: (bool) Sewn
         Returns the flag that indicates whether the faces of the addendum sheet body will be sewn into one sheet body
                    or individual sheet bodies for each face will be output.  
            True indicates one sewn sheet body will be output.   
         
        """
        pass
    @Sewn.setter
    def Sewn(self, sewn: bool):
        """
        Setter for property: (bool) Sewn
         Returns the flag that indicates whether the faces of the addendum sheet body will be sewn into one sheet body
                    or individual sheet bodies for each face will be output.  
            True indicates one sewn sheet body will be output.   
         
        """
        pass
    @property
    def Spine(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Spine
         Returns the spine string, which determines the orientation of the sample planes   
            
         
        """
        pass
    @property
    def SpineRadius(self) -> float:
        """
        Getter for property: (float) SpineRadius
         Returns the spine radius, used by  NXOpen::Die::AddSurfBuilder::CreateDefaultSpine    
            
         
        """
        pass
    @SpineRadius.setter
    def SpineRadius(self, spineRadius: float):
        """
        Setter for property: (float) SpineRadius
         Returns the spine radius, used by  NXOpen::Die::AddSurfBuilder::CreateDefaultSpine    
            
         
        """
        pass
    @property
    def TrimBound(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) TrimBound
         Returns the trimming boundary for the addendum surface.  
             
         
        """
        pass
    def CreateDefaultSpine(self) -> None:
        """
         Creates a smoothed spine curve from the forming boundary using the spine radius value 
        """
        pass
import NXOpen
import NXOpen.Features
class CastReliefBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a NXOpen.Die.CastReliefBuilder builder
    """
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
    def BaseOrientation(self) -> DiePlaneBuilder:
        """
        Getter for property: ( DiePlaneBuilder NXOp) BaseOrientation
         Returns the base orientation of the die casting used for orienting the relief construction   
            
         
        """
        pass
    @property
    def CreateSupportCasting(self) -> bool:
        """
        Getter for property: (bool) CreateSupportCasting
         Returns the value (true or false) to decide if support casting should be created   
            
         
        """
        pass
    @CreateSupportCasting.setter
    def CreateSupportCasting(self, createSupportCasting: bool):
        """
        Setter for property: (bool) CreateSupportCasting
         Returns the value (true or false) to decide if support casting should be created   
            
         
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
    def ReliefDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ReliefDepth
         Returns the depth value of the relief   
            
         
        """
        pass
    @property
    def ReliefProfile(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) ReliefProfile
         Returns the closed profiles used for determining the relief   
            
         
        """
        pass
    @property
    def ReliefSheet(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) ReliefSheet
         Returns the sheet to offset to specify the relief surface   
            
         
        """
        pass
    @property
    def SheetMetal(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) SheetMetal
         Returns the sheet that specifies the sheet metal surface   
            
         
        """
        pass
    @property
    def Target(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) Target
         Returns the target solid the relief will be united with   
            
         
        """
        pass
    @property
    def Thickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Thickness
         Returns the thickness value of the support casting surrounding the relief   
            
         
        """
        pass
import NXOpen
import NXOpen.Features
class CastReliefParentBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Die Cast Relief sub feature. """
    @property
    def BuildStatus(self) -> DieBuildStatusOption:
        """
        Getter for property: ( DieBuildStatusOption NXOp) BuildStatus
         Returns the build status of cast relief.  
             
         
        """
        pass
    @property
    def DesignStatus(self) -> bool:
        """
        Getter for property: (bool) DesignStatus
         Returns the design status of cast relief, if true the cast relief will be built into the model, if false it will not.  
             
         
        """
        pass
    @DesignStatus.setter
    def DesignStatus(self, design_status: bool):
        """
        Setter for property: (bool) DesignStatus
         Returns the design status of cast relief, if true the cast relief will be built into the model, if false it will not.  
             
         
        """
        pass
    @property
    def DisplayStatus(self) -> bool:
        """
        Getter for property: (bool) DisplayStatus
         Returns the display status of cast relief, if true input data to the cast relief will be displayed, if false the input data will not be displayed.  
             
         
        """
        pass
    @DisplayStatus.setter
    def DisplayStatus(self, display_status: bool):
        """
        Setter for property: (bool) DisplayStatus
         Returns the display status of cast relief, if true input data to the cast relief will be displayed, if false the input data will not be displayed.  
             
         
        """
        pass
    @property
    def ReliefDepth(self) -> float:
        """
        Getter for property: (float) ReliefDepth
         Returns the relief depth of cast relief.  
             
         
        """
        pass
    @ReliefDepth.setter
    def ReliefDepth(self, relief_depth: float):
        """
        Setter for property: (float) ReliefDepth
         Returns the relief depth of cast relief.  
             
         
        """
        pass
    @property
    def ReliefSheet(self) -> NXOpen.Body:
        """
        Getter for property: ( NXOpen.Body) ReliefSheet
         Returns the relief sheet of cast relief.  
             
         
        """
        pass
    @ReliefSheet.setter
    def ReliefSheet(self, relief_sheet: NXOpen.Body):
        """
        Setter for property: ( NXOpen.Body) ReliefSheet
         Returns the relief sheet of cast relief.  
             
         
        """
        pass
    def GetCastRelief(self) -> Tuple[List[NXOpen.IProfile], DirectionOption]:
        """
         Gets the profile of the cast relief. 
         Returns A tuple consisting of (profile_entries, direction). 
         - profile_entries is:  NXOpen.IProfile Li. The profile entries, will be curves, edges, faces, sketches or curve features. .
         - direction is:  DirectionOption NXOp. Profile direction. .

        """
        pass
    def SetCastRelief(self, direction: DirectionOption, profile_entries: List[NXOpen.IProfile]) -> None:
        """
         Sets the profile of the cast relief. 
        """
        pass
import NXOpen.Features
class CastRelief(NXOpen.Features.BodyFeature): 
    """ Represents a cast relief feature """
    pass
import NXOpen
import NXOpen.Features
class ClampingSlotBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a Clamping Slot feature builder
    """
    class Types(Enum):
        """
        Members Include: 
         |Hydraulic|  
         |Traveling|  
         |Automatic|  

        """
        Hydraulic: int
        Traveling: int
        Automatic: int
        @staticmethod
        def ValueOf(value: int) -> ClampingSlotBuilder.Types:
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
    def BasePlane(self) -> DiePlaneBuilder:
        """
        Getter for property: ( DiePlaneBuilder NXOp) BasePlane
         Returns the base plane of the clamping slot pad   
            
         
        """
        pass
    @property
    def CenterlineLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CenterlineLength
         Returns the length from the location to the flange   
            
         
        """
        pass
    @property
    def DieCenterlineCoordinateSystem(self) -> NXOpen.SelectCartesianCoordinateSystem:
        """
        Getter for property: ( NXOpen.SelectCartesianCoordinateSystem) DieCenterlineCoordinateSystem
         Returns the die centerline coordinate system for orienting the slot   
            
         
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
    def FlangeBaseProfile(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) FlangeBaseProfile
         Returns the closed profile of the flange base   
            
         
        """
        pass
    @property
    def FlangeThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlangeThickness
         Returns the thickness of the flange   
            
         
        """
        pass
    @property
    def InnerWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InnerWidth
         Returns the width of the cutout at the back of the slot   
            
         
        """
        pass
    @property
    def LocationOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LocationOffset
         Returns the amount to move along the location offset direction if specified   
            
         
        """
        pass
    @property
    def LocationOffsetDirection(self) -> DieDirectionBuilder:
        """
        Getter for property: ( DieDirectionBuilder NXOp) LocationOffsetDirection
         Returns the direction to offset the clampslot locations if needed   
            
         
        """
        pass
    @property
    def LocationOnFlange(self) -> bool:
        """
        Getter for property: (bool) LocationOnFlange
         Returns the toggle to identify if the location should be mapped to the flange before building   
            
         
        """
        pass
    @LocationOnFlange.setter
    def LocationOnFlange(self, locationOnFlange: bool):
        """
        Setter for property: (bool) LocationOnFlange
         Returns the toggle to identify if the location should be mapped to the flange before building   
            
         
        """
        pass
    @property
    def Locations(self) -> DieLocationsBuilder:
        """
        Getter for property: ( DieLocationsBuilder NXOp) Locations
         Returns the locations for the clamping slots   
            
         
        """
        pass
    @property
    def NotchAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NotchAngle
         Returns the angle of the notch with respect to the base of the pad  
            
         
        """
        pass
    @property
    def NotchFacesAttributes(self) -> DieAttributesBuilder:
        """
        Getter for property: ( DieAttributesBuilder NXOp) NotchFacesAttributes
         Returns the attributes for the notch faces   
            
         
        """
        pass
    @property
    def NotchHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NotchHeight
         Returns the height of the notch on the pad from the base   
            
         
        """
        pass
    @property
    def NotchWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NotchWidth
         Returns the width from the center of the slot to the outer edge of the notch   
            
         
        """
        pass
    @property
    def OffsetWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OffsetWidth
         Returns the width of the additional flange casting added for pad support   
            
         
        """
        pass
    @property
    def OrientationPlane(self) -> DiePlaneBuilder:
        """
        Getter for property: ( DiePlaneBuilder NXOp) OrientationPlane
         Returns the top orientation plane of the clamping slot pad   
            
         
        """
        pass
    @property
    def Overhang(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Overhang
         Returns the amount the pad will overhang from the flange   
            
         
        """
        pass
    @property
    def OverhangFacesAttributes(self) -> DieAttributesBuilder:
        """
        Getter for property: ( DieAttributesBuilder NXOp) OverhangFacesAttributes
         Returns the attributes for the overhang faces   
            
         
        """
        pass
    @property
    def PadFacesAttributes(self) -> DieAttributesBuilder:
        """
        Getter for property: ( DieAttributesBuilder NXOp) PadFacesAttributes
         Returns the attributes for the pad faces  
            
         
        """
        pass
    @property
    def PadHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PadHeight
         Returns the height of the pad   
            
         
        """
        pass
    @property
    def PadLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PadLength
         Returns the length of the pad from front to back   
            
         
        """
        pass
    @property
    def PadOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PadOffset
         Returns the amount to offset from the pad orientation to determine true top of pad   
            
         
        """
        pass
    @property
    def PadRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PadRadius
         Returns the radius of the pad at the back corners   
            
         
        """
        pass
    @property
    def PadWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PadWidth
         Returns the width of the pad   
            
         
        """
        pass
    @property
    def SlotEndFacesAttributes(self) -> DieAttributesBuilder:
        """
        Getter for property: ( DieAttributesBuilder NXOp) SlotEndFacesAttributes
         Returns the attributes for the end faces of the slot  
            
         
        """
        pass
    @property
    def SlotFacesAttributes(self) -> DieAttributesBuilder:
        """
        Getter for property: ( DieAttributesBuilder NXOp) SlotFacesAttributes
         Returns the attributes for the slot faces   
            
         
        """
        pass
    @property
    def SlotLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SlotLength
         Returns the length of the slot   
            
         
        """
        pass
    @property
    def SlotRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SlotRadius
         Returns the radius of the back cutout   
            
         
        """
        pass
    @property
    def SlotWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SlotWidth
         Returns the width of the slot   
            
         
        """
        pass
    @property
    def Target(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) Target
         Returns the target solid the clamp slots will be united with   
            
         
        """
        pass
    @property
    def TopLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TopLength
         Returns the distance from the front of the slot to the back cutout   
            
         
        """
        pass
    @property
    def Type(self) -> ClampingSlotBuilder.Types:
        """
        Getter for property: ( ClampingSlotBuilder.Types NXOp) Type
         Returns the clamping slot type to build   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: ClampingSlotBuilder.Types):
        """
        Setter for property: ( ClampingSlotBuilder.Types NXOp) Type
         Returns the clamping slot type to build   
            
         
        """
        pass
import NXOpen.Features
class ClampingSlot(NXOpen.Features.BodyFeature): 
    """ Represents a clamping slot feature """
    pass
import NXOpen
import NXOpen.Features
class ClearanceBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a builder that is used to create or edit a NXOpen.Die.Clearance feature.
    """
    class ClearanceGeometryTypes(Enum):
        """
        Members Include: 
         |Solid|  The input is solids. 
         |Section|  The input is closed profiles. 

        """
        Solid: int
        Section: int
        @staticmethod
        def ValueOf(value: int) -> ClearanceBuilder.ClearanceGeometryTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |Gage|  Clearance will be provided encompassing gage solids. 
         |Gripper|  Clearance will be provided encompassing gripper, or transfer, machinery solids. 
         |Lifter|  Clearance will be provided encompassing interior casting lifting solids. 

        """
        Gage: int
        Gripper: int
        Lifter: int
        @staticmethod
        def ValueOf(value: int) -> ClearanceBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngleTolerance(self) -> float:
        """
        Getter for property: (float) AngleTolerance
         Returns the angle tolerance.  
             
         
        """
        pass
    @AngleTolerance.setter
    def AngleTolerance(self, angleTolerance: float):
        """
        Setter for property: (float) AngleTolerance
         Returns the angle tolerance.  
             
         
        """
        pass
    @property
    def Attributes(self) -> DieAttributesBuilder:
        """
        Getter for property: ( DieAttributesBuilder NXOp) Attributes
         Returns the attribute title, value and face color to apply to the clearance faces.  
             
         
        """
        pass
    @property
    def ClearanceDirection(self) -> DieDirectionBuilder:
        """
        Getter for property: ( DieDirectionBuilder NXOp) ClearanceDirection
         Returns the direction to use when extruding to create the clearance areas.  
             
         
        """
        pass
    @property
    def ClearanceGeometryType(self) -> ClearanceBuilder.ClearanceGeometryTypes:
        """
        Getter for property: ( ClearanceBuilder.ClearanceGeometryTypes NXOp) ClearanceGeometryType
         Returns the input type of the clearance geometry.  
             
         
        """
        pass
    @ClearanceGeometryType.setter
    def ClearanceGeometryType(self, clearanceGeometryType: ClearanceBuilder.ClearanceGeometryTypes):
        """
        Setter for property: ( ClearanceBuilder.ClearanceGeometryTypes NXOp) ClearanceGeometryType
         Returns the input type of the clearance geometry.  
             
         
        """
        pass
    @property
    def Distance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Distance
         Returns the expression containing the distance value for extrusions when defining the clearance area.  
          
                    If the value is 0.0, then a value will be generated from the target solid.   
         
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
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance.  
             
         
        """
        pass
    @property
    def Geometry(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: ( NXOpen.SelectBodyList) Geometry
         Returns the solid to use for the basis of the clearance area.  
           Only valid when type is  NXOpen::Die::ClearanceBuilder::ClearanceGeometryTypesSolid .   
         
        """
        pass
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Offset
         Returns the expression containing the offset value to apply to create a clearance area around the solid or closed profile definitions.  
             
         
        """
        pass
    @property
    def Orientation(self) -> DiePlaneBuilder:
        """
        Getter for property: ( DiePlaneBuilder NXOp) Orientation
         Returns the projection plane for the closed profiles to define the clearance areas.  
           Only valid when type is  NXOpen::Die::ClearanceBuilder::ClearanceGeometryTypesSection .   
         
        """
        pass
    @property
    def Section(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Section
         Returns the closed profile sections to use for the basis of the clearance area.  
           Only valid when type is  NXOpen::Die::ClearanceBuilder::ClearanceGeometryTypesSection .   
         
        """
        pass
    @property
    def Target(self) -> NXOpen.SelectBody:
        """
        Getter for property: ( NXOpen.SelectBody) Target
         Returns the target solid the clearance will be subtracted from.  
             
         
        """
        pass
    @property
    def Type(self) -> ClearanceBuilder.Types:
        """
        Getter for property: ( ClearanceBuilder.Types NXOp) Type
         Returns the identification of the clearance type ( NXOpen::Die::ClearanceBuilder::TypesGage ,  NXOpen::Die::ClearanceBuilder::TypesGripper , 
                    or  NXOpen::Die::ClearanceBuilder::TypesLifter ) to create in the target solid.  
             
         
        """
        pass
    @Type.setter
    def Type(self, type: ClearanceBuilder.Types):
        """
        Setter for property: ( ClearanceBuilder.Types NXOp) Type
         Returns the identification of the clearance type ( NXOpen::Die::ClearanceBuilder::TypesGage ,  NXOpen::Die::ClearanceBuilder::TypesGripper , 
                    or  NXOpen::Die::ClearanceBuilder::TypesLifter ) to create in the target solid.  
             
         
        """
        pass
import NXOpen.Features
class Clearance(NXOpen.Features.BodyFeature): 
    """ Represents a die design clearance feature. """
    pass
import NXOpen
import NXOpen.Features
class CompensateRoughDataBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a NXOpen.Die.CompensateRoughDataBuilder. This class is used to edit
    and create a Compensate Rough Curve or Compensate Rough Sheet feature.
    """
    class ApproximationType(Enum):
        """
        Members Include: 
         |Coarse|  Perform a coarse approximation. 
         |Rough|  Perform a rough approximation. 
         |Fine|  Perform a fine approximation. 
         |Exact|  Perform no approximation. 

        """
        Coarse: int
        Rough: int
        Fine: int
        Exact: int
        @staticmethod
        def ValueOf(value: int) -> CompensateRoughDataBuilder.ApproximationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |SheetBody|  Sheet bodies being compensated. 
         |Curve|  Curves being compensated. 

        """
        SheetBody: int
        Curve: int
        @staticmethod
        def ValueOf(value: int) -> CompensateRoughDataBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngleTolerance(self) -> float:
        """
        Getter for property: (float) AngleTolerance
         Returns the angle tolerance.  
             
         
        """
        pass
    @AngleTolerance.setter
    def AngleTolerance(self, angleTolerance: float):
        """
        Setter for property: (float) AngleTolerance
         Returns the angle tolerance.  
             
         
        """
        pass
    @property
    def Approximation(self) -> CompensateRoughDataBuilder.ApproximationType:
        """
        Getter for property: ( CompensateRoughDataBuilder.ApproximationType NXOp) Approximation
         Returns the approximation desired.  
             
         
        """
        pass
    @Approximation.setter
    def Approximation(self, approximation: CompensateRoughDataBuilder.ApproximationType):
        """
        Setter for property: ( CompensateRoughDataBuilder.ApproximationType NXOp) Approximation
         Returns the approximation desired.  
             
         
        """
        pass
    @property
    def CurveCollector(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) CurveCollector
         Returns the curve collector containing the curves that will be approximated.  
             
         
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
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance.  
             
         
        """
        pass
    @property
    def JoinOutputCurves(self) -> bool:
        """
        Getter for property: (bool) JoinOutputCurves
         Returns the join output curves setting, true indicates that the output curves will be joined
                    into a single curve.  
             
         
        """
        pass
    @JoinOutputCurves.setter
    def JoinOutputCurves(self, joinOutputCurves: bool):
        """
        Setter for property: (bool) JoinOutputCurves
         Returns the join output curves setting, true indicates that the output curves will be joined
                    into a single curve.  
             
         
        """
        pass
    @property
    def MaximumGap(self) -> float:
        """
        Getter for property: (float) MaximumGap
         Returns the maximum gap.  
             
         
        """
        pass
    @MaximumGap.setter
    def MaximumGap(self, maximumGap: float):
        """
        Setter for property: (float) MaximumGap
         Returns the maximum gap.  
             
         
        """
        pass
    @property
    def ModifyInputSheet(self) -> bool:
        """
        Getter for property: (bool) ModifyInputSheet
         Returns the modify input sheet setting.  
           If true the input sheet will be modified, otherwise
                    a new sheet will be created.   
         
        """
        pass
    @ModifyInputSheet.setter
    def ModifyInputSheet(self, modifyInputSheet: bool):
        """
        Setter for property: (bool) ModifyInputSheet
         Returns the modify input sheet setting.  
           If true the input sheet will be modified, otherwise
                    a new sheet will be created.   
         
        """
        pass
    @property
    def ProjectToFaces(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) ProjectToFaces
         Returns the faces to project the output curves onto.  
           If faces are selected then the output curves will be 
                    projected normal to these faces.   
         
        """
        pass
    @property
    def SheetBodies(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: ( NXOpen.SelectBodyList) SheetBodies
         Returns the sheet bodies that will be approximated.  
             
         
        """
        pass
    @property
    def Type(self) -> CompensateRoughDataBuilder.Types:
        """
        Getter for property: ( CompensateRoughDataBuilder.Types NXOp) Type
         Returns the type of input data being supplied.  
             
         
        """
        pass
    @Type.setter
    def Type(self, type: CompensateRoughDataBuilder.Types):
        """
        Setter for property: ( CompensateRoughDataBuilder.Types NXOp) Type
         Returns the type of input data being supplied.  
             
         
        """
        pass
import NXOpen
import NXOpen.Features
class ConnectProfileParentBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Die Connecting Profile sub feature. """
    @property
    def BuildStatus(self) -> DieBuildStatusOption:
        """
        Getter for property: ( DieBuildStatusOption NXOp) BuildStatus
         Returns the build status of die connecting profiles   
            
         
        """
        pass
    @property
    def DesignStatus(self) -> bool:
        """
        Getter for property: (bool) DesignStatus
         Returns the design status of  die connecting profiles   
            
         
        """
        pass
    @DesignStatus.setter
    def DesignStatus(self, design_status: bool):
        """
        Setter for property: (bool) DesignStatus
         Returns the design status of  die connecting profiles   
            
         
        """
        pass
    @property
    def DisplayStatus(self) -> bool:
        """
        Getter for property: (bool) DisplayStatus
         Returns the display status of die pierce holes   
            
         
        """
        pass
    @DisplayStatus.setter
    def DisplayStatus(self, display_status: bool):
        """
        Setter for property: (bool) DisplayStatus
         Returns the display status of die pierce holes   
            
         
        """
        pass
    def GetProfile(self) -> Tuple[List[NXOpen.IProfile], DirectionOption]:
        """
         Gets the connecting profiles of the steel insert 
         Returns A tuple consisting of (profile_entries, direction). 
         - profile_entries is:  NXOpen.IProfile Li. profile entries .
         - direction is:  DirectionOption NXOp. profile direction .

        """
        pass
    def SetProfile(self, direction: DirectionOption, profile_entries: List[NXOpen.IProfile]) -> None:
        """
         Sets the connecting profiles of the steel insert 
        """
        pass
import NXOpen
import NXOpen.Features
class DeckParentBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Die Deck Feature sub feature. Used by the Upper Draw Die
 and Draw Die Punch to capture the deck definition. Unless specified, the
 attributes and methods are generic and can be applied to any type of deck. """
    @property
    def BuildStatus(self) -> DieBuildStatusOption:
        """
        Getter for property: ( DieBuildStatusOption NXOp) BuildStatus
         Returns the build status of deck.  
             
         
        """
        pass
    @property
    def DesignStatus(self) -> bool:
        """
        Getter for property: (bool) DesignStatus
         Returns the design status of deck, if true the deck will be built into the model, if false it will not.  
             
         
        """
        pass
    @DesignStatus.setter
    def DesignStatus(self, design_status: bool):
        """
        Setter for property: (bool) DesignStatus
         Returns the design status of deck, if true the deck will be built into the model, if false it will not.  
             
         
        """
        pass
    @property
    def DisplayStatus(self) -> bool:
        """
        Getter for property: (bool) DisplayStatus
         Returns the display status of deck, if true input data to the deck will be displayed, if false the input data will not be displayed.  
             
         
        """
        pass
    @DisplayStatus.setter
    def DisplayStatus(self, display_status: bool):
        """
        Setter for property: (bool) DisplayStatus
         Returns the display status of deck, if true input data to the deck will be displayed, if false the input data will not be displayed.  
             
         
        """
        pass
    @property
    def InnerDeckSheet(self) -> NXOpen.Body:
        """
        Getter for property: ( NXOpen.Body) InnerDeckSheet
         Returns the inner deck sheet of deck.  
             
         
        """
        pass
    @InnerDeckSheet.setter
    def InnerDeckSheet(self, inner_sheet: NXOpen.Body):
        """
        Setter for property: ( NXOpen.Body) InnerDeckSheet
         Returns the inner deck sheet of deck.  
             
         
        """
        pass
    @property
    def IntermediateDeckOrientation(self) -> NXOpen.ISurface:
        """
        Getter for property: ( NXOpen.ISurface) IntermediateDeckOrientation
         Returns the intermediate deck orientation of the deck.  
             
         
        """
        pass
    @IntermediateDeckOrientation.setter
    def IntermediateDeckOrientation(self, intermediate_deck_orientation: NXOpen.ISurface):
        """
        Setter for property: ( NXOpen.ISurface) IntermediateDeckOrientation
         Returns the intermediate deck orientation of the deck.  
             
         
        """
        pass
    def GetBaseFlange(self) -> Tuple[List[NXOpen.IProfile], DirectionOption]:
        """
         Gets the base flange profile of the draw die punch.
            Knowledge Fusion: Binder Edge of Upper Draw Die.
             
         Returns A tuple consisting of (profile_entries, direction). 
         - profile_entries is:  NXOpen.IProfile Li. The profile entries, will be curves, edges, faces, sketches or curve features. .
         - direction is:  DirectionOption NXOp. Profile direction. .

        """
        pass
    def GetBinderEdge(self) -> Tuple[List[NXOpen.IProfile], DirectionOption]:
        """
         Gets the binder edge profile of the upper draw die deck. 
         Returns A tuple consisting of (profile_entries, direction). 
         - profile_entries is:  NXOpen.IProfile Li. The profile entries, will be curves, edges, faces, sketches or curve features. .
         - direction is:  DirectionOption NXOp. Profile direction. .

        """
        pass
    def GetIntermediateDeck(self) -> Tuple[List[NXOpen.IProfile], DirectionOption]:
        """
         Gets the intermediate deck profile of the deck. 
         Returns A tuple consisting of (profile_entries, direction). 
         - profile_entries is:  NXOpen.IProfile Li. The profile entries, will be curves, edges, faces, sketches or curve features. .
         - direction is:  DirectionOption NXOp. Profile direction. .

        """
        pass
    def GetMainDeck(self) -> Tuple[List[NXOpen.IProfile], DirectionOption]:
        """
         Gets the main deck profile of the upper draw die deck. 
         Returns A tuple consisting of (profile_entries, direction). 
         - profile_entries is:  NXOpen.IProfile Li. The profile entries, will be curves, edges, faces, sketches or curve features. .
         - direction is:  DirectionOption NXOp. Profile direction. .

        """
        pass
    def GetMainWallCenterline(self) -> Tuple[List[NXOpen.IProfile], DirectionOption]:
        """
         Gets the main wall centerline profile of the draw die punch.
              Knowledge Fusion: Main Deck of Upper Draw Die.
             
         Returns A tuple consisting of (profile_entries, direction). 
         - profile_entries is:  NXOpen.IProfile Li. The profile entries, will be curves, edges, faces, sketches or curve features. .
         - direction is:  DirectionOption NXOp. Profile direction. .

        """
        pass
    def SetBaseFlange(self, direction: DirectionOption, profile_entries: List[NXOpen.IProfile]) -> None:
        """
         Sets the base flange profile of the draw die punch.
            Knowledge Fusion: Binder Edge of Upper Draw Die.
             
        """
        pass
    def SetBinderEdge(self, direction: DirectionOption, profile_entries: List[NXOpen.IProfile]) -> None:
        """
         Sets the binder edge profile of the upper draw die deck. 
        """
        pass
    def SetIntermediateDeck(self, direction: DirectionOption, profile_entries: List[NXOpen.IProfile]) -> None:
        """
         Sets the intermediate deck profile of the deck. 
        """
        pass
    def SetMainDeck(self, direction: DirectionOption, profile_entries: List[NXOpen.IProfile]) -> None:
        """
         Sets the main deck profile of the upper draw die deck. 
        """
        pass
    def SetMainWallCenterline(self, direction: DirectionOption, profile_entries: List[NXOpen.IProfile]) -> None:
        """
         Sets the main wall centerline profile of the draw die punch.
            Knowledge Fusion: Main Deck of Upper Draw Die.
             
        """
        pass
import NXOpen
class DieAssistantFlangeProfileList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[DieAssistantFlangeProfile]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: DieAssistantFlangeProfile) -> None:
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
    def Erase(self, obj: DieAssistantFlangeProfile) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: DieAssistantFlangeProfile, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: DieAssistantFlangeProfile) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> DieAssistantFlangeProfile:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( DieAssistantFlangeProfile NXOp):  object found at input index .
        """
        pass
    def GetContents(self) -> List[DieAssistantFlangeProfile]:
        """
         Gets the contents of the entire list 
         Returns objects ( DieAssistantFlangeProfile List[NX):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: DieAssistantFlangeProfile) -> None:
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
    def SetContents(self, objects: List[DieAssistantFlangeProfile]) -> None:
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
    def Swap(self, object1: DieAssistantFlangeProfile, object2: DieAssistantFlangeProfile) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
class DieAssistantFlangeProfileType(Enum):
    """
    Members Include: 
     |Wipe|  Wipe flange steel. 
     |FormAndRestrike|  Form and restrike flange steel. 

    """
    Wipe: int
    FormAndRestrike: int
    @staticmethod
    def ValueOf(value: int) -> DieAssistantFlangeProfileType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class DieAssistantFlangeProfile(NXOpen.NXObject): 
    """
    Represents a NXOpen.Die.DieAssistantFlangeProfile
    """
    @property
    def FlangeDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) FlangeDirection
         Returns the flange profile flange direction   
            
         
        """
        pass
    @FlangeDirection.setter
    def FlangeDirection(self, flangeDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) FlangeDirection
         Returns the flange profile flange direction   
            
         
        """
        pass
    @property
    def FlangeEndProfile(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FlangeEndProfile
         Returns the flange end profile   
            
         
        """
        pass
    @property
    def FlangeProfile(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FlangeProfile
         Returns the flange profile   
            
         
        """
        pass
    @property
    def FlangeProfileDirection(self) -> DirectionOption:
        """
        Getter for property: ( DirectionOption NXOp) FlangeProfileDirection
         Returns the flange profile direction   
            
         
        """
        pass
    @FlangeProfileDirection.setter
    def FlangeProfileDirection(self, flangeProfileDirection: DirectionOption):
        """
        Setter for property: ( DirectionOption NXOp) FlangeProfileDirection
         Returns the flange profile direction   
            
         
        """
        pass
    @property
    def FlangeSide(self) -> bool:
        """
        Getter for property: (bool) FlangeSide
         Returns the flange profile reverse flange side indicator   
            
         
        """
        pass
    @FlangeSide.setter
    def FlangeSide(self, flangeSide: bool):
        """
        Setter for property: (bool) FlangeSide
         Returns the flange profile reverse flange side indicator   
            
         
        """
        pass
    @property
    def FlangeType(self) -> DieAssistantFlangeProfileType:
        """
        Getter for property: ( DieAssistantFlangeProfileType NXOp) FlangeType
         Returns the flange type   
            
         
        """
        pass
    @FlangeType.setter
    def FlangeType(self, flangeType: DieAssistantFlangeProfileType):
        """
        Setter for property: ( DieAssistantFlangeProfileType NXOp) FlangeType
         Returns the flange type   
            
         
        """
        pass
    def DefineBases(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
import NXOpen
class DieAssistantTrimProfileList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[DieAssistantTrimProfile]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: DieAssistantTrimProfile) -> None:
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
    def Erase(self, obj: DieAssistantTrimProfile) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: DieAssistantTrimProfile, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: DieAssistantTrimProfile) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> DieAssistantTrimProfile:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( DieAssistantTrimProfile NXOp):  object found at input index .
        """
        pass
    def GetContents(self) -> List[DieAssistantTrimProfile]:
        """
         Gets the contents of the entire list 
         Returns objects ( DieAssistantTrimProfile List[NX):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: DieAssistantTrimProfile) -> None:
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
    def SetContents(self, objects: List[DieAssistantTrimProfile]) -> None:
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
    def Swap(self, object1: DieAssistantTrimProfile, object2: DieAssistantTrimProfile) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class DieAssistantTrimProfile(NXOpen.NXObject): 
    """
    Represents a NXOpen.Die.DieAssistantTrimProfile
    """
    @property
    def TrimDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) TrimDirection
         Returns the trim profile trim direction   
            
         
        """
        pass
    @TrimDirection.setter
    def TrimDirection(self, trimDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) TrimDirection
         Returns the trim profile trim direction   
            
         
        """
        pass
    @property
    def TrimProfile(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) TrimProfile
         Returns the trim profile   
            
         
        """
        pass
    @property
    def TrimProfileDirection(self) -> DirectionOption:
        """
        Getter for property: ( DirectionOption NXOp) TrimProfileDirection
         Returns the trim profile direction   
            
         
        """
        pass
    @TrimProfileDirection.setter
    def TrimProfileDirection(self, trimProfileDirection: DirectionOption):
        """
        Setter for property: ( DirectionOption NXOp) TrimProfileDirection
         Returns the trim profile direction   
            
         
        """
        pass
    @property
    def TrimSide(self) -> bool:
        """
        Getter for property: (bool) TrimSide
         Returns the trim profile reverse trim side indicator   
            
         
        """
        pass
    @TrimSide.setter
    def TrimSide(self, trimSide: bool):
        """
        Setter for property: (bool) TrimSide
         Returns the trim profile reverse trim side indicator   
            
         
        """
        pass
    def DefineBases(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class DieAttributesBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.Die.DieAttributesBuilder. The Die Attributes class is a helper to
    the main Die Design feature to gather the attribute title and value and face color to be applied.
    The attribute will be applied to a face or faces in the application of varying types, such as a
    base face.
    """
    @property
    def AttributeColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) AttributeColor
         Returns the color to be applied to the face, or faces, in the application   
            
         
        """
        pass
    @AttributeColor.setter
    def AttributeColor(self, attributeColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) AttributeColor
         Returns the color to be applied to the face, or faces, in the application   
            
         
        """
        pass
    @property
    def AttributeTitle(self) -> str:
        """
        Getter for property: (str) AttributeTitle
         Returns the title of the attribute to be applied   
            
         
        """
        pass
    @AttributeTitle.setter
    def AttributeTitle(self, attributeTitle: str):
        """
        Setter for property: (str) AttributeTitle
         Returns the title of the attribute to be applied   
            
         
        """
        pass
    @property
    def AttributeValue(self) -> str:
        """
        Getter for property: (str) AttributeValue
         Returns the value given to the attribute   
            
         
        """
        pass
    @AttributeValue.setter
    def AttributeValue(self, attributeValue: str):
        """
        Setter for property: (str) AttributeValue
         Returns the value given to the attribute   
            
         
        """
        pass
import NXOpen
class DieBooleanBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[DieBooleanBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: DieBooleanBuilder) -> None:
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
    def Erase(self, obj: DieBooleanBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: DieBooleanBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: DieBooleanBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> DieBooleanBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( DieBooleanBuilder NXOp):  object found at input index .
        """
        pass
    def GetContents(self) -> List[DieBooleanBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( DieBooleanBuilder List[NX):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: DieBooleanBuilder) -> None:
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
    def SetContents(self, objects: List[DieBooleanBuilder]) -> None:
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
    def Swap(self, object1: DieBooleanBuilder, object2: DieBooleanBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class DieBooleanBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.Die.DieBooleanBuilder. This class is a helper to other
    Die Design features that identify specific booleans in their dialogs, such as the Die Shoe
    feature. 
    """
    class BooleanType(Enum):
        """
        Members Include: 
         |Unite|  Unite the solids to the application solid. 
         |Subtract|  Subtract the solids from the application solid. 
         |Intersect|  Intersect the solids with the application solid. 

        """
        Unite: int
        Subtract: int
        Intersect: int
        @staticmethod
        def ValueOf(value: int) -> DieBooleanBuilder.BooleanType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BooleanOptions(self) -> DieBooleanBuilder.BooleanType:
        """
        Getter for property: ( DieBooleanBuilder.BooleanType NXOp) BooleanOptions
         Returns the boolean option to apply to the list of selected solids   
            
         
        """
        pass
    @BooleanOptions.setter
    def BooleanOptions(self, booleanOptions: DieBooleanBuilder.BooleanType):
        """
        Setter for property: ( DieBooleanBuilder.BooleanType NXOp) BooleanOptions
         Returns the boolean option to apply to the list of selected solids   
            
         
        """
        pass
    @property
    def SelectBodies(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SelectBodies
         Returns the bodies to be booleaned to the main feature body   
            
         
        """
        pass
class DieBuildStatusOption(Enum):
    """
    Members Include: 
     |Indeterminant|  Build status could not be determined since sub feature is not active. 
     |Unknown|  Build status is unknown since sub feature has not been built yet. 
     |Fail|  Sub feature build has failed. 
     |Valid|  Sub feature has built successfully. 

    """
    Indeterminant: int
    Unknown: int
    Fail: int
    Valid: int
    @staticmethod
    def ValueOf(value: int) -> DieBuildStatusOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.Features
class DieCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a Die EngineeringDesign feature builder. """
    def CastRelief(self, cast_relief: CastRelief) -> CastReliefBuilder:
        """
         Creates a cast relief feature builder NXOpen.Die.CastReliefBuilder. 
         Returns builder ( CastReliefBuilder NXOp):  .
        """
        pass
    def ClampingSlot(self, clamping_slot: ClampingSlot) -> ClampingSlotBuilder:
        """
         Creates a clamping slot feature builder NXOpen.Die.ClampingSlotBuilder. 
         Returns builder ( ClampingSlotBuilder NXOp):  .
        """
        pass
    def CompensateRoughData(self, compensate_rough_data: NXOpen.Features.CompensateRoughData) -> CompensateRoughDataBuilder:
        """
         Creates a NXOpen.Die.CompensateRoughDataBuilder. 
         Returns builder ( CompensateRoughDataBuilder NXOp):  .
        """
        pass
    def CreateAddSurfBuilder(self, add_surf: NXOpen.Features.Feature) -> AddSurfBuilder:
        """
         Creates a NXOpen.Die.AddSurfBuilder. 
         Returns builder ( AddSurfBuilder NXOp):  .
        """
        pass
    def CreateAddendumSectionBuilder(self, add_section: NXOpen.Features.Feature) -> AddendumSectionBuilder:
        """
         CreatesEdits the addendum section builder. 
         Returns builder ( AddendumSectionBuilder NXOp):  .
        """
        pass
    def CreateAddendumSectionUserDefinedBuilder(self) -> AddendumSectionUserDefinedBuilder:
        """
         Creates a user defined addendum section builder. 
         Returns builder ( AddendumSectionUserDefinedBuilder NXOp):  User Defined Section builder. .
        """
        pass
    def CreateClearanceBuilder(self, clearance: Clearance) -> ClearanceBuilder:
        """
         Creates a clearance builder NXOpen.Die.ClearanceBuilder. 
         Returns builder ( ClearanceBuilder NXOp):  .
        """
        pass
    def CreateDieAttribute(self) -> DieAttributesBuilder:
        """
         Creates a NXOpen.Die.DieAttributesBuilder. 
         Returns item ( DieAttributesBuilder NXOp):  .
        """
        pass
    def CreateDieBoolean(self) -> DieBooleanBuilder:
        """
         Creates a NXOpen.Die.DieBooleanBuilder. 
         Returns item ( DieBooleanBuilder NXOp):  .
        """
        pass
    def CreateDieDirection(self, feature: NXOpen.Features.Feature) -> DieDirectionBuilder:
        """
         Creates a NXOpen.Die.DieDirectionBuilder. 
         Returns item ( DieDirectionBuilder NXOp):  .
        """
        pass
    def CreateDieLimits(self) -> DieLimitsBuilder:
        """
         Creates a NXOpen.Die.DieLimitsBuilder. 
         Returns item ( DieLimitsBuilder NXOp):  .
        """
        pass
    def CreateDieLocation(self) -> DieLocationBuilder:
        """
         Creates a NXOpen.Die.DieLocationBuilder. 
         Returns item ( DieLocationBuilder NXOp):  .
        """
        pass
    def CreateDieLocations(self, feature: NXOpen.Features.Feature, allowSelection: bool, allowNewPoint: bool, allowNewCoordinateSystem: bool, allowNewVector: bool, allowNewPlane: bool, isRequired: bool, allowMultipleSelection: bool) -> DieLocationsBuilder:
        """
         Creates a NXOpen.Die.DieLocationsBuilder. 
         Returns item ( DieLocationsBuilder NXOp):  .
        """
        pass
    def CreateDiePlane(self, feature: NXOpen.Features.Feature) -> DiePlaneBuilder:
        """
         Creates a NXOpen.Die.DiePlaneBuilder. 
         Returns item ( DiePlaneBuilder NXOp):  .
        """
        pass
    def CreateDrawBeadBuilder(self, draw_bead: DrawBead) -> DrawBeadBuilder:
        """
         Creates a draw bead builder NXOpen.Die.DrawBeadBuilder. 
         Returns builder ( DrawBeadBuilder NXOp):  .
        """
        pass
    def CreateFillAreaBuilder(self, fill_area: FillArea) -> FillAreaBuilder:
        """
         Creates a fill area builder NXOpen.Die.FillAreaBuilder. 
         Returns builder ( FillAreaBuilder NXOp):  .
        """
        pass
    def CreateFingerClearanceNotchBuilder(self, finger_clearance_notch: FingerClearanceNotch) -> FingerClearanceNotchBuilder:
        """
         Creates a finger clearance notch builder NXOpen.Die.FingerClearanceNotchBuilder. 
         Returns builder ( FingerClearanceNotchBuilder NXOp):  .
        """
        pass
    def CreateHandlingCoreBuilder(self, handling_core: HandlingCore) -> HandlingCoreBuilder:
        """
         Creates a handling core builder NXOpen.Die.HandlingCoreBuilder. 
         Returns builder ( HandlingCoreBuilder NXOp):  .
        """
        pass
    def CreateMachineReliefBuilder(self, machine_relief: MachineRelief) -> MachineReliefBuilder:
        """
         Creates a machine relief builder NXOpen.Die.MachineReliefBuilder. 
         Returns builder ( MachineReliefBuilder NXOp):  .
        """
        pass
    def CreateQuickBinderBuilder(self, quick_binder: NXOpen.Features.QuickBinder) -> QuickBinderBuilder:
        """
         Creates a NXOpen.Die.QuickBinderBuilder 
         Returns builder ( QuickBinderBuilder NXOp):  .
        """
        pass
    def CreateQuickBinderWrapBuilder(self, quick_binder_wrap: NXOpen.Features.Feature) -> QuickBinderWrapBuilder:
        """
         Creates a NXOpen.Die.QuickBinderWrapBuilder. 
         Returns builder ( QuickBinderWrapBuilder NXOp):  .
        """
        pass
    def CreateSpringbackCompensationBuilder(self, springback_compensation: SpringbackCompensation) -> SpringbackCompensationBuilder:
        """
         Creates a springback compensation builder NXOpen.Die.SpringbackCompensationBuilder. 
         Returns builder ( SpringbackCompensationBuilder NXOp):  .
        """
        pass
    def CreateTrimLineDevelopmentBuilder(self, trim_line_development: NXOpen.Features.Feature) -> TrimLineDevelopmentBuilder:
        """
         Creates a NXOpen.Die.TrimLineDevelopmentBuilder. 
         Returns builder ( TrimLineDevelopmentBuilder NXOp):  .
        """
        pass
    def CreateTrimSteelParametersBuilder(self) -> TrimSteelParametersBuilder:
        """
         Creates a trim steel parameters builder NXOpen.Die.TrimSteelParametersBuilder. 
         Returns builder ( TrimSteelParametersBuilder NXOp): .
        """
        pass
    def CreateUncutRegionsBuilder(self) -> UncutRegionsBuilder:
        """
         Creates a NXOpen.Die.UncutRegionsBuilder 
         Returns builder ( UncutRegionsBuilder NXOp):  .
        """
        pass
    def DieShoe(self, die_shoe: DieShoe) -> DieShoeBuilder:
        """
         Creates a die_shoe feature builder NXOpen.Die.DieShoeBuilder. 
         Returns builder ( DieShoeBuilder NXOp):  .
        """
        pass
    def DrawDiePunch(self, draw_die_punch: NXOpen.Features.Feature) -> DrawDiePunchBuilder:
        """
         Creates the draw die punch feature builder. 
         Returns builder ( DrawDiePunchBuilder NXOp):  Draw Die Punch feature builder. .
        """
        pass
    def FaceSheet(self, face_sheet: NXOpen.Features.Feature) -> FaceSheetBuilder:
        """
         Creates a NXOpen.Die.FaceSheetBuilder. 
         Returns builder ( FaceSheetBuilder NXOp):  .
        """
        pass
    def Fill(self, fill: NXOpen.Features.Feature) -> FillBuilder:
        """
         CreatesEdits the die area fill feature builder. 
         Returns builder ( FillBuilder NXOp):  area fill feature builder.
        """
        pass
    def FlangeTask(self, flange_task: NXOpen.Features.Feature) -> FlangeTaskBuilder:
        """
         CreatesEdits the flange task feature builder. 
         Returns builder ( FlangeTaskBuilder NXOp):  Flange Task feature builder.
        """
        pass
    def FormTask(self, form_task: NXOpen.Features.Feature) -> FormTaskBuilder:
        """
         CreatesEdits the form task feature builder. 
         Returns builder ( FormTaskBuilder NXOp):  Form Task feature builder. .
        """
        pass
    def Heelpost(self, heelpost: Heelpost) -> HeelpostBuilder:
        """
         Creates a heelpost feature builder NXOpen.Die.HeelpostBuilder. 
         Returns builder ( HeelpostBuilder NXOp):  .
        """
        pass
    def Keyway(self, keyway: Keyway) -> KeywayBuilder:
        """
         Creates a keyway feature builder NXOpen.Die.KeywayBuilder. 
         Returns builder ( KeywayBuilder NXOp):  .
        """
        pass
    def Lineup(self, lineup: NXOpen.Features.Feature) -> LineupBuilder:
        """
         CreatesEdits the die lineup feature builder. 
         Returns builder ( LineupBuilder NXOp):  lineup feature builder.
        """
        pass
    def OutputCurves(self, outcurves: NXOpen.Features.Feature) -> OutputCurvesBuilder:
        """
         CreatesEdits the die output curves feature builder. 
         Returns builder ( OutputCurvesBuilder NXOp):  output curves feature builder.
        """
        pass
    def PierceTask(self, pierce_task: NXOpen.Features.Feature) -> PierceTaskBuilder:
        """
         CreatesEdits the pierce task feature builder. 
         Returns builder ( PierceTaskBuilder NXOp):  Pierce Task feature builder.
        """
        pass
    def Rotor(self, rotor: NXOpen.Features.Feature) -> RotorBuilder:
        """
         Creates the die_rotor feature builder. 
         Returns builder ( RotorBuilder NXOp):  Die Rotor feature builder. .
        """
        pass
    def Steelinsert(self, steel_insert: NXOpen.Features.Feature) -> SteelInsertBuilder:
        """
         CreatesEdits the steel insert feature builder. 
         Returns builder ( SteelInsertBuilder NXOp):  Steel Insert feature builder.
        """
        pass
    def TrimFlangeDieAssistant(self, null_feature: NXOpen.Features.Feature) -> TrimFlangeDieAssistantBuilder:
        """
         Creates the trimflange die assistant builder. 
         Returns builder ( TrimFlangeDieAssistantBuilder NXOp):  TrimFlange Die Assistant builder.
        """
        pass
    def TrimTask(self, trim_task: NXOpen.Features.Feature) -> TrimTaskBuilder:
        """
         CreatesEdits the trim task feature builder. 
         Returns builder ( TrimTaskBuilder NXOp):  Trim Task feature builder.
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class DieDirectionBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.Die.DieDirectionBuilder. The Die 
    Direction is a helper to the main Die Design feature to gather the 
    vector for items such as Trim direction or Flange direction. Note that
    if a coordinate system is specified, then the direction will be -Z of
    that coordinate system.
    """
    class DirectionType(Enum):
        """
        Members Include: 
         |Selection|  Select a coordinate system (-Z) or plane for the direction. 
         |CoordinateSystem|  Define a coordinate system (-Z) for the direction. 
         |Vector|  Define a vector for the direction. 

        """
        Selection: int
        CoordinateSystem: int
        Vector: int
        @staticmethod
        def ValueOf(value: int) -> DieDirectionBuilder.DirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CoordinateSystemMatrix(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: ( NXOpen.Matrix3x3) CoordinateSystemMatrix
         Returns the coordinate system matrix   
            
         
        """
        pass
    @CoordinateSystemMatrix.setter
    def CoordinateSystemMatrix(self, coordinateSystemMatrix: NXOpen.Matrix3x3):
        """
        Setter for property: ( NXOpen.Matrix3x3) CoordinateSystemMatrix
         Returns the coordinate system matrix   
            
         
        """
        pass
    @property
    def CoordinateSystemOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) CoordinateSystemOrigin
         Returns the coordinate system origin   
            
         
        """
        pass
    @CoordinateSystemOrigin.setter
    def CoordinateSystemOrigin(self, coordinateSystemOrigin: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) CoordinateSystemOrigin
         Returns the coordinate system origin   
            
         
        """
        pass
    @property
    def Direction(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) Direction
         Returns the selected direction   
            
         
        """
        pass
    @property
    def InputType(self) -> DieDirectionBuilder.DirectionType:
        """
        Getter for property: ( DieDirectionBuilder.DirectionType NXOp) InputType
         Returns the type of input that defined the direction   
            
         
        """
        pass
    @InputType.setter
    def InputType(self, inputType: DieDirectionBuilder.DirectionType):
        """
        Setter for property: ( DieDirectionBuilder.DirectionType NXOp) InputType
         Returns the type of input that defined the direction   
            
         
        """
        pass
    @property
    def ReverseSourceDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseSourceDirection
         Returns the indication if the source's direction should be reversed.  
           True indicates the source's direction should be reversed  
         
        """
        pass
    @ReverseSourceDirection.setter
    def ReverseSourceDirection(self, reverseSourceDirection: bool):
        """
        Setter for property: (bool) ReverseSourceDirection
         Returns the indication if the source's direction should be reversed.  
           True indicates the source's direction should be reversed  
         
        """
        pass
    @property
    def Vector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) Vector
         Returns the specified vector   
            
         
        """
        pass
    @Vector.setter
    def Vector(self, vector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) Vector
         Returns the specified vector   
            
         
        """
        pass
import NXOpen
class DieLimitsBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[DieLimitsBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: DieLimitsBuilder) -> None:
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
    def Erase(self, obj: DieLimitsBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: DieLimitsBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: DieLimitsBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> DieLimitsBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( DieLimitsBuilder NXOp):  object found at input index .
        """
        pass
    def GetContents(self) -> List[DieLimitsBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( DieLimitsBuilder List[NX):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: DieLimitsBuilder) -> None:
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
    def SetContents(self, objects: List[DieLimitsBuilder]) -> None:
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
    def Swap(self, object1: DieLimitsBuilder, object2: DieLimitsBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class DieLimitsBuilder(NXOpen.TaggedObject): 
    """ Limits a path to a segment of the path. """
    @property
    def Curve(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Curve
         Returns the curve used to set the limits.  
            The string will be combined into a single curve and the endpoints of
                    the combined curve will be used to set the first and last limit points.
                  
         
        """
        pass
    @property
    def Point1(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) Point1
         Returns the first limit point.  
             
         
        """
        pass
    @property
    def Point2(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) Point2
         Returns the last limit point.  
             
         
        """
        pass
    @property
    def RemoveLimitPoints(self) -> bool:
        """
        Getter for property: (bool) RemoveLimitPoints
         Returns the indication that limit points are being removed.  
             
         
        """
        pass
    @RemoveLimitPoints.setter
    def RemoveLimitPoints(self, remove: bool):
        """
        Setter for property: (bool) RemoveLimitPoints
         Returns the indication that limit points are being removed.  
             
         
        """
        pass
    @property
    def Reverse(self) -> int:
        """
        Getter for property: (int) Reverse
         Returns the indication that limit points should be reversed.  
           Setting of 1 indicates to reverse.   
         
        """
        pass
    @Reverse.setter
    def Reverse(self, reverse: int):
        """
        Setter for property: (int) Reverse
         Returns the indication that limit points should be reversed.  
           Setting of 1 indicates to reverse.   
         
        """
        pass
    def GetPath(self) -> NXOpen.Curve:
        """
         Get the path used for the limits. 
         Returns pathCurve ( NXOpen.Curve): .
        """
        pass
    def GetPathObjects(self) -> List[NXOpen.NXObject]:
        """
         Get the objects used to create the path. 
         Returns object_array ( NXOpen.NXObject Li):  The opening objects that were used to create the path. .
        """
        pass
    def SetLimitsFromCurve(self, curve: NXOpen.Curve) -> None:
        """
         Set the limits from the endpoints of the input curve. 
        """
        pass
    def SetPath(self, path: NXOpen.Curve) -> None:
        """
         Set the path used for the limits. 
        """
        pass
    def SetPathObjects(self, object_array: List[NXOpen.NXObject]) -> None:
        """
         Set the objects used to create the path. 
        """
        pass
import NXOpen
class DieLocationBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[DieLocationBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: DieLocationBuilder) -> None:
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
    def Erase(self, obj: DieLocationBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: DieLocationBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: DieLocationBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> DieLocationBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( DieLocationBuilder NXOp):  object found at input index .
        """
        pass
    def GetContents(self) -> List[DieLocationBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( DieLocationBuilder List[NX):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: DieLocationBuilder) -> None:
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
    def SetContents(self, objects: List[DieLocationBuilder]) -> None:
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
    def Swap(self, object1: DieLocationBuilder, object2: DieLocationBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class DieLocationBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.Die.DieLocationBuilder. The Die 
    Location Item is a helper and identifies a single item in the
    NXOpen.Die.DieLocationBuilder. The item allows the user to
    fully specify a single location point for items such as hole center
    or clamping slot location. Note that a non-point is selected,
    such as a plane or coordinate system, the control point of the object
    will be used for the location.
    """
    class LocationType(Enum):
        """
        Members Include: 
         |SelectLocation|  Select the point to be used. 
         |NewPoint|  Define the point to be used. 
         |NewCoordinateSystem|  Define a coordinate system to specify the location. 
         |NewVector|  Define a vector to specify the location. 
         |NewPlane|  Define a plane to specify the location. 

        """
        SelectLocation: int
        NewPoint: int
        NewCoordinateSystem: int
        NewVector: int
        NewPlane: int
        @staticmethod
        def ValueOf(value: int) -> DieLocationBuilder.LocationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CoordinateSystemMatrix(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: ( NXOpen.Matrix3x3) CoordinateSystemMatrix
         Returns the coordinate system matrix   
            
         
        """
        pass
    @CoordinateSystemMatrix.setter
    def CoordinateSystemMatrix(self, coordinateSystemMatrix: NXOpen.Matrix3x3):
        """
        Setter for property: ( NXOpen.Matrix3x3) CoordinateSystemMatrix
         Returns the coordinate system matrix   
            
         
        """
        pass
    @property
    def CoordinateSystemOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) CoordinateSystemOrigin
         Returns the coordinate system origin   
            
         
        """
        pass
    @CoordinateSystemOrigin.setter
    def CoordinateSystemOrigin(self, coordinateSystemOrigin: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) CoordinateSystemOrigin
         Returns the coordinate system origin   
            
         
        """
        pass
    @property
    def InputType(self) -> DieLocationBuilder.LocationType:
        """
        Getter for property: ( DieLocationBuilder.LocationType NXOp) InputType
         Returns the type of source that defined the location   
            
         
        """
        pass
    @InputType.setter
    def InputType(self, inputType: DieLocationBuilder.LocationType):
        """
        Setter for property: ( DieLocationBuilder.LocationType NXOp) InputType
         Returns the type of source that defined the location   
            
         
        """
        pass
    @property
    def Location(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) Location
         Returns the selected location   
            
         
        """
        pass
    @property
    def Plane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) Plane
         Returns the specified plane   
            
         
        """
        pass
    @Plane.setter
    def Plane(self, plane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) Plane
         Returns the specified plane   
            
         
        """
        pass
    @property
    def Point(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Point
         Returns the specified point   
            
         
        """
        pass
    @Point.setter
    def Point(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Point
         Returns the specified point   
            
         
        """
        pass
    @property
    def Vector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) Vector
         Returns the specified vector   
            
         
        """
        pass
    @Vector.setter
    def Vector(self, vector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) Vector
         Returns the specified vector   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class DieLocationsBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.Die.DieLocationsBuilder. The Die 
    Locations is a helper to the main Die Design feature to gather the 
    location points for items such as hole center or clamping slot location.
    Note that a non-point is selected, such as a plane or coordinate system,
    the control point of the object will be used for the location.
    """
    @property
    def List(self) -> DieLocationBuilderList:
        """
        Getter for property: ( DieLocationBuilderList NXOp) List
         Returns the list containing the die location objects  
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class DiePlaneBuilder(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.Die.DiePlaneBuilder. The Die Plane is
    a helper to the main Die Design feature to specify the plane, such as the
    base plane or end planes. If a coordinate system is specified, then the
    XY plane of the coordinate system will be used.
    """
    class PlaneType(Enum):
        """
        Members Include: 
         |Selection|  Select the plane to be used. 
         |Plane|  Define the plane to be used. 
         |CoordinateSystem|  Define a coordinate system to specify the plane. 

        """
        Selection: int
        Plane: int
        CoordinateSystem: int
        @staticmethod
        def ValueOf(value: int) -> DiePlaneBuilder.PlaneType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CoordinateSystemMatrix(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: ( NXOpen.Matrix3x3) CoordinateSystemMatrix
         Returns the coordinate system matrix   
            
         
        """
        pass
    @CoordinateSystemMatrix.setter
    def CoordinateSystemMatrix(self, coordinateSystemMatrix: NXOpen.Matrix3x3):
        """
        Setter for property: ( NXOpen.Matrix3x3) CoordinateSystemMatrix
         Returns the coordinate system matrix   
            
         
        """
        pass
    @property
    def CoordinateSystemOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) CoordinateSystemOrigin
         Returns the coordinate system origin   
            
         
        """
        pass
    @CoordinateSystemOrigin.setter
    def CoordinateSystemOrigin(self, coordinateSystemOrigin: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) CoordinateSystemOrigin
         Returns the coordinate system origin   
            
         
        """
        pass
    @property
    def InputType(self) -> DiePlaneBuilder.PlaneType:
        """
        Getter for property: ( DiePlaneBuilder.PlaneType NXOp) InputType
         Returns the type of input that defined the plane   
            
         
        """
        pass
    @InputType.setter
    def InputType(self, inputType: DiePlaneBuilder.PlaneType):
        """
        Setter for property: ( DiePlaneBuilder.PlaneType NXOp) InputType
         Returns the type of input that defined the plane   
            
         
        """
        pass
    @property
    def ReverseSourceDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseSourceDirection
         Returns the indication if the source's direction should be reversed.  
           True indicates the source's direction should be reversed   
         
        """
        pass
    @ReverseSourceDirection.setter
    def ReverseSourceDirection(self, reverseSourceDirection: bool):
        """
        Setter for property: (bool) ReverseSourceDirection
         Returns the indication if the source's direction should be reversed.  
           True indicates the source's direction should be reversed   
         
        """
        pass
    @property
    def SelectPlane(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) SelectPlane
         Returns the selected plane   
            
         
        """
        pass
    @property
    def SpecifyPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) SpecifyPlane
         Returns the specified plane   
            
         
        """
        pass
    @SpecifyPlane.setter
    def SpecifyPlane(self, specifyPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) SpecifyPlane
         Returns the specified plane   
            
         
        """
        pass
import NXOpen
import NXOpen.Features
class DieShoeBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a Die Shoe feature builder.
    """
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
    def BaseAttributes(self) -> DieAttributesBuilder:
        """
        Getter for property: ( DieAttributesBuilder NXOp) BaseAttributes
         Returns the base attributes   
            
         
        """
        pass
    @property
    def BaseFlangeSection(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) BaseFlangeSection
         Returns the base flange section   
            
         
        """
        pass
    @property
    def BaseOrientation(self) -> DiePlaneBuilder:
        """
        Getter for property: ( DiePlaneBuilder NXOp) BaseOrientation
         Returns the base orientation   
            
         
        """
        pass
    @property
    def CenterlineSlotAttributes(self) -> DieAttributesBuilder:
        """
        Getter for property: ( DieAttributesBuilder NXOp) CenterlineSlotAttributes
         Returns the centerline slot attributes   
            
         
        """
        pass
    @property
    def CenterlineSlotCreate(self) -> bool:
        """
        Getter for property: (bool) CenterlineSlotCreate
         Returns the toggle to create the centerline slot   
            
         
        """
        pass
    @CenterlineSlotCreate.setter
    def CenterlineSlotCreate(self, centerlineSlotCreate: bool):
        """
        Setter for property: (bool) CenterlineSlotCreate
         Returns the toggle to create the centerline slot   
            
         
        """
        pass
    @property
    def CenterlineSlotDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CenterlineSlotDepth
         Returns the centerline slot depth   
            
         
        """
        pass
    @property
    def CenterlineSlotDirection(self) -> DieDirectionBuilder:
        """
        Getter for property: ( DieDirectionBuilder NXOp) CenterlineSlotDirection
         Returns the centerline slot direction   
            
         
        """
        pass
    @property
    def CenterlineSlotWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CenterlineSlotWidth
         Returns the centerline slot width   
            
         
        """
        pass
    @property
    def DeckCutoutsSection(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) DeckCutoutsSection
         Returns the cutout sections in the main deck   
            
         
        """
        pass
    @property
    def DeckThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DeckThickness
         Returns the deck thickness   
            
         
        """
        pass
    @property
    def DieBooleansList(self) -> DieBooleanBuilderList:
        """
        Getter for property: ( DieBooleanBuilderList NXOp) DieBooleansList
         Returns the die boolean solids list   
            
         
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
    def FlangeThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlangeThickness
         Returns the flange thickness   
            
         
        """
        pass
    @property
    def MainDeckAttributes(self) -> DieAttributesBuilder:
        """
        Getter for property: ( DieAttributesBuilder NXOp) MainDeckAttributes
         Returns the main deck attributes   
            
         
        """
        pass
    @property
    def MainDeckOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MainDeckOffset
         Returns the offset for the main deck either measured from the main deck specification or the base plane   
            
         
        """
        pass
    @property
    def MainDeckPlane(self) -> DiePlaneBuilder:
        """
        Getter for property: ( DiePlaneBuilder NXOp) MainDeckPlane
         Returns the main deck plane   
            
         
        """
        pass
    @property
    def MainDeckSection(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) MainDeckSection
         Returns the main deck section   
            
         
        """
        pass
    @property
    def WallThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) WallThickness
         Returns the wall thickness   
            
         
        """
        pass
import NXOpen.Features
class DieShoe(NXOpen.Features.BodyFeature): 
    """ Represents a die shoe feature """
    pass
import NXOpen
class DieSimCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Die Simulation - Press Models """
    def FindActivePressModel(self) -> PressModel:
        """
         Finds the active press model, if any, in the part's assembly structure 
         Returns active_press_model ( PressModel NXOp): .
        """
        pass
class DirectionOption(Enum):
    """
    Members Include: 
     |FromEnd|  Profile direction is aligned with the first curve from the end to start. 
     |FromStart|  Profile direction is aligned with the first curve from the start to end. 

    """
    FromEnd: int
    FromStart: int
    @staticmethod
    def ValueOf(value: int) -> DirectionOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.Features
class DrawBeadBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a builder that is used to create or edit a NXOpen.Die.DrawBead feature.
    """
    class FemaleDepthTypes(Enum):
        """
        Members Include: 
         |Derived|  The female depth is derived from the male bead (Max Male Depth + Constant). 
         |Constant|  The female depth is a user specified constant. 

        """
        Derived: int
        Constant: int
        @staticmethod
        def ValueOf(value: int) -> DrawBeadBuilder.FemaleDepthTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FemaleWidthTypes(Enum):
        """
        Members Include: 
         |Derived|  The female width is derived from the male (Male Width + 2(Sheet Metal Thickness + Clearance)). 
         |Constant|  The female width is a user specified constant. 

        """
        Derived: int
        Constant: int
        @staticmethod
        def ValueOf(value: int) -> DrawBeadBuilder.FemaleWidthTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MaleBeadPositionTypes(Enum):
        """
        Members Include: 
         |Upper|  Attach the male bead to the upper die casting. 
         |Lower|  Attach the male bead to the lower die casting. 

        """
        Upper: int
        Lower: int
        @staticmethod
        def ValueOf(value: int) -> DrawBeadBuilder.MaleBeadPositionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OrientSectionToDrawTypes(Enum):
        """
        Members Include: 
         |DrawDirection|  Orient height parameter to the draw direction. 
         |SheetMetalNormal|  Orient height parameter to the sheet metal normal at the section location. 

        """
        DrawDirection: int
        SheetMetalNormal: int
        @staticmethod
        def ValueOf(value: int) -> DrawBeadBuilder.OrientSectionToDrawTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OrientationTypes(Enum):
        """
        Members Include: 
         |Orthogonal|  The width and angle parameters are orthogonal, or normal, to the sheet metal normal at the section location. 
         |Vertical|  The width and angle parameters are oriented along the draw direction at the section location. 

        """
        Orthogonal: int
        Vertical: int
        @staticmethod
        def ValueOf(value: int) -> DrawBeadBuilder.OrientationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OutputTypes(Enum):
        """
        Members Include: 
         |NotSet|  Creates a small sphere on the centerline. 
         |Male|  Creates the male bead only. 
         |PlusFemale|  Creates the male and female bead. 
         |PlusSheetMetal|  Creates the male, female and sheet metal bead. 

        """
        NotSet: int
        Male: int
        PlusFemale: int
        PlusSheetMetal: int
        @staticmethod
        def ValueOf(value: int) -> DrawBeadBuilder.OutputTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ProjectionDirectionTypes(Enum):
        """
        Members Include: 
         |DrawDirection|  Project the centerline along the draw direction vector. 
         |NormalToPlacementFace|  Project the centerline along the placement face normal. 

        """
        DrawDirection: int
        NormalToPlacementFace: int
        @staticmethod
        def ValueOf(value: int) -> DrawBeadBuilder.ProjectionDirectionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TransitionDefinitionTypes(Enum):
        """
        Members Include: 
         |Automatic|  Shorten the bead segment that has the lowest height. 
         |Manual|  User specified start and end segments so transition areas are fully defined. 

        """
        Automatic: int
        Manual: int
        @staticmethod
        def ValueOf(value: int) -> DrawBeadBuilder.TransitionDefinitionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngleTolerance(self) -> float:
        """
        Getter for property: (float) AngleTolerance
         Returns the angle tolerance.  
             
         
        """
        pass
    @AngleTolerance.setter
    def AngleTolerance(self, angleTolerance: float):
        """
        Setter for property: (float) AngleTolerance
         Returns the angle tolerance.  
             
         
        """
        pass
    @property
    def BaseOrientation(self) -> DrawBeadBuilder.OrientationTypes:
        """
        Getter for property: ( DrawBeadBuilder.OrientationTypes NXOp) BaseOrientation
         Returns the orientation used to construct the sections representing the bead shape.  
             
         
        """
        pass
    @BaseOrientation.setter
    def BaseOrientation(self, baseOrientation: DrawBeadBuilder.OrientationTypes):
        """
        Setter for property: ( DrawBeadBuilder.OrientationTypes NXOp) BaseOrientation
         Returns the orientation used to construct the sections representing the bead shape.  
             
         
        """
        pass
    @property
    def BuildEndTaper(self) -> bool:
        """
        Getter for property: (bool) BuildEndTaper
         Returns the indication if the taper at the end of the bead should be built.  
           True indicates that the taper at the end of the bead should be created.   
         
        """
        pass
    @BuildEndTaper.setter
    def BuildEndTaper(self, buildEndTaper: bool):
        """
        Setter for property: (bool) BuildEndTaper
         Returns the indication if the taper at the end of the bead should be built.  
           True indicates that the taper at the end of the bead should be created.   
         
        """
        pass
    @property
    def BuildStartTaper(self) -> bool:
        """
        Getter for property: (bool) BuildStartTaper
         Returns the indication if the taper at the start of the bead should be built.  
           True indicates that the taper at the start of the bead should be created.   
         
        """
        pass
    @BuildStartTaper.setter
    def BuildStartTaper(self, buildStartTaper: bool):
        """
        Setter for property: (bool) BuildStartTaper
         Returns the indication if the taper at the start of the bead should be built.  
           True indicates that the taper at the start of the bead should be created.   
         
        """
        pass
    @property
    def Centerline(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Centerline
         Returns the section containing the centerline of the bead.  
             
         
        """
        pass
    @property
    def CenterlineProjection(self) -> DrawBeadBuilder.ProjectionDirectionTypes:
        """
        Getter for property: ( DrawBeadBuilder.ProjectionDirectionTypes NXOp) CenterlineProjection
         Returns the projection method to apply to the centerline to place it on the sewn faces.  
             
         
        """
        pass
    @CenterlineProjection.setter
    def CenterlineProjection(self, centerlineProjection: DrawBeadBuilder.ProjectionDirectionTypes):
        """
        Setter for property: ( DrawBeadBuilder.ProjectionDirectionTypes NXOp) CenterlineProjection
         Returns the projection method to apply to the centerline to place it on the sewn faces.  
             
         
        """
        pass
    @property
    def Clearance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Clearance
         Returns the expression containing the clearance value between the male and female bead sheets.  
             
         
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
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance.  
             
         
        """
        pass
    @property
    def DrawDirection(self) -> DieDirectionBuilder:
        """
        Getter for property: ( DieDirectionBuilder NXOp) DrawDirection
         Returns the draw direction.  
             
         
        """
        pass
    @property
    def EndPoint(self) -> DieLocationBuilder:
        """
        Getter for property: ( DieLocationBuilder NXOp) EndPoint
         Returns the point location defining the end of the centerline.  
             
         
        """
        pass
    @property
    def EndTaper(self) -> DrawBeadTaperBuilder:
        """
        Getter for property: ( DrawBeadTaperBuilder NXOp) EndTaper
         Returns the taper definition at the end of the bead.  
             
         
        """
        pass
    @property
    def FemaleDepthType(self) -> DrawBeadBuilder.FemaleDepthTypes:
        """
        Getter for property: ( DrawBeadBuilder.FemaleDepthTypes NXOp) FemaleDepthType
         Returns the method used to calculate the female depth.  
           Only valid when taper bead is false.   
         
        """
        pass
    @FemaleDepthType.setter
    def FemaleDepthType(self, femaleDepthType: DrawBeadBuilder.FemaleDepthTypes):
        """
        Setter for property: ( DrawBeadBuilder.FemaleDepthTypes NXOp) FemaleDepthType
         Returns the method used to calculate the female depth.  
           Only valid when taper bead is false.   
         
        """
        pass
    @property
    def FemaleDepthValue(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FemaleDepthValue
         Returns the expression containing the female depth value.  
           Only valid when taper bead is false and type is  NXOpen::Die::DrawBeadBuilder::FemaleDepthTypesConstant .   
         
        """
        pass
    @property
    def FemaleFaceAttribute(self) -> DieAttributesBuilder:
        """
        Getter for property: ( DieAttributesBuilder NXOp) FemaleFaceAttribute
         Returns the attribute definition to be applied to the faces of the female bead sheet body.  
             
         
        """
        pass
    @property
    def FemaleSheetAttribute(self) -> DieAttributesBuilder:
        """
        Getter for property: ( DieAttributesBuilder NXOp) FemaleSheetAttribute
         Returns the attribute definition to be applied to the female bead sheet body.  
             
         
        """
        pass
    @property
    def FemaleWidthType(self) -> DrawBeadBuilder.FemaleWidthTypes:
        """
        Getter for property: ( DrawBeadBuilder.FemaleWidthTypes NXOp) FemaleWidthType
         Returns the method used to calculate the female width.  
           Changing this will affect all segments. Only valid when taper bead is false.   
         
        """
        pass
    @FemaleWidthType.setter
    def FemaleWidthType(self, femaleWidthType: DrawBeadBuilder.FemaleWidthTypes):
        """
        Setter for property: ( DrawBeadBuilder.FemaleWidthTypes NXOp) FemaleWidthType
         Returns the method used to calculate the female width.  
           Changing this will affect all segments. Only valid when taper bead is false.   
         
        """
        pass
    @property
    def FemaleWidthValue(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FemaleWidthValue
         Returns the expression containing the female width value.  
           Only valid when taper bead is false and type is  NXOpen::Die::DrawBeadBuilder::FemaleWidthTypesConstant .  
         
        """
        pass
    @property
    def GenerateHeightCurve(self) -> bool:
        """
        Getter for property: (bool) GenerateHeightCurve
         Returns the indication if the height curve should be generated.  
           True if the height curve should be generated and kept.   
         
        """
        pass
    @GenerateHeightCurve.setter
    def GenerateHeightCurve(self, generateHeightCurve: bool):
        """
        Setter for property: (bool) GenerateHeightCurve
         Returns the indication if the height curve should be generated.  
           True if the height curve should be generated and kept.   
         
        """
        pass
    @property
    def MachineOffset(self) -> bool:
        """
        Getter for property: (bool) MachineOffset
         Returns the indication if the male and female output bodies are to be built with machining.  
           Only valid when taper bead is true.   
         
        """
        pass
    @MachineOffset.setter
    def MachineOffset(self, machineOffset: bool):
        """
        Setter for property: (bool) MachineOffset
         Returns the indication if the male and female output bodies are to be built with machining.  
           Only valid when taper bead is true.   
         
        """
        pass
    @property
    def MachiningOffsetTitleAttribute(self) -> DieAttributesBuilder:
        """
        Getter for property: ( DieAttributesBuilder NXOp) MachiningOffsetTitleAttribute
         Returns the title of the real attribute to be applied to the male and female bodies.  
           The value of the attribute specifies the machining offset value to be applied. The value is derived during feature construction.   
         
        """
        pass
    @property
    def MaleBeadPosition(self) -> DrawBeadBuilder.MaleBeadPositionTypes:
        """
        Getter for property: ( DrawBeadBuilder.MaleBeadPositionTypes NXOp) MaleBeadPosition
         Returns the casting in which to create the male bead.  
             
         
        """
        pass
    @MaleBeadPosition.setter
    def MaleBeadPosition(self, maleBeadPosition: DrawBeadBuilder.MaleBeadPositionTypes):
        """
        Setter for property: ( DrawBeadBuilder.MaleBeadPositionTypes NXOp) MaleBeadPosition
         Returns the casting in which to create the male bead.  
             
         
        """
        pass
    @property
    def MaleFaceAttribute(self) -> DieAttributesBuilder:
        """
        Getter for property: ( DieAttributesBuilder NXOp) MaleFaceAttribute
         Returns the attribute definition to be applied to the faces of the male bead sheet body.  
             
         
        """
        pass
    @property
    def MaleSheetAttribute(self) -> DieAttributesBuilder:
        """
        Getter for property: ( DieAttributesBuilder NXOp) MaleSheetAttribute
         Returns the attribute definition to be applied to the male bead sheet body.  
             
         
        """
        pass
    @property
    def MetalThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MetalThickness
         Returns the expression containing the sheet metal thickness value.  
             
         
        """
        pass
    @property
    def OrientSectionToDraw(self) -> DrawBeadBuilder.OrientSectionToDrawTypes:
        """
        Getter for property: ( DrawBeadBuilder.OrientSectionToDrawTypes NXOp) OrientSectionToDraw
         Returns the method used to orient the section dimensions.  
             
         
        """
        pass
    @OrientSectionToDraw.setter
    def OrientSectionToDraw(self, orientSectionToDraw: DrawBeadBuilder.OrientSectionToDrawTypes):
        """
        Setter for property: ( DrawBeadBuilder.OrientSectionToDrawTypes NXOp) OrientSectionToDraw
         Returns the method used to orient the section dimensions.  
             
         
        """
        pass
    @property
    def Output(self) -> DrawBeadBuilder.OutputTypes:
        """
        Getter for property: ( DrawBeadBuilder.OutputTypes NXOp) Output
         Returns the output to be constructed by the draw bead feature.  
             
         
        """
        pass
    @Output.setter
    def Output(self, output: DrawBeadBuilder.OutputTypes):
        """
        Setter for property: ( DrawBeadBuilder.OutputTypes NXOp) Output
         Returns the output to be constructed by the draw bead feature.  
             
         
        """
        pass
    @property
    def PlacementFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) PlacementFace
         Returns the collector containing faces (which will sew together) that identifies the surface shape the bead is attached too.  
             
         
        """
        pass
    @property
    def ReferenceDirection(self) -> bool:
        """
        Getter for property: (bool) ReferenceDirection
         Returns the indication if the "Left" direction for section orientation should be reversed from the default direction.  
           
                    The default direction is determined by the cross of the centerline tangency and the draw direction. True indicates that the default calculation should be reversed.   
         
        """
        pass
    @ReferenceDirection.setter
    def ReferenceDirection(self, referenceDirection: bool):
        """
        Setter for property: (bool) ReferenceDirection
         Returns the indication if the "Left" direction for section orientation should be reversed from the default direction.  
           
                    The default direction is determined by the cross of the centerline tangency and the draw direction. True indicates that the default calculation should be reversed.   
         
        """
        pass
    @property
    def ReverseMetalThickness(self) -> bool:
        """
        Getter for property: (bool) ReverseMetalThickness
         Returns the indication if the thickness of the sheet metal should be the same as the sewn face normals.  
           True indicates that the sheet will be thickened in the same direction as the sewn face normals.   
         
        """
        pass
    @ReverseMetalThickness.setter
    def ReverseMetalThickness(self, reverseMetalThickness: bool):
        """
        Setter for property: (bool) ReverseMetalThickness
         Returns the indication if the thickness of the sheet metal should be the same as the sewn face normals.  
           True indicates that the sheet will be thickened in the same direction as the sewn face normals.   
         
        """
        pass
    @property
    def SegmentList(self) -> DrawBeadSegmentBuilderList:
        """
        Getter for property: ( DrawBeadSegmentBuilderList NXOp) SegmentList
         Returns the list of  NXOpen::Die::DrawBeadSegmentBuilder  defining the bead sections along the centerline.  
             
         
        """
        pass
    @property
    def SheetMetalFaceAttribute(self) -> DieAttributesBuilder:
        """
        Getter for property: ( DieAttributesBuilder NXOp) SheetMetalFaceAttribute
         Returns the attribute definition to be applied to the faces of the sheet metal sheet body.  
             
         
        """
        pass
    @property
    def SheetMetalSheetAttribute(self) -> DieAttributesBuilder:
        """
        Getter for property: ( DieAttributesBuilder NXOp) SheetMetalSheetAttribute
         Returns the attribute definition to be applied to the sheet metal sheet body.  
             
         
        """
        pass
    @property
    def StartPoint(self) -> DieLocationBuilder:
        """
        Getter for property: ( DieLocationBuilder NXOp) StartPoint
         Returns the point location defining the start of the centerline.  
             
         
        """
        pass
    @property
    def StartTaper(self) -> DrawBeadTaperBuilder:
        """
        Getter for property: ( DrawBeadTaperBuilder NXOp) StartTaper
         Returns the taper definition at the start of the bead.  
             
         
        """
        pass
    @property
    def TaperBead(self) -> bool:
        """
        Getter for property: (bool) TaperBead
         Returns the indication if the bead should allow taper to be added to the side walls.  
           Changing this will affect all segments and may affect the transition definition and output.   
         
        """
        pass
    @TaperBead.setter
    def TaperBead(self, taperBead: bool):
        """
        Setter for property: (bool) TaperBead
         Returns the indication if the bead should allow taper to be added to the side walls.  
           Changing this will affect all segments and may affect the transition definition and output.   
         
        """
        pass
    @property
    def TransitionDefinition(self) -> DrawBeadBuilder.TransitionDefinitionTypes:
        """
        Getter for property: ( DrawBeadBuilder.TransitionDefinitionTypes NXOp) TransitionDefinition
         Returns the method used to build the transition between segments.  
           Changing this will affect all segments.   
         
        """
        pass
    @TransitionDefinition.setter
    def TransitionDefinition(self, transitionDefinition: DrawBeadBuilder.TransitionDefinitionTypes):
        """
        Setter for property: ( DrawBeadBuilder.TransitionDefinitionTypes NXOp) TransitionDefinition
         Returns the method used to build the transition between segments.  
           Changing this will affect all segments.   
         
        """
        pass
    def CreateDrawBeadSegment(self) -> DrawBeadSegmentBuilder:
        """
         Creates a NXOpen.Die.DrawBeadSegmentBuilder builder. 
         Returns item ( DrawBeadSegmentBuilder NXOp):  .
        """
        pass
    def CreateSegmentsFromCenterlineCurves(self) -> None:
        """
         For each curve of the centerline, create a bead segment. 
        """
        pass
    def GetMoreDetails(self) -> List[str]:
        """
         Get the detailed description strings of the draw bead. 
         Returns strings (List[str]):  Array of detail strings. .
        """
        pass
    def SetDefaultDrawDirection(self) -> None:
        """
         Set the default draw direction to the -Z direction of the work coordinate system. 
        """
        pass
    def SetMoreDetails(self, strings: List[str]) -> None:
        """
         Set the detailed description strings of the draw bead. 
        """
        pass
import NXOpen
class DrawBeadSegmentBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[DrawBeadSegmentBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: DrawBeadSegmentBuilder) -> None:
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
    def Erase(self, obj: DrawBeadSegmentBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: DrawBeadSegmentBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: DrawBeadSegmentBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> DrawBeadSegmentBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( DrawBeadSegmentBuilder NXOp):  object found at input index .
        """
        pass
    def GetContents(self) -> List[DrawBeadSegmentBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( DrawBeadSegmentBuilder List[NX):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: DrawBeadSegmentBuilder) -> None:
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
    def SetContents(self, objects: List[DrawBeadSegmentBuilder]) -> None:
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
    def Swap(self, object1: DrawBeadSegmentBuilder, object2: DrawBeadSegmentBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class DrawBeadSegmentBuilder(NXOpen.TaggedObject): 
    """ Segment builder for Die Engineering draw bead. The segment is
    defined along the centerline by either a single point (and then the
    next segment) or 2 end points along the segment. """
    class MaleBeadWidthTypes(Enum):
        """
        Members Include: 
         |Constant|  The male bead width is specified by a constant value. 
         |Derived|  The male bead width is derived from the width specified for the female. 

        """
        Constant: int
        Derived: int
        @staticmethod
        def ValueOf(value: int) -> DrawBeadSegmentBuilder.MaleBeadWidthTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EndLocation(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) EndLocation
         Returns the end location along the centerline for this segment.  
             
         
        """
        pass
    @property
    def FemaleLeftRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FemaleLeftRadius
         Returns the expression containing the female left radius value.  
             
         
        """
        pass
    @property
    def FemaleRightRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FemaleRightRadius
         Returns the expression containing the female right radius value.  
             
         
        """
        pass
    @property
    def Flow(self) -> bool:
        """
        Getter for property: (bool) Flow
         Returns the value identifying if the segment is of flow type (the top radius is half the width).  
           Only allowed if the bead is symmetric.   
         
        """
        pass
    @Flow.setter
    def Flow(self, flow: bool):
        """
        Setter for property: (bool) Flow
         Returns the value identifying if the segment is of flow type (the top radius is half the width).  
           Only allowed if the bead is symmetric.   
         
        """
        pass
    @property
    def MaleBeadHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaleBeadHeight
         Returns the expression containing the male bead height value.  
           The height is measured from the centerline to the top of the bead.   
         
        """
        pass
    @property
    def MaleBeadWidthType(self) -> DrawBeadSegmentBuilder.MaleBeadWidthTypes:
        """
        Getter for property: ( DrawBeadSegmentBuilder.MaleBeadWidthTypes NXOp) MaleBeadWidthType
         Returns the male bead width type.  
             
         
        """
        pass
    @MaleBeadWidthType.setter
    def MaleBeadWidthType(self, maleBeadWidthType: DrawBeadSegmentBuilder.MaleBeadWidthTypes):
        """
        Setter for property: ( DrawBeadSegmentBuilder.MaleBeadWidthTypes NXOp) MaleBeadWidthType
         Returns the male bead width type.  
             
         
        """
        pass
    @property
    def MaleLeftSheetRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaleLeftSheetRadius
         Returns the expression containing the male sheet radius value for the "Left" side.  
             
         
        """
        pass
    @property
    def MaleLeftTopRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaleLeftTopRadius
         Returns the expression containing the male top radius value for the "Left" side.  
             
         
        """
        pass
    @property
    def MaleLeftWallAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaleLeftWallAngle
         Returns the expression containing the male wall angle value for the "Left" side.  
             
         
        """
        pass
    @property
    def MaleLeftWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaleLeftWidth
         Returns the expression containing the male width value for the "left" side.  
             
         
        """
        pass
    @property
    def MaleRightSheetRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaleRightSheetRadius
         Returns the expression containing the male sheet radius value for the "Right" side.  
             
         
        """
        pass
    @property
    def MaleRightTopRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaleRightTopRadius
         Returns the expression containing the male top radius value for the "Right" side.  
             
         
        """
        pass
    @property
    def MaleRightWallAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaleRightWallAngle
         Returns the expression containing the male wall angle value for the "Right" side.  
             
         
        """
        pass
    @property
    def MaleRightWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaleRightWidth
         Returns the expression containing the male width value for the "Right" side.  
             
         
        """
        pass
    @property
    def MaleTransitionLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaleTransitionLength
         Returns the expression containing the male transition length value.  
           The transition length is between bead segments.   
         
        """
        pass
    @property
    def StartLocation(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) StartLocation
         Returns the start location along the centerline for this segment.  
             
         
        """
        pass
    @property
    def Symmetry(self) -> bool:
        """
        Getter for property: (bool) Symmetry
         Returns the value identifying that the male width is symmetrical about the location and reference direction.  
           True indictaes that it is symmetrical.   
         
        """
        pass
    @Symmetry.setter
    def Symmetry(self, symmetry: bool):
        """
        Setter for property: (bool) Symmetry
         Returns the value identifying that the male width is symmetrical about the location and reference direction.  
           True indictaes that it is symmetrical.   
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class DrawBeadTaperBuilder(NXOpen.TaggedObject): 
    """ Taper definition for the end of the Die Engineering Draw Bead. The taper
    can be defined at the start, end, or both ends of the draw bead and smoothly
    transition the bead back into the sheet body. """
    class TaperTypes(Enum):
        """
        Members Include: 
         |Spherical|  Create a spherical end based on a radius. 
         |Washout|  Create a slope based on the height and length desired. 
         |Point|  Use the spherical method, but the radius is defined by a point location and distance to the end of the centerline. 

        """
        Spherical: int
        Washout: int
        Point: int
        @staticmethod
        def ValueOf(value: int) -> DrawBeadTaperBuilder.TaperTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def TaperPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) TaperPoint
         Returns the point used for defining the radius value of the spherical taper.  
             
         
        """
        pass
    @TaperPoint.setter
    def TaperPoint(self, taperPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) TaperPoint
         Returns the point used for defining the radius value of the spherical taper.  
             
         
        """
        pass
    @property
    def TaperRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TaperRadius
         Returns the expression containing the radius value for a spherical taper.  
             
         
        """
        pass
    @property
    def TaperType(self) -> DrawBeadTaperBuilder.TaperTypes:
        """
        Getter for property: ( DrawBeadTaperBuilder.TaperTypes NXOp) TaperType
         Returns the method to apply for defining the taper.  
             
         
        """
        pass
    @TaperType.setter
    def TaperType(self, taperType: DrawBeadTaperBuilder.TaperTypes):
        """
        Setter for property: ( DrawBeadTaperBuilder.TaperTypes NXOp) TaperType
         Returns the method to apply for defining the taper.  
             
         
        """
        pass
    @property
    def TaperWashoutHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TaperWashoutHeight
         Returns the expression containing the height value for a washout taper.  
             
         
        """
        pass
    @property
    def TaperWashoutLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TaperWashoutLength
         Returns the expression containing the length value for a washout taper.  
             
         
        """
        pass
import NXOpen.Features
class DrawBead(NXOpen.Features.BodyFeature): 
    """ Represents a draw bead feature. """
    pass
import NXOpen
import NXOpen.Features
class DrawDiePunchBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Draw Die Punch feature builder. """
    @property
    def AlignStartOrientation(self) -> bool:
        """
        Getter for property: (bool) AlignStartOrientation
         Returns the align start orientation switch of the draw die punch casting, if true use the alignment point to define the start of the punch profile,
                if false use the default algorithm to define the start of the punch profile.  
             
         
        """
        pass
    @AlignStartOrientation.setter
    def AlignStartOrientation(self, align_start_orientation: bool):
        """
        Setter for property: (bool) AlignStartOrientation
         Returns the align start orientation switch of the draw die punch casting, if true use the alignment point to define the start of the punch profile,
                if false use the default algorithm to define the start of the punch profile.  
             
         
        """
        pass
    @property
    def AngleTolerance(self) -> float:
        """
        Getter for property: (float) AngleTolerance
         Returns the angle tolerance of the draw die punch casting.  
             
         
        """
        pass
    @AngleTolerance.setter
    def AngleTolerance(self, angle_tolerance: float):
        """
        Setter for property: (float) AngleTolerance
         Returns the angle tolerance of the draw die punch casting.  
             
         
        """
        pass
    @property
    def BaseOrientation(self) -> NXOpen.ISurface:
        """
        Getter for property: ( NXOpen.ISurface) BaseOrientation
         Returns the base orientation of the draw die punch casting.  
             
         
        """
        pass
    @BaseOrientation.setter
    def BaseOrientation(self, base_orientation: NXOpen.ISurface):
        """
        Setter for property: ( NXOpen.ISurface) BaseOrientation
         Returns the base orientation of the draw die punch casting.  
             
         
        """
        pass
    @property
    def BoltHoleParent(self) -> HoleParentBuilder:
        """
        Getter for property: ( HoleParentBuilder NXOp) BoltHoleParent
         Returns the bolt hole parent builder of the draw die punch.  
             
         
        """
        pass
    @property
    def CastReliefParent(self) -> CastReliefParentBuilder:
        """
        Getter for property: ( CastReliefParentBuilder NXOp) CastReliefParent
         Returns the cast relief builder of the draw die punch.  
             
         
        """
        pass
    @property
    def ClosedStartOrientation(self) -> NXOpen.IOrientation:
        """
        Getter for property: ( NXOpen.IOrientation) ClosedStartOrientation
         Returns the closed start orientation of the draw die punch casting.  
             
         
        """
        pass
    @ClosedStartOrientation.setter
    def ClosedStartOrientation(self, closed_start_orientation: NXOpen.IOrientation):
        """
        Setter for property: ( NXOpen.IOrientation) ClosedStartOrientation
         Returns the closed start orientation of the draw die punch casting.  
             
         
        """
        pass
    @property
    def CoordinatingHoleParent(self) -> HoleParentBuilder:
        """
        Getter for property: ( HoleParentBuilder NXOp) CoordinatingHoleParent
         Returns the coordinating hole parent builder of the draw die punch.  
             
         
        """
        pass
    @property
    def CorePunch(self) -> bool:
        """
        Getter for property: (bool) CorePunch
         Returns the core punch switch of the draw die punch casting, if true the punch will be cored, if false the punch will not be cored.  
             
         
        """
        pass
    @CorePunch.setter
    def CorePunch(self, core_punch: bool):
        """
        Setter for property: (bool) CorePunch
         Returns the core punch switch of the draw die punch casting, if true the punch will be cored, if false the punch will not be cored.  
             
         
        """
        pass
    @property
    def DeckParent(self) -> DeckParentBuilder:
        """
        Getter for property: ( DeckParentBuilder NXOp) DeckParent
         Returns the deck builder of the draw die punch.  
             
         
        """
        pass
    @property
    def DieCenterlineCsys(self) -> NXOpen.CartesianCoordinateSystem:
        """
        Getter for property: ( NXOpen.CartesianCoordinateSystem) DieCenterlineCsys
         Returns the die centerline csys of the draw die punch casting.  
             
         
        """
        pass
    @DieCenterlineCsys.setter
    def DieCenterlineCsys(self, die_centerline_csys: NXOpen.CartesianCoordinateSystem):
        """
        Setter for property: ( NXOpen.CartesianCoordinateSystem) DieCenterlineCsys
         Returns the die centerline csys of the draw die punch casting.  
             
         
        """
        pass
    @property
    def DisplayHoles(self) -> bool:
        """
        Getter for property: (bool) DisplayHoles
         Returns the display holes switch of the draw die punch casting, if true holes will be created in the punch, if false holes will not be created.  
             
         
        """
        pass
    @DisplayHoles.setter
    def DisplayHoles(self, display_holes: bool):
        """
        Setter for property: (bool) DisplayHoles
         Returns the display holes switch of the draw die punch casting, if true holes will be created in the punch, if false holes will not be created.  
             
         
        """
        pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance of the draw die punch casting.  
             
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distance_tolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance of the draw die punch casting.  
             
         
        """
        pass
    @property
    def DowelHoleParent(self) -> HoleParentBuilder:
        """
        Getter for property: ( HoleParentBuilder NXOp) DowelHoleParent
         Returns the dowel hole parent builder of the draw die punch.  
             
         
        """
        pass
    @property
    def HandlingCoreParent(self) -> HandlingCoreParentBuilder:
        """
        Getter for property: ( HandlingCoreParentBuilder NXOp) HandlingCoreParent
         Returns the handling core parent builder of the draw die punch.  
             
         
        """
        pass
    @property
    def KeywayParent(self) -> KeywayParentBuilder:
        """
        Getter for property: ( KeywayParentBuilder NXOp) KeywayParent
         Returns the keyway parent builder of the draw die punch.  
             
         
        """
        pass
    @property
    def PartialRibbingParent(self) -> RibParentBuilder:
        """
        Getter for property: ( RibParentBuilder NXOp) PartialRibbingParent
         Returns the partial ribbing parent builder of the draw die punch.  
             
         
        """
        pass
    @property
    def PreliminaryBuild(self) -> bool:
        """
        Getter for property: (bool) PreliminaryBuild
         Returns the preliminary build switch of the draw die punch casting, if true the fast build options will be used,
                if false accurate build options will be used.  
             
         
        """
        pass
    @PreliminaryBuild.setter
    def PreliminaryBuild(self, preliminary_build: bool):
        """
        Setter for property: (bool) PreliminaryBuild
         Returns the preliminary build switch of the draw die punch casting, if true the fast build options will be used,
                if false accurate build options will be used.  
             
         
        """
        pass
    @property
    def PressureSystemParent(self) -> PressureSystemParentBuilder:
        """
        Getter for property: ( PressureSystemParentBuilder NXOp) PressureSystemParent
         Returns the pressure system parent builder of the draw die punch.  
             
         
        """
        pass
    @property
    def PressureSystemReversalParent(self) -> PointParentBuilder:
        """
        Getter for property: ( PointParentBuilder NXOp) PressureSystemReversalParent
         Returns the pressure system reversal parent builder of the draw die punch.  
             
         
        """
        pass
    @property
    def RibbingParent(self) -> RibParentBuilder:
        """
        Getter for property: ( RibParentBuilder NXOp) RibbingParent
         Returns the ribbing parent builder of the draw die punch.  
             
         
        """
        pass
    @property
    def Section(self) -> DrawDiePunchSectionBuilder:
        """
        Getter for property: ( DrawDiePunchSectionBuilder NXOp) Section
         Returns the section builder of the draw die punch.  
             
         
        """
        pass
    @property
    def SheetMetal(self) -> NXOpen.Body:
        """
        Getter for property: ( NXOpen.Body) SheetMetal
         Returns the sheet metal of the draw die punch casting.  
             
         
        """
        pass
    @SheetMetal.setter
    def SheetMetal(self, sheet_metal: NXOpen.Body):
        """
        Setter for property: ( NXOpen.Body) SheetMetal
         Returns the sheet metal of the draw die punch casting.  
             
         
        """
        pass
    @property
    def StrengtheningRibbingParent(self) -> RibParentBuilder:
        """
        Getter for property: ( RibParentBuilder NXOp) StrengtheningRibbingParent
         Returns the strengthening ribbing parent builder of the draw die punch.  
             
         
        """
        pass
    @property
    def VentHoleParent(self) -> HoleParentBuilder:
        """
        Getter for property: ( HoleParentBuilder NXOp) VentHoleParent
         Returns the vent hole parent builder of the draw die punch.  
             
         
        """
        pass
    @property
    def WearPlateParent(self) -> PadParentBuilder:
        """
        Getter for property: ( PadParentBuilder NXOp) WearPlateParent
         Returns the wear plate parent builder of the draw die punch.  
             
         
        """
        pass
    def GetPunchProfile(self) -> Tuple[DirectionOption, List[NXOpen.IProfile]]:
        """
         Gets the punch profile of the draw die punch casting. 
         Returns A tuple consisting of (direction, profile_entries). 
         - direction is:  DirectionOption NXOp. Profile direction. .
         - profile_entries is:  NXOpen.IProfile Li. The profile entries, will be curves, edges, faces, sketches or curve features. .

        """
        pass
    def SetPunchProfile(self, direction: DirectionOption, profile_entries: List[NXOpen.IProfile]) -> None:
        """
         Sets the punch profile of the draw die punch casting. 
        """
        pass
import NXOpen
import NXOpen.Features
class DrawDiePunchSectionBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Draw Die Punch Section sub feature. """
    @property
    def BaseThickness(self) -> float:
        """
        Getter for property: (float) BaseThickness
         Returns the base thickness of the draw die punch casting.  
             
         
        """
        pass
    @property
    def BaseWidth(self) -> float:
        """
        Getter for property: (float) BaseWidth
         Returns the base width of the draw die punch casting.  
             
         
        """
        pass
    @property
    def BeltThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BeltThickness
         Returns the belt thickness of the draw die punch casting.  
             
         
        """
        pass
    @property
    def BuildStatus(self) -> DieBuildStatusOption:
        """
        Getter for property: ( DieBuildStatusOption NXOp) BuildStatus
         Returns the build status of the draw die punch casting.  
             
         
        """
        pass
    @property
    def DeckThickness(self) -> float:
        """
        Getter for property: (float) DeckThickness
         Returns the deck thickness of the draw die punch casting.  
             
         
        """
        pass
    @property
    def DesignStatus(self) -> bool:
        """
        Getter for property: (bool) DesignStatus
         Returns the design status of the draw die punch casting, if true the casting will be built into the model, if false it will not.  
             
         
        """
        pass
    @property
    def DisplayStatus(self) -> bool:
        """
        Getter for property: (bool) DisplayStatus
         Returns the display status of the draw die punch casting, if true input data to the draw die punch casting will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    @property
    def OffsetProfileToTop(self) -> float:
        """
        Getter for property: (float) OffsetProfileToTop
         Returns the offset profile to top distance of the draw die punch casting.  
             
         
        """
        pass
    @property
    def PartialRibHeight(self) -> float:
        """
        Getter for property: (float) PartialRibHeight
         Returns the partial rib height of the draw die punch casting.  
             
         
        """
        pass
    @property
    def ReliefAngle(self) -> float:
        """
        Getter for property: (float) ReliefAngle
         Returns the relief angle of the draw die punch casting.  
             
         
        """
        pass
    @property
    def ReliefDistance(self) -> float:
        """
        Getter for property: (float) ReliefDistance
         Returns the relief distance of the draw die punch casting.  
             
         
        """
        pass
    @property
    def WallThickness(self) -> float:
        """
        Getter for property: (float) WallThickness
         Returns the wall thickness of the draw die punch casting.  
             
         
        """
        pass
    def GetBaseAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the base faces attributes. 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. Title for attribute. .
         - value is: str. Value of attribute. .
         - color is: int. Color of base faces. .

        """
        pass
    def GetBeltWallAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the belt wall faces attributes. 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. Title for attribute. .
         - value is: str. Value of attribute. .
         - color is: int. Color of belt wall faces. .

        """
        pass
    def GetFormingAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the forming faces attributes. 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. Title for attribute. .
         - value is: str. Value of attribute. .
         - color is: int. Color of forming faces. .

        """
        pass
    def GetPunchProfileAttributes(self) -> Tuple[str, str]:
        """
         Gets the punch profile edges attributes. 
         Returns A tuple consisting of (title, value). 
         - title is: str. Title for attribute. .
         - value is: str. Value of attribute. .

        """
        pass
    def SetBaseAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the base faces attributes. 
        """
        pass
    def SetBaseThickness(self, base_thickness: float) -> None:
        """
         
        """
        pass
    def SetBaseWidth(self, base_width: float) -> None:
        """
         
        """
        pass
    def SetBeltThickness(self, belt_thickness: str) -> None:
        """
         
        """
        pass
    def SetBeltWallAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the belt wall faces attributes. 
        """
        pass
    def SetDeckThickness(self, deck_thickness: float) -> None:
        """
         
        """
        pass
    def SetDesignStatus(self, design_status: bool) -> None:
        """
         
        """
        pass
    def SetDisplayStatus(self, display_status: bool) -> None:
        """
         
        """
        pass
    def SetFormingAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the forming faces attributes. 
        """
        pass
    def SetOffsetProfileToTop(self, offset_profile_to_top: float) -> None:
        """
         
        """
        pass
    def SetPartialRibHeight(self, partial_rib_height: float) -> None:
        """
         
        """
        pass
    def SetPunchProfileAttributes(self, title: str, value: str) -> None:
        """
         Sets the punch profile edges attributes. 
        """
        pass
    def SetReliefAngle(self, relief_angle: float) -> None:
        """
         
        """
        pass
    def SetReliefDistance(self, relief_distance: float) -> None:
        """
         
        """
        pass
    def SetWallThickness(self, wall_thickness: float) -> None:
        """
         
        """
        pass
import NXOpen.Features
class FaceSheetBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Face Sheet feature """
    @property
    def StampingOutput(self) -> NXOpen.Features.Feature:
        """
        Getter for property: ( NXOpen.Features.Feature) StampingOutput
         Returns the stamping output feature of the Face Sheet   
            
         
        """
        pass
    @StampingOutput.setter
    def StampingOutput(self, object: NXOpen.Features.Feature):
        """
        Setter for property: ( NXOpen.Features.Feature) StampingOutput
         Returns the stamping output feature of the Face Sheet   
            
         
        """
        pass
import NXOpen
import NXOpen.Features
class FillAreaBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a builder that is used to create or edit a NXOpen.Die.FillArea feature.
    """
    class Types(Enum):
        """
        Members Include: 
         |BaseFlange|  Fill area is in the base flange area. 
         |ProductContact|  Fill area is in the upper deck where relief for the product has been added. 
         |ScrapArea|  Remove the volume instead of filling. Targeted for the outer trim line area. 
         |UserDefined|  The user must defined all the constraints for the area (inputs from the target are ignored). 

        """
        BaseFlange: int
        ProductContact: int
        ScrapArea: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> FillAreaBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class UpperLimitTypes(Enum):
        """
        Members Include: 
         |Sheet|  Upper limit is defined by a sheet body. 
         |Plane|  Upper limit is defined by a plane. 

        """
        Sheet: int
        Plane: int
        @staticmethod
        def ValueOf(value: int) -> FillAreaBuilder.UpperLimitTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngleTolerance(self) -> float:
        """
        Getter for property: (float) AngleTolerance
         Returns the angle tolerance.  
             
         
        """
        pass
    @AngleTolerance.setter
    def AngleTolerance(self, angleTolerance: float):
        """
        Setter for property: (float) AngleTolerance
         Returns the angle tolerance.  
             
         
        """
        pass
    @property
    def BaseOrientation(self) -> DiePlaneBuilder:
        """
        Getter for property: ( DiePlaneBuilder NXOp) BaseOrientation
         Returns the plane defining the base of the target solid.  
           Used to orient the direction of the build and the trims for the fill area. May be supplied by the selected target.   
         
        """
        pass
    @property
    def Boundary(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Boundary
         Returns the closed boundary profile that defines the fill area.  
             
         
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
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance.  
             
         
        """
        pass
    @property
    def LowerLimitOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LowerLimitOffset
         Returns the expression containing the lower limit offset used to adjust the lower limit to ensure a boolean.  
           A positive value will indicate transforming the limit away from the upper limit.   
         
        """
        pass
    @property
    def LowerLimitSheet(self) -> NXOpen.SelectBody:
        """
        Getter for property: ( NXOpen.SelectBody) LowerLimitSheet
         Returns the sheet (such as the inner deck sheet) used to trim the fill area solid.  
           This might be a sheet that is interior to the upper deck, but is always defined between the base and the upper limit. 
                    Only valid when type is  Die::FillAreaBuilder::TypesProductContact  or  Die::FillAreaBuilder::TypesUserDefined .   
         
        """
        pass
    @property
    def Target(self) -> NXOpen.SelectBody:
        """
        Getter for property: ( NXOpen.SelectBody) Target
         Returns the target solid the fill area will be united with or subtracted from.  
             
         
        """
        pass
    @property
    def Type(self) -> FillAreaBuilder.Types:
        """
        Getter for property: ( FillAreaBuilder.Types NXOp) Type
         Returns the indicator for the type of fill area to build.  
             
         
        """
        pass
    @Type.setter
    def Type(self, type: FillAreaBuilder.Types):
        """
        Setter for property: ( FillAreaBuilder.Types NXOp) Type
         Returns the indicator for the type of fill area to build.  
             
         
        """
        pass
    @property
    def UpperLimitPlane(self) -> DiePlaneBuilder:
        """
        Getter for property: ( DiePlaneBuilder NXOp) UpperLimitPlane
         Returns the plane used to trim the fill area solid.  
           A plane might be used to limit the fill area solid to just the flange of the casting. Only valid when type is  Die::FillAreaBuilder::UpperLimitTypesPlane .   
         
        """
        pass
    @property
    def UpperLimitSheet(self) -> NXOpen.SelectBody:
        """
        Getter for property: ( NXOpen.SelectBody) UpperLimitSheet
         Returns the sheet (such as the sheet metal) used to trim the fill area solid.  
           Only valid when type is  Die::FillAreaBuilder::UpperLimitTypesSheet .   
         
        """
        pass
    @property
    def UpperLimitType(self) -> FillAreaBuilder.UpperLimitTypes:
        """
        Getter for property: ( FillAreaBuilder.UpperLimitTypes NXOp) UpperLimitType
         Returns the value that determines whether the upper limit is defined by a sheet or plane.  
           Only valid when type is  Die::FillAreaBuilder::TypesScrapArea  
                    or  Die::FillAreaBuilder::TypesUserDefined .   
         
        """
        pass
    @UpperLimitType.setter
    def UpperLimitType(self, upperLimitType: FillAreaBuilder.UpperLimitTypes):
        """
        Setter for property: ( FillAreaBuilder.UpperLimitTypes NXOp) UpperLimitType
         Returns the value that determines whether the upper limit is defined by a sheet or plane.  
           Only valid when type is  Die::FillAreaBuilder::TypesScrapArea  
                    or  Die::FillAreaBuilder::TypesUserDefined .   
         
        """
        pass
import NXOpen.Features
class FillArea(NXOpen.Features.BodyFeature): 
    """ Represents a die design fill area feature. """
    pass
import NXOpen
import NXOpen.Features
class FillBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents an Area Fill feature """
    @property
    def AngleTolerance(self) -> float:
        """
        Getter for property: (float) AngleTolerance
         Returns the angle tolerance of the area fill   
            
         
        """
        pass
    @AngleTolerance.setter
    def AngleTolerance(self, angle_tolerance: float):
        """
        Setter for property: (float) AngleTolerance
         Returns the angle tolerance of the area fill   
            
         
        """
        pass
    @property
    def CopyAndMirror(self) -> bool:
        """
        Getter for property: (bool) CopyAndMirror
         Returns the copy and mirror setting of the area fill   
            
         
        """
        pass
    @CopyAndMirror.setter
    def CopyAndMirror(self, copy_and_mirror: bool):
        """
        Setter for property: (bool) CopyAndMirror
         Returns the copy and mirror setting of the area fill   
            
         
        """
        pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance of the area fill   
            
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distance_tolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance of the area fill   
            
         
        """
        pass
    @property
    def FillForAddendum(self) -> bool:
        """
        Getter for property: (bool) FillForAddendum
         Returns the fill for addendum setting of the area fill   
            
         
        """
        pass
    @FillForAddendum.setter
    def FillForAddendum(self, fill_for_addendum: bool):
        """
        Setter for property: (bool) FillForAddendum
         Returns the fill for addendum setting of the area fill   
            
         
        """
        pass
    @property
    def MirrorPlane(self) -> NXOpen.ISurface:
        """
        Getter for property: ( NXOpen.ISurface) MirrorPlane
         Returns the plane to mirror the area fill about   
            
         
        """
        pass
    @MirrorPlane.setter
    def MirrorPlane(self, mirror_plane: NXOpen.ISurface):
        """
        Setter for property: ( NXOpen.ISurface) MirrorPlane
         Returns the plane to mirror the area fill about   
            
         
        """
        pass
    @property
    def PointInRegion(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) PointInRegion
         Returns the point in region of the area fill   
            
         
        """
        pass
    @PointInRegion.setter
    def PointInRegion(self, point_in_region: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) PointInRegion
         Returns the point in region of the area fill   
            
         
        """
        pass
    @property
    def TippedProduct(self) -> NXOpen.Features.Feature:
        """
        Getter for property: ( NXOpen.Features.Feature) TippedProduct
         Returns the tipped product of the area fill   
            
         
        """
        pass
    @TippedProduct.setter
    def TippedProduct(self, tipped_product: NXOpen.Features.Feature):
        """
        Setter for property: ( NXOpen.Features.Feature) TippedProduct
         Returns the tipped product of the area fill   
            
         
        """
        pass
    def GetFillShape(self) -> List[NXOpen.Body]:
        """
         Gets the fill shape of the area fill 
         Returns bodies ( NXOpen.Body Li):  bodies .
        """
        pass
    def GetRegionBounds(self) -> Tuple[List[NXOpen.IProfile], DirectionOption]:
        """
         Gets the region bounds of the area fill 
         Returns A tuple consisting of (profile_entries, direction). 
         - profile_entries is:  NXOpen.IProfile Li. profile entries .
         - direction is:  DirectionOption NXOp. Profile direction .

        """
        pass
    def SetFillShape(self, bodies: List[NXOpen.Body]) -> None:
        """
         Sets the fill shape of the area fill 
        """
        pass
    def SetRegionBounds(self, direction: DirectionOption, profile_entries: List[NXOpen.IProfile]) -> None:
        """
         Sets the region bounds of the area fill 
        """
        pass
import NXOpen
import NXOpen.Features
class FingerClearanceNotchBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a builder that is used to create or edit a NXOpen.Die.FingerClearanceNotch feature.
    """
    class Types(Enum):
        """
        Members Include: 
         |Section|  Build from an open section profile. 
         |Face|  Build from either a single face or a set of connected faces. 
         |SheetBody|  Build from either a sheet body or a solid body. 

        """
        Section: int
        Face: int
        SheetBody: int
        @staticmethod
        def ValueOf(value: int) -> FingerClearanceNotchBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngleTolerance(self) -> float:
        """
        Getter for property: (float) AngleTolerance
         Returns the angle tolerance.  
             
         
        """
        pass
    @AngleTolerance.setter
    def AngleTolerance(self, angleTolerance: float):
        """
        Setter for property: (float) AngleTolerance
         Returns the angle tolerance.  
             
         
        """
        pass
    @property
    def Attributes(self) -> DieAttributesBuilder:
        """
        Getter for property: ( DieAttributesBuilder NXOp) Attributes
         Returns the attribute title, value and face color to apply to the notch faces.  
             
         
        """
        pass
    @property
    def BaseOrientation(self) -> DiePlaneBuilder:
        """
        Getter for property: ( DiePlaneBuilder NXOp) BaseOrientation
         Returns the plane defining the base of the target solid.  
           Used to orient the extrude and clearance directions.   
         
        """
        pass
    @property
    def ClearanceDirection(self) -> DieDirectionBuilder:
        """
        Getter for property: ( DieDirectionBuilder NXOp) ClearanceDirection
         Returns the direction (pointing away from the solid) in which to clear material from the target solid.  
             
         
        """
        pass
    @property
    def Depth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Depth
         Returns the expression containing the value for the clearance to provide into the target solid.  
             
         
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
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance.  
             
         
        """
        pass
    @property
    def ExtrudeWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ExtrudeWidth
         Returns the expression containing the value to use to extrude the section.  
           The extrusion direction is specified by the cross product of the base orientation and the clearance direction.   
         
        """
        pass
    @property
    def Geometry(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Geometry
         Returns the geometry to use as the definition of the notch.  
           A single face or multiple connected faces can be specified, or a single sheet or body may be specified. 
                    Only valid when type is  Die::FingerClearanceNotchBuilder::TypesFace  or  Die::FingerClearanceNotchBuilder::TypesSheetBody .   
         
        """
        pass
    @property
    def ReverseDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseDirection
         Returns the value to apply, for the purpose of reversing, to the derived clearance direction if a face or sheet body is specified.  
           If TRUE, then the derived direction will be flipped.   
         
        """
        pass
    @ReverseDirection.setter
    def ReverseDirection(self, reverseDirection: bool):
        """
        Setter for property: (bool) ReverseDirection
         Returns the value to apply, for the purpose of reversing, to the derived clearance direction if a face or sheet body is specified.  
           If TRUE, then the derived direction will be flipped.   
         
        """
        pass
    @property
    def Section(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Section
         Returns the open section constructed from curves, edges, or a sketch.  
           Only valid when type is  Die::FingerClearanceNotchBuilder::TypesSection .   
         
        """
        pass
    @property
    def Target(self) -> NXOpen.SelectBody:
        """
        Getter for property: ( NXOpen.SelectBody) Target
         Returns the target solid the finger clearance notch will be subtracted from.  
             
         
        """
        pass
    @property
    def Type(self) -> FingerClearanceNotchBuilder.Types:
        """
        Getter for property: ( FingerClearanceNotchBuilder.Types NXOp) Type
         Returns the indicator specifying the type of input data that defines how to build the notch.  
             
         
        """
        pass
    @Type.setter
    def Type(self, type: FingerClearanceNotchBuilder.Types):
        """
        Setter for property: ( FingerClearanceNotchBuilder.Types NXOp) Type
         Returns the indicator specifying the type of input data that defines how to build the notch.  
             
         
        """
        pass
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Width
         Returns the expression containing the value for the clearance to provide on either side of the notch.  
             
         
        """
        pass
import NXOpen.Features
class FingerClearanceNotch(NXOpen.Features.BodyFeature): 
    """ Represents a die design finger clearance notch feature. """
    pass
import NXOpen
import NXOpen.Features
class FlangeSteelRibChildBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Die Flange Steel Rib Child sub feature. """
    @property
    def Angle(self) -> float:
        """
        Getter for property: (float) Angle
         Returns the angle of the Flange Steel Rib   
            
         
        """
        pass
    @Angle.setter
    def Angle(self, angle: float):
        """
        Setter for property: (float) Angle
         Returns the angle of the Flange Steel Rib   
            
         
        """
        pass
    @property
    def BackDistance(self) -> float:
        """
        Getter for property: (float) BackDistance
         Returns the back distance of the Flange Steel Rib   
            
         
        """
        pass
    @BackDistance.setter
    def BackDistance(self, back_distance: float):
        """
        Setter for property: (float) BackDistance
         Returns the back distance of the Flange Steel Rib   
            
         
        """
        pass
    @property
    def BuildStatus(self) -> DieBuildStatusOption:
        """
        Getter for property: ( DieBuildStatusOption NXOp) BuildStatus
         Returns the build status of the Flange Steel Rib   
            
         
        """
        pass
    @property
    def ChamferDistance(self) -> float:
        """
        Getter for property: (float) ChamferDistance
         Returns the chamfer distance of the Flange Steel Rib   
            
         
        """
        pass
    @ChamferDistance.setter
    def ChamferDistance(self, chamfer_distance: float):
        """
        Setter for property: (float) ChamferDistance
         Returns the chamfer distance of the Flange Steel Rib   
            
         
        """
        pass
    @property
    def DesignStatus(self) -> bool:
        """
        Getter for property: (bool) DesignStatus
         Returns the design status of the Flange Steel Rib   
            
         
        """
        pass
    @DesignStatus.setter
    def DesignStatus(self, design_status: bool):
        """
        Setter for property: (bool) DesignStatus
         Returns the design status of the Flange Steel Rib   
            
         
        """
        pass
    @property
    def DisplayStatus(self) -> bool:
        """
        Getter for property: (bool) DisplayStatus
         Returns the display status of the Flange Steel Rib   
            
         
        """
        pass
    @DisplayStatus.setter
    def DisplayStatus(self, display_status: bool):
        """
        Setter for property: (bool) DisplayStatus
         Returns the display status of the Flange Steel Rib   
            
         
        """
        pass
    @property
    def Offset(self) -> float:
        """
        Getter for property: (float) Offset
         Returns the offset of the Flange Steel Rib   
            
         
        """
        pass
    @Offset.setter
    def Offset(self, offset: float):
        """
        Setter for property: (float) Offset
         Returns the offset of the Flange Steel Rib   
            
         
        """
        pass
    @property
    def Plane(self) -> NXOpen.ISurface:
        """
        Getter for property: ( NXOpen.ISurface) Plane
         Returns the plane of the Flange Steel Rib   
            
         
        """
        pass
    @Plane.setter
    def Plane(self, plane: NXOpen.ISurface):
        """
        Setter for property: ( NXOpen.ISurface) Plane
         Returns the plane of the Flange Steel Rib   
            
         
        """
        pass
    @property
    def SheetMetalDistance(self) -> float:
        """
        Getter for property: (float) SheetMetalDistance
         Returns the sheet metal distance of the Flange Steel Rib   
            
         
        """
        pass
    @SheetMetalDistance.setter
    def SheetMetalDistance(self, sheet_metal_distance: float):
        """
        Setter for property: (float) SheetMetalDistance
         Returns the sheet metal distance of the Flange Steel Rib   
            
         
        """
        pass
    @property
    def Thickness(self) -> float:
        """
        Getter for property: (float) Thickness
         Returns the thickness of the Flange Steel Rib   
            
         
        """
        pass
    @Thickness.setter
    def Thickness(self, thickness: float):
        """
        Setter for property: (float) Thickness
         Returns the thickness of the Flange Steel Rib   
            
         
        """
        pass
    @property
    def UseAngle(self) -> int:
        """
        Getter for property: (int) UseAngle
         Returns the use angle toggle of the Flange Steel Ribs   
            
         
        """
        pass
    @UseAngle.setter
    def UseAngle(self, use_angle: int):
        """
        Setter for property: (int) UseAngle
         Returns the use angle toggle of the Flange Steel Ribs   
            
         
        """
        pass
import NXOpen.Features
class FlangeSteelRibParentBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Die Flange Steel Rib Parent sub feature. """
    @property
    def Angle(self) -> float:
        """
        Getter for property: (float) Angle
         Returns the angle of the Flange Steel Ribs   
            
         
        """
        pass
    @Angle.setter
    def Angle(self, angle: float):
        """
        Setter for property: (float) Angle
         Returns the angle of the Flange Steel Ribs   
            
         
        """
        pass
    @property
    def BackDistance(self) -> float:
        """
        Getter for property: (float) BackDistance
         Returns the back distance of the Flange Steel Ribs   
            
         
        """
        pass
    @BackDistance.setter
    def BackDistance(self, back_distance: float):
        """
        Setter for property: (float) BackDistance
         Returns the back distance of the Flange Steel Ribs   
            
         
        """
        pass
    @property
    def BuildStatus(self) -> DieBuildStatusOption:
        """
        Getter for property: ( DieBuildStatusOption NXOp) BuildStatus
         Returns the build status of the Flange Steel Ribs   
            
         
        """
        pass
    @property
    def ChamferDistance(self) -> float:
        """
        Getter for property: (float) ChamferDistance
         Returns the chamfer distance of the Flange Steel Ribs   
            
         
        """
        pass
    @ChamferDistance.setter
    def ChamferDistance(self, chamfer_distance: float):
        """
        Setter for property: (float) ChamferDistance
         Returns the chamfer distance of the Flange Steel Ribs   
            
         
        """
        pass
    @property
    def DesignStatus(self) -> bool:
        """
        Getter for property: (bool) DesignStatus
         Returns the design status of the Flange Steel Ribs   
            
         
        """
        pass
    @DesignStatus.setter
    def DesignStatus(self, design_status: bool):
        """
        Setter for property: (bool) DesignStatus
         Returns the design status of the Flange Steel Ribs   
            
         
        """
        pass
    @property
    def DisplayStatus(self) -> bool:
        """
        Getter for property: (bool) DisplayStatus
         Returns the display status of the Flange Steel Ribs   
            
         
        """
        pass
    @DisplayStatus.setter
    def DisplayStatus(self, display_status: bool):
        """
        Setter for property: (bool) DisplayStatus
         Returns the display status of the Flange Steel Ribs   
            
         
        """
        pass
    @property
    def Offset(self) -> float:
        """
        Getter for property: (float) Offset
         Returns the offset of the Flange Steel Ribs   
            
         
        """
        pass
    @Offset.setter
    def Offset(self, offset: float):
        """
        Setter for property: (float) Offset
         Returns the offset of the Flange Steel Ribs   
            
         
        """
        pass
    @property
    def SheetMetalDistance(self) -> float:
        """
        Getter for property: (float) SheetMetalDistance
         Returns the sheet metal distance of the Flange Steel Ribs   
            
         
        """
        pass
    @SheetMetalDistance.setter
    def SheetMetalDistance(self, sheet_metal_distance: float):
        """
        Setter for property: (float) SheetMetalDistance
         Returns the sheet metal distance of the Flange Steel Ribs   
            
         
        """
        pass
    @property
    def Thickness(self) -> float:
        """
        Getter for property: (float) Thickness
         Returns the thickness of the Flange Steel Ribs   
            
         
        """
        pass
    @Thickness.setter
    def Thickness(self, thickness: float):
        """
        Setter for property: (float) Thickness
         Returns the thickness of the Flange Steel Ribs   
            
         
        """
        pass
    @property
    def UseAngle(self) -> int:
        """
        Getter for property: (int) UseAngle
         Returns the use angle toggle of the Flange Steel Ribs   
            
         
        """
        pass
    @UseAngle.setter
    def UseAngle(self, use_angle: int):
        """
        Setter for property: (int) UseAngle
         Returns the use angle toggle of the Flange Steel Ribs   
            
         
        """
        pass
    def CreateChild(self) -> FlangeSteelRibChildBuilder:
        """
         Creates a child Flange Steel Rib. 
         Returns diefsribchild ( FlangeSteelRibChildBuilder NXOp):  .
        """
        pass
    def DeleteChild(self, diefsribchild: FlangeSteelRibChildBuilder) -> None:
        """
         Deletes a child Flange Steel Rib. 
        """
        pass
    def GetChildren(self) -> List[FlangeSteelRibChildBuilder]:
        """
         Outputs the Flange Steel Rib children 
         Returns children ( FlangeSteelRibChildBuilder List[NX):  children .
        """
        pass
import NXOpen
import NXOpen.Features
class FlangeTaskBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Flange Task feature builder. """
    class CamTypes(Enum):
        """
        Members Include: 
         |Direct|  Direct 
         |AerialConventional|  Aerial Cam - Conventional Fill 
         |BaseConventional|  Base Mounted Cam - Conventional Fill 
         |AerialRotary|  Aerial Cam - Rotary Fill 
         |BellCrank|  Bell Crank 

        """
        Direct: int
        AerialConventional: int
        BaseConventional: int
        AerialRotary: int
        BellCrank: int
        @staticmethod
        def ValueOf(value: int) -> FlangeTaskBuilder.CamTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PierceTypes(Enum):
        """
        Members Include: 
         |Gage|  Use Gage tolerance. 
         |Critical|  Use Critical tolerance. 
         |Standard|  Use Standard tolerance. 

        """
        Gage: int
        Critical: int
        Standard: int
        @staticmethod
        def ValueOf(value: int) -> FlangeTaskBuilder.PierceTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SpringbackTypes(Enum):
        """
        Members Include: 
         |Constant|  Constant 
         |Law|  Law Controlled 

        """
        Constant: int
        Law: int
        @staticmethod
        def ValueOf(value: int) -> FlangeTaskBuilder.SpringbackTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngleTolerance(self) -> float:
        """
        Getter for property: (float) AngleTolerance
         Returns the angle tolerance of the flange task   
            
         
        """
        pass
    @AngleTolerance.setter
    def AngleTolerance(self, angle_tolerance: float):
        """
        Setter for property: (float) AngleTolerance
         Returns the angle tolerance of the flange task   
            
         
        """
        pass
    @property
    def CamDirection(self) -> NXOpen.ILocation:
        """
        Getter for property: ( NXOpen.ILocation) CamDirection
         Returns the cam direction of the flange task   
            
         
        """
        pass
    @CamDirection.setter
    def CamDirection(self, cam_direction: NXOpen.ILocation):
        """
        Setter for property: ( NXOpen.ILocation) CamDirection
         Returns the cam direction of the flange task   
            
         
        """
        pass
    @property
    def CamType(self) -> FlangeTaskBuilder.CamTypes:
        """
        Getter for property: ( FlangeTaskBuilder.CamTypes NXOp) CamType
         Returns the cam type of the flange task   
            
         
        """
        pass
    @CamType.setter
    def CamType(self, cam_type: FlangeTaskBuilder.CamTypes):
        """
        Setter for property: ( FlangeTaskBuilder.CamTypes NXOp) CamType
         Returns the cam type of the flange task   
            
         
        """
        pass
    @property
    def DisplayRotatedItems(self) -> bool:
        """
        Getter for property: (bool) DisplayRotatedItems
         Returns the display rotated items setting of the flange task.  
           
                True indicates that the reference point and cam direction objects should be created and displayed in the die face feature.   
         
        """
        pass
    @DisplayRotatedItems.setter
    def DisplayRotatedItems(self, display_setting: bool):
        """
        Setter for property: (bool) DisplayRotatedItems
         Returns the display rotated items setting of the flange task.  
           
                True indicates that the reference point and cam direction objects should be created and displayed in the die face feature.   
         
        """
        pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance of the flange task   
            
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distance_tolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance of the flange task   
            
         
        """
        pass
    @property
    def FinishOperation(self) -> bool:
        """
        Getter for property: (bool) FinishOperation
         Returns the finish operation of the flange task   
            
         
        """
        pass
    @FinishOperation.setter
    def FinishOperation(self, finish_operation: bool):
        """
        Setter for property: (bool) FinishOperation
         Returns the finish operation of the flange task   
            
         
        """
        pass
    @property
    def PierceAndExtrude(self) -> bool:
        """
        Getter for property: (bool) PierceAndExtrude
         Returns the pierce and extrude setting of the flange task.  
           
                True indicates that the flange task is a pierce and extrude type.   
         
        """
        pass
    @PierceAndExtrude.setter
    def PierceAndExtrude(self, pierce_and_extrude: bool):
        """
        Setter for property: (bool) PierceAndExtrude
         Returns the pierce and extrude setting of the flange task.  
           
                True indicates that the flange task is a pierce and extrude type.   
         
        """
        pass
    @property
    def PierceType(self) -> FlangeTaskBuilder.PierceTypes:
        """
        Getter for property: ( FlangeTaskBuilder.PierceTypes NXOp) PierceType
         Returns the pierce type of the flange task   
            
         
        """
        pass
    @PierceType.setter
    def PierceType(self, pierce_type: FlangeTaskBuilder.PierceTypes):
        """
        Setter for property: ( FlangeTaskBuilder.PierceTypes NXOp) PierceType
         Returns the pierce type of the flange task   
            
         
        """
        pass
    @property
    def PointInRegion(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) PointInRegion
         Returns the keep point in the region of the flange task   
            
         
        """
        pass
    @PointInRegion.setter
    def PointInRegion(self, point_in_region: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) PointInRegion
         Returns the keep point in the region of the flange task   
            
         
        """
        pass
    @property
    def SpringbackAngle(self) -> str:
        """
        Getter for property: (str) SpringbackAngle
         Returns the springback angle of the flange task   
            
         
        """
        pass
    @SpringbackAngle.setter
    def SpringbackAngle(self, springback_angle: str):
        """
        Setter for property: (str) SpringbackAngle
         Returns the springback angle of the flange task   
            
         
        """
        pass
    @property
    def SpringbackType(self) -> FlangeTaskBuilder.SpringbackTypes:
        """
        Getter for property: ( FlangeTaskBuilder.SpringbackTypes NXOp) SpringbackType
         Returns the springback type of the flange task   
            
         
        """
        pass
    @SpringbackType.setter
    def SpringbackType(self, springback_type: FlangeTaskBuilder.SpringbackTypes):
        """
        Setter for property: ( FlangeTaskBuilder.SpringbackTypes NXOp) SpringbackType
         Returns the springback type of the flange task   
            
         
        """
        pass
    @property
    def TippedProduct(self) -> NXOpen.Features.Feature:
        """
        Getter for property: ( NXOpen.Features.Feature) TippedProduct
         Returns the tipped product of the flange task   
            
         
        """
        pass
    @TippedProduct.setter
    def TippedProduct(self, tipped_product: NXOpen.Features.Feature):
        """
        Setter for property: ( NXOpen.Features.Feature) TippedProduct
         Returns the tipped product of the flange task   
            
         
        """
        pass
    def GetAssociativeObjects(self) -> List[NXOpen.DisplayableObject]:
        """
         Gets the associative objects of the flange task 
         Returns objects ( NXOpen.DisplayableObject Li):  .
        """
        pass
    def GetCameraLayerAndXmlp(self) -> Tuple[List[str], List[str]]:
        """
         Gets the camera layer settings and xmlp data 
         Returns A tuple consisting of (layer_settings, xmlp_data). 
         - layer_settings is: List[str]. 1 layer setting string for each camera object. 
                                                                       the string needs to be 256 characters long 
                                                                       (one for each user layer) with either 0 for off
                                                                       or 1 for on. .
         - xmlp_data is: List[str]. xmlp data .

        """
        pass
    def GetCameraNames(self) -> List[str]:
        """
         Gets the names of the camera 
         Returns strings (List[str]):  each string contains the name of a camera object .
        """
        pass
    def GetCameraViews(self) -> List[NXOpen.View]:
        """
         Gets the camera views of the flange task 
         Returns objects ( NXOpen.View Li):  .
        """
        pass
    def GetDetails(self) -> List[str]:
        """
         Gets the detailed description of the flange task 
         Returns strings (List[str]):  detail strings .
        """
        pass
    def GetRegionBounds(self) -> Tuple[List[NXOpen.IProfile], DirectionOption]:
        """
         Gets the region bounds of the flange task 
         Returns A tuple consisting of (profile_entries, direction). 
         - profile_entries is:  NXOpen.IProfile Li. Profile entries that make up the 
                                                                                                   boundary of the flange task .
         - direction is:  DirectionOption NXOp. Profile direction .

        """
        pass
    @overload
    def GetShapeDetail(self) -> Tuple[List[NXOpen.IProfile], DirectionOption]:
        """
         Gets the shape detail of the flange task for profiles 
         Returns A tuple consisting of (profile_entries, direction). 
         - profile_entries is:  NXOpen.IProfile Li. Profile entries .
         - direction is:  DirectionOption NXOp. Profile direction .

        """
        pass
    @overload
    def GetShapeDetail(self) -> List[NXOpen.Body]:
        """
         Gets the shape detail of the form task for bodies 
         Returns bodies ( NXOpen.Body Li):  bodies .
        """
        pass
    def SetAssociativeObjects(self, objects: List[NXOpen.DisplayableObject]) -> None:
        """
         Sets the associative objects of the flange task 
        """
        pass
    def SetCameraLayerAndXmlp(self, layer_settings: List[str], xmlp_data: List[str]) -> None:
        """
         Sets the camera layer settings and xmlp data 
        """
        pass
    def SetCameraNames(self, strings: List[str]) -> None:
        """
         Sets the names of the camera 
        """
        pass
    def SetCameraViews(self, objects: List[NXOpen.View]) -> None:
        """
         Sets the camera views of the flange task 
        """
        pass
    def SetDetails(self, strings: List[str]) -> None:
        """
         Sets the detailed description of the flange task 
        """
        pass
    def SetRegionBounds(self, direction: DirectionOption, profile_entries: List[NXOpen.IProfile]) -> None:
        """
         Sets the region bounds of the flange task 
        """
        pass
    @overload
    def SetShapeDetail(self, direction: DirectionOption, profile_entries: List[NXOpen.IProfile]) -> None:
        """
         Sets the shape detail of the flange task for profiles 
        """
        pass
    @overload
    def SetShapeDetail(self, bodies: List[NXOpen.Body]) -> None:
        """
         Sets the shape detail of the form task for bodies 
        """
        pass
import NXOpen
import NXOpen.Features
class FormTaskBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Form Task feature builder. """
    @property
    def AngleTolerance(self) -> float:
        """
        Getter for property: (float) AngleTolerance
         Returns the angle tolerance of the form task.  
             
         
        """
        pass
    @AngleTolerance.setter
    def AngleTolerance(self, angle_tolerance: float):
        """
        Setter for property: (float) AngleTolerance
         Returns the angle tolerance of the form task.  
             
         
        """
        pass
    @property
    def CamDirection(self) -> NXOpen.ILocation:
        """
        Getter for property: ( NXOpen.ILocation) CamDirection
         Returns the cam direction of the form task.  
             
         
        """
        pass
    @CamDirection.setter
    def CamDirection(self, cam_direction: NXOpen.ILocation):
        """
        Setter for property: ( NXOpen.ILocation) CamDirection
         Returns the cam direction of the form task.  
             
         
        """
        pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance of the form task.  
             
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distance_tolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance of the form task.  
             
         
        """
        pass
    @property
    def FinishOperation(self) -> bool:
        """
        Getter for property: (bool) FinishOperation
         Returns the finish operation switch of the form task, if true the form task is a finish operation, if false it is not.  
             
         
        """
        pass
    @FinishOperation.setter
    def FinishOperation(self, finish_operation: bool):
        """
        Setter for property: (bool) FinishOperation
         Returns the finish operation switch of the form task, if true the form task is a finish operation, if false it is not.  
             
         
        """
        pass
    @property
    def PointInRegion(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) PointInRegion
         Returns the point in region of the form task.  
             
         
        """
        pass
    @PointInRegion.setter
    def PointInRegion(self, point_in_region: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) PointInRegion
         Returns the point in region of the form task.  
             
         
        """
        pass
    @property
    def TippedProduct(self) -> NXOpen.Features.Feature:
        """
        Getter for property: ( NXOpen.Features.Feature) TippedProduct
         Returns the tipped product of the form task.  
             
         
        """
        pass
    @TippedProduct.setter
    def TippedProduct(self, tipped_product: NXOpen.Features.Feature):
        """
        Setter for property: ( NXOpen.Features.Feature) TippedProduct
         Returns the tipped product of the form task.  
             
         
        """
        pass
    def GetDetails(self) -> List[str]:
        """
         Gets the details of the form task. 
         Returns strings (List[str]):  Detail strings. .
        """
        pass
    def GetRegionBounds(self) -> Tuple[List[NXOpen.IProfile], DirectionOption]:
        """
         Gets the region bounds of the form task. 
         Returns A tuple consisting of (profile_entries, direction). 
         - profile_entries is:  NXOpen.IProfile Li. The profile entries, will be curves, edges, faces, sketches or curve features. .
         - direction is:  DirectionOption NXOp. Profile direction. .

        """
        pass
    @overload
    def GetShapeDetail(self) -> Tuple[List[NXOpen.IProfile], DirectionOption]:
        """
         Gets the shape detail of the form task as a profile. 
         Returns A tuple consisting of (profile_entries, direction). 
         - profile_entries is:  NXOpen.IProfile Li. The profile entries, will be curves, edges, faces, sketches or curve features. .
         - direction is:  DirectionOption NXOp. Profile direction. .

        """
        pass
    @overload
    def GetShapeDetail(self) -> List[NXOpen.Body]:
        """
         Gets the shape detail of the form task. 
         Returns bodies ( NXOpen.Body Li):  Sheet bodies defining the unfinished shape. .
        """
        pass
    def SetDetails(self, strings: List[str]) -> None:
        """
         Sets the details of the form task. 
        """
        pass
    def SetRegionBounds(self, direction: DirectionOption, profile_entries: List[NXOpen.IProfile]) -> None:
        """
         Sets the region bounds of the form task. 
        """
        pass
    @overload
    def SetShapeDetail(self, direction: DirectionOption, profile_entries: List[NXOpen.IProfile]) -> None:
        """
         Sets the shape detail of the form task using a profile. 
        """
        pass
    @overload
    def SetShapeDetail(self, bodies: List[NXOpen.Body]) -> None:
        """
         Sets the shape detail of the form task. 
        """
        pass
import NXOpen
import NXOpen.Features
class HandlingCoreBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a builder that is used to create or edit a NXOpen.Die.HandlingCore feature.
    """
    class Types(Enum):
        """
        Members Include: 
         |AtLocation|  Location specified by the user. 
         |FromBase|  Location is an offset from the base. 
         |MapFromBase|  Locate by finding the minimum distance to the main profile of the target and then project and offset from the base. Used specifically for coring the main wall. 

        """
        AtLocation: int
        FromBase: int
        MapFromBase: int
        @staticmethod
        def ValueOf(value: int) -> HandlingCoreBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngleTolerance(self) -> float:
        """
        Getter for property: (float) AngleTolerance
         Returns the angle tolerance.  
             
         
        """
        pass
    @AngleTolerance.setter
    def AngleTolerance(self, angleTolerance: float):
        """
        Setter for property: (float) AngleTolerance
         Returns the angle tolerance.  
             
         
        """
        pass
    @property
    def BaseOrientation(self) -> DiePlaneBuilder:
        """
        Getter for property: ( DiePlaneBuilder NXOp) BaseOrientation
         Returns the base plane of the target.  
           Used for orienting the core and offset if needed.   
         
        """
        pass
    @property
    def Clearance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Clearance
         Returns the expression containing the value to use for the clearance offset of the core from the base plane.  
           
                    Only valid when type is  Die::HandlingCoreBuilder::TypesFromBase  or  Die::HandlingCoreBuilder::TypesMapFromBase .   
         
        """
        pass
    @property
    def CoreOrientation(self) -> DiePlaneBuilder:
        """
        Getter for property: ( DiePlaneBuilder NXOp) CoreOrientation
         Returns the plane of the core for deriving the rectangle and the start of the core.  
           Only valid when type is  Die::HandlingCoreBuilder::TypesAtLocation .   
         
        """
        pass
    @property
    def Depth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Depth
         Returns the expression containing the value to use for the extrusion depth when creating the core.  
             
         
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
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance.  
             
         
        """
        pass
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Height
         Returns the expression containing the value to use for the height of the core.  
             
         
        """
        pass
    @property
    def Location(self) -> DieLocationsBuilder:
        """
        Getter for property: ( DieLocationsBuilder NXOp) Location
         Returns the center location of the handling core.  
             
         
        """
        pass
    @property
    def Target(self) -> NXOpen.SelectBody:
        """
        Getter for property: ( NXOpen.SelectBody) Target
         Returns the target solid the handling core will be subtracted from.  
             
         
        """
        pass
    @property
    def Type(self) -> HandlingCoreBuilder.Types:
        """
        Getter for property: ( HandlingCoreBuilder.Types NXOp) Type
         Returns the indicator defining how the handling core is located in space.  
             
         
        """
        pass
    @Type.setter
    def Type(self, type: HandlingCoreBuilder.Types):
        """
        Setter for property: ( HandlingCoreBuilder.Types NXOp) Type
         Returns the indicator defining how the handling core is located in space.  
             
         
        """
        pass
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Width
         Returns the expression containing the value to use for the width of the core.  
             
         
        """
        pass
import NXOpen
import NXOpen.Features
class HandlingCoreChildBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Die Handling Core Child sub feature. """
    @property
    def BuildStatus(self) -> DieBuildStatusOption:
        """
        Getter for property: ( DieBuildStatusOption NXOp) BuildStatus
         Returns the build status of the handling core.  
             
         
        """
        pass
    @property
    def Center(self) -> NXOpen.ILocation:
        """
        Getter for property: ( NXOpen.ILocation) Center
         Returns the center of the handling core.  
             
         
        """
        pass
    @Center.setter
    def Center(self, center: NXOpen.ILocation):
        """
        Setter for property: ( NXOpen.ILocation) Center
         Returns the center of the handling core.  
             
         
        """
        pass
    @property
    def Clearance(self) -> float:
        """
        Getter for property: (float) Clearance
         Returns the clearance of the handling core.  
             
         
        """
        pass
    @Clearance.setter
    def Clearance(self, clearance: float):
        """
        Setter for property: (float) Clearance
         Returns the clearance of the handling core.  
             
         
        """
        pass
    @property
    def CoreOrientation(self) -> NXOpen.ISurface:
        """
        Getter for property: ( NXOpen.ISurface) CoreOrientation
         Returns the core orientation of the handling core.  
             
         
        """
        pass
    @CoreOrientation.setter
    def CoreOrientation(self, core_orientation: NXOpen.ISurface):
        """
        Setter for property: ( NXOpen.ISurface) CoreOrientation
         Returns the core orientation of the handling core.  
             
         
        """
        pass
    @property
    def Depth(self) -> float:
        """
        Getter for property: (float) Depth
         Returns the depth of the handling core.  
             
         
        """
        pass
    @Depth.setter
    def Depth(self, depth: float):
        """
        Setter for property: (float) Depth
         Returns the depth of the handling core.  
             
         
        """
        pass
    @property
    def DesignStatus(self) -> bool:
        """
        Getter for property: (bool) DesignStatus
         Returns the design status of the handling core, if true the handling core will be built into the model, if false it will not.  
             
         
        """
        pass
    @DesignStatus.setter
    def DesignStatus(self, design_status: bool):
        """
        Setter for property: (bool) DesignStatus
         Returns the design status of the handling core, if true the handling core will be built into the model, if false it will not.  
             
         
        """
        pass
    @property
    def DisplayStatus(self) -> bool:
        """
        Getter for property: (bool) DisplayStatus
         Returns the display status of the handling core, if true input data to the handling core will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    @DisplayStatus.setter
    def DisplayStatus(self, display_status: bool):
        """
        Setter for property: (bool) DisplayStatus
         Returns the display status of the handling core, if true input data to the handling core will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    @property
    def Height(self) -> float:
        """
        Getter for property: (float) Height
         Returns the height of the handling core.  
             
         
        """
        pass
    @Height.setter
    def Height(self, height: float):
        """
        Setter for property: (float) Height
         Returns the height of the handling core.  
             
         
        """
        pass
    @property
    def ReverseOrientation(self) -> bool:
        """
        Getter for property: (bool) ReverseOrientation
         Returns the value to reverse the orientation of the core plane,
             if true the handling core orientation normal will be reversed,
             if false it will not.  
             
         
        """
        pass
    @ReverseOrientation.setter
    def ReverseOrientation(self, reverse_orientation: bool):
        """
        Setter for property: (bool) ReverseOrientation
         Returns the value to reverse the orientation of the core plane,
             if true the handling core orientation normal will be reversed,
             if false it will not.  
             
         
        """
        pass
    @property
    def Width(self) -> float:
        """
        Getter for property: (float) Width
         Returns the width of the handling core.  
             
         
        """
        pass
    @Width.setter
    def Width(self, width: float):
        """
        Setter for property: (float) Width
         Returns the width of the handling core.  
             
         
        """
        pass
    def TranslateCenter(self, translate_dist: NXOpen.Vector3d) -> None:
        """
         Translates the center of the die handling core by the specified amount. 
        """
        pass
import NXOpen.Features
class HandlingCoreParentBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Die Handling Core Parent sub feature. """
    @property
    def BuildStatus(self) -> DieBuildStatusOption:
        """
        Getter for property: ( DieBuildStatusOption NXOp) BuildStatus
         Returns the build status of handling cores.  
             
         
        """
        pass
    @property
    def Clearance(self) -> float:
        """
        Getter for property: (float) Clearance
         Returns the clearance of handling cores.  
             
         
        """
        pass
    @Clearance.setter
    def Clearance(self, clearance: float):
        """
        Setter for property: (float) Clearance
         Returns the clearance of handling cores.  
             
         
        """
        pass
    @property
    def Depth(self) -> float:
        """
        Getter for property: (float) Depth
         Returns the depth of handling cores.  
             
         
        """
        pass
    @Depth.setter
    def Depth(self, depth: float):
        """
        Setter for property: (float) Depth
         Returns the depth of handling cores.  
             
         
        """
        pass
    @property
    def DesignStatus(self) -> bool:
        """
        Getter for property: (bool) DesignStatus
         Returns the design status of handling cores, if true the handling cores will be built into the model, if false they will not.  
             
         
        """
        pass
    @DesignStatus.setter
    def DesignStatus(self, design_status: bool):
        """
        Setter for property: (bool) DesignStatus
         Returns the design status of handling cores, if true the handling cores will be built into the model, if false they will not.  
             
         
        """
        pass
    @property
    def DisplayStatus(self) -> bool:
        """
        Getter for property: (bool) DisplayStatus
         Returns the display status of handling cores, if true input data to the handling cores will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    @DisplayStatus.setter
    def DisplayStatus(self, display_status: bool):
        """
        Setter for property: (bool) DisplayStatus
         Returns the display status of handling cores, if true input data to the handling cores will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    @property
    def Height(self) -> float:
        """
        Getter for property: (float) Height
         Returns the height of handling cores.  
             
         
        """
        pass
    @Height.setter
    def Height(self, height: float):
        """
        Setter for property: (float) Height
         Returns the height of handling cores.  
             
         
        """
        pass
    @property
    def Width(self) -> float:
        """
        Getter for property: (float) Width
         Returns the width of handling cores.  
             
         
        """
        pass
    @Width.setter
    def Width(self, width: float):
        """
        Setter for property: (float) Width
         Returns the width of handling cores.  
             
         
        """
        pass
    def CreateChild(self) -> HandlingCoreChildBuilder:
        """
         Creates a child handling core. 
         Returns diehandlingcorechild ( HandlingCoreChildBuilder NXOp):  .
        """
        pass
    def DeleteChild(self, diehandlingcorechild: HandlingCoreChildBuilder) -> None:
        """
         Deletes a child handling core. 
        """
        pass
    def GetChildren(self) -> List[HandlingCoreChildBuilder]:
        """
         Outputs the child handling cores. 
         Returns children ( HandlingCoreChildBuilder List[NX):  The child handling cores. .
        """
        pass
import NXOpen.Features
class HandlingCore(NXOpen.Features.BodyFeature): 
    """ Represents a die design handling core feature. """
    pass
import NXOpen
import NXOpen.Features
class HeelpostBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a NXOpen.Die.HeelpostBuilder builder
    """
    class Types(Enum):
        """
        Members Include: 
         |GuidepostWearplate|  allows a guide pin hole to be created 
         |StorageBlock|  no hole allowed 
         |SafetyBlock|  no hole allowed 

        """
        GuidepostWearplate: int
        StorageBlock: int
        SafetyBlock: int
        @staticmethod
        def ValueOf(value: int) -> HeelpostBuilder.Types:
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
    def BaseOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BaseOffset
         Returns the offset to apply to the given base before building the heelpost   
            
         
        """
        pass
    @property
    def BaseOrientation(self) -> DiePlaneBuilder:
        """
        Getter for property: ( DiePlaneBuilder NXOp) BaseOrientation
         Returns the base of the heelpost   
            
         
        """
        pass
    @property
    def Center(self) -> DieLocationBuilder:
        """
        Getter for property: ( DieLocationBuilder NXOp) Center
         Returns the location (center) for the heelpost   
            
         
        """
        pass
    @property
    def CreateFloor(self) -> bool:
        """
        Getter for property: (bool) CreateFloor
         Returns the value (true or false) to decide if the floor of the post should be created   
            
         
        """
        pass
    @CreateFloor.setter
    def CreateFloor(self, createFloor: bool):
        """
        Setter for property: (bool) CreateFloor
         Returns the value (true or false) to decide if the floor of the post should be created   
            
         
        """
        pass
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Diameter
         Returns the diameter of the guide pin hole   
            
         
        """
        pass
    @property
    def DieCenterlineCoordinateSystem(self) -> NXOpen.SelectCoordinateSystem:
        """
        Getter for property: ( NXOpen.SelectCoordinateSystem) DieCenterlineCoordinateSystem
         Returns the die centerline coordinate system for orienting the heelpost   
            
         
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
    def FloorThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FloorThickness
         Returns the floor thickness   
            
         
        """
        pass
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Height
         Returns the height from the selected base orientation to the origin of the pad orientation, if the pad orientation is not specified.  
           This is before application of any specified base and pad offsets.    
         
        """
        pass
    @property
    def HoleAttributes(self) -> DieAttributesBuilder:
        """
        Getter for property: ( DieAttributesBuilder NXOp) HoleAttributes
         Returns the hole attributes   
            
         
        """
        pass
    @property
    def HoleDiameterAttributes(self) -> DieAttributesBuilder:
        """
        Getter for property: ( DieAttributesBuilder NXOp) HoleDiameterAttributes
         Returns the hole diameter attributes (only the title is used)   
            
         
        """
        pass
    @property
    def Length(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Length
         Returns the length with respect to the coordinate system   
            
         
        """
        pass
    @property
    def LocationOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LocationOffset
         Returns the offset value to apply in the offset direction to find the heelpost center   
            
         
        """
        pass
    @property
    def OffsetDirection(self) -> DieDirectionBuilder:
        """
        Getter for property: ( DieDirectionBuilder NXOp) OffsetDirection
         Returns the direction to apply to the location to determine the center of the heelpost   
            
         
        """
        pass
    @property
    def PadAttributes(self) -> DieAttributesBuilder:
        """
        Getter for property: ( DieAttributesBuilder NXOp) PadAttributes
         Returns the pad attributes   
            
         
        """
        pass
    @property
    def PadOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PadOffset
         Returns the offset value to apply to the pad orientation before building the heelpost   
            
         
        """
        pass
    @property
    def PadOrientation(self) -> DiePlaneBuilder:
        """
        Getter for property: ( DiePlaneBuilder NXOp) PadOrientation
         Returns the orientation at the top of the heelpost   
            
         
        """
        pass
    @property
    def PadThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PadThickness
         Returns the pad thickness at the top of the post   
            
         
        """
        pass
    @property
    def ReliefAttributes(self) -> DieAttributesBuilder:
        """
        Getter for property: ( DieAttributesBuilder NXOp) ReliefAttributes
         Returns the relief attributes   
            
         
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
    def ReliefWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ReliefWidth
         Returns the relief width   
            
         
        """
        pass
    @property
    def Target(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) Target
         Returns the target solid the heelpost will be united with   
            
         
        """
        pass
    @property
    def Type(self) -> HeelpostBuilder.Types:
        """
        Getter for property: ( HeelpostBuilder.Types NXOp) Type
         Returns the post type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: HeelpostBuilder.Types):
        """
        Setter for property: ( HeelpostBuilder.Types NXOp) Type
         Returns the post type   
            
         
        """
        pass
    @property
    def UsePercent(self) -> bool:
        """
        Getter for property: (bool) UsePercent
         Returns the value (true or false) to decide how to determine the wall thickness.  
           True will evaluate each wall based on the total area of the post   
         
        """
        pass
    @UsePercent.setter
    def UsePercent(self, usePercent: bool):
        """
        Setter for property: (bool) UsePercent
         Returns the value (true or false) to decide how to determine the wall thickness.  
           True will evaluate each wall based on the total area of the post   
         
        """
        pass
    @property
    def WallACreate(self) -> bool:
        """
        Getter for property: (bool) WallACreate
         Returns the value (true or false) to decide if the "A" wall should be created   
            
         
        """
        pass
    @WallACreate.setter
    def WallACreate(self, wallACreate: bool):
        """
        Setter for property: (bool) WallACreate
         Returns the value (true or false) to decide if the "A" wall should be created   
            
         
        """
        pass
    @property
    def WallAOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) WallAOffset
         Returns the offset from the outside to be applied to the "A" wall   
            
         
        """
        pass
    @property
    def WallARelief(self) -> bool:
        """
        Getter for property: (bool) WallARelief
         Returns the value (true or false) to decide if relief should be created at the top of the "A" wall   
            
         
        """
        pass
    @WallARelief.setter
    def WallARelief(self, wallARelief: bool):
        """
        Setter for property: (bool) WallARelief
         Returns the value (true or false) to decide if relief should be created at the top of the "A" wall   
            
         
        """
        pass
    @property
    def WallAThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) WallAThickness
         Returns the "A" wall thickness   
            
         
        """
        pass
    @property
    def WallBCreate(self) -> bool:
        """
        Getter for property: (bool) WallBCreate
         Returns the value (true or false) to decide if the "B" wall should be created   
            
         
        """
        pass
    @WallBCreate.setter
    def WallBCreate(self, wallBCreate: bool):
        """
        Setter for property: (bool) WallBCreate
         Returns the value (true or false) to decide if the "B" wall should be created   
            
         
        """
        pass
    @property
    def WallBOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) WallBOffset
         Returns the offset from the outside to be applied to the "B wall   
            
         
        """
        pass
    @property
    def WallBRelief(self) -> bool:
        """
        Getter for property: (bool) WallBRelief
         Returns the value (true or false) to decide if relief should be created at the top of the "B" wall   
            
         
        """
        pass
    @WallBRelief.setter
    def WallBRelief(self, wallBRelief: bool):
        """
        Setter for property: (bool) WallBRelief
         Returns the value (true or false) to decide if relief should be created at the top of the "B" wall   
            
         
        """
        pass
    @property
    def WallBThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) WallBThickness
         Returns the "B" wall thickness   
            
         
        """
        pass
    @property
    def WallCCreate(self) -> bool:
        """
        Getter for property: (bool) WallCCreate
         Returns the value (true or false) to decide if the "C" wall should be created   
            
         
        """
        pass
    @WallCCreate.setter
    def WallCCreate(self, wallCCreate: bool):
        """
        Setter for property: (bool) WallCCreate
         Returns the value (true or false) to decide if the "C" wall should be created   
            
         
        """
        pass
    @property
    def WallCOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) WallCOffset
         Returns the offset from the outside to be applied to the "C" wall   
            
         
        """
        pass
    @property
    def WallCRelief(self) -> bool:
        """
        Getter for property: (bool) WallCRelief
         Returns the value (true or false) to decide if relief should be created at the top of the "C" wall   
            
         
        """
        pass
    @WallCRelief.setter
    def WallCRelief(self, wallCRelief: bool):
        """
        Setter for property: (bool) WallCRelief
         Returns the value (true or false) to decide if relief should be created at the top of the "C" wall   
            
         
        """
        pass
    @property
    def WallCThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) WallCThickness
         Returns the "C" wall thickness   
            
         
        """
        pass
    @property
    def WallDCreate(self) -> bool:
        """
        Getter for property: (bool) WallDCreate
         Returns the value (true or false) to decide if the "D" wall should be created   
            
         
        """
        pass
    @WallDCreate.setter
    def WallDCreate(self, wallDCreate: bool):
        """
        Setter for property: (bool) WallDCreate
         Returns the value (true or false) to decide if the "D" wall should be created   
            
         
        """
        pass
    @property
    def WallDOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) WallDOffset
         Returns the offset from the outside to be applied to the "D" wall   
            
         
        """
        pass
    @property
    def WallDRelief(self) -> bool:
        """
        Getter for property: (bool) WallDRelief
         Returns the value (true or false) to decide if relief should be created at the top of the "D" wall   
            
         
        """
        pass
    @WallDRelief.setter
    def WallDRelief(self, wallDRelief: bool):
        """
        Setter for property: (bool) WallDRelief
         Returns the value (true or false) to decide if relief should be created at the top of the "D" wall   
            
         
        """
        pass
    @property
    def WallDThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) WallDThickness
         Returns the "D" wall thickness   
            
         
        """
        pass
    @property
    def WallPercentage(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) WallPercentage
         Returns the percentage of the post area to be applied to determine the wall thicknesses   
            
         
        """
        pass
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Width
         Returns the width with respect to the coordinate system   
            
         
        """
        pass
    @property
    def XOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) XOffset
         Returns the offset applied in the X direction to determine the hole center   
            
         
        """
        pass
    @property
    def YOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YOffset
         Returns the offset applied in the Y direction to determine the hole center   
            
         
        """
        pass
import NXOpen.Features
class Heelpost(NXOpen.Features.BodyFeature): 
    """ Represents a heelpost feature """
    pass
import NXOpen
import NXOpen.Features
class HoleChildBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Die Hole Child sub feature. """
    @property
    def BuildStatus(self) -> DieBuildStatusOption:
        """
        Getter for property: ( DieBuildStatusOption NXOp) BuildStatus
         Returns the build status of the die hole.  
             
         
        """
        pass
    @property
    def Center(self) -> NXOpen.ILocation:
        """
        Getter for property: ( NXOpen.ILocation) Center
         Returns the center of the die hole.  
             
         
        """
        pass
    @Center.setter
    def Center(self, center: NXOpen.ILocation):
        """
        Setter for property: ( NXOpen.ILocation) Center
         Returns the center of the die hole.  
             
         
        """
        pass
    @property
    def CounterBoreDiameter(self) -> float:
        """
        Getter for property: (float) CounterBoreDiameter
         Returns the counter bore diameter of the die hole.  
             
         
        """
        pass
    @CounterBoreDiameter.setter
    def CounterBoreDiameter(self, counter_bore_diameter: float):
        """
        Setter for property: (float) CounterBoreDiameter
         Returns the counter bore diameter of the die hole.  
             
         
        """
        pass
    @property
    def CreateWithPad(self) -> bool:
        """
        Getter for property: (bool) CreateWithPad
         Returns the create with pad switch of the die hole, if true a pad will be created around the hole, if false the pad will not be created.  
             
         
        """
        pass
    @CreateWithPad.setter
    def CreateWithPad(self, create_with_pad: bool):
        """
        Setter for property: (bool) CreateWithPad
         Returns the create with pad switch of the die hole, if true a pad will be created around the hole, if false the pad will not be created.  
             
         
        """
        pass
    @property
    def Depth(self) -> float:
        """
        Getter for property: (float) Depth
         Returns the depth of the die hole.  
             
         
        """
        pass
    @Depth.setter
    def Depth(self, depth: float):
        """
        Setter for property: (float) Depth
         Returns the depth of the die hole.  
             
         
        """
        pass
    @property
    def DesignStatus(self) -> bool:
        """
        Getter for property: (bool) DesignStatus
         Returns the design status of the die hole, if true the hole will be built into the model, if false it will not.  
             
         
        """
        pass
    @DesignStatus.setter
    def DesignStatus(self, design_status: bool):
        """
        Setter for property: (bool) DesignStatus
         Returns the design status of the die hole, if true the hole will be built into the model, if false it will not.  
             
         
        """
        pass
    @property
    def Diameter(self) -> float:
        """
        Getter for property: (float) Diameter
         Returns the diameter of the die hole.  
             
         
        """
        pass
    @Diameter.setter
    def Diameter(self, diameter: float):
        """
        Setter for property: (float) Diameter
         Returns the diameter of the die hole.  
             
         
        """
        pass
    @property
    def DisplayHoles(self) -> bool:
        """
        Getter for property: (bool) DisplayHoles
         Returns the display holes switch of the die hole, if true the hole will be built into the model, if false it will not.  
           
                Note that this setting has the same affect as design status, unless the create with pad switch is true.   
         
        """
        pass
    @DisplayHoles.setter
    def DisplayHoles(self, display_holes: bool):
        """
        Setter for property: (bool) DisplayHoles
         Returns the display holes switch of the die hole, if true the hole will be built into the model, if false it will not.  
           
                Note that this setting has the same affect as design status, unless the create with pad switch is true.   
         
        """
        pass
    @property
    def DisplayStatus(self) -> bool:
        """
        Getter for property: (bool) DisplayStatus
         Returns the display status of the die hole, if true input data to the hole will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    @DisplayStatus.setter
    def DisplayStatus(self, display_status: bool):
        """
        Setter for property: (bool) DisplayStatus
         Returns the display status of the die hole, if true input data to the hole will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    @property
    def DropThruDiameter(self) -> float:
        """
        Getter for property: (float) DropThruDiameter
         Returns the drop thru diameter of the die hole.  
             
         
        """
        pass
    @DropThruDiameter.setter
    def DropThruDiameter(self, drop_thru_diameter: float):
        """
        Setter for property: (float) DropThruDiameter
         Returns the drop thru diameter of the die hole.  
             
         
        """
        pass
    @property
    def PadDiameter(self) -> float:
        """
        Getter for property: (float) PadDiameter
         Returns the pad diameter of the die hole.  
             
         
        """
        pass
    @PadDiameter.setter
    def PadDiameter(self, pad_diameter: float):
        """
        Setter for property: (float) PadDiameter
         Returns the pad diameter of the die hole.  
             
         
        """
        pass
    @property
    def PadHeight(self) -> float:
        """
        Getter for property: (float) PadHeight
         Returns the pad height of the die hole.  
             
         
        """
        pass
    @PadHeight.setter
    def PadHeight(self, pad_height: float):
        """
        Setter for property: (float) PadHeight
         Returns the pad height of the die hole.  
             
         
        """
        pass
    @property
    def Plane(self) -> NXOpen.ISurface:
        """
        Getter for property: ( NXOpen.ISurface) Plane
         Returns the plane of the die hole.  
             
         
        """
        pass
    @Plane.setter
    def Plane(self, plane: NXOpen.ISurface):
        """
        Setter for property: ( NXOpen.ISurface) Plane
         Returns the plane of the die hole.  
             
         
        """
        pass
    @property
    def PlaneOffset(self) -> float:
        """
        Getter for property: (float) PlaneOffset
         Returns the plane offset of the die hole.  
             
         
        """
        pass
    @PlaneOffset.setter
    def PlaneOffset(self, plane_offset: float):
        """
        Setter for property: (float) PlaneOffset
         Returns the plane offset of the die hole.  
             
         
        """
        pass
    def GetHoleAttributes(self) -> Tuple[str, str, int, str, str, str]:
        """
         Gets the hole attributes, note existance of attributes depends on usage in
                main feature. 
         Returns A tuple consisting of (title, value, color, diameter_title, depth_title, counter_bore_diameter_title). 
         - title is: str. Title for attribute. .
         - value is: str. Value of attribute. .
         - color is: int. Color of hole faces. .
         - diameter_title is: str. Title for diameter attribute. .
         - depth_title is: str. Title for depth attribute. .
         - counter_bore_diameter_title is: str. Title for counter bore diameter attribute. .

        """
        pass
    def GetPadAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the pad attributes, note existance of attributes depends on usage in
                main feature. 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. Title for attribute. .
         - value is: str. Value of attribute. .
         - color is: int. Color of pad faces. .

        """
        pass
    def SetHoleAttributes(self, title: str, value: str, color: int, diameter_title: str, depth_title: str, counter_bore_diameter_title: str) -> None:
        """
         Sets the hole attributes, note existance of attributes depends on usage in
                main feature. 
        """
        pass
    def SetPadAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the pad attributes, note existance of attributes depends on usage in
                main feature. 
        """
        pass
    def TranslateCenter(self, translate_dist: NXOpen.Vector3d) -> None:
        """
         Translates the center of the die hole by the specified amount. 
        """
        pass
import NXOpen.Features
class HoleParentBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Die Hole Parent sub feature. """
    @property
    def BuildStatus(self) -> DieBuildStatusOption:
        """
        Getter for property: ( DieBuildStatusOption NXOp) BuildStatus
         Returns the build status of die holes.  
             
         
        """
        pass
    @property
    def CounterBoreDiameter(self) -> float:
        """
        Getter for property: (float) CounterBoreDiameter
         Returns the counter bore diameter of die holes.  
             
         
        """
        pass
    @CounterBoreDiameter.setter
    def CounterBoreDiameter(self, counter_bore_diameter: float):
        """
        Setter for property: (float) CounterBoreDiameter
         Returns the counter bore diameter of die holes.  
             
         
        """
        pass
    @property
    def CreateWithPad(self) -> bool:
        """
        Getter for property: (bool) CreateWithPad
         Returns the create with pad switch of die holes, if true a pad will be created around the holes, if false the pad will not be created.  
             
         
        """
        pass
    @CreateWithPad.setter
    def CreateWithPad(self, create_with_pad: bool):
        """
        Setter for property: (bool) CreateWithPad
         Returns the create with pad switch of die holes, if true a pad will be created around the holes, if false the pad will not be created.  
             
         
        """
        pass
    @property
    def Depth(self) -> float:
        """
        Getter for property: (float) Depth
         Returns the depth of die holes.  
             
         
        """
        pass
    @Depth.setter
    def Depth(self, depth: float):
        """
        Setter for property: (float) Depth
         Returns the depth of die holes.  
             
         
        """
        pass
    @property
    def DesignStatus(self) -> bool:
        """
        Getter for property: (bool) DesignStatus
         Returns the design status of die holes, if true the holes will be built into the model, if false they will not.  
             
         
        """
        pass
    @DesignStatus.setter
    def DesignStatus(self, design_status: bool):
        """
        Setter for property: (bool) DesignStatus
         Returns the design status of die holes, if true the holes will be built into the model, if false they will not.  
             
         
        """
        pass
    @property
    def Diameter(self) -> float:
        """
        Getter for property: (float) Diameter
         Returns the diameter of die holes.  
             
         
        """
        pass
    @Diameter.setter
    def Diameter(self, diameter: float):
        """
        Setter for property: (float) Diameter
         Returns the diameter of die holes.  
             
         
        """
        pass
    @property
    def DisplayHoles(self) -> bool:
        """
        Getter for property: (bool) DisplayHoles
         Returns the display holes switch of die holes, if true the holes will be built into the model, if false they will not.  
           
                Note that this setting has the same affect as design status, unless the create with pad switch is true.   
         
        """
        pass
    @DisplayHoles.setter
    def DisplayHoles(self, display_holes: bool):
        """
        Setter for property: (bool) DisplayHoles
         Returns the display holes switch of die holes, if true the holes will be built into the model, if false they will not.  
           
                Note that this setting has the same affect as design status, unless the create with pad switch is true.   
         
        """
        pass
    @property
    def DisplayStatus(self) -> bool:
        """
        Getter for property: (bool) DisplayStatus
         Returns the display status of die holes, if true input data to the holes will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    @DisplayStatus.setter
    def DisplayStatus(self, display_status: bool):
        """
        Setter for property: (bool) DisplayStatus
         Returns the display status of die holes, if true input data to the holes will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    @property
    def DropThruDiameter(self) -> float:
        """
        Getter for property: (float) DropThruDiameter
         Returns the drop thru diameter of die holes.  
             
         
        """
        pass
    @DropThruDiameter.setter
    def DropThruDiameter(self, drop_thru_diameter: float):
        """
        Setter for property: (float) DropThruDiameter
         Returns the drop thru diameter of die holes.  
             
         
        """
        pass
    @property
    def PadDiameter(self) -> float:
        """
        Getter for property: (float) PadDiameter
         Returns the pad diameter of die holes.  
             
         
        """
        pass
    @PadDiameter.setter
    def PadDiameter(self, pad_diameter: float):
        """
        Setter for property: (float) PadDiameter
         Returns the pad diameter of die holes.  
             
         
        """
        pass
    @property
    def PadHeight(self) -> float:
        """
        Getter for property: (float) PadHeight
         Returns the pad height of die holes.  
             
         
        """
        pass
    @PadHeight.setter
    def PadHeight(self, pad_height: float):
        """
        Setter for property: (float) PadHeight
         Returns the pad height of die holes.  
             
         
        """
        pass
    @property
    def PlaneOffset(self) -> float:
        """
        Getter for property: (float) PlaneOffset
         Returns the plane offset of die holes.  
             
         
        """
        pass
    @PlaneOffset.setter
    def PlaneOffset(self, plane_offset: float):
        """
        Setter for property: (float) PlaneOffset
         Returns the plane offset of die holes.  
             
         
        """
        pass
    def CreateChild(self) -> HoleChildBuilder:
        """
         Creates a child hole. 
         Returns dieholechild ( HoleChildBuilder NXOp):  .
        """
        pass
    def DeleteChild(self, dieholechild: HoleChildBuilder) -> None:
        """
         Deletes a child hole. 
        """
        pass
    def GetChildren(self) -> List[HoleChildBuilder]:
        """
         Outputs the child holes. 
         Returns children ( HoleChildBuilder List[NX):  The child holes. .
        """
        pass
    def GetHoleAttributes(self) -> Tuple[str, str, int, str, str, str]:
        """
         Gets the hole attributes, note existance of attributes depends on usage in
                main feature. 
         Returns A tuple consisting of (title, value, color, diameter_title, depth_title, counter_bore_diameter_title). 
         - title is: str. Title for attribute. .
         - value is: str. Value of attribute. .
         - color is: int. Color of hole faces. .
         - diameter_title is: str. Title for diameter attribute. .
         - depth_title is: str. Title for depth attribute. .
         - counter_bore_diameter_title is: str. Title for counter bore diameter attribute. .

        """
        pass
    def GetPadAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the pad attributes, note existance of attributes depends on usage in
                main feature. 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. Title for attribute. .
         - value is: str. Value of attribute. .
         - color is: int. Color of pad faces. .

        """
        pass
    def SetHoleAttributes(self, title: str, value: str, color: int, diameter_title: str, depth_title: str, counter_bore_diameter_title: str) -> None:
        """
         Sets the hole attributes, note existance of attributes depends on usage in
                main feature. 
        """
        pass
    def SetPadAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the pad attributes, note existance of attributes depends on usage in
                main feature. 
        """
        pass
import NXOpen
import NXOpen.Features
class KeywayBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a NXOpen.Die.KeywayBuilder builder
    """
    class LocationType(Enum):
        """
        Members Include: 
         |PositiveX|  +X relative to the center of the coordinate system 
         |NegativeX|  -X relative to the center of the coordinate system 
         |PositiveY|  +Y relative to the center of the coordinate system 
         |NegativeY|  -Y relative to the center of the coordinate system 

        """
        PositiveX: int
        NegativeX: int
        PositiveY: int
        NegativeY: int
        @staticmethod
        def ValueOf(value: int) -> KeywayBuilder.LocationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |Rectangular|  tool runoff is perpendicular to slot 
         |Circular|  tool runoff is created using a plunge cut at the end of the slot 

        """
        Rectangular: int
        Circular: int
        @staticmethod
        def ValueOf(value: int) -> KeywayBuilder.Types:
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
    def BaseFlange(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) BaseFlange
         Returns the closed loop section representing the base flange   
            
         
        """
        pass
    @property
    def BaseOrientation(self) -> DiePlaneBuilder:
        """
        Getter for property: ( DiePlaneBuilder NXOp) BaseOrientation
         Returns the bottom orientation plane of the keyway pad   
            
         
        """
        pass
    @property
    def CreateWithPad(self) -> bool:
        """
        Getter for property: (bool) CreateWithPad
         Returns the value, true or false) to decide if the pad should be created for the keyway   
            
         
        """
        pass
    @CreateWithPad.setter
    def CreateWithPad(self, createWithPad: bool):
        """
        Setter for property: (bool) CreateWithPad
         Returns the value, true or false) to decide if the pad should be created for the keyway   
            
         
        """
        pass
    @property
    def DeckThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DeckThickness
         Returns the expression for the deck thickness   
            
         
        """
        pass
    @property
    def DieCenterlineCoordinateSystem(self) -> NXOpen.SelectCartesianCoordinateSystem:
        """
        Getter for property: ( NXOpen.SelectCartesianCoordinateSystem) DieCenterlineCoordinateSystem
         Returns the die centerline coordinate system for orienting the keyway   
            
         
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
    def InteriorProfile(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) InteriorProfile
         Returns the closed loop section representing the interior profile of the casting   
            
         
        """
        pass
    @property
    def Location(self) -> KeywayBuilder.LocationType:
        """
        Getter for property: ( KeywayBuilder.LocationType NXOp) Location
         Returns the location for the keyway   
            
         
        """
        pass
    @Location.setter
    def Location(self, location: KeywayBuilder.LocationType):
        """
        Setter for property: ( KeywayBuilder.LocationType NXOp) Location
         Returns the location for the keyway   
            
         
        """
        pass
    @property
    def MinimumRibHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumRibHeight
         Returns the expression for the minimum rib height   
            
         
        """
        pass
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Offset
         Returns the amount to offset the keyway perpendicular to the slot orientation   
            
         
        """
        pass
    @property
    def PadAttributes(self) -> DieAttributesBuilder:
        """
        Getter for property: ( DieAttributesBuilder NXOp) PadAttributes
         Returns the pad attributes   
            
         
        """
        pass
    @property
    def PadHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PadHeight
         Returns the expression for the pad height   
            
         
        """
        pass
    @property
    def PadWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PadWidth
         Returns the expression for the pad width   
            
         
        """
        pass
    @property
    def PlacementOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PlacementOffset
         Returns the amount to offset the base orientation   
            
         
        """
        pass
    @property
    def RunoffDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RunoffDepth
         Returns the expression for the runoff depth   
            
         
        """
        pass
    @property
    def RunoffLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RunoffLength
         Returns the expression for the runoff length   
            
         
        """
        pass
    @property
    def RunoffRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RunoffRadius
         Returns the expression for the runoff radius   
            
         
        """
        pass
    @property
    def RunoffWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RunoffWidth
         Returns the expression for the runoff width   
            
         
        """
        pass
    @property
    def SheetMetal(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) SheetMetal
         Returns the sheet metal being formed by the casting.  
           Used to measure the height.   
         
        """
        pass
    @property
    def SlotAttributes(self) -> DieAttributesBuilder:
        """
        Getter for property: ( DieAttributesBuilder NXOp) SlotAttributes
         Returns the slot attributes   
            
         
        """
        pass
    @property
    def SlotDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SlotDepth
         Returns the expression for the slot depth   
            
         
        """
        pass
    @property
    def SlotLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SlotLength
         Returns the expression for the slot length   
            
         
        """
        pass
    @property
    def SlotWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SlotWidth
         Returns the expression for the slot width   
            
         
        """
        pass
    @property
    def Target(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) Target
         Returns the target solid the keyway will be united with   
            
         
        """
        pass
    @property
    def Type(self) -> KeywayBuilder.Types:
        """
        Getter for property: ( KeywayBuilder.Types NXOp) Type
         Returns the type of the keyway runoff   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: KeywayBuilder.Types):
        """
        Setter for property: ( KeywayBuilder.Types NXOp) Type
         Returns the type of the keyway runoff   
            
         
        """
        pass
import NXOpen
import NXOpen.Features
class KeywayChildBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Die Keyway Child sub feature. """
    class LocationOption(Enum):
        """
        Members Include: 
         |PositiveX|  Keyway built in positive x direction. 
         |NegativeX|  Keyway built in negative x direction. 
         |PositiveY|  Keyway built in positive y direction. 
         |NegativeY|  Keyway built in negative y direction. 

        """
        PositiveX: int
        NegativeX: int
        PositiveY: int
        NegativeY: int
        @staticmethod
        def ValueOf(value: int) -> KeywayChildBuilder.LocationOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RunoffTypeOption(Enum):
        """
        Members Include: 
         |Rectangular|  Rectangular runoff. 
         |Circular|  Circular runoff. 

        """
        Rectangular: int
        Circular: int
        @staticmethod
        def ValueOf(value: int) -> KeywayChildBuilder.RunoffTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BuildStatus(self) -> DieBuildStatusOption:
        """
        Getter for property: ( DieBuildStatusOption NXOp) BuildStatus
         Returns the build status of the keyway.  
             
         
        """
        pass
    @property
    def Depth(self) -> float:
        """
        Getter for property: (float) Depth
         Returns the depth of the keyway.  
             
         
        """
        pass
    @Depth.setter
    def Depth(self, depth: float):
        """
        Setter for property: (float) Depth
         Returns the depth of the keyway.  
             
         
        """
        pass
    @property
    def DesignStatus(self) -> bool:
        """
        Getter for property: (bool) DesignStatus
         Returns the design status of the keyway, if true the keyway will be built into the model, if false it will not.  
             
         
        """
        pass
    @DesignStatus.setter
    def DesignStatus(self, design_status: bool):
        """
        Setter for property: (bool) DesignStatus
         Returns the design status of the keyway, if true the keyway will be built into the model, if false it will not.  
             
         
        """
        pass
    @property
    def DisplayStatus(self) -> bool:
        """
        Getter for property: (bool) DisplayStatus
         Returns the display status of the keyway, if true input data to the keyway will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    @DisplayStatus.setter
    def DisplayStatus(self, display_status: bool):
        """
        Setter for property: (bool) DisplayStatus
         Returns the display status of the keyway, if true input data to the keyway will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    @property
    def Length(self) -> float:
        """
        Getter for property: (float) Length
         Returns the length of the keyway.  
             
         
        """
        pass
    @Length.setter
    def Length(self, length: float):
        """
        Setter for property: (float) Length
         Returns the length of the keyway.  
             
         
        """
        pass
    @property
    def Location(self) -> KeywayChildBuilder.LocationOption:
        """
        Getter for property: ( KeywayChildBuilder.LocationOption NXOp) Location
         Returns the location of the keyway.  
             
         
        """
        pass
    @Location.setter
    def Location(self, location: KeywayChildBuilder.LocationOption):
        """
        Setter for property: ( KeywayChildBuilder.LocationOption NXOp) Location
         Returns the location of the keyway.  
             
         
        """
        pass
    @property
    def MinimumRibHeight(self) -> float:
        """
        Getter for property: (float) MinimumRibHeight
         Returns the minimum rib height of the keyway.  
             
         
        """
        pass
    @MinimumRibHeight.setter
    def MinimumRibHeight(self, minimum_rib_height: float):
        """
        Setter for property: (float) MinimumRibHeight
         Returns the minimum rib height of the keyway.  
             
         
        """
        pass
    @property
    def Offset(self) -> float:
        """
        Getter for property: (float) Offset
         Returns the offset of the keyway.  
             
         
        """
        pass
    @Offset.setter
    def Offset(self, offset: float):
        """
        Setter for property: (float) Offset
         Returns the offset of the keyway.  
             
         
        """
        pass
    @property
    def PadHeight(self) -> float:
        """
        Getter for property: (float) PadHeight
         Returns the pad height of the keyway.  
             
         
        """
        pass
    @PadHeight.setter
    def PadHeight(self, pad_height: float):
        """
        Setter for property: (float) PadHeight
         Returns the pad height of the keyway.  
             
         
        """
        pass
    @property
    def PadWidth(self) -> float:
        """
        Getter for property: (float) PadWidth
         Returns the pad width of the keyway.  
             
         
        """
        pass
    @PadWidth.setter
    def PadWidth(self, pad_width: float):
        """
        Setter for property: (float) PadWidth
         Returns the pad width of the keyway.  
             
         
        """
        pass
    @property
    def PlacementOffset(self) -> float:
        """
        Getter for property: (float) PlacementOffset
         Returns the placement offset of the keyway.  
             
         
        """
        pass
    @PlacementOffset.setter
    def PlacementOffset(self, placement_offset: float):
        """
        Setter for property: (float) PlacementOffset
         Returns the placement offset of the keyway.  
             
         
        """
        pass
    @property
    def Plane(self) -> NXOpen.IOrientation:
        """
        Getter for property: ( NXOpen.IOrientation) Plane
         Returns the plane of the keyway.  
             
         
        """
        pass
    @Plane.setter
    def Plane(self, plane: NXOpen.IOrientation):
        """
        Setter for property: ( NXOpen.IOrientation) Plane
         Returns the plane of the keyway.  
             
         
        """
        pass
    @property
    def ReverseOrientation(self) -> bool:
        """
        Getter for property: (bool) ReverseOrientation
         Returns the value to reverse the orientation of the orientation plane,
             if true the keyway orientation normal will be reversed,
             if false it will not.  
             
         
        """
        pass
    @ReverseOrientation.setter
    def ReverseOrientation(self, reverse_orientation: bool):
        """
        Setter for property: (bool) ReverseOrientation
         Returns the value to reverse the orientation of the orientation plane,
             if true the keyway orientation normal will be reversed,
             if false it will not.  
             
         
        """
        pass
    @property
    def RunoffDepth(self) -> float:
        """
        Getter for property: (float) RunoffDepth
         Returns the runoff depth of the keyway.  
             
         
        """
        pass
    @RunoffDepth.setter
    def RunoffDepth(self, runoff_depth: float):
        """
        Setter for property: (float) RunoffDepth
         Returns the runoff depth of the keyway.  
             
         
        """
        pass
    @property
    def RunoffDiameter(self) -> float:
        """
        Getter for property: (float) RunoffDiameter
         Returns the runoff diameter of the keyway.  
             
         
        """
        pass
    @RunoffDiameter.setter
    def RunoffDiameter(self, runoff_diameter: float):
        """
        Setter for property: (float) RunoffDiameter
         Returns the runoff diameter of the keyway.  
             
         
        """
        pass
    @property
    def RunoffLength(self) -> float:
        """
        Getter for property: (float) RunoffLength
         Returns the runoff length of the keyway.  
             
         
        """
        pass
    @RunoffLength.setter
    def RunoffLength(self, runoff_length: float):
        """
        Setter for property: (float) RunoffLength
         Returns the runoff length of the keyway.  
             
         
        """
        pass
    @property
    def RunoffType(self) -> KeywayChildBuilder.RunoffTypeOption:
        """
        Getter for property: ( KeywayChildBuilder.RunoffTypeOption NXOp) RunoffType
         Returns the runoff type of the keyway.  
             
         
        """
        pass
    @RunoffType.setter
    def RunoffType(self, runoff_type: KeywayChildBuilder.RunoffTypeOption):
        """
        Setter for property: ( KeywayChildBuilder.RunoffTypeOption NXOp) RunoffType
         Returns the runoff type of the keyway.  
             
         
        """
        pass
    @property
    def RunoffWidth(self) -> float:
        """
        Getter for property: (float) RunoffWidth
         Returns the runoff width of the keyway.  
             
         
        """
        pass
    @RunoffWidth.setter
    def RunoffWidth(self, runoff_width: float):
        """
        Setter for property: (float) RunoffWidth
         Returns the runoff width of the keyway.  
             
         
        """
        pass
    @property
    def Width(self) -> float:
        """
        Getter for property: (float) Width
         Returns the width of the keyway.  
             
         
        """
        pass
    @Width.setter
    def Width(self, width: float):
        """
        Setter for property: (float) Width
         Returns the width of the keyway.  
             
         
        """
        pass
    def GetPadAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the pad attributes, note existance of attributes depends on usage in
                main feature. 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. Title for attribute. .
         - value is: str. Value of attribute. .
         - color is: int. Color of pad faces. .

        """
        pass
    def GetSlotAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the slot attributes, note existance of attributes depends on usage in
                main feature. 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. Title for attribute. .
         - value is: str. Value of attribute. .
         - color is: int. Color of slot faces. .

        """
        pass
    def SetPadAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the pad attributes, note existance of attributes depends on usage in
                main feature. 
        """
        pass
    def SetSlotAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the slot attributes, note existance of attributes depends on usage in
                main feature. 
        """
        pass
import NXOpen.Features
class KeywayParentBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Die Keyway Parent sub feature. """
    class RunoffTypeOption(Enum):
        """
        Members Include: 
         |Rectangular|  Rectangular runoff. 
         |Circular|  Circular runoff. 

        """
        Rectangular: int
        Circular: int
        @staticmethod
        def ValueOf(value: int) -> KeywayParentBuilder.RunoffTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BuildStatus(self) -> DieBuildStatusOption:
        """
        Getter for property: ( DieBuildStatusOption NXOp) BuildStatus
         Returns the build status of keyways.  
             
         
        """
        pass
    @property
    def Depth(self) -> float:
        """
        Getter for property: (float) Depth
         Returns the depth of keyways.  
             
         
        """
        pass
    @Depth.setter
    def Depth(self, depth: float):
        """
        Setter for property: (float) Depth
         Returns the depth of keyways.  
             
         
        """
        pass
    @property
    def DesignStatus(self) -> bool:
        """
        Getter for property: (bool) DesignStatus
         Returns the design status of keyways, if true the keyways will be built into the model, if false they will not.  
             
         
        """
        pass
    @DesignStatus.setter
    def DesignStatus(self, design_status: bool):
        """
        Setter for property: (bool) DesignStatus
         Returns the design status of keyways, if true the keyways will be built into the model, if false they will not.  
             
         
        """
        pass
    @property
    def DisplayStatus(self) -> bool:
        """
        Getter for property: (bool) DisplayStatus
         Returns the display status of keyways, if true input data to the keyways will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    @DisplayStatus.setter
    def DisplayStatus(self, display_status: bool):
        """
        Setter for property: (bool) DisplayStatus
         Returns the display status of keyways, if true input data to the keyways will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    @property
    def Length(self) -> float:
        """
        Getter for property: (float) Length
         Returns the length of keyways.  
             
         
        """
        pass
    @Length.setter
    def Length(self, length: float):
        """
        Setter for property: (float) Length
         Returns the length of keyways.  
             
         
        """
        pass
    @property
    def MinimumRibHeight(self) -> float:
        """
        Getter for property: (float) MinimumRibHeight
         Returns the minimum rib height of keyways.  
             
         
        """
        pass
    @MinimumRibHeight.setter
    def MinimumRibHeight(self, minimum_rib_height: float):
        """
        Setter for property: (float) MinimumRibHeight
         Returns the minimum rib height of keyways.  
             
         
        """
        pass
    @property
    def PadHeight(self) -> float:
        """
        Getter for property: (float) PadHeight
         Returns the pad height of keyways.  
             
         
        """
        pass
    @PadHeight.setter
    def PadHeight(self, pad_height: float):
        """
        Setter for property: (float) PadHeight
         Returns the pad height of keyways.  
             
         
        """
        pass
    @property
    def PadWidth(self) -> float:
        """
        Getter for property: (float) PadWidth
         Returns the pad width of keyways.  
             
         
        """
        pass
    @PadWidth.setter
    def PadWidth(self, pad_width: float):
        """
        Setter for property: (float) PadWidth
         Returns the pad width of keyways.  
             
         
        """
        pass
    @property
    def PlacementOffset(self) -> float:
        """
        Getter for property: (float) PlacementOffset
         Returns the placement offset of keyways.  
             
         
        """
        pass
    @PlacementOffset.setter
    def PlacementOffset(self, placement_offset: float):
        """
        Setter for property: (float) PlacementOffset
         Returns the placement offset of keyways.  
             
         
        """
        pass
    @property
    def RunoffDepth(self) -> float:
        """
        Getter for property: (float) RunoffDepth
         Returns the runoff depth of keyways.  
             
         
        """
        pass
    @RunoffDepth.setter
    def RunoffDepth(self, runoff_depth: float):
        """
        Setter for property: (float) RunoffDepth
         Returns the runoff depth of keyways.  
             
         
        """
        pass
    @property
    def RunoffDiameter(self) -> float:
        """
        Getter for property: (float) RunoffDiameter
         Returns the runoff diameter of keyways.  
             
         
        """
        pass
    @RunoffDiameter.setter
    def RunoffDiameter(self, runoff_diameter: float):
        """
        Setter for property: (float) RunoffDiameter
         Returns the runoff diameter of keyways.  
             
         
        """
        pass
    @property
    def RunoffLength(self) -> float:
        """
        Getter for property: (float) RunoffLength
         Returns the runoff length of keyways.  
             
         
        """
        pass
    @RunoffLength.setter
    def RunoffLength(self, runoff_length: float):
        """
        Setter for property: (float) RunoffLength
         Returns the runoff length of keyways.  
             
         
        """
        pass
    @property
    def RunoffType(self) -> KeywayParentBuilder.RunoffTypeOption:
        """
        Getter for property: ( KeywayParentBuilder.RunoffTypeOption NXOp) RunoffType
         Returns the runoff type of keyways.  
             
         
        """
        pass
    @RunoffType.setter
    def RunoffType(self, runoff_type: KeywayParentBuilder.RunoffTypeOption):
        """
        Setter for property: ( KeywayParentBuilder.RunoffTypeOption NXOp) RunoffType
         Returns the runoff type of keyways.  
             
         
        """
        pass
    @property
    def RunoffWidth(self) -> float:
        """
        Getter for property: (float) RunoffWidth
         Returns the runoff width of keyways.  
             
         
        """
        pass
    @RunoffWidth.setter
    def RunoffWidth(self, runoff_width: float):
        """
        Setter for property: (float) RunoffWidth
         Returns the runoff width of keyways.  
             
         
        """
        pass
    @property
    def Width(self) -> float:
        """
        Getter for property: (float) Width
         Returns the width of keyways.  
             
         
        """
        pass
    @Width.setter
    def Width(self, width: float):
        """
        Setter for property: (float) Width
         Returns the width of keyways.  
             
         
        """
        pass
    def CreateChild(self) -> KeywayChildBuilder:
        """
         Creates a child keyway. 
         Returns diekeywaychild ( KeywayChildBuilder NXOp):  .
        """
        pass
    def DeleteChild(self, diekeywaychild: KeywayChildBuilder) -> None:
        """
         Deletes a child keyway. 
        """
        pass
    def GetChildren(self) -> List[KeywayChildBuilder]:
        """
         Outputs the child keyways. 
         Returns children ( KeywayChildBuilder List[NX):  The child keyways. .
        """
        pass
    def GetPadAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the pad attributes, note existance of attributes depends on usage in
                main feature. 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. Title for attribute. .
         - value is: str. Value of attribute. .
         - color is: int. Color of pad faces. .

        """
        pass
    def GetSlotAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the slot attributes, note existance of attributes depends on usage in
                main feature. 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. Title for attribute. .
         - value is: str. Value of attribute. .
         - color is: int. Color of slot faces. .

        """
        pass
    def SetPadAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the pad attributes, note existance of attributes depends on usage in
                main feature. 
        """
        pass
    def SetSlotAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the slot attributes, note existance of attributes depends on usage in
                main feature. 
        """
        pass
import NXOpen.Features
class Keyway(NXOpen.Features.BodyFeature): 
    """ Represents a keyway feature """
    pass
import NXOpen
import NXOpen.Features
class LineupBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Lineup feature builder """
    @property
    def FlowDirection(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) FlowDirection
         Returns the flow direction of the lineup   
            
         
        """
        pass
    @FlowDirection.setter
    def FlowDirection(self, flowDirection: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) FlowDirection
         Returns the flow direction of the lineup   
            
         
        """
        pass
    @property
    def Origin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) Origin
         Returns the origin of the lineup   
            
         
        """
        pass
    @Origin.setter
    def Origin(self, origin: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) Origin
         Returns the origin of the lineup   
            
         
        """
        pass
    @property
    def PressDirection(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) PressDirection
         Returns the press direction of the lineup   
            
         
        """
        pass
    @PressDirection.setter
    def PressDirection(self, pressDirection: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) PressDirection
         Returns the press direction of the lineup   
            
         
        """
        pass
    def GetDetails(self) -> List[str]:
        """
         Gets the detailed description of the lineup 
         Returns strings (List[str]):  detail strings .
        """
        pass
    def GetProductBodies(self) -> List[NXOpen.Body]:
        """
         Gets the product sheet bodies of the lineup 
         Returns objects ( NXOpen.Body Li):  .
        """
        pass
    def SetDetails(self, strings: List[str]) -> None:
        """
         Sets the detailed description of the lineup 
        """
        pass
    def SetProductBodies(self, objects: List[NXOpen.Body]) -> None:
        """
         Sets the product sheet bodies of the lineup 
        """
        pass
import NXOpen
import NXOpen.Features
class MachineReliefBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a builder that is used to create or edit a NXOpen.Die.MachineRelief feature. The builder may generate a Cam Definition, Machine Relief, or Wall Thickness.
    """
    class MainProfileTypes(Enum):
        """
        Members Include: 
         |Exterior|  Profile is for the exterior surface of the main wall. 
         |Interior|  Profile is for the interior surface of the main wall. 

        """
        Exterior: int
        Interior: int
        @staticmethod
        def ValueOf(value: int) -> MachineReliefBuilder.MainProfileTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TrimSheetTypes(Enum):
        """
        Members Include: 
         |Sheet|  Trimming surface is a sheet body. 
         |Face|  Trimming surface is a face, or faces to be sewed together. 

        """
        Sheet: int
        Face: int
        @staticmethod
        def ValueOf(value: int) -> MachineReliefBuilder.TrimSheetTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |Cam|  Add casting material for the trim, or flange, steel mating surface. 
         |Relief|  Remove casting material to allow for clearance between two mating objects (such as the upper and lower castings). 
         |Thicken|  Add casting material to thicken an existing wall. 

        """
        Cam: int
        Relief: int
        Thicken: int
        @staticmethod
        def ValueOf(value: int) -> MachineReliefBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngleTolerance(self) -> float:
        """
        Getter for property: (float) AngleTolerance
         Returns the angle tolerance.  
             
         
        """
        pass
    @AngleTolerance.setter
    def AngleTolerance(self, angleTolerance: float):
        """
        Setter for property: (float) AngleTolerance
         Returns the angle tolerance.  
             
         
        """
        pass
    @property
    def BaseOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BaseOffset
         Returns the expression containing the offset value to apply to the base definition before trimming the base of the tool solids.  
             
         
        """
        pass
    @property
    def BaseOrientation(self) -> DiePlaneBuilder:
        """
        Getter for property: ( DiePlaneBuilder NXOp) BaseOrientation
         Returns the base orientation of the target solid.  
             
         
        """
        pass
    @property
    def BeltAttributes(self) -> DieAttributesBuilder:
        """
        Getter for property: ( DieAttributesBuilder NXOp) BeltAttributes
         Returns the attribute title, value and face color to apply to the belt faces.  
             
         
        """
        pass
    @property
    def BeltFaceThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BeltFaceThickness
         Returns the expression containing the value to apply for the belt face on the cam definition.  
           Only valid when type is  Die::MachineReliefBuilder::TypesCam .   
         
        """
        pass
    @property
    def CamDirection(self) -> DieDirectionBuilder:
        """
        Getter for property: ( DieDirectionBuilder NXOp) CamDirection
         Returns the direction of the cam for trimming.  
           Only valid when type is  Die::MachineReliefBuilder::TypesCam  or  Die::MachineReliefBuilder::TypesRelief .   
         
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
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance.  
             
         
        """
        pass
    @property
    def End(self) -> DieLocationBuilder:
        """
        Getter for property: ( DieLocationBuilder NXOp) End
         Returns the location for the end of the segment definition.  
           The default is the end of the segment if an open profile is selected.   
         
        """
        pass
    @property
    def InsideWallProfile(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) InsideWallProfile
         Returns the wall profile defining the inside of the main wall used for the cam definition.  
           Only valid when type is  Die::MachineReliefBuilder::TypesCam .   
         
        """
        pass
    @property
    def JogWall(self) -> bool:
        """
        Getter for property: (bool) JogWall
         Returns the indicator defining if the wall should be jogged (or changed) to accommodate the cam definition.  
           TRUE indicates that the wal should be jogged.   
         
        """
        pass
    @JogWall.setter
    def JogWall(self, jogWall: bool):
        """
        Setter for property: (bool) JogWall
         Returns the indicator defining if the wall should be jogged (or changed) to accommodate the cam definition.  
           TRUE indicates that the wal should be jogged.   
         
        """
        pass
    @property
    def MainProfile(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) MainProfile
         Returns the primary profile for the machine relief casting.  
             
         
        """
        pass
    @property
    def MainProfileType(self) -> MachineReliefBuilder.MainProfileTypes:
        """
        Getter for property: ( MachineReliefBuilder.MainProfileTypes NXOp) MainProfileType
         Returns the value specifying the main profile for the Thicken operation.  
           Only valid when type is  Die::MachineReliefBuilder::TypesThicken .   
         
        """
        pass
    @MainProfileType.setter
    def MainProfileType(self, mainProfileType: MachineReliefBuilder.MainProfileTypes):
        """
        Setter for property: ( MachineReliefBuilder.MainProfileTypes NXOp) MainProfileType
         Returns the value specifying the main profile for the Thicken operation.  
           Only valid when type is  Die::MachineReliefBuilder::TypesThicken .   
         
        """
        pass
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Offset
         Returns the expression containing the value to apply for the thicken operation to create the tool solid.  
           
                    Only valid when type is  Die::MachineReliefBuilder::TypesRelief  or  Die::MachineReliefBuilder::TypesThicken .   
         
        """
        pass
    @property
    def ProfileOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ProfileOffset
         Returns the expression containing the value to apply to the profile to create the primary head solid for the cam definition.  
           Only valid when type is  Die::MachineReliefBuilder::TypesCam .   
         
        """
        pass
    @property
    def Relief(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Relief
         Returns the expression containing the value to apply for the machine relief operation to create the tool solid.  
           
                    Only valid when type is  Die::MachineReliefBuilder::TypesRelief  or  Die::MachineReliefBuilder::TypesThicken .   
         
        """
        pass
    @property
    def ReliefOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ReliefOffset
         Returns the expression containing the value of the relief around the primary head solid for the cam definition if a wall is created.  
           Only valid when type is  Die::MachineReliefBuilder::TypesCam .   
         
        """
        pass
    @property
    def Start(self) -> DieLocationBuilder:
        """
        Getter for property: ( DieLocationBuilder NXOp) Start
         Returns the location for the start of the segment definition.  
           The default is the start of the segment if an open profile is selected.   
         
        """
        pass
    @property
    def SwitchTrimSide(self) -> bool:
        """
        Getter for property: (bool) SwitchTrimSide
         Returns the indicator if the trim side should be switched from the default for the sheet metal.  
           TRUE indicates that the trim side should be reversed.   
         
        """
        pass
    @SwitchTrimSide.setter
    def SwitchTrimSide(self, switchTrimSide: bool):
        """
        Setter for property: (bool) SwitchTrimSide
         Returns the indicator if the trim side should be switched from the default for the sheet metal.  
           TRUE indicates that the trim side should be reversed.   
         
        """
        pass
    @property
    def Target(self) -> NXOpen.SelectBody:
        """
        Getter for property: ( NXOpen.SelectBody) Target
         Returns the target solid to add or subtract material too.  
             
         
        """
        pass
    @property
    def TopOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TopOffset
         Returns the expression containing the offset value from the base to define the top extent of the internal builds.  
           This value will be defined internally if a target is selected.   
         
        """
        pass
    @property
    def TrimOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TrimOffset
         Returns the expression containing the clearance value to apply at the start and the end of the cam definition to define the primary head solid.  
           Only valid when type is  Die::MachineReliefBuilder::TypesCam .   
         
        """
        pass
    @property
    def TrimSheet(self) -> NXOpen.SelectBody:
        """
        Getter for property: ( NXOpen.SelectBody) TrimSheet
         Returns the sheet body selection for the trim sheet.  
             
         
        """
        pass
    @property
    def TrimSheetFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) TrimSheetFace
         Returns the face selections to define the trim sheet.  
             
         
        """
        pass
    @property
    def TrimSheetOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TrimSheetOffset
         Returns the expression containing the offset value to apply to the trim sheet to construct the tool solids.  
           
                    Only valid when type is  Die::MachineReliefBuilder::TypesRelief  or  Die::MachineReliefBuilder::TypesThicken .   
         
        """
        pass
    @property
    def TrimSheetType(self) -> MachineReliefBuilder.TrimSheetTypes:
        """
        Getter for property: ( MachineReliefBuilder.TrimSheetTypes NXOp) TrimSheetType
         Returns the indicator for how the trim sheet is specified.  
             
         
        """
        pass
    @TrimSheetType.setter
    def TrimSheetType(self, trimSheetType: MachineReliefBuilder.TrimSheetTypes):
        """
        Setter for property: ( MachineReliefBuilder.TrimSheetTypes NXOp) TrimSheetType
         Returns the indicator for how the trim sheet is specified.  
             
         
        """
        pass
    @property
    def Type(self) -> MachineReliefBuilder.Types:
        """
        Getter for property: ( MachineReliefBuilder.Types NXOp) Type
         Returns the value defining the type of build to perform for this tool.  
             
         
        """
        pass
    @Type.setter
    def Type(self, type: MachineReliefBuilder.Types):
        """
        Setter for property: ( MachineReliefBuilder.Types NXOp) Type
         Returns the value defining the type of build to perform for this tool.  
             
         
        """
        pass
    @property
    def WallOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) WallOffset
         Returns the expression containing the offset to apply to the wall to create the wall area for the cam definition.  
           Only valid when type is  Die::MachineReliefBuilder::TypesCam .   
         
        """
        pass
    @property
    def WallThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) WallThickness
         Returns the expression containing the thickness value of the wall for the cam definition.  
           Only valid when type is  Die::MachineReliefBuilder::TypesCam .   
         
        """
        pass
import NXOpen.Features
class MachineRelief(NXOpen.Features.BodyFeature): 
    """ Represents a die design machine relief feature. """
    pass
import NXOpen
import NXOpen.Features
class OutputCurvesBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents an output curves feature builder. """
    class SmoothTypes(Enum):
        """
        Members Include: 
         |NotSet|  No smoothing 
         |Cubic|  Cubic 
         |Quintic|  Quintic 

        """
        NotSet: int
        Cubic: int
        Quintic: int
        @staticmethod
        def ValueOf(value: int) -> OutputCurvesBuilder.SmoothTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TrimCurveCreateTypes(Enum):
        """
        Members Include: 
         |Section|  Section. 
         |Surface|  Surface. 

        """
        Section: int
        Surface: int
        @staticmethod
        def ValueOf(value: int) -> OutputCurvesBuilder.TrimCurveCreateTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TrimCurveTypes(Enum):
        """
        Members Include: 
         |Trim|  Regular trim curve. 
         |Extended|  extended trim curve. 
         |NotSet|  No trim curve. 

        """
        Trim: int
        Extended: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> OutputCurvesBuilder.TrimCurveTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TrimOutputCurveTypes(Enum):
        """
        Members Include: 
         |Geometric|  Geometric. 
         |Corrected|  Corrected. 
         |Both|  Both geometric and corrected. 

        """
        Geometric: int
        Corrected: int
        Both: int
        @staticmethod
        def ValueOf(value: int) -> OutputCurvesBuilder.TrimOutputCurveTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngleTolerance(self) -> float:
        """
        Getter for property: (float) AngleTolerance
         Returns the angle tolerance.  
             
         
        """
        pass
    @AngleTolerance.setter
    def AngleTolerance(self, angle_tolerance: float):
        """
        Setter for property: (float) AngleTolerance
         Returns the angle tolerance.  
             
         
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
    def DistanceTolerance(self, distance_tolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance.  
             
         
        """
        pass
    @property
    def FirstLimitPoint(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) FirstLimitPoint
         Returns the first limit point.  
             
         
        """
        pass
    @FirstLimitPoint.setter
    def FirstLimitPoint(self, first_limit_point: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) FirstLimitPoint
         Returns the first limit point.  
             
         
        """
        pass
    @property
    def LastLimitPoint(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) LastLimitPoint
         Returns the last limit point.  
             
         
        """
        pass
    @LastLimitPoint.setter
    def LastLimitPoint(self, last_limit_point: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) LastLimitPoint
         Returns the last limit point.  
             
         
        """
        pass
    @property
    def OffsetDistance(self) -> float:
        """
        Getter for property: (float) OffsetDistance
         Returns the offset distance   
            
         
        """
        pass
    @OffsetDistance.setter
    def OffsetDistance(self, offset_distance: float):
        """
        Setter for property: (float) OffsetDistance
         Returns the offset distance   
            
         
        """
        pass
    @property
    def ReferenceFeature(self) -> NXOpen.Features.Feature:
        """
        Getter for property: ( NXOpen.Features.Feature) ReferenceFeature
         Returns the reference feature - must be either a die section or form task feature   
            
         
        """
        pass
    @ReferenceFeature.setter
    def ReferenceFeature(self, reference_feature: NXOpen.Features.Feature):
        """
        Setter for property: ( NXOpen.Features.Feature) ReferenceFeature
         Returns the reference feature - must be either a die section or form task feature   
            
         
        """
        pass
    @property
    def ReferencePoint(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) ReferencePoint
         Returns the reference point.  
             
         
        """
        pass
    @ReferencePoint.setter
    def ReferencePoint(self, reference_point: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) ReferencePoint
         Returns the reference point.  
             
         
        """
        pass
    @property
    def SmoothTolerance(self) -> float:
        """
        Getter for property: (float) SmoothTolerance
         Returns the tolerance used for cubic or quintic smoothing.  
             
         
        """
        pass
    @SmoothTolerance.setter
    def SmoothTolerance(self, smooth_tolerance: float):
        """
        Setter for property: (float) SmoothTolerance
         Returns the tolerance used for cubic or quintic smoothing.  
             
         
        """
        pass
    @property
    def SmoothType(self) -> OutputCurvesBuilder.SmoothTypes:
        """
        Getter for property: ( OutputCurvesBuilder.SmoothTypes NXOp) SmoothType
         Returns the smooth type   
            
         
        """
        pass
    @SmoothType.setter
    def SmoothType(self, smooth_type: OutputCurvesBuilder.SmoothTypes):
        """
        Setter for property: ( OutputCurvesBuilder.SmoothTypes NXOp) SmoothType
         Returns the smooth type   
            
         
        """
        pass
    @property
    def TrimCurveCreateType(self) -> OutputCurvesBuilder.TrimCurveCreateTypes:
        """
        Getter for property: ( OutputCurvesBuilder.TrimCurveCreateTypes NXOp) TrimCurveCreateType
         Returns the trim curve creation type   
            
         
        """
        pass
    @TrimCurveCreateType.setter
    def TrimCurveCreateType(self, trim_curve_type: OutputCurvesBuilder.TrimCurveCreateTypes):
        """
        Setter for property: ( OutputCurvesBuilder.TrimCurveCreateTypes NXOp) TrimCurveCreateType
         Returns the trim curve creation type   
            
         
        """
        pass
    @property
    def TrimCurveType(self) -> OutputCurvesBuilder.TrimCurveTypes:
        """
        Getter for property: ( OutputCurvesBuilder.TrimCurveTypes NXOp) TrimCurveType
         Returns the trim curve type.  
            Needs to be set before reference point   
         
        """
        pass
    @TrimCurveType.setter
    def TrimCurveType(self, trim_curve_type: OutputCurvesBuilder.TrimCurveTypes):
        """
        Setter for property: ( OutputCurvesBuilder.TrimCurveTypes NXOp) TrimCurveType
         Returns the trim curve type.  
            Needs to be set before reference point   
         
        """
        pass
    @property
    def TrimOutputCurveType(self) -> OutputCurvesBuilder.TrimOutputCurveTypes:
        """
        Getter for property: ( OutputCurvesBuilder.TrimOutputCurveTypes NXOp) TrimOutputCurveType
         Returns the trim curve output type   
            
         
        """
        pass
    @TrimOutputCurveType.setter
    def TrimOutputCurveType(self, trim_curve_output_type: OutputCurvesBuilder.TrimOutputCurveTypes):
        """
        Setter for property: ( OutputCurvesBuilder.TrimOutputCurveTypes NXOp) TrimOutputCurveType
         Returns the trim curve output type   
            
         
        """
        pass
    def CreateNonAssociative(self) -> List[NXOpen.ICurve]:
        """
         Creates the output curve without a feature. 
         Returns curves ( NXOpen.ICurve Li):  output curves .
        """
        pass
import NXOpen
import NXOpen.Features
class PadChildBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Die Pad Child sub feature. """
    class ShapeTypeOption(Enum):
        """
        Members Include: 
         |Rectangular|  Rectangular pad. 
         |Circular|  Circular pad. 
         |Curve|  Curve defined pad. 

        """
        Rectangular: int
        Circular: int
        Curve: int
        @staticmethod
        def ValueOf(value: int) -> PadChildBuilder.ShapeTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BuildStatus(self) -> DieBuildStatusOption:
        """
        Getter for property: ( DieBuildStatusOption NXOp) BuildStatus
         Returns the build status of the die pad.  
             
         
        """
        pass
    @property
    def CenterHole(self) -> bool:
        """
        Getter for property: (bool) CenterHole
         Returns the center hole switch of the die pad, if true the center hole will be created in the pad, if false it will not.  
             
         
        """
        pass
    @CenterHole.setter
    def CenterHole(self, center_hole: bool):
        """
        Setter for property: (bool) CenterHole
         Returns the center hole switch of the die pad, if true the center hole will be created in the pad, if false it will not.  
             
         
        """
        pass
    @property
    def DesignStatus(self) -> bool:
        """
        Getter for property: (bool) DesignStatus
         Returns the design status of the die pad, if true the pad will be built into the model, if false it will not.  
             
         
        """
        pass
    @DesignStatus.setter
    def DesignStatus(self, design_status: bool):
        """
        Setter for property: (bool) DesignStatus
         Returns the design status of the die pad, if true the pad will be built into the model, if false it will not.  
             
         
        """
        pass
    @property
    def Diameter(self) -> float:
        """
        Getter for property: (float) Diameter
         Returns the diameter of the die pad.  
             
         
        """
        pass
    @Diameter.setter
    def Diameter(self, diameter: float):
        """
        Setter for property: (float) Diameter
         Returns the diameter of the die pad.  
             
         
        """
        pass
    @property
    def DisplayStatus(self) -> bool:
        """
        Getter for property: (bool) DisplayStatus
         Returns the display status of the die pad, if true input data to the pad will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    @DisplayStatus.setter
    def DisplayStatus(self, display_status: bool):
        """
        Setter for property: (bool) DisplayStatus
         Returns the display status of the die pad, if true input data to the pad will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    @property
    def Height(self) -> float:
        """
        Getter for property: (float) Height
         Returns the height of the die pad.  
             
         
        """
        pass
    @Height.setter
    def Height(self, height: float):
        """
        Setter for property: (float) Height
         Returns the height of the die pad.  
             
         
        """
        pass
    @property
    def HoleDiameter(self) -> float:
        """
        Getter for property: (float) HoleDiameter
         Returns the hole diameter of the die pad.  
             
         
        """
        pass
    @HoleDiameter.setter
    def HoleDiameter(self, hole_diameter: float):
        """
        Setter for property: (float) HoleDiameter
         Returns the hole diameter of the die pad.  
             
         
        """
        pass
    @property
    def Length(self) -> float:
        """
        Getter for property: (float) Length
         Returns the length of the die pad.  
             
         
        """
        pass
    @Length.setter
    def Length(self, length: float):
        """
        Setter for property: (float) Length
         Returns the length of the die pad.  
             
         
        """
        pass
    @property
    def LimitingSurface(self) -> NXOpen.IOrientation:
        """
        Getter for property: ( NXOpen.IOrientation) LimitingSurface
         Returns the limiting surface of the die pad.  
             
         
        """
        pass
    @LimitingSurface.setter
    def LimitingSurface(self, limiting_surface: NXOpen.IOrientation):
        """
        Setter for property: ( NXOpen.IOrientation) LimitingSurface
         Returns the limiting surface of the die pad.  
             
         
        """
        pass
    @property
    def Location(self) -> NXOpen.ILocation:
        """
        Getter for property: ( NXOpen.ILocation) Location
         Returns the location of the die pad.  
             
         
        """
        pass
    @Location.setter
    def Location(self, location: NXOpen.ILocation):
        """
        Setter for property: ( NXOpen.ILocation) Location
         Returns the location of the die pad.  
             
         
        """
        pass
    @property
    def LocationOffset(self) -> float:
        """
        Getter for property: (float) LocationOffset
         Returns the location offset of the die pad.  
             
         
        """
        pass
    @LocationOffset.setter
    def LocationOffset(self, location_offset: float):
        """
        Setter for property: (float) LocationOffset
         Returns the location offset of the die pad.  
             
         
        """
        pass
    @property
    def LocationOffsetDirection(self) -> NXOpen.IReferenceAxis:
        """
        Getter for property: ( NXOpen.IReferenceAxis) LocationOffsetDirection
         Returns the location offset direction of the die pad.  
             
         
        """
        pass
    @LocationOffsetDirection.setter
    def LocationOffsetDirection(self, location_offset_direction: NXOpen.IReferenceAxis):
        """
        Setter for property: ( NXOpen.IReferenceAxis) LocationOffsetDirection
         Returns the location offset direction of the die pad.  
             
         
        """
        pass
    @property
    def OrientationPlane(self) -> NXOpen.IOrientation:
        """
        Getter for property: ( NXOpen.IOrientation) OrientationPlane
         Returns the orientation plane of the die pad.  
             
         
        """
        pass
    @OrientationPlane.setter
    def OrientationPlane(self, orientation_plane: NXOpen.IOrientation):
        """
        Setter for property: ( NXOpen.IOrientation) OrientationPlane
         Returns the orientation plane of the die pad.  
             
         
        """
        pass
    @property
    def Relief(self) -> bool:
        """
        Getter for property: (bool) Relief
         Returns the relief switch of the die pad, if true the relief will be built around the pad, if false it will not.  
             
         
        """
        pass
    @Relief.setter
    def Relief(self, relief: bool):
        """
        Setter for property: (bool) Relief
         Returns the relief switch of the die pad, if true the relief will be built around the pad, if false it will not.  
             
         
        """
        pass
    @property
    def ReliefDepth(self) -> float:
        """
        Getter for property: (float) ReliefDepth
         Returns the relief depth of the die pad.  
             
         
        """
        pass
    @ReliefDepth.setter
    def ReliefDepth(self, relief_depth: float):
        """
        Setter for property: (float) ReliefDepth
         Returns the relief depth of the die pad.  
             
         
        """
        pass
    @property
    def ReliefWidth(self) -> float:
        """
        Getter for property: (float) ReliefWidth
         Returns the relief width of the die pad.  
             
         
        """
        pass
    @ReliefWidth.setter
    def ReliefWidth(self, relief_width: float):
        """
        Setter for property: (float) ReliefWidth
         Returns the relief width of the die pad.  
             
         
        """
        pass
    @property
    def ReverseOrientation(self) -> bool:
        """
        Getter for property: (bool) ReverseOrientation
         Returns the value to reverse the orientation of the orientation plane,
             if true the pad orientation normal will be reversed,
             if false it will not.  
             
         
        """
        pass
    @ReverseOrientation.setter
    def ReverseOrientation(self, reverse_orientation: bool):
        """
        Setter for property: (bool) ReverseOrientation
         Returns the value to reverse the orientation of the orientation plane,
             if true the pad orientation normal will be reversed,
             if false it will not.  
             
         
        """
        pass
    @property
    def ShapeType(self) -> PadChildBuilder.ShapeTypeOption:
        """
        Getter for property: ( PadChildBuilder.ShapeTypeOption NXOp) ShapeType
         Returns the shape type of the die pad.  
             
         
        """
        pass
    @ShapeType.setter
    def ShapeType(self, shape_type: PadChildBuilder.ShapeTypeOption):
        """
        Setter for property: ( PadChildBuilder.ShapeTypeOption NXOp) ShapeType
         Returns the shape type of the die pad.  
             
         
        """
        pass
    @property
    def SurfaceOffset(self) -> float:
        """
        Getter for property: (float) SurfaceOffset
         Returns the surface offset of the die pad.  
             
         
        """
        pass
    @SurfaceOffset.setter
    def SurfaceOffset(self, surface_offset: float):
        """
        Setter for property: (float) SurfaceOffset
         Returns the surface offset of the die pad.  
             
         
        """
        pass
    @property
    def Width(self) -> float:
        """
        Getter for property: (float) Width
         Returns the width of the die pad.  
             
         
        """
        pass
    @Width.setter
    def Width(self, width: float):
        """
        Setter for property: (float) Width
         Returns the width of the die pad.  
             
         
        """
        pass
    def GetHoleAttributes(self) -> Tuple[str, str, int, str]:
        """
         Gets the hole attributes, note existance of attributes depends on usage in
                main feature. 
         Returns A tuple consisting of (title, value, color, diameter_title). 
         - title is: str. Title for attribute. .
         - value is: str. Value of attribute. .
         - color is: int. Color of hole faces. .
         - diameter_title is: str. Title for diameter attribute. .

        """
        pass
    def GetHoleCenters(self) -> List[NXOpen.Point]:
        """
         Gets the hole centers of the die pad. 
         Returns holes ( NXOpen.Point Li):  The hole centers. .
        """
        pass
    def GetPadAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the pad attributes, note existance of attributes depends on usage in
                main feature. 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. Title for attribute. .
         - value is: str. Value of attribute. .
         - color is: int. Color of pad faces. .

        """
        pass
    def GetReliefAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the relief attributes, note existance of attributes depends on usage in
                main feature. 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. Title for attribute. .
         - value is: str. Value of attribute. .
         - color is: int. Color of relief faces. .

        """
        pass
    def GetShape(self) -> Tuple[List[NXOpen.IProfile], DirectionOption]:
        """
         Gets the shape profile of the die pads. 
         Returns A tuple consisting of (profile_entries, direction). 
         - profile_entries is:  NXOpen.IProfile Li. The profile entries, will be curves, edges, faces, sketches or curve features. .
         - direction is:  DirectionOption NXOp. Profile direction. .

        """
        pass
    def SetHoleAttributes(self, title: str, value: str, color: int, diameter_title: str) -> None:
        """
         Sets the hole attributes, note existance of attributes depends on usage in
                main feature. 
        """
        pass
    def SetHoleCenters(self, holes: List[NXOpen.Point]) -> None:
        """
         Sets the hole centers of the die pad. 
        """
        pass
    def SetPadAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the pad attributes, note existance of attributes depends on usage in
                main feature. 
        """
        pass
    def SetReliefAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the relief attributes, note existance of attributes depends on usage in
                main feature. 
        """
        pass
    def SetShape(self, direction: DirectionOption, profile_entries: List[NXOpen.IProfile]) -> None:
        """
         Sets the shape profile of the die pad. 
        """
        pass
    def TranslateLocation(self, translate_dist: NXOpen.Vector3d) -> None:
        """
         Translates the location of the die pad by the specified amount. 
        """
        pass
import NXOpen.Features
class PadParentBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Die Pad Parent sub feature. """
    class ShapeTypeOption(Enum):
        """
        Members Include: 
         |Rectangular|  Rectangular pad. 
         |Circular|  Circular pad. 
         |Curve|  Curve defined pad. 

        """
        Rectangular: int
        Circular: int
        Curve: int
        @staticmethod
        def ValueOf(value: int) -> PadParentBuilder.ShapeTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BuildStatus(self) -> DieBuildStatusOption:
        """
        Getter for property: ( DieBuildStatusOption NXOp) BuildStatus
         Returns the build status of die pads.  
             
         
        """
        pass
    @property
    def CenterHole(self) -> bool:
        """
        Getter for property: (bool) CenterHole
         Returns the center hole switch of die pads, if true the center hole will be created in the pads, if false they will not.  
             
         
        """
        pass
    @CenterHole.setter
    def CenterHole(self, center_hole: bool):
        """
        Setter for property: (bool) CenterHole
         Returns the center hole switch of die pads, if true the center hole will be created in the pads, if false they will not.  
             
         
        """
        pass
    @property
    def DesignStatus(self) -> bool:
        """
        Getter for property: (bool) DesignStatus
         Returns the design status of die pads, if true the pads will be built into the model, if false they will not.  
             
         
        """
        pass
    @DesignStatus.setter
    def DesignStatus(self, design_status: bool):
        """
        Setter for property: (bool) DesignStatus
         Returns the design status of die pads, if true the pads will be built into the model, if false they will not.  
             
         
        """
        pass
    @property
    def Diameter(self) -> float:
        """
        Getter for property: (float) Diameter
         Returns the diameter of die pads.  
             
         
        """
        pass
    @Diameter.setter
    def Diameter(self, diameter: float):
        """
        Setter for property: (float) Diameter
         Returns the diameter of die pads.  
             
         
        """
        pass
    @property
    def DisplayStatus(self) -> bool:
        """
        Getter for property: (bool) DisplayStatus
         Returns the display status of die pads, if true input data to the pads will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    @DisplayStatus.setter
    def DisplayStatus(self, display_status: bool):
        """
        Setter for property: (bool) DisplayStatus
         Returns the display status of die pads, if true input data to the pads will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    @property
    def Height(self) -> float:
        """
        Getter for property: (float) Height
         Returns the height of die pads.  
             
         
        """
        pass
    @Height.setter
    def Height(self, height: float):
        """
        Setter for property: (float) Height
         Returns the height of die pads.  
             
         
        """
        pass
    @property
    def HoleDiameter(self) -> float:
        """
        Getter for property: (float) HoleDiameter
         Returns the hole diameter of die pads.  
             
         
        """
        pass
    @HoleDiameter.setter
    def HoleDiameter(self, hole_diameter: float):
        """
        Setter for property: (float) HoleDiameter
         Returns the hole diameter of die pads.  
             
         
        """
        pass
    @property
    def Length(self) -> float:
        """
        Getter for property: (float) Length
         Returns the length of die pads.  
             
         
        """
        pass
    @Length.setter
    def Length(self, length: float):
        """
        Setter for property: (float) Length
         Returns the length of die pads.  
             
         
        """
        pass
    @property
    def LocationOffset(self) -> float:
        """
        Getter for property: (float) LocationOffset
         Returns the location offset of die pads.  
             
         
        """
        pass
    @LocationOffset.setter
    def LocationOffset(self, location_offset: float):
        """
        Setter for property: (float) LocationOffset
         Returns the location offset of die pads.  
             
         
        """
        pass
    @property
    def Relief(self) -> bool:
        """
        Getter for property: (bool) Relief
         Returns the relief switch of die pads, if true the relief will be built around the pads, if false they will not.  
             
         
        """
        pass
    @Relief.setter
    def Relief(self, relief: bool):
        """
        Setter for property: (bool) Relief
         Returns the relief switch of die pads, if true the relief will be built around the pads, if false they will not.  
             
         
        """
        pass
    @property
    def ReliefDepth(self) -> float:
        """
        Getter for property: (float) ReliefDepth
         Returns the relief depth of die pads.  
             
         
        """
        pass
    @ReliefDepth.setter
    def ReliefDepth(self, relief_depth: float):
        """
        Setter for property: (float) ReliefDepth
         Returns the relief depth of die pads.  
             
         
        """
        pass
    @property
    def ReliefWidth(self) -> float:
        """
        Getter for property: (float) ReliefWidth
         Returns the relief width of die pads.  
             
         
        """
        pass
    @ReliefWidth.setter
    def ReliefWidth(self, relief_width: float):
        """
        Setter for property: (float) ReliefWidth
         Returns the relief width of die pads.  
             
         
        """
        pass
    @property
    def ShapeType(self) -> PadParentBuilder.ShapeTypeOption:
        """
        Getter for property: ( PadParentBuilder.ShapeTypeOption NXOp) ShapeType
         Returns the shape type of die pads.  
             
         
        """
        pass
    @ShapeType.setter
    def ShapeType(self, shape_type: PadParentBuilder.ShapeTypeOption):
        """
        Setter for property: ( PadParentBuilder.ShapeTypeOption NXOp) ShapeType
         Returns the shape type of die pads.  
             
         
        """
        pass
    @property
    def SurfaceOffset(self) -> float:
        """
        Getter for property: (float) SurfaceOffset
         Returns the surface offset of die pads.  
             
         
        """
        pass
    @SurfaceOffset.setter
    def SurfaceOffset(self, surface_offset: float):
        """
        Setter for property: (float) SurfaceOffset
         Returns the surface offset of die pads.  
             
         
        """
        pass
    @property
    def Width(self) -> float:
        """
        Getter for property: (float) Width
         Returns the width of die pads.  
             
         
        """
        pass
    @Width.setter
    def Width(self, width: float):
        """
        Setter for property: (float) Width
         Returns the width of die pads.  
             
         
        """
        pass
    def CreateChild(self) -> PadChildBuilder:
        """
         Creates a child pad. 
         Returns diepadchild ( PadChildBuilder NXOp):  .
        """
        pass
    def DeleteChild(self, diepadchild: PadChildBuilder) -> None:
        """
         Deletes a child pad. 
        """
        pass
    def GetChildren(self) -> List[PadChildBuilder]:
        """
         Outputs the child pads. 
         Returns children ( PadChildBuilder List[NX):  The child pads. .
        """
        pass
    def GetHoleAttributes(self) -> Tuple[str, str, int, str]:
        """
         Gets the hole attributes, note existance of attributes depends on usage in
                main feature. 
         Returns A tuple consisting of (title, value, color, diameter_title). 
         - title is: str. Title for attribute. .
         - value is: str. Value of attribute. .
         - color is: int. Color of hole faces. .
         - diameter_title is: str. Title for diameter attribute. .

        """
        pass
    def GetPadAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the pad attributes, note existance of attributes depends on usage in
                main feature. 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. Title for attribute. .
         - value is: str. Value of attribute. .
         - color is: int. Color of pad faces. .

        """
        pass
    def GetReliefAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the relief attributes, note existance of attributes depends on usage in
                main feature. 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. Title for attribute. .
         - value is: str. Value of attribute. .
         - color is: int. Color of relief faces. .

        """
        pass
    def SetHoleAttributes(self, title: str, value: str, color: int, diameter_title: str) -> None:
        """
         Sets the hole attributes, note existance of attributes depends on usage in
                main feature. 
        """
        pass
    def SetPadAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the pad attributes, note existance of attributes depends on usage in
                main feature. 
        """
        pass
    def SetReliefAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the relief attributes, note existance of attributes depends on usage in
                main feature. 
        """
        pass
import NXOpen
import NXOpen.Features
class PierceHoleChildBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Pierce Hole Child sub feature. """
    class ShapeTypeOption(Enum):
        """
        Members Include: 
         |Circular|  circular hole 
         |Rectangular|  rectangular hole 
         |Curve|  curve defined hole 

        """
        Circular: int
        Rectangular: int
        Curve: int
        @staticmethod
        def ValueOf(value: int) -> PierceHoleChildBuilder.ShapeTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BreakerHoleDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BreakerHoleDepth
         Returns the breaker hole depth of the pierce hole   
            
         
        """
        pass
    @property
    def BreakerHoleDirection(self) -> NXOpen.ILocation:
        """
        Getter for property: ( NXOpen.ILocation) BreakerHoleDirection
         Returns the breaker hole direction of the pierce hole   
            
         
        """
        pass
    @BreakerHoleDirection.setter
    def BreakerHoleDirection(self, breaker_hole_direction: NXOpen.ILocation):
        """
        Setter for property: ( NXOpen.ILocation) BreakerHoleDirection
         Returns the breaker hole direction of the pierce hole   
            
         
        """
        pass
    @property
    def BreakerHoleFactor(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BreakerHoleFactor
         Returns the breaker hole factor of the pierce hole   
            
         
        """
        pass
    @property
    def BreakerHoleLocation(self) -> NXOpen.ILocation:
        """
        Getter for property: ( NXOpen.ILocation) BreakerHoleLocation
         Returns the location of breaker holes for the pierce hole   
            
         
        """
        pass
    @BreakerHoleLocation.setter
    def BreakerHoleLocation(self, breaker_hole_location: NXOpen.ILocation):
        """
        Setter for property: ( NXOpen.ILocation) BreakerHoleLocation
         Returns the location of breaker holes for the pierce hole   
            
         
        """
        pass
    @property
    def BreakerHoleOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BreakerHoleOffset
         Returns the breaker hole offset of the pierce hole   
            
         
        """
        pass
    @property
    def BuildStatus(self) -> DieBuildStatusOption:
        """
        Getter for property: ( DieBuildStatusOption NXOp) BuildStatus
         Returns the build status of the pierce hole   
            
         
        """
        pass
    @property
    def CircularSlugHole(self) -> bool:
        """
        Getter for property: (bool) CircularSlugHole
         Returns the circular slug hole switch of the pierce hole   
            
         
        """
        pass
    @CircularSlugHole.setter
    def CircularSlugHole(self, circular_slug_hole: bool):
        """
        Setter for property: (bool) CircularSlugHole
         Returns the circular slug hole switch of the pierce hole   
            
         
        """
        pass
    @property
    def Depth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Depth
         Returns the depth of the pierce hole   
            
         
        """
        pass
    @property
    def DesignStatus(self) -> bool:
        """
        Getter for property: (bool) DesignStatus
         Returns the design status of the pierce hole   
            
         
        """
        pass
    @DesignStatus.setter
    def DesignStatus(self, design_status: bool):
        """
        Setter for property: (bool) DesignStatus
         Returns the design status of the pierce hole   
            
         
        """
        pass
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Diameter
         Returns the diameter of the pierce hole   
            
         
        """
        pass
    @property
    def DieClearance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DieClearance
         Returns the die clearance of the pierce hole   
            
         
        """
        pass
    @property
    def DisplayHoles(self) -> bool:
        """
        Getter for property: (bool) DisplayHoles
         Returns the display holes option of the pierce hole   
            
         
        """
        pass
    @DisplayHoles.setter
    def DisplayHoles(self, display_pierce_holes: bool):
        """
        Setter for property: (bool) DisplayHoles
         Returns the display holes option of the pierce hole   
            
         
        """
        pass
    @property
    def DisplayStatus(self) -> bool:
        """
        Getter for property: (bool) DisplayStatus
         Returns the display status of the pierce hole   
            
         
        """
        pass
    @DisplayStatus.setter
    def DisplayStatus(self, display_status: bool):
        """
        Setter for property: (bool) DisplayStatus
         Returns the display status of the pierce hole   
            
         
        """
        pass
    @property
    def Length(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Length
         Returns the length of the pierce hole   
            
         
        """
        pass
    @property
    def PierceHoleDirection(self) -> NXOpen.ILocation:
        """
        Getter for property: ( NXOpen.ILocation) PierceHoleDirection
         Returns the pierce hole direction   
            
         
        """
        pass
    @PierceHoleDirection.setter
    def PierceHoleDirection(self, pierce_hole_direction: NXOpen.ILocation):
        """
        Setter for property: ( NXOpen.ILocation) PierceHoleDirection
         Returns the pierce hole direction   
            
         
        """
        pass
    @property
    def ProfileBlendRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ProfileBlendRadius
         Returns the profile blend radius of the pierce hole   
            
         
        """
        pass
    @property
    def ShapeType(self) -> PierceHoleChildBuilder.ShapeTypeOption:
        """
        Getter for property: ( PierceHoleChildBuilder.ShapeTypeOption NXOp) ShapeType
         Returns the pierce hole shape type   
            
         
        """
        pass
    @ShapeType.setter
    def ShapeType(self, shape_type: PierceHoleChildBuilder.ShapeTypeOption):
        """
        Setter for property: ( PierceHoleChildBuilder.ShapeTypeOption NXOp) ShapeType
         Returns the pierce hole shape type   
            
         
        """
        pass
    @property
    def SlugHoleDiameterIncrement(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SlugHoleDiameterIncrement
         Returns the slug hole diameter increment of the pierce hole   
            
         
        """
        pass
    @property
    def SlugHoleOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SlugHoleOffset
         Returns the slug hole offset of the pierce hole   
            
         
        """
        pass
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Width
         Returns the width of the pierce hole   
            
         
        """
        pass
    def GetBreakerHoleAttributes(self) -> Tuple[str, str, int, str]:
        """
         Gets the breaker hole attributes, note existance of attributes depends on usage in
                main feature 
         Returns A tuple consisting of (title, value, color, diameter_title). 
         - title is: str. title for attribute .
         - value is: str. value of attribute .
         - color is: int. color of hole faces .
         - diameter_title is: str. title for diameter attribute .

        """
        pass
    def GetBreakerHoleShape(self) -> Tuple[List[NXOpen.IProfile], DirectionOption]:
        """
         Gets the breaker hole shape of the pierce hole 
         Returns A tuple consisting of (profile_entries, direction). 
         - profile_entries is:  NXOpen.IProfile Li. profile entries .
         - direction is:  DirectionOption NXOp. profile direction .

        """
        pass
    def GetHoleAttributes(self) -> Tuple[str, str, int, str]:
        """
         Gets the hole attributes, note existance of attributes depends on usage in
                main feature 
         Returns A tuple consisting of (title, value, color, diameter_title). 
         - title is: str. title for attribute .
         - value is: str. value of attribute .
         - color is: int. color of hole faces .
         - diameter_title is: str. title for diameter attribute .

        """
        pass
    def GetPierceHoleLocation(self) -> List[NXOpen.ILocation]:
        """
         Gets the locations of the pierce hole 
         Returns pierce_hole_locations ( NXOpen.ILocation Li):  pierce hole location .
        """
        pass
    def GetPierceHoleShape(self) -> Tuple[List[NXOpen.IProfile], DirectionOption]:
        """
         Gets the shape of the pierce hole 
         Returns A tuple consisting of (profile_entries, direction). 
         - profile_entries is:  NXOpen.IProfile Li. profile entries .
         - direction is:  DirectionOption NXOp. profile direction .

        """
        pass
    def GetSlugHoleAttributes(self) -> Tuple[str, str, int, str]:
        """
         Gets the slug hole attributes, note existance of attributes depends on usage in
                main feature 
         Returns A tuple consisting of (title, value, color, diameter_title). 
         - title is: str. title for attribute .
         - value is: str. value of attribute .
         - color is: int. color of hole faces .
         - diameter_title is: str. title for diameter attribute .

        """
        pass
    def GetSlugHoleShape(self) -> Tuple[List[NXOpen.IProfile], DirectionOption]:
        """
         Gets the slug hole shape of the pierce hole 
         Returns A tuple consisting of (profile_entries, direction). 
         - profile_entries is:  NXOpen.IProfile Li. profile entries .
         - direction is:  DirectionOption NXOp. profile direction .

        """
        pass
    def SetBreakerHoleAttributes(self, title: str, value: str, color: int, diameter_title: str) -> None:
        """
         Sets the breaker hole attributes, note existance of attributes depends on usage in
                main feature 
        """
        pass
    def SetBreakerHoleDepth(self, breaker_hole_depth: str) -> None:
        """
         
        """
        pass
    def SetBreakerHoleFactor(self, breaker_hole_factor: str) -> None:
        """
         
        """
        pass
    def SetBreakerHoleOffset(self, breaker_hole_offset: str) -> None:
        """
         
        """
        pass
    def SetBreakerHoleShape(self, direction: DirectionOption, profile_entries: List[NXOpen.IProfile]) -> None:
        """
         Sets the breaker hole shape of the pierce hole 
        """
        pass
    def SetDepth(self, depth: str) -> None:
        """
         
        """
        pass
    def SetDiameter(self, diameter: str) -> None:
        """
         
        """
        pass
    def SetDieClearance(self, die_clearance: str) -> None:
        """
          
        """
        pass
    def SetHoleAttributes(self, title: str, value: str, color: int, diameter_title: str) -> None:
        """
         Sets the hole attributes, note existance of attributes depends on usage in
                main feature 
        """
        pass
    def SetLength(self, length: str) -> None:
        """
         
        """
        pass
    def SetPierceHoleLocation(self, pierce_hole_locations: List[NXOpen.ILocation]) -> None:
        """
         Sets the locations of the pierce hole 
        """
        pass
    def SetPierceHoleShape(self, direction: DirectionOption, profile_entries: List[NXOpen.IProfile]) -> None:
        """
         Sets the shape of the pierce hole 
        """
        pass
    def SetProfileBlendRadius(self, profile_blend_radius: str) -> None:
        """
          
        """
        pass
    def SetSlugHoleAttributes(self, title: str, value: str, color: int, diameter_title: str) -> None:
        """
         Sets the slug hole attributes, note existance of attributes depends on usage in
                main feature 
        """
        pass
    def SetSlugHoleDiameterIncrement(self, slug_hole_diameter_increment: str) -> None:
        """
         
        """
        pass
    def SetSlugHoleOffset(self, slug_hole_offset: str) -> None:
        """
         
        """
        pass
    def SetSlugHoleShape(self, direction: DirectionOption, profile_entries: List[NXOpen.IProfile]) -> None:
        """
         Sets the slug hole shape of the pierce hole 
        """
        pass
    def SetWidth(self, width: str) -> None:
        """
         
        """
        pass
    def TranslatePierceHoleLocation(self, translate_dist: NXOpen.Vector3d) -> None:
        """
         Translates the center of the die pierce hole by the specified amount. 
        """
        pass
import NXOpen
import NXOpen.Features
class PierceHoleParentBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Pierce Hole Parent sub feature. """
    @property
    def BreakerHoleDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BreakerHoleDepth
         Returns the breaker hole depth of pierce holes   
            
         
        """
        pass
    @property
    def BreakerHoleFactor(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BreakerHoleFactor
         Returns the breaker hole factor of pierce holes   
            
         
        """
        pass
    @property
    def BreakerHoleOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BreakerHoleOffset
         Returns the breaker hole offset of pierce holes   
            
         
        """
        pass
    @property
    def BuildStatus(self) -> DieBuildStatusOption:
        """
        Getter for property: ( DieBuildStatusOption NXOp) BuildStatus
         Returns the build status of pierce holes   
            
         
        """
        pass
    @property
    def CircularSlugHole(self) -> bool:
        """
        Getter for property: (bool) CircularSlugHole
         Returns the circular slug hole switch of pierce holes   
            
         
        """
        pass
    @CircularSlugHole.setter
    def CircularSlugHole(self, circular_slug_hole: bool):
        """
        Setter for property: (bool) CircularSlugHole
         Returns the circular slug hole switch of pierce holes   
            
         
        """
        pass
    @property
    def CommonSlugHole(self) -> bool:
        """
        Getter for property: (bool) CommonSlugHole
         Returns the common slug hole switch of pierce holes   
            
         
        """
        pass
    @CommonSlugHole.setter
    def CommonSlugHole(self, common_slug_hole: bool):
        """
        Setter for property: (bool) CommonSlugHole
         Returns the common slug hole switch of pierce holes   
            
         
        """
        pass
    @property
    def Depth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Depth
         Returns the depth of pierce holes   
            
         
        """
        pass
    @property
    def DesignStatus(self) -> bool:
        """
        Getter for property: (bool) DesignStatus
         Returns the design status of pierce holes   
            
         
        """
        pass
    @DesignStatus.setter
    def DesignStatus(self, design_status: bool):
        """
        Setter for property: (bool) DesignStatus
         Returns the design status of pierce holes   
            
         
        """
        pass
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Diameter
         Returns the diameter of pierce holes   
            
         
        """
        pass
    @property
    def DieClearance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DieClearance
         Returns the die clearance of pierce holes   
            
         
        """
        pass
    @property
    def DisplayHoles(self) -> bool:
        """
        Getter for property: (bool) DisplayHoles
         Returns the display holes option of pierce holes   
            
         
        """
        pass
    @DisplayHoles.setter
    def DisplayHoles(self, display_pierce_holes: bool):
        """
        Setter for property: (bool) DisplayHoles
         Returns the display holes option of pierce holes   
            
         
        """
        pass
    @property
    def DisplayStatus(self) -> bool:
        """
        Getter for property: (bool) DisplayStatus
         Returns the display status of pierce holes   
            
         
        """
        pass
    @DisplayStatus.setter
    def DisplayStatus(self, display_status: bool):
        """
        Setter for property: (bool) DisplayStatus
         Returns the display status of pierce holes   
            
         
        """
        pass
    @property
    def Length(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Length
         Returns the length of pierce holes   
            
         
        """
        pass
    @property
    def ProfileBlendRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ProfileBlendRadius
         Returns the profile blend radius of pierce holes   
            
         
        """
        pass
    @property
    def SlugHoleDiameterIncrement(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SlugHoleDiameterIncrement
         Returns the slug hole diameter increment of pierce holes   
            
         
        """
        pass
    @property
    def SlugHoleOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SlugHoleOffset
         Returns the slug hole offset of pierce holes   
            
         
        """
        pass
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Width
         Returns the width of pierce holes   
            
         
        """
        pass
    def CreateChild(self) -> PierceHoleChildBuilder:
        """
         Creates a child pierce hole 
         Returns dieholechild ( PierceHoleChildBuilder NXOp):  .
        """
        pass
    def DeleteChild(self, dieholechild: PierceHoleChildBuilder) -> None:
        """
         Deletes a child pierce hole 
        """
        pass
    def GetBreakerHoleAttributes(self) -> Tuple[str, str, int, str]:
        """
         Gets the breaker hole attributes, note existance of attributes depends on usage in
                main feature 
         Returns A tuple consisting of (title, value, color, diameter_title). 
         - title is: str. title for attribute .
         - value is: str. value of attribute .
         - color is: int. color of hole faces .
         - diameter_title is: str. title for diameter attribute .

        """
        pass
    def GetChildren(self) -> List[PierceHoleChildBuilder]:
        """
         Outputs the pierce hole children 
         Returns children ( PierceHoleChildBuilder List[NX):  children .
        """
        pass
    def GetHoleAttributes(self) -> Tuple[str, str, int, str]:
        """
         Gets the hole attributes, note existance of attributes depends on usage in
                main feature 
         Returns A tuple consisting of (title, value, color, diameter_title). 
         - title is: str. title for attribute .
         - value is: str. value of attribute .
         - color is: int. color of hole faces .
         - diameter_title is: str. title for diameter attribute .

        """
        pass
    def GetSlugHoleAttributes(self) -> Tuple[str, str, int, str]:
        """
         Gets the slug hole attributes, note existance of attributes depends on usage in
                main feature 
         Returns A tuple consisting of (title, value, color, diameter_title). 
         - title is: str. title for attribute .
         - value is: str. value of attribute .
         - color is: int. color of hole faces .
         - diameter_title is: str. title for diameter attribute .

        """
        pass
    def SetBreakerHoleAttributes(self, title: str, value: str, color: int, diameter_title: str) -> None:
        """
         Sets the breaker hole attributes, note existance of attributes depends on usage in
                main feature 
        """
        pass
    def SetBreakerHoleDepth(self, breaker_hole_depth: str) -> None:
        """
         
        """
        pass
    def SetBreakerHoleFactor(self, breaker_hole_factor: str) -> None:
        """
         
        """
        pass
    def SetBreakerHoleOffset(self, breaker_hole_offset: str) -> None:
        """
         
        """
        pass
    def SetDepth(self, depth: str) -> None:
        """
         
        """
        pass
    def SetDiameter(self, diameter: str) -> None:
        """
          
        """
        pass
    def SetDieClearance(self, die_clearance: str) -> None:
        """
         
        """
        pass
    def SetHoleAttributes(self, title: str, value: str, color: int, diameter_title: str) -> None:
        """
         Sets the hole attributes, note existance of attributes depends on usage in
                main feature 
        """
        pass
    def SetLength(self, length: str) -> None:
        """
         
        """
        pass
    def SetProfileBlendRadius(self, profile_blend_radius: str) -> None:
        """
          
        """
        pass
    def SetSlugHoleAttributes(self, title: str, value: str, color: int, diameter_title: str) -> None:
        """
         Sets the slug hole attributes, note existance of attributes depends on usage in
                main feature 
        """
        pass
    def SetSlugHoleDiameterIncrement(self, slug_hole_diameter_increment: str) -> None:
        """
         
        """
        pass
    def SetSlugHoleOffset(self, slug_hole_offset: str) -> None:
        """
         
        """
        pass
    def SetWidth(self, pierce_hole_width: str) -> None:
        """
         
        """
        pass
import NXOpen
class PierceItemBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[PierceItemBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: PierceItemBuilder) -> None:
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
    def Erase(self, obj: PierceItemBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: PierceItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: PierceItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> PierceItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( PierceItemBuilder NXOp):  object found at input index .
        """
        pass
    def GetContents(self) -> List[PierceItemBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( PierceItemBuilder List[NX):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: PierceItemBuilder) -> None:
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
    def SetContents(self, objects: List[PierceItemBuilder]) -> None:
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
    def Swap(self, object1: PierceItemBuilder, object2: PierceItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class PierceItemBuilder(NXOpen.NXObject): 
    """
    Represents a NXOpen.Die.PierceItemBuilder
    """
    class HoleShapeType(Enum):
        """
        Members Include: 
         |Circular|  Circular shaped hole 
         |Oblong|  Oblong shaped hole 
         |Square|  Square shaped hole 
         |Rectangular|  Rectangular shaped hole 
         |RoundedRectangular|  Rouned Rectangular shaped hole 
         |ChordRectangular|  Chord Rectangular hole 
         |Hexagonal|  Hexagonal shaped hole 
         |Other|  Not a standard shape 

        """
        Circular: int
        Oblong: int
        Square: int
        Rectangular: int
        RoundedRectangular: int
        ChordRectangular: int
        Hexagonal: int
        Other: int
        @staticmethod
        def ValueOf(value: int) -> PierceItemBuilder.HoleShapeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SizingMethodOption(Enum):
        """
        Members Include: 
         |Auto|  Will calculate size at creation and during update 
         |Manual|  Will use size specified 

        """
        Auto: int
        Manual: int
        @staticmethod
        def ValueOf(value: int) -> PierceItemBuilder.SizingMethodOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def HoleShape(self) -> PierceItemBuilder.HoleShapeType:
        """
        Getter for property: ( PierceItemBuilder.HoleShapeType NXOp) HoleShape
         Returns the hole shape   
            
         
        """
        pass
    @HoleShape.setter
    def HoleShape(self, holeShape: PierceItemBuilder.HoleShapeType):
        """
        Setter for property: ( PierceItemBuilder.HoleShapeType NXOp) HoleShape
         Returns the hole shape   
            
         
        """
        pass
    @property
    def PunchDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PunchDiameter
         Returns the punch radius   
            
         
        """
        pass
    @property
    def PunchLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PunchLength
         Returns the punch length   
            
         
        """
        pass
    @property
    def PunchRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PunchRadius
         Returns the punch radius   
            
         
        """
        pass
    @property
    def PunchWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PunchWidth
         Returns the punch width   
            
         
        """
        pass
    @property
    def ReferenceVector(self) -> NXOpen.ILocation:
        """
        Getter for property: ( NXOpen.ILocation) ReferenceVector
         Returns the reference direction of the hole   
            
         
        """
        pass
    @ReferenceVector.setter
    def ReferenceVector(self, ref_vector: NXOpen.ILocation):
        """
        Setter for property: ( NXOpen.ILocation) ReferenceVector
         Returns the reference direction of the hole   
            
         
        """
        pass
    @property
    def SizingMethod(self) -> PierceItemBuilder.SizingMethodOption:
        """
        Getter for property: ( PierceItemBuilder.SizingMethodOption NXOp) SizingMethod
         Returns the sizing method   
            
         
        """
        pass
    @SizingMethod.setter
    def SizingMethod(self, sizingMethod: PierceItemBuilder.SizingMethodOption):
        """
        Setter for property: ( PierceItemBuilder.SizingMethodOption NXOp) SizingMethod
         Returns the sizing method   
            
         
        """
        pass
    def GetPierceObjects(self) -> List[NXOpen.IProfile]:
        """
         Gets the objects making up the hole to be pierced. 
         Returns objects ( NXOpen.IProfile Li):  Objects that make up the hole to be pierced .
        """
        pass
    def SetPierceObjects(self, objects: List[NXOpen.IProfile]) -> None:
        """
         Sets the objects making up the hole to be pierced. 
        """
        pass
import NXOpen
import NXOpen.Features
class PierceTaskBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Pierce Task feature builder """
    class CamTypes(Enum):
        """
        Members Include: 
         |Direct|  Direct 
         |Aerial|  Aerial Cam 
         |BaseMounted|  Base Mounted Cam 

        """
        Direct: int
        Aerial: int
        BaseMounted: int
        @staticmethod
        def ValueOf(value: int) -> PierceTaskBuilder.CamTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CenterPointOptionTypes(Enum):
        """
        Members Include: 
         |NotSet|  No center points output 
         |Die|  Center points output in die position 
         |Product|  Center points output in product position 
         |Both|  Center points output in both die and product position 

        """
        NotSet: int
        Die: int
        Product: int
        Both: int
        @staticmethod
        def ValueOf(value: int) -> PierceTaskBuilder.CenterPointOptionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PrecisionTypes(Enum):
        """
        Members Include: 
         |Gage|  Gage hole 
         |Critical|  Critical hole 
         |Standard|  Standard hole 

        """
        Gage: int
        Critical: int
        Standard: int
        @staticmethod
        def ValueOf(value: int) -> PierceTaskBuilder.PrecisionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngleTolerance(self) -> float:
        """
        Getter for property: (float) AngleTolerance
         Returns the angle tolerance of the pierce task   
            
         
        """
        pass
    @AngleTolerance.setter
    def AngleTolerance(self, angle_tolerance: float):
        """
        Setter for property: (float) AngleTolerance
         Returns the angle tolerance of the pierce task   
            
         
        """
        pass
    @property
    def AssociatedObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) AssociatedObjects
         Returns the assoc objects   
            
         
        """
        pass
    @property
    def CamDirection(self) -> NXOpen.ILocation:
        """
        Getter for property: ( NXOpen.ILocation) CamDirection
         Returns the cam direction of the pierce task   
            
         
        """
        pass
    @CamDirection.setter
    def CamDirection(self, cam_direction: NXOpen.ILocation):
        """
        Setter for property: ( NXOpen.ILocation) CamDirection
         Returns the cam direction of the pierce task   
            
         
        """
        pass
    @property
    def CamType(self) -> PierceTaskBuilder.CamTypes:
        """
        Getter for property: ( PierceTaskBuilder.CamTypes NXOp) CamType
         Returns the cam type of the pierce task   
            
         
        """
        pass
    @CamType.setter
    def CamType(self, cam_type: PierceTaskBuilder.CamTypes):
        """
        Setter for property: ( PierceTaskBuilder.CamTypes NXOp) CamType
         Returns the cam type of the pierce task   
            
         
        """
        pass
    @property
    def CenterPointOption(self) -> PierceTaskBuilder.CenterPointOptionTypes:
        """
        Getter for property: ( PierceTaskBuilder.CenterPointOptionTypes NXOp) CenterPointOption
         Returns the center point output option of the pierce task   
            
         
        """
        pass
    @CenterPointOption.setter
    def CenterPointOption(self, center_point_option: PierceTaskBuilder.CenterPointOptionTypes):
        """
        Setter for property: ( PierceTaskBuilder.CenterPointOptionTypes NXOp) CenterPointOption
         Returns the center point output option of the pierce task   
            
         
        """
        pass
    @property
    def CreateScrap(self) -> bool:
        """
        Getter for property: (bool) CreateScrap
         Returns the create scrap setting of the pierce task.  
           
                True indicates that the scrap is to be created.   
         
        """
        pass
    @CreateScrap.setter
    def CreateScrap(self, create_scrap: bool):
        """
        Setter for property: (bool) CreateScrap
         Returns the create scrap setting of the pierce task.  
           
                True indicates that the scrap is to be created.   
         
        """
        pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance of the pierce task   
            
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distance_tolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance of the pierce task   
            
         
        """
        pass
    @property
    def FinishOperation(self) -> bool:
        """
        Getter for property: (bool) FinishOperation
         Returns the finish operation of the pierce task 
                True indicates the pierce is to be a finish pierce.  
           False indicates rough pierce.   
         
        """
        pass
    @FinishOperation.setter
    def FinishOperation(self, finish_operation: bool):
        """
        Setter for property: (bool) FinishOperation
         Returns the finish operation of the pierce task 
                True indicates the pierce is to be a finish pierce.  
           False indicates rough pierce.   
         
        """
        pass
    @property
    def LayoutFlange(self) -> bool:
        """
        Getter for property: (bool) LayoutFlange
         Returns the layout flange setting of the pierce task.  
           
                True indicates that the pierce curve is to be laid out on the flange.   
         
        """
        pass
    @LayoutFlange.setter
    def LayoutFlange(self, layout_flange: bool):
        """
        Setter for property: (bool) LayoutFlange
         Returns the layout flange setting of the pierce task.  
           
                True indicates that the pierce curve is to be laid out on the flange.   
         
        """
        pass
    @property
    def PierceHoles(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) PierceHoles
         Returns the pierce holes   
            
         
        """
        pass
    @property
    def PierceHolesList(self) -> PierceItemBuilderList:
        """
        Getter for property: ( PierceItemBuilderList NXOp) PierceHolesList
         Returns the pierce holes list   
            
         
        """
        pass
    @property
    def PrecisionType(self) -> PierceTaskBuilder.PrecisionTypes:
        """
        Getter for property: ( PierceTaskBuilder.PrecisionTypes NXOp) PrecisionType
         Returns the precision type of the pierce task   
            
         
        """
        pass
    @PrecisionType.setter
    def PrecisionType(self, precision_type: PierceTaskBuilder.PrecisionTypes):
        """
        Setter for property: ( PierceTaskBuilder.PrecisionTypes NXOp) PrecisionType
         Returns the precision type of the pierce task   
            
         
        """
        pass
    @property
    def TipFeature(self) -> NXOpen.Features.SelectFeature:
        """
        Getter for property: ( NXOpen.Features.SelectFeature) TipFeature
         Returns the tip feature   
            
         
        """
        pass
    @property
    def TippedProduct(self) -> NXOpen.Features.Feature:
        """
        Getter for property: ( NXOpen.Features.Feature) TippedProduct
         Returns the tipped product of the pierce task   
            
         
        """
        pass
    @TippedProduct.setter
    def TippedProduct(self, tipped_product: NXOpen.Features.Feature):
        """
        Setter for property: ( NXOpen.Features.Feature) TippedProduct
         Returns the tipped product of the pierce task   
            
         
        """
        pass
    @property
    def TrimNewDieFace(self) -> bool:
        """
        Getter for property: (bool) TrimNewDieFace
         Returns the trim new die face, from NX10.  
          0 new stamping output can import one new die face to die engineer process.
                    If this pierce task will trim this new die face, set trimNewDieFace to true, or else set it to false.   
         
        """
        pass
    @TrimNewDieFace.setter
    def TrimNewDieFace(self, trimNewDieFace: bool):
        """
        Setter for property: (bool) TrimNewDieFace
         Returns the trim new die face, from NX10.  
          0 new stamping output can import one new die face to die engineer process.
                    If this pierce task will trim this new die face, set trimNewDieFace to true, or else set it to false.   
         
        """
        pass
    @property
    def WithoutWorkflowSheet(self) -> NXOpen.Body:
        """
        Getter for property: ( NXOpen.Body) WithoutWorkflowSheet
         Returns the without workflow sheet of the pierce task builder.  
           
                    In release NX11.0, pierce task supports without workflow type 
                    when the workflow tip feature does not exist.   
         
        """
        pass
    @WithoutWorkflowSheet.setter
    def WithoutWorkflowSheet(self, sheet: NXOpen.Body):
        """
        Setter for property: ( NXOpen.Body) WithoutWorkflowSheet
         Returns the without workflow sheet of the pierce task builder.  
           
                    In release NX11.0, pierce task supports without workflow type 
                    when the workflow tip feature does not exist.   
         
        """
        pass
    def GetAssociativeObjects(self) -> List[NXOpen.DisplayableObject]:
        """
         Gets the associative objects of the pierce task 
         Returns objects ( NXOpen.DisplayableObject Li):  .
        """
        pass
    def GetCameraLayerAndXmlp(self) -> Tuple[List[str], List[str]]:
        """
         Gets the camera layer settings and xmlp data 
         Returns A tuple consisting of (layer_settings, xmlp_data). 
         - layer_settings is: List[str]. 1 layer setting string for each camera object. 
                                                                       the string needs to be 256 characters long 
                                                                       (one for each user layer) with either 0 for off
                                                                       or 1 for on. .
         - xmlp_data is: List[str]. xmlp data .

        """
        pass
    def GetCameraNames(self) -> List[str]:
        """
         Gets the names of the camera 
         Returns strings (List[str]):  each string contains the name of a camera object .
        """
        pass
    def GetCameraViews(self) -> List[NXOpen.View]:
        """
         Gets the camera views of the pierce task 
         Returns objects ( NXOpen.View Li):  .
        """
        pass
    def GetDetails(self) -> List[str]:
        """
         Gets the detailed description of the pierce task 
         Returns strings (List[str]):  detail strings .
        """
        pass
    def GetPierceBounds(self) -> Tuple[List[NXOpen.IProfile], DirectionOption]:
        """
         Gets the pierce bounds of the pierce task 
         Returns A tuple consisting of (profile_entries, direction). 
         - profile_entries is:  NXOpen.IProfile Li. Profile entries that make up the 
                                                                                                   boundary of the pierce task .
         - direction is:  DirectionOption NXOp. Profile direction .

        """
        pass
    def NewPierceHole(self, hole_shape: PierceItemBuilder.HoleShapeType) -> PierceItemBuilder:
        """
         Creates a new pierce hole item in the set 
         Returns pierceHole ( PierceItemBuilder NXOp): .
        """
        pass
    def SetAssociativeObjects(self, objects: List[NXOpen.DisplayableObject]) -> None:
        """
         Sets the associative objects of the pierce task 
        """
        pass
    def SetCameraLayerAndXmlp(self, layer_settings: List[str], xmlp_data: List[str]) -> None:
        """
         Sets the camera layer settings and xmlp data 
        """
        pass
    def SetCameraNames(self, strings: List[str]) -> None:
        """
         Sets the names of the camera 
        """
        pass
    def SetCameraViews(self, objects: List[NXOpen.View]) -> None:
        """
         Sets the camera views of the pierce task 
        """
        pass
    def SetDetails(self, strings: List[str]) -> None:
        """
         Sets the detailed description of the pierce task 
        """
        pass
    def SetPierceBounds(self, direction: DirectionOption, profile_entries: List[NXOpen.IProfile]) -> None:
        """
         Sets the pierce bounds of the pierce task. 
                Note - Die.PierceTaskBuilder.TippedProduct needs to be called before this function. 
        """
        pass
import NXOpen
import NXOpen.Features
class PointChildBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Die Point Child sub feature. """
    @property
    def BuildStatus(self) -> DieBuildStatusOption:
        """
        Getter for property: ( DieBuildStatusOption NXOp) BuildStatus
         Returns the build status of the point.  
             
         
        """
        pass
    @property
    def DesignStatus(self) -> bool:
        """
        Getter for property: (bool) DesignStatus
         Returns the design status of the point, if true the point will be built into the model, if false it will not.  
             
         
        """
        pass
    @DesignStatus.setter
    def DesignStatus(self, design_status: bool):
        """
        Setter for property: (bool) DesignStatus
         Returns the design status of the point, if true the point will be built into the model, if false it will not.  
             
         
        """
        pass
    @property
    def DisplayStatus(self) -> bool:
        """
        Getter for property: (bool) DisplayStatus
         Returns the display status of the point, if true input data to the point will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    @DisplayStatus.setter
    def DisplayStatus(self, display_status: bool):
        """
        Setter for property: (bool) DisplayStatus
         Returns the display status of the point, if true input data to the point will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    @property
    def Point(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Point
         Returns the location of the point.  
             
         
        """
        pass
    @Point.setter
    def Point(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Point
         Returns the location of the point.  
             
         
        """
        pass
import NXOpen.Features
class PointParentBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Die Point Parent sub feature. """
    @property
    def BuildStatus(self) -> DieBuildStatusOption:
        """
        Getter for property: ( DieBuildStatusOption NXOp) BuildStatus
         Returns the build status of points.  
             
         
        """
        pass
    @property
    def DesignStatus(self) -> bool:
        """
        Getter for property: (bool) DesignStatus
         Returns the design status of points, if true the points will be built into the model, if false they will not.  
             
         
        """
        pass
    @DesignStatus.setter
    def DesignStatus(self, design_status: bool):
        """
        Setter for property: (bool) DesignStatus
         Returns the design status of points, if true the points will be built into the model, if false they will not.  
             
         
        """
        pass
    @property
    def DisplayStatus(self) -> bool:
        """
        Getter for property: (bool) DisplayStatus
         Returns the display status of points, if true input data to the points will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    @DisplayStatus.setter
    def DisplayStatus(self, display_status: bool):
        """
        Setter for property: (bool) DisplayStatus
         Returns the display status of points, if true input data to the points will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    def CreateChild(self) -> PointChildBuilder:
        """
         Creates a child point. 
         Returns diepointchild ( PointChildBuilder NXOp):  .
        """
        pass
    def DeleteChild(self, diepointchild: PointChildBuilder) -> None:
        """
         Deletes a child point. 
        """
        pass
    def GetChildren(self) -> List[PointChildBuilder]:
        """
         Outputs the child points. 
         Returns children ( PointChildBuilder List[NX):  The child points. .
        """
        pass
import NXOpen
class PressModelRoot(NXOpen.TaggedObject): 
    """ Represents a Die Simulation - Press Model Root. """
    def IsActive(self) -> bool:
        """
         Is the press model active 
         Returns active (bool): .
        """
        pass
import NXOpen
class PressModel(NXOpen.TransientObject): 
    """ Represents a Die Simulation - Press Model """
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
           it is illegal to use the object.  In .NET, this method is automatically
           called when the object is deleted by the garbage collector.  
        """
        pass
    def GetNumOperations(self) -> int:
        """
         Get number of operations 
         Returns num_operations (int): .
        """
        pass
    def SetOperationCushionSettings(self, operation: int, lift_start_angle: float, lift_stop_angle: float, lift_to_dist: float, lock_at_dist: float) -> None:
        """
         Set operation cushion values (Obsolete) 
        """
        pass
    def SetOperationCushionSettings2(self, operation: int, ventilation_lift_distance: float, ventilation_lift_stay: int, binder_way_lift_distance: float, binder_way_lift_duration: int, upper_limit: float, lower_limit: float) -> None:
        """
         Set operation cushion values 
        """
        pass
    def SetOperationSlideHeight(self, operation: int, slide_height: float) -> None:
        """
         Set operation slide height 
        """
        pass
    def SetOperationTransportCurveSet(self, operation: int, curve_set: int) -> None:
        """
         Tell the press model which transport curve set to use in the given operation 
        """
        pass
    def SetOperationUserTransportCurves(self, operation: int, vals: List[float]) -> None:
        """
         Set values of the User Defined transport curve set, for given operation 
        """
        pass
import NXOpen
import NXOpen.Features
class PressureSystemChildBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Die Pressure System Child sub feature. """
    @property
    def BuildStatus(self) -> DieBuildStatusOption:
        """
        Getter for property: ( DieBuildStatusOption NXOp) BuildStatus
         Returns the build status of the pressure system.  
             
         
        """
        pass
    @property
    def Clearance(self) -> float:
        """
        Getter for property: (float) Clearance
         Returns the clearance of the pressure system.  
             
         
        """
        pass
    @Clearance.setter
    def Clearance(self, clearance: float):
        """
        Setter for property: (float) Clearance
         Returns the clearance of the pressure system.  
             
         
        """
        pass
    @property
    def Csys(self) -> NXOpen.CartesianCoordinateSystem:
        """
        Getter for property: ( NXOpen.CartesianCoordinateSystem) Csys
         Returns the csys of the pressure system.  
             
         
        """
        pass
    @Csys.setter
    def Csys(self, csys: NXOpen.CartesianCoordinateSystem):
        """
        Setter for property: ( NXOpen.CartesianCoordinateSystem) Csys
         Returns the csys of the pressure system.  
             
         
        """
        pass
    @property
    def DesignStatus(self) -> bool:
        """
        Getter for property: (bool) DesignStatus
         Returns the design status of the pressure system, if true the pressure system will be built into the model, if false it will not.  
             
         
        """
        pass
    @DesignStatus.setter
    def DesignStatus(self, design_status: bool):
        """
        Setter for property: (bool) DesignStatus
         Returns the design status of the pressure system, if true the pressure system will be built into the model, if false it will not.  
             
         
        """
        pass
    @property
    def Diameter(self) -> float:
        """
        Getter for property: (float) Diameter
         Returns the diameter of the pressure system.  
             
         
        """
        pass
    @Diameter.setter
    def Diameter(self, diameter: float):
        """
        Setter for property: (float) Diameter
         Returns the diameter of the pressure system.  
             
         
        """
        pass
    @property
    def DisplayStatus(self) -> bool:
        """
        Getter for property: (bool) DisplayStatus
         Returns the display status of the pressure system, if true input data to the pressure system will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    @DisplayStatus.setter
    def DisplayStatus(self, display_status: bool):
        """
        Setter for property: (bool) DisplayStatus
         Returns the display status of the pressure system, if true input data to the pressure system will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    @property
    def Height(self) -> float:
        """
        Getter for property: (float) Height
         Returns the height of the pressure system.  
             
         
        """
        pass
    @Height.setter
    def Height(self, height: float):
        """
        Setter for property: (float) Height
         Returns the height of the pressure system.  
             
         
        """
        pass
    @property
    def Point(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Point
         Returns the location of the pressure system.  
             
         
        """
        pass
    @Point.setter
    def Point(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Point
         Returns the location of the pressure system.  
             
         
        """
        pass
import NXOpen.Features
class PressureSystemParentBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Die Pressure System Parent sub feature. """
    @property
    def BuildStatus(self) -> DieBuildStatusOption:
        """
        Getter for property: ( DieBuildStatusOption NXOp) BuildStatus
         Returns the build status of pressure systems.  
             
         
        """
        pass
    @property
    def Clearance(self) -> float:
        """
        Getter for property: (float) Clearance
         Returns the clearance of pressure systems.  
             
         
        """
        pass
    @Clearance.setter
    def Clearance(self, clearance: float):
        """
        Setter for property: (float) Clearance
         Returns the clearance of pressure systems.  
             
         
        """
        pass
    @property
    def DesignStatus(self) -> bool:
        """
        Getter for property: (bool) DesignStatus
         Returns the design status of pressure systems, if true the pressure systems will be built into the model, if false they will not.  
             
         
        """
        pass
    @DesignStatus.setter
    def DesignStatus(self, design_status: bool):
        """
        Setter for property: (bool) DesignStatus
         Returns the design status of pressure systems, if true the pressure systems will be built into the model, if false they will not.  
             
         
        """
        pass
    @property
    def Diameter(self) -> float:
        """
        Getter for property: (float) Diameter
         Returns the diameter of pressure systems.  
             
         
        """
        pass
    @Diameter.setter
    def Diameter(self, diameter: float):
        """
        Setter for property: (float) Diameter
         Returns the diameter of pressure systems.  
             
         
        """
        pass
    @property
    def DisplayStatus(self) -> bool:
        """
        Getter for property: (bool) DisplayStatus
         Returns the display status of pressure systems, if true input data to the pressure systems will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    @DisplayStatus.setter
    def DisplayStatus(self, display_status: bool):
        """
        Setter for property: (bool) DisplayStatus
         Returns the display status of pressure systems, if true input data to the pressure systems will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    @property
    def Height(self) -> float:
        """
        Getter for property: (float) Height
         Returns the height of pressure systems.  
             
         
        """
        pass
    @Height.setter
    def Height(self, height: float):
        """
        Setter for property: (float) Height
         Returns the height of pressure systems.  
             
         
        """
        pass
    @property
    def XCount(self) -> int:
        """
        Getter for property: (int) XCount
         Returns the x count of pressure systems.  
             
         
        """
        pass
    @XCount.setter
    def XCount(self, x_count: int):
        """
        Setter for property: (int) XCount
         Returns the x count of pressure systems.  
             
         
        """
        pass
    @property
    def XDistance(self) -> float:
        """
        Getter for property: (float) XDistance
         Returns the x distance of pressure systems.  
             
         
        """
        pass
    @XDistance.setter
    def XDistance(self, x_distance: float):
        """
        Setter for property: (float) XDistance
         Returns the x distance of pressure systems.  
             
         
        """
        pass
    @property
    def XOffset(self) -> float:
        """
        Getter for property: (float) XOffset
         Returns the x offset of pressure systems.  
             
         
        """
        pass
    @XOffset.setter
    def XOffset(self, x_offset: float):
        """
        Setter for property: (float) XOffset
         Returns the x offset of pressure systems.  
             
         
        """
        pass
    @property
    def YCount(self) -> int:
        """
        Getter for property: (int) YCount
         Returns the y count of pressure systems.  
             
         
        """
        pass
    @YCount.setter
    def YCount(self, y_count: int):
        """
        Setter for property: (int) YCount
         Returns the y count of pressure systems.  
             
         
        """
        pass
    @property
    def YDistance(self) -> float:
        """
        Getter for property: (float) YDistance
         Returns the y distance of pressure systems.  
             
         
        """
        pass
    @YDistance.setter
    def YDistance(self, y_distance: float):
        """
        Setter for property: (float) YDistance
         Returns the y distance of pressure systems.  
             
         
        """
        pass
    @property
    def YOffset(self) -> float:
        """
        Getter for property: (float) YOffset
         Returns the y offset of pressure systems.  
             
         
        """
        pass
    @YOffset.setter
    def YOffset(self, y_offset: float):
        """
        Setter for property: (float) YOffset
         Returns the y offset of pressure systems.  
             
         
        """
        pass
    def CreateChild(self) -> PressureSystemChildBuilder:
        """
         Creates a child pressure system. 
         Returns diepressuresystemchild ( PressureSystemChildBuilder NXOp):  .
        """
        pass
    def DeleteChild(self, diepressuresystemchild: PressureSystemChildBuilder) -> None:
        """
         Deletes a child pressure system. 
        """
        pass
    def GetChildren(self) -> List[PressureSystemChildBuilder]:
        """
         Outputs the child pressure systems. 
         Returns children ( PressureSystemChildBuilder List[NX):  The child pressure systems. .
        """
        pass
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
class QuickBinderBuilder(NXOpen.Features.FeatureBuilder): 
    """ 
    Represents a NXOpen.Die.QuickBinderBuilder builder which builds a developable binder sheet
    body by adding cones, cylinders, or planes to an approximated face.
    """
    class EditTypes(Enum):
        """
        Members Include: 
         |EdgeExtend|  Extend edge of a face. 
         |EdgeExtendStart|  Extend start edge of a planar face. 
         |EdgeExtendEnd|  Extend end edge of a planar face. 
         |EdgeAngleStart|  Change the angle of the start edge of a planar face. 
         |EdgeAngleEnd|  Change the angle of the end edge of a planar face. 
         |FaceRadius|  Change the face radius of a conicalcylindrical face. 
         |FaceCentralAngle|  Change the central angle of a conicalcylindrical face. 
         |FaceReverseConvexity|  Reverse the convexity of a conicalcylindrical face. 
         |Transform|  Transform body. 
         |ExtendUMinimum|  Extend the U Minimum edge of the anchor face. 
         |ExtendUMaximum|  Extend the U Maximum edge of the anchor face. 
         |ExtendVMinimum|  Extend the V Minimum edge of the anchor face. 
         |ExtendVMaximum|  Extend the V Maximum edge of the anchor face. 

        """
        EdgeExtend: int
        EdgeExtendStart: int
        EdgeExtendEnd: int
        EdgeAngleStart: int
        EdgeAngleEnd: int
        FaceRadius: int
        FaceCentralAngle: int
        FaceReverseConvexity: int
        Transform: int
        ExtendUMinimum: int
        ExtendUMaximum: int
        ExtendVMinimum: int
        ExtendVMaximum: int
        @staticmethod
        def ValueOf(value: int) -> QuickBinderBuilder.EditTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |Planar|  planar 
         |Cylindrical|  cylindrical 
         |Conical|  conical 
         |MonoArc|  mono arc 

        """
        Planar: int
        Cylindrical: int
        Conical: int
        MonoArc: int
        @staticmethod
        def ValueOf(value: int) -> QuickBinderBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AnchorBaseRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) AnchorBaseRadius
         Returns the base radius for a conical anchor face.  
             
         
        """
        pass
    @property
    def AnchorRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) AnchorRadius
         Returns the radius value of a cylidrical anchor face.  
            
         
        """
        pass
    @property
    def AnchorTopRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) AnchorTopRadius
         Returns the top radius for a conical anchor face.  
             
         
        """
        pass
    @property
    def BaseRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BaseRadius
         Returns the base radius for a cone.  
             
         
        """
        pass
    @property
    def CentralAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CentralAngle
         Returns the central angle of a cylindercone.  
             
         
        """
        pass
    @property
    def EdgeIndexToEdit(self) -> int:
        """
        Getter for property: (int) EdgeIndexToEdit
         Returns the index of the edge to edit.  
             
         
        """
        pass
    @EdgeIndexToEdit.setter
    def EdgeIndexToEdit(self, index: int):
        """
        Setter for property: (int) EdgeIndexToEdit
         Returns the index of the edge to edit.  
             
         
        """
        pass
    @property
    def EditType(self) -> QuickBinderBuilder.EditTypes:
        """
        Getter for property: ( QuickBinderBuilder.EditTypes NXOp) EditType
         Returns the type edit to be performed on the face or edge.  
             
         
        """
        pass
    @EditType.setter
    def EditType(self, type: QuickBinderBuilder.EditTypes):
        """
        Setter for property: ( QuickBinderBuilder.EditTypes NXOp) EditType
         Returns the type edit to be performed on the face or edge.  
             
         
        """
        pass
    @property
    def End(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) End
         Returns the end length extension.  
             
         
        """
        pass
    @property
    def EndAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndAngle
         Returns the end angle of a planar face.  
            This angle rotates the side edge around the face normal with 
                    the rotation point being one of the endpoints of the edge that is attached to the previous face.
                  
         
        """
        pass
    @property
    def Extend(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Extend
         Returns the value to extend both sides of a face.  
             
         
        """
        pass
    @property
    def FaceIndexToEdit(self) -> int:
        """
        Getter for property: (int) FaceIndexToEdit
         Returns the index of the face to edit.  
             
         
        """
        pass
    @FaceIndexToEdit.setter
    def FaceIndexToEdit(self, index: int):
        """
        Setter for property: (int) FaceIndexToEdit
         Returns the index of the face to edit.  
             
         
        """
        pass
    @property
    def Faces(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Faces
         Returns the product faces used to perform the initial approximation.  
             
         
        """
        pass
    @property
    def Limits(self) -> NXOpen.GeometricUtilities.Limits:
        """
        Getter for property: ( NXOpen.GeometricUtilities.Limits) Limits
         Returns the central angle limits of cylindercone.  
             
         
        """
        pass
    @property
    def OriginAnchorOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) OriginAnchorOrigin
         Returns the anchor origin of binder sheet body.  
             
         
        """
        pass
    @OriginAnchorOrigin.setter
    def OriginAnchorOrigin(self, origin: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) OriginAnchorOrigin
         Returns the anchor origin of binder sheet body.  
             
         
        """
        pass
    @property
    def Radius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Radius
         Returns the radius value of a cylidrical face.  
            
         
        """
        pass
    @property
    def Start(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Start
         Returns the start length extension.  
             
         
        """
        pass
    @property
    def StartAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartAngle
         Returns the start angle of a planar face.  
            This angle rotates the side edge around the face normal with 
                    the rotation point being one of the endpoints of the edge that is attached to the previous face.
                  
         
        """
        pass
    @property
    def TopRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TopRadius
         Returns the top radius for a cone.  
             
         
        """
        pass
    @property
    def TransformMatrix(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: ( NXOpen.Matrix3x3) TransformMatrix
         Returns the rotation matrix of binder sheet body transformation.  
             
         
        """
        pass
    @TransformMatrix.setter
    def TransformMatrix(self, matrix: NXOpen.Matrix3x3):
        """
        Setter for property: ( NXOpen.Matrix3x3) TransformMatrix
         Returns the rotation matrix of binder sheet body transformation.  
             
         
        """
        pass
    @property
    def TransformOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) TransformOrigin
         Returns the new origin of binder sheet body transformation.  
             
         
        """
        pass
    @TransformOrigin.setter
    def TransformOrigin(self, origin: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) TransformOrigin
         Returns the new origin of binder sheet body transformation.  
             
         
        """
        pass
    @property
    def Type(self) -> QuickBinderBuilder.Types:
        """
        Getter for property: ( QuickBinderBuilder.Types NXOp) Type
         Returns the type of initial face created by approximating the faces indicated by
                     NXOpen::Die::QuickBinderBuilder::Faces .  
          
                  
         
        """
        pass
    @Type.setter
    def Type(self, type: QuickBinderBuilder.Types):
        """
        Setter for property: ( QuickBinderBuilder.Types NXOp) Type
         Returns the type of initial face created by approximating the faces indicated by
                     NXOpen::Die::QuickBinderBuilder::Faces .  
          
                  
         
        """
        pass
    @property
    def UMaximum(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) UMaximum
         Returns the u maximum extension distance.  
             
         
        """
        pass
    @property
    def UMinimum(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) UMinimum
         Returns the u minimum extension distance.  
             
         
        """
        pass
    @property
    def VMaximum(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) VMaximum
         Returns the v maximum extension distance.  
             
         
        """
        pass
    @property
    def VMinimum(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) VMinimum
         Returns the v minimum extension distance.  
             
         
        """
        pass
    def AddFace(self, type: QuickBinderBuilder.Types) -> int:
        """
         Add a component face to the binder body. 
         Returns faceIndex (int):  index of component face created .
        """
        pass
    def CreateAnchorFace(self) -> int:
        """
         Create initial face approximated from the selected faces. 
         Returns faceIndex (int):  index of anchor face created .
        """
        pass
    def EditFace(self) -> None:
        """
         Edit the parameters of a face according to the type of edit previously indicated by 
                    NXOpen.Die.QuickBinderBuilder.EditType.
                
        """
        pass
    def GetEdgesOfFace(self, faceIndex: int) -> Tuple[List[int], List[NXOpen.Point3d]]:
        """
         Get the edge indexes for a face.  Also returns corresponding points for each edge to be used as input to
                    NXOpen.Die.QuickBinderBuilder.SetReferencePoint.
                
         Returns A tuple consisting of (edgeIndex, referencePoints). 
         - edgeIndex is: List[int]. edge indexes .
         - referencePoints is:  NXOpen.Point3d Li. reference points corresponding to each edge .

        """
        pass
    def RemoveFace(self) -> None:
        """
         Remove a face from the binder body.  Face to remove is indicated by 
                    NXOpen.Die.QuickBinderBuilder.FaceIndexToEdit.
                
        """
        pass
    def SetReferencePoint(self, location: NXOpen.Point3d) -> None:
        """
         Set the point used to determine the start and end side of the face. Also used to determine
                    which end of the conic to edit.
                
        """
        pass
import NXOpen
import NXOpen.Features
class QuickBinderWrapBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a NXOpen.Die.QuickBinderWrapBuilder builder
    """
    class EditSizeType(Enum):
        """
        Members Include: 
         |Radius|  
         |Scale|  

        """
        Radius: int
        Scale: int
        @staticmethod
        def ValueOf(value: int) -> QuickBinderWrapBuilder.EditSizeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |Planar|  Planar 
         |Cylindrical|  Cylidrical 
         |Conical|  Conical 

        """
        Planar: int
        Cylindrical: int
        Conical: int
        @staticmethod
        def ValueOf(value: int) -> QuickBinderWrapBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Button(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: ( NXOpen.SelectBodyList) Button
         Returns the button   
            
         
        """
        pass
    @property
    def ChangeRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ChangeRadius
         Returns the change radius value   
            
         
        """
        pass
    @property
    def EditSizeChoice(self) -> QuickBinderWrapBuilder.EditSizeType:
        """
        Getter for property: ( QuickBinderWrapBuilder.EditSizeType NXOp) EditSizeChoice
         Returns the edit size choice   
            
         
        """
        pass
    @EditSizeChoice.setter
    def EditSizeChoice(self, sizeChoice: QuickBinderWrapBuilder.EditSizeType):
        """
        Setter for property: ( QuickBinderWrapBuilder.EditSizeType NXOp) EditSizeChoice
         Returns the edit size choice   
            
         
        """
        pass
    @property
    def Matrix(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: ( NXOpen.Matrix3x3) Matrix
         Returns the rotation matrix   
            
         
        """
        pass
    @Matrix.setter
    def Matrix(self, matrix: NXOpen.Matrix3x3):
        """
        Setter for property: ( NXOpen.Matrix3x3) Matrix
         Returns the rotation matrix   
            
         
        """
        pass
    @property
    def Origin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) Origin
         Returns the origin   
            
         
        """
        pass
    @Origin.setter
    def Origin(self, origin: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) Origin
         Returns the origin   
            
         
        """
        pass
    @property
    def Type(self) -> QuickBinderWrapBuilder.Types:
        """
        Getter for property: ( QuickBinderWrapBuilder.Types NXOp) Type
         Returns the method   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: QuickBinderWrapBuilder.Types):
        """
        Setter for property: ( QuickBinderWrapBuilder.Types NXOp) Type
         Returns the method   
            
         
        """
        pass
    @property
    def UMaximum(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) UMaximum
         Returns the maximum U value   
            
         
        """
        pass
    @property
    def UMinimum(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) UMinimum
         Returns the minumum U value   
            
         
        """
        pass
    @property
    def VMaximum(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) VMaximum
         Returns the maximum V value   
            
         
        """
        pass
    @property
    def VMinimum(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) VMinimum
         Returns the minumum V value   
            
         
        """
        pass
import NXOpen
import NXOpen.Features
class RibChildBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Die Rib Child sub feature. """
    @property
    def AdjustedThickness(self) -> float:
        """
        Getter for property: (float) AdjustedThickness
         Returns the adjusted thickness of the die rib.  
             
         
        """
        pass
    @AdjustedThickness.setter
    def AdjustedThickness(self, adjusted_thickness: float):
        """
        Setter for property: (float) AdjustedThickness
         Returns the adjusted thickness of the die rib.  
             
         
        """
        pass
    @property
    def Angle(self) -> float:
        """
        Getter for property: (float) Angle
         Returns the angle of the die rib.  
             
         
        """
        pass
    @Angle.setter
    def Angle(self, angle: float):
        """
        Setter for property: (float) Angle
         Returns the angle of the die rib.  
             
         
        """
        pass
    @property
    def Bottom(self) -> NXOpen.IOrientation:
        """
        Getter for property: ( NXOpen.IOrientation) Bottom
         Returns the bottom limit geometry of the die rib.  
             
         
        """
        pass
    @Bottom.setter
    def Bottom(self, bottom: NXOpen.IOrientation):
        """
        Setter for property: ( NXOpen.IOrientation) Bottom
         Returns the bottom limit geometry of the die rib.  
             
         
        """
        pass
    @property
    def BottomEnd(self) -> NXOpen.IOrientation:
        """
        Getter for property: ( NXOpen.IOrientation) BottomEnd
         Returns the bottom end limit geometry of the die rib.  
             
         
        """
        pass
    @BottomEnd.setter
    def BottomEnd(self, bottom_end: NXOpen.IOrientation):
        """
        Setter for property: ( NXOpen.IOrientation) BottomEnd
         Returns the bottom end limit geometry of the die rib.  
             
         
        """
        pass
    @property
    def BottomHorizontalOffset(self) -> float:
        """
        Getter for property: (float) BottomHorizontalOffset
         Returns the bottom horizontal offset of the die rib.  
             
         
        """
        pass
    @BottomHorizontalOffset.setter
    def BottomHorizontalOffset(self, bottom_horizontal_offset: float):
        """
        Setter for property: (float) BottomHorizontalOffset
         Returns the bottom horizontal offset of the die rib.  
             
         
        """
        pass
    @property
    def BottomLimitOffset(self) -> float:
        """
        Getter for property: (float) BottomLimitOffset
         Returns the bottom limit offset of the die rib.  
             
         
        """
        pass
    @BottomLimitOffset.setter
    def BottomLimitOffset(self, bottom_limit_offset: float):
        """
        Setter for property: (float) BottomLimitOffset
         Returns the bottom limit offset of the die rib.  
             
         
        """
        pass
    @property
    def BottomVerticalOffset(self) -> float:
        """
        Getter for property: (float) BottomVerticalOffset
         Returns the bottom vertical offset of the die rib.  
             
         
        """
        pass
    @BottomVerticalOffset.setter
    def BottomVerticalOffset(self, bottom_vertical_offset: float):
        """
        Setter for property: (float) BottomVerticalOffset
         Returns the bottom vertical offset of the die rib.  
             
         
        """
        pass
    @property
    def BuildStatus(self) -> DieBuildStatusOption:
        """
        Getter for property: ( DieBuildStatusOption NXOp) BuildStatus
         Returns the build status of the die rib.  
             
         
        """
        pass
    @property
    def CenterlineXyOffset(self) -> float:
        """
        Getter for property: (float) CenterlineXyOffset
         Returns the centerline xy offset of the die rib.  
             
         
        """
        pass
    @CenterlineXyOffset.setter
    def CenterlineXyOffset(self, centerline_xy_offset: float):
        """
        Setter for property: (float) CenterlineXyOffset
         Returns the centerline xy offset of the die rib.  
             
         
        """
        pass
    @property
    def DesignStatus(self) -> bool:
        """
        Getter for property: (bool) DesignStatus
         Returns the design status of the die rib, if true the rib will be built into the model, if false it will not.  
             
         
        """
        pass
    @DesignStatus.setter
    def DesignStatus(self, design_status: bool):
        """
        Setter for property: (bool) DesignStatus
         Returns the design status of the die rib, if true the rib will be built into the model, if false it will not.  
             
         
        """
        pass
    @property
    def DisplayStatus(self) -> bool:
        """
        Getter for property: (bool) DisplayStatus
         Returns the display status of the die rib, if true input data to the rib will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    @DisplayStatus.setter
    def DisplayStatus(self, display_status: bool):
        """
        Setter for property: (bool) DisplayStatus
         Returns the display status of the die rib, if true input data to the rib will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    @property
    def Height(self) -> float:
        """
        Getter for property: (float) Height
         Returns the height of the die rib.  
             
         
        """
        pass
    @Height.setter
    def Height(self, height: float):
        """
        Setter for property: (float) Height
         Returns the height of the die rib.  
             
         
        """
        pass
    @property
    def LccMinWidth(self) -> float:
        """
        Getter for property: (float) LccMinWidth
         Returns the lightening core mininum width of the die rib.  
             
         
        """
        pass
    @LccMinWidth.setter
    def LccMinWidth(self, lcc_min_width: float):
        """
        Setter for property: (float) LccMinWidth
         Returns the lightening core mininum width of the die rib.  
             
         
        """
        pass
    @property
    def LighteningCore(self) -> bool:
        """
        Getter for property: (bool) LighteningCore
         Returns the lightening core switch of the die rib, if true the lightening core will be built into the rib, if false it will not.  
             
         
        """
        pass
    @LighteningCore.setter
    def LighteningCore(self, lightening_core: bool):
        """
        Setter for property: (bool) LighteningCore
         Returns the lightening core switch of the die rib, if true the lightening core will be built into the rib, if false it will not.  
             
         
        """
        pass
    @property
    def LighteningCoreClearance(self) -> float:
        """
        Getter for property: (float) LighteningCoreClearance
         Returns the lightening core clearance of the die rib.  
             
         
        """
        pass
    @LighteningCoreClearance.setter
    def LighteningCoreClearance(self, lightening_core_clearance: float):
        """
        Setter for property: (float) LighteningCoreClearance
         Returns the lightening core clearance of the die rib.  
             
         
        """
        pass
    @property
    def Rectangular(self) -> bool:
        """
        Getter for property: (bool) Rectangular
         Returns the rectangular switch of the die rib, if true the lightening core will be rectangular, 
                if false it will follow the shape of the rib.  
             
         
        """
        pass
    @Rectangular.setter
    def Rectangular(self, rectangular: bool):
        """
        Setter for property: (bool) Rectangular
         Returns the rectangular switch of the die rib, if true the lightening core will be rectangular, 
                if false it will follow the shape of the rib.  
             
         
        """
        pass
    @property
    def Start(self) -> NXOpen.IOrientation:
        """
        Getter for property: ( NXOpen.IOrientation) Start
         Returns the start limit geometry of the die rib.  
             
         
        """
        pass
    @Start.setter
    def Start(self, start: NXOpen.IOrientation):
        """
        Setter for property: ( NXOpen.IOrientation) Start
         Returns the start limit geometry of the die rib.  
             
         
        """
        pass
    @property
    def Thickness(self) -> float:
        """
        Getter for property: (float) Thickness
         Returns the thickness of the die rib.  
             
         
        """
        pass
    @Thickness.setter
    def Thickness(self, thickness: float):
        """
        Setter for property: (float) Thickness
         Returns the thickness of the die rib.  
             
         
        """
        pass
    @property
    def Top(self) -> NXOpen.IOrientation:
        """
        Getter for property: ( NXOpen.IOrientation) Top
         Returns the top limit geometry of the die rib.  
             
         
        """
        pass
    @Top.setter
    def Top(self, top: NXOpen.IOrientation):
        """
        Setter for property: ( NXOpen.IOrientation) Top
         Returns the top limit geometry of the die rib.  
             
         
        """
        pass
    @property
    def TopEnd(self) -> NXOpen.IOrientation:
        """
        Getter for property: ( NXOpen.IOrientation) TopEnd
         Returns the top end limit geometry of the die rib.  
             
         
        """
        pass
    @TopEnd.setter
    def TopEnd(self, top_end: NXOpen.IOrientation):
        """
        Setter for property: ( NXOpen.IOrientation) TopEnd
         Returns the top end limit geometry of the die rib.  
             
         
        """
        pass
    @property
    def TopHorizontalOffset(self) -> float:
        """
        Getter for property: (float) TopHorizontalOffset
         Returns the top horizontal offset of the die rib.  
             
         
        """
        pass
    @TopHorizontalOffset.setter
    def TopHorizontalOffset(self, top_horizontal_offset: float):
        """
        Setter for property: (float) TopHorizontalOffset
         Returns the top horizontal offset of the die rib.  
             
         
        """
        pass
    @property
    def TopLimitOffset(self) -> float:
        """
        Getter for property: (float) TopLimitOffset
         Returns the top limit offset of the die rib.  
             
         
        """
        pass
    @TopLimitOffset.setter
    def TopLimitOffset(self, top_limit_offset: float):
        """
        Setter for property: (float) TopLimitOffset
         Returns the top limit offset of the die rib.  
             
         
        """
        pass
    @property
    def TopVerticalOffset(self) -> float:
        """
        Getter for property: (float) TopVerticalOffset
         Returns the top vertical offset of the die rib.  
             
         
        """
        pass
    @TopVerticalOffset.setter
    def TopVerticalOffset(self, top_vertical_offset: float):
        """
        Setter for property: (float) TopVerticalOffset
         Returns the top vertical offset of the die rib.  
             
         
        """
        pass
    @overload
    def GetBottomEnd(self) -> Tuple[List[NXOpen.IProfile], DirectionOption]:
        """
         Gets the bottom end limit geometry of the die rib as a profile. 
         Returns A tuple consisting of (profile_entries, direction). 
         - profile_entries is:  NXOpen.IProfile Li. The profile entries, will be curves, edges, faces, sketches or curve features. .
         - direction is:  DirectionOption NXOp. Profile direction. .

        """
        pass
    def GetCenterline(self) -> Tuple[List[NXOpen.IProfile], DirectionOption]:
        """
         Gets the centerline of the rib. 
         Returns A tuple consisting of (profile_entries, direction). 
         - profile_entries is:  NXOpen.IProfile Li. The profile entries, will be curves, edges, faces, sketches or curve features. .
         - direction is:  DirectionOption NXOp. Profile direction. .

        """
        pass
    @overload
    def GetStart(self) -> Tuple[List[NXOpen.IProfile], DirectionOption]:
        """
         Gets the start limit geometry of the die rib as a profile. 
         Returns A tuple consisting of (profile_entries, direction). 
         - profile_entries is:  NXOpen.IProfile Li. The profile entries, will be curves, edges, faces, sketches or curve features. .
         - direction is:  DirectionOption NXOp. Profile direction. .

        """
        pass
    @overload
    def GetTopEnd(self) -> Tuple[List[NXOpen.IProfile], DirectionOption]:
        """
         Gets the top end limit geometry of the die rib as a profile. 
         Returns A tuple consisting of (profile_entries, direction). 
         - profile_entries is:  NXOpen.IProfile Li. The profile entries, will be curves, edges, faces, sketches or curve features. .
         - direction is:  DirectionOption NXOp. Profile direction. .

        """
        pass
    @overload
    def SetBottomEnd(self, direction: DirectionOption, profile_entries: List[NXOpen.IProfile]) -> None:
        """
         Sets the bottom end limit geometry of the die rib using a profile. 
        """
        pass
    def SetCenterline(self, direction: DirectionOption, profile_entries: List[NXOpen.IProfile]) -> None:
        """
         Sets the centerline of the rib. 
        """
        pass
    @overload
    def SetStart(self, direction: DirectionOption, profile_entries: List[NXOpen.IProfile]) -> None:
        """
         Sets the start limit geometry of the die rib using a profile. 
        """
        pass
    @overload
    def SetTopEnd(self, direction: DirectionOption, profile_entries: List[NXOpen.IProfile]) -> None:
        """
         Sets the top end limit geometry of the die rib using a profile. 
        """
        pass
import NXOpen.Features
class RibParentBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Die Rib Parent sub feature. """
    @property
    def AdjustedThickness(self) -> float:
        """
        Getter for property: (float) AdjustedThickness
         Returns the adjusted thickness of die ribs.  
             
         
        """
        pass
    @AdjustedThickness.setter
    def AdjustedThickness(self, adjusted_thickness: float):
        """
        Setter for property: (float) AdjustedThickness
         Returns the adjusted thickness of die ribs.  
             
         
        """
        pass
    @property
    def Angle(self) -> float:
        """
        Getter for property: (float) Angle
         Returns the angle of die ribs.  
             
         
        """
        pass
    @Angle.setter
    def Angle(self, angle: float):
        """
        Setter for property: (float) Angle
         Returns the angle of die ribs.  
             
         
        """
        pass
    @property
    def BottomHorizontalOffset(self) -> float:
        """
        Getter for property: (float) BottomHorizontalOffset
         Returns the bottom horizontal offset of die ribs.  
             
         
        """
        pass
    @BottomHorizontalOffset.setter
    def BottomHorizontalOffset(self, bottom_horizontal_offset: float):
        """
        Setter for property: (float) BottomHorizontalOffset
         Returns the bottom horizontal offset of die ribs.  
             
         
        """
        pass
    @property
    def BottomLimitOffset(self) -> float:
        """
        Getter for property: (float) BottomLimitOffset
         Returns the bottom limit offset of die ribs.  
             
         
        """
        pass
    @BottomLimitOffset.setter
    def BottomLimitOffset(self, bottom_limit_offset: float):
        """
        Setter for property: (float) BottomLimitOffset
         Returns the bottom limit offset of die ribs.  
             
         
        """
        pass
    @property
    def BottomVerticalOffset(self) -> float:
        """
        Getter for property: (float) BottomVerticalOffset
         Returns the bottom vertical offset of die ribs.  
             
         
        """
        pass
    @BottomVerticalOffset.setter
    def BottomVerticalOffset(self, bottom_vertical_offset: float):
        """
        Setter for property: (float) BottomVerticalOffset
         Returns the bottom vertical offset of die ribs.  
             
         
        """
        pass
    @property
    def BuildStatus(self) -> DieBuildStatusOption:
        """
        Getter for property: ( DieBuildStatusOption NXOp) BuildStatus
         Returns the build status of die ribs.  
             
         
        """
        pass
    @property
    def CenterlineXyOffset(self) -> float:
        """
        Getter for property: (float) CenterlineXyOffset
         Returns the centerline xy offset of die ribs.  
             
         
        """
        pass
    @CenterlineXyOffset.setter
    def CenterlineXyOffset(self, centerline_xy_offset: float):
        """
        Setter for property: (float) CenterlineXyOffset
         Returns the centerline xy offset of die ribs.  
             
         
        """
        pass
    @property
    def DesignStatus(self) -> bool:
        """
        Getter for property: (bool) DesignStatus
         Returns the design status of die ribs, if true the ribs will be built into the model, if false they will not.  
             
         
        """
        pass
    @DesignStatus.setter
    def DesignStatus(self, design_status: bool):
        """
        Setter for property: (bool) DesignStatus
         Returns the design status of die ribs, if true the ribs will be built into the model, if false they will not.  
             
         
        """
        pass
    @property
    def DisplayStatus(self) -> bool:
        """
        Getter for property: (bool) DisplayStatus
         Returns the display status of die ribs, if true input data to the ribs will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    @DisplayStatus.setter
    def DisplayStatus(self, display_status: bool):
        """
        Setter for property: (bool) DisplayStatus
         Returns the display status of die ribs, if true input data to the ribs will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    @property
    def Height(self) -> float:
        """
        Getter for property: (float) Height
         Returns the height of die ribs.  
             
         
        """
        pass
    @Height.setter
    def Height(self, height: float):
        """
        Setter for property: (float) Height
         Returns the height of die ribs.  
             
         
        """
        pass
    @property
    def LccMinWidth(self) -> float:
        """
        Getter for property: (float) LccMinWidth
         Returns the lightening core mininum width of die ribs.  
             
         
        """
        pass
    @LccMinWidth.setter
    def LccMinWidth(self, lcc_min_width: float):
        """
        Setter for property: (float) LccMinWidth
         Returns the lightening core mininum width of die ribs.  
             
         
        """
        pass
    @property
    def LighteningCore(self) -> bool:
        """
        Getter for property: (bool) LighteningCore
         Returns the lightening core switch of die ribs, if true the lightening core will be built into the rib, if false it will not.  
             
         
        """
        pass
    @LighteningCore.setter
    def LighteningCore(self, lightening_core: bool):
        """
        Setter for property: (bool) LighteningCore
         Returns the lightening core switch of die ribs, if true the lightening core will be built into the rib, if false it will not.  
             
         
        """
        pass
    @property
    def LighteningCoreClearance(self) -> float:
        """
        Getter for property: (float) LighteningCoreClearance
         Returns the lightening core clearance of die ribs.  
             
         
        """
        pass
    @LighteningCoreClearance.setter
    def LighteningCoreClearance(self, lightening_core_clearance: float):
        """
        Setter for property: (float) LighteningCoreClearance
         Returns the lightening core clearance of die ribs.  
             
         
        """
        pass
    @property
    def Rectangular(self) -> bool:
        """
        Getter for property: (bool) Rectangular
         Returns the rectangular switch of die ribs, if true the lightening cores will be rectangular, 
                if false they will follow the shape of the rib.  
             
         
        """
        pass
    @Rectangular.setter
    def Rectangular(self, rectangular: bool):
        """
        Setter for property: (bool) Rectangular
         Returns the rectangular switch of die ribs, if true the lightening cores will be rectangular, 
                if false they will follow the shape of the rib.  
             
         
        """
        pass
    @property
    def Thickness(self) -> float:
        """
        Getter for property: (float) Thickness
         Returns the thickness of die ribs.  
             
         
        """
        pass
    @Thickness.setter
    def Thickness(self, thickness: float):
        """
        Setter for property: (float) Thickness
         Returns the thickness of die ribs.  
             
         
        """
        pass
    @property
    def TopHorizontalOffset(self) -> float:
        """
        Getter for property: (float) TopHorizontalOffset
         Returns the top horizontal offset of die ribs.  
             
         
        """
        pass
    @TopHorizontalOffset.setter
    def TopHorizontalOffset(self, top_horizontal_offset: float):
        """
        Setter for property: (float) TopHorizontalOffset
         Returns the top horizontal offset of die ribs.  
             
         
        """
        pass
    @property
    def TopLimitOffset(self) -> float:
        """
        Getter for property: (float) TopLimitOffset
         Returns the top limit offset of die ribs.  
             
         
        """
        pass
    @TopLimitOffset.setter
    def TopLimitOffset(self, top_limit_offset: float):
        """
        Setter for property: (float) TopLimitOffset
         Returns the top limit offset of die ribs.  
             
         
        """
        pass
    @property
    def TopVerticalOffset(self) -> float:
        """
        Getter for property: (float) TopVerticalOffset
         Returns the top vertical offset of die ribs.  
             
         
        """
        pass
    @TopVerticalOffset.setter
    def TopVerticalOffset(self, top_vertical_offset: float):
        """
        Setter for property: (float) TopVerticalOffset
         Returns the top vertical offset of die ribs.  
             
         
        """
        pass
    @property
    def XDistance(self) -> float:
        """
        Getter for property: (float) XDistance
         Returns the x distance of die ribs.  
             
         
        """
        pass
    @XDistance.setter
    def XDistance(self, x_distance: float):
        """
        Setter for property: (float) XDistance
         Returns the x distance of die ribs.  
             
         
        """
        pass
    @property
    def XOffset(self) -> float:
        """
        Getter for property: (float) XOffset
         Returns the x offset of die ribs.  
             
         
        """
        pass
    @XOffset.setter
    def XOffset(self, x_offset: float):
        """
        Setter for property: (float) XOffset
         Returns the x offset of die ribs.  
             
         
        """
        pass
    @property
    def YDistance(self) -> float:
        """
        Getter for property: (float) YDistance
         Returns the y distance of die ribs.  
             
         
        """
        pass
    @YDistance.setter
    def YDistance(self, y_distance: float):
        """
        Setter for property: (float) YDistance
         Returns the y distance of die ribs.  
             
         
        """
        pass
    @property
    def YOffset(self) -> float:
        """
        Getter for property: (float) YOffset
         Returns the y offset of die ribs.  
             
         
        """
        pass
    @YOffset.setter
    def YOffset(self, y_offset: float):
        """
        Setter for property: (float) YOffset
         Returns the y offset of die ribs.  
             
         
        """
        pass
    def CreateChild(self) -> RibChildBuilder:
        """
         Creates a child rib. 
         Returns dieribchild ( RibChildBuilder NXOp):  .
        """
        pass
    def DeleteChild(self, dieribchild: RibChildBuilder) -> None:
        """
         Deletes a child rib. 
        """
        pass
    def GetChildren(self) -> List[RibChildBuilder]:
        """
         Outputs the child ribs. 
         Returns children ( RibChildBuilder List[NX):  The child ribs. .
        """
        pass
import NXOpen
import NXOpen.Features
class RotorBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a CAM Rotor feature builder. """
    @property
    def AirCylinderParent(self) -> PadParentBuilder:
        """
        Getter for property: ( PadParentBuilder NXOp) AirCylinderParent
         Returns the air cylinder parent builder of the rotor.  
             
         
        """
        pass
    @property
    def AngleTolerance(self) -> float:
        """
        Getter for property: (float) AngleTolerance
         Returns the angle tolerance of the rotor casting.  
             
         
        """
        pass
    @AngleTolerance.setter
    def AngleTolerance(self, angle_tolerance: float):
        """
        Setter for property: (float) AngleTolerance
         Returns the angle tolerance of the rotor casting.  
             
         
        """
        pass
    @property
    def BoltHoleParent(self) -> HoleParentBuilder:
        """
        Getter for property: ( HoleParentBuilder NXOp) BoltHoleParent
         Returns the bolt holes parent builder of the rotor.  
             
         
        """
        pass
    @property
    def DisplayHoles(self) -> bool:
        """
        Getter for property: (bool) DisplayHoles
         Returns the display holes of the rotor casting.  
             
         
        """
        pass
    @DisplayHoles.setter
    def DisplayHoles(self, display_holes: bool):
        """
        Setter for property: (bool) DisplayHoles
         Returns the display holes of the rotor casting.  
             
         
        """
        pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance of the rotor casting.  
             
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distance_tolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance of the rotor casting.  
             
         
        """
        pass
    @property
    def DowelHoleParent(self) -> HoleParentBuilder:
        """
        Getter for property: ( HoleParentBuilder NXOp) DowelHoleParent
         Returns the dowel holes parent builder of the rotor.  
             
         
        """
        pass
    @property
    def EndStopsParent(self) -> PadParentBuilder:
        """
        Getter for property: ( PadParentBuilder NXOp) EndStopsParent
         Returns the end stops parent builder of the rotor.  
             
         
        """
        pass
    @property
    def HandlingHoleParent(self) -> HoleParentBuilder:
        """
        Getter for property: ( HoleParentBuilder NXOp) HandlingHoleParent
         Returns the handling holes parent builder of the rotor.  
             
         
        """
        pass
    @property
    def PressDirection(self) -> NXOpen.IReferenceAxis:
        """
        Getter for property: ( NXOpen.IReferenceAxis) PressDirection
         Returns the press direction of the rotor casting.  
             
         
        """
        pass
    @PressDirection.setter
    def PressDirection(self, press_direction: NXOpen.IReferenceAxis):
        """
        Setter for property: ( NXOpen.IReferenceAxis) PressDirection
         Returns the press direction of the rotor casting.  
             
         
        """
        pass
    @property
    def RotorRotationAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RotorRotationAngle
         Returns the rotor rotation angle value of the rotor casting.  
             
         
        """
        pass
    @property
    def RotorSolid(self) -> NXOpen.Body:
        """
        Getter for property: ( NXOpen.Body) RotorSolid
         Returns the rotor solid of the rotor casting.  
             
         
        """
        pass
    @RotorSolid.setter
    def RotorSolid(self, rotor_solid: NXOpen.Body):
        """
        Setter for property: ( NXOpen.Body) RotorSolid
         Returns the rotor solid of the rotor casting.  
             
         
        """
        pass
    @property
    def Section(self) -> RotorSectionBuilder:
        """
        Getter for property: ( RotorSectionBuilder NXOp) Section
         Returns the section builder of the rotor.  
             
         
        """
        pass
    @property
    def SensorParent(self) -> PadParentBuilder:
        """
        Getter for property: ( PadParentBuilder NXOp) SensorParent
         Returns the sensor parent builder of the rotor.  
             
         
        """
        pass
    @property
    def SetupBlocksParent(self) -> PadParentBuilder:
        """
        Getter for property: ( PadParentBuilder NXOp) SetupBlocksParent
         Returns the setup blocks parent builder of the rotor.  
             
         
        """
        pass
    @property
    def SheetMetal(self) -> NXOpen.Body:
        """
        Getter for property: ( NXOpen.Body) SheetMetal
         Returns the sheet metal of the rotor casting.  
             
         
        """
        pass
    @SheetMetal.setter
    def SheetMetal(self, sheet_metal: NXOpen.Body):
        """
        Setter for property: ( NXOpen.Body) SheetMetal
         Returns the sheet metal of the rotor casting.  
             
         
        """
        pass
    @property
    def TbarHoleParent(self) -> HoleParentBuilder:
        """
        Getter for property: ( HoleParentBuilder NXOp) TbarHoleParent
         Returns the T-bar holes parent builder of the rotor.  
             
         
        """
        pass
    @property
    def ThroatDefinitionParent(self) -> ThroatParentBuilder:
        """
        Getter for property: ( ThroatParentBuilder NXOp) ThroatDefinitionParent
         Returns the throat definition parent builder of the rotor.  
             
         
        """
        pass
    @property
    def ThroatOrientation(self) -> NXOpen.CartesianCoordinateSystem:
        """
        Getter for property: ( NXOpen.CartesianCoordinateSystem) ThroatOrientation
         Returns the throat orientation of the rotor casting.  
             
         
        """
        pass
    @ThroatOrientation.setter
    def ThroatOrientation(self, throat_orientation: NXOpen.CartesianCoordinateSystem):
        """
        Setter for property: ( NXOpen.CartesianCoordinateSystem) ThroatOrientation
         Returns the throat orientation of the rotor casting.  
             
         
        """
        pass
    @property
    def WearPlateLocatorsParent(self) -> WearPlateLocParentBuilder:
        """
        Getter for property: ( WearPlateLocParentBuilder NXOp) WearPlateLocatorsParent
         Returns the wear plate and locator parent builder of the rotor.  
             
         
        """
        pass
    def GetEndOfFlangeProfile(self) -> Tuple[List[NXOpen.IProfile], DirectionOption]:
        """
         Gets the end of flange profile of the die rotor casting. 
         Returns A tuple consisting of (profile_entries, direction). 
         - profile_entries is:  NXOpen.IProfile Li. The profile entries, will be curves, edges, faces, sketches or curve features. .
         - direction is:  DirectionOption NXOp. Profile direction. .

        """
        pass
    def GetEndOrientation(self) -> List[NXOpen.ISurface]:
        """
         Gets the end orientation of the rotor casting. 
         Returns end_entries ( NXOpen.ISurface Li):  .
        """
        pass
    def GetFlangeBendProfile(self) -> Tuple[List[NXOpen.IProfile], DirectionOption]:
        """
         Gets the flange bend profile of the rotor casting. 
         Returns A tuple consisting of (profile_entries, direction). 
         - profile_entries is:  NXOpen.IProfile Li. The profile entries, will be curves, edges, faces, sketches or curve features. .
         - direction is:  DirectionOption NXOp. Profile direction. .

        """
        pass
    def GetStartOrientation(self) -> List[NXOpen.ISurface]:
        """
         Gets the start orientation of the rotor casting. 
         Returns start_entries ( NXOpen.ISurface Li):  .
        """
        pass
    def SetEndOfFlangeProfile(self, direction: DirectionOption, profile_entries: List[NXOpen.IProfile]) -> None:
        """
         Sets the end of flange profile of the die rotor casting. 
        """
        pass
    def SetEndOrientation(self, end_entries: List[NXOpen.ISurface]) -> None:
        """
         Sets the end orientation of the rotor casting. 
        """
        pass
    def SetFlangeBendProfile(self, direction: DirectionOption, profile_entries: List[NXOpen.IProfile]) -> None:
        """
         Sets the flange bend profile of the rotor casting. 
        """
        pass
    def SetRotorRotationAngle(self, degrees: str) -> None:
        """
         
        """
        pass
    def SetStartOrientation(self, start_entries: List[NXOpen.ISurface]) -> None:
        """
         Sets the start orientation of the rotor casting. 
        """
        pass
import NXOpen
import NXOpen.Features
class RotorSectionBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Rotor Section sub feature. """
    @property
    def BuildStatus(self) -> DieBuildStatusOption:
        """
        Getter for property: ( DieBuildStatusOption NXOp) BuildStatus
         Returns the build status of the die rotor casting   
            
         
        """
        pass
    @property
    def DesignStatus(self) -> bool:
        """
        Getter for property: (bool) DesignStatus
         Returns the design status of the die rotor casting   
            
         
        """
        pass
    @DesignStatus.setter
    def DesignStatus(self, design_status: bool):
        """
        Setter for property: (bool) DesignStatus
         Returns the design status of the die rotor casting   
            
         
        """
        pass
    @property
    def DisplayStatus(self) -> bool:
        """
        Getter for property: (bool) DisplayStatus
         Returns the display status of the die rotor casting   
            
         
        """
        pass
    @DisplayStatus.setter
    def DisplayStatus(self, display_status: bool):
        """
        Setter for property: (bool) DisplayStatus
         Returns the display status of the die rotor casting   
            
         
        """
        pass
    @property
    def MinimumCavityDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumCavityDepth
         Returns the throat minimum cavity depth of the die rotor casting   
            
         
        """
        pass
    @property
    def MinimumExtensionLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumExtensionLength
         Returns the throat minimum extension length of the die rotor casting   
            
         
        """
        pass
    def GetEndAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the end faces attributes 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. title for attribute .
         - value is: str. value of attribute .
         - color is: int. color of end faces .

        """
        pass
    def GetFlangeWallAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the flange wall faces attributes 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. title for attribute .
         - value is: str. value of attribute .
         - color is: int. color of flange wall faces .

        """
        pass
    def GetFormingAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the forming faces attributes 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. title for attribute .
         - value is: str. value of attribute .
         - color is: int. color of forming faces .

        """
        pass
    def GetRotorAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the rotor faces attributes 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. title for attribute .
         - value is: str. value of attribute .
         - color is: int. color of rotor faces .

        """
        pass
    def SetEndAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the end faces attributes 
        """
        pass
    def SetFlangeWallAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the flange wall faces attributes 
        """
        pass
    def SetFormingAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the forming faces attributes 
        """
        pass
    def SetMinimumCavityDepth(self, minimum_cavity_depth: str) -> None:
        """
         
        """
        pass
    def SetMinimumExtensionLength(self, minimum_extension_length: str) -> None:
        """
         
        """
        pass
    def SetRotorAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the rotor faces attributes 
        """
        pass
import NXOpen
import NXOpen.Facet
import NXOpen.Features
class SpringbackCompensationBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Used to create or edit a NXOpen.Die.SpringbackCompensation feature.
    """
    class DefinedByType(Enum):
        """
        Members Include: 
         |OneStepFeature|  A One-Step feature. 
         |FacetedBodies|  Facted bodies. 
         |Points|  Points . 

        """
        OneStepFeature: int
        FacetedBodies: int
        Points: int
        @staticmethod
        def ValueOf(value: int) -> SpringbackCompensationBuilder.DefinedByType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DegreeType(Enum):
        """
        Members Include: 
         |Two|  Degree is 2 
         |Three|  Degree is 3 
         |Five|  Degree is 5 
         |Seven|  Degree is 7 

        """
        Two: int
        Three: int
        Five: int
        Seven: int
        @staticmethod
        def ValueOf(value: int) -> SpringbackCompensationBuilder.DegreeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ResultSheetType(Enum):
        """
        Members Include: 
         |Compensated|  Compensated sheet body. 
         |Sprung|  Sprung sheet body. 

        """
        Compensated: int
        Sprung: int
        @staticmethod
        def ValueOf(value: int) -> SpringbackCompensationBuilder.ResultSheetType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngleTolerance(self) -> float:
        """
        Getter for property: (float) AngleTolerance
         Returns the angle tolerance.  
             
         
        """
        pass
    @AngleTolerance.setter
    def AngleTolerance(self, angleTolerance: float):
        """
        Setter for property: (float) AngleTolerance
         Returns the angle tolerance.  
             
         
        """
        pass
    @property
    def CalculateMaxDeviation(self) -> bool:
        """
        Getter for property: (bool) CalculateMaxDeviation
         Returns the indication if the feature should calculate the maximum deviation of the result.  
           True indicates the deviation should be calculated, false indicates the deviation will not be calculated.   
         
        """
        pass
    @CalculateMaxDeviation.setter
    def CalculateMaxDeviation(self, calculateMaxDeviation: bool):
        """
        Setter for property: (bool) CalculateMaxDeviation
         Returns the indication if the feature should calculate the maximum deviation of the result.  
           True indicates the deviation should be calculated, false indicates the deviation will not be calculated.   
         
        """
        pass
    @property
    def ConvexityDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ConvexityDirection
         Returns the convexity direction.  
             
         
        """
        pass
    @ConvexityDirection.setter
    def ConvexityDirection(self, convexityDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ConvexityDirection
         Returns the convexity direction.  
             
         
        """
        pass
    @property
    def ConvexityEnabled(self) -> bool:
        """
        Getter for property: (bool) ConvexityEnabled
         Returns the toggle that determines whether to constrain convexity   
            
         
        """
        pass
    @ConvexityEnabled.setter
    def ConvexityEnabled(self, isConvexityEnabled: bool):
        """
        Setter for property: (bool) ConvexityEnabled
         Returns the toggle that determines whether to constrain convexity   
            
         
        """
        pass
    @property
    def CreateFacets(self) -> bool:
        """
        Getter for property: (bool) CreateFacets
         Returns the value determines if a faceted output body is also created.  
           True indicates to output a faceted body, false indicates that a faceted body is not output.
                    Only when type is  Die::SpringbackCompensationBuilder::DefinedByTypeFacetedBodies 
                  
         
        """
        pass
    @CreateFacets.setter
    def CreateFacets(self, createFacets: bool):
        """
        Setter for property: (bool) CreateFacets
         Returns the value determines if a faceted output body is also created.  
           True indicates to output a faceted body, false indicates that a faceted body is not output.
                    Only when type is  Die::SpringbackCompensationBuilder::DefinedByTypeFacetedBodies 
                  
         
        """
        pass
    @property
    def DefinedBy(self) -> SpringbackCompensationBuilder.DefinedByType:
        """
        Getter for property: ( SpringbackCompensationBuilder.DefinedByType NXOp) DefinedBy
         Returns the type of data that will be used to define the feature.  
          
                       Die::SpringbackCompensationBuilder::DefinedByTypeOneStepFeature  
                    
                     Die::SpringbackCompensationBuilder::OneStep 
                    
                      
                       Die::SpringbackCompensationBuilder::DefinedByTypeFacetedBodies  
                    
                     Die::SpringbackCompensationBuilder::ProductSheet 
                     Die::SpringbackCompensationBuilder::ProductFacets 
                     Die::SpringbackCompensationBuilder::SprungFacets 
                    
                      
                       Die::SpringbackCompensationBuilder::DefinedByTypePoints  
                    
                     Die::SpringbackCompensationBuilder::ProductSheet 
                     Die::SpringbackCompensationBuilder::SetProductPoints 
                     Die::SpringbackCompensationBuilder::SetSprungPoints 
                    
                      
                  
         
        """
        pass
    @DefinedBy.setter
    def DefinedBy(self, definedBy: SpringbackCompensationBuilder.DefinedByType):
        """
        Setter for property: ( SpringbackCompensationBuilder.DefinedByType NXOp) DefinedBy
         Returns the type of data that will be used to define the feature.  
          
                       Die::SpringbackCompensationBuilder::DefinedByTypeOneStepFeature  
                    
                     Die::SpringbackCompensationBuilder::OneStep 
                    
                      
                       Die::SpringbackCompensationBuilder::DefinedByTypeFacetedBodies  
                    
                     Die::SpringbackCompensationBuilder::ProductSheet 
                     Die::SpringbackCompensationBuilder::ProductFacets 
                     Die::SpringbackCompensationBuilder::SprungFacets 
                    
                      
                       Die::SpringbackCompensationBuilder::DefinedByTypePoints  
                    
                     Die::SpringbackCompensationBuilder::ProductSheet 
                     Die::SpringbackCompensationBuilder::SetProductPoints 
                     Die::SpringbackCompensationBuilder::SetSprungPoints 
                    
                      
                  
         
        """
        pass
    @property
    def DeformationFactor(self) -> float:
        """
        Getter for property: (float) DeformationFactor
         Returns the deformation factor determines how much of the calculated deformation is applied to the result body.  
             
         
        """
        pass
    @DeformationFactor.setter
    def DeformationFactor(self, deformationFactor: float):
        """
        Setter for property: (float) DeformationFactor
         Returns the deformation factor determines how much of the calculated deformation is applied to the result body.  
             
         
        """
        pass
    @property
    def Degree(self) -> SpringbackCompensationBuilder.DegreeType:
        """
        Getter for property: ( SpringbackCompensationBuilder.DegreeType NXOp) Degree
         Returns the polynomial degree (one unit less than the order).  
             
         
        """
        pass
    @Degree.setter
    def Degree(self, degree: SpringbackCompensationBuilder.DegreeType):
        """
        Setter for property: ( SpringbackCompensationBuilder.DegreeType NXOp) Degree
         Returns the polynomial degree (one unit less than the order).  
             
         
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
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance.  
             
         
        """
        pass
    @property
    def Divisions(self) -> int:
        """
        Getter for property: (int) Divisions
         Returns the number of equi-distant points to divide the cube of the sheet body (N x N x N).  
              
         
        """
        pass
    @Divisions.setter
    def Divisions(self, divisions: int):
        """
        Setter for property: (int) Divisions
         Returns the number of equi-distant points to divide the cube of the sheet body (N x N x N).  
              
         
        """
        pass
    @property
    def DrawVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) DrawVector
         Returns the vector indicating the draw direction.  
             
         
        """
        pass
    @DrawVector.setter
    def DrawVector(self, drawVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) DrawVector
         Returns the vector indicating the draw direction.  
             
         
        """
        pass
    @property
    def InnerCurve(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) InnerCurve
         Returns the inner boundary curve of the transition area.  
             
         
        """
        pass
    @property
    def IsGlobalDeformation(self) -> bool:
        """
        Getter for property: (bool) IsGlobalDeformation
         Returns the indication if the feature is a generic Global Deformation.  
           True indicates the feature is a Global Deformation, false indicates the feature is not a Global Deformation.   
         
        """
        pass
    @IsGlobalDeformation.setter
    def IsGlobalDeformation(self, isGlobalDeformation: bool):
        """
        Setter for property: (bool) IsGlobalDeformation
         Returns the indication if the feature is a generic Global Deformation.  
           True indicates the feature is a Global Deformation, false indicates the feature is not a Global Deformation.   
         
        """
        pass
    @property
    def OneStep(self) -> NXOpen.Features.SelectFeature:
        """
        Getter for property: ( NXOpen.Features.SelectFeature) OneStep
         Returns the one-step feature.  
           Only when type is  Die::SpringbackCompensationBuilder::DefinedByTypeOneStepFeature .   
         
        """
        pass
    @property
    def OuterCurve(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) OuterCurve
         Returns the outer boundary curve of transition area.  
             
         
        """
        pass
    @property
    def ProductFacets(self) -> NXOpen.Facet.SelectFacetedBody:
        """
        Getter for property: ( NXOpen.Facet.SelectFacetedBody) ProductFacets
         Returns the product facets.  
           Only when type is  Die::SpringbackCompensationBuilder::DefinedByTypeFacetedBodies . Optional.   
         
        """
        pass
    @property
    def ProductPointsFile(self) -> str:
        """
        Getter for property: (str) ProductPointsFile
         Returns the product points file name.  
           This is saved for reference only. 
                    The product points are actually defined by calling  Die::SpringbackCompensationBuilder::SetProductPoints . 
                    Only when type is  Die::SpringbackCompensationBuilder::DefinedByTypePoints . Optional.
                  
         
        """
        pass
    @ProductPointsFile.setter
    def ProductPointsFile(self, filename: str):
        """
        Setter for property: (str) ProductPointsFile
         Returns the product points file name.  
           This is saved for reference only. 
                    The product points are actually defined by calling  Die::SpringbackCompensationBuilder::SetProductPoints . 
                    Only when type is  Die::SpringbackCompensationBuilder::DefinedByTypePoints . Optional.
                  
         
        """
        pass
    @property
    def ProductSheet(self) -> NXOpen.SelectBody:
        """
        Getter for property: ( NXOpen.SelectBody) ProductSheet
         Returns the sheet body representing the product shape.  
           Only when type is  Die::SpringbackCompensationBuilder::DefinedByTypeFacetedBodies  or
                     Die::SpringbackCompensationBuilder::DefinedByTypePoints .     
         
        """
        pass
    @property
    def ResultType(self) -> SpringbackCompensationBuilder.ResultSheetType:
        """
        Getter for property: ( SpringbackCompensationBuilder.ResultSheetType NXOp) ResultType
         Returns the type of output to generate.  
             
         
        """
        pass
    @ResultType.setter
    def ResultType(self, resultType: SpringbackCompensationBuilder.ResultSheetType):
        """
        Setter for property: ( SpringbackCompensationBuilder.ResultSheetType NXOp) ResultType
         Returns the type of output to generate.  
             
         
        """
        pass
    @property
    def ShapeValue(self) -> float:
        """
        Getter for property: (float) ShapeValue
         Returns the parameter that determines the shape of the transition area.  
             
         
        """
        pass
    @ShapeValue.setter
    def ShapeValue(self, shapeValue: float):
        """
        Setter for property: (float) ShapeValue
         Returns the parameter that determines the shape of the transition area.  
             
         
        """
        pass
    @property
    def SmoothingFactor(self) -> float:
        """
        Getter for property: (float) SmoothingFactor
         Returns the smoothing factor regulates a trade-off between interpolation error and smoothing when creating the result body.  
             
         
        """
        pass
    @SmoothingFactor.setter
    def SmoothingFactor(self, smoothingFactor: float):
        """
        Setter for property: (float) SmoothingFactor
         Returns the smoothing factor regulates a trade-off between interpolation error and smoothing when creating the result body.  
             
         
        """
        pass
    @property
    def SprungFacets(self) -> NXOpen.Facet.SelectFacetedBody:
        """
        Getter for property: ( NXOpen.Facet.SelectFacetedBody) SprungFacets
         Returns the sprung facets.  
           Only when type is  Die::SpringbackCompensationBuilder::DefinedByTypeFacetedBodies .   
         
        """
        pass
    @property
    def SprungPointsFile(self) -> str:
        """
        Getter for property: (str) SprungPointsFile
         Returns the sprung points file name.  
           This is saved for reference only. 
                    The product points are actually defined by calling  Die::SpringbackCompensationBuilder::SetSprungPoints . 
                    Only when type is  Die::SpringbackCompensationBuilder::DefinedByTypePoints . Optional.
                  
         
        """
        pass
    @SprungPointsFile.setter
    def SprungPointsFile(self, filename: str):
        """
        Setter for property: (str) SprungPointsFile
         Returns the sprung points file name.  
           This is saved for reference only. 
                    The product points are actually defined by calling  Die::SpringbackCompensationBuilder::SetSprungPoints . 
                    Only when type is  Die::SpringbackCompensationBuilder::DefinedByTypePoints . Optional.
                  
         
        """
        pass
    @property
    def StepSize(self) -> float:
        """
        Getter for property: (float) StepSize
         Returns the step size.  
             
         
        """
        pass
    @StepSize.setter
    def StepSize(self, stepSize: float):
        """
        Setter for property: (float) StepSize
         Returns the step size.  
             
         
        """
        pass
    def GetProductPoints(self) -> List[NXOpen.Point3d]:
        """
         Get the sample points on the product surface. Only when type is Die.SpringbackCompensationBuilder.DefinedByType.Points. Optional. 
         Returns product_points ( NXOpen.Point3d Li):  Points representing the shape of the product. .
        """
        pass
    def GetSprungPoints(self) -> List[NXOpen.Point3d]:
        """
         Get the sample points on the sprung surface. Only when type is Die.SpringbackCompensationBuilder.DefinedByType.Points. 
         Returns sprung_points ( NXOpen.Point3d Li):  Points representing the shape of the sprung sheet. .
        """
        pass
    def SetProductPoints(self, product_points: List[NXOpen.Point3d]) -> None:
        """
         Set the sample points on the product surface. Must have the same number as sprung points. Only when type is Die.SpringbackCompensationBuilder.DefinedByType.Points. Optional. 
        """
        pass
    def SetSprungPoints(self, sprung_points: List[NXOpen.Point3d]) -> None:
        """
         Set the sample points on the sprung surface. Must have the same number as product points. Only when type is Die.SpringbackCompensationBuilder.DefinedByType.Points. 
        """
        pass
import NXOpen.Features
class SpringbackCompensation(NXOpen.Features.BodyFeature): 
    """ Represents a springback compensation feature. """
    pass
import NXOpen
import NXOpen.Features
class SteelInsertBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Steel Insert feature builder. """
    class InsertTypeOption(Enum):
        """
        Members Include: 
         |Trim|  trim 
         |Flange|  flange 
         |OffsetFlange|  offset_flange 

        """
        Trim: int
        Flange: int
        OffsetFlange: int
        @staticmethod
        def ValueOf(value: int) -> SteelInsertBuilder.InsertTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngleTolerance(self) -> float:
        """
        Getter for property: (float) AngleTolerance
         Returns the angle tolerance of the diesteelinsert   
            
         
        """
        pass
    @AngleTolerance.setter
    def AngleTolerance(self, angle_tolerance: float):
        """
        Setter for property: (float) AngleTolerance
         Returns the angle tolerance of the diesteelinsert   
            
         
        """
        pass
    @property
    def BackReliefToggle(self) -> int:
        """
        Getter for property: (int) BackReliefToggle
         Returns the back relief toggle   
            
         
        """
        pass
    @BackReliefToggle.setter
    def BackReliefToggle(self, back_relief_toggle: int):
        """
        Setter for property: (int) BackReliefToggle
         Returns the back relief toggle   
            
         
        """
        pass
    @property
    def BaseOrientation(self) -> NXOpen.ISurface:
        """
        Getter for property: ( NXOpen.ISurface) BaseOrientation
         Returns the base orientation of the steelinsert   
            
         
        """
        pass
    @BaseOrientation.setter
    def BaseOrientation(self, base_orientation: NXOpen.ISurface):
        """
        Setter for property: ( NXOpen.ISurface) BaseOrientation
         Returns the base orientation of the steelinsert   
            
         
        """
        pass
    @property
    def BoltHoleParent(self) -> HoleParentBuilder:
        """
        Getter for property: ( HoleParentBuilder NXOp) BoltHoleParent
         Returns the bolt hole parent builder of the diesteelinsert   
            
         
        """
        pass
    @property
    def CamDirection(self) -> NXOpen.IReferenceAxis:
        """
        Getter for property: ( NXOpen.IReferenceAxis) CamDirection
         Returns the cam direction of the steelinsert   
            
         
        """
        pass
    @CamDirection.setter
    def CamDirection(self, cam_direction: NXOpen.IReferenceAxis):
        """
        Setter for property: ( NXOpen.IReferenceAxis) CamDirection
         Returns the cam direction of the steelinsert   
            
         
        """
        pass
    @property
    def ConnectProfilesParent(self) -> ConnectProfileParentBuilder:
        """
        Getter for property: ( ConnectProfileParentBuilder NXOp) ConnectProfilesParent
         Returns the connecting profiles parent builder of the diesteelinsert   
            
         
        """
        pass
    @property
    def DisplayHoles(self) -> bool:
        """
        Getter for property: (bool) DisplayHoles
         Returns the display holes of the diesteelinsert    
            
         
        """
        pass
    @DisplayHoles.setter
    def DisplayHoles(self, display_holes: bool):
        """
        Setter for property: (bool) DisplayHoles
         Returns the display holes of the diesteelinsert    
            
         
        """
        pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance of the diesteelinsert casting   
            
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distance_tolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance of the diesteelinsert casting   
            
         
        """
        pass
    @property
    def DowelHoleParent(self) -> HoleParentBuilder:
        """
        Getter for property: ( HoleParentBuilder NXOp) DowelHoleParent
         Returns the dowel hole parent builder of the diesteelinsert   
            
         
        """
        pass
    @property
    def EndOrientation(self) -> NXOpen.ISurface:
        """
        Getter for property: ( NXOpen.ISurface) EndOrientation
         Returns the end orientation of the steelinsert   
            
         
        """
        pass
    @EndOrientation.setter
    def EndOrientation(self, end_orientation: NXOpen.ISurface):
        """
        Setter for property: ( NXOpen.ISurface) EndOrientation
         Returns the end orientation of the steelinsert   
            
         
        """
        pass
    @property
    def InsertType(self) -> SteelInsertBuilder.InsertTypeOption:
        """
        Getter for property: ( SteelInsertBuilder.InsertTypeOption NXOp) InsertType
         Returns the insert type   
            
         
        """
        pass
    @InsertType.setter
    def InsertType(self, insert_type: SteelInsertBuilder.InsertTypeOption):
        """
        Setter for property: ( SteelInsertBuilder.InsertTypeOption NXOp) InsertType
         Returns the insert type   
            
         
        """
        pass
    @property
    def PierceHoleParent(self) -> PierceHoleParentBuilder:
        """
        Getter for property: ( PierceHoleParentBuilder NXOp) PierceHoleParent
         Returns the pierce hole  parent builder of the diesteelinsert   
            
         
        """
        pass
    @property
    def ProfileReliefToggle(self) -> int:
        """
        Getter for property: (int) ProfileReliefToggle
         Returns the profile relief toggle   
            
         
        """
        pass
    @ProfileReliefToggle.setter
    def ProfileReliefToggle(self, profile_relief_toggle: int):
        """
        Setter for property: (int) ProfileReliefToggle
         Returns the profile relief toggle   
            
         
        """
        pass
    @property
    def ReverseTrimSide(self) -> bool:
        """
        Getter for property: (bool) ReverseTrimSide
         Returns the reverse trim side setting of the steel insert.  
           
                True indicates that the trim side should be reversed.   
         
        """
        pass
    @ReverseTrimSide.setter
    def ReverseTrimSide(self, reverse: bool):
        """
        Setter for property: (bool) ReverseTrimSide
         Returns the reverse trim side setting of the steel insert.  
           
                True indicates that the trim side should be reversed.   
         
        """
        pass
    @property
    def RibsParent(self) -> FlangeSteelRibParentBuilder:
        """
        Getter for property: ( FlangeSteelRibParentBuilder NXOp) RibsParent
         Returns the ribs  parent builder of the diesteelinsert   
            
         
        """
        pass
    @property
    def Section(self) -> SteelInsertSectionBuilder:
        """
        Getter for property: ( SteelInsertSectionBuilder NXOp) Section
         Returns the section builder of the diesteelinsert   
            
         
        """
        pass
    @property
    def SegmentsParent(self) -> SteelInsertSegmentParentBuilder:
        """
        Getter for property: ( SteelInsertSegmentParentBuilder NXOp) SegmentsParent
         Returns the segments parent builder of the diesteelinsert   
            
         
        """
        pass
    @property
    def SheetMetal(self) -> NXOpen.Body:
        """
        Getter for property: ( NXOpen.Body) SheetMetal
         Returns the sheet metal of the die steelinsert    
            
         
        """
        pass
    @SheetMetal.setter
    def SheetMetal(self, sheet_metal: NXOpen.Body):
        """
        Setter for property: ( NXOpen.Body) SheetMetal
         Returns the sheet metal of the die steelinsert    
            
         
        """
        pass
    @property
    def StartOrientation(self) -> NXOpen.ISurface:
        """
        Getter for property: ( NXOpen.ISurface) StartOrientation
         Returns the start orientation of the steelinsert   
            
         
        """
        pass
    @StartOrientation.setter
    def StartOrientation(self, start_orientation: NXOpen.ISurface):
        """
        Setter for property: ( NXOpen.ISurface) StartOrientation
         Returns the start orientation of the steelinsert   
            
         
        """
        pass
    def GetBackShape(self) -> List[NXOpen.ISurface]:
        """
         Gets the back shape of the die steelinsert 
         Returns back_entries ( NXOpen.ISurface Li):  back entries .
        """
        pass
    def GetFlangeEndProfile(self) -> Tuple[List[NXOpen.IProfile], DirectionOption]:
        """
         Gets the flange end profile of the steel insert 
         Returns A tuple consisting of (profile_entries, direction). 
         - profile_entries is:  NXOpen.IProfile Li. profile entries .
         - direction is:  DirectionOption NXOp. profile direction .

        """
        pass
    def GetHoleGridOrientation(self) -> Tuple[NXOpen.Point3d, NXOpen.Matrix3x3]:
        """
         Gets the hole grid orientation for the dowel and bolt holes 
         Returns A tuple consisting of (grid_origin, grid_matrix). 
         - grid_origin is:  NXOpen.Point3d. .
         - grid_matrix is:  NXOpen.Matrix3x3. .

        """
        pass
    def GetMainProfile(self) -> Tuple[List[NXOpen.IProfile], DirectionOption]:
        """
         Gets the main profile of the steel insert 
         Returns A tuple consisting of (profile_entries, direction). 
         - profile_entries is:  NXOpen.IProfile Li. profile entries .
         - direction is:  DirectionOption NXOp. profile direction .

        """
        pass
    def SetBackShape(self, back_entries: List[NXOpen.ISurface]) -> None:
        """
         
        """
        pass
    def SetFlangeEndProfile(self, direction: DirectionOption, profile_entries: List[NXOpen.IProfile]) -> None:
        """
         Sets the flange end profile of the steel insert 
        """
        pass
    def SetHoleGridOrientation(self, grid_origin: NXOpen.Point3d, grid_matrix: NXOpen.Matrix3x3) -> None:
        """
          
        """
        pass
    def SetMainProfile(self, direction: DirectionOption, profile_entries: List[NXOpen.IProfile]) -> None:
        """
         Sets the main profile of the steel insert 
        """
        pass
import NXOpen
import NXOpen.Features
class SteelInsertSectionBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Steel Insert Section sub feature. """
    class ExtensionTypeOption(Enum):
        """
        Members Include: 
         |Constant|  constant 
         |MaxdistPlusConst|  maximum distance + constant 
         |Law|  law 

        """
        Constant: int
        MaxdistPlusConst: int
        Law: int
        @staticmethod
        def ValueOf(value: int) -> SteelInsertSectionBuilder.ExtensionTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BackSideReliefDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BackSideReliefDistance
         Returns the backside relief distance of the steel insert casting   
            
         
        """
        pass
    @property
    def BeltThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BeltThickness
         Returns the belt thickness   
            
         
        """
        pass
    @property
    def ExtensionDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ExtensionDistance
         Returns the extension distance   
            
         
        """
        pass
    @property
    def ExtensionType(self) -> SteelInsertSectionBuilder.ExtensionTypeOption:
        """
        Getter for property: ( SteelInsertSectionBuilder.ExtensionTypeOption NXOp) ExtensionType
         Returns the extension type   
            
         
        """
        pass
    @ExtensionType.setter
    def ExtensionType(self, extension_type: SteelInsertSectionBuilder.ExtensionTypeOption):
        """
        Setter for property: ( SteelInsertSectionBuilder.ExtensionTypeOption NXOp) ExtensionType
         Returns the extension type   
            
         
        """
        pass
    @property
    def MassLimit(self) -> float:
        """
        Getter for property: (float) MassLimit
         Returns the mass limit of the steel insert casting   
            
         
        """
        pass
    @MassLimit.setter
    def MassLimit(self, mass_limit: float):
        """
        Setter for property: (float) MassLimit
         Returns the mass limit of the steel insert casting   
            
         
        """
        pass
    @property
    def OffsetProfileToTop(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OffsetProfileToTop
         Returns the offset of the profile to the top of the steel insert casting   
            
         
        """
        pass
    @property
    def PlanarOffsetHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PlanarOffsetHeight
         Returns the planar contact height of the steel insert casting   
            
         
        """
        pass
    @property
    def ProductContactRelief(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ProductContactRelief
         Returns the product contact relief of the steel insert casting   
            
         
        """
        pass
    @property
    def ProductContactWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ProductContactWidth
         Returns the product contact width of the steel insert casting   
            
         
        """
        pass
    @property
    def ProfileRelief(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ProfileRelief
         Returns the profile relief   
            
         
        """
        pass
    @property
    def ReliefAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ReliefAngle
         Returns the relief angle   
            
         
        """
        pass
    def GetBackAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the back faces attributes 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. title for attribute .
         - value is: str. value of attribute .
         - color is: int. color of back faces .

        """
        pass
    def GetBaseAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the base faces attributes 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. title for attribute .
         - value is: str. value of attribute .
         - color is: int. color of base faces .

        """
        pass
    def GetEndAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the end faces attributes 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. title for attribute .
         - value is: str. value of attribute .
         - color is: int. color of end faces .

        """
        pass
    def GetFlangeWallAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the flange wall attributes 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. title for attribute .
         - value is: str. value of attribute .
         - color is: int. color of flange wall faces .

        """
        pass
    def GetFormingAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the forming faces attributes 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. title for attribute .
         - value is: str. value of attribute .
         - color is: int. color of forming faces .

        """
        pass
    def GetTrimWallAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the steelinsert trim wall faces attributes 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. title for attribute .
         - value is: str. value of attribute .
         - color is: int. color of trim wall faces .

        """
        pass
    def SetBackAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the back faces attributes 
        """
        pass
    def SetBackSideReliefDistance(self, back_side_relief_distance: str) -> None:
        """
         
        """
        pass
    def SetBaseAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the base faces attributes 
        """
        pass
    def SetBeltThickness(self, belt_thickness: str) -> None:
        """
         
        """
        pass
    def SetEndAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the end faces attributes 
        """
        pass
    def SetExtensionDistance(self, extension_distance: str) -> None:
        """
         
        """
        pass
    def SetFlangeWallAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the flange wall attributes 
        """
        pass
    def SetFormingAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the forming faces attributes 
        """
        pass
    def SetOffsetProfileToTop(self, offset_profile_to_top: str) -> None:
        """
         
        """
        pass
    def SetPlanarOffsetHeight(self, planar_offset_height: str) -> None:
        """
         
        """
        pass
    def SetProductContactRelief(self, product_contact_relief: str) -> None:
        """
         
        """
        pass
    def SetProductContactWidth(self, product_contact_width: str) -> None:
        """
         
        """
        pass
    def SetProfileRelief(self, profile_relief: str) -> None:
        """
         
        """
        pass
    def SetReliefAngle(self, relief_angle: str) -> None:
        """
         
        """
        pass
    def SetTrimWallAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the steelinsert trim wall faces attributes 
        """
        pass
import NXOpen
import NXOpen.Features
class SteelInsertSegmentChildBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Steel Insert Segment Child sub feature. """
    class ExtensionTypeOption(Enum):
        """
        Members Include: 
         |Constant|  constant 
         |MaxdistPlusConst|  maximum distance + constant 
         |Law|  law 

        """
        Constant: int
        MaxdistPlusConst: int
        Law: int
        @staticmethod
        def ValueOf(value: int) -> SteelInsertSegmentChildBuilder.ExtensionTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class InsertTypeOption(Enum):
        """
        Members Include: 
         |Trim|  trim 
         |Flange|  flange 
         |OffsetFlange|  offset_flange 

        """
        Trim: int
        Flange: int
        OffsetFlange: int
        @staticmethod
        def ValueOf(value: int) -> SteelInsertSegmentChildBuilder.InsertTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BeltThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BeltThickness
         Returns the belt thickness   
            
         
        """
        pass
    @property
    def BuildStatus(self) -> DieBuildStatusOption:
        """
        Getter for property: ( DieBuildStatusOption NXOp) BuildStatus
         Returns the build status of die sisegs   
            
         
        """
        pass
    @property
    def DesignStatus(self) -> bool:
        """
        Getter for property: (bool) DesignStatus
         Returns the design status of die sisegs   
            
         
        """
        pass
    @DesignStatus.setter
    def DesignStatus(self, design_status: bool):
        """
        Setter for property: (bool) DesignStatus
         Returns the design status of die sisegs   
            
         
        """
        pass
    @property
    def DisplayStatus(self) -> bool:
        """
        Getter for property: (bool) DisplayStatus
         Returns the display status of die sisegs   
            
         
        """
        pass
    @DisplayStatus.setter
    def DisplayStatus(self, display_status: bool):
        """
        Setter for property: (bool) DisplayStatus
         Returns the display status of die sisegs   
            
         
        """
        pass
    @property
    def ExtensionDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ExtensionDistance
         Returns the extension distance   
            
         
        """
        pass
    @property
    def ExtensionType(self) -> SteelInsertSegmentChildBuilder.ExtensionTypeOption:
        """
        Getter for property: ( SteelInsertSegmentChildBuilder.ExtensionTypeOption NXOp) ExtensionType
         Returns the extension type   
            
         
        """
        pass
    @ExtensionType.setter
    def ExtensionType(self, extension_type: SteelInsertSegmentChildBuilder.ExtensionTypeOption):
        """
        Setter for property: ( SteelInsertSegmentChildBuilder.ExtensionTypeOption NXOp) ExtensionType
         Returns the extension type   
            
         
        """
        pass
    @property
    def InsertType(self) -> SteelInsertSegmentChildBuilder.InsertTypeOption:
        """
        Getter for property: ( SteelInsertSegmentChildBuilder.InsertTypeOption NXOp) InsertType
         Returns the insert type   
            
         
        """
        pass
    @InsertType.setter
    def InsertType(self, insert_type: SteelInsertSegmentChildBuilder.InsertTypeOption):
        """
        Setter for property: ( SteelInsertSegmentChildBuilder.InsertTypeOption NXOp) InsertType
         Returns the insert type   
            
         
        """
        pass
    @property
    def ProfileRelief(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ProfileRelief
         Returns the profile relief   
            
         
        """
        pass
    @property
    def ProfileReliefToggle(self) -> bool:
        """
        Getter for property: (bool) ProfileReliefToggle
         Returns the profile relief toggle   
            
         
        """
        pass
    @ProfileReliefToggle.setter
    def ProfileReliefToggle(self, profile_relief_toggle: bool):
        """
        Setter for property: (bool) ProfileReliefToggle
         Returns the profile relief toggle   
            
         
        """
        pass
    @property
    def ReliefAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ReliefAngle
         Returns the relief angle   
            
         
        """
        pass
    @property
    def SegDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) SegDirection
         Returns the steel insert seg directions   
            
         
        """
        pass
    @SegDirection.setter
    def SegDirection(self, seg_direction: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) SegDirection
         Returns the steel insert seg directions   
            
         
        """
        pass
    @property
    def SegPoint(self) -> NXOpen.IOrientation:
        """
        Getter for property: ( NXOpen.IOrientation) SegPoint
         Returns the steel insert seg point or plane   
            
         
        """
        pass
    @SegPoint.setter
    def SegPoint(self, seg_point: NXOpen.IOrientation):
        """
        Setter for property: ( NXOpen.IOrientation) SegPoint
         Returns the steel insert seg point or plane   
            
         
        """
        pass
    def SetBeltThickness(self, belt_thickness: str) -> None:
        """
         
        """
        pass
    def SetExtensionDistance(self, extension_distance: str) -> None:
        """
         
        """
        pass
    def SetProfileRelief(self, profile_relief: str) -> None:
        """
         
        """
        pass
    def SetReliefAngle(self, relief_angle: str) -> None:
        """
         
        """
        pass
import NXOpen
import NXOpen.Features
class SteelInsertSegmentParentBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Steel Insert Segment Parent sub feature. """
    class ExtensionTypeOption(Enum):
        """
        Members Include: 
         |Constant|  constant 
         |MaxdistPlusConst|  maximum distance + constant 
         |Law|  law 

        """
        Constant: int
        MaxdistPlusConst: int
        Law: int
        @staticmethod
        def ValueOf(value: int) -> SteelInsertSegmentParentBuilder.ExtensionTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class InsertTypeOption(Enum):
        """
        Members Include: 
         |Trim|  trim 
         |Flange|  flange 
         |OffsetFlange|  offset_flange 

        """
        Trim: int
        Flange: int
        OffsetFlange: int
        @staticmethod
        def ValueOf(value: int) -> SteelInsertSegmentParentBuilder.InsertTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AddEndPointsSwitch(self) -> int:
        """
        Getter for property: (int) AddEndPointsSwitch
         Returns the add end points switch   
            
         
        """
        pass
    @AddEndPointsSwitch.setter
    def AddEndPointsSwitch(self, add_end_points_switch: int):
        """
        Setter for property: (int) AddEndPointsSwitch
         Returns the add end points switch   
            
         
        """
        pass
    @property
    def BeltThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BeltThickness
         Returns the belt thickness   
            
         
        """
        pass
    @property
    def BuildStatus(self) -> DieBuildStatusOption:
        """
        Getter for property: ( DieBuildStatusOption NXOp) BuildStatus
         Returns the build status of die sisegs   
            
         
        """
        pass
    @property
    def DesignStatus(self) -> bool:
        """
        Getter for property: (bool) DesignStatus
         Returns the design status of die sisegs   
            
         
        """
        pass
    @DesignStatus.setter
    def DesignStatus(self, design_status: bool):
        """
        Setter for property: (bool) DesignStatus
         Returns the design status of die sisegs   
            
         
        """
        pass
    @property
    def DisplayStatus(self) -> bool:
        """
        Getter for property: (bool) DisplayStatus
         Returns the display status of die sisegs   
            
         
        """
        pass
    @DisplayStatus.setter
    def DisplayStatus(self, display_status: bool):
        """
        Setter for property: (bool) DisplayStatus
         Returns the display status of die sisegs   
            
         
        """
        pass
    @property
    def ExtensionDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ExtensionDistance
         Returns the extension distance   
            
         
        """
        pass
    @property
    def ExtensionType(self) -> SteelInsertSegmentParentBuilder.ExtensionTypeOption:
        """
        Getter for property: ( SteelInsertSegmentParentBuilder.ExtensionTypeOption NXOp) ExtensionType
         Returns the extension type   
            
         
        """
        pass
    @ExtensionType.setter
    def ExtensionType(self, extension_type: SteelInsertSegmentParentBuilder.ExtensionTypeOption):
        """
        Setter for property: ( SteelInsertSegmentParentBuilder.ExtensionTypeOption NXOp) ExtensionType
         Returns the extension type   
            
         
        """
        pass
    @property
    def InsertType(self) -> SteelInsertSegmentParentBuilder.InsertTypeOption:
        """
        Getter for property: ( SteelInsertSegmentParentBuilder.InsertTypeOption NXOp) InsertType
         Returns the insert type   
            
         
        """
        pass
    @InsertType.setter
    def InsertType(self, insert_type: SteelInsertSegmentParentBuilder.InsertTypeOption):
        """
        Setter for property: ( SteelInsertSegmentParentBuilder.InsertTypeOption NXOp) InsertType
         Returns the insert type   
            
         
        """
        pass
    @property
    def ProfileRelief(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ProfileRelief
         Returns the profile relief   
            
         
        """
        pass
    @property
    def ProfileReliefToggle(self) -> bool:
        """
        Getter for property: (bool) ProfileReliefToggle
         Returns the profile relief   
            
         
        """
        pass
    @ProfileReliefToggle.setter
    def ProfileReliefToggle(self, profile_relief_toggle: bool):
        """
        Setter for property: (bool) ProfileReliefToggle
         Returns the profile relief   
            
         
        """
        pass
    @property
    def ReliefAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ReliefAngle
         Returns the relief angle   
            
         
        """
        pass
    def CreateChild(self) -> SteelInsertSegmentChildBuilder:
        """
         Creates a child siseg 
         Returns diesisegchild ( SteelInsertSegmentChildBuilder NXOp):  .
        """
        pass
    def DeleteChild(self, diesisegchild: SteelInsertSegmentChildBuilder) -> None:
        """
         Deletes a child siseg 
        """
        pass
    def GetChildren(self) -> List[SteelInsertSegmentChildBuilder]:
        """
         Outputs the children 
         Returns children ( SteelInsertSegmentChildBuilder List[NX):  children .
        """
        pass
    def SetBeltThickness(self, belt_thickness: str) -> None:
        """
         
        """
        pass
    def SetExtensionDistance(self, extension_distance: str) -> None:
        """
         
        """
        pass
    def SetProfileRelief(self, profile_relief: str) -> None:
        """
         
        """
        pass
    def SetReliefAngle(self, relief_angle: str) -> None:
        """
         
        """
        pass
import NXOpen
import NXOpen.Features
class ThroatChildBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Die Throat Child sub feature. """
    class TypeOption(Enum):
        """
        Members Include: 
         |Wipe|  Throat section is built for a wipe operation. 
         |Restrike|  Throat section is built for a restrike operation. 

        """
        Wipe: int
        Restrike: int
        @staticmethod
        def ValueOf(value: int) -> ThroatChildBuilder.TypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BuildStatus(self) -> DieBuildStatusOption:
        """
        Getter for property: ( DieBuildStatusOption NXOp) BuildStatus
         Returns the build status of the throat section.  
             
         
        """
        pass
    @property
    def CavityDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CavityDepth
         Returns the distance measured from the bend profile of the flange to the
                base of the throat.  
           The base of the throat is considered to be
                the surface the wear plates are mounted on for guiding and aliging
                the flange steels. The value given must be larger than the
                minimum cavity depth. An expression containg the value.
                Value is used in both the Wipe and Restrike Flange.   
         
        """
        pass
    @property
    def CavityOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CavityOffset
         Returns the offset distance measured from the Throat CSYS to the back
                cavity area of the throat.  
           Both positive and negative values may
                given to adjust the cavity to the proper location.
                An expression containg the value.
                Value is used in both the Wipe and Restrike Flange.   
         
        """
        pass
    @property
    def DesignStatus(self) -> bool:
        """
        Getter for property: (bool) DesignStatus
         Returns the design status of the throat section, if true the throat section will be built into the model, if false it will not.  
             
         
        """
        pass
    @DesignStatus.setter
    def DesignStatus(self, design_status: bool):
        """
        Setter for property: (bool) DesignStatus
         Returns the design status of the throat section, if true the throat section will be built into the model, if false it will not.  
             
         
        """
        pass
    @property
    def DisplayStatus(self) -> bool:
        """
        Getter for property: (bool) DisplayStatus
         Returns the display status of the throat section, if true input data to the throat section will be displayed,
                if false the input data will not be displayed.  
             
         
        """
        pass
    @DisplayStatus.setter
    def DisplayStatus(self, display_status: bool):
        """
        Setter for property: (bool) DisplayStatus
         Returns the display status of the throat section, if true input data to the throat section will be displayed,
                if false the input data will not be displayed.  
             
         
        """
        pass
    @property
    def ExtensionLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ExtensionLength
         Returns the tangent distance to add to the end of the flange.  
          
                An expression containg the length along the tangent.
                Value is used in both the Wipe and Restrike Flange.   
         
        """
        pass
    @property
    def LowerRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LowerRadius
         Returns the radius to apply to the lower corner of the throat cavity.  
          
                Typically, both the lower and the upper radius will be the
                same. An expression containg the value.
                Value is used in both the Wipe and Restrike Flange.   
         
        """
        pass
    @property
    def Radius(self) -> float:
        """
        Getter for property: (float) Radius
         Returns the radius to be applied at the back of the throat, top and bottom   
            
         
        """
        pass
    @Radius.setter
    def Radius(self, radius: float):
        """
        Setter for property: (float) Radius
         Returns the radius to be applied at the back of the throat, top and bottom   
            
         
        """
        pass
    @property
    def SectionPlacement(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SectionPlacement
         Returns the throat section placement along the center line, an expression containg the length along the centerline for placement   
            
         
        """
        pass
    @property
    def Step(self) -> float:
        """
        Getter for property: (float) Step
         Returns the step to be applied at the end of the tangent extension of the flange   
            
         
        """
        pass
    @Step.setter
    def Step(self, step: float):
        """
        Setter for property: (float) Step
         Returns the step to be applied at the end of the tangent extension of the flange   
            
         
        """
        pass
    @property
    def StepDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StepDistance
         Returns the step distance to add at the end of the tangent extension.  
           The
                step is at a right angle and only applies to the Wipe Flange. An
                expression containg the step distance.   
         
        """
        pass
    @property
    def UpperRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) UpperRadius
         Returns the radius to apply to the upper corner of the throat cavity.  
          
                An expression containg the value.
                Value is used in both the Wipe and Restrike Flange.   
         
        """
        pass
    def GetCavityAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the cavity attributes, note existance of attributes depends on usage in
                main feature. 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. Title for attribute. .
         - value is: str. Value of attribute. .
         - color is: int. Color of cavity faces. .

        """
        pass
    def GetExtensionAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the extension attributes, note existance of attributes depends on usage in
                main feature. 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. Title for attribute. .
         - value is: str. Value of attribute. .
         - color is: int. Color of extension faces. .

        """
        pass
    def SetCavityAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the cavity attributes, note existance of attributes depends on usage in
                main feature. 
        """
        pass
    def SetCavityDepth(self, cavity_depth: str) -> None:
        """
         
        """
        pass
    def SetCavityOffset(self, cavity_offset: str) -> None:
        """
         
        """
        pass
    def SetExtensionAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the extension attributes, note existance of attributes depends on usage in
                main feature. 
        """
        pass
    def SetExtensionLength(self, extension_length: str) -> None:
        """
         
        """
        pass
    def SetLowerRadius(self, lower_radius: str) -> None:
        """
         
        """
        pass
    def SetSectionPlacement(self, section_placement: str) -> None:
        """
         
        """
        pass
    def SetStepDistance(self, step_distance: str) -> None:
        """
         
        """
        pass
    def SetUpperRadius(self, upper_radius: str) -> None:
        """
         
        """
        pass
import NXOpen.Features
class ThroatParentBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Die Throat Parent sub feature. """
    class TypeOption(Enum):
        """
        Members Include: 
         |Wipe|  Throat is built for a wipe operation. 
         |Restrike|  Throat is built for a restrike operation. 

        """
        Wipe: int
        Restrike: int
        @staticmethod
        def ValueOf(value: int) -> ThroatParentBuilder.TypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BuildStatus(self) -> DieBuildStatusOption:
        """
        Getter for property: ( DieBuildStatusOption NXOp) BuildStatus
         Returns the build status of the throat sections.  
             
         
        """
        pass
    @property
    def DesignStatus(self) -> bool:
        """
        Getter for property: (bool) DesignStatus
         Returns the design status of the throat sections, if true the throat sections will be built into the model, if false they will not.  
             
         
        """
        pass
    @DesignStatus.setter
    def DesignStatus(self, design_status: bool):
        """
        Setter for property: (bool) DesignStatus
         Returns the design status of the throat sections, if true the throat sections will be built into the model, if false they will not.  
             
         
        """
        pass
    @property
    def DisplayStatus(self) -> bool:
        """
        Getter for property: (bool) DisplayStatus
         Returns the display status of the throat sections, if true input data to the throat sections will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    @DisplayStatus.setter
    def DisplayStatus(self, display_status: bool):
        """
        Setter for property: (bool) DisplayStatus
         Returns the display status of the throat sections, if true input data to the throat sections will be displayed, 
                if false the input data will not be displayed.  
             
         
        """
        pass
    @property
    def Radius(self) -> float:
        """
        Getter for property: (float) Radius
         Returns the radius to be applied at the back of the throat, top and bottom   
            
         
        """
        pass
    @Radius.setter
    def Radius(self, radius: float):
        """
        Setter for property: (float) Radius
         Returns the radius to be applied at the back of the throat, top and bottom   
            
         
        """
        pass
    @property
    def Step(self) -> float:
        """
        Getter for property: (float) Step
         Returns the step to be applied at the end of the tangential extension of the flange   
            
         
        """
        pass
    @Step.setter
    def Step(self, step: float):
        """
        Setter for property: (float) Step
         Returns the step to be applied at the end of the tangential extension of the flange   
            
         
        """
        pass
    @property
    def Type(self) -> ThroatParentBuilder.TypeOption:
        """
        Getter for property: ( ThroatParentBuilder.TypeOption NXOp) Type
         Returns the type of throat sections.  
             
         
        """
        pass
    @Type.setter
    def Type(self, type: ThroatParentBuilder.TypeOption):
        """
        Setter for property: ( ThroatParentBuilder.TypeOption NXOp) Type
         Returns the type of throat sections.  
             
         
        """
        pass
    def CreateChild(self) -> ThroatChildBuilder:
        """
         Creates a child throat section. 
         Returns diethroatchild ( ThroatChildBuilder NXOp):  .
        """
        pass
    def DeleteChild(self, diethroatchild: ThroatChildBuilder) -> None:
        """
         Deletes a child throat section. 
        """
        pass
    def GetCavityAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the cavity attributes, note existance of attributes depends on usage in
                main feature. 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. Title for attribute. .
         - value is: str. Value of attribute. .
         - color is: int. Color of cavity faces. .

        """
        pass
    def GetChildren(self) -> List[ThroatChildBuilder]:
        """
         Outputs the child throat sections. 
         Returns children ( ThroatChildBuilder List[NX):  The child throat sections. .
        """
        pass
    def GetExtensionAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the extension attributes, note existance of attributes depends on usage in
                main feature. 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. Title for attribute. .
         - value is: str. Value of attribute. .
         - color is: int. Color of extension faces. .

        """
        pass
    def SetCavityAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the cavity attributes, note existance of attributes depends on usage in
                main feature. 
        """
        pass
    def SetExtensionAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the extension attributes, note existance of attributes depends on usage in
                main feature. 
        """
        pass
import NXOpen
import NXOpen.Features
class Tip(NXOpen.Features.Feature): 
    """ Represents a Tip feature. """
    def AddToDieData(self, objects: List[NXOpen.Curve]) -> None:
        """
         Adds the input curves to the die data. 
        """
        pass
    def CreateDieData(self, all_tips: bool) -> None:
        """
         Creates a copy of the product data in die position. The product data is not visible upon creation. 
                This method must be called before using the methods Die.Tip.DeleteDieData, 
                Die.Tip.DisplayDieData, Die.Tip.UndisplayDieData, 
                Die.Tip.TransformDiePoint, or Die.Tip.TransformDieDirection. 
        """
        pass
    def DeleteDieData(self) -> None:
        """
         Deletes the copy of the product data. 
        """
        pass
    def DisplayDieData(self) -> None:
        """
         Makes the product data in die position visible. The display of the Tip feature is made invisible. 
        """
        pass
    def GetUnprocessedHoles(self) -> List[NXOpen.Edge]:
        """
         Finds the hole edges that have not been processed yet. 
         Returns edges ( NXOpen.Edge Li): .
        """
        pass
    def MapCollectorToDie(self, collector: NXOpen.ScCollector) -> None:
        """
         Maps the edges in the collector from part position to die position. 
        """
        pass
    def MapCollectorToPart(self, collector: NXOpen.ScCollector) -> None:
        """
         Maps the edges in the collector from die position to part position. 
        """
        pass
    def MapEdge(self, in_edge: NXOpen.IProfile) -> Tuple[NXOpen.IProfile, NXOpen.IProfile]:
        """
         Maps the edge to find the part and die position entity, either can be a . 
         Returns A tuple consisting of (part_edge, die_edge). 
         - part_edge is:  NXOpen.IProfile.
         - die_edge is:  NXOpen.IProfile.

        """
        pass
    def SetReferenceCurves(self, objects: List[NXOpen.Curve]) -> None:
        """
         Sets reference curves in the die tip feature. 
        """
        pass
    def TransformDieDirection(self, vector: NXOpen.Direction) -> None:
        """
         Transforms the direction from die position to product position. 
        """
        pass
    def TransformDiePoint(self, point: NXOpen.Point) -> None:
        """
         Transforms the point from die position to product position. 
        """
        pass
    def UndisplayDieData(self) -> None:
        """
         Makes the product data in die position invisible. The display of the Tip feature is made visible. 
        """
        pass
import NXOpen
import NXOpen.Features
class TrimFlangeDieAssistantBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a NXOpen.Die.TrimFlangeDieAssistantBuilder
    """
    @property
    def Clearance(self) -> float:
        """
        Getter for property: (float) Clearance
         Returns the clearance used in the automatic generation of the lower post flange profile   
            
         
        """
        pass
    @Clearance.setter
    def Clearance(self, clearance: float):
        """
        Setter for property: (float) Clearance
         Returns the clearance used in the automatic generation of the lower post flange profile   
            
         
        """
        pass
    @property
    def FlangeProfile(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FlangeProfile
         Returns the flange profile   
            
         
        """
        pass
    @property
    def FlangeProfileSet(self) -> DieAssistantFlangeProfileList:
        """
        Getter for property: ( DieAssistantFlangeProfileList NXOp) FlangeProfileSet
         Returns the flange profile set   
            
         
        """
        pass
    @property
    def LowerBase(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) LowerBase
         Returns the lower base   
            
         
        """
        pass
    @LowerBase.setter
    def LowerBase(self, lowerBase: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) LowerBase
         Returns the lower base   
            
         
        """
        pass
    @property
    def PierceLocations(self) -> NXOpen.SelectPointList:
        """
        Getter for property: ( NXOpen.SelectPointList) PierceLocations
         Returns the pierce locations   
            
         
        """
        pass
    @property
    def SheetMetal(self) -> NXOpen.SelectBody:
        """
        Getter for property: ( NXOpen.SelectBody) SheetMetal
         Returns the sheet metal   
            
         
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
    @property
    def TrimProfileSet(self) -> DieAssistantTrimProfileList:
        """
        Getter for property: ( DieAssistantTrimProfileList NXOp) TrimProfileSet
         Returns the trim profile set   
            
         
        """
        pass
    @property
    def UpperBase(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) UpperBase
         Returns the upper base   
            
         
        """
        pass
    @UpperBase.setter
    def UpperBase(self, upperBase: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) UpperBase
         Returns the upper base   
            
         
        """
        pass
    def AutoGen(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    def FlangeSteelRestrikeParms(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    def FlangeSteelWipeParms(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    def LowerPostParms(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    def LowerScrapCutterBaseParms(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    def LowerScrapCutterParms(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    def NewFlangeProfile(self) -> DieAssistantFlangeProfile:
        """
         Creates a new flange profile item in the set 
         Returns flangeProfile ( DieAssistantFlangeProfile NXOp): .
        """
        pass
    def NewTrimProfile(self) -> DieAssistantTrimProfile:
        """
         Creates a new trim profile item in the set 
         Returns trimProfile ( DieAssistantTrimProfile NXOp): .
        """
        pass
    def TrimSteelParms(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    def UpperPadParms(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
import NXOpen.Features
class TrimFlangeDieAssistant(NXOpen.Features.BodyFeature): 
    """ Represents a trimflange die assistant """
    pass
import NXOpen
import NXOpen.Features
class TrimLineDevelopmentBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a NXOpen.Features.TrimLineDevelopment builder
    """
    class CalculateType(Enum):
        """
        Members Include: 
         |GeometryMethod| geometry method
         |OneStepTrimLine| Onestep trim line method 

        """
        GeometryMethod: int
        OneStepTrimLine: int
        @staticmethod
        def ValueOf(value: int) -> TrimLineDevelopmentBuilder.CalculateType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Convergency(Enum):
        """
        Members Include: 
         |Low| Onestep solver convergency level is low
         |Medium| Onestep solver convergency level is medium
         |High| Onestep solver convergency level is high

        """
        Low: int
        Medium: int
        High: int
        @staticmethod
        def ValueOf(value: int) -> TrimLineDevelopmentBuilder.Convergency:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MaterialTypeName(Enum):
        """
        Members Include: 
         |Steel|  Steel 
         |Aluminum|  Aluminum 

        """
        Steel: int
        Aluminum: int
        @staticmethod
        def ValueOf(value: int) -> TrimLineDevelopmentBuilder.MaterialTypeName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MeshElement(Enum):
        """
        Members Include: 
         |Triangle| Generate 2D triangle mesh element
         |Quadrate| Generate 2D quadrate mesh element

        """
        Triangle: int
        Quadrate: int
        @staticmethod
        def ValueOf(value: int) -> TrimLineDevelopmentBuilder.MeshElement:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OutputMethodName(Enum):
        """
        Members Include: 
         |Geometric|  Geometric curve only 
         |Corrected|  Corrected curve only 
         |Both|  Both geometric and corrected curves 

        """
        Geometric: int
        Corrected: int
        Both: int
        @staticmethod
        def ValueOf(value: int) -> TrimLineDevelopmentBuilder.OutputMethodName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SmoothingName(Enum):
        """
        Members Include: 
         |Linear|  Linear (no smoothing) 
         |Cubic|  Cubic approximation 
         |Quintic|  Quintic approximation 

        """
        Linear: int
        Cubic: int
        Quintic: int
        @staticmethod
        def ValueOf(value: int) -> TrimLineDevelopmentBuilder.SmoothingName:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Surface(Enum):
        """
        Members Include: 
         |Inner| Onestep solver will offset inner surface and enlarge it
         |Middle| Onestep solver will not offset middle surface 
         |Outer| Onestep solver will offset outer surface and shrink it 

        """
        Inner: int
        Middle: int
        Outer: int
        @staticmethod
        def ValueOf(value: int) -> TrimLineDevelopmentBuilder.Surface:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Addendum(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Addendum
         Returns the collection of addendum faces   
            
         
        """
        pass
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns the associative switch.  
            True indicates a feature should be output   
         
        """
        pass
    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
         Returns the associative switch.  
            True indicates a feature should be output   
         
        """
        pass
    @property
    def BendAllowance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BendAllowance
         Returns the bend allowance formula.  
            Value should be between 0 and 1   
         
        """
        pass
    @property
    def ConstraintCurveFromTargetRegion(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) ConstraintCurveFromTargetRegion
         Returns the collection of constraint curve from target region   
            
         
        """
        pass
    @property
    def ConstraintCurveFromUnformRegion(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) ConstraintCurveFromUnformRegion
         Returns the collection of constraint curve from unform region   
            
         
        """
        pass
    @property
    def ContactPointsTolerance(self) -> float:
        """
        Getter for property: (float) ContactPointsTolerance
         Returns the tolerance to find contact points.  
             
         
        """
        pass
    @ContactPointsTolerance.setter
    def ContactPointsTolerance(self, tolerance: float):
        """
        Setter for property: (float) ContactPointsTolerance
         Returns the tolerance to find contact points.  
             
         
        """
        pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance.  
            Used for sewing sheet bodies and joining curves   
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distTol: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance.  
            Used for sewing sheet bodies and joining curves   
         
        """
        pass
    @property
    def DrawDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) DrawDirection
         Returns the draw direction.  
            Also points in the direction of material side of metal   
         
        """
        pass
    @DrawDirection.setter
    def DrawDirection(self, punchDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) DrawDirection
         Returns the draw direction.  
            Also points in the direction of material side of metal   
         
        """
        pass
    @property
    def Faces(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Faces
         Returns the collection of formed faces   
            
         
        """
        pass
    @property
    def FormingBoundary(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FormingBoundary
         Returns the forming boundary   
            
         
        """
        pass
    @property
    def InferElementSize(self) -> bool:
        """
        Getter for property: (bool) InferElementSize
         Returns the option to infer 2-D element size.  
           
                If it is true, the element size will be auto-detected. If it is false, the element size will be required as input.   
         
        """
        pass
    @InferElementSize.setter
    def InferElementSize(self, inforElementSize: bool):
        """
        Setter for property: (bool) InferElementSize
         Returns the option to infer 2-D element size.  
           
                If it is true, the element size will be auto-detected. If it is false, the element size will be required as input.   
         
        """
        pass
    @property
    def InferThickness(self) -> bool:
        """
        Getter for property: (bool) InferThickness
         Returns the option to infer thickness.  
          
                If it is true, the thickness will be auto-detected. If it is false, thickness will be required to input.  
         
        """
        pass
    @InferThickness.setter
    def InferThickness(self, inferThickness: bool):
        """
        Setter for property: (bool) InferThickness
         Returns the option to infer thickness.  
          
                If it is true, the thickness will be auto-detected. If it is false, thickness will be required to input.  
         
        """
        pass
    @property
    def LimitPoint1(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) LimitPoint1
         Returns the first limit point   
            
         
        """
        pass
    @LimitPoint1.setter
    def LimitPoint1(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) LimitPoint1
         Returns the first limit point   
            
         
        """
        pass
    @property
    def LimitPoint2(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) LimitPoint2
         Returns the last limit point   
            
         
        """
        pass
    @LimitPoint2.setter
    def LimitPoint2(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) LimitPoint2
         Returns the last limit point   
            
         
        """
        pass
    @property
    def Limits(self) -> DieLimitsBuilder:
        """
        Getter for property: ( DieLimitsBuilder NXOp) Limits
         Returns the limits to control the span of the addendum   
            
         
        """
        pass
    @property
    def MaterialPropertyDensity(self) -> float:
        """
        Getter for property: (float) MaterialPropertyDensity
         Returns the density of material.  
             
         
        """
        pass
    @MaterialPropertyDensity.setter
    def MaterialPropertyDensity(self, materialPropertyDensity: float):
        """
        Setter for property: (float) MaterialPropertyDensity
         Returns the density of material.  
             
         
        """
        pass
    @property
    def MaterialPropertyE(self) -> float:
        """
        Getter for property: (float) MaterialPropertyE
         Returns the material property elasticity(E) which enables a material to return to its original shape and dimension.  
             
         
        """
        pass
    @MaterialPropertyE.setter
    def MaterialPropertyE(self, materialPropertyE: float):
        """
        Setter for property: (float) MaterialPropertyE
         Returns the material property elasticity(E) which enables a material to return to its original shape and dimension.  
             
         
        """
        pass
    @property
    def MaterialPropertyF(self) -> float:
        """
        Getter for property: (float) MaterialPropertyF
         Returns the friction of material.  
             
         
        """
        pass
    @MaterialPropertyF.setter
    def MaterialPropertyF(self, materialPropertyF: float):
        """
        Setter for property: (float) MaterialPropertyF
         Returns the friction of material.  
             
         
        """
        pass
    @property
    def MaterialPropertyInitialStrain(self) -> float:
        """
        Getter for property: (float) MaterialPropertyInitialStrain
         Returns the material initial strain to represent in a material upon achieving the given loading conditions in a relaxation or creep test.  
             
         
        """
        pass
    @MaterialPropertyInitialStrain.setter
    def MaterialPropertyInitialStrain(self, materialPropertyInitialStrain: float):
        """
        Setter for property: (float) MaterialPropertyInitialStrain
         Returns the material initial strain to represent in a material upon achieving the given loading conditions in a relaxation or creep test.  
             
         
        """
        pass
    @property
    def MaterialPropertyK(self) -> float:
        """
        Getter for property: (float) MaterialPropertyK
         Returns the K(Strength Coefficient) of material.  
             
         
        """
        pass
    @MaterialPropertyK.setter
    def MaterialPropertyK(self, materialPropertyK: float):
        """
        Setter for property: (float) MaterialPropertyK
         Returns the K(Strength Coefficient) of material.  
             
         
        """
        pass
    @property
    def MaterialPropertyN(self) -> float:
        """
        Getter for property: (float) MaterialPropertyN
         Returns the  material n(Hardening Exponent) to represent the constant index used in calculations for stress-strain behaviour.  
             
         
        """
        pass
    @MaterialPropertyN.setter
    def MaterialPropertyN(self, materialPropertyN: float):
        """
        Setter for property: (float) MaterialPropertyN
         Returns the  material n(Hardening Exponent) to represent the constant index used in calculations for stress-strain behaviour.  
             
         
        """
        pass
    @property
    def MaterialPropertyPoisson(self) -> float:
        """
        Getter for property: (float) MaterialPropertyPoisson
         Returns the material Poisson's ratio between the contraction at right angles to a stress and the direct extension.  
             
         
        """
        pass
    @MaterialPropertyPoisson.setter
    def MaterialPropertyPoisson(self, materialPropertyPoisson: float):
        """
        Setter for property: (float) MaterialPropertyPoisson
         Returns the material Poisson's ratio between the contraction at right angles to a stress and the direct extension.  
             
         
        """
        pass
    @property
    def MaterialPropertyR0(self) -> float:
        """
        Getter for property: (float) MaterialPropertyR0
         Returns the r0(Anisotropy Coefficient) of material.  
             
         
        """
        pass
    @MaterialPropertyR0.setter
    def MaterialPropertyR0(self, materialPropertyR0: float):
        """
        Setter for property: (float) MaterialPropertyR0
         Returns the r0(Anisotropy Coefficient) of material.  
             
         
        """
        pass
    @property
    def MaterialPropertyR45(self) -> float:
        """
        Getter for property: (float) MaterialPropertyR45
         Returns the r45(Anisotropy Coefficient) of material.  
             
         
        """
        pass
    @MaterialPropertyR45.setter
    def MaterialPropertyR45(self, materialPropertyR45: float):
        """
        Setter for property: (float) MaterialPropertyR45
         Returns the r45(Anisotropy Coefficient) of material.  
             
         
        """
        pass
    @property
    def MaterialPropertyR90(self) -> float:
        """
        Getter for property: (float) MaterialPropertyR90
         Returns the r90(Anisotropy Coefficient) of material.  
             
         
        """
        pass
    @MaterialPropertyR90.setter
    def MaterialPropertyR90(self, materialPropertyR90: float):
        """
        Setter for property: (float) MaterialPropertyR90
         Returns the r90(Anisotropy Coefficient) of material.  
             
         
        """
        pass
    @property
    def MaterialPropertyYieldStress(self) -> float:
        """
        Getter for property: (float) MaterialPropertyYieldStress
         Returns the yield stress of material.  
             
         
        """
        pass
    @MaterialPropertyYieldStress.setter
    def MaterialPropertyYieldStress(self, materialPropertyYieldStress: float):
        """
        Setter for property: (float) MaterialPropertyYieldStress
         Returns the yield stress of material.  
             
         
        """
        pass
    @property
    def MaterialType(self) -> TrimLineDevelopmentBuilder.MaterialTypeName:
        """
        Getter for property: ( TrimLineDevelopmentBuilder.MaterialTypeName NXOp) MaterialType
         Returns the material type - steel or aluminum   
            
         
        """
        pass
    @MaterialType.setter
    def MaterialType(self, materialType: TrimLineDevelopmentBuilder.MaterialTypeName):
        """
        Setter for property: ( TrimLineDevelopmentBuilder.MaterialTypeName NXOp) MaterialType
         Returns the material type - steel or aluminum   
            
         
        """
        pass
    @property
    def MeshAttemptMapping(self) -> bool:
        """
        Getter for property: (bool) MeshAttemptMapping
         Returns the option to attemp mapping for mesh elements.  
           
                If it is true, mesh element nodes will be mapped to the orginal surface to ensure the accuracy. if it is false, it will not do mapping.   
         
        """
        pass
    @MeshAttemptMapping.setter
    def MeshAttemptMapping(self, meshAttemptMapping: bool):
        """
        Setter for property: (bool) MeshAttemptMapping
         Returns the option to attemp mapping for mesh elements.  
           
                If it is true, mesh element nodes will be mapped to the orginal surface to ensure the accuracy. if it is false, it will not do mapping.   
         
        """
        pass
    @property
    def MeshElementSize(self) -> float:
        """
        Getter for property: (float) MeshElementSize
         Returns the 2-D element size for mesh.  
             
         
        """
        pass
    @MeshElementSize.setter
    def MeshElementSize(self, meshElementSize: float):
        """
        Setter for property: (float) MeshElementSize
         Returns the 2-D element size for mesh.  
             
         
        """
        pass
    @property
    def MeshElementType(self) -> TrimLineDevelopmentBuilder.MeshElement:
        """
        Getter for property: ( TrimLineDevelopmentBuilder.MeshElement NXOp) MeshElementType
         Returns the 2-D mesh element type, either triangle or quadrate element.  
            
         
        """
        pass
    @MeshElementType.setter
    def MeshElementType(self, meshElementType: TrimLineDevelopmentBuilder.MeshElement):
        """
        Setter for property: ( TrimLineDevelopmentBuilder.MeshElement NXOp) MeshElementType
         Returns the 2-D mesh element type, either triangle or quadrate element.  
            
         
        """
        pass
    @property
    def MeshMaxJacobian(self) -> float:
        """
        Getter for property: (float) MeshMaxJacobian
         Returns the maximum Jacobian for mesh elements.  
           It is used to control the element shape and quality.   
         
        """
        pass
    @MeshMaxJacobian.setter
    def MeshMaxJacobian(self, meshMaxJacobian: float):
        """
        Setter for property: (float) MeshMaxJacobian
         Returns the maximum Jacobian for mesh elements.  
           It is used to control the element shape and quality.   
         
        """
        pass
    @property
    def MeshMaxWarp(self) -> float:
        """
        Getter for property: (float) MeshMaxWarp
         Returns the maximum warp for meshing.  
             
         
        """
        pass
    @MeshMaxWarp.setter
    def MeshMaxWarp(self, meshMaxWarp: float):
        """
        Setter for property: (float) MeshMaxWarp
         Returns the maximum warp for meshing.  
             
         
        """
        pass
    @property
    def MeshProcessFillet(self) -> bool:
        """
        Getter for property: (bool) MeshProcessFillet
         Returns the option to process fillet for mesh element.  
          
                If it is true, the small fillet area will be specially processed when generate mesh element. If it is false, it will be not specially processed.   
         
        """
        pass
    @MeshProcessFillet.setter
    def MeshProcessFillet(self, meshProcessFillet: bool):
        """
        Setter for property: (bool) MeshProcessFillet
         Returns the option to process fillet for mesh element.  
          
                If it is true, the small fillet area will be specially processed when generate mesh element. If it is false, it will be not specially processed.   
         
        """
        pass
    @property
    def MeshSizeVariation(self) -> int:
        """
        Getter for property: (int) MeshSizeVariation
         Returns the variation of mesh element size.  
             
         
        """
        pass
    @MeshSizeVariation.setter
    def MeshSizeVariation(self, meshSizeVariation: int):
        """
        Setter for property: (int) MeshSizeVariation
         Returns the variation of mesh element size.  
             
         
        """
        pass
    @property
    def MeshSmallFeature(self) -> float:
        """
        Getter for property: (float) MeshSmallFeature
         Returns the value of small feature for mesh setting  
            
         
        """
        pass
    @MeshSmallFeature.setter
    def MeshSmallFeature(self, meshSmallFeature: float):
        """
        Setter for property: (float) MeshSmallFeature
         Returns the value of small feature for mesh setting  
            
         
        """
        pass
    @property
    def MeshSplitQuad(self) -> bool:
        """
        Getter for property: (bool) MeshSplitQuad
         Returns the option to split quadrate element to triangle element when creating meshes.  
             
         
        """
        pass
    @MeshSplitQuad.setter
    def MeshSplitQuad(self, meshSplitQuad: bool):
        """
        Setter for property: (bool) MeshSplitQuad
         Returns the option to split quadrate element to triangle element when creating meshes.  
             
         
        """
        pass
    @property
    def OutputMethod(self) -> TrimLineDevelopmentBuilder.OutputMethodName:
        """
        Getter for property: ( TrimLineDevelopmentBuilder.OutputMethodName NXOp) OutputMethod
         Returns the curve output method - geometric, corrected or both   
            
         
        """
        pass
    @OutputMethod.setter
    def OutputMethod(self, outputMethod: TrimLineDevelopmentBuilder.OutputMethodName):
        """
        Setter for property: ( TrimLineDevelopmentBuilder.OutputMethodName NXOp) OutputMethod
         Returns the curve output method - geometric, corrected or both   
            
         
        """
        pass
    @property
    def RegionPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) RegionPoint
         Returns the point in product region   
            
         
        """
        pass
    @RegionPoint.setter
    def RegionPoint(self, regionPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) RegionPoint
         Returns the point in product region   
            
         
        """
        pass
    @property
    def RemoveLoops(self) -> bool:
        """
        Getter for property: (bool) RemoveLoops
         Returns the remove loops setting.  
            True indicates loops should be removed from the output curves   
         
        """
        pass
    @RemoveLoops.setter
    def RemoveLoops(self, removeLoops: bool):
        """
        Setter for property: (bool) RemoveLoops
         Returns the remove loops setting.  
            True indicates loops should be removed from the output curves   
         
        """
        pass
    @property
    def ReverseSide(self) -> bool:
        """
        Getter for property: (bool) ReverseSide
         Returns the option to indicate whether or not to unform the profile to the other side on the target body.  
           
                 This option is appliable only in case the following conditions are all satisfied: entire unform to seperate target body, Curve to Curve constraint on inner edges.  
         
        """
        pass
    @ReverseSide.setter
    def ReverseSide(self, reverseSide: bool):
        """
        Setter for property: (bool) ReverseSide
         Returns the option to indicate whether or not to unform the profile to the other side on the target body.  
           
                 This option is appliable only in case the following conditions are all satisfied: entire unform to seperate target body, Curve to Curve constraint on inner edges.  
         
        """
        pass
    @property
    def SampleDensityIndex(self) -> int:
        """
        Getter for property: (int) SampleDensityIndex
         Returns the sample density index which controls the density of the sample planes.  
            Value should be between 1 and 9   
         
        """
        pass
    @SampleDensityIndex.setter
    def SampleDensityIndex(self, sampleDensityIndex: int):
        """
        Setter for property: (int) SampleDensityIndex
         Returns the sample density index which controls the density of the sample planes.  
            Value should be between 1 and 9   
         
        """
        pass
    @property
    def SheetThickness(self) -> float:
        """
        Getter for property: (float) SheetThickness
         Returns the thickness of sheet metal model.  
             
         
        """
        pass
    @SheetThickness.setter
    def SheetThickness(self, thickness: float):
        """
        Setter for property: (float) SheetThickness
         Returns the thickness of sheet metal model.  
             
         
        """
        pass
    @property
    def Smoothing(self) -> TrimLineDevelopmentBuilder.SmoothingName:
        """
        Getter for property: ( TrimLineDevelopmentBuilder.SmoothingName NXOp) Smoothing
         Returns the curve smoothing method - linear (none), cubic or quintic   
            
         
        """
        pass
    @Smoothing.setter
    def Smoothing(self, smoothing: TrimLineDevelopmentBuilder.SmoothingName):
        """
        Setter for property: ( TrimLineDevelopmentBuilder.SmoothingName NXOp) Smoothing
         Returns the curve smoothing method - linear (none), cubic or quintic   
            
         
        """
        pass
    @property
    def SolverConvergencyLevel(self) -> TrimLineDevelopmentBuilder.Convergency:
        """
        Getter for property: ( TrimLineDevelopmentBuilder.Convergency NXOp) SolverConvergencyLevel
         Returns the convergency level of onestep solver.  
             
         
        """
        pass
    @SolverConvergencyLevel.setter
    def SolverConvergencyLevel(self, solverConvergencyLevel: TrimLineDevelopmentBuilder.Convergency):
        """
        Setter for property: ( TrimLineDevelopmentBuilder.Convergency NXOp) SolverConvergencyLevel
         Returns the convergency level of onestep solver.  
             
         
        """
        pass
    @property
    def SolverJoinOutputCurves(self) -> bool:
        """
        Getter for property: (bool) SolverJoinOutputCurves
         Returns the option to join output curves.  
          
                If it is true, join output curves. If it is false, do not join output curves  
         
        """
        pass
    @SolverJoinOutputCurves.setter
    def SolverJoinOutputCurves(self, solverJoinOutputCurves: bool):
        """
        Setter for property: (bool) SolverJoinOutputCurves
         Returns the option to join output curves.  
          
                If it is true, join output curves. If it is false, do not join output curves  
         
        """
        pass
    @property
    def SolverMaxIterationSteps(self) -> int:
        """
        Getter for property: (int) SolverMaxIterationSteps
         Returnsthe maximum number of iteration steps in onestep solver.  
             
         
        """
        pass
    @SolverMaxIterationSteps.setter
    def SolverMaxIterationSteps(self, solverMaxIterationSteps: int):
        """
        Setter for property: (int) SolverMaxIterationSteps
         Returnsthe maximum number of iteration steps in onestep solver.  
             
         
        """
        pass
    @property
    def SolverSaveAnalysisResultsIntoFeature(self) -> bool:
        """
        Getter for property: (bool) SolverSaveAnalysisResultsIntoFeature
         Returns the option to save analysis result into feature.  
          
                If it is true, save analysis result into feature. If it is false, do not save analysis result into feature.  
         
        """
        pass
    @SolverSaveAnalysisResultsIntoFeature.setter
    def SolverSaveAnalysisResultsIntoFeature(self, solverSaveAnalysisResultsIntoFeature: bool):
        """
        Setter for property: (bool) SolverSaveAnalysisResultsIntoFeature
         Returns the option to save analysis result into feature.  
          
                If it is true, save analysis result into feature. If it is false, do not save analysis result into feature.  
         
        """
        pass
    @property
    def Spine(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Spine
         Returns the spine string, which determines the orientation of the sample planes   
            
         
        """
        pass
    @property
    def SpineRadius(self) -> float:
        """
        Getter for property: (float) SpineRadius
         Returns the spine radius, used by  NXOpen::Die::TrimLineDevelopmentBuilder::CreateDefaultSpine    
            
         
        """
        pass
    @SpineRadius.setter
    def SpineRadius(self, spineRadius: float):
        """
        Setter for property: (float) SpineRadius
         Returns the spine radius, used by  NXOpen::Die::TrimLineDevelopmentBuilder::CreateDefaultSpine    
            
         
        """
        pass
    @property
    def SurfaceType(self) -> TrimLineDevelopmentBuilder.Surface:
        """
        Getter for property: ( TrimLineDevelopmentBuilder.Surface NXOp) SurfaceType
         Returns the surface type used to determine offset direction.  
             
         
        """
        pass
    @SurfaceType.setter
    def SurfaceType(self, surfaceType: TrimLineDevelopmentBuilder.Surface):
        """
        Setter for property: ( TrimLineDevelopmentBuilder.Surface NXOp) SurfaceType
         Returns the surface type used to determine offset direction.  
             
         
        """
        pass
    @property
    def Thickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Thickness
         Returns the material thickness.  
            Value should be greater than zero.   
         
        """
        pass
    @property
    def TrimlinePoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) TrimlinePoint
         Returns the point where the thickness direction is defined for trimline.  
             
         
        """
        pass
    @TrimlinePoint.setter
    def TrimlinePoint(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) TrimlinePoint
         Returns the point where the thickness direction is defined for trimline.  
             
         
        """
        pass
    @property
    def Type(self) -> TrimLineDevelopmentBuilder.CalculateType:
        """
        Getter for property: ( TrimLineDevelopmentBuilder.CalculateType NXOp) Type
         Returns the calculate method type.  
             
         
        """
        pass
    @Type.setter
    def Type(self, type: TrimLineDevelopmentBuilder.CalculateType):
        """
        Setter for property: ( TrimLineDevelopmentBuilder.CalculateType NXOp) Type
         Returns the calculate method type.  
             
         
        """
        pass
    def Calculation(self) -> None:
        """
         Starts solver to calculate. 
        """
        pass
    def CreateDefaultSpine(self) -> None:
        """
         Creates a smoothed spine curve from the forming boundary using the spine radius value 
        """
        pass
    def DefaultDraw(self) -> None:
        """
         Creates a default draw vector by finding the least squares plane of the formed faces 
        """
        pass
    def Mesh(self) -> None:
        """
         Create FEM 2-D meshes based on the unform region surfaces and the target region surfaces.
        """
        pass
import NXOpen
class TrimSteelParametersBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Die.TrimSteelParametersBuilder
    """
    @property
    def BaseFaceColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) BaseFaceColor
         Returns the base face color   
            
         
        """
        pass
    @BaseFaceColor.setter
    def BaseFaceColor(self, baseFaceColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) BaseFaceColor
         Returns the base face color   
            
         
        """
        pass
    @property
    def BaseFaceTitle(self) -> str:
        """
        Getter for property: (str) BaseFaceTitle
         Returns the base face title   
            
         
        """
        pass
    @BaseFaceTitle.setter
    def BaseFaceTitle(self, baseFaceTitle: str):
        """
        Setter for property: (str) BaseFaceTitle
         Returns the base face title   
            
         
        """
        pass
    @property
    def BaseFaceValue(self) -> str:
        """
        Getter for property: (str) BaseFaceValue
         Returns the base face value   
            
         
        """
        pass
    @BaseFaceValue.setter
    def BaseFaceValue(self, baseFaceValue: str):
        """
        Setter for property: (str) BaseFaceValue
         Returns the base face value   
            
         
        """
        pass
    @property
    def BaseHeight(self) -> float:
        """
        Getter for property: (float) BaseHeight
         Returns the base height   
            
         
        """
        pass
    @BaseHeight.setter
    def BaseHeight(self, baseHeight: float):
        """
        Setter for property: (float) BaseHeight
         Returns the base height   
            
         
        """
        pass
    @property
    def BeltThick(self) -> float:
        """
        Getter for property: (float) BeltThick
         Returns the belt thick   
            
         
        """
        pass
    @BeltThick.setter
    def BeltThick(self, beltThick: float):
        """
        Setter for property: (float) BeltThick
         Returns the belt thick   
            
         
        """
        pass
    @property
    def BoltAttrDepthTitle(self) -> str:
        """
        Getter for property: (str) BoltAttrDepthTitle
         Returns the bolt attr depth title   
            
         
        """
        pass
    @BoltAttrDepthTitle.setter
    def BoltAttrDepthTitle(self, boltAttrDepthTitle: str):
        """
        Setter for property: (str) BoltAttrDepthTitle
         Returns the bolt attr depth title   
            
         
        """
        pass
    @property
    def BoltAttrDiaTitle(self) -> str:
        """
        Getter for property: (str) BoltAttrDiaTitle
         Returns the bolt attr dia title   
            
         
        """
        pass
    @BoltAttrDiaTitle.setter
    def BoltAttrDiaTitle(self, boltAttrDiaTitle: str):
        """
        Setter for property: (str) BoltAttrDiaTitle
         Returns the bolt attr dia title   
            
         
        """
        pass
    @property
    def BoltCboreDiaTitle(self) -> str:
        """
        Getter for property: (str) BoltCboreDiaTitle
         Returns the bolt cbore dia title   
            
         
        """
        pass
    @BoltCboreDiaTitle.setter
    def BoltCboreDiaTitle(self, boltCboreDiaTitle: str):
        """
        Setter for property: (str) BoltCboreDiaTitle
         Returns the bolt cbore dia title   
            
         
        """
        pass
    @property
    def BoltDepth(self) -> float:
        """
        Getter for property: (float) BoltDepth
         Returns the bolt depth   
            
         
        """
        pass
    @BoltDepth.setter
    def BoltDepth(self, boltDepth: float):
        """
        Setter for property: (float) BoltDepth
         Returns the bolt depth   
            
         
        """
        pass
    @property
    def BoltDia(self) -> float:
        """
        Getter for property: (float) BoltDia
         Returns the bolt dia   
            
         
        """
        pass
    @BoltDia.setter
    def BoltDia(self, boltDia: float):
        """
        Setter for property: (float) BoltDia
         Returns the bolt dia   
            
         
        """
        pass
    @property
    def BoltHoleColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) BoltHoleColor
         Returns the bolt hole color   
            
         
        """
        pass
    @BoltHoleColor.setter
    def BoltHoleColor(self, boltHoleColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) BoltHoleColor
         Returns the bolt hole color   
            
         
        """
        pass
    @property
    def BoltHoleTitle(self) -> str:
        """
        Getter for property: (str) BoltHoleTitle
         Returns the bolt hole title   
            
         
        """
        pass
    @BoltHoleTitle.setter
    def BoltHoleTitle(self, boltHoleTitle: str):
        """
        Setter for property: (str) BoltHoleTitle
         Returns the bolt hole title   
            
         
        """
        pass
    @property
    def BoltHoleValue(self) -> str:
        """
        Getter for property: (str) BoltHoleValue
         Returns the bolt hole value   
            
         
        """
        pass
    @BoltHoleValue.setter
    def BoltHoleValue(self, boltHoleValue: str):
        """
        Setter for property: (str) BoltHoleValue
         Returns the bolt hole value   
            
         
        """
        pass
    @property
    def CBoreDia(self) -> float:
        """
        Getter for property: (float) CBoreDia
         Returns the c bore dia   
            
         
        """
        pass
    @CBoreDia.setter
    def CBoreDia(self, cBoreDia: float):
        """
        Setter for property: (float) CBoreDia
         Returns the c bore dia   
            
         
        """
        pass
    @property
    def CboreBaseAttrColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) CboreBaseAttrColor
         Returns the cbore base attr color   
            
         
        """
        pass
    @CboreBaseAttrColor.setter
    def CboreBaseAttrColor(self, cboreBaseAttrColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) CboreBaseAttrColor
         Returns the cbore base attr color   
            
         
        """
        pass
    @property
    def CboreBaseAttrTitle(self) -> str:
        """
        Getter for property: (str) CboreBaseAttrTitle
         Returns the cbore base attr title   
            
         
        """
        pass
    @CboreBaseAttrTitle.setter
    def CboreBaseAttrTitle(self, cboreBaseAttrTitle: str):
        """
        Setter for property: (str) CboreBaseAttrTitle
         Returns the cbore base attr title   
            
         
        """
        pass
    @property
    def CboreBaseAttrValue(self) -> str:
        """
        Getter for property: (str) CboreBaseAttrValue
         Returns the cbore base attr value   
            
         
        """
        pass
    @CboreBaseAttrValue.setter
    def CboreBaseAttrValue(self, cboreBaseAttrValue: str):
        """
        Setter for property: (str) CboreBaseAttrValue
         Returns the cbore base attr value   
            
         
        """
        pass
    @property
    def Distance1(self) -> float:
        """
        Getter for property: (float) Distance1
         Returns the distance1   
            
         
        """
        pass
    @Distance1.setter
    def Distance1(self, distance1: float):
        """
        Setter for property: (float) Distance1
         Returns the distance1   
            
         
        """
        pass
    @property
    def Distance2(self) -> float:
        """
        Getter for property: (float) Distance2
         Returns the distance2   
            
         
        """
        pass
    @Distance2.setter
    def Distance2(self, distance2: float):
        """
        Setter for property: (float) Distance2
         Returns the distance2   
            
         
        """
        pass
    @property
    def DowelDia(self) -> float:
        """
        Getter for property: (float) DowelDia
         Returns the dowel dia   
            
         
        """
        pass
    @DowelDia.setter
    def DowelDia(self, dowelDia: float):
        """
        Setter for property: (float) DowelDia
         Returns the dowel dia   
            
         
        """
        pass
    @property
    def DowelDiameterTitle(self) -> str:
        """
        Getter for property: (str) DowelDiameterTitle
         Returns the dowel diameter title   
            
         
        """
        pass
    @DowelDiameterTitle.setter
    def DowelDiameterTitle(self, dowelDiameterTitle: str):
        """
        Setter for property: (str) DowelDiameterTitle
         Returns the dowel diameter title   
            
         
        """
        pass
    @property
    def DowelHoleColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) DowelHoleColor
         Returns the dowel hole color   
            
         
        """
        pass
    @DowelHoleColor.setter
    def DowelHoleColor(self, dowelHoleColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) DowelHoleColor
         Returns the dowel hole color   
            
         
        """
        pass
    @property
    def DowelHoleTitle(self) -> str:
        """
        Getter for property: (str) DowelHoleTitle
         Returns the dowel hole title   
            
         
        """
        pass
    @DowelHoleTitle.setter
    def DowelHoleTitle(self, dowelHoleTitle: str):
        """
        Setter for property: (str) DowelHoleTitle
         Returns the dowel hole title   
            
         
        """
        pass
    @property
    def DowelHoleValue(self) -> str:
        """
        Getter for property: (str) DowelHoleValue
         Returns the dowel hole value   
            
         
        """
        pass
    @DowelHoleValue.setter
    def DowelHoleValue(self, dowelHoleValue: str):
        """
        Setter for property: (str) DowelHoleValue
         Returns the dowel hole value   
            
         
        """
        pass
    @property
    def EndFaceColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) EndFaceColor
         Returns the end face color   
            
         
        """
        pass
    @EndFaceColor.setter
    def EndFaceColor(self, endFaceColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) EndFaceColor
         Returns the end face color   
            
         
        """
        pass
    @property
    def EndFaceTitle(self) -> str:
        """
        Getter for property: (str) EndFaceTitle
         Returns the end face title   
            
         
        """
        pass
    @EndFaceTitle.setter
    def EndFaceTitle(self, endFaceTitle: str):
        """
        Setter for property: (str) EndFaceTitle
         Returns the end face title   
            
         
        """
        pass
    @property
    def EndFaceValue(self) -> str:
        """
        Getter for property: (str) EndFaceValue
         Returns the end face value   
            
         
        """
        pass
    @EndFaceValue.setter
    def EndFaceValue(self, endFaceValue: str):
        """
        Setter for property: (str) EndFaceValue
         Returns the end face value   
            
         
        """
        pass
    @property
    def FormingFaceColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) FormingFaceColor
         Returns the forming face color   
            
         
        """
        pass
    @FormingFaceColor.setter
    def FormingFaceColor(self, formingFaceColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) FormingFaceColor
         Returns the forming face color   
            
         
        """
        pass
    @property
    def FormingFaceTitle(self) -> str:
        """
        Getter for property: (str) FormingFaceTitle
         Returns the forming face title   
            
         
        """
        pass
    @FormingFaceTitle.setter
    def FormingFaceTitle(self, formingFaceTitle: str):
        """
        Setter for property: (str) FormingFaceTitle
         Returns the forming face title   
            
         
        """
        pass
    @property
    def FormingFaceValue(self) -> str:
        """
        Getter for property: (str) FormingFaceValue
         Returns the forming face value   
            
         
        """
        pass
    @FormingFaceValue.setter
    def FormingFaceValue(self, formingFaceValue: str):
        """
        Setter for property: (str) FormingFaceValue
         Returns the forming face value   
            
         
        """
        pass
    @property
    def LandAngl(self) -> float:
        """
        Getter for property: (float) LandAngl
         Returns the land angl   
            
         
        """
        pass
    @LandAngl.setter
    def LandAngl(self, landAngl: float):
        """
        Setter for property: (float) LandAngl
         Returns the land angl   
            
         
        """
        pass
    @property
    def LandRelief(self) -> float:
        """
        Getter for property: (float) LandRelief
         Returns the land relief   
            
         
        """
        pass
    @LandRelief.setter
    def LandRelief(self, landRelief: float):
        """
        Setter for property: (float) LandRelief
         Returns the land relief   
            
         
        """
        pass
    @property
    def LandThick(self) -> float:
        """
        Getter for property: (float) LandThick
         Returns the land thick   
            
         
        """
        pass
    @LandThick.setter
    def LandThick(self, landThick: float):
        """
        Setter for property: (float) LandThick
         Returns the land thick   
            
         
        """
        pass
    @property
    def LifterDia(self) -> float:
        """
        Getter for property: (float) LifterDia
         Returns the lifter dia   
            
         
        """
        pass
    @LifterDia.setter
    def LifterDia(self, lifterDia: float):
        """
        Setter for property: (float) LifterDia
         Returns the lifter dia   
            
         
        """
        pass
    @property
    def LifterHeight(self) -> float:
        """
        Getter for property: (float) LifterHeight
         Returns the lifter height   
            
         
        """
        pass
    @LifterHeight.setter
    def LifterHeight(self, lifterHeight: float):
        """
        Setter for property: (float) LifterHeight
         Returns the lifter height   
            
         
        """
        pass
    @property
    def LwCutterClearance(self) -> float:
        """
        Getter for property: (float) LwCutterClearance
         Returns the lw cutter clearance   
            
         
        """
        pass
    @LwCutterClearance.setter
    def LwCutterClearance(self, lwCutterClearance: float):
        """
        Setter for property: (float) LwCutterClearance
         Returns the lw cutter clearance   
            
         
        """
        pass
    @property
    def PushPinDia(self) -> float:
        """
        Getter for property: (float) PushPinDia
         Returns the push pin dia   
            
         
        """
        pass
    @PushPinDia.setter
    def PushPinDia(self, pushPinDia: float):
        """
        Setter for property: (float) PushPinDia
         Returns the push pin dia   
            
         
        """
        pass
    @property
    def PushPinInnerDepth(self) -> float:
        """
        Getter for property: (float) PushPinInnerDepth
         Returns the push pin inner depth   
            
         
        """
        pass
    @PushPinInnerDepth.setter
    def PushPinInnerDepth(self, pushPinInnerDepth: float):
        """
        Setter for property: (float) PushPinInnerDepth
         Returns the push pin inner depth   
            
         
        """
        pass
    @property
    def PushPinInnerDia(self) -> float:
        """
        Getter for property: (float) PushPinInnerDia
         Returns the push pin inner dia   
            
         
        """
        pass
    @PushPinInnerDia.setter
    def PushPinInnerDia(self, pushPinInnerDia: float):
        """
        Setter for property: (float) PushPinInnerDia
         Returns the push pin inner dia   
            
         
        """
        pass
    @property
    def Relief(self) -> float:
        """
        Getter for property: (float) Relief
         Returns the relief   
            
         
        """
        pass
    @Relief.setter
    def Relief(self, relief: float):
        """
        Setter for property: (float) Relief
         Returns the relief   
            
         
        """
        pass
    @property
    def ReliefAngl(self) -> float:
        """
        Getter for property: (float) ReliefAngl
         Returns the relief angl   
            
         
        """
        pass
    @ReliefAngl.setter
    def ReliefAngl(self, reliefAngl: float):
        """
        Setter for property: (float) ReliefAngl
         Returns the relief angl   
            
         
        """
        pass
    @property
    def RibDistance(self) -> float:
        """
        Getter for property: (float) RibDistance
         Returns the rib distance   
            
         
        """
        pass
    @RibDistance.setter
    def RibDistance(self, ribDistance: float):
        """
        Setter for property: (float) RibDistance
         Returns the rib distance   
            
         
        """
        pass
    @property
    def RibHeightLimit(self) -> float:
        """
        Getter for property: (float) RibHeightLimit
         Returns the rib height limit   
            
         
        """
        pass
    @RibHeightLimit.setter
    def RibHeightLimit(self, ribHeightLimit: float):
        """
        Setter for property: (float) RibHeightLimit
         Returns the rib height limit   
            
         
        """
        pass
    @property
    def RibThickness(self) -> float:
        """
        Getter for property: (float) RibThickness
         Returns the rib thickness   
            
         
        """
        pass
    @RibThickness.setter
    def RibThickness(self, ribThickness: float):
        """
        Setter for property: (float) RibThickness
         Returns the rib thickness   
            
         
        """
        pass
    @property
    def ScrapCutFaceColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) ScrapCutFaceColor
         Returns the scrap cut face color   
            
         
        """
        pass
    @ScrapCutFaceColor.setter
    def ScrapCutFaceColor(self, scrapCutFaceColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) ScrapCutFaceColor
         Returns the scrap cut face color   
            
         
        """
        pass
    @property
    def ScrapCutFaceTitle(self) -> str:
        """
        Getter for property: (str) ScrapCutFaceTitle
         Returns the scrap cut face title   
            
         
        """
        pass
    @ScrapCutFaceTitle.setter
    def ScrapCutFaceTitle(self, scrapCutFaceTitle: str):
        """
        Setter for property: (str) ScrapCutFaceTitle
         Returns the scrap cut face title   
            
         
        """
        pass
    @property
    def ScrapCutFaceValue(self) -> str:
        """
        Getter for property: (str) ScrapCutFaceValue
         Returns the scrap cut face value   
            
         
        """
        pass
    @ScrapCutFaceValue.setter
    def ScrapCutFaceValue(self, scrapCutFaceValue: str):
        """
        Setter for property: (str) ScrapCutFaceValue
         Returns the scrap cut face value   
            
         
        """
        pass
    @property
    def ScrapCutOverhang(self) -> float:
        """
        Getter for property: (float) ScrapCutOverhang
         Returns the scrap cut overhang   
            
         
        """
        pass
    @ScrapCutOverhang.setter
    def ScrapCutOverhang(self, scrapCutOverhang: float):
        """
        Setter for property: (float) ScrapCutOverhang
         Returns the scrap cut overhang   
            
         
        """
        pass
    @property
    def SteelBodyAttrColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) SteelBodyAttrColor
         Returns the steel body attr color   
            
         
        """
        pass
    @SteelBodyAttrColor.setter
    def SteelBodyAttrColor(self, steelBodyAttrColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) SteelBodyAttrColor
         Returns the steel body attr color   
            
         
        """
        pass
    @property
    def SteelBodyAttrTitle(self) -> str:
        """
        Getter for property: (str) SteelBodyAttrTitle
         Returns the steel body attr title   
            
         
        """
        pass
    @SteelBodyAttrTitle.setter
    def SteelBodyAttrTitle(self, steelBodyAttrTitle: str):
        """
        Setter for property: (str) SteelBodyAttrTitle
         Returns the steel body attr title   
            
         
        """
        pass
    @property
    def SteelBodyAttrValue(self) -> str:
        """
        Getter for property: (str) SteelBodyAttrValue
         Returns the steel body attr value   
            
         
        """
        pass
    @SteelBodyAttrValue.setter
    def SteelBodyAttrValue(self, steelBodyAttrValue: str):
        """
        Setter for property: (str) SteelBodyAttrValue
         Returns the steel body attr value   
            
         
        """
        pass
    @property
    def SteelEntranceParm(self) -> float:
        """
        Getter for property: (float) SteelEntranceParm
         Returns the steel entrance parm   
            
         
        """
        pass
    @SteelEntranceParm.setter
    def SteelEntranceParm(self, steelEntranceParm: float):
        """
        Setter for property: (float) SteelEntranceParm
         Returns the steel entrance parm   
            
         
        """
        pass
    @property
    def SteelRelief(self) -> float:
        """
        Getter for property: (float) SteelRelief
         Returns the steel relief   
            
         
        """
        pass
    @SteelRelief.setter
    def SteelRelief(self, steelRelief: float):
        """
        Setter for property: (float) SteelRelief
         Returns the steel relief   
            
         
        """
        pass
    @property
    def SteepWallMinEntrance(self) -> float:
        """
        Getter for property: (float) SteepWallMinEntrance
         Returns the steep wall min entrance   
            
         
        """
        pass
    @SteepWallMinEntrance.setter
    def SteepWallMinEntrance(self, steepWallMinEntrance: float):
        """
        Setter for property: (float) SteepWallMinEntrance
         Returns the steep wall min entrance   
            
         
        """
        pass
    @property
    def TabDepth(self) -> float:
        """
        Getter for property: (float) TabDepth
         Returns the tab depth   
            
         
        """
        pass
    @TabDepth.setter
    def TabDepth(self, tabDepth: float):
        """
        Setter for property: (float) TabDepth
         Returns the tab depth   
            
         
        """
        pass
    @property
    def TabFaceColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) TabFaceColor
         Returns the tab face color   
            
         
        """
        pass
    @TabFaceColor.setter
    def TabFaceColor(self, tabFaceColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) TabFaceColor
         Returns the tab face color   
            
         
        """
        pass
    @property
    def TabFaceTitle(self) -> str:
        """
        Getter for property: (str) TabFaceTitle
         Returns the tab face title   
            
         
        """
        pass
    @TabFaceTitle.setter
    def TabFaceTitle(self, tabFaceTitle: str):
        """
        Setter for property: (str) TabFaceTitle
         Returns the tab face title   
            
         
        """
        pass
    @property
    def TabFaceValue(self) -> str:
        """
        Getter for property: (str) TabFaceValue
         Returns the tab face value   
            
         
        """
        pass
    @TabFaceValue.setter
    def TabFaceValue(self, tabFaceValue: str):
        """
        Setter for property: (str) TabFaceValue
         Returns the tab face value   
            
         
        """
        pass
    @property
    def TabRelief(self) -> float:
        """
        Getter for property: (float) TabRelief
         Returns the tab relief   
            
         
        """
        pass
    @TabRelief.setter
    def TabRelief(self, tabRelief: float):
        """
        Setter for property: (float) TabRelief
         Returns the tab relief   
            
         
        """
        pass
    @property
    def TabWidth(self) -> float:
        """
        Getter for property: (float) TabWidth
         Returns the tab width   
            
         
        """
        pass
    @TabWidth.setter
    def TabWidth(self, tabWidth: float):
        """
        Setter for property: (float) TabWidth
         Returns the tab width   
            
         
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
    @property
    def TrmEdgeTitle(self) -> str:
        """
        Getter for property: (str) TrmEdgeTitle
         Returns the trm edge title   
            
         
        """
        pass
    @TrmEdgeTitle.setter
    def TrmEdgeTitle(self, trmEdgeTitle: str):
        """
        Setter for property: (str) TrmEdgeTitle
         Returns the trm edge title   
            
         
        """
        pass
    @property
    def TrmEdgeValue(self) -> str:
        """
        Getter for property: (str) TrmEdgeValue
         Returns the trm edge value   
            
         
        """
        pass
    @TrmEdgeValue.setter
    def TrmEdgeValue(self, trmEdgeValue: str):
        """
        Setter for property: (str) TrmEdgeValue
         Returns the trm edge value   
            
         
        """
        pass
    @property
    def TrmWalFaceValue(self) -> str:
        """
        Getter for property: (str) TrmWalFaceValue
         Returns the trm wal face value   
            
         
        """
        pass
    @TrmWalFaceValue.setter
    def TrmWalFaceValue(self, trmWalFaceValue: str):
        """
        Setter for property: (str) TrmWalFaceValue
         Returns the trm wal face value   
            
         
        """
        pass
    @property
    def TrmWallFaceColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) TrmWallFaceColor
         Returns the trm wall face color   
            
         
        """
        pass
    @TrmWallFaceColor.setter
    def TrmWallFaceColor(self, trmWallFaceColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) TrmWallFaceColor
         Returns the trm wall face color   
            
         
        """
        pass
    @property
    def TrmWallFaceTitle(self) -> str:
        """
        Getter for property: (str) TrmWallFaceTitle
         Returns the trm wall face title   
            
         
        """
        pass
    @TrmWallFaceTitle.setter
    def TrmWallFaceTitle(self, trmWallFaceTitle: str):
        """
        Setter for property: (str) TrmWallFaceTitle
         Returns the trm wall face title   
            
         
        """
        pass
    def CoverParmsFromSorceBuilderToBuilder(self, sourceBuilder: NXOpen.Builder) -> None:
        """
         Cover parameters data from source builder to this builder 
        """
        pass
    def ResetParameters(self) -> None:
        """
         Reset trim steel parameters as customer default setting 
        """
        pass
    def ValidateTrimSteelParameters(self) -> None:
        """
         Validate trim steel parameters 
        """
        pass
import NXOpen
import NXOpen.Features
class TrimTaskBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Trim Task feature builder. """
    class CamTypes(Enum):
        """
        Members Include: 
         |Direct|  Direct 
         |Aerial|  Aerial Cam 
         |BaseMounted|  Base Mounted Cam 

        """
        Direct: int
        Aerial: int
        BaseMounted: int
        @staticmethod
        def ValueOf(value: int) -> TrimTaskBuilder.CamTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MatchCutTypes(Enum):
        """
        Members Include: 
         |NotSet|  No match cut. 
         |AtStart|  At start plane only. 
         |AtEnd|  At end plane only. 
         |AtBoth|  At both start and end planes. 

        """
        NotSet: int
        AtStart: int
        AtEnd: int
        AtBoth: int
        @staticmethod
        def ValueOf(value: int) -> TrimTaskBuilder.MatchCutTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngleTolerance(self) -> float:
        """
        Getter for property: (float) AngleTolerance
         Returns the angle tolerance of the trim task   
            
         
        """
        pass
    @AngleTolerance.setter
    def AngleTolerance(self, angle_tolerance: float):
        """
        Setter for property: (float) AngleTolerance
         Returns the angle tolerance of the trim task   
            
         
        """
        pass
    @property
    def CamDirection(self) -> NXOpen.ILocation:
        """
        Getter for property: ( NXOpen.ILocation) CamDirection
         Returns the cam direction of the trim task   
            
         
        """
        pass
    @CamDirection.setter
    def CamDirection(self, cam_direction: NXOpen.ILocation):
        """
        Setter for property: ( NXOpen.ILocation) CamDirection
         Returns the cam direction of the trim task   
            
         
        """
        pass
    @property
    def CamType(self) -> TrimTaskBuilder.CamTypes:
        """
        Getter for property: ( TrimTaskBuilder.CamTypes NXOp) CamType
         Returns the cam type of the trim task   
            
         
        """
        pass
    @CamType.setter
    def CamType(self, cam_type: TrimTaskBuilder.CamTypes):
        """
        Setter for property: ( TrimTaskBuilder.CamTypes NXOp) CamType
         Returns the cam type of the trim task   
            
         
        """
        pass
    @property
    def CreateScrap(self) -> bool:
        """
        Getter for property: (bool) CreateScrap
         Returns the create scrap setting of the trim task.  
           
                True indicates that the scrap is to be created.   
         
        """
        pass
    @CreateScrap.setter
    def CreateScrap(self, create_scrap: bool):
        """
        Setter for property: (bool) CreateScrap
         Returns the create scrap setting of the trim task.  
           
                True indicates that the scrap is to be created.   
         
        """
        pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance of the trim task   
            
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distance_tolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance of the trim task   
            
         
        """
        pass
    @property
    def EndPlane(self) -> NXOpen.ISurface:
        """
        Getter for property: ( NXOpen.ISurface) EndPlane
         Returns the end plane of the trim task   
            
         
        """
        pass
    @EndPlane.setter
    def EndPlane(self, end_plane: NXOpen.ISurface):
        """
        Setter for property: ( NXOpen.ISurface) EndPlane
         Returns the end plane of the trim task   
            
         
        """
        pass
    @property
    def FinishOperation(self) -> bool:
        """
        Getter for property: (bool) FinishOperation
         Returns the finish operation of the trim task 
                True indicates the trim is to be a finish trim.  
           False indicates rough trim.   
         
        """
        pass
    @FinishOperation.setter
    def FinishOperation(self, finish_operation: bool):
        """
        Setter for property: (bool) FinishOperation
         Returns the finish operation of the trim task 
                True indicates the trim is to be a finish trim.  
           False indicates rough trim.   
         
        """
        pass
    @property
    def LayoutFlange(self) -> bool:
        """
        Getter for property: (bool) LayoutFlange
         Returns the layout flange setting of the trim task.  
           
                True indicates that the trim curve is to be laid out on the flange.   
         
        """
        pass
    @LayoutFlange.setter
    def LayoutFlange(self, layout_flange: bool):
        """
        Setter for property: (bool) LayoutFlange
         Returns the layout flange setting of the trim task.  
           
                True indicates that the trim curve is to be laid out on the flange.   
         
        """
        pass
    @property
    def MatchCutExtensionAngle(self) -> float:
        """
        Getter for property: (float) MatchCutExtensionAngle
         Returns the match cut extension angle dimension of the trim task   
            
         
        """
        pass
    @MatchCutExtensionAngle.setter
    def MatchCutExtensionAngle(self, extension_angle: float):
        """
        Setter for property: (float) MatchCutExtensionAngle
         Returns the match cut extension angle dimension of the trim task   
            
         
        """
        pass
    @property
    def MatchCutFirstRadius(self) -> float:
        """
        Getter for property: (float) MatchCutFirstRadius
         Returns the match cut first radius dimension of the trim task   
            
         
        """
        pass
    @MatchCutFirstRadius.setter
    def MatchCutFirstRadius(self, first_radius: float):
        """
        Setter for property: (float) MatchCutFirstRadius
         Returns the match cut first radius dimension of the trim task   
            
         
        """
        pass
    @property
    def MatchCutNotchOffset(self) -> float:
        """
        Getter for property: (float) MatchCutNotchOffset
         Returns the match cut notch offset dimension of the trim task   
            
         
        """
        pass
    @MatchCutNotchOffset.setter
    def MatchCutNotchOffset(self, notch_offset: float):
        """
        Setter for property: (float) MatchCutNotchOffset
         Returns the match cut notch offset dimension of the trim task   
            
         
        """
        pass
    @property
    def MatchCutOffsetFromPlane(self) -> float:
        """
        Getter for property: (float) MatchCutOffsetFromPlane
         Returns the match cut offset from plane dimension of the trim task   
            
         
        """
        pass
    @MatchCutOffsetFromPlane.setter
    def MatchCutOffsetFromPlane(self, offset_from_plane: float):
        """
        Setter for property: (float) MatchCutOffsetFromPlane
         Returns the match cut offset from plane dimension of the trim task   
            
         
        """
        pass
    @property
    def MatchCutOffsetLength(self) -> float:
        """
        Getter for property: (float) MatchCutOffsetLength
         Returns the match cut offset length dimension of the trim task   
            
         
        """
        pass
    @MatchCutOffsetLength.setter
    def MatchCutOffsetLength(self, offset_length: float):
        """
        Setter for property: (float) MatchCutOffsetLength
         Returns the match cut offset length dimension of the trim task   
            
         
        """
        pass
    @property
    def MatchCutScrapCutterLength(self) -> float:
        """
        Getter for property: (float) MatchCutScrapCutterLength
         Returns the match cut scrap cutter length dimension of the trim task   
            
         
        """
        pass
    @MatchCutScrapCutterLength.setter
    def MatchCutScrapCutterLength(self, scrap_cutter_length: float):
        """
        Setter for property: (float) MatchCutScrapCutterLength
         Returns the match cut scrap cutter length dimension of the trim task   
            
         
        """
        pass
    @property
    def MatchCutSecondRadius(self) -> float:
        """
        Getter for property: (float) MatchCutSecondRadius
         Returns the match cut second radius dimension of the trim task   
            
         
        """
        pass
    @MatchCutSecondRadius.setter
    def MatchCutSecondRadius(self, second_radius: float):
        """
        Setter for property: (float) MatchCutSecondRadius
         Returns the match cut second radius dimension of the trim task   
            
         
        """
        pass
    @property
    def MatchCutThirdRadius(self) -> float:
        """
        Getter for property: (float) MatchCutThirdRadius
         Returns the match cut third radius dimension of the trim task   
            
         
        """
        pass
    @MatchCutThirdRadius.setter
    def MatchCutThirdRadius(self, third_radius: float):
        """
        Setter for property: (float) MatchCutThirdRadius
         Returns the match cut third radius dimension of the trim task   
            
         
        """
        pass
    @property
    def MatchCutType(self) -> TrimTaskBuilder.MatchCutTypes:
        """
        Getter for property: ( TrimTaskBuilder.MatchCutTypes NXOp) MatchCutType
         Returns the match cut type of the trim task   
            
         
        """
        pass
    @MatchCutType.setter
    def MatchCutType(self, match_cut_type: TrimTaskBuilder.MatchCutTypes):
        """
        Setter for property: ( TrimTaskBuilder.MatchCutTypes NXOp) MatchCutType
         Returns the match cut type of the trim task   
            
         
        """
        pass
    @property
    def ReverseTrimSide(self) -> bool:
        """
        Getter for property: (bool) ReverseTrimSide
         Returns the reverse trim side setting of the trim task.  
           
                True indicates that the trim side should be reversed.   
         
        """
        pass
    @ReverseTrimSide.setter
    def ReverseTrimSide(self, reverse: bool):
        """
        Setter for property: (bool) ReverseTrimSide
         Returns the reverse trim side setting of the trim task.  
           
                True indicates that the trim side should be reversed.   
         
        """
        pass
    @property
    def StartPlane(self) -> NXOpen.ISurface:
        """
        Getter for property: ( NXOpen.ISurface) StartPlane
         Returns the start plane of the trim task   
            
         
        """
        pass
    @StartPlane.setter
    def StartPlane(self, start_plane: NXOpen.ISurface):
        """
        Setter for property: ( NXOpen.ISurface) StartPlane
         Returns the start plane of the trim task   
            
         
        """
        pass
    @property
    def TippedProduct(self) -> NXOpen.Features.Feature:
        """
        Getter for property: ( NXOpen.Features.Feature) TippedProduct
         Returns the tipped product of the trim task   
            
         
        """
        pass
    @TippedProduct.setter
    def TippedProduct(self, tipped_product: NXOpen.Features.Feature):
        """
        Setter for property: ( NXOpen.Features.Feature) TippedProduct
         Returns the tipped product of the trim task   
            
         
        """
        pass
    @property
    def TrimNewDieFace(self) -> bool:
        """
        Getter for property: (bool) TrimNewDieFace
         Returns the trim new die face, from NX10.  
          0 new stamping output can import one new die face to die engineer process.
                If this trim task will trim this new die face, set newDieFace to true, or else set it to false.   
         
        """
        pass
    @TrimNewDieFace.setter
    def TrimNewDieFace(self, newDieFace: bool):
        """
        Setter for property: (bool) TrimNewDieFace
         Returns the trim new die face, from NX10.  
          0 new stamping output can import one new die face to die engineer process.
                If this trim task will trim this new die face, set newDieFace to true, or else set it to false.   
         
        """
        pass
    def CheckAndMovePlanes(self, origTip: NXOpen.Features.Feature, targetTip: NXOpen.Features.Feature, origStartPlaneTag: NXOpen.ISurface, origEndPlaneTag: NXOpen.ISurface) -> Tuple[NXOpen.ISurface, NXOpen.ISurface]:
        """
         Move end planes if the position of Trim Task is changed. 
         Returns A tuple consisting of (targetStartPlaneTag, targetEndPlaneTag). 
         - targetStartPlaneTag is:  NXOpen.ISurface. Start plane in target operation. .
         - targetEndPlaneTag is:  NXOpen.ISurface. End plane in target operation. .

        """
        pass
    def GetAssociativeObjects(self) -> List[NXOpen.DisplayableObject]:
        """
         Gets the associative objects of the trim task 
         Returns objects ( NXOpen.DisplayableObject Li):  .
        """
        pass
    def GetCameraLayerAndXmlp(self) -> Tuple[List[str], List[str]]:
        """
         Gets the camera layer settings and xmlp data 
         Returns A tuple consisting of (layer_settings, xmlp_data). 
         - layer_settings is: List[str]. 1 layer setting string for each camera object. 
                                                                       the string needs to be 256 characters long 
                                                                       (one for each user layer) with either 0 for off
                                                                       or 1 for on. .
         - xmlp_data is: List[str]. xmlp data .

        """
        pass
    def GetCameraNames(self) -> List[str]:
        """
         Gets the names of the camera 
         Returns strings (List[str]):  each string contains the name of a camera object .
        """
        pass
    def GetCameraViews(self) -> List[NXOpen.View]:
        """
         Gets the camera views of the trim task 
         Returns objects ( NXOpen.View Li):  .
        """
        pass
    def GetDetails(self) -> List[str]:
        """
         Gets the detailed description of the trim task 
         Returns strings (List[str]):  detail strings .
        """
        pass
    def GetScrapCutters(self) -> List[NXOpen.ISurface]:
        """
         Gets the scrap cutters of the trim task 
         Returns planes ( NXOpen.ISurface Li):  .
        """
        pass
    def GetTrimBounds(self) -> Tuple[List[NXOpen.IProfile], DirectionOption]:
        """
         Gets the trim bounds of the trim task 
         Returns A tuple consisting of (profile_entries, direction). 
         - profile_entries is:  NXOpen.IProfile Li. Profile entries that make up the 
                                                                                                   boundary of the trim task .
         - direction is:  DirectionOption NXOp. Profile direction .

        """
        pass
    def SetAssociativeObjects(self, objects: List[NXOpen.DisplayableObject]) -> None:
        """
         Sets the associative objects of the trim task 
        """
        pass
    def SetCameraLayerAndXmlp(self, layer_settings: List[str], xmlp_data: List[str]) -> None:
        """
         Sets the camera layer settings and xmlp data 
        """
        pass
    def SetCameraNames(self, strings: List[str]) -> None:
        """
         Sets the names of the camera 
        """
        pass
    def SetCameraViews(self, objects: List[NXOpen.View]) -> None:
        """
         Sets the camera views of the trim task 
        """
        pass
    def SetDetails(self, strings: List[str]) -> None:
        """
         Sets the detailed description of the trim task 
        """
        pass
    def SetScrapCutters(self, planes: List[NXOpen.ISurface]) -> None:
        """
         Sets the scrap cutters of the trim task 
        """
        pass
    def SetTrimBounds(self, direction: DirectionOption, profile_entries: List[NXOpen.IProfile]) -> None:
        """
         Sets the trim bounds of the trim task.
                Note - Die.TrimTaskBuilder.TippedProduct needs to be called before this function. 
        """
        pass
import NXOpen
class UncutRegionsBuilder(NXOpen.Builder): 
    """ Calculates the uncut regions of a curve given a radius value for the cut tool. """
    class ResultsType(Enum):
        """
        Members Include: 
         |OneSide|  Find uncut regions on one side only 
         |BothSides|  Find uncut regions on both sides of curve 

        """
        OneSide: int
        BothSides: int
        @staticmethod
        def ValueOf(value: int) -> UncutRegionsBuilder.ResultsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Curves(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Curves
         Returns the curves to check for uncut regions.  
             
         
        """
        pass
    @property
    def Results(self) -> UncutRegionsBuilder.ResultsType:
        """
        Getter for property: ( UncutRegionsBuilder.ResultsType NXOp) Results
         Returns the side of the curve to show the results.  
             
         
        """
        pass
    @Results.setter
    def Results(self, results: UncutRegionsBuilder.ResultsType):
        """
        Setter for property: ( UncutRegionsBuilder.ResultsType NXOp) Results
         Returns the side of the curve to show the results.  
             
         
        """
        pass
    @property
    def ToolAxis(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ToolAxis
         Returns the tool axis.  
             
         
        """
        pass
    @ToolAxis.setter
    def ToolAxis(self, toolAxis: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ToolAxis
         Returns the tool axis.  
             
         
        """
        pass
    @property
    def ToolSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ToolSize
         Returns the expression that contains the tool radius.  
             
         
        """
        pass
    def ReverseSide(self) -> None:
        """
         Reverse the tool side 
        """
        pass
import NXOpen
import NXOpen.Features
class WearPlateLocChildBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Die Wear Plate Locator sub feature. """
    class PositionType(Enum):
        """
        Members Include: 
         |Left|  Position locator to the left of the wear plate. 
         |Right|  Position locator to the right of the wear plate. 
         |Both|  Position locator on both sides of the wear plate. 
         |Neither|  No locators. 

        """
        Left: int
        Right: int
        Both: int
        Neither: int
        @staticmethod
        def ValueOf(value: int) -> WearPlateLocChildBuilder.PositionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BuildStatus(self) -> DieBuildStatusOption:
        """
        Getter for property: ( DieBuildStatusOption NXOp) BuildStatus
         Returns the build status of wear plate and locators   
            
         
        """
        pass
    @property
    def DesignStatus(self) -> bool:
        """
        Getter for property: (bool) DesignStatus
         Returns the design status of wear plate and locators   
            
         
        """
        pass
    @DesignStatus.setter
    def DesignStatus(self, design_status: bool):
        """
        Setter for property: (bool) DesignStatus
         Returns the design status of wear plate and locators   
            
         
        """
        pass
    @property
    def DisplayStatus(self) -> bool:
        """
        Getter for property: (bool) DisplayStatus
         Returns the display status of wear plate and locators   
            
         
        """
        pass
    @DisplayStatus.setter
    def DisplayStatus(self, display_status: bool):
        """
        Setter for property: (bool) DisplayStatus
         Returns the display status of wear plate and locators   
            
         
        """
        pass
    @property
    def LocatorDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LocatorDepth
         Returns the locator depth of die wear plate and locators   
            
         
        """
        pass
    @property
    def LocatorPosition(self) -> WearPlateLocChildBuilder.PositionType:
        """
        Getter for property: ( WearPlateLocChildBuilder.PositionType NXOp) LocatorPosition
         Returns the locator position of die wear plate and locators   
            
         
        """
        pass
    @LocatorPosition.setter
    def LocatorPosition(self, position: WearPlateLocChildBuilder.PositionType):
        """
        Setter for property: ( WearPlateLocChildBuilder.PositionType NXOp) LocatorPosition
         Returns the locator position of die wear plate and locators   
            
         
        """
        pass
    @property
    def LocatorWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LocatorWidth
         Returns the locator width of die wear plate and locators   
            
         
        """
        pass
    @property
    def Orientation(self) -> NXOpen.ISurface:
        """
        Getter for property: ( NXOpen.ISurface) Orientation
         Returns the orientation plane of die wear plate and locators   
            
         
        """
        pass
    @Orientation.setter
    def Orientation(self, orientation: NXOpen.ISurface):
        """
        Setter for property: ( NXOpen.ISurface) Orientation
         Returns the orientation plane of die wear plate and locators   
            
         
        """
        pass
    @property
    def Point(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Point
         Returns the point location along the centerline of die wear plate and locators   
            
         
        """
        pass
    @property
    def ReverseNormal(self) -> int:
        """
        Getter for property: (int) ReverseNormal
         Returns the reverse normal setting of die wear plate and locators   
            
         
        """
        pass
    @ReverseNormal.setter
    def ReverseNormal(self, reverse_normal: int):
        """
        Setter for property: (int) ReverseNormal
         Returns the reverse normal setting of die wear plate and locators   
            
         
        """
        pass
    @property
    def RibSupportWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RibSupportWidth
         Returns the wear plate rib support width of die wear plate and locators   
            
         
        """
        pass
    @property
    def WearPlateLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) WearPlateLength
         Returns the wear plate length of die wear plate and locators   
            
         
        """
        pass
    @property
    def WearPlateWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) WearPlateWidth
         Returns the wear plate width of die wear plate and locators   
            
         
        """
        pass
    def GetPadAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the pad attributes, note existance of attributes depends on usage in
                main feature 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. title for attribute .
         - value is: str. value of attribute .
         - color is: int. color of pad faces .

        """
        pass
    def GetRecessAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the recess attributes 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. title for attribute .
         - value is: str. value of attribute .
         - color is: int. color of recess faces .

        """
        pass
    def GetReliefAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the relief attributes 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. title for attribute .
         - value is: str. value of attribute .
         - color is: int. color of relief faces .

        """
        pass
    def SetLocatorDepth(self, depth: str) -> None:
        """
         
        """
        pass
    def SetLocatorWidth(self, width: str) -> None:
        """
         
        """
        pass
    def SetPadAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the pad attributes, note existance of attributes depends on usage in
                main feature 
        """
        pass
    def SetPoint(self, point_location: str) -> None:
        """
         
        """
        pass
    def SetRecessAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the recess attributes 
        """
        pass
    def SetReliefAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the relief attributes 
        """
        pass
    def SetRibSupportWidth(self, rib_support_width: str) -> None:
        """
         
        """
        pass
    def SetWearPlateLength(self, length: str) -> None:
        """
         
        """
        pass
    def SetWearPlateWidth(self, width: str) -> None:
        """
         
        """
        pass
import NXOpen
import NXOpen.Features
class WearPlateLocParentBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Die Wear Plate Locator sub feature. """
    class PositionType(Enum):
        """
        Members Include: 
         |Left|  Position locator to the left of the wear plate. 
         |Right|  Position locator to the right of the wear plate. 
         |Both|  Position locator on both sides of the wear plate. 
         |Neither|  No locators. 

        """
        Left: int
        Right: int
        Both: int
        Neither: int
        @staticmethod
        def ValueOf(value: int) -> WearPlateLocParentBuilder.PositionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BuildStatus(self) -> DieBuildStatusOption:
        """
        Getter for property: ( DieBuildStatusOption NXOp) BuildStatus
         Returns the build status of wear plate and locators   
            
         
        """
        pass
    @property
    def DesignStatus(self) -> bool:
        """
        Getter for property: (bool) DesignStatus
         Returns the design status of wear plate and locators   
            
         
        """
        pass
    @DesignStatus.setter
    def DesignStatus(self, design_status: bool):
        """
        Setter for property: (bool) DesignStatus
         Returns the design status of wear plate and locators   
            
         
        """
        pass
    @property
    def DisplayStatus(self) -> bool:
        """
        Getter for property: (bool) DisplayStatus
         Returns the display status of wear plate and locators   
            
         
        """
        pass
    @DisplayStatus.setter
    def DisplayStatus(self, display_status: bool):
        """
        Setter for property: (bool) DisplayStatus
         Returns the display status of wear plate and locators   
            
         
        """
        pass
    @property
    def LocatorDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LocatorDepth
         Returns the locator depth of die wear plate and locators   
            
         
        """
        pass
    @property
    def LocatorPosition(self) -> WearPlateLocParentBuilder.PositionType:
        """
        Getter for property: ( WearPlateLocParentBuilder.PositionType NXOp) LocatorPosition
         Returns the locator position of die wear plate and locators   
            
         
        """
        pass
    @LocatorPosition.setter
    def LocatorPosition(self, position: WearPlateLocParentBuilder.PositionType):
        """
        Setter for property: ( WearPlateLocParentBuilder.PositionType NXOp) LocatorPosition
         Returns the locator position of die wear plate and locators   
            
         
        """
        pass
    @property
    def LocatorWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LocatorWidth
         Returns the locator width of die wear plate and locators   
            
         
        """
        pass
    @property
    def ReverseNormal(self) -> int:
        """
        Getter for property: (int) ReverseNormal
         Returns the reverse normal setting of die wear plate and locators   
            
         
        """
        pass
    @ReverseNormal.setter
    def ReverseNormal(self, reverse_normal: int):
        """
        Setter for property: (int) ReverseNormal
         Returns the reverse normal setting of die wear plate and locators   
            
         
        """
        pass
    @property
    def RibSupportWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RibSupportWidth
         Returns the wear plate rib support width of die wear plate and locators   
            
         
        """
        pass
    @property
    def WearPlateLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) WearPlateLength
         Returns the wear plate length of die wear plate and locators   
            
         
        """
        pass
    @property
    def WearPlateWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) WearPlateWidth
         Returns the wear plate width of die wear plate and locators   
            
         
        """
        pass
    def CreateChild(self) -> WearPlateLocChildBuilder:
        """
         Creates a child wear plate and locator 
         Returns diewearplatelocchild ( WearPlateLocChildBuilder NXOp):  .
        """
        pass
    def DeleteChild(self, diewearplatelocchild: WearPlateLocChildBuilder) -> None:
        """
         Deletes a child wear plate and locator 
        """
        pass
    def GetChildren(self) -> List[WearPlateLocChildBuilder]:
        """
         Outputs the children 
         Returns children ( WearPlateLocChildBuilder List[NX):  children .
        """
        pass
    def GetPadAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the pad attributes, note existance of attributes depends on usage in
                main feature 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. title for attribute .
         - value is: str. value of attribute .
         - color is: int. color of pad faces .

        """
        pass
    def GetRecessAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the recess attributes 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. title for attribute .
         - value is: str. value of attribute .
         - color is: int. color of recess faces .

        """
        pass
    def GetReliefAttributes(self) -> Tuple[str, str, int]:
        """
         Gets the relief attributes 
         Returns A tuple consisting of (title, value, color). 
         - title is: str. title for attribute .
         - value is: str. value of attribute .
         - color is: int. color of relief faces .

        """
        pass
    def SetLocatorDepth(self, depth: str) -> None:
        """
         
        """
        pass
    def SetLocatorWidth(self, width: str) -> None:
        """
         
        """
        pass
    def SetPadAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the pad attributes, note existance of attributes depends on usage in
                main feature 
        """
        pass
    def SetRecessAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the recess attributes 
        """
        pass
    def SetReliefAttributes(self, title: str, value: str, color: int) -> None:
        """
         Sets the relief attributes 
        """
        pass
    def SetRibSupportWidth(self, rib_support_width: str) -> None:
        """
         
        """
        pass
    def SetWearPlateLength(self, length: str) -> None:
        """
         
        """
        pass
    def SetWearPlateWidth(self, width: str) -> None:
        """
         
        """
        pass
