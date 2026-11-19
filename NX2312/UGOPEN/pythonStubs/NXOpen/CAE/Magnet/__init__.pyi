from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.CAE
##  Contains magnet utility methods  <br> To obtain an instance of this class, refer to @link NXOpen::CAE::CaeSession  NXOpen::CAE::CaeSession @endlink  <br> 
## 
##  <br>  Usable only on Windows <br>  
## 
##   <br>  Created in NX2312.0.0  <br> 

class Utils(NXOpen.Object): 
    """ Contains magnet utility methods """


    ##  Populates the result objects 
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## <param name="propTable"> (@link NXOpen.CAE.ModelingObjectPropertyTable NXOpen.CAE.ModelingObjectPropertyTable@endlink) </param>
    ## <param name="propName"> (str) </param>
    ## <param name="ptGeometries"> (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink) </param>
    def FillResultObjects(propTable: NXOpen.CAE.ModelingObjectPropertyTable, propName: str, ptGeometries: List[NXOpen.DisplayableObject]) -> None:
        """
         Populates the result objects 
        """
        pass
    
    ##  Retrieves the conducting bodies 
    ##  @return oBodies (@link NXOpen.CAE.CAEBody List[NXOpen.CAE.CAEBody]@endlink):  all bodies matching the specifications.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetConductingBodies() -> List[NXOpen.CAE.CAEBody]:
        """
         Retrieves the conducting bodies 
         @return oBodies (@link NXOpen.CAE.CAEBody List[NXOpen.CAE.CAEBody]@endlink):  all bodies matching the specifications.
        """
        pass
    
    ##  Retrieves the conducting faces 
    ##  @return oFaces (@link NXOpen.CAE.CAEFace List[NXOpen.CAE.CAEFace]@endlink):  all faces matching the specifications.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetConductingFaces() -> List[NXOpen.CAE.CAEFace]:
        """
         Retrieves the conducting faces 
         @return oFaces (@link NXOpen.CAE.CAEFace List[NXOpen.CAE.CAEFace]@endlink):  all faces matching the specifications.
        """
        pass
    
    ##  Retrieves the magnetic loss bodies 
    ##  @return oBodies (@link NXOpen.CAE.CAEBody List[NXOpen.CAE.CAEBody]@endlink):  all bodies matching the specifications.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetMagneticLossBodies() -> List[NXOpen.CAE.CAEBody]:
        """
         Retrieves the magnetic loss bodies 
         @return oBodies (@link NXOpen.CAE.CAEBody List[NXOpen.CAE.CAEBody]@endlink):  all bodies matching the specifications.
        """
        pass
    
    ##  Retrieves the magnetic loss faces 
    ##  @return oFaces (@link NXOpen.CAE.CAEFace List[NXOpen.CAE.CAEFace]@endlink):  all faces matching the specifications.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetMagneticLossFaces() -> List[NXOpen.CAE.CAEFace]:
        """
         Retrieves the magnetic loss faces 
         @return oFaces (@link NXOpen.CAE.CAEFace List[NXOpen.CAE.CAEFace]@endlink):  all faces matching the specifications.
        """
        pass
    
    ##  Retrieves the magnetostriction bodies 
    ##  @return oBodies (@link NXOpen.CAE.CAEBody List[NXOpen.CAE.CAEBody]@endlink):  all bodies matching the specifications.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetMagnetostrictionBodies() -> List[NXOpen.CAE.CAEBody]:
        """
         Retrieves the magnetostriction bodies 
         @return oBodies (@link NXOpen.CAE.CAEBody List[NXOpen.CAE.CAEBody]@endlink):  all bodies matching the specifications.
        """
        pass
    
    ##  Retrieves the magnetostriction faces 
    ##  @return oFaces (@link NXOpen.CAE.CAEFace List[NXOpen.CAE.CAEFace]@endlink):  all faces matching the specifications.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetMagnetostrictionFaces() -> List[NXOpen.CAE.CAEFace]:
        """
         Retrieves the magnetostriction faces 
         @return oFaces (@link NXOpen.CAE.CAEFace List[NXOpen.CAE.CAEFace]@endlink):  all faces matching the specifications.
        """
        pass
    
    ##  Retrieves the permanent magnet bodies 
    ##  @return oBodies (@link NXOpen.CAE.CAEBody List[NXOpen.CAE.CAEBody]@endlink):  all bodies matching the specifications.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPermanentMagnetBodies() -> List[NXOpen.CAE.CAEBody]:
        """
         Retrieves the permanent magnet bodies 
         @return oBodies (@link NXOpen.CAE.CAEBody List[NXOpen.CAE.CAEBody]@endlink):  all bodies matching the specifications.
        """
        pass
    
    ##  Retrieves the permanent magnet faces 
    ##  @return oFaces (@link NXOpen.CAE.CAEFace List[NXOpen.CAE.CAEFace]@endlink):  all faces matching the specifications.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPermanentMagnetFaces() -> List[NXOpen.CAE.CAEFace]:
        """
         Retrieves the permanent magnet faces 
         @return oFaces (@link NXOpen.CAE.CAEFace List[NXOpen.CAE.CAEFace]@endlink):  all faces matching the specifications.
        """
        pass
    
    ##  Retrieves the permeable bodies 
    ##  @return oBodies (@link NXOpen.CAE.CAEBody List[NXOpen.CAE.CAEBody]@endlink):  all bodies matching the specifications.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ##  check if the permeability value is greater than 1 
    @staticmethod
    def GetPermeableBodies(checkPermeabilityValue: bool) -> List[NXOpen.CAE.CAEBody]:
        """
         Retrieves the permeable bodies 
         @return oBodies (@link NXOpen.CAE.CAEBody List[NXOpen.CAE.CAEBody]@endlink):  all bodies matching the specifications.
        """
        pass
    
    ##  Retrieves the permeable faces 
    ##  @return oFaces (@link NXOpen.CAE.CAEFace List[NXOpen.CAE.CAEFace]@endlink):  all faces matching the specifications.
    ## 
    ##  <br>  Usable only on Windows <br>  
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ##  check if the permeability value is greater than 1 
    @staticmethod
    def GetPermeableFaces(checkPermeabilityValue: bool) -> List[NXOpen.CAE.CAEFace]:
        """
         Retrieves the permeable faces 
         @return oFaces (@link NXOpen.CAE.CAEFace List[NXOpen.CAE.CAEFace]@endlink):  all faces matching the specifications.
        """
        pass
    
## @package NXOpen.CAE.Magnet
## Classes, Enums and Structs under NXOpen.CAE.Magnet namespace

