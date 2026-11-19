from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class BaseObjectBuilder(NXOpen.Builder): 
    """  Represents a BaseObjectBuilder.  """
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
         Returns the id of the object.  
             
         
        """
        pass
    @property
    def Label(self) -> str:
        """
        Getter for property: (str) Label
         Returns the tag of this object.  
             
         
        """
        pass
    @property
    def Sheet(self) -> Sheet:
        """
        Getter for property: ( Sheet NXOpen.) Sheet
         Returns the sheet containing the object.  
             
         
        """
        pass
    @Sheet.setter
    def Sheet(self, sheet: Sheet):
        """
        Setter for property: ( Sheet NXOpen.) Sheet
         Returns the sheet containing the object.  
             
         
        """
        pass
    def GetDisciplines(self) -> List[str]:
        """
         Gets the discipline of the object. 
         Returns disciplines (List[str]): .
        """
        pass
    def SetDisciplines(self, disciplines: List[str]) -> None:
        """
         Sets the discipline of the object. 
        """
        pass
import NXOpen
import NXOpen.Diagramming
class BulkEditBuilder(NXOpen.Builder): 
    """
    Represents a BulkEditBuilder to edit bulk of objects.
    """
    def SetDeltaXCoordinate(self, deltaXCoordinate: float) -> None:
        """
         Sets the delta value of X coordinate for bulk moving. 
        """
        pass
    def SetDeltaYCoordinate(self, deltaYCoordinate: float) -> None:
        """
         Sets the delta value of Y coordinate for bulk moving. 
        """
        pass
    def SetHide(self, hide: bool) -> None:
        """
         Sets the visibility of sheet elements. 
        """
        pass
    def SetHideLabel(self, hideLabel: bool) -> None:
        """
         Sets the visibility of labels. 
        """
        pass
    def SetSheetElements(self, sheetElements: List[NXOpen.Diagramming.SheetElement]) -> None:
        """
         Sets the sheet elements for bulk editing. 
        """
        pass
import NXOpen
class BulkReplaceBuilder(NXOpen.Builder): 
    """
    Represents a BulkReplaceBuilder to  bulk replace of objects.
    """
    def AddReplacementData(self, replacementData: ReplacementData) -> None:
        """
         Adds the replacement data for bulk replace. 
        """
        pass
    def SetReplacementData(self, replacementData: List[ReplacementData]) -> None:
        """
         Sets the replacement data for bulk replace. 
        """
        pass
class ConnectionAttributeSourceType(Enum):
    """
    Members Include: 
     |Object| 
     |Stock| 
     |Insulation| 
     |CableType| 

    """
    Object: int
    Stock: int
    Insulation: int
    CableType: int
    @staticmethod
    def ValueOf(value: int) -> ConnectionAttributeSourceType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.Diagramming
class ConnectionBuilder(BaseObjectBuilder): 
    """  Represents a ConnectionBuilder.  """
    @property
    def CableType(self) -> str:
        """
        Getter for property: (str) CableType
         Returns the cable type of the connection.  
             
         
        """
        pass
    @CableType.setter
    def CableType(self, cableType: str):
        """
        Setter for property: (str) CableType
         Returns the cable type of the connection.  
             
         
        """
        pass
    @property
    def ConnectionData(self) -> ConnectionDataBuilder:
        """
        Getter for property: ( ConnectionDataBuilder NXOpen.) ConnectionData
         Returns the connection data builder.  
             
         
        """
        pass
    @property
    def ElementId(self) -> str:
        """
        Getter for property: (str) ElementId
         Returns the current element ID of this connection.  
           It works only in edit mode, it's optional and the first element ID stored in the connection will be used as default.  
         
        """
        pass
    @ElementId.setter
    def ElementId(self, elementId: str):
        """
        Setter for property: (str) ElementId
         Returns the current element ID of this connection.  
           It works only in edit mode, it's optional and the first element ID stored in the connection will be used as default.  
         
        """
        pass
    @property
    def EndJunction(self) -> NodeBuilder:
        """
        Getter for property: ( NodeBuilder NXOpen.) EndJunction
         Returns the end junction builder.  
             
         
        """
        pass
    @property
    def SplittedConnection(self) -> Connection:
        """
        Getter for property: ( Connection NXOpen.) SplittedConnection
         Returns the new created connection after breaking the old connection.  
             
         
        """
        pass
    @property
    def StartJunction(self) -> NodeBuilder:
        """
        Getter for property: ( NodeBuilder NXOpen.) StartJunction
         Returns the start junction builder.  
             
         
        """
        pass
    def CreateConnectionData(self) -> ConnectionDataBuilder:
        """
         Creates the connection data builder. 
         Returns connectionData ( ConnectionDataBuilder NXOpen.): .
        """
        pass
    def CreateEndJunction(self, node: Node) -> NodeBuilder:
        """
         Creates the end junction builder. 
         Returns junctionBuilder ( NodeBuilder NXOpen.): .
        """
        pass
    def CreateStartJunction(self, node: Node) -> NodeBuilder:
        """
         Creates the start junction builder. 
         Returns junctionBuilder ( NodeBuilder NXOpen.): .
        """
        pass
    def GetBendPoints(self) -> List[NXOpen.Point2d]:
        """
         Get bending points for polyline to render the connection. 
         Returns points ( NXOpen.Point2d Li): .
        """
        pass
    def GetConnection(self) -> NXOpen.Diagramming.Connection:
        """
         Get the connection object of the connection builder. 
         Returns connection ( NXOpen.Diagramming.Connection): .
        """
        pass
    def GetEnd(self) -> Port:
        """
         Gets the end port of this connection.
         Returns port ( Port NXOpen.): .
        """
        pass
    def GetEndLocation(self) -> NXOpen.Point2d:
        """
         Get the end location of this connection.
                    This end location is applicable only when the Diagramming.ConnectionBuilder.End port is . 
         Returns endLocation ( NXOpen.Point2d): .
        """
        pass
    def GetEndNode(self) -> Node:
        """
         Gets the end Node of this connection.
                 Note: When the builder is commited, a dynamic Port will be used and can be found in the GetEnd method
         Returns node ( Node NXOpen.): .
        """
        pass
    def GetLineType(self) -> str:
        """
         Gets the line type of the connection. 
         Returns lineType (str): .
        """
        pass
    def GetShapeType(self) -> NXOpen.Diagramming.ConnectionBuilder.ShapeOption:
        """
         Gets the connection shape. 
         Returns shapeType ( NXOpen.Diagramming.ConnectionBuilder.ShapeOption): .
        """
        pass
    def GetStart(self) -> Port:
        """
         Gets the start port of this connection in native. 
         Returns port ( Port NXOpen.): .
        """
        pass
    def GetStartLocation(self) -> NXOpen.Point2d:
        """
         Get the start location of this connection.
                    This start location is applicable only when the Diagramming.ConnectionBuilder.Start is .
         Returns startLocation ( NXOpen.Point2d): .
        """
        pass
    def GetStartNode(self) -> Node:
        """
         Gets the start Node of this connection. 
                Note: When the builder is commited, a dynamic Port will be used and can be found in the GetStart method
         Returns node ( Node NXOpen.): .
        """
        pass
    def GetTeeEndLocation(self) -> Tuple[Connection, int, float]:
        """
         Get the connection location for tee object at the end of the connection. 
         Returns A tuple consisting of (connection, segmentId, percent). 
         - connection is:  Connection NXOpen..
         - segmentId is: int.
         - percent is: float.

        """
        pass
    def GetTeeStartLocation(self) -> Tuple[Connection, int, float]:
        """
         Get the connection location for tee object at the start of the connection. 
         Returns A tuple consisting of (connection, segmentId, percent). 
         - connection is:  Connection NXOpen..
         - segmentId is: int.
         - percent is: float.

        """
        pass
    def SetBendPoints(self, points: List[NXOpen.Point2d]) -> None:
        """
         Set bending points for polyline to render the connection. 
        """
        pass
    def SetEnd(self, port: Port) -> None:
        """
         Sets the end port of this connection.
        """
        pass
    def SetEndLocation(self, endLocation: NXOpen.Point2d) -> None:
        """
         Set the end location of this connection.
                    This end location is applicable only when the Diagramming.ConnectionBuilder.End port is . 
        """
        pass
    def SetEndNode(self, node: Node, percentX: float, percentY: float, offsetX: float, offsetY: float, connectionDirectionX: float, connectionDirectionY: float, trimPolicy: ConnectionTrimPolicyType) -> None:
        """
         Sets the end Node of this connection.
                Note: When the builder is commited, a Dynamic Port will be created based on the the other inputs.
                This dynamic Port can be found in the GetEnd method
        """
        pass
    def SetLineType(self, lineType: str) -> None:
        """
         Sets the line type of the connection. 
        """
        pass
    def SetShapeType(self, shapeType: NXOpen.Diagramming.ConnectionBuilder.ShapeOption) -> None:
        """
         Sets the connection shape. 
        """
        pass
    def SetStart(self, port: Port) -> None:
        """
         Sets the start port of this connection in native. 
        """
        pass
    def SetStartLocation(self, startLocation: NXOpen.Point2d) -> None:
        """
         Set the start location of this connection.
                    This start location is applicable only when the Diagramming.ConnectionBuilder.Start is .
        """
        pass
    def SetStartNode(self, node: Node, percentX: float, percentY: float, offsetX: float, offsetY: float, connectionDirectionX: float, connectionDirectionY: float, trimPolicy: ConnectionTrimPolicyType) -> None:
        """
         Sets the start Node of this connection. 
                Note: When the builder is commited, a Dynamic Port will be created based on the the other inputs. 
                This dynamic Port can be found in the GetStart method
        """
        pass
    def SetTeeEndLocation(self, connection: Connection, segmentId: int, percent: float) -> None:
        """
         Set the connection location for tee object at the end of the connection. 
        """
        pass
    def SetTeeStartLocation(self, connection: Connection, segmentId: int, percent: float) -> None:
        """
         Set the connection location for tee object at the start of the connection. 
        """
        pass
import NXOpen
class ConnectionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Schematic.Connection. """
    def FindObject(self, journalIdentifier: str) -> Connection:
        """
         Finds the Schematic.Connection with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         Returns connection ( Connection NXOpen.):  Schematic.Connection with this name. .
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ConnectionDataBuilder(NXOpen.TaggedObject): 
    """  Represents a ConnectionDataBuilder.  """
    @property
    def InsulationId(self) -> str:
        """
        Getter for property: (str) InsulationId
         Returns the insulation id.  
             
         
        """
        pass
    @InsulationId.setter
    def InsulationId(self, insulationId: str):
        """
        Setter for property: (str) InsulationId
         Returns the insulation id.  
             
         
        """
        pass
    @property
    def StockId(self) -> str:
        """
        Getter for property: (str) StockId
         Returns the stock id.  
             
         
        """
        pass
    @StockId.setter
    def StockId(self, stockId: str):
        """
        Setter for property: (str) StockId
         Returns the stock id.  
             
         
        """
        pass
    def GetSourceAttributeOwner(self, sourceType: ConnectionAttributeSourceType) -> NXOpen.NXObject:
        """
         Gets the attribute owner of the object.
         Returns owner ( NXOpen.NXObject): .
        """
        pass
class ConnectionEndType(Enum):
    """
    Members Include: 
     |Start|  The start of connection. 
     |End|  The end of connection. 

    """
    Start: int
    End: int
    @staticmethod
    def ValueOf(value: int) -> ConnectionEndType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class ConnectionTrimPolicyType(Enum):
    """
    Members Include: 
     |NodeAndPort| 
     |Port| 
     |Node| 
     |NoTrim| 

    """
    NodeAndPort: int
    Port: int
    Node: int
    NoTrim: int
    @staticmethod
    def ValueOf(value: int) -> ConnectionTrimPolicyType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class Connection(NXOpen.NXObject): 
    """ Represents the schematic connection class. """
    def Detach(self, port: Port) -> None:
        """
         Detaches from the schematic Port and optionally, allow port deletion if it was dynamically created. This can be replaced with JA_SCHEMATIC_CONNECTION_DetachPort. 
        """
        pass
    def DetachPort(self, port: Port, detachStart: bool) -> None:
        """
         Detaches from the diagramming Port and optionally, allow port deletion if it was dynamically created. This is more common API to use.
        """
        pass
    def Refresh(self) -> None:
        """
         Refreshes the connection. 
        """
        pass
    def ReverseAuxiliaryLine(self) -> None:
        """
         Reverses the offset direction of the auxiliary line along the connection. 
        """
        pass
import NXOpen
class DesignValidationBuilder(NXOpen.Builder): 
    """  Represents a DesignValidationBuilder.  """
    @property
    def SaveResult(self) -> bool:
        """
        Getter for property: (bool) SaveResult
         Returns the option to save validation result   
            
         
        """
        pass
    @SaveResult.setter
    def SaveResult(self, saveResult: bool):
        """
        Setter for property: (bool) SaveResult
         Returns the option to save validation result   
            
         
        """
        pass
    def GetSelectedCheckerIds(self) -> List[str]:
        """
         Gets the selected checker ids 
         Returns selectedCheckerIds (List[str]):  A list of checker ids .
        """
        pass
    def SetSelectedCheckerIds(self, selectedCheckerIds: List[str]) -> None:
        """
         Specifies the selected checker ids 
        """
        pass
class EquipmentAttributeSourceType(Enum):
    """
    Members Include: 
     |Object| 
     |Classification| 

    """
    Object: int
    Classification: int
    @staticmethod
    def ValueOf(value: int) -> EquipmentAttributeSourceType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class FileNewApplicationBuilder(NXOpen.Builder): 
    """ Represents a builder class that performs New Sheet operations. """
    @property
    def FileNew(self) -> NXOpen.FileNew:
        """
        Getter for property: ( NXOpen.FileNew) FileNew
         Returns the file new object   
            
         
        """
        pass
    @FileNew.setter
    def FileNew(self, fileNew: NXOpen.FileNew):
        """
        Setter for property: ( NXOpen.FileNew) FileNew
         Returns the file new object   
            
         
        """
        pass
    def SetSystem(self, systemSpec: str) -> None:
        """
         Set the system object of sheet 
        """
        pass
import NXOpen
class FlowDirectionArrowBuilder(NXOpen.Builder): 
    """ 
    Represents FlowDirectionArrowBuilder 
     """
    @property
    def LocationPercent(self) -> float:
        """
        Getter for property: (float) LocationPercent
         Returns the percent along the segment for this Flow Direction Arrow.  
             
         
        """
        pass
    @LocationPercent.setter
    def LocationPercent(self, locationPercent: float):
        """
        Setter for property: (float) LocationPercent
         Returns the percent along the segment for this Flow Direction Arrow.  
             
         
        """
        pass
    @property
    def LocationSegment(self) -> int:
        """
        Getter for property: (int) LocationSegment
         Returns the segment this Flow Direction Arrow is located on.  
             
         
        """
        pass
    @LocationSegment.setter
    def LocationSegment(self, locationPercent: int):
        """
        Setter for property: (int) LocationSegment
         Returns the segment this Flow Direction Arrow is located on.  
             
         
        """
        pass
    def GetConnection(self) -> Connection:
        """
         Gets the connection for this Flow Direction Arrow. 
         Returns connection ( Connection NXOpen.): .
        """
        pass
    def ReverseDirection(self) -> None:
        """
         Change the direction of FDA. 
        """
        pass
    def SetConnection(self, connection: Connection) -> None:
        """
         Sets the connection for this Flow Direction Arrow. 
        """
        pass
import NXOpen
class FlowDirectionArrow(NXOpen.NXObject): 
    """  A symbol that indicates the direction the of the flow """
    pass
class InstrumentationSymbolType(Enum):
    """
    Members Include: 
     |DiscreteInstrumentPrimaryLocation|  discrete instrument and primary location. 
     |DiscreteInstrumentFieldMounted|  discrete instrument and field mounted. 
     |DiscreteInstrumentAuxiliaryLocation|  discrete instrument and auxiliary location. 
     |SharedDisplaySharedControlPrimaryLocation|  shared display, shared control and primary location. 
     |SharedDisplaySharedControlFieldMounted|  shared display, shared control and field mounted. 
     |SharedDisplaySharedControlAuxiliaryLocation|  shared display, shared control and auxiliary location. 
     |ComputerFunctionPrimaryLocation|  computer function and primary location. 
     |ComputerFunctionFieldMounted|  computer function and field mounted. 
     |ComputerFunctionAuxiliaryLocation|  computer function and auxiliary location. 
     |ProgrammableLogicControlPrimaryLocation|  programmable logic control and primary location. 
     |ProgrammableLogicControlFieldMounted|  programmable logic control and field mounted. 
     |ProgrammableLogicControlAuxiliaryLocation|  programmable logic control and auxiliary location. 

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
    @staticmethod
    def ValueOf(value: int) -> InstrumentationSymbolType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class InstrumentationType(Enum):
    """
    Members Include: 
     |NotSet|  not a instrumentation. 
     |Symbol|  instrumentation symbol. 

    """
    NotSet: int
    Symbol: int
    @staticmethod
    def ValueOf(value: int) -> InstrumentationType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class JaSchematicPropertytype(Enum):
    """
    Members Include: 
     |Null|  Null type 
     |Index|  Index of object 
     |UserAttribute|  User attribute 
     |Id|  ID object 
     |Name|  Name of object 
     |Symbol|  The symbol svg 
     |SymbolDescription|  The symbol description 
     |Quantity|  The quantity of same object 
     |ParentRun|  The parent run of pipe stock 
     |RunAttribute|  The attribute of run object 
     |EquipmentAttribute|  The attribute of equipment object 
     |PipeAttribute|  Pipe  attribute 
     |BranchAttribute|  The attribute of branch object 
     |StockAttribute|  The attribute of stock object 
     |SymbolAttribute|  The attribute of symbol object 
     |CableAttribute|  The attribute of cable object 

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
    StockAttribute: int
    SymbolAttribute: int
    CableAttribute: int
    @staticmethod
    def ValueOf(value: int) -> JaSchematicPropertytype:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.Diagramming
class NodeBuilder(BaseObjectBuilder): 
    """  Represents a NodeBuilder.  """
    @property
    def ExistingSymbol(self) -> NXOpen.Diagramming.Node:
        """
        Getter for property: ( NXOpen.Diagramming.Node) ExistingSymbol
         Returns the symbol from foundation window.  
           It is only applicable when  Schematic::NodeBuilder::SymbolSourceType  is  Schematic::SymbolSourceOptionExistingSymbol .  
         
        """
        pass
    @ExistingSymbol.setter
    def ExistingSymbol(self, existingSymbol: NXOpen.Diagramming.Node):
        """
        Setter for property: ( NXOpen.Diagramming.Node) ExistingSymbol
         Returns the symbol from foundation window.  
           It is only applicable when  Schematic::NodeBuilder::SymbolSourceType  is  Schematic::SymbolSourceOptionExistingSymbol .  
         
        """
        pass
    @property
    def FlipHorizontal(self) -> bool:
        """
        Getter for property: (bool) FlipHorizontal
         Returns the option to flip the symbol horizontally.  
             
         
        """
        pass
    @FlipHorizontal.setter
    def FlipHorizontal(self, flipHorizontal: bool):
        """
        Setter for property: (bool) FlipHorizontal
         Returns the option to flip the symbol horizontally.  
             
         
        """
        pass
    @property
    def FlipVertical(self) -> bool:
        """
        Getter for property: (bool) FlipVertical
         Returns the option to flip the symbol vertically.  
             
         
        """
        pass
    @FlipVertical.setter
    def FlipVertical(self, flipVertical: bool):
        """
        Setter for property: (bool) FlipVertical
         Returns the option to flip the symbol vertically.  
             
         
        """
        pass
    @property
    def LockAspectRatio(self) -> bool:
        """
        Getter for property: (bool) LockAspectRatio
         Returns the option to lock the aspect ratio.  
             
         
        """
        pass
    @LockAspectRatio.setter
    def LockAspectRatio(self, lockAspectRatio: bool):
        """
        Setter for property: (bool) LockAspectRatio
         Returns the option to lock the aspect ratio.  
             
         
        """
        pass
    @property
    def NodeType(self) -> NodeType:
        """
        Getter for property: ( NodeType NXOpen.) NodeType
         Returns the node type.  
             
         
        """
        pass
    @NodeType.setter
    def NodeType(self, nodeType: NodeType):
        """
        Setter for property: ( NodeType NXOpen.) NodeType
         Returns the node type.  
             
         
        """
        pass
    @property
    def RelativeLocation(self) -> NXOpen.Diagramming.LocationBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.LocationBuilder) RelativeLocation
         Returns the node relative location.  
             
         
        """
        pass
    @property
    def Rotate(self) -> RotateAngleOption:
        """
        Getter for property: ( RotateAngleOption NXOpen.) Rotate
         Returns the symbol rotation angle.  
             
         
        """
        pass
    @Rotate.setter
    def Rotate(self, rotate: RotateAngleOption):
        """
        Setter for property: ( RotateAngleOption NXOpen.) Rotate
         Returns the symbol rotation angle.  
             
         
        """
        pass
    @property
    def Scale(self) -> float:
        """
        Getter for property: (float) Scale
         Returns the scale value.  
           It is only applicable when  Schematic::NodeBuilder::LockAspectRatio  is true.  
         
        """
        pass
    @Scale.setter
    def Scale(self, scale: float):
        """
        Setter for property: (float) Scale
         Returns the scale value.  
           It is only applicable when  Schematic::NodeBuilder::LockAspectRatio  is true.  
         
        """
        pass
    @property
    def ScaleX(self) -> float:
        """
        Getter for property: (float) ScaleX
         Returns the x scale value.  
           It is only applicable when  Schematic::NodeBuilder::LockAspectRatio  is false.  
         
        """
        pass
    @ScaleX.setter
    def ScaleX(self, scaleX: float):
        """
        Setter for property: (float) ScaleX
         Returns the x scale value.  
           It is only applicable when  Schematic::NodeBuilder::LockAspectRatio  is false.  
         
        """
        pass
    @property
    def ScaleY(self) -> float:
        """
        Getter for property: (float) ScaleY
         Returns the y scale value.  
           It is only applicable when  Schematic::NodeBuilder::LockAspectRatio  is false.  
         
        """
        pass
    @ScaleY.setter
    def ScaleY(self, scaleY: float):
        """
        Setter for property: (float) ScaleY
         Returns the y scale value.  
           It is only applicable when  Schematic::NodeBuilder::LockAspectRatio  is false.  
         
        """
        pass
    @property
    def SplittedConnection(self) -> Connection:
        """
        Getter for property: ( Connection NXOpen.) SplittedConnection
         Returns the new created connection after breaking the old connection.  
             
         
        """
        pass
    @property
    def SymbolId(self) -> str:
        """
        Getter for property: (str) SymbolId
         Returns the symbol ID of this node.  
           It is only applicable when  NXOpen::Schematic::NodeBuilder::SymbolSourceType  is  NXOpen::Schematic::SymbolSourceOptionReuseLibrary .  
         
        """
        pass
    @SymbolId.setter
    def SymbolId(self, symbolId: str):
        """
        Setter for property: (str) SymbolId
         Returns the symbol ID of this node.  
           It is only applicable when  NXOpen::Schematic::NodeBuilder::SymbolSourceType  is  NXOpen::Schematic::SymbolSourceOptionReuseLibrary .  
         
        """
        pass
    @property
    def SymbolSourceType(self) -> SymbolSourceOption:
        """
        Getter for property: ( SymbolSourceOption NXOpen.) SymbolSourceType
         Returns the symbol source type   
            
         
        """
        pass
    @SymbolSourceType.setter
    def SymbolSourceType(self, symbolSourceType: SymbolSourceOption):
        """
        Setter for property: ( SymbolSourceOption NXOpen.) SymbolSourceType
         Returns the symbol source type   
            
         
        """
        pass
    @property
    def TextStyle(self) -> NXOpen.Diagramming.TextStyleBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.TextStyleBuilder) TextStyle
         Returns the text style   
            
         
        """
        pass
    @property
    def UseExistingSymbolId(self) -> bool:
        """
        Getter for property: (bool) UseExistingSymbolId
         Returns the option to place a symbol referencing an existing equipment.  
             
         
        """
        pass
    @UseExistingSymbolId.setter
    def UseExistingSymbolId(self, useExistingID: bool):
        """
        Setter for property: (bool) UseExistingSymbolId
         Returns the option to place a symbol referencing an existing equipment.  
             
         
        """
        pass
    def DetachAllConnections(self) -> None:
        """
         Detaches the equipment from all attached connections. 
        """
        pass
    def DetachPortOnNode(self, portId: str) -> None:
        """
         Detaches specific port on node
        """
        pass
    def GetInlineSymbolLocation(self) -> Tuple[Connection, int, float]:
        """
         Gets connection location for the inline symbol. 
         Returns A tuple consisting of (connection, segementId, percent). 
         - connection is:  Connection NXOpen..
         - segementId is: int.
         - percent is: float.

        """
        pass
    def GetLocation(self) -> NXOpen.Point2d:
        """
         Gets the symbol location. 
         Returns location ( NXOpen.Point2d):  the symbol location. .
        """
        pass
    def GetNewInlineConnection(self) -> Tuple[NXOpen.NXObject, str]:
        """
         Gets new connection after inserting an inline symbol.
         Returns A tuple consisting of (con, connectionId). 
         - con is:  NXOpen.NXObject.
         - connectionId is: str.

        """
        pass
    def GetNode(self) -> NXOpen.Diagramming.Node:
        """
         Get the node object of the equipment builder. 
         Returns node ( NXOpen.Diagramming.Node): .
        """
        pass
    def GetSourceAttributeOwner(self, sourceType: EquipmentAttributeSourceType) -> NXOpen.NXObject:
        """
         Gets the attribute owner of the object.
         Returns owner ( NXOpen.NXObject): .
        """
        pass
    def ReplaceSymbol(self, symbolId: str) -> None:
        """
         Replaces the symbol of this node to another one. 
        """
        pass
    def SetAttachedSymbol(self, sourcePortId: str, toSymbol: Node, targetPortId: str) -> None:
        """
         Sets target port attaching to source port. 
        """
        pass
    def SetInlineSymbolLocation(self, connection: Connection, segementId: int, percent: float) -> None:
        """
         Sets connection location for the inline symbol. 
        """
        pass
    def SetLocation(self, location: NXOpen.Point2d) -> None:
        """
         Sets the symbol location. 
        """
        pass
import NXOpen
class NodeCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Schematic.Node. """
    def FindObject(self, journalIdentifier: str) -> Node:
        """
         Finds the Schematic.Node with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         Returns node ( Node NXOpen.):  Schematic.Node with this name. .
        """
        pass
