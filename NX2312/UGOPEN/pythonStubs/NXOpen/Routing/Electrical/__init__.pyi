from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##      
##     Represents a @link NXOpen::Routing::Electrical::AssignProxyBuilder NXOpen::Routing::Electrical::AssignProxyBuilder@endlink . This is used 
##     to create a proxy port and assign it to a connector.
##      <br> To create a new instance of this class, use @link NXOpen::Routing::RouteManager::CreateAssignProxyBuilder  NXOpen::Routing::RouteManager::CreateAssignProxyBuilder @endlink  <br> 
## 
##   <br>  Created in NX8.0.0  <br> 

class AssignProxyBuilder(NXOpen.Builder): 
    """     
    Represents a <ja_class>NXOpen.Routing.Electrical.AssignProxyBuilder</ja_class>. This is used 
    to create a proxy port and assign it to a connector.
    """


    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point
    ##   the position of the proxy port to be created.  
    ##   
    ##           
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def Point(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point
          the position of the proxy port to be created.  
          
                  
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point

    ##   the position of the proxy port to be created.  
    ##   
    ##           
    ##  
    ## Setter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @Point.setter
    def Point(self, point: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point
          the position of the proxy port to be created.  
          
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector
    ##   the direction of the proxy port to be created.  
    ##   
    ##           
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def Vector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector
          the direction of the proxy port to be created.  
          
                  
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector

    ##   the direction of the proxy port to be created.  
    ##   
    ##           
    ##  
    ## Setter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @Vector.setter
    def Vector(self, vector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector
          the direction of the proxy port to be created.  
          
                  
         
        """
        pass
    
import NXOpen
##  Represents a collection of @link NXOpen::Routing::Electrical::CableConnection NXOpen::Routing::Electrical::CableConnection@endlink  objects.
##              <br> 
##             See the NX Routing help for detailed information on the Connection data model.
##              <br> 
##          <br> To obtain an instance of this class, refer to @link NXOpen::Routing::RouteManager  NXOpen::Routing::RouteManager @endlink  <br> 
## 
##   <br>  Created in NX4.0.2  <br> 

class CableConnectionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of <ja_class>NXOpen.Routing.Electrical.CableConnection</ja_class> objects.
            <para>
            See the NX Routing help for detailed information on the Connection data model.
            </para>
        """


    ##  Creates a @link NXOpen::Routing::Electrical::CableConnection NXOpen::Routing::Electrical::CableConnection@endlink  object. 
    ##  @return cable_connection (@link CableConnection NXOpen.Routing.Electrical.CableConnection@endlink):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    def CreateCableConnection(object_in_part: CableConnectionCollection) -> CableConnection:
        """
         Creates a @link NXOpen::Routing::Electrical::CableConnection NXOpen::Routing::Electrical::CableConnection@endlink  object. 
         @return cable_connection (@link CableConnection NXOpen.Routing.Electrical.CableConnection@endlink):  .
        """
        pass
    
    ##  Creates a @link NXOpen::Routing::Electrical::CableConnection NXOpen::Routing::Electrical::CableConnection@endlink  object
    ##                 implemented by a @link NXOpen::Routing::Electrical::ShieldDevice NXOpen::Routing::Electrical::ShieldDevice@endlink . 
    ##  @return cable_connection (@link CableConnection NXOpen.Routing.Electrical.CableConnection@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    def CreateShieldConnection(object_in_part: CableConnectionCollection) -> CableConnection:
        """
         Creates a @link NXOpen::Routing::Electrical::CableConnection NXOpen::Routing::Electrical::CableConnection@endlink  object
                        implemented by a @link NXOpen::Routing::Electrical::ShieldDevice NXOpen::Routing::Electrical::ShieldDevice@endlink . 
         @return cable_connection (@link CableConnection NXOpen.Routing.Electrical.CableConnection@endlink):  .
        """
        pass
    
##  Connection used by a @link NXOpen::Routing::Electrical::CableDevice NXOpen::Routing::Electrical::CableDevice@endlink .
##              <br> 
##             Use is similar to a @link NXOpen::Routing::Electrical::PathConnection NXOpen::Routing::Electrical::PathConnection@endlink , 
##             except that a cable connection may have many paths due to many wire and/or cable children.
##              <br> 
##             See the NX Routing help for detailed information on the Connection data model.
##          <br> To create a new instance of this class, use @link NXOpen::Routing::Electrical::CableConnectionCollection::CreateCableConnection  NXOpen::Routing::Electrical::CableConnectionCollection::CreateCableConnection @endlink  <br> 
## 
##   <br>  Created in NX4.0.2  <br> 

class CableConnection(Connection): 
    """ Connection used by a <ja_class>NXOpen.Routing.Electrical.CableDevice</ja_class>.
            <para>
            Use is similar to a <ja_class>NXOpen.Routing.Electrical.PathConnection</ja_class>, 
            except that a cable connection may have many paths due to many wire and/or cable children.
            </para>
            See the NX Routing help for detailed information on the Connection data model.
        """


    ##  Is this cable routed? 
    ##  @return is_routed (bool):  <ul>
    ##                                 <li><tt>true</tt> The cable is routed.</li>
    ##                                 <li><tt>false</tt> The cable not routed.</li>
    ##                             </ul>
    ##                         .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def IsCableRouted(connection: CableConnection) -> bool:
        """
         Is this cable routed? 
         @return is_routed (bool):  <ul>
                                        <li><tt>true</tt> The cable is routed.</li>
                                        <li><tt>false</tt> The cable not routed.</li>
                                    </ul>
                                .
        """
        pass
    
import NXOpen.Routing
##  Holds the collection of wires in a @link NXOpen::Routing::Electrical::CableDevice NXOpen::Routing::Electrical::CableDevice@endlink .
##              <br> 
##             A cable consists of both a @link NXOpen::Routing::Electrical::CableDevice NXOpen::Routing::Electrical::CableDevice@endlink 
##             and a @link NXOpen::Routing::Electrical::CableDefinition NXOpen::Routing::Electrical::CableDefinition@endlink .
##             A @link NXOpen::Routing::Electrical::CableDevice NXOpen::Routing::Electrical::CableDevice@endlink  object uses a 
##             @link NXOpen::Routing::Electrical::CableDefinition NXOpen::Routing::Electrical::CableDefinition@endlink  to hold
##             a collection of @link NXOpen::Routing::Electrical::WireDevice NXOpen::Routing::Electrical::WireDevice@endlink  objects and/or
##             @link NXOpen::Routing::Electrical::CableDevice NXOpen::Routing::Electrical::CableDevice@endlink  objects contained
##             by the cable. This definition corresponds to AP212 Assembly_definition.
##              <br> 
##             See the NX Routing help for detailed information on the Connection data model.
##          <br> Creator not available in KF.  <br> 
## 
##   <br>  Created in NX4.0.2  <br> 

class CableDefinition(NXOpen.Routing.AssemblyDefinition): 
    """ Holds the collection of wires in a <ja_class>NXOpen.Routing.Electrical.CableDevice</ja_class>.
            <para>
            A cable consists of both a <ja_class>NXOpen.Routing.Electrical.CableDevice</ja_class>
            and a <ja_class>NXOpen.Routing.Electrical.CableDefinition</ja_class>.
            A <ja_class>NXOpen.Routing.Electrical.CableDevice</ja_class> object uses a 
            <ja_class>NXOpen.Routing.Electrical.CableDefinition</ja_class> to hold
            a collection of <ja_class>NXOpen.Routing.Electrical.WireDevice</ja_class> objects and/or
            <ja_class>NXOpen.Routing.Electrical.CableDevice</ja_class> objects contained
            by the cable. This definition corresponds to AP212 Assembly_definition.
            </para>
            See the NX Routing help for detailed information on the Connection data model.
        """
    pass


##  Corresponds to a cable instance of an @link NXOpen::Routing::Electrical::ElectricalStockDevice NXOpen::Routing::Electrical::ElectricalStockDevice@endlink .
##              <br> 
##             A cable consists of both a @link NXOpen::Routing::Electrical::CableDevice NXOpen::Routing::Electrical::CableDevice@endlink 
##             and a @link NXOpen::Routing::Electrical::CableDefinition NXOpen::Routing::Electrical::CableDefinition@endlink .
##             A @link NXOpen::Routing::Electrical::CableDevice NXOpen::Routing::Electrical::CableDevice@endlink  object uses a 
##             @link NXOpen::Routing::Electrical::CableDefinition NXOpen::Routing::Electrical::CableDefinition@endlink  to hold
##             a collection of @link NXOpen::Routing::Electrical::WireDevice NXOpen::Routing::Electrical::WireDevice@endlink  objects and/or
##             @link NXOpen::Routing::Electrical::CableDevice NXOpen::Routing::Electrical::CableDevice@endlink  objects contained
##             by the cable.
##              <br> 
##             See the NX Routing help for detailed information on the Connection data model.
##          <br> Creator not available in KF.  <br> 
## 
##   <br>  Created in NX4.0.2  <br> 

class CableDevice(ElectricalStockDevice): 
    """ Corresponds to a cable instance of an <ja_class>NXOpen.Routing.Electrical.ElectricalStockDevice</ja_class>.
            <para>
            A cable consists of both a <ja_class>NXOpen.Routing.Electrical.CableDevice</ja_class>
            and a <ja_class>NXOpen.Routing.Electrical.CableDefinition</ja_class>.
            A <ja_class>NXOpen.Routing.Electrical.CableDevice</ja_class> object uses a 
            <ja_class>NXOpen.Routing.Electrical.CableDefinition</ja_class> to hold
            a collection of <ja_class>NXOpen.Routing.Electrical.WireDevice</ja_class> objects and/or
            <ja_class>NXOpen.Routing.Electrical.CableDevice</ja_class> objects contained
            by the cable.
            </para>
            See the NX Routing help for detailed information on the Connection data model.
        """


    ##  Returns the associated @link NXOpen::Routing::Electrical::CableDefinition NXOpen::Routing::Electrical::CableDefinition@endlink . 
    ##  @return elec_cable_definition (@link CableDefinition NXOpen.Routing.Electrical.CableDefinition@endlink):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def GetAssemblyDefinition(elec_cable_device: CableDevice) -> CableDefinition:
        """
         Returns the associated @link NXOpen::Routing::Electrical::CableDefinition NXOpen::Routing::Electrical::CableDefinition@endlink . 
         @return elec_cable_definition (@link CableDefinition NXOpen.Routing.Electrical.CableDefinition@endlink):  .
        """
        pass
    
    ##  Returns the part number of the conduit applied over this @link NXOpen::Routing::Electrical::CableDevice NXOpen::Routing::Electrical::CableDevice@endlink 
    ##                 object. 
    ##  @return conduitPartNumber (str):  .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def GetConduitPartNumber(elecCableDevice: CableDevice) -> str:
        """
         Returns the part number of the conduit applied over this @link NXOpen::Routing::Electrical::CableDevice NXOpen::Routing::Electrical::CableDevice@endlink 
                        object. 
         @return conduitPartNumber (str):  .
        """
        pass
    
    ##  Loads the given cable part and imports the connections from given part and adds them as
    ##                 children to the @link NXOpen::Routing::Electrical::CableDevice NXOpen::Routing::Electrical::CableDevice@endlink . 
    ## 
    ##   <br>  Created in NX6.0.1  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## Must be fullpath and PART_NAME for a regular part and PART_NAME for
    ##                        part family or part table parts
    def ImportCablePart(elec_cable_device: CableDevice, part_name: str) -> None:
        """
         Loads the given cable part and imports the connections from given part and adds them as
                        children to the @link NXOpen::Routing::Electrical::CableDevice NXOpen::Routing::Electrical::CableDevice@endlink . 
        """
        pass
    
    ##  Sets the part number of the conduit to be applied over this @link NXOpen::Routing::Electrical::CableDevice NXOpen::Routing::Electrical::CableDevice@endlink 
    ##                 object. 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  
    def SetConduitPartNumber(elecCableDevice: CableDevice, conduitPartNumber: str) -> None:
        """
         Sets the part number of the conduit to be applied over this @link NXOpen::Routing::Electrical::CableDevice NXOpen::Routing::Electrical::CableDevice@endlink 
                        object. 
        """
        pass
    
##  Describes a cable's stock.
##              <br> 
##             Contains characteristics of the material that makes up the cable.
##              <br> 
##             See the NX Routing help for detailed information on the Connection data model.
##          <br> Creator not available in KF.  <br> 
## 
##   <br>  Created in NX4.0.2  <br> 

class CableStockDefinition(ElectricalStockDefinition): 
    """ Describes a cable's stock.
            <para>
            Contains characteristics of the material that makes up the cable.
            </para>
            See the NX Routing help for detailed information on the Connection data model.
        """


    ## Getter for property: (int) CableLocation
    ##  the cable stock's location   
    ##     
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## @return int
    @property
    def CableLocation(self) -> int:
        """
        Getter for property: (int) CableLocation
         the cable stock's location   
            
         
        """
        pass
    
    ## Setter for property: (int) CableLocation

    ##  the cable stock's location   
    ##     
    ##  
    ## Setter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @CableLocation.setter
    def CableLocation(self, locationValue: int):
        """
        Setter for property: (int) CableLocation
         the cable stock's location   
            
         
        """
        pass
    
    ## Getter for property: (float) CoverThickness
    ##  the thickness of the cable's covering.  
    ##      
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## @return float
    @property
    def CoverThickness(self) -> float:
        """
        Getter for property: (float) CoverThickness
         the thickness of the cable's covering.  
             
         
        """
        pass
    
    ## Setter for property: (float) CoverThickness

    ##  the thickness of the cable's covering.  
    ##      
    ##  
    ## Setter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @CoverThickness.setter
    def CoverThickness(self, thicknessValue: float):
        """
        Setter for property: (float) CoverThickness
         the thickness of the cable's covering.  
             
         
        """
        pass
    
    ## Getter for property: (float) WireSpacing
    ##  the separation between wires in a cable.  
    ##      
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## @return float
    @property
    def WireSpacing(self) -> float:
        """
        Getter for property: (float) WireSpacing
         the separation between wires in a cable.  
             
         
        """
        pass
    
    ## Setter for property: (float) WireSpacing

    ##  the separation between wires in a cable.  
    ##      
    ##  
    ## Setter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @WireSpacing.setter
    def WireSpacing(self, spacingValue: float):
        """
        Setter for property: (float) WireSpacing
         the separation between wires in a cable.  
             
         
        """
        pass
    
import NXOpen
import NXOpen.Routing
##  Represents @link NXOpen::Routing::Electrical::CablewaysBuilder NXOpen::Routing::Electrical::CablewaysBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::Routing::RouteManager::CreateCablewaysBuilder  NXOpen::Routing::RouteManager::CreateCablewaysBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AllowNewCables </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## AllowOverFill </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## CableTrayArea.Value </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## CableTrayMaximumHeight.Value </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## CabletrayHeight.Value </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## CabletrayWidth.Value </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## FillPercentage.Value </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## SpecifiedFillPercentage.Value </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX7.5.0  <br> 

class CablewaysBuilder(NXOpen.Builder): 
    """ Represents <ja_class>NXOpen.Routing.Electrical.CablewaysBuilder</ja_class>. """


    ## Getter for property: (bool) AllowNewCables
    ##   the allow new cables toggle   
    ##     
    ##  
    ## Getter License requirements: routing_cabling ("Routing Cabling")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def AllowNewCables(self) -> bool:
        """
        Getter for property: (bool) AllowNewCables
          the allow new cables toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) AllowNewCables

    ##   the allow new cables toggle   
    ##     
    ##  
    ## Setter License requirements: routing_cabling ("Routing Cabling")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @AllowNewCables.setter
    def AllowNewCables(self, allowNewCables: bool):
        """
        Setter for property: (bool) AllowNewCables
          the allow new cables toggle   
            
         
        """
        pass
    
    ## Getter for property: (bool) AllowOverFill
    ##   the Allow Overfill toggle   
    ##     
    ##  
    ## Getter License requirements: routing_cabling ("Routing Cabling")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def AllowOverFill(self) -> bool:
        """
        Getter for property: (bool) AllowOverFill
          the Allow Overfill toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) AllowOverFill

    ##   the Allow Overfill toggle   
    ##     
    ##  
    ## Setter License requirements: routing_cabling ("Routing Cabling")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @AllowOverFill.setter
    def AllowOverFill(self, allowOverfill: bool):
        """
        Setter for property: (bool) AllowOverFill
          the Allow Overfill toggle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CableTrayArea
    ##   the cabletray area expression   
    ##     
    ##  
    ## Getter License requirements: routing_cabling ("Routing Cabling")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.Expression
    @property
    def CableTrayArea(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CableTrayArea
          the cabletray area expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CableTrayMaximumHeight
    ##   the cabletray maximum height expression   
    ##     
    ##  
    ## Getter License requirements: routing_cabling ("Routing Cabling")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.Expression
    @property
    def CableTrayMaximumHeight(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CableTrayMaximumHeight
          the cabletray maximum height expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CabletrayHeight
    ##   the cabletray height expression   
    ##     
    ##  
    ## Getter License requirements: routing_cabling ("Routing Cabling")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.Expression
    @property
    def CabletrayHeight(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CabletrayHeight
          the cabletray height expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CabletrayWidth
    ##   the cabletray width expression   
    ##     
    ##  
    ## Getter License requirements: routing_cabling ("Routing Cabling")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.Expression
    @property
    def CabletrayWidth(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CabletrayWidth
          the cabletray width expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FillPercentage
    ##   the fill percentage expression   
    ##     
    ##  
    ## Getter License requirements: routing_cabling ("Routing Cabling")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Expression
    @property
    def FillPercentage(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FillPercentage
          the fill percentage expression   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Routing.RouteObjectCollector NXOpen.Routing.RouteObjectCollector@endlink) RouteObjectCollector
    ##   the route object collector   
    ##     
    ##  
    ## Getter License requirements: routing_cabling ("Routing Cabling")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Routing.RouteObjectCollector
    @property
    def RouteObjectCollector(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: (@link NXOpen.Routing.RouteObjectCollector NXOpen.Routing.RouteObjectCollector@endlink) RouteObjectCollector
          the route object collector   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SpecifiedFillPercentage
    ##   the specified fill percentage expression   
    ##     
    ##  
    ## Getter License requirements: routing_cabling ("Routing Cabling")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return NXOpen.Expression
    @property
    def SpecifiedFillPercentage(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SpecifiedFillPercentage
          the specified fill percentage expression   
            
         
        """
        pass
    
import NXOpen
##  Represents @link NXOpen::Routing::Electrical::CablewaysLayoutBuilder NXOpen::Routing::Electrical::CablewaysLayoutBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::Routing::RouteManager::CreateCablewaysLayoutBuilder  NXOpen::Routing::RouteManager::CreateCablewaysLayoutBuilder @endlink  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class CablewaysLayoutBuilder(NXOpen.Builder): 
    """ Represents <ja_class>NXOpen.Routing.Electrical.CablewaysLayoutBuilder</ja_class>. """
    pass


import NXOpen
##  Represents a collection of @link NXOpen::Routing::Electrical::CablewaysLayoutView NXOpen::Routing::Electrical::CablewaysLayoutView@endlink  objects.  <br> To obtain an instance of this class, refer to @link NXOpen::Routing::RouteManager  NXOpen::Routing::RouteManager @endlink  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class CablewaysLayoutViewCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of <ja_class>NXOpen.Routing.Electrical.CablewaysLayoutView</ja_class> objects. """


    ##  Creates @link NXOpen::Routing::Electrical::CablewaysLayoutView NXOpen::Routing::Electrical::CablewaysLayoutView@endlink  object. 
    ##             Only one @link NXOpen::Routing::Electrical::CablewaysLayoutView NXOpen::Routing::Electrical::CablewaysLayoutView@endlink  object
    ##             can exist per segment, so if the object already exists, it returns the same.
    ##         
    ##  @return view (@link CablewaysLayoutView NXOpen.Routing.Electrical.CablewaysLayoutView@endlink): .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_cabling ("Routing Cabling")
    ##  Segment on which layout view should be created or whose view is asked. 
    def CreateLayoutView(objectInPart: CablewaysLayoutViewCollection, segment: NXOpen.Curve) -> CablewaysLayoutView:
        """
         Creates @link NXOpen::Routing::Electrical::CablewaysLayoutView NXOpen::Routing::Electrical::CablewaysLayoutView@endlink  object. 
                    Only one @link NXOpen::Routing::Electrical::CablewaysLayoutView NXOpen::Routing::Electrical::CablewaysLayoutView@endlink  object
                    can exist per segment, so if the object already exists, it returns the same.
                
         @return view (@link CablewaysLayoutView NXOpen.Routing.Electrical.CablewaysLayoutView@endlink): .
        """
        pass
    
import NXOpen
##  Represents the CablewaysLayoutView class.  <br> No creator as of now  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class CablewaysLayoutView(NXOpen.NXObject): 
    """ Represents the CablewaysLayoutView class. """


    ##  Condemns the layout view entities. 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_cabling ("Routing Cabling")
    @staticmethod
    def CondemnLayoutViewEntities(layoutView: CablewaysLayoutView) -> None:
        """
         Condemns the layout view entities. 
        """
        pass
    
    ##  Flips the layout view along view direction. 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_cabling ("Routing Cabling")
    @staticmethod
    def FlipView(layoutView: CablewaysLayoutView) -> None:
        """
         Flips the layout view along view direction. 
        """
        pass
    
    ##  Returns the view direction. 
    ##  @return viewDirection (bool):  .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_cabling ("Routing Cabling")
    @staticmethod
    def GetViewDirection(layoutView: CablewaysLayoutView) -> bool:
        """
         Returns the view direction. 
         @return viewDirection (bool):  .
        """
        pass
    
    ##  Returns the orientation matrix and origin associated with the layout view. 
    ##  @return A tuple consisting of (orientation, origin). 
    ##  - orientation is: @link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink. .
    ##  - origin is: @link NXOpen.Point3d NXOpen.Point3d@endlink. .

    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_cabling ("Routing Cabling")
    @staticmethod
    def GetViewMatrixAndOrigin(layoutView: CablewaysLayoutView) -> Tuple[NXOpen.Matrix3x3, NXOpen.Point3d]:
        """
         Returns the orientation matrix and origin associated with the layout view. 
         @return A tuple consisting of (orientation, origin). 
         - orientation is: @link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink. .
         - origin is: @link NXOpen.Point3d NXOpen.Point3d@endlink. .

        """
        pass
    
    ##  Highlights the layout view. 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_cabling ("Routing Cabling")
    @staticmethod
    def HighlightView(layoutView: CablewaysLayoutView) -> None:
        """
         Highlights the layout view. 
        """
        pass
    
    ##   Positions the layout view in the 3D space as per input orientation matrix and origin. 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_cabling ("Routing Cabling")
    ##  
    @overload
    def PositionLayoutView(self, layoutView: CablewaysLayoutView, orientation: NXOpen.Matrix3x3, origin: NXOpen.Point3d) -> None:
        """
          Positions the layout view in the 3D space as per input orientation matrix and origin. 
        """
        pass
    
    ##   Positions the layout view in the 3D space as per the @link NXOpen::Xform NXOpen::Xform@endlink . 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_cabling ("Routing Cabling")
    ##  
    @overload
    def PositionLayoutView(self, layoutView: CablewaysLayoutView, toOrientation: NXOpen.Xform) -> None:
        """
          Positions the layout view in the 3D space as per the @link NXOpen::Xform NXOpen::Xform@endlink . 
        """
        pass
    
    ##   Uncondemns the layout view entities. 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_cabling ("Routing Cabling")
    @staticmethod
    def UncondemnLayoutViewEntities(layoutView: CablewaysLayoutView) -> None:
        """
          Uncondemns the layout view entities. 
        """
        pass
    
    ##  Unhighlights the layout view. 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_cabling ("Routing Cabling")
    @staticmethod
    def UnhighlightView(layoutView: CablewaysLayoutView) -> None:
        """
         Unhighlights the layout view. 
        """
        pass
    
import NXOpen
##  Represents a collection of @link NXOpen::Routing::Electrical::Connection NXOpen::Routing::Electrical::Connection@endlink  objects.   <br> To obtain an instance of this class, refer to @link NXOpen::Routing::RouteManager  NXOpen::Routing::RouteManager @endlink  <br> 
## 
##   <br>  Created in NX4.0.3  <br> 

class ConnectionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of <ja_class>NXOpen.Routing.Electrical.Connection</ja_class> objects.  """


    ##  Get Connections 
    ##  @return connections (@link Connection List[NXOpen.Routing.Electrical.Connection]@endlink):  .
    ## 
    ##   <br>  Created in NX4.0.3  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def GetConnections(object_in_part: ConnectionCollection) -> List[Connection]:
        """
         Get Connections 
         @return connections (@link Connection List[NXOpen.Routing.Electrical.Connection]@endlink):  .
        """
        pass
    
import NXOpen.Routing
##   @brief 
##             The electrical usage of a @link NXOpen::Routing::LogicalConnection NXOpen::Routing::LogicalConnection@endlink , restricted to
##             one From and one To terminal.
##              
## 
##  
##              <br> 
##             See NX Open Routing help for detailed information on the Connection data model.
##              <br> 
##          <br> Creator not available in KF.  <br> 
## 
##   <br>  Created in NX4.0.2  <br> 

class Connection(NXOpen.Routing.LogicalConnection): 
    """ <summary>
            The electrical usage of a <ja_class>NXOpen.Routing.LogicalConnection</ja_class>, restricted to
            one From and one To terminal.
            </summary>
            <para>
            See NX Open Routing help for detailed information on the Connection data model.
            </para>
        """


    ##  Routing level. 
    ##  Route to the pin on the connector component. 
    class RouteLevel(Enum):
        """
        Members Include: <NotRouted> <Pin> <Component> <Mixed>
        """
        NotRouted: int
        Pin: int
        Component: int
        Mixed: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Connection.RouteLevel:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Routing.LogicalTerminal NXOpen.Routing.LogicalTerminal@endlink) FromTerminal
    ##   the From terminal.  
    ##    The From terminal is one end of an electrical connection.  From does not imply an ordering.  
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## @return NXOpen.Routing.LogicalTerminal
    @property
    def FromTerminal(self) -> NXOpen.Routing.LogicalTerminal:
        """
        Getter for property: (@link NXOpen.Routing.LogicalTerminal NXOpen.Routing.LogicalTerminal@endlink) FromTerminal
          the From terminal.  
           The From terminal is one end of an electrical connection.  From does not imply an ordering.  
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Routing.LogicalTerminal NXOpen.Routing.LogicalTerminal@endlink) FromTerminal

    ##   the From terminal.  
    ##    The From terminal is one end of an electrical connection.  From does not imply an ordering.  
    ##  
    ## Setter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    @FromTerminal.setter
    def FromTerminal(self, from_terminal: NXOpen.Routing.LogicalTerminal):
        """
        Setter for property: (@link NXOpen.Routing.LogicalTerminal NXOpen.Routing.LogicalTerminal@endlink) FromTerminal
          the From terminal.  
           The From terminal is one end of an electrical connection.  From does not imply an ordering.  
         
        """
        pass
    
    ## Getter for property: (float) MaximumPathLength
    ##   the maximum path length for this connection.  
    ##     Maximum path length is the longest allowable length
    ##                 of all segments referred to by this connection.  
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## @return float
    @property
    def MaximumPathLength(self) -> float:
        """
        Getter for property: (float) MaximumPathLength
          the maximum path length for this connection.  
            Maximum path length is the longest allowable length
                        of all segments referred to by this connection.  
         
        """
        pass
    
    ## Setter for property: (float) MaximumPathLength

    ##   the maximum path length for this connection.  
    ##     Maximum path length is the longest allowable length
    ##                 of all segments referred to by this connection.  
    ##  
    ## Setter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    @MaximumPathLength.setter
    def MaximumPathLength(self, path_length: float):
        """
        Setter for property: (float) MaximumPathLength
          the maximum path length for this connection.  
            Maximum path length is the longest allowable length
                        of all segments referred to by this connection.  
         
        """
        pass
    
    ## Getter for property: (float) MinimumPathLength
    ##   the minimum path length for this connection.  
    ##     Minimum path length is the shortest allowable length
    ##                 of all segments referred to by this connection.  
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## @return float
    @property
    def MinimumPathLength(self) -> float:
        """
        Getter for property: (float) MinimumPathLength
          the minimum path length for this connection.  
            Minimum path length is the shortest allowable length
                        of all segments referred to by this connection.  
         
        """
        pass
    
    ## Setter for property: (float) MinimumPathLength

    ##   the minimum path length for this connection.  
    ##     Minimum path length is the shortest allowable length
    ##                 of all segments referred to by this connection.  
    ##  
    ## Setter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    @MinimumPathLength.setter
    def MinimumPathLength(self, path_length: float):
        """
        Setter for property: (float) MinimumPathLength
          the minimum path length for this connection.  
            Minimum path length is the shortest allowable length
                        of all segments referred to by this connection.  
         
        """
        pass
    
    ## Getter for property: (str) PathLengthMultiplier
    ##   the path length multiplier.  
    ##     Used to calculate cut length.
    ##                 Cut length = length * multiplier + offset   
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## @return str
    @property
    def PathLengthMultiplier(self) -> str:
        """
        Getter for property: (str) PathLengthMultiplier
          the path length multiplier.  
            Used to calculate cut length.
                        Cut length = length * multiplier + offset   
         
        """
        pass
    
    ## Setter for property: (str) PathLengthMultiplier

    ##   the path length multiplier.  
    ##     Used to calculate cut length.
    ##                 Cut length = length * multiplier + offset   
    ##  
    ## Setter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    @PathLengthMultiplier.setter
    def PathLengthMultiplier(self, path_length_multiplier: str):
        """
        Setter for property: (str) PathLengthMultiplier
          the path length multiplier.  
            Used to calculate cut length.
                        Cut length = length * multiplier + offset   
         
        """
        pass
    
    ## Getter for property: (str) PathLengthOffset
    ##   the path length offset.  
    ##     Used to calculate cut length.
    ##                 Cut length = length * multiplier + offset   
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## @return str
    @property
    def PathLengthOffset(self) -> str:
        """
        Getter for property: (str) PathLengthOffset
          the path length offset.  
            Used to calculate cut length.
                        Cut length = length * multiplier + offset   
         
        """
        pass
    
    ## Setter for property: (str) PathLengthOffset

    ##   the path length offset.  
    ##     Used to calculate cut length.
    ##                 Cut length = length * multiplier + offset   
    ##  
    ## Setter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    @PathLengthOffset.setter
    def PathLengthOffset(self, path_length_offset: str):
        """
        Setter for property: (str) PathLengthOffset
          the path length offset.  
            Used to calculate cut length.
                        Cut length = length * multiplier + offset   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Routing.LogicalTerminal NXOpen.Routing.LogicalTerminal@endlink) ToTerminal
    ##   the To terminal.  
    ##    The To terminal is one end of an electrical connection.  To does not imply an ordering  
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## @return NXOpen.Routing.LogicalTerminal
    @property
    def ToTerminal(self) -> NXOpen.Routing.LogicalTerminal:
        """
        Getter for property: (@link NXOpen.Routing.LogicalTerminal NXOpen.Routing.LogicalTerminal@endlink) ToTerminal
          the To terminal.  
           The To terminal is one end of an electrical connection.  To does not imply an ordering  
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Routing.LogicalTerminal NXOpen.Routing.LogicalTerminal@endlink) ToTerminal

    ##   the To terminal.  
    ##    The To terminal is one end of an electrical connection.  To does not imply an ordering  
    ##  
    ## Setter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    @ToTerminal.setter
    def ToTerminal(self, to_terminal: NXOpen.Routing.LogicalTerminal):
        """
        Setter for property: (@link NXOpen.Routing.LogicalTerminal NXOpen.Routing.LogicalTerminal@endlink) ToTerminal
          the To terminal.  
           The To terminal is one end of an electrical connection.  To does not imply an ordering  
         
        """
        pass
    
    ##  Add an intermediate terminal to this connection
    ##  @return result (bool):  Was the @link NXOpen::Routing::LogicalTerminal NXOpen::Routing::LogicalTerminal@endlink  added successfully?  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  Can not be NULL 
    def AddIntermediateTerminal(connection: Connection, intermediate_terminal: NXOpen.Routing.LogicalTerminal) -> bool:
        """
         Add an intermediate terminal to this connection
         @return result (bool):  Was the @link NXOpen::Routing::LogicalTerminal NXOpen::Routing::LogicalTerminal@endlink  added successfully?  .
        """
        pass
    
    ##  Assigns the given path to this connection and routes the connection on the path using the given routing level.
    ##                 Use @link NXOpen::Routing::Electrical::Connection::FindPaths NXOpen::Routing::Electrical::Connection::FindPaths@endlink  to find all available paths for this connection.
    ##             
    ## 
    ##   <br>  Created in NX8.0.3  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  The path on which to route this connection. 
    def AssignPath(connection: Connection, routeLevel: Connection.RouteLevel, path: NXOpen.Routing.Path) -> None:
        """
         Assigns the given path to this connection and routes the connection on the path using the given routing level.
                        Use @link NXOpen::Routing::Electrical::Connection::FindPaths NXOpen::Routing::Electrical::Connection::FindPaths@endlink  to find all available paths for this connection.
                    
        """
        pass
    
    ##  Automatically routes this connection on the shortest path using the given routing level. 
    ## 
    ##   <br>  Created in NX8.0.3  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ## <param name="routeLevel"> (@link Connection.RouteLevel NXOpen.Routing.Electrical.Connection.RouteLevel@endlink) </param>
    def AutomaticallyRoute(connection: Connection, routeLevel: Connection.RouteLevel) -> None:
        """
         Automatically routes this connection on the shortest path using the given routing level. 
        """
        pass
    
    ##  Get the From Connector for this connection.  From does not imply an ordering. 
    ##  @return connector_device (@link ConnectorDevice NXOpen.Routing.Electrical.ConnectorDevice@endlink):  May be NULL  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def FindFromConnector(connection: Connection) -> ConnectorDevice:
        """
         Get the From Connector for this connection.  From does not imply an ordering. 
         @return connector_device (@link ConnectorDevice NXOpen.Routing.Electrical.ConnectorDevice@endlink):  May be NULL  .
        """
        pass
    
    ##  Query this connection to find the nearest harness.
    ##                 Only finds a cable that is a parent to this connection at some level up the connection heirarchy.
    ##  @return cable_device (@link CableDevice NXOpen.Routing.Electrical.CableDevice@endlink):  Will be NULL if connection is not in a cable .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def FindNearestCableDevice(connection: Connection) -> CableDevice:
        """
         Query this connection to find the nearest harness.
                        Only finds a cable that is a parent to this connection at some level up the connection heirarchy.
         @return cable_device (@link CableDevice NXOpen.Routing.Electrical.CableDevice@endlink):  Will be NULL if connection is not in a cable .
        """
        pass
    
    ##  Query this connection to find the nearest harness.
    ##                 Only finds a harness that is a parent to this connection at some level up the connection heirarchy. 
    ##  @return harness_device (@link HarnessDevice NXOpen.Routing.Electrical.HarnessDevice@endlink):  May be NULL if connection is not in a harness .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def FindNearestHarnessDevice(connection: Connection) -> HarnessDevice:
        """
         Query this connection to find the nearest harness.
                        Only finds a harness that is a parent to this connection at some level up the connection heirarchy. 
         @return harness_device (@link HarnessDevice NXOpen.Routing.Electrical.HarnessDevice@endlink):  May be NULL if connection is not in a harness .
        """
        pass
    
    ##  Queries this connection for the nearest parent device.  The nearest parent device is either
    ##                 a cable, shield, or harness  
    ##  @return single_device (@link NXOpen.Routing.SingleDevice NXOpen.Routing.SingleDevice@endlink):  Will be NULL if connection is not in a harness, cable, or shield. .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def FindNearestParentDevice(connection: Connection) -> NXOpen.Routing.SingleDevice:
        """
         Queries this connection for the nearest parent device.  The nearest parent device is either
                        a cable, shield, or harness  
         @return single_device (@link NXOpen.Routing.SingleDevice NXOpen.Routing.SingleDevice@endlink):  Will be NULL if connection is not in a harness, cable, or shield. .
        """
        pass
    
    ##  Returns all the possible paths this connection can use. 
    ##  @return paths (@link NXOpen.Routing.Path List[NXOpen.Routing.Path]@endlink):  Possible paths this connection can use. .
    ## 
    ##   <br>  Created in NX8.0.3  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ## <param name="routeLevel"> (@link Connection.RouteLevel NXOpen.Routing.Electrical.Connection.RouteLevel@endlink) </param>
    def FindPaths(connection: Connection, routeLevel: Connection.RouteLevel) -> List[NXOpen.Routing.Path]:
        """
         Returns all the possible paths this connection can use. 
         @return paths (@link NXOpen.Routing.Path List[NXOpen.Routing.Path]@endlink):  Possible paths this connection can use. .
        """
        pass
    
    ##  Get the To Connector for this connection.  To does not imply an ordering 
    ##  @return connector_device (@link ConnectorDevice NXOpen.Routing.Electrical.ConnectorDevice@endlink):  May be NULL .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def FindToConnector(connection: Connection) -> ConnectorDevice:
        """
         Get the To Connector for this connection.  To does not imply an ordering 
         @return connector_device (@link ConnectorDevice NXOpen.Routing.Electrical.ConnectorDevice@endlink):  May be NULL .
        """
        pass
    
    ##  Get the intermediate terminals associated with this connection. Intermediate Terminals are
    ##                 optional and need not exist for a @link NXOpen::Routing::Electrical::Connection NXOpen::Routing::Electrical::Connection@endlink  to be valid in NX.
    ##  @return intermediate_terminals (@link NXOpen.Routing.LogicalTerminal List[NXOpen.Routing.LogicalTerminal]@endlink):  Collection of intermediate @link NXOpen::Routing::LogicalTerminal NXOpen::Routing::LogicalTerminal@endlink  - May be NULL.
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def GetIntermediateTerminals(connection: Connection) -> List[NXOpen.Routing.LogicalTerminal]:
        """
         Get the intermediate terminals associated with this connection. Intermediate Terminals are
                        optional and need not exist for a @link NXOpen::Routing::Electrical::Connection NXOpen::Routing::Electrical::Connection@endlink  to be valid in NX.
         @return intermediate_terminals (@link NXOpen.Routing.LogicalTerminal List[NXOpen.Routing.LogicalTerminal]@endlink):  Collection of intermediate @link NXOpen::Routing::LogicalTerminal NXOpen::Routing::LogicalTerminal@endlink  - May be NULL.
        """
        pass
    
    ##  Gets the level used to route this connection. 
    ##  @return routed_level (str):  <ul>
    ##                                                                    <li>"C" Connection routed at component level</li>
    ##                                                                    <li>"P" Connection routed at pin level</li>
    ##                                                                    <li>"M" Connection routed at mixed level</li>
    ##                                                                    </ul> .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def GetRoutedLevel(connection: Connection) -> str:
        """
         Gets the level used to route this connection. 
         @return routed_level (str):  <ul>
                                                                           <li>"C" Connection routed at component level</li>
                                                                           <li>"P" Connection routed at pin level</li>
                                                                           <li>"M" Connection routed at mixed level</li>
                                                                           </ul> .
        """
        pass
    
    ##  Similar to @link NXOpen::Routing::Electrical::Connection::GetRoutedLevel NXOpen::Routing::Electrical::Connection::GetRoutedLevel@endlink ,
    ##                 but returns the @link NXOpen::Routing::Electrical::Connection::RouteLevel NXOpen::Routing::Electrical::Connection::RouteLevel@endlink  enumeration instead of a string. 
    ##  @return route_level (@link Connection.RouteLevel NXOpen.Routing.Electrical.Connection.RouteLevel@endlink):  Route level. .
    ## 
    ##   <br>  Created in NX8.0.3  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def GetRoutedLevelEnum(connection: Connection) -> Connection.RouteLevel:
        """
         Similar to @link NXOpen::Routing::Electrical::Connection::GetRoutedLevel NXOpen::Routing::Electrical::Connection::GetRoutedLevel@endlink ,
                        but returns the @link NXOpen::Routing::Electrical::Connection::RouteLevel NXOpen::Routing::Electrical::Connection::RouteLevel@endlink  enumeration instead of a string. 
         @return route_level (@link Connection.RouteLevel NXOpen.Routing.Electrical.Connection.RouteLevel@endlink):  Route level. .
        """
        pass
    
    ##  Gets the method used to route this connection. 
    ##  @return routing_method (str):  <ul>
    ##                                                                     <li>"A" Connection is auto routed</li>
    ##                                                                     <li>"M" Connection is manual routed</li>
    ##                                                                     <li>"N" Connection is not routed</li>
    ##                                                                     </ul> .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def GetRoutingMethod(connection: Connection) -> str:
        """
         Gets the method used to route this connection. 
         @return routing_method (str):  <ul>
                                                                            <li>"A" Connection is auto routed</li>
                                                                            <li>"M" Connection is manual routed</li>
                                                                            <li>"N" Connection is not routed</li>
                                                                            </ul> .
        """
        pass
    
    ## 
    ##              Returns true if connection is routed externally, else returns false.
    ##             
    ##  @return is_externally_routed (bool): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced")
    @staticmethod
    def IsExternallyRouted(connection: Connection) -> bool:
        """
        
                     Returns true if connection is routed externally, else returns false.
                    
         @return is_externally_routed (bool): .
        """
        pass
    
    ##  Is this connection routed? 
    ##  @return is_routed (bool):  Is this connection routed? .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def IsRouted(connection: Connection) -> bool:
        """
         Is this connection routed? 
         @return is_routed (bool):  Is this connection routed? .
        """
        pass
    
    ##  Remove an intermediate terminal from this connection
    ##  @return result (bool):  Was the @link NXOpen::Routing::LogicalTerminal NXOpen::Routing::LogicalTerminal@endlink  removed successfully?  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  may be NULL 
    def RemoveIntermediateTerminal(connection: Connection, intermediate_terminal: NXOpen.Routing.LogicalTerminal) -> bool:
        """
         Remove an intermediate terminal from this connection
         @return result (bool):  Was the @link NXOpen::Routing::LogicalTerminal NXOpen::Routing::LogicalTerminal@endlink  removed successfully?  .
        """
        pass
    
    ##  Replaces the intermediate terminals associated with this connection. 
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  Collection of intermediate @link NXOpen::Routing::LogicalTerminal NXOpen::Routing::LogicalTerminal@endlink  - Use NULL to remove all intermdiate terminals 
    def ReplaceIntermediateTerminals(connection: Connection, intermediate_terminals: List[NXOpen.Routing.LogicalTerminal]) -> None:
        """
         Replaces the intermediate terminals associated with this connection. 
        """
        pass
    
    ##  Unroutes this connection. 
    ## 
    ##   <br>  Created in NX8.0.3  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def Unroute(connection: Connection) -> None:
        """
         Unroutes this connection. 
        """
        pass
    
