from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.CAE
##  Contains mesh mapping utility methods.  <br> To obtain an instance of this class, refer to @link NXOpen::CAE::CaeSession  NXOpen::CAE::CaeSession @endlink  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class Utils(NXOpen.Object): 
    """ Contains mesh mapping utility methods. """


    ##  Create structural node groups and panels from the acoustical groups by using a mesh mapping algorithm. 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: sc_nv_modeling ("Simcenter Noise and Vibration modeling")
    ## <param name="sourceGroups"> (@link NXOpen.CAE.CaeGroup List[NXOpen.CAE.CaeGroup]@endlink)  The array of source acoustical groups.</param>
    ## <param name="targetObjects"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink)  The array of target structural objects.</param>
    ## <param name="maxDistance"> (float)  Mesh Mapping parameter: Maximum Distance.</param>
    ## <param name="numInfluencingNodes"> (int)  Mesh Mapping parameter: Number of Influencing Nodes.</param>
    ## <param name="groupNames"> (List[str])  The array of structural group names. The size of the array should equal to the number of source groups. </param>
    ## <param name="panelNames"> (List[str])  The array of structural panel names. The size of the array should equal to the number of source groups. </param>
    def CreateMappedPanelsFromNodes(sourceGroups: List[NXOpen.CAE.CaeGroup], targetObjects: List[NXOpen.TaggedObject], maxDistance: float, numInfluencingNodes: int, groupNames: List[str], panelNames: List[str]) -> None:
        """
         Create structural node groups and panels from the acoustical groups by using a mesh mapping algorithm. 
        """
        pass
    
## @package NXOpen.CAE.MeshMapping
## Classes, Enums and Structs under NXOpen.CAE.MeshMapping namespace

