from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.GeometricUtilities
##  Represents the circular grid section specifications for a @link NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder@endlink .
##             Only used when type is @link NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder::TypesCircular NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder::TypesCircular@endlink .
##         
## 
##   <br>  Created in NX6.0.0  <br> 

class CircularGridBuilder(NXOpen.TaggedObject): 
    """ Represents the circular grid section specifications for a <ja_class>NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder</ja_class>.
            Only used when type is <ja_enum_member>NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.Types.Circular</ja_enum_member>.
        """


    ## Getter for property: (@link NXOpen.GeometricUtilities.CircularFrameBuilder NXOpen.GeometricUtilities.CircularFrameBuilder@endlink) CircularFrame
    ##   the circular frame   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.CircularFrameBuilder
    @property
    def CircularFrame(self) -> NXOpen.GeometricUtilities.CircularFrameBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.CircularFrameBuilder NXOpen.GeometricUtilities.CircularFrameBuilder@endlink) CircularFrame
          the circular frame   
            
         
        """
        pass
    
    ## Getter for property: (@link GridSpacingBuilder NXOpen.GeometricAnalysis.SectionAnalysis.GridSpacingBuilder@endlink) Spacing
    ##   the spacing specification for the circular grid   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return GridSpacingBuilder
    @property
    def Spacing(self) -> GridSpacingBuilder:
        """
        Getter for property: (@link GridSpacingBuilder NXOpen.GeometricAnalysis.SectionAnalysis.GridSpacingBuilder@endlink) Spacing
          the spacing specification for the circular grid   
            
         
        """
        pass
    
    ## Getter for property: (@link SectionPlaneBuilder NXOpen.GeometricAnalysis.SectionAnalysis.SectionPlaneBuilder@endlink) SpecifiedPlane
    ##   the user specified section plane   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return SectionPlaneBuilder
    @property
    def SpecifiedPlane(self) -> SectionPlaneBuilder:
        """
        Getter for property: (@link SectionPlaneBuilder NXOpen.GeometricAnalysis.SectionAnalysis.SectionPlaneBuilder@endlink) SpecifiedPlane
          the user specified section plane   
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents the Curve Aligned specification for a @link NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder@endlink .
## 
##   <br>  Created in NX7.0.0  <br> 

class CurveAlignedBuilder(NXOpen.TaggedObject): 
    """ Represents the Curve Aligned specification for a <ja_class>NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder</ja_class>."""


    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) Curves
    ##   the curves   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def Curves(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) Curves
          the curves   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsSpacingEnabled
    ##   a value indicating whether the spacing is applied   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return bool
    @property
    def IsSpacingEnabled(self) -> bool:
        """
        Getter for property: (bool) IsSpacingEnabled
          a value indicating whether the spacing is applied   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsSpacingEnabled

    ##   a value indicating whether the spacing is applied   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @IsSpacingEnabled.setter
    def IsSpacingEnabled(self, isSpacingEnabled: bool):
        """
        Setter for property: (bool) IsSpacingEnabled
          a value indicating whether the spacing is applied   
            
         
        """
        pass
    
    ## Getter for property: (int) Number
    ##   a value indicating how many sections should be created   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return int
    @property
    def Number(self) -> int:
        """
        Getter for property: (int) Number
          a value indicating how many sections should be created   
            
         
        """
        pass
    
    ## Setter for property: (int) Number

    ##   a value indicating how many sections should be created   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @Number.setter
    def Number(self, number: int):
        """
        Setter for property: (int) Number
          a value indicating how many sections should be created   
            
         
        """
        pass
    
    ## Getter for property: (float) Offset
    ##   a value indicating the distance from the start position   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return float
    @property
    def Offset(self) -> float:
        """
        Getter for property: (float) Offset
          a value indicating the distance from the start position   
            
         
        """
        pass
    
    ## Setter for property: (float) Offset

    ##   a value indicating the distance from the start position   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @Offset.setter
    def Offset(self, offset: float):
        """
        Setter for property: (float) Offset
          a value indicating the distance from the start position   
            
         
        """
        pass
    
    ## Getter for property: (float) Spacing
    ##   a value indicating the space between sections   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return float
    @property
    def Spacing(self) -> float:
        """
        Getter for property: (float) Spacing
          a value indicating the space between sections   
            
         
        """
        pass
    
    ## Setter for property: (float) Spacing

    ##   a value indicating the space between sections   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @Spacing.setter
    def Spacing(self, spacing: float):
        """
        Setter for property: (float) Spacing
          a value indicating the space between sections   
            
         
        """
        pass
    
    ## Getter for property: (@link SectionPlaneBuilder NXOpen.GeometricAnalysis.SectionAnalysis.SectionPlaneBuilder@endlink) SpecifiedPlane
    ##   the user specified project plane   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return SectionPlaneBuilder
    @property
    def SpecifiedPlane(self) -> SectionPlaneBuilder:
        """
        Getter for property: (@link SectionPlaneBuilder NXOpen.GeometricAnalysis.SectionAnalysis.SectionPlaneBuilder@endlink) SpecifiedPlane
          the user specified project plane   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseProjectedCurve
    ##   a value indicating whether to project the curve to a plane   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return bool
    @property
    def UseProjectedCurve(self) -> bool:
        """
        Getter for property: (bool) UseProjectedCurve
          a value indicating whether to project the curve to a plane   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseProjectedCurve

    ##   a value indicating whether to project the curve to a plane   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @UseProjectedCurve.setter
    def UseProjectedCurve(self, useProjectedCurve: bool):
        """
        Setter for property: (bool) UseProjectedCurve
          a value indicating whether to project the curve to a plane   
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents the grid spacing for certain types of section specifications for
##             the @link NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder@endlink .
##         
## 
##   <br>  Created in NX6.0.0  <br> 

