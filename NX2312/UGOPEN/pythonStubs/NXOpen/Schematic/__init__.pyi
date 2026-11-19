from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##   @brief  Represents a BaseObjectBuilder.  
## 
##    <br> This is an abstract class and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class BaseObjectBuilder(NXOpen.Builder): 
    """ <summary> Represents a BaseObjectBuilder. </summary> """


    ## Getter for property: (str) Id
    ##   the id of the object.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
          the id of the object.  
             
         
        """
        pass
    
    ## Getter for property: (str) Label
    ##   the tag of this object.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def Label(self) -> str:
        """
        Getter for property: (str) Label
          the tag of this object.  
             
         
        """
        pass
    
    ## Getter for property: (@link Sheet NXOpen.Schematic.Sheet@endlink) Sheet
    ##   the sheet containing the object.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return Sheet
    @property
    def Sheet(self) -> Sheet:
        """
        Getter for property: (@link Sheet NXOpen.Schematic.Sheet@endlink) Sheet
          the sheet containing the object.  
             
         
        """
        pass
    
    ## Setter for property: (@link Sheet NXOpen.Schematic.Sheet@endlink) Sheet

    ##   the sheet containing the object.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @Sheet.setter
    def Sheet(self, sheet: Sheet):
        """
        Setter for property: (@link Sheet NXOpen.Schematic.Sheet@endlink) Sheet
          the sheet containing the object.  
             
         
        """
        pass
    
    ##  Gets the discipline of the object. 
    ##  @return disciplines (List[str]): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetDisciplines(builder: BaseObjectBuilder) -> List[str]:
        """
         Gets the discipline of the object. 
         @return disciplines (List[str]): .
        """
        pass
    
    ##  Sets the discipline of the object. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="disciplines"> (List[str]) </param>
    def SetDisciplines(builder: BaseObjectBuilder, disciplines: List[str]) -> None:
        """
         Sets the discipline of the object. 
        """
        pass
    
import NXOpen
import NXOpen.Diagramming
## 
##     Represents a BulkEditBuilder to edit bulk of objects.
##      <br> To create a new instance of this class, use @link NXOpen::Schematic::SchematicManager::CreateBulkEditBuilder  NXOpen::Schematic::SchematicManager::CreateBulkEditBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class BulkEditBuilder(NXOpen.Builder): 
    """
    Represents a BulkEditBuilder to edit bulk of objects.
    """


    ##  Sets the delta value of X coordinate for bulk moving. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="deltaXCoordinate"> (float) </param>
    def SetDeltaXCoordinate(builder: BulkEditBuilder, deltaXCoordinate: float) -> None:
        """
         Sets the delta value of X coordinate for bulk moving. 
        """
        pass
    
    ##  Sets the delta value of Y coordinate for bulk moving. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="deltaYCoordinate"> (float) </param>
    def SetDeltaYCoordinate(builder: BulkEditBuilder, deltaYCoordinate: float) -> None:
        """
         Sets the delta value of Y coordinate for bulk moving. 
        """
        pass
    
    ##  Sets the visibility of sheet elements. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="hide"> (bool) </param>
    def SetHide(builder: BulkEditBuilder, hide: bool) -> None:
        """
         Sets the visibility of sheet elements. 
        """
        pass
    
    ##  Sets the visibility of labels. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="hideLabel"> (bool) </param>
    def SetHideLabel(builder: BulkEditBuilder, hideLabel: bool) -> None:
        """
         Sets the visibility of labels. 
        """
        pass
    
    ##  Sets the sheet elements for bulk editing. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sheetElements"> (@link NXOpen.Diagramming.SheetElement List[NXOpen.Diagramming.SheetElement]@endlink) </param>
    def SetSheetElements(builder: BulkEditBuilder, sheetElements: List[NXOpen.Diagramming.SheetElement]) -> None:
        """
         Sets the sheet elements for bulk editing. 
        """
        pass
    
## Represents the connection attribute source type. 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Object</term><description> 
## </description> </item><item><term> 
## Stock</term><description> 
## </description> </item><item><term> 
## Insulation</term><description> 
## </description> </item></list>
class ConnectionAttributeSourceType(Enum):
    """
    Members Include: <Object> <Stock> <Insulation>
    """
    Object: int
    Stock: int
    Insulation: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ConnectionAttributeSourceType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
import NXOpen.Diagramming
##   @brief  Represents a ConnectionBuilder.  
## 
##    <br> To create a new instance of this class, use @link NXOpen::Schematic::SchematicManager::CreateConnectionBuilder  NXOpen::Schematic::SchematicManager::CreateConnectionBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## EndJunction.InstrumentSymbolSize </term> <description> 
##  
## 15 </description> </item> 
## 
## <item><term> 
##  
## EndJunction.Rotate </term> <description> 
##  
## Zero </description> </item> 
## 
## <item><term> 
##  
## EndJunction.SymbolSourceType </term> <description> 
##  
## ReuseLibrary </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1980.0.0  <br> 

class ConnectionBuilder(BaseObjectBuilder): 
    """ <summary> Represents a ConnectionBuilder. </summary> """


    ## Getter for property: (@link ConnectionDataBuilder NXOpen.Schematic.ConnectionDataBuilder@endlink) ConnectionData
    ##   the connection data builder.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return ConnectionDataBuilder
    @property
    def ConnectionData(self) -> ConnectionDataBuilder:
        """
        Getter for property: (@link ConnectionDataBuilder NXOpen.Schematic.ConnectionDataBuilder@endlink) ConnectionData
          the connection data builder.  
             
         
        """
        pass
    
    ## Getter for property: (str) ElementId
    ##   the current element ID of this connection.  
    ##    It works only in edit mode, it's optional and the first element ID stored in the connection will be used as default.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def ElementId(self) -> str:
        """
        Getter for property: (str) ElementId
          the current element ID of this connection.  
           It works only in edit mode, it's optional and the first element ID stored in the connection will be used as default.  
         
        """
        pass
    
    ## Setter for property: (str) ElementId

    ##   the current element ID of this connection.  
    ##    It works only in edit mode, it's optional and the first element ID stored in the connection will be used as default.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ElementId.setter
    def ElementId(self, elementId: str):
        """
        Setter for property: (str) ElementId
          the current element ID of this connection.  
           It works only in edit mode, it's optional and the first element ID stored in the connection will be used as default.  
         
        """
        pass
    
    ## Getter for property: (@link NodeBuilder NXOpen.Schematic.NodeBuilder@endlink) EndJunction
    ##   the end junction builder.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NodeBuilder
    @property
    def EndJunction(self) -> NodeBuilder:
        """
        Getter for property: (@link NodeBuilder NXOpen.Schematic.NodeBuilder@endlink) EndJunction
          the end junction builder.  
             
         
        """
        pass
    
    ## Getter for property: (@link Connection NXOpen.Schematic.Connection@endlink) SplittedConnection
    ##   the new created connection after breaking the old connection.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return Connection
    @property
    def SplittedConnection(self) -> Connection:
        """
        Getter for property: (@link Connection NXOpen.Schematic.Connection@endlink) SplittedConnection
          the new created connection after breaking the old connection.  
             
         
        """
        pass
    
    ## Getter for property: (@link NodeBuilder NXOpen.Schematic.NodeBuilder@endlink) StartJunction
    ##   the start junction builder.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NodeBuilder
    @property
    def StartJunction(self) -> NodeBuilder:
        """
        Getter for property: (@link NodeBuilder NXOpen.Schematic.NodeBuilder@endlink) StartJunction
          the start junction builder.  
             
         
        """
        pass
    
    ##  Creates the connection data builder. 
    ##  @return connectionData (@link ConnectionDataBuilder NXOpen.Schematic.ConnectionDataBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def CreateConnectionData(builder: ConnectionBuilder) -> ConnectionDataBuilder:
        """
         Creates the connection data builder. 
         @return connectionData (@link ConnectionDataBuilder NXOpen.Schematic.ConnectionDataBuilder@endlink): .
        """
        pass
    
    ##  Creates the end junction builder. 
    ##  @return junctionBuilder (@link NodeBuilder NXOpen.Schematic.NodeBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="node"> (@link Node NXOpen.Schematic.Node@endlink) </param>
    def CreateEndJunction(builder: ConnectionBuilder, node: Node) -> NodeBuilder:
        """
         Creates the end junction builder. 
         @return junctionBuilder (@link NodeBuilder NXOpen.Schematic.NodeBuilder@endlink): .
        """
        pass
    
    ##  Creates the start junction builder. 
    ##  @return junctionBuilder (@link NodeBuilder NXOpen.Schematic.NodeBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="node"> (@link Node NXOpen.Schematic.Node@endlink) </param>
    def CreateStartJunction(builder: ConnectionBuilder, node: Node) -> NodeBuilder:
        """
         Creates the start junction builder. 
         @return junctionBuilder (@link NodeBuilder NXOpen.Schematic.NodeBuilder@endlink): .
        """
        pass
    
    ##  Get bending points for polyline to render the connection. 
    ##  @return points (@link NXOpen.Point2d List[NXOpen.Point2d]@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetBendPoints(builder: ConnectionBuilder) -> List[NXOpen.Point2d]:
        """
         Get bending points for polyline to render the connection. 
         @return points (@link NXOpen.Point2d List[NXOpen.Point2d]@endlink): .
        """
        pass
    
    ##  Get the connection object of the connection builder. 
    ##  @return connection (@link NXOpen.Diagramming.Connection NXOpen.Diagramming.Connection@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetConnection(builder: ConnectionBuilder) -> NXOpen.Diagramming.Connection:
        """
         Get the connection object of the connection builder. 
         @return connection (@link NXOpen.Diagramming.Connection NXOpen.Diagramming.Connection@endlink): .
        """
        pass
    
    ##  Gets the end port of this connection.
    ##  @return port (@link Port NXOpen.Schematic.Port@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetEnd(builder: ConnectionBuilder) -> Port:
        """
         Gets the end port of this connection.
         @return port (@link Port NXOpen.Schematic.Port@endlink): .
        """
        pass
    
    ##  Get the end location of this connection.
    ##             This end location is applicable only when the @link Diagramming::ConnectionBuilder::End Diagramming::ConnectionBuilder::End@endlink  port is NULL. 
    ##  @return endLocation (@link NXOpen.Point2d NXOpen.Point2d@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetEndLocation(builder: ConnectionBuilder) -> NXOpen.Point2d:
        """
         Get the end location of this connection.
                    This end location is applicable only when the @link Diagramming::ConnectionBuilder::End Diagramming::ConnectionBuilder::End@endlink  port is NULL. 
         @return endLocation (@link NXOpen.Point2d NXOpen.Point2d@endlink): .
        """
        pass
    
    ##  Gets the end Node of this connection.
    ##          Note: When the builder is commited, a dynamic Port will be used and can be found in the GetEnd method
    ##  @return node (@link Node NXOpen.Schematic.Node@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetEndNode(builder: ConnectionBuilder) -> Node:
        """
         Gets the end Node of this connection.
                 Note: When the builder is commited, a dynamic Port will be used and can be found in the GetEnd method
         @return node (@link Node NXOpen.Schematic.Node@endlink): .
        """
        pass
    
    ##  Gets the line type of the connection. 
    ##  @return lineType (str): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLineType(builder: ConnectionBuilder) -> str:
        """
         Gets the line type of the connection. 
         @return lineType (str): .
        """
        pass
    
    ##  Gets the start port of this connection in native. 
    ##  @return port (@link Port NXOpen.Schematic.Port@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStart(builder: ConnectionBuilder) -> Port:
        """
         Gets the start port of this connection in native. 
         @return port (@link Port NXOpen.Schematic.Port@endlink): .
        """
        pass
    
    ##  Get the start location of this connection.
    ##             This start location is applicable only when the @link Diagramming::ConnectionBuilder::Start Diagramming::ConnectionBuilder::Start@endlink  is NULL.
    ##  @return startLocation (@link NXOpen.Point2d NXOpen.Point2d@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStartLocation(builder: ConnectionBuilder) -> NXOpen.Point2d:
        """
         Get the start location of this connection.
                    This start location is applicable only when the @link Diagramming::ConnectionBuilder::Start Diagramming::ConnectionBuilder::Start@endlink  is NULL.
         @return startLocation (@link NXOpen.Point2d NXOpen.Point2d@endlink): .
        """
        pass
    
    ##  Gets the start Node of this connection. 
    ##         Note: When the builder is commited, a dynamic Port will be used and can be found in the GetStart method
    ##  @return node (@link Node NXOpen.Schematic.Node@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetStartNode(builder: ConnectionBuilder) -> Node:
        """
         Gets the start Node of this connection. 
                Note: When the builder is commited, a dynamic Port will be used and can be found in the GetStart method
         @return node (@link Node NXOpen.Schematic.Node@endlink): .
        """
        pass
    
    ##  Get the connection location for tee object at the end of the connection. 
    ##  @return A tuple consisting of (connection, segmentId, percent). 
    ##  - connection is: @link Connection NXOpen.Schematic.Connection@endlink.
    ##  - segmentId is: int.
    ##  - percent is: float.

    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetTeeEndLocation(builder: ConnectionBuilder) -> Tuple[Connection, int, float]:
        """
         Get the connection location for tee object at the end of the connection. 
         @return A tuple consisting of (connection, segmentId, percent). 
         - connection is: @link Connection NXOpen.Schematic.Connection@endlink.
         - segmentId is: int.
         - percent is: float.

        """
        pass
    
    ##  Get the connection location for tee object at the start of the connection. 
    ##  @return A tuple consisting of (connection, segmentId, percent). 
    ##  - connection is: @link Connection NXOpen.Schematic.Connection@endlink.
    ##  - segmentId is: int.
    ##  - percent is: float.

    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetTeeStartLocation(builder: ConnectionBuilder) -> Tuple[Connection, int, float]:
        """
         Get the connection location for tee object at the start of the connection. 
         @return A tuple consisting of (connection, segmentId, percent). 
         - connection is: @link Connection NXOpen.Schematic.Connection@endlink.
         - segmentId is: int.
         - percent is: float.

        """
        pass
    
    ##  Set bending points for polyline to render the connection. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="points"> (@link NXOpen.Point2d List[NXOpen.Point2d]@endlink) </param>
    def SetBendPoints(builder: ConnectionBuilder, points: List[NXOpen.Point2d]) -> None:
        """
         Set bending points for polyline to render the connection. 
        """
        pass
    
    ##  Sets the end port of this connection.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="port"> (@link Port NXOpen.Schematic.Port@endlink) </param>
    def SetEnd(builder: ConnectionBuilder, port: Port) -> None:
        """
         Sets the end port of this connection.
        """
        pass
    
    ##  Set the end location of this connection.
    ##             This end location is applicable only when the @link Diagramming::ConnectionBuilder::End Diagramming::ConnectionBuilder::End@endlink  port is NULL. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="endLocation"> (@link NXOpen.Point2d NXOpen.Point2d@endlink) </param>
    def SetEndLocation(builder: ConnectionBuilder, endLocation: NXOpen.Point2d) -> None:
        """
         Set the end location of this connection.
                    This end location is applicable only when the @link Diagramming::ConnectionBuilder::End Diagramming::ConnectionBuilder::End@endlink  port is NULL. 
        """
        pass
    
    ##  Sets the end Node of this connection.
    ##         Note: When the builder is commited, a Dynamic Port will be created based on the the other inputs.
    ##         This dynamic Port can be found in the GetEnd method
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="node"> (@link Node NXOpen.Schematic.Node@endlink) </param>
    ## <param name="percentX"> (float) </param>
    ## <param name="percentY"> (float) </param>
    ## <param name="offsetX"> (float) </param>
    ## <param name="offsetY"> (float) </param>
    ## <param name="connectionDirectionX"> (float) </param>
    ## <param name="connectionDirectionY"> (float) </param>
    ## <param name="trimPolicy"> (@link ConnectionTrimPolicyType NXOpen.Schematic.ConnectionTrimPolicyType@endlink) </param>
    def SetEndNode(builder: ConnectionBuilder, node: Node, percentX: float, percentY: float, offsetX: float, offsetY: float, connectionDirectionX: float, connectionDirectionY: float, trimPolicy: ConnectionTrimPolicyType) -> None:
        """
         Sets the end Node of this connection.
                Note: When the builder is commited, a Dynamic Port will be created based on the the other inputs.
                This dynamic Port can be found in the GetEnd method
        """
        pass
    
    ##  Sets the line type of the connection. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="lineType"> (str) </param>
    def SetLineType(builder: ConnectionBuilder, lineType: str) -> None:
        """
         Sets the line type of the connection. 
        """
        pass
    
    ##  Sets the start port of this connection in native. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="port"> (@link Port NXOpen.Schematic.Port@endlink) </param>
    def SetStart(builder: ConnectionBuilder, port: Port) -> None:
        """
         Sets the start port of this connection in native. 
        """
        pass
    
    ##  Set the start location of this connection.
    ##             This start location is applicable only when the @link Diagramming::ConnectionBuilder::Start Diagramming::ConnectionBuilder::Start@endlink  is NULL.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="startLocation"> (@link NXOpen.Point2d NXOpen.Point2d@endlink) </param>
    def SetStartLocation(builder: ConnectionBuilder, startLocation: NXOpen.Point2d) -> None:
        """
         Set the start location of this connection.
                    This start location is applicable only when the @link Diagramming::ConnectionBuilder::Start Diagramming::ConnectionBuilder::Start@endlink  is NULL.
        """
        pass
    
    ##  Sets the start Node of this connection. 
    ##         Note: When the builder is commited, a Dynamic Port will be created based on the the other inputs. 
    ##         This dynamic Port can be found in the GetStart method
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="node"> (@link Node NXOpen.Schematic.Node@endlink) </param>
    ## <param name="percentX"> (float) </param>
    ## <param name="percentY"> (float) </param>
    ## <param name="offsetX"> (float) </param>
    ## <param name="offsetY"> (float) </param>
    ## <param name="connectionDirectionX"> (float) </param>
    ## <param name="connectionDirectionY"> (float) </param>
    ## <param name="trimPolicy"> (@link ConnectionTrimPolicyType NXOpen.Schematic.ConnectionTrimPolicyType@endlink) </param>
    def SetStartNode(builder: ConnectionBuilder, node: Node, percentX: float, percentY: float, offsetX: float, offsetY: float, connectionDirectionX: float, connectionDirectionY: float, trimPolicy: ConnectionTrimPolicyType) -> None:
        """
         Sets the start Node of this connection. 
                Note: When the builder is commited, a Dynamic Port will be created based on the the other inputs. 
                This dynamic Port can be found in the GetStart method
        """
        pass
    
    ##  Set the connection location for tee object at the end of the connection. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="connection"> (@link Connection NXOpen.Schematic.Connection@endlink) </param>
    ## <param name="segmentId"> (int) </param>
    ## <param name="percent"> (float) </param>
    def SetTeeEndLocation(builder: ConnectionBuilder, connection: Connection, segmentId: int, percent: float) -> None:
        """
         Set the connection location for tee object at the end of the connection. 
        """
        pass
    
    ##  Set the connection location for tee object at the start of the connection. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="connection"> (@link Connection NXOpen.Schematic.Connection@endlink) </param>
    ## <param name="segmentId"> (int) </param>
    ## <param name="percent"> (float) </param>
    def SetTeeStartLocation(builder: ConnectionBuilder, connection: Connection, segmentId: int, percent: float) -> None:
        """
         Set the connection location for tee object at the start of the connection. 
        """
        pass
    
import NXOpen
##  Represents a collection of Schematic.Connection.  <br> To obtain an instance of this class, refer to @link NXOpen::Schematic::SchematicManager  NXOpen::Schematic::SchematicManager @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class ConnectionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Schematic.Connection. """


    ##  Finds the @link Schematic::Connection Schematic::Connection@endlink  with the given identifier as recorded in a journal.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return connection (@link Connection NXOpen.Schematic.Connection@endlink):  @link Schematic::Connection Schematic::Connection@endlink  with this name. .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ##  Identifier to be found 
    def FindObject(part: ConnectionCollection, journalIdentifier: str) -> Connection:
        """
         Finds the @link Schematic::Connection Schematic::Connection@endlink  with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         @return connection (@link Connection NXOpen.Schematic.Connection@endlink):  @link Schematic::Connection Schematic::Connection@endlink  with this name. .
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##   @brief  Represents a ConnectionDataBuilder.  
## 
##   
## 
##   <br>  Created in NX2306.0.0  <br> 

class ConnectionDataBuilder(NXOpen.TaggedObject): 
    """ <summary> Represents a ConnectionDataBuilder. </summary> """


    ## Getter for property: (str) InsulationId
    ##   the insulation id.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def InsulationId(self) -> str:
        """
        Getter for property: (str) InsulationId
          the insulation id.  
             
         
        """
        pass
    
    ## Setter for property: (str) InsulationId

    ##   the insulation id.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @InsulationId.setter
    def InsulationId(self, insulationId: str):
        """
        Setter for property: (str) InsulationId
          the insulation id.  
             
         
        """
        pass
    
    ## Getter for property: (str) StockId
    ##   the stock id.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def StockId(self) -> str:
        """
        Getter for property: (str) StockId
          the stock id.  
             
         
        """
        pass
    
    ## Setter for property: (str) StockId

    ##   the stock id.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @StockId.setter
    def StockId(self, stockId: str):
        """
        Setter for property: (str) StockId
          the stock id.  
             
         
        """
        pass
    
    ##  Gets the attribute owner of the object.
    ##  @return owner (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sourceType"> (@link ConnectionAttributeSourceType NXOpen.Schematic.ConnectionAttributeSourceType@endlink) </param>
    def GetSourceAttributeOwner(builder: ConnectionDataBuilder, sourceType: ConnectionAttributeSourceType) -> NXOpen.NXObject:
        """
         Gets the attribute owner of the object.
         @return owner (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
        """
        pass
    
##  Represents the connection end type. 
##  The start of connection. 
class ConnectionEndType(Enum):
    """
    Members Include: <Start> <End>
    """
    Start: int
    End: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ConnectionEndType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


## Represents the Connection TrimPolicy type. 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## NodeAndPort</term><description> 
## </description> </item><item><term> 
## Port</term><description> 
## </description> </item><item><term> 
## Node</term><description> 
## </description> </item><item><term> 
## NoTrim</term><description> 
## </description> </item></list>
class ConnectionTrimPolicyType(Enum):
    """
    Members Include: <NodeAndPort> <Port> <Node> <NoTrim>
    """
    NodeAndPort: int
    Port: int
    Node: int
    NoTrim: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ConnectionTrimPolicyType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  Represents the schematic connection class.  <br> To create or edit an instance of this class, use @link NXOpen::Schematic::ConnectionBuilder  NXOpen::Schematic::ConnectionBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class Connection(NXOpen.NXObject): 
    """ Represents the schematic connection class. """


    ##  Detaches from the Port and optionally, allow port deletion if it was dynamically created. 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="port"> (@link Port NXOpen.Schematic.Port@endlink) </param>
    def Detach(connection: Connection, port: Port) -> None:
        """
         Detaches from the Port and optionally, allow port deletion if it was dynamically created. 
        """
        pass
    
    ##  Refreshes the connection. 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Refresh(connection: Connection) -> None:
        """
         Refreshes the connection. 
        """
        pass
    
    ##  Reverses the offset direction of the auxiliary line along the connection. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def ReverseAuxiliaryLine(connection: Connection) -> None:
        """
         Reverses the offset direction of the auxiliary line along the connection. 
        """
        pass
    
import NXOpen
##   @brief  Represents a DesignValidationBuilder.  
## 
##    <br> To create a new instance of this class, use @link NXOpen::Schematic::SchematicManager::CreateDesignValidationBuilder  NXOpen::Schematic::SchematicManager::CreateDesignValidationBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class DesignValidationBuilder(NXOpen.Builder): 
    """ <summary> Represents a DesignValidationBuilder. </summary> """


    ## Getter for property: (bool) SaveResult
    ##   the option to save validation result   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def SaveResult(self) -> bool:
        """
        Getter for property: (bool) SaveResult
          the option to save validation result   
            
         
        """
        pass
    
    ## Setter for property: (bool) SaveResult

    ##   the option to save validation result   
    ##     
    ##  
    ## Setter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @SaveResult.setter
    def SaveResult(self, saveResult: bool):
        """
        Setter for property: (bool) SaveResult
          the option to save validation result   
            
         
        """
        pass
    
    ##  Gets the selected checker ids 
    ##  @return selectedCheckerIds (List[str]):  A list of checker ids .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectedCheckerIds(builder: DesignValidationBuilder) -> List[str]:
        """
         Gets the selected checker ids 
         @return selectedCheckerIds (List[str]):  A list of checker ids .
        """
        pass
    
    ##  Specifies the selected checker ids 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_diagramming ("NX Diagramming")
    ##  A list of checker ids 
    def SetSelectedCheckerIds(builder: DesignValidationBuilder, selectedCheckerIds: List[str]) -> None:
        """
         Specifies the selected checker ids 
        """
        pass
    
## Represents the equipment attribute source type. 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Object</term><description> 
## </description> </item><item><term> 
## Classification</term><description> 
## </description> </item></list>
class EquipmentAttributeSourceType(Enum):
    """
    Members Include: <Object> <Classification>
    """
    Object: int
    Classification: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> EquipmentAttributeSourceType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  Represents a builder class that performs New Sheet operations.  <br> To create a new instance of this class, use @link NXOpen::Schematic::SystemManager::CreateFileNewApplicationBuilder  NXOpen::Schematic::SystemManager::CreateFileNewApplicationBuilder @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class FileNewApplicationBuilder(NXOpen.Builder): 
    """ Represents a builder class that performs New Sheet operations. """


    ## Getter for property: (@link NXOpen.FileNew NXOpen.FileNew@endlink) FileNew
    ##   the file new object   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.FileNew
    @property
    def FileNew(self) -> NXOpen.FileNew:
        """
        Getter for property: (@link NXOpen.FileNew NXOpen.FileNew@endlink) FileNew
          the file new object   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.FileNew NXOpen.FileNew@endlink) FileNew

    ##   the file new object   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @FileNew.setter
    def FileNew(self, fileNew: NXOpen.FileNew):
        """
        Setter for property: (@link NXOpen.FileNew NXOpen.FileNew@endlink) FileNew
          the file new object   
            
         
        """
        pass
    
    ##  Set the system object of sheet 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="systemSpec"> (str) </param>
    def SetSystem(builder: FileNewApplicationBuilder, systemSpec: str) -> None:
        """
         Set the system object of sheet 
        """
        pass
    
