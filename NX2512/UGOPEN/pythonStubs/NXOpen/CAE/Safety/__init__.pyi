from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class DummyPositionerBuilder(NXOpen.Builder): 
    """
        Represents a NXOpen.CAE.Safety.DummyPositionerBuilder
        """
    @property
    def DummyName(self) -> str:
        """
        Getter for property: (str) DummyName
         Returns the name of dummy   
            
         
        """
        pass
    @DummyName.setter
    def DummyName(self, pDummyName: str):
        """
        Setter for property: (str) DummyName
         Returns the name of dummy   
            
         
        """
        pass
    def ResetLimbPosition(self, pLimbName: str) -> None:
        """
         Resets rotated limb to its original position 
        """
        pass
    def SetLimbRotation(self, pLimbName: str, taitBryanAxisType: int, dAngle: float) -> None:
        """
         Rotates limb of the dummy by given angle about the given axis 
        """
        pass