import NXOpen
##  Represents a collection of @link NXOpen::Routing::Electrical::ConnectorDevice NXOpen::Routing::Electrical::ConnectorDevice@endlink  (CD) objects.   <br> To obtain an instance of this class, refer to @link NXOpen::Routing::RouteManager  NXOpen::Routing::RouteManager @endlink  <br> 
## 
##   <br>  Created in NX4.0.2  <br> 

class ConnectorDeviceCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of <ja_class>NXOpen.Routing.Electrical.ConnectorDevice</ja_class> (CD) objects.  """


    ##  Auto assignment is done using one
    ##             of the three matching methods, Part Name, Component Name or Attribute. 
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  
    def AutoAssignConnectors(object_in_part: ConnectorDeviceCollection, connectors: List[ConnectorDevice]) -> None:
        """
         Auto assignment is done using one
                    of the three matching methods, Part Name, Component Name or Attribute. 
        """
        pass
    
    ##  Creates a @link NXOpen::Routing::Electrical::ConnectorDevice NXOpen::Routing::Electrical::ConnectorDevice@endlink . 
    ##  @return connector_device (@link ConnectorDevice NXOpen.Routing.Electrical.ConnectorDevice@endlink):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  
    @overload
    def CreateConnectorDevice(self, object_in_part: ConnectorDeviceCollection, connector_type: ConnectorDevice.ComponentType, component_name: str) -> ConnectorDevice:
        """
         Creates a @link NXOpen::Routing::Electrical::ConnectorDevice NXOpen::Routing::Electrical::ConnectorDevice@endlink . 
         @return connector_device (@link ConnectorDevice NXOpen.Routing.Electrical.ConnectorDevice@endlink):  .
        """
        pass
    
    ##  Finds or Creates a @link NXOpen::Routing::Electrical::ConnectorDevice NXOpen::Routing::Electrical::ConnectorDevice@endlink  for given equipmentName and or 
    ##                 connectorName. Builds @link NXOpen::Routing::Electrical::ElectricalDeviceRelationship NXOpen::Routing::Electrical::ElectricalDeviceRelationship@endlink  between 
    ##                 equipment and connector, if equipmentName and connectorName are not NULL.
    ##                 Adds connector to harnessDevice, if connectorName and harnessDevice are not NULL. 
    ##  @return connector_device (@link ConnectorDevice NXOpen.Routing.Electrical.ConnectorDevice@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  can be NULL 
    @overload
    def CreateConnectorDevice(self, object_in_part: ConnectorDeviceCollection, harness_device: HarnessDevice, equipment_name: str, connector_name: str, connector_type: ConnectorDevice.ComponentType) -> ConnectorDevice:
        """
         Finds or Creates a @link NXOpen::Routing::Electrical::ConnectorDevice NXOpen::Routing::Electrical::ConnectorDevice@endlink  for given equipmentName and or 
                        connectorName. Builds @link NXOpen::Routing::Electrical::ElectricalDeviceRelationship NXOpen::Routing::Electrical::ElectricalDeviceRelationship@endlink  between 
                        equipment and connector, if equipmentName and connectorName are not NULL.
                        Adds connector to harnessDevice, if connectorName and harnessDevice are not NULL. 
         @return connector_device (@link ConnectorDevice NXOpen.Routing.Electrical.ConnectorDevice@endlink):  .
        """
        pass
    
    ##  Get connectors from the work part. 
    ##  @return connectors (@link ConnectorDevice List[NXOpen.Routing.Electrical.ConnectorDevice]@endlink):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def GetConnectorSingleDevices(object_in_part: ConnectorDeviceCollection) -> List[ConnectorDevice]:
        """
         Get connectors from the work part. 
         @return connectors (@link ConnectorDevice List[NXOpen.Routing.Electrical.ConnectorDevice]@endlink):  .
        """
        pass
    
    ##  Get equipment from the work part. 
    ##  @return equipment (@link ConnectorDevice List[NXOpen.Routing.Electrical.ConnectorDevice]@endlink):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def GetEquipmentSingleDevices(object_in_part: ConnectorDeviceCollection) -> List[ConnectorDevice]:
        """
         Get equipment from the work part. 
         @return equipment (@link ConnectorDevice List[NXOpen.Routing.Electrical.ConnectorDevice]@endlink):  .
        """
        pass
    
    ##  Returns Splice @link NXOpen::Routing::Electrical::ConnectorDevice NXOpen::Routing::Electrical::ConnectorDevice@endlink , based on the name provided. 
    ##  @return spliceSingleDevice (@link ConnectorDevice NXOpen.Routing.Electrical.ConnectorDevice@endlink):  .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced")
    ## 
    ## <param name="spliceName"> (str) </param>
    def GetSpliceConnectorDevice(object_in_part: ConnectorDeviceCollection, spliceName: str) -> ConnectorDevice:
        """
         Returns Splice @link NXOpen::Routing::Electrical::ConnectorDevice NXOpen::Routing::Electrical::ConnectorDevice@endlink , based on the name provided. 
         @return spliceSingleDevice (@link ConnectorDevice NXOpen.Routing.Electrical.ConnectorDevice@endlink):  .
        """
        pass
    
import NXOpen
import NXOpen.Assemblies
import NXOpen.Routing
## 
##             The Electrical ConnectorDevice corresponds to a connector instance of
##             @link NXOpen::Routing::SingleDevice NXOpen::Routing::SingleDevice@endlink .
##          <br> To create a new instance of this class, use @link NXOpen::Routing::Electrical::ConnectorDeviceCollection::CreateConnectorDevice  NXOpen::Routing::Electrical::ConnectorDeviceCollection::CreateConnectorDevice @endlink  <br> 
## 
##   <br>  Created in NX4.0.2  <br> 

class ConnectorDevice(NXOpen.Routing.SingleDevice): 
    """
            The Electrical ConnectorDevice corresponds to a connector instance of
            <ja_class>NXOpen.Routing.SingleDevice</ja_class>.
        """


    ##  Assignment method 
    ##  
    class Assign(Enum):
        """
        Members Include: <NotSet> <Auto> <Manual>
        """
        NotSet: int
        Auto: int
        Manual: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ConnectorDevice.Assign:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Component type 
    ##  
    class ComponentType(Enum):
        """
        Members Include: <NotSet> <Connector> <Splice> <Device> <Other>
        """
        NotSet: int
        Connector: int
        Splice: int
        Device: int
        Other: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ConnectorDevice.ComponentType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) ComponentName
    ##   the component name.  
    ##      
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## @return str
    @property
    def ComponentName(self) -> str:
        """
        Getter for property: (str) ComponentName
          the component name.  
             
         
        """
        pass
    
    ## Setter for property: (str) ComponentName

    ##   the component name.  
    ##      
    ##  
    ## Setter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    @ComponentName.setter
    def ComponentName(self, component_name: str):
        """
        Setter for property: (str) ComponentName
          the component name.  
             
         
        """
        pass
    
    ## Getter for property: (@link ConnectorDevice.ComponentType NXOpen.Routing.Electrical.ConnectorDevice.ComponentType@endlink) ConnectorType
    ##   the connector type.  
    ##      
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## @return ConnectorDevice.ComponentType
    @property
    def ConnectorType(self) -> ConnectorDevice.ComponentType:
        """
        Getter for property: (@link ConnectorDevice.ComponentType NXOpen.Routing.Electrical.ConnectorDevice.ComponentType@endlink) ConnectorType
          the connector type.  
             
         
        """
        pass
    
    ## Setter for property: (@link ConnectorDevice.ComponentType NXOpen.Routing.Electrical.ConnectorDevice.ComponentType@endlink) ConnectorType

    ##   the connector type.  
    ##      
    ##  
    ## Setter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    @ConnectorType.setter
    def ConnectorType(self, elec_rlist_component: ConnectorDevice.ComponentType):
        """
        Setter for property: (@link ConnectorDevice.ComponentType NXOpen.Routing.Electrical.ConnectorDevice.ComponentType@endlink) ConnectorType
          the connector type.  
             
         
        """
        pass
    
    ##  Assigns a connector to the given compoent and sets the assignment method to "automatically assigned". 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  Component to assign. 
    def AutomaticallyAssignConnector(elec_connector_device: ConnectorDevice, elec_connector_part_occurrence: NXOpen.Assemblies.Component) -> None:
        """
         Assigns a connector to the given compoent and sets the assignment method to "automatically assigned". 
        """
        pass
    
    ##  Find connections. 
    ##  @return connections (@link Connection List[NXOpen.Routing.Electrical.Connection]@endlink):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def FindConnections(elec_connector_device: ConnectorDevice) -> List[Connection]:
        """
         Find connections. 
         @return connections (@link Connection List[NXOpen.Routing.Electrical.Connection]@endlink):  .
        """
        pass
    
    ##  Find parts matching the connector device. Searches for "PART_NAME" 
    ##                 property on connector device to search for matches in the part tables
    ##                 Returns  all matching rows from the part tables. 
    ##  @return matches (@link NXOpen.Routing.CharacteristicList List[NXOpen.Routing.CharacteristicList]@endlink):  .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def FindMatchingParts(elec_connector_device: ConnectorDevice) -> List[NXOpen.Routing.CharacteristicList]:
        """
         Find parts matching the connector device. Searches for "PART_NAME" 
                        property on connector device to search for matches in the part tables
                        Returns  all matching rows from the part tables. 
         @return matches (@link NXOpen.Routing.CharacteristicList List[NXOpen.Routing.CharacteristicList]@endlink):  .
        """
        pass
    
    ##  Get the nearest @link NXOpen::Routing::Electrical::CableDevice NXOpen::Routing::Electrical::CableDevice@endlink  encountered up the parent-child hierarchy. 
    ##  @return elec_nearest_cable_device (@link CableDevice NXOpen.Routing.Electrical.CableDevice@endlink):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def FindNearestCableDevice(elec_connector_device: ConnectorDevice) -> CableDevice:
        """
         Get the nearest @link NXOpen::Routing::Electrical::CableDevice NXOpen::Routing::Electrical::CableDevice@endlink  encountered up the parent-child hierarchy. 
         @return elec_nearest_cable_device (@link CableDevice NXOpen.Routing.Electrical.CableDevice@endlink):  .
        """
        pass
    
    ##  Get the nearest @link NXOpen::Routing::Electrical::HarnessDevice NXOpen::Routing::Electrical::HarnessDevice@endlink  encountered up the parent-child hierarchy. 
    ##  @return elec_nearest_harness_device (@link HarnessDevice NXOpen.Routing.Electrical.HarnessDevice@endlink):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def FindNearestHarnessDevice(elec_connector_device: ConnectorDevice) -> HarnessDevice:
        """
         Get the nearest @link NXOpen::Routing::Electrical::HarnessDevice NXOpen::Routing::Electrical::HarnessDevice@endlink  encountered up the parent-child hierarchy. 
         @return elec_nearest_harness_device (@link HarnessDevice NXOpen.Routing.Electrical.HarnessDevice@endlink):  .
        """
        pass
    
    ##  Searches for a placement port for the connector device. The placement
    ##                 port is defined in the component list by attribute "DEVICE_PIN", 
    ##                 "EQUIPMENT_PIN", or "MODULAR_PARENT_POSITION". If the attribute is not defined,
    ##                 searches for the first available port on the relating device.
    ##             
    ##  @return A tuple consisting of (port, portPosition). 
    ##  - port is: @link NXOpen.Routing.Port NXOpen.Routing.Port@endlink.
    ##  - portPosition is: @link NXOpen.Point3d NXOpen.Point3d@endlink. The position of the port in the context of the work part. .

    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def FindPlacementPort(elec_connector_device: ConnectorDevice) -> Tuple[NXOpen.Routing.Port, NXOpen.Point3d]:
        """
         Searches for a placement port for the connector device. The placement
                        port is defined in the component list by attribute "DEVICE_PIN", 
                        "EQUIPMENT_PIN", or "MODULAR_PARENT_POSITION". If the attribute is not defined,
                        searches for the first available port on the relating device.
                    
         @return A tuple consisting of (port, portPosition). 
         - port is: @link NXOpen.Routing.Port NXOpen.Routing.Port@endlink.
         - portPosition is: @link NXOpen.Point3d NXOpen.Point3d@endlink. The position of the port in the context of the work part. .

        """
        pass
    
    ##  Find routed stock devices. 
    ##  @return routed_stock_devices (@link ElectricalStockDevice List[NXOpen.Routing.Electrical.ElectricalStockDevice]@endlink):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def FindRoutedStockDevices(elec_connector_device: ConnectorDevice) -> List[ElectricalStockDevice]:
        """
         Find routed stock devices. 
         @return routed_stock_devices (@link ElectricalStockDevice List[NXOpen.Routing.Electrical.ElectricalStockDevice]@endlink):  .
        """
        pass
    
    ##  Find stock devices. 
    ##  @return stock_devices (@link ElectricalStockDevice List[NXOpen.Routing.Electrical.ElectricalStockDevice]@endlink):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def FindStockDevices(elec_connector_device: ConnectorDevice) -> List[ElectricalStockDevice]:
        """
         Find stock devices. 
         @return stock_devices (@link ElectricalStockDevice List[NXOpen.Routing.Electrical.ElectricalStockDevice]@endlink):  .
        """
        pass
    
    ##  Get assign method. 
    ##  @return elec_connector_device_assign_method (@link ConnectorDevice.Assign NXOpen.Routing.Electrical.ConnectorDevice.Assign@endlink):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def GetAssignMethod(elec_connector_device: ConnectorDevice) -> ConnectorDevice.Assign:
        """
         Get assign method. 
         @return elec_connector_device_assign_method (@link ConnectorDevice.Assign NXOpen.Routing.Electrical.ConnectorDevice.Assign@endlink):  .
        """
        pass
    
    ##  Get part definition. 
    ##  @return elec_part_definition_shadow (@link ElectricalPartDefinitionShadow NXOpen.Routing.Electrical.ElectricalPartDefinitionShadow@endlink):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def GetPartDefinition(elec_connector_device: ConnectorDevice) -> ElectricalPartDefinitionShadow:
        """
         Get part definition. 
         @return elec_part_definition_shadow (@link ElectricalPartDefinitionShadow NXOpen.Routing.Electrical.ElectricalPartDefinitionShadow@endlink):  .
        """
        pass
    
    ##  Get @link NXOpen::Routing::LogicalTerminal NXOpen::Routing::LogicalTerminal@endlink  given the name of the terminal.
    ##                 If a terminal does not exists creates a terminal
    ##  @return terminal (@link NXOpen.Routing.LogicalTerminal NXOpen.Routing.LogicalTerminal@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  
    def GetTerminal(elec_connector_device: ConnectorDevice, terminal_name: str, create_terminal: bool) -> NXOpen.Routing.LogicalTerminal:
        """
         Get @link NXOpen::Routing::LogicalTerminal NXOpen::Routing::LogicalTerminal@endlink  given the name of the terminal.
                        If a terminal does not exists creates a terminal
         @return terminal (@link NXOpen.Routing.LogicalTerminal NXOpen.Routing.LogicalTerminal@endlink):  .
        """
        pass
    
    ##  Get terminals. 
    ##  @return route_terminals (@link NXOpen.Routing.LogicalTerminal List[NXOpen.Routing.LogicalTerminal]@endlink):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def GetTerminals(elec_connector_device: ConnectorDevice) -> List[NXOpen.Routing.LogicalTerminal]:
        """
         Get terminals. 
         @return route_terminals (@link NXOpen.Routing.LogicalTerminal List[NXOpen.Routing.LogicalTerminal]@endlink):  .
        """
        pass
    
    ##  Get status of a connector device (assigned or not). 
    ##  @return result (bool):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def IsAssigned(elec_connector_device: ConnectorDevice) -> bool:
        """
         Get status of a connector device (assigned or not). 
         @return result (bool):  .
        """
        pass
    
    ##  Is the device a connector? 
    ##  @return result (bool):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  
    def IsNxConnector(elec_connector_device: ConnectorDevice, elec_harness_device: HarnessDevice) -> bool:
        """
         Is the device a connector? 
         @return result (bool):  .
        """
        pass
    
    ##  Is the device a NX device? 
    ##  @return result (bool):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  
    def IsNxDevice(elec_connector_device: ConnectorDevice, elec_harness_device: HarnessDevice) -> bool:
        """
         Is the device a NX device? 
         @return result (bool):  .
        """
        pass
    
    ##  Is the device used in a routed connection? 
    ##  @return result (bool):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  
    def IsUsedInRoutedConnection(elec_connector_device: ConnectorDevice, elec_harness_device: HarnessDevice) -> bool:
        """
         Is the device used in a routed connection? 
         @return result (bool):  .
        """
        pass
    
    ##  Assign a connector manually. 
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  Component to assign. 
    def ManuallyAssignConnector(elec_connector_device: ConnectorDevice, elec_connector_part_occurrence: NXOpen.Assemblies.Component) -> None:
        """
         Assign a connector manually. 
        """
        pass
    
    ##  Assign a connector manually for object NXOpen.Group. 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  Component to assign. 
    def ManuallyAssignConnectorGroup(elec_connector_device: ConnectorDevice, elec_connector_group: NXOpen.Group) -> None:
        """
         Assign a connector manually for object NXOpen.Group. 
        """
        pass
    
    ##  Loads the parts based on the @link NXOpen::Routing::CharacteristicList NXOpen::Routing::CharacteristicList@endlink 
    ##                 adds the instance of the part to the current work part and places the 
    ##                 instance on the placer. 
    ##  @return nxComp (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink):  .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  
    def PlaceConnectorOnPort(elec_connector_device: ConnectorDevice, match: NXOpen.Routing.CharacteristicList, placer: NXOpen.Routing.Port) -> NXOpen.Assemblies.Component:
        """
         Loads the parts based on the @link NXOpen::Routing::CharacteristicList NXOpen::Routing::CharacteristicList@endlink 
                        adds the instance of the part to the current work part and places the 
                        instance on the placer. 
         @return nxComp (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink):  .
        """
        pass
    
    ##  Assign a connector to a proxy port. 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  Assigned port. 
    def ProxyAssignConnector(elec_connector_device: ConnectorDevice, proxy: NXOpen.Routing.Port) -> None:
        """
         Assign a connector to a proxy port. 
        """
        pass
    
    ##  Remove a terminal. 
    ##  @return result (bool):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  
    def RemoveTerminal(elec_connector_device: ConnectorDevice, route_terminal_to_remove: NXOpen.Routing.LogicalTerminal) -> bool:
        """
         Remove a terminal. 
         @return result (bool):  .
        """
        pass
    
    ##  Sets part definition. 
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  
    def SetPartDefinition(elec_connector_device: ConnectorDevice, elec_part_definition_shadow: ElectricalPartDefinitionShadow) -> None:
        """
         Sets part definition. 
        """
        pass
    
    ##  Unassign connector. 
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def UnassignConnector(elec_connector_device: ConnectorDevice) -> None:
        """
         Unassign connector. 
        """
        pass
    
##  Represents a @link NXOpen::Routing::Electrical::DerivativeDefinition NXOpen::Routing::Electrical::DerivativeDefinition@endlink   <br> Creator not available in KF.  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class DerivativeDefinition(HarnessDefinition): 
    """ Represents a <ja_class>NXOpen.Routing.Electrical.DerivativeDefinition</ja_class> """
    pass


import NXOpen
##  Represents a collection of @link Routing::Electrical::DerivativeDevice Routing::Electrical::DerivativeDevice@endlink  objects.   <br> To obtain an instance of this class, refer to @link NXOpen::Routing::RouteManager  NXOpen::Routing::RouteManager @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class DerivativeDeviceCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of <ja_class>Routing.Electrical.DerivativeDevice</ja_class> objects.  """


    ##  Creates @link Routing::Electrical::DerivativeDevice Routing::Electrical::DerivativeDevice@endlink  with given name. 
    ##  @return derivative_device (@link DerivativeDevice NXOpen.Routing.Electrical.DerivativeDevice@endlink):  .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    def CreateDerivativeDevice(object_in_part: DerivativeDeviceCollection) -> DerivativeDevice:
        """
         Creates @link Routing::Electrical::DerivativeDevice Routing::Electrical::DerivativeDevice@endlink  with given name. 
         @return derivative_device (@link DerivativeDevice NXOpen.Routing.Electrical.DerivativeDevice@endlink):  .
        """
        pass
    
    ##  Get derivatives 
    ##  @return derivatives (@link DerivativeDevice List[NXOpen.Routing.Electrical.DerivativeDevice]@endlink):  .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def GetDerivativeSingleDevices(object_in_part: DerivativeDeviceCollection) -> List[DerivativeDevice]:
        """
         Get derivatives 
         @return derivatives (@link DerivativeDevice List[NXOpen.Routing.Electrical.DerivativeDevice]@endlink):  .
        """
        pass
    
