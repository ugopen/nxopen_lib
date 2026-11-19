from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
## 
##         Represents a @link NXOpen::CAE::Safety::DummyPositionerBuilder NXOpen::CAE::Safety::DummyPositionerBuilder@endlink 
##          <br> To create a new instance of this class, use @link NXOpen::CAE::SafetyManager::CreateDummyPositionerBuilder  NXOpen::CAE::SafetyManager::CreateDummyPositionerBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class DummyPositionerBuilder(NXOpen.Builder): 
    """
        Represents a <ja_class>NXOpen.CAE.Safety.DummyPositionerBuilder</ja_class>
        """


    ## Getter for property: (str) DummyName
    ##   the name of dummy   
    ##     
    ##  
    ## Getter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def DummyName(self) -> str:
        """
        Getter for property: (str) DummyName
          the name of dummy   
            
         
        """
        pass
    
    ## Setter for property: (str) DummyName

    ##   the name of dummy   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @DummyName.setter
    def DummyName(self, pDummyName: str):
        """
        Setter for property: (str) DummyName
          the name of dummy   
            
         
        """
        pass
    
    ##  Resets rotated limb to its original position 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Name of Limb 
    def ResetLimbPosition(builder: DummyPositionerBuilder, pLimbName: str) -> None:
        """
         Resets rotated limb to its original position 
        """
        pass
    
    ##  Rotates limb of the dummy by given angle about the given axis 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  Name of Limb 
    def SetLimbRotation(builder: DummyPositionerBuilder, pLimbName: str, taitBryanAxisType: int, dAngle: float) -> None:
        """
         Rotates limb of the dummy by given angle about the given axis 
        """
        pass
    
## @package NXOpen.CAE.Safety
## Classes, Enums and Structs under NXOpen.CAE.Safety namespace