import NXOpen
##   @brief 
##     Represents FlowDirectionArrowBuilder  
## 
##  
##       <br> To create a new instance of this class, use @link NXOpen::Schematic::SchematicManager::CreateFdaBuilder  NXOpen::Schematic::SchematicManager::CreateFdaBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class FlowDirectionArrowBuilder(NXOpen.Builder): 
    """ <summary>
    Represents FlowDirectionArrowBuilder </summary>
     """


    ## Getter for property: (float) LocationPercent
    ##   the percent along the segment for this Flow Direction Arrow.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return float
    @property
    def LocationPercent(self) -> float:
        """
        Getter for property: (float) LocationPercent
          the percent along the segment for this Flow Direction Arrow.  
             
         
        """
        pass
    
    ## Setter for property: (float) LocationPercent

    ##   the percent along the segment for this Flow Direction Arrow.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @LocationPercent.setter
    def LocationPercent(self, locationPercent: float):
        """
        Setter for property: (float) LocationPercent
          the percent along the segment for this Flow Direction Arrow.  
             
         
        """
        pass
    
    ## Getter for property: (int) LocationSegment
    ##   the segment this Flow Direction Arrow is located on.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return int
    @property
    def LocationSegment(self) -> int:
        """
        Getter for property: (int) LocationSegment
          the segment this Flow Direction Arrow is located on.  
             
         
        """
        pass
    
    ## Setter for property: (int) LocationSegment

    ##   the segment this Flow Direction Arrow is located on.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @LocationSegment.setter
    def LocationSegment(self, locationPercent: int):
        """
        Setter for property: (int) LocationSegment
          the segment this Flow Direction Arrow is located on.  
             
         
        """
        pass
    
    ##  Gets the connection for this Flow Direction Arrow. 
    ##  @return connection (@link Connection NXOpen.Schematic.Connection@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetConnection(builder: FlowDirectionArrowBuilder) -> Connection:
        """
         Gets the connection for this Flow Direction Arrow. 
         @return connection (@link Connection NXOpen.Schematic.Connection@endlink): .
        """
        pass
    
    ##  Change the direction of FDA. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def ReverseDirection(builder: FlowDirectionArrowBuilder) -> None:
        """
         Change the direction of FDA. 
        """
        pass
    
    ##  Sets the connection for this Flow Direction Arrow. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="connection"> (@link Connection NXOpen.Schematic.Connection@endlink) </param>
    def SetConnection(builder: FlowDirectionArrowBuilder, connection: Connection) -> None:
        """
         Sets the connection for this Flow Direction Arrow. 
        """
        pass
    
