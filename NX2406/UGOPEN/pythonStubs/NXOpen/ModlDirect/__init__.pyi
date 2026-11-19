from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.GeometricUtilities
## 
##     Represents a @link NXOpen::ModlDirect::SelectBlend NXOpen::ModlDirect::SelectBlend@endlink 
##     Allows user to specify blend faces.
##     
## 
##   <br>  Created in NX5.0.2  <br> 

class SelectBlend(NXOpen.TaggedObject): 
    """
    Represents a <ja_class>NXOpen.ModlDirect.SelectBlend</ja_class>
    Allows user to specify blend faces.
    """


    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FaceCollector
    ##  Returns the blend faces collector.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.2  <br> 

    ## @return NXOpen.ScCollector
    @property
    def FaceCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FaceCollector
         Returns the blend faces collector.  
             
         
        """
        pass
    
    ##  Exclude the user de-selected blend face 
    ## 
    ##   <br>  Created in NX5.0.2  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING")
    ## 
    ## <param name="blendFace"> (@link NXOpen.Face NXOpen.Face@endlink)  the blend face to exclude </param>
    def ExcludeBlend(self, blendFace: NXOpen.Face) -> None:
        """
         Exclude the user de-selected blend face 
        """
        pass
    
    ##  Include the use selected blend face 
    ## 
    ##   <br>  Created in NX5.0.2  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING")
    ## 
    ## <param name="blendFace"> (@link NXOpen.Face NXOpen.Face@endlink)  the blend face to include </param>
    def IncludeBlend(self, blendFace: NXOpen.Face) -> None:
        """
         Include the use selected blend face 
        """
        pass
    
    ##  Auto regonize the adjacent blends of input base faces 
    ##  @return blends (@link NXOpen.Face List[NXOpen.Face]@endlink):  the adjacent blend faces .
    ## 
    ##   <br>  Created in NX5.0.2  <br> 

    ## License requirements: solid_modeling ("SOLIDS MODELING") OR cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING")
    ## 
    ## <param name="baseFaces"> (@link NXOpen.Face List[NXOpen.Face]@endlink)  the base faces </param>
    def RecognizeBlends(self, baseFaces: List[NXOpen.Face]) -> List[NXOpen.Face]:
        """
         Auto regonize the adjacent blends of input base faces 
         @return blends (@link NXOpen.Face List[NXOpen.Face]@endlink):  the adjacent blend faces .
        """
        pass
    
## @package NXOpen.ModlDirect
## Classes, Enums and Structs under NXOpen.ModlDirect namespace