class GridSpacingBuilder(NXOpen.TaggedObject): 
    """ Represents the grid spacing for certain types of section specifications for
            the <ja_class>NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder</ja_class>.
        """


    ## Getter for property: (bool) BoundSections1
    ##   the flag to bound the section to grid in direction 1   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def BoundSections1(self) -> bool:
        """
        Getter for property: (bool) BoundSections1
          the flag to bound the section to grid in direction 1   
            
         
        """
        pass
    
    ## Setter for property: (bool) BoundSections1

    ##   the flag to bound the section to grid in direction 1   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @BoundSections1.setter
    def BoundSections1(self, boundSections1: bool):
        """
        Setter for property: (bool) BoundSections1
          the flag to bound the section to grid in direction 1   
            
         
        """
        pass
    
    ## Getter for property: (bool) BoundSections2
    ##   the flag to bound the section to grid in direction 2   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def BoundSections2(self) -> bool:
        """
        Getter for property: (bool) BoundSections2
          the flag to bound the section to grid in direction 2   
            
         
        """
        pass
    
    ## Setter for property: (bool) BoundSections2

    ##   the flag to bound the section to grid in direction 2   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @BoundSections2.setter
    def BoundSections2(self, boundSections2: bool):
        """
        Setter for property: (bool) BoundSections2
          the flag to bound the section to grid in direction 2   
            
         
        """
        pass
    
    ## Getter for property: (float) Interval1
    ##   the interval of sections in direction 1   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return float
    @property
    def Interval1(self) -> float:
        """
        Getter for property: (float) Interval1
          the interval of sections in direction 1   
            
         
        """
        pass
    
    ## Setter for property: (float) Interval1

    ##   the interval of sections in direction 1   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @Interval1.setter
    def Interval1(self, interval1: float):
        """
        Setter for property: (float) Interval1
          the interval of sections in direction 1   
            
         
        """
        pass
    
    ## Getter for property: (float) Interval2
    ##   the interval of sections in direction 2   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return float
    @property
    def Interval2(self) -> float:
        """
        Getter for property: (float) Interval2
          the interval of sections in direction 2   
            
         
        """
        pass
    
    ## Setter for property: (float) Interval2

    ##   the interval of sections in direction 2   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @Interval2.setter
    def Interval2(self, interval2: float):
        """
        Setter for property: (float) Interval2
          the interval of sections in direction 2   
            
         
        """
        pass
    
    ## Getter for property: (bool) LockInterval1
    ##   the flag to lock the section interval in direction 1   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def LockInterval1(self) -> bool:
        """
        Getter for property: (bool) LockInterval1
          the flag to lock the section interval in direction 1   
            
         
        """
        pass
    
    ## Setter for property: (bool) LockInterval1

    ##   the flag to lock the section interval in direction 1   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @LockInterval1.setter
    def LockInterval1(self, lockInterval1: bool):
        """
        Setter for property: (bool) LockInterval1
          the flag to lock the section interval in direction 1   
            
         
        """
        pass
    
    ## Getter for property: (bool) LockInterval2
    ##   the flag to lock the section interval in direction 2   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def LockInterval2(self) -> bool:
        """
        Getter for property: (bool) LockInterval2
          the flag to lock the section interval in direction 2   
            
         
        """
        pass
    
    ## Setter for property: (bool) LockInterval2

    ##   the flag to lock the section interval in direction 2   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @LockInterval2.setter
    def LockInterval2(self, lockInterval2: bool):
        """
        Setter for property: (bool) LockInterval2
          the flag to lock the section interval in direction 2   
            
         
        """
        pass
    
    ## Getter for property: (int) SectionNumber1
    ##   the number of sections in direction 1   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return int
    @property
    def SectionNumber1(self) -> int:
        """
        Getter for property: (int) SectionNumber1
          the number of sections in direction 1   
            
         
        """
        pass
    
    ## Setter for property: (int) SectionNumber1

    ##   the number of sections in direction 1   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @SectionNumber1.setter
    def SectionNumber1(self, sectionNumber1: int):
        """
        Setter for property: (int) SectionNumber1
          the number of sections in direction 1   
            
         
        """
        pass
    
    ## Getter for property: (int) SectionNumber2
    ##   the number of sections in direction 2   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return int
    @property
    def SectionNumber2(self) -> int:
        """
        Getter for property: (int) SectionNumber2
          the number of sections in direction 2   
            
         
        """
        pass
    
    ## Setter for property: (int) SectionNumber2

    ##   the number of sections in direction 2   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @SectionNumber2.setter
    def SectionNumber2(self, sectionNumber2: int):
        """
        Setter for property: (int) SectionNumber2
          the number of sections in direction 2   
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents the Interactive specification for a @link NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder@endlink .
## 
##   <br>  Created in NX7.0.0  <br> 

class InteractiveBuilder(NXOpen.TaggedObject): 
    """ Represents the Interactive specification for a <ja_class>NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder</ja_class>."""


    ## Getter for property: (@link NXOpen.GeometricUtilities.InteractiveSectionBuilder NXOpen.GeometricUtilities.InteractiveSectionBuilder@endlink) InteractiveSection
    ##   the interactive section lines   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.InteractiveSectionBuilder
    @property
    def InteractiveSection(self) -> NXOpen.GeometricUtilities.InteractiveSectionBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.InteractiveSectionBuilder NXOpen.GeometricUtilities.InteractiveSectionBuilder@endlink) InteractiveSection
          the interactive section lines   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsCutInfiniteEnabled
    ##   a value indicating whether extending the interactive section lines to infinite   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return bool
    @property
    def IsCutInfiniteEnabled(self) -> bool:
        """
        Getter for property: (bool) IsCutInfiniteEnabled
          a value indicating whether extending the interactive section lines to infinite   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsCutInfiniteEnabled

    ##   a value indicating whether extending the interactive section lines to infinite   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @IsCutInfiniteEnabled.setter
    def IsCutInfiniteEnabled(self, enabled: bool):
        """
        Setter for property: (bool) IsCutInfiniteEnabled
          a value indicating whether extending the interactive section lines to infinite   
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents the Isoparametric specification for a @link GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder@endlink .
## 
##   <br>  Created in NX7.0.0  <br> 

class IsoparametricBuilder(NXOpen.TaggedObject): 
    """ Represents the Isoparametric specification for a <ja_class>GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder</ja_class>."""


    ## Getter for property: (bool) IsSpacingEnabled
    ##   a value indicating whether the spacing is applied   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return bool
    @property
    def IsSpacingEnabled(self) -> bool:
        """
        Getter for property: (bool) IsSpacingEnabled
          a value indicating whether the spacing is applied   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsSpacingEnabled

    ##   a value indicating whether the spacing is applied   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @IsSpacingEnabled.setter
    def IsSpacingEnabled(self, isSpacingEnabled: bool):
        """
        Setter for property: (bool) IsSpacingEnabled
          a value indicating whether the spacing is applied   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsUEnabled
    ##   a value indicating wheter the U direction is enabled   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return bool
    @property
    def IsUEnabled(self) -> bool:
        """
        Getter for property: (bool) IsUEnabled
          a value indicating wheter the U direction is enabled   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsUEnabled

    ##   a value indicating wheter the U direction is enabled   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @IsUEnabled.setter
    def IsUEnabled(self, isUEnabled: bool):
        """
        Setter for property: (bool) IsUEnabled
          a value indicating wheter the U direction is enabled   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsVEnabled
    ##   a value indicating wheter the V direction is enabled   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return bool
    @property
    def IsVEnabled(self) -> bool:
        """
        Getter for property: (bool) IsVEnabled
          a value indicating wheter the V direction is enabled   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsVEnabled

    ##   a value indicating wheter the V direction is enabled   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @IsVEnabled.setter
    def IsVEnabled(self, isVEnabled: bool):
        """
        Setter for property: (bool) IsVEnabled
          a value indicating wheter the V direction is enabled   
            
         
        """
        pass
    
    ## Getter for property: (int) Number
    ##   a value indicating how many sections should be created   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return int
    @property
    def Number(self) -> int:
        """
        Getter for property: (int) Number
          a value indicating how many sections should be created   
            
         
        """
        pass
    
    ## Setter for property: (int) Number

    ##   a value indicating how many sections should be created   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @Number.setter
    def Number(self, number: int):
        """
        Setter for property: (int) Number
          a value indicating how many sections should be created   
            
         
        """
        pass
    
    ## Getter for property: (float) Spacing
    ##   a value indicating the space between sections   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return float
    @property
    def Spacing(self) -> float:
        """
        Getter for property: (float) Spacing
          a value indicating the space between sections   
            
         
        """
        pass
    
    ## Setter for property: (float) Spacing

    ##   a value indicating the space between sections   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @Spacing.setter
    def Spacing(self, spacing: float):
        """
        Setter for property: (float) Spacing
          a value indicating the space between sections   
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents the Parallel Plane specification for a @link GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder@endlink .
## 
##   <br>  Created in NX7.0.0  <br> 

class ParallelPlanesExBuilder(NXOpen.TaggedObject): 
    """ Represents the Parallel Plane specification for a <ja_class>GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder</ja_class>."""


    ## Getter for property: (bool) IsNumberEnabled
    ##   a value indicating whether the number is used   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return bool
    @property
    def IsNumberEnabled(self) -> bool:
        """
        Getter for property: (bool) IsNumberEnabled
          a value indicating whether the number is used   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsNumberEnabled

    ##   a value indicating whether the number is used   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @IsNumberEnabled.setter
    def IsNumberEnabled(self, isNumberEnabled: bool):
        """
        Setter for property: (bool) IsNumberEnabled
          a value indicating whether the number is used   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsSpacingEnabled
    ##   a value indicating whether the spacing is applied   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return bool
    @property
    def IsSpacingEnabled(self) -> bool:
        """
        Getter for property: (bool) IsSpacingEnabled
          a value indicating whether the spacing is applied   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsSpacingEnabled

    ##   a value indicating whether the spacing is applied   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @IsSpacingEnabled.setter
    def IsSpacingEnabled(self, isSpacingEnabled: bool):
        """
        Setter for property: (bool) IsSpacingEnabled
          a value indicating whether the spacing is applied   
            
         
        """
        pass
    
    ## Getter for property: (int) Number
    ##   a value indicating how many sections should be created   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return int
    @property
    def Number(self) -> int:
        """
        Getter for property: (int) Number
          a value indicating how many sections should be created   
            
         
        """
        pass
    
    ## Setter for property: (int) Number

    ##   a value indicating how many sections should be created   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @Number.setter
    def Number(self, number: int):
        """
        Setter for property: (int) Number
          a value indicating how many sections should be created   
            
         
        """
        pass
    
    ## Getter for property: (float) Offset
    ##   a value indicating the distance from the start position   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return float
    @property
    def Offset(self) -> float:
        """
        Getter for property: (float) Offset
          a value indicating the distance from the start position   
            
         
        """
        pass
    
    ## Setter for property: (float) Offset

    ##   a value indicating the distance from the start position   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @Offset.setter
    def Offset(self, offset: float):
        """
        Setter for property: (float) Offset
          a value indicating the distance from the start position   
            
         
        """
        pass
    
    ## Getter for property: (float) Spacing
    ##   a value indicating the space between sections   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return float
    @property
    def Spacing(self) -> float:
        """
        Getter for property: (float) Spacing
          a value indicating the space between sections   
            
         
        """
        pass
    
    ## Setter for property: (float) Spacing

    ##   a value indicating the space between sections   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @Spacing.setter
    def Spacing(self, spacing: float):
        """
        Setter for property: (float) Spacing
          a value indicating the space between sections   
            
         
        """
        pass
    
    ## Getter for property: (@link SectionPlaneBuilder NXOpen.GeometricAnalysis.SectionAnalysis.SectionPlaneBuilder@endlink) SpecifiedPlane
    ##   the user specified section plane   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return SectionPlaneBuilder
    @property
    def SpecifiedPlane(self) -> SectionPlaneBuilder:
        """
        Getter for property: (@link SectionPlaneBuilder NXOpen.GeometricAnalysis.SectionAnalysis.SectionPlaneBuilder@endlink) SpecifiedPlane
          the user specified section plane   
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents the quadrilateral grid section specifications for a @link GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder@endlink .
##             Only used when type is @link GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder::TypesQuadrilateral GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder::TypesQuadrilateral@endlink .
##         
## 
##   <br>  Created in NX6.0.0  <br> 

class QuadrilateralGridBuilder(NXOpen.TaggedObject): 
    """ Represents the quadrilateral grid section specifications for a <ja_class>GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder</ja_class>.
            Only used when type is <ja_enum_member>GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.Types.Quadrilateral</ja_enum_member>.
        """


    ## Getter for property: (@link NXOpen.GeometricUtilities.QuadrilateralFrameBuilder NXOpen.GeometricUtilities.QuadrilateralFrameBuilder@endlink) QuadrilateralFrame
    ##   the quadrilateral frame   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.QuadrilateralFrameBuilder
    @property
    def QuadrilateralFrame(self) -> NXOpen.GeometricUtilities.QuadrilateralFrameBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.QuadrilateralFrameBuilder NXOpen.GeometricUtilities.QuadrilateralFrameBuilder@endlink) QuadrilateralFrame
          the quadrilateral frame   
            
         
        """
        pass
    
    ## Getter for property: (@link GridSpacingBuilder NXOpen.GeometricAnalysis.SectionAnalysis.GridSpacingBuilder@endlink) Spacing
    ##   the spacing specification for the quadrilateral grid   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return GridSpacingBuilder
    @property
    def Spacing(self) -> GridSpacingBuilder:
        """
        Getter for property: (@link GridSpacingBuilder NXOpen.GeometricAnalysis.SectionAnalysis.GridSpacingBuilder@endlink) Spacing
          the spacing specification for the quadrilateral grid   
            
         
        """
        pass
    
    ## Getter for property: (@link SectionPlaneBuilder NXOpen.GeometricAnalysis.SectionAnalysis.SectionPlaneBuilder@endlink) SpecifiedPlane
    ##   the user specified section plane   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return SectionPlaneBuilder
    @property
    def SpecifiedPlane(self) -> SectionPlaneBuilder:
        """
        Getter for property: (@link SectionPlaneBuilder NXOpen.GeometricAnalysis.SectionAnalysis.SectionPlaneBuilder@endlink) SpecifiedPlane
          the user specified section plane   
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents the Radial specification for a @link GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder@endlink .
## 
##   <br>  Created in NX7.0.0  <br> 

class RadialBuilder(NXOpen.TaggedObject): 
    """ Represents the Radial specification for a <ja_class>GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder</ja_class>."""


    ##  The type of the rotation axis
    ##  XC axis 
    class RotationAxisType(Enum):
        """
        Members Include: <Xc> <Yc> <Zc> <View> <ArbitraryVector>
        """
        Xc: int
        Yc: int
        Zc: int
        View: int
        ArbitraryVector: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RadialBuilder.RotationAxisType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) IsSpacingEnabled
    ##   a value indicating whether the spacing is applied   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return bool
    @property
    def IsSpacingEnabled(self) -> bool:
        """
        Getter for property: (bool) IsSpacingEnabled
          a value indicating whether the spacing is applied   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsSpacingEnabled

    ##   a value indicating whether the spacing is applied   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @IsSpacingEnabled.setter
    def IsSpacingEnabled(self, isSpacingEnabled: bool):
        """
        Setter for property: (bool) IsSpacingEnabled
          a value indicating whether the spacing is applied   
            
         
        """
        pass
    
    ## Getter for property: (int) Number
    ##   a value indicating how many sections should created   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return int
    @property
    def Number(self) -> int:
        """
        Getter for property: (int) Number
          a value indicating how many sections should created   
            
         
        """
        pass
    
    ## Setter for property: (int) Number

    ##   a value indicating how many sections should created   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @Number.setter
    def Number(self, number: int):
        """
        Setter for property: (int) Number
          a value indicating how many sections should created   
            
         
        """
        pass
    
    ## Getter for property: (float) Offset
    ##   a value indicating the distance from the start position   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return float
    @property
    def Offset(self) -> float:
        """
        Getter for property: (float) Offset
          a value indicating the distance from the start position   
            
         
        """
        pass
    
    ## Setter for property: (float) Offset

    ##   a value indicating the distance from the start position   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @Offset.setter
    def Offset(self, offset: float):
        """
        Setter for property: (float) Offset
          a value indicating the distance from the start position   
            
         
        """
        pass
    
    ## Getter for property: (@link RadialBuilder.RotationAxisType NXOpen.GeometricAnalysis.SectionAnalysis.RadialBuilder.RotationAxisType@endlink) RotationAxis
    ##   a value indicating the type of the rotation axis  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return RadialBuilder.RotationAxisType
    @property
    def RotationAxis(self) -> RadialBuilder.RotationAxisType:
        """
        Getter for property: (@link RadialBuilder.RotationAxisType NXOpen.GeometricAnalysis.SectionAnalysis.RadialBuilder.RotationAxisType@endlink) RotationAxis
          a value indicating the type of the rotation axis  
            
         
        """
        pass
    
    ## Setter for property: (@link RadialBuilder.RotationAxisType NXOpen.GeometricAnalysis.SectionAnalysis.RadialBuilder.RotationAxisType@endlink) RotationAxis

    ##   a value indicating the type of the rotation axis  
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @RotationAxis.setter
    def RotationAxis(self, rotationAxis: RadialBuilder.RotationAxisType):
        """
        Setter for property: (@link RadialBuilder.RotationAxisType NXOpen.GeometricAnalysis.SectionAnalysis.RadialBuilder.RotationAxisType@endlink) RotationAxis
          a value indicating the type of the rotation axis  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) RotationVector
    ##   the user specified rotation vector   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return NXOpen.Vector3d
    @property
    def RotationVector(self) -> NXOpen.Vector3d:
        """
        Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) RotationVector
          the user specified rotation vector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) RotationVector

    ##   the user specified rotation vector   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @RotationVector.setter
    def RotationVector(self, rotationVector: NXOpen.Vector3d):
        """
        Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) RotationVector
          the user specified rotation vector   
            
         
        """
        pass
    
    ## Getter for property: (float) Spacing
    ##   a value indicating the space between sections   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return float
    @property
    def Spacing(self) -> float:
        """
        Getter for property: (float) Spacing
          a value indicating the space between sections   
            
         
        """
        pass
    
    ## Setter for property: (float) Spacing

    ##   a value indicating the space between sections   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @Spacing.setter
    def Spacing(self, spacing: float):
        """
        Setter for property: (float) Spacing
          a value indicating the space between sections   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) SpecifiedRotationPoint
    ##   the rotation point   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def SpecifiedRotationPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) SpecifiedRotationPoint
          the rotation point   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) SpecifiedRotationPoint

    ##   the rotation point   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @SpecifiedRotationPoint.setter
    def SpecifiedRotationPoint(self, specifiedRotationPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) SpecifiedRotationPoint
          the rotation point   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectPoint NXOpen.SelectPoint@endlink) StartPosition
    ##   the start position   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return NXOpen.SelectPoint
    @property
    def StartPosition(self) -> NXOpen.SelectPoint:
        """
        Getter for property: (@link NXOpen.SelectPoint NXOpen.SelectPoint@endlink) StartPosition
          the start position   
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a @link NXOpen::GeometricAnalysis::SectionAnalysisObject NXOpen::GeometricAnalysis::SectionAnalysisObject@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisObjectCollection::CreateSectionAnalysisBuilder  NXOpen::GeometricAnalysis::AnalysisObjectCollection::CreateSectionAnalysisBuilder @endlink  <br> 
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
## CircularGrid.CircularFrame.AnchorAttachment </term> <description> 
##  
## None </description> </item> 
## 
## <item><term> 
##  
## CircularGrid.CircularFrame.Subtype </term> <description> 
##  
## Arbitrary </description> </item> 
## 
## <item><term> 
##  
## CircularGrid.Spacing.BoundSections1 </term> <description> 
##  
## True </description> </item> 
## 
## <item><term> 
##  
## CircularGrid.Spacing.BoundSections2 </term> <description> 
##  
## True </description> </item> 
## 
## <item><term> 
##  
## CircularGrid.Spacing.Interval1 </term> <description> 
##  
## 45.0 </description> </item> 
## 
## <item><term> 
##  
## CircularGrid.Spacing.Interval2 </term> <description> 
##  
## 50.0 (millimeters part), 2.0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## CircularGrid.Spacing.LockInterval1 </term> <description> 
##  
## False </description> </item> 
## 
## <item><term> 
##  
## CircularGrid.Spacing.LockInterval2 </term> <description> 
##  
## False </description> </item> 
## 
## <item><term> 
##  
## CircularGrid.Spacing.SectionNumber1 </term> <description> 
##  
## 5 </description> </item> 
## 
## <item><term> 
##  
## CircularGrid.Spacing.SectionNumber2 </term> <description> 
##  
## 5 </description> </item> 
## 
## <item><term> 
##  
## CircularGrid.SpecifiedPlane.Plane </term> <description> 
##  
## View </description> </item> 
## 
## <item><term> 
##  
## NeedleDirection </term> <description> 
##  
## Outside </description> </item> 
## 
## <item><term> 
##  
## Output </term> <description> 
##  
## AnalysisObject </description> </item> 
## 
## <item><term> 
##  
## QuadrilateralGrid.QuadrilateralFrame.AnchorAttachment </term> <description> 
##  
## None </description> </item> 
## 
## <item><term> 
##  
## QuadrilateralGrid.QuadrilateralFrame.Subtype </term> <description> 
##  
## Arbitrary </description> </item> 
## 
## <item><term> 
##  
## ScalingMethod </term> <description> 
##  
## Linear </description> </item> 
## 
## <item><term> 
##  
## ShowInflectionPoints </term> <description> 
##  
## False </description> </item> 
## 
## <item><term> 
##  
## ShowPeakPoints </term> <description> 
##  
## False </description> </item> 
## 
## <item><term> 
##  
## ShowSectionLength </term> <description> 
##  
## False </description> </item> 
## 
## <item><term> 
##  
## TriangularGrid.TriangularFrame.AnchorAttachment </term> <description> 
##  
## None </description> </item> 
## 
## <item><term> 
##  
## TriangularGrid.TriangularFrame.Subtype </term> <description> 
##  
## Arbitrary </description> </item> 
## 
## <item><term> 
##  
## Type </term> <description> 
##  
## Parallel </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX6.0.0  <br> 

class SectionAnalysisBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.GeometricAnalysis.SectionAnalysisObject</ja_class> builder. """


    ##  The calculation method 
    ##  Curvature 
    class CalculationMethodType(Enum):
        """
        Members Include: <Curvature> <RadiusofCurvature>
        """
        Curvature: int
        RadiusofCurvature: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SectionAnalysisBuilder.CalculationMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The needle direction 
    ##  Inside 
    class NeedleDirectionType(Enum):
        """
        Members Include: <Inside> <Outside>
        """
        Inside: int
        Outside: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SectionAnalysisBuilder.NeedleDirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The output options 
    ##  Analysis Object 
    class OutputType(Enum):
        """
        Members Include: <AnalysisObject> <SectionCurves> <Both>
        """
        AnalysisObject: int
        SectionCurves: int
        Both: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SectionAnalysisBuilder.OutputType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The scaling method 
    ##  Linear 
    class ScalingMethodType(Enum):
        """
        Members Include: <Linear> <Logarithmic>
        """
        Linear: int
        Logarithmic: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SectionAnalysisBuilder.ScalingMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents the sectioning types 
    ##  Parallel Planes 
    class Types(Enum):
        """
        Members Include: <Parallel> <Isoparametric> <AlongCurve> <Quadrilateral> <Triangular> <Circular>
        """
        Parallel: int
        Isoparametric: int
        AlongCurve: int
        Quadrilateral: int
        Triangular: int
        Circular: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SectionAnalysisBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link SectionAnalysisBuilder.CalculationMethodType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.CalculationMethodType@endlink) CalculationMethod
    ##   the calculation method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return SectionAnalysisBuilder.CalculationMethodType
    @property
    def CalculationMethod(self) -> SectionAnalysisBuilder.CalculationMethodType:
        """
        Getter for property: (@link SectionAnalysisBuilder.CalculationMethodType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.CalculationMethodType@endlink) CalculationMethod
          the calculation method   
            
         
        """
        pass
    
    ## Setter for property: (@link SectionAnalysisBuilder.CalculationMethodType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.CalculationMethodType@endlink) CalculationMethod

    ##   the calculation method   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @CalculationMethod.setter
    def CalculationMethod(self, calculationMethod: SectionAnalysisBuilder.CalculationMethodType):
        """
        Setter for property: (@link SectionAnalysisBuilder.CalculationMethodType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.CalculationMethodType@endlink) CalculationMethod
          the calculation method   
            
         
        """
        pass
    
    ## Getter for property: (@link CircularGridBuilder NXOpen.GeometricAnalysis.SectionAnalysis.CircularGridBuilder@endlink) CircularGrid
    ##   the circular grid.  
    ##   
    ##                 Only used when type is @link NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder::TypesCircular NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder::TypesCircular@endlink    
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return CircularGridBuilder
    @property
    def CircularGrid(self) -> CircularGridBuilder:
        """
        Getter for property: (@link CircularGridBuilder NXOpen.GeometricAnalysis.SectionAnalysis.CircularGridBuilder@endlink) CircularGrid
          the circular grid.  
          
                        Only used when type is @link NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder::TypesCircular NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder::TypesCircular@endlink    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.CombOptionsBuilder NXOpen.GeometricUtilities.CombOptionsBuilder@endlink) CombOptions
    ##   the comb options   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.CombOptionsBuilder
    @property
    def CombOptions(self) -> NXOpen.GeometricUtilities.CombOptionsBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.CombOptionsBuilder NXOpen.GeometricUtilities.CombOptionsBuilder@endlink) CombOptions
          the comb options   
            
         
        """
        pass
    
    ## Getter for property: (@link SectionAnalysisBuilder.NeedleDirectionType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.NeedleDirectionType@endlink) NeedleDirection
    ##   the needle direction   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return SectionAnalysisBuilder.NeedleDirectionType
    @property
    def NeedleDirection(self) -> SectionAnalysisBuilder.NeedleDirectionType:
        """
        Getter for property: (@link SectionAnalysisBuilder.NeedleDirectionType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.NeedleDirectionType@endlink) NeedleDirection
          the needle direction   
            
         
        """
        pass
    
    ## Setter for property: (@link SectionAnalysisBuilder.NeedleDirectionType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.NeedleDirectionType@endlink) NeedleDirection

    ##   the needle direction   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @NeedleDirection.setter
    def NeedleDirection(self, needleDirection: SectionAnalysisBuilder.NeedleDirectionType):
        """
        Setter for property: (@link SectionAnalysisBuilder.NeedleDirectionType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.NeedleDirectionType@endlink) NeedleDirection
          the needle direction   
            
         
        """
        pass
    
    ## Getter for property: (@link SectionAnalysisBuilder.OutputType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.OutputType@endlink) Output
    ##   the output   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return SectionAnalysisBuilder.OutputType
    @property
    def Output(self) -> SectionAnalysisBuilder.OutputType:
        """
        Getter for property: (@link SectionAnalysisBuilder.OutputType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.OutputType@endlink) Output
          the output   
            
         
        """
        pass
    
    ## Setter for property: (@link SectionAnalysisBuilder.OutputType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.OutputType@endlink) Output

    ##   the output   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @Output.setter
    def Output(self, output: SectionAnalysisBuilder.OutputType):
        """
        Setter for property: (@link SectionAnalysisBuilder.OutputType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.OutputType@endlink) Output
          the output   
            
         
        """
        pass
    
    ## Getter for property: (@link QuadrilateralGridBuilder NXOpen.GeometricAnalysis.SectionAnalysis.QuadrilateralGridBuilder@endlink) QuadrilateralGrid
    ##   the quadrilateral grid.  
    ##   
    ##                 Only used when type is @link NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder::TypesQuadrilateral NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder::TypesQuadrilateral@endlink    
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return QuadrilateralGridBuilder
    @property
    def QuadrilateralGrid(self) -> QuadrilateralGridBuilder:
        """
        Getter for property: (@link QuadrilateralGridBuilder NXOpen.GeometricAnalysis.SectionAnalysis.QuadrilateralGridBuilder@endlink) QuadrilateralGrid
          the quadrilateral grid.  
          
                        Only used when type is @link NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder::TypesQuadrilateral NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder::TypesQuadrilateral@endlink    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) References
    ##   the references (faces or faceted bodies)   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.SelectTaggedObjectList
    @property
    def References(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) References
          the references (faces or faceted bodies)   
            
         
        """
        pass
    
    ## Getter for property: (@link SectionAnalysisBuilder.ScalingMethodType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.ScalingMethodType@endlink) ScalingMethod
    ##   the scaling method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return SectionAnalysisBuilder.ScalingMethodType
    @property
    def ScalingMethod(self) -> SectionAnalysisBuilder.ScalingMethodType:
        """
        Getter for property: (@link SectionAnalysisBuilder.ScalingMethodType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.ScalingMethodType@endlink) ScalingMethod
          the scaling method   
            
         
        """
        pass
    
    ## Setter for property: (@link SectionAnalysisBuilder.ScalingMethodType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.ScalingMethodType@endlink) ScalingMethod

    ##   the scaling method   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @ScalingMethod.setter
    def ScalingMethod(self, scalingMethod: SectionAnalysisBuilder.ScalingMethodType):
        """
        Setter for property: (@link SectionAnalysisBuilder.ScalingMethodType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.ScalingMethodType@endlink) ScalingMethod
          the scaling method   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowInflectionPoints
    ##   the flag to show the inflection points of planar sections   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def ShowInflectionPoints(self) -> bool:
        """
        Getter for property: (bool) ShowInflectionPoints
          the flag to show the inflection points of planar sections   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowInflectionPoints

    ##   the flag to show the inflection points of planar sections   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ShowInflectionPoints.setter
    def ShowInflectionPoints(self, showInflectionPoints: bool):
        """
        Setter for property: (bool) ShowInflectionPoints
          the flag to show the inflection points of planar sections   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowPeakPoints
    ##   the flag to show the peak points of the sections   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def ShowPeakPoints(self) -> bool:
        """
        Getter for property: (bool) ShowPeakPoints
          the flag to show the peak points of the sections   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowPeakPoints

    ##   the flag to show the peak points of the sections   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ShowPeakPoints.setter
    def ShowPeakPoints(self, showPeakPoints: bool):
        """
        Setter for property: (bool) ShowPeakPoints
          the flag to show the peak points of the sections   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowSectionLength
    ##   the flag to show the section length labels   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def ShowSectionLength(self) -> bool:
        """
        Getter for property: (bool) ShowSectionLength
          the flag to show the section length labels   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowSectionLength

    ##   the flag to show the section length labels   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ShowSectionLength.setter
    def ShowSectionLength(self, showSectionLength: bool):
        """
        Setter for property: (bool) ShowSectionLength
          the flag to show the section length labels   
            
         
        """
        pass
    
    ## Getter for property: (@link TriangularGridBuilder NXOpen.GeometricAnalysis.SectionAnalysis.TriangularGridBuilder@endlink) TriangularGrid
    ##   the triangular grid.  
    ##   
    ##                 Only used when type is @link NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder::TypesTriangular NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder::TypesTriangular@endlink    
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return TriangularGridBuilder
    @property
    def TriangularGrid(self) -> TriangularGridBuilder:
        """
        Getter for property: (@link TriangularGridBuilder NXOpen.GeometricAnalysis.SectionAnalysis.TriangularGridBuilder@endlink) TriangularGrid
          the triangular grid.  
          
                        Only used when type is @link NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder::TypesTriangular NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder::TypesTriangular@endlink    
         
        """
        pass
    
    ## Getter for property: (@link SectionAnalysisBuilder.Types NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.Types@endlink) Type
    ##   the sectioning type   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return SectionAnalysisBuilder.Types
    @property
    def Type(self) -> SectionAnalysisBuilder.Types:
        """
        Getter for property: (@link SectionAnalysisBuilder.Types NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.Types@endlink) Type
          the sectioning type   
            
         
        """
        pass
    
    ## Setter for property: (@link SectionAnalysisBuilder.Types NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.Types@endlink) Type

    ##   the sectioning type   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @Type.setter
    def Type(self, type: SectionAnalysisBuilder.Types):
        """
        Setter for property: (@link SectionAnalysisBuilder.Types NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.Types@endlink) Type
          the sectioning type   
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a @link NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExObject NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExObject@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisObjectCollection::CreateSectionAnalysisExBuilder  NXOpen::GeometricAnalysis::AnalysisObjectCollection::CreateSectionAnalysisExBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Alignment </term> <description> 
##  
## XYZPlane </description> </item> 
## 
## <item><term> 
##  
## CalculationMethod </term> <description> 
##  
## Curvature </description> </item> 
## 
## <item><term> 
##  
## CurveAligned.IsSpacingEnabled </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## CurveAligned.Number </term> <description> 
##  
## 5 </description> </item> 
## 
## <item><term> 
##  
## CurveAligned.Offset </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## CurveAligned.Spacing </term> <description> 
##  
## 25 </description> </item> 
## 
## <item><term> 
##  
## CurveAligned.SpecifiedPlane.Plane </term> <description> 
##  
## View </description> </item> 
## 
## <item><term> 
##  
## CurveAligned.UseProjectedCurve </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## Interactive.IsCutInfiniteEnabled </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## IsShowInflectionPointsEnabled </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## IsShowLengthEnabled </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## IsShowPeakPointsEnabled </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## Isoparametric.IsSpacingEnabled </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## Isoparametric.IsUEnabled </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## Isoparametric.IsVEnabled </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## Isoparametric.Number </term> <description> 
##  
## 5 </description> </item> 
## 
## <item><term> 
##  
## Isoparametric.Spacing </term> <description> 
##  
## 25 </description> </item> 
## 
## <item><term> 
##  
## NeedleDirection </term> <description> 
##  
## Outside </description> </item> 
## 
## <item><term> 
##  
## Output </term> <description> 
##  
## AnalysisObject </description> </item> 
## 
## <item><term> 
##  
## ParallelPlanes.IsNumberEnabled </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ParallelPlanes.IsSpacingEnabled </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ParallelPlanes.Number </term> <description> 
##  
## 5 </description> </item> 
## 
## <item><term> 
##  
## ParallelPlanes.Offset </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ParallelPlanes.Spacing </term> <description> 
##  
## 50 (millimeters part), 2 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Placement </term> <description> 
##  
## Uniform </description> </item> 
## 
## <item><term> 
##  
## Radial.IsSpacingEnabled </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## Radial.Number </term> <description> 
##  
## 5 </description> </item> 
## 
## <item><term> 
##  
## Radial.Offset </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## Radial.RotationAxis </term> <description> 
##  
## View </description> </item> 
## 
## <item><term> 
##  
## Radial.Spacing </term> <description> 
##  
## 72 </description> </item> 
## 
## <item><term> 
##  
## ScalingMethod </term> <description> 
##  
## Linear </description> </item> 
## 
## <item><term> 
##  
## XYZPlane.IsNumberEnabled </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## XYZPlane.IsSpacingEnabled </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## XYZPlane.IsXEnabled </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## XYZPlane.IsYEnabled </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## XYZPlane.IsZEnabled </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## XYZPlane.Number </term> <description> 
##  
## 5 </description> </item> 
## 
## <item><term> 
##  
## XYZPlane.Spacing </term> <description> 
##  
## 50 (millimeters part), 2 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX7.0.0  <br> 

class SectionAnalysisExBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExObject</ja_class> builder """


    ##  The section alignment type 
    ##  The cutting planes are perpendicular to X, Y or Z plane 
    class AlignmentType(Enum):
        """
        Members Include: <XYZPlane> <ParallelPlanes> <CurveAligned> <Isoparametric> <Radial>
        """
        XYZPlane: int
        ParallelPlanes: int
        CurveAligned: int
        Isoparametric: int
        Radial: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SectionAnalysisExBuilder.AlignmentType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The calculation method 
    ##  Curvature 
    class CalculationMethodType(Enum):
        """
        Members Include: <Curvature> <RadiusofCurvature>
        """
        Curvature: int
        RadiusofCurvature: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SectionAnalysisExBuilder.CalculationMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The needle direction 
    ##  Inside 
    class NeedleDirectionType(Enum):
        """
        Members Include: <Inside> <Outside>
        """
        Inside: int
        Outside: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SectionAnalysisExBuilder.NeedleDirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The output options 
    ##  Analysis Object 
    class OutputType(Enum):
        """
        Members Include: <AnalysisObject> <SectionCurves> <Both>
        """
        AnalysisObject: int
        SectionCurves: int
        Both: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SectionAnalysisExBuilder.OutputType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The types of the section placement
    ##  Uniformly distributed 
    class PlacementType(Enum):
        """
        Members Include: <Uniform> <ThroughPoints> <BetweenPoints> <Interactive>
        """
        Uniform: int
        ThroughPoints: int
        BetweenPoints: int
        Interactive: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SectionAnalysisExBuilder.PlacementType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The scaling method 
    ##  Linear 
    class ScalingMethodType(Enum):
        """
        Members Include: <Linear> <Logarithmic>
        """
        Linear: int
        Logarithmic: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SectionAnalysisExBuilder.ScalingMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link SectionAnalysisExBuilder.AlignmentType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.AlignmentType@endlink) Alignment
    ##   the alignment type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return SectionAnalysisExBuilder.AlignmentType
    @property
    def Alignment(self) -> SectionAnalysisExBuilder.AlignmentType:
        """
        Getter for property: (@link SectionAnalysisExBuilder.AlignmentType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.AlignmentType@endlink) Alignment
          the alignment type   
            
         
        """
        pass
    
    ## Setter for property: (@link SectionAnalysisExBuilder.AlignmentType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.AlignmentType@endlink) Alignment

    ##   the alignment type   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @Alignment.setter
    def Alignment(self, alignment: SectionAnalysisExBuilder.AlignmentType):
        """
        Setter for property: (@link SectionAnalysisExBuilder.AlignmentType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.AlignmentType@endlink) Alignment
          the alignment type   
            
         
        """
        pass
    
    ## Getter for property: (@link SectionAnalysisExBuilder.CalculationMethodType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.CalculationMethodType@endlink) CalculationMethod
    ##   the calculation method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return SectionAnalysisExBuilder.CalculationMethodType
    @property
    def CalculationMethod(self) -> SectionAnalysisExBuilder.CalculationMethodType:
        """
        Getter for property: (@link SectionAnalysisExBuilder.CalculationMethodType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.CalculationMethodType@endlink) CalculationMethod
          the calculation method   
            
         
        """
        pass
    
    ## Setter for property: (@link SectionAnalysisExBuilder.CalculationMethodType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.CalculationMethodType@endlink) CalculationMethod

    ##   the calculation method   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @CalculationMethod.setter
    def CalculationMethod(self, calculationMethod: SectionAnalysisExBuilder.CalculationMethodType):
        """
        Setter for property: (@link SectionAnalysisExBuilder.CalculationMethodType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.CalculationMethodType@endlink) CalculationMethod
          the calculation method   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.CombOptionsBuilder NXOpen.GeometricUtilities.CombOptionsBuilder@endlink) CombOptions
    ##   the comb options specification  
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
          the comb options specification  
            
         
        """
        pass
    
    ## Getter for property: (@link CurveAlignedBuilder NXOpen.GeometricAnalysis.SectionAnalysis.CurveAlignedBuilder@endlink) CurveAligned
    ##   the Curve Aligned section specification.  
    ##   
    ##                 Only used when type is @link NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder::AlignmentTypeCurveAligned NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder::AlignmentTypeCurveAligned@endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return CurveAlignedBuilder
    @property
    def CurveAligned(self) -> CurveAlignedBuilder:
        """
        Getter for property: (@link CurveAlignedBuilder NXOpen.GeometricAnalysis.SectionAnalysis.CurveAlignedBuilder@endlink) CurveAligned
          the Curve Aligned section specification.  
          
                        Only used when type is @link NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder::AlignmentTypeCurveAligned NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder::AlignmentTypeCurveAligned@endlink    
         
        """
        pass
    
    ## Getter for property: (@link InteractiveBuilder NXOpen.GeometricAnalysis.SectionAnalysis.InteractiveBuilder@endlink) Interactive
    ##   the Interactive placement specification.  
    ##   
    ##                 Only used when type is @link NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder::PlacementTypeInteractive NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder::PlacementTypeInteractive@endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return InteractiveBuilder
    @property
    def Interactive(self) -> InteractiveBuilder:
        """
        Getter for property: (@link InteractiveBuilder NXOpen.GeometricAnalysis.SectionAnalysis.InteractiveBuilder@endlink) Interactive
          the Interactive placement specification.  
          
                        Only used when type is @link NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder::PlacementTypeInteractive NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder::PlacementTypeInteractive@endlink    
         
        """
        pass
    
    ## Getter for property: (bool) IsShowInflectionPointsEnabled
    ##   a value indicating whether to show the inflection points   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return bool
    @property
    def IsShowInflectionPointsEnabled(self) -> bool:
        """
        Getter for property: (bool) IsShowInflectionPointsEnabled
          a value indicating whether to show the inflection points   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsShowInflectionPointsEnabled

    ##   a value indicating whether to show the inflection points   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @IsShowInflectionPointsEnabled.setter
    def IsShowInflectionPointsEnabled(self, inflection: bool):
        """
        Setter for property: (bool) IsShowInflectionPointsEnabled
          a value indicating whether to show the inflection points   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsShowLengthEnabled
    ##   a value indicating whether to show the length of each section curve   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return bool
    @property
    def IsShowLengthEnabled(self) -> bool:
        """
        Getter for property: (bool) IsShowLengthEnabled
          a value indicating whether to show the length of each section curve   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsShowLengthEnabled

    ##   a value indicating whether to show the length of each section curve   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @IsShowLengthEnabled.setter
    def IsShowLengthEnabled(self, length: bool):
        """
        Setter for property: (bool) IsShowLengthEnabled
          a value indicating whether to show the length of each section curve   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsShowPeakPointsEnabled
    ##   a value indicating whether to show the peak points   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return bool
    @property
    def IsShowPeakPointsEnabled(self) -> bool:
        """
        Getter for property: (bool) IsShowPeakPointsEnabled
          a value indicating whether to show the peak points   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsShowPeakPointsEnabled

    ##   a value indicating whether to show the peak points   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @IsShowPeakPointsEnabled.setter
    def IsShowPeakPointsEnabled(self, peak: bool):
        """
        Setter for property: (bool) IsShowPeakPointsEnabled
          a value indicating whether to show the peak points   
            
         
        """
        pass
    
    ## Getter for property: (@link IsoparametricBuilder NXOpen.GeometricAnalysis.SectionAnalysis.IsoparametricBuilder@endlink) Isoparametric
    ##   the Isoparametric section specification.  
    ##   
    ##                 Only used when type is @link NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder::AlignmentTypeIsoparametric NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder::AlignmentTypeIsoparametric@endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return IsoparametricBuilder
    @property
    def Isoparametric(self) -> IsoparametricBuilder:
        """
        Getter for property: (@link IsoparametricBuilder NXOpen.GeometricAnalysis.SectionAnalysis.IsoparametricBuilder@endlink) Isoparametric
          the Isoparametric section specification.  
          
                        Only used when type is @link NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder::AlignmentTypeIsoparametric NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder::AlignmentTypeIsoparametric@endlink    
         
        """
        pass
    
    ## Getter for property: (@link SectionAnalysisExBuilder.NeedleDirectionType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.NeedleDirectionType@endlink) NeedleDirection
    ##   the needle direction   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return SectionAnalysisExBuilder.NeedleDirectionType
    @property
    def NeedleDirection(self) -> SectionAnalysisExBuilder.NeedleDirectionType:
        """
        Getter for property: (@link SectionAnalysisExBuilder.NeedleDirectionType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.NeedleDirectionType@endlink) NeedleDirection
          the needle direction   
            
         
        """
        pass
    
    ## Setter for property: (@link SectionAnalysisExBuilder.NeedleDirectionType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.NeedleDirectionType@endlink) NeedleDirection

    ##   the needle direction   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @NeedleDirection.setter
    def NeedleDirection(self, needleDirection: SectionAnalysisExBuilder.NeedleDirectionType):
        """
        Setter for property: (@link SectionAnalysisExBuilder.NeedleDirectionType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.NeedleDirectionType@endlink) NeedleDirection
          the needle direction   
            
         
        """
        pass
    
    ## Getter for property: (@link SectionAnalysisExBuilder.OutputType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.OutputType@endlink) Output
    ##   the output   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return SectionAnalysisExBuilder.OutputType
    @property
    def Output(self) -> SectionAnalysisExBuilder.OutputType:
        """
        Getter for property: (@link SectionAnalysisExBuilder.OutputType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.OutputType@endlink) Output
          the output   
            
         
        """
        pass
    
    ## Setter for property: (@link SectionAnalysisExBuilder.OutputType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.OutputType@endlink) Output

    ##   the output   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @Output.setter
    def Output(self, output: SectionAnalysisExBuilder.OutputType):
        """
        Setter for property: (@link SectionAnalysisExBuilder.OutputType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.OutputType@endlink) Output
          the output   
            
         
        """
        pass
    
    ## Getter for property: (@link ParallelPlanesExBuilder NXOpen.GeometricAnalysis.SectionAnalysis.ParallelPlanesExBuilder@endlink) ParallelPlanes
    ##   the Parallel Planes section specification.  
    ##   
    ##                 Only used when type is @link NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder::AlignmentTypeParallelPlanes NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder::AlignmentTypeParallelPlanes@endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return ParallelPlanesExBuilder
    @property
    def ParallelPlanes(self) -> ParallelPlanesExBuilder:
        """
        Getter for property: (@link ParallelPlanesExBuilder NXOpen.GeometricAnalysis.SectionAnalysis.ParallelPlanesExBuilder@endlink) ParallelPlanes
          the Parallel Planes section specification.  
          
                        Only used when type is @link NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder::AlignmentTypeParallelPlanes NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder::AlignmentTypeParallelPlanes@endlink    
         
        """
        pass
    
    ## Getter for property: (@link SectionAnalysisExBuilder.PlacementType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.PlacementType@endlink) Placement
    ##   the placement   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return SectionAnalysisExBuilder.PlacementType
    @property
    def Placement(self) -> SectionAnalysisExBuilder.PlacementType:
        """
        Getter for property: (@link SectionAnalysisExBuilder.PlacementType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.PlacementType@endlink) Placement
          the placement   
            
         
        """
        pass
    
    ## Setter for property: (@link SectionAnalysisExBuilder.PlacementType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.PlacementType@endlink) Placement

    ##   the placement   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @Placement.setter
    def Placement(self, placement: SectionAnalysisExBuilder.PlacementType):
        """
        Setter for property: (@link SectionAnalysisExBuilder.PlacementType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.PlacementType@endlink) Placement
          the placement   
            
         
        """
        pass
    
    ## Getter for property: (@link RadialBuilder NXOpen.GeometricAnalysis.SectionAnalysis.RadialBuilder@endlink) Radial
    ##   the Radial section specification.  
    ##   
    ##                 Only used when type is @link NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder::AlignmentTypeCurveAligned NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder::AlignmentTypeCurveAligned@endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return RadialBuilder
    @property
    def Radial(self) -> RadialBuilder:
        """
        Getter for property: (@link RadialBuilder NXOpen.GeometricAnalysis.SectionAnalysis.RadialBuilder@endlink) Radial
          the Radial section specification.  
          
                        Only used when type is @link NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder::AlignmentTypeCurveAligned NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder::AlignmentTypeCurveAligned@endlink    
         
        """
        pass
    
    ## Getter for property: (@link SectionAnalysisExBuilder.ScalingMethodType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.ScalingMethodType@endlink) ScalingMethod
    ##   the scaling method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return SectionAnalysisExBuilder.ScalingMethodType
    @property
    def ScalingMethod(self) -> SectionAnalysisExBuilder.ScalingMethodType:
        """
        Getter for property: (@link SectionAnalysisExBuilder.ScalingMethodType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.ScalingMethodType@endlink) ScalingMethod
          the scaling method   
            
         
        """
        pass
    
    ## Setter for property: (@link SectionAnalysisExBuilder.ScalingMethodType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.ScalingMethodType@endlink) ScalingMethod

    ##   the scaling method   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @ScalingMethod.setter
    def ScalingMethod(self, scalingMethod: SectionAnalysisExBuilder.ScalingMethodType):
        """
        Setter for property: (@link SectionAnalysisExBuilder.ScalingMethodType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.ScalingMethodType@endlink) ScalingMethod
          the scaling method   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) SelectObject
    ##   the selected objects   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return NXOpen.SelectTaggedObjectList
    @property
    def SelectObject(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) SelectObject
          the selected objects   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectPointList NXOpen.SelectPointList@endlink) SpecifyPoint
    ##   the specified points   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return NXOpen.SelectPointList
    @property
    def SpecifyPoint(self) -> NXOpen.SelectPointList:
        """
        Getter for property: (@link NXOpen.SelectPointList NXOpen.SelectPointList@endlink) SpecifyPoint
          the specified points   
            
         
        """
        pass
    
    ## Getter for property: (@link XYZPlaneBuilder NXOpen.GeometricAnalysis.SectionAnalysis.XYZPlaneBuilder@endlink) XYZPlane
    ##   the XYZ Planes section specification.  
    ##   
    ##                 Only used when type is @link NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder::AlignmentTypeXYZPlane NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder::AlignmentTypeXYZPlane@endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return XYZPlaneBuilder
    @property
    def XYZPlane(self) -> XYZPlaneBuilder:
        """
        Getter for property: (@link XYZPlaneBuilder NXOpen.GeometricAnalysis.SectionAnalysis.XYZPlaneBuilder@endlink) XYZPlane
          the XYZ Planes section specification.  
          
                        Only used when type is @link NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder::AlignmentTypeXYZPlane NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder::AlignmentTypeXYZPlane@endlink    
         
        """
        pass
    
import NXOpen.GeometricAnalysis
##  Represents a Section Analysis Object of the new version.  Section Analysis
##             generates planar or isoparametric sections across faces and faceted bodies 
##             to help evaluating sectional curvature flow of faces and surface quality and 
##             characteristics in general. Section Analysis object update dynamically on geometry 
##             changes of the sectioned faces and faceted bodies.  <br> To create or edit an instance of this class, use @link NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder  NXOpen::GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder @endlink  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class SectionAnalysisExObject(NXOpen.GeometricAnalysis.AnalysisObject): 
    """ Represents a Section Analysis Object of the new version.  Section Analysis
            generates planar or isoparametric sections across faces and faceted bodies 
            to help evaluating sectional curvature flow of faces and surface quality and 
            characteristics in general. Section Analysis object update dynamically on geometry 
            changes of the sectioned faces and faceted bodies. """
    pass


import NXOpen
import NXOpen.GeometricUtilities
##  Represents a plane which is used to cut sections on faces or facet bodies 
## 
##   <br>  Created in NX7.0.0  <br> 

class SectionPlaneBuilder(NXOpen.TaggedObject): 
    """ Represents a plane which is used to cut sections on faces or facet bodies """


    ##  The type of different section planes 
    ##  XC plane 
    class PlaneType(Enum):
        """
        Members Include: <Xc> <Yc> <Zc> <View> <Plane>
        """
        Xc: int
        Yc: int
        Zc: int
        View: int
        Plane: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SectionPlaneBuilder.PlaneType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Origin
    ##   the plane origin   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def Origin(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Origin
          the plane origin   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Origin

    ##   the plane origin   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @Origin.setter
    def Origin(self, origin: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Origin
          the plane origin   
            
         
        """
        pass
    
    ## Getter for property: (@link SectionPlaneBuilder.PlaneType NXOpen.GeometricAnalysis.SectionAnalysis.SectionPlaneBuilder.PlaneType@endlink) Plane
    ##   the plane type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return SectionPlaneBuilder.PlaneType
    @property
    def Plane(self) -> SectionPlaneBuilder.PlaneType:
        """
        Getter for property: (@link SectionPlaneBuilder.PlaneType NXOpen.GeometricAnalysis.SectionAnalysis.SectionPlaneBuilder.PlaneType@endlink) Plane
          the plane type   
            
         
        """
        pass
    
    ## Setter for property: (@link SectionPlaneBuilder.PlaneType NXOpen.GeometricAnalysis.SectionAnalysis.SectionPlaneBuilder.PlaneType@endlink) Plane

    ##   the plane type   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @Plane.setter
    def Plane(self, plane: SectionPlaneBuilder.PlaneType):
        """
        Setter for property: (@link SectionPlaneBuilder.PlaneType NXOpen.GeometricAnalysis.SectionAnalysis.SectionPlaneBuilder.PlaneType@endlink) Plane
          the plane type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) XAxis
    ##   the plane X axis   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return NXOpen.Vector3d
    @property
    def XAxis(self) -> NXOpen.Vector3d:
        """
        Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) XAxis
          the plane X axis   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) XAxis

    ##   the plane X axis   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @XAxis.setter
    def XAxis(self, xAxis: NXOpen.Vector3d):
        """
        Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) XAxis
          the plane X axis   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) YAxis
    ##   the plane Y axis   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return NXOpen.Vector3d
    @property
    def YAxis(self) -> NXOpen.Vector3d:
        """
        Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) YAxis
          the plane Y axis   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) YAxis

    ##   the plane Y axis   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @YAxis.setter
    def YAxis(self, yAxis: NXOpen.Vector3d):
        """
        Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) YAxis
          the plane Y axis   
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents the triangular grid section specifications for a SectionAnalysisBuilder.
##             Only used when type is @link GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder::TypesTriangular GeometricAnalysis::SectionAnalysis::SectionAnalysisBuilder::TypesTriangular@endlink .
##         
## 
##   <br>  Created in NX6.0.0  <br> 

class TriangularGridBuilder(NXOpen.TaggedObject): 
    """ Represents the triangular grid section specifications for a SectionAnalysisBuilder.
            Only used when type is <ja_enum_member>GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.Types.Triangular</ja_enum_member>.
        """


    ## Getter for property: (@link GridSpacingBuilder NXOpen.GeometricAnalysis.SectionAnalysis.GridSpacingBuilder@endlink) Spacing
    ##   the spacing specification for the triangular grid   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return GridSpacingBuilder
    @property
    def Spacing(self) -> GridSpacingBuilder:
        """
        Getter for property: (@link GridSpacingBuilder NXOpen.GeometricAnalysis.SectionAnalysis.GridSpacingBuilder@endlink) Spacing
          the spacing specification for the triangular grid   
            
         
        """
        pass
    
    ## Getter for property: (@link SectionPlaneBuilder NXOpen.GeometricAnalysis.SectionAnalysis.SectionPlaneBuilder@endlink) SpecifiedPlane
    ##   the user specified section plane   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return SectionPlaneBuilder
    @property
    def SpecifiedPlane(self) -> SectionPlaneBuilder:
        """
        Getter for property: (@link SectionPlaneBuilder NXOpen.GeometricAnalysis.SectionAnalysis.SectionPlaneBuilder@endlink) SpecifiedPlane
          the user specified section plane   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.TriangularFrameBuilder NXOpen.GeometricUtilities.TriangularFrameBuilder@endlink) TriangularFrame
    ##   the triangular frame   
    ##     
    ##  
    ## Getter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.TriangularFrameBuilder
    @property
    def TriangularFrame(self) -> NXOpen.GeometricUtilities.TriangularFrameBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.TriangularFrameBuilder NXOpen.GeometricUtilities.TriangularFrameBuilder@endlink) TriangularFrame
          the triangular frame   
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents the XYZ Plane specification for a @link GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder GeometricAnalysis::SectionAnalysis::SectionAnalysisExBuilder@endlink .
## 
##   <br>  Created in NX7.0.0  <br> 