## 
##             The Electrical DerivativeDevice corresponds to a derivative instance of the 
##             @link Routing::Electrical::HarnessDevice Routing::Electrical::HarnessDevice@endlink .
##          <br> To create a new instance of this class, use @link NXOpen::Routing::Electrical::DerivativeDeviceCollection::CreateDerivativeDevice  NXOpen::Routing::Electrical::DerivativeDeviceCollection::CreateDerivativeDevice @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class DerivativeDevice(HarnessDevice): 
    """
            The Electrical DerivativeDevice corresponds to a derivative instance of the 
            <ja_class>Routing.Electrical.HarnessDevice</ja_class>.
        """


    ##  Get derivative definition. 
    ##  @return elec_derivative_definition (@link DerivativeDefinition NXOpen.Routing.Electrical.DerivativeDefinition@endlink):  .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def GetDerivativeDefinition(elec_derivative_device: DerivativeDevice) -> DerivativeDefinition:
        """
         Get derivative definition. 
         @return elec_derivative_definition (@link DerivativeDefinition NXOpen.Routing.Electrical.DerivativeDefinition@endlink):  .
        """
        pass
    
import NXOpen
##  @brief 
##              Represents a collection of @link NXOpen::Routing::Electrical::ElectricalDeviceRelationship NXOpen::Routing::Electrical::ElectricalDeviceRelationship@endlink  objects.
##             
## 
##  
##          <br> To obtain an instance of this class, refer to @link NXOpen::Routing::RouteManager  NXOpen::Routing::RouteManager @endlink  <br> 
## 
##   <br>  Created in NX4.0.2  <br> 