class NodeType(Enum):
    """
    Members Include: 
     |Default|  default node. 
     |Fitting|  fitting node. 

    """
    Default: int
    Fitting: int
    @staticmethod
    def ValueOf(value: int) -> NodeType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class Node(NXOpen.NXObject): 
    """ Represents the schematic node class. """
    def CreateDynamicPort(self, percentX: float, percentY: float, offsetX: float, offsetY: float) -> Port:
        """
         Create a dynamic port for the node. 
         Returns dynamicPort ( Port NXOpen.): .
        """
        pass
    def Refresh(self) -> None:
        """
         Refresh the node display. 
        """
        pass
import NXOpen
import NXOpen.Diagramming.Tables
class ObjectTableBuilder(NXOpen.Builder): 
    """  Represents a ObjectTableBuilder.  """
    class StockOption(Enum):
        """
        Members Include: 
         |Pipe|  Pipe Stock 
         |Hvac|  HVAC Stock 

        """
        Pipe: int
        Hvac: int
        @staticmethod
        def ValueOf(value: int) -> ObjectTableBuilder.StockOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Sheet(self) -> Sheet:
        """
        Getter for property: ( Sheet NXOpen.) Sheet
         Returns the sheet, only available if the ScopeType is OtherSheet.  
             
         
        """
        pass
    @Sheet.setter
    def Sheet(self, sheet: Sheet):
        """
        Setter for property: ( Sheet NXOpen.) Sheet
         Returns the sheet, only available if the ScopeType is OtherSheet.  
             
         
        """
        pass
    @property
    def StockType(self) -> ObjectTableBuilder.StockOption:
        """
        Getter for property: ( ObjectTableBuilder.StockOption NXOpen.) StockType
         Returns the stock type to output.  
           Only applicable when  
         
        """
        pass
    @StockType.setter
    def StockType(self, stockType: ObjectTableBuilder.StockOption):
        """
        Setter for property: ( ObjectTableBuilder.StockOption NXOpen.) StockType
         Returns the stock type to output.  
           Only applicable when  
         
        """
        pass
    @property
    def Table(self) -> NXOpen.Diagramming.Tables.TableBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.Tables.TableBuilder) Table
         Returns the  NXOpen::Diagramming::Tables::TableBuilder  of the  NXOpen::Diagramming::Tables::Table .  
             
         
        """
        pass
    @Table.setter
    def Table(self, diagrammingTable: NXOpen.Diagramming.Tables.TableBuilder):
        """
        Setter for property: ( NXOpen.Diagramming.Tables.TableBuilder) Table
         Returns the  NXOpen::Diagramming::Tables::TableBuilder  of the  NXOpen::Diagramming::Tables::Table .  
             
         
        """
        pass
    def AddObjectType(self, objectType: str) -> None:
        """
         Adds specified object type to the list of objects being represented in the table
        """
        pass
    def GetNumberOfPropertyColumns(self) -> int:
        """
         Gets the number of property columns. 
         Returns number (int):  the number of property columns .
        """
        pass
    def GetPropertyColumn(self, index: int) -> PropertyCellRangeBuilder:
        """
         Gets the property column at the given index. 
                    The index must be greater than or equal to 0, and less than the number of property columns. 
                
         Returns propertyColumn ( PropertyCellRangeBuilder NXOpen.): .
        """
        pass
    def InsertPropertyColumns(self, index: int, propertyTypes: List[JaSchematicPropertytype], propertyKeys: List[str]) -> None:
        """
         Inserts the given number of property columns at the given index. 
                    The index must be greater than or equal to 0, and less than or equal to the number of property columns.
                    The number of property types and the number of property keys must be same, and must be greater than 0.
                
        """
        pass
    def RemoveObjectType(self, objectType: str) -> None:
        """
         Removes object type if it exists 
        """
        pass
    def RemovePropertyColumns(self, index: int, number: int) -> None:
        """
         Removes the given number of property columns starting with the given index. 
                    The index must be greater than or equal to 0, and less than the number of property columns.
                    The number must be greater than 0, and "index + number" must be less than or equal to the number of property columns.
                
        """
        pass
import NXOpen
import NXOpen.PDM
class ObjectTableCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of ObjectTable. """
    def FindObject(self, journalIdentifier: str) -> ObjectTable:
        """
         Finds the NXOpen.Schematic.ObjectTable with the given identifier as recorded in a journal.
                   An exception will be thrown if no object can be found with given name. 
         Returns objectTable ( ObjectTable NXOpen.):  NXOpen.Schematic.ObjectTable with this name. .
        """
        pass
    def ReadFromTemplate(self, templatePartName: str) -> ObjectTable:
        """
         Reads the Schematic.ObjectTable from template part. 
                    Opens the template part with specified part name, and copies the NXOpen.Schematic.ObjectTable from template part to this sheet.
                
         Returns automaticTable ( ObjectTable NXOpen.):  the new NXOpen.Schematic.ObjectTable .
        """
        pass
    def SaveAsTemplateFromBuilder(self, automaticTable: ObjectTable, builder: NXOpen.PDM.PartOperationCreateBuilder) -> None:
        """
         Saves the NXOpen.Schematic.ObjectTable as template part. 
                    Creates a template part with specified part name on PartOperationCreateBuilder, and copies the NXOpen.Schematic.ObjectTable to the template part.
                
        """
        pass
    def SaveAsTemplateFromChar(self, automaticTable: ObjectTable, templatePartName: str) -> None:
        """
         Saves the NXOpen.Schematic.ObjectTable as template part. 
                    Creates a template part with specified part name, and copies the NXOpen.Schematic.ObjectTable to the template part.
                
        """
        pass