class XYZPlaneBuilder(NXOpen.TaggedObject): 
    """ Represents the XYZ Plane specification for a <ja_class>GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder</ja_class>."""


    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) AnchorOrigin
    ##   the anchor position   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def AnchorOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) AnchorOrigin
          the anchor position   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) AnchorOrigin

    ##   the anchor position   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @AnchorOrigin.setter
    def AnchorOrigin(self, anchorOrigin: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) AnchorOrigin
          the anchor position   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) AnchorXAxis
    ##   the anchor X axis   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return NXOpen.Vector3d
    @property
    def AnchorXAxis(self) -> NXOpen.Vector3d:
        """
        Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) AnchorXAxis
          the anchor X axis   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) AnchorXAxis

    ##   the anchor X axis   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @AnchorXAxis.setter
    def AnchorXAxis(self, anchorXAxis: NXOpen.Vector3d):
        """
        Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) AnchorXAxis
          the anchor X axis   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) AnchorYAxis
    ##   the anchor Y axis   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return NXOpen.Vector3d
    @property
    def AnchorYAxis(self) -> NXOpen.Vector3d:
        """
        Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) AnchorYAxis
          the anchor Y axis   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) AnchorYAxis

    ##   the anchor Y axis   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @AnchorYAxis.setter
    def AnchorYAxis(self, anchorYAxis: NXOpen.Vector3d):
        """
        Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) AnchorYAxis
          the anchor Y axis   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsNumberEnabled
    ##   a value indicating whether the number is used   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return bool
    @property
    def IsNumberEnabled(self) -> bool:
        """
        Getter for property: (bool) IsNumberEnabled
          a value indicating whether the number is used   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsNumberEnabled

    ##   a value indicating whether the number is used   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @IsNumberEnabled.setter
    def IsNumberEnabled(self, isNumberEnabled: bool):
        """
        Setter for property: (bool) IsNumberEnabled
          a value indicating whether the number is used   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsSpacingEnabled
    ##   a value indicating whether the spacing is applied   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return bool
    @property
    def IsSpacingEnabled(self) -> bool:
        """
        Getter for property: (bool) IsSpacingEnabled
          a value indicating whether the spacing is applied   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsSpacingEnabled

    ##   a value indicating whether the spacing is applied   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @IsSpacingEnabled.setter
    def IsSpacingEnabled(self, isSpacingEnabled: bool):
        """
        Setter for property: (bool) IsSpacingEnabled
          a value indicating whether the spacing is applied   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsXEnabled
    ##   a value indicating whether X is enabled   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return bool
    @property
    def IsXEnabled(self) -> bool:
        """
        Getter for property: (bool) IsXEnabled
          a value indicating whether X is enabled   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsXEnabled

    ##   a value indicating whether X is enabled   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @IsXEnabled.setter
    def IsXEnabled(self, isXEnabled: bool):
        """
        Setter for property: (bool) IsXEnabled
          a value indicating whether X is enabled   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsYEnabled
    ##   a value indicating whether Y is enabled   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return bool
    @property
    def IsYEnabled(self) -> bool:
        """
        Getter for property: (bool) IsYEnabled
          a value indicating whether Y is enabled   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsYEnabled

    ##   a value indicating whether Y is enabled   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @IsYEnabled.setter
    def IsYEnabled(self, isYEnabled: bool):
        """
        Setter for property: (bool) IsYEnabled
          a value indicating whether Y is enabled   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsZEnabled
    ##   a value indicating whether Z is enabled   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return bool
    @property
    def IsZEnabled(self) -> bool:
        """
        Getter for property: (bool) IsZEnabled
          a value indicating whether Z is enabled   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsZEnabled

    ##   a value indicating whether Z is enabled   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @IsZEnabled.setter
    def IsZEnabled(self, isZEnabled: bool):
        """
        Setter for property: (bool) IsZEnabled
          a value indicating whether Z is enabled   
            
         
        """
        pass
    
    ## Getter for property: (int) Number
    ##   a value indicating how many sections should be created   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return int
    @property
    def Number(self) -> int:
        """
        Getter for property: (int) Number
          a value indicating how many sections should be created   
            
         
        """
        pass
    
    ## Setter for property: (int) Number

    ##   a value indicating how many sections should be created   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @Number.setter
    def Number(self, number: int):
        """
        Setter for property: (int) Number
          a value indicating how many sections should be created   
            
         
        """
        pass
    
    ## Getter for property: (float) Spacing
    ##   a value indicating the space between sections   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    ## @return float
    @property
    def Spacing(self) -> float:
        """
        Getter for property: (float) Spacing
          a value indicating the space between sections   
            
         
        """
        pass
    
    ## Setter for property: (float) Spacing

    ##   a value indicating the space between sections   
    ##     
    ##  
    ## Setter License requirements: studio_analyze ("STUDIO ANALYZE")
    ## 
    ##   <br>  Created in NX7.0.0  <br> 

    @Spacing.setter
    def Spacing(self, spacing: float):
        """
        Setter for property: (float) Spacing
          a value indicating the space between sections   
            
         
        """
        pass
    
## @package NXOpen.GeometricAnalysis.SectionAnalysis
## Classes, Enums and Structs under NXOpen.GeometricAnalysis.SectionAnalysis namespace

##  @link RadialBuilderRotationAxisType NXOpen.GeometricAnalysis.SectionAnalysis.RadialBuilderRotationAxisType @endlink is an alias for @link RadialBuilder.RotationAxisType NXOpen.GeometricAnalysis.SectionAnalysis.RadialBuilder.RotationAxisType@endlink
RadialBuilderRotationAxisType = RadialBuilder.RotationAxisType


##  @link SectionAnalysisBuilderCalculationMethodType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilderCalculationMethodType @endlink is an alias for @link SectionAnalysisBuilder.CalculationMethodType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.CalculationMethodType@endlink
SectionAnalysisBuilderCalculationMethodType = SectionAnalysisBuilder.CalculationMethodType


##  @link SectionAnalysisBuilderNeedleDirectionType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilderNeedleDirectionType @endlink is an alias for @link SectionAnalysisBuilder.NeedleDirectionType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.NeedleDirectionType@endlink
SectionAnalysisBuilderNeedleDirectionType = SectionAnalysisBuilder.NeedleDirectionType


##  @link SectionAnalysisBuilderOutputType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilderOutputType @endlink is an alias for @link SectionAnalysisBuilder.OutputType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.OutputType@endlink
SectionAnalysisBuilderOutputType = SectionAnalysisBuilder.OutputType


##  @link SectionAnalysisBuilderScalingMethodType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilderScalingMethodType @endlink is an alias for @link SectionAnalysisBuilder.ScalingMethodType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.ScalingMethodType@endlink
SectionAnalysisBuilderScalingMethodType = SectionAnalysisBuilder.ScalingMethodType


##  @link SectionAnalysisBuilderTypes NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilderTypes @endlink is an alias for @link SectionAnalysisBuilder.Types NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisBuilder.Types@endlink
SectionAnalysisBuilderTypes = SectionAnalysisBuilder.Types


##  @link SectionAnalysisExBuilderAlignmentType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilderAlignmentType @endlink is an alias for @link SectionAnalysisExBuilder.AlignmentType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.AlignmentType@endlink
SectionAnalysisExBuilderAlignmentType = SectionAnalysisExBuilder.AlignmentType


##  @link SectionAnalysisExBuilderCalculationMethodType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilderCalculationMethodType @endlink is an alias for @link SectionAnalysisExBuilder.CalculationMethodType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.CalculationMethodType@endlink
SectionAnalysisExBuilderCalculationMethodType = SectionAnalysisExBuilder.CalculationMethodType


##  @link SectionAnalysisExBuilderNeedleDirectionType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilderNeedleDirectionType @endlink is an alias for @link SectionAnalysisExBuilder.NeedleDirectionType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.NeedleDirectionType@endlink
SectionAnalysisExBuilderNeedleDirectionType = SectionAnalysisExBuilder.NeedleDirectionType


##  @link SectionAnalysisExBuilderOutputType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilderOutputType @endlink is an alias for @link SectionAnalysisExBuilder.OutputType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.OutputType@endlink
SectionAnalysisExBuilderOutputType = SectionAnalysisExBuilder.OutputType


##  @link SectionAnalysisExBuilderPlacementType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilderPlacementType @endlink is an alias for @link SectionAnalysisExBuilder.PlacementType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.PlacementType@endlink
SectionAnalysisExBuilderPlacementType = SectionAnalysisExBuilder.PlacementType


##  @link SectionAnalysisExBuilderScalingMethodType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilderScalingMethodType @endlink is an alias for @link SectionAnalysisExBuilder.ScalingMethodType NXOpen.GeometricAnalysis.SectionAnalysis.SectionAnalysisExBuilder.ScalingMethodType@endlink
SectionAnalysisExBuilderScalingMethodType = SectionAnalysisExBuilder.ScalingMethodType


##  @link SectionPlaneBuilderPlaneType NXOpen.GeometricAnalysis.SectionAnalysis.SectionPlaneBuilderPlaneType @endlink is an alias for @link SectionPlaneBuilder.PlaneType NXOpen.GeometricAnalysis.SectionAnalysis.SectionPlaneBuilder.PlaneType@endlink
SectionPlaneBuilderPlaneType = SectionPlaneBuilder.PlaneType