import NXOpen
##   @brief  A symbol that indicates the direction the of the flow 
## 
##    <br> To create or edit an instance of this class, use @link NXOpen::Schematic::FlowDirectionArrowBuilder  NXOpen::Schematic::FlowDirectionArrowBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class FlowDirectionArrow(NXOpen.NXObject): 
    """ <summary> A symbol that indicates the direction the of the flow</summary> """
    pass


## Represents the instrumentation symbol type. 
##  discrete instrument and primary location. 
class InstrumentationSymbolType(Enum):
    """
    Members Include: <DiscreteInstrumentPrimaryLocation> <DiscreteInstrumentFieldMounted> <DiscreteInstrumentAuxiliaryLocation> <SharedDisplaySharedControlPrimaryLocation> <SharedDisplaySharedControlFieldMounted> <SharedDisplaySharedControlAuxiliaryLocation> <ComputerFunctionPrimaryLocation> <ComputerFunctionFieldMounted> <ComputerFunctionAuxiliaryLocation> <ProgrammableLogicControlPrimaryLocation> <ProgrammableLogicControlFieldMounted> <ProgrammableLogicControlAuxiliaryLocation>
    """
    DiscreteInstrumentPrimaryLocation: int
    DiscreteInstrumentFieldMounted: int
    DiscreteInstrumentAuxiliaryLocation: int
    SharedDisplaySharedControlPrimaryLocation: int
    SharedDisplaySharedControlFieldMounted: int
    SharedDisplaySharedControlAuxiliaryLocation: int
    ComputerFunctionPrimaryLocation: int
    ComputerFunctionFieldMounted: int
    ComputerFunctionAuxiliaryLocation: int
    ProgrammableLogicControlPrimaryLocation: int
    ProgrammableLogicControlFieldMounted: int
    ProgrammableLogicControlAuxiliaryLocation: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> InstrumentationSymbolType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


## Represents the instrumentation type. 
##  not a instrumentation. 
class InstrumentationType(Enum):
    """
    Members Include: <NotSet> <Symbol>
    """
    NotSet: int
    Symbol: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> InstrumentationType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents the property type. 
##  Null type 
class JaSchematicPropertytype(Enum):
    """
    Members Include: <Null> <Index> <UserAttribute> <Id> <Name> <Symbol> <SymbolDescription> <Quantity> <ParentRun> <RunAttribute> <EquipmentAttribute> <PipeAttribute> <BranchAttribute>
    """
    Null: int
    Index: int
    UserAttribute: int
    Id: int
    Name: int
    Symbol: int
    SymbolDescription: int
    Quantity: int
    ParentRun: int
    RunAttribute: int
    EquipmentAttribute: int
    PipeAttribute: int
    BranchAttribute: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> JaSchematicPropertytype:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
import NXOpen.Diagramming
##   @brief  Represents a NodeBuilder.  
## 
##    <br> To create a new instance of this class, use @link NXOpen::Schematic::SchematicManager::CreateNodeBuilder  NXOpen::Schematic::SchematicManager::CreateNodeBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## InstrumentSymbolSize </term> <description> 
##  
## 15 </description> </item> 
## 
## <item><term> 
##  
## Rotate </term> <description> 
##  
## Zero </description> </item> 
## 
## <item><term> 
##  
## SymbolSourceType </term> <description> 
##  
## ReuseLibrary </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1980.0.0  <br> 