import NXOpen
import NXOpen.Diagramming.Tables
class ObjectTable(NXOpen.NXObject): 
    """  the object table for Schematic objects  """
    @property
    def Table(self) -> NXOpen.Diagramming.Tables.Table:
        """
        Getter for property: ( NXOpen.Diagramming.Tables.Table) Table
         Returns the  NXOpen::Diagramming::Tables::Table  which displays in sheet.  
             
         
        """
        pass
    def Refresh(self) -> None:
        """
         Refreshes the table contents. 
        """
        pass
import NXOpen
import NXOpen.Diagramming
class OffSheetConnectorBuilder(NXOpen.Builder): 
    """ 
    Builder used to model a piece of Off Sheet Connector. 
    """
    class StyleOption(Enum):
        """
        Members Include: 
         |SmallFilledArrowOut| 
         |SmallFilledArrowIn| 
         |Box| 
         |ChevronOut| 
         |ChevronIn| 
         |PipeUpFar| 
         |PipeUpClose| 
         |Details| 

        """
        SmallFilledArrowOut: int
        SmallFilledArrowIn: int
        Box: int
        ChevronOut: int
        ChevronIn: int
        PipeUpFar: int
        PipeUpClose: int
        Details: int
        @staticmethod
        def ValueOf(value: int) -> OffSheetConnectorBuilder.StyleOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ElementId(self) -> str:
        """
        Getter for property: (str) ElementId
         Returns the current element ID of this OSC.  
           It works only in edit mode, it's optional and the first element ID stored in the OSC will be used as default.  
         
        """
        pass
    @ElementId.setter
    def ElementId(self, elementId: str):
        """
        Setter for property: (str) ElementId
         Returns the current element ID of this OSC.  
           It works only in edit mode, it's optional and the first element ID stored in the OSC will be used as default.  
         
        """
        pass
    @property
    def Horizontal(self) -> bool:
        """
        Getter for property: (bool) Horizontal
         Returns the option to flip the symbol horizontally.  
             
         
        """
        pass
    @property
    def OwningSheet(self) -> Sheet:
        """
        Getter for property: ( Sheet NXOpen.) OwningSheet
         Returns the owning sheet of this sheet element.  
           Its setting method works only in creation mode.   
         
        """
        pass
    @OwningSheet.setter
    def OwningSheet(self, owningSheet: Sheet):
        """
        Setter for property: ( Sheet NXOpen.) OwningSheet
         Returns the owning sheet of this sheet element.  
           Its setting method works only in creation mode.   
         
        """
        pass
    @property
    def RotateOption(self) -> RotateAngleOption:
        """
        Getter for property: ( RotateAngleOption NXOpen.) RotateOption
         Returns the symbol rotation angle.  
             
         
        """
        pass
    @RotateOption.setter
    def RotateOption(self, rotate: RotateAngleOption):
        """
        Setter for property: ( RotateAngleOption NXOpen.) RotateOption
         Returns the symbol rotation angle.  
             
         
        """
        pass
    @property
    def Style(self) -> OffSheetConnectorBuilder.StyleOption:
        """
        Getter for property: ( OffSheetConnectorBuilder.StyleOption NXOpen.) Style
         Returns the style of OSC   
            
         
        """
        pass
    @Style.setter
    def Style(self, style: OffSheetConnectorBuilder.StyleOption):
        """
        Setter for property: ( OffSheetConnectorBuilder.StyleOption NXOpen.) Style
         Returns the style of OSC   
            
         
        """
        pass
    @property
    def TextStyleBuilder(self) -> NXOpen.Diagramming.TextStyleBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.TextStyleBuilder) TextStyleBuilder
         Returns the text style of the OSC.  
             
         
        """
        pass
    @property
    def Vertical(self) -> bool:
        """
        Getter for property: (bool) Vertical
         Returns the option to flip the symbol vertically.  
             
         
        """
        pass
    def FlipHorizontally(self) -> None:
        """
         To flip a off sheet connector horizonally
        """
        pass
    def FlipVertically(self) -> None:
        """
         To flip a off sheet connector vertically
        """
        pass
    def GetConnection(self) -> Tuple[ConnectionEndType, Connection]:
        """
         To get the connection connecting to the OSC sheet element.
         Returns A tuple consisting of (type, connection). 
         - type is:  ConnectionEndType NXOpen..
         - connection is:  Connection NXOpen..

        """
        pass
    def GetLocation(self) -> NXOpen.Point2d:
        """
         Gets the symbol location. 
         Returns location ( NXOpen.Point2d):  the symbol location. .
        """
        pass
    def Rotate(self) -> None:
        """
         To rotate a off sheet connector
        """
        pass
    def SetConnection(self, type: ConnectionEndType, connection: Connection) -> None:
        """
         To set the connection connecting to the OSC sheet element.
        """
        pass
    def SetDestination(self, desObject: OffSheetConnector) -> None:
        """
         Links to the destination OSC. If the input OffSheetConnector is nullptr, it means to break the existing link.  
        """
        pass
    def SetLocation(self, location: NXOpen.Point2d) -> None:
        """
         Sets the symbol location. 
        """
        pass
import NXOpen
class OffSheetConnectorCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Schematic.OffSheetConnector. """
    def FindObject(self, journalIdentifier: str) -> OffSheetConnector:
        """
         Finds the Schematic.OffSheetConnector with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         Returns osc ( OffSheetConnector NXOpen.):  Schematic.OffSheetConnector with this name. .
        """
        pass
