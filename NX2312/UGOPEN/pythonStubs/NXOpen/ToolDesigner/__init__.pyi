from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents a class that is used for ToolDesigner testing.  This class shouldn't be made available to customers  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ToolDesignerDebugSession(NXOpen.Object): 
    """ Represents a class that is used for ToolDesigner testing.  This class shouldn't be made available to customers """


    ##  Dump the table entry for a part 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: fp_fixture_planner ("FULL FIXTURE PLANNER")
    @staticmethod
    def ValidateFpData() -> None:
        """
         Dump the table entry for a part 
        """
        pass
    
## @package NXOpen.ToolDesigner
## Classes, Enums and Structs under NXOpen.ToolDesigner namespace

