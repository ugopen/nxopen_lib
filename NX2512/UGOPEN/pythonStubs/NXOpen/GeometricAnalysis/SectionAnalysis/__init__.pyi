from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.GeometricUtilities
class CircularGridBuilder(NXOpen.TaggedObject): 
    """ Represents the circular grid section specifications for a NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.
            Only used when type is NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.Types.Circular.
        """
    @property
    def CircularFrame(self) -> NXOpen.GeometricUtilities.CircularFrameBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.CircularFrameBuilder) CircularFrame
         Returns the circular frame   
            
         
        """
        pass
    @property
    def Spacing(self) -> GridSpacingBuilder:
        """
        Getter for property: ( GridSpacingBuilder NXOpen.GeometricAna) Spacing
         Returns the spacing specification for the circular grid   
            
         
        """
        pass
    @property
    def SpecifiedPlane(self) -> SectionPlaneBuilder:
        """
        Getter for property: ( SectionPlaneBuilder NXOpen.GeometricAna) SpecifiedPlane
         Returns the user specified section plane   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class CurveAlignedBuilder(NXOpen.TaggedObject): 
    """ Represents the Curve Aligned specification for a NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder."""
    @property
    def Curves(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Curves
         Returns the curves   
            
         
        """
        pass
    @property
    def IsSpacingEnabled(self) -> bool:
        """
        Getter for property: (bool) IsSpacingEnabled
         Returns a value indicating whether the spacing is applied   
            
         
        """
        pass
    @IsSpacingEnabled.setter
    def IsSpacingEnabled(self, isSpacingEnabled: bool):
        """
        Setter for property: (bool) IsSpacingEnabled
         Returns a value indicating whether the spacing is applied   
            
         
        """
        pass
    @property
    def Number(self) -> int:
        """
        Getter for property: (int) Number
         Returns a value indicating how many sections should be created   
            
         
        """
        pass
    @Number.setter
    def Number(self, number: int):
        """
        Setter for property: (int) Number
         Returns a value indicating how many sections should be created   
            
         
        """
        pass
    @property
    def Offset(self) -> float:
        """
        Getter for property: (float) Offset
         Returns a value indicating the distance from the start position   
            
         
        """
        pass
    @Offset.setter
    def Offset(self, offset: float):
        """
        Setter for property: (float) Offset
         Returns a value indicating the distance from the start position   
            
         
        """
        pass
    @property
    def Spacing(self) -> float:
        """
        Getter for property: (float) Spacing
         Returns a value indicating the space between sections   
            
         
        """
        pass
    @Spacing.setter
    def Spacing(self, spacing: float):
        """
        Setter for property: (float) Spacing
         Returns a value indicating the space between sections   
            
         
        """
        pass
    @property
    def SpecifiedPlane(self) -> SectionPlaneBuilder:
        """
        Getter for property: ( SectionPlaneBuilder NXOpen.GeometricAna) SpecifiedPlane
         Returns the user specified project plane   
            
         
        """
        pass
    @property
    def UseProjectedCurve(self) -> bool:
        """
        Getter for property: (bool) UseProjectedCurve
         Returns a value indicating whether to project the curve to a plane   
            
         
        """
        pass
    @UseProjectedCurve.setter
    def UseProjectedCurve(self, useProjectedCurve: bool):
        """
        Setter for property: (bool) UseProjectedCurve
         Returns a value indicating whether to project the curve to a plane   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class GridSpacingBuilder(NXOpen.TaggedObject): 
    """ Represents the grid spacing for certain types of section specifications for
            the NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.
        """
    @property
    def BoundSections1(self) -> bool:
        """
        Getter for property: (bool) BoundSections1
         Returns the flag to bound the section to grid in direction 1   
            
         
        """
        pass
    @BoundSections1.setter
    def BoundSections1(self, boundSections1: bool):
        """
        Setter for property: (bool) BoundSections1
         Returns the flag to bound the section to grid in direction 1   
            
         
        """
        pass
    @property
    def BoundSections2(self) -> bool:
        """
        Getter for property: (bool) BoundSections2
         Returns the flag to bound the section to grid in direction 2   
            
         
        """
        pass
    @BoundSections2.setter
    def BoundSections2(self, boundSections2: bool):
        """
        Setter for property: (bool) BoundSections2
         Returns the flag to bound the section to grid in direction 2   
            
         
        """
        pass
    @property
    def Interval1(self) -> float:
        """
        Getter for property: (float) Interval1
         Returns the interval of sections in direction 1   
            
         
        """
        pass
    @Interval1.setter
    def Interval1(self, interval1: float):
        """
        Setter for property: (float) Interval1
         Returns the interval of sections in direction 1   
            
         
        """
        pass
    @property
    def Interval2(self) -> float:
        """
        Getter for property: (float) Interval2
         Returns the interval of sections in direction 2   
            
         
        """
        pass
    @Interval2.setter
    def Interval2(self, interval2: float):
        """
        Setter for property: (float) Interval2
         Returns the interval of sections in direction 2   
            
         
        """
        pass
    @property
    def LockInterval1(self) -> bool:
        """
        Getter for property: (bool) LockInterval1
         Returns the flag to lock the section interval in direction 1   
            
         
        """
        pass
    @LockInterval1.setter
    def LockInterval1(self, lockInterval1: bool):
        """
        Setter for property: (bool) LockInterval1
         Returns the flag to lock the section interval in direction 1   
            
         
        """
        pass
    @property
    def LockInterval2(self) -> bool:
        """
        Getter for property: (bool) LockInterval2
         Returns the flag to lock the section interval in direction 2   
            
         
        """
        pass
    @LockInterval2.setter
    def LockInterval2(self, lockInterval2: bool):
        """
        Setter for property: (bool) LockInterval2
         Returns the flag to lock the section interval in direction 2   
            
         
        """
        pass
    @property
    def SectionNumber1(self) -> int:
        """
        Getter for property: (int) SectionNumber1
         Returns the number of sections in direction 1   
            
         
        """
        pass
    @SectionNumber1.setter
    def SectionNumber1(self, sectionNumber1: int):
        """
        Setter for property: (int) SectionNumber1
         Returns the number of sections in direction 1   
            
         
        """
        pass
    @property
    def SectionNumber2(self) -> int:
        """
        Getter for property: (int) SectionNumber2
         Returns the number of sections in direction 2   
            
         
        """
        pass
    @SectionNumber2.setter
    def SectionNumber2(self, sectionNumber2: int):
        """
        Setter for property: (int) SectionNumber2
         Returns the number of sections in direction 2   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class InteractiveBuilder(NXOpen.TaggedObject): 
    """ Represents the Interactive specification for a NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder."""
    @property
    def InteractiveSection(self) -> NXOpen.GeometricUtilities.InteractiveSectionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.InteractiveSectionBuilder) InteractiveSection
         Returns the interactive section lines   
            
         
        """
        pass
    @property
    def IsCutInfiniteEnabled(self) -> bool:
        """
        Getter for property: (bool) IsCutInfiniteEnabled
         Returns a value indicating whether extending the interactive section lines to infinite   
            
         
        """
        pass
    @IsCutInfiniteEnabled.setter
    def IsCutInfiniteEnabled(self, enabled: bool):
        """
        Setter for property: (bool) IsCutInfiniteEnabled
         Returns a value indicating whether extending the interactive section lines to infinite   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class IsoparametricBuilder(NXOpen.TaggedObject): 
    """ Represents the Isoparametric specification for a GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder."""
    @property
    def IsSpacingEnabled(self) -> bool:
        """
        Getter for property: (bool) IsSpacingEnabled
         Returns a value indicating whether the spacing is applied   
            
         
        """
        pass
    @IsSpacingEnabled.setter
    def IsSpacingEnabled(self, isSpacingEnabled: bool):
        """
        Setter for property: (bool) IsSpacingEnabled
         Returns a value indicating whether the spacing is applied   
            
         
        """
        pass
    @property
    def IsUEnabled(self) -> bool:
        """
        Getter for property: (bool) IsUEnabled
         Returns a value indicating wheter the U direction is enabled   
            
         
        """
        pass
    @IsUEnabled.setter
    def IsUEnabled(self, isUEnabled: bool):
        """
        Setter for property: (bool) IsUEnabled
         Returns a value indicating wheter the U direction is enabled   
            
         
        """
        pass
    @property
    def IsVEnabled(self) -> bool:
        """
        Getter for property: (bool) IsVEnabled
         Returns a value indicating wheter the V direction is enabled   
            
         
        """
        pass
    @IsVEnabled.setter
    def IsVEnabled(self, isVEnabled: bool):
        """
        Setter for property: (bool) IsVEnabled
         Returns a value indicating wheter the V direction is enabled   
            
         
        """
        pass
    @property
    def Number(self) -> int:
        """
        Getter for property: (int) Number
         Returns a value indicating how many sections should be created   
            
         
        """
        pass
    @Number.setter
    def Number(self, number: int):
        """
        Setter for property: (int) Number
         Returns a value indicating how many sections should be created   
            
         
        """
        pass
    @property
    def Spacing(self) -> float:
        """
        Getter for property: (float) Spacing
         Returns a value indicating the space between sections   
            
         
        """
        pass
    @Spacing.setter
    def Spacing(self, spacing: float):
        """
        Setter for property: (float) Spacing
         Returns a value indicating the space between sections   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ParallelPlanesExBuilder(NXOpen.TaggedObject): 
    """ Represents the Parallel Plane specification for a GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder."""
    @property
    def IsNumberEnabled(self) -> bool:
        """
        Getter for property: (bool) IsNumberEnabled
         Returns a value indicating whether the number is used   
            
         
        """
        pass
    @IsNumberEnabled.setter
    def IsNumberEnabled(self, isNumberEnabled: bool):
        """
        Setter for property: (bool) IsNumberEnabled
         Returns a value indicating whether the number is used   
            
         
        """
        pass
    @property
    def IsSpacingEnabled(self) -> bool:
        """
        Getter for property: (bool) IsSpacingEnabled
         Returns a value indicating whether the spacing is applied   
            
         
        """
        pass
    @IsSpacingEnabled.setter
    def IsSpacingEnabled(self, isSpacingEnabled: bool):
        """
        Setter for property: (bool) IsSpacingEnabled
         Returns a value indicating whether the spacing is applied   
            
         
        """
        pass
    @property
    def Number(self) -> int:
        """
        Getter for property: (int) Number
         Returns a value indicating how many sections should be created   
            
         
        """
        pass
    @Number.setter
    def Number(self, number: int):
        """
        Setter for property: (int) Number
         Returns a value indicating how many sections should be created   
            
         
        """
        pass
    @property
    def Offset(self) -> float:
        """
        Getter for property: (float) Offset
         Returns a value indicating the distance from the start position   
            
         
        """
        pass
    @Offset.setter
    def Offset(self, offset: float):
        """
        Setter for property: (float) Offset
         Returns a value indicating the distance from the start position   
            
         
        """
        pass
    @property
    def Spacing(self) -> float:
        """
        Getter for property: (float) Spacing
         Returns a value indicating the space between sections   
            
         
        """
        pass
    @Spacing.setter
    def Spacing(self, spacing: float):
        """
        Setter for property: (float) Spacing
         Returns a value indicating the space between sections   
            
         
        """
        pass
    @property
    def SpecifiedPlane(self) -> SectionPlaneBuilder:
        """
        Getter for property: ( SectionPlaneBuilder NXOpen.GeometricAna) SpecifiedPlane
         Returns the user specified section plane   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class QuadrilateralGridBuilder(NXOpen.TaggedObject): 
    """ Represents the quadrilateral grid section specifications for a GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.
            Only used when type is GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.Types.Quadrilateral.
        """
    @property
    def QuadrilateralFrame(self) -> NXOpen.GeometricUtilities.QuadrilateralFrameBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.QuadrilateralFrameBuilder) QuadrilateralFrame
         Returns the quadrilateral frame   
            
         
        """
        pass
    @property
    def Spacing(self) -> GridSpacingBuilder:
        """
        Getter for property: ( GridSpacingBuilder NXOpen.GeometricAna) Spacing
         Returns the spacing specification for the quadrilateral grid   
            
         
        """
        pass
    @property
    def SpecifiedPlane(self) -> SectionPlaneBuilder:
        """
        Getter for property: ( SectionPlaneBuilder NXOpen.GeometricAna) SpecifiedPlane
         Returns the user specified section plane   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class RadialBuilder(NXOpen.TaggedObject): 
    """ Represents the Radial specification for a GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder."""
    class RotationAxisType(Enum):
        """
        Members Include: 
         |Xc|  XC axis 
         |Yc|  YC axis 
         |Zc|  ZC axis 
         |View|  View direction 
         |ArbitraryVector|  A user specified vector 

        """
        Xc: int
        Yc: int
        Zc: int
        View: int
        ArbitraryVector: int
        @staticmethod
        def ValueOf(value: int) -> RadialBuilder.RotationAxisType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def IsSpacingEnabled(self) -> bool:
        """
        Getter for property: (bool) IsSpacingEnabled
         Returns a value indicating whether the spacing is applied   
            
         
        """
        pass
    @IsSpacingEnabled.setter
    def IsSpacingEnabled(self, isSpacingEnabled: bool):
        """
        Setter for property: (bool) IsSpacingEnabled
         Returns a value indicating whether the spacing is applied   
            
         
        """
        pass
    @property
    def Number(self) -> int:
        """
        Getter for property: (int) Number
         Returns a value indicating how many sections should created   
            
         
        """
        pass
    @Number.setter
    def Number(self, number: int):
        """
        Setter for property: (int) Number
         Returns a value indicating how many sections should created   
            
         
        """
        pass
    @property
    def Offset(self) -> float:
        """
        Getter for property: (float) Offset
         Returns a value indicating the distance from the start position   
            
         
        """
        pass
    @Offset.setter
    def Offset(self, offset: float):
        """
        Setter for property: (float) Offset
         Returns a value indicating the distance from the start position   
            
         
        """
        pass
    @property
    def RotationAxis(self) -> RadialBuilder.RotationAxisType:
        """
        Getter for property: ( RadialBuilder.RotationAxisType NXOpen.GeometricAna) RotationAxis
         Returns a value indicating the type of the rotation axis  
            
         
        """
        pass
    @RotationAxis.setter
    def RotationAxis(self, rotationAxis: RadialBuilder.RotationAxisType):
        """
        Setter for property: ( RadialBuilder.RotationAxisType NXOpen.GeometricAna) RotationAxis
         Returns a value indicating the type of the rotation axis  
            
         
        """
        pass
    @property
    def RotationVector(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) RotationVector
         Returns the user specified rotation vector   
            
         
        """
        pass
    @RotationVector.setter
    def RotationVector(self, rotationVector: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) RotationVector
         Returns the user specified rotation vector   
            
         
        """
        pass
    @property
    def Spacing(self) -> float:
        """
        Getter for property: (float) Spacing
         Returns a value indicating the space between sections   
            
         
        """
        pass
    @Spacing.setter
    def Spacing(self, spacing: float):
        """
        Setter for property: (float) Spacing
         Returns a value indicating the space between sections   
            
         
        """
        pass
    @property
    def SpecifiedRotationPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) SpecifiedRotationPoint
         Returns the rotation point   
            
         
        """
        pass
    @SpecifiedRotationPoint.setter
    def SpecifiedRotationPoint(self, specifiedRotationPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) SpecifiedRotationPoint
         Returns the rotation point   
            
         
        """
        pass
    @property
    def StartPosition(self) -> NXOpen.SelectPoint:
        """
        Getter for property: ( NXOpen.SelectPoint) StartPosition
         Returns the start position   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SectionAnalysisBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.GeometricAnalysis.SectionAnalysisObject builder. """
    class CalculationMethodType(Enum):
        """
        Members Include: 
         |Curvature|  Curvature 
         |RadiusofCurvature|  Radius of curvature 

        """
        Curvature: int
        RadiusofCurvature: int
        @staticmethod
        def ValueOf(value: int) -> SectionAnalysisBuilder.CalculationMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class NeedleDirectionType(Enum):
        """
        Members Include: 
         |Inside|  Inside 
         |Outside|  Outside 

        """
        Inside: int
        Outside: int
        @staticmethod
        def ValueOf(value: int) -> SectionAnalysisBuilder.NeedleDirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OutputType(Enum):
        """
        Members Include: 
         |AnalysisObject|  Analysis Object 
         |SectionCurves|  section curves 
         |Both|  Both Analysis Object and section curves 

        """
        AnalysisObject: int
        SectionCurves: int
        Both: int
        @staticmethod
        def ValueOf(value: int) -> SectionAnalysisBuilder.OutputType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ScalingMethodType(Enum):
        """
        Members Include: 
         |Linear|  Linear 
         |Logarithmic|  Logarithmic 

        """
        Linear: int
        Logarithmic: int
        @staticmethod
        def ValueOf(value: int) -> SectionAnalysisBuilder.ScalingMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |Parallel|  Parallel Planes 
         |Isoparametric|  Isoparametric 
         |AlongCurve|  Along Curve 
         |Quadrilateral|  Quadrilateral 
         |Triangular|  Triangular 
         |Circular|  Circular 

        """
        Parallel: int
        Isoparametric: int
        AlongCurve: int
        Quadrilateral: int
        Triangular: int
        Circular: int
        @staticmethod
        def ValueOf(value: int) -> SectionAnalysisBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CalculationMethod(self) -> SectionAnalysisBuilder.CalculationMethodType:
        """
        Getter for property: ( SectionAnalysisBuilder.CalculationMethodType NXOpen.GeometricAna) CalculationMethod
         Returns the calculation method   
            
         
        """
        pass
    @CalculationMethod.setter
    def CalculationMethod(self, calculationMethod: SectionAnalysisBuilder.CalculationMethodType):
        """
        Setter for property: ( SectionAnalysisBuilder.CalculationMethodType NXOpen.GeometricAna) CalculationMethod
         Returns the calculation method   
            
         
        """
        pass
    @property
    def CircularGrid(self) -> CircularGridBuilder:
        """
        Getter for property: ( CircularGridBuilder NXOpen.GeometricAna) CircularGrid
         Returns the circular grid.  
          
                        Only used when type is  NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder::TypesCircular    
         
        """
        pass
    @property
    def CombOptions(self) -> NXOpen.GeometricUtilities.CombOptionsBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.CombOptionsBuilder) CombOptions
         Returns the comb options   
            
         
        """
        pass
    @property
    def NeedleDirection(self) -> SectionAnalysisBuilder.NeedleDirectionType:
        """
        Getter for property: ( SectionAnalysisBuilder.NeedleDirectionType NXOpen.GeometricAna) NeedleDirection
         Returns the needle direction   
            
         
        """
        pass
    @NeedleDirection.setter
    def NeedleDirection(self, needleDirection: SectionAnalysisBuilder.NeedleDirectionType):
        """
        Setter for property: ( SectionAnalysisBuilder.NeedleDirectionType NXOpen.GeometricAna) NeedleDirection
         Returns the needle direction   
            
         
        """
        pass
    @property
    def Output(self) -> SectionAnalysisBuilder.OutputType:
        """
        Getter for property: ( SectionAnalysisBuilder.OutputType NXOpen.GeometricAna) Output
         Returns the output   
            
         
        """
        pass
    @Output.setter
    def Output(self, output: SectionAnalysisBuilder.OutputType):
        """
        Setter for property: ( SectionAnalysisBuilder.OutputType NXOpen.GeometricAna) Output
         Returns the output   
            
         
        """
        pass
    @property
    def QuadrilateralGrid(self) -> QuadrilateralGridBuilder:
        """
        Getter for property: ( QuadrilateralGridBuilder NXOpen.GeometricAna) QuadrilateralGrid
         Returns the quadrilateral grid.  
          
                        Only used when type is  NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder::TypesQuadrilateral    
         
        """
        pass
    @property
    def References(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) References
         Returns the references (faces or faceted bodies)   
            
         
        """
        pass
    @property
    def ScalingMethod(self) -> SectionAnalysisBuilder.ScalingMethodType:
        """
        Getter for property: ( SectionAnalysisBuilder.ScalingMethodType NXOpen.GeometricAna) ScalingMethod
         Returns the scaling method   
            
         
        """
        pass
    @ScalingMethod.setter
    def ScalingMethod(self, scalingMethod: SectionAnalysisBuilder.ScalingMethodType):
        """
        Setter for property: ( SectionAnalysisBuilder.ScalingMethodType NXOpen.GeometricAna) ScalingMethod
         Returns the scaling method   
            
         
        """
        pass
    @property
    def ShowInflectionPoints(self) -> bool:
        """
        Getter for property: (bool) ShowInflectionPoints
         Returns the flag to show the inflection points of planar sections   
            
         
        """
        pass
    @ShowInflectionPoints.setter
    def ShowInflectionPoints(self, showInflectionPoints: bool):
        """
        Setter for property: (bool) ShowInflectionPoints
         Returns the flag to show the inflection points of planar sections   
            
         
        """
        pass
    @property
    def ShowPeakPoints(self) -> bool:
        """
        Getter for property: (bool) ShowPeakPoints
         Returns the flag to show the peak points of the sections   
            
         
        """
        pass
    @ShowPeakPoints.setter
    def ShowPeakPoints(self, showPeakPoints: bool):
        """
        Setter for property: (bool) ShowPeakPoints
         Returns the flag to show the peak points of the sections   
            
         
        """
        pass
    @property
    def ShowSectionLength(self) -> bool:
        """
        Getter for property: (bool) ShowSectionLength
         Returns the flag to show the section length labels   
            
         
        """
        pass
    @ShowSectionLength.setter
    def ShowSectionLength(self, showSectionLength: bool):
        """
        Setter for property: (bool) ShowSectionLength
         Returns the flag to show the section length labels   
            
         
        """
        pass
    @property
    def TriangularGrid(self) -> TriangularGridBuilder:
        """
        Getter for property: ( TriangularGridBuilder NXOpen.GeometricAna) TriangularGrid
         Returns the triangular grid.  
          
                        Only used when type is  NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder::TypesTriangular    
         
        """
        pass
    @property
    def Type(self) -> SectionAnalysisBuilder.Types:
        """
        Getter for property: ( SectionAnalysisBuilder.Types NXOpen.GeometricAna) Type
         Returns the sectioning type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: SectionAnalysisBuilder.Types):
        """
        Setter for property: ( SectionAnalysisBuilder.Types NXOpen.GeometricAna) Type
         Returns the sectioning type   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SectionAnalysisExBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExObject builder """
    class AlignmentType(Enum):
        """
        Members Include: 
         |XYZPlane|  The cutting planes are perpendicular to X, Y or Z plane 
         |ParallelPlanes|  The cutting planes are parallel to a specified plane 
         |CurveAligned|  The cutting planes are perpendicular to specified curves 
         |Isoparametric|  The sections are along isoparametric lines 
         |Radial|  The cutting planes are distributed along a circle 

        """
        XYZPlane: int
        ParallelPlanes: int
        CurveAligned: int
        Isoparametric: int
        Radial: int
        @staticmethod
        def ValueOf(value: int) -> SectionAnalysisExBuilder.AlignmentType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CalculationMethodType(Enum):
        """
        Members Include: 
         |Curvature|  Curvature 
         |RadiusofCurvature|  Radius of curvature 

        """
        Curvature: int
        RadiusofCurvature: int
        @staticmethod
        def ValueOf(value: int) -> SectionAnalysisExBuilder.CalculationMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class NeedleDirectionType(Enum):
        """
        Members Include: 
         |Inside|  Inside 
         |Outside|  Outside 

        """
        Inside: int
        Outside: int
        @staticmethod
        def ValueOf(value: int) -> SectionAnalysisExBuilder.NeedleDirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OutputType(Enum):
        """
        Members Include: 
         |AnalysisObject|  Analysis Object 
         |SectionCurves|  section curves 
         |Both|  Both Analysis Object and section curves 

        """
        AnalysisObject: int
        SectionCurves: int
        Both: int
        @staticmethod
        def ValueOf(value: int) -> SectionAnalysisExBuilder.OutputType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PlacementType(Enum):
        """
        Members Include: 
         |Uniform|  Uniformly distributed 
         |ThroughPoints|  Through the specified points 
         |BetweenPoints|  Distributed between two specified points
         |Interactive|  Interactively specified 

        """
        Uniform: int
        ThroughPoints: int
        BetweenPoints: int
        Interactive: int
        @staticmethod
        def ValueOf(value: int) -> SectionAnalysisExBuilder.PlacementType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ScalingMethodType(Enum):
        """
        Members Include: 
         |Linear|  Linear 
         |Logarithmic|  Logarithmic 

        """
        Linear: int
        Logarithmic: int
        @staticmethod
        def ValueOf(value: int) -> SectionAnalysisExBuilder.ScalingMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Alignment(self) -> SectionAnalysisExBuilder.AlignmentType:
        """
        Getter for property: ( SectionAnalysisExBuilder.AlignmentType NXOpen.GeometricAna) Alignment
         Returns the alignment type   
            
         
        """
        pass
    @Alignment.setter
    def Alignment(self, alignment: SectionAnalysisExBuilder.AlignmentType):
        """
        Setter for property: ( SectionAnalysisExBuilder.AlignmentType NXOpen.GeometricAna) Alignment
         Returns the alignment type   
            
         
        """
        pass
    @property
    def CalculationMethod(self) -> SectionAnalysisExBuilder.CalculationMethodType:
        """
        Getter for property: ( SectionAnalysisExBuilder.CalculationMethodType NXOpen.GeometricAna) CalculationMethod
         Returns the calculation method   
            
         
        """
        pass
    @CalculationMethod.setter
    def CalculationMethod(self, calculationMethod: SectionAnalysisExBuilder.CalculationMethodType):
        """
        Setter for property: ( SectionAnalysisExBuilder.CalculationMethodType NXOpen.GeometricAna) CalculationMethod
         Returns the calculation method   
            
         
        """
        pass
    @property
    def CombOptions(self) -> NXOpen.GeometricUtilities.CombOptionsBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.CombOptionsBuilder) CombOptions
         Returns the comb options specification  
            
         
        """
        pass
    @property
    def CurveAligned(self) -> CurveAlignedBuilder:
        """
        Getter for property: ( CurveAlignedBuilder NXOpen.GeometricAna) CurveAligned
         Returns the Curve Aligned section specification.  
          
                        Only used when type is  NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder::AlignmentTypeCurveAligned    
         
        """
        pass
    @property
    def Interactive(self) -> InteractiveBuilder:
        """
        Getter for property: ( InteractiveBuilder NXOpen.GeometricAna) Interactive
         Returns the Interactive placement specification.  
          
                        Only used when type is  NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder::PlacementTypeInteractive    
         
        """
        pass
    @property
    def IsShowInflectionPointsEnabled(self) -> bool:
        """
        Getter for property: (bool) IsShowInflectionPointsEnabled
         Returns a value indicating whether to show the inflection points   
            
         
        """
        pass
    @IsShowInflectionPointsEnabled.setter
    def IsShowInflectionPointsEnabled(self, inflection: bool):
        """
        Setter for property: (bool) IsShowInflectionPointsEnabled
         Returns a value indicating whether to show the inflection points   
            
         
        """
        pass
    @property
    def IsShowLengthEnabled(self) -> bool:
        """
        Getter for property: (bool) IsShowLengthEnabled
         Returns a value indicating whether to show the length of each section curve   
            
         
        """
        pass
    @IsShowLengthEnabled.setter
    def IsShowLengthEnabled(self, length: bool):
        """
        Setter for property: (bool) IsShowLengthEnabled
         Returns a value indicating whether to show the length of each section curve   
            
         
        """
        pass
    @property
    def IsShowPeakPointsEnabled(self) -> bool:
        """
        Getter for property: (bool) IsShowPeakPointsEnabled
         Returns a value indicating whether to show the peak points   
            
         
        """
        pass
    @IsShowPeakPointsEnabled.setter
    def IsShowPeakPointsEnabled(self, peak: bool):
        """
        Setter for property: (bool) IsShowPeakPointsEnabled
         Returns a value indicating whether to show the peak points   
            
         
        """
        pass
    @property
    def Isoparametric(self) -> IsoparametricBuilder:
        """
        Getter for property: ( IsoparametricBuilder NXOpen.GeometricAna) Isoparametric
         Returns the Isoparametric section specification.  
          
                        Only used when type is  NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder::AlignmentTypeIsoparametric    
         
        """
        pass
    @property
    def NeedleDirection(self) -> SectionAnalysisExBuilder.NeedleDirectionType:
        """
        Getter for property: ( SectionAnalysisExBuilder.NeedleDirectionType NXOpen.GeometricAna) NeedleDirection
         Returns the needle direction   
            
         
        """
        pass
    @NeedleDirection.setter
    def NeedleDirection(self, needleDirection: SectionAnalysisExBuilder.NeedleDirectionType):
        """
        Setter for property: ( SectionAnalysisExBuilder.NeedleDirectionType NXOpen.GeometricAna) NeedleDirection
         Returns the needle direction   
            
         
        """
        pass
    @property
    def Output(self) -> SectionAnalysisExBuilder.OutputType:
        """
        Getter for property: ( SectionAnalysisExBuilder.OutputType NXOpen.GeometricAna) Output
         Returns the output   
            
         
        """
        pass
    @Output.setter
    def Output(self, output: SectionAnalysisExBuilder.OutputType):
        """
        Setter for property: ( SectionAnalysisExBuilder.OutputType NXOpen.GeometricAna) Output
         Returns the output   
            
         
        """
        pass
    @property
    def ParallelPlanes(self) -> ParallelPlanesExBuilder:
        """
        Getter for property: ( ParallelPlanesExBuilder NXOpen.GeometricAna) ParallelPlanes
         Returns the Parallel Planes section specification.  
          
                        Only used when type is  NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder::AlignmentTypeParallelPlanes    
         
        """
        pass
    @property
    def Placement(self) -> SectionAnalysisExBuilder.PlacementType:
        """
        Getter for property: ( SectionAnalysisExBuilder.PlacementType NXOpen.GeometricAna) Placement
         Returns the placement   
            
         
        """
        pass
    @Placement.setter
    def Placement(self, placement: SectionAnalysisExBuilder.PlacementType):
        """
        Setter for property: ( SectionAnalysisExBuilder.PlacementType NXOpen.GeometricAna) Placement
         Returns the placement   
            
         
        """
        pass
    @property
    def Radial(self) -> RadialBuilder:
        """
        Getter for property: ( RadialBuilder NXOpen.GeometricAna) Radial
         Returns the Radial section specification.  
          
                        Only used when type is  NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder::AlignmentTypeCurveAligned    
         
        """
        pass
    @property
    def ScalingMethod(self) -> SectionAnalysisExBuilder.ScalingMethodType:
        """
        Getter for property: ( SectionAnalysisExBuilder.ScalingMethodType NXOpen.GeometricAna) ScalingMethod
         Returns the scaling method   
            
         
        """
        pass
    @ScalingMethod.setter
    def ScalingMethod(self, scalingMethod: SectionAnalysisExBuilder.ScalingMethodType):
        """
        Setter for property: ( SectionAnalysisExBuilder.ScalingMethodType NXOpen.GeometricAna) ScalingMethod
         Returns the scaling method   
            
         
        """
        pass
    @property
    def SelectObject(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) SelectObject
         Returns the selected objects   
            
         
        """
        pass
    @property
    def SpecifyPoint(self) -> NXOpen.SelectPointList:
        """
        Getter for property: ( NXOpen.SelectPointList) SpecifyPoint
         Returns the specified points   
            
         
        """
        pass
    @property
    def XYZPlane(self) -> XYZPlaneBuilder:
        """
        Getter for property: ( XYZPlaneBuilder NXOpen.GeometricAna) XYZPlane
         Returns the XYZ Planes section specification.  
          
                        Only used when type is  NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder::AlignmentTypeXYZPlane    
         
        """
        pass
import NXOpen.GeometricAnalysis
class SectionAnalysisExObject(NXOpen.GeometricAnalysis.AnalysisObject): 
    """ Represents a Section Analysis Object of the new version.  Section Analysis
            generates planar or isoparametric sections across faces and faceted bodies 
            to help evaluating sectional curvature flow of faces and surface quality and 
            characteristics in general. Section Analysis object update dynamically on geometry 
            changes of the sectioned faces and faceted bodies. """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class SectionPlaneBuilder(NXOpen.TaggedObject): 
    """ Represents a plane which is used to cut sections on faces or facet bodies """
    class PlaneType(Enum):
        """
        Members Include: 
         |Xc|  XC plane 
         |Yc|  YC plane 
         |Zc|  ZC plane 
         |View|  View plane 
         |Plane|  A user specifed plane 

        """
        Xc: int
        Yc: int
        Zc: int
        View: int
        Plane: int
        @staticmethod
        def ValueOf(value: int) -> SectionPlaneBuilder.PlaneType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Origin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) Origin
         Returns the plane origin   
            
         
        """
        pass
    @Origin.setter
    def Origin(self, origin: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) Origin
         Returns the plane origin   
            
         
        """
        pass
    @property
    def Plane(self) -> SectionPlaneBuilder.PlaneType:
        """
        Getter for property: ( SectionPlaneBuilder.PlaneType NXOpen.GeometricAna) Plane
         Returns the plane type   
            
         
        """
        pass
    @Plane.setter
    def Plane(self, plane: SectionPlaneBuilder.PlaneType):
        """
        Setter for property: ( SectionPlaneBuilder.PlaneType NXOpen.GeometricAna) Plane
         Returns the plane type   
            
         
        """
        pass
    @property
    def XAxis(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) XAxis
         Returns the plane X axis   
            
         
        """
        pass
    @XAxis.setter
    def XAxis(self, xAxis: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) XAxis
         Returns the plane X axis   
            
         
        """
        pass
    @property
    def YAxis(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) YAxis
         Returns the plane Y axis   
            
         
        """
        pass
    @YAxis.setter
    def YAxis(self, yAxis: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) YAxis
         Returns the plane Y axis   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class TriangularGridBuilder(NXOpen.TaggedObject): 
    """ Represents the triangular grid section specifications for a SectionAnalysisBuilder.
            Only used when type is GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.Types.Triangular.
        """
    @property
    def Spacing(self) -> GridSpacingBuilder:
        """
        Getter for property: ( GridSpacingBuilder NXOpen.GeometricAna) Spacing
         Returns the spacing specification for the triangular grid   
            
         
        """
        pass
    @property
    def SpecifiedPlane(self) -> SectionPlaneBuilder:
        """
        Getter for property: ( SectionPlaneBuilder NXOpen.GeometricAna) SpecifiedPlane
         Returns the user specified section plane   
            
         
        """
        pass
    @property
    def TriangularFrame(self) -> NXOpen.GeometricUtilities.TriangularFrameBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.TriangularFrameBuilder) TriangularFrame
         Returns the triangular frame   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class XYZPlaneBuilder(NXOpen.TaggedObject): 
    """ Represents the XYZ Plane specification for a GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder."""
    @property
    def AnchorOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) AnchorOrigin
         Returns the anchor position   
            
         
        """
        pass
    @AnchorOrigin.setter
    def AnchorOrigin(self, anchorOrigin: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) AnchorOrigin
         Returns the anchor position   
            
         
        """
        pass
    @property
    def AnchorXAxis(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) AnchorXAxis
         Returns the anchor X axis   
            
         
        """
        pass
    @AnchorXAxis.setter
    def AnchorXAxis(self, anchorXAxis: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) AnchorXAxis
         Returns the anchor X axis   
            
         
        """
        pass
    @property
    def AnchorYAxis(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) AnchorYAxis
         Returns the anchor Y axis   
            
         
        """
        pass
    @AnchorYAxis.setter
    def AnchorYAxis(self, anchorYAxis: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) AnchorYAxis
         Returns the anchor Y axis   
            
         
        """
        pass
    @property
    def IsNumberEnabled(self) -> bool:
        """
        Getter for property: (bool) IsNumberEnabled
         Returns a value indicating whether the number is used   
            
         
        """
        pass
    @IsNumberEnabled.setter
    def IsNumberEnabled(self, isNumberEnabled: bool):
        """
        Setter for property: (bool) IsNumberEnabled
         Returns a value indicating whether the number is used   
            
         
        """
        pass
    @property
    def IsSpacingEnabled(self) -> bool:
        """
        Getter for property: (bool) IsSpacingEnabled
         Returns a value indicating whether the spacing is applied   
            
         
        """
        pass
    @IsSpacingEnabled.setter
    def IsSpacingEnabled(self, isSpacingEnabled: bool):
        """
        Setter for property: (bool) IsSpacingEnabled
         Returns a value indicating whether the spacing is applied   
            
         
        """
        pass
    @property
    def IsXEnabled(self) -> bool:
        """
        Getter for property: (bool) IsXEnabled
         Returns a value indicating whether X is enabled   
            
         
        """
        pass
    @IsXEnabled.setter
    def IsXEnabled(self, isXEnabled: bool):
        """
        Setter for property: (bool) IsXEnabled
         Returns a value indicating whether X is enabled   
            
         
        """
        pass
    @property
    def IsYEnabled(self) -> bool:
        """
        Getter for property: (bool) IsYEnabled
         Returns a value indicating whether Y is enabled   
            
         
        """
        pass
    @IsYEnabled.setter
    def IsYEnabled(self, isYEnabled: bool):
        """
        Setter for property: (bool) IsYEnabled
         Returns a value indicating whether Y is enabled   
            
         
        """
        pass
    @property
    def IsZEnabled(self) -> bool:
        """
        Getter for property: (bool) IsZEnabled
         Returns a value indicating whether Z is enabled   
            
         
        """
        pass
    @IsZEnabled.setter
    def IsZEnabled(self, isZEnabled: bool):
        """
        Setter for property: (bool) IsZEnabled
         Returns a value indicating whether Z is enabled   
            
         
        """
        pass
    @property
    def Number(self) -> int:
        """
        Getter for property: (int) Number
         Returns a value indicating how many sections should be created   
            
         
        """
        pass
    @Number.setter
    def Number(self, number: int):
        """
        Setter for property: (int) Number
         Returns a value indicating how many sections should be created   
            
         
        """
        pass
    @property
    def Spacing(self) -> float:
        """
        Getter for property: (float) Spacing
         Returns a value indicating the space between sections   
            
         
        """
        pass
    @Spacing.setter
    def Spacing(self, spacing: float):
        """
        Setter for property: (float) Spacing
         Returns a value indicating the space between sections   
            
         
        """
        pass