class ElectricalDeviceRelationshipCollection(NXOpen.TaggedObjectCollection): 
    """<summary>
             Represents a collection of <ja_class>NXOpen.Routing.Electrical.ElectricalDeviceRelationship</ja_class> objects.
           </summary>
        """


    ##  Creates a @link NXOpen::Routing::Electrical::ElectricalDeviceRelationship NXOpen::Routing::Electrical::ElectricalDeviceRelationship@endlink  object. 
    ##  @return electrical_device_relationship (@link ElectricalDeviceRelationship NXOpen.Routing.Electrical.ElectricalDeviceRelationship@endlink):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    def CreateElectricalDeviceRelationship(object_in_part: ElectricalDeviceRelationshipCollection) -> ElectricalDeviceRelationship:
        """
         Creates a @link NXOpen::Routing::Electrical::ElectricalDeviceRelationship NXOpen::Routing::Electrical::ElectricalDeviceRelationship@endlink  object. 
         @return electrical_device_relationship (@link ElectricalDeviceRelationship NXOpen.Routing.Electrical.ElectricalDeviceRelationship@endlink):  .
        """
        pass
    
import NXOpen.Routing
##  @brief 
##              Represents a relationship between Routing Electrical devices.
##             
## 
##  
##             <br> 
##              Use this class to associate electrical connectors to electrical equipment outside of a harness.
##             <br>  
##             @code 
##             (example)
##                 Use an ElectricalDeviceRelationship to represent connectors C1 and C2 mounted on a piece of equipment, D1.
##                 The Relating object is D1 and the Related objects are C1 and C2.
##             @endcode 
##          <br> To create a new instance of this class, use @link NXOpen::Routing::Electrical::ElectricalDeviceRelationshipCollection::CreateElectricalDeviceRelationship  NXOpen::Routing::Electrical::ElectricalDeviceRelationshipCollection::CreateElectricalDeviceRelationship @endlink  <br> 
## 
##   <br>  Created in NX4.0.2  <br> 

class ElectricalDeviceRelationship(NXOpen.Routing.DeviceRelationship): 
    """<summary>
             Represents a relationship between Routing Electrical devices.
           </summary>
           <para>
             Use this class to associate electrical connectors to electrical equipment outside of a harness.
           </para> 
           <code>
            (example)
                Use an ElectricalDeviceRelationship to represent connectors C1 and C2 mounted on a piece of equipment, D1.
                The Relating object is D1 and the Related objects are C1 and C2.
           </code>
        """
    pass


import NXOpen
##  Represents a Routing @link NXOpen::Routing::Electrical::ElectricalFormatCollection NXOpen::Routing::Electrical::ElectricalFormatCollection@endlink  object.
##           <br> To obtain an instance of this class, refer to @link NXOpen::Routing::RouteManager  NXOpen::Routing::RouteManager @endlink  <br> 
## 
##   <br>  Created in NX5.0.1  <br> 

class ElectricalFormatCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a Routing <ja_class>NXOpen.Routing.Electrical.ElectricalFormatCollection</ja_class> object.
         """


    ##  Creates a @link NXOpen::Routing::Electrical::ElectricalFormat NXOpen::Routing::Electrical::ElectricalFormat@endlink  object. 
    ##  @return format (@link ElectricalFormat NXOpen.Routing.Electrical.ElectricalFormat@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.1  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  
    def CreateFormat(object_in_part: ElectricalFormatCollection, name: str, type: ElectricalFormat.Type) -> ElectricalFormat:
        """
         Creates a @link NXOpen::Routing::Electrical::ElectricalFormat NXOpen::Routing::Electrical::ElectricalFormat@endlink  object. 
         @return format (@link ElectricalFormat NXOpen.Routing.Electrical.ElectricalFormat@endlink):  .
        """
        pass
    
    ##  Get the displayed @link NXOpen::Routing::Electrical::ElectricalFormat NXOpen::Routing::Electrical::ElectricalFormat@endlink  object for the
    ##                 given navigator type. 
    ##  @return format (@link ElectricalFormat NXOpen.Routing.Electrical.ElectricalFormat@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.1  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  
    def GetDisplayFormat(object_in_part: ElectricalFormatCollection, type: ElectricalFormat.Type) -> ElectricalFormat:
        """
         Get the displayed @link NXOpen::Routing::Electrical::ElectricalFormat NXOpen::Routing::Electrical::ElectricalFormat@endlink  object for the
                        given navigator type. 
         @return format (@link ElectricalFormat NXOpen.Routing.Electrical.ElectricalFormat@endlink):  .
        """
        pass
    
    ##  Set the @link NXOpen::Routing::Electrical::ElectricalFormat NXOpen::Routing::Electrical::ElectricalFormat@endlink  object as displayed
    ##                 format for the given navigator type. 
    ## 
    ##   <br>  Created in NX5.0.1  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  
    def SetDisplayFormat(object_in_part: ElectricalFormatCollection, type: ElectricalFormat.Type, format: ElectricalFormat) -> None:
        """
         Set the @link NXOpen::Routing::Electrical::ElectricalFormat NXOpen::Routing::Electrical::ElectricalFormat@endlink  object as displayed
                        format for the given navigator type. 
        """
        pass
    
import NXOpen
##  Represents a Routing Electrical ElectricalFormat.
##           <br> To create an  instance of this class use @link NXOpen::Routing::Electrical::ElectricalFormatCollection NXOpen::Routing::Electrical::ElectricalFormatCollection@endlink   <br> 
## 
##   <br>  Created in NX5.0.1  <br> 

class ElectricalFormat(NXOpen.TaggedObject): 
    """ Represents a Routing Electrical ElectricalFormat.
         """


    ##  Describes how system reports the lengths of the stock. 
    ##  
    class Type(Enum):
        """
        Members Include: <Connections> <Components>
        """
        Connections: int
        Components: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ElectricalFormat.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link ElectricalFormat.Type NXOpen.Routing.Electrical.ElectricalFormat.Type@endlink) FormatType
    ##   the type of @link NXOpen::Routing::Electrical::ElectricalFormat NXOpen::Routing::Electrical::ElectricalFormat@endlink    
    ##     
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX5.0.1  <br> 

    ## @return ElectricalFormat.Type
    @property
    def FormatType(self) -> ElectricalFormat.Type:
        """
        Getter for property: (@link ElectricalFormat.Type NXOpen.Routing.Electrical.ElectricalFormat.Type@endlink) FormatType
          the type of @link NXOpen::Routing::Electrical::ElectricalFormat NXOpen::Routing::Electrical::ElectricalFormat@endlink    
            
         
        """
        pass
    
    ## Setter for property: (@link ElectricalFormat.Type NXOpen.Routing.Electrical.ElectricalFormat.Type@endlink) FormatType

    ##   the type of @link NXOpen::Routing::Electrical::ElectricalFormat NXOpen::Routing::Electrical::ElectricalFormat@endlink    
    ##     
    ##  
    ## Setter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX5.0.1  <br> 

    @FormatType.setter
    def FormatType(self, type: ElectricalFormat.Type):
        """
        Setter for property: (@link ElectricalFormat.Type NXOpen.Routing.Electrical.ElectricalFormat.Type@endlink) FormatType
          the type of @link NXOpen::Routing::Electrical::ElectricalFormat NXOpen::Routing::Electrical::ElectricalFormat@endlink    
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the name of @link NXOpen::Routing::Electrical::ElectricalFormat NXOpen::Routing::Electrical::ElectricalFormat@endlink    
    ##     
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX5.0.1  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the name of @link NXOpen::Routing::Electrical::ElectricalFormat NXOpen::Routing::Electrical::ElectricalFormat@endlink    
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the name of @link NXOpen::Routing::Electrical::ElectricalFormat NXOpen::Routing::Electrical::ElectricalFormat@endlink    
    ##     
    ##  
    ## Setter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX5.0.1  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
          the name of @link NXOpen::Routing::Electrical::ElectricalFormat NXOpen::Routing::Electrical::ElectricalFormat@endlink    
            
         
        """
        pass
    
import NXOpen
##  Represents a Routing @link NXOpen::Routing::Electrical::ElectricalNavigatorFilterCollection NXOpen::Routing::Electrical::ElectricalNavigatorFilterCollection@endlink  object.
##           <br> To obtain an instance of this class, refer to @link NXOpen::Routing::RouteManager  NXOpen::Routing::RouteManager @endlink  <br> 
## 
##   <br>  Created in NX5.0.1  <br> 

class ElectricalNavigatorFilterCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a Routing <ja_class>NXOpen.Routing.Electrical.ElectricalNavigatorFilterCollection</ja_class> object.
         """


    ##  Creates a @link NXOpen::Routing::Electrical::ElectricalNavigatorFilter NXOpen::Routing::Electrical::ElectricalNavigatorFilter@endlink  object. 
    ##  @return filter (@link ElectricalNavigatorFilter NXOpen.Routing.Electrical.ElectricalNavigatorFilter@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.1  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  Name of the filter 
    def CreateFilter(object_in_part: ElectricalNavigatorFilterCollection, name: str, clause: str) -> ElectricalNavigatorFilter:
        """
         Creates a @link NXOpen::Routing::Electrical::ElectricalNavigatorFilter NXOpen::Routing::Electrical::ElectricalNavigatorFilter@endlink  object. 
         @return filter (@link ElectricalNavigatorFilter NXOpen.Routing.Electrical.ElectricalNavigatorFilter@endlink):  .
        """
        pass
    
    ##  Get the displayed @link NXOpen::Routing::Electrical::ElectricalNavigatorFilter NXOpen::Routing::Electrical::ElectricalNavigatorFilter@endlink  object
    ##                 for the given navigator type 
    ##  @return filter (@link ElectricalNavigatorFilter NXOpen.Routing.Electrical.ElectricalNavigatorFilter@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.1  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  
    def GetDisplayFilter(object_in_part: ElectricalNavigatorFilterCollection, type: ElectricalFormat.Type) -> ElectricalNavigatorFilter:
        """
         Get the displayed @link NXOpen::Routing::Electrical::ElectricalNavigatorFilter NXOpen::Routing::Electrical::ElectricalNavigatorFilter@endlink  object
                        for the given navigator type 
         @return filter (@link ElectricalNavigatorFilter NXOpen.Routing.Electrical.ElectricalNavigatorFilter@endlink):  .
        """
        pass
    
    ##  Set the @link NXOpen::Routing::Electrical::ElectricalNavigatorFilter NXOpen::Routing::Electrical::ElectricalNavigatorFilter@endlink  object as 
    ##                 displayed filter for given navigator type. 
    ## 
    ##   <br>  Created in NX5.0.1  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  
    def SetDisplayFilter(object_in_part: ElectricalNavigatorFilterCollection, type: ElectricalFormat.Type, filter: ElectricalNavigatorFilter) -> None:
        """
         Set the @link NXOpen::Routing::Electrical::ElectricalNavigatorFilter NXOpen::Routing::Electrical::ElectricalNavigatorFilter@endlink  object as 
                        displayed filter for given navigator type. 
        """
        pass
    
import NXOpen
##  Represents a Routing Electrical Navigator Filter object.
##           <br> To create an  instance of this class use @link NXOpen::Routing::Electrical::ElectricalNavigatorFilterCollection NXOpen::Routing::Electrical::ElectricalNavigatorFilterCollection@endlink   <br> 
## 
##   <br>  Created in NX5.0.1  <br> 

class ElectricalNavigatorFilter(NXOpen.NavigatorFilter): 
    """ Represents a Routing Electrical Navigator Filter object.
         """
    pass


import NXOpen.Routing
##  Represents @link NXOpen::Routing::Electrical::ElectricalPartDefinitionShadow NXOpen::Routing::Electrical::ElectricalPartDefinitionShadow@endlink  object  <br> Creator not available in KF.  <br> 
## 
##   <br>  Created in NX4.0.2  <br> 

class ElectricalPartDefinitionShadow(NXOpen.Routing.PartDefinitionShadow): 
    """ Represents <ja_class>NXOpen.Routing.Electrical.ElectricalPartDefinitionShadow</ja_class> object """
    pass


import NXOpen.Routing
##  Represents @link NXOpen::Routing::Electrical::ElectricalStockDefinition NXOpen::Routing::Electrical::ElectricalStockDefinition@endlink  object  <br> Creator not available in KF.  <br> 
## 
##   <br>  Created in NX4.0.2  <br> 

class ElectricalStockDefinition(NXOpen.Routing.StockDefinition): 
    """ Represents <ja_class>NXOpen.Routing.Electrical.ElectricalStockDefinition</ja_class> object """


    ##  Stock section type. 
    ##  
    class SectionType(Enum):
        """
        Members Include: <Circular> <Rectangular>
        """
        Circular: int
        Rectangular: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ElectricalStockDefinition.SectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link ElectricalStockDefinition.SectionType NXOpen.Routing.Electrical.ElectricalStockDefinition.SectionType@endlink) CrossSectionType
    ##    the cross section type of stock   
    ##     
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## @return ElectricalStockDefinition.SectionType
    @property
    def CrossSectionType(self) -> ElectricalStockDefinition.SectionType:
        """
        Getter for property: (@link ElectricalStockDefinition.SectionType NXOpen.Routing.Electrical.ElectricalStockDefinition.SectionType@endlink) CrossSectionType
           the cross section type of stock   
            
         
        """
        pass
    
    ## Setter for property: (@link ElectricalStockDefinition.SectionType NXOpen.Routing.Electrical.ElectricalStockDefinition.SectionType@endlink) CrossSectionType

    ##    the cross section type of stock   
    ##     
    ##  
    ## Setter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @CrossSectionType.setter
    def CrossSectionType(self, sectionType: ElectricalStockDefinition.SectionType):
        """
        Setter for property: (@link ElectricalStockDefinition.SectionType NXOpen.Routing.Electrical.ElectricalStockDefinition.SectionType@endlink) CrossSectionType
           the cross section type of stock   
            
         
        """
        pass
    
    ## Getter for property: (float) Gauge
    ##    the gauge of stock   
    ##     
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## @return float
    @property
    def Gauge(self) -> float:
        """
        Getter for property: (float) Gauge
           the gauge of stock   
            
         
        """
        pass
    
    ## Setter for property: (float) Gauge

    ##    the gauge of stock   
    ##     
    ##  
    ## Setter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Gauge.setter
    def Gauge(self, gaugeValue: float):
        """
        Setter for property: (float) Gauge
           the gauge of stock   
            
         
        """
        pass
    
    ## Getter for property: (float) Height
    ##    the height of stock   
    ##     
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## @return float
    @property
    def Height(self) -> float:
        """
        Getter for property: (float) Height
           the height of stock   
            
         
        """
        pass
    
    ## Setter for property: (float) Height

    ##    the height of stock   
    ##     
    ##  
    ## Setter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Height.setter
    def Height(self, heightValue: float):
        """
        Setter for property: (float) Height
           the height of stock   
            
         
        """
        pass
    
    ## Getter for property: (float) LinearDensity
    ##    the linear density of stock    
    ##     
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## @return float
    @property
    def LinearDensity(self) -> float:
        """
        Getter for property: (float) LinearDensity
           the linear density of stock    
            
         
        """
        pass
    
    ## Setter for property: (float) LinearDensity

    ##    the linear density of stock    
    ##     
    ##  
    ## Setter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @LinearDensity.setter
    def LinearDensity(self, densityValue: float):
        """
        Setter for property: (float) LinearDensity
           the linear density of stock    
            
         
        """
        pass
    
    ## Getter for property: (float) MinBendRadius
    ##    the min bend radius of stock   
    ##     
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## @return float
    @property
    def MinBendRadius(self) -> float:
        """
        Getter for property: (float) MinBendRadius
           the min bend radius of stock   
            
         
        """
        pass
    
    ## Setter for property: (float) MinBendRadius

    ##    the min bend radius of stock   
    ##     
    ##  
    ## Setter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @MinBendRadius.setter
    def MinBendRadius(self, radiusValue: float):
        """
        Setter for property: (float) MinBendRadius
           the min bend radius of stock   
            
         
        """
        pass
    
    ## Getter for property: (float) Width
    ##   the width of stock   
    ##     
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## @return float
    @property
    def Width(self) -> float:
        """
        Getter for property: (float) Width
          the width of stock   
            
         
        """
        pass
    
    ## Setter for property: (float) Width

    ##   the width of stock   
    ##     
    ##  
    ## Setter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Width.setter
    def Width(self, widthValue: float):
        """
        Setter for property: (float) Width
          the width of stock   
            
         
        """
        pass
    
    ## Getter for property: (str) WireType
    ##    the wire type of stock   
    ##     
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## @return str
    @property
    def WireType(self) -> str:
        """
        Getter for property: (str) WireType
           the wire type of stock   
            
         
        """
        pass
    
    ## Setter for property: (str) WireType

    ##    the wire type of stock   
    ##     
    ##  
    ## Setter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @WireType.setter
    def WireType(self, wireType: str):
        """
        Setter for property: (str) WireType
           the wire type of stock   
            
         
        """
        pass
    
import NXOpen
##  Represents a collection of @link NXOpen::Routing::Electrical::ElectricalStockDevice NXOpen::Routing::Electrical::ElectricalStockDevice@endlink  (ESD) objects.   <br> To obtain an instance of this class, refer to @link NXOpen::Routing::RouteManager  NXOpen::Routing::RouteManager @endlink  <br> 
## 
##   <br>  Created in NX4.0.2  <br> 

class ElectricalStockDeviceCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of <ja_class>NXOpen.Routing.Electrical.ElectricalStockDevice</ja_class> (ESD) objects.  """


    ##  Assign @link NXOpen::Routing::Stock NXOpen::Routing::Stock@endlink  to input stock devices.
    ##                 The assigned @link NXOpen::Routing::Stock NXOpen::Routing::Stock@endlink  is a bundle stock,
    ##                 and the routine will perform the bundling calculations. This routine
    ##                 should also be called after performing @link NXOpen::Routing::Electrical::ElectricalStockDevice::ManuallyRoute NXOpen::Routing::Electrical::ElectricalStockDevice::ManuallyRoute@endlink . 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  
    def AssignStock(object_part: ElectricalStockDeviceCollection, stock_devices: List[ElectricalStockDevice], route_type: ElectricalStockDevice.RouteTypes) -> None:
        """
         Assign @link NXOpen::Routing::Stock NXOpen::Routing::Stock@endlink  to input stock devices.
                        The assigned @link NXOpen::Routing::Stock NXOpen::Routing::Stock@endlink  is a bundle stock,
                        and the routine will perform the bundling calculations. This routine
                        should also be called after performing @link NXOpen::Routing::Electrical::ElectricalStockDevice::ManuallyRoute NXOpen::Routing::Electrical::ElectricalStockDevice::ManuallyRoute@endlink . 
        """
        pass
    
    ##  Automatically routes all of the stock devices in the work part. Routing can be done
    ##                 on pin, component or mixed level and it is based on shortest length
    ##                 (See @link NXOpen::Routing::Electrical::ElectricalStockDevice NXOpen::Routing::Electrical::ElectricalStockDevice@endlink  for more details). 
    ##  @return A tuple consisting of (no_of_routed_stock_devices, error_list). 
    ##  - no_of_routed_stock_devices is: int. .
    ##  - error_list is: @link NXOpen.ErrorList NXOpen.ErrorList@endlink. Any errors that occurred during Automatic Routing. .

    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  
    @staticmethod
    def AutoRouteAll(object_part: ElectricalStockDeviceCollection, route_level: ElectricalStockDevice.RouteLevel, route_sel: ElectricalStockDevice.AutoRouteSel) -> Tuple[int, NXOpen.ErrorList]:
        """
         Automatically routes all of the stock devices in the work part. Routing can be done
                        on pin, component or mixed level and it is based on shortest length
                        (See @link NXOpen::Routing::Electrical::ElectricalStockDevice NXOpen::Routing::Electrical::ElectricalStockDevice@endlink  for more details). 
         @return A tuple consisting of (no_of_routed_stock_devices, error_list). 
         - no_of_routed_stock_devices is: int. .
         - error_list is: @link NXOpen.ErrorList NXOpen.ErrorList@endlink. Any errors that occurred during Automatic Routing. .

        """
        pass
    
    ##  Automatically routes the selected stock devices. Routing can be done
    ##                 on pin, component or mixed level and it is based on shortest length
    ##                 (See @link NXOpen::Routing::Electrical::ElectricalStockDevice NXOpen::Routing::Electrical::ElectricalStockDevice@endlink  for more details). 
    ##  @return A tuple consisting of (no_of_routed_stock_devices, error_list). 
    ##  - no_of_routed_stock_devices is: int. .
    ##  - error_list is: @link NXOpen.ErrorList NXOpen.ErrorList@endlink. Any errors that occurred during Automatic Routing. .

    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  
    @staticmethod
    def AutoRouteConnections(object_part: ElectricalStockDeviceCollection, route_level: ElectricalStockDevice.RouteLevel, route_sel: ElectricalStockDevice.AutoRouteSel, stock_devices: List[ElectricalStockDevice]) -> Tuple[int, NXOpen.ErrorList]:
        """
         Automatically routes the selected stock devices. Routing can be done
                        on pin, component or mixed level and it is based on shortest length
                        (See @link NXOpen::Routing::Electrical::ElectricalStockDevice NXOpen::Routing::Electrical::ElectricalStockDevice@endlink  for more details). 
         @return A tuple consisting of (no_of_routed_stock_devices, error_list). 
         - no_of_routed_stock_devices is: int. .
         - error_list is: @link NXOpen.ErrorList NXOpen.ErrorList@endlink. Any errors that occurred during Automatic Routing. .

        """
        pass
    
    ##  Returns the electrical stock devices in part. 
    ##  @return stockDevices (@link ElectricalStockDevice List[NXOpen.Routing.Electrical.ElectricalStockDevice]@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def GetElectricalStockDevicesInPart(object_part: ElectricalStockDeviceCollection) -> List[ElectricalStockDevice]:
        """
         Returns the electrical stock devices in part. 
         @return stockDevices (@link ElectricalStockDevice List[NXOpen.Routing.Electrical.ElectricalStockDevice]@endlink): .
        """
        pass
    
    ##  Removes @link NXOpen::Routing::Stock NXOpen::Routing::Stock@endlink  from input stock devices.
    ##                 Removes all segments from input wires and updates harnesses associated 
    ##                 to wires, resizes and rebuilds bundle stocks for those harnesses. Deletes
    ##                 the @link NXOpen::Routing::Wire NXOpen::Routing::Wire@endlink . 
    ##  @return removed_stock_devices (@link ElectricalStockDevice List[NXOpen.Routing.Electrical.ElectricalStockDevice]@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  
    def RemoveStock(object_part: ElectricalStockDeviceCollection, stock_devices: List[ElectricalStockDevice]) -> List[ElectricalStockDevice]:
        """
         Removes @link NXOpen::Routing::Stock NXOpen::Routing::Stock@endlink  from input stock devices.
                        Removes all segments from input wires and updates harnesses associated 
                        to wires, resizes and rebuilds bundle stocks for those harnesses. Deletes
                        the @link NXOpen::Routing::Wire NXOpen::Routing::Wire@endlink . 
         @return removed_stock_devices (@link ElectricalStockDevice List[NXOpen.Routing.Electrical.ElectricalStockDevice]@endlink):  .
        """
        pass
    
    ##  Removes all bundle @link NXOpen::Routing::Stock NXOpen::Routing::Stock@endlink  from input stock devices.
    ##                 Removes all segments from input wires and updates harnesses associated 
    ##                 to wires, resizes and rebuilds bundle stocks for those harnesses. Deletes
    ##                 the @link NXOpen::Routing::Wire NXOpen::Routing::Wire@endlink . Use this when no rebundling is 
    ##                 necessary 
    ##  @return removed_stock_devices (@link ElectricalStockDevice List[NXOpen.Routing.Electrical.ElectricalStockDevice]@endlink):  .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  
    def Unroute(object_part: ElectricalStockDeviceCollection, stock_devices: List[ElectricalStockDevice]) -> List[ElectricalStockDevice]:
        """
         Removes all bundle @link NXOpen::Routing::Stock NXOpen::Routing::Stock@endlink  from input stock devices.
                        Removes all segments from input wires and updates harnesses associated 
                        to wires, resizes and rebuilds bundle stocks for those harnesses. Deletes
                        the @link NXOpen::Routing::Wire NXOpen::Routing::Wire@endlink . Use this when no rebundling is 
                        necessary 
         @return removed_stock_devices (@link ElectricalStockDevice List[NXOpen.Routing.Electrical.ElectricalStockDevice]@endlink):  .
        """
        pass
    
    ##  Removes all bundle @link NXOpen::Routing::Stock NXOpen::Routing::Stock@endlink  from all stock devices.
    ##                 Removes all segments from input wires and updates harnesses associated 
    ##                 to wires, resizes and rebuilds bundle stocks for those harnesses. Deletes
    ##                 the @link NXOpen::Routing::Wire NXOpen::Routing::Wire@endlink . Use this when no rebundling is 
    ##                 necessary 
    ##  @return removed_stock_devices (@link ElectricalStockDevice List[NXOpen.Routing.Electrical.ElectricalStockDevice]@endlink):  .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def UnrouteAll(object_part: ElectricalStockDeviceCollection) -> List[ElectricalStockDevice]:
        """
         Removes all bundle @link NXOpen::Routing::Stock NXOpen::Routing::Stock@endlink  from all stock devices.
                        Removes all segments from input wires and updates harnesses associated 
                        to wires, resizes and rebuilds bundle stocks for those harnesses. Deletes
                        the @link NXOpen::Routing::Wire NXOpen::Routing::Wire@endlink . Use this when no rebundling is 
                        necessary 
         @return removed_stock_devices (@link ElectricalStockDevice List[NXOpen.Routing.Electrical.ElectricalStockDevice]@endlink):  .
        """
        pass
    
import NXOpen.Routing
## 
##            The Electrical Stock Device is a non instantiable superclass to classify
##            all electrical stock-based single devices.
##          <br> Creator not available in KF.  <br> 
## 
##   <br>  Created in NX4.0.2  <br> 

class ElectricalStockDevice(NXOpen.Routing.StockDevice): 
    """
           The Electrical Stock Device is a non instantiable superclass to classify
           all electrical stock-based single devices.
        """


    ##  Auto-route selections. 
    ##  
    class AutoRouteSel(Enum):
        """
        Members Include: <BundleDiameter> <LeastBundles> <DesignRules> <LeastSegments> <ShortestLength>
        """
        BundleDiameter: int
        LeastBundles: int
        DesignRules: int
        LeastSegments: int
        ShortestLength: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ElectricalStockDevice.AutoRouteSel:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Routing level. 
    ##  
    class RouteLevel(Enum):
        """
        Members Include: <Pin> <Comp> <Mixed> <Partial>
        """
        Pin: int
        Comp: int
        Mixed: int
        Partial: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ElectricalStockDevice.RouteLevel:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Route types (manual/auto). 
    ##  
    class RouteTypes(Enum):
        """
        Members Include: <DefaultRoute> <AutoRoute> <ManualRoute>
        """
        DefaultRoute: int
        AutoRoute: int
        ManualRoute: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ElectricalStockDevice.RouteTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) ColorName
    ##   the color name.  
    ##      
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## @return str
    @property
    def ColorName(self) -> str:
        """
        Getter for property: (str) ColorName
          the color name.  
             
         
        """
        pass
    
    ## Setter for property: (str) ColorName

    ##   the color name.  
    ##      
    ##  
    ## Setter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    @ColorName.setter
    def ColorName(self, color_name: str):
        """
        Setter for property: (str) ColorName
          the color name.  
             
         
        """
        pass
    
    ## Getter for property: (float) CutLength
    ##   the cut length.  
    ##      
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## @return float
    @property
    def CutLength(self) -> float:
        """
        Getter for property: (float) CutLength
          the cut length.  
             
         
        """
        pass
    
    ## Setter for property: (float) CutLength

    ##   the cut length.  
    ##      
    ##  
    ## Setter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    @CutLength.setter
    def CutLength(self, cut_length: float):
        """
        Setter for property: (float) CutLength
          the cut length.  
             
         
        """
        pass
    
    ## Getter for property: (int) NxColorValue
    ##   the NX color value.  
    ##      
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## @return int
    @property
    def NxColorValue(self) -> int:
        """
        Getter for property: (int) NxColorValue
          the NX color value.  
             
         
        """
        pass
    
    ## Setter for property: (int) NxColorValue

    ##   the NX color value.  
    ##      
    ##  
    ## Setter License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    @NxColorValue.setter
    def NxColorValue(self, nx_color_value: int):
        """
        Setter for property: (int) NxColorValue
          the NX color value.  
             
         
        """
        pass
    
    ##  Calculates and sets cut length on object. 
    ##  @return cut_length (float):  Calculated cut length .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def CalculateCutLength(elec_stock_device: ElectricalStockDevice) -> float:
        """
         Calculates and sets cut length on object. 
         @return cut_length (float):  Calculated cut length .
        """
        pass
    
    ##  Adds this stockdevice as child of given HarnessDevice. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  
    def ChangeHarness(elec_stock_device: ElectricalStockDevice, harness_device: HarnessDevice) -> None:
        """
         Adds this stockdevice as child of given HarnessDevice. 
        """
        pass
    
    ##  Find the from connector for this stock device. If there is no
    ##             from connector, NULL is returned. 
    ##  @return from_connector (@link ConnectorDevice NXOpen.Routing.Electrical.ConnectorDevice@endlink):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def FindFromConnector(elec_stock_device: ElectricalStockDevice) -> ConnectorDevice:
        """
         Find the from connector for this stock device. If there is no
                    from connector, NULL is returned. 
         @return from_connector (@link ConnectorDevice NXOpen.Routing.Electrical.ConnectorDevice@endlink):  .
        """
        pass
    
    ##  Find the @link NXOpen::Routing::Electrical::Connection NXOpen::Routing::Electrical::Connection@endlink  implemented by this device. 
    ##  @return implemented_connection (@link Connection NXOpen.Routing.Electrical.Connection@endlink):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def FindImplementedConnection(elec_stock_device: ElectricalStockDevice) -> Connection:
        """
         Find the @link NXOpen::Routing::Electrical::Connection NXOpen::Routing::Electrical::Connection@endlink  implemented by this device. 
         @return implemented_connection (@link Connection NXOpen.Routing.Electrical.Connection@endlink):  .
        """
        pass
    
    ##  Get nearest @link NXOpen::Routing::Electrical::HarnessDefinition NXOpen::Routing::Electrical::HarnessDefinition@endlink  encountered up the parent-child hierarchy. 
    ##  @return elec_harness_definition (@link HarnessDefinition NXOpen.Routing.Electrical.HarnessDefinition@endlink):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def FindNearestHarnessDefinition(elec_stock_device: ElectricalStockDevice) -> HarnessDefinition:
        """
         Get nearest @link NXOpen::Routing::Electrical::HarnessDefinition NXOpen::Routing::Electrical::HarnessDefinition@endlink  encountered up the parent-child hierarchy. 
         @return elec_harness_definition (@link HarnessDefinition NXOpen.Routing.Electrical.HarnessDefinition@endlink):  .
        """
        pass
    
    ##  Find the nearest @link NXOpen::Routing::Electrical::HarnessDevice NXOpen::Routing::Electrical::HarnessDevice@endlink  encountered up the parent-child hierarchy. 
    ##  @return elec_harness_device (@link HarnessDevice NXOpen.Routing.Electrical.HarnessDevice@endlink):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def FindNearestHarnessDevice(elec_stock_device: ElectricalStockDevice) -> HarnessDevice:
        """
         Find the nearest @link NXOpen::Routing::Electrical::HarnessDevice NXOpen::Routing::Electrical::HarnessDevice@endlink  encountered up the parent-child hierarchy. 
         @return elec_harness_device (@link HarnessDevice NXOpen.Routing.Electrical.HarnessDevice@endlink):  .
        """
        pass
    
    ##  Find the to connector for this stock device. If there is no
    ##             to connector, NULL is returned. 
    ##  @return to_connector (@link ConnectorDevice NXOpen.Routing.Electrical.ConnectorDevice@endlink):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def FindToConnector(elec_stock_device: ElectricalStockDevice) -> ConnectorDevice:
        """
         Find the to connector for this stock device. If there is no
                    to connector, NULL is returned. 
         @return to_connector (@link ConnectorDevice NXOpen.Routing.Electrical.ConnectorDevice@endlink):  .
        """
        pass
    
    ##  Get topmost @link NXOpen::Routing::Electrical::CableDefinition NXOpen::Routing::Electrical::CableDefinition@endlink  encountered up the parent-child hierarchy. 
    ##  @return elec_cable_definition (@link CableDefinition NXOpen.Routing.Electrical.CableDefinition@endlink):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def FindTopmostCableDefinition(elec_stock_device: ElectricalStockDevice) -> CableDefinition:
        """
         Get topmost @link NXOpen::Routing::Electrical::CableDefinition NXOpen::Routing::Electrical::CableDefinition@endlink  encountered up the parent-child hierarchy. 
         @return elec_cable_definition (@link CableDefinition NXOpen.Routing.Electrical.CableDefinition@endlink):  .
        """
        pass
    
    ##  Get intermediate components 
    ##  @return intermediate_components (@link ConnectorDevice List[NXOpen.Routing.Electrical.ConnectorDevice]@endlink):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def GetIntermediateComponents(elec_stock_device: ElectricalStockDevice) -> List[ConnectorDevice]:
        """
         Get intermediate components 
         @return intermediate_components (@link ConnectorDevice List[NXOpen.Routing.Electrical.ConnectorDevice]@endlink):  .
        """
        pass
    
    ##  Get the intermediate terminals associated to this stock device. 
    ##  @return intermediate_terminals (@link NXOpen.Routing.LogicalTerminal List[NXOpen.Routing.LogicalTerminal]@endlink):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def GetIntermediateTerminals(elec_stock_device: ElectricalStockDevice) -> List[NXOpen.Routing.LogicalTerminal]:
        """
         Get the intermediate terminals associated to this stock device. 
         @return intermediate_terminals (@link NXOpen.Routing.LogicalTerminal List[NXOpen.Routing.LogicalTerminal]@endlink):  .
        """
        pass
    
    ##  Does this stock device have intermediate components? 
    ##  @return result (bool):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def HasIntermediateComponents(elec_stock_device: ElectricalStockDevice) -> bool:
        """
         Does this stock device have intermediate components? 
         @return result (bool):  .
        """
        pass
    
    ##  Manually routes a @link NXOpen::Routing::Electrical::ElectricalStockDevice NXOpen::Routing::Electrical::ElectricalStockDevice@endlink . 
    ##                 on given @link NXOpen::Routing::ISegment NXOpen::Routing::ISegment@endlink . The input segments should form a continuous 
    ##                 path between two @link NXOpen::Routing::Electrical::ConnectorDevice NXOpen::Routing::Electrical::ConnectorDevice@endlink  objects. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  Routing type. 
    def ManuallyRoute(elec_stock_device: ElectricalStockDevice, route_level: ElectricalStockDevice.RouteLevel, segments: List[NXOpen.Routing.ISegment]) -> None:
        """
         Manually routes a @link NXOpen::Routing::Electrical::ElectricalStockDevice NXOpen::Routing::Electrical::ElectricalStockDevice@endlink . 
                        on given @link NXOpen::Routing::ISegment NXOpen::Routing::ISegment@endlink . The input segments should form a continuous 
                        path between two @link NXOpen::Routing::Electrical::ConnectorDevice NXOpen::Routing::Electrical::ConnectorDevice@endlink  objects. 
        """
        pass
    
import NXOpen.Routing
##  Represents a @link NXOpen::Routing::Electrical::HarnessDefinition NXOpen::Routing::Electrical::HarnessDefinition@endlink   <br> Creator not available in KF.  <br> 
## 
##   <br>  Created in NX4.0.2  <br> 

class HarnessDefinition(NXOpen.Routing.AssemblyDefinition): 
    """ Represents a <ja_class>NXOpen.Routing.Electrical.HarnessDefinition</ja_class> """


    ##  Returns all of the Connection objects that are implemented by single devices
    ##                 that are children of this harness
    ##               
    ##  @return connections (@link Connection List[NXOpen.Routing.Electrical.Connection]@endlink): .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def GetChildConnections(objectValue: HarnessDefinition) -> List[Connection]:
        """
         Returns all of the Connection objects that are implemented by single devices
                        that are children of this harness
                      
         @return connections (@link Connection List[NXOpen.Routing.Electrical.Connection]@endlink): .
        """
        pass
    
import NXOpen
##  Represents a collection of @link Routing::Electrical::HarnessDevice Routing::Electrical::HarnessDevice@endlink  objects.   <br> To obtain an instance of this class, refer to @link NXOpen::Routing::RouteManager  NXOpen::Routing::RouteManager @endlink  <br> 
## 
##   <br>  Created in NX4.0.2  <br> 

class HarnessDeviceCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of <ja_class>Routing.Electrical.HarnessDevice</ja_class> objects.  """


    ##  Creates @link Routing::Electrical::HarnessDevice Routing::Electrical::HarnessDevice@endlink . 
    ##  @return harness_device (@link HarnessDevice NXOpen.Routing.Electrical.HarnessDevice@endlink):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## <param name="object_in_part"> (@link HarnessDeviceCollection NXOpen.Routing.Electrical.HarnessDeviceCollection@endlink) </param>
    @overload
    def CreateHarnessDevice(self, object_in_part: HarnessDeviceCollection) -> HarnessDevice:
        """
         Creates @link Routing::Electrical::HarnessDevice Routing::Electrical::HarnessDevice@endlink . 
         @return harness_device (@link HarnessDevice NXOpen.Routing.Electrical.HarnessDevice@endlink):  .
        """
        pass
    
    ##  Creates @link Routing::Electrical::HarnessDevice Routing::Electrical::HarnessDevice@endlink  with given name. 
    ##  @return harness_device (@link HarnessDevice NXOpen.Routing.Electrical.HarnessDevice@endlink):  .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  
    @overload
    def CreateHarnessDevice(self, object_in_part: HarnessDeviceCollection, harness_name: str) -> HarnessDevice:
        """
         Creates @link Routing::Electrical::HarnessDevice Routing::Electrical::HarnessDevice@endlink  with given name. 
         @return harness_device (@link HarnessDevice NXOpen.Routing.Electrical.HarnessDevice@endlink):  .
        """
        pass
    
    ##  Get harnesses 
    ##  @return harnesses (@link HarnessDevice List[NXOpen.Routing.Electrical.HarnessDevice]@endlink):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def GetHarnessSingleDevices(object_in_part: HarnessDeviceCollection) -> List[HarnessDevice]:
        """
         Get harnesses 
         @return harnesses (@link HarnessDevice List[NXOpen.Routing.Electrical.HarnessDevice]@endlink):  .
        """
        pass
    
