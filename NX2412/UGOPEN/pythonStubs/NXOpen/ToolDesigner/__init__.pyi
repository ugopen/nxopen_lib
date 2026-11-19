from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class ToolDesignerDebugSession(NXOpen.Object): 
    """ Represents a class that is used for ToolDesigner testing.  This class shouldn't be made available to customers """
    def ValidateFpData() -> None:
        """
         Dump the table entry for a part 
        """
        pass