class NodeBuilder(BaseObjectBuilder): 
    """ <summary> Represents a NodeBuilder. </summary> """


    ## Getter for property: (@link NXOpen.Diagramming.Node NXOpen.Diagramming.Node@endlink) ExistingSymbol
    ##   the symbol from foundation window.  
    ##    It is only applicable when @link Schematic::NodeBuilder::SymbolSourceType Schematic::NodeBuilder::SymbolSourceType@endlink  is @link Schematic::SymbolSourceOptionExistingSymbol Schematic::SymbolSourceOptionExistingSymbol@endlink .  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Diagramming.Node
    @property
    def ExistingSymbol(self) -> NXOpen.Diagramming.Node:
        """
        Getter for property: (@link NXOpen.Diagramming.Node NXOpen.Diagramming.Node@endlink) ExistingSymbol
          the symbol from foundation window.  
           It is only applicable when @link Schematic::NodeBuilder::SymbolSourceType Schematic::NodeBuilder::SymbolSourceType@endlink  is @link Schematic::SymbolSourceOptionExistingSymbol Schematic::SymbolSourceOptionExistingSymbol@endlink .  
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Diagramming.Node NXOpen.Diagramming.Node@endlink) ExistingSymbol

    ##   the symbol from foundation window.  
    ##    It is only applicable when @link Schematic::NodeBuilder::SymbolSourceType Schematic::NodeBuilder::SymbolSourceType@endlink  is @link Schematic::SymbolSourceOptionExistingSymbol Schematic::SymbolSourceOptionExistingSymbol@endlink .  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ExistingSymbol.setter
    def ExistingSymbol(self, existingSymbol: NXOpen.Diagramming.Node):
        """
        Setter for property: (@link NXOpen.Diagramming.Node NXOpen.Diagramming.Node@endlink) ExistingSymbol
          the symbol from foundation window.  
           It is only applicable when @link Schematic::NodeBuilder::SymbolSourceType Schematic::NodeBuilder::SymbolSourceType@endlink  is @link Schematic::SymbolSourceOptionExistingSymbol Schematic::SymbolSourceOptionExistingSymbol@endlink .  
         
        """
        pass
    
    ## Getter for property: (bool) FlipHorizontal
    ##   the option to flip the symbol horizontally.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def FlipHorizontal(self) -> bool:
        """
        Getter for property: (bool) FlipHorizontal
          the option to flip the symbol horizontally.  
             
         
        """
        pass
    
    ## Setter for property: (bool) FlipHorizontal

    ##   the option to flip the symbol horizontally.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @FlipHorizontal.setter
    def FlipHorizontal(self, flipHorizontal: bool):
        """
        Setter for property: (bool) FlipHorizontal
          the option to flip the symbol horizontally.  
             
         
        """
        pass
    
    ## Getter for property: (bool) FlipVertical
    ##   the option to flip the symbol vertically.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def FlipVertical(self) -> bool:
        """
        Getter for property: (bool) FlipVertical
          the option to flip the symbol vertically.  
             
         
        """
        pass
    
    ## Setter for property: (bool) FlipVertical

    ##   the option to flip the symbol vertically.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @FlipVertical.setter
    def FlipVertical(self, flipVertical: bool):
        """
        Setter for property: (bool) FlipVertical
          the option to flip the symbol vertically.  
             
         
        """
        pass
    
    ## Getter for property: (bool) LockAspectRatio
    ##   the option to lock the aspect ratio.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def LockAspectRatio(self) -> bool:
        """
        Getter for property: (bool) LockAspectRatio
          the option to lock the aspect ratio.  
             
         
        """
        pass
    
    ## Setter for property: (bool) LockAspectRatio

    ##   the option to lock the aspect ratio.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @LockAspectRatio.setter
    def LockAspectRatio(self, lockAspectRatio: bool):
        """
        Setter for property: (bool) LockAspectRatio
          the option to lock the aspect ratio.  
             
         
        """
        pass
    
    ## Getter for property: (@link NodeType NXOpen.Schematic.NodeType@endlink) NodeType
    ##   the node type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NodeType
    @property
    def NodeType(self) -> NodeType:
        """
        Getter for property: (@link NodeType NXOpen.Schematic.NodeType@endlink) NodeType
          the node type.  
             
         
        """
        pass
    
    ## Setter for property: (@link NodeType NXOpen.Schematic.NodeType@endlink) NodeType

    ##   the node type.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @NodeType.setter
    def NodeType(self, nodeType: NodeType):
        """
        Setter for property: (@link NodeType NXOpen.Schematic.NodeType@endlink) NodeType
          the node type.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Diagramming.LocationBuilder NXOpen.Diagramming.LocationBuilder@endlink) RelativeLocation
    ##   the node relative location.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Diagramming.LocationBuilder
    @property
    def RelativeLocation(self) -> NXOpen.Diagramming.LocationBuilder:
        """
        Getter for property: (@link NXOpen.Diagramming.LocationBuilder NXOpen.Diagramming.LocationBuilder@endlink) RelativeLocation
          the node relative location.  
             
         
        """
        pass
    
    ## Getter for property: (@link RotateAngleOption NXOpen.Schematic.RotateAngleOption@endlink) Rotate
    ##   the symbol rotation angle.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return RotateAngleOption
    @property
    def Rotate(self) -> RotateAngleOption:
        """
        Getter for property: (@link RotateAngleOption NXOpen.Schematic.RotateAngleOption@endlink) Rotate
          the symbol rotation angle.  
             
         
        """
        pass
    
    ## Setter for property: (@link RotateAngleOption NXOpen.Schematic.RotateAngleOption@endlink) Rotate

    ##   the symbol rotation angle.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @Rotate.setter
    def Rotate(self, rotate: RotateAngleOption):
        """
        Setter for property: (@link RotateAngleOption NXOpen.Schematic.RotateAngleOption@endlink) Rotate
          the symbol rotation angle.  
             
         
        """
        pass
    
    ## Getter for property: (float) Scale
    ##   the scale value.  
    ##    It is only applicable when @link Schematic::NodeBuilder::LockAspectRatio Schematic::NodeBuilder::LockAspectRatio@endlink  is true.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return float
    @property
    def Scale(self) -> float:
        """
        Getter for property: (float) Scale
          the scale value.  
           It is only applicable when @link Schematic::NodeBuilder::LockAspectRatio Schematic::NodeBuilder::LockAspectRatio@endlink  is true.  
         
        """
        pass
    
    ## Setter for property: (float) Scale

    ##   the scale value.  
    ##    It is only applicable when @link Schematic::NodeBuilder::LockAspectRatio Schematic::NodeBuilder::LockAspectRatio@endlink  is true.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @Scale.setter
    def Scale(self, scale: float):
        """
        Setter for property: (float) Scale
          the scale value.  
           It is only applicable when @link Schematic::NodeBuilder::LockAspectRatio Schematic::NodeBuilder::LockAspectRatio@endlink  is true.  
         
        """
        pass
    
    ## Getter for property: (float) ScaleX
    ##   the x scale value.  
    ##    It is only applicable when @link Schematic::NodeBuilder::LockAspectRatio Schematic::NodeBuilder::LockAspectRatio@endlink  is false.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return float
    @property
    def ScaleX(self) -> float:
        """
        Getter for property: (float) ScaleX
          the x scale value.  
           It is only applicable when @link Schematic::NodeBuilder::LockAspectRatio Schematic::NodeBuilder::LockAspectRatio@endlink  is false.  
         
        """
        pass
    
    ## Setter for property: (float) ScaleX

    ##   the x scale value.  
    ##    It is only applicable when @link Schematic::NodeBuilder::LockAspectRatio Schematic::NodeBuilder::LockAspectRatio@endlink  is false.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ScaleX.setter
    def ScaleX(self, scaleX: float):
        """
        Setter for property: (float) ScaleX
          the x scale value.  
           It is only applicable when @link Schematic::NodeBuilder::LockAspectRatio Schematic::NodeBuilder::LockAspectRatio@endlink  is false.  
         
        """
        pass
    
    ## Getter for property: (float) ScaleY
    ##   the y scale value.  
    ##    It is only applicable when @link Schematic::NodeBuilder::LockAspectRatio Schematic::NodeBuilder::LockAspectRatio@endlink  is false.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return float
    @property
    def ScaleY(self) -> float:
        """
        Getter for property: (float) ScaleY
          the y scale value.  
           It is only applicable when @link Schematic::NodeBuilder::LockAspectRatio Schematic::NodeBuilder::LockAspectRatio@endlink  is false.  
         
        """
        pass
    
    ## Setter for property: (float) ScaleY

    ##   the y scale value.  
    ##    It is only applicable when @link Schematic::NodeBuilder::LockAspectRatio Schematic::NodeBuilder::LockAspectRatio@endlink  is false.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ScaleY.setter
    def ScaleY(self, scaleY: float):
        """
        Setter for property: (float) ScaleY
          the y scale value.  
           It is only applicable when @link Schematic::NodeBuilder::LockAspectRatio Schematic::NodeBuilder::LockAspectRatio@endlink  is false.  
         
        """
        pass
    
    ## Getter for property: (@link Connection NXOpen.Schematic.Connection@endlink) SplittedConnection
    ##   the new created connection after breaking the old connection.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return Connection
    @property
    def SplittedConnection(self) -> Connection:
        """
        Getter for property: (@link Connection NXOpen.Schematic.Connection@endlink) SplittedConnection
          the new created connection after breaking the old connection.  
             
         
        """
        pass
    
    ## Getter for property: (str) SymbolId
    ##   the symbol ID of this node.  
    ##    It is only applicable when @link NXOpen::Schematic::NodeBuilder::SymbolSourceType NXOpen::Schematic::NodeBuilder::SymbolSourceType@endlink  is @link NXOpen::Schematic::SymbolSourceOptionReuseLibrary NXOpen::Schematic::SymbolSourceOptionReuseLibrary@endlink .  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def SymbolId(self) -> str:
        """
        Getter for property: (str) SymbolId
          the symbol ID of this node.  
           It is only applicable when @link NXOpen::Schematic::NodeBuilder::SymbolSourceType NXOpen::Schematic::NodeBuilder::SymbolSourceType@endlink  is @link NXOpen::Schematic::SymbolSourceOptionReuseLibrary NXOpen::Schematic::SymbolSourceOptionReuseLibrary@endlink .  
         
        """
        pass
    
    ## Setter for property: (str) SymbolId

    ##   the symbol ID of this node.  
    ##    It is only applicable when @link NXOpen::Schematic::NodeBuilder::SymbolSourceType NXOpen::Schematic::NodeBuilder::SymbolSourceType@endlink  is @link NXOpen::Schematic::SymbolSourceOptionReuseLibrary NXOpen::Schematic::SymbolSourceOptionReuseLibrary@endlink .  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @SymbolId.setter
    def SymbolId(self, symbolId: str):
        """
        Setter for property: (str) SymbolId
          the symbol ID of this node.  
           It is only applicable when @link NXOpen::Schematic::NodeBuilder::SymbolSourceType NXOpen::Schematic::NodeBuilder::SymbolSourceType@endlink  is @link NXOpen::Schematic::SymbolSourceOptionReuseLibrary NXOpen::Schematic::SymbolSourceOptionReuseLibrary@endlink .  
         
        """
        pass
    
    ## Getter for property: (@link SymbolSourceOption NXOpen.Schematic.SymbolSourceOption@endlink) SymbolSourceType
    ##   the symbol source type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return SymbolSourceOption
    @property
    def SymbolSourceType(self) -> SymbolSourceOption:
        """
        Getter for property: (@link SymbolSourceOption NXOpen.Schematic.SymbolSourceOption@endlink) SymbolSourceType
          the symbol source type   
            
         
        """
        pass
    
    ## Setter for property: (@link SymbolSourceOption NXOpen.Schematic.SymbolSourceOption@endlink) SymbolSourceType

    ##   the symbol source type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @SymbolSourceType.setter
    def SymbolSourceType(self, symbolSourceType: SymbolSourceOption):
        """
        Setter for property: (@link SymbolSourceOption NXOpen.Schematic.SymbolSourceOption@endlink) SymbolSourceType
          the symbol source type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Diagramming.TextStyleBuilder NXOpen.Diagramming.TextStyleBuilder@endlink) TextStyle
    ##   the text style   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Diagramming.TextStyleBuilder
    @property
    def TextStyle(self) -> NXOpen.Diagramming.TextStyleBuilder:
        """
        Getter for property: (@link NXOpen.Diagramming.TextStyleBuilder NXOpen.Diagramming.TextStyleBuilder@endlink) TextStyle
          the text style   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseExistingSymbolId
    ##   the option to place a symbol referencing an existing equipment.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def UseExistingSymbolId(self) -> bool:
        """
        Getter for property: (bool) UseExistingSymbolId
          the option to place a symbol referencing an existing equipment.  
             
         
        """
        pass
    
    ## Setter for property: (bool) UseExistingSymbolId

    ##   the option to place a symbol referencing an existing equipment.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @UseExistingSymbolId.setter
    def UseExistingSymbolId(self, useExistingID: bool):
        """
        Setter for property: (bool) UseExistingSymbolId
          the option to place a symbol referencing an existing equipment.  
             
         
        """
        pass
    
    ##  Detaches the equipment from all attached connections. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def DetachAllConnections(builder: NodeBuilder) -> None:
        """
         Detaches the equipment from all attached connections. 
        """
        pass
    
    ##  Detaches specific port on node
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="portId"> (str) </param>
    def DetachPortOnNode(builder: NodeBuilder, portId: str) -> None:
        """
         Detaches specific port on node
        """
        pass
    
    ##  Gets connection location for the inline symbol. 
    ##  @return A tuple consisting of (connection, segementId, percent). 
    ##  - connection is: @link Connection NXOpen.Schematic.Connection@endlink.
    ##  - segementId is: int.
    ##  - percent is: float.

    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetInlineSymbolLocation(builder: NodeBuilder) -> Tuple[Connection, int, float]:
        """
         Gets connection location for the inline symbol. 
         @return A tuple consisting of (connection, segementId, percent). 
         - connection is: @link Connection NXOpen.Schematic.Connection@endlink.
         - segementId is: int.
         - percent is: float.

        """
        pass
    
    ##  Gets the symbol location. 
    ##  @return location (@link NXOpen.Point2d NXOpen.Point2d@endlink):  the symbol location. .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLocation(builder: NodeBuilder) -> NXOpen.Point2d:
        """
         Gets the symbol location. 
         @return location (@link NXOpen.Point2d NXOpen.Point2d@endlink):  the symbol location. .
        """
        pass
    
    ##  Gets new connection after inserting an inline symbol.
    ##  @return A tuple consisting of (con, connectionId). 
    ##  - con is: @link NXOpen.NXObject NXOpen.NXObject@endlink.
    ##  - connectionId is: str.

    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetNewInlineConnection(builder: NodeBuilder) -> Tuple[NXOpen.NXObject, str]:
        """
         Gets new connection after inserting an inline symbol.
         @return A tuple consisting of (con, connectionId). 
         - con is: @link NXOpen.NXObject NXOpen.NXObject@endlink.
         - connectionId is: str.

        """
        pass
    
    ##  Get the node object of the equipment builder. 
    ##  @return node (@link NXOpen.Diagramming.Node NXOpen.Diagramming.Node@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetNode(builder: NodeBuilder) -> NXOpen.Diagramming.Node:
        """
         Get the node object of the equipment builder. 
         @return node (@link NXOpen.Diagramming.Node NXOpen.Diagramming.Node@endlink): .
        """
        pass
    
    ##  Gets the attribute owner of the object.
    ##  @return owner (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sourceType"> (@link EquipmentAttributeSourceType NXOpen.Schematic.EquipmentAttributeSourceType@endlink) </param>
    def GetSourceAttributeOwner(builder: NodeBuilder, sourceType: EquipmentAttributeSourceType) -> NXOpen.NXObject:
        """
         Gets the attribute owner of the object.
         @return owner (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
        """
        pass
    
    ##  Replaces the symbol of this node to another one. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="symbolId"> (str) </param>
    def ReplaceSymbol(builder: NodeBuilder, symbolId: str) -> None:
        """
         Replaces the symbol of this node to another one. 
        """
        pass
    
    ##  Sets target port attaching to source port. 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ##  the port id of this equipment symbol for the attachment. 
    def SetAttachedSymbol(builder: NodeBuilder, sourcePortId: str, toSymbol: Node, targetPortId: str) -> None:
        """
         Sets target port attaching to source port. 
        """
        pass
    
    ##  Sets connection location for the inline symbol. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="connection"> (@link Connection NXOpen.Schematic.Connection@endlink) </param>
    ## <param name="segementId"> (int) </param>
    ## <param name="percent"> (float) </param>
    def SetInlineSymbolLocation(builder: NodeBuilder, connection: Connection, segementId: int, percent: float) -> None:
        """
         Sets connection location for the inline symbol. 
        """
        pass
    
    ##  Sets the symbol location. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ##  the symbol location. 
    def SetLocation(builder: NodeBuilder, location: NXOpen.Point2d) -> None:
        """
         Sets the symbol location. 
        """
        pass
    
import NXOpen
##  Represents a collection of Schematic.Node.  <br> To obtain an instance of this class, refer to @link NXOpen::Schematic::SchematicManager  NXOpen::Schematic::SchematicManager @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class NodeCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Schematic.Node. """


    ##  Finds the @link Schematic::Node Schematic::Node@endlink  with the given identifier as recorded in a journal.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return node (@link Node NXOpen.Schematic.Node@endlink):  @link Schematic::Node Schematic::Node@endlink  with this name. .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ##  Identifier to be found 
    def FindObject(part: NodeCollection, journalIdentifier: str) -> Node:
        """
         Finds the @link Schematic::Node Schematic::Node@endlink  with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         @return node (@link Node NXOpen.Schematic.Node@endlink):  @link Schematic::Node Schematic::Node@endlink  with this name. .
        """
        pass
    
##  Represents the node type. 
##  default node. 
class NodeType(Enum):
    """
    Members Include: <Default> <Fitting>
    """
    Default: int
    Fitting: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> NodeType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  Represents the schematic node class.  <br> To create or edit an instance of this class, use @link NXOpen::Schematic::NodeBuilder  NXOpen::Schematic::NodeBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class Node(NXOpen.NXObject): 
    """ Represents the schematic node class. """


    ##  Refresh the node display. 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Refresh(node: Node) -> None:
        """
         Refresh the node display. 
        """
        pass
    
import NXOpen
##   @brief  Represents a ObjectTableBuilder.  
## 
##    <br> To create a new instance of this class, use @link NXOpen::Schematic::SchematicManager::CreateObjectTableBuilder  NXOpen::Schematic::SchematicManager::CreateObjectTableBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## StockType </term> <description> 
##  
## Pipe </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2212.0.0  <br> 

class ObjectTableBuilder(NXOpen.Builder): 
    """ <summary> Represents a ObjectTableBuilder. </summary> """


    ##  Represents the stock type. 
    ##  Pipe Stock 
    class StockOption(Enum):
        """
        Members Include: <Pipe> <Hvac>
        """
        Pipe: int
        Hvac: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ObjectTableBuilder.StockOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
import NXOpen
##  Represents a collection of ObjectTable.  <br> To obtain an instance of this class, refer to @link NXOpen::Schematic::Sheet  NXOpen::Schematic::Sheet @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ObjectTableCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of ObjectTable. """
    pass


import NXOpen
##   @brief  the object table for Schematic objects  
## 
##    <br> To create or edit an instance of this class, use @link NXOpen::Schematic::ObjectTableBuilder  NXOpen::Schematic::ObjectTableBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ObjectTable(NXOpen.NXObject): 
    """ <summary> the object table for Schematic objects </summary> """


    ##  Refreshes the table contents. 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Refresh(objectTable: ObjectTable) -> None:
        """
         Refreshes the table contents. 
        """
        pass
    