import NXOpen.Routing
## 
##             The Electrical HarnessDevice corresponds to a harness instance of the 
##             @link Routing::SingleDevice Routing::SingleDevice@endlink .
##          <br> To create a new instance of this class, use @link NXOpen::Routing::Electrical::HarnessDeviceCollection::CreateHarnessDevice  NXOpen::Routing::Electrical::HarnessDeviceCollection::CreateHarnessDevice @endlink  <br> 
## 
##   <br>  Created in NX4.0.2  <br> 

class HarnessDevice(NXOpen.Routing.SingleDevice): 
    """
            The Electrical HarnessDevice corresponds to a harness instance of the 
            <ja_class>Routing.SingleDevice</ja_class>.
        """


    ##  Get harness definition. 
    ##  @return elec_harness_definition (@link HarnessDefinition NXOpen.Routing.Electrical.HarnessDefinition@endlink):  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def GetHarnessDefinition(elec_harness_device: HarnessDevice) -> HarnessDefinition:
        """
         Get harness definition. 
         @return elec_harness_definition (@link HarnessDefinition NXOpen.Routing.Electrical.HarnessDefinition@endlink):  .
        """
        pass
    
import NXOpen
##  A collection of @link NXOpen::Routing::Electrical::JumperConnection NXOpen::Routing::Electrical::JumperConnection@endlink  objects.  <br> To obtain an instance of this class, refer to @link NXOpen::Routing::RouteManager  NXOpen::Routing::RouteManager @endlink  <br> 
## 
##   <br>  Created in NX4.0.2  <br> 

class JumperConnectionCollection(NXOpen.TaggedObjectCollection): 
    """ A collection of <ja_class>NXOpen.Routing.Electrical.JumperConnection</ja_class> objects. """


    ##  Creates a @link NXOpen::Routing::Electrical::JumperConnection NXOpen::Routing::Electrical::JumperConnection@endlink  object. 
    ##  @return jumper_connection (@link JumperConnection NXOpen.Routing.Electrical.JumperConnection@endlink):  A @link NXOpen::Routing::Electrical::JumperConnection NXOpen::Routing::Electrical::JumperConnection@endlink  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    def CreateJumperConnection(object_in_part: JumperConnectionCollection) -> JumperConnection:
        """
         Creates a @link NXOpen::Routing::Electrical::JumperConnection NXOpen::Routing::Electrical::JumperConnection@endlink  object. 
         @return jumper_connection (@link JumperConnection NXOpen.Routing.Electrical.JumperConnection@endlink):  A @link NXOpen::Routing::Electrical::JumperConnection NXOpen::Routing::Electrical::JumperConnection@endlink  .
        """
        pass
    
##   @brief 
##            A jumper connection connects ports on the same connector.
##             
## 
##             
##             <br> 
##            A path may or may not be associated with this type of connection.  
##            Specifies that terminals on the same part instance are connected somehow.
##            See NX Open Routing help for detailed information on the Connection data model.
##             <br> 
##            
##          <br> To create a new instance of this class, use @link NXOpen::Routing::Electrical::JumperConnectionCollection::CreateJumperConnection  NXOpen::Routing::Electrical::JumperConnectionCollection::CreateJumperConnection @endlink  <br> 
## 
##   <br>  Created in NX4.0.2  <br> 

class JumperConnection(PathConnection): 
    """ <summary>
           A jumper connection connects ports on the same connector.
           </summary>           
           <para>
           A path may or may not be associated with this type of connection.  
           Specifies that terminals on the same part instance are connected somehow.
           See NX Open Routing help for detailed information on the Connection data model.
           </para>
           
        """
    pass


import NXOpen
##   @brief 
##             A collection of @link NXOpen::Routing::Electrical::NonPathConnection NXOpen::Routing::Electrical::NonPathConnection@endlink  objects.
##              
## 
##  
##              <br> 
##             See NX Open Routing help for detailed information on the Connection data model.
##              <br> 
##           <br> To obtain an instance of this class, refer to @link NXOpen::Routing::RouteManager  NXOpen::Routing::RouteManager @endlink  <br> 
## 
##   <br>  Created in NX4.0.2  <br> 

class NonPathConnectionCollection(NXOpen.TaggedObjectCollection): 
    """ <summary>
            A collection of <ja_class>NXOpen.Routing.Electrical.NonPathConnection</ja_class> objects.
            </summary>
            <para>
            See NX Open Routing help for detailed information on the Connection data model.
            </para>
         """


    ##  Creates a @link NXOpen::Routing::Electrical::NonPathConnection NXOpen::Routing::Electrical::NonPathConnection@endlink  object. 
    ##  @return non_path_connection (@link NonPathConnection NXOpen.Routing.Electrical.NonPathConnection@endlink):  A @link NXOpen::Routing::Electrical::NonPathConnection NXOpen::Routing::Electrical::NonPathConnection@endlink   .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    def CreateNonPathConnection(object_in_part: NonPathConnectionCollection) -> NonPathConnection:
        """
         Creates a @link NXOpen::Routing::Electrical::NonPathConnection NXOpen::Routing::Electrical::NonPathConnection@endlink  object. 
         @return non_path_connection (@link NonPathConnection NXOpen.Routing.Electrical.NonPathConnection@endlink):  A @link NXOpen::Routing::Electrical::NonPathConnection NXOpen::Routing::Electrical::NonPathConnection@endlink   .
        """
        pass
    
##   @brief 
##             Describes a connection that does not have a path
##              
## 
##  
##              <br> 
##             A pathless connection represents the abilitiy for objects to be 
##             connected even though there is not an explicit path between them.
##             See NX Open Routing help for detailed information on the Connection data model.
##              <br> 
##          <br> To create a new instance of this class, use @link NXOpen::Routing::Electrical::NonPathConnectionCollection::CreateNonPathConnection  NXOpen::Routing::Electrical::NonPathConnectionCollection::CreateNonPathConnection @endlink  <br> 
## 
##   <br>  Created in NX4.0.2  <br> 

class NonPathConnection(Connection): 
    """ <summary>
            Describes a connection that does not have a path
            </summary>
            <para>
            A pathless connection represents the abilitiy for objects to be 
            connected even though there is not an explicit path between them.
            See NX Open Routing help for detailed information on the Connection data model.
            </para>
        """
    pass


import NXOpen
import NXOpen.Assemblies
import NXOpen.Routing
##  Builder class to manage Path Arrangements.
##      <br> To create a new instance of this class, use @link NXOpen::Routing::RouteManager::CreatePathArrangementBuilder  NXOpen::Routing::RouteManager::CreatePathArrangementBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.3  <br> 

class PathArrangementBuilder(NXOpen.Builder): 
    """ Builder class to manage Path Arrangements.
    """


    ## Getter for property: (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink) HarnessPartOccurrence
    ##   the harness component in the context of the part that was used to create the extracted port.  
    ##      
    ##  
    ## Getter License requirements: routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## @return NXOpen.Assemblies.Component
    @property
    def HarnessPartOccurrence(self) -> NXOpen.Assemblies.Component:
        """
        Getter for property: (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink) HarnessPartOccurrence
          the harness component in the context of the part that was used to create the extracted port.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink) HarnessPartOccurrence

    ##   the harness component in the context of the part that was used to create the extracted port.  
    ##      
    ##  
    ## Setter License requirements: routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    @HarnessPartOccurrence.setter
    def HarnessPartOccurrence(self, partOcc: NXOpen.Assemblies.Component):
        """
        Setter for property: (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink) HarnessPartOccurrence
          the harness component in the context of the part that was used to create the extracted port.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Routing.Port NXOpen.Routing.Port@endlink) PrototypePort
    ##   the prototype of the extract port that is used as the reference port.  
    ##      
    ##  
    ## Getter License requirements: routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## @return NXOpen.Routing.Port
    @property
    def PrototypePort(self) -> NXOpen.Routing.Port:
        """
        Getter for property: (@link NXOpen.Routing.Port NXOpen.Routing.Port@endlink) PrototypePort
          the prototype of the extract port that is used as the reference port.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Routing.Port NXOpen.Routing.Port@endlink) PrototypePort

    ##   the prototype of the extract port that is used as the reference port.  
    ##      
    ##  
    ## Setter License requirements: routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    @PrototypePort.setter
    def PrototypePort(self, port: NXOpen.Routing.Port):
        """
        Setter for property: (@link NXOpen.Routing.Port NXOpen.Routing.Port@endlink) PrototypePort
          the prototype of the extract port that is used as the reference port.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink) PrototypePortPartOccurrence
    ##   the component part that contains the prototype of the extract port that is used as the reference
    ##             port.  
    ##      
    ##  
    ## Getter License requirements: routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## @return NXOpen.Assemblies.Component
    @property
    def PrototypePortPartOccurrence(self) -> NXOpen.Assemblies.Component:
        """
        Getter for property: (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink) PrototypePortPartOccurrence
          the component part that contains the prototype of the extract port that is used as the reference
                    port.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink) PrototypePortPartOccurrence

    ##   the component part that contains the prototype of the extract port that is used as the reference
    ##             port.  
    ##      
    ##  
    ## Setter License requirements: routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    @PrototypePortPartOccurrence.setter
    def PrototypePortPartOccurrence(self, partOcc: NXOpen.Assemblies.Component):
        """
        Setter for property: (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink) PrototypePortPartOccurrence
          the component part that contains the prototype of the extract port that is used as the reference
                    port.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ReferencePort
    ##   the port on which the offset is based when defining the path arrangement.  
    ##    The port property
    ##             can be either a port or a port occurrence.   
    ##  
    ## Getter License requirements: routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def ReferencePort(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ReferencePort
          the port on which the offset is based when defining the path arrangement.  
           The port property
                    can be either a port or a port occurrence.   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ReferencePort

    ##   the port on which the offset is based when defining the path arrangement.  
    ##    The port property
    ##             can be either a port or a port occurrence.   
    ##  
    ## Setter License requirements: routing_base ("Routing Basic")
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    @ReferencePort.setter
    def ReferencePort(self, port: NXOpen.TaggedObject):
        """
        Setter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) ReferencePort
          the port on which the offset is based when defining the path arrangement.  
           The port property
                    can be either a port or a port occurrence.   
         
        """
        pass
    
    ##  Clears the builder data associated with stored harness, namely the ReferencePort and
    ##          * the HarnessOccurrence, along with internal data. Note that the PrototypePortPartOccurrence
    ##          * and the PrototypePort are not cleared with this call.  
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: routing_base ("Routing Basic")
    @staticmethod
    def ClearHarnessData(builder: PathArrangementBuilder) -> None:
        """
         Clears the builder data associated with stored harness, namely the ReferencePort and
                 * the HarnessOccurrence, along with internal data. Note that the PrototypePortPartOccurrence
                 * and the PrototypePort are not cleared with this call.  
        """
        pass
    
    ##  Deletes path arrangement through builder 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: routing_base ("Routing Basic")
    @staticmethod
    def DeletePathArrangement(builder: PathArrangementBuilder) -> None:
        """
         Deletes path arrangement through builder 
        """
        pass
    
    ##  Retrieves the Path Arrangement object based on the data stored in the builder. If one does not
    ##             yet exist, a new one will be created. The retrieved object is stored internally in the biuilder.
    ##             This method is called after setting HarnessPartOccurrence and ReferencePort 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: routing_base ("Routing Basic")
    @staticmethod
    def EstablishPathArrangement(builder: PathArrangementBuilder) -> None:
        """
         Retrieves the Path Arrangement object based on the data stored in the builder. If one does not
                    yet exist, a new one will be created. The retrieved object is stored internally in the biuilder.
                    This method is called after setting HarnessPartOccurrence and ReferencePort 
        """
        pass
    
    ##  Initializes builder from arranged port 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: routing_base ("Routing Basic")
    ##  Routing port whose associated path arrangement object is used to populate the data in the builder 
    def InitializeBuilderFromArrangedPort(builder: PathArrangementBuilder, port: NXOpen.Routing.Port) -> None:
        """
         Initializes builder from arranged port 
        """
        pass
    
    ##  Sets a new origin for the point on the harness path. This point should be in the
    ##             context of the current root part. 
    ## 
    ##   <br>  Created in NX10.0.3  <br> 

    ## License requirements: routing_base ("Routing Basic")
    ##  Origin of the path arrangement in the context of the root part. 
    def SetPathArrangementOrigin(builder: PathArrangementBuilder, point: NXOpen.Point3d) -> None:
        """
         Sets a new origin for the point on the harness path. This point should be in the
                    context of the current root part. 
        """
        pass
    
import NXOpen
##   @brief 
##             A collection of @link NXOpen::Routing::Electrical::PathConnection NXOpen::Routing::Electrical::PathConnection@endlink  objects.
##              
## 
##  
##              <br> 
##             See NX Open Routing help for detailed information on the Connection data model.
##              <br> 
##           <br> To obtain an instance of this class, refer to @link NXOpen::Routing::RouteManager  NXOpen::Routing::RouteManager @endlink  <br> 
## 
##   <br>  Created in NX4.0.2  <br> 

class PathConnectionCollection(NXOpen.TaggedObjectCollection): 
    """ <summary>
            A collection of <ja_class>NXOpen.Routing.Electrical.PathConnection</ja_class> objects.
            </summary>
            <para>
            See NX Open Routing help for detailed information on the Connection data model.
            </para>
         """


    ##  Create a @link NXOpen::Routing::Electrical::PathConnection NXOpen::Routing::Electrical::PathConnection@endlink  object. 
    ##  @return path_connection (@link PathConnection NXOpen.Routing.Electrical.PathConnection@endlink):  A @link NXOpen::Routing::Electrical::PathConnection NXOpen::Routing::Electrical::PathConnection@endlink  .
    ## 
    ##   <br>  Created in NX4.0.2  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    def CreatePathConnection(object_in_part: PathConnectionCollection) -> PathConnection:
        """
         Create a @link NXOpen::Routing::Electrical::PathConnection NXOpen::Routing::Electrical::PathConnection@endlink  object. 
         @return path_connection (@link PathConnection NXOpen.Routing.Electrical.PathConnection@endlink):  A @link NXOpen::Routing::Electrical::PathConnection NXOpen::Routing::Electrical::PathConnection@endlink  .
        """
        pass
    
##   @brief 
##             Describes a connection that has a path
##              
## 
##  
##              <br> 
##             From and To terminals are not coincident and need a path definition to be routable.            
##             See NX Open Routing help for detailed information on the Connection data model.
##              <br> 
##          <br> To create a new instance of this class, use @link NXOpen::Routing::Electrical::PathConnectionCollection::CreatePathConnection  NXOpen::Routing::Electrical::PathConnectionCollection::CreatePathConnection @endlink  <br> 
## 
##   <br>  Created in NX4.0.2  <br> 

class PathConnection(Connection): 
    """ <summary>
            Describes a connection that has a path
            </summary>
            <para>
            From and To terminals are not coincident and need a path definition to be routable.            
            See NX Open Routing help for detailed information on the Connection data model.
            </para>
        """
    pass


##  Represents Routing Electrical ShieldDefinition object  <br> Creator not available in KF.  <br> 
## 
##   <br>  Created in NX4.0.2  <br> 

class ShieldDefinition(CableDefinition): 
    """ Represents Routing Electrical ShieldDefinition object """
    pass


## 
##             The Electrical ShieldDevice corresponds to a shield instance of
##             @link Routing::Electrical::ElectricalStockDevice Routing::Electrical::ElectricalStockDevice@endlink . 
##             An electrical shield device is both an assembly definition and a electrical stock device.
##          <br> Creator not available in KF.  <br> 
## 
##   <br>  Created in NX4.0.2  <br> 

class ShieldDevice(CableDevice): 
    """
            The Electrical ShieldDevice corresponds to a shield instance of
            <ja_class>Routing.Electrical.ElectricalStockDevice</ja_class>. 
            An electrical shield device is both an assembly definition and a electrical stock device.
        """
    pass


##  Represents Routing Electrical ShieldStockDefinition object  <br> Creator not available in KF.  <br> 
## 
##   <br>  Created in NX4.0.2  <br> 

class ShieldStockDefinition(CableStockDefinition): 
    """ Represents Routing Electrical ShieldStockDefinition object """
    pass


import NXOpen
##  Data object created by Routing just before routing connections.
##             Routing sends this object to any registered Sort Connections plugin with the
##             "Stock Devices to sort" filled in.
## 
##             It is the Sort Connections plugin responsibility to sort the Stock Devices and
##             to put the sorted Stock Devices into "Sorted Stock Devices".
## 
##             For more information, see @link Routing::CustomManager Routing::CustomManager@endlink  and the
##             @link Routing::CustomManager::SetSortConnectionsPlugin Routing::CustomManager::SetSortConnectionsPlugin@endlink 
##          <br> An instance of this object will be sent to the Sort Connections plugin.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class SortConnectionsPluginData(NXOpen.TaggedObject): 
    """ Data object created by Routing just before routing connections.
            Routing sends this object to any registered Sort Connections plugin with the
            "Stock Devices to sort" filled in.

            It is the Sort Connections plugin responsibility to sort the Stock Devices and
            to put the sorted Stock Devices into "Sorted Stock Devices".

            For more information, see <ja_class>Routing.CustomManager</ja_class> and the
            <ja_method>Routing.CustomManager.SetSortConnectionsPlugin</ja_method>
        """


    ##  Gets the stock devices such as @link Routing::Electrical::WireDevice Routing::Electrical::WireDevice@endlink s
    ##                 that implement connections Routing is about to route along their paths. 
    ##  @return stockDevices (@link ElectricalStockDevice List[NXOpen.Routing.Electrical.ElectricalStockDevice]@endlink):  The @link Routing::Electrical::ElectricalStockDevice Routing::Electrical::ElectricalStockDevice@endlink s to sort in the order in which
    ##                     you want to route them. .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def GetStockDevicesToSort(dataObject: SortConnectionsPluginData) -> List[ElectricalStockDevice]:
        """
         Gets the stock devices such as @link Routing::Electrical::WireDevice Routing::Electrical::WireDevice@endlink s
                        that implement connections Routing is about to route along their paths. 
         @return stockDevices (@link ElectricalStockDevice List[NXOpen.Routing.Electrical.ElectricalStockDevice]@endlink):  The @link Routing::Electrical::ElectricalStockDevice Routing::Electrical::ElectricalStockDevice@endlink s to sort in the order in which
                            you want to route them. .
        """
        pass
    
    ##  Sets the stock devices sorted in the order in which you want their connections to route. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  The @link Routing::Electrical::ElectricalStockDevice Routing::Electrical::ElectricalStockDevice@endlink s sorted in the order in which
    ##                     you want to route them. 
    def SetSortedStockDevices(dataObject: SortConnectionsPluginData, stockDevices: List[ElectricalStockDevice]) -> None:
        """
         Sets the stock devices sorted in the order in which you want their connections to route. 
        """
        pass
    