import NXOpen
class OffSheetConnector(NXOpen.NXObject): 
    """ Represents the off sheet connector class. """
    pass
class PortDirectionOption(Enum):
    """
    Members Include: 
     |Input|  input. 
     |Output|  output. 
     |BiDirectional|  bi-directional. 

    """
    Input: int
    Output: int
    BiDirectional: int
    @staticmethod
    def ValueOf(value: int) -> PortDirectionOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class Port(NXOpen.NXObject): 
    """ Represents the schematic Port class. """
    pass
import NXOpen
import NXOpen.Diagramming
import NXOpen.Diagramming.Tables
import NXOpen.GeometricUtilities
class PreferencesAnnotationBuilder(NXOpen.TaggedObject): 
    """
    Represents a PreferencesAnnotationBuilder
    """
    @property
    def ConnectionLabelHorizontalOffsetPosition(self) -> NXOpen.Diagramming.DiagrammingConnectionlabelhorizontaloffsetposition:
        """
        Getter for property: ( NXOpen.Diagramming.DiagrammingConnectionlabelhorizontaloffsetposition) ConnectionLabelHorizontalOffsetPosition
         Returns the horizontal position of the connection tag.  
             
         
        """
        pass
    @ConnectionLabelHorizontalOffsetPosition.setter
    def ConnectionLabelHorizontalOffsetPosition(self, position: NXOpen.Diagramming.DiagrammingConnectionlabelhorizontaloffsetposition):
        """
        Setter for property: ( NXOpen.Diagramming.DiagrammingConnectionlabelhorizontaloffsetposition) ConnectionLabelHorizontalOffsetPosition
         Returns the horizontal position of the connection tag.  
             
         
        """
        pass
    @property
    def ConnectionLabelOffset(self) -> float:
        """
        Getter for property: (float) ConnectionLabelOffset
         Returns the gap between the connection and the tag.  
            
         
        """
        pass
    @ConnectionLabelOffset.setter
    def ConnectionLabelOffset(self, offset: float):
        """
        Setter for property: (float) ConnectionLabelOffset
         Returns the gap between the connection and the tag.  
            
         
        """
        pass
    @property
    def ConnectionLabelPositionCenter(self) -> bool:
        """
        Getter for property: (bool) ConnectionLabelPositionCenter
         Returns the tag is displayed at the center of the connection.  
            
         
        """
        pass
    @ConnectionLabelPositionCenter.setter
    def ConnectionLabelPositionCenter(self, center: bool):
        """
        Setter for property: (bool) ConnectionLabelPositionCenter
         Returns the tag is displayed at the center of the connection.  
            
         
        """
        pass
    @property
    def ConnectionLabelVerticalOffsetPosition(self) -> NXOpen.Diagramming.DiagrammingConnectionlabelverticaloffsetposition:
        """
        Getter for property: ( NXOpen.Diagramming.DiagrammingConnectionlabelverticaloffsetposition) ConnectionLabelVerticalOffsetPosition
         Returns the vertical position of the connection tag.  
             
         
        """
        pass
    @ConnectionLabelVerticalOffsetPosition.setter
    def ConnectionLabelVerticalOffsetPosition(self, position: NXOpen.Diagramming.DiagrammingConnectionlabelverticaloffsetposition):
        """
        Setter for property: ( NXOpen.Diagramming.DiagrammingConnectionlabelverticaloffsetposition) ConnectionLabelVerticalOffsetPosition
         Returns the vertical position of the connection tag.  
             
         
        """
        pass
    @property
    def ShowConnectionTag(self) -> bool:
        """
        Getter for property: (bool) ShowConnectionTag
         Returns    the Connection Tag Display Status.  
             
         
        """
        pass
    @ShowConnectionTag.setter
    def ShowConnectionTag(self, showConnectionTag: bool):
        """
        Setter for property: (bool) ShowConnectionTag
         Returns    the Connection Tag Display Status.  
             
         
        """
        pass
    @property
    def TablesBorderCellSettings(self) -> NXOpen.Diagramming.RenderingPropertiesBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.RenderingPropertiesBuilder) TablesBorderCellSettings
         Returns    the preferences tabular note border cell settings builder   
            
         
        """
        pass
    @property
    def TablesCellSettings(self) -> NXOpen.Diagramming.Tables.CellSettingsBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.Tables.CellSettingsBuilder) TablesCellSettings
         Returns    the preferences tabular note settings builder   
            
         
        """
        pass
    @property
    def TextStyleConnectionBuilder(self) -> NXOpen.Diagramming.TextStyleBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.TextStyleBuilder) TextStyleConnectionBuilder
         Returns the connection text style of the Annotation.  
             
         
        """
        pass
    @property
    def TextStyleNoteBuilder(self) -> NXOpen.Diagramming.TextStyleBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.TextStyleBuilder) TextStyleNoteBuilder
         Returns the note text style of the Annotation.  
             
         
        """
        pass
