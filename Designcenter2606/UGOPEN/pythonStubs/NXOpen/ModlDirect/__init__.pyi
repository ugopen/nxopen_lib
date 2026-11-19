from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.GeometricUtilities
class SelectBlend(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.ModlDirect.SelectBlend
    Allows user to specify blend faces.
    """
    @property
    def FaceCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FaceCollector
         Returns the blend faces collector.  
             
         
        """
        pass
    def ExcludeBlend(self, blendFace: NXOpen.Face) -> None:
        """
         Exclude the user de-selected blend face 
        """
        pass
    def IncludeBlend(self, blendFace: NXOpen.Face) -> None:
        """
         Include the use selected blend face 
        """
        pass
    def RecognizeBlends(self, baseFaces: List[NXOpen.Face]) -> List[NXOpen.Face]:
        """
         Auto regonize the adjacent blends of input base faces 
         Returns blends ( NXOpen.Face Li):  the adjacent blend faces .
        """
        pass
