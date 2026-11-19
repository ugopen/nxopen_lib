from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class PlacementEngineBuilder(NXOpen.Builder): 
    """ Represents a builder class that will create and work with placement solutions.
    """
    def ApplyPlacementSolution(self, placementSolution: PlacementSolution) -> None:
        """
         Sets the transform on part being placed using the supplied placement solution.
                
        """
        pass
    def ComputePlacementSolutions(self) -> List[PlacementSolution]:
        """
         Computes and returns the placement solutions
                
         Returns placementSolutions ( PlacementSolution List[NXOpe): .
        """
        pass
    def SetFilteredPlacementSolutions(self, placementSolutions: List[PlacementSolution]) -> None:
        """
         Sets the input PlacementSolutions as the filtered solutions on the PlacementEngineBuilder in the given order.
                    Different clients can have their own methodology for filtering the solutions 
                    e.g. Part Placement can decide to filter out solutions based on a particular port on the input placeable object.
                
        """
        pass
import NXOpen
class PlacementSolution(NXOpen.NXObject): 
    """ This class represents the placement solution
    """
    pass