import NXOpen
class PreferencesBuilder(NXOpen.Builder): 
    """
    Represents a PreferencesBuilder
    """
    @property
    def Annotation(self) -> PreferencesAnnotationBuilder:
        """
        Getter for property: ( PreferencesAnnotationBuilder NXOpen.) Annotation
         Returns    the preferences annotation builder   
            
         
        """
        pass
    @property
    def Connection(self) -> PreferencesConnectionBuilder:
        """
        Getter for property: ( PreferencesConnectionBuilder NXOpen.) Connection
         Returns    the preferences connection builder   
            
         
        """
        pass
    @property
    def General(self) -> PreferencesGeneralBuilder:
        """
        Getter for property: ( PreferencesGeneralBuilder NXOpen.) General
         Returns    the preferences general builder   
            
         
        """
        pass
import NXOpen
import NXOpen.Diagramming
import NXOpen.GeometricUtilities
class PreferencesConnectionBuilder(NXOpen.TaggedObject): 
    """
    Represents a PreferencesConnectionBuilder
    """
    @property
    def AllowBreakConnections(self) -> bool:
        """
        Getter for property: (bool) AllowBreakConnections
         Returns the allow break connections.  
            
         
        """
        pass
    @AllowBreakConnections.setter
    def AllowBreakConnections(self, allowBreakConnections: bool):
        """
        Setter for property: (bool) AllowBreakConnections
         Returns the allow break connections.  
            
         
        """
        pass
    @property
    def AllowNonOrthogonalConnections(self) -> bool:
        """
        Getter for property: (bool) AllowNonOrthogonalConnections
         Returns the allow non-orthogonal connections.  
            
         
        """
        pass
    @AllowNonOrthogonalConnections.setter
    def AllowNonOrthogonalConnections(self, allowNonOrthogonal: bool):
        """
        Setter for property: (bool) AllowNonOrthogonalConnections
         Returns the allow non-orthogonal connections.  
            
         
        """
        pass
    @property
    def ArrowSize(self) -> float:
        """
        Getter for property: (float) ArrowSize
         Returns the arrow size.  
            
         
        """
        pass
    @ArrowSize.setter
    def ArrowSize(self, size: float):
        """
        Setter for property: (float) ArrowSize
         Returns the arrow size.  
            
         
        """
        pass
    @property
    def ArrowStyle(self) -> NXOpen.Diagramming.DiagrammingFlowdirectionarrowstyle:
        """
        Getter for property: ( NXOpen.Diagramming.DiagrammingFlowdirectionarrowstyle) ArrowStyle
         Returns the arrow style.  
            
         
        """
        pass
    @ArrowStyle.setter
    def ArrowStyle(self, style: NXOpen.Diagramming.DiagrammingFlowdirectionarrowstyle):
        """
        Setter for property: ( NXOpen.Diagramming.DiagrammingFlowdirectionarrowstyle) ArrowStyle
         Returns the arrow style.  
            
         
        """
        pass
    @property
    def DefaultTeeSymbolId(self) -> str:
        """
        Getter for property: (str) DefaultTeeSymbolId
         Returns the Default Junction Symbol  
            
         
        """
        pass
    @DefaultTeeSymbolId.setter
    def DefaultTeeSymbolId(self, symbolId: str):
        """
        Setter for property: (str) DefaultTeeSymbolId
         Returns the Default Junction Symbol  
            
         
        """
        pass
    @property
    def DefaultTeeSymbolIdForPDM(self) -> str:
        """
        Getter for property: (str) DefaultTeeSymbolIdForPDM
         Returns the full default Junction Symbol in the Teamcenter environment.  
          
                Schematic requires the item's name, rather than the DBNameRev information  
         
        """
        pass
    @DefaultTeeSymbolIdForPDM.setter
    def DefaultTeeSymbolIdForPDM(self, symbolId: str):
        """
        Setter for property: (str) DefaultTeeSymbolIdForPDM
         Returns the full default Junction Symbol in the Teamcenter environment.  
          
                Schematic requires the item's name, rather than the DBNameRev information  
         
        """
        pass
    @property
    def JumperGap(self) -> float:
        """
        Getter for property: (float) JumperGap
         Returns the jumper gap.  
            
         
        """
        pass
    @JumperGap.setter
    def JumperGap(self, gap: float):
        """
        Setter for property: (float) JumperGap
         Returns the jumper gap.  
            
         
        """
        pass
    @property
    def JumperPriority(self) -> NXOpen.Diagramming.DiagrammingJumperprioritytype:
        """
        Getter for property: ( NXOpen.Diagramming.DiagrammingJumperprioritytype) JumperPriority
         Returns the jumper priority type.  
             
         
        """
        pass
    @JumperPriority.setter
    def JumperPriority(self, jumperPriorityType: NXOpen.Diagramming.DiagrammingJumperprioritytype):
        """
        Setter for property: ( NXOpen.Diagramming.DiagrammingJumperprioritytype) JumperPriority
         Returns the jumper priority type.  
             
         
        """
        pass
    @property
    def JumperPriorityUseLineType(self) -> bool:
        """
        Getter for property: (bool) JumperPriorityUseLineType
         Returns the jumper priority use line type.  
            
         
        """
        pass
    @JumperPriorityUseLineType.setter
    def JumperPriorityUseLineType(self, useLineType: bool):
        """
        Setter for property: (bool) JumperPriorityUseLineType
         Returns the jumper priority use line type.  
            
         
        """
        pass
    @property
    def JumperType(self) -> NXOpen.Diagramming.DiagrammingJumpertype:
        """
        Getter for property: ( NXOpen.Diagramming.DiagrammingJumpertype) JumperType
         Returns the jumper type.  
             
         
        """
        pass
    @JumperType.setter
    def JumperType(self, jumperType: NXOpen.Diagramming.DiagrammingJumpertype):
        """
        Setter for property: ( NXOpen.Diagramming.DiagrammingJumpertype) JumperType
         Returns the jumper type.  
             
         
        """
        pass
    @property
    def MinimumSegmentLength(self) -> float:
        """
        Getter for property: (float) MinimumSegmentLength
         Returns the minimum segment length.  
            
         
        """
        pass
    @MinimumSegmentLength.setter
    def MinimumSegmentLength(self, length: float):
        """
        Setter for property: (float) MinimumSegmentLength
         Returns the minimum segment length.  
            
         
        """
        pass
    @property
    def SnapAngle(self) -> float:
        """
        Getter for property: (float) SnapAngle
         Returns the snap angle   
            
         
        """
        pass
    @SnapAngle.setter
    def SnapAngle(self, angle: float):
        """
        Setter for property: (float) SnapAngle
         Returns the snap angle   
            
         
        """
        pass
    @property
    def TeeSize(self) -> float:
        """
        Getter for property: (float) TeeSize
         Returns the tee size.  
            
         
        """
        pass
    @TeeSize.setter
    def TeeSize(self, size: float):
        """
        Setter for property: (float) TeeSize
         Returns the tee size.  
            
         
        """
        pass
    @property
    def UseDefaultTee(self) -> bool:
        """
        Getter for property: (bool) UseDefaultTee
         Returns the option for using default Junctions.  
            
         
        """
        pass
    @UseDefaultTee.setter
    def UseDefaultTee(self, useDefaultTee: bool):
        """
        Setter for property: (bool) UseDefaultTee
         Returns the option for using default Junctions.  
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class PreferencesGeneralBuilder(NXOpen.TaggedObject): 
    """
    Represents a PreferencesGeneralBuilder
    """
    @property
    def HidePorts(self) -> bool:
        """
        Getter for property: (bool) HidePorts
         Returns  the flag to hide the ports.  
             
         
        """
        pass
    @HidePorts.setter
    def HidePorts(self, hidePorts: bool):
        """
        Setter for property: (bool) HidePorts
         Returns  the flag to hide the ports.  
             
         
        """
        pass
    @property
    def ShowSymbolHandles(self) -> bool:
        """
        Getter for property: (bool) ShowSymbolHandles
         Returns  the flag to show the Symbol Handles.  
             
         
        """
        pass
    @ShowSymbolHandles.setter
    def ShowSymbolHandles(self, showSymbolHandles: bool):
        """
        Setter for property: (bool) ShowSymbolHandles
         Returns  the flag to show the Symbol Handles.  
             
         
        """
        pass
    @property
    def TagMask(self) -> str:
        """
        Getter for property: (str) TagMask
         Returns  the name of the file containing the tag mask configurations.  
             
         
        """
        pass
    @TagMask.setter
    def TagMask(self, tagMaskFile: str):
        """
        Setter for property: (str) TagMask
         Returns  the name of the file containing the tag mask configurations.  
             
         
        """
        pass
import NXOpen
import NXOpen.Diagramming.Tables
import NXOpen.GeometricUtilities
class PropertyCellRangeBuilder(NXOpen.TaggedObject): 
    """  Represents a PropertyCellRangeBuilder.  """
    @property
    def PropertyKey(self) -> str:
        """
        Getter for property: (str) PropertyKey
         Returns the property key.  
             
         
        """
        pass
    @PropertyKey.setter
    def PropertyKey(self, propertyKey: str):
        """
        Setter for property: (str) PropertyKey
         Returns the property key.  
             
         
        """
        pass
    @property
    def PropertyType(self) -> JaSchematicPropertytype:
        """
        Getter for property: ( JaSchematicPropertytype NXOpen.) PropertyType
         Returns the property type.  
             
         
        """
        pass
    @PropertyType.setter
    def PropertyType(self, propertyType: JaSchematicPropertytype):
        """
        Setter for property: ( JaSchematicPropertytype NXOpen.) PropertyType
         Returns the property type.  
             
         
        """
        pass
    @property
    def TableCellRange(self) -> NXOpen.Diagramming.Tables.CellRangeBuilder:
        """
        Getter for property: ( NXOpen.Diagramming.Tables.CellRangeBuilder) TableCellRange
         Returns the cell range.  
             
         
        """
        pass
import NXOpen
class ReplacementData(NXOpen.TransientObject): 
    """ Represents the ReplacementData class. """
    class RetainReasonType(Enum):
        """
        Members Include: 
         |NotSet|  Default value, it represents one of the two cases: 
                                                                              1. The bulk replacement operation is not skipped.
                                                                              2. The bulk replacement is skipped, but no reason is provided
         |Explicit|  The user explicitly retains the original symbolID of the object 
         |UnavailableComponents|  No candidates found for object in destination specification. Even the original symbolID does not satisfy the specification 
         |UnavailableOtherComponents|  No candidates other than current selection is found for object in destination specification.

        """
        NotSet: int
        Explicit: int
        UnavailableComponents: int
        UnavailableOtherComponents: int
        @staticmethod
        def ValueOf(value: int) -> ReplacementData.RetainReasonType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Type(Enum):
        """
        Members Include: 
         |NoChange|  Nothing to be replaced 
         |SymbolId|  Symbol ID is to be replaced 
         |PipeStock|  Pipe stock is to be replaced 

        """
        NoChange: int
        SymbolId: int
        PipeStock: int
        @staticmethod
        def ValueOf(value: int) -> ReplacementData.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def Dispose(self) -> None:
        """
         Frees resources associated with the instance.
        """
        pass
class RotateAngleOption(Enum):
    """
    Members Include: 
     |Zero|  0 degree. 
     |Ninety|  90 degree. 
     |OneHundredAndEighty|  180 degree. 
     |TwoHundredAndSeventy|  270 degree. 

    """
    Zero: int
    Ninety: int
    OneHundredAndEighty: int
    TwoHundredAndSeventy: int
    @staticmethod
    def ValueOf(value: int) -> RotateAngleOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.Diagramming
import NXOpen.Schematic.Mechanical
class SchematicManager(NXOpen.Object): 
    """ A manager to deal with all objects. """
    @property
    def Sheets() -> SheetCollection:
        """
         Returns the  NXOpen::Schematic::SheetCollection   belonging to this part 
        """
        pass
    @property
    def Nodes() -> NodeCollection:
        """
         Returns the  NXOpen::Schematic::NodeCollection   belonging to this part 
        """
        pass
    @property
    def Connections() -> ConnectionCollection:
        """
         Returns the  NXOpen::Schematic::ConnectionCollection   belonging to this part 
        """
        pass
    @property
    def Ports() -> PortCollection:
        """
         This is an internal API and can be changed at any time 
        """
        pass
    @property
    def OffSheetConnectors() -> OffSheetConnectorCollection:
        """
         Returns the  NXOpen::Schematic::OffSheetConnectorCollection   belonging to this part 
        """
        pass
    @property
    def RunsManager() -> NXOpen.Schematic.Mechanical.RunsManager:
        """
         Returns a  NXOpen::Schematic::Mechanical::RunsManager  object.
        """
        pass
    def AddConnectionToRun(self, run: NXOpen.Schematic.Mechanical.Run, connection: Connection) -> None:
        """
         Adds the connection from the unassigned folder to the run. 
        """
        pass
    def CopySchematicObjects(self, inputObjects: List[NXOpen.NXObject], isDeepCopy: bool) -> List[NXOpen.NXObject]:
        """
         Copy the Schematic objects. 
         Returns outputObjects ( NXOpen.NXObject Li):  Copies of Schematic Objects .
        """
        pass
    def CreateBulkEditBuilder(self) -> BulkEditBuilder:
        """
         Creates a NXOpen.Schematic.BulkEditBuilder 
         Returns builder ( BulkEditBuilder NXOpen.): .
        """
        pass
    def CreateBulkReplaceBuilder(self) -> BulkReplaceBuilder:
        """
         Creates a NXOpen.Schematic.BulkReplaceBuilder 
         Returns builder ( BulkReplaceBuilder NXOpen.): .
        """
        pass
    def CreateConnectionBuilder(self, connection: Connection) -> ConnectionBuilder:
        """
         Creates a NXOpen.Schematic.ConnectionBuilder. 
         Returns builder ( ConnectionBuilder NXOpen.): .
        """
        pass
    def CreateDesignValidationBuilder(self) -> DesignValidationBuilder:
        """
         Creates a NXOpen.Schematic.DesignValidationBuilder. 
         Returns builder ( DesignValidationBuilder NXOpen.): .
        """
        pass
    def CreateFdaBuilder(self, node: NXOpen.Diagramming.Node) -> FlowDirectionArrowBuilder:
        """
         Creates a NXOpen.Schematic.FlowDirectionArrowBuilder. 
         Returns builder ( FlowDirectionArrowBuilder NXOpen.): .
        """
        pass
    def CreateNodeBuilder(self, node: Node) -> NodeBuilder:
        """
         Creates a NXOpen.Schematic.NodeBuilder. 
         Returns builder ( NodeBuilder NXOpen.): .
        """
        pass
    def CreateObjectTableBuilder(self, table: ObjectTable) -> ObjectTableBuilder:
        """
         Creates a NXOpen.Schematic.ObjectTableBuilder. 
         Returns builder ( ObjectTableBuilder NXOpen.): .
        """
        pass
    def CreateOffSheetConnectorBuilder(self, oscObject: OffSheetConnector) -> OffSheetConnectorBuilder:
        """
         Creates a NXOpen.Schematic.OffSheetConnectorBuilder. 
         Returns builder ( OffSheetConnectorBuilder NXOpen.): .
        """
        pass
    def CreatePreferencesBuilder(self, sheet: Sheet) -> PreferencesBuilder:
        """
         Creates a NXOpen.Schematic.PreferencesBuilder. 
         Returns builder ( PreferencesBuilder NXOpen.): .
        """
        pass
    def CreateReplacementData(self, objectToReplace: NXOpen.NXObject, replacementType: ReplacementData.Type, replacementValue: str, retainReasonType: ReplacementData.RetainReasonType) -> ReplacementData:
        """
         Creates a Schematic.ReplacementData. 
         Returns replacementData ( ReplacementData NXOpen.): .
        """
        pass
    def CreateSheet(self) -> Sheet:
        """
         Creates a NXOpen.Schematic.Sheet. 
         Returns sheet ( Sheet NXOpen.): .
        """
        pass
    def CreateStockBuilder(self) -> StockBuilder:
        """
         Creates a NXOpen.Schematic.StockBuilder 
         Returns builder ( StockBuilder NXOpen.): .
        """
        pass
    def ExportRunNative(self, runTags: List[NXOpen.NXObject], destination: str) -> None:
        """
         Exports run 
        """
        pass
    def ExportRunNativeWithSpecificName(self, runTags: List[NXOpen.NXObject], fileNames: List[str], destination: str) -> None:
        """
         Exports run 
        """
        pass
    def MakeBranchTerminating(self, node: Node, isTerminating: bool) -> None:
        """
         Makes the inline NXOpen.Schematic.Node terminating in branch or not. 
        """
        pass
    def RemoveBranchFromRun(self, run: NXOpen.Schematic.Mechanical.Run, branch: NXOpen.Schematic.Mechanical.Branch) -> None:
        """
         Removes the branch from the run. The connections of the removed branch will be moved to unassigned folder. 
        """
        pass
    def ReparentBranch(self, sourceRun: NXOpen.Schematic.Mechanical.Run, destinationRun: NXOpen.Schematic.Mechanical.Run, oldbranch: NXOpen.Schematic.Mechanical.Branch) -> NXOpen.Schematic.Mechanical.Branch:
        """
         Moves branch from one run to another. The original branch will be destroyed. 
         Returns newbranch ( NXOpen.Schematic.Mechanical.Branch): .
        """
        pass
import NXOpen
class SheetCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Schematic.Sheet. """
    def FindObject(self, journalIdentifier: str) -> Sheet:
        """
         Finds the Schematic.Sheet with the given identifier as recorded in a journal.
                    An exception will be thrown if no object can be found with given name. 
         Returns sheet ( Sheet NXOpen.):  Schematic.Sheet with this name. .
        """
        pass