import NXOpen
import NXOpen.Diagramming
##   @brief 
##     Builder used to model a piece of Off Sheet Connector.  
## 
##  
##      <br> To create a new instance of this class, use @link NXOpen::Schematic::SchematicManager::CreateOffSheetConnectorBuilder  NXOpen::Schematic::SchematicManager::CreateOffSheetConnectorBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## RotateOption </term> <description> 
##  
## Zero </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class OffSheetConnectorBuilder(NXOpen.Builder): 
    """ <summary>
    Builder used to model a piece of Off Sheet Connector. </summary>
    """


    ##   @brief  the style of OSC elements.  
    ## 
    ##   
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SmallFilledArrowOut</term><description> 
    ## </description> </item><item><term> 
    ## SmallFilledArrowIn</term><description> 
    ## </description> </item><item><term> 
    ## Box</term><description> 
    ## </description> </item><item><term> 
    ## ChevronOut</term><description> 
    ## </description> </item><item><term> 
    ## ChevronIn</term><description> 
    ## </description> </item><item><term> 
    ## PipeUpFar</term><description> 
    ## </description> </item><item><term> 
    ## PipeUpClose</term><description> 
    ## </description> </item><item><term> 
    ## Details</term><description> 
    ## </description> </item></list>
    class StyleOption(Enum):
        """
        Members Include: <SmallFilledArrowOut> <SmallFilledArrowIn> <Box> <ChevronOut> <ChevronIn> <PipeUpFar> <PipeUpClose> <Details>
        """
        SmallFilledArrowOut: int
        SmallFilledArrowIn: int
        Box: int
        ChevronOut: int
        ChevronIn: int
        PipeUpFar: int
        PipeUpClose: int
        Details: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OffSheetConnectorBuilder.StyleOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) ElementId
    ##   the current element ID of this OSC.  
    ##    It works only in edit mode, it's optional and the first element ID stored in the OSC will be used as default.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def ElementId(self) -> str:
        """
        Getter for property: (str) ElementId
          the current element ID of this OSC.  
           It works only in edit mode, it's optional and the first element ID stored in the OSC will be used as default.  
         
        """
        pass
    
    ## Setter for property: (str) ElementId

    ##   the current element ID of this OSC.  
    ##    It works only in edit mode, it's optional and the first element ID stored in the OSC will be used as default.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ElementId.setter
    def ElementId(self, elementId: str):
        """
        Setter for property: (str) ElementId
          the current element ID of this OSC.  
           It works only in edit mode, it's optional and the first element ID stored in the OSC will be used as default.  
         
        """
        pass
    
    ## Getter for property: (bool) Horizontal
    ##   the option to flip the symbol horizontally.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def Horizontal(self) -> bool:
        """
        Getter for property: (bool) Horizontal
          the option to flip the symbol horizontally.  
             
         
        """
        pass
    
    ## Getter for property: (@link Sheet NXOpen.Schematic.Sheet@endlink) OwningSheet
    ##   the owning sheet of this sheet element.  
    ##    Its setting method works only in creation mode.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return Sheet
    @property
    def OwningSheet(self) -> Sheet:
        """
        Getter for property: (@link Sheet NXOpen.Schematic.Sheet@endlink) OwningSheet
          the owning sheet of this sheet element.  
           Its setting method works only in creation mode.   
         
        """
        pass
    
    ## Setter for property: (@link Sheet NXOpen.Schematic.Sheet@endlink) OwningSheet

    ##   the owning sheet of this sheet element.  
    ##    Its setting method works only in creation mode.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @OwningSheet.setter
    def OwningSheet(self, owningSheet: Sheet):
        """
        Setter for property: (@link Sheet NXOpen.Schematic.Sheet@endlink) OwningSheet
          the owning sheet of this sheet element.  
           Its setting method works only in creation mode.   
         
        """
        pass
    
    ## Getter for property: (@link RotateAngleOption NXOpen.Schematic.RotateAngleOption@endlink) RotateOption
    ##   the symbol rotation angle.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return RotateAngleOption
    @property
    def RotateOption(self) -> RotateAngleOption:
        """
        Getter for property: (@link RotateAngleOption NXOpen.Schematic.RotateAngleOption@endlink) RotateOption
          the symbol rotation angle.  
             
         
        """
        pass
    
    ## Setter for property: (@link RotateAngleOption NXOpen.Schematic.RotateAngleOption@endlink) RotateOption

    ##   the symbol rotation angle.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @RotateOption.setter
    def RotateOption(self, rotate: RotateAngleOption):
        """
        Setter for property: (@link RotateAngleOption NXOpen.Schematic.RotateAngleOption@endlink) RotateOption
          the symbol rotation angle.  
             
         
        """
        pass
    
    ## Getter for property: (@link OffSheetConnectorBuilder.StyleOption NXOpen.Schematic.OffSheetConnectorBuilder.StyleOption@endlink) Style
    ##   the style of OSC   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return OffSheetConnectorBuilder.StyleOption
    @property
    def Style(self) -> OffSheetConnectorBuilder.StyleOption:
        """
        Getter for property: (@link OffSheetConnectorBuilder.StyleOption NXOpen.Schematic.OffSheetConnectorBuilder.StyleOption@endlink) Style
          the style of OSC   
            
         
        """
        pass
    
    ## Setter for property: (@link OffSheetConnectorBuilder.StyleOption NXOpen.Schematic.OffSheetConnectorBuilder.StyleOption@endlink) Style

    ##   the style of OSC   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Style.setter
    def Style(self, style: OffSheetConnectorBuilder.StyleOption):
        """
        Setter for property: (@link OffSheetConnectorBuilder.StyleOption NXOpen.Schematic.OffSheetConnectorBuilder.StyleOption@endlink) Style
          the style of OSC   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Diagramming.TextStyleBuilder NXOpen.Diagramming.TextStyleBuilder@endlink) TextStyleBuilder
    ##   the text style of the OSC.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Diagramming.TextStyleBuilder
    @property
    def TextStyleBuilder(self) -> NXOpen.Diagramming.TextStyleBuilder:
        """
        Getter for property: (@link NXOpen.Diagramming.TextStyleBuilder NXOpen.Diagramming.TextStyleBuilder@endlink) TextStyleBuilder
          the text style of the OSC.  
             
         
        """
        pass
    
    ## Getter for property: (bool) Vertical
    ##   the option to flip the symbol vertically.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def Vertical(self) -> bool:
        """
        Getter for property: (bool) Vertical
          the option to flip the symbol vertically.  
             
         
        """
        pass
    
    ##  To flip a off sheet connector horizonally
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def FlipHorizontally(builder: OffSheetConnectorBuilder) -> None:
        """
         To flip a off sheet connector horizonally
        """
        pass
    
    ##  To flip a off sheet connector vertically
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def FlipVertically(builder: OffSheetConnectorBuilder) -> None:
        """
         To flip a off sheet connector vertically
        """
        pass
    
    ##  To get the connection connecting to the OSC sheet element.
    ##  @return A tuple consisting of (type, connection). 
    ##  - type is: @link ConnectionEndType NXOpen.Schematic.ConnectionEndType@endlink.
    ##  - connection is: @link Connection NXOpen.Schematic.Connection@endlink.

    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetConnection(builder: OffSheetConnectorBuilder) -> Tuple[ConnectionEndType, Connection]:
        """
         To get the connection connecting to the OSC sheet element.
         @return A tuple consisting of (type, connection). 
         - type is: @link ConnectionEndType NXOpen.Schematic.ConnectionEndType@endlink.
         - connection is: @link Connection NXOpen.Schematic.Connection@endlink.

        """
        pass
    
    ##  Gets the symbol location. 
    ##  @return location (@link NXOpen.Point2d NXOpen.Point2d@endlink):  the symbol location. .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLocation(builder: OffSheetConnectorBuilder) -> NXOpen.Point2d:
        """
         Gets the symbol location. 
         @return location (@link NXOpen.Point2d NXOpen.Point2d@endlink):  the symbol location. .
        """
        pass
    
    ##  To rotate a off sheet connector
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Rotate(builder: OffSheetConnectorBuilder) -> None:
        """
         To rotate a off sheet connector
        """
        pass
    
    ##  To set the connection connecting to the OSC sheet element.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="type"> (@link ConnectionEndType NXOpen.Schematic.ConnectionEndType@endlink) </param>
    ## <param name="connection"> (@link Connection NXOpen.Schematic.Connection@endlink) </param>
    def SetConnection(builder: OffSheetConnectorBuilder, type: ConnectionEndType, connection: Connection) -> None:
        """
         To set the connection connecting to the OSC sheet element.
        """
        pass
    
    ##  Links to the destination OSC. If the input OffSheetConnector is nullptr, it means to break the existing link.  
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="desObject"> (@link OffSheetConnector NXOpen.Schematic.OffSheetConnector@endlink) </param>
    def SetDestination(builder: OffSheetConnectorBuilder, desObject: OffSheetConnector) -> None:
        """
         Links to the destination OSC. If the input OffSheetConnector is nullptr, it means to break the existing link.  
        """
        pass
    
    ##  Sets the symbol location. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ##  the osc location. 
    def SetLocation(builder: OffSheetConnectorBuilder, location: NXOpen.Point2d) -> None:
        """
         Sets the symbol location. 
        """
        pass
    
import NXOpen
##  Represents a collection of Schematic.OffSheetConnector.  <br> To obtain an instance of this class, refer to @link NXOpen::Schematic::SchematicManager  NXOpen::Schematic::SchematicManager @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class OffSheetConnectorCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Schematic.OffSheetConnector. """


    ##  Finds the @link Schematic::OffSheetConnector Schematic::OffSheetConnector@endlink  with the given identifier as recorded in a journal.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return osc (@link OffSheetConnector NXOpen.Schematic.OffSheetConnector@endlink):  @link Schematic::OffSheetConnector Schematic::OffSheetConnector@endlink  with this name. .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ##  Identifier to be found 
    def FindObject(part: OffSheetConnectorCollection, journalIdentifier: str) -> OffSheetConnector:
        """
         Finds the @link Schematic::OffSheetConnector Schematic::OffSheetConnector@endlink  with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         @return osc (@link OffSheetConnector NXOpen.Schematic.OffSheetConnector@endlink):  @link Schematic::OffSheetConnector Schematic::OffSheetConnector@endlink  with this name. .
        """
        pass
    
import NXOpen
##  Represents the off sheet connector class.  <br> To create or edit an instance of this class, use @link NXOpen::Schematic::OffSheetConnectorBuilder  NXOpen::Schematic::OffSheetConnectorBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class OffSheetConnector(NXOpen.NXObject): 
    """ Represents the off sheet connector class. """
    pass


##  Represents the port direction option. 
##  input. 
class PortDirectionOption(Enum):
    """
    Members Include: <Input> <Output> <BiDirectional>
    """
    Input: int
    Output: int
    BiDirectional: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> PortDirectionOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  Represents the schematic Port class.  <br> To create or edit an instance of this class, use @link NXOpen::Schematic::PortBuilder  NXOpen::Schematic::PortBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class Port(NXOpen.NXObject): 
    """ Represents the schematic Port class. """
    pass


import NXOpen
import NXOpen.Diagramming
import NXOpen.Diagramming.Tables
import NXOpen.GeometricUtilities
## 
##     Represents a PreferencesAnnotationBuilder
##     
## 
##   <br>  Created in NX1980.0.0  <br> 

