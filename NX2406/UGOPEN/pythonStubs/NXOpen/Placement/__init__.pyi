from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents a builder class that will create and work with placement solutions.
##      <br> An instance of this class can be obtained from @link NXOpen::RoutingCommon::PartPlacementBuilder::InitializePlacementEngineBuilder NXOpen::RoutingCommon::PartPlacementBuilder::InitializePlacementEngineBuilder@endlink   <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class PlacementEngineBuilder(NXOpen.Builder): 
    """ Represents a builder class that will create and work with placement solutions.
    """


    ##  Sets the transform on part being placed using the supplied placement solution.
    ##         
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="placementSolution"> (@link PlacementSolution NXOpen.Placement.PlacementSolution@endlink) </param>
    def ApplyPlacementSolution(self, placementSolution: PlacementSolution) -> None:
        """
         Sets the transform on part being placed using the supplied placement solution.
                
        """
        pass
    
    ##  Computes and returns the placement solutions
    ##         
    ##  @return placementSolutions (@link PlacementSolution List[NXOpen.Placement.PlacementSolution]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def ComputePlacementSolutions(self) -> List[PlacementSolution]:
        """
         Computes and returns the placement solutions
                
         @return placementSolutions (@link PlacementSolution List[NXOpen.Placement.PlacementSolution]@endlink): .
        """
        pass
    
    ##  Sets the input PlacementSolutions as the filtered solutions on the PlacementEngineBuilder in the given order.
    ##             Different clients can have their own methodology for filtering the solutions 
    ##             e.g. Part Placement can decide to filter out solutions based on a particular port on the input placeable object.
    ##         
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="placementSolutions"> (@link PlacementSolution List[NXOpen.Placement.PlacementSolution]@endlink) </param>
    def SetFilteredPlacementSolutions(self, placementSolutions: List[PlacementSolution]) -> None:
        """
         Sets the input PlacementSolutions as the filtered solutions on the PlacementEngineBuilder in the given order.
                    Different clients can have their own methodology for filtering the solutions 
                    e.g. Part Placement can decide to filter out solutions based on a particular port on the input placeable object.
                
        """
        pass
    
import NXOpen
##  This class represents the placement solution
##      <br> Use @link Placement::PlacementEngineBuilder::ComputePlacementSolutions Placement::PlacementEngineBuilder::ComputePlacementSolutions@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class PlacementSolution(NXOpen.NXObject): 
    """ This class represents the placement solution
    """
    pass


## @package NXOpen.Placement
## Classes, Enums and Structs under NXOpen.Placement namespace