import NXOpen
class Sheet(NXOpen.NXObject): 
    """ 
        Represents Schematic Sheet class
    """
    @property
    def ObjectTables() -> ObjectTableCollection:
        """
         Returns the  NXOpen::Schematic::ObjectTableCollection   belonging to this part 
        """
        pass
import NXOpen
class StockBuilder(NXOpen.Builder): 
    """  Represents a StockBuilder.  """
    @property
    def Connections(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Connections
         Returns the connections   
            
         
        """
        pass
    @property
    def StockIdentifier(self) -> str:
        """
        Getter for property: (str) StockIdentifier
         Returns the stock of the connection.  
             
         
        """
        pass
    @StockIdentifier.setter
    def StockIdentifier(self, stockId: str):
        """
        Setter for property: (str) StockIdentifier
         Returns the stock of the connection.  
             
         
        """
        pass
    def SetStockId(self, stockId: str) -> None:
        """
         Sets the stock of the connection. 
        """
        pass
class SymbolSourceOption(Enum):
    """
    Members Include: 
     |ReuseLibrary|  from the reuse library. 
     |ExistingSymbol|  from the symbol in document window. 
     |ModelNode|  from the graph node. 

    """
    ReuseLibrary: int
    ExistingSymbol: int
    ModelNode: int
    @staticmethod
    def ValueOf(value: int) -> SymbolSourceOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.PDM
class SystemContextBuilder(NXOpen.Builder): 
    """ Represents a builder class that performs Schematic System Context operations."""
    @property
    def ConfigurationContext(self) -> NXOpen.PDM.ConfigurationContextBuilder:
        """
        Getter for property: ( NXOpen.PDM.ConfigurationContextBuilder) ConfigurationContext
         Returns the configuration context builder.  
             
         
        """
        pass
    def SetSystem(self, plmObjectFileSpec: str) -> None:
        """
         Sets the system of the SystemContextBuilder. 
        """
        pass
import NXOpen
class SystemManager(NXOpen.Object): 
    """ A manager to deal with all objects. """
    def CreateFileNewApplicationBuilder() -> FileNewApplicationBuilder:
        """
         Creates a NXOpen.Schematic.FileNewApplicationBuilder 
         Returns builder ( FileNewApplicationBuilder NXOpen.): .
        """
        pass
    def CreateSystemContextBuilder() -> SystemContextBuilder:
        """
         Creates a NXOpen.Schematic.SystemContextBuilder 
         Returns builder ( SystemContextBuilder NXOpen.): .
        """
        pass
    def SystemContextReload() -> None:
        """
         Reloads the NXOpen.Schematic.SystemContextBuilder . 
        """
        pass