class PreferencesAnnotationBuilder(NXOpen.TaggedObject): 
    """
    Represents a PreferencesAnnotationBuilder
    """


    ## Getter for property: (@link NXOpen.Diagramming.DiagrammingConnectionlabelhorizontaloffsetposition NXOpen.Diagramming.DiagrammingConnectionlabelhorizontaloffsetposition@endlink) ConnectionLabelHorizontalOffsetPosition
    ##   the horizontal position of the connection tag.  
    ##      
    ##  
    ## Getter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Diagramming.DiagrammingConnectionlabelhorizontaloffsetposition
    @property
    def ConnectionLabelHorizontalOffsetPosition(self) -> NXOpen.Diagramming.DiagrammingConnectionlabelhorizontaloffsetposition:
        """
        Getter for property: (@link NXOpen.Diagramming.DiagrammingConnectionlabelhorizontaloffsetposition NXOpen.Diagramming.DiagrammingConnectionlabelhorizontaloffsetposition@endlink) ConnectionLabelHorizontalOffsetPosition
          the horizontal position of the connection tag.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Diagramming.DiagrammingConnectionlabelhorizontaloffsetposition NXOpen.Diagramming.DiagrammingConnectionlabelhorizontaloffsetposition@endlink) ConnectionLabelHorizontalOffsetPosition

    ##   the horizontal position of the connection tag.  
    ##      
    ##  
    ## Setter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ConnectionLabelHorizontalOffsetPosition.setter
    def ConnectionLabelHorizontalOffsetPosition(self, position: NXOpen.Diagramming.DiagrammingConnectionlabelhorizontaloffsetposition):
        """
        Setter for property: (@link NXOpen.Diagramming.DiagrammingConnectionlabelhorizontaloffsetposition NXOpen.Diagramming.DiagrammingConnectionlabelhorizontaloffsetposition@endlink) ConnectionLabelHorizontalOffsetPosition
          the horizontal position of the connection tag.  
             
         
        """
        pass
    
    ## Getter for property: (float) ConnectionLabelOffset
    ##   the gap between the connection and the tag.  
    ##     
    ##  
    ## Getter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return float
    @property
    def ConnectionLabelOffset(self) -> float:
        """
        Getter for property: (float) ConnectionLabelOffset
          the gap between the connection and the tag.  
            
         
        """
        pass
    
    ## Setter for property: (float) ConnectionLabelOffset

    ##   the gap between the connection and the tag.  
    ##     
    ##  
    ## Setter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ConnectionLabelOffset.setter
    def ConnectionLabelOffset(self, offset: float):
        """
        Setter for property: (float) ConnectionLabelOffset
          the gap between the connection and the tag.  
            
         
        """
        pass
    
    ## Getter for property: (bool) ConnectionLabelPositionCenter
    ##   the tag is displayed at the center of the connection.  
    ##     
    ##  
    ## Getter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def ConnectionLabelPositionCenter(self) -> bool:
        """
        Getter for property: (bool) ConnectionLabelPositionCenter
          the tag is displayed at the center of the connection.  
            
         
        """
        pass
    
    ## Setter for property: (bool) ConnectionLabelPositionCenter

    ##   the tag is displayed at the center of the connection.  
    ##     
    ##  
    ## Setter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ConnectionLabelPositionCenter.setter
    def ConnectionLabelPositionCenter(self, center: bool):
        """
        Setter for property: (bool) ConnectionLabelPositionCenter
          the tag is displayed at the center of the connection.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Diagramming.DiagrammingConnectionlabelverticaloffsetposition NXOpen.Diagramming.DiagrammingConnectionlabelverticaloffsetposition@endlink) ConnectionLabelVerticalOffsetPosition
    ##   the vertical position of the connection tag.  
    ##      
    ##  
    ## Getter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Diagramming.DiagrammingConnectionlabelverticaloffsetposition
    @property
    def ConnectionLabelVerticalOffsetPosition(self) -> NXOpen.Diagramming.DiagrammingConnectionlabelverticaloffsetposition:
        """
        Getter for property: (@link NXOpen.Diagramming.DiagrammingConnectionlabelverticaloffsetposition NXOpen.Diagramming.DiagrammingConnectionlabelverticaloffsetposition@endlink) ConnectionLabelVerticalOffsetPosition
          the vertical position of the connection tag.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Diagramming.DiagrammingConnectionlabelverticaloffsetposition NXOpen.Diagramming.DiagrammingConnectionlabelverticaloffsetposition@endlink) ConnectionLabelVerticalOffsetPosition

    ##   the vertical position of the connection tag.  
    ##      
    ##  
    ## Setter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ConnectionLabelVerticalOffsetPosition.setter
    def ConnectionLabelVerticalOffsetPosition(self, position: NXOpen.Diagramming.DiagrammingConnectionlabelverticaloffsetposition):
        """
        Setter for property: (@link NXOpen.Diagramming.DiagrammingConnectionlabelverticaloffsetposition NXOpen.Diagramming.DiagrammingConnectionlabelverticaloffsetposition@endlink) ConnectionLabelVerticalOffsetPosition
          the vertical position of the connection tag.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ShowConnectionTag
    ##      the Connection Tag Display Status.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def ShowConnectionTag(self) -> bool:
        """
        Getter for property: (bool) ShowConnectionTag
             the Connection Tag Display Status.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ShowConnectionTag

    ##      the Connection Tag Display Status.  
    ##      
    ##  
    ## Setter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @ShowConnectionTag.setter
    def ShowConnectionTag(self, showConnectionTag: bool):
        """
        Setter for property: (bool) ShowConnectionTag
             the Connection Tag Display Status.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) TablesBorderCellSettings
    ##      the preferences tabular note border cell settings builder   
    ##     
    ##  
    ## Getter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Diagramming.RenderingPropertiesBuilder
    @property
    def TablesBorderCellSettings(self) -> NXOpen.Diagramming.RenderingPropertiesBuilder:
        """
        Getter for property: (@link NXOpen.Diagramming.RenderingPropertiesBuilder NXOpen.Diagramming.RenderingPropertiesBuilder@endlink) TablesBorderCellSettings
             the preferences tabular note border cell settings builder   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Diagramming.Tables.CellSettingsBuilder NXOpen.Diagramming.Tables.CellSettingsBuilder@endlink) TablesCellSettings
    ##      the preferences tabular note settings builder   
    ##     
    ##  
    ## Getter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Diagramming.Tables.CellSettingsBuilder
    @property
    def TablesCellSettings(self) -> NXOpen.Diagramming.Tables.CellSettingsBuilder:
        """
        Getter for property: (@link NXOpen.Diagramming.Tables.CellSettingsBuilder NXOpen.Diagramming.Tables.CellSettingsBuilder@endlink) TablesCellSettings
             the preferences tabular note settings builder   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Diagramming.TextStyleBuilder NXOpen.Diagramming.TextStyleBuilder@endlink) TextStyleConnectionBuilder
    ##   the connection text style of the Annotation.  
    ##      
    ##  
    ## Getter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Diagramming.TextStyleBuilder
    @property
    def TextStyleConnectionBuilder(self) -> NXOpen.Diagramming.TextStyleBuilder:
        """
        Getter for property: (@link NXOpen.Diagramming.TextStyleBuilder NXOpen.Diagramming.TextStyleBuilder@endlink) TextStyleConnectionBuilder
          the connection text style of the Annotation.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Diagramming.TextStyleBuilder NXOpen.Diagramming.TextStyleBuilder@endlink) TextStyleNoteBuilder
    ##   the note text style of the Annotation.  
    ##      
    ##  
    ## Getter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Diagramming.TextStyleBuilder
    @property
    def TextStyleNoteBuilder(self) -> NXOpen.Diagramming.TextStyleBuilder:
        """
        Getter for property: (@link NXOpen.Diagramming.TextStyleBuilder NXOpen.Diagramming.TextStyleBuilder@endlink) TextStyleNoteBuilder
          the note text style of the Annotation.  
             
         
        """
        pass
    
import NXOpen
## 
##     Represents a PreferencesBuilder
##      <br> To create a new instance of this class, use @link NXOpen::Schematic::SchematicManager::CreatePreferencesBuilder  NXOpen::Schematic::SchematicManager::CreatePreferencesBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class PreferencesBuilder(NXOpen.Builder): 
    """
    Represents a PreferencesBuilder
    """


    ## Getter for property: (@link PreferencesAnnotationBuilder NXOpen.Schematic.PreferencesAnnotationBuilder@endlink) Annotation
    ##      the preferences annotation builder   
    ##     
    ##  
    ## Getter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return PreferencesAnnotationBuilder
    @property
    def Annotation(self) -> PreferencesAnnotationBuilder:
        """
        Getter for property: (@link PreferencesAnnotationBuilder NXOpen.Schematic.PreferencesAnnotationBuilder@endlink) Annotation
             the preferences annotation builder   
            
         
        """
        pass
    
    ## Getter for property: (@link PreferencesConnectionBuilder NXOpen.Schematic.PreferencesConnectionBuilder@endlink) Connection
    ##      the preferences connection builder   
    ##     
    ##  
    ## Getter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return PreferencesConnectionBuilder
    @property
    def Connection(self) -> PreferencesConnectionBuilder:
        """
        Getter for property: (@link PreferencesConnectionBuilder NXOpen.Schematic.PreferencesConnectionBuilder@endlink) Connection
             the preferences connection builder   
            
         
        """
        pass
    
    ## Getter for property: (@link PreferencesGeneralBuilder NXOpen.Schematic.PreferencesGeneralBuilder@endlink) General
    ##      the preferences general builder   
    ##     
    ##  
    ## Getter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return PreferencesGeneralBuilder
    @property
    def General(self) -> PreferencesGeneralBuilder:
        """
        Getter for property: (@link PreferencesGeneralBuilder NXOpen.Schematic.PreferencesGeneralBuilder@endlink) General
             the preferences general builder   
            
         
        """
        pass
    
import NXOpen
import NXOpen.Diagramming
import NXOpen.GeometricUtilities
## 
##     Represents a PreferencesConnectionBuilder
##     
## 
##   <br>  Created in NX1980.0.0  <br> 

class PreferencesConnectionBuilder(NXOpen.TaggedObject): 
    """
    Represents a PreferencesConnectionBuilder
    """


    ## Getter for property: (bool) AllowBreakConnections
    ##   the allow break connections.  
    ##     
    ##  
    ## Getter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def AllowBreakConnections(self) -> bool:
        """
        Getter for property: (bool) AllowBreakConnections
          the allow break connections.  
            
         
        """
        pass
    
    ## Setter for property: (bool) AllowBreakConnections

    ##   the allow break connections.  
    ##     
    ##  
    ## Setter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @AllowBreakConnections.setter
    def AllowBreakConnections(self, allowBreakConnections: bool):
        """
        Setter for property: (bool) AllowBreakConnections
          the allow break connections.  
            
         
        """
        pass
    
    ## Getter for property: (bool) AllowNonOrthogonalConnections
    ##   the allow non-orthogonal connections.  
    ##     
    ##  
    ## Getter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def AllowNonOrthogonalConnections(self) -> bool:
        """
        Getter for property: (bool) AllowNonOrthogonalConnections
          the allow non-orthogonal connections.  
            
         
        """
        pass
    
    ## Setter for property: (bool) AllowNonOrthogonalConnections

    ##   the allow non-orthogonal connections.  
    ##     
    ##  
    ## Setter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @AllowNonOrthogonalConnections.setter
    def AllowNonOrthogonalConnections(self, allowNonOrthogonal: bool):
        """
        Setter for property: (bool) AllowNonOrthogonalConnections
          the allow non-orthogonal connections.  
            
         
        """
        pass
    
    ## Getter for property: (float) ArrowSize
    ##   the arrow size.  
    ##     
    ##  
    ## Getter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return float
    @property
    def ArrowSize(self) -> float:
        """
        Getter for property: (float) ArrowSize
          the arrow size.  
            
         
        """
        pass
    
    ## Setter for property: (float) ArrowSize

    ##   the arrow size.  
    ##     
    ##  
    ## Setter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ArrowSize.setter
    def ArrowSize(self, size: float):
        """
        Setter for property: (float) ArrowSize
          the arrow size.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Diagramming.DiagrammingFlowdirectionarrowstyle NXOpen.Diagramming.DiagrammingFlowdirectionarrowstyle@endlink) ArrowStyle
    ##   the arrow style.  
    ##     
    ##  
    ## Getter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Diagramming.DiagrammingFlowdirectionarrowstyle
    @property
    def ArrowStyle(self) -> NXOpen.Diagramming.DiagrammingFlowdirectionarrowstyle:
        """
        Getter for property: (@link NXOpen.Diagramming.DiagrammingFlowdirectionarrowstyle NXOpen.Diagramming.DiagrammingFlowdirectionarrowstyle@endlink) ArrowStyle
          the arrow style.  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Diagramming.DiagrammingFlowdirectionarrowstyle NXOpen.Diagramming.DiagrammingFlowdirectionarrowstyle@endlink) ArrowStyle

    ##   the arrow style.  
    ##     
    ##  
    ## Setter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ArrowStyle.setter
    def ArrowStyle(self, style: NXOpen.Diagramming.DiagrammingFlowdirectionarrowstyle):
        """
        Setter for property: (@link NXOpen.Diagramming.DiagrammingFlowdirectionarrowstyle NXOpen.Diagramming.DiagrammingFlowdirectionarrowstyle@endlink) ArrowStyle
          the arrow style.  
            
         
        """
        pass
    
    ## Getter for property: (str) DefaultTeeSymbolId
    ##   the Default Junction Symbol  
    ##     
    ##  
    ## Getter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def DefaultTeeSymbolId(self) -> str:
        """
        Getter for property: (str) DefaultTeeSymbolId
          the Default Junction Symbol  
            
         
        """
        pass
    
    ## Setter for property: (str) DefaultTeeSymbolId

    ##   the Default Junction Symbol  
    ##     
    ##  
    ## Setter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @DefaultTeeSymbolId.setter
    def DefaultTeeSymbolId(self, symbolId: str):
        """
        Setter for property: (str) DefaultTeeSymbolId
          the Default Junction Symbol  
            
         
        """
        pass
    
    ## Getter for property: (str) DefaultTeeSymbolIdForPDM
    ##   the full default Junction Symbol in the Teamcenter environment.  
    ##   
    ##         Schematic requires the item's name, rather than the DB/Name/Rev information  
    ##  
    ## Getter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def DefaultTeeSymbolIdForPDM(self) -> str:
        """
        Getter for property: (str) DefaultTeeSymbolIdForPDM
          the full default Junction Symbol in the Teamcenter environment.  
          
                Schematic requires the item's name, rather than the DB/Name/Rev information  
         
        """
        pass
    
    ## Setter for property: (str) DefaultTeeSymbolIdForPDM

    ##   the full default Junction Symbol in the Teamcenter environment.  
    ##   
    ##         Schematic requires the item's name, rather than the DB/Name/Rev information  
    ##  
    ## Setter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @DefaultTeeSymbolIdForPDM.setter
    def DefaultTeeSymbolIdForPDM(self, symbolId: str):
        """
        Setter for property: (str) DefaultTeeSymbolIdForPDM
          the full default Junction Symbol in the Teamcenter environment.  
          
                Schematic requires the item's name, rather than the DB/Name/Rev information  
         
        """
        pass
    
    ## Getter for property: (float) JumperGap
    ##   the jumper gap.  
    ##     
    ##  
    ## Getter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return float
    @property
    def JumperGap(self) -> float:
        """
        Getter for property: (float) JumperGap
          the jumper gap.  
            
         
        """
        pass
    
    ## Setter for property: (float) JumperGap

    ##   the jumper gap.  
    ##     
    ##  
    ## Setter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @JumperGap.setter
    def JumperGap(self, gap: float):
        """
        Setter for property: (float) JumperGap
          the jumper gap.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Diagramming.DiagrammingJumperprioritytype NXOpen.Diagramming.DiagrammingJumperprioritytype@endlink) JumperPriority
    ##   the jumper priority type.  
    ##      
    ##  
    ## Getter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Diagramming.DiagrammingJumperprioritytype
    @property
    def JumperPriority(self) -> NXOpen.Diagramming.DiagrammingJumperprioritytype:
        """
        Getter for property: (@link NXOpen.Diagramming.DiagrammingJumperprioritytype NXOpen.Diagramming.DiagrammingJumperprioritytype@endlink) JumperPriority
          the jumper priority type.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Diagramming.DiagrammingJumperprioritytype NXOpen.Diagramming.DiagrammingJumperprioritytype@endlink) JumperPriority

    ##   the jumper priority type.  
    ##      
    ##  
    ## Setter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @JumperPriority.setter
    def JumperPriority(self, jumperPriorityType: NXOpen.Diagramming.DiagrammingJumperprioritytype):
        """
        Setter for property: (@link NXOpen.Diagramming.DiagrammingJumperprioritytype NXOpen.Diagramming.DiagrammingJumperprioritytype@endlink) JumperPriority
          the jumper priority type.  
             
         
        """
        pass
    
    ## Getter for property: (bool) JumperPriorityUseLineType
    ##   the jumper priority use line type.  
    ##     
    ##  
    ## Getter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def JumperPriorityUseLineType(self) -> bool:
        """
        Getter for property: (bool) JumperPriorityUseLineType
          the jumper priority use line type.  
            
         
        """
        pass
    
    ## Setter for property: (bool) JumperPriorityUseLineType

    ##   the jumper priority use line type.  
    ##     
    ##  
    ## Setter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @JumperPriorityUseLineType.setter
    def JumperPriorityUseLineType(self, useLineType: bool):
        """
        Setter for property: (bool) JumperPriorityUseLineType
          the jumper priority use line type.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Diagramming.DiagrammingJumpertype NXOpen.Diagramming.DiagrammingJumpertype@endlink) JumperType
    ##   the jumper type.  
    ##      
    ##  
    ## Getter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Diagramming.DiagrammingJumpertype
    @property
    def JumperType(self) -> NXOpen.Diagramming.DiagrammingJumpertype:
        """
        Getter for property: (@link NXOpen.Diagramming.DiagrammingJumpertype NXOpen.Diagramming.DiagrammingJumpertype@endlink) JumperType
          the jumper type.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Diagramming.DiagrammingJumpertype NXOpen.Diagramming.DiagrammingJumpertype@endlink) JumperType

    ##   the jumper type.  
    ##      
    ##  
    ## Setter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @JumperType.setter
    def JumperType(self, jumperType: NXOpen.Diagramming.DiagrammingJumpertype):
        """
        Setter for property: (@link NXOpen.Diagramming.DiagrammingJumpertype NXOpen.Diagramming.DiagrammingJumpertype@endlink) JumperType
          the jumper type.  
             
         
        """
        pass
    
    ## Getter for property: (float) MinimumSegmentLength
    ##   the minimum segment length.  
    ##     
    ##  
    ## Getter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return float
    @property
    def MinimumSegmentLength(self) -> float:
        """
        Getter for property: (float) MinimumSegmentLength
          the minimum segment length.  
            
         
        """
        pass
    
    ## Setter for property: (float) MinimumSegmentLength

    ##   the minimum segment length.  
    ##     
    ##  
    ## Setter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @MinimumSegmentLength.setter
    def MinimumSegmentLength(self, length: float):
        """
        Setter for property: (float) MinimumSegmentLength
          the minimum segment length.  
            
         
        """
        pass
    
    ## Getter for property: (float) SnapAngle
    ##   the snap angle   
    ##     
    ##  
    ## Getter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return float
    @property
    def SnapAngle(self) -> float:
        """
        Getter for property: (float) SnapAngle
          the snap angle   
            
         
        """
        pass
    
    ## Setter for property: (float) SnapAngle

    ##   the snap angle   
    ##     
    ##  
    ## Setter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @SnapAngle.setter
    def SnapAngle(self, angle: float):
        """
        Setter for property: (float) SnapAngle
          the snap angle   
            
         
        """
        pass
    
    ## Getter for property: (float) TeeSize
    ##   the tee size.  
    ##     
    ##  
    ## Getter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return float
    @property
    def TeeSize(self) -> float:
        """
        Getter for property: (float) TeeSize
          the tee size.  
            
         
        """
        pass
    
    ## Setter for property: (float) TeeSize

    ##   the tee size.  
    ##     
    ##  
    ## Setter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @TeeSize.setter
    def TeeSize(self, size: float):
        """
        Setter for property: (float) TeeSize
          the tee size.  
            
         
        """
        pass
    
    ## Getter for property: (bool) UseDefaultTee
    ##   the option for using default Junctions.  
    ##     
    ##  
    ## Getter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def UseDefaultTee(self) -> bool:
        """
        Getter for property: (bool) UseDefaultTee
          the option for using default Junctions.  
            
         
        """
        pass
    
    ## Setter for property: (bool) UseDefaultTee

    ##   the option for using default Junctions.  
    ##     
    ##  
    ## Setter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @UseDefaultTee.setter
    def UseDefaultTee(self, useDefaultTee: bool):
        """
        Setter for property: (bool) UseDefaultTee
          the option for using default Junctions.  
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
## 
##     Represents a PreferencesGeneralBuilder
##     
## 
##   <br>  Created in NX1980.0.0  <br> 

