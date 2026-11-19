from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents the BaseObject class.  <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class BaseObject(NXOpen.NXObject): 
    """ Represents the BaseObject class. """


    ## Getter for property: (str) Identifier
    ##  Returns the identifier  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def Identifier(self) -> str:
        """
        Getter for property: (str) Identifier
         Returns the identifier  
            
         
        """
        pass
    
    ## Setter for property: (str) Identifier

    ##  Returns the identifier  
    ##     
    ##  
    ## Setter License requirements: nx_diagramming ("NX Diagramming"), routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @Identifier.setter
    def Identifier(self, id: str):
        """
        Setter for property: (str) Identifier
         Returns the identifier  
            
         
        """
        pass
    
##  Represents the Connection class.  <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class Connection(BaseObject): 
    """ Represents the Connection class. """


    ##  Gets the end port of the connection.
    ##  @return port (@link Port NXOpen.Schematic.Model.Port@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def GetEnd(self) -> Port:
        """
         Gets the end port of the connection.
         @return port (@link Port NXOpen.Schematic.Model.Port@endlink): .
        """
        pass
    
    ##  Gets the start port of the connection.
    ##  @return port (@link Port NXOpen.Schematic.Model.Port@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def GetStart(self) -> Port:
        """
         Gets the start port of the connection.
         @return port (@link Port NXOpen.Schematic.Model.Port@endlink): .
        """
        pass
    
##  Represents the Node class.  <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class Node(BaseObject): 
    """ Represents the Node class. """
    pass


##  Represents the Port class.  <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class Port(BaseObject): 
    """ Represents the Port class. """
    pass


## @package NXOpen.Schematic.Model
## Classes, Enums and Structs under NXOpen.Schematic.Model namespace