import NXOpen
##  The collection of all @link NXOpen::Routing::Electrical::SplicePoint NXOpen::Routing::Electrical::SplicePoint@endlink s.
##             Use the @link NXOpen::Routing::Electrical::SplicePositionBuilder NXOpen::Routing::Electrical::SplicePositionBuilder@endlink  to create
##             a @link NXOpen::Routing::Electrical::SplicePoint NXOpen::Routing::Electrical::SplicePoint@endlink .
##          <br> To obtain an instance of this class, refer to @link NXOpen::Routing::RouteManager  NXOpen::Routing::RouteManager @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class SplicePointCollection(NXOpen.TaggedObjectCollection): 
    """ The collection of all <ja_class>NXOpen.Routing.Electrical.SplicePoint</ja_class>s.
            Use the <ja_class>NXOpen.Routing.Electrical.SplicePositionBuilder</ja_class> to create
            a <ja_class>NXOpen.Routing.Electrical.SplicePoint</ja_class>.
        """
    pass


import NXOpen
import NXOpen.Features
##  Represents a @link NXOpen::Routing::Electrical::SplicePoint NXOpen::Routing::Electrical::SplicePoint@endlink .  <br> To create or edit an instance of this class, use @link NXOpen::Routing::Electrical::SplicePositionBuilder  NXOpen::Routing::Electrical::SplicePositionBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class SplicePoint(NXOpen.Point): 
    """ Represents a <ja_class>NXOpen.Routing.Electrical.SplicePoint</ja_class>. """


    ## Getter for property: (float) AdditionalLength
    ##   the additional length required for a wire using this splice point.  
    ##      
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def AdditionalLength(self) -> float:
        """
        Getter for property: (float) AdditionalLength
          the additional length required for a wire using this splice point.  
             
         
        """
        pass
    
    ## Getter for property: (@link ConnectorDevice NXOpen.Routing.Electrical.ConnectorDevice@endlink) ConnectorDevice
    ##   the @link Routing::Electrical::ConnectorDevice Routing::Electrical::ConnectorDevice@endlink  to which this splice is assigned.  
    ##     
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return ConnectorDevice
    @property
    def ConnectorDevice(self) -> ConnectorDevice:
        """
        Getter for property: (@link ConnectorDevice NXOpen.Routing.Electrical.ConnectorDevice@endlink) ConnectorDevice
          the @link Routing::Electrical::ConnectorDevice Routing::Electrical::ConnectorDevice@endlink  to which this splice is assigned.  
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##   the name of this splice point.  
    ##      
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the name of this splice point.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink) SphereFeature
    ##   the sphere feature that represents this splice point.  
    ##      
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Features.Feature
    @property
    def SphereFeature(self) -> NXOpen.Features.Feature:
        """
        Getter for property: (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink) SphereFeature
          the sphere feature that represents this splice point.  
             
         
        """
        pass
    
import NXOpen
import NXOpen.Routing
##  Represents @link NXOpen::Routing::Electrical::SplicePositionBuilder NXOpen::Routing::Electrical::SplicePositionBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::Routing::RouteManager::CreateSplicePositionBuilder  NXOpen::Routing::RouteManager::CreateSplicePositionBuilder @endlink  <br> 
## 
##   <br>  Created in NX1872.0.0  <br> 

class SplicePositionBuilder(NXOpen.Builder): 
    """ Represents <ja_class>NXOpen.Routing.Electrical.SplicePositionBuilder</ja_class>. """


    ## Getter for property: (float) AdditionalLength
    ##   the additional length required for the wire for the fabrication of splice.  
    ##      
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return float
    @property
    def AdditionalLength(self) -> float:
        """
        Getter for property: (float) AdditionalLength
          the additional length required for the wire for the fabrication of splice.  
             
         
        """
        pass
    
    ## Setter for property: (float) AdditionalLength

    ##   the additional length required for the wire for the fabrication of splice.  
    ##      
    ##  
    ## Setter License requirements: routing_advanced ("Routing Advanced")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @AdditionalLength.setter
    def AdditionalLength(self, additionalLength: float):
        """
        Setter for property: (float) AdditionalLength
          the additional length required for the wire for the fabrication of splice.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceForSplicePoint
    ##   the distance for splice point from the inferred anchor node on route section.  
    ##      
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DistanceForSplicePoint(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceForSplicePoint
          the distance for splice point from the inferred anchor node on route section.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOnPath
    ##   the point on path/curve selected by user to position a splice   
    ##     
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def PointOnPath(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOnPath
          the point on path/curve selected by user to position a splice   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOnPath

    ##   the point on path/curve selected by user to position a splice   
    ##     
    ##  
    ## Setter License requirements: routing_advanced ("Routing Advanced")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @PointOnPath.setter
    def PointOnPath(self, pointOnPath: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOnPath
          the point on path/curve selected by user to position a splice   
            
         
        """
        pass
    
    ## Getter for property: (str) SpliceName
    ##   the splice name given by NX user or received from capital.  
    ##      
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return str
    @property
    def SpliceName(self) -> str:
        """
        Getter for property: (str) SpliceName
          the splice name given by NX user or received from capital.  
             
         
        """
        pass
    
    ## Setter for property: (str) SpliceName

    ##   the splice name given by NX user or received from capital.  
    ##      
    ##  
    ## Setter License requirements: routing_advanced ("Routing Advanced")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @SpliceName.setter
    def SpliceName(self, spliceName: str):
        """
        Setter for property: (str) SpliceName
          the splice name given by NX user or received from capital.  
             
         
        """
        pass
    
    ## Getter for property: (bool) SwitchRouteNode
    ##   the switch route node can be used by user to highlight and store the route node opposite to the inferred anchor node.  
    ##      
    ##  
    ## Getter License requirements: routing_advanced ("Routing Advanced")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return bool
    @property
    def SwitchRouteNode(self) -> bool:
        """
        Getter for property: (bool) SwitchRouteNode
          the switch route node can be used by user to highlight and store the route node opposite to the inferred anchor node.  
             
         
        """
        pass
    
    ## Setter for property: (bool) SwitchRouteNode

    ##   the switch route node can be used by user to highlight and store the route node opposite to the inferred anchor node.  
    ##      
    ##  
    ## Setter License requirements: routing_advanced ("Routing Advanced")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @SwitchRouteNode.setter
    def SwitchRouteNode(self, switchRouteNode: bool):
        """
        Setter for property: (bool) SwitchRouteNode
          the switch route node can be used by user to highlight and store the route node opposite to the inferred anchor node.  
             
         
        """
        pass
    
    ##  The automation user has to set distance to place a splice on route section. The distance would be considered from the start node
    ##                 of the route section. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced")
    ## 
    ## <param name="distanceForSplicePoint"> (float) </param>
    def SetDistanceFromAnchorNode(builder: SplicePositionBuilder, distanceForSplicePoint: float) -> None:
        """
         The automation user has to set distance to place a splice on route section. The distance would be considered from the start node
                        of the route section. 
        """
        pass
    
    ##  The automation user has to set the end route nodes of the route section in order to place splice on route section. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced")
    ## 
    ## <param name="startRouteNode"> (@link NXOpen.Routing.ControlPoint NXOpen.Routing.ControlPoint@endlink) </param>
    ## <param name="endRouteNode"> (@link NXOpen.Routing.ControlPoint NXOpen.Routing.ControlPoint@endlink) </param>
    def SetEndRouteNodesOfRouteSection(builder: SplicePositionBuilder, startRouteNode: NXOpen.Routing.ControlPoint, endRouteNode: NXOpen.Routing.ControlPoint) -> None:
        """
         The automation user has to set the end route nodes of the route section in order to place splice on route section. 
        """
        pass
    
    ##  The automation user has to set the total length of route section. This will be used for internal validations and to place splice correctly. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced")
    ## 
    ## <param name="totalLengthOfRouteSection"> (float) </param>
    def SetTotalCurveLengthOfRouteSection(builder: SplicePositionBuilder, totalLengthOfRouteSection: float) -> None:
        """
         The automation user has to set the total length of route section. This will be used for internal validations and to place splice correctly. 
        """
        pass
    
##  Represents a @link NXOpen::Routing::Electrical::SystemDefinition NXOpen::Routing::Electrical::SystemDefinition@endlink   <br> Creator not available in KF.  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class SystemDefinition(HarnessDefinition): 
    """ Represents a <ja_class>NXOpen.Routing.Electrical.SystemDefinition</ja_class> """
    pass


import NXOpen
##  Represents a collection of @link NXOpen::Routing::Electrical::SystemDevice NXOpen::Routing::Electrical::SystemDevice@endlink  objects.   <br> To obtain an instance of this class, refer to @link NXOpen::Routing::RouteManager  NXOpen::Routing::RouteManager @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class SystemDeviceCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of <ja_class>NXOpen.Routing.Electrical.SystemDevice</ja_class> objects.  """


    ##  Creates @link NXOpen::Routing::Electrical::SystemDevice NXOpen::Routing::Electrical::SystemDevice@endlink . 
    ##  @return system_device (@link SystemDevice NXOpen.Routing.Electrical.SystemDevice@endlink):  The new System Device. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ## <param name="object_in_part"> (@link SystemDeviceCollection NXOpen.Routing.Electrical.SystemDeviceCollection@endlink) </param>
    @overload
    def CreateSystemDevice(self, object_in_part: SystemDeviceCollection) -> SystemDevice:
        """
         Creates @link NXOpen::Routing::Electrical::SystemDevice NXOpen::Routing::Electrical::SystemDevice@endlink . 
         @return system_device (@link SystemDevice NXOpen.Routing.Electrical.SystemDevice@endlink):  The new System Device. .
        """
        pass
    
    ##  Creates @link NXOpen::Routing::Electrical::SystemDevice NXOpen::Routing::Electrical::SystemDevice@endlink  with given name. 
    ##  @return system_device (@link SystemDevice NXOpen.Routing.Electrical.SystemDevice@endlink):  The new System Device. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    ##  The name of the new system.
    ##                                                              (NULL not allowed) 
    @overload
    def CreateSystemDevice(self, object_in_part: SystemDeviceCollection, system_name: str) -> SystemDevice:
        """
         Creates @link NXOpen::Routing::Electrical::SystemDevice NXOpen::Routing::Electrical::SystemDevice@endlink  with given name. 
         @return system_device (@link SystemDevice NXOpen.Routing.Electrical.SystemDevice@endlink):  The new System Device. .
        """
        pass
    
    ##  Get System Devices. 
    ##  @return systems (@link SystemDevice List[NXOpen.Routing.Electrical.SystemDevice]@endlink):  The array of System Devices in the given part. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def GetSystemSingleDevices(object_in_part: SystemDeviceCollection) -> List[SystemDevice]:
        """
         Get System Devices. 
         @return systems (@link SystemDevice List[NXOpen.Routing.Electrical.SystemDevice]@endlink):  The array of System Devices in the given part. .
        """
        pass
    
## 
##             The Electrical SystemDevice corresponds to a system instance of the 
##             @link NXOpen::Routing::SingleDevice NXOpen::Routing::SingleDevice@endlink .
##          <br> To create a new instance of this class, use @link NXOpen::Routing::Electrical::SystemDeviceCollection::CreateSystemDevice  NXOpen::Routing::Electrical::SystemDeviceCollection::CreateSystemDevice @endlink  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class SystemDevice(HarnessDevice): 
    """
            The Electrical SystemDevice corresponds to a system instance of the 
            <ja_class>NXOpen.Routing.SingleDevice</ja_class>.
        """


    ##  Returns the @link NXOpen::Routing::Electrical::SystemDefinition NXOpen::Routing::Electrical::SystemDefinition@endlink 
    ##                 used by this @link NXOpen::Routing::Electrical::SystemDevice NXOpen::Routing::Electrical::SystemDevice@endlink . 
    ##  @return system_definition (@link SystemDefinition NXOpen.Routing.Electrical.SystemDefinition@endlink):  The @link NXOpen::Routing::Electrical::SystemDefinition NXOpen::Routing::Electrical::SystemDefinition@endlink  used by this @link NXOpen::Routing::Electrical::SystemDevice NXOpen::Routing::Electrical::SystemDevice@endlink . .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: routing_advanced ("Routing Advanced"), routing_base ("Routing Basic")
    @staticmethod
    def GetSystemDefinition(system_device: SystemDevice) -> SystemDefinition:
        """
         Returns the @link NXOpen::Routing::Electrical::SystemDefinition NXOpen::Routing::Electrical::SystemDefinition@endlink 
                        used by this @link NXOpen::Routing::Electrical::SystemDevice NXOpen::Routing::Electrical::SystemDevice@endlink . 
         @return system_definition (@link SystemDefinition NXOpen.Routing.Electrical.SystemDefinition@endlink):  The @link NXOpen::Routing::Electrical::SystemDefinition NXOpen::Routing::Electrical::SystemDefinition@endlink  used by this @link NXOpen::Routing::Electrical::SystemDevice NXOpen::Routing::Electrical::SystemDevice@endlink . .
        """
        pass
    
## 
##             The Electrical WireDevice corresponds to a wire instance of
##             @link NXOpen::Routing::Electrical::ElectricalStockDevice NXOpen::Routing::Electrical::ElectricalStockDevice@endlink .
##          <br> Creator not available in KF.  <br> 
## 
##   <br>  Created in NX4.0.2  <br> 

class WireDevice(ElectricalStockDevice): 
    """
            The Electrical WireDevice corresponds to a wire instance of
            <ja_class>NXOpen.Routing.Electrical.ElectricalStockDevice</ja_class>.
        """
    pass


## @package NXOpen.Routing.Electrical
## Classes, Enums and Structs under NXOpen.Routing.Electrical namespace

##  @link ConnectionRouteLevel NXOpen.Routing.Electrical.ConnectionRouteLevel @endlink is an alias for @link Connection.RouteLevel NXOpen.Routing.Electrical.Connection.RouteLevel@endlink
ConnectionRouteLevel = Connection.RouteLevel


##  @link ConnectorDeviceAssign NXOpen.Routing.Electrical.ConnectorDeviceAssign @endlink is an alias for @link ConnectorDevice.Assign NXOpen.Routing.Electrical.ConnectorDevice.Assign@endlink
ConnectorDeviceAssign = ConnectorDevice.Assign


##  @link ConnectorDeviceComponentType NXOpen.Routing.Electrical.ConnectorDeviceComponentType @endlink is an alias for @link ConnectorDevice.ComponentType NXOpen.Routing.Electrical.ConnectorDevice.ComponentType@endlink
ConnectorDeviceComponentType = ConnectorDevice.ComponentType


##  @link ElectricalFormatType NXOpen.Routing.Electrical.ElectricalFormatType @endlink is an alias for @link ElectricalFormat.Type NXOpen.Routing.Electrical.ElectricalFormat.Type@endlink
ElectricalFormatType = ElectricalFormat.Type


##  @link ElectricalStockDefinitionSectionType NXOpen.Routing.Electrical.ElectricalStockDefinitionSectionType @endlink is an alias for @link ElectricalStockDefinition.SectionType NXOpen.Routing.Electrical.ElectricalStockDefinition.SectionType@endlink
ElectricalStockDefinitionSectionType = ElectricalStockDefinition.SectionType


##  @link ElectricalStockDeviceAutoRouteSel NXOpen.Routing.Electrical.ElectricalStockDeviceAutoRouteSel @endlink is an alias for @link ElectricalStockDevice.AutoRouteSel NXOpen.Routing.Electrical.ElectricalStockDevice.AutoRouteSel@endlink
ElectricalStockDeviceAutoRouteSel = ElectricalStockDevice.AutoRouteSel


##  @link ElectricalStockDeviceRouteLevel NXOpen.Routing.Electrical.ElectricalStockDeviceRouteLevel @endlink is an alias for @link ElectricalStockDevice.RouteLevel NXOpen.Routing.Electrical.ElectricalStockDevice.RouteLevel@endlink
ElectricalStockDeviceRouteLevel = ElectricalStockDevice.RouteLevel


##  @link ElectricalStockDeviceRouteTypes NXOpen.Routing.Electrical.ElectricalStockDeviceRouteTypes @endlink is an alias for @link ElectricalStockDevice.RouteTypes NXOpen.Routing.Electrical.ElectricalStockDevice.RouteTypes@endlink
ElectricalStockDeviceRouteTypes = ElectricalStockDevice.RouteTypes


