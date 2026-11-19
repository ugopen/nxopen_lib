from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.CAE
class Utils(NXOpen.Object): 
    """ Contains mesh mapping utility methods. """
    def CreateMappedPanelsFromNodes(sourceGroups: List[NXOpen.CAE.CaeGroup], targetObjects: List[NXOpen.TaggedObject], maxDistance: float, numInfluencingNodes: int, groupNames: List[str], panelNames: List[str]) -> None:
        """
         Create structural node groups and panels from the acoustical groups by using a mesh mapping algorithm. 
        """
        pass