class PreferencesGeneralBuilder(NXOpen.TaggedObject): 
    """
    Represents a PreferencesGeneralBuilder
    """


    ## Getter for property: (bool) HidePorts
    ##    the flag to hide the ports.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def HidePorts(self) -> bool:
        """
        Getter for property: (bool) HidePorts
           the flag to hide the ports.  
             
         
        """
        pass
    
    ## Setter for property: (bool) HidePorts

    ##    the flag to hide the ports.  
    ##      
    ##  
    ## Setter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @HidePorts.setter
    def HidePorts(self, hidePorts: bool):
        """
        Setter for property: (bool) HidePorts
           the flag to hide the ports.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ShowSymbolHandles
    ##    the flag to show the Symbol Handles.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def ShowSymbolHandles(self) -> bool:
        """
        Getter for property: (bool) ShowSymbolHandles
           the flag to show the Symbol Handles.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ShowSymbolHandles

    ##    the flag to show the Symbol Handles.  
    ##      
    ##  
    ## Setter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @ShowSymbolHandles.setter
    def ShowSymbolHandles(self, showSymbolHandles: bool):
        """
        Setter for property: (bool) ShowSymbolHandles
           the flag to show the Symbol Handles.  
             
         
        """
        pass
    
    ## Getter for property: (str) TagMask
    ##    the name of the file containing the tag mask configurations.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def TagMask(self) -> str:
        """
        Getter for property: (str) TagMask
           the name of the file containing the tag mask configurations.  
             
         
        """
        pass
    
    ## Setter for property: (str) TagMask

    ##    the name of the file containing the tag mask configurations.  
    ##      
    ##  
    ## Setter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @TagMask.setter
    def TagMask(self, tagMaskFile: str):
        """
        Setter for property: (str) TagMask
           the name of the file containing the tag mask configurations.  
             
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##   @brief  Represents a PropertyCellRangeBuilder.  
## 
##    <br> This is a sub-builder class and cannot be directly instantiated  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class PropertyCellRangeBuilder(NXOpen.TaggedObject): 
    """ <summary> Represents a PropertyCellRangeBuilder. </summary> """
    pass


##  Represents the symbol rotation angle options. 
##  0 degree. 
class RotateAngleOption(Enum):
    """
    Members Include: <Zero> <Ninety> <OneHundredAndEighty> <TwoHundredAndSeventy>
    """
    Zero: int
    Ninety: int
    OneHundredAndEighty: int
    TwoHundredAndSeventy: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> RotateAngleOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
import NXOpen.Diagramming
import NXOpen.Schematic.Mechanical
##  A manager to deal with all objects.  <br> To obtain an instance of this class, refer to @link NXOpen::Part  NXOpen::Part @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class SchematicManager(NXOpen.Object): 
    """ A manager to deal with all objects. """


    ##  Returns the @link NXOpen::Schematic::SheetCollection  NXOpen::Schematic::SheetCollection @endlink  belonging to this part 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @link SheetCollection NXOpen.Schematic.SheetCollection@endlink
    @property
    def Sheets() -> SheetCollection:
        """
         Returns the @link NXOpen::Schematic::SheetCollection  NXOpen::Schematic::SheetCollection @endlink  belonging to this part 
        """
        pass
    
    ##  Returns the @link NXOpen::Schematic::NodeCollection  NXOpen::Schematic::NodeCollection @endlink  belonging to this part 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @link NodeCollection NXOpen.Schematic.NodeCollection@endlink
    @property
    def Nodes() -> NodeCollection:
        """
         Returns the @link NXOpen::Schematic::NodeCollection  NXOpen::Schematic::NodeCollection @endlink  belonging to this part 
        """
        pass
    
    ##  Returns the @link NXOpen::Schematic::ConnectionCollection  NXOpen::Schematic::ConnectionCollection @endlink  belonging to this part 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @link ConnectionCollection NXOpen.Schematic.ConnectionCollection@endlink
    @property
    def Connections() -> ConnectionCollection:
        """
         Returns the @link NXOpen::Schematic::ConnectionCollection  NXOpen::Schematic::ConnectionCollection @endlink  belonging to this part 
        """
        pass
    
    ##  This is an internal API and can be changed at any time 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @link PortCollection NXOpen.Schematic.PortCollection@endlink
    @property
    def Ports() -> PortCollection:
        """
         This is an internal API and can be changed at any time 
        """
        pass
    
    ##  Returns the @link NXOpen::Schematic::OffSheetConnectorCollection  NXOpen::Schematic::OffSheetConnectorCollection @endlink  belonging to this part 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @link OffSheetConnectorCollection NXOpen.Schematic.OffSheetConnectorCollection@endlink
    @property
    def OffSheetConnectors() -> OffSheetConnectorCollection:
        """
         Returns the @link NXOpen::Schematic::OffSheetConnectorCollection  NXOpen::Schematic::OffSheetConnectorCollection @endlink  belonging to this part 
        """
        pass
    
    ##  Returns a @link NXOpen::Schematic::Mechanical::RunsManager NXOpen::Schematic::Mechanical::RunsManager@endlink  object.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @link NXOpen.Schematic.Mechanical.RunsManager NXOpen.Schematic.Mechanical.RunsManager@endlink
    @property
    def RunsManager() -> NXOpen.Schematic.Mechanical.RunsManager:
        """
         Returns a @link NXOpen::Schematic::Mechanical::RunsManager NXOpen::Schematic::Mechanical::RunsManager@endlink  object.
        """
        pass
    
    ##  Adds the connection from the unassigned folder to the run. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="run"> (@link NXOpen.Schematic.Mechanical.Run NXOpen.Schematic.Mechanical.Run@endlink) </param>
    ## <param name="connection"> (@link Connection NXOpen.Schematic.Connection@endlink) </param>
    def AddConnectionToRun(part: SchematicManager, run: NXOpen.Schematic.Mechanical.Run, connection: Connection) -> None:
        """
         Adds the connection from the unassigned folder to the run. 
        """
        pass
    
    ##  Copy the Schematic objects. 
    ##  @return outputObjects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  Copies of Schematic Objects .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ##  Schematic Objects to be copied 
    def CopySchematicObjects(part: SchematicManager, inputObjects: List[NXOpen.NXObject], isDeepCopy: bool) -> List[NXOpen.NXObject]:
        """
         Copy the Schematic objects. 
         @return outputObjects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  Copies of Schematic Objects .
        """
        pass
    
    ##  Creates a @link NXOpen::Schematic::BulkEditBuilder NXOpen::Schematic::BulkEditBuilder@endlink  
    ##  @return builder (@link BulkEditBuilder NXOpen.Schematic.BulkEditBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    def CreateBulkEditBuilder(part: SchematicManager) -> BulkEditBuilder:
        """
         Creates a @link NXOpen::Schematic::BulkEditBuilder NXOpen::Schematic::BulkEditBuilder@endlink  
         @return builder (@link BulkEditBuilder NXOpen.Schematic.BulkEditBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Schematic::ConnectionBuilder NXOpen::Schematic::ConnectionBuilder@endlink . 
    ##  @return builder (@link ConnectionBuilder NXOpen.Schematic.ConnectionBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ##  @link NXOpen::Schematic::Connection NXOpen::Schematic::Connection@endlink  to be edited, if NULL then create a new one 
    def CreateConnectionBuilder(part: SchematicManager, connection: Connection) -> ConnectionBuilder:
        """
         Creates a @link NXOpen::Schematic::ConnectionBuilder NXOpen::Schematic::ConnectionBuilder@endlink . 
         @return builder (@link ConnectionBuilder NXOpen.Schematic.ConnectionBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Schematic::DesignValidationBuilder NXOpen::Schematic::DesignValidationBuilder@endlink . 
    ##  @return builder (@link DesignValidationBuilder NXOpen.Schematic.DesignValidationBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_diagramming ("NX Diagramming")
    def CreateDesignValidationBuilder(part: SchematicManager) -> DesignValidationBuilder:
        """
         Creates a @link NXOpen::Schematic::DesignValidationBuilder NXOpen::Schematic::DesignValidationBuilder@endlink . 
         @return builder (@link DesignValidationBuilder NXOpen.Schematic.DesignValidationBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Schematic::FlowDirectionArrowBuilder NXOpen::Schematic::FlowDirectionArrowBuilder@endlink . 
    ##  @return builder (@link FlowDirectionArrowBuilder NXOpen.Schematic.FlowDirectionArrowBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="node"> (@link NXOpen.Diagramming.Node NXOpen.Diagramming.Node@endlink) </param>
    def CreateFdaBuilder(part: SchematicManager, node: NXOpen.Diagramming.Node) -> FlowDirectionArrowBuilder:
        """
         Creates a @link NXOpen::Schematic::FlowDirectionArrowBuilder NXOpen::Schematic::FlowDirectionArrowBuilder@endlink . 
         @return builder (@link FlowDirectionArrowBuilder NXOpen.Schematic.FlowDirectionArrowBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Schematic::NodeBuilder NXOpen::Schematic::NodeBuilder@endlink . 
    ##  @return builder (@link NodeBuilder NXOpen.Schematic.NodeBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ##  @link NXOpen::Schematic::Node NXOpen::Schematic::Node@endlink  to be edited, if NULL then create a new one 
    def CreateNodeBuilder(part: SchematicManager, node: Node) -> NodeBuilder:
        """
         Creates a @link NXOpen::Schematic::NodeBuilder NXOpen::Schematic::NodeBuilder@endlink . 
         @return builder (@link NodeBuilder NXOpen.Schematic.NodeBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Schematic::OffSheetConnectorBuilder NXOpen::Schematic::OffSheetConnectorBuilder@endlink . 
    ##  @return builder (@link OffSheetConnectorBuilder NXOpen.Schematic.OffSheetConnectorBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="oscObject"> (@link OffSheetConnector NXOpen.Schematic.OffSheetConnector@endlink) </param>
    def CreateOffSheetConnectorBuilder(part: SchematicManager, oscObject: OffSheetConnector) -> OffSheetConnectorBuilder:
        """
         Creates a @link NXOpen::Schematic::OffSheetConnectorBuilder NXOpen::Schematic::OffSheetConnectorBuilder@endlink . 
         @return builder (@link OffSheetConnectorBuilder NXOpen.Schematic.OffSheetConnectorBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Schematic::PreferencesBuilder NXOpen::Schematic::PreferencesBuilder@endlink . 
    ##  @return builder (@link PreferencesBuilder NXOpen.Schematic.PreferencesBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sheet"> (@link Sheet NXOpen.Schematic.Sheet@endlink) </param>
    def CreatePreferencesBuilder(part: SchematicManager, sheet: Sheet) -> PreferencesBuilder:
        """
         Creates a @link NXOpen::Schematic::PreferencesBuilder NXOpen::Schematic::PreferencesBuilder@endlink . 
         @return builder (@link PreferencesBuilder NXOpen.Schematic.PreferencesBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Schematic::Sheet NXOpen::Schematic::Sheet@endlink . 
    ##  @return sheet (@link Sheet NXOpen.Schematic.Sheet@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    def CreateSheet(part: SchematicManager) -> Sheet:
        """
         Creates a @link NXOpen::Schematic::Sheet NXOpen::Schematic::Sheet@endlink . 
         @return sheet (@link Sheet NXOpen.Schematic.Sheet@endlink): .
        """
        pass
    
    ##  Exports run 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ##  The runs to be exported 
    def ExportRunNative(part: SchematicManager, runTags: List[NXOpen.NXObject], destination: str) -> None:
        """
         Exports run 
        """
        pass
    
    ##  Exports run 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ##  The runs to be exported 
    def ExportRunNativeWithSpecificName(part: SchematicManager, runTags: List[NXOpen.NXObject], fileNames: List[str], destination: str) -> None:
        """
         Exports run 
        """
        pass
    
    ##  Makes the inline @link NXOpen::Schematic::Node NXOpen::Schematic::Node@endlink  terminating in branch or not. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="node"> (@link Node NXOpen.Schematic.Node@endlink) </param>
    ## <param name="isTerminating"> (bool) </param>
    def MakeBranchTerminating(part: SchematicManager, node: Node, isTerminating: bool) -> None:
        """
         Makes the inline @link NXOpen::Schematic::Node NXOpen::Schematic::Node@endlink  terminating in branch or not. 
        """
        pass
    
    ##  Removes the branch from the run. The connections of the removed branch will be moved to unassigned folder. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="run"> (@link NXOpen.Schematic.Mechanical.Run NXOpen.Schematic.Mechanical.Run@endlink) </param>
    ## <param name="branch"> (@link NXOpen.Schematic.Mechanical.Branch NXOpen.Schematic.Mechanical.Branch@endlink) </param>
    def RemoveBranchFromRun(part: SchematicManager, run: NXOpen.Schematic.Mechanical.Run, branch: NXOpen.Schematic.Mechanical.Branch) -> None:
        """
         Removes the branch from the run. The connections of the removed branch will be moved to unassigned folder. 
        """
        pass
    
    ##  Moves branch from one run to another. The original branch will be destroyed. 
    ##  @return newbranch (@link NXOpen.Schematic.Mechanical.Branch NXOpen.Schematic.Mechanical.Branch@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sourceRun"> (@link NXOpen.Schematic.Mechanical.Run NXOpen.Schematic.Mechanical.Run@endlink) </param>
    ## <param name="destinationRun"> (@link NXOpen.Schematic.Mechanical.Run NXOpen.Schematic.Mechanical.Run@endlink) </param>
    ## <param name="oldbranch"> (@link NXOpen.Schematic.Mechanical.Branch NXOpen.Schematic.Mechanical.Branch@endlink) </param>
    def ReparentBranch(part: SchematicManager, sourceRun: NXOpen.Schematic.Mechanical.Run, destinationRun: NXOpen.Schematic.Mechanical.Run, oldbranch: NXOpen.Schematic.Mechanical.Branch) -> NXOpen.Schematic.Mechanical.Branch:
        """
         Moves branch from one run to another. The original branch will be destroyed. 
         @return newbranch (@link NXOpen.Schematic.Mechanical.Branch NXOpen.Schematic.Mechanical.Branch@endlink): .
        """
        pass
    
import NXOpen
##  Represents a collection of Schematic.Sheet.  <br> To obtain an instance of this class, refer to @link NXOpen::Schematic::SchematicManager  NXOpen::Schematic::SchematicManager @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class SheetCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Schematic.Sheet. """


    ##  Finds the @link Schematic::Sheet Schematic::Sheet@endlink  with the given identifier as recorded in a journal.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return sheet (@link Sheet NXOpen.Schematic.Sheet@endlink):  @link Schematic::Sheet Schematic::Sheet@endlink  with this name. .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ##  Identifier to be found 
    def FindObject(part: SheetCollection, journalIdentifier: str) -> Sheet:
        """
         Finds the @link Schematic::Sheet Schematic::Sheet@endlink  with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         @return sheet (@link Sheet NXOpen.Schematic.Sheet@endlink):  @link Schematic::Sheet Schematic::Sheet@endlink  with this name. .
        """
        pass
    
import NXOpen
##  
##         Represents Schematic Sheet class
##      <br> Use the static method to obtain an instance.  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class Sheet(NXOpen.NXObject): 
    """ 
        Represents Schematic Sheet class
    """


    ##  Returns the @link NXOpen::Schematic::ObjectTableCollection  NXOpen::Schematic::ObjectTableCollection @endlink  belonging to this part 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @link ObjectTableCollection NXOpen.Schematic.ObjectTableCollection@endlink
    @property
    def ObjectTables() -> ObjectTableCollection:
        """
         Returns the @link NXOpen::Schematic::ObjectTableCollection  NXOpen::Schematic::ObjectTableCollection @endlink  belonging to this part 
        """
        pass
    
##  Represents the symbol source options. 
##  from the reuse library. 
class SymbolSourceOption(Enum):
    """
    Members Include: <ReuseLibrary> <ExistingSymbol> <ModelNode>
    """
    ReuseLibrary: int
    ExistingSymbol: int
    ModelNode: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> SymbolSourceOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
import NXOpen.PDM
##  Represents a builder class that performs Schematic System Context operations. <br> To create a new instance of this class, use @link NXOpen::Schematic::SystemManager::CreateSystemContextBuilder  NXOpen::Schematic::SystemManager::CreateSystemContextBuilder @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class SystemContextBuilder(NXOpen.Builder): 
    """ Represents a builder class that performs Schematic System Context operations."""


    ## Getter for property: (@link NXOpen.PDM.ConfigurationContextBuilder NXOpen.PDM.ConfigurationContextBuilder@endlink) ConfigurationContext
    ##   the configuration context builder.  
    ##      
    ##  
    ## Getter License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.PDM.ConfigurationContextBuilder
    @property
    def ConfigurationContext(self) -> NXOpen.PDM.ConfigurationContextBuilder:
        """
        Getter for property: (@link NXOpen.PDM.ConfigurationContextBuilder NXOpen.PDM.ConfigurationContextBuilder@endlink) ConfigurationContext
          the configuration context builder.  
             
         
        """
        pass
    
    ##  Sets the system of the SystemContextBuilder. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_diagramming ("NX Diagramming")
    ## 
    ## <param name="plmObjectFileSpec"> (str) </param>
    def SetSystem(builder: SystemContextBuilder, plmObjectFileSpec: str) -> None:
        """
         Sets the system of the SystemContextBuilder. 
        """
        pass
    
import NXOpen
##  A manager to deal with all objects.  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class SystemManager(NXOpen.Object): 
    """ A manager to deal with all objects. """


    ##  Creates a @link NXOpen::Schematic::FileNewApplicationBuilder NXOpen::Schematic::FileNewApplicationBuilder@endlink  
    ##  @return builder (@link FileNewApplicationBuilder NXOpen.Schematic.FileNewApplicationBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_diagramming ("NX Diagramming")
    def CreateFileNewApplicationBuilder() -> FileNewApplicationBuilder:
        """
         Creates a @link NXOpen::Schematic::FileNewApplicationBuilder NXOpen::Schematic::FileNewApplicationBuilder@endlink  
         @return builder (@link FileNewApplicationBuilder NXOpen.Schematic.FileNewApplicationBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Schematic::SystemContextBuilder NXOpen::Schematic::SystemContextBuilder@endlink  
    ##  @return builder (@link SystemContextBuilder NXOpen.Schematic.SystemContextBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_diagramming ("NX Diagramming")
    def CreateSystemContextBuilder() -> SystemContextBuilder:
        """
         Creates a @link NXOpen::Schematic::SystemContextBuilder NXOpen::Schematic::SystemContextBuilder@endlink  
         @return builder (@link SystemContextBuilder NXOpen.Schematic.SystemContextBuilder@endlink): .
        """
        pass
    
## @package NXOpen.Schematic
## Classes, Enums and Structs under NXOpen.Schematic namespace

##  @link ObjectTableBuilderStockOption NXOpen.Schematic.ObjectTableBuilderStockOption @endlink is an alias for @link ObjectTableBuilder.StockOption NXOpen.Schematic.ObjectTableBuilder.StockOption@endlink
ObjectTableBuilderStockOption = ObjectTableBuilder.StockOption


##  @link OffSheetConnectorBuilderStyleOption NXOpen.Schematic.OffSheetConnectorBuilderStyleOption @endlink is an alias for @link OffSheetConnectorBuilder.StyleOption NXOpen.Schematic.OffSheetConnectorBuilder.StyleOption@endlink
OffSheetConnectorBuilderStyleOption = OffSheetConnectorBuilder.StyleOption


