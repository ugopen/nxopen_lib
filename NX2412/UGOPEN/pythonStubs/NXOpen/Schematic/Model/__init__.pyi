from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class BaseObject(NXOpen.NXObject): 
    """ Represents the BaseObject class. """
    @property
    def Identifier(self) -> str:
        """
        Getter for property: (str) Identifier
         Returns the identifier  
            
         
        """
        pass
    @Identifier.setter
    def Identifier(self, id: str):
        """
        Setter for property: (str) Identifier
         Returns the identifier  
            
         
        """
        pass
class Connection(BaseObject): 
    """ Represents the Connection class. """
    def GetEnd(self) -> Port:
        """
         Gets the end port of the connection.
         Returns port ( Port NXOpen.Sch): .
        """
        pass
    def GetStart(self) -> Port:
        """
         Gets the start port of the connection.
         Returns port ( Port NXOpen.Sch): .
        """
        pass
class Node(BaseObject): 
    """ Represents the Node class. """
    pass
class Port(BaseObject): 
    """ Represents the Port class. """
    pass
